<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T21:15:23+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "mr"
}
-->
# कार्यशाळा नमुने - जलद संदर्भ कार्ड

**शेवटचे अद्यतन**: 8 ऑक्टोबर, 2025

---

## 🚀 जलद सुरुवात

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

## 📂 नमुन्यांचा आढावा

| सत्र | नमुना | उद्देश | वेळ |
|------|-------|--------|------|
| 01 | `chat_bootstrap.py` | मूलभूत चॅट + स्ट्रीमिंग | ~30 सेकंद |
| 02 | `rag_pipeline.py` | एम्बेडिंगसह RAG | ~45 सेकंद |
| 02 | `rag_eval_ragas.py` | RAG मूल्यांकन | ~60 सेकंद |
| 03 | `benchmark_oss_models.py` | मॉडेल बेंचमार्किंग | ~2 मिनिटे |
| 04 | `model_compare.py` | SLM vs LLM | ~45 सेकंद |
| 05 | `agents_orchestrator.py` | मल्टी-एजंट प्रणाली | ~60 सेकंद |
| 06 | `models_router.py` | हेतू रूटिंग | ~45 सेकंद |
| 06 | `models_pipeline.py` | मल्टी-स्टेप पाइपलाइन | ~60 सेकंद |

---

## 🛠️ पर्यावरणीय व्हेरिएबल्स

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

## ✅ सत्यापन आणि चाचणी

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

## 🐛 समस्या निराकरण

### कनेक्शन त्रुटी
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### आयात त्रुटी
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### मॉडेल सापडले नाही
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### धीम्या कार्यक्षमता
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 सामान्य नमुने

### मूलभूत चॅट
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### क्लायंट मिळवा
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### त्रुटी हाताळणी
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

## 📊 मॉडेल निवड

| मॉडेल | आकार | सर्वोत्तम उपयोग | गती |
|-------|------|----------------|-----|
| `qwen2.5-0.5b` | 0.5B | जलद वर्गीकरण | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | जलद कोड निर्मिती | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | सर्जनशील लेखन | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | कोड, पुनर्रचना | ⚡⚡ |
| `phi-4-mini` | 4B | सामान्य, सारांश | ⚡⚡ |
| `qwen2.5-7b` | 7B | जटिल विचार | ⚡ |

---

## 🔗 संसाधने

- **SDK दस्तऐवज**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **जलद संदर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **अद्यतन सारांश**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **मायग्रेशन नोट्स**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 टिप्स

1. **क्लायंट कॅश करा**: `workshop_utils` तुमच्यासाठी कॅश करतो
2. **लहान मॉडेल वापरा**: चाचणीसाठी `qwen2.5-0.5b` पासून सुरुवात करा
3. **वापर आकडेवारी सक्षम करा**: टोकन ट्रॅक करण्यासाठी `SHOW_USAGE=1` सेट करा
4. **बॅच प्रक्रिया**: अनेक प्रॉम्प्ट्स अनुक्रमे प्रक्रिया करा
5. **कमाल टोकन कमी करा**: जलद प्रतिसादासाठी विलंब कमी करा

---

## 🎯 नमुना कार्यप्रवाह

### सर्वकाही चाचणी करा
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### मॉडेल बेंचमार्क करा
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

### मल्टी-एजंट प्रणाली
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**जलद मदत**: `samples` डिरेक्टरीमधून कोणताही नमुना `--help` सह चालवा किंवा डॉक्स्ट्रिंग तपासा:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**सर्व नमुने ऑक्टोबर 2025 मध्ये Foundry Local SDK सर्वोत्तम पद्धतींसह अद्यतनित केले** ✨

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.