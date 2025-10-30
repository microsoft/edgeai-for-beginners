<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T20:34:15+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "zh"
}
-->
# 第一节：开始使用 Foundry Local

## 摘要

通过在 Windows 11 上安装和配置 Foundry Local，开启您的探索之旅。学习如何设置 CLI、启用硬件加速以及缓存模型以实现快速的本地推理。本次动手实践课程将指导您使用可复现的 CLI 命令运行 Phi、Qwen、DeepSeek 和 GPT-OSS-20B 等模型。

## 学习目标

在本节课结束时，您将能够：

- **安装和配置**：在 Windows 11 上设置 Foundry Local，并优化性能设置
- **掌握 CLI 操作**：使用 Foundry Local CLI 进行模型管理和部署
- **启用硬件加速**：使用 ONNXRuntime 或 WebGPU 配置 GPU 加速
- **部署多个模型**：在本地运行 phi-4、GPT-OSS-20B、Qwen 和 DeepSeek 模型
- **构建您的第一个应用程序**：改编现有示例以使用 Foundry Local Python SDK

# 测试模型（非交互式单次提示）
foundry model run phi-4-mini --prompt "你好，请介绍一下自己"

- Windows 11 (22H2 或更高版本)
# 列出可用的目录模型（运行后加载的模型会显示）
foundry model list
## 注意：目前没有专门的 `--running` 标志；要查看哪些模型已加载，请启动聊天或检查服务日志。
- 已安装 Python 3.10+
- Visual Studio Code 和 Python 扩展
- 安装所需的管理员权限

### （可选）环境变量

创建 `.env` 文件（或在 shell 中设置）以使脚本更具可移植性：
# 比较响应（非交互式）
foundry model run gpt-oss-20b --prompt "用简单的语言解释边缘 AI"
| 变量 | 用途 | 示例 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 首选模型别名（目录自动选择最佳变体） | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆盖端点（否则由管理器自动生成） | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | 启用流式演示 | `true` |

> 如果 `FOUNDRY_LOCAL_ENDPOINT=auto`（或未设置），我们将从 SDK 管理器中推导出端点。

## 演示流程（30 分钟）

### 1. 安装 Foundry Local 并验证 CLI 设置（10 分钟）

# 列出缓存的模型
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS（预览 / 如果支持）**

如果提供了原生 macOS 包（请查看官方文档以获取最新信息）：

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

如果尚未提供 macOS 原生二进制文件，您仍然可以：
1. 使用 Windows 11 ARM/Intel 虚拟机（Parallels / UTM），并按照 Windows 步骤操作。
2. 通过容器运行模型（如果已发布容器镜像），并将 `FOUNDRY_LOCAL_ENDPOINT` 设置为暴露的端口。

**创建 Python 虚拟环境（跨平台）**

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

升级 pip 并安装核心依赖项：
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 步骤 1.2：验证安装

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 步骤 1.3：配置环境

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK 引导（推荐）

与其手动启动服务和运行模型，不如使用 **Foundry Local Python SDK** 来引导一切：

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

如果您更喜欢显式控制，仍然可以使用 CLI + OpenAI 客户端，如后续所示。

### 2. 通过 CLI 本地运行模型（10 分钟）

#### 步骤 3.1：部署 Phi-4 模型

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 步骤 3.2：部署 GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 步骤 3.3：加载其他模型

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. 初学项目：改编 01-run-phi 以使用 Foundry Local（5 分钟）

#### 步骤 4.1：创建基础聊天应用程序

创建 `samples/01-foundry-quickstart/chat_quickstart.py`（更新以使用管理器，如果可用）：

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

#### 步骤 4.2：测试应用程序

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## 涉及的关键概念

### 1. Foundry Local 架构

- **本地推理引擎**：完全在您的设备上运行模型
- **OpenAI SDK 兼容性**：与现有 OpenAI 代码无缝集成
- **模型管理**：高效下载、缓存和运行多个模型
- **硬件优化**：利用 GPU、NPU 和 CPU 加速

### 2. CLI 命令参考

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

## 常见问题排查

