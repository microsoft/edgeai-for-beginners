<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T21:49:44+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "zh"
}
-->
# 第1节：开始使用 Foundry Local

## 摘要

学习如何安装、配置并运行您的第一个 AI 模型，使用 Microsoft Foundry Local。本次动手实践课程将从安装到使用 Phi-4、Qwen 和 DeepSeek 等模型构建您的第一个聊天应用程序，提供逐步的本地推理入门指导。

## 学习目标

完成本节课程后，您将能够：

- **安装和配置**：正确安装并验证 Foundry Local
- **掌握 CLI 操作**：使用 Foundry Local CLI 进行模型管理和部署
- **运行您的第一个模型**：成功部署并与本地 AI 模型交互
- **构建聊天应用程序**：使用 Foundry Local Python SDK 创建一个基础聊天应用程序
- **理解本地 AI**：掌握本地推理和模型管理的基础知识

## 前置条件

### 系统要求

- **Windows**：Windows 11（22H2或更高版本）或 **macOS**：macOS 11+（有限支持）
- **内存**：最低8GB，推荐16GB以上
- **存储空间**：模型需要至少10GB的可用空间
- **Python**：安装3.10或更高版本
- **管理员权限**：安装需要管理员权限

### 开发环境

- 推荐使用带有 Python 扩展的 Visual Studio Code
- 命令行访问（Windows上的PowerShell，macOS上的终端）
- Git（用于克隆代码库，可选）

## 课程流程（30分钟）

### 第1步：安装 Foundry Local（5分钟）

#### Windows 安装

使用 Windows 包管理器安装 Foundry Local：

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

替代方法：直接从 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) 下载

#### macOS 安装（有限支持）

> [!NOTE]  
> macOS 支持目前处于预览阶段。请查看官方文档以获取最新信息。

如果支持，使用 Homebrew 安装：

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS 用户的替代方法：**
- 使用 Windows 11 虚拟机（Parallels/UTM），并按照 Windows 步骤操作
- 如果可用，通过容器运行并配置 `FOUNDRY_LOCAL_ENDPOINT`

### 第2步：验证安装（3分钟）

安装完成后，重启终端并验证 Foundry Local 是否正常工作：

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

预期输出应显示版本信息和可用命令。

### 第3步：设置 Python 环境（5分钟）

为本次课程创建一个专用的 Python 环境：

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


### 第4步：运行您的第一个模型（7分钟）

现在让我们在本地运行第一个 AI 模型！

#### 从 Phi-4 Mini 开始（推荐的第一个模型）

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> 此命令会下载模型（首次运行时）并自动启动 Foundry Local 服务。

#### 检查运行状态

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### 尝试其他模型

在 phi-4-mini 正常运行后，尝试其他模型：

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### 第5步：构建您的第一个聊天应用程序（10分钟）

现在让我们创建一个使用刚刚启动的模型的 Python 应用程序。

#### 创建聊天脚本

创建一个名为 `my_first_chat.py` 的新文件（或使用提供的示例）：

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
> **相关示例**：有关更高级的用法，请参阅：
>
> - **Python 示例**：`Workshop/samples/session01/chat_bootstrap.py` - 包括流式响应和错误处理
> - **Jupyter Notebook**：`Workshop/notebooks/session01_chat_bootstrap.ipynb` - 带详细说明的交互版本

#### 测试您的聊天应用程序

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

替代方法：直接使用提供的示例

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

或者探索交互式笔记本  
在 VS Code 中打开 Workshop/notebooks/session01_chat_bootstrap.ipynb

尝试以下示例对话：

- “什么是 Microsoft Foundry Local？”
- “列出运行本地 AI 模型的三个好处”
- “帮我理解边缘 AI”

## 您的成果

恭喜！您已经成功完成：

