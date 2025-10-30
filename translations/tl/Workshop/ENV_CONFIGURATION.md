<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:44:37+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "tl"
}
-->
# Gabay sa Pag-configure ng Kapaligiran

## Pangkalahatang-ideya

Ang mga halimbawa sa Workshop ay gumagamit ng mga environment variable para sa configuration, na nakapaloob sa `.env` file sa ugat ng repository. Pinapadali nito ang pag-customize nang hindi kinakailangang baguhin ang code.

## Mabilisang Simula

### 1. Suriin ang mga Kinakailangan

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. I-configure ang Kapaligiran

Ang `.env` file ay naka-configure na may mga default na setting. Karamihan sa mga user ay hindi na kailangang baguhin ito.

**Opsyonal**: Suriin at i-customize ang mga setting:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. I-apply ang Configuration

**Para sa Python Scripts:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Para sa Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Sanggunian sa Environment Variables

### Pangunahing Configuration

| Variable | Default | Deskripsyon |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Default na modelo para sa mga halimbawa |
| `FOUNDRY_LOCAL_ENDPOINT` | (walang laman) | Override sa service endpoint |
| `PYTHONPATH` | Mga path ng Workshop | Path para sa paghahanap ng Python module |

**Kailan dapat i-set ang FOUNDRY_LOCAL_ENDPOINT:**
- Remote na Foundry Local instance
- Custom na port configuration
- Paghiwalay ng development/production

**Halimbawa:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Mga Variable na Pang-Sesyon

#### Sesyon 02: RAG Pipeline
| Variable | Default | Layunin |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | Pre-configured | Test na tanong |

#### Sesyon 03: Benchmarking
| Variable | Default | Layunin |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Mga modelong ibe-benchmark |
| `BENCH_ROUNDS` | `3` | Mga iteration kada modelo |
| `BENCH_PROMPT` | Pre-configured | Test na prompt |
| `BENCH_STREAM` | `0` | Sukatin ang latency ng unang token |

#### Sesyon 04: Paghahambing ng Modelo
| Variable | Default | Layunin |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Maliit na language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Malaking language model |
| `COMPARE_PROMPT` | Pre-configured | Prompt para sa paghahambing |
| `COMPARE_RETRIES` | `2` | Mga attempt sa pag-retry |

#### Sesyon 05: Multi-Agent Orchestration
| Variable | Default | Layunin |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelo ng researcher agent |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modelo ng editor agent |
| `AGENT_QUESTION` | Pre-configured | Test na tanong |

### Configuration para sa Kahusayan

| Variable | Default | Layunin |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | I-print ang token usage |
| `RETRY_ON_FAIL` | `1` | Paganahin ang retry logic |
| `RETRY_BACKOFF` | `1.0` | Delay sa pag-retry (segundo) |

## Karaniwang Configurations

### Setup para sa Development (Mabilisang Iteration)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Setup para sa Production (Pagtuon sa Kalidad)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Setup para sa Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Espesyalisasyon ng Multi-Agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Remote Development
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Mga Inirerekomendang Modelo

### Ayon sa Gamit

**Pangkalahatang Layunin:**
- `phi-4-mini` - Balanseng kalidad at bilis

**Mabilis na Tugon:**
- `qwen2.5-0.5b` - Napakabilis, maganda para sa classification
- `phi-4-mini` - Mabilis na may magandang kalidad

**Mataas na Kalidad:**
- `qwen2.5-7b` - Pinakamahusay na kalidad, mas mataas ang resource usage
- `phi-4-mini` - Magandang kalidad, mas mababa ang resources

**Pagbuo ng Code:**
- `deepseek-coder-1.3b` - Espesyal para sa code
- `phi-4-mini` - Pangkalahatang layunin sa coding

### Ayon sa Availability ng Resource

**Mababang Resource (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Katamtamang Resource (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Mataas na Resource (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Advanced na Configuration

### Custom na Endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperature & Sampling (Override sa Code)

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

## Pag-aayos ng Problema

### Hindi Nalo-load ang Environment Variables

**Mga Sintomas:**
- Mali ang mga modelong ginagamit ng scripts
- Mga error sa koneksyon
- Hindi nakikilala ang mga variable

**Mga Solusyon:**
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

### Mga Isyu sa Koneksyon ng Serbisyo

**Mga Sintomas:**
- Mga error na "Connection refused"
- "Service not available"
- Mga timeout error

**Mga Solusyon:**
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

### Hindi Natagpuan ang Modelo

**Mga Sintomas:**
- Mga error na "Model not found"
- "Alias not recognized"

**Mga Solusyon:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Mga Error sa Import

**Mga Sintomas:**
- Mga error na "Module not found"

**Mga Solusyon:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Pagsubok ng Configuration

### Suriin ang Pag-load ng Kapaligiran

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

### Subukan ang Koneksyon sa Foundry Local

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

## Mga Pinakamahusay na Kasanayan sa Seguridad

### 1. Huwag Kailanman I-commit ang Mga Secrets

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Gumamit ng Hiwa-hiwalay na .env Files

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. I-rotate ang Mga API Keys

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Gumamit ng Config na Pang-Specific sa Kapaligiran

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentasyon ng SDK

- **Pangunahing Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentasyon**: Tingnan ang SDK repository para sa pinakabago

## Karagdagang Resources

- `QUICK_START.md` - Gabay sa pagsisimula
- `SDK_MIGRATION_NOTES.md` - Mga detalye sa pag-update ng SDK
- `Workshop/samples/*/README.md` - Mga gabay para sa partikular na halimbawa

---

**Huling Na-update**: 2025-01-08  
**Bersyon**: 2.0  
**SDK**: Foundry Local Python SDK (pinakabago)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.