# نمونه جلسه ۶: مدل‌ها به عنوان ابزار

این نمونه یک مسیریاب ساده + ثبت ابزار را پیاده‌سازی می‌کند که بر اساس درخواست کاربر یک مدل را انتخاب کرده و نقطه پایانی سازگار با OpenAI در Foundry Local را فراخوانی می‌کند.

## فایل‌ها
- `router.py`: ثبت ساده و مسیریابی مبتنی بر اکتشافی؛ کشف نقطه پایانی + بررسی سلامت.

## اجرا (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## نکات
- مسیریاب از اکتشافات ساده کلمات کلیدی برای انتخاب بین ابزارهای `general`، `reasoning` و `code` استفاده می‌کند و در شروع `/v1/models` را چاپ می‌کند.
- تنظیمات از طریق متغیرهای محیطی:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## منابع
- Foundry Local (آموزش): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ادغام با SDKهای استنتاج: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.