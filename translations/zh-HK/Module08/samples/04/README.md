# 範例 04：使用 Chainlit 建立生產級聊天應用程式

一個全面的範例，展示了使用 Microsoft Foundry Local 建立生產級聊天應用程式的多種方法，包含現代化的網頁介面、串流回應以及尖端的瀏覽器技術。

## 包含內容

- **🚀 Chainlit 聊天應用程式** (`app.py`)：具備串流功能的生產級聊天應用程式
- **🌐 WebGPU 示範** (`webgpu-demo/`)：基於瀏覽器的 AI 推理，支援硬體加速
- **🎨 開放 WebUI 整合** (`open-webui-guide.md`)：專業的 ChatGPT 風格介面
- **📚 教育筆記本** (`chainlit_app.ipynb`)：互動式學習材料

## 快速開始

### 1. Chainlit 聊天應用程式

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

開啟於：`http://localhost:8080`

### 2. WebGPU 瀏覽器示範

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

開啟於：`http://localhost:5173`

### 3. 開放 WebUI 設定

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

開啟於：`http://localhost:3000`

## 架構模式

### 本地 vs 雲端決策矩陣

| 情境 | 建議 | 原因 |
|------|------|------|
| **隱私敏感資料** | 🏠 本地 (Foundry) | 資料不會離開裝置 |
| **複雜推理** | ☁️ 雲端 (Azure OpenAI) | 可使用更大的模型 |
| **即時聊天** | 🏠 本地 (Foundry) | 延遲更低，回應更快 |
| **文件分析** | 🔄 混合 | 本地進行提取，雲端進行分析 |
| **程式碼生成** | 🏠 本地 (Foundry) | 隱私 + 專用模型 |
| **研究任務** | ☁️ 雲端 (Azure OpenAI) | 需要廣泛的知識庫 |

### 技術比較

| 技術 | 使用情境 | 優點 | 缺點 |
|------|----------|------|------|
| **Chainlit** | Python 開發者、快速原型設計 | 設定簡單，支援串流 | 僅限 Python |
| **WebGPU** | 最大隱私、離線情境 | 瀏覽器原生，無需伺服器 | 模型大小有限 |
| **開放 WebUI** | 生產部署、團隊使用 | 專業 UI，使用者管理 | 需要 Docker |

## 先決條件

- **Foundry Local**：已安裝並運行 ([下載](https://aka.ms/foundry-local-installer))
- **Python**：3.10+ 並啟用虛擬環境
- **模型**：至少載入一個 (`foundry model run phi-4-mini`)
- **瀏覽器**：支援 WebGPU 的 Chrome/Edge，用於示範
- **Docker**：用於開放 WebUI (可選)

## 安裝與設定

### 1. Python 環境設定

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local 設定

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 範例應用程式

### Chainlit 聊天應用程式

**功能：**
- 🚀 **即時串流**：生成的 token 即時顯示
- 🛡️ **強大的錯誤處理**：優雅降級與恢復
- 🎨 **現代化 UI**：內建專業聊天介面
- 🔧 **靈活配置**：環境變數與自動檢測
- 📱 **響應式設計**：適用於桌面與行動裝置

**快速開始：**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU 瀏覽器示範

**功能：**
- 🌐 **瀏覽器原生 AI**：無需伺服器，完全在瀏覽器中運行
- ⚡ **WebGPU 加速**：硬體加速（若可用）
- 🔒 **最大隱私**：資料不會離開您的裝置
- 🎯 **零安裝**：適用於任何相容的瀏覽器
- 🔄 **優雅降級**：若 WebGPU 不可用，則回退至 CPU

**運行：**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### 開放 WebUI 整合

**功能：**
- 🎨 **ChatGPT 風格介面**：專業且熟悉的 UI
- 👥 **多使用者支援**：使用者帳號與對話歷史
- 📁 **文件處理**：上傳並分析文件
- 🔄 **模型切換**：輕鬆切換不同模型
- 🐳 **Docker 部署**：生產級容器化設定

**快速設定：**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 配置參考

### 環境變數

| 變數 | 描述 | 預設值 | 範例 |
|------|------|--------|------|
| `MODEL` | 使用的模型別名 | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local 端點 | 自動檢測 | `http://localhost:51211` |
| `API_KEY` | API 金鑰 (本地可選) | `""` | `your-api-key` |

## 疑難排解

### 常見問題

**Chainlit 應用程式：**

1. **服務不可用：**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **端口衝突：**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python 環境問題：**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU 示範：**

1. **WebGPU 不支援：**
   - 更新至 Chrome/Edge 113+
   - 啟用 WebGPU：`chrome://flags/#enable-unsafe-webgpu`
   - 檢查 GPU 狀態：`chrome://gpu`
   - 示範將自動回退至 CPU

2. **模型載入錯誤：**
   - 確保網路連線以下載模型
   - 檢查瀏覽器主控台是否有 CORS 錯誤
   - 確保使用 HTTP 提供服務 (非 file://)

**開放 WebUI：**

1. **連線被拒：**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **模型未顯示：**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### 驗證清單

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## 高級用法

### 性能優化

**Chainlit：**
- 使用串流以提升感知性能
- 實施連線池以支援高併發
- 緩存模型回應以處理重複查詢
- 監控大型對話歷史的記憶體使用情況

**WebGPU：**
- 使用 WebGPU 以獲得最大隱私與速度
- 實施模型量化以減小模型大小
- 使用 Web Workers 進行背景處理
- 在瀏覽器存儲中緩存已編譯的模型

**開放 WebUI：**
- 使用持久化卷保存對話歷史
- 為 Docker 容器配置資源限制
- 實施使用者資料的備份策略
- 設置反向代理以進行 SSL 終止

### 整合模式

**本地/雲端混合：**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**多模態管道：**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## 生產部署

### 安全考量

- **API 金鑰**：使用環境變數，切勿硬編碼
- **網路**：在生產環境中使用 HTTPS，考慮使用 VPN 供團隊存取
- **存取控制**：為開放 WebUI 實施身份驗證
- **資料隱私**：審核哪些資料留在本地，哪些發送至雲端
- **更新**：保持 Foundry Local 和容器的最新版本

### 監控與維護

- **健康檢查**：實施端點監控
- **日誌**：集中管理所有元件的日誌
- **指標**：追蹤回應時間、錯誤率、資源使用情況
- **備份**：定期備份對話資料與配置

## 參考與資源

### 文件
- [Chainlit 文件](https://docs.chainlit.io/) - 完整框架指南
- [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - 微軟官方文件
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU 整合
- [開放 WebUI 文件](https://docs.openwebui.com/) - 高級配置指南

### 範例檔案
- [`app.py`](../../../../../Module08/samples/04/app.py) - 生產級 Chainlit 應用程式
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - 教育筆記本
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - 基於瀏覽器的 AI 推理
- [`open-webui-guide.md`](./open-webui-guide.md) - 完整的開放 WebUI 設定

### 相關範例
- [Session 4 文件](../../04.CuttingEdgeModels.md) - 完整課程指南
- [Foundry Local 範例](https://github.com/microsoft/foundry-local/tree/main/samples) - 官方範例

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。