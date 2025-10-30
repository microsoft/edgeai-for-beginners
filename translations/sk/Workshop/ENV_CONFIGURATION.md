<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:04:46+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "sk"
}
-->
# Príručka konfigurácie prostredia

## Prehľad

Ukážky Workshopu používajú na konfiguráciu premenné prostredia, ktoré sú centralizované v súbore `.env` v koreňovom adresári repozitára. To umožňuje jednoduché prispôsobenie bez úprav kódu.

## Rýchly štart

### 1. Overte predpoklady

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurácia prostredia

Súbor `.env` je už prednastavený s rozumnými predvolenými hodnotami. Väčšina používateľov nebude musieť nič meniť.

**Voliteľné**: Skontrolujte a prispôsobte nastavenia:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Použite konfiguráciu

**Pre Python skripty:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Pre notebooky:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referencia premenných prostredia

### Základná konfigurácia

| Premenná | Predvolená hodnota | Popis |
|----------|--------------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Predvolený model pre ukážky |
| `FOUNDRY_LOCAL_ENDPOINT` | (prázdne) | Prepis koncového bodu služby |
| `PYTHONPATH` | Cesty Workshopu | Cesta pre vyhľadávanie Python modulov |

**Kedy nastaviť FOUNDRY_LOCAL_ENDPOINT:**
- Vzdialená inštancia Foundry Local
- Vlastná konfigurácia portu
- Oddelenie vývoja/produkcie

**Príklad:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Premenné špecifické pre reláciu

#### Relácia 02: RAG Pipeline
| Premenná | Predvolená hodnota | Účel |
|----------|--------------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model pre embedding |
| `RAG_QUESTION` | Predkonfigurované | Testovacia otázka |

#### Relácia 03: Benchmarking
| Premenná | Predvolená hodnota | Účel |
|----------|--------------------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modely na benchmarking |
| `BENCH_ROUNDS` | `3` | Počet iterácií na model |
| `BENCH_PROMPT` | Predkonfigurované | Testovací prompt |
| `BENCH_STREAM` | `0` | Meranie latencie prvého tokenu |

#### Relácia 04: Porovnanie modelov
| Premenná | Predvolená hodnota | Účel |
|----------|--------------------|------|
| `SLM_ALIAS` | `phi-4-mini` | Malý jazykový model |
| `LLM_ALIAS` | `qwen2.5-7b` | Veľký jazykový model |
| `COMPARE_PROMPT` | Predkonfigurované | Prompt na porovnanie |
| `COMPARE_RETRIES` | `2` | Počet pokusov o opakovanie |

#### Relácia 05: Orchestrácia viacerých agentov
| Premenná | Predvolená hodnota | Účel |
|----------|--------------------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model výskumného agenta |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model editora agenta |
| `AGENT_QUESTION` | Predkonfigurované | Testovacia otázka |

### Konfigurácia spoľahlivosti

| Premenná | Predvolená hodnota | Účel |
|----------|--------------------|------|
| `SHOW_USAGE` | `1` | Tlač tokenovej spotreby |
| `RETRY_ON_FAIL` | `1` | Povolenie logiky opakovania |
| `RETRY_BACKOFF` | `1.0` | Meškanie pri opakovaní (sekundy) |

## Bežné konfigurácie

### Nastavenie pre vývoj (rýchla iterácia)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Nastavenie pre produkciu (zameranie na kvalitu)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Nastavenie pre benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Špecializácia viacerých agentov
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Vzdialený vývoj
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Odporúčané modely

### Podľa použitia

**Všeobecné účely:**
- `phi-4-mini` - Vyvážená kvalita a rýchlosť

**Rýchle odpovede:**
- `qwen2.5-0.5b` - Veľmi rýchly, vhodný na klasifikáciu
- `phi-4-mini` - Rýchly s dobrou kvalitou

**Vysoká kvalita:**
- `qwen2.5-7b` - Najlepšia kvalita, vyššie nároky na zdroje
- `phi-4-mini` - Dobrá kvalita, nižšie nároky na zdroje

**Generovanie kódu:**
- `deepseek-coder-1.3b` - Špecializovaný na kód
- `phi-4-mini` - Všeobecné účely kódovania

### Podľa dostupnosti zdrojov

**Nízke zdroje (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Stredné zdroje (8-16GB RAM):**
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

## Pokročilá konfigurácia

### Vlastné koncové body

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Teplota a vzorkovanie (prepis v kóde)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Hybridné nastavenie Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Riešenie problémov

### Premenné prostredia sa nenačítali

**Príznaky:**
- Skripty používajú nesprávne modely
- Chyby pripojenia
- Premenné nie sú rozpoznané

**Riešenia:**
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

### Problémy s pripojením k službe

**Príznaky:**
- Chyby "Connection refused"
- "Služba nie je dostupná"
- Chyby časového limitu

**Riešenia:**
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

### Model nebol nájdený

**Príznaky:**
- Chyby "Model nebol nájdený"
- "Alias nebol rozpoznaný"

**Riešenia:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Chyby importu

**Príznaky:**
- Chyby "Modul nebol nájdený"

**Riešenia:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testovanie konfigurácie

### Overenie načítania prostredia

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

### Test pripojenia Foundry Local

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

## Najlepšie bezpečnostné postupy

### 1. Nikdy neukladajte tajné údaje do repozitára

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Používajte samostatné súbory .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Pravidelne rotujte API kľúče

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Používajte konfiguráciu špecifickú pre prostredie

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentácia SDK

- **Hlavný repozitár**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentácia**: Pozrite si najnovšie informácie v repozitári SDK

## Ďalšie zdroje

- `QUICK_START.md` - Príručka pre začiatok
- `SDK_MIGRATION_NOTES.md` - Detaily aktualizácie SDK
- `Workshop/samples/*/README.md` - Príručky špecifické pre ukážky

---

**Posledná aktualizácia**: 2025-01-08  
**Verzia**: 2.0  
**SDK**: Foundry Local Python SDK (najnovšia)

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.