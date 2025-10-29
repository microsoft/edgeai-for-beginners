<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T23:03:14+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "cs"
}
-->
# Ukázky workshopu - Rychlá referenční karta

**Poslední aktualizace**: 8. října 2025

---

## 🚀 Rychlý start

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

## 📂 Přehled ukázek

| Sezení | Ukázka | Účel | Čas |
|--------|--------|------|------|
| 01 | `chat_bootstrap.py` | Základní chat + streamování | ~30s |
| 02 | `rag_pipeline.py` | RAG s embeddingy | ~45s |
| 02 | `rag_eval_ragas.py` | Hodnocení RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Porovnání modelů | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Systém s více agenty | ~60s |
| 06 | `models_router.py` | Směrování záměrů | ~45s |
| 06 | `models_pipeline.py` | Vícekrokový proces | ~60s |

---

## 🛠️ Proměnné prostředí

### Základní
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Specifické pro sezení
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

## ✅ Ověření a testování

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

## 🐛 Řešení problémů

### Chyba připojení
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Chyba importu
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model nenalezen
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Pomalý výkon
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Běžné vzory

### Základní chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Získání klienta
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Zpracování chyb
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streamování
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

## 📊 Výběr modelu

| Model | Velikost | Nejlepší pro | Rychlost |
|-------|----------|-------------|----------|
| `qwen2.5-0.5b` | 0.5B | Rychlá klasifikace | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Rychlá generace kódu | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreativní psaní | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kód, refaktoring | ⚡⚡ |
| `phi-4-mini` | 4B | Obecné, shrnutí | ⚡⚡ |
| `qwen2.5-7b` | 7B | Složitější uvažování | ⚡ |

---

## 🔗 Zdroje

- **SDK dokumentace**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rychlá reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Shrnutí aktualizací**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Poznámky k migraci**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Tipy

1. **Cache klientů**: `workshop_utils` to za vás ukládá do mezipaměti
2. **Používejte menší modely**: Začněte s `qwen2.5-0.5b` pro testování
3. **Povolte statistiky využití**: Nastavte `SHOW_USAGE=1` pro sledování tokenů
4. **Zpracování v dávkách**: Zpracovávejte více promptů postupně
5. **Snižte max_tokens**: Snižuje latenci pro rychlé odpovědi

---

## 🎯 Ukázkové pracovní postupy

### Otestujte vše
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Porovnání modelů
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG pipeline
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Systém s více agenty
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Rychlá pomoc**: Spusťte jakoukoli ukázku s `--help` z adresáře `samples` nebo si přečtěte docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Všechny ukázky aktualizovány v říjnu 2025 podle nejlepších postupů Foundry Local SDK** ✨

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.