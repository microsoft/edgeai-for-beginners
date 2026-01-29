# 環境配置指南

## 概述

Workshop 範例使用環境變數進行配置，集中於存放在倉庫根目錄的 `.env` 文件中。這使得用戶可以輕鬆自定義配置，而無需修改程式碼。

## 快速開始

### 1. 驗證先決條件

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. 配置環境

`.env` 文件已預設配置了合理的默認值。大多數用戶無需進行更改。

**可選**：檢查並自定義設置：
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. 應用配置

**針對 Python 腳本：**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**針對 Notebook：**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## 環境變數參考

### 核心配置

| 變數 | 默認值 | 描述 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | 範例的默認模型 |
| `FOUNDRY_LOCAL_ENDPOINT` | (空) | 覆蓋服務端點 |
| `PYTHONPATH` | Workshop 路徑 | Python 模組搜索路徑 |

**何時設置 FOUNDRY_LOCAL_ENDPOINT：**
- 遠端 Foundry Local 實例
- 自定義端口配置
- 區分開發/生產環境

**範例：**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### 特定會話變數

#### 會話 02：RAG 管道
| 變數 | 默認值 | 用途 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 嵌入模型 |
| `RAG_QUESTION` | 預設配置 | 測試問題 |

#### 會話 03：基準測試
| 變數 | 默認值 | 用途 |
|------|--------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | 要進行基準測試的模型 |
| `BENCH_ROUNDS` | `3` | 每個模型的迭代次數 |
| `BENCH_PROMPT` | 預設配置 | 測試提示 |
| `BENCH_STREAM` | `0` | 測量首個 token 的延遲 |

#### 會話 04：模型比較
| 變數 | 默認值 | 用途 |
|------|--------|------|
| `SLM_ALIAS` | `phi-4-mini` | 小型語言模型 |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型語言模型 |
| `COMPARE_PROMPT` | 預設配置 | 比較提示 |
| `COMPARE_RETRIES` | `2` | 重試次數 |

#### 會話 05：多代理協作
| 變數 | 默認值 | 用途 |
|------|--------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 研究員代理模型 |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | 編輯代理模型 |
| `AGENT_QUESTION` | 預設配置 | 測試問題 |

### 可靠性配置

| 變數 | 默認值 | 用途 |
|------|--------|------|
| `SHOW_USAGE` | `1` | 顯示 token 使用情況 |
| `RETRY_ON_FAIL` | `1` | 啟用重試邏輯 |
| `RETRY_BACKOFF` | `1.0` | 重試延遲（秒） |

## 常見配置

### 開發設置（快速迭代）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### 生產設置（質量優先）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### 基準測試設置
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### 多代理專業化
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### 遠端開發
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## 推薦模型

### 根據使用場景

**通用用途：**
- `phi-4-mini` - 平衡質量與速度

**快速響應：**
- `qwen2.5-0.5b` - 非常快，適合分類
- `phi-4-mini` - 快速且質量良好

**高質量：**
- `qwen2.5-7b` - 最佳質量，資源使用較高
- `phi-4-mini` - 質量良好，資源需求較低

**代碼生成：**
- `deepseek-coder-1.3b` - 專為代碼設計
- `phi-4-mini` - 通用代碼用途

### 根據資源可用性

**低資源（< 8GB RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**中等資源（8-16GB RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**高資源（16GB+ RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## 高級配置

### 自定義端點

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### 溫度與採樣（在代碼中覆蓋）

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI 混合設置

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 疑難排解

### 環境變數未加載

**症狀：**
- 腳本使用錯誤的模型
- 連接錯誤
- 無法識別變數

**解決方案：**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### 服務連接問題

**症狀：**
- "Connection refused" 錯誤
- "Service not available"
- 超時錯誤

**解決方案：**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### 模型未找到

**症狀：**
- "Model not found" 錯誤
- "Alias not recognized"

**解決方案：**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### 導入錯誤

**症狀：**
- "Module not found" 錯誤

**解決方案：**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## 測試配置

### 驗證環境加載

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### 測試 Foundry Local 連接

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## 安全最佳實踐

### 1. 切勿提交機密信息

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. 使用單獨的 .env 文件

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. 定期更換 API 密鑰

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. 使用特定環境配置

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK 文件

- **主倉庫**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API 文件**: 請檢查 SDK 倉庫以獲取最新版本

## 其他資源

- `QUICK_START.md` - 快速入門指南
- `Workshop/samples/*/README.md` - 範例特定指南

---

**最後更新日期**: 2025-01-08  
**版本**: 2.0  
**SDK**: Foundry Local Python SDK (最新)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->