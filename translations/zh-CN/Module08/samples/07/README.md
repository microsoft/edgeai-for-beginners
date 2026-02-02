# Foundry Local 作为 API 示例

此示例展示了如何将 Microsoft Foundry Local 作为 REST API 服务使用，而无需依赖 OpenAI SDK。它展示了直接的 HTTP 集成模式，以实现最大程度的控制和定制。

## 概述

基于 Microsoft 官方的 Foundry Local 模式，此示例提供：
- 与 FoundryLocalManager 的直接 REST API 集成
- 自定义 HTTP 客户端实现
- 模型管理和健康监控
- 流式和非流式响应处理
- 面向生产环境的错误处理和重试逻辑

## 前提条件

1. **Foundry Local 安装**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python 依赖**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## 架构

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 关键功能

### 1. **直接 HTTP 集成**
- 纯 REST API 调用，无需 SDK 依赖
- 自定义认证和请求头
- 完全控制请求/响应处理

### 2. **模型管理**
- 动态加载和卸载模型
- 健康监控和状态检查
- 性能指标收集

### 3. **生产模式**
- 带有指数回退的重试机制
- 故障容错的断路器模式
- 全面的日志记录和监控

### 4. **灵活的响应处理**
- 用于实时应用的流式响应
- 用于高吞吐量场景的批量处理
- 自定义响应解析和验证

## 使用示例

### 基本 API 集成
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### 流式集成
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### 健康监控
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## 文件结构

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local 集成

此示例遵循 Microsoft 官方模式：

1. **SDK 集成**：使用 `FoundryLocalManager` 进行服务管理
2. **REST 端点**：直接调用 `/v1/chat/completions` 和其他端点
3. **认证**：正确处理本地服务的 API 密钥
4. **模型管理**：目录列出、下载和加载模式
5. **错误处理**：Microsoft 推荐的错误代码和响应

## 入门指南

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **运行基本示例**
   ```bash
   python examples/basic_usage.py
   ```

3. **尝试流式处理**
   ```bash
   python examples/streaming.py
   ```

4. **生产环境设置**
   ```bash
   python examples/production.py
   ```

## 配置

用于定制的环境变量：
- `FOUNDRY_MODEL`：默认使用的模型（默认值："phi-4-mini"）
- `FOUNDRY_TIMEOUT`：请求超时时间（秒）（默认值：30）
- `FOUNDRY_RETRIES`：重试次数（默认值：3）
- `FOUNDRY_LOG_LEVEL`：日志级别（默认值："INFO"）

## 最佳实践

1. **连接管理**：重用 HTTP 连接以提高性能
2. **错误处理**：实现带有指数回退的重试逻辑
3. **资源监控**：跟踪模型内存使用和性能
4. **安全性**：即使是本地服务也要使用正确的认证
5. **测试**：包括单元测试和集成测试

## 故障排除

### 常见问题

**服务未运行**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**模型加载问题**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**连接错误**
- 验证 Foundry Local 是否运行在正确的端口
- 检查防火墙设置
- 确保正确的认证请求头

## 性能优化

1. **连接池**：使用会话对象处理多次请求
2. **异步操作**：利用 asyncio 进行并发请求
3. **缓存**：在适当情况下缓存模型响应
4. **监控**：跟踪响应时间并调整超时设置

## 学习成果

完成此示例后，您将了解：
- 与 Foundry Local 的直接 REST API 集成
- 自定义 HTTP 客户端实现模式
- 面向生产环境的错误处理和监控
- Microsoft Foundry Local 服务架构
- 本地 AI 服务的性能优化技术

## 下一步

- 探索示例 08：Windows 11 聊天应用
- 尝试示例 09：多代理编排
- 学习示例 10：Foundry Local 作为工具集成

---

