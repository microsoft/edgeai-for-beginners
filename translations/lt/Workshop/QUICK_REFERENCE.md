<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-12T00:54:20+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "lt"
}
-->
# Dirbtuvių pavyzdžiai - Greitos nuorodos kortelė

**Paskutinį kartą atnaujinta**: 2025 m. spalio 8 d.

---

## 🚀 Greitas startas

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

## 📂 Pavyzdžių apžvalga

| Sesija | Pavyzdys | Tikslas | Laikas |
|--------|----------|---------|-------|
| 01 | `chat_bootstrap.py` | Pagrindinis pokalbis + transliacija | ~30s |
| 02 | `rag_pipeline.py` | RAG su įterpimais | ~45s |
| 02 | `rag_eval_ragas.py` | RAG vertinimas | ~60s |
| 03 | `benchmark_oss_models.py` | Modelių palyginimas | ~2m |
| 04 | `model_compare.py` | SLM prieš LLM | ~45s |
| 05 | `agents_orchestrator.py` | Daugiaveiksmių agentų sistema | ~60s |
| 06 | `models_router.py` | Ketinimų nukreipimas | ~45s |
| 06 | `models_pipeline.py` | Daugiapakopė sistema | ~60s |

---

## 🛠️ Aplinkos kintamieji

### Esminiai
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Specifiniai sesijai
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

## ✅ Validacija ir testavimas

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

## 🐛 Trikčių šalinimas

### Ryšio klaida
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importavimo klaida
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modelis nerastas
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Lėtas veikimas
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Dažniausi šablonai

### Pagrindinis pokalbis
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Gauti klientą
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Klaidų tvarkymas
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Transliacija
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

## 📊 Modelio pasirinkimas

| Modelis | Dydis | Geriausiai tinka | Greitis |
|---------|-------|------------------|---------|
| `qwen2.5-0.5b` | 0.5B | Greita klasifikacija | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Greita kodo generacija | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kūrybinis rašymas | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kodas, refaktoringas | ⚡⚡ |
| `phi-4-mini` | 4B | Bendras, santrauka | ⚡⚡ |
| `qwen2.5-7b` | 7B | Sudėtingas samprotavimas | ⚡ |

---

## 🔗 Ištekliai

- **SDK dokumentacija**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Greita nuoroda**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Patarimai

1. **Kešuokite klientus**: `workshop_utils` tai padarys už jus
2. **Naudokite mažesnius modelius**: Pradėkite nuo `qwen2.5-0.5b` testavimui
3. **Įjunkite naudojimo statistiką**: Nustatykite `SHOW_USAGE=1`, kad stebėtumėte žetonus
4. **Apdorokite partijomis**: Apdorokite kelis užklausimus iš eilės
5. **Sumažinkite max_tokens**: Sutrumpina atsakymo laiką

---

## 🎯 Pavyzdinės darbo eigos

### Testuokite viską
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Modelių palyginimas
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG sistema
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Daugiaveiksmių agentų sistema
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Greita pagalba**: Paleiskite bet kurį pavyzdį su `--help` iš `samples` katalogo arba peržiūrėkite docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Visi pavyzdžiai atnaujinti 2025 m. spalio mėn. pagal Foundry Local SDK geriausią praktiką** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->