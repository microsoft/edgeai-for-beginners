# العينة 01: دردشة سريعة باستخدام OpenAI SDK

مثال بسيط للدردشة يوضح كيفية استخدام OpenAI SDK مع Microsoft Foundry Local للاستدلال المحلي للذكاء الاصطناعي.

## نظرة عامة

يُظهر هذا المثال كيفية:
- استخدام OpenAI Python SDK مع Foundry Local
- التعامل مع تكوينات Azure OpenAI وFoundry المحلية
- تنفيذ معالجة الأخطاء بشكل صحيح واستراتيجيات التراجع
- استخدام FoundryLocalManager لإدارة الخدمات

## المتطلبات الأساسية

- **Foundry Local**: مثبت ومتوفر في PATH
- **Python**: الإصدار 3.8 أو أحدث
- **النموذج**: نموذج محمل في Foundry Local (مثل `phi-4-mini`)

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

3. **تشغيل خدمة Foundry Local وتحميل نموذج:**
   ```cmd
   foundry model run phi-4-mini
   ```


## الاستخدام

### Foundry Local (الإعداد الافتراضي)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## ميزات الكود

### تكامل FoundryLocalManager

يستخدم المثال SDK الرسمي لـ Foundry Local لإدارة الخدمات بشكل صحيح:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### معالجة الأخطاء

معالجة الأخطاء بشكل قوي مع التراجع إلى التكوين اليدوي:
- اكتشاف الخدمة تلقائيًا
- تدهور سلس إذا كان SDK غير متوفر
- رسائل خطأ واضحة لاستكشاف الأخطاء وإصلاحها

## متغيرات البيئة

| المتغير | الوصف | الافتراضي | مطلوب |
|---------|-------|-----------|--------|
| `MODEL` | اسم أو لقب النموذج | `phi-4-mini` | لا |
| `BASE_URL` | عنوان URL الأساسي لـ Foundry Local | `http://localhost:8000` | لا |
| `API_KEY` | مفتاح API (عادةً غير مطلوب محليًا) | `""` | لا |
| `AZURE_OPENAI_ENDPOINT` | نقطة نهاية Azure OpenAI | - | لـ Azure |
| `AZURE_OPENAI_API_KEY` | مفتاح API لـ Azure OpenAI | - | لـ Azure |
| `AZURE_OPENAI_API_VERSION` | إصدار API لـ Azure | `2024-08-01-preview` | لا |

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

1. **تحذير "تعذر استخدام Foundry SDK":**
   - قم بتثبيت foundry-local-sdk: `pip install foundry-local-sdk`
   - أو قم بتعيين متغيرات البيئة للتكوين اليدوي

2. **رفض الاتصال:**
   - تأكد من تشغيل Foundry Local: `foundry service status`
   - تحقق من تحميل نموذج: `foundry service ps`

3. **النموذج غير موجود:**
   - عرض النماذج المتاحة: `foundry model list`
   - تحميل نموذج: `foundry model run phi-4-mini`

### التحقق

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## المراجع

- [وثائق Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [مرجع API المتوافق مع OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

