<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:32:16+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ur"
}
-->
# فاؤنڈری لوکل SDK مائیگریشن نوٹس

## جائزہ

ورکشاپ فولڈر میں موجود تمام Python فائلز کو تازہ ترین پیٹرنز کے مطابق اپ ڈیٹ کیا گیا ہے جو آفیشل [فاؤنڈری لوکل Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) سے مطابقت رکھتے ہیں۔

## تبدیلیوں کا خلاصہ

### بنیادی انفراسٹرکچر (`workshop_utils.py`)

#### بہتر خصوصیات:
- **اینڈ پوائنٹ اووررائیڈ سپورٹ**: `FOUNDRY_LOCAL_ENDPOINT` انوائرمنٹ ویریبل سپورٹ شامل کی گئی
- **بہتر ایرر ہینڈلنگ**: تفصیلی ایرر میسیجز کے ساتھ بہتر ایکسیپشن ہینڈلنگ
- **بہتر کیشنگ**: کیش کیز میں اینڈ پوائنٹ شامل کیا گیا تاکہ ملٹی اینڈ پوائنٹ سیناریوز میں آسانی ہو
- **ایکسپونینشل بیک آف**: ریٹری لاجک میں ایکسپونینشل بیک آف کا استعمال کیا گیا تاکہ زیادہ قابل اعتماد ہو
- **ٹائپ اینوٹیشنز**: بہتر IDE سپورٹ کے لیے جامع ٹائپ ہنٹس شامل کی گئیں

#### نئی صلاحیتیں:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### نمونہ ایپلیکیشنز

#### سیشن 01: چیٹ بوٹ اسٹرپ (`chat_bootstrap.py`)
- ڈیفالٹ ماڈل کو `phi-3.5-mini` سے `phi-4-mini` میں اپ ڈیٹ کیا گیا
- اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی
- SDK حوالہ جات کے ساتھ دستاویزات کو بہتر بنایا گیا

#### سیشن 02: RAG پائپ لائن (`rag_pipeline.py`)
- ڈیفالٹ ماڈل کو `phi-4-mini` میں اپ ڈیٹ کیا گیا
- اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی
- انوائرمنٹ ویریبلز کی تفصیلات کے ساتھ دستاویزات کو بہتر بنایا گیا

#### سیشن 02: RAG ایویلیوایشن (`rag_eval_ragas.py`)
- ماڈل ڈیفالٹس کو اپ ڈیٹ کیا گیا
- اینڈ پوائنٹ کنفیگریشن شامل کی گئی
- ایرر ہینڈلنگ کو بہتر بنایا گیا

#### سیشن 03: بینچ مارکنگ (`benchmark_oss_models.py`)
- ڈیفالٹ ماڈل لسٹ کو `phi-4-mini` میں شامل کیا گیا
- جامع انوائرمنٹ ویریبلز دستاویزات شامل کی گئیں
- فنکشن دستاویزات کو بہتر بنایا گیا
- پورے سیشن میں اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی

#### سیشن 04: ماڈل کمپیریزن (`model_compare.py`)
- ڈیفالٹ LLM کو `gpt-oss-20b` سے `qwen2.5-7b` میں اپ ڈیٹ کیا گیا
- اینڈ پوائنٹ کنفیگریشن شامل کی گئی
- دستاویزات کو بہتر بنایا گیا

#### سیشن 05: ملٹی ایجنٹ آرکسٹریشن (`agents_orchestrator.py`)
- ٹائپ ہنٹس شامل کی گئیں (مثلاً `str | None` کو `Optional[str]` میں تبدیل کیا گیا)
- ایجنٹ کلاس کی دستاویزات کو بہتر بنایا گیا
- اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی
- انیشیالائزیشن پیٹرن کو بہتر بنایا گیا

#### سیشن 06: ماڈل روٹر (`models_router.py`)
- اینڈ پوائنٹ کنفیگریشن شامل کی گئی
- انٹینٹ ڈیٹیکشن دستاویزات کو بہتر بنایا گیا
- روٹنگ لاجک دستاویزات کو بہتر بنایا گیا