### 问题 1：“Foundry 命令未找到”

**解决方案：**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### 问题 2：“模型加载失败”

**解决方案：**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### 问题 3：“localhost:5273 上的连接被拒绝”

**解决方案：**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## 性能优化技巧

### 1. 模型选择策略

- **Phi-4-mini**：适合一般任务，内存使用较低
- **Qwen2.5-0.5b**：推理速度最快，资源需求最少
- **GPT-OSS-20B**：质量最高，但需要更多资源
- **DeepSeek-Coder**：针对编程任务优化

### 2. 硬件优化

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. 性能监控

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### 可选增强功能

| 增强功能 | 内容 | 方法 |
|----------|------|------|
| 共享工具 | 删除重复的客户端/引导逻辑 | 使用 `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| 令牌使用可见性 | 提前培养成本/效率意识 | 设置 `SHOW_USAGE=1` 以打印提示/完成/总令牌 |
| 确定性比较 | 稳定的基准测试和回归检查 | 使用 `temperature=0`、`top_p=1`、一致的提示文本 |
| 首令牌延迟 | 感知响应性指标 | 使用流式传输调整基准脚本（`BENCH_STREAM=1`） |
| 瞬时错误重试 | 冷启动时的弹性演示 | `RETRY_ON_FAIL=1`（默认）并调整 `RETRY_BACKOFF` |
| 冒烟测试 | 快速验证关键流程 | 在研讨会前运行 `python Workshop/tests/smoke.py` |
| 模型别名配置文件 | 在机器之间快速切换模型集 | 维护 `.env` 文件，包含 `FOUNDRY_LOCAL_ALIAS`、`SLM_ALIAS`、`LLM_ALIAS` |
| 缓存效率 | 避免在多样本运行中重复预热 | 工具缓存管理器；在脚本/笔记本之间重用 |
| 首次运行预热 | 减少 p95 延迟峰值 | 在创建 `FoundryLocalManager` 后发送一个小提示

示例确定性预热基线（PowerShell）：

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

您应该在第二次运行时看到类似的输出和相同的令牌计数，确认确定性。

## 下一步

完成本节课程后：

1. **探索第二节**：使用 Azure AI Foundry RAG 构建 AI 解决方案
2. **尝试不同模型**：实验 Qwen、DeepSeek 和其他模型系列
3. **优化性能**：根据您的具体硬件微调设置
4. **构建自定义应用程序**：在您的项目中使用 Foundry Local SDK

## 其他资源

### 文档
- [Foundry Local Python SDK 参考](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 安装指南](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [模型目录](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 示例代码
- [模块08 示例 01](./samples/01/README.md) - REST 聊天快速入门
- [模块08 示例 02](./samples/02/README.md) - OpenAI SDK 集成
- [模块08 示例 03](./samples/03/README.md) - 模型发现与基准测试

### 社区
- [Foundry Local GitHub 讨论](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 社区](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**课程时长**：30 分钟动手实践 + 15 分钟问答
**难度级别**：初学者
**先决条件**：Windows 11、Python 3.10+、管理员权限

## 示例场景与研讨会映射

| 研讨会脚本 / 笔记本 | 场景 | 目标 | 示例输入 | 所需数据集 |
|---------------------|------|------|----------|------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | 内部 IT 团队评估设备上的推理能力，用于隐私评估门户 | 证明本地 SLM 在标准提示下的响应时间低于一秒 | “列出本地推理的两个优点。” | 无（单次提示） |
| 快速入门改编代码块 | 开发者将现有 OpenAI 脚本迁移到 Foundry Local | 展示即插即用的兼容性 | “列出本地推理的两个优点。” | 仅内联提示 |

### 场景叙述
安全与合规团队必须验证敏感原型数据是否可以在本地处理。他们使用引导脚本运行多个提示（隐私、延迟、成本），并使用确定性 `temperature=0` 模式捕获基线输出，以供后续比较（第三节基准测试和第四节 SLM 与 LLM 对比）。

### 最小提示集 JSON（可选）
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

使用此列表创建可复现的评估循环或为未来的回归测试框架提供种子。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。