<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T22:18:45+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "hi"
}
-->
# वर्कशॉप सैंपल्स - त्वरित संदर्भ कार्ड

**अंतिम अपडेट**: 8 अक्टूबर, 2025

---

## 🚀 त्वरित शुरुआत

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

## 📂 सैंपल अवलोकन

| सत्र | सैंपल | उद्देश्य | समय |
|------|-------|---------|------|
| 01 | `chat_bootstrap.py` | बेसिक चैट + स्ट्रीमिंग | ~30 सेकंड |
| 02 | `rag_pipeline.py` | RAG एम्बेडिंग के साथ | ~45 सेकंड |
| 02 | `rag_eval_ragas.py` | RAG मूल्यांकन | ~60 सेकंड |
| 03 | `benchmark_oss_models.py` | मॉडल बेंचमार्किंग | ~2 मिनट |
| 04 | `model_compare.py` | SLM बनाम LLM | ~45 सेकंड |
| 05 | `agents_orchestrator.py` | मल्टी-एजेंट सिस्टम | ~60 सेकंड |
| 06 | `models_router.py` | इंटेंट रूटिंग | ~45 सेकंड |
| 06 | `models_pipeline.py` | मल्टी-स्टेप पाइपलाइन | ~60 सेकंड |

---

## 🛠️ पर्यावरण वेरिएबल्स

### आवश्यक
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### सत्र-विशिष्ट
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

## ✅ सत्यापन और परीक्षण

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

## 🐛 समस्या निवारण

### कनेक्शन त्रुटि
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### आयात त्रुटि
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### मॉडल नहीं मिला
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### धीमा प्रदर्शन
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 सामान्य पैटर्न

### बेसिक चैट
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### क्लाइंट प्राप्त करें
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### त्रुटि प्रबंधन
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### स्ट्रीमिंग
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

## 📊 मॉडल चयन

| मॉडल | आकार | सर्वश्रेष्ठ उपयोग | गति |
|------|------|------------------|------|
| `qwen2.5-0.5b` | 0.5B | तेज वर्गीकरण | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | त्वरित कोड जनरेशन | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | रचनात्मक लेखन | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | कोड, रिफैक्टरिंग | ⚡⚡ |
| `phi-4-mini` | 4B | सामान्य, सारांश | ⚡⚡ |
| `qwen2.5-7b` | 7B | जटिल तर्क | ⚡ |

---

## 🔗 संसाधन

- **SDK दस्तावेज़**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **त्वरित संदर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 सुझाव

1. **क्लाइंट्स कैश करें**: `workshop_utils` आपके लिए कैश करता है
2. **छोटे मॉडल का उपयोग करें**: परीक्षण के लिए `qwen2.5-0.5b` से शुरू करें
3. **उपयोग आँकड़े सक्षम करें**: टोकन ट्रैक करने के लिए `SHOW_USAGE=1` सेट करें
4. **बैच प्रोसेसिंग**: कई प्रॉम्प्ट्स को क्रमिक रूप से प्रोसेस करें
5. **max_tokens कम करें**: त्वरित प्रतिक्रिया के लिए विलंबता कम करें

---

## 🎯 सैंपल वर्कफ़्लो

### सब कुछ परीक्षण करें
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### मॉडल बेंचमार्क करें
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG पाइपलाइन
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### मल्टी-एजेंट सिस्टम
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**त्वरित सहायता**: `samples` डायरेक्टरी से किसी भी सैंपल को `--help` के साथ चलाएं या डॉकस्ट्रिंग देखें:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**सभी सैंपल अक्टूबर 2025 में Foundry Local SDK सर्वोत्तम प्रथाओं के साथ अपडेट किए गए** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->