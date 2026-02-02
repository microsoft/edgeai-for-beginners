# نمونه استفاده از Foundry Local به عنوان API

این نمونه نشان می‌دهد که چگونه می‌توان از Microsoft Foundry Local به عنوان یک سرویس REST API استفاده کرد، بدون نیاز به OpenAI SDK. این نمونه الگوهای یکپارچه‌سازی مستقیم HTTP را برای کنترل و سفارشی‌سازی بیشتر ارائه می‌دهد.

## مرور کلی

بر اساس الگوهای رسمی Microsoft Foundry Local، این نمونه موارد زیر را ارائه می‌دهد:
- یکپارچه‌سازی مستقیم REST API با FoundryLocalManager
- پیاده‌سازی کلاینت HTTP سفارشی
- مدیریت مدل و نظارت بر سلامت
- مدیریت پاسخ‌های استریم و غیر استریم
- مدیریت خطا و منطق تلاش مجدد آماده برای تولید

## پیش‌نیازها

1. **نصب Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **وابستگی‌های پایتون**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```


## معماری

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```


## ویژگی‌های کلیدی

### 1. **یکپارچه‌سازی مستقیم HTTP**
- فراخوانی‌های خالص REST API بدون وابستگی به SDK
- احراز هویت و هدرهای سفارشی
- کنترل کامل بر مدیریت درخواست/پاسخ

### 2. **مدیریت مدل**
- بارگذاری و تخلیه پویا مدل‌ها
- نظارت بر سلامت و بررسی وضعیت
- جمع‌آوری معیارهای عملکرد

### 3. **الگوهای تولید**
- مکانیزم‌های تلاش مجدد با بک‌آف نمایی
- مدار شکن برای تحمل خطا
- ثبت و نظارت جامع

### 4. **مدیریت پاسخ انعطاف‌پذیر**
- پاسخ‌های استریم برای برنامه‌های زمان واقعی
- پردازش دسته‌ای برای سناریوهای با توان بالا
- تجزیه و اعتبارسنجی پاسخ سفارشی

## مثال‌های استفاده

### یکپارچه‌سازی پایه API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### یکپارچه‌سازی استریم
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### نظارت بر سلامت
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```


## ساختار فایل

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```


## یکپارچه‌سازی Microsoft Foundry Local

این نمونه از الگوهای رسمی Microsoft پیروی می‌کند:

1. **یکپارچه‌سازی SDK**: استفاده از `FoundryLocalManager` برای مدیریت سرویس
2. **نقاط پایانی REST**: فراخوانی مستقیم `/v1/chat/completions` و سایر نقاط پایانی
3. **احراز هویت**: مدیریت صحیح کلید API برای سرویس‌های محلی
4. **مدیریت مدل**: لیست کاتالوگ، دانلود و الگوهای بارگذاری
5. **مدیریت خطا**: کدها و پاسخ‌های خطای توصیه‌شده توسط Microsoft

## شروع به کار

1. **نصب وابستگی‌ها**
   ```bash
   pip install -r requirements.txt
   ```

2. **اجرای مثال پایه**
   ```bash
   python examples/basic_usage.py
   ```

3. **آزمایش استریم**
   ```bash
   python examples/streaming.py
   ```

4. **راه‌اندازی تولید**
   ```bash
   python examples/production.py
   ```


## پیکربندی

متغیرهای محیطی برای سفارشی‌سازی:
- `FOUNDRY_MODEL`: مدل پیش‌فرض برای استفاده (پیش‌فرض: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: زمان انتظار درخواست به ثانیه (پیش‌فرض: 30)
- `FOUNDRY_RETRIES`: تعداد تلاش‌های مجدد (پیش‌فرض: 3)
- `FOUNDRY_LOG_LEVEL`: سطح ثبت وقایع (پیش‌فرض: "INFO")

## بهترین شیوه‌ها

1. **مدیریت اتصال**: استفاده مجدد از اتصالات HTTP برای عملکرد بهتر
2. **مدیریت خطا**: پیاده‌سازی منطق تلاش مجدد با بک‌آف نمایی
3. **نظارت بر منابع**: ردیابی استفاده از حافظه مدل و عملکرد
4. **امنیت**: استفاده از احراز هویت مناسب حتی برای سرویس‌های محلی
5. **آزمایش**: شامل آزمایش‌های واحد و یکپارچه

## رفع اشکال

### مشکلات رایج

**سرویس اجرا نمی‌شود**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**مشکلات بارگذاری مدل**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**خطاهای اتصال**
- بررسی کنید که Foundry Local روی پورت صحیح اجرا می‌شود
- تنظیمات فایروال را بررسی کنید
- اطمینان حاصل کنید که هدرهای احراز هویت صحیح هستند

## بهینه‌سازی عملکرد

1. **مدیریت اتصال**: استفاده از اشیاء جلسه برای درخواست‌های متعدد
2. **عملیات غیرهمزمان**: استفاده از asyncio برای درخواست‌های همزمان
3. **کشینگ**: کش کردن پاسخ‌های مدل در صورت مناسب بودن
4. **نظارت**: ردیابی زمان پاسخ‌ها و تنظیم زمان‌های انتظار

## نتایج یادگیری

پس از تکمیل این نمونه، شما درک خواهید کرد:
- یکپارچه‌سازی مستقیم REST API با Foundry Local
- الگوهای پیاده‌سازی کلاینت HTTP سفارشی
- مدیریت خطا و نظارت آماده برای تولید
- معماری سرویس Microsoft Foundry Local
- تکنیک‌های بهینه‌سازی عملکرد برای سرویس‌های هوش مصنوعی محلی

## مراحل بعدی

- بررسی نمونه 08: برنامه چت ویندوز 11
- آزمایش نمونه 09: ارکستراسیون چند عاملی
- یادگیری نمونه 10: Foundry Local به عنوان یکپارچه‌سازی ابزار‌ها

---

