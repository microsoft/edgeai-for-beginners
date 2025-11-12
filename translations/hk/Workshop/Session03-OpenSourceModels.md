<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T22:00:08+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "hk"
}
-->
# 第三節：Foundry Local 中的開源模型

## 摘要

探索如何將 Hugging Face 和其他開源模型引入 Foundry Local。學習模型選擇策略、社群貢獻工作流程、性能比較方法，以及如何透過自定義模型註冊擴展 Foundry。本節課程與每週的「模型星期一」探索主題相呼應，幫助您在擴展到 Azure 之前，先在本地評估並運行開源模型。

## 學習目標

完成後，您將能夠：

- **探索與評估**：根據品質與資源權衡，識別候選模型（mistral、gemma、qwen、deepseek）。
- **載入與運行**：使用 Foundry Local CLI 下載、緩存並啟動社群模型。
- **基準測試**：應用一致的延遲 + token 吞吐量 + 品質指標。
- **擴展**：按照 SDK 兼容模式註冊或調整自定義模型包裝器。
- **比較**：生成結構化比較，用於 SLM 與中型 LLM 的選擇決策。

## 先決條件

- 完成第一節與第二節
- 安裝了 `foundry-local-sdk` 的 Python 環境
- 至少 15GB 的磁碟空間，用於多個模型緩存

### 跨平台環境快速啟動

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

在 macOS 上對 Windows 主機服務進行基準測試時，設置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 演示流程（30 分鐘）

### 1. 通過 CLI 載入 Hugging Face 模型（8 分鐘）

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. 運行與快速探測（5 分鐘）

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. 基準測試腳本（8 分鐘）

創建 `samples/03-oss-models/benchmark_models.py`：

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```


運行：

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. 比較性能（5 分鐘）

討論權衡：載入時間、記憶體佔用（觀察任務管理器 / `nvidia-smi` / 操作系統資源監視器）、輸出品質與速度。使用 Python 基準測試腳本（第三節）進行延遲與吞吐量測試；啟用 GPU 加速後重複測試。

### 5. 初始項目（4 分鐘）

創建模型比較報告生成器（擴展基準測試腳本，支持 Markdown 輸出）。

## 初始項目：擴展 `03-huggingface-models`

增強現有範例：

1. 添加基準測試聚合 + CSV/Markdown 輸出。
2. 實現簡單的定性評分（提示對集 + 手動註解樣本文件）。
3. 引入 JSON 配置文件（`models.json`），支持可插拔的模型列表與提示集。

## 驗證清單

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

所有目標模型應出現並響應探測聊天請求。

## 範例場景與工作坊映射

| 工作坊腳本 | 場景 | 目標 | 提示 / 數據集來源 |
|------------|------|------|------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | 邊緣平台團隊選擇嵌入式摘要器的默認 SLM | 生成候選模型的延遲 + p95 + token/sec 比較 | 內嵌 `PROMPT` 變數 + 環境 `BENCH_MODELS` 列表 |

### 場景敘述
產品工程團隊需要選擇一個默認的輕量化摘要模型，用於離線會議記錄功能。他們在固定的提示集上運行受控的確定性基準測試（temperature=0），並收集有無 GPU 加速的延遲與吞吐量指標。

### 範例提示集 JSON（可擴展）
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

對每個模型循環每個提示，捕獲每個提示的延遲以推導分佈指標並檢測異常值。

## 模型選擇框架

| 維度 | 指標 | 為何重要 |
|------|------|---------|
| 延遲 | 平均 / p95 | 用戶體驗一致性 |
| 吞吐量 | token/sec | 批量與流式擴展性 |
| 記憶體 | 常駐大小 | 設備適配與並發性 |
| 品質 | 評分提示 | 任務適用性 |
| 占用 | 磁碟緩存 | 分發與更新 |
| 授權 | 使用許可 | 商業合規性 |

## 使用自定義模型進行擴展

高層次模式（偽代碼）：

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

請參考官方倉庫以了解不斷演進的適配器介面：
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## 疑難排解

| 問題 | 原因 | 解決方法 |
|------|------|---------|
| mistral-7b 出現 OOM | RAM/GPU 不足 | 停止其他模型；嘗試較小的變體 |
| 首次響應速度慢 | 冷載入 | 使用定期輕量提示保持熱啟動 |
| 下載卡住 | 網絡不穩定 | 重試；在非高峰期預取 |

## 參考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- 模型星期一: https://aka.ms/model-mondays
- Hugging Face 模型探索: https://huggingface.co/models

---

**課程時長**：30 分鐘（+ 可選深入探討）  
**難度**：中級

### 可選增強功能

| 增強功能 | 好處 | 方法 |
|----------|------|-----|
| 流式首 token 延遲 | 測量感知響應性 | 使用 `BENCH_STREAM=1` 運行基準測試（增強腳本位於 `Workshop/samples/session03`） |
| 確定性模式 | 穩定的回歸比較 | `temperature=0`，固定提示集，捕獲 JSON 輸出並進行版本控制 |
| 品質評分標準 | 增加定性維度 | 維護 `prompts.json`，包含預期特徵；手動或通過次級模型註解分數（1–5） |
| CSV / Markdown 輸出 | 可分享的報告 | 擴展腳本以生成 `benchmark_report.md`，包含表格與亮點 |
| 模型能力標籤 | 有助於後續自動路由 | 維護 `models.json`，包含 `{alias: {capabilities:[], size_mb:..}}` |
| 緩存預熱階段 | 減少冷啟動偏差 | 在計時循環之前執行一次預熱（已實現） |
| 百分位準確性 | 強健的尾部延遲 | 使用 numpy 百分位（已在重構腳本中） |
| token 成本估算 | 經濟比較 | 估算成本 = (token/sec * 每次請求的平均 token 數) * 能耗估算 |
| 自動跳過失敗模型 | 批量運行的韌性 | 將每個基準測試包裹在 try/except 中，並標記狀態字段 |

#### 最小 Markdown 輸出片段

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### 確定性提示集範例

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

循環靜態列表，而非隨機提示，以便在不同提交間獲得可比較的指標。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->