1. ✅ **安装 Foundry Local** 并验证其正常工作  
2. ✅ **本地启动您的第一个 AI 模型**（phi-4-mini）  
3. ✅ **通过命令行测试不同模型**  
4. ✅ **构建了一个连接到本地 AI 的聊天应用程序**  
5. ✅ **体验了无需云依赖的本地 AI 推理**  

## 理解发生了什么

### 本地 AI 推理

- 您的 AI 模型完全在您的计算机上运行
- 没有数据发送到云端
- 响应由您的 CPU/GPU 本地生成
- 隐私和安全性得到保障

### 模型管理

- `foundry model run` 下载并启动模型
- **FoundryLocalManager SDK** 自动处理服务启动和模型加载
- 模型会缓存到本地以供将来使用
- 可以下载多个模型，但通常一次运行一个
- 服务会自动管理模型生命周期

### SDK 与 CLI 方法

- **CLI 方法**：使用 `foundry model run <model>` 手动管理模型
- **SDK 方法**：使用 `FoundryLocalManager(alias)` 自动服务和模型管理
- **推荐**：应用程序使用 SDK，测试和探索使用 CLI

## 常用命令参考

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


### 模型推荐

- **phi-4-mini**：最佳入门模型 - 快速、轻量、质量良好
- **qwen2.5-0.5b**：推理速度最快，内存占用最少
- **gpt-oss-20b**：响应质量更高，但需要更多资源
- **deepseek-coder-1.3b**：针对编程和代码任务优化

## 故障排除

### “找不到 Foundry 命令”

**解决方案：**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### “模型加载失败”

**解决方案：**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### “本地主机连接被拒绝”

**解决方案：**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## 下一步

### 立即行动

1. **尝试**不同的模型和提示
2. **修改**您的聊天应用程序以尝试不同的模型
3. **创建**您自己的提示并测试响应
4. **探索**第2节：构建 RAG 应用程序

### 高级学习路径

1. **第2节**：使用 RAG（检索增强生成）构建 AI 解决方案
2. **第3节**：比较不同的开源模型
3. **第4节**：使用最前沿的模型
4. **第5节**：构建多代理 AI 系统

## 环境变量（可选）

对于更高级的用法，您可以设置以下环境变量：

| 变量 | 用途 | 示例 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 默认使用的模型 | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆盖端点 URL | `http://localhost:5273/v1` |

在项目目录中创建一个 `.env` 文件：
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## 其他资源

### 文档

- [Foundry Local Python SDK 参考](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 安装指南](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [模型目录](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 示例代码

- **第1节 Python 示例**：`Workshop/samples/session01/chat_bootstrap.py` - 包含流式聊天应用程序
- **第1节笔记本**：`Workshop/notebooks/session01_chat_bootstrap.ipynb` - 交互式教程  
- [模块08 示例01](../Module08/samples/01/README.md) - REST 聊天快速入门
- [模块08 示例02](../Module08/samples/02/README.md) - OpenAI SDK 集成
- [模块08 示例03](../Module08/samples/03/README.md) - 模型发现与基准测试

### 社区

- [Foundry Local GitHub 讨论区](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 社区](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**课程时长**：30分钟动手实践 + 15分钟问答  
**难度级别**：初学者  
**前置条件**：Windows 11/macOS 11+，Python 3.10+，管理员权限

## 课程示例场景

### 真实场景

**场景**：某企业 IT 团队需要评估设备上的 AI 推理，以处理敏感的员工反馈数据，而无需将数据发送到外部服务。

**您的目标**：展示本地 AI 模型能够在保持数据完全隐私的同时，以亚秒级的延迟提供高质量的响应。

### 测试提示

使用以下提示验证您的设置：

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### 成功标准

- ✅ 所有提示在2秒内获得响应  
- ✅ 没有数据离开您的本地机器  
- ✅ 响应相关且有帮助  
- ✅ 您的聊天应用程序运行顺畅  

此验证确保您的 Foundry Local 设置已准备好参加第2至第6节的高级课程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->