# العينة 02: تكامل OpenAI SDK

عرض تكامل متقدم مع OpenAI Python SDK، يدعم كل من Microsoft Foundry Local وAzure OpenAI مع استجابات متدفقة ومعالجة أخطاء بشكل صحيح.

## نظرة عامة

تُبرز هذه العينة:
- التبديل السلس بين Foundry Local وAzure OpenAI
- استكمال المحادثات المتدفقة لتحسين تجربة المستخدم
- الاستخدام الصحيح لـ FoundryLocalManager SDK
- آليات معالجة الأخطاء والاحتياطيات القوية
- أنماط كود جاهزة للإنتاج

## المتطلبات الأساسية

- **Foundry Local**: مثبت ويعمل (للاستدلال المحلي)
- **Python**: الإصدار 3.8 أو أحدث مع OpenAI SDK
- **Azure OpenAI**: نقطة نهاية صالحة ومفتاح API (للاستدلال السحابي)

## التثبيت

1. **إعداد بيئة Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **تثبيت التبعيات:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **تشغيل Foundry Local (للوضع المحلي):**
   ```cmd
   foundry model run phi-4-mini
   ```


## سيناريوهات الاستخدام

### Foundry Local (الوضع الافتراضي)

**الخيار 1: استخدام FoundryLocalManager (موصى به)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**الخيار 2: التكوين اليدوي**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## هيكل الكود

### نمط مصنع العميل

تستخدم العينة نمط المصنع لإنشاء العملاء المناسبين:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### الاستجابات المتدفقة

تُظهر العينة كيفية استخدام التدفق لتوليد استجابات في الوقت الفعلي:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## متغيرات البيئة

### تكوين Foundry Local

| المتغير | الوصف | الافتراضي | مطلوب |
|---------|-------|----------|--------|
| `MODEL` | اسم النموذج المستخدم | `phi-4-mini` | لا |
| `BASE_URL` | نقطة نهاية Foundry Local | `http://localhost:8000` | لا |
| `API_KEY` | مفتاح API (اختياري للوضع المحلي) | `""` | لا |

### تكوين Azure OpenAI

| المتغير | الوصف | الافتراضي | مطلوب |
|---------|-------|----------|--------|
| `AZURE_OPENAI_ENDPOINT` | نقطة نهاية مورد Azure OpenAI | - | نعم |
| `AZURE_OPENAI_API_KEY` | مفتاح API لـ Azure OpenAI | - | نعم |
| `AZURE_OPENAI_API_VERSION` | إصدار API | `2024-08-01-preview` | لا |
| `MODEL` | اسم النشر في Azure | `your-deployment-name` | نعم |

## الميزات المتقدمة

### اكتشاف الخدمة التلقائي

تكتشف العينة الخدمة المناسبة تلقائيًا بناءً على متغيرات البيئة:

1. **وضع Azure**: إذا تم تعيين `AZURE_OPENAI_ENDPOINT` و`AZURE_OPENAI_API_KEY`
2. **وضع Foundry SDK**: إذا كان Foundry Local SDK متاحًا
3. **الوضع اليدوي**: الرجوع إلى التكوين اليدوي

### معالجة الأخطاء

- الانتقال السلس من SDK إلى التكوين اليدوي
- رسائل خطأ واضحة لاستكشاف الأخطاء وإصلاحها
- معالجة استثناءات الشبكة بشكل صحيح
- التحقق من متغيرات البيئة المطلوبة

## اعتبارات الأداء

### المفاضلة بين المحلي والسحابي

**مزايا Foundry Local:**
- ✅ لا توجد تكاليف API
- ✅ خصوصية البيانات (لا تغادر البيانات الجهاز)
- ✅ زمن استجابة منخفض للنماذج المدعومة
- ✅ يعمل بدون اتصال بالإنترنت

**مزايا Azure OpenAI:**
- ✅ الوصول إلى أحدث النماذج الكبيرة
- ✅ إنتاجية أعلى
- ✅ لا توجد متطلبات للحوسبة المحلية
- ✅ اتفاقية مستوى خدمة على مستوى المؤسسات

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

1. **تحذير "تعذر استخدام Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **أخطاء المصادقة في Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **النموذج غير متوفر:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### فحوصات الصحة

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## الخطوات التالية

- **العينة 03**: اكتشاف النماذج واختبار الأداء
- **العينة 04**: بناء تطبيق Chainlit RAG
- **العينة 05**: تنسيق متعدد الوكلاء
- **العينة 06**: توجيه النماذج كأدوات

## المراجع

- [وثائق Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [مرجع Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [وثائق OpenAI Python SDK](https://github.com/openai/openai-python)
- [دليل الاستكمالات المتدفقة](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

