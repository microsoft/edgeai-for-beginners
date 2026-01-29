# ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ ਗਾਈਡ

## ਝਲਕ

ਵਰਕਸ਼ਾਪ ਦੇ ਨਮੂਨੇ ਸੰਰਚਨਾ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ, ਜੋ `.env` ਫਾਈਲ ਵਿੱਚ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਰੂਟ 'ਤੇ ਕੇਂਦਰਿਤ ਕੀਤੇ ਗਏ ਹਨ। ਇਸ ਨਾਲ ਕੋਡ ਨੂੰ ਬਦਲਣ ਦੀ ਲੋੜ ਬਿਨਾਂ ਅਸਾਨੀ ਨਾਲ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ ਹੋ ਸਕਦੀ ਹੈ।

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

### 1. ਪੂਰਵ ਸ਼ਰਤਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ ਕਰੋ

`.env` ਫਾਈਲ ਪਹਿਲਾਂ ਹੀ ਸਮਝਦਾਰ ਡਿਫਾਲਟ ਨਾਲ ਸੰਰਚਿਤ ਕੀਤੀ ਗਈ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਕੁਝ ਵੀ ਬਦਲਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੋਵੇਗੀ।

**ਵਿਕਲਪਿਕ**: ਸੈਟਿੰਗਾਂ ਦੀ ਸਮੀਖਾ ਕਰੋ ਅਤੇ ਕਸਟਮਾਈਜ਼ ਕਰੋ:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. ਸੰਰਚਨਾ ਲਾਗੂ ਕਰੋ

**ਪਾਈਥਨ ਸਕ੍ਰਿਪਟਾਂ ਲਈ:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**ਨੋਟਬੁੱਕਾਂ ਲਈ:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦਾ ਹਵਾਲਾ

### ਮੁੱਖ ਸੰਰਚਨਾ

| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਵੇਰਵਾ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | ਨਮੂਨਿਆਂ ਲਈ ਡਿਫਾਲਟ ਮਾਡਲ |
| `FOUNDRY_LOCAL_ENDPOINT` | (ਖਾਲੀ) | ਸੇਵਾ ਐਂਡਪੌਇੰਟ ਨੂੰ ਓਵਰਰਾਈਡ ਕਰੋ |
| `PYTHONPATH` | ਵਰਕਸ਼ਾਪ ਪਾਥ | ਪਾਈਥਨ ਮੋਡਿਊਲ ਖੋਜ ਪਾਥ |

**ਜਦੋਂ FOUNDRY_LOCAL_ENDPOINT ਸੈਟ ਕਰਨਾ ਹੋਵੇ:**
- ਰਿਮੋਟ Foundry Local ਇੰਸਟੈਂਸ
- ਕਸਟਮ ਪੋਰਟ ਸੰਰਚਨਾ
- ਵਿਕਾਸ/ਉਤਪਾਦਨ ਵੱਖ-ਵੱਖ

**ਉਦਾਹਰਨ:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### ਸੈਸ਼ਨ-ਵਿਸ਼ੇਸ਼ ਵੈਰੀਏਬਲ

#### ਸੈਸ਼ਨ 02: RAG ਪਾਈਪਲਾਈਨ
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਉਦੇਸ਼ |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ਐਮਬੈਡਿੰਗ ਮਾਡਲ |
| `RAG_QUESTION` | ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ | ਟੈਸਟ ਪ੍ਰਸ਼ਨ |

#### ਸੈਸ਼ਨ 03: ਬੈਂਚਮਾਰਕਿੰਗ
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਉਦੇਸ਼ |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | ਬੈਂਚਮਾਰਕ ਕਰਨ ਲਈ ਮਾਡਲ |
| `BENCH_ROUNDS` | `3` | ਪ੍ਰਤੀ ਮਾਡਲ ਦੁਹਰਾਈਆਂ |
| `BENCH_PROMPT` | ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ | ਟੈਸਟ ਪ੍ਰੰਪਟ |
| `BENCH_STREAM` | `0` | ਪਹਿਲੇ ਟੋਕਨ ਦੀ ਲੈਟੈਂਸੀ ਮਾਪੋ |

