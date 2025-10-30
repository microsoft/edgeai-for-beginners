<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:45:23+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "hk"
}
-->
# 工作坊範例 - 快速參考卡

**最後更新**：2025年10月8日

---

## 🚀 快速開始

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 範例概覽

| 課程 | 範例 | 目的 | 時間 |
|------|------|------|------|
| 01 | `chat_bootstrap.py` | 基本聊天 + 串流 | ~30秒 |
| 02 | `rag_pipeline.py` | RAG與嵌入 | ~45秒 |
| 02 | `rag_eval_ragas.py` | RAG評估 | ~60秒 |
| 03 | `benchmark_oss_models.py` | 模型基準測試 | ~2分鐘 |
| 04 | `model_compare.py` | SLM vs LLM | ~45秒 |
| 05 | `agents_orchestrator.py` | 多代理系統 | ~60秒 |
| 06 | `models_router.py` | 意圖路由 | ~45秒 |
| 06 | `models_pipeline.py` | 多步驟管道 | ~60秒 |

---

## 🛠️ 環境變數

### 必需
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### 特定課程
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ 驗證與測試

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 疑難排解

### 連接錯誤
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### 匯入錯誤
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### 模型未找到
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### 性能緩慢
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 常見模式

### 基本聊天
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### 獲取客戶端
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### 錯誤處理
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 串流
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 模型選擇

| 模型 | 大小 | 最適用途 | 速度 |
|------|------|----------|------|
| `qwen2.5-0.5b` | 0.5B | 快速分類 | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | 快速代碼生成 | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | 創意寫作 | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | 代碼、重構 | ⚡⚡ |
| `phi-4-mini` | 4B | 通用、摘要 | ⚡⚡ |
| `qwen2.5-7b` | 7B | 複雜推理 | ⚡ |

---

## 🔗 資源

- **SDK文件**：https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **快速參考**：`Workshop/FOUNDRY_SDK_QUICKREF.md`
- **更新摘要**：`Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **遷移說明**：`Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 提示

1. **緩存客戶端**：`workshop_utils` 為您緩存
2. **使用較小的模型**：測試時先使用 `qwen2.5-0.5b`
3. **啟用使用統計**：設置 `SHOW_USAGE=1` 以追蹤 token 使用情況
4. **批量處理**：依次處理多個提示
5. **降低 max_tokens**：減少延遲以獲得快速回應

---

## 🎯 範例工作流程

### 測試所有內容
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### 基準測試模型
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG管道
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### 多代理系統
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**快速幫助**：在 `samples` 目錄中使用 `--help` 運行任何範例或查看文檔字符串：
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**所有範例已於2025年10月更新，符合Foundry Local SDK最佳實踐** ✨

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。