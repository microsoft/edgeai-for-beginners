# Esempi di Workshop - Scheda di Riferimento Rapida

**Ultimo aggiornamento**: 8 ottobre 2025

---

## 🚀 Avvio Rapido

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Panoramica degli Esempi

| Sessione | Esempio | Scopo | Tempo |
|----------|---------|-------|-------|
| 01 | `chat_bootstrap.py` | Chat di base + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG con embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Valutazione RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmarking dei modelli | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Sistema multi-agente | ~60s |
| 06 | `models_router.py` | Routing per intenti | ~45s |
| 06 | `models_pipeline.py` | Pipeline multi-step | ~60s |

---

## 🛠️ Variabili d'Ambiente

### Essenziali
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Specifiche per Sessione
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Validazione e Test

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Risoluzione dei Problemi

### Errore di Connessione
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Errore di Importazione
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modello Non Trovato
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Prestazioni Lente
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Pattern Comuni

### Chat di Base
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Ottenere il Client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Gestione degli Errori
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Selezione del Modello

| Modello | Dimensione | Ideale per | Velocità |
|---------|------------|------------|----------|
| `qwen2.5-0.5b` | 0.5B | Classificazione veloce | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Generazione rapida di codice | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Scrittura creativa | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Codice, refactoring | ⚡⚡ |
| `phi-4-mini` | 4B | Generale, riassunti | ⚡⚡ |
| `qwen2.5-7b` | 7B | Ragionamento complesso | ⚡ |

---

## 🔗 Risorse

- **Documentazione SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Riferimento Rapido**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Consigli

1. **Cache dei client**: `workshop_utils` gestisce la cache per te
2. **Usa modelli più piccoli**: Inizia con `qwen2.5-0.5b` per i test
3. **Abilita statistiche di utilizzo**: Imposta `SHOW_USAGE=1` per monitorare i token
4. **Elaborazione in batch**: Processa più prompt in sequenza
5. **Riduci max_tokens**: Diminuisce la latenza per risposte rapide

---

## 🎯 Flussi di Lavoro Esempio

### Test Completo
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark dei Modelli
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Pipeline RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Sistema Multi-Agente
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Aiuto Rapido**: Esegui qualsiasi esempio con `--help` dalla directory `samples` o consulta il docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Tutti gli esempi aggiornati a ottobre 2025 con le migliori pratiche del Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->