#### ਸੈਸ਼ਨ 04: ਮਾਡਲ ਤੁਲਨਾ
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਉਦੇਸ਼ |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `LLM_ALIAS` | `qwen2.5-7b` | ਵੱਡਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `COMPARE_PROMPT` | ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ | ਤੁਲਨਾ ਪ੍ਰੰਪਟ |
| `COMPARE_RETRIES` | `2` | ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ |

#### ਸੈਸ਼ਨ 05: ਮਲਟੀ-ਏਜੰਟ ਆਰਕਸਟਰੈਸ਼ਨ
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਉਦੇਸ਼ |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ਰਿਸਰਚਰ ਏਜੰਟ ਮਾਡਲ |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ਐਡੀਟਰ ਏਜੰਟ ਮਾਡਲ |
| `AGENT_QUESTION` | ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ | ਟੈਸਟ ਪ੍ਰਸ਼ਨ |

### ਭਰੋਸੇਮੰਦ ਸੰਰਚਨਾ

| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਉਦੇਸ਼ |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | ਟੋਕਨ ਦੀ ਵਰਤੋਂ ਪ੍ਰਿੰਟ ਕਰੋ |
| `RETRY_ON_FAIL` | `1` | ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਲਾਜ਼ਮੀ ਕਰੋ |
| `RETRY_BACKOFF` | `1.0` | ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਦੇਰੀ (ਸਕਿੰਟ) |

## ਆਮ ਸੰਰਚਨਾਵਾਂ

### ਵਿਕਾਸ ਸੈਟਅਪ (ਤੇਜ਼ ਦੁਹਰਾਈ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### ਉਤਪਾਦਨ ਸੈਟਅਪ (ਗੁਣਵੱਤਾ ਫੋਕਸ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### ਬੈਂਚਮਾਰਕਿੰਗ ਸੈਟਅਪ
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### ਮਲਟੀ-ਏਜੰਟ ਵਿਸ਼ੇਸ਼ਤਾ
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### ਰਿਮੋਟ ਵਿਕਾਸ
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## ਸਿਫਾਰਸ਼ੀ ਮਾਡਲ

### ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਨੁਸਾਰ

**ਸਧਾਰਨ ਉਦੇਸ਼:**
- `phi-4-mini` - ਗੁਣਵੱਤਾ ਅਤੇ ਗਤੀ ਦਾ ਸੰਤੁਲਨ

**ਤੇਜ਼ ਜਵਾਬ:**
- `qwen2.5-0.5b` - ਬਹੁਤ ਤੇਜ਼, ਵਰਗੀਕਰਨ ਲਈ ਵਧੀਆ
- `phi-4-mini` - ਤੇਜ਼ ਅਤੇ ਚੰਗੀ ਗੁਣਵੱਤਾ

**ਉੱਚ ਗੁਣਵੱਤਾ:**
- `qwen2.5-7b` - ਸਭ ਤੋਂ ਵਧੀਆ ਗੁਣਵੱਤਾ, ਵਧੇਰੇ ਸਰੋਤ ਦੀ ਵਰਤੋਂ
- `phi-4-mini` - ਚੰਗੀ ਗੁਣਵੱਤਾ, ਘੱਟ ਸਰੋਤ

**ਕੋਡ ਜਨਰੇਸ਼ਨ:**
- `deepseek-coder-1.3b` - ਕੋਡ ਲਈ ਵਿਸ਼ੇਸ਼
- `phi-4-mini` - ਸਧਾਰਨ ਉਦੇਸ਼ ਕੋਡਿੰਗ

### ਸਰੋਤ ਉਪਲਬਧਤਾ ਅਨੁਸਾਰ

