# نمونه ۰۲: یکپارچه‌سازی SDK OpenAI

نمایش یکپارچه‌سازی پیشرفته با SDK پایتون OpenAI، پشتیبانی از Foundry Local مایکروسافت و Azure OpenAI با پاسخ‌های استریم و مدیریت صحیح خطا.

## مرور کلی

این نمونه موارد زیر را نشان می‌دهد:
- تغییر بدون مشکل بین Foundry Local و Azure OpenAI
- تکمیل چت استریم برای تجربه بهتر کاربر
- استفاده صحیح از SDK FoundryLocalManager
- مدیریت خطاهای قوی و مکانیزم‌های جایگزین
- الگوهای کدنویسی آماده برای تولید

## پیش‌نیازها

- **Foundry Local**: نصب شده و در حال اجرا (برای استنتاج محلی)
- **پایتون**: نسخه ۳.۸ یا بالاتر با SDK OpenAI
- **Azure OpenAI**: نقطه پایانی معتبر و کلید API (برای استنتاج ابری)

## نصب

۱. **راه‌اندازی محیط پایتون:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

۲. **نصب وابستگی‌ها:**
   ```cmd
   pip install -r requirements.txt
   ```

۳. **شروع Foundry Local (برای حالت محلی):**
   ```cmd
   foundry model run phi-4-mini
   ```


## سناریوهای استفاده

### Foundry Local (پیش‌فرض)

**گزینه ۱: استفاده از FoundryLocalManager (توصیه‌شده)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**گزینه ۲: پیکربندی دستی**
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


## معماری کد

### الگوی کارخانه کلاینت

این نمونه از الگوی کارخانه برای ایجاد کلاینت‌های مناسب استفاده می‌کند:

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


### پاسخ‌های استریم

این نمونه استریم را برای تولید پاسخ‌های بلادرنگ نشان می‌دهد:

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


## متغیرهای محیطی

### پیکربندی Foundry Local

| متغیر | توضیحات | پیش‌فرض | ضروری |
|-------|----------|---------|--------|
| `MODEL` | نام مستعار مدل برای استفاده | `phi-4-mini` | خیر |
| `BASE_URL` | نقطه پایانی Foundry Local | `http://localhost:8000` | خیر |
| `API_KEY` | کلید API (اختیاری برای حالت محلی) | `""` | خیر |

### پیکربندی Azure OpenAI

| متغیر | توضیحات | پیش‌فرض | ضروری |
|-------|----------|---------|--------|
| `AZURE_OPENAI_ENDPOINT` | نقطه پایانی منبع Azure OpenAI | - | بله |
| `AZURE_OPENAI_API_KEY` | کلید API Azure OpenAI | - | بله |
| `AZURE_OPENAI_API_VERSION` | نسخه API | `2024-08-01-preview` | خیر |
| `MODEL` | نام استقرار Azure | `your-deployment-name` | بله |

## ویژگی‌های پیشرفته

### کشف خودکار سرویس

این نمونه به‌طور خودکار سرویس مناسب را بر اساس متغیرهای محیطی تشخیص می‌دهد:

۱. **حالت Azure**: اگر `AZURE_OPENAI_ENDPOINT` و `AZURE_OPENAI_API_KEY` تنظیم شده باشند
۲. **حالت SDK Foundry**: اگر SDK Foundry Local در دسترس باشد
۳. **حالت دستی**: بازگشت به پیکربندی دستی

### مدیریت خطا

- بازگشت بدون مشکل از SDK به پیکربندی دستی
- پیام‌های خطای واضح برای رفع اشکال
- مدیریت صحیح استثناها برای مشکلات شبکه
- اعتبارسنجی متغیرهای محیطی ضروری

## ملاحظات عملکرد

### مزایا و معایب محلی در مقابل ابری

**مزایای Foundry Local:**
- ✅ بدون هزینه API
- ✅ حفظ حریم خصوصی داده‌ها (هیچ داده‌ای دستگاه را ترک نمی‌کند)
- ✅ تأخیر کم برای مدل‌های پشتیبانی‌شده
- ✅ کارکرد آفلاین

**مزایای Azure OpenAI:**
- ✅ دسترسی به مدل‌های بزرگ جدید
- ✅ توان عملیاتی بالاتر
- ✅ بدون نیاز به محاسبات محلی
- ✅ SLA در سطح سازمانی

## رفع اشکال

### مشکلات رایج

۱. **هشدار "امکان استفاده از SDK Foundry وجود ندارد":**
   ```cmd
   pip install foundry-local-sdk
   ```

۲. **خطاهای احراز هویت Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

۳. **مدل در دسترس نیست:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### بررسی سلامت

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## مراحل بعدی

- **نمونه ۰۳**: کشف مدل و ارزیابی عملکرد
- **نمونه ۰۴**: ساخت یک برنامه Chainlit RAG
- **نمونه ۰۵**: هماهنگی چند عامل
- **نمونه ۰۶**: مسیریابی مدل‌ها به‌عنوان ابزار

## منابع

- [مستندات Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [مرجع SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [مستندات SDK پایتون OpenAI](https://github.com/openai/openai-python)
- [راهنمای تکمیل‌های استریم](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

