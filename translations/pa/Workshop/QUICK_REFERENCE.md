# ਵਰਕਸ਼ਾਪ ਨਮੂਨੇ - ਤੁਰੰਤ ਸੰਦਰਭ ਕਾਰਡ

**ਆਖਰੀ ਅਪਡੇਟ**: ਅਕਤੂਬਰ 8, 2025

---

## 🚀 ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

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

## 📂 ਨਮੂਨਾ ਝਲਕ

| ਸੈਸ਼ਨ | ਨਮੂਨਾ | ਉਦੇਸ਼ | ਸਮਾਂ |
|-------|--------|-------|------|
| 01 | `chat_bootstrap.py` | ਬੁਨਿਆਦੀ ਚੈਟ + ਸਟ੍ਰੀਮਿੰਗ | ~30ਸੇ |
| 02 | `rag_pipeline.py` | RAG ਐਮਬੈਡਿੰਗ ਨਾਲ | ~45ਸੇ |
| 02 | `rag_eval_ragas.py` | RAG ਮੁਲਾਂਕਣ | ~60ਸੇ |
| 03 | `benchmark_oss_models.py` | ਮਾਡਲ ਬੈਂਚਮਾਰਕਿੰਗ | ~2ਮਿੰਟ |
| 04 | `model_compare.py` | SLM vs LLM | ~45ਸੇ |
| 05 | `agents_orchestrator.py` | ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ | ~60ਸੇ |
| 06 | `models_router.py` | ਇਰਾਦਾ ਰੂਟਿੰਗ | ~45ਸੇ |
| 06 | `models_pipeline.py` | ਮਲਟੀ-ਸਟੈਪ ਪਾਈਪਲਾਈਨ | ~60ਸੇ |

---

## 🛠️ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

### ਜ਼ਰੂਰੀ
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### ਸੈਸ਼ਨ-ਵਿਸ਼ੇਸ਼
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

## ✅ ਵੈਧਤਾ ਅਤੇ ਟੈਸਟਿੰਗ

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

## 🐛 ਸਮੱਸਿਆ ਹੱਲ

### ਕਨੈਕਸ਼ਨ ਐਰਰ
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### ਇੰਪੋਰਟ ਐਰਰ
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### ਹੌਲੀ ਪ੍ਰਦਰਸ਼ਨ
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 ਆਮ ਪੈਟਰਨ

### ਬੁਨਿਆਦੀ ਚੈਟ
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### ਕਲਾਇੰਟ ਪ੍ਰਾਪਤ ਕਰੋ
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### ਐਰਰ ਹੈਂਡਲਿੰਗ
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ਸਟ੍ਰੀਮਿੰਗ
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

## 📊 ਮਾਡਲ ਚੋਣ

| ਮਾਡਲ | ਆਕਾਰ | ਸਭ ਤੋਂ ਵਧੀਆ | ਗਤੀ |
|------|------|-------------|------|
| `qwen2.5-0.5b` | 0.5B | ਤੇਜ਼ ਵਰਗੀਕਰਨ | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | ਤੇਜ਼ ਕੋਡ ਜਨਰੇਸ਼ਨ | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | ਰਚਨਾਤਮਕ ਲਿਖਤ | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | ਕੋਡ, ਰੀਫੈਕਟੋਰਿੰਗ | ⚡⚡ |
| `phi-4-mini` | 4B | ਜਨਰਲ, ਸਾਰ | ⚡⚡ |
| `qwen2.5-7b` | 7B | ਜਟਿਲ ਤਰਕ | ⚡ |

---

## 🔗 ਸਰੋਤ

- **SDK ਦਸਤਾਵੇਜ਼**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **ਤੁਰੰਤ ਸੰਦਰਭ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 ਸੁਝਾਅ

1. **ਕਲਾਇੰਟ ਕੈਸ਼ ਕਰੋ**: `workshop_utils` ਤੁਹਾਡੇ ਲਈ ਕੈਸ਼ ਕਰਦਾ ਹੈ
2. **ਛੋਟੇ ਮਾਡਲ ਵਰਤੋ**: ਟੈਸਟਿੰਗ ਲਈ `qwen2.5-0.5b` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ
3. **ਵਰਤੋਂ ਸਾਂਖੇਪ ਸਥਾਪਿਤ ਕਰੋ**: ਟੋਕਨ ਟ੍ਰੈਕ ਕਰਨ ਲਈ `SHOW_USAGE=1` ਸੈਟ ਕਰੋ
4. **ਬੈਚ ਪ੍ਰੋਸੈਸਿੰਗ**: ਕਈ ਪ੍ਰੋਮਪਟ ਲਗਾਤਾਰ ਪ੍ਰੋਸੈਸ ਕਰੋ
5. **ਘੱਟ max_tokens**: ਤੇਜ਼ ਜਵਾਬਾਂ ਲਈ ਲੈਟੈਂਸੀ ਘਟਾਉਂਦਾ ਹੈ

---

## 🎯 ਨਮੂਨਾ ਵਰਕਫਲੋ

### ਸਭ ਕੁਝ ਟੈਸਟ ਕਰੋ
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### ਮਾਡਲ ਬੈਂਚਮਾਰਕ
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG ਪਾਈਪਲਾਈਨ
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**ਤੁਰੰਤ ਮਦਦ**: `samples` ਡਾਇਰੈਕਟਰੀ ਤੋਂ `--help` ਨਾਲ ਕੋਈ ਵੀ ਨਮੂਨਾ ਚਲਾਓ ਜਾਂ ਡਾਕਸਟ੍ਰਿੰਗ ਚੈੱਕ ਕਰੋ:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**ਸਾਰੇ ਨਮੂਨੇ ਅਕਤੂਬਰ 2025 ਵਿੱਚ Foundry Local SDK ਦੀਆਂ ਸਭ ਤੋਂ ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਨਾਲ ਅਪਡੇਟ ਕੀਤੇ ਗਏ** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->