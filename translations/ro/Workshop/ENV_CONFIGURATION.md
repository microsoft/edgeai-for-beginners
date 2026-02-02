# Ghid de Configurare a Mediului

## Prezentare Generală

Exemplele din Workshop utilizează variabile de mediu pentru configurare, centralizate în fișierul `.env` aflat la rădăcina depozitului. Acest lucru permite personalizarea ușoară fără a modifica codul.

## Start Rapid

### 1. Verifică Prerechizitele

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configurează Mediul

Fișierul `.env` este deja configurat cu valori implicite rezonabile. Majoritatea utilizatorilor nu vor trebui să schimbe nimic.

**Opțional**: Revizuiește și personalizează setările:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Aplică Configurarea

**Pentru Scripturi Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Pentru Notebook-uri:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referință pentru Variabilele de Mediu

### Configurare de Bază

| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Model implicit pentru exemple |
| `FOUNDRY_LOCAL_ENDPOINT` | (gol) | Suprascrie endpoint-ul serviciului |
| `PYTHONPATH` | Căi Workshop | Calea de căutare a modulelor Python |

**Când să setezi FOUNDRY_LOCAL_ENDPOINT:**
- Instanță Foundry Local la distanță
- Configurare port personalizată
- Separare dezvoltare/producție

**Exemplu:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variabile Specifice Sesiunii

#### Sesiunea 02: Pipeline RAG
| Variabilă | Implicit | Scop |
|-----------|----------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model de încorporare |
| `RAG_QUESTION` | Pre-configurat | Întrebare de test |

#### Sesiunea 03: Benchmarking
| Variabilă | Implicit | Scop |
|-----------|----------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modele pentru benchmarking |
| `BENCH_ROUNDS` | `3` | Iterații per model |
| `BENCH_PROMPT` | Pre-configurat | Prompt de test |
| `BENCH_STREAM` | `0` | Măsoară latența primului token |

#### Sesiunea 04: Compararea Modelului
| Variabilă | Implicit | Scop |
|-----------|----------|------|
| `SLM_ALIAS` | `phi-4-mini` | Model de limbaj mic |
| `LLM_ALIAS` | `qwen2.5-7b` | Model de limbaj mare |
| `COMPARE_PROMPT` | Pre-configurat | Prompt de comparație |
| `COMPARE_RETRIES` | `2` | Încercări de reîncercare |

#### Sesiunea 05: Orchestrare Multi-Agent
| Variabilă | Implicit | Scop |
|-----------|----------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model agent cercetător |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model agent editor |
| `AGENT_QUESTION` | Pre-configurat | Întrebare de test |

### Configurare Fiabilitate

| Variabilă | Implicit | Scop |
|-----------|----------|------|
| `SHOW_USAGE` | `1` | Afișează utilizarea token-urilor |
| `RETRY_ON_FAIL` | `1` | Activează logica de reîncercare |
| `RETRY_BACKOFF` | `1.0` | Întârziere reîncercare (secunde) |

## Configurări Comune

### Configurare pentru Dezvoltare (Iterație Rapidă)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Configurare pentru Producție (Focus pe Calitate)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Configurare pentru Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specializare Multi-Agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Dezvoltare la Distanță
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Modele Recomandate

### După Scop

**Scop General:**
- `phi-4-mini` - Echilibru între calitate și viteză

**Răspunsuri Rapide:**
- `qwen2.5-0.5b` - Foarte rapid, bun pentru clasificare
- `phi-4-mini` - Rapid cu calitate bună

**Calitate Ridicată:**
- `qwen2.5-7b` - Cea mai bună calitate, consum mai mare de resurse
- `phi-4-mini` - Calitate bună, resurse mai reduse

**Generare Cod:**
- `deepseek-coder-1.3b` - Specializat pentru cod
- `phi-4-mini` - Codare generală

### După Disponibilitatea Resurselor

**Resurse Reduse (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Resurse Medii (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Resurse Mari (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Configurare Avansată

### Endpoint-uri Personalizate

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatură și Sampling (Suprascriere în Cod)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Configurare Hibridă Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Depanare

### Variabile de Mediu Neîncărcate

**Simptome:**
- Scripturile folosesc modele greșite
- Erori de conexiune
- Variabile nerecunoscute

**Soluții:**
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

### Probleme de Conexiune la Serviciu

**Simptome:**
- Erori "Connection refused"
- "Serviciu indisponibil"
- Erori de timeout

**Soluții:**
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

### Modelul Nu Este Găsit

**Simptome:**
- Erori "Model not found"
- "Alias nerecunoscut"

**Soluții:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Erori de Import

**Simptome:**
- Erori "Module not found"

**Soluții:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testarea Configurării

### Verifică Încărcarea Mediului

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

### Testează Conexiunea Foundry Local

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

## Practici de Securitate Recomandate

### 1. Nu Comite Niciodată Secrete

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Folosește Fișiere .env Separate

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotește Cheile API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Folosește Configurări Specifice Mediului

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Documentația SDK

- **Depozit Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentație API**: Verifică depozitul SDK pentru cele mai recente informații

## Resurse Suplimentare

- `QUICK_START.md` - Ghid de început
- `Workshop/samples/*/README.md` - Ghiduri specifice exemplelor

---

**Ultima Actualizare**: 2025-01-08  
**Versiune**: 2.0  
**SDK**: Foundry Local Python SDK (latest)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->