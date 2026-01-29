# ماحول کی تشکیل کے رہنما

## جائزہ

ورکشاپ کے نمونے ترتیب کے لیے ماحول کے متغیرات استعمال کرتے ہیں، جو ریپوزیٹری کی جڑ میں `.env` فائل میں مرکوز ہیں۔ اس سے کوڈ میں تبدیلی کیے بغیر آسان تخصیص ممکن ہوتی ہے۔

## فوری آغاز

### 1. ضروریات کی تصدیق کریں

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. ماحول کی تشکیل کریں

`.env` فائل پہلے سے معقول ڈیفالٹس کے ساتھ ترتیب دی گئی ہے۔ زیادہ تر صارفین کو کچھ تبدیل کرنے کی ضرورت نہیں ہوگی۔

**اختیاری**: ترتیبات کا جائزہ لیں اور تخصیص کریں:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. ترتیب کو نافذ کریں

**پائتھون اسکرپٹس کے لیے:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**نوٹ بکس کے لیے:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## ماحول کے متغیرات کا حوالہ

### بنیادی ترتیب

| متغیر | ڈیفالٹ | وضاحت |
|-------|--------|-------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | نمونوں کے لیے ڈیفالٹ ماڈل |
| `FOUNDRY_LOCAL_ENDPOINT` | (خالی) | سروس اینڈ پوائنٹ کو اووررائیڈ کریں |
| `PYTHONPATH` | ورکشاپ کے راستے | پائتھون ماڈیول تلاش کا راستہ |

**FOUNDRY_LOCAL_ENDPOINT کب سیٹ کریں:**
- ریموٹ فاؤنڈری لوکل انسٹینس
- کسٹم پورٹ کی تشکیل
- ترقی/پیداوار کی علیحدگی

**مثال:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### سیشن کے مخصوص متغیرات

#### سیشن 02: RAG پائپ لائن
| متغیر | ڈیفالٹ | مقصد |
|-------|--------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ایمبیڈنگ ماڈل |
| `RAG_QUESTION` | پہلے سے ترتیب شدہ | ٹیسٹ سوال |

#### سیشن 03: بینچ مارکنگ
| متغیر | ڈیفالٹ | مقصد |
|-------|--------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | بینچ مارک کرنے کے لیے ماڈلز |
| `BENCH_ROUNDS` | `3` | ہر ماڈل کے لیے تکرار |
| `BENCH_PROMPT` | پہلے سے ترتیب شدہ | ٹیسٹ پرامپٹ |
| `BENCH_STREAM` | `0` | پہلے ٹوکن کی تاخیر کی پیمائش کریں |

#### سیشن 04: ماڈل کا موازنہ
| متغیر | ڈیفالٹ | مقصد |
|-------|--------|-------|
| `SLM_ALIAS` | `phi-4-mini` | چھوٹا زبان ماڈل |
| `LLM_ALIAS` | `qwen2.5-7b` | بڑا زبان ماڈل |
| `COMPARE_PROMPT` | پہلے سے ترتیب شدہ | موازنہ پرامپٹ |
| `COMPARE_RETRIES` | `2` | دوبارہ کوشش کی تعداد |

#### سیشن 05: ملٹی ایجنٹ آرکسٹریشن
| متغیر | ڈیفالٹ | مقصد |
|-------|--------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ریسرچر ایجنٹ ماڈل |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ایڈیٹر ایجنٹ ماڈل |
| `AGENT_QUESTION` | پہلے سے ترتیب شدہ | ٹیسٹ سوال |

### قابل اعتماد ترتیب

| متغیر | ڈیفالٹ | مقصد |
|-------|--------|-------|
| `SHOW_USAGE` | `1` | ٹوکن کے استعمال کو پرنٹ کریں |
| `RETRY_ON_FAIL` | `1` | دوبارہ کوشش کی منطق کو فعال کریں |
| `RETRY_BACKOFF` | `1.0` | دوبارہ کوشش کی تاخیر (سیکنڈز) |

## عام ترتیبات

### ترقیاتی سیٹ اپ (تیز تکرار)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### پیداواری سیٹ اپ (معیار پر توجہ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### بینچ مارکنگ سیٹ اپ
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### ملٹی ایجنٹ کی تخصیص
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### ریموٹ ترقی
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## تجویز کردہ ماڈلز

### استعمال کے کیس کے لحاظ سے

**عام مقصد:**
- `phi-4-mini` - معیار اور رفتار میں توازن

**تیز جوابات:**
- `qwen2.5-0.5b` - بہت تیز، درجہ بندی کے لیے اچھا
- `phi-4-mini` - تیز اور اچھے معیار کے ساتھ

**اعلی معیار:**
- `qwen2.5-7b` - بہترین معیار، زیادہ وسائل کا استعمال
- `phi-4-mini` - اچھا معیار، کم وسائل

**کوڈ جنریشن:**
- `deepseek-coder-1.3b` - کوڈ کے لیے خاص
- `phi-4-mini` - عمومی مقصد کوڈنگ

### وسائل کی دستیابی کے لحاظ سے

**کم وسائل (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**درمیانی وسائل (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**زیادہ وسائل (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## اعلی درجے کی ترتیب

### کسٹم اینڈ پوائنٹس

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### درجہ حرارت اور سیمپلنگ (کوڈ میں اووررائیڈ کریں)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI ہائبرڈ سیٹ اپ

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## مسائل کا حل

### ماحول کے متغیرات لوڈ نہیں ہو رہے

**علامات:**
- اسکرپٹس غلط ماڈلز استعمال کر رہے ہیں
- کنکشن کی غلطیاں
- متغیرات کو تسلیم نہیں کیا جا رہا

**حل:**
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

### سروس کنکشن کے مسائل

**علامات:**
- "کنکشن ریفیوزڈ" کی غلطیاں
- "سروس دستیاب نہیں"
- ٹائم آؤٹ کی غلطیاں

**حل:**
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

### ماڈل نہیں ملا

**علامات:**
- "ماڈل نہیں ملا" کی غلطیاں
- "عرفیت تسلیم نہیں کیا گیا"

**حل:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### درآمد کی غلطیاں

**علامات:**
- "ماڈیول نہیں ملا" کی غلطیاں

**حل:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## ترتیب کی جانچ

### ماحول لوڈنگ کی تصدیق کریں

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

### فاؤنڈری لوکل کنکشن کی جانچ کریں

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

## سیکیورٹی کے بہترین طریقے

### 1. کبھی بھی راز کو کمیٹ نہ کریں

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. الگ الگ .env فائلیں استعمال کریں

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API کیز کو گھمائیں

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. ماحول کے مخصوص ترتیب استعمال کریں

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK دستاویزات

- **مین ریپوزیٹری**: https://github.com/microsoft/Foundry-Local
- **پائتھون SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API دستاویزات**: تازہ ترین کے لیے SDK ریپوزیٹری چیک کریں

## اضافی وسائل

- `QUICK_START.md` - شروعاتی رہنما
- `Workshop/samples/*/README.md` - نمونہ مخصوص رہنما

---

**آخری اپ ڈیٹ**: 2025-01-08  
**ورژن**: 2.0  
**SDK**: فاؤنڈری لوکل پائتھون SDK (تازہ ترین)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->