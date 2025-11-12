<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T23:23:56+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "no"
}
-->
# Workshop Eksempler - Hurtigreferansekort

**Sist oppdatert**: 8. oktober 2025

---

## 🚀 Kom i gang

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

## 📂 Oversikt over eksempler

| Sesjon | Eksempel | Formål | Tid |
|--------|----------|--------|-----|
| 01 | `chat_bootstrap.py` | Grunnleggende chat + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG med embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | RAG evaluering | ~60s |
| 03 | `benchmark_oss_models.py` | Modellbenchmarking | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-agent system | ~60s |
| 06 | `models_router.py` | Intent-routing | ~45s |
| 06 | `models_pipeline.py` | Flertrinns pipeline | ~60s |

---

## 🛠️ Miljøvariabler

### Essensielle
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Sesjonsspesifikke
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

## ✅ Validering og testing

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

## 🐛 Feilsøking

### Tilkoblingsfeil
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importfeil
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modell ikke funnet
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Langsom ytelse
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Vanlige mønstre

### Grunnleggende chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Hent klient
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Feilhåndtering
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

## 📊 Modellvalg

| Modell | Størrelse | Best til | Hastighet |
|--------|-----------|----------|-----------|
| `qwen2.5-0.5b` | 0.5B | Rask klassifisering | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Rask kodegenerering | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreativ skriving | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kode, refaktorering | ⚡⚡ |
| `phi-4-mini` | 4B | Generelt, oppsummering | ⚡⚡ |
| `qwen2.5-7b` | 7B | Kompleks resonnering | ⚡ |

---

## 🔗 Ressurser

- **SDK-dokumentasjon**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hurtigreferanse**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Tips

1. **Cache klienter**: `workshop_utils` cacher for deg
2. **Bruk mindre modeller**: Start med `qwen2.5-0.5b` for testing
3. **Aktiver bruksstatistikk**: Sett `SHOW_USAGE=1` for å spore tokens
4. **Batch-prosessering**: Behandle flere forespørsler sekvensielt
5. **Reduser max_tokens**: Reduserer ventetid for raske svar

---

## 🎯 Eksempelarbeidsflyter

### Test alt
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark modeller
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG Pipeline
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Multi-agent system
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Hurtighjelp**: Kjør et hvilket som helst eksempel med `--help` fra `samples`-katalogen eller sjekk docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Alle eksempler oppdatert oktober 2025 med Foundry Local SDK beste praksis** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->