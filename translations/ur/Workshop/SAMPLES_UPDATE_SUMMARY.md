<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:31:56+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ur"
}
-->
# ورکشاپ نمونے - فاؤنڈری لوکل SDK اپ ڈیٹ کا خلاصہ

## جائزہ

`Workshop/samples` ڈائریکٹری میں موجود تمام پائتھون نمونوں کو فاؤنڈری لوکل SDK کے بہترین طریقوں کے مطابق اپ ڈیٹ کیا گیا ہے اور ورکشاپ کے اندر مستقل مزاجی کو یقینی بنایا گیا ہے۔

**تاریخ**: 8 اکتوبر، 2025  
**دائرہ کار**: 6 ورکشاپ سیشنز میں 9 پائتھون فائلز  
**اہم توجہ**: غلطی سے نمٹنا، دستاویزات، SDK پیٹرنز، صارف کا تجربہ

---

## اپ ڈیٹ شدہ فائلز

### سیشن 01: شروعات کرنا
- ✅ `chat_bootstrap.py` - بنیادی چیٹ اور اسٹریمنگ کے مثالیں

### سیشن 02: RAG حل
- ✅ `rag_pipeline.py` - RAG ایمبیڈنگ کے ساتھ عمل درآمد
- ✅ `rag_eval_ragas.py` - RAGAS میٹرکس کے ساتھ RAG کا جائزہ

### سیشن 03: اوپن سورس ماڈلز
- ✅ `benchmark_oss_models.py` - ملٹی ماڈل بینچ مارکنگ

### سیشن 04: جدید ماڈلز
- ✅ `model_compare.py` - SLM بمقابلہ LLM موازنہ

### سیشن 05: AI سے چلنے والے ایجنٹس
- ✅ `agents_orchestrator.py` - ملٹی ایجنٹ کوآرڈینیشن

### سیشن 06: ماڈلز بطور ٹولز
- ✅ `models_router.py` - ارادے پر مبنی ماڈل روٹنگ
- ✅ `models_pipeline.py` - ملٹی اسٹیپ روٹڈ پائپ لائن

### معاون انفراسٹرکچر
- ✅ `workshop_utils.py` - پہلے سے بہترین طریقوں پر عمل کر رہا ہے (کوئی تبدیلی کی ضرورت نہیں)

---

## اہم بہتریاں

### 1. بہتر غلطی سے نمٹنا

**پہلے:**
```python
manager, client, model_id = get_client(alias)
```

**بعد میں:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**فوائد:**
- واضح غلطی کے پیغامات کے ساتھ شائستہ غلطی سے نمٹنا
- قابل عمل خرابیوں کا سراغ لگانے کے اشارے
- اسکرپٹنگ کے لیے مناسب ایگزٹ کوڈز

### 2. بہتر درآمد کا انتظام

**پہلے:**
```python
from sentence_transformers import SentenceTransformer
```

**بعد میں:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**فوائد:**
- جب انحصار غائب ہو تو واضح رہنمائی
- مبہم درآمد کی غلطیوں کو روکتا ہے
- صارف دوست انسٹالیشن ہدایات

### 3. جامع دستاویزات

**تمام نمونوں میں شامل:**
- ڈاک اسٹرنگز میں ماحول متغیرات کی دستاویزات
- SDK حوالہ لنکس
- استعمال کی مثالیں
- تفصیلی فنکشن/پیرامیٹر دستاویزات
- بہتر IDE سپورٹ کے لیے ٹائپ ہنٹس

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

### 4. بہتر صارف کی رائے

**معلوماتی لاگنگ شامل کی گئی:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**پروگریس انڈیکیٹرز:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**منظم آؤٹ پٹ:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. مضبوط بینچ مارکنگ

**سیشن 03 میں بہتری:**
- فی ماڈل غلطی سے نمٹنا (ناکامی پر جاری رہتا ہے)
- تفصیلی پیش رفت کی رپورٹنگ
- وارم اپ راؤنڈز مناسب طریقے سے انجام دیے گئے
- پہلے ٹوکن کی تاخیر کی پیمائش کی حمایت
- مراحل کی واضح علیحدگی