#### سیشن 06: پائپ لائن (`models_pipeline.py`)
- جامع فنکشن دستاویزات شامل کی گئیں
- مرحلہ وار دستاویزات کو بہتر بنایا گیا
- ایرر ہینڈلنگ کو بہتر بنایا گیا

### اسکرپٹس

#### بینچ مارک ایکسپورٹ (`export_benchmark_markdown.py`)
- اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی
- ڈیفالٹ ماڈلز کو اپ ڈیٹ کیا گیا
- فنکشن دستاویزات کو بہتر بنایا گیا
- ایرر ہینڈلنگ کو بہتر بنایا گیا

#### CLI لنٹر (`lint_markdown_cli.py`)
- SDK حوالہ لنکس شامل کیے گئے
- استعمال کی دستاویزات کو بہتر بنایا گیا

### ٹیسٹس

#### اسموک ٹیسٹس (`smoke.py`)
- اینڈ پوائنٹ اووررائیڈ سپورٹ شامل کی گئی
- دستاویزات کو بہتر بنایا گیا
- ٹیسٹ کیس دستاویزات کو بہتر بنایا گیا
- بہتر ایرر رپورٹنگ

## انوائرمنٹ ویریبلز

تمام نمونوں میں اب یہ انوائرمنٹ ویریبلز سپورٹ کی جاتی ہیں:

### بنیادی کنفیگریشن
- `FOUNDRY_LOCAL_ALIAS` - استعمال کرنے کے لیے ماڈل کا عرف (ڈیفالٹ نمونے کے مطابق مختلف ہوتا ہے)
- `FOUNDRY_LOCAL_ENDPOINT` - سروس اینڈ پوائنٹ کو اووررائیڈ کریں (اختیاری)
- `SHOW_USAGE` - ٹوکن استعمال کے اعدادوشمار دکھائیں (ڈیفالٹ: "0")
- `RETRY_ON_FAIL` - ریٹری لاجک کو فعال کریں (ڈیفالٹ: "1")
- `RETRY_BACKOFF` - ریٹری کی ابتدائی تاخیر سیکنڈز میں (ڈیفالٹ: "1.0")

### نمونہ مخصوص
- `EMBED_MODEL` - RAG نمونوں کے لیے ایمبیڈنگ ماڈل
- `BENCH_MODELS` - بینچ مارکنگ کے لیے کاما سے جدا ماڈلز
- `BENCH_ROUNDS` - بینچ مارک راؤنڈز کی تعداد
- `BENCH_PROMPT` - بینچ مارکس کے لیے ٹیسٹ پرامپٹ
- `BENCH_STREAM` - پہلے ٹوکن کی لیٹنسی کو ماپیں
- `RAG_QUESTION` - RAG نمونوں کے لیے ٹیسٹ سوال
- `AGENT_MODEL_PRIMARY` - پرائمری ایجنٹ ماڈل
- `AGENT_MODEL_EDITOR` - ایڈیٹر ایجنٹ ماڈل
- `SLM_ALIAS` - چھوٹے زبان ماڈل کا عرف
- `LLM_ALIAS` - بڑے زبان ماڈل کا عرف

## SDK بہترین طریقے نافذ کیے گئے

### 1. مناسب کلائنٹ انیشیالائزیشن
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

### 2. ماڈل معلومات کی بازیافت
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. ایرر ہینڈلنگ
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. ایکسپونینشل بیک آف کے ساتھ ریٹری لاجک
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

### 5. اسٹریمنگ سپورٹ
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

## کسٹم نمونوں کے لیے مائیگریشن گائیڈ

اگر آپ نئے نمونے بنا رہے ہیں یا موجودہ کو اپ ڈیٹ کر رہے ہیں:

1. **`workshop_utils.py` ہیلپرز کا استعمال کریں**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **اینڈ پوائنٹ اووررائیڈ سپورٹ کریں**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **جامع دستاویزات شامل کریں**:
   - انوائرمنٹ ویریبلز کو ڈاکسٹرنگ میں شامل کریں
   - SDK حوالہ لنک
   - استعمال کی مثالیں

