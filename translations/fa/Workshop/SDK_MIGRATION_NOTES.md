<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:27:01+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "fa"
}
-->
# یادداشت‌های مهاجرت SDK محلی Foundry

## نمای کلی

تمام فایل‌های پایتون در پوشه Workshop به‌روزرسانی شده‌اند تا با الگوهای جدید از [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) رسمی مطابقت داشته باشند.

## خلاصه تغییرات

### زیرساخت اصلی (`workshop_utils.py`)

#### ویژگی‌های بهبود یافته:
- **پشتیبانی از جایگزینی نقطه پایانی**: اضافه شدن پشتیبانی از متغیر محیطی `FOUNDRY_LOCAL_ENDPOINT`
- **بهبود مدیریت خطا**: مدیریت بهتر استثناها با پیام‌های خطای دقیق‌تر
- **بهبود کش**: کلیدهای کش اکنون شامل نقطه پایانی برای سناریوهای چند نقطه پایانی هستند
- **بازگشت نمایی**: منطق تلاش مجدد اکنون از بازگشت نمایی برای قابلیت اطمینان بهتر استفاده می‌کند
- **حاشیه‌نویسی نوع**: اضافه شدن نکات نوع جامع برای پشتیبانی بهتر از IDE

#### قابلیت‌های جدید:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### برنامه‌های نمونه

#### جلسه 01: راه‌اندازی چت (`chat_bootstrap.py`)
- مدل پیش‌فرض از `phi-3.5-mini` به `phi-4-mini` به‌روزرسانی شد
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی
- بهبود مستندسازی با ارجاعات SDK

#### جلسه 02: خط لوله RAG (`rag_pipeline.py`)
- به‌روزرسانی برای استفاده از `phi-4-mini` به‌عنوان پیش‌فرض
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی
- بهبود مستندسازی با جزئیات متغیرهای محیطی

#### جلسه 02: ارزیابی RAG (`rag_eval_ragas.py`)
- به‌روزرسانی پیش‌فرض‌های مدل
- اضافه شدن پیکربندی نقطه پایانی
- بهبود مدیریت خطا

#### جلسه 03: محک‌زنی (`benchmark_oss_models.py`)
- به‌روزرسانی لیست مدل‌های پیش‌فرض برای شامل شدن `phi-4-mini`
- اضافه شدن مستندسازی جامع متغیرهای محیطی
- بهبود مستندسازی توابع
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی در سراسر

#### جلسه 04: مقایسه مدل‌ها (`model_compare.py`)
- مدل LLM پیش‌فرض از `gpt-oss-20b` به `qwen2.5-7b` به‌روزرسانی شد
- اضافه شدن پیکربندی نقطه پایانی
- بهبود مستندسازی

#### جلسه 05: هماهنگی چند عاملی (`agents_orchestrator.py`)
- اضافه شدن نکات نوع (تغییر `str | None` به `Optional[str]`)
- بهبود مستندسازی کلاس Agent
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی
- بهبود الگوی اولیه‌سازی

#### جلسه 06: مسیریابی مدل (`models_router.py`)
- اضافه شدن پیکربندی نقطه پایانی
- بهبود مستندسازی تشخیص قصد
- بهبود مستندسازی منطق مسیریابی

#### جلسه 06: خط لوله (`models_pipeline.py`)
- اضافه شدن مستندسازی جامع توابع
- بهبود مستندسازی مرحله به مرحله
- بهبود مدیریت خطا

### اسکریپت‌ها

#### خروجی محک‌زنی (`export_benchmark_markdown.py`)
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی
- به‌روزرسانی مدل‌های پیش‌فرض
- بهبود مستندسازی توابع
- بهبود مدیریت خطا

#### بررسی CLI (`lint_markdown_cli.py`)
- اضافه شدن لینک‌های ارجاع SDK
- بهبود مستندسازی استفاده

### تست‌ها

#### تست‌های دود (`smoke.py`)
- اضافه شدن پشتیبانی از جایگزینی نقطه پایانی
- بهبود مستندسازی
- بهبود مستندسازی موارد تست
- گزارش‌دهی بهتر خطا

## متغیرهای محیطی

تمام نمونه‌ها اکنون از این متغیرهای محیطی پشتیبانی می‌کنند:

### پیکربندی اصلی
- `FOUNDRY_LOCAL_ALIAS` - نام مستعار مدل برای استفاده (پیش‌فرض بسته به نمونه متفاوت است)
- `FOUNDRY_LOCAL_ENDPOINT` - جایگزینی نقطه پایانی سرویس (اختیاری)
- `SHOW_USAGE` - نمایش آمار استفاده از توکن‌ها (پیش‌فرض: "0")
- `RETRY_ON_FAIL` - فعال کردن منطق تلاش مجدد (پیش‌فرض: "1")
- `RETRY_BACKOFF` - تأخیر اولیه تلاش مجدد به ثانیه (پیش‌فرض: "1.0")

