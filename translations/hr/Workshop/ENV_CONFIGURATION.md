<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-12T00:31:47+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "hr"
}
-->
# Vodič za konfiguraciju okruženja

## Pregled

Primjeri radionice koriste varijable okruženja za konfiguraciju, centralizirane u `.env` datoteci na korijenu repozitorija. Ovo omogućuje jednostavnu prilagodbu bez izmjene koda.

## Brzi početak

### 1. Provjerite preduvjete

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurirajte okruženje

`.env` datoteka već je konfigurirana s razumnim zadanim postavkama. Većina korisnika neće trebati ništa mijenjati.

**Opcionalno**: Pregledajte i prilagodite postavke:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Primijenite konfiguraciju

**Za Python skripte:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Za bilježnice:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referenca varijabli okruženja

### Osnovna konfiguracija

| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Zadani model za primjere |
| `FOUNDRY_LOCAL_ENDPOINT` | (prazno) | Prekoračenje krajnje točke usluge |
| `PYTHONPATH` | Putovi radionice | Put za pretraživanje Python modula |

**Kada postaviti FOUNDRY_LOCAL_ENDPOINT:**
- Udaljena instanca Foundry Local
- Prilagođena konfiguracija porta
- Razdvajanje razvoja/produkcije

**Primjer:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Varijable specifične za sesiju

#### Sesija 02: RAG cjevovod
| Varijabla | Zadano | Svrha |
|-----------|--------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model za ugrađivanje |
| `RAG_QUESTION` | Predkonfigurirano | Testno pitanje |

#### Sesija 03: Benchmarking
| Varijabla | Zadano | Svrha |
|-----------|--------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeli za benchmarking |
| `BENCH_ROUNDS` | `3` | Iteracije po modelu |
| `BENCH_PROMPT` | Predkonfigurirano | Testni prompt |
| `BENCH_STREAM` | `0` | Mjerenje latencije prvog tokena |

#### Sesija 04: Usporedba modela
| Varijabla | Zadano | Svrha |
|-----------|--------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Mali jezični model |
| `LLM_ALIAS` | `qwen2.5-7b` | Veliki jezični model |
| `COMPARE_PROMPT` | Predkonfigurirano | Prompt za usporedbu |
| `COMPARE_RETRIES` | `2` | Pokušaji ponovnog pokušaja |

#### Sesija 05: Orkestracija više agenata
| Varijabla | Zadano | Svrha |
|-----------|--------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model istraživačkog agenta |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model uredničkog agenta |
| `AGENT_QUESTION` | Predkonfigurirano | Testno pitanje |

### Konfiguracija pouzdanosti

| Varijabla | Zadano | Svrha |
|-----------|--------|-------|
| `SHOW_USAGE` | `1` | Ispis potrošnje tokena |
| `RETRY_ON_FAIL` | `1` | Omogućuje logiku ponovnog pokušaja |
| `RETRY_BACKOFF` | `1.0` | Kašnjenje ponovnog pokušaja (sekunde) |

## Uobičajene konfiguracije

### Postavka za razvoj (brza iteracija)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Postavka za produkciju (fokus na kvalitetu)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Postavka za benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specijalizacija za više agenata
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Udaljeni razvoj
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Preporučeni modeli

### Prema namjeni

**Opća namjena:**
- `phi-4-mini` - Uravnotežena kvaliteta i brzina

**Brzi odgovori:**
- `qwen2.5-0.5b` - Vrlo brz, dobar za klasifikaciju
- `phi-4-mini` - Brz s dobrom kvalitetom

**Visoka kvaliteta:**
- `qwen2.5-7b` - Najbolja kvaliteta, veća potrošnja resursa
- `phi-4-mini` - Dobra kvaliteta, manja potrošnja resursa

**Generiranje koda:**
- `deepseek-coder-1.3b` - Specijaliziran za kod
- `phi-4-mini` - Opća namjena za kodiranje

### Prema dostupnosti resursa

**Mali resursi (< 8GB RAM-a):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Srednji resursi (8-16GB RAM-a):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Veliki resursi (16GB+ RAM-a):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Napredna konfiguracija

### Prilagođene krajnje točke

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura i uzorkovanje (prepisivanje u kodu)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Hibridna postavka Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Rješavanje problema

### Varijable okruženja nisu učitane

**Simptomi:**
- Skripte koriste pogrešne modele
- Pogreške povezivanja
- Varijable nisu prepoznate

**Rješenja:**
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

### Problemi s povezivanjem usluge

**Simptomi:**
- Pogreške "Connection refused"
- "Usluga nije dostupna"
- Pogreške vremenskog ograničenja

**Rješenja:**
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

### Model nije pronađen

**Simptomi:**
- Pogreške "Model nije pronađen"
- "Alias nije prepoznat"

**Rješenja:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Pogreške pri uvozu

**Simptomi:**
- Pogreške "Modul nije pronađen"

**Rješenja:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testiranje konfiguracije

### Provjera učitavanja okruženja

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

### Testiranje povezivanja s Foundry Local

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

## Najbolje prakse za sigurnost

### 1. Nikada ne dijelite tajne

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Koristite odvojene .env datoteke

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotirajte API ključeve

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Koristite konfiguraciju specifičnu za okruženje

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK dokumentacija

- **Glavni repozitorij**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Provjerite najnovije informacije u SDK repozitoriju

## Dodatni resursi

- `QUICK_START.md` - Vodič za početak
- `Workshop/samples/*/README.md` - Vodiči specifični za primjere

---

**Zadnje ažuriranje**: 2025-01-08  
**Verzija**: 2.0  
**SDK**: Foundry Local Python SDK (najnoviji)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->