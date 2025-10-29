<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:12:33+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "no"
}
-->
# Veiledning for Miljøkonfigurasjon

## Oversikt

Workshop-eksemplene bruker miljøvariabler for konfigurasjon, sentralisert i `.env`-filen i rotmappen til depotet. Dette gjør det enkelt å tilpasse uten å endre koden.

## Kom i gang raskt

### 1. Bekreft forutsetninger

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurer miljøet

`.env`-filen er allerede konfigurert med fornuftige standardverdier. De fleste brukere trenger ikke å endre noe.

**Valgfritt**: Gå gjennom og tilpass innstillingene:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Bruk konfigurasjonen

**For Python-skript:**
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

## Referanse for miljøvariabler

### Kjernekonfigurasjon

| Variabel | Standard | Beskrivelse |
|----------|----------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Standardmodell for eksempler |
| `FOUNDRY_LOCAL_ENDPOINT` | (tom) | Overstyr tjenesteendepunkt |
| `PYTHONPATH` | Workshop-stier | Søkesti for Python-moduler |

**Når du bør sette FOUNDRY_LOCAL_ENDPOINT:**
- Fjernstyrt Foundry Local-instans
- Tilpasset portkonfigurasjon
- Skille mellom utvikling og produksjon

**Eksempel:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Øktspesifikke variabler

#### Økt 02: RAG Pipeline
| Variabel | Standard | Formål |
|----------|----------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embeddingsmodell |
| `RAG_QUESTION` | Forhåndskonfigurert | Testspørsmål |

#### Økt 03: Benchmarking
| Variabel | Standard | Formål |
|----------|----------|--------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeller for benchmarking |
| `BENCH_ROUNDS` | `3` | Iterasjoner per modell |
| `BENCH_PROMPT` | Forhåndskonfigurert | Testprompt |
| `BENCH_STREAM` | `0` | Måle latens for første token |

#### Økt 04: Modell-sammenligning
| Variabel | Standard | Formål |
|----------|----------|--------|
| `SLM_ALIAS` | `phi-4-mini` | Liten språkmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor språkmodell |
| `COMPARE_PROMPT` | Forhåndskonfigurert | Sammenligningsprompt |
| `COMPARE_RETRIES` | `2` | Antall forsøk på nytt |

#### Økt 05: Multi-Agent Orkestrering
| Variabel | Standard | Formål |
|----------|----------|--------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Forsker-agentmodell |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Redaktør-agentmodell |
| `AGENT_QUESTION` | Forhåndskonfigurert | Testspørsmål |

### Pålitelighetskonfigurasjon

| Variabel | Standard | Formål |
|----------|----------|--------|
| `SHOW_USAGE` | `1` | Vis tokenbruk |
| `RETRY_ON_FAIL` | `1` | Aktiver logikk for å prøve på nytt |
| `RETRY_BACKOFF` | `1.0` | Forsinkelse før nytt forsøk (sekunder) |

## Vanlige konfigurasjoner

### Utviklingsoppsett (Rask iterasjon)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produksjonsoppsett (Fokus på kvalitet)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking-oppsett
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Spesialisering for Multi-Agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Fjernutvikling
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Anbefalte modeller

### Etter bruksområde

**Generelt bruk:**
- `phi-4-mini` - Balanse mellom kvalitet og hastighet

**Raske svar:**
- `qwen2.5-0.5b` - Svært rask, god for klassifisering
- `phi-4-mini` - Rask med god kvalitet

**Høy kvalitet:**
- `qwen2.5-7b` - Beste kvalitet, høyere ressursbruk
- `phi-4-mini` - God kvalitet, lavere ressurser

**Kodegenerering:**
- `deepseek-coder-1.3b` - Spesialisert for kode
- `phi-4-mini` - Generell bruk for koding

### Etter ressurskapasitet

**Lave ressurser (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Middels ressurser (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Høye ressurser (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Avansert konfigurasjon

### Tilpassede endepunkter

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatur og sampling (Overstyr i kode)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI Hybrid-oppsett

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Feilsøking

### Miljøvariabler lastes ikke

**Symptomer:**
- Skript bruker feil modeller
- Tilkoblingsfeil
- Variabler ikke gjenkjent

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

### Tilkoblingsproblemer med tjenesten

**Symptomer:**
- Feil som "Tilkobling nektet"
- "Tjenesten er ikke tilgjengelig"
- Tidsavbruddsfeil

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

### Modell ikke funnet

**Symptomer:**
- Feil som "Modell ikke funnet"
- "Alias ikke gjenkjent"

**Løsninger:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importfeil

**Symptomer:**
- Feil som "Modul ikke funnet"

**Løsninger:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testing av konfigurasjon

### Verifiser miljølasting

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

### Test Foundry Local-tilkobling

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

## Sikkerhetspraksis

### 1. Aldri legg ut hemmeligheter

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Bruk separate .env-filer

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Roter API-nøkler

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Bruk miljøspesifikk konfigurasjon

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK-dokumentasjon

- **Hoveddepot**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentasjon**: Sjekk SDK-depotet for siste versjon

## Tilleggsressurser

- `QUICK_START.md` - Kom i gang-veiledning
- `SDK_MIGRATION_NOTES.md` - Detaljer om SDK-oppdatering
- `Workshop/samples/*/README.md` - Veiledninger for spesifikke eksempler

---

**Sist oppdatert**: 2025-01-08  
**Versjon**: 2.0  
**SDK**: Foundry Local Python SDK (siste versjon)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.