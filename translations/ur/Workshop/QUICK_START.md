# ورکشاپ فوری آغاز گائیڈ

## ضروریات

### 1. فاؤنڈری لوکل انسٹال کریں

سرکاری انسٹالیشن گائیڈ پر عمل کریں:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. پائتھن ڈیپینڈنسیز انسٹال کریں

ورکشاپ ڈائریکٹری سے:

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

## ورکشاپ سیمپلز چلانا

### سیشن 01: بنیادی چیٹ

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**ماحولیاتی متغیرات:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### سیشن 02: RAG پائپ لائن

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**ماحولیاتی متغیرات:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### سیشن 02: RAG ایویلیوایشن (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**نوٹ**: اضافی ڈیپینڈنسیز کی ضرورت ہے جو `requirements.txt` کے ذریعے انسٹال کی جائیں گی

### سیشن 03: بینچ مارکنگ

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**ماحولیاتی متغیرات:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**آؤٹ پٹ**: لیٹنسی، تھروپٹ، اور فرسٹ ٹوکن میٹرکس کے ساتھ JSON

### سیشن 04: ماڈل موازنہ

```bash
cd Workshop/samples
python -m session04.model_compare
```

**ماحولیاتی متغیرات:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### سیشن 05: ملٹی ایجنٹ آرکسٹریشن

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**ماحولیاتی متغیرات:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### سیشن 06: ماڈل روٹر

```bash
cd Workshop/samples
python -m session06.models_router
```

**روٹنگ منطق کی جانچ** مختلف ارادوں کے ساتھ (کوڈ، خلاصہ، درجہ بندی)

### سیشن 06: پائپ لائن

```bash
python -m session06.models_pipeline
```

**پیچیدہ ملٹی اسٹیپ پائپ لائن** منصوبہ بندی، عمل درآمد، اور بہتری کے ساتھ

## اسکرپٹس

### بینچ مارک رپورٹ ایکسپورٹ کریں

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**آؤٹ پٹ**: مارک ڈاؤن ٹیبل + JSON میٹرکس

### مارک ڈاؤن CLI پیٹرنز کو لنٹ کریں

```bash
python lint_markdown_cli.py --verbose
```

**مقصد**: دستاویزات میں پرانے CLI پیٹرنز کا پتہ لگائیں

## ٹیسٹنگ

### اسموک ٹیسٹس

```bash
cd Workshop
python -m tests.smoke
```

**ٹیسٹس**: اہم سیمپلز کی بنیادی فعالیت

## مسائل کا حل

### سروس نہیں چل رہی

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### ماڈیول امپورٹ ایررز

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### کنکشن ایررز

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### ماڈل نہیں ملا

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## ماحولیاتی متغیرات کا حوالہ

### کور کنفیگریشن
| متغیر | ڈیفالٹ | وضاحت |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | مختلف | استعمال کرنے کے لیے ماڈل عرف |
| `FOUNDRY_LOCAL_ENDPOINT` | خودکار | سروس اینڈ پوائنٹ کو اووررائیڈ کریں |
| `SHOW_USAGE` | `0` | ٹوکن استعمال کے اعداد و شمار دکھائیں |
| `RETRY_ON_FAIL` | `1` | ریٹری منطق کو فعال کریں |
| `RETRY_BACKOFF` | `1.0` | ابتدائی ریٹری تاخیر (سیکنڈز) |

### سیشن مخصوص
| متغیر | ڈیفالٹ | وضاحت |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ایمبیڈنگ ماڈل |
| `RAG_QUESTION` | سیمپل دیکھیں | RAG ٹیسٹ سوال |
| `BENCH_MODELS` | مختلف | کاما سے جدا ماڈلز |
| `BENCH_ROUNDS` | `3` | بینچ مارک تکرار |
| `BENCH_PROMPT` | سیمپل دیکھیں | بینچ مارک پرامپٹ |
| `BENCH_STREAM` | `0` | فرسٹ ٹوکن لیٹنسی کی پیمائش کریں |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | پرائمری ایجنٹ ماڈل |
| `AGENT_MODEL_EDITOR` | پرائمری | ایڈیٹر ایجنٹ ماڈل |
| `SLM_ALIAS` | `phi-4-mini` | چھوٹا لینگویج ماڈل |
| `LLM_ALIAS` | `qwen2.5-7b` | بڑا لینگویج ماڈل |
| `COMPARE_PROMPT` | سیمپل دیکھیں | موازنہ پرامپٹ |

## تجویز کردہ ماڈلز

### ترقی اور ٹیسٹنگ
- **phi-4-mini** - معیار اور رفتار میں توازن
- **qwen2.5-0.5b** - درجہ بندی کے لیے بہت تیز
- **gemma-2-2b** - اچھا معیار، معتدل رفتار

### پروڈکشن منظرنامے
- **phi-4-mini** - عمومی مقصد
- **deepseek-coder-1.3b** - کوڈ جنریشن
- **qwen2.5-7b** - اعلی معیار کے جوابات

## SDK دستاویزات

- **فاؤنڈری لوکل**: https://github.com/microsoft/Foundry-Local
- **پائتھن SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## مدد حاصل کریں

1. سروس کی حالت چیک کریں: `foundry service status`
2. لاگز دیکھیں: فاؤنڈری لوکل سروس لاگز چیک کریں
3. SDK دستاویزات چیک کریں: https://github.com/microsoft/Foundry-Local
4. سیمپل کوڈ کا جائزہ لیں: تمام سیمپلز میں تفصیلی ڈاکسٹرنگز ہیں

## اگلے مراحل

1. تمام ورکشاپ سیشنز کو ترتیب وار مکمل کریں
2. مختلف ماڈلز کے ساتھ تجربہ کریں
3. اپنے استعمال کے معاملات کے لیے سیمپلز میں ترمیم کریں

---

**آخری اپ ڈیٹ**: 2025-01-08  
**ورکشاپ ورژن**: تازہ ترین  
**SDK**: فاؤنڈری لوکل پائتھن SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->