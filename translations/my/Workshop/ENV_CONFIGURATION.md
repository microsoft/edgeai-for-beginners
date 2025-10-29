<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:35:06+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "my"
}
-->
# ပတ်ဝန်းကျင်ဖွဲ့စည်းမှုလမ်းညွှန်

## အကျဉ်းချုပ်

Workshop နမူနာများသည် `.env` ဖိုင်တွင် စုစည်းထားသော ပတ်ဝန်းကျင်အပြောင်းအလဲများကို အသုံးပြုသည်။ ၎င်းသည် ကုဒ်ကို ပြင်ဆင်ရန်မလိုဘဲ လွယ်ကူစွာစိတ်ကြိုက်ပြင်ဆင်နိုင်စေသည်။

## အမြန်စတင်ခြင်း

### 1. လိုအပ်ချက်များကို စစ်ဆေးပါ

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. ပတ်ဝန်းကျင်ကို ဖွဲ့စည်းပါ

`.env` ဖိုင်ကို အဆင်ပြေသော ပုံစံများဖြင့် ရှိပြီးသားဖြစ်သည်။ အသုံးပြုသူအများစုသည် ဘာမှ ပြောင်းလဲရန်မလိုအပ်ပါ။

**အလိုအလျောက်**: ဆက်တင်များကို ပြန်လည်သုံးသပ်ပြီး စိတ်ကြိုက်ပြင်ဆင်ပါ:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. ဖွဲ့စည်းမှုကို အသုံးပြုပါ

**Python Scripts အတွက်:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Notebooks အတွက်:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ရည်ညွှန်းခြင်း

### အဓိကဖွဲ့စည်းမှု

| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | နမူနာများအတွက် ပုံမှန်မော်ဒယ် |
| `FOUNDRY_LOCAL_ENDPOINT` | (အလွတ်) | ဝန်ဆောင်မှု endpoint ကို ပြောင်းလဲရန် |
| `PYTHONPATH` | Workshop လမ်းကြောင်းများ | Python module ရှာဖွေမှုလမ်းကြောင်း |

**FOUNDRY_LOCAL_ENDPOINT ကို သတ်မှတ်ရန်အချိန်:**
- Remote Foundry Local instance
- Custom port configuration
- Development/production ခွဲခြားမှု

**ဥပမာ:**
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
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding မော်ဒယ် |
| `RAG_QUESTION` | Pre-configured | စမ်းသပ်မေးခွန်း |

#### Session 03: Benchmarking
| Variable | Default | Purpose |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Benchmark ပြုလုပ်ရန် မော်ဒယ်များ |
| `BENCH_ROUNDS` | `3` | မော်ဒယ်တစ်ခုစီအတွက် iteration အရေအတွက် |
| `BENCH_PROMPT` | Pre-configured | စမ်းသပ် prompt |
| `BENCH_STREAM` | `0` | ပထမဆုံး token latency ကို တိုင်းတာရန် |

#### Session 04: Model Comparison
| Variable | Default | Purpose |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | သေးငယ်သော ဘာသာစကားမော်ဒယ် |
| `LLM_ALIAS` | `qwen2.5-7b` | ကြီးမားသော ဘာသာစကားမော်ဒယ် |
| `COMPARE_PROMPT` | Pre-configured | နှိုင်းယှဉ်မှု prompt |
| `COMPARE_RETRIES` | `2` | ပြန်လည်ကြိုးစားမှုအကြိမ်ရေ |

#### Session 05: Multi-Agent Orchestration
| Variable | Default | Purpose |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | သုတေသနအေးဂျင့်မော်ဒယ် |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | အယ်ဒီတာအေးဂျင့်မော်ဒယ် |
| `AGENT_QUESTION` | Pre-configured | စမ်းသပ်မေးခွန်း |

### ယုံကြည်စိတ်ချမှုဖွဲ့စည်းမှု

| Variable | Default | Purpose |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Token အသုံးပြုမှုကို ပုံနှိပ်ရန် |
| `RETRY_ON_FAIL` | `1` | ပြန်လည်ကြိုးစားမှု logic ကို ဖွင့်ရန် |
| `RETRY_BACKOFF` | `1.0` | ပြန်လည်ကြိုးစားမှုအချိန်နှောင့်နှေးမှု (စက္ကန့်) |

