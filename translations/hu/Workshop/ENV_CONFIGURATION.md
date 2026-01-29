# Környezet Konfigurációs Útmutató

## Áttekintés

A Workshop minták környezeti változókat használnak a konfigurációhoz, amelyek központilag a `.env` fájlban találhatók a repozitórium gyökerében. Ez lehetővé teszi az egyszerű testreszabást a kód módosítása nélkül.

## Gyors kezdés

### 1. Ellenőrizze az előfeltételeket

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Környezet konfigurálása

A `.env` fájl már ésszerű alapértelmezésekkel van konfigurálva. A legtöbb felhasználónak nem kell semmit módosítania.

**Opcionális**: Tekintse át és testreszabja a beállításokat:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Konfiguráció alkalmazása

**Python szkriptekhez:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Notebookokhoz:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Környezeti változók referenciája

### Alapvető konfiguráció

| Változó | Alapértelmezett | Leírás |
|---------|-----------------|--------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Alapértelmezett modell a mintákhoz |
| `FOUNDRY_LOCAL_ENDPOINT` | (üres) | Szolgáltatási végpont felülírása |
| `PYTHONPATH` | Workshop útvonalak | Python modul keresési útvonal |

**Mikor állítsa be a FOUNDRY_LOCAL_ENDPOINT értékét:**
- Távoli Foundry Local példány
- Egyedi port konfiguráció
- Fejlesztés/gyártás szétválasztása

**Példa:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Munkamenet-specifikus változók

#### Munkamenet 02: RAG Pipeline
| Változó | Alapértelmezett | Cél |
|---------|-----------------|-----|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Beágyazási modell |
| `RAG_QUESTION` | Előre konfigurált | Tesztkérdés |

#### Munkamenet 03: Teljesítménytesztelés
| Változó | Alapértelmezett | Cél |
|---------|-----------------|-----|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Tesztelendő modellek |
| `BENCH_ROUNDS` | `3` | Iterációk modellenként |
| `BENCH_PROMPT` | Előre konfigurált | Teszt prompt |
| `BENCH_STREAM` | `0` | Első token késleltetés mérése |

#### Munkamenet 04: Modell összehasonlítás
| Változó | Alapértelmezett | Cél |
|---------|-----------------|-----|
| `SLM_ALIAS` | `phi-4-mini` | Kis nyelvi modell |
| `LLM_ALIAS` | `qwen2.5-7b` | Nagy nyelvi modell |
| `COMPARE_PROMPT` | Előre konfigurált | Összehasonlító prompt |
| `COMPARE_RETRIES` | `2` | Újrapróbálkozások száma |

#### Munkamenet 05: Többügynökös Orkesztráció
| Változó | Alapértelmezett | Cél |
|---------|-----------------|-----|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Kutató ügynök modell |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Szerkesztő ügynök modell |
| `AGENT_QUESTION` | Előre konfigurált | Tesztkérdés |

### Megbízhatósági konfiguráció

| Változó | Alapértelmezett | Cél |
|---------|-----------------|-----|
| `SHOW_USAGE` | `1` | Tokenhasználat megjelenítése |
| `RETRY_ON_FAIL` | `1` | Újrapróbálkozási logika engedélyezése |
| `RETRY_BACKOFF` | `1.0` | Újrapróbálkozási késleltetés (másodperc) |

## Gyakori konfigurációk

### Fejlesztési beállítás (Gyors iteráció)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Gyártási beállítás (Minőségi fókusz)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Teljesítménytesztelési beállítás
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Többügynökös specializáció
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Távoli fejlesztés
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Ajánlott modellek

### Felhasználási esetek szerint

**Általános célú:**
- `phi-4-mini` - Kiegyensúlyozott minőség és sebesség

**Gyors válaszok:**
- `qwen2.5-0.5b` - Nagyon gyors, jó osztályozáshoz
- `phi-4-mini` - Gyors, jó minőséggel

**Magas minőség:**
- `qwen2.5-7b` - Legjobb minőség, magasabb erőforrásigény
- `phi-4-mini` - Jó minőség, alacsonyabb erőforrásigény

**Kódgenerálás:**
- `deepseek-coder-1.3b` - Kódra specializált
- `phi-4-mini` - Általános célú kódolás

### Erőforrás elérhetőség szerint

**Alacsony erőforrás (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Közepes erőforrás (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Magas erőforrás (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Haladó konfiguráció

### Egyedi végpontok

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Hőmérséklet és mintavétel (Felülírás kódban)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI hibrid beállítás

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Hibakeresés

### Környezeti változók nem töltődnek be

**Tünetek:**
- A szkriptek rossz modelleket használnak
- Kapcsolódási hibák
- Nem felismert változók

**Megoldások:**
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

### Szolgáltatási kapcsolódási problémák

**Tünetek:**
- "Kapcsolat megtagadva" hibák
- "Szolgáltatás nem elérhető"
- Időtúllépési hibák

**Megoldások:**
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

### Modell nem található

**Tünetek:**
- "Modell nem található" hibák
- "Alias nem ismert"

**Megoldások:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importálási hibák

**Tünetek:**
- "Modul nem található" hibák

**Megoldások:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Konfiguráció tesztelése

### Környezet betöltésének ellenőrzése

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

### Foundry Local kapcsolat tesztelése

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

## Biztonsági legjobb gyakorlatok

### 1. Soha ne kövessen el titkokat

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Használjon külön `.env` fájlokat

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API kulcsok rotálása

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Környezet-specifikus konfiguráció használata

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK Dokumentáció

- **Fő repozitórium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentáció**: A legfrissebb információkért nézze meg az SDK repozitóriumot

## További források

- `QUICK_START.md` - Kezdő útmutató
- `Workshop/samples/*/README.md` - Minta-specifikus útmutatók

---

**Utolsó frissítés**: 2025-01-08  
**Verzió**: 2.0  
**SDK**: Foundry Local Python SDK (legfrissebb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->