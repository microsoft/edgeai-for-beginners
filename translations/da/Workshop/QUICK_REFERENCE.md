# Workshop Eksempler - Hurtig Referencekort

**Sidst Opdateret**: 8. oktober 2025

---

## 🚀 Hurtig Start

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

## 📂 Eksempeloversigt

| Session | Eksempel | Formål | Tid |
|---------|----------|--------|-----|
| 01 | `chat_bootstrap.py` | Grundlæggende chat + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG med embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | RAG evaluering | ~60s |
| 03 | `benchmark_oss_models.py` | Modelbenchmarking | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-agent system | ~60s |
| 06 | `models_router.py` | Intent-routing | ~45s |
| 06 | `models_pipeline.py` | Multi-step pipeline | ~60s |

---

## 🛠️ Miljøvariabler

### Nødvendige
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Session-Specifikke
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

## ✅ Validering & Test

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

## 🐛 Fejlfinding

### Forbindelsesfejl
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importfejl
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model Ikke Fundet
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Langsom Ydeevne
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Almindelige Mønstre

### Grundlæggende Chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Hent Klient
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Fejlhåndtering
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

## 📊 Modelvalg

| Model | Størrelse | Bedst Til | Hastighed |
|-------|-----------|-----------|-----------|
| `qwen2.5-0.5b` | 0.5B | Hurtig klassificering | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Hurtig kodegenerering | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreativ skrivning | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kode, refaktorering | ⚡⚡ |
| `phi-4-mini` | 4B | Generelt, opsummering | ⚡⚡ |
| `qwen2.5-7b` | 7B | Kompleks ræsonnement | ⚡ |

---

## 🔗 Ressourcer

- **SDK Dokumentation**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hurtig Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Tips

1. **Cache klienter**: `workshop_utils` cacher for dig
2. **Brug mindre modeller**: Start med `qwen2.5-0.5b` til test
3. **Aktiver brugstatistik**: Sæt `SHOW_USAGE=1` for at spore tokens
4. **Batchbehandling**: Behandl flere prompts sekventielt
5. **Reducer max_tokens**: Mindsker ventetid for hurtige svar

---

## 🎯 Eksempelarbejdsgange

### Test Alt
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark Modeller
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

### Multi-Agent System
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Hurtig Hjælp**: Kør et hvilket som helst eksempel med `--help` fra `samples`-mappen eller tjek docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Alle eksempler opdateret oktober 2025 med Foundry Local SDK bedste praksis** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->