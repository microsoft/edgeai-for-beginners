<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:26:33+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "fa"
}
-->
# نمونه‌های کارگاه - کارت مرجع سریع

**آخرین به‌روزرسانی**: ۸ اکتبر ۲۰۲۵

---

## 🚀 شروع سریع

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 نمای کلی نمونه‌ها

| جلسه | نمونه | هدف | زمان |
|------|-------|------|------|
| 01 | `chat_bootstrap.py` | چت پایه + استریم | ~۳۰ ثانیه |
| 02 | `rag_pipeline.py` | RAG با تعبیه‌ها | ~۴۵ ثانیه |
| 02 | `rag_eval_ragas.py` | ارزیابی RAG | ~۶۰ ثانیه |
| 03 | `benchmark_oss_models.py` | ارزیابی مدل‌ها | ~۲ دقیقه |
| 04 | `model_compare.py` | SLM در مقابل LLM | ~۴۵ ثانیه |
| 05 | `agents_orchestrator.py` | سیستم چند عاملی | ~۶۰ ثانیه |
| 06 | `models_router.py` | مسیریابی هدف | ~۴۵ ثانیه |
| 06 | `models_pipeline.py` | خط لوله چند مرحله‌ای | ~۶۰ ثانیه |

---

## 🛠️ متغیرهای محیطی

### ضروری
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### مخصوص جلسه
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ اعتبارسنجی و آزمایش

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 رفع اشکال

### خطای اتصال
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### خطای وارد کردن
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### مدل پیدا نشد
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### عملکرد کند
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 الگوهای رایج

### چت پایه
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### دریافت کلاینت
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### مدیریت خطا
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### استریم
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 انتخاب مدل

| مدل | اندازه | بهترین کاربرد | سرعت |
|-----|--------|--------------|-------|
| `qwen2.5-0.5b` | 0.5B | طبقه‌بندی سریع | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | تولید سریع کد | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | نوشتن خلاقانه | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | کدنویسی، بازسازی | ⚡⚡ |
| `phi-4-mini` | 4B | عمومی، خلاصه‌سازی | ⚡⚡ |
| `qwen2.5-7b` | 7B | استدلال پیچیده | ⚡ |

---

## 🔗 منابع

- **مستندات SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **مرجع سریع**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **خلاصه به‌روزرسانی**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **یادداشت‌های مهاجرت**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 نکات

1. **کلاینت‌ها را کش کنید**: `workshop_utils` این کار را برای شما انجام می‌دهد
2. **از مدل‌های کوچک‌تر استفاده کنید**: برای آزمایش با `qwen2.5-0.5b` شروع کنید
3. **آمار استفاده را فعال کنید**: `SHOW_USAGE=1` را تنظیم کنید تا توکن‌ها را ردیابی کنید
4. **پردازش دسته‌ای**: چندین درخواست را به صورت متوالی پردازش کنید
5. **کاهش max_tokens**: زمان پاسخ‌دهی را برای پاسخ‌های سریع کاهش دهید

---

## 🎯 جریان‌های کاری نمونه

### آزمایش همه چیز
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### ارزیابی مدل‌ها
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### خط لوله RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### سیستم چند عاملی
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**راهنمای سریع**: هر نمونه را با `--help` از دایرکتوری `samples` اجرا کنید یا توضیحات را بررسی کنید:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**همه نمونه‌ها در اکتبر ۲۰۲۵ با بهترین روش‌های Foundry Local SDK به‌روزرسانی شده‌اند** ✨

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.