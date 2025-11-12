<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T21:48:05+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ur"
}
-->
# ورکشاپ نمونے - فوری حوالہ کارڈ

**آخری اپ ڈیٹ**: 8 اکتوبر، 2025

---

## 🚀 فوری آغاز

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

## 📂 نمونوں کا جائزہ

| سیشن | نمونہ | مقصد | وقت |
|------|-------|-------|------|
| 01 | `chat_bootstrap.py` | بنیادی چیٹ + اسٹریمنگ | ~30 سیکنڈ |
| 02 | `rag_pipeline.py` | RAG ایمبیڈنگ کے ساتھ | ~45 سیکنڈ |
| 02 | `rag_eval_ragas.py` | RAG کا جائزہ | ~60 سیکنڈ |
| 03 | `benchmark_oss_models.py` | ماڈل بینچ مارکنگ | ~2 منٹ |
| 04 | `model_compare.py` | SLM بمقابلہ LLM | ~45 سیکنڈ |
| 05 | `agents_orchestrator.py` | ملٹی ایجنٹ سسٹم | ~60 سیکنڈ |
| 06 | `models_router.py` | ارادے کی رہنمائی | ~45 سیکنڈ |
| 06 | `models_pipeline.py` | ملٹی اسٹیپ پائپ لائن | ~60 سیکنڈ |

---

## 🛠️ ماحول کے متغیرات

### ضروری
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### سیشن کے مطابق
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

## ✅ توثیق اور جانچ

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

## 🐛 مسائل کا حل

### کنکشن کی خرابی
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### درآمد کی خرابی
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### ماڈل نہیں ملا
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### سست کارکردگی
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 عام نمونے

### بنیادی چیٹ
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### کلائنٹ حاصل کریں
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### خرابی کا انتظام
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### اسٹریمنگ
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

## 📊 ماڈل کا انتخاب

| ماڈل | سائز | بہترین استعمال | رفتار |
|------|------|----------------|-------|
| `qwen2.5-0.5b` | 0.5B | تیز درجہ بندی | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | فوری کوڈ جنریشن | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | تخلیقی تحریر | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | کوڈ، ریفیکٹرنگ | ⚡⚡ |
| `phi-4-mini` | 4B | عمومی، خلاصہ | ⚡⚡ |
| `qwen2.5-7b` | 7B | پیچیدہ استدلال | ⚡ |

---

## 🔗 وسائل

- **SDK دستاویزات**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **فوری حوالہ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 تجاویز

1. **کلائنٹس کو کیش کریں**: `workshop_utils` آپ کے لیے کیش کرتا ہے
2. **چھوٹے ماڈلز استعمال کریں**: ٹیسٹنگ کے لیے `qwen2.5-0.5b` سے شروع کریں
3. **استعمال کے اعدادوشمار فعال کریں**: ٹوکنز کو ٹریک کرنے کے لیے `SHOW_USAGE=1` سیٹ کریں
4. **بیچ پروسیسنگ**: متعدد پرامپٹس کو ترتیب وار پروسیس کریں
5. **کم سے کم ٹوکنز**: فوری جوابات کے لیے تاخیر کو کم کریں

---

## 🎯 نمونہ ورک فلو

### سب کچھ جانچیں
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### ماڈلز کا بینچ مارک
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG پائپ لائن
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### ملٹی ایجنٹ سسٹم
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**فوری مدد**: کسی بھی نمونے کو `--help` کے ساتھ `samples` ڈائریکٹری سے چلائیں یا ڈاکسٹرنگ چیک کریں:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**تمام نمونے اکتوبر 2025 میں Foundry Local SDK بہترین طریقوں کے ساتھ اپ ڈیٹ کیے گئے** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->