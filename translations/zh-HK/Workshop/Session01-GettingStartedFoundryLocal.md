# 第1節：開始使用 Foundry Local

## 摘要

學習如何安裝、配置及運行您的第一個 AI 模型，使用 Microsoft Foundry Local。本次實作課程將逐步介紹本地推理的過程，從安裝到使用 Phi-4、Qwen 和 DeepSeek 等模型建立您的第一個聊天應用程式。

## 學習目標

完成本節後，您將能夠：

- **安裝與配置**：正確設置 Foundry Local 並驗證安裝
- **掌握 CLI 操作**：使用 Foundry Local CLI 進行模型管理與部署
- **運行您的第一個模型**：成功部署並與本地 AI 模型互動
- **建立聊天應用程式**：使用 Foundry Local Python SDK 創建基本聊天應用程式
- **理解本地 AI**：掌握本地推理及模型管理的基本概念

## 先決條件

### 系統需求

- **Windows**：Windows 11 (22H2 或更新版本) 或 **macOS**：macOS 11+（有限支援）
- **RAM**：最低 8GB，建議 16GB 或以上
- **儲存空間**：模型需要至少 10GB 的可用空間
- **Python**：已安裝 3.10 或更新版本
- **管理員權限**：安裝需要管理員權限

### 開發環境

- 建議使用 Visual Studio Code 並安裝 Python 擴展
- 命令行訪問（Windows 使用 PowerShell，macOS 使用 Terminal）
- Git 用於克隆存儲庫（可選）

## 工作坊流程（30 分鐘）

### 第1步：安裝 Foundry Local（5 分鐘）

#### Windows 安裝

使用 Windows 套件管理器安裝 Foundry Local：

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

替代方法：直接從 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) 下載

#### macOS 安裝（有限支援）

> [!NOTE]  
> macOS 支援目前處於預覽階段。請查看官方文件以獲取最新資訊。

如果可用，使用 Homebrew 安裝：

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS 使用者的替代方法：**
- 使用 Windows 11 虛擬機（Parallels/UTM），並按照 Windows 步驟操作
- 如果可用，通過容器運行並配置 `FOUNDRY_LOCAL_ENDPOINT`

### 第2步：驗證安裝（3 分鐘）

安裝完成後，重啟終端並驗證 Foundry Local 是否正常運行：

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

預期輸出應顯示版本資訊及可用命令。

### 第3步：設置 Python 環境（5 分鐘）

為本次工作坊創建專用的 Python 環境：

**Windows：**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux：**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### 第4步：運行您的第一個模型（7 分鐘）

現在讓我們在本地運行第一個 AI 模型！

#### 從 Phi-4 Mini 開始（推薦的第一個模型）

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> 此命令會下載模型（首次運行時）並自動啟動 Foundry Local 服務。

#### 檢查正在運行的內容

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### 嘗試不同的模型

Phi-4 Mini 運行後，嘗試其他模型：

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### 第5步：建立您的第一個聊天應用程式（10 分鐘）

現在讓我們創建一個使用剛啟動的模型的 Python 應用程式。

#### 創建聊天腳本

創建一個名為 `my_first_chat.py` 的新文件（或使用提供的範例）：

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]  
> **相關範例**：如需更高級的用法，請參考：
>
> - **Python 範例**：`Workshop/samples/session01/chat_bootstrap.py` - 包含流式回應及錯誤處理
> - **Jupyter Notebook**：`Workshop/notebooks/session01_chat_bootstrap.ipynb` - 詳細解釋的互動版本

#### 測試您的聊天應用程式

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

替代方法：直接使用提供的範例

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

或探索互動式筆記本  
在 VS Code 中打開 Workshop/notebooks/session01_chat_bootstrap.ipynb

嘗試以下示例對話：

- "什麼是 Microsoft Foundry Local？"
- "列出本地運行 AI 模型的三個好處"
- "幫我理解邊緣 AI"

## 您已完成的內容

恭喜！您已成功：

