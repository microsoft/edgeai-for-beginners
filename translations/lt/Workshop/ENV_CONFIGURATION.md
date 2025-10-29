<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:46:12+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "lt"
}
-->
# Aplinkos konfigūravimo vadovas

## Apžvalga

Dirbtuvių pavyzdžiai naudoja aplinkos kintamuosius konfigūravimui, kurie yra centralizuoti `.env` faile, esančiame saugyklos šaknyje. Tai leidžia lengvai pritaikyti nustatymus, nekeičiant kodo.

## Greitas pradėjimas

### 1. Patikrinkite reikalavimus

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigūruokite aplinką

`.env` failas jau sukonfigūruotas su tinkamais numatytaisiais nustatymais. Daugumai vartotojų nereikės nieko keisti.

**Pasirinktinai**: Peržiūrėkite ir pritaikykite nustatymus:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Taikykite konfigūraciją

**Python scenarijams:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Užrašų knygelėms:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Aplinkos kintamųjų nuoroda

### Pagrindinė konfigūracija

| Kintamasis | Numatytasis | Aprašymas |
|------------|-------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Numatytoji modelio versija pavyzdžiams |
| `FOUNDRY_LOCAL_ENDPOINT` | (tuščias) | Paslaugos pabaigos taško pakeitimas |
| `PYTHONPATH` | Dirbtuvių keliai | Python modulių paieškos kelias |

**Kada nustatyti FOUNDRY_LOCAL_ENDPOINT:**
- Nuotolinė Foundry Local instancija
- Individualus prievado konfigūravimas
- Skirtumas tarp kūrimo/produkcijos aplinkų

**Pavyzdys:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Sesijos specifiniai kintamieji

#### Sesija 02: RAG vamzdynas
| Kintamasis | Numatytasis | Paskirtis |
|------------|-------------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Įterpimo modelis |
| `RAG_QUESTION` | Iš anksto sukonfigūruota | Testavimo klausimas |

#### Sesija 03: Testavimas
| Kintamasis | Numatytasis | Paskirtis |
|------------|-------------|-----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modeliai testavimui |
| `BENCH_ROUNDS` | `3` | Iteracijų skaičius kiekvienam modeliui |
| `BENCH_PROMPT` | Iš anksto sukonfigūruota | Testavimo užklausa |
| `BENCH_STREAM` | `0` | Pirmojo ženklo vėlavimo matavimas |

#### Sesija 04: Modelių palyginimas
| Kintamasis | Numatytasis | Paskirtis |
|------------|-------------|-----------|
| `SLM_ALIAS` | `phi-4-mini` | Mažas kalbos modelis |
| `LLM_ALIAS` | `qwen2.5-7b` | Didelis kalbos modelis |
| `COMPARE_PROMPT` | Iš anksto sukonfigūruota | Palyginimo užklausa |
| `COMPARE_RETRIES` | `2` | Bandymų skaičius |

#### Sesija 05: Daugiaveiksmė orkestracija
| Kintamasis | Numatytasis | Paskirtis |
|------------|-------------|-----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Tyrėjo agento modelis |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Redaktoriaus agento modelis |
| `AGENT_QUESTION` | Iš anksto sukonfigūruota | Testavimo klausimas |

### Patikimumo konfigūracija

| Kintamasis | Numatytasis | Paskirtis |
|------------|-------------|-----------|
| `SHOW_USAGE` | `1` | Spausdinti ženklo naudojimą |
| `RETRY_ON_FAIL` | `1` | Įjungti bandymo logiką |
| `RETRY_BACKOFF` | `1.0` | Bandymo vėlavimas (sekundėmis) |

## Dažnos konfigūracijos

### Kūrimo aplinka (greitas iteravimas)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produkcijos aplinka (kokybės prioritetas)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Testavimo aplinka
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Daugiaveiksmė specializacija
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Nuotolinis kūrimas
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Rekomenduojami modeliai

### Pagal naudojimo atvejį

**Bendras naudojimas:**
- `phi-4-mini` - Subalansuota kokybė ir greitis

**Greiti atsakymai:**
- `qwen2.5-0.5b` - Labai greitas, tinkamas klasifikacijai
- `phi-4-mini` - Greitas su gera kokybe

**Aukšta kokybė:**
- `qwen2.5-7b` - Geriausia kokybė, didesnis resursų naudojimas
- `phi-4-mini` - Gera kokybė, mažesnis resursų naudojimas

**Kodo generavimas:**
- `deepseek-coder-1.3b` - Specializuotas kodui
- `phi-4-mini` - Bendro naudojimo kodavimas

### Pagal resursų prieinamumą

**Maži resursai (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Vidutiniai resursai (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Dideli resursai (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Išplėstinė konfigūracija

### Individualūs pabaigos taškai

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatūra ir mėginių ėmimas (pakeisti kode)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI hibridinė konfigūracija

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Trikčių šalinimas

### Aplinkos kintamieji neįkelti

**Simptomai:**
- Scenarijai naudoja neteisingus modelius
- Ryšio klaidos
- Kintamieji neatpažįstami

**Sprendimai:**
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

### Ryšio su paslauga problemos

**Simptomai:**
- Klaidos "Ryšys atmestas"
- "Paslauga nepasiekiama"
- Laiko limitų klaidos

**Sprendimai:**
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

### Modelis nerastas

**Simptomai:**
- Klaidos "Modelis nerastas"
- "Alias nepažintas"

**Sprendimai:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importavimo klaidos

**Simptomai:**
- Klaidos "Modulis nerastas"

**Sprendimai:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Konfigūracijos testavimas

### Patikrinkite aplinkos įkėlimą

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

### Testuokite Foundry Local ryšį

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

## Saugumo geriausios praktikos

### 1. Niekada neįkelkite slaptažodžių

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Naudokite atskirus .env failus

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Reguliariai keiskite API raktus

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Naudokite aplinkai specifinę konfigūraciją

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK dokumentacija

- **Pagrindinė saugykla**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Naujausią informaciją rasite SDK saugykloje

## Papildomi ištekliai

- `QUICK_START.md` - Pradžios vadovas
- `SDK_MIGRATION_NOTES.md` - SDK atnaujinimo detalės
- `Workshop/samples/*/README.md` - Pavyzdžių specifiniai vadovai

---

**Paskutinį kartą atnaujinta**: 2025-01-08  
**Versija**: 2.0  
**SDK**: Foundry Local Python SDK (naujausia)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.