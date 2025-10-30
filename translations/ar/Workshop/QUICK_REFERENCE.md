<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:21:31+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ar"
}
-->
# عينات ورشة العمل - بطاقة مرجعية سريعة

**آخر تحديث**: 8 أكتوبر 2025

---

## 🚀 البداية السريعة

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

## 📂 نظرة عامة على العينات

| الجلسة | العينة | الهدف | الوقت |
|---------|--------|---------|------|
| 01 | `chat_bootstrap.py` | دردشة أساسية + بث | ~30 ثانية |
| 02 | `rag_pipeline.py` | RAG مع التضمينات | ~45 ثانية |
| 02 | `rag_eval_ragas.py` | تقييم RAG | ~60 ثانية |
| 03 | `benchmark_oss_models.py` | قياس أداء النماذج | ~2 دقيقة |
| 04 | `model_compare.py` | SLM مقابل LLM | ~45 ثانية |
| 05 | `agents_orchestrator.py` | نظام متعدد الوكلاء | ~60 ثانية |
| 06 | `models_router.py` | توجيه النوايا | ~45 ثانية |
| 06 | `models_pipeline.py` | خط أنابيب متعدد الخطوات | ~60 ثانية |

---

## 🛠️ متغيرات البيئة

### أساسية
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### خاصة بالجلسة
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

## ✅ التحقق والاختبار

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

## 🐛 استكشاف الأخطاء وإصلاحها

### خطأ في الاتصال
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### خطأ في الاستيراد
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### النموذج غير موجود
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### الأداء البطيء
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 الأنماط الشائعة

### دردشة أساسية
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### الحصول على العميل
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### معالجة الأخطاء
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### البث
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

## 📊 اختيار النموذج

| النموذج | الحجم | الأفضل لـ | السرعة |
|-------|------|----------|-------|
| `qwen2.5-0.5b` | 0.5B | التصنيف السريع | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | توليد الكود السريع | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | الكتابة الإبداعية | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | الكود، إعادة الهيكلة | ⚡⚡ |
| `phi-4-mini` | 4B | عام، التلخيص | ⚡⚡ |
| `qwen2.5-7b` | 7B | التفكير المعقد | ⚡ |

---

## 🔗 الموارد

- **وثائق SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **المرجع السريع**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **ملخص التحديثات**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **ملاحظات الترحيل**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 نصائح

1. **تخزين العملاء مؤقتًا**: يقوم `workshop_utils` بذلك نيابةً عنك
2. **استخدام نماذج أصغر**: ابدأ بـ `qwen2.5-0.5b` للاختبار
3. **تمكين إحصائيات الاستخدام**: قم بتعيين `SHOW_USAGE=1` لتتبع الرموز
4. **المعالجة الدُفعية**: قم بمعالجة عدة مطالبات بشكل متسلسل
5. **تقليل max_tokens**: يقلل من زمن الاستجابة للحصول على ردود سريعة

---

## 🎯 تدفقات العمل النموذجية

### اختبار كل شيء
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### قياس أداء النماذج
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### خط أنابيب RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### نظام متعدد الوكلاء
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**مساعدة سريعة**: قم بتشغيل أي عينة باستخدام `--help` من دليل `samples` أو تحقق من docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**تم تحديث جميع العينات في أكتوبر 2025 مع أفضل ممارسات Foundry Local SDK** ✨

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.