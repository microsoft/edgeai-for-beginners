# 範例 01：使用 OpenAI SDK 快速聊天

一個簡單的聊天範例，展示如何使用 OpenAI SDK 與 Microsoft Foundry Local 進行本地 AI 推理。

## 概述

此範例展示如何：
- 使用 OpenAI Python SDK 與 Foundry Local
- 處理 Azure OpenAI 和本地 Foundry 的配置
- 實現正確的錯誤處理和備援策略
- 使用 FoundryLocalManager 進行服務管理

## 先決條件

- **Foundry Local**：已安裝並可在 PATH 中使用
- **Python**：版本 3.8 或以上
- **模型**：已在 Foundry Local 中載入的模型（例如 `phi-4-mini`）

## 安裝

1. **設置 Python 環境：**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **安裝依賴項：**
   ```cmd
   pip install -r requirements.txt
   ```

3. **啟動 Foundry Local 服務並載入模型：**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用方法

### Foundry Local（預設）

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## 程式特性

### FoundryLocalManager 整合

此範例使用官方 Foundry Local SDK 進行正確的服務管理：

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### 錯誤處理

強大的錯誤處理機制，包含手動配置的備援：
- 自動服務發現
- 如果 SDK 不可用，能夠平穩降級
- 提供清晰的錯誤訊息以便排查問題

## 環境變數

| 變數 | 描述 | 預設值 | 必需 |
|------|------|--------|------|
| `MODEL` | 模型別名或名稱 | `phi-4-mini` | 否 |
| `BASE_URL` | Foundry Local 基本 URL | `http://localhost:8000` | 否 |
| `API_KEY` | API 金鑰（通常本地不需要） | `""` | 否 |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI 端點 | - | 用於 Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API 金鑰 | - | 用於 Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API 版本 | `2024-08-01-preview` | 否 |

## 疑難排解

### 常見問題

1. **「無法使用 Foundry SDK」警告：**
   - 安裝 foundry-local-sdk：`pip install foundry-local-sdk`
   - 或設置環境變數進行手動配置

2. **連線被拒絕：**
   - 確保 Foundry Local 正在運行：`foundry service status`
   - 檢查是否已載入模型：`foundry service ps`

3. **找不到模型：**
   - 列出可用模型：`foundry model list`
   - 載入模型：`foundry model run phi-4-mini`

### 驗證

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## 參考資料

- [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI 兼容 API 參考](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

