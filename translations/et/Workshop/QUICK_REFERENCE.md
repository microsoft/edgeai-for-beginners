<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-12T01:05:31+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "et"
}
-->
# Töötuba Näidised - Kiire Viitekaart

**Viimati uuendatud**: 8. oktoober 2025

---

## 🚀 Kiire alustamine

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

## 📂 Näidiste ülevaade

| Sessioon | Näidis | Eesmärk | Aeg |
|----------|--------|---------|------|
| 01 | `chat_bootstrap.py` | Põhiline vestlus + voogedastus | ~30s |
| 02 | `rag_pipeline.py` | RAG koos sisenditega | ~45s |
| 02 | `rag_eval_ragas.py` | RAG hindamine | ~60s |
| 03 | `benchmark_oss_models.py` | Mudelite võrdlus | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-agent süsteem | ~60s |
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

### Sessioonipõhised
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

## ✅ Valideerimine ja testimine

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

### Impordiviga
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

## 📖 Levinud mustrid

### Põhiline vestlus
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Kliendi hankimine
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Vigade käsitlemine
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

## 📊 Mudeli valik

| Mudel | Suurus | Parim kasutus | Kiirus |
|-------|--------|--------------|--------|
| `qwen2.5-0.5b` | 0.5B | Kiire klassifikatsioon | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Kiire koodi genereerimine | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Loov kirjutamine | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kood, refaktorimine | ⚡⚡ |
| `phi-4-mini` | 4B | Üldine, kokkuvõtted | ⚡⚡ |
| `qwen2.5-7b` | 7B | Keeruline arutlemine | ⚡ |

---

## 🔗 Ressursid

- **SDK dokumentatsioon**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Kiire viide**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Näpunäited

1. **Vahemälu kliendid**: `workshop_utils` teeb seda teie eest
2. **Kasuta väiksemaid mudeleid**: Alusta testimiseks `qwen2.5-0.5b` mudeliga
3. **Luba kasutusstatistika**: Määra `SHOW_USAGE=1`, et jälgida tokenite kasutust
4. **Partii töötlemine**: Töötle mitu sisendit järjest
5. **Vähenda max_tokens väärtust**: Vähendab latentsust kiirete vastuste jaoks

---

## 🎯 Näidistöövood

### Testi kõike
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Mudelite võrdlemine
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG torustik
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Multi-agent süsteem
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Kiire abi**: Käivita ükskõik milline näidis `--help` käsuga `samples` kataloogist või vaata docstring'i:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Kõik näidised uuendatud oktoobris 2025 vastavalt Foundry Local SDK parimatele praktikatele** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun olge teadlik, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->