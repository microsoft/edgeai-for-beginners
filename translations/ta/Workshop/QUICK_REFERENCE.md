# வேலைகள் மாதிரிகள் - விரைவான குறிப்புகள் அட்டை

**கடைசியாக புதுப்பிக்கப்பட்டது**: அக்டோபர் 8, 2025

---

## 🚀 விரைவான தொடக்கம்

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

## 📂 மாதிரி கண்ணோட்டம்

| அமர்வு | மாதிரி | நோக்கம் | நேரம் |
|---------|--------|---------|------|
| 01 | `chat_bootstrap.py` | அடிப்படை உரையாடல் + ஸ்ட்ரீமிங் | ~30s |
| 02 | `rag_pipeline.py` | எம்பெடிங்குகளுடன் RAG | ~45s |
| 02 | `rag_eval_ragas.py` | RAG மதிப்பீடு | ~60s |
| 03 | `benchmark_oss_models.py` | மாதிரி மதிப்பீடு | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | பல முகவர் அமைப்பு | ~60s |
| 06 | `models_router.py` | நோக்கம் வழிமுறை | ~45s |
| 06 | `models_pipeline.py` | பல படி குழாய் | ~60s |

---

## 🛠️ சூழல் மாறிகள்

### அவசியமானவை
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### அமர்வு-குறிப்பானவை
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

## ✅ சரிபார்ப்பு & சோதனை

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

## 🐛 பிரச்சினைகளை சரிசெய்தல்

### இணைப்பு பிழை
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### இறக்குமதி பிழை
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### மாதிரி கிடைக்கவில்லை
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### மெதுவான செயல்திறன்
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 பொதுவான முறைமைகள்

### அடிப்படை உரையாடல்
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### கிளையன்ட் பெறுதல்
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### பிழை கையாளுதல்
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ஸ்ட்ரீமிங்
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

## 📊 மாதிரி தேர்வு

| மாதிரி | அளவு | சிறந்தது | வேகம் |
|-------|------|----------|-------|
| `qwen2.5-0.5b` | 0.5B | வேகமான வகைப்படுத்தல் | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | விரைவான குறியீடு உருவாக்கம் | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | படைப்பாற்றல் எழுத்து | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | குறியீடு, மறுசீரமைப்பு | ⚡⚡ |
| `phi-4-mini` | 4B | பொது, சுருக்கம் | ⚡⚡ |
| `qwen2.5-7b` | 7B | சிக்கலான காரணம் | ⚡ |

---

## 🔗 வளங்கள்

- **SDK ஆவணங்கள்**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **விரைவான குறிப்பு**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 குறிப்புகள்

1. **கிளையன்ட்களை காச்ச் செய்யவும்**: `workshop_utils` உங்களுக்காக காச்ச் செய்கிறது
2. **சிறிய மாதிரிகளை பயன்படுத்தவும்**: சோதனைக்கு `qwen2.5-0.5b` உடன் தொடங்கவும்
3. **பயன்பாட்டு புள்ளிவிவரங்களை இயக்கவும்**: டோக்கன்களை கண்காணிக்க `SHOW_USAGE=1` அமைக்கவும்
4. **தொகுதி செயலாக்கம்**: பல கேள்விகளை தொடர்ச்சியாக செயலாக்கவும்
5. **max_tokens குறைக்கவும்**: விரைவான பதில்களுக்கு தாமதத்தை குறைக்கிறது

---

## 🎯 மாதிரி வேலைகள்

### அனைத்தையும் சோதிக்கவும்
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### மாதிரிகளை மதிப்பீடு செய்யவும்
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG குழாய்
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### பல முகவர் அமைப்பு
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**விரைவான உதவி**: `samples` கோப்பகத்தில் இருந்து `--help` உடன் எந்த மாதிரியையும் இயக்கவும் அல்லது டாக்ஸ்ட்ரிங் பார்க்கவும்:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**அனைத்து மாதிரிகள் அக்டோபர் 2025-இல் Foundry Local SDK சிறந்த நடைமுறைகளுடன் புதுப்பிக்கப்பட்டது** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->