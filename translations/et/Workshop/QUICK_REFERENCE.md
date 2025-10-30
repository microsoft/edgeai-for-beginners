<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-29T00:01:11+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "et"
}
-->
# Töötuba Näidised - Kiire Viitekaart

**Viimati uuendatud**: 8. oktoober 2025

---

## 🚀 Kiire Alustamine

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

## 📂 Näidiste Ülevaade

| Sessioon | Näidis | Eesmärk | Aeg |
|----------|--------|---------|-----|
| 01 | `chat_bootstrap.py` | Põhiline vestlus + voogedastus | ~30s |
| 02 | `rag_pipeline.py` | RAG koos sisenditega | ~45s |
| 02 | `rag_eval_ragas.py` | RAG hindamine | ~60s |
| 03 | `benchmark_oss_models.py` | Mudelite võrdlus | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Mitme agendi süsteem | ~60s |
| 06 | `models_router.py` | Kavatsuste suunamine | ~45s |
| 06 | `models_pipeline.py` | Mitmeastmeline torustik | ~60s |

---

## 🛠️ Keskkonnamuutujad

### Olulised
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Sessioonispetsiifilised
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

## ✅ Valideerimine ja Testimine

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

## 🐛 Tõrkeotsing

### Ühenduse viga
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Impordi viga
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Mudelit ei leitud
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Aeglane jõudlus
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Levinud Mustrid

### Põhiline Vestlus
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Kliendi Hankimine
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Vigade Käitlemine
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Voogedastus
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

## 📊 Mudeli Valik

| Mudel | Suurus | Parim Kasutus | Kiirus |
|-------|--------|---------------|--------|
| `qwen2.5-0.5b` | 0.5B | Kiire klassifikatsioon | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Kiire koodi genereerimine | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Loov kirjutamine | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kood, refaktoreerimine | ⚡⚡ |
| `phi-4-mini` | 4B | Üldine, kokkuvõtted | ⚡⚡ |
| `qwen2.5-7b` | 7B | Keeruline arutlemine | ⚡ |

---

## 🔗 Ressursid

- **SDK Dokumentatsioon**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Kiire Viide**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Uuenduste Kokkuvõte**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Migreerimise Märkmed**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Näpunäited

1. **Vahemälu kliendid**: `workshop_utils` haldab vahemälu sinu eest
2. **Kasuta väiksemaid mudeleid**: Alusta testimist `qwen2.5-0.5b` mudeliga
3. **Luba kasutusstatistika**: Määra `SHOW_USAGE=1`, et jälgida tokenite kasutust
4. **Partii töötlemine**: Töötle mitu sisendit järjestikku
5. **Vähenda max_tokens väärtust**: Vähendab latentsust kiirete vastuste jaoks

---

## 🎯 Näidiste Töövood

### Testi Kõike
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Võrdle Modelle
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG Torustik
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Mitme Agendi Süsteem
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Kiire Abi**: Käivita ükskõik milline näidis `--help` käsuga `samples` kataloogist või vaata docstring'i:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Kõik näidised uuendatud oktoobris 2025 vastavalt Foundry Local SDK parimatele praktikatele** ✨

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.