4. **ٹائپ ہنٹس کا استعمال کریں**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **مناسب ایرر ہینڈلنگ نافذ کریں**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## ٹیسٹنگ

تمام نمونوں کو درج ذیل طریقے سے ٹیسٹ کیا جا سکتا ہے:

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

## SDK دستاویزات کے حوالہ جات

- **مین ریپوزٹری**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API دستاویزات**: تازہ ترین API ڈاکس کے لیے SDK ریپوزٹری چیک کریں

## بریکنگ تبدیلیاں

### کوئی توقع نہیں
تمام تبدیلیاں پچھلے ورژنز کے ساتھ مطابقت رکھتی ہیں۔ اپ ڈیٹس بنیادی طور پر:
- نئے اختیاری خصوصیات شامل کرتی ہیں (اینڈ پوائنٹ اووررائیڈ)
- ایرر ہینڈلنگ کو بہتر بناتی ہیں
- دستاویزات کو بہتر بناتی ہیں
- ڈیفالٹ ماڈل ناموں کو موجودہ سفارشات کے مطابق اپ ڈیٹ کرتی ہیں

### اختیاری بہتریاں
آپ اپنے کوڈ کو اپ ڈیٹ کرنا چاہیں گے تاکہ:
- `FOUNDRY_LOCAL_ENDPOINT` کو واضح اینڈ پوائنٹ کنٹرول کے لیے استعمال کریں
- `SHOW_USAGE=1` کو ٹوکن استعمال کی وضاحت کے لیے فعال کریں
- اپ ڈیٹ شدہ ماڈل ڈیفالٹس (`phi-4-mini` بجائے `phi-3.5-mini`)

## عام مسائل اور حل

### مسئلہ: "کلائنٹ انیشیالائزیشن ناکام"
**حل**: یقینی بنائیں کہ فاؤنڈری لوکل سروس چل رہی ہے:
```bash
foundry service start
foundry model run phi-4-mini
```

### مسئلہ: "ماڈل نہیں ملا"
**حل**: دستیاب ماڈلز چیک کریں:
```bash
foundry model list
```

### مسئلہ: اینڈ پوائنٹ کنکشن ایررز
**حل**: اینڈ پوائنٹ کی تصدیق کریں:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## اگلے اقدامات

1. **ماڈیول08 نمونوں کو اپ ڈیٹ کریں**: ماڈیول08/samples میں اسی پیٹرنز کو نافذ کریں
2. **انٹیگریشن ٹیسٹس شامل کریں**: جامع ٹیسٹ سوٹ بنائیں
3. **کارکردگی بینچ مارکنگ**: پہلے اور بعد کی کارکردگی کا موازنہ کریں
4. **دستاویزات کو اپ ڈیٹ کریں**: نئے پیٹرنز کے ساتھ مین README کو اپ ڈیٹ کریں

## تعاون کے رہنما اصول

جب نئے نمونے شامل کریں:
1. مستقل مزاجی کے لیے `workshop_utils.py` کا استعمال کریں
2. موجودہ نمونوں میں پیٹرنز کی پیروی کریں
3. جامع ڈاکسٹرنگ شامل کریں
4. SDK حوالہ لنکس شامل کریں
5. اینڈ پوائنٹ اووررائیڈ سپورٹ کریں
6. مناسب ٹائپ ہنٹس شامل کریں
7. ڈاکسٹرنگ میں استعمال کی مثالیں شامل کریں

## ورژن مطابقت

یہ اپ ڈیٹس مطابقت رکھتی ہیں:
- `foundry-local-sdk` (تازہ ترین)
- `openai>=1.30.0`
- Python 3.8+

---

**آخری اپ ڈیٹ**: 2025-01-08  
**مینٹینر**: ایج اے آئی ورکشاپ ٹیم  
**SDK ورژن**: فاؤنڈری لوکل SDK (تازہ ترین 0.7.117+67073234e7)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