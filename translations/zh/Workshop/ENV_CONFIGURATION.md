<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T20:33:34+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "zh"
}
-->
# 环境配置指南

## 概述

Workshop 示例使用环境变量进行配置，集中在代码库根目录的 `.env` 文件中。这种方式可以轻松定制配置，而无需修改代码。

## 快速开始

### 1. 验证先决条件

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. 配置环境

`.env` 文件已预配置为合理的默认值。大多数用户无需更改任何内容。

**可选**：查看并定制设置：
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. 应用配置

**对于 Python 脚本：**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**对于 Notebook：**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## 环境变量参考

### 核心配置

| 变量 | 默认值 | 描述 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | 示例的默认模型 |
| `FOUNDRY_LOCAL_ENDPOINT` | （空） | 覆盖服务端点 |
| `PYTHONPATH` | Workshop 路径 | Python 模块搜索路径 |

**何时设置 FOUNDRY_LOCAL_ENDPOINT：**
- 远程 Foundry Local 实例
- 自定义端口配置
- 开发/生产环境分离

**示例：**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### 会话特定变量

#### 会话 02：RAG 管道
| 变量 | 默认值 | 用途 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 嵌入模型 |
| `RAG_QUESTION` | 预配置 | 测试问题 |

#### 会话 03：基准测试
| 变量 | 默认值 | 用途 |
|------|--------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | 要测试的模型 |
| `BENCH_ROUNDS` | `3` | 每个模型的迭代次数 |
| `BENCH_PROMPT` | 预配置 | 测试提示 |
| `BENCH_STREAM` | `0` | 测量首个 token 的延迟 |

#### 会话 04：模型比较
| 变量 | 默认值 | 用途 |
|------|--------|------|
| `SLM_ALIAS` | `phi-4-mini` | 小型语言模型 |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型语言模型 |
| `COMPARE_PROMPT` | 预配置 | 比较提示 |
| `COMPARE_RETRIES` | `2` | 重试次数 |

#### 会话 05：多代理编排
| 变量 | 默认值 | 用途 |
|------|--------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 研究员代理模型 |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | 编辑代理模型 |
| `AGENT_QUESTION` | 预配置 | 测试问题 |

### 可靠性配置

| 变量 | 默认值 | 用途 |
|------|--------|------|
| `SHOW_USAGE` | `1` | 打印 token 使用情况 |
| `RETRY_ON_FAIL` | `1` | 启用重试逻辑 |
| `RETRY_BACKOFF` | `1.0` | 重试延迟（秒） |

## 常见配置

### 开发设置（快速迭代）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### 生产设置（质量优先）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### 基准测试设置
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### 多代理专用设置
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### 远程开发
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## 推荐模型

### 按使用场景

**通用用途：**
- `phi-4-mini` - 质量与速度平衡

**快速响应：**
- `qwen2.5-0.5b` - 非常快，适合分类任务
- `phi-4-mini` - 快速且质量良好

**高质量：**
- `qwen2.5-7b` - 最佳质量，资源需求较高
- `phi-4-mini` - 质量良好，资源需求较低

**代码生成：**
- `deepseek-coder-1.3b` - 专为代码生成设计
- `phi-4-mini` - 通用代码生成

### 按资源可用性

**低资源（< 8GB RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**中等资源（8-16GB RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**高资源（16GB+ RAM）：**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## 高级配置

### 自定义端点

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### 温度与采样（代码中覆盖）

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI 混合设置

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 故障排除

### 环境变量未加载

**症状：**
- 脚本使用错误的模型
- 连接错误
- 变量未被识别

**解决方案：**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### 服务连接问题

**症状：**
- “连接被拒绝”错误
- “服务不可用”
- 超时错误

**解决方案：**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### 模型未找到

**症状：**
- “模型未找到”错误
- “别名未被识别”

**解决方案：**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### 导入错误

**症状：**
- “模块未找到”错误

**解决方案：**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## 测试配置

### 验证环境加载

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### 测试 Foundry Local 连接

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## 安全最佳实践

### 1. 切勿提交敏感信息

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. 使用单独的 .env 文件

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. 定期更换 API 密钥

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. 使用特定环境的配置

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK 文档

- **主代码库**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API 文档**: 请查看 SDK 代码库以获取最新信息

## 其他资源

- `QUICK_START.md` - 快速入门指南
- `SDK_MIGRATION_NOTES.md` - SDK 更新详情
- `Workshop/samples/*/README.md` - 示例特定指南

---

**最后更新日期**: 2025-01-08  
**版本**: 2.0  
**SDK**: Foundry Local Python SDK（最新）

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。