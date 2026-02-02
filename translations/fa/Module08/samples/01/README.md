# نمونه ۰۱: گفتگوی سریع با استفاده از OpenAI SDK

یک مثال ساده از چت که نشان می‌دهد چگونه می‌توان از OpenAI SDK همراه با Microsoft Foundry Local برای استنتاج محلی هوش مصنوعی استفاده کرد.

## مرور کلی

این نمونه نشان می‌دهد که چگونه:
- از OpenAI Python SDK همراه با Foundry Local استفاده کنید
- تنظیمات Azure OpenAI و Foundry محلی را مدیریت کنید
- مدیریت صحیح خطاها و استراتژی‌های جایگزین را پیاده‌سازی کنید
- از FoundryLocalManager برای مدیریت سرویس استفاده کنید

## پیش‌نیازها

- **Foundry Local**: نصب شده و در مسیر PATH موجود باشد
- **پایتون**: نسخه ۳.۸ یا بالاتر
- **مدل**: یک مدل بارگذاری شده در Foundry Local (مانند `phi-4-mini`)

## نصب

1. **راه‌اندازی محیط پایتون:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **نصب وابستگی‌ها:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **راه‌اندازی سرویس Foundry Local و بارگذاری یک مدل:**
   ```cmd
   foundry model run phi-4-mini
   ```


## استفاده

### Foundry Local (پیش‌فرض)

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


## ویژگی‌های کد

### یکپارچگی FoundryLocalManager

این نمونه از SDK رسمی Foundry Local برای مدیریت صحیح سرویس استفاده می‌کند:

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


### مدیریت خطا

مدیریت خطای قوی با جایگزینی تنظیمات دستی:
- کشف خودکار سرویس
- کاهش تدریجی در صورت عدم دسترسی به SDK
- پیام‌های خطای واضح برای رفع اشکال

## متغیرهای محیطی

| متغیر | توضیحات | پیش‌فرض | ضروری |
|-------|---------|---------|--------|
| `MODEL` | نام یا نام مستعار مدل | `phi-4-mini` | خیر |
| `BASE_URL` | آدرس پایه Foundry Local | `http://localhost:8000` | خیر |
| `API_KEY` | کلید API (معمولاً برای محلی نیاز نیست) | `""` | خیر |
| `AZURE_OPENAI_ENDPOINT` | نقطه پایانی Azure OpenAI | - | برای Azure |
| `AZURE_OPENAI_API_KEY` | کلید API Azure OpenAI | - | برای Azure |
| `AZURE_OPENAI_API_VERSION` | نسخه API Azure | `2024-08-01-preview` | خیر |

## رفع اشکال

### مشکلات رایج

1. **هشدار "عدم امکان استفاده از Foundry SDK":**
   - نصب foundry-local-sdk: `pip install foundry-local-sdk`
   - یا تنظیم متغیرهای محیطی برای پیکربندی دستی

2. **اتصال رد شد:**
   - اطمینان حاصل کنید که Foundry Local در حال اجرا است: `foundry service status`
   - بررسی کنید که آیا یک مدل بارگذاری شده است: `foundry service ps`

3. **مدل یافت نشد:**
   - لیست مدل‌های موجود: `foundry model list`
   - بارگذاری یک مدل: `foundry model run phi-4-mini`

### تأیید

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## منابع

- [مستندات Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [مرجع API سازگار با OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

