<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:57:03+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "hk"
}
-->
# 第四節：探索尖端模型 – LLMs、SLMs 和設備端推理

## 摘要

比較大型語言模型（LLMs）和小型語言模型（SLMs）在本地與雲端推理場景中的表現。學習如何利用 ONNX Runtime 加速、WebGPU 執行以及混合 RAG 體驗進行部署。包括使用本地模型的 Chainlit RAG 演示以及可選的 OpenWebUI 探索。您將調整 WebGPU 推理入門範例，並評估 Phi 與 GPT-OSS-20B 的能力及成本/性能權衡。

## 學習目標

- **對比** SLM 與 LLM 在延遲、記憶體和質量方面的表現
- **部署** 使用 ONNXRuntime 和（支持的情況下）WebGPU 的模型
- **運行** 基於瀏覽器的推理（保護隱私的互動演示）
- **整合** 使用本地 SLM 後端的 Chainlit RAG 管道
- **評估** 使用輕量化的質量和成本準則

## 先決條件

- 完成第一至第三節
- 已安裝 `chainlit`（已包含在 Module08 的 `requirements.txt` 中）
- 支持 WebGPU 的瀏覽器（Windows 11 上最新版本的 Edge / Chrome）
- Foundry Local 正在運行（`foundry service status`）

### 跨平台注意事項

Windows 仍然是主要目標環境。對於等待原生二進制文件的 macOS 開發者：
1. 在 Windows 11 虛擬機（Parallels / UTM）或遠程 Windows 工作站中運行 Foundry Local。
2. 將服務暴露（默認端口 5273），並在 macOS 上設置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. 使用與之前課程相同的 Python 虛擬環境步驟。

Chainlit 安裝（兩個平台均適用）：
```bash
pip install chainlit
```

## 演示流程（30 分鐘）

### 1. 比較 Phi（SLM）與 GPT-OSS-20B（LLM）（6 分鐘）

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

追蹤：響應深度、事實準確性、風格豐富性、延遲。

觀察啟用 GPU 與僅使用 CPU 時的吞吐量變化。

### 3. 瀏覽器中的 WebGPU 推理（6 分鐘）

調整入門範例 `04-webgpu-inference`（創建 `samples/04-cutting-edge/webgpu_demo.html`）：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

在瀏覽器中打開文件；觀察低延遲的本地回傳。

### 4. Chainlit RAG 聊天應用（7 分鐘）

簡化版 `samples/04-cutting-edge/chainlit_app.py`：

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

運行：

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. 入門項目：調整 `04-webgpu-inference`（6 分鐘）

交付成果：
- 替換佔位符抓取邏輯為流式令牌（啟用後使用 `stream=True` 端點變體）
- 添加延遲圖表（客戶端）以切換 phi 與 gpt-oss-20b
- 嵌入 RAG 上下文（參考文檔的文本框）

## 評估準則

| 類別 | Phi-4-mini | GPT-OSS-20B | 觀察 |
|------|------------|-------------|------|
| 延遲（冷啟動） | 快速 | 較慢 | SLM 啟動速度快 |
| 記憶體 | 低 | 高 | 設備可行性 |
| 上下文遵循 | 良好 | 強 | 大型模型可能更冗長 |
| 成本（本地） | 最低 | 較高（資源） | 能源/時間權衡 |
| 最佳使用場景 | 邊緣應用 | 深度推理 | 可實現混合管道 |

## 驗證環境

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## 故障排除

| 症狀 | 原因 | 措施 |
|------|------|------|
| 網頁抓取失敗 | CORS 或服務中斷 | 使用 `curl` 驗證端點；如有需要啟用 CORS 代理 |
| Chainlit 空白 | 環境未激活 | 激活 venv 並重新安裝依賴 |
| 高延遲 | 模型剛加載 | 使用小提示序列進行預熱 |

## 參考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit 文檔: https://docs.chainlit.io
- RAG 評估（Ragas）: https://docs.ragas.io

---

**課程時長**: 30 分鐘  
**難度**: 高級

## 示例場景與工作坊映射

| 工作坊產物 | 場景 | 目標 | 數據/提示來源 |
|------------|------|------|--------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | 架構團隊評估 SLM 與 LLM 用於高管摘要生成 | 量化延遲與令牌使用差異 | 單一 `COMPARE_PROMPT` 環境變量 |
| `chainlit_app.py`（RAG 演示） | 內部知識助手原型 | 使用最少的詞彙檢索生成簡短答案 | 文件中的內嵌 `DOCS` 列表 |
| `webgpu_demo.html` | 未來設備端瀏覽器推理預覽 | 展示低延遲的本地回傳與用戶體驗敘述 | 僅限即時用戶提示 |

### 場景敘述
產品部門希望有一個高管簡報生成器。一個輕量化的 SLM（phi-4-mini）草擬摘要；一個更大的 LLM（gpt-oss-20b）可能僅用於精煉高優先級報告。課程腳本捕捉了實際延遲和令牌指標，以證明混合設計的合理性，而 Chainlit 演示則展示了如何通過基於事實的檢索保持小型模型答案的準確性。WebGPU 概念頁提供了一個完全客戶端處理的未來路徑，當瀏覽器加速成熟時。

### 最小 RAG 上下文（Chainlit）
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### 混合草擬→精煉流程（偽代碼）
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

追蹤兩個延遲組件以報告混合平均成本。

### 可選增強功能

| 重點 | 增強 | 原因 | 實施提示 |
|------|------|------|---------|
| 比較指標 | 追蹤令牌使用與首令牌延遲 | 全面性能視圖 | 使用增強的基準腳本（第三節）並設置 `BENCH_STREAM=1` |
| 混合管道 | SLM 草擬 → LLM 精煉 | 降低延遲與成本 | 使用 phi-4-mini 生成，使用 gpt-oss-20b 精煉摘要 |
| 流式 UI | Chainlit 中更好的用戶體驗 | 增量反饋 | 一旦本地流式推理啟用，使用 `stream=True`；累積塊 |
| WebGPU 緩存 | 更快的 JS 初始化 | 降低重新編譯開銷 | 緩存編譯的著色器工件（未來運行時功能） |
| 確定性 QA 集 | 公平的模型比較 | 消除變異性 | 固定提示列表並設置 `temperature=0` 進行評估運行 |
| 輸出評分 | 結構化質量視角 | 超越軼事 | 簡單的評分標準：連貫性/事實性/簡潔性（1–5） |
| 能源/資源筆記 | 課堂討論 | 展示權衡 | 使用操作系統監控（任務管理器，`nvidia-smi`）+ 基準腳本輸出 |
| 成本模擬 | 雲端前的論證 | 計劃擴展 | 將令牌映射到假設的雲端定價以構建 TCO 敘述 |
| 延遲分解 | 識別瓶頸 | 針對優化 | 測量提示準備、請求發送、首令牌、完整完成 |
| RAG + LLM 回退 | 質量安全網 | 改善困難查詢 | 如果 SLM 答案長度低於閾值或信心低 → 升級 |

#### 示例混合草擬/精煉模式

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### 延遲分解草圖

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

在模型間使用一致的測量框架以進行公平比較。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->