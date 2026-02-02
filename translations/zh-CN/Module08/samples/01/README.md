# 示例 01：通过 OpenAI SDK 快速聊天

一个简单的聊天示例，展示如何使用 OpenAI SDK 与 Microsoft Foundry Local 进行本地 AI 推理。

## 概述

此示例展示了如何：
- 使用 OpenAI Python SDK 与 Foundry Local
- 处理 Azure OpenAI 和本地 Foundry 配置
- 实现正确的错误处理和回退策略
- 使用 FoundryLocalManager 进行服务管理

## 前提条件

- **Foundry Local**：已安装并可通过 PATH 访问
- **Python**：3.8 或更高版本
- **模型**：在 Foundry Local 中加载的模型（例如，`phi-4-mini`）

## 安装

1. **设置 Python 环境：**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **安装依赖项：**
   ```cmd
   pip install -r requirements.txt
   ```

3. **启动 Foundry Local 服务并加载模型：**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用方法

### Foundry Local（默认）

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


## 代码功能

### FoundryLocalManager 集成

此示例使用官方 Foundry Local SDK 进行服务管理：

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


### 错误处理

通过回退到手动配置实现稳健的错误处理：
- 自动服务发现
- 如果 SDK 不可用则优雅降级
- 提供清晰的错误信息以便排查问题

## 环境变量

| 变量 | 描述 | 默认值 | 是否必需 |
|------|------|--------|----------|
| `MODEL` | 模型别名或名称 | `phi-4-mini` | 否 |
| `BASE_URL` | Foundry Local 基础 URL | `http://localhost:8000` | 否 |
| `API_KEY` | API 密钥（通常本地不需要） | `""` | 否 |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI 端点 | - | 用于 Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API 密钥 | - | 用于 Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API 版本 | `2024-08-01-preview` | 否 |

## 故障排除

### 常见问题

1. **“无法使用 Foundry SDK”警告：**
   - 安装 foundry-local-sdk：`pip install foundry-local-sdk`
   - 或设置环境变量以进行手动配置

2. **连接被拒绝：**
   - 确保 Foundry Local 正在运行：`foundry service status`
   - 检查是否已加载模型：`foundry service ps`

3. **模型未找到：**
   - 列出可用模型：`foundry model list`
   - 加载模型：`foundry model run phi-4-mini`

### 验证

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## 参考资料

- [Foundry Local 文档](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI 兼容 API 参考](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

