<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T20:42:06+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "hk"
}
-->
# 第四節：探索尖端模型——LLMs、SLMs及設備端推理

## 摘要

比較大型語言模型（LLMs）與小型語言模型（SLMs）在本地與雲端推理場景中的表現。學習利用ONNX Runtime加速、WebGPU執行及混合RAG體驗的部署模式。包括使用本地模型的Chainlit RAG演示，以及可選的OpenWebUI探索。您將調整WebGPU推理入門範例，並評估Phi與GPT-OSS-20B的能力及成本/性能取捨。

## 學習目標

- **對比** SLM與LLM在延遲、記憶體及質量方面的表現
- **部署** 使用ONNXRuntime及（支持的情況下）WebGPU的模型
- **運行** 基於瀏覽器的推理（保護隱私的交互式演示）
- **整合** 使用本地SLM後端的Chainlit RAG管道
- **評估** 使用輕量化的質量及成本啟發式方法

## 先決條件

- 完成第一至第三節
- 已安裝`chainlit`（已包含在Module08的`requirements.txt`中）
- 支持WebGPU的瀏覽器（Windows 11上的最新版本Edge/Chrome）
- Foundry Local正在運行（`foundry status`）

### 跨平台注意事項

Windows仍然是主要目標環境。對於等待原生二進制文件的macOS開發者：
1. 在Windows 11虛擬機（Parallels / UTM）或遠程Windows工作站中運行Foundry Local。
2. 將服務暴露（默認端口5273），並在macOS上設置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. 使用與之前課程相同的Python虛擬環境步驟。

Chainlit安裝（兩個平台均適用）：
```bash
pip install chainlit
```

## 演示流程（30分鐘）

### 1. 比較Phi（SLM）與GPT-OSS-20B（LLM）（6分鐘）

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

### 2. ONNX Runtime加速（5分鐘）

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

觀察啟用GPU與僅使用CPU後的吞吐量變化。

### 3. 瀏覽器中的WebGPU推理（6分鐘）

調整入門範例`04-webgpu-inference`（創建`samples/04-cutting-edge/webgpu_demo.html`）：

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

### 4. Chainlit RAG聊天應用（7分鐘）

最小化的`samples/04-cutting-edge/chainlit_app.py`：

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

### 5. 入門項目：調整`04-webgpu-inference`（6分鐘）

交付物：
- 用流式令牌替換佔位符提取邏輯（啟用`stream=True`端點變體後使用）
- 添加延遲圖表（客戶端）以切換phi與gpt-oss-20b
- 嵌入RAG上下文（用於參考文檔的文本框）

## 評估啟發式方法

| 類別 | Phi-4-mini | GPT-OSS-20B | 觀察 |
|------|------------|-------------|------|
| 延遲（冷啟動） | 快速 | 較慢 | SLM啟動速度快 |
| 記憶體 | 低 | 高 | 設備可行性 |
| 上下文遵守 | 良好 | 強 | 較大的模型可能更詳細 |
| 成本（本地） | 最低 | 較高（資源） | 能源/時間取捨 |
| 最佳使用場景 | 邊緣應用 | 深度推理 | 可行的混合管道 |

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

## 疑難排解

| 症狀 | 原因 | 措施 |
|------|------|------|
| 網頁提取失敗 | CORS或服務中斷 | 使用`curl`驗證端點；如有需要啟用CORS代理 |
| Chainlit空白 | 環境未激活 | 激活虛擬環境並重新安裝依賴 |
| 高延遲 | 模型剛加載 | 使用小提示序列進行預熱 |

## 參考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit文檔: https://docs.chainlit.io
- RAG評估（Ragas）: https://docs.ragas.io

---

**課程時長**: 30分鐘  
**難度**: 高級

## 示例場景及工作坊映射

| 工作坊產物 | 場景 | 目標 | 數據/提示來源 |
|------------|------|------|---------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | 架構團隊評估SLM與LLM用於高層摘要生成 | 量化延遲及令牌使用差異 | 單一`COMPARE_PROMPT`環境變量 |
| `chainlit_app.py`（RAG演示） | 內部知識助手原型 | 用最少的詞彙檢索支持簡短回答 | 文件中的內嵌`DOCS`列表 |
| `webgpu_demo.html` | 未來設備端瀏覽器推理預覽 | 展示低延遲本地回傳及用戶體驗敘述 | 僅限即時用戶提示 |

### 場景敘述
產品部門希望開發一個高層簡報生成器。一個輕量化的SLM（phi‑4‑mini）負責草擬摘要；較大的LLM（gpt‑oss‑20b）僅精煉高優先級報告。課程腳本捕捉了實際延遲及令牌指標以證明混合設計的合理性，而Chainlit演示則展示了如何通過基於事實的檢索保持小型模型回答的準確性。WebGPU概念頁提供了瀏覽器加速成熟後完全客戶端處理的願景路徑。

### 最小RAG上下文（Chainlit）
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

| 重點 | 增強功能 | 原因 | 實施提示 |
|------|----------|------|----------|
| 比較指標 | 追蹤令牌使用及首令牌延遲 | 全面性能視圖 | 使用增強的基準腳本（第三節）及`BENCH_STREAM=1` |
| 混合管道 | SLM草擬→LLM精煉 | 降低延遲及成本 | 使用phi-4-mini生成，使用gpt-oss-20b精煉摘要 |
| 流式UI | Chainlit中的更佳用戶體驗 | 增量反饋 | 一旦本地流式功能開放，使用`stream=True`；累積塊 |
| WebGPU緩存 | 更快的JS初始化 | 降低重編譯開銷 | 緩存編譯的著色器工件（未來運行時功能） |
| 確定性QA集 | 公平的模型比較 | 消除變異性 | 固定提示列表及評估運行的`temperature=0` |
| 輸出評分 | 結構化質量視角 | 超越軼事 | 簡單的評分標準：連貫性/事實性/簡潔性（1–5分） |
| 能源/資源註釋 | 課堂討論 | 展示取捨 | 使用操作系統監控（`foundry system info`，任務管理器，`nvidia-smi`）及基準腳本輸出 |
| 成本模擬 | 雲端前的論證 | 計劃擴展 | 將令牌映射到假設的雲端定價以進行總擁有成本敘述 |
| 延遲分解 | 識別瓶頸 | 目標優化 | 測量提示準備、請求發送、首令牌、完整完成 |
| RAG + LLM後備 | 質量安全網 | 改善困難查詢 | 如果SLM回答長度低於閾值或信心低→升級 |

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

使用一致的測量框架跨模型進行公平比較。

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。