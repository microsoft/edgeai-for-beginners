<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:40:54+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "it"
}
-->
# Esempi del Workshop - Riepilogo Aggiornamento SDK Locale Foundry

## Panoramica

Tutti gli esempi Python nella directory `Workshop/samples` sono stati aggiornati per seguire le migliori pratiche dell'SDK Locale Foundry e garantire coerenza in tutto il workshop.

**Data**: 8 ottobre 2025  
**Ambito**: 9 file Python in 6 sessioni del workshop  
**Focus principale**: Gestione degli errori, documentazione, modelli SDK, esperienza utente

---

## File Aggiornati

### Sessione 01: Introduzione
- ✅ `chat_bootstrap.py` - Esempi di base di chat e streaming

### Sessione 02: Soluzioni RAG
- ✅ `rag_pipeline.py` - Implementazione RAG con embeddings
- ✅ `rag_eval_ragas.py` - Valutazione RAG con metriche RAGAS

### Sessione 03: Modelli Open Source
- ✅ `benchmark_oss_models.py` - Benchmarking multi-modello

### Sessione 04: Modelli Avanzati
- ✅ `model_compare.py` - Confronto tra SLM e LLM

### Sessione 05: Agenti Alimentati dall'AI
- ✅ `agents_orchestrator.py` - Coordinamento multi-agente

### Sessione 06: Modelli come Strumenti
- ✅ `models_router.py` - Routing basato sull'intento
- ✅ `models_pipeline.py` - Pipeline multi-step con routing

### Infrastruttura di Supporto
- ✅ `workshop_utils.py` - Già conforme alle migliori pratiche (nessuna modifica necessaria)

---

## Miglioramenti Chiave

### 1. Gestione degli Errori Migliorata

**Prima:**
```python
manager, client, model_id = get_client(alias)
```

**Dopo:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Vantaggi:**
- Gestione degli errori più fluida con messaggi chiari
- Suggerimenti pratici per la risoluzione dei problemi
- Codici di uscita appropriati per gli script

### 2. Gestione degli Import Migliorata

**Prima:**
```python
from sentence_transformers import SentenceTransformer
```

**Dopo:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Vantaggi:**
- Indicazioni chiare quando mancano dipendenze
- Prevenzione di errori di importazione criptici
- Istruzioni di installazione user-friendly

### 3. Documentazione Completa

**Aggiunto a tutti gli esempi:**
- Documentazione delle variabili d'ambiente nei docstring
- Link di riferimento all'SDK
- Esempi di utilizzo
- Documentazione dettagliata di funzioni/parametri
- Suggerimenti di tipo per un supporto migliore negli IDE

**Esempio:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Feedback Utente Migliorato

**Aggiunto logging informativo:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indicatori di progresso:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Output strutturato:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking Robusto

**Miglioramenti nella Sessione 03:**
- Gestione degli errori per modello (continua in caso di errore)
- Report dettagliati sul progresso
- Esecuzione corretta dei round di warmup
- Supporto alla misurazione della latenza del primo token
- Separazione chiara delle fasi

### 6. Suggerimenti di Tipo Coerenti

**Aggiunti ovunque:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Vantaggi:**
- Autocompletamento migliore negli IDE
- Rilevamento precoce degli errori
- Codice auto-documentante

### 7. Router dei Modelli Migliorato

**Miglioramenti nella Sessione 06:**
- Documentazione completa del rilevamento dell'intento
- Spiegazione dell'algoritmo di selezione del modello
- Log dettagliati del routing
- Formattazione dell'output dei test
- Recupero degli errori nei test batch

### 8. Orchestrazione Multi-Agente

**Miglioramenti nella Sessione 05:**
- Report sul progresso fase per fase
- Gestione degli errori per agente
- Struttura chiara della pipeline
- Documentazione migliorata sulla gestione della memoria

---

## Checklist di Test

### Prerequisiti
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testare Ogni Esempio

#### Sessione 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sessione 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sessione 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sessione 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sessione 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sessione 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Riferimento Variabili d'Ambiente

### Globali (Tutti gli Esempi)
| Variabile | Descrizione | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias del modello da utilizzare | Varia in base all'esempio |
| `FOUNDRY_LOCAL_ENDPOINT` | Sovrascrive l'endpoint del servizio | Rilevato automaticamente |
| `SHOW_USAGE` | Mostra l'utilizzo dei token | `0` |
| `RETRY_ON_FAIL` | Abilita la logica di retry | `1` |
| `RETRY_BACKOFF` | Ritardo iniziale per il retry | `1.0` |

