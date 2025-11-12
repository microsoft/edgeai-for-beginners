<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T22:00:56+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "tw"
}
-->
# 工作坊快速入門指南

## 先決條件

### 1. 安裝 Foundry Local

請參考官方安裝指南：  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. 安裝 Python 依賴項

在工作坊目錄中執行：

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## 執行工作坊範例

### Session 01: 基本聊天

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**環境變數：**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG 管道

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**環境變數：**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: RAG 評估 (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**注意**：需要通過 `requirements.txt` 安裝額外的依賴項

### Session 03: 基準測試

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**環境變數：**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**輸出**：包含延遲、吞吐量和首字元指標的 JSON

### Session 04: 模型比較

```bash
cd Workshop/samples
python -m session04.model_compare
```

**環境變數：**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05: 多代理協作

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**環境變數：**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06: 模型路由器

```bash
cd Workshop/samples
python -m session06.models_router
```

**測試路由邏輯**，包含多種意圖（代碼、摘要、分類）

### Session 06: 管道

```bash
python -m session06.models_pipeline
```

**複雜的多步驟管道**，包括規劃、執行和改進

## 腳本

### 匯出基準報告

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**輸出**：Markdown 表格 + JSON 指標

### Lint Markdown CLI 模式

```bash
python lint_markdown_cli.py --verbose
```

**目的**：檢測文檔中已棄用的 CLI 模式

## 測試

### 煙霧測試

```bash
cd Workshop
python -m tests.smoke
```

**測試**：關鍵範例的基本功能

## 疑難排解

### 服務未運行

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### 模組導入錯誤

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### 連接錯誤

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### 模型未找到

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## 環境變數參考

### 核心配置
| 變數 | 預設值 | 描述 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | 不同 | 使用的模型別名 |
| `FOUNDRY_LOCAL_ENDPOINT` | 自動 | 覆蓋服務端點 |
| `SHOW_USAGE` | `0` | 顯示令牌使用統計 |
| `RETRY_ON_FAIL` | `1` | 啟用重試邏輯 |
| `RETRY_BACKOFF` | `1.0` | 初始重試延遲（秒） |

### 特定會話
| 變數 | 預設值 | 描述 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 嵌入模型 |
| `RAG_QUESTION` | 見範例 | RAG 測試問題 |
| `BENCH_MODELS` | 不同 | 逗號分隔的模型 |
| `BENCH_ROUNDS` | `3` | 基準測試迭代次數 |
| `BENCH_PROMPT` | 見範例 | 基準測試提示 |
| `BENCH_STREAM` | `0` | 測量首字元延遲 |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 主代理模型 |
| `AGENT_MODEL_EDITOR` | 主代理 | 編輯代理模型 |
| `SLM_ALIAS` | `phi-4-mini` | 小型語言模型 |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型語言模型 |
| `COMPARE_PROMPT` | 見範例 | 比較提示 |

## 推薦模型

### 開發與測試
- **phi-4-mini** - 平衡質量與速度
- **qwen2.5-0.5b** - 分類速度非常快
- **gemma-2-2b** - 質量良好，速度適中

### 生產場景
- **phi-4-mini** - 通用用途
- **deepseek-coder-1.3b** - 代碼生成
- **qwen2.5-7b** - 高質量回應

## SDK 文檔

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## 獲取幫助

1. 檢查服務狀態：`foundry service status`  
2. 查看日誌：檢查 Foundry Local 服務日誌  
3. 查看 SDK 文檔：https://github.com/microsoft/Foundry-Local  
4. 查看範例代碼：所有範例均包含詳細的文檔字符串  

## 下一步

1. 按順序完成所有工作坊會話  
2. 嘗試不同的模型  
3. 修改範例以適應您的使用場景  

---

**最後更新日期**：2025-01-08  
**工作坊版本**：最新  
**SDK**：Foundry Local Python SDK  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->