<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-12T00:35:22+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "hr"
}
-->
# Uzorci radionice - Brza referentna kartica

**Zadnje ažuriranje**: 8. listopada 2025.

---

## 🚀 Brzi početak

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

## 📂 Pregled uzoraka

| Sesija | Uzorak | Svrha | Vrijeme |
|--------|--------|-------|---------|
| 01 | `chat_bootstrap.py` | Osnovni chat + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG s ugrađenim podacima | ~45s |
| 02 | `rag_eval_ragas.py` | Evaluacija RAG-a | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmarking modela | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Sustav s više agenata | ~60s |
| 06 | `models_router.py` | Usmjeravanje prema namjeri | ~45s |
| 06 | `models_pipeline.py` | Višekorakna cjevovodna obrada | ~60s |

---

## 🛠️ Varijable okruženja

### Osnovne
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Specifične za sesiju
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

## ✅ Validacija i testiranje

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

## 🐛 Rješavanje problema

### Greška u povezivanju
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Greška pri uvozu
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model nije pronađen
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Sporo izvođenje
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Uobičajeni obrasci

### Osnovni chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Dohvati klijenta
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Rukovanje greškama
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

## 📊 Odabir modela

| Model | Veličina | Najbolje za | Brzina |
|-------|----------|-------------|--------|
| `qwen2.5-0.5b` | 0.5B | Brza klasifikacija | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Brza generacija koda | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreativno pisanje | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kodiranje, refaktoriranje | ⚡⚡ |
| `phi-4-mini` | 4B | Općenito, sažeci | ⚡⚡ |
| `qwen2.5-7b` | 7B | Složeno zaključivanje | ⚡ |

---

## 🔗 Resursi

- **SDK dokumentacija**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Brza referenca**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Savjeti

1. **Keširajte klijente**: `workshop_utils` to radi za vas
2. **Koristite manje modele**: Počnite s `qwen2.5-0.5b` za testiranje
3. **Omogućite statistiku korištenja**: Postavite `SHOW_USAGE=1` za praćenje tokena
4. **Obrada u serijama**: Obradite više upita uzastopno
5. **Smanjite max_tokens**: Smanjuje kašnjenje za brze odgovore

---

## 🎯 Radni tijekovi uzoraka

### Testiraj sve
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark modela
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG cjevovod
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Sustav s više agenata
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Brza pomoć**: Pokrenite bilo koji uzorak s `--help` iz direktorija `samples` ili provjerite docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Svi uzorci ažurirani u listopadu 2025. prema najboljim praksama Foundry Local SDK-a** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->