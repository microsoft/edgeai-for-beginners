# 示例 02：OpenAI SDK 集成

展示与 OpenAI Python SDK 的高级集成，支持 Microsoft Foundry Local 和 Azure OpenAI，包含流式响应和完善的错误处理。

## 概述

此示例展示：
- 在 Foundry Local 和 Azure OpenAI 之间的无缝切换
- 流式聊天完成以提升用户体验
- 正确使用 FoundryLocalManager SDK
- 强大的错误处理和回退机制
- 适用于生产环境的代码模式

## 前提条件

- **Foundry Local**：已安装并运行（用于本地推理）
- **Python**：3.8 或更高版本，安装了 OpenAI SDK
- **Azure OpenAI**：有效的端点和 API 密钥（用于云推理）

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

3. **启动 Foundry Local（用于本地模式）：**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用场景

### Foundry Local（默认）

**选项 1：使用 FoundryLocalManager（推荐）**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**选项 2：手动配置**
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


## 代码架构

### 客户端工厂模式

此示例使用工厂模式创建适当的客户端：

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


### 流式响应

此示例展示了流式响应以实现实时响应生成：

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


## 环境变量

### Foundry Local 配置

| 变量         | 描述                 | 默认值           | 是否必需 |
|--------------|----------------------|------------------|----------|
| `MODEL`      | 使用的模型别名       | `phi-4-mini`     | 否       |
| `BASE_URL`   | Foundry Local 端点   | `http://localhost:8000` | 否       |
| `API_KEY`    | API 密钥（本地可选） | `""`             | 否       |

### Azure OpenAI 配置

| 变量                     | 描述                     | 默认值                 | 是否必需 |
|--------------------------|--------------------------|------------------------|----------|
| `AZURE_OPENAI_ENDPOINT`  | Azure OpenAI 资源端点    | -                      | 是       |
| `AZURE_OPENAI_API_KEY`   | Azure OpenAI API 密钥    | -                      | 是       |
| `AZURE_OPENAI_API_VERSION` | API 版本               | `2024-08-01-preview`   | 否       |
| `MODEL`                  | Azure 部署名称           | `your-deployment-name` | 是       |

## 高级功能

### 自动服务发现

此示例根据环境变量自动检测适当的服务：

1. **Azure 模式**：如果设置了 `AZURE_OPENAI_ENDPOINT` 和 `AZURE_OPENAI_API_KEY`
2. **Foundry SDK 模式**：如果 Foundry Local SDK 可用
3. **手动模式**：回退到手动配置

### 错误处理

- 从 SDK 到手动配置的优雅回退
- 清晰的错误信息以便排查问题
- 针对网络问题的正确异常处理
- 验证必需的环境变量

## 性能考虑

### 本地与云的权衡

**Foundry Local 优势：**
- ✅ 无 API 成本
- ✅ 数据隐私（数据不离开设备）
- ✅ 支持模型的低延迟
- ✅ 可离线工作

**Azure OpenAI 优势：**
- ✅ 访问最新的大型模型
- ✅ 更高的吞吐量
- ✅ 无需本地计算资源
- ✅ 企业级 SLA

## 故障排除

### 常见问题

1. **“无法使用 Foundry SDK”警告：**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure 身份验证错误：**
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


### 健康检查

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## 后续步骤

- **示例 03**：模型发现与基准测试
- **示例 04**：构建 Chainlit RAG 应用
- **示例 05**：多代理编排
- **示例 06**：模型作为工具的路由

## 参考资料

- [Azure OpenAI 文档](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK 参考](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK 文档](https://github.com/openai/openai-python)
- [流式完成指南](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

