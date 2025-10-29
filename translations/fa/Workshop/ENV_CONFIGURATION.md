<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T20:23:19+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "fa"
}
-->
# راهنمای تنظیم محیط

## مرور کلی

نمونه‌های کارگاه از متغیرهای محیطی برای تنظیمات استفاده می‌کنند که در فایل `.env` در ریشه مخزن متمرکز شده‌اند. این روش امکان سفارشی‌سازی آسان را بدون نیاز به تغییر کد فراهم می‌کند.

## شروع سریع

### 1. بررسی پیش‌نیازها

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. تنظیم محیط

فایل `.env` از پیش با مقادیر پیش‌فرض مناسب تنظیم شده است. اکثر کاربران نیازی به تغییر آن ندارند.

**اختیاری**: تنظیمات را بررسی و سفارشی کنید:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. اعمال تنظیمات

**برای اسکریپت‌های پایتون:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**برای نوت‌بوک‌ها:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## مرجع متغیرهای محیطی

### تنظیمات اصلی

| متغیر | پیش‌فرض | توضیحات |
|-------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | مدل پیش‌فرض برای نمونه‌ها |
| `FOUNDRY_LOCAL_ENDPOINT` | (خالی) | جایگزینی نقطه پایانی سرویس |
| `PYTHONPATH` | مسیرهای کارگاه | مسیر جستجوی ماژول‌های پایتون |

**زمان تنظیم FOUNDRY_LOCAL_ENDPOINT:**
- نمونه Foundry Local از راه دور
- تنظیمات پورت سفارشی
- جداسازی توسعه/تولید

**مثال:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### متغیرهای خاص جلسه

#### جلسه 02: خط لوله RAG
| متغیر | پیش‌فرض | هدف |
|-------|---------|-----|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | مدل جاسازی |
| `RAG_QUESTION` | از پیش تنظیم شده | سوال آزمایشی |

#### جلسه 03: ارزیابی
| متغیر | پیش‌فرض | هدف |
|-------|---------|-----|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | مدل‌های ارزیابی |
| `BENCH_ROUNDS` | `3` | تعداد تکرار برای هر مدل |
| `BENCH_PROMPT` | از پیش تنظیم شده | درخواست آزمایشی |
| `BENCH_STREAM` | `0` | اندازه‌گیری تأخیر اولین توکن |

#### جلسه 04: مقایسه مدل‌ها
| متغیر | پیش‌فرض | هدف |
|-------|---------|-----|
| `SLM_ALIAS` | `phi-4-mini` | مدل زبان کوچک |
| `LLM_ALIAS` | `qwen2.5-7b` | مدل زبان بزرگ |
| `COMPARE_PROMPT` | از پیش تنظیم شده | درخواست مقایسه |
| `COMPARE_RETRIES` | `2` | تعداد تلاش مجدد |

#### جلسه 05: هماهنگی چند عاملی
| متغیر | پیش‌فرض | هدف |
|-------|---------|-----|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | مدل عامل پژوهشگر |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | مدل عامل ویرایشگر |
| `AGENT_QUESTION` | از پیش تنظیم شده | سوال آزمایشی |

### تنظیمات قابلیت اطمینان

| متغیر | پیش‌فرض | هدف |
|-------|---------|-----|
| `SHOW_USAGE` | `1` | چاپ استفاده از توکن |
| `RETRY_ON_FAIL` | `1` | فعال کردن منطق تلاش مجدد |
| `RETRY_BACKOFF` | `1.0` | تأخیر تلاش مجدد (ثانیه) |

## تنظیمات رایج

### تنظیمات توسعه (تکرار سریع)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### تنظیمات تولید (تمرکز بر کیفیت)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### تنظیمات ارزیابی
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### تخصص چند عاملی
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### توسعه از راه دور
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## مدل‌های پیشنهادی

### بر اساس مورد استفاده

**کاربرد عمومی:**
- `phi-4-mini` - تعادل کیفیت و سرعت

**پاسخ‌های سریع:**
- `qwen2.5-0.5b` - بسیار سریع، مناسب برای طبقه‌بندی
- `phi-4-mini` - سریع با کیفیت خوب

**کیفیت بالا:**
- `qwen2.5-7b` - بهترین کیفیت، مصرف منابع بیشتر
- `phi-4-mini` - کیفیت خوب، منابع کمتر

**تولید کد:**
- `deepseek-coder-1.3b` - تخصصی برای کدنویسی
- `phi-4-mini` - کدنویسی عمومی

### بر اساس دسترسی به منابع

**منابع کم (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**منابع متوسط (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**منابع بالا (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## تنظیمات پیشرفته

### نقاط پایانی سفارشی

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### دما و نمونه‌گیری (جایگزینی در کد)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### تنظیم ترکیبی Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## رفع اشکال

### متغیرهای محیطی بارگذاری نمی‌شوند

**علائم:**
- اسکریپت‌ها از مدل‌های اشتباه استفاده می‌کنند
- خطاهای اتصال
- متغیرها شناسایی نمی‌شوند

**راه‌حل‌ها:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### مشکلات اتصال سرویس

**علائم:**
- خطاهای "اتصال رد شد"
- "سرویس در دسترس نیست"
- خطاهای زمان‌بندی

**راه‌حل‌ها:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### مدل پیدا نشد

**علائم:**
- خطاهای "مدل پیدا نشد"
- "نام مستعار شناسایی نشد"

**راه‌حل‌ها:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### خطاهای وارد کردن

**علائم:**
- خطاهای "ماژول پیدا نشد"

**راه‌حل‌ها:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## آزمایش تنظیمات

### بررسی بارگذاری محیط

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### آزمایش اتصال Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## بهترین شیوه‌های امنیتی

### 1. هرگز اطلاعات حساس را کامیت نکنید

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. از فایل‌های .env جداگانه استفاده کنید

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. کلیدهای API را چرخشی کنید

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. از تنظیمات خاص محیط استفاده کنید

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## مستندات SDK

- **مخزن اصلی**: https://github.com/microsoft/Foundry-Local
- **SDK پایتون**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **مستندات API**: برای آخرین نسخه به مخزن SDK مراجعه کنید

## منابع اضافی

- `QUICK_START.md` - راهنمای شروع سریع
- `SDK_MIGRATION_NOTES.md` - جزئیات به‌روزرسانی SDK
- `Workshop/samples/*/README.md` - راهنماهای خاص نمونه‌ها

---

**آخرین به‌روزرسانی**: 2025-01-08  
**نسخه**: 2.0  
**SDK**: Foundry Local Python SDK (آخرین نسخه)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.