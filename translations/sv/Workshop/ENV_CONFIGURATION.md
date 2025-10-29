<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:03:41+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "sv"
}
-->
# Guide för Miljökonfiguration

## Översikt

Workshop-exemplen använder miljövariabler för konfiguration, centraliserade i `.env`-filen vid roten av repositoryn. Detta möjliggör enkel anpassning utan att ändra koden.

## Snabbstart

### 1. Kontrollera Förutsättningar

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurera Miljön

`.env`-filen är redan konfigurerad med rimliga standardinställningar. De flesta användare behöver inte ändra något.

**Valfritt**: Granska och anpassa inställningar:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Tillämpa Konfiguration

**För Python-skript:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**För Notebookar:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referens för Miljövariabler

### Grundläggande Konfiguration

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Standardmodell för exempel |
| `FOUNDRY_LOCAL_ENDPOINT` | (tom) | Åsidosätt tjänstendpoint |
| `PYTHONPATH` | Workshop-sökvägar | Sökväg för Python-moduler |

**När man ska ställa in FOUNDRY_LOCAL_ENDPOINT:**
- Fjärrinstans av Foundry Local
- Anpassad portkonfiguration
- Separering av utveckling/produktion

**Exempel:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Sessionsspecifika Variabler

#### Session 02: RAG Pipeline
| Variabel | Standard | Syfte |
|----------|---------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Inbäddningsmodell |
| `RAG_QUESTION` | Förkonfigurerad | Testfråga |

#### Session 03: Benchmarking
| Variabel | Standard | Syfte |
|----------|---------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeller att benchmarka |
| `BENCH_ROUNDS` | `3` | Iterationer per modell |
| `BENCH_PROMPT` | Förkonfigurerad | Testprompt |
| `BENCH_STREAM` | `0` | Mäta fördröjning för första token |

#### Session 04: Modelljämförelse
| Variabel | Standard | Syfte |
|----------|---------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Liten språkmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor språkmodell |
| `COMPARE_PROMPT` | Förkonfigurerad | Jämförelseprompt |
| `COMPARE_RETRIES` | `2` | Försök att köra om |

#### Session 05: Multi-Agent Orchestration
| Variabel | Standard | Syfte |
|----------|---------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Forskaragentens modell |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Redaktörsagentens modell |
| `AGENT_QUESTION` | Förkonfigurerad | Testfråga |

### Tillförlitlighetskonfiguration

| Variabel | Standard | Syfte |
|----------|---------|-------|
| `SHOW_USAGE` | `1` | Visa tokenanvändning |
| `RETRY_ON_FAIL` | `1` | Aktivera återförsökslogik |
| `RETRY_BACKOFF` | `1.0` | Fördröjning vid återförsök (sekunder) |

## Vanliga Konfigurationer

### Utvecklingsinställning (Snabba Iterationer)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produktionsinställning (Kvalitetsfokus)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking-inställning
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specialisering för Multi-Agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Fjärrutveckling
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Rekommenderade Modeller

### Beroende på Användningsområde

**Allmänt Syfte:**
- `phi-4-mini` - Balanserad kvalitet och hastighet

**Snabba Svar:**
- `qwen2.5-0.5b` - Mycket snabb, bra för klassificering
- `phi-4-mini` - Snabb med god kvalitet

**Hög Kvalitet:**
- `qwen2.5-7b` - Bästa kvalitet, högre resursanvändning
- `phi-4-mini` - Bra kvalitet, lägre resursanvändning

**Kodgenerering:**
- `deepseek-coder-1.3b` - Specialiserad för kod
- `phi-4-mini` - Allmänt syfte för kodning

### Beroende på Resurstillgång

**Låga Resurser (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Medelresurser (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Höga Resurser (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Avancerad Konfiguration

### Anpassade Endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatur & Sampling (Åsidosätt i Kod)

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

## Felsökning

### Miljövariabler Laddas Inte

**Symptom:**
- Skript använder fel modeller
- Anslutningsfel
- Variabler känns inte igen

**Lösningar:**
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

### Problem med Tjänsteanslutning

**Symptom:**
- Felmeddelanden "Connection refused"
- "Tjänsten är inte tillgänglig"
- Timeout-fel

**Lösningar:**
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

### Modell Saknas

**Symptom:**
- Felmeddelanden "Modell saknas"
- "Alias känns inte igen"

**Lösningar:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importfel

**Symptom:**
- Felmeddelanden "Modul saknas"

**Lösningar:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testa Konfiguration

### Kontrollera Miljöladdning

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

### Testa Foundry Local-anslutning

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

## Säkerhetsbästa Praxis

### 1. Lämna Aldrig Ut Hemligheter

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Använd Separata .env-filer

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotera API-nycklar

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Använd Miljöspecifik Konfiguration

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK Dokumentation

- **Huvudrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentation**: Se SDK-repositoryn för senaste versionen

## Ytterligare Resurser

- `QUICK_START.md` - Kom igång-guide
- `SDK_MIGRATION_NOTES.md` - Detaljer om SDK-uppdateringar
- `Workshop/samples/*/README.md` - Exempelspecifika guider

---

**Senast Uppdaterad**: 2025-01-08  
**Version**: 2.0  
**SDK**: Foundry Local Python SDK (senaste)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.