### 6. مستقل ٹائپ ہنٹس

**ہر جگہ شامل:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**فوائد:**
- بہتر IDE آٹو کمپلیٹ
- ابتدائی غلطی کا پتہ لگانا
- خود دستاویزات کوڈ

### 7. بہتر ماڈل روٹر

**سیشن 06 میں بہتری:**
- جامع ارادے کا پتہ لگانے کی دستاویزات
- ماڈل انتخاب الگورتھم کی وضاحت
- تفصیلی روٹنگ لاگز
- ٹیسٹ آؤٹ پٹ فارمیٹنگ
- بیچ ٹیسٹنگ میں غلطی کی بازیابی

### 8. ملٹی ایجنٹ آرکسٹریشن

**سیشن 05 میں بہتری:**
- مرحلہ وار پیش رفت کی رپورٹنگ
- فی ایجنٹ غلطی سے نمٹنا
- واضح پائپ لائن ڈھانچہ
- بہتر میموری مینجمنٹ دستاویزات

---

## ٹیسٹنگ چیک لسٹ

### ضروریات
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### ہر نمونہ ٹیسٹ کریں

#### سیشن 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### سیشن 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### سیشن 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### سیشن 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### سیشن 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### سیشن 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## ماحول متغیرات کا حوالہ

### عالمی (تمام نمونے)
| متغیر | وضاحت | ڈیفالٹ |
|-------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | استعمال کرنے کے لیے ماڈل کا عرف | نمونے کے لحاظ سے مختلف |
| `FOUNDRY_LOCAL_ENDPOINT` | سروس اینڈ پوائنٹ کو اوور رائیڈ کریں | خودکار طور پر معلوم |
| `SHOW_USAGE` | ٹوکن کے استعمال کو دکھائیں | `0` |
| `RETRY_ON_FAIL` | ریٹری منطق کو فعال کریں | `1` |
| `RETRY_BACKOFF` | ابتدائی ریٹری تاخیر | `1.0` |

### نمونہ مخصوص
| متغیر | استعمال کنندہ | وضاحت |
|-------|---------------|---------|
| `EMBED_MODEL` | سیشن 02 | ایمبیڈنگ ماڈل کا نام |
| `RAG_QUESTION` | سیشن 02 | RAG کے لیے ٹیسٹ سوال |
| `BENCH_MODELS` | سیشن 03 | بینچ مارک کرنے کے لیے ماڈلز کی کاما سے جدا فہرست |
| `BENCH_ROUNDS` | سیشن 03 | بینچ مارک راؤنڈز کی تعداد |
| `BENCH_PROMPT` | سیشن 03 | بینچ مارکس کے لیے ٹیسٹ پرامپٹ |
| `BENCH_STREAM` | سیشن 03 | پہلے ٹوکن کی تاخیر کی پیمائش |
| `SLM_ALIAS` | سیشن 04 | چھوٹا لینگویج ماڈل |
| `LLM_ALIAS` | سیشن 04 | بڑا لینگویج ماڈل |
| `COMPARE_PROMPT` | سیشن 04 | موازنہ ٹیسٹ پرامپٹ |
| `AGENT_MODEL_PRIMARY` | سیشن 05 | پرائمری ایجنٹ ماڈل |
| `AGENT_MODEL_EDITOR` | سیشن 05 | ایڈیٹر ایجنٹ ماڈل |
| `AGENT_QUESTION` | سیشن 05 | ایجنٹس کے لیے ٹیسٹ سوال |
| `PIPELINE_TASK` | سیشن 06 | پائپ لائن کے لیے کام |

---

## اہم تبدیلیاں

**کوئی نہیں** - تمام تبدیلیاں پچھلے ورژن کے ساتھ مطابقت رکھتی ہیں۔

موجودہ اسکرپٹس کام کرتے رہیں گے۔ نئی خصوصیات:
- اختیاری ماحول متغیرات
- بہتر غلطی کے پیغامات (فنکشنلٹی کو متاثر نہیں کرتے)
- اضافی لاگنگ (دبایا جا سکتا ہے)
- بہتر ٹائپ ہنٹس (کوئی رن ٹائم اثر نہیں)

---