## ပုံမှန်ဖွဲ့စည်းမှုများ

### Development Setup (အမြန် iteration)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Production Setup (အရည်အသွေးအာရုံစိုက်မှု)
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

## အကြံပြုမော်ဒယ်များ

### အသုံးပြုမှုအလိုက်

**အထွေထွေသုံးအတွက်:**
- `phi-4-mini` - အရည်အသွေးနှင့် အမြန်နှုန်းကို ညှိထားသည်

**အမြန်တုံ့ပြန်မှုအတွက်:**
- `qwen2.5-0.5b` - အလွန်မြန်ပြီး အမျိုးအစားခွဲခြားမှုအတွက်ကောင်းသည်
- `phi-4-mini` - အရည်အသွေးကောင်းပြီး မြန်ဆန်သည်

**အရည်အသွေးမြင့်မားမှုအတွက်:**
- `qwen2.5-7b` - အရည်အသွေးအကောင်းဆုံး၊ အရင်းအမြစ်အသုံးပြုမှုများ
- `phi-4-mini` - အရည်အသွေးကောင်းပြီး အရင်းအမြစ်နည်းပါး

**Code Generation အတွက်:**
- `deepseek-coder-1.3b` - Code အတွက် အထူးပြု
- `phi-4-mini` - အထွေထွေ coding

### အရင်းအမြစ်ရရှိနိုင်မှုအလိုက်

**အရင်းအမြစ်နည်း (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**အရင်းအမြစ်အလယ်အလတ် (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**အရင်းအမြစ်များ (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## အဆင့်မြင့်ဖွဲ့စည်းမှု

### Custom Endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperature & Sampling (Code တွင် Override ပြုလုပ်ရန်)

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

## ပြဿနာဖြေရှင်းခြင်း

### ပတ်ဝန်းကျင်အပြောင်းအလဲများ မတင်နိုင်ခြင်း

**လက္ခဏာများ:**
- Scripts မှ မော်ဒယ်များမှားယွင်းစွာအသုံးပြုခြင်း
- ချိတ်ဆက်မှုအမှားများ
- Variable များကို မသိရှိခြင်း

**ဖြေရှင်းနည်းများ:**
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

### ဝန်ဆောင်မှုချိတ်ဆက်မှုပြဿနာများ

**လက္ခဏာများ:**
- "Connection refused" အမှားများ
- "Service not available"
- Timeout အမှားများ

**ဖြေရှင်းနည်းများ:**
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

### မော်ဒယ်မတွေ့ရှိခြင်း

**လက္ခဏာများ:**
- "Model not found" အမှားများ
- "Alias not recognized"

**ဖြေရှင်းနည်းများ:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Import အမှားများ

**လက္ခဏာများ:**
- "Module not found" အမှားများ

**ဖြေရှင်းနည်းများ:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## ဖွဲ့စည်းမှုစမ်းသပ်ခြင်း

### ပတ်ဝန်းကျင် Loading ကို စစ်ဆေးပါ

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

### Foundry Local ချိတ်ဆက်မှုကို စမ်းသပ်ပါ

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

## လုံခြုံရေးအကောင်းဆုံးလက်တွေ့ကျမှုများ

### 1. လျှို့ဝှက်ချက်များကို မ commit လုပ်ပါနှင့်

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. သီးခြား .env ဖိုင်များကို အသုံးပြုပါ

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API Key များကို ပြန်လည်ပြောင်းလဲပါ

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. ပတ်ဝန်းကျင်အလိုက် ဖွဲ့စည်းမှုကို အသုံးပြုပါ

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK Documentation

- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentation**: SDK repository တွင် နောက်ဆုံးပေါ်ကို ကြည့်ပါ

## အပိုဆောင်းအရင်းအမြစ်များ

- `QUICK_START.md` - စတင်အသုံးပြုရန်လမ်းညွှန်
- `SDK_MIGRATION_NOTES.md` - SDK အပ်ဒိတ်အသေးစိတ်
- `Workshop/samples/*/README.md` - နမူနာအထူးပြုလမ်းညွှန်များ

---

**နောက်ဆုံးအပ်ဒိတ်**: 2025-01-08  
**ဗားရှင်း**: 2.0  
**SDK**: Foundry Local Python SDK (latest)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူသားမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။