<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T23:38:53+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "my"
}
-->
# Workshop Samples - အမြန်ကိုးကားကဒ်

**နောက်ဆုံးအပ်ဒိတ်**: အောက်တိုဘာ ၈၊ ၂၀၂၅

---

## 🚀 အမြန်စတင်ရန်

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

## 📂 နမူနာအကျဉ်းချုပ်

| အစည်းအဝေး | နမူနာ | ရည်ရွယ်ချက် | အချိန် |
|------------|--------|-------------|--------|
| 01 | `chat_bootstrap.py` | အခြေခံ chat + streaming | ~30 စက္ကန့် |
| 02 | `rag_pipeline.py` | RAG နှင့် embeddings | ~45 စက္ကန့် |
| 02 | `rag_eval_ragas.py` | RAG အကဲဖြတ်ခြင်း | ~60 စက္ကန့် |
| 03 | `benchmark_oss_models.py` | မော်ဒယ် benchmarking | ~2 မိနစ် |
| 04 | `model_compare.py` | SLM နှင့် LLM | ~45 စက္ကန့် |
| 05 | `agents_orchestrator.py` | Multi-agent system | ~60 စက္ကန့် |
| 06 | `models_router.py` | ရည်ရွယ်ချက် routing | ~45 စက္ကန့် |
| 06 | `models_pipeline.py` | Multi-step pipeline | ~60 စက္ကန့် |

---

## 🛠️ ပတ်ဝန်းကျင် Variables

### အရေးကြီးသော
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### အစည်းအဝေးအလိုက်
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

## ✅ အတည်ပြုခြင်းနှင့် စမ်းသပ်ခြင်း

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

## 🐛 ပြဿနာများကို ဖြေရှင်းခြင်း

### ချိတ်ဆက်မှုအမှား
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Import အမှား
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### မော်ဒယ်မတွေ့ရှိ
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### အလုပ်နှေးခြင်း
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 အများဆုံးတွေ့ရသော Pattern များ

### အခြေခံ Chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Client ရယူခြင်း
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### အမှားကို ကိုင်တွယ်ခြင်း
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

## 📊 မော်ဒယ်ရွေးချယ်ခြင်း

| မော်ဒယ် | အရွယ်အစား | အကောင်းဆုံးအသုံးပြုမှု | အမြန်နှုန်း |
|---------|------------|------------------------|-------------|
| `qwen2.5-0.5b` | 0.5B | အမြန်အတန်းခွဲခြင်း | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | အမြန် code ဖန်တီးခြင်း | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | ဖန်တီးမှုရေးသားခြင်း | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Code, refactoring | ⚡⚡ |
| `phi-4-mini` | 4B | အထွေထွေ, အကျဉ်းချုပ် | ⚡⚡ |
| `qwen2.5-7b` | 7B | ရှုပ်ထွေးသော reasoning | ⚡ |

---

## 🔗 အရင်းအမြစ်များ

- **SDK Docs**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **အမြန်ကိုးကား**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **အပ်ဒိတ်အကျဉ်းချုပ်**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **ပြောင်းရွှေ့မှတ်စုများ**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 အကြံပေးချက်များ

1. **Cache clients**: `workshop_utils` သင့်အတွက် cache လုပ်ပေးသည်
2. **မော်ဒယ်အသေးများကို အသုံးပြုပါ**: စမ်းသပ်ရန် `qwen2.5-0.5b` ဖြင့် စတင်ပါ
3. **အသုံးပြုမှုစာရင်းကို ဖွင့်ပါ**: `SHOW_USAGE=1` ကို သတ်မှတ်ပြီး token များကို စောင့်ကြည့်ပါ
4. **Batch စီမံခြင်း**: prompt များကို အဆင့်ဆင့် စီမံပါ
5. **max_tokens ကို လျှော့ချပါ**: အမြန်တုံ့ပြန်မှုအတွက် latency ကို လျှော့ချသည်

---

## 🎯 နမူနာ Workflow များ

### အားလုံးကို စမ်းသပ်ပါ
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### မော်ဒယ်များကို Benchmark လုပ်ပါ
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

**အမြန်အကူအညီ**: `samples` directory မှ `--help` ဖြင့် နမူနာတစ်ခုခုကို run လုပ်ပါ၊ သို့မဟုတ် docstring ကို ကြည့်ပါ:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**နမူနာအားလုံးကို Foundry Local SDK အကောင်းဆုံးအလေ့အကျင့်များဖြင့် အောက်တိုဘာ ၂၀၂၅ တွင် အပ်ဒိတ်လုပ်ပြီးဖြစ်သည်** ✨

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူသားမှ ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။