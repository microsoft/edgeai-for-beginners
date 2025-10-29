<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:26:42+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "fa"
}
-->
# نمونه‌های کارگاه - خلاصه به‌روزرسانی Foundry Local SDK

## مرور کلی

تمام نمونه‌های پایتون در پوشه `Workshop/samples` به‌روزرسانی شده‌اند تا از بهترین شیوه‌های Foundry Local SDK پیروی کنند و هماهنگی در سراسر کارگاه تضمین شود.

**تاریخ**: ۸ اکتبر ۲۰۲۵  
**دامنه**: ۹ فایل پایتون در ۶ جلسه کارگاه  
**تمرکز اصلی**: مدیریت خطا، مستندسازی، الگوهای SDK، تجربه کاربری

---

## فایل‌های به‌روزرسانی‌شده

### جلسه ۰۱: شروع به کار
- ✅ `chat_bootstrap.py` - مثال‌های پایه‌ای چت و استریم

### جلسه ۰۲: راه‌حل‌های RAG
- ✅ `rag_pipeline.py` - پیاده‌سازی RAG با استفاده از embeddings
- ✅ `rag_eval_ragas.py` - ارزیابی RAG با معیارهای RAGAS

### جلسه ۰۳: مدل‌های متن‌باز
- ✅ `benchmark_oss_models.py` - ارزیابی چند مدل

### جلسه ۰۴: مدل‌های پیشرفته
- ✅ `model_compare.py` - مقایسه SLM و LLM

### جلسه ۰۵: عوامل هوش مصنوعی
- ✅ `agents_orchestrator.py` - هماهنگی چند عامل

### جلسه ۰۶: مدل‌ها به‌عنوان ابزار
- ✅ `models_router.py` - مسیریابی مدل مبتنی بر هدف
- ✅ `models_pipeline.py` - خط لوله چند مرحله‌ای مسیریابی‌شده

### زیرساخت پشتیبانی
- ✅ `workshop_utils.py` - قبلاً از بهترین شیوه‌ها پیروی می‌کرد (نیازی به تغییر نبود)

---

## بهبودهای کلیدی

### ۱. بهبود مدیریت خطا

**قبل:**
```python
manager, client, model_id = get_client(alias)
```

**بعد:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**مزایا:**
- مدیریت خطای روان با پیام‌های خطای واضح
- نکات قابل اجرا برای رفع مشکلات
- کدهای خروجی مناسب برای اسکریپت‌ها

### ۲. مدیریت بهتر واردات

**قبل:**
```python
from sentence_transformers import SentenceTransformer
```

**بعد:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**مزایا:**
- راهنمایی واضح در صورت نبود وابستگی‌ها
- جلوگیری از خطاهای واردات مبهم
- دستورالعمل‌های نصب کاربرپسند

### ۳. مستندسازی جامع

**اضافه‌شده به تمام نمونه‌ها:**
- مستندسازی متغیرهای محیطی در docstrings
- لینک‌های مرجع SDK
- مثال‌های استفاده
- مستندسازی دقیق توابع/پارامترها
- اشاره‌گرهای نوع برای پشتیبانی بهتر از IDE

**مثال:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### ۴. بهبود بازخورد کاربر

**اضافه‌شده: لاگ‌گیری اطلاعاتی:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**شاخص‌های پیشرفت:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**خروجی ساختاریافته:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### ۵. ارزیابی قوی

**بهبودهای جلسه ۰۳:**
- مدیریت خطا برای هر مدل (ادامه در صورت خطا)
- گزارش‌دهی دقیق پیشرفت
- اجرای صحیح مراحل گرم‌کردن
- پشتیبانی از اندازه‌گیری تأخیر اولین توکن
- جداسازی واضح مراحل

### ۶. اشاره‌گرهای نوع سازگار

**اضافه‌شده در سراسر پروژه:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**مزایا:**
- تکمیل خودکار بهتر در IDE
- شناسایی زودهنگام خطاها
- کد خودمستند

### ۷. بهبود مسیریاب مدل

**بهبودهای جلسه ۰۶:**
- مستندسازی جامع تشخیص هدف
- توضیح الگوریتم انتخاب مدل
- لاگ‌های مسیریابی دقیق
- قالب‌بندی خروجی تست
- بازیابی خطا در تست‌های دسته‌ای

### ۸. هماهنگی چند عاملی

**بهبودهای جلسه ۰۵:**
- گزارش‌دهی پیشرفت مرحله به مرحله
- مدیریت خطا برای هر عامل
- ساختار واضح خط لوله
- مستندسازی بهتر مدیریت حافظه

---

## چک‌لیست تست

### پیش‌نیازها
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### تست هر نمونه

#### جلسه ۰۱
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### جلسه ۰۲
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### جلسه ۰۳
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### جلسه ۰۴
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### جلسه ۰۵
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### جلسه ۰۶
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## مرجع متغیرهای محیطی

### عمومی (تمام نمونه‌ها)
| متغیر | توضیحات | پیش‌فرض |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | نام مستعار مدل برای استفاده | بسته به نمونه متفاوت است |
| `FOUNDRY_LOCAL_ENDPOINT` | جایگزینی نقطه پایانی سرویس | به‌صورت خودکار شناسایی می‌شود |
| `SHOW_USAGE` | نمایش استفاده از توکن | `0` |
| `RETRY_ON_FAIL` | فعال‌سازی منطق تلاش مجدد | `1` |
| `RETRY_BACKOFF` | تأخیر اولیه تلاش مجدد | `1.0` |

