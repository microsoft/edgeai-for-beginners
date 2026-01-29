# Guida Rapida al Workshop

## Prerequisiti

### 1. Installa Foundry Local

Segui la guida ufficiale all'installazione:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Installa le Dipendenze Python

Dalla directory del Workshop:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Esecuzione degli Esempi del Workshop

### Sessione 01: Chat di Base

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Variabili d'Ambiente:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sessione 02: Pipeline RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Variabili d'Ambiente:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sessione 02: Valutazione RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Nota**: Richiede dipendenze aggiuntive installate tramite `requirements.txt`

### Sessione 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Variabili d'Ambiente:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON con metriche di latenza, throughput e primo token

### Sessione 04: Confronto Modelli

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Variabili d'Ambiente:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sessione 05: Orchestrazione Multi-Agente

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Variabili d'Ambiente:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sessione 06: Router Modelli

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testa la logica di instradamento** con intenti multipli (codice, riassunto, classificazione)

### Sessione 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline complessa multi-step** con pianificazione, esecuzione e perfezionamento

## Script

### Esporta Report Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Tabella Markdown + metriche JSON

### Lint Markdown CLI Patterns

```bash
python lint_markdown_cli.py --verbose
```

**Scopo**: Rilevare pattern CLI deprecati nella documentazione

## Test

### Test di Base

```bash
cd Workshop
python -m tests.smoke
```

**Test**: Funzionalità di base degli esempi principali

## Risoluzione dei Problemi

### Servizio Non Attivo

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Errori di Importazione Moduli

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Errori di Connessione

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modello Non Trovato

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Riferimento alle Variabili d'Ambiente

### Configurazione Principale
| Variabile | Predefinito | Descrizione |
|-----------|-------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varia | Alias del modello da utilizzare |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Sovrascrive l'endpoint del servizio |
| `SHOW_USAGE` | `0` | Mostra le statistiche di utilizzo dei token |
| `RETRY_ON_FAIL` | `1` | Abilita la logica di retry |
| `RETRY_BACKOFF` | `1.0` | Ritardo iniziale per il retry (secondi) |

### Specifiche per Sessione
| Variabile | Predefinito | Descrizione |
|-----------|-------------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modello di embedding |
| `RAG_QUESTION` | Vedi esempio | Domanda di test RAG |
| `BENCH_MODELS` | Varia | Modelli separati da virgola |
| `BENCH_ROUNDS` | `3` | Iterazioni del benchmark |
| `BENCH_PROMPT` | Vedi esempio | Prompt del benchmark |
| `BENCH_STREAM` | `0` | Misura la latenza del primo token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modello agente primario |
| `AGENT_MODEL_EDITOR` | Primario | Modello agente editor |
| `SLM_ALIAS` | `phi-4-mini` | Modello linguistico piccolo |
| `LLM_ALIAS` | `qwen2.5-7b` | Modello linguistico grande |
| `COMPARE_PROMPT` | Vedi esempio | Prompt di confronto |

## Modelli Consigliati

### Sviluppo e Test
- **phi-4-mini** - Qualità e velocità bilanciate
- **qwen2.5-0.5b** - Molto veloce per la classificazione
- **gemma-2-2b** - Buona qualità, velocità moderata

### Scenari di Produzione
- **phi-4-mini** - Uso generico
- **deepseek-coder-1.3b** - Generazione di codice
- **qwen2.5-7b** - Risposte di alta qualità

## Documentazione SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## Ottenere Aiuto

1. Controlla lo stato del servizio: `foundry service status`  
2. Visualizza i log: Controlla i log del servizio Foundry Local  
3. Consulta la documentazione SDK: https://github.com/microsoft/Foundry-Local  
4. Esamina il codice di esempio: Tutti gli esempi includono docstring dettagliati  

## Prossimi Passi

1. Completa tutte le sessioni del workshop in ordine  
2. Sperimenta con modelli diversi  
3. Modifica gli esempi per i tuoi casi d'uso  

---

**Ultimo Aggiornamento**: 2025-01-08  
**Versione del Workshop**: Ultima  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->