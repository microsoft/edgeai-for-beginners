<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:51:47+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "ta"
}
-->
# சூழல் கட்டமைப்பு வழிகாட்டி

## மேலோட்டம்

வார்ஷாப் மாதிரிகள் `.env` கோப்பில் மையமாக்கப்பட்டுள்ள சூழல் மாறிகள் மூலம் கட்டமைப்பை பயன்படுத்துகின்றன. இது குறியீட்டை மாற்றாமல் எளிதாக தனிப்பயனாக்க அனுமதிக்கிறது.

## விரைவான தொடக்கம்

### 1. முன் தேவைகளை சரிபார்க்கவும்

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. சூழலை அமைக்கவும்

`.env` கோப்பு ஏற்கனவே சரியான இயல்புநிலை அமைப்புகளுடன் அமைக்கப்பட்டுள்ளது. பெரும்பாலான பயனாளர்கள் எதையும் மாற்ற தேவையில்லை.

**விருப்பத்தேர்வு**: அமைப்புகளை மதிப்பீடு செய்து தனிப்பயனாக்கவும்:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. கட்டமைப்பை பயன்படுத்தவும்

**Python ஸ்கிரிப்டுகளுக்கு:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**நோட்புக்குகளுக்கு:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## சூழல் மாறிகள் குறிப்பு

### முக்கிய கட்டமைப்பு

| மாறி | இயல்புநிலை | விளக்கம் |
|------|------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | மாதிரிகளுக்கான இயல்புநிலை மாடல் |
| `FOUNDRY_LOCAL_ENDPOINT` | (காலியாக) | சேவை முடுக்கத்தை மாற்றவும் |
| `PYTHONPATH` | வார்ஷாப் பாதைகள் | Python தொகுதி தேடல் பாதை |

**FOUNDRY_LOCAL_ENDPOINT அமைக்க வேண்டிய நேரம்:**
- தொலை Foundry Local நிகழ்வு
- தனிப்பயன் போர்ட் அமைப்பு
- மேம்பாடு/உற்பத்தி பிரிப்பு

**உதாரணம்:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### அமர்வு-சிறப்பு மாறிகள்

#### அமர்வு 02: RAG குழாய்
| மாறி | இயல்புநிலை | நோக்கம் |
|------|------------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | எம்பெடிங் மாடல் |
| `RAG_QUESTION` | முன்கூட்டியே அமைக்கப்பட்டது | சோதனை கேள்வி |

#### அமர்வு 03: தரவாய்வு
| மாறி | இயல்புநிலை | நோக்கம் |
|------|------------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | தரவாய்வு செய்யும் மாடல்கள் |
| `BENCH_ROUNDS` | `3` | மாடல் ஒன்றுக்கு மீள்பார்வை |
| `BENCH_PROMPT` | முன்கூட்டியே அமைக்கப்பட்டது | சோதனை ப்ராம்ட் |
| `BENCH_STREAM` | `0` | முதல் டோக்கன் தாமதத்தை அளவிடவும் |

#### அமர்வு 04: மாடல் ஒப்பீடு
| மாறி | இயல்புநிலை | நோக்கம் |
|------|------------|---------|
| `SLM_ALIAS` | `phi-4-mini` | சிறிய மொழி மாடல் |
| `LLM_ALIAS` | `qwen2.5-7b` | பெரிய மொழி மாடல் |
| `COMPARE_PROMPT` | முன்கூட்டியே அமைக்கப்பட்டது | ஒப்பீட்டு ப்ராம்ட் |
| `COMPARE_RETRIES` | `2` | மீண்டும் முயற்சிகள் |

#### அமர்வு 05: பல முகவர் ஒருங்கிணைப்பு
| மாறி | இயல்புநிலை | நோக்கம் |
|------|------------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ஆராய்ச்சியாளர் முகவர் மாடல் |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ஆசிரியர் முகவர் மாடல் |
| `AGENT_QUESTION` | முன்கூட்டியே அமைக்கப்பட்டது | சோதனை கேள்வி |

### நம்பகத்தன்மை அமைப்பு

| மாறி | இயல்புநிலை | நோக்கம் |
|------|------------|---------|
| `SHOW_USAGE` | `1` | டோக்கன் பயன்பாட்டை அச்சிடவும் |
| `RETRY_ON_FAIL` | `1` | மீண்டும் முயற்சி செய்யும் தந்திரத்தை இயக்கவும் |
| `RETRY_BACKOFF` | `1.0` | மீண்டும் முயற்சி தாமதம் (வினாடிகள்) |

