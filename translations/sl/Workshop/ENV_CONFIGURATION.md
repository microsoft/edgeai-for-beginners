<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:30:05+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "sl"
}
-->
# Vodnik za konfiguracijo okolja

## Pregled

Primeri delavnice uporabljajo okoljske spremenljivke za konfiguracijo, ki so centralizirane v datoteki `.env` na korenu repozitorija. To omogoča enostavno prilagajanje brez spreminjanja kode.

## Hitri začetek

### 1. Preverite predpogoje

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurirajte okolje

Datoteka `.env` je že konfigurirana z razumnimi privzetimi nastavitvami. Večina uporabnikov ne bo potrebovala sprememb.

**Neobvezno**: Preglejte in prilagodite nastavitve:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Uporabite konfiguracijo

**Za Python skripte:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Za zvezke:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referenca okoljskih spremenljivk

### Osnovna konfiguracija

| Spremenljivka | Privzeto | Opis |
|---------------|----------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Privzeti model za primere |
| `FOUNDRY_LOCAL_ENDPOINT` | (prazno) | Preklic privzetega končnega točke storitve |
| `PYTHONPATH` | Poti delavnice | Pot iskanja Python modulov |

**Kdaj nastaviti FOUNDRY_LOCAL_ENDPOINT:**
- Oddaljena instanca Foundry Local
- Prilagojena konfiguracija vrat
- Ločitev razvoja/produkcije

**Primer:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Spremenljivke, specifične za sejo

#### Seja 02: RAG cevovod
| Spremenljivka | Privzeto | Namen |
|---------------|----------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model za vdelavo |
| `RAG_QUESTION` | Vnaprej konfigurirano | Testno vprašanje |

#### Seja 03: Primerjava zmogljivosti
| Spremenljivka | Privzeto | Namen |
|---------------|----------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeli za primerjavo |
| `BENCH_ROUNDS` | `3` | Iteracije na model |
| `BENCH_PROMPT` | Vnaprej konfigurirano | Testni poziv |
| `BENCH_STREAM` | `0` | Merjenje zakasnitve prvega žetona |

#### Seja 04: Primerjava modelov
| Spremenljivka | Privzeto | Namen |
|---------------|----------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Majhen jezikovni model |
| `LLM_ALIAS` | `qwen2.5-7b` | Velik jezikovni model |
| `COMPARE_PROMPT` | Vnaprej konfigurirano | Poziv za primerjavo |
| `COMPARE_RETRIES` | `2` | Število poskusov ponovnega zagona |

#### Seja 05: Orkestracija več agentov
| Spremenljivka | Privzeto | Namen |
|---------------|----------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model raziskovalnega agenta |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model uredniškega agenta |
| `AGENT_QUESTION` | Vnaprej konfigurirano | Testno vprašanje |

### Konfiguracija zanesljivosti

| Spremenljivka | Privzeto | Namen |
|---------------|----------|-------|
| `SHOW_USAGE` | `1` | Prikaz uporabe žetonov |
| `RETRY_ON_FAIL` | `1` | Omogoči logiko ponovnega poskusa |
| `RETRY_BACKOFF` | `1.0` | Zakasnitev ponovnega poskusa (sekunde) |

## Pogoste konfiguracije

### Razvojna nastavitev (hitre iteracije)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produkcijska nastavitev (osredotočenost na kakovost)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Nastavitev za primerjavo zmogljivosti
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specializacija več agentov
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Oddaljeni razvoj
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Priporočeni modeli

### Po namenu uporabe

**Splošna uporaba:**
- `phi-4-mini` - Uravnotežena kakovost in hitrost

**Hitri odzivi:**
- `qwen2.5-0.5b` - Zelo hiter, dober za klasifikacijo
- `phi-4-mini` - Hiter z dobro kakovostjo

**Visoka kakovost:**
- `qwen2.5-7b` - Najboljša kakovost, večja poraba virov
- `phi-4-mini` - Dobra kakovost, manjša poraba virov

**Generiranje kode:**
- `deepseek-coder-1.3b` - Specializiran za kodo
- `phi-4-mini` - Splošna uporaba za kodiranje

### Po razpoložljivosti virov

**Nizki viri (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Srednji viri (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Visoki viri (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Napredna konfiguracija

### Prilagojene končne točke

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura in vzorčenje (preklic v kodi)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Hibridna nastavitev Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Odpravljanje težav

### Okoljske spremenljivke niso naložene

**Simptomi:**
- Skripte uporabljajo napačne modele
- Napake pri povezovanju
- Spremenljivke niso prepoznane

**Rešitve:**
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

### Težave s povezavo storitve

**Simptomi:**
- Napake "Povezava zavrnjena"
- "Storitev ni na voljo"
- Napake časovne omejitve

**Rešitve:**
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

### Model ni najden

**Simptomi:**
- Napake "Model ni najden"
- "Alias ni prepoznan"

**Rešitve:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Napake pri uvozu

**Simptomi:**
- Napake "Modul ni najden"

**Rešitve:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testiranje konfiguracije

### Preverite nalaganje okolja

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

### Testirajte povezavo Foundry Local

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

## Najboljše prakse za varnost

### 1. Nikoli ne shranjujte občutljivih podatkov

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Uporabljajte ločene `.env` datoteke

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Redno menjajte API ključe

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Uporabljajte konfiguracijo, specifično za okolje

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentacija SDK

- **Glavni repozitorij**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Preverite repozitorij SDK za najnovejše informacije

## Dodatni viri

- `QUICK_START.md` - Vodnik za začetek
- `SDK_MIGRATION_NOTES.md` - Podrobnosti o posodobitvi SDK
- `Workshop/samples/*/README.md` - Vodniki, specifični za primere

---

**Zadnja posodobitev**: 2025-01-08  
**Različica**: 2.0  
**SDK**: Foundry Local Python SDK (najnovejši)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.