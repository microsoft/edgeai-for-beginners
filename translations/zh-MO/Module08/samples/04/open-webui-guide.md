# Open WebUI + Foundry Local 整合指南

本指南展示如何將 Open WebUI 與 Microsoft Foundry Local 整合，打造一個專業的 ChatGPT 介面，並使用您本地的 AI 模型。

## 概述

Open WebUI 提供了一個現代化、使用者友好的聊天介面，可連接至任何兼容 OpenAI 的 API。透過與 Foundry Local 整合，您可以獲得以下功能：

- **專業介面**：類似 ChatGPT 的現代化設計
- **本地隱私**：所有處理均在您的設備上進行
- **模型切換**：輕鬆切換不同的本地模型
- **對話歷史**：持久的聊天記錄與上下文
- **檔案上傳**：文件分析與檔案處理功能
- **自訂角色**：系統提示與角色自訂

## 先決條件

### 必需軟體

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### 加載模型

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 快速設定（推薦）

### 步驟 1：使用 Docker 運行 Open WebUI

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### 步驟 2：初始設定

1. **打開瀏覽器**：前往 `http://localhost:3000`
2. **建立帳戶**：設置管理員使用者（第一個使用者將成為管理員）
3. **驗證連接**：模型應自動出現在下拉選單中

### 步驟 3：測試連接

1. 從下拉選單中選擇您的模型（例如 "phi-4-mini"）
2. 輸入測試訊息："你好！你能介紹一下自己嗎？"
3. 您應該能看到本地模型的流式回應

## 高級配置

### 環境變數

| 變數 | 用途 | 預設值 | 範例 |
|------|------|--------|------|
| `OPENAI_API_BASE_URL` | Foundry Local 端點 | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API 金鑰（必需但本地未使用） | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | 會話加密金鑰 | 自動生成 | `your-secret-key` |
| `ENABLE_SIGNUP` | 允許新使用者註冊 | `True` | `False` |

### 手動配置（替代方案）

如果環境變數無法正常工作，可手動配置：

1. **打開設定**：點擊設定（齒輪圖示）
2. **前往連接**：設定 → 連接 → OpenAI
3. **設置 API 詳細資訊**：
   - API 基本 URL：`http://host.docker.internal:51211/v1`
   - API 金鑰：`foundry-local-key`（任意值均可）
4. **保存並測試**：點擊 "保存"，然後使用模型進行測試

### 持久化數據存儲

若需保存對話與設定：

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 疑難排解

### 連接問題

**問題**："連接被拒絕" 或模型未加載

**解決方案**：
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### 模型未顯示

**問題**：Open WebUI 的下拉選單中未顯示模型

**調試步驟**：
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**修復**：確保模型已正確加載：
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker 網絡問題

**問題**：`host.docker.internal` 無法解析

**Windows 解決方案**：
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**替代方案**：找到您的機器 IP：
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### 性能問題

**回應速度慢**：
1. 檢查模型是否使用 GPU 加速：`foundry service ps`
2. 確保系統資源充足（RAM/GPU 記憶體）
3. 測試使用較小的模型

**記憶體問題**：
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## 使用指南

### 基本聊天

1. **選擇模型**：從下拉選單中選擇 Foundry Local 模型
2. **輸入訊息**：使用底部的文字輸入框
3. **發送**：按 Enter 或點擊發送按鈕
4. **查看回應**：即時查看流式回應

### 高級功能

**檔案上傳**：
1. 點擊迴紋針圖示
2. 上傳文件（PDF、TXT 等）
3. 提問有關內容的問題
4. 模型將根據文件進行分析並回應

**自訂系統提示**：
1. 設定 → 個性化
2. 設置自訂系統提示
3. 創建一致的 AI 個性/行為

**對話管理**：
- **新聊天**：點擊 "+" 開始新的對話
- **聊天歷史**：從側邊欄訪問之前的對話
- **導出**：下載聊天記錄為文字/JSON 格式

**模型比較**：
1. 在多個瀏覽器標籤中打開相同的 Open WebUI
2. 在每個標籤中選擇不同的模型
3. 比較相同提示的回應

### 整合模式

**開發工作流程**：
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## 生產部署

### 安全設置

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### 多使用者設置

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### 監控與日誌

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## 清理

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## 下一步

### 增強建議

1. **自訂模型**：將您自己的微調模型添加到 Foundry Local
2. **API 整合**：通過 Open WebUI 功能連接外部 API
3. **文件處理**：設置高級 RAG 管道
4. **多模態**：配置視覺模型進行圖像分析

### 擴展考量

- **負載均衡**：在反向代理後運行多個 Foundry Local 實例
- **模型路由**：針對不同用例使用不同模型
- **資源管理**：優化 GPU 記憶體以支持多使用者
- **備份策略**：定期備份對話數據與配置

## 參考資料

- [Open WebUI 文件](https://docs.openwebui.com/)
- [Open WebUI GitHub 儲存庫](https://github.com/open-webui/open-webui)
- [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker 安裝指南](https://docs.docker.com/get-docker/)

---