### نمونه‌های خاص
- `EMBED_MODEL` - مدل جاسازی برای نمونه‌های RAG
- `BENCH_MODELS` - مدل‌های جدا شده با کاما برای محک‌زنی
- `BENCH_ROUNDS` - تعداد دورهای محک‌زنی
- `BENCH_PROMPT` - درخواست آزمایشی برای محک‌زنی
- `BENCH_STREAM` - اندازه‌گیری تأخیر اولین توکن
- `RAG_QUESTION` - سوال آزمایشی برای نمونه‌های RAG
- `AGENT_MODEL_PRIMARY` - مدل عامل اصلی
- `AGENT_MODEL_EDITOR` - مدل عامل ویرایشگر
- `SLM_ALIAS` - نام مستعار مدل زبان کوچک
- `LLM_ALIAS` - نام مستعار مدل زبان بزرگ

## بهترین شیوه‌های SDK اجرا شده

### 1. اولیه‌سازی صحیح کلاینت
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

### 2. بازیابی اطلاعات مدل
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. مدیریت خطا
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. منطق تلاش مجدد با بازگشت نمایی
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

### 5. پشتیبانی از جریان
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

## راهنمای مهاجرت برای نمونه‌های سفارشی

اگر نمونه‌های جدید ایجاد می‌کنید یا نمونه‌های موجود را به‌روزرسانی می‌کنید:

1. **از کمک‌های `workshop_utils.py` استفاده کنید**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **پشتیبانی از جایگزینی نقطه پایانی**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **مستندسازی جامع اضافه کنید**:
   - متغیرهای محیطی در docstring
   - لینک ارجاع SDK
   - مثال‌های استفاده

4. **از نکات نوع استفاده کنید**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **مدیریت خطای مناسب را اجرا کنید**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## تست

تمام نمونه‌ها را می‌توان با استفاده از موارد زیر تست کرد:

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

## ارجاعات مستندسازی SDK

- **مخزن اصلی**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **مستندات API**: برای آخرین مستندات API به مخزن SDK مراجعه کنید

## تغییرات مهم

### انتظار نمی‌رود
تمام تغییرات با نسخه‌های قبلی سازگار هستند. به‌روزرسانی‌ها عمدتاً:
- ویژگی‌های اختیاری جدید اضافه می‌کنند (جایگزینی نقطه پایانی)
- مدیریت خطا را بهبود می‌بخشند
- مستندسازی را ارتقا می‌دهند
- نام مدل‌های پیش‌فرض را به توصیه‌های فعلی به‌روزرسانی می‌کنند

### بهبودهای اختیاری
ممکن است بخواهید کد خود را به‌روزرسانی کنید تا از موارد زیر استفاده کنید:
- `FOUNDRY_LOCAL_ENDPOINT` برای کنترل صریح نقطه پایانی
- `SHOW_USAGE=1` برای مشاهده استفاده از توکن‌ها
- به‌روزرسانی پیش‌فرض‌های مدل (`phi-4-mini` به جای `phi-3.5-mini`)

## مشکلات رایج و راه‌حل‌ها

### مشکل: "اولیه‌سازی کلاینت شکست خورد"
**راه‌حل**: اطمینان حاصل کنید که سرویس Foundry Local در حال اجرا است:
```bash
foundry service start
foundry model run phi-4-mini
```

### مشکل: "مدل یافت نشد"
**راه‌حل**: مدل‌های موجود را بررسی کنید:
```bash
foundry model list
```

### مشکل: خطاهای اتصال نقطه پایانی
**راه‌حل**: نقطه پایانی را بررسی کنید:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## مراحل بعدی

1. **به‌روزرسانی نمونه‌های Module08**: الگوهای مشابه را به Module08/samples اعمال کنید
2. **اضافه کردن تست‌های یکپارچه‌سازی**: ایجاد مجموعه تست جامع
3. **محک‌زنی عملکرد**: مقایسه عملکرد قبل/بعد
4. **به‌روزرسانی مستندات**: README اصلی را با الگوهای جدید به‌روزرسانی کنید

## دستورالعمل‌های مشارکت

هنگام اضافه کردن نمونه‌های جدید:
1. از `workshop_utils.py` برای سازگاری استفاده کنید
2. الگوی موجود در نمونه‌های فعلی را دنبال کنید
3. docstring‌های جامع اضافه کنید
4. لینک‌های ارجاع SDK را شامل کنید
5. پشتیبانی از جایگزینی نقطه پایانی را اضافه کنید
6. نکات نوع مناسب را اضافه کنید
7. مثال‌های استفاده را در docstring شامل کنید

## سازگاری نسخه

این به‌روزرسانی‌ها با موارد زیر سازگار هستند:
- `foundry-local-sdk` (آخرین نسخه)
- `openai>=1.30.0`
- پایتون 3.8+

---

**آخرین به‌روزرسانی**: 2025-01-08  
**نگهدارنده**: تیم کارگاه EdgeAI  
**نسخه SDK**: Foundry Local SDK (آخرین 0.7.117+67073234e7)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.