### Specifiche per Esempio
| Variabile | Utilizzata da | Descrizione |
|----------|---------------|-------------|
| `EMBED_MODEL` | Sessione 02 | Nome del modello di embedding |
| `RAG_QUESTION` | Sessione 02 | Domanda di test per RAG |
| `BENCH_MODELS` | Sessione 03 | Modelli da testare separati da virgola |
| `BENCH_ROUNDS` | Sessione 03 | Numero di round di benchmark |
| `BENCH_PROMPT` | Sessione 03 | Prompt di test per i benchmark |
| `BENCH_STREAM` | Sessione 03 | Misura della latenza del primo token |
| `SLM_ALIAS` | Sessione 04 | Modello di linguaggio piccolo |
| `LLM_ALIAS` | Sessione 04 | Modello di linguaggio grande |
| `COMPARE_PROMPT` | Sessione 04 | Prompt di test per il confronto |
| `AGENT_MODEL_PRIMARY` | Sessione 05 | Modello agente primario |
| `AGENT_MODEL_EDITOR` | Sessione 05 | Modello agente editor |
| `AGENT_QUESTION` | Sessione 05 | Domanda di test per gli agenti |
| `PIPELINE_TASK` | Sessione 06 | Compito per la pipeline |

---

## Modifiche Importanti

**Nessuna** - Tutte le modifiche sono retrocompatibili.

Gli script esistenti continueranno a funzionare. Le nuove funzionalità includono:
- Variabili d'ambiente opzionali
- Messaggi di errore migliorati (non interrompono la funzionalità)
- Logging aggiuntivo (può essere disattivato)
- Migliori suggerimenti di tipo (nessun impatto a runtime)

---

## Migliori Pratiche Implementate

### 1. Utilizzare Sempre Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Modello di Gestione degli Errori Corretto
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Logging Informativo
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Suggerimenti di Tipo
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstring Completi
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Supporto alle Variabili d'Ambiente
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Degradazione Graduale
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Problemi Comuni e Soluzioni

### Problema: Errori di Importazione
**Soluzione:** Installare le dipendenze mancanti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problema: Errori di Connessione
**Soluzione:** Assicurarsi che Foundry Local sia in esecuzione
```bash
foundry service status
foundry model run phi-4-mini
```

### Problema: Modello Non Trovato
**Soluzione:** Verificare i modelli disponibili
```bash
foundry model ls
foundry model download <alias>
```

### Problema: Prestazioni Lente
**Soluzione:** Utilizzare modelli più piccoli o regolare i parametri
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Prossimi Passi

### 1. Testare Tutti gli Esempi
Seguire la checklist di test sopra per verificare che tutti gli esempi funzionino correttamente.

### 2. Aggiornare la Documentazione
- Aggiornare i file markdown delle sessioni con i nuovi esempi
- Aggiungere una sezione di risoluzione dei problemi al README principale
- Creare una guida di riferimento rapido

### 3. Creare Test di Integrazione
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Aggiungere Benchmark di Prestazioni
Monitorare i miglioramenti delle prestazioni derivanti dai miglioramenti nella gestione degli errori.

### 5. Feedback Utente
Raccogliere feedback dai partecipanti al workshop su:
- Chiarezza dei messaggi di errore
- Completezza della documentazione
- Facilità d'uso

---

## Risorse

- **SDK Locale Foundry**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Riferimento Rapido**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Note di Migrazione**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Repository Principale**: https://github.com/microsoft/Foundry-Local

---

## Manutenzione

### Aggiungere Nuovi Esempi
Seguire questi modelli quando si creano nuovi esempi:

1. Utilizzare `workshop_utils` per la gestione del client
2. Aggiungere una gestione completa degli errori
3. Includere il supporto alle variabili d'ambiente
4. Aggiungere suggerimenti di tipo e docstring
5. Fornire logging informativo
6. Includere esempi di utilizzo nei docstring
7. Collegarsi alla documentazione dell'SDK

### Revisionare gli Aggiornamenti
Quando si revisionano gli aggiornamenti degli esempi, verificare:
- [ ] Gestione degli errori su tutte le operazioni di I/O
- [ ] Suggerimenti di tipo sulle funzioni pubbliche
- [ ] Docstring completi
- [ ] Documentazione delle variabili d'ambiente
- [ ] Feedback informativo per l'utente
- [ ] Link di riferimento all'SDK
- [ ] Stile del codice coerente

---

**Riepilogo**: Tutti gli esempi Python del Workshop ora seguono le migliori pratiche dell'SDK Locale Foundry con gestione degli errori migliorata, documentazione completa e un'esperienza utente ottimizzata. Nessuna modifica incompatibile - tutte le funzionalità esistenti sono state preservate e migliorate.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.