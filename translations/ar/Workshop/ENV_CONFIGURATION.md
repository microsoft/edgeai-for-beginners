# دليل إعداد البيئة

## نظرة عامة

تستخدم عينات الورشة متغيرات البيئة للتكوين، ويتم تجميعها في ملف `.env` الموجود في جذر المستودع. يتيح ذلك تخصيصًا سهلاً دون الحاجة لتعديل الكود.

## البدء السريع

### 1. التحقق من المتطلبات الأساسية

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. إعداد البيئة

تم إعداد ملف `.env` مسبقًا بقيم افتراضية مناسبة. معظم المستخدمين لن يحتاجوا إلى تغيير أي شيء.

**اختياري**: مراجعة وتخصيص الإعدادات:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. تطبيق الإعدادات

**لبرامج Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**لدفاتر الملاحظات:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## مرجع متغيرات البيئة

### التكوين الأساسي

| المتغير | الافتراضي | الوصف |
|---------|-----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | النموذج الافتراضي للعينات |
| `FOUNDRY_LOCAL_ENDPOINT` | (فارغ) | تجاوز نقطة خدمة |
| `PYTHONPATH` | مسارات الورشة | مسار البحث عن وحدات Python |

**متى يتم تعيين FOUNDRY_LOCAL_ENDPOINT:**
- مثيل Foundry Local عن بُعد
- تكوين منفذ مخصص
- فصل التطوير والإنتاج

**مثال:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### متغيرات خاصة بالجلسة

#### الجلسة 02: خط أنابيب RAG
| المتغير | الافتراضي | الهدف |
|---------|-----------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | نموذج التضمين |
| `RAG_QUESTION` | مُعد مسبقًا | سؤال الاختبار |

#### الجلسة 03: قياس الأداء
| المتغير | الافتراضي | الهدف |
|---------|-----------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | النماذج المراد قياس أدائها |
| `BENCH_ROUNDS` | `3` | عدد التكرارات لكل نموذج |
| `BENCH_PROMPT` | مُعد مسبقًا | موجه الاختبار |
| `BENCH_STREAM` | `0` | قياس زمن استجابة أول رمز |

#### الجلسة 04: مقارنة النماذج
| المتغير | الافتراضي | الهدف |
|---------|-----------|-------|
| `SLM_ALIAS` | `phi-4-mini` | نموذج لغة صغير |
| `LLM_ALIAS` | `qwen2.5-7b` | نموذج لغة كبير |
| `COMPARE_PROMPT` | مُعد مسبقًا | موجه المقارنة |
| `COMPARE_RETRIES` | `2` | محاولات إعادة المحاولة |

#### الجلسة 05: تنسيق متعدد الوكلاء
| المتغير | الافتراضي | الهدف |
|---------|-----------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | نموذج وكيل الباحث |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | نموذج وكيل المحرر |
| `AGENT_QUESTION` | مُعد مسبقًا | سؤال الاختبار |

### إعدادات الموثوقية

| المتغير | الافتراضي | الهدف |
|---------|-----------|-------|
| `SHOW_USAGE` | `1` | طباعة استخدام الرموز |
| `RETRY_ON_FAIL` | `1` | تمكين منطق إعادة المحاولة |
| `RETRY_BACKOFF` | `1.0` | تأخير إعادة المحاولة (بالثواني) |

## الإعدادات الشائعة

### إعداد التطوير (تكرار سريع)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### إعداد الإنتاج (تركيز على الجودة)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### إعداد قياس الأداء
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### تخصص متعدد الوكلاء
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### التطوير عن بُعد
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## النماذج الموصى بها

### حسب الاستخدام

**الاستخدام العام:**
- `phi-4-mini` - توازن بين الجودة والسرعة

**الاستجابات السريعة:**
- `qwen2.5-0.5b` - سريع جدًا، جيد للتصنيف
- `phi-4-mini` - سريع بجودة جيدة

**الجودة العالية:**
- `qwen2.5-7b` - أفضل جودة، استخدام موارد أعلى
- `phi-4-mini` - جودة جيدة، موارد أقل

**توليد الأكواد:**
- `deepseek-coder-1.3b` - متخصص في الأكواد
- `phi-4-mini` - متعدد الاستخدامات للأكواد

### حسب توفر الموارد

**موارد منخفضة (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**موارد متوسطة (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**موارد عالية (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## إعدادات متقدمة

### نقاط النهاية المخصصة

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### درجة الحرارة وأخذ العينات (تجاوز في الكود)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### إعداد Azure OpenAI الهجين

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## استكشاف الأخطاء وإصلاحها

### متغيرات البيئة غير محملة

**الأعراض:**
- استخدام نماذج خاطئة في البرامج
- أخطاء الاتصال
- عدم التعرف على المتغيرات

**الحلول:**
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

### مشاكل الاتصال بالخدمة

**الأعراض:**
- أخطاء "رفض الاتصال"
- "الخدمة غير متوفرة"
- أخطاء انتهاء المهلة

**الحلول:**
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

### النموذج غير موجود

**الأعراض:**
- أخطاء "النموذج غير موجود"
- "الاسم المستعار غير معترف به"

**الحلول:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### أخطاء الاستيراد

**الأعراض:**
- أخطاء "الوحدة غير موجودة"

**الحلول:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## اختبار الإعدادات

### التحقق من تحميل البيئة

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

### اختبار اتصال Foundry Local

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

## أفضل ممارسات الأمان

### 1. لا تقم أبدًا بتضمين الأسرار

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. استخدم ملفات .env منفصلة

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. قم بتدوير مفاتيح API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. استخدم إعدادات خاصة بالبيئة

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## وثائق SDK

- **المستودع الرئيسي**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **وثائق API**: تحقق من مستودع SDK للحصول على أحدث المعلومات

## موارد إضافية

- `QUICK_START.md` - دليل البدء السريع
- `Workshop/samples/*/README.md` - أدلة خاصة بالعينات

---

**آخر تحديث**: 2025-01-08  
**الإصدار**: 2.0  
**SDK**: Foundry Local Python SDK (الأحدث)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->