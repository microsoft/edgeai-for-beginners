<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:49:06+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Usanidi wa Mazingira

## Muhtasari

Mifano ya Warsha hutumia vigezo vya mazingira kwa usanidi, vilivyowekwa katikati kwenye faili `.env` katika mzizi wa hifadhi. Hii inaruhusu ubinafsishaji rahisi bila kubadilisha msimbo.

## Kuanza Haraka

### 1. Hakikisha Mahitaji

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Sanidi Mazingira

Faili `.env` tayari imewekwa na chaguo-msingi zinazofaa. Watumiaji wengi hawatahitaji kubadilisha chochote.

**Hiari**: Kagua na ubadilishe mipangilio:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Tumia Usanidi

**Kwa Script za Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Kwa Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Marejeleo ya Vigezo vya Mazingira

### Usanidi wa Msingi

| Kigezo | Chaguo-msingi | Maelezo |
|--------|---------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Mfano wa chaguo-msingi kwa mifano |
| `FOUNDRY_LOCAL_ENDPOINT` | (tupu) | Badilisha huduma ya mwisho |
| `PYTHONPATH` | Njia za Warsha | Njia ya utafutaji wa moduli za Python |

**Wakati wa kuweka FOUNDRY_LOCAL_ENDPOINT:**
- Kesi ya mbali ya Foundry Local
- Usanidi wa bandari maalum
- Utengano wa maendeleo/uzalishaji

**Mfano:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Vigezo Maalum vya Kikao

#### Kikao 02: RAG Pipeline
| Kigezo | Chaguo-msingi | Kusudi |
|--------|---------------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Mfano wa kuweka |
| `RAG_QUESTION` | Imewekwa awali | Swali la majaribio |

#### Kikao 03: Upimaji
| Kigezo | Chaguo-msingi | Kusudi |
|--------|---------------|--------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Mifano ya kupima |
| `BENCH_ROUNDS` | `3` | Marudio kwa kila mfano |
| `BENCH_PROMPT` | Imewekwa awali | Maelekezo ya majaribio |
| `BENCH_STREAM` | `0` | Pima ucheleweshaji wa tokeni ya kwanza |

#### Kikao 04: Ulinganisho wa Mfano
| Kigezo | Chaguo-msingi | Kusudi |
|--------|---------------|--------|
| `SLM_ALIAS` | `phi-4-mini` | Mfano mdogo wa lugha |
| `LLM_ALIAS` | `qwen2.5-7b` | Mfano mkubwa wa lugha |
| `COMPARE_PROMPT` | Imewekwa awali | Maelekezo ya kulinganisha |
| `COMPARE_RETRIES` | `2` | Jaribio la kurudia |

#### Kikao 05: Uratibu wa Wakala Wengi
| Kigezo | Chaguo-msingi | Kusudi |
|--------|---------------|--------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Mfano wa wakala wa utafiti |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Mfano wa wakala wa mhariri |
| `AGENT_QUESTION` | Imewekwa awali | Swali la majaribio |

### Usanidi wa Uaminifu

| Kigezo | Chaguo-msingi | Kusudi |
|--------|---------------|--------|
| `SHOW_USAGE` | `1` | Chapisha matumizi ya tokeni |
| `RETRY_ON_FAIL` | `1` | Washa mantiki ya kurudia |
| `RETRY_BACKOFF` | `1.0` | Muda wa kuchelewa kurudia (sekunde) |

## Usanidi wa Kawaida

### Usanidi wa Maendeleo (Kurudia Haraka)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Usanidi wa Uzalishaji (Kuzingatia Ubora)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Usanidi wa Upimaji
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Utaalamu wa Wakala Wengi
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Maendeleo ya Mbali
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Mifano Inayopendekezwa

### Kwa Kesi ya Matumizi

**Matumizi ya Kawaida:**
- `phi-4-mini` - Ubora na kasi iliyosawazishwa

**Majibu ya Haraka:**
- `qwen2.5-0.5b` - Haraka sana, nzuri kwa uainishaji
- `phi-4-mini` - Haraka na ubora mzuri

**Ubora wa Juu:**
- `qwen2.5-7b` - Ubora bora, matumizi ya rasilimali zaidi
- `phi-4-mini` - Ubora mzuri, rasilimali za chini

**Uzalishaji wa Msimbo:**
- `deepseek-coder-1.3b` - Imebobea kwa msimbo
- `phi-4-mini` - Kusudi la jumla la msimbo

### Kwa Upatikanaji wa Rasilimali

**Rasilimali Chache (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Rasilimali za Kati (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Rasilimali za Juu (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Usanidi wa Juu

### Huduma za Mwisho Maalum

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Joto & Sampuli (Badilisha kwenye Msimbo)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Usanidi Mseto wa Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Utatuzi wa Matatizo

### Vigezo vya Mazingira Havijapakiwa

**Dalili:**
- Script zinatumia mifano isiyo sahihi
- Hitilafu za muunganisho
- Vigezo havitambuliki

**Suluhisho:**
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

### Masuala ya Muunganisho wa Huduma

**Dalili:**
- Hitilafu za "Connection refused"
- "Huduma haipatikani"
- Hitilafu za muda wa kuisha

**Suluhisho:**
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

### Mfano Haupatikani

**Dalili:**
- Hitilafu za "Model not found"
- "Alias haijatambulika"

**Suluhisho:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Hitilafu za Uingizaji

**Dalili:**
- Hitilafu za "Module not found"

**Suluhisho:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Kupima Usanidi

### Hakikisha Upakiaji wa Mazingira

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

### Jaribu Muunganisho wa Foundry Local

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

## Mazoea Bora ya Usalama

### 1. Usikubali Siri

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Tumia Faili za .env Zilizotenganishwa

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Badilisha Funguo za API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Tumia Usanidi Maalum wa Mazingira

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Nyaraka za SDK

- **Hifadhi Kuu**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Nyaraka za API**: Angalia hifadhi ya SDK kwa za hivi karibuni

## Rasilimali Zingine

- `QUICK_START.md` - Mwongozo wa kuanza
- `SDK_MIGRATION_NOTES.md` - Maelezo ya sasisho la SDK
- `Workshop/samples/*/README.md` - Miongozo maalum ya mifano

---

**Imeboreshwa Mwisho**: 2025-01-08  
**Toleo**: 2.0  
**SDK**: Foundry Local Python SDK (ya hivi karibuni)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.