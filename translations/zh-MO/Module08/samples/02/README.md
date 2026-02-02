# 範例 02：OpenAI SDK 整合

展示如何進階整合 OpenAI Python SDK，支援 Microsoft Foundry Local 和 Azure OpenAI，包含串流回應及完善的錯誤處理。

## 概述

此範例展示：
- 在 Foundry Local 和 Azure OpenAI 之間無縫切換
- 串流聊天完成，提升使用者體驗
- 正確使用 FoundryLocalManager SDK
- 強大的錯誤處理及備援機制
- 適合生產環境的程式碼模式

## 先決條件

- **Foundry Local**：已安裝並運行（用於本地推理）
- **Python**：3.8 或更新版本，並安裝 OpenAI SDK
- **Azure OpenAI**：有效的端點及 API 金鑰（用於雲端推理）

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

3. **啟動 Foundry Local（本地模式）：**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用場景

### Foundry Local（預設）

**選項 1：使用 FoundryLocalManager（推薦）**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**選項 2：手動配置**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## 程式架構

### 客戶端工廠模式

此範例使用工廠模式來創建適合的客戶端：

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### 串流回應

此範例展示如何進行串流以生成即時回應：

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## 環境變數

### Foundry Local 配置

| 變數         | 描述                     | 預設值          | 必需 |
|--------------|--------------------------|-----------------|------|
| `MODEL`      | 使用的模型別名           | `phi-4-mini`    | 否   |
| `BASE_URL`   | Foundry Local 端點       | `http://localhost:8000` | 否   |
| `API_KEY`    | API 金鑰（本地可選）     | `""`            | 否   |

### Azure OpenAI 配置

| 變數                   | 描述                     | 預設值          | 必需 |
|------------------------|--------------------------|-----------------|------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI 資源端點    | -               | 是   |
| `AZURE_OPENAI_API_KEY`  | Azure OpenAI API 金鑰    | -               | 是   |
| `AZURE_OPENAI_API_VERSION` | API 版本              | `2024-08-01-preview` | 否   |
| `MODEL`                | Azure 部署名稱           | `your-deployment-name` | 是   |

## 高級功能

### 自動服務檢測

此範例根據環境變數自動檢測適合的服務：

1. **Azure 模式**：若設置了 `AZURE_OPENAI_ENDPOINT` 和 `AZURE_OPENAI_API_KEY`
2. **Foundry SDK 模式**：若 Foundry Local SDK 可用
3. **手動模式**：回退至手動配置

### 錯誤處理

- 從 SDK 回退至手動配置的平滑過渡
- 清晰的錯誤訊息以便排查問題
- 網絡問題的正確異常處理
- 必需環境變數的驗證

## 性能考量

### 本地與雲端的取捨

**Foundry Local 優勢：**
- ✅ 無 API 成本
- ✅ 資料隱私（資料不離開設備）
- ✅ 支援模型的低延遲
- ✅ 可離線運行

**Azure OpenAI 優勢：**
- ✅ 可使用最新的大型模型
- ✅ 更高的吞吐量
- ✅ 無需本地計算資源
- ✅ 企業級 SLA

## 疑難排解

### 常見問題

1. **"無法使用 Foundry SDK" 警告：**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure 認證錯誤：**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **模型不可用：**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### 健康檢查

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## 下一步

- **範例 03**：模型檢測及效能測試
- **範例 04**：構建 Chainlit RAG 應用
- **範例 05**：多代理協作
- **範例 06**：模型作為工具的路由

## 參考資料

- [Azure OpenAI 文件](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK 參考](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK 文件](https://github.com/openai/openai-python)
- [串流完成指南](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