**ਘੱਟ ਸਰੋਤ (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**ਦਰਮਿਆਨੀ ਸਰੋਤ (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**ਉੱਚ ਸਰੋਤ (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## ਉੱਚ-ਸਤਹ ਸੰਰਚਨਾ

### ਕਸਟਮ ਐਂਡਪੌਇੰਟ

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### ਤਾਪਮਾਨ ਅਤੇ ਸੈਂਪਲਿੰਗ (ਕੋਡ ਵਿੱਚ ਓਵਰਰਾਈਡ ਕਰੋ)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### ਐਜ਼ਰ ਓਪਨਏਆਈ ਹਾਈਬ੍ਰਿਡ ਸੈਟਅਪ

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## ਸਮੱਸਿਆ ਹੱਲ

### ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਲੋਡ ਨਹੀਂ ਹੋਏ

**ਲੱਛਣ:**
- ਸਕ੍ਰਿਪਟ ਗਲਤ ਮਾਡਲ ਵਰਤਦੇ ਹਨ
- ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ
- ਵੈਰੀਏਬਲ ਪਛਾਣੇ ਨਹੀਂ ਗਏ

**ਹੱਲ:**
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

### ਸੇਵਾ ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ

**ਲੱਛਣ:**
- "ਕਨੈਕਸ਼ਨ ਰਿਫਿਊਜ਼ਡ" ਗਲਤੀਆਂ
- "ਸੇਵਾ ਉਪਲਬਧ ਨਹੀਂ"
- ਟਾਈਮਆਉਟ ਗਲਤੀਆਂ

**ਹੱਲ:**
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

### ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ

**ਲੱਛਣ:**
- "ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ" ਗਲਤੀਆਂ
- "Alias ਪਛਾਣਿਆ ਨਹੀਂ ਗਿਆ"

**ਹੱਲ:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ਇੰਪੋਰਟ ਗਲਤੀਆਂ

**ਲੱਛਣ:**
- "ਮੋਡਿਊਲ ਨਹੀਂ ਮਿਲਿਆ" ਗਲਤੀਆਂ

**ਹੱਲ:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## ਸੰਰਚਨਾ ਦੀ ਜਾਂਚ

### ਵਾਤਾਵਰਣ ਲੋਡਿੰਗ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

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

### Foundry Local ਕਨੈਕਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ

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

## ਸੁਰੱਖਿਆ ਦੇ ਵਧੀਆ ਤਰੀਕੇ

### 1. ਕਦੇ ਵੀ ਰਾਜ਼ ਕਮਿਟ ਨਾ ਕਰੋ

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. ਵੱਖ-ਵੱਖ .env ਫਾਈਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API ਕੁੰਜੀਆਂ ਨੂੰ ਰੋਟੇਟ ਕਰੋ

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. ਵਾਤਾਵਰਣ-ਵਿਸ਼ੇਸ਼ ਸੰਰਚਨਾ ਦੀ ਵਰਤੋਂ ਕਰੋ

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK ਦਸਤਾਵੇਜ਼

- **ਮੁੱਖ ਰਿਪੋਜ਼ਟਰੀ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ਦਸਤਾਵੇਜ਼**: ਨਵੀਂ ਜਾਣਕਾਰੀ ਲਈ SDK ਰਿਪੋਜ਼ਟਰੀ ਚੈੱਕ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

- `QUICK_START.md` - ਸ਼ੁਰੂਆਤ ਕਰਨ ਦੀ ਗਾਈਡ
- `Workshop/samples/*/README.md` - ਨਮੂਨਾ-ਵਿਸ਼ੇਸ਼ ਗਾਈਡ

---

**ਆਖਰੀ ਅਪਡੇਟ**: 2025-01-08  
**ਵਰਜਨ**: 2.0  
**SDK**: Foundry Local Python SDK (ਤਾਜ਼ਾ)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->