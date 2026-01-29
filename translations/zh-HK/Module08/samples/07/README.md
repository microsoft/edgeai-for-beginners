# Foundry Local 作為 API 範例

此範例展示如何使用 Microsoft Foundry Local 作為 REST API 服務，而不依賴 OpenAI SDK。它展示了直接的 HTTP 整合模式，以實現最大程度的控制和自定義。

## 概述

基於 Microsoft 官方的 Foundry Local 模式，此範例提供：
- 與 FoundryLocalManager 的直接 REST API 整合
- 自定義 HTTP 客戶端實現
- 模型管理和健康監控
- 流式和非流式響應處理
- 適合生產環境的錯誤處理和重試邏輯

## 先決條件

1. **Foundry Local 安裝**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python 依賴項**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## 架構

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 主要功能

### 1. **直接 HTTP 整合**
- 純 REST API 調用，無需 SDK 依賴
- 自定義身份驗證和標頭
- 完全控制請求/響應處理

### 2. **模型管理**
- 動態模型加載和卸載
- 健康監控和狀態檢查
- 性能指標收集

### 3. **生產模式**
- 帶有指數回退的重試機制
- 故障容忍的斷路器
- 全面的日誌記錄和監控

### 4. **靈活的響應處理**
- 用於實時應用的流式響應
- 用於高吞吐量場景的批量處理
- 自定義響應解析和驗證

## 使用範例

### 基本 API 整合
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

### 流式整合
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### 健康監控
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## 文件結構

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

## Microsoft Foundry Local 整合

此範例遵循 Microsoft 的官方模式：

1. **SDK 整合**：使用 `FoundryLocalManager` 進行服務管理
2. **REST 端點**：直接調用 `/v1/chat/completions` 和其他端點
3. **身份驗證**：正確處理本地服務的 API 密鑰
4. **模型管理**：目錄列出、下載和加載模式
5. **錯誤處理**：Microsoft 推薦的錯誤代碼和響應

## 入門指南

1. **安裝依賴項**
   ```bash
   pip install -r requirements.txt
   ```

2. **運行基本範例**
   ```bash
   python examples/basic_usage.py
   ```

3. **嘗試流式處理**
   ```bash
   python examples/streaming.py
   ```

4. **生產環境設置**
   ```bash
   python examples/production.py
   ```

## 配置

用於自定義的環境變量：
- `FOUNDRY_MODEL`：默認使用的模型（默認值："phi-4-mini"）
- `FOUNDRY_TIMEOUT`：請求超時時間（秒）（默認值：30）
- `FOUNDRY_RETRIES`：重試次數（默認值：3）
- `FOUNDRY_LOG_LEVEL`：日誌級別（默認值："INFO"）

## 最佳實踐

1. **連接管理**：重用 HTTP 連接以提高性能
2. **錯誤處理**：實施帶有指數回退的正確重試邏輯
3. **資源監控**：跟蹤模型內存使用和性能
4. **安全性**：即使是本地服務也要使用正確的身份驗證
5. **測試**：包括單元測試和整合測試

## 疑難排解

### 常見問題

**服務未運行**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**模型加載問題**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**連接錯誤**
- 確保 Foundry Local 在正確的端口上運行
- 檢查防火牆設置
- 確保正確的身份驗證標頭

## 性能優化

1. **連接池**：對多次請求使用 session 對象
2. **異步操作**：利用 asyncio 進行並發請求
3. **緩存**：在適當的地方緩存模型響應
4. **監控**：跟蹤響應時間並調整超時設置

## 學習成果

完成此範例後，您將了解：
- 與 Foundry Local 的直接 REST API 整合
- 自定義 HTTP 客戶端實現模式
- 適合生產環境的錯誤處理和監控
- Microsoft Foundry Local 服務架構
- 本地 AI 服務的性能優化技術

## 下一步

- 探索範例 08：Windows 11 聊天應用程序
- 嘗試範例 09：多代理協作
- 學習範例 10：Foundry Local 作為工具整合

---

