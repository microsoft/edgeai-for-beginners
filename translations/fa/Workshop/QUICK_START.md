<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T21:39:30+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "fa"
}
-->
# راهنمای شروع سریع کارگاه

## پیش‌نیازها

### 1. نصب Foundry Local

راهنمای نصب رسمی را دنبال کنید:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. نصب وابستگی‌های پایتون

از دایرکتوری کارگاه:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## اجرای نمونه‌های کارگاه

### جلسه 01: چت پایه

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**متغیرهای محیطی:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### جلسه 02: خط لوله RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**متغیرهای محیطی:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### جلسه 02: ارزیابی RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**توجه**: نیاز به نصب وابستگی‌های اضافی از طریق `requirements.txt` دارد

### جلسه 03: ارزیابی عملکرد

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**متغیرهای محیطی:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**خروجی**: JSON شامل معیارهای تأخیر، توان عملیاتی و اولین توکن

### جلسه 04: مقایسه مدل‌ها

```bash
cd Workshop/samples
python -m session04.model_compare
```

**متغیرهای محیطی:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### جلسه 05: هماهنگی چند عامل

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**متغیرهای محیطی:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### جلسه 06: مسیریاب مدل

```bash
cd Workshop/samples
python -m session06.models_router
```

**منطق مسیریابی را آزمایش می‌کند** با اهداف مختلف (کد، خلاصه‌سازی، طبقه‌بندی)

### جلسه 06: خط لوله

```bash
python -m session06.models_pipeline
```

**خط لوله پیچیده چند مرحله‌ای** با برنامه‌ریزی، اجرا و اصلاح

## اسکریپت‌ها

### خروجی گزارش ارزیابی عملکرد

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**خروجی**: جدول Markdown + معیارهای JSON

### بررسی الگوهای CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**هدف**: شناسایی الگوهای CLI منسوخ در مستندات

## آزمایش‌ها

### آزمایش‌های اولیه

```bash
cd Workshop
python -m tests.smoke
```

**آزمایش‌ها**: عملکرد پایه نمونه‌های کلیدی

## رفع مشکلات

### سرویس اجرا نمی‌شود

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### خطاهای وارد کردن ماژول

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### خطاهای اتصال

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### مدل پیدا نشد

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## مرجع متغیرهای محیطی

### پیکربندی اصلی
| متغیر | پیش‌فرض | توضیحات |
|-------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | متغیر | نام مستعار مدل برای استفاده |
| `FOUNDRY_LOCAL_ENDPOINT` | خودکار | جایگزینی نقطه پایانی سرویس |
| `SHOW_USAGE` | `0` | نمایش آمار استفاده از توکن |
| `RETRY_ON_FAIL` | `1` | فعال کردن منطق تلاش مجدد |
| `RETRY_BACKOFF` | `1.0` | تأخیر اولیه تلاش مجدد (ثانیه) |

### مخصوص جلسه
| متغیر | پیش‌فرض | توضیحات |
|-------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | مدل جاسازی |
| `RAG_QUESTION` | نمونه را ببینید | سوال آزمایشی RAG |
| `BENCH_MODELS` | متغیر | مدل‌های جدا شده با کاما |
| `BENCH_ROUNDS` | `3` | تکرارهای ارزیابی عملکرد |
| `BENCH_PROMPT` | نمونه را ببینید | درخواست ارزیابی عملکرد |
| `BENCH_STREAM` | `0` | اندازه‌گیری تأخیر اولین توکن |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | مدل عامل اصلی |
| `AGENT_MODEL_EDITOR` | اصلی | مدل عامل ویرایشگر |
| `SLM_ALIAS` | `phi-4-mini` | مدل زبان کوچک |
| `LLM_ALIAS` | `qwen2.5-7b` | مدل زبان بزرگ |
| `COMPARE_PROMPT` | نمونه را ببینید | درخواست مقایسه |

## مدل‌های پیشنهادی

### توسعه و آزمایش
- **phi-4-mini** - کیفیت و سرعت متعادل
- **qwen2.5-0.5b** - بسیار سریع برای طبقه‌بندی
- **gemma-2-2b** - کیفیت خوب، سرعت متوسط

### سناریوهای تولید
- **phi-4-mini** - کاربرد عمومی
- **deepseek-coder-1.3b** - تولید کد
- **qwen2.5-7b** - پاسخ‌های با کیفیت بالا

## مستندات SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## دریافت کمک

1. وضعیت سرویس را بررسی کنید: `foundry service status`
2. لاگ‌ها را مشاهده کنید: لاگ‌های سرویس Foundry Local را بررسی کنید
3. مستندات SDK را بررسی کنید: https://github.com/microsoft/Foundry-Local
4. کد نمونه را مرور کنید: همه نمونه‌ها دارای توضیحات دقیق هستند

## مراحل بعدی

1. تمام جلسات کارگاه را به ترتیب کامل کنید
2. با مدل‌های مختلف آزمایش کنید
3. نمونه‌ها را برای موارد استفاده خود تغییر دهید

---

**آخرین به‌روزرسانی**: 2025-01-08  
**نسخه کارگاه**: آخرین  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->