<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-12T01:01:48+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "et"
}
-->
# Keskkonna seadistamise juhend

## Ülevaade

Töötoa näidised kasutavad konfiguratsiooniks keskkonnamuutujaid, mis on koondatud `.env` faili hoidla juurkausta. See võimaldab lihtsat kohandamist ilma koodi muutmata.

## Kiire alustamine

### 1. Kontrolli eeldusi

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Seadista keskkond

`.env` fail on juba seadistatud mõistlike vaikeseadetega. Enamik kasutajaid ei pea midagi muutma.

**Valikuline**: Vaata üle ja kohanda seadeid:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Rakenda konfiguratsioon

**Python skriptide jaoks:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Notebookide jaoks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Keskkonnamuutujate viide

### Põhikonfiguratsioon

| Muutuja | Vaikeseade | Kirjeldus |
|---------|------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Vaikemudel näidiste jaoks |
| `FOUNDRY_LOCAL_ENDPOINT` | (tühi) | Teenuse lõpp-punkti ülekirjutamine |
| `PYTHONPATH` | Töötoa teed | Python moodulite otsingutee |

**Millal seadistada FOUNDRY_LOCAL_ENDPOINT:**
- Kaug-Fondry Local instants
- Kohandatud pordi konfiguratsioon
- Arendus-/tootmiskeskkonna eristamine

**Näide:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Sessioonipõhised muutujad

#### Sessioon 02: RAG torujuhe
| Muutuja | Vaikeseade | Eesmärk |
|---------|------------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding mudel |
| `RAG_QUESTION` | Eelseadistatud | Testküsimus |

#### Sessioon 03: Võrdlusuuring
| Muutuja | Vaikeseade | Eesmärk |
|---------|------------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Mudelid võrdlemiseks |
| `BENCH_ROUNDS` | `3` | Iteratsioonid mudeli kohta |
| `BENCH_PROMPT` | Eelseadistatud | Testkäsk |
| `BENCH_STREAM` | `0` | Esimese märgi latentsuse mõõtmine |

#### Sessioon 04: Mudelite võrdlus
| Muutuja | Vaikeseade | Eesmärk |
|---------|------------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Väike keelemudel |
| `LLM_ALIAS` | `qwen2.5-7b` | Suur keelemudel |
| `COMPARE_PROMPT` | Eelseadistatud | Võrdluskäsk |
| `COMPARE_RETRIES` | `2` | Uuesti proovimise katsed |

#### Sessioon 05: Multi-agent orkestreerimine
| Muutuja | Vaikeseade | Eesmärk |
|---------|------------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Teaduri agendi mudel |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Toimetaja agendi mudel |
| `AGENT_QUESTION` | Eelseadistatud | Testküsimus |

### Usaldusväärsuse konfiguratsioon

| Muutuja | Vaikeseade | Eesmärk |
|---------|------------|---------|
| `SHOW_USAGE` | `1` | Prindi tokenite kasutus |
| `RETRY_ON_FAIL` | `1` | Luba uuesti proovimise loogika |
| `RETRY_BACKOFF` | `1.0` | Uuesti proovimise viivitus (sekundites) |

## Tavalised konfiguratsioonid

### Arenduskeskkond (kiire iteratsioon)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Tootmiskeskkond (kvaliteedi fookus)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Võrdlusuuringu seadistus
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Multi-agent spetsialiseerumine
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Kaug-arendus
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Soovitatud mudelid

### Kasutuse järgi

**Üldotstarbeline:**
- `phi-4-mini` - Tasakaalustatud kvaliteet ja kiirus

**Kiired vastused:**
- `qwen2.5-0.5b` - Väga kiire, sobib klassifitseerimiseks
- `phi-4-mini` - Kiire ja hea kvaliteediga

**Kõrge kvaliteet:**
- `qwen2.5-7b` - Parim kvaliteet, suurem ressursikasutus
- `phi-4-mini` - Hea kvaliteet, madalam ressursikasutus

**Koodi genereerimine:**
- `deepseek-coder-1.3b` - Spetsialiseerunud koodile
- `phi-4-mini` - Üldotstarbeline koodimine

### Ressursside kättesaadavuse järgi

**Väikesed ressursid (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Keskmised ressursid (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Suured ressursid (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Täpsem konfiguratsioon

### Kohandatud lõpp-punktid

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatuur ja proovivõtmine (ülekirjutamine koodis)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI hübriidseadistus

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Tõrkeotsing

### Keskkonnamuutujad ei laetud

**Sümptomid:**
- Skriptid kasutavad valesid mudeleid
- Ühenduse vead
- Muutujaid ei tunnistata

**Lahendused:**
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

### Teenuse ühenduse probleemid

**Sümptomid:**
- "Ühendus keelatud" vead
- "Teenust pole saadaval"
- Aegumise vead

**Lahendused:**
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

### Mudelit ei leitud

**Sümptomid:**
- "Mudel ei leitud" vead
- "Alias ei tunnistatud"

**Lahendused:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importimise vead

**Sümptomid:**
- "Moodulit ei leitud" vead

**Lahendused:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Konfiguratsiooni testimine

### Kontrolli keskkonna laadimist

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

### Testi Foundry Local ühendust

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

## Turvalisuse parimad tavad

### 1. Ära kunagi salvesta saladusi

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Kasuta eraldi .env faile

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Pööra API võtmeid

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Kasuta keskkonnaspetsiifilist konfiguratsiooni

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK dokumentatsioon

- **Peamine hoidla**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentatsioon**: Vaata SDK hoidlat uusima info jaoks

## Täiendavad ressursid

- `QUICK_START.md` - Alustamise juhend
- `Workshop/samples/*/README.md` - Näidiste spetsiifilised juhendid

---

**Viimati uuendatud**: 2025-01-08  
**Versioon**: 2.0  
**SDK**: Foundry Local Python SDK (uusim)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->