1. ✅ **安裝 Foundry Local** 並驗證其正常運行  
2. ✅ **本地啟動您的第一個 AI 模型**（Phi-4 Mini）  
3. ✅ **通過命令行測試不同模型**  
4. ✅ **建立一個連接本地 AI 的聊天應用程式**  
5. ✅ **體驗本地 AI 推理**，無需依賴雲端  

## 理解發生了什麼

### 本地 AI 推理

- 您的 AI 模型完全在您的電腦上運行
- 沒有數據被發送到雲端
- 回應由您的 CPU/GPU 本地生成
- 保持隱私和安全性

### 模型管理

- `foundry model run` 下載並啟動模型
- **FoundryLocalManager SDK** 自動處理服務啟動及模型加載
- 模型會緩存於本地以供未來使用
- 可下載多個模型，但通常一次只運行一個
- 服務會自動管理模型生命周期

### SDK 與 CLI 方法

- **CLI 方法**：使用 `foundry model run <model>` 手動管理模型
- **SDK 方法**：使用 `FoundryLocalManager(alias)` 自動管理服務及模型
- **推薦**：應用程式使用 SDK，測試及探索使用 CLI

## 常用命令參考

### 基本 CLI 命令

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```


### 模型推薦

- **phi-4-mini**：最佳入門模型 - 快速、輕量、質量良好
- **qwen2.5-0.5b**：推理速度最快，內存使用最少
- **gpt-oss-20b**：回應質量更高，但需要更多資源
- **deepseek-coder-1.3b**：針對編程及代碼任務進行優化

## 疑難排解

### "找不到 Foundry 命令"

**解決方案：**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "模型加載失敗"

**解決方案：**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### "本地主機連接被拒絕"

**解決方案：**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## 下一步

### 即時行動

1. **嘗試**不同的模型及提示
2. **修改**您的聊天應用程式以嘗試不同模型
3. **創建**自己的提示並測試回應
4. **探索**第2節：建立 RAG 應用程式

### 高級學習路徑

1. **第2節**：使用 RAG（檢索增強生成）構建 AI 解決方案
2. **第3節**：比較不同的開源模型
3. **第4節**：使用尖端模型
4. **第5節**：構建多代理 AI 系統

## 環境變數（可選）

如需更高級的用法，您可以設置以下環境變數：

| 變數 | 用途 | 示例 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 預設使用的模型 | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆蓋端點 URL | `http://localhost:5273/v1` |

在您的項目目錄中創建 `.env` 文件：
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## 附加資源

### 文件

- [Foundry Local Python SDK 參考](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 安裝指南](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [模型目錄](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 範例代碼

- **Session01 Python 範例**：`Workshop/samples/session01/chat_bootstrap.py` - 完整的聊天應用程式，包含流式回應
- **Session01 Notebook**：`Workshop/notebooks/session01_chat_bootstrap.ipynb` - 互動式教程  
- [Module08 範例 01](../Module08/samples/01/README.md) - REST 聊天快速入門
- [Module08 範例 02](../Module08/samples/02/README.md) - OpenAI SDK 集成
- [Module08 範例 03](../Module08/samples/03/README.md) - 模型發現及基準測試

### 社群

- [Foundry Local GitHub 討論](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 社群](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**課程時長**：30 分鐘實作 + 15 分鐘問答  
**難度等級**：初學者  
**先決條件**：Windows 11/macOS 11+，Python 3.10+，管理員權限

## 工作坊示例場景

### 真實世界背景

**場景**：某企業 IT 團隊需要評估設備上的 AI 推理，以處理敏感的員工反饋，而不將數據發送到外部服務。

**您的目標**：展示本地 AI 模型能夠在保持數據完全隱私的情況下，以毫秒級延遲提供高質量回應。

### 測試提示

使用以下提示驗證您的設置：

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### 成功標準

- ✅ 所有提示在 2 秒內獲得回應  
- ✅ 沒有數據離開您的本地機器  
- ✅ 回應相關且有幫助  
- ✅ 您的聊天應用程式運行流暢  

此驗證確保您的 Foundry Local 設置已準備好參加第2至第6節的高級工作坊。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->