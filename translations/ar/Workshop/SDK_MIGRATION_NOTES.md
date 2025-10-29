<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:22:17+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ar"
}
-->
# ملاحظات حول ترقية SDK المحلي لـ Foundry

## نظرة عامة

تم تحديث جميع ملفات Python في مجلد Workshop لتتبع أحدث الأنماط من [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## ملخص التغييرات

### البنية التحتية الأساسية (`workshop_utils.py`)

#### ميزات محسّنة:
- **دعم تجاوز نقطة النهاية**: إضافة دعم لمتغير البيئة `FOUNDRY_LOCAL_ENDPOINT`
- **تحسين معالجة الأخطاء**: تحسين التعامل مع الاستثناءات مع رسائل خطأ مفصلة
- **تحسين التخزين المؤقت**: الآن تتضمن مفاتيح التخزين المؤقت نقطة النهاية لدعم سيناريوهات متعددة النقاط
- **الرجوع التدريجي**: منطق إعادة المحاولة يستخدم الآن الرجوع التدريجي لتحسين الموثوقية
- **تعليقات النوع**: إضافة تلميحات نوع شاملة لدعم أفضل في بيئة التطوير

#### قدرات جديدة:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### التطبيقات النموذجية

#### الجلسة 01: إعداد الدردشة (`chat_bootstrap.py`)
- تحديث النموذج الافتراضي من `phi-3.5-mini` إلى `phi-4-mini`
- إضافة دعم تجاوز نقطة النهاية
- تحسين التوثيق مع إشارات إلى SDK

#### الجلسة 02: خط أنابيب RAG (`rag_pipeline.py`)
- تحديث لاستخدام `phi-4-mini` كنموذج افتراضي
- إضافة دعم تجاوز نقطة النهاية
- تحسين التوثيق مع تفاصيل متغيرات البيئة

#### الجلسة 02: تقييم RAG (`rag_eval_ragas.py`)
- تحديث النماذج الافتراضية
- إضافة تكوين نقطة النهاية
- تحسين معالجة الأخطاء

#### الجلسة 03: قياس الأداء (`benchmark_oss_models.py`)
- تحديث قائمة النماذج الافتراضية لتشمل `phi-4-mini`
- إضافة توثيق شامل لمتغيرات البيئة
- تحسين توثيق الوظائف
- إضافة دعم تجاوز نقطة النهاية في جميع الأنحاء

#### الجلسة 04: مقارنة النماذج (`model_compare.py`)
- تحديث النموذج الافتراضي LLM من `gpt-oss-20b` إلى `qwen2.5-7b`
- إضافة تكوين نقطة النهاية
- تحسين التوثيق

#### الجلسة 05: تنسيق الوكلاء المتعددين (`agents_orchestrator.py`)
- إضافة تلميحات النوع (تغيير `str | None` إلى `Optional[str]`)
- تحسين توثيق فئة الوكيل
- إضافة دعم تجاوز نقطة النهاية
- تحسين نمط التهيئة

#### الجلسة 06: موجه النماذج (`models_router.py`)
- إضافة تكوين نقطة النهاية
- تحسين توثيق اكتشاف النوايا
- تحسين توثيق منطق التوجيه

#### الجلسة 06: خط الأنابيب (`models_pipeline.py`)
- إضافة توثيق شامل للوظائف
- تحسين التوثيق خطوة بخطوة
- تحسين معالجة الأخطاء

### السكربتات

#### تصدير قياس الأداء (`export_benchmark_markdown.py`)
- إضافة دعم تجاوز نقطة النهاية
- تحديث النماذج الافتراضية
- تحسين توثيق الوظائف
- تحسين معالجة الأخطاء

#### مدقق CLI (`lint_markdown_cli.py`)
- إضافة روابط مرجعية لـ SDK
- تحسين توثيق الاستخدام

### الاختبارات

#### اختبارات الدخان (`smoke.py`)
- إضافة دعم تجاوز نقطة النهاية
- تحسين التوثيق
- تحسين توثيق حالات الاختبار
- تحسين تقارير الأخطاء

## متغيرات البيئة

جميع العينات تدعم الآن هذه المتغيرات البيئية:

### التكوين الأساسي
- `FOUNDRY_LOCAL_ALIAS` - الاسم المستعار للنموذج المستخدم (الافتراضي يختلف حسب العينة)
- `FOUNDRY_LOCAL_ENDPOINT` - تجاوز نقطة خدمة (اختياري)
- `SHOW_USAGE` - عرض إحصائيات استخدام الرموز (الافتراضي: "0")
- `RETRY_ON_FAIL` - تمكين منطق إعادة المحاولة (الافتراضي: "1")
- `RETRY_BACKOFF` - تأخير إعادة المحاولة الأولي بالثواني (الافتراضي: "1.0")

### خاصة بالعينة
- `EMBED_MODEL` - نموذج التضمين لعينات RAG
- `BENCH_MODELS` - النماذج مفصولة بفواصل لقياس الأداء
- `BENCH_ROUNDS` - عدد جولات قياس الأداء
- `BENCH_PROMPT` - موجه الاختبار لقياس الأداء
- `BENCH_STREAM` - قياس زمن استجابة الرمز الأول
- `RAG_QUESTION` - سؤال الاختبار لعينة RAG
- `AGENT_MODEL_PRIMARY` - نموذج الوكيل الأساسي
- `AGENT_MODEL_EDITOR` - نموذج وكيل المحرر
- `SLM_ALIAS` - الاسم المستعار للنموذج اللغوي الصغير
- `LLM_ALIAS` - الاسم المستعار للنموذج اللغوي الكبير

## أفضل الممارسات المطبقة في SDK

### 1. تهيئة العميل بشكل صحيح
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. استرجاع معلومات النموذج
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. معالجة الأخطاء
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. منطق إعادة المحاولة مع الرجوع التدريجي
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. دعم البث
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## دليل الترقية للعينة المخصصة

إذا كنت تقوم بإنشاء عينات جديدة أو تحديث عينات موجودة:

1. **استخدام مساعدي `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **دعم تجاوز نقطة النهاية**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **إضافة توثيق شامل**:
   - متغيرات البيئة في التعليقات
   - رابط مرجعي لـ SDK
   - أمثلة على الاستخدام

4. **استخدام تلميحات النوع**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **تنفيذ معالجة الأخطاء بشكل صحيح**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## الاختبار

يمكن اختبار جميع العينات باستخدام:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## مراجع توثيق SDK

- **المستودع الرئيسي**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **توثيق API**: تحقق من مستودع SDK للحصول على أحدث وثائق API

## تغييرات كبيرة

### لا توجد تغييرات متوقعة
جميع التغييرات متوافقة مع الإصدارات السابقة. التحديثات بشكل أساسي:
- إضافة ميزات اختيارية جديدة (تجاوز نقطة النهاية)
- تحسين معالجة الأخطاء
- تحسين التوثيق
- تحديث أسماء النماذج الافتراضية لتوصيات الحالية

### تحسينات اختيارية
قد ترغب في تحديث الكود الخاص بك لاستخدام:
- `FOUNDRY_LOCAL_ENDPOINT` للتحكم الصريح في نقطة النهاية
- `SHOW_USAGE=1` لعرض استخدام الرموز
- تحديث النماذج الافتراضية (`phi-4-mini` بدلاً من `phi-3.5-mini`)

## المشاكل الشائعة والحلول

### المشكلة: "فشل تهيئة العميل"
**الحل**: تأكد من تشغيل خدمة Foundry Local:
```bash
foundry service start
foundry model run phi-4-mini
```

### المشكلة: "النموذج غير موجود"
**الحل**: تحقق من النماذج المتاحة:
```bash
foundry model list
```

### المشكلة: أخطاء اتصال نقطة النهاية
**الحل**: تحقق من نقطة النهاية:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## الخطوات التالية

1. **تحديث عينات Module08**: تطبيق أنماط مشابهة على Module08/samples
2. **إضافة اختبارات تكامل**: إنشاء مجموعة اختبارات شاملة
3. **قياس الأداء**: مقارنة الأداء قبل وبعد
4. **تحديث التوثيق**: تحديث README الرئيسي بالأنماط الجديدة

## إرشادات المساهمة

عند إضافة عينات جديدة:
1. استخدم `workshop_utils.py` لتحقيق التناسق
2. اتبع النمط في العينات الحالية
3. أضف تعليقات شاملة
4. قم بتضمين روابط مرجعية لـ SDK
5. دعم تجاوز نقطة النهاية
6. أضف تلميحات النوع المناسبة
7. قم بتضمين أمثلة الاستخدام في التعليقات

## توافق الإصدارات

هذه التحديثات متوافقة مع:
- `foundry-local-sdk` (الأحدث)
- `openai>=1.30.0`
- Python 3.8+

---

**آخر تحديث**: 2025-01-08  
**المسؤول**: فريق EdgeAI Workshop  
**إصدار SDK**: Foundry Local SDK (الأحدث 0.7.117+67073234e7)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.