## பொதுவான அமைப்புகள்

### மேம்பாட்டு அமைப்பு (வேகமான மீள்பார்வை)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### உற்பத்தி அமைப்பு (தரத்தை மையமாக்குதல்)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### தரவாய்வு அமைப்பு
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### பல முகவர் சிறப்பு
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### தொலை மேம்பாடு
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## பரிந்துரைக்கப்பட்ட மாடல்கள்

### பயன்பாட்டு வழக்கு அடிப்படையில்

**பொதுவான நோக்கம்:**
- `phi-4-mini` - தரம் மற்றும் வேகத்திற்கு சமநிலை

**வேகமான பதில்கள்:**
- `qwen2.5-0.5b` - மிகவும் வேகமானது, வகைப்பாட்டிற்கு சிறந்தது
- `phi-4-mini` - நல்ல தரத்துடன் வேகமானது

**உயர் தரம்:**
- `qwen2.5-7b` - சிறந்த தரம், அதிக வளங்களை பயன்படுத்துகிறது
- `phi-4-mini` - நல்ல தரம், குறைந்த வளங்கள்

**கோடு உருவாக்கல்:**
- `deepseek-coder-1.3b` - கோடுக்கு சிறப்பு
- `phi-4-mini` - பொதுவான நோக்குக்கான கோடிங்

### வளங்களின் கிடைப்பின் அடிப்படையில்

**குறைந்த வளங்கள் (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**மிதமான வளங்கள் (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**அதிக வளங்கள் (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## மேம்பட்ட அமைப்பு

### தனிப்பயன் முடுக்கங்கள்

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### வெப்பநிலை மற்றும் மாதிரிகள் (கோடில் மாற்றவும்)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI கலப்பு அமைப்பு

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## சிக்கல்களை சரி செய்யுதல்

### சூழல் மாறிகள் ஏற்றப்படவில்லை

**அறிகுறிகள்:**
- ஸ்கிரிப்ட்கள் தவறான மாடல்களை பயன்படுத்துகின்றன
- இணைப்பு பிழைகள்
- மாறிகள் அடையாளம் காணப்படவில்லை

**தீர்வுகள்:**
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

### சேவை இணைப்பு சிக்கல்கள்

**அறிகுறிகள்:**
- "இணைப்பு மறுக்கப்பட்டது" பிழைகள்
- "சேவை கிடைக்கவில்லை"
- நேரம் முடிந்த பிழைகள்

**தீர்வுகள்:**
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

### மாடல் கிடைக்கவில்லை

**அறிகுறிகள்:**
- "மாடல் கிடைக்கவில்லை" பிழைகள்
- "அலியாஸ் அடையாளம் காணப்படவில்லை"

**தீர்வுகள்:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### இறக்குமதி பிழைகள்

**அறிகுறிகள்:**
- "மொடியூல் கிடைக்கவில்லை" பிழைகள்

**தீர்வுகள்:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## கட்டமைப்பை சோதித்தல்

### சூழல் ஏற்றலை சரிபார்க்கவும்

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

### Foundry Local இணைப்பை சோதிக்கவும்

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

## பாதுகாப்பு சிறந்த நடைமுறைகள்

### 1. ரகசியங்களை ஒருபோதும் ஒப்படைக்க வேண்டாம்

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. தனித்துவமான .env கோப்புகளை பயன்படுத்தவும்

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API விசைகளை மாற்றவும்

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. சூழல்-சிறப்பு அமைப்பை பயன்படுத்தவும்

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK ஆவணங்கள்

- **முக்கிய களஞ்சியம்**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ஆவணங்கள்**: சமீபத்திய தகவலுக்கு SDK களஞ்சியத்தை சரிபார்க்கவும்

## கூடுதல் வளங்கள்

- `QUICK_START.md` - தொடக்க வழிகாட்டி
- `SDK_MIGRATION_NOTES.md` - SDK புதுப்பிப்பு விவரங்கள்
- `Workshop/samples/*/README.md` - மாதிரி-சிறப்பு வழிகாட்டிகள்

---

**கடைசியாக புதுப்பிக்கப்பட்டது**: 2025-01-08  
**பதிப்பு**: 2.0  
**SDK**: Foundry Local Python SDK (சமீபத்திய)

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.