## بہترین طریقے نافذ کیے گئے

### 1. ہمیشہ ورکشاپ یوٹیلز استعمال کریں
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. مناسب غلطی سے نمٹنے کا پیٹرن
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. معلوماتی لاگنگ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. ٹائپ ہنٹس
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. جامع ڈاک اسٹرنگز
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

### 6. ماحول متغیرات کی حمایت
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. شائستہ تنزلی
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

## عام مسائل اور حل

### مسئلہ: درآمد کی غلطیاں
**حل:** غائب انحصار انسٹال کریں
```bash
pip install sentence-transformers ragas datasets numpy
```

### مسئلہ: کنکشن کی غلطیاں
**حل:** یقینی بنائیں کہ فاؤنڈری لوکل چل رہا ہے
```bash
foundry service status
foundry model run phi-4-mini
```

### مسئلہ: ماڈل نہیں ملا
**حل:** دستیاب ماڈلز چیک کریں
```bash
foundry model ls
foundry model download <alias>
```

### مسئلہ: سست کارکردگی
**حل:** چھوٹے ماڈلز استعمال کریں یا پیرامیٹرز کو ایڈجسٹ کریں
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## اگلے اقدامات

### 1. تمام نمونوں کا ٹیسٹ کریں
اوپر دی گئی ٹیسٹنگ چیک لسٹ کے ذریعے تمام نمونوں کی درستگی کی تصدیق کریں۔

### 2. دستاویزات کو اپ ڈیٹ کریں
- نئے مثالوں کے ساتھ سیشن مارک ڈاؤن فائلز کو اپ ڈیٹ کریں
- مرکزی README میں خرابیوں کا سراغ لگانے کا سیکشن شامل کریں
- فوری حوالہ گائیڈ بنائیں

### 3. انٹیگریشن ٹیسٹ بنائیں
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. کارکردگی کے بینچ مارکس شامل کریں
غلطی سے نمٹنے کی بہتری سے کارکردگی میں بہتری کو ٹریک کریں۔

### 5. صارف کی رائے
ورکشاپ کے شرکاء سے رائے جمع کریں:
- غلطی کے پیغامات کی وضاحت
- دستاویزات کی مکملیت
- استعمال میں آسانی

---

## وسائل

- **فاؤنڈری لوکل SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **فوری حوالہ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **مائیگریشن نوٹس**: `Workshop/SDK_MIGRATION_NOTES.md`
- **مرکزی ریپوزیٹری**: https://github.com/microsoft/Foundry-Local

---

## دیکھ بھال

### نئے نمونے شامل کرنا
نئے نمونے بناتے وقت ان پیٹرنز پر عمل کریں:

1. کلائنٹ مینجمنٹ کے لیے `workshop_utils` استعمال کریں
2. جامع غلطی سے نمٹنے کو شامل کریں
3. ماحول متغیرات کی حمایت شامل کریں
4. ٹائپ ہنٹس اور ڈاک اسٹرنگز شامل کریں
5. معلوماتی لاگنگ فراہم کریں
6. ڈاک اسٹرنگ میں استعمال کی مثالیں شامل کریں
7. SDK دستاویزات کے لنک شامل کریں

### اپ ڈیٹس کا جائزہ لینا
نمونوں کی اپ ڈیٹس کا جائزہ لیتے وقت چیک کریں:
- [ ] تمام I/O آپریشنز پر غلطی سے نمٹنا
- [ ] عوامی فنکشنز پر ٹائپ ہنٹس
- [ ] جامع ڈاک اسٹرنگز
- [ ] ماحول متغیرات کی دستاویزات
- [ ] معلوماتی صارف کی رائے
- [ ] SDK حوالہ لنکس
- [ ] مستقل کوڈ اسٹائل

---

**خلاصہ**: تمام ورکشاپ پائتھون نمونے اب فاؤنڈری لوکل SDK کے بہترین طریقوں پر عمل کرتے ہیں، بہتر غلطی سے نمٹنے، جامع دستاویزات، اور بہتر صارف کے تجربے کے ساتھ۔ کوئی اہم تبدیلی نہیں - تمام موجودہ فعالیت محفوظ اور بہتر کی گئی ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