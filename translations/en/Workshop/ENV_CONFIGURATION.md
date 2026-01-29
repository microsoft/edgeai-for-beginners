# Environment Configuration Guide

## Overview

The Workshop samples use environment variables for configuration, centralized in the `.env` file located at the root of the repository. This makes it easy to customize settings without modifying the code.

## Quick Start

### 1. Verify Prerequisites

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configure Environment

The `.env` file comes pre-configured with reasonable defaults. Most users won't need to make any changes.

**Optional**: Review and adjust settings:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Apply Configuration

**For Python Scripts:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**For Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Environment Variables Reference

### Core Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Default model used in samples |
| `FOUNDRY_LOCAL_ENDPOINT` | (empty) | Custom service endpoint override |
| `PYTHONPATH` | Workshop paths | Python module search path |

**When to set FOUNDRY_LOCAL_ENDPOINT:**
- Using a remote Foundry Local instance
- Custom port configurations
- Separating development and production environments

**Example:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Session-Specific Variables

#### Session 02: RAG Pipeline
| Variable | Default | Purpose |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | Pre-configured | Test question |

#### Session 03: Benchmarking
| Variable | Default | Purpose |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Models to benchmark |
| `BENCH_ROUNDS` | `3` | Number of iterations per model |
| `BENCH_PROMPT` | Pre-configured | Test prompt |
| `BENCH_STREAM` | `0` | Measure latency for the first token |

#### Session 04: Model Comparison
| Variable | Default | Purpose |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Small language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Large language model |
| `COMPARE_PROMPT` | Pre-configured | Comparison prompt |
| `COMPARE_RETRIES` | `2` | Number of retry attempts |

#### Session 05: Multi-Agent Orchestration
| Variable | Default | Purpose |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Researcher agent model |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Editor agent model |
| `AGENT_QUESTION` | Pre-configured | Test question |

### Reliability Configuration

| Variable | Default | Purpose |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Display token usage |
| `RETRY_ON_FAIL` | `1` | Enable retry logic |
| `RETRY_BACKOFF` | `1.0` | Delay between retries (in seconds) |

## Common Configurations

### Development Setup (Fast Iteration)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Production Setup (Quality Focus)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking Setup
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Multi-Agent Specialization
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Remote Development
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Recommended Models

### By Use Case

**General Purpose:**
- `phi-4-mini` - Balanced quality and speed

**Fast Responses:**
- `qwen2.5-0.5b` - Very fast, ideal for classification tasks
- `phi-4-mini` - Fast with good quality

**High Quality:**
- `qwen2.5-7b` - Best quality, higher resource consumption
- `phi-4-mini` - Good quality with lower resource usage

**Code Generation:**
- `deepseek-coder-1.3b` - Specialized for coding tasks
- `phi-4-mini` - General-purpose coding

### By Resource Availability

**Low Resources (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Medium Resources (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**High Resources (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Advanced Configuration

### Custom Endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperature & Sampling (Override in Code)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI Hybrid Setup

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Troubleshooting

### Environment Variables Not Loaded

**Symptoms:**
- Scripts use incorrect models
- Connection errors occur
- Variables are not recognized

**Solutions:**
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

### Service Connection Issues

**Symptoms:**
- "Connection refused" errors
- "Service not available" messages
- Timeout errors

**Solutions:**
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

### Model Not Found

**Symptoms:**
- "Model not found" errors
- "Alias not recognized" messages

**Solutions:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Import Errors

**Symptoms:**
- "Module not found" errors

**Solutions:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testing Configuration

### Verify Environment Loading

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

### Test Foundry Local Connection

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

## Security Best Practices

### 1. Never Commit Secrets

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Use Separate .env Files

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotate API Keys

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Use Environment-Specific Config

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK Documentation

- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentation**: Refer to the SDK repository for the latest updates

## Additional Resources

- `QUICK_START.md` - Guide for getting started
- `Workshop/samples/*/README.md` - Guides specific to samples

---

**Last Updated**: 2025-01-08  
**Version**: 2.0  
**SDK**: Foundry Local Python SDK (latest)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->