### مختص نمونه
| متغیر | استفاده‌شده توسط | توضیحات |
|----------|---------|-------------|
| `EMBED_MODEL` | جلسه ۰۲ | نام مدل embedding |
| `RAG_QUESTION` | جلسه ۰۲ | سوال تست برای RAG |
| `BENCH_MODELS` | جلسه ۰۳ | مدل‌های جداشده با کاما برای ارزیابی |
| `BENCH_ROUNDS` | جلسه ۰۳ | تعداد دورهای ارزیابی |
| `BENCH_PROMPT` | جلسه ۰۳ | درخواست تست برای ارزیابی‌ها |
| `BENCH_STREAM` | جلسه ۰۳ | اندازه‌گیری تأخیر اولین توکن |
| `SLM_ALIAS` | جلسه ۰۴ | مدل زبان کوچک |
| `LLM_ALIAS` | جلسه ۰۴ | مدل زبان بزرگ |
| `COMPARE_PROMPT` | جلسه ۰۴ | درخواست تست مقایسه |
| `AGENT_MODEL_PRIMARY` | جلسه ۰۵ | مدل عامل اصلی |
| `AGENT_MODEL_EDITOR` | جلسه ۰۵ | مدل عامل ویرایشگر |
| `AGENT_QUESTION` | جلسه ۰۵ | سوال تست برای عوامل |
| `PIPELINE_TASK` | جلسه ۰۶ | وظیفه برای خط لوله |

---

## تغییرات شکسته

**هیچ‌کدام** - تمام تغییرات با نسخه‌های قبلی سازگار هستند.

اسکریپت‌های موجود همچنان کار خواهند کرد. ویژگی‌های جدید عبارتند از:
- متغیرهای محیطی اختیاری
- پیام‌های خطای بهبودیافته (عملکرد را مختل نمی‌کنند)
- لاگ‌گیری اضافی (قابل غیرفعال‌سازی)
- اشاره‌گرهای نوع بهتر (بدون تأثیر در زمان اجرا)

---

## بهترین شیوه‌های پیاده‌سازی‌شده

### ۱. همیشه از Workshop Utils استفاده کنید
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### ۲. الگوی مناسب مدیریت خطا
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ۳. لاگ‌گیری اطلاعاتی
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### ۴. اشاره‌گرهای نوع
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### ۵. Docstrings جامع
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### ۶. پشتیبانی از متغیرهای محیطی
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### ۷. کاهش تدریجی
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## مشکلات رایج و راه‌حل‌ها

### مشکل: خطاهای واردات
**راه‌حل:** نصب وابستگی‌های گمشده
```bash
pip install sentence-transformers ragas datasets numpy
```

### مشکل: خطاهای اتصال
**راه‌حل:** اطمینان حاصل کنید که Foundry Local در حال اجرا است
```bash
foundry service status
foundry model run phi-4-mini
```

### مشکل: مدل پیدا نشد
**راه‌حل:** مدل‌های موجود را بررسی کنید
```bash
foundry model ls
foundry model download <alias>
```

### مشکل: عملکرد کند
**راه‌حل:** از مدل‌های کوچک‌تر استفاده کنید یا پارامترها را تنظیم کنید
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## گام‌های بعدی

### ۱. تست تمام نمونه‌ها
چک‌لیست تست بالا را مرور کنید تا از عملکرد صحیح تمام نمونه‌ها اطمینان حاصل کنید.

### ۲. به‌روزرسانی مستندات
- فایل‌های مارک‌داون جلسات را با مثال‌های جدید به‌روزرسانی کنید.
- بخش عیب‌یابی را به README اصلی اضافه کنید.
- یک راهنمای مرجع سریع ایجاد کنید.

### ۳. ایجاد تست‌های یکپارچه
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### ۴. افزودن ارزیابی‌های عملکرد
بهبودهای عملکرد ناشی از بهبود مدیریت خطا را پیگیری کنید.

### ۵. بازخورد کاربران
بازخورد شرکت‌کنندگان کارگاه را در مورد موارد زیر جمع‌آوری کنید:
- وضوح پیام‌های خطا
- کامل بودن مستندات
- سهولت استفاده

---

## منابع

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **مرجع سریع**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **یادداشت‌های مهاجرت**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **مخزن اصلی**: https://github.com/microsoft/Foundry-Local  

---

## نگهداری

### افزودن نمونه‌های جدید
هنگام ایجاد نمونه‌های جدید، این الگوها را دنبال کنید:

1. از `workshop_utils` برای مدیریت کلاینت استفاده کنید.
2. مدیریت خطای جامع اضافه کنید.
3. پشتیبانی از متغیرهای محیطی را اضافه کنید.
4. اشاره‌گرهای نوع و docstrings اضافه کنید.
5. لاگ‌گیری اطلاعاتی ارائه دهید.
6. مثال‌های استفاده را در docstring قرار دهید.
7. لینک به مستندات SDK را اضافه کنید.

### بررسی به‌روزرسانی‌ها
هنگام بررسی به‌روزرسانی نمونه‌ها، موارد زیر را بررسی کنید:
- [ ] مدیریت خطا در تمام عملیات I/O
- [ ] اشاره‌گرهای نوع در توابع عمومی
- [ ] Docstrings جامع
- [ ] مستندسازی متغیرهای محیطی
- [ ] بازخورد اطلاعاتی به کاربر
- [ ] لینک‌های مرجع SDK
- [ ] سبک کدنویسی سازگار

---

**خلاصه**: تمام نمونه‌های پایتون کارگاه اکنون از بهترین شیوه‌های Foundry Local SDK پیروی می‌کنند و با مدیریت خطای بهبودیافته، مستندسازی جامع و تجربه کاربری بهتر به‌روزرسانی شده‌اند. هیچ تغییری که باعث اختلال شود وجود ندارد - تمام عملکردهای موجود حفظ و بهبود یافته‌اند.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.