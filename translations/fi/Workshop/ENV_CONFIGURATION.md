<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T23:25:30+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "fi"
}
-->
# Ympäristön Konfigurointiohje

## Yleiskatsaus

Workshop-esimerkit käyttävät ympäristömuuttujia konfigurointiin, jotka on keskitetty `.env`-tiedostoon arkiston juurihakemistossa. Tämä mahdollistaa helpon mukauttamisen ilman koodin muokkaamista.

## Pikakäynnistys

### 1. Varmista vaatimukset

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfiguroi ympäristö

`.env`-tiedosto on jo valmiiksi konfiguroitu järkevillä oletusasetuksilla. Useimpien käyttäjien ei tarvitse muuttaa mitään.

**Valinnainen**: Tarkista ja mukauta asetuksia:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Käytä konfiguraatiota

**Python-skripteille:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Notebooksille:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Ympäristömuuttujien viite

### Keskeinen konfiguraatio

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Oletusmalli esimerkeille |
| `FOUNDRY_LOCAL_ENDPOINT` | (tyhjä) | Ylikirjoita palvelun päätepiste |
| `PYTHONPATH` | Workshop-polut | Python-moduulien hakupolku |

**Milloin asettaa FOUNDRY_LOCAL_ENDPOINT:**
- Etäkäytössä oleva Foundry Local -instanssi
- Mukautettu porttikonfiguraatio
- Kehitys-/tuotantoerottelu

**Esimerkki:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Istuntokohtaiset muuttujat

#### Istunto 02: RAG-putkisto
| Muuttuja | Oletus | Tarkoitus |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Upotusmalli |
| `RAG_QUESTION` | Esikonfiguroitu | Testikysymys |

#### Istunto 03: Benchmarking
| Muuttuja | Oletus | Tarkoitus |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Mallit vertailuun |
| `BENCH_ROUNDS` | `3` | Iteraatiot per malli |
| `BENCH_PROMPT` | Esikonfiguroitu | Testikehotus |
| `BENCH_STREAM` | `0` | Ensimmäisen tokenin viiveen mittaus |

#### Istunto 04: Mallivertailu
| Muuttuja | Oletus | Tarkoitus |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Pieni kielimalli |
| `LLM_ALIAS` | `qwen2.5-7b` | Suuri kielimalli |
| `COMPARE_PROMPT` | Esikonfiguroitu | Vertailukehotus |
| `COMPARE_RETRIES` | `2` | Uusintayritykset |

#### Istunto 05: Moniagenttiorganisointi
| Muuttuja | Oletus | Tarkoitus |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Tutkija-agenttimalli |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Editor-agenttimalli |
| `AGENT_QUESTION` | Esikonfiguroitu | Testikysymys |

### Luotettavuuskonfiguraatio

| Muuttuja | Oletus | Tarkoitus |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Tulosta tokenien käyttö |
| `RETRY_ON_FAIL` | `1` | Ota käyttöön uusintalogiikka |
| `RETRY_BACKOFF` | `1.0` | Uusintaviive (sekunteina) |

## Yleiset konfiguraatiot

### Kehitysympäristö (Nopea iterointi)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Tuotantoympäristö (Laatupainotus)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking-asetukset
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Moniagenttien erikoistuminen
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Etäkehitys
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Suositellut mallit

### Käyttötarkoituksen mukaan

**Yleiskäyttö:**
- `phi-4-mini` - Tasapainoinen laatu ja nopeus

**Nopeat vastaukset:**
- `qwen2.5-0.5b` - Erittäin nopea, hyvä luokitteluun
- `phi-4-mini` - Nopea ja hyvä laatu

**Korkea laatu:**
- `qwen2.5-7b` - Paras laatu, suurempi resurssien käyttö
- `phi-4-mini` - Hyvä laatu, pienemmät resurssit

**Koodin generointi:**
- `deepseek-coder-1.3b` - Erikoistunut koodiin
- `phi-4-mini` - Yleiskäyttöinen koodaus

### Resurssien saatavuuden mukaan

**Vähäiset resurssit (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Keskimääräiset resurssit (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Suuret resurssit (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Edistynyt konfiguraatio

### Mukautetut päätepisteet

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Lämpötila ja näytteenotto (Ylikirjoita koodissa)

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

## Vianmääritys

### Ympäristömuuttujia ei ladattu

**Oireet:**
- Skriptit käyttävät vääriä malleja
- Yhteysvirheet
- Muuttujia ei tunnisteta

**Ratkaisut:**
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

### Palveluyhteysongelmat

**Oireet:**
- "Yhteys kielletty" -virheet
- "Palvelu ei saatavilla"
- Aikakatkaisuvirheet

**Ratkaisut:**
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

### Mallia ei löydy

**Oireet:**
- "Mallia ei löydy" -virheet
- "Alias ei tunnistettu"

**Ratkaisut:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Tuontivirheet

**Oireet:**
- "Moduulia ei löydy" -virheet

**Ratkaisut:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Konfiguraation testaus

### Varmista ympäristön lataus

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

### Testaa Foundry Local -yhteys

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

## Tietoturvan parhaat käytännöt

### 1. Älä koskaan tallenna salaisuuksia

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Käytä erillisiä .env-tiedostoja

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Vaihda API-avaimet säännöllisesti

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Käytä ympäristökohtaisia asetuksia

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK-dokumentaatio

- **Pääarkisto**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentaatio**: Tarkista SDK-arkisto uusimpia varten

## Lisäresurssit

- `QUICK_START.md` - Aloitusopas
- `Workshop/samples/*/README.md` - Esimerkkikohtaiset oppaat

---

**Viimeksi päivitetty**: 2025-01-08  
**Versio**: 2.0  
**SDK**: Foundry Local Python SDK (uusin)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->