<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T20:19:08+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ar"
}
-->
# الجلسة الأولى: البدء مع Foundry Local

## الملخص

ابدأ رحلتك مع Foundry Local من خلال تثبيته وتكوينه على نظام Windows 11. تعلم كيفية إعداد واجهة الأوامر (CLI)، تمكين تسريع الأجهزة، وتخزين النماذج مؤقتًا للحصول على استنتاج محلي سريع. هذه الجلسة العملية تستعرض كيفية تشغيل نماذج مثل Phi، Qwen، DeepSeek، وGPT-OSS-20B باستخدام أوامر CLI قابلة للتكرار.

## أهداف التعلم

بنهاية هذه الجلسة، ستتمكن من:

- **التثبيت والتكوين**: إعداد Foundry Local على Windows 11 مع إعدادات الأداء المثلى
- **إتقان عمليات CLI**: استخدام واجهة الأوامر لإدارة النماذج ونشرها
- **تمكين تسريع الأجهزة**: تكوين تسريع GPU باستخدام ONNXRuntime أو WebGPU
- **نشر نماذج متعددة**: تشغيل نماذج phi-4، GPT-OSS-20B، Qwen، وDeepSeek محليًا
- **بناء أول تطبيق لك**: تعديل العينات الحالية لاستخدام Foundry Local Python SDK

# اختبار النموذج (طلب واحد غير تفاعلي)
foundry model run phi-4-mini --prompt "مرحبًا، قدم نفسك"

- Windows 11 (22H2 أو أحدث)
# عرض النماذج المتاحة في الكتالوج (النماذج المحملة تظهر بعد التشغيل)
foundry model list
## ملاحظة: لا يوجد حاليًا علامة `--running` مخصصة؛ لرؤية النماذج المحملة، ابدأ محادثة أو تحقق من سجلات الخدمة.
- Python 3.10+ مثبت
- Visual Studio Code مع إضافة Python
- صلاحيات المسؤول للتثبيت

### (اختياري) متغيرات البيئة

قم بإنشاء ملف `.env` (أو ضبطه في shell) لجعل السكربتات قابلة للنقل:
# مقارنة الردود (غير تفاعلي)
foundry model run gpt-oss-20b --prompt "اشرح الذكاء الاصطناعي الطرفي بطريقة بسيطة"
| المتغير | الغرض | المثال |
|---------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | الاسم المستعار المفضل للنموذج (يختار الكتالوج تلقائيًا أفضل نسخة) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | تجاوز نقطة النهاية (وإلا يتم تحديدها تلقائيًا من المدير) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | تمكين عرض البث | `true` |

> إذا كان `FOUNDRY_LOCAL_ENDPOINT=auto` (أو غير مضبوط)، يتم اشتقاقه من مدير SDK.

## سير العرض التوضيحي (30 دقيقة)

### 1. تثبيت Foundry Local والتحقق من إعداد CLI (10 دقائق)

# عرض النماذج المخزنة مؤقتًا
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (معاينة / إذا كان مدعومًا)**

إذا تم توفير حزمة macOS الأصلية (تحقق من الوثائق الرسمية للحصول على أحدث المعلومات):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

إذا لم تكن الحزم الأصلية لـ macOS متوفرة بعد، يمكنك:
1. استخدام Windows 11 ARM/Intel VM (Parallels / UTM) واتباع خطوات Windows.
2. تشغيل النماذج عبر الحاوية (إذا تم نشر صورة الحاوية) وضبط `FOUNDRY_LOCAL_ENDPOINT` على المنفذ المكشوف.

**إنشاء بيئة افتراضية لـ Python (عبر الأنظمة)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

ترقية pip وتثبيت التبعيات الأساسية:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### الخطوة 1.2: التحقق من التثبيت

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### الخطوة 1.3: تكوين البيئة

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### إعداد SDK (موصى به)

بدلاً من بدء الخدمة يدويًا وتشغيل النماذج، يمكن لـ **Foundry Local Python SDK** إعداد كل شيء:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

إذا كنت تفضل التحكم الصريح، يمكنك استخدام CLI + عميل OpenAI كما هو موضح لاحقًا.

### 2. تشغيل النماذج محليًا عبر CLI (10 دقائق)

#### الخطوة 3.1: نشر نموذج Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### الخطوة 3.2: نشر GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### الخطوة 3.3: تحميل نماذج إضافية

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. مشروع البداية: تعديل 01-run-phi لـ Foundry Local (5 دقائق)

#### الخطوة 4.1: إنشاء تطبيق محادثة أساسي

إنشاء `samples/01-foundry-quickstart/chat_quickstart.py` (محدث لاستخدام المدير إذا كان متاحًا):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### الخطوة 4.2: اختبار التطبيق

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## المفاهيم الرئيسية التي تم تغطيتها

### 1. بنية Foundry Local

- **محرك الاستنتاج المحلي**: تشغيل النماذج بالكامل على جهازك
- **توافق SDK مع OpenAI**: تكامل سلس مع كود OpenAI الحالي
- **إدارة النماذج**: تنزيل، تخزين مؤقت، وتشغيل نماذج متعددة بكفاءة
- **تحسين الأجهزة**: الاستفادة من تسريع GPU، NPU، وCPU

### 2. مرجع أوامر CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. تكامل Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## استكشاف المشكلات الشائعة

### المشكلة 1: "لم يتم العثور على أمر Foundry"

**الحل:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### المشكلة 2: "فشل تحميل النموذج"

**الحل:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### المشكلة 3: "رفض الاتصال على localhost:5273"

**الحل:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## نصائح لتحسين الأداء

### 1. استراتيجية اختيار النموذج

- **Phi-4-mini**: الأفضل للمهام العامة، استخدام ذاكرة أقل
- **Qwen2.5-0.5b**: أسرع استنتاج، موارد قليلة
- **GPT-OSS-20B**: أعلى جودة، يتطلب موارد أكثر
- **DeepSeek-Coder**: مُحسن للمهام البرمجية

### 2. تحسين الأجهزة

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. مراقبة الأداء

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### تحسينات اختيارية

| التحسين | ماذا | كيف |
|---------|------|-----|
| الأدوات المشتركة | إزالة منطق العميل/الإعداد المكرر | استخدام `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| رؤية استخدام الرموز | تعليم التفكير في التكلفة/الكفاءة مبكرًا | ضبط `SHOW_USAGE=1` لطباعة الرموز المستخدمة |
| مقارنات حتمية | اختبارات مستقرة ومقارنة الانحدار | استخدام `temperature=0`, `top_p=1`, نص طلب ثابت |
| زمن استجابة أول رمز | مقياس استجابة محسوس | تعديل سكربت القياس مع البث (`BENCH_STREAM=1`) |
| إعادة المحاولة عند الأخطاء المؤقتة | عروض مرنة عند بدء التشغيل البارد | `RETRY_ON_FAIL=1` (افتراضي) وضبط `RETRY_BACKOFF` |
| اختبار سريع | التحقق السريع عبر التدفقات الرئيسية | تشغيل `python Workshop/tests/smoke.py` قبل الورشة |
| ملفات تعريف أسماء النماذج | التبديل السريع بين مجموعات النماذج | الحفاظ على `.env` مع `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| كفاءة التخزين المؤقت | تجنب الإحماء المتكرر في تشغيل متعدد العينات | أدوات مديري التخزين المؤقت؛ إعادة الاستخدام عبر السكربتات/دفاتر الملاحظات |
| الإحماء الأول | تقليل ارتفاعات زمن الاستجابة | تشغيل طلب صغير بعد إنشاء `FoundryLocalManager`

مثال على الإحماء الحتمي الأساسي (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

يجب أن ترى مخرجات مشابهة وعدد رموز متطابق في التشغيل الثاني، مما يؤكد الحتمية.

## الخطوات التالية

بعد إكمال هذه الجلسة:

1. **استكشاف الجلسة الثانية**: بناء حلول الذكاء الاصطناعي باستخدام Azure AI Foundry RAG
2. **تجربة نماذج مختلفة**: تجربة Qwen، DeepSeek، وعائلات النماذج الأخرى
3. **تحسين الأداء**: ضبط الإعدادات لتناسب أجهزتك
4. **بناء تطبيقات مخصصة**: استخدام Foundry Local SDK في مشاريعك الخاصة

## موارد إضافية

### الوثائق
- [مرجع Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [دليل تثبيت Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [كتالوج النماذج](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### كود العينات
- [العينة 01 من Module08](./samples/01/README.md) - بداية محادثة REST
- [العينة 02 من Module08](./samples/02/README.md) - تكامل OpenAI SDK
- [العينة 03 من Module08](./samples/03/README.md) - اكتشاف النماذج واختبار الأداء

### المجتمع
- [مناقشات Foundry Local على GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [مجتمع Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**مدة الجلسة**: 30 دقيقة عملية + 15 دقيقة للأسئلة
**مستوى الصعوبة**: مبتدئ
**المتطلبات الأساسية**: Windows 11، Python 3.10+، صلاحيات المسؤول

## سيناريو العينة وتخطيط الورشة

| سكربت الورشة / دفتر الملاحظات | السيناريو | الهدف | المدخلات النموذجية | البيانات المطلوبة |
|-------------------------------|-----------|-------|--------------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | فريق تكنولوجيا المعلومات الداخلي يقيم الاستنتاج على الجهاز لبوابة تقييم الخصوصية | إثبات أن SLM المحلي يستجيب بزمن استجابة أقل من الثانية على الطلبات القياسية | "اذكر فائدتين للاستنتاج المحلي." | لا شيء (طلب واحد) |
| كود تعديل البداية السريعة | مطور ينقل سكربت OpenAI الحالي إلى Foundry Local | إظهار التوافق السريع | "اذكر فائدتين للاستنتاج المحلي." | طلب داخلي فقط |

### سرد السيناريو
يجب على فريق الأمن والامتثال التحقق مما إذا كان يمكن معالجة بيانات النموذج الأولي الحساسة محليًا. يقومون بتشغيل سكربت الإعداد مع عدة طلبات (الخصوصية، زمن الاستجابة، التكلفة) باستخدام وضع درجة الحرارة الحتمية=0 لالتقاط المخرجات الأساسية للمقارنة لاحقًا (اختبار الأداء في الجلسة 3 ومقارنة SLM مقابل LLM في الجلسة 4).

### مجموعة الطلبات الأساسية JSON (اختياري)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

استخدم هذه القائمة لإنشاء حلقة تقييم قابلة للتكرار أو لتغذية إطار اختبار الانحدار المستقبلي.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.