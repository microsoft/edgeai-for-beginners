<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:59:53+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "cs"
}
-->
# Průvodce konfigurací prostředí

## Přehled

Ukázky Workshopu používají pro konfiguraci proměnné prostředí, které jsou centralizovány v souboru `.env` v kořenovém adresáři repozitáře. To umožňuje snadné přizpůsobení bez úprav kódu.

## Rychlý start

### 1. Ověřte požadavky

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurace prostředí

Soubor `.env` je již nastaven s rozumnými výchozími hodnotami. Většina uživatelů nebude muset nic měnit.

**Volitelné**: Zkontrolujte a přizpůsobte nastavení:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Použití konfigurace

**Pro Python skripty:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Pro notebooky:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referenční proměnné prostředí

### Základní konfigurace

| Proměnná | Výchozí hodnota | Popis |
|----------|-----------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Výchozí model pro ukázky |
| `FOUNDRY_LOCAL_ENDPOINT` | (prázdné) | Přepsání koncového bodu služby |
| `PYTHONPATH` | Cesty Workshopu | Cesta pro vyhledávání Python modulů |

**Kdy nastavit FOUNDRY_LOCAL_ENDPOINT:**
- Vzdálená instance Foundry Local
- Vlastní konfigurace portu
- Oddělení vývoje/produkce

**Příklad:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Proměnné specifické pro relaci

#### Relace 02: RAG Pipeline
| Proměnná | Výchozí hodnota | Účel |
|----------|-----------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model pro vkládání |
| `RAG_QUESTION` | Přednastaveno | Testovací otázka |

#### Relace 03: Benchmarking
| Proměnná | Výchozí hodnota | Účel |
|----------|-----------------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modely pro benchmarking |
| `BENCH_ROUNDS` | `3` | Počet iterací na model |
| `BENCH_PROMPT` | Přednastaveno | Testovací prompt |
| `BENCH_STREAM` | `0` | Měření latence prvního tokenu |

#### Relace 04: Porovnání modelů
| Proměnná | Výchozí hodnota | Účel |
|----------|-----------------|------|
| `SLM_ALIAS` | `phi-4-mini` | Malý jazykový model |
| `LLM_ALIAS` | `qwen2.5-7b` | Velký jazykový model |
| `COMPARE_PROMPT` | Přednastaveno | Prompt pro porovnání |
| `COMPARE_RETRIES` | `2` | Počet pokusů o opakování |

#### Relace 05: Orchestrace více agentů
| Proměnná | Výchozí hodnota | Účel |
|----------|-----------------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model výzkumného agenta |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model editačního agenta |
| `AGENT_QUESTION` | Přednastaveno | Testovací otázka |

### Konfigurace spolehlivosti

| Proměnná | Výchozí hodnota | Účel |
|----------|-----------------|------|
| `SHOW_USAGE` | `1` | Tisknout využití tokenů |
| `RETRY_ON_FAIL` | `1` | Povolit logiku opakování |
| `RETRY_BACKOFF` | `1.0` | Zpoždění opakování (v sekundách) |

## Běžné konfigurace

### Nastavení pro vývoj (rychlá iterace)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Nastavení pro produkci (důraz na kvalitu)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Nastavení pro benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specializace více agentů
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Vzdálený vývoj
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Doporučené modely

### Podle použití

**Obecné účely:**
- `phi-4-mini` - Vyvážená kvalita a rychlost

**Rychlé odpovědi:**
- `qwen2.5-0.5b` - Velmi rychlý, vhodný pro klasifikaci
- `phi-4-mini` - Rychlý s dobrou kvalitou

**Vysoká kvalita:**
- `qwen2.5-7b` - Nejlepší kvalita, vyšší nároky na zdroje
- `phi-4-mini` - Dobrá kvalita, nižší nároky na zdroje

**Generování kódu:**
- `deepseek-coder-1.3b` - Specializovaný na kód
- `phi-4-mini` - Obecné účely pro kódování

### Podle dostupnosti zdrojů

**Nízké zdroje (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Střední zdroje (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Vysoké zdroje (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Pokročilá konfigurace

### Vlastní koncové body

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Teplota a vzorkování (přepsání v kódu)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Hybridní nastavení Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Řešení problémů

### Proměnné prostředí nejsou načteny

**Příznaky:**
- Skripty používají nesprávné modely
- Chyby připojení
- Proměnné nejsou rozpoznány

**Řešení:**
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

### Problémy s připojením ke službě

**Příznaky:**
- Chyby "Connection refused"
- "Služba není dostupná"
- Chyby časového limitu

**Řešení:**
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

### Model nebyl nalezen

**Příznaky:**
- Chyby "Model nebyl nalezen"
- "Alias nebyl rozpoznán"

**Řešení:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Chyby importu

**Příznaky:**
- Chyby "Modul nebyl nalezen"

**Řešení:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testování konfigurace

### Ověření načítání prostředí

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

### Test připojení Foundry Local

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

## Nejlepší bezpečnostní postupy

### 1. Nikdy neukládejte tajné informace

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Používejte oddělené soubory .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Pravidelně měňte API klíče

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Používejte konfiguraci specifickou pro prostředí

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentace SDK

- **Hlavní repozitář**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentace API**: Podívejte se na repozitář SDK pro nejnovější informace

## Další zdroje

- `QUICK_START.md` - Průvodce začátkem
- `SDK_MIGRATION_NOTES.md` - Podrobnosti o aktualizaci SDK
- `Workshop/samples/*/README.md` - Průvodce specifický pro ukázky

---

**Poslední aktualizace**: 2025-01-08  
**Verze**: 2.0  
**SDK**: Foundry Local Python SDK (nejnovější)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.