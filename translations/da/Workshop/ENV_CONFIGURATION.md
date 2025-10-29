<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:08:10+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "da"
}
-->
# Guide til miljøkonfiguration

## Oversigt

Workshop-eksemplerne bruger miljøvariabler til konfiguration, som er centraliseret i `.env`-filen i roden af repositoryet. Dette gør det nemt at tilpasse uden at ændre koden.

## Hurtig start

### 1. Bekræft forudsætninger

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurer miljøet

`.env`-filen er allerede konfigureret med fornuftige standardindstillinger. De fleste brugere behøver ikke at ændre noget.

**Valgfrit**: Gennemgå og tilpas indstillinger:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Anvend konfigurationen

**For Python-scripts:**
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

## Reference for miljøvariabler

### Grundlæggende konfiguration

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Standardmodel for eksempler |
| `FOUNDRY_LOCAL_ENDPOINT` | (tom) | Overstyr service-endpoint |
| `PYTHONPATH` | Workshop-stier | Søgesti for Python-moduler |

**Hvornår skal FOUNDRY_LOCAL_ENDPOINT sættes:**
- Fjern Foundry Local-instans
- Tilpasset portkonfiguration
- Adskillelse af udvikling/produktion

**Eksempel:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Sessionsspecifikke variabler

#### Session 02: RAG Pipeline
| Variabel | Standard | Formål |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding-model |
| `RAG_QUESTION` | Forudkonfigureret | Testspørgsmål |

#### Session 03: Benchmarking
| Variabel | Standard | Formål |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeller til benchmarking |
| `BENCH_ROUNDS` | `3` | Iterationer pr. model |
| `BENCH_PROMPT` | Forudkonfigureret | Testprompt |
| `BENCH_STREAM` | `0` | Måling af første-token latenstid |

#### Session 04: Model sammenligning
| Variabel | Standard | Formål |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Lille sprogmodel |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor sprogmodel |
| `COMPARE_PROMPT` | Forudkonfigureret | Sammenligningsprompt |
| `COMPARE_RETRIES` | `2` | Forsøg på genprøvning |

#### Session 05: Multi-agent orkestrering
| Variabel | Standard | Formål |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Forsker-agent model |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Redaktør-agent model |
| `AGENT_QUESTION` | Forudkonfigureret | Testspørgsmål |

### Konfiguration for pålidelighed

| Variabel | Standard | Formål |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Udskriv tokenforbrug |
| `RETRY_ON_FAIL` | `1` | Aktiver genprøvningslogik |
| `RETRY_BACKOFF` | `1.0` | Forsinkelse ved genprøvning (sekunder) |

## Almindelige konfigurationer

### Udviklingsopsætning (hurtig iteration)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produktionsopsætning (fokus på kvalitet)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking opsætning
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specialisering af multi-agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Fjernudvikling
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Anbefalede modeller

### Efter anvendelsesområde

**Generelt formål:**
- `phi-4-mini` - Balanceret kvalitet og hastighed

**Hurtige svar:**
- `qwen2.5-0.5b` - Meget hurtig, god til klassifikation
- `phi-4-mini` - Hurtig med god kvalitet

**Høj kvalitet:**
- `qwen2.5-7b` - Bedste kvalitet, højere ressourceforbrug
- `phi-4-mini` - God kvalitet, lavere ressourcer

**Kodegenerering:**
- `deepseek-coder-1.3b` - Specialiseret til kode
- `phi-4-mini` - Generelt formål for kodning

### Efter ressource tilgængelighed

**Lave ressourcer (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Mellem ressourcer (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Høje ressourcer (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Avanceret konfiguration

### Tilpassede endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatur & sampling (overstyr i kode)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI hybrid opsætning

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Fejlfinding

### Miljøvariabler ikke indlæst

**Symptomer:**
- Scripts bruger forkerte modeller
- Forbindelsesfejl
- Variabler ikke genkendt

**Løsninger:**
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

### Problemer med serviceforbindelse

**Symptomer:**
- "Connection refused" fejl
- "Service ikke tilgængelig"
- Timeout fejl

**Løsninger:**
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

### Model ikke fundet

**Symptomer:**
- "Model ikke fundet" fejl
- "Alias ikke genkendt"

**Løsninger:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importfejl

**Symptomer:**
- "Modul ikke fundet" fejl

**Løsninger:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Test af konfiguration

### Bekræft indlæsning af miljø

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

### Test Foundry Local-forbindelse

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

## Sikkerhedspraksis

### 1. Aldrig commit hemmeligheder

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Brug separate .env-filer

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Roter API-nøgler

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Brug miljøspecifik konfiguration

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK-dokumentation

- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentation**: Se SDK-repository for seneste

## Yderligere ressourcer

- `QUICK_START.md` - Kom godt i gang guide
- `SDK_MIGRATION_NOTES.md` - Detaljer om SDK-opdatering
- `Workshop/samples/*/README.md` - Guides specifikt for eksempler

---

**Sidst opdateret**: 2025-01-08  
**Version**: 2.0  
**SDK**: Foundry Local Python SDK (seneste)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.