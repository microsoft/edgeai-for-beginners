<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T22:49:16+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "it"
}
-->
# Guida alla Configurazione dell'Ambiente

## Panoramica

Gli esempi del Workshop utilizzano variabili d'ambiente per la configurazione, centralizzate nel file `.env` alla radice del repository. Questo consente una facile personalizzazione senza modificare il codice.

## Avvio Rapido

### 1. Verifica dei Prerequisiti

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configura l'Ambiente

Il file `.env` è già configurato con valori predefiniti sensati. La maggior parte degli utenti non avrà bisogno di modificare nulla.

**Opzionale**: Rivedi e personalizza le impostazioni:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Applica la Configurazione

**Per Script Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Per Notebook:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Riferimento alle Variabili d'Ambiente

### Configurazione Principale

| Variabile | Predefinito | Descrizione |
|-----------|-------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Modello predefinito per gli esempi |
| `FOUNDRY_LOCAL_ENDPOINT` | (vuoto) | Sovrascrive l'endpoint del servizio |
| `PYTHONPATH` | Percorsi del Workshop | Percorso di ricerca dei moduli Python |

**Quando impostare FOUNDRY_LOCAL_ENDPOINT:**
- Istanza remota di Foundry Local
- Configurazione di porta personalizzata
- Separazione tra sviluppo e produzione

**Esempio:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variabili Specifiche per Sessione

#### Sessione 02: Pipeline RAG
| Variabile | Predefinito | Scopo |
|-----------|-------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modello di embedding |
| `RAG_QUESTION` | Preconfigurata | Domanda di test |

#### Sessione 03: Benchmarking
| Variabile | Predefinito | Scopo |
|-----------|-------------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modelli da confrontare |
| `BENCH_ROUNDS` | `3` | Iterazioni per modello |
| `BENCH_PROMPT` | Preconfigurato | Prompt di test |
| `BENCH_STREAM` | `0` | Misura la latenza del primo token |

#### Sessione 04: Confronto Modelli
| Variabile | Predefinito | Scopo |
|-----------|-------------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Modello linguistico piccolo |
| `LLM_ALIAS` | `qwen2.5-7b` | Modello linguistico grande |
| `COMPARE_PROMPT` | Preconfigurato | Prompt di confronto |
| `COMPARE_RETRIES` | `2` | Tentativi di ripetizione |

#### Sessione 05: Orchestrazione Multi-Agente
| Variabile | Predefinito | Scopo |
|-----------|-------------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modello agente ricercatore |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modello agente editor |
| `AGENT_QUESTION` | Preconfigurata | Domanda di test |

### Configurazione di Affidabilità

| Variabile | Predefinito | Scopo |
|-----------|-------------|-------|
| `SHOW_USAGE` | `1` | Stampa l'utilizzo dei token |
| `RETRY_ON_FAIL` | `1` | Abilita la logica di ripetizione |
| `RETRY_BACKOFF` | `1.0` | Ritardo tra i tentativi (secondi) |

## Configurazioni Comuni

### Configurazione per Sviluppo (Iterazione Rapida)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Configurazione per Produzione (Focus sulla Qualità)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Configurazione per Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specializzazione Multi-Agente
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Sviluppo Remoto
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Modelli Consigliati

### Per Caso d'Uso

**Uso Generale:**
- `phi-4-mini` - Qualità e velocità bilanciate

**Risposte Veloci:**
- `qwen2.5-0.5b` - Molto veloce, ideale per classificazione
- `phi-4-mini` - Veloce con buona qualità

**Alta Qualità:**
- `qwen2.5-7b` - Migliore qualità, maggiore utilizzo di risorse
- `phi-4-mini` - Buona qualità, minore utilizzo di risorse

**Generazione di Codice:**
- `deepseek-coder-1.3b` - Specializzato per il codice
- `phi-4-mini` - Generico per la programmazione

### Per Disponibilità di Risorse

**Risorse Basse (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Risorse Medie (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Risorse Alte (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Configurazione Avanzata

### Endpoint Personalizzati

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura e Campionamento (Sovrascrivere nel Codice)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Configurazione Ibrida Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Risoluzione dei Problemi

### Variabili d'Ambiente Non Caricate

**Sintomi:**
- Gli script utilizzano modelli sbagliati
- Errori di connessione
- Variabili non riconosciute

**Soluzioni:**
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

### Problemi di Connessione al Servizio

**Sintomi:**
- Errori "Connessione rifiutata"
- "Servizio non disponibile"
- Errori di timeout

**Soluzioni:**
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

### Modello Non Trovato

**Sintomi:**
- Errori "Modello non trovato"
- "Alias non riconosciuto"

**Soluzioni:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Errori di Importazione

**Sintomi:**
- Errori "Modulo non trovato"

**Soluzioni:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Test della Configurazione

### Verifica del Caricamento dell'Ambiente

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

### Test della Connessione a Foundry Local

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

## Pratiche di Sicurezza Consigliate

### 1. Non Commettere Mai Segreti

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Usa File .env Separati

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Ruota le Chiavi API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Usa Configurazioni Specifiche per l'Ambiente

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Documentazione SDK

- **Repository Principale**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentazione API**: Consulta il repository SDK per le ultime novità

## Risorse Aggiuntive

- `QUICK_START.md` - Guida introduttiva
- `Workshop/samples/*/README.md` - Guide specifiche per gli esempi

---

**Ultimo Aggiornamento**: 2025-01-08  
**Versione**: 2.0  
**SDK**: Foundry Local Python SDK (ultima versione)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->