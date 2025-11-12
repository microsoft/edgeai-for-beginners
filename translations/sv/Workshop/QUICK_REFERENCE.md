<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T23:15:24+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "sv"
}
-->
# Workshop Exempel - Snabb Referenskort

**Senast Uppdaterad**: 8 oktober 2025

---

## 🚀 Snabbstart

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

## 📂 Översikt av Exempel

| Session | Exempel | Syfte | Tid |
|---------|---------|-------|-----|
| 01 | `chat_bootstrap.py` | Grundläggande chatt + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG med embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | RAG-utvärdering | ~60s |
| 03 | `benchmark_oss_models.py` | Modellbenchmarking | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-agent system | ~60s |
| 06 | `models_router.py` | Intent-routing | ~45s |
| 06 | `models_pipeline.py` | Flerstegs-pipeline | ~60s |

---

## 🛠️ Miljövariabler

### Grundläggande
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Sessionsspecifika
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

## ✅ Validering & Testning

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

## 🐛 Felsökning

### Anslutningsfel
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importfel
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modell Ej Hittad
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Långsam Prestanda
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Vanliga Mönster

### Grundläggande Chatt
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Hämta Klient
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Felhantering
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

## 📊 Modellval

| Modell | Storlek | Bäst För | Hastighet |
|--------|---------|----------|-----------|
| `qwen2.5-0.5b` | 0.5B | Snabb klassificering | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Snabb kodgenerering | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreativt skrivande | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kod, omstrukturering | ⚡⚡ |
| `phi-4-mini` | 4B | Generellt, sammanfattning | ⚡⚡ |
| `qwen2.5-7b` | 7B | Komplex resonemang | ⚡ |

---

## 🔗 Resurser

- **SDK Dokumentation**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Snabb Referens**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Tips

1. **Cachea klienter**: `workshop_utils` cachear åt dig
2. **Använd mindre modeller**: Börja med `qwen2.5-0.5b` för testning
3. **Aktivera användningsstatistik**: Ställ in `SHOW_USAGE=1` för att spåra tokens
4. **Batchbearbetning**: Bearbeta flera prompts sekventiellt
5. **Sänk max_tokens**: Minskar latens för snabba svar

---

## 🎯 Exempelarbetsflöden

### Testa Allt
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

**Snabb Hjälp**: Kör vilket exempel som helst med `--help` från katalogen `samples` eller kontrollera docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Alla exempel uppdaterade oktober 2025 med Foundry Local SDK bästa praxis** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->