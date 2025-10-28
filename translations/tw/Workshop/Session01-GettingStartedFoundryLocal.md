<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:15:52+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "tw"
}
-->
# 第 1 節：開始使用 Foundry Local

## 摘要

透過在 Windows 11 上安裝和配置 Foundry Local，開啟您的旅程。學習如何設置 CLI、啟用硬體加速以及緩存模型以進行快速的本地推理。本次動手操作課程將逐步演示如何使用可重現的 CLI 命令運行 Phi、Qwen、DeepSeek 和 GPT-OSS-20B 等模型。

## 學習目標

完成本節後，您將能夠：

- **安裝和配置**：在 Windows 11 上設置 Foundry Local，並進行最佳性能配置
- **掌握 CLI 操作**：使用 Foundry Local CLI 進行模型管理和部署
- **啟用硬體加速**：使用 ONNXRuntime 或 WebGPU 配置 GPU 加速
- **部署多個模型**：本地運行 phi-4、GPT-OSS-20B、Qwen 和 DeepSeek 模型
- **建立您的第一個應用程式**：改編現有範例以使用 Foundry Local Python SDK

# 測試模型（非互動式單次提示）
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 或更高版本)
# 列出可用的目錄模型（運行後加載的模型會出現）
foundry model list
## 注意：目前沒有專門的 `--running` 標誌；要查看哪些模型已加載，請啟動聊天或檢查服務日誌。
- 已安裝 Python 3.10+
- 安裝了 Python 擴展的 Visual Studio Code
- 安裝需要管理員權限

### （可選）環境變數

創建 `.env`（或在 shell 中設置）以使腳本可移植：
# 比較回應（非互動式）
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| 變數 | 用途 | 示例 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 首選模型別名（目錄自動選擇最佳變體） | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆蓋端點（否則由管理器自動生成） | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | 啟用流式演示 | `true` |

> 如果 `FOUNDRY_LOCAL_ENDPOINT=auto`（或未設置），我們將從 SDK 管理器中推導。

## 演示流程（30 分鐘）

### 1. 安裝 Foundry Local 並驗證 CLI 設置（10 分鐘）

# 列出緩存的模型
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS（預覽 / 如果支持）**

如果提供了原生 macOS 套件（請檢查官方文檔以獲取最新信息）：

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

如果尚未提供 macOS 原生二進制文件，您仍然可以：
1. 使用 Windows 11 ARM/Intel VM（Parallels / UTM），並按照 Windows 步驟操作。
2. 通過容器運行模型（如果已發布容器映像），並將 `FOUNDRY_LOCAL_ENDPOINT` 設置為暴露的端口。

**創建 Python 虛擬環境（跨平台）**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

升級 pip 並安裝核心依賴項：
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 步驟 1.2：驗證安裝

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 步驟 1.3：配置環境

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK 引導（推薦）

與手動啟動服務和運行模型相比，**Foundry Local Python SDK** 可以引導所有操作：

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

如果您更喜歡顯式控制，仍然可以使用 CLI + OpenAI 客戶端，如後續所示。

### 2. 通過 CLI 本地運行模型（10 分鐘）

#### 步驟 3.1：部署 Phi-4 模型

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 步驟 3.2：部署 GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 步驟 3.3：加載其他模型

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. 初學者項目：改編 01-run-phi 用於 Foundry Local（5 分鐘）

#### 步驟 4.1：創建基本聊天應用程式

創建 `samples/01-foundry-quickstart/chat_quickstart.py`（更新以使用管理器，如果可用）：

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### 步驟 4.2：測試應用程式

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## 涵蓋的關鍵概念

### 1. Foundry Local 架構

- **本地推理引擎**：完全在您的設備上運行模型
- **OpenAI SDK 兼容性**：與現有 OpenAI 代碼無縫集成
- **模型管理**：高效下載、緩存和運行多個模型
- **硬體優化**：利用 GPU、NPU 和 CPU 加速

### 2. CLI 命令參考

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK 集成

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## 常見問題排查

### 問題 1："Foundry command not found"

**解決方案：**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### 問題 2："Model failed to load"

**解決方案：**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### 問題 3："Connection refused on localhost:5273"

**解決方案：**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## 性能優化提示

### 1. 模型選擇策略

- **Phi-4-mini**：適合一般任務，內存使用較低
- **Qwen2.5-0.5b**：推理速度最快，資源需求最少
- **GPT-OSS-20B**：質量最高，需要更多資源
- **DeepSeek-Coder**：針對編程任務進行優化

### 2. 硬體優化

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. 監控性能

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### 可選增強功能

| 增強功能 | 內容 | 方法 |
|----------|------|------|
| 共享工具 | 移除重複的客戶端/引導邏輯 | 使用 `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| 令牌使用可見性 | 提早教導成本/效率思維 | 設置 `SHOW_USAGE=1` 以打印提示/完成/總令牌 |
| 確定性比較 | 穩定的基準測試和回歸檢查 | 使用 `temperature=0`、`top_p=1`、一致的提示文本 |
| 首令牌延遲 | 感知響應性指標 | 使用流式方式改編基準腳本（`BENCH_STREAM=1`） |
| 暫時錯誤重試 | 冷啟動時的彈性演示 | `RETRY_ON_FAIL=1`（默認）並調整 `RETRY_BACKOFF` |
| 冒煙測試 | 快速檢查關鍵流程 | 在工作坊前運行 `python Workshop/tests/smoke.py` |
| 模型別名配置檔案 | 在機器之間快速切換模型集 | 維護 `.env`，設置 `FOUNDRY_LOCAL_ALIAS`、`SLM_ALIAS`、`LLM_ALIAS` |
| 緩存效率 | 避免多範例運行中的重複預熱 | 工具緩存管理器；在腳本/筆記本中重用 |
| 首次運行預熱 | 減少 p95 延遲峰值 | 在創建 `FoundryLocalManager` 後發送一個小提示 |

示例確定性預熱基線（PowerShell）：

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

您應該在第二次運行中看到類似的輸出和相同的令牌計數，確認確定性。

## 下一步

完成本節後：

1. **探索第 2 節**：使用 Azure AI Foundry RAG 構建 AI 解決方案
2. **嘗試不同模型**：試驗 Qwen、DeepSeek 和其他模型系列
3. **優化性能**：根據您的特定硬體進行設置微調
4. **構建自定義應用程式**：在您的項目中使用 Foundry Local SDK

## 附加資源

### 文檔
- [Foundry Local Python SDK 參考](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 安裝指南](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [模型目錄](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 範例代碼
- [Module08 範例 01](./samples/01/README.md) - REST 聊天快速入門
- [Module08 範例 02](./samples/02/README.md) - OpenAI SDK 集成
- [Module08 範例 03](./samples/03/README.md) - 模型發現與基準測試

### 社群
- [Foundry Local GitHub 討論](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 社群](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**課程時長**：30 分鐘動手操作 + 15 分鐘問答
**難度級別**：初學者
**先決條件**：Windows 11、Python 3.10+、管理員訪問權限

## 範例場景與工作坊映射

| 工作坊腳本 / 筆記本 | 場景 | 目標 | 示例輸入 | 所需數據集 |
|---------------------|------|------|----------|------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | 評估設備推理的隱私評估門戶的內部 IT 團隊 | 證明本地 SLM 在標準提示下的響應時間低於一秒 | "列出本地推理的兩個優勢。" | 無（單次提示） |
| 快速入門改編代碼塊 | 開發者將現有 OpenAI 腳本遷移到 Foundry Local | 展示即插即用的兼容性 | "列出本地推理的兩個優勢。" | 僅內嵌提示 |

### 場景敘述
安全與合規小組必須驗證敏感原型數據是否可以在本地處理。他們使用引導腳本運行多個提示（隱私、延遲、成本），並使用確定性 `temperature=0` 模式捕獲基線輸出以供後續比較（第 3 節基準測試和第 4 節 SLM 與 LLM 對比）。

### 最小提示集 JSON（可選）
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

使用此列表創建可重現的評估循環或為未來的回歸測試框架提供種子。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。