# الجلسة الأولى: البدء مع Foundry Local

## الملخص

تعلم كيفية تثبيت وتكوين وتشغيل نماذج الذكاء الاصطناعي الأولى باستخدام Microsoft Foundry Local. تقدم هذه الجلسة العملية مقدمة خطوة بخطوة للاستدلال المحلي، بدءًا من التثبيت وحتى بناء أول تطبيق دردشة باستخدام نماذج مثل Phi-4، Qwen، وDeepSeek.

## أهداف التعلم

بنهاية هذه الجلسة، ستتمكن من:

- **التثبيت والتكوين**: إعداد Foundry Local مع التحقق من التثبيت بشكل صحيح
- **إتقان عمليات CLI**: استخدام Foundry Local CLI لإدارة النماذج ونشرها
- **تشغيل النموذج الأول**: نشر والتفاعل بنجاح مع نموذج ذكاء اصطناعي محلي
- **بناء تطبيق دردشة**: إنشاء تطبيق دردشة أساسي باستخدام Foundry Local Python SDK
- **فهم الذكاء الاصطناعي المحلي**: استيعاب أساسيات الاستدلال المحلي وإدارة النماذج

## المتطلبات الأساسية

### متطلبات النظام

- **ويندوز**: Windows 11 (22H2 أو أحدث) أو **macOS**: macOS 11+ (دعم محدود)
- **الذاكرة**: 8GB كحد أدنى، يوصى بـ 16GB+
- **التخزين**: مساحة خالية 10GB+ للنماذج
- **بايثون**: الإصدار 3.10 أو أحدث مثبت
- **صلاحيات المسؤول**: صلاحيات المسؤول للتثبيت

### بيئة التطوير

- Visual Studio Code مع إضافة Python (موصى به)
- الوصول إلى سطر الأوامر (PowerShell على ويندوز، Terminal على macOS)
- Git لاستنساخ المستودعات (اختياري)

## سير ورشة العمل (30 دقيقة)

### الخطوة 1: تثبيت Foundry Local (5 دقائق)

#### تثبيت ويندوز

قم بتثبيت Foundry Local باستخدام مدير الحزم الخاص بويندوز:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

بديل: قم بتنزيله مباشرة من [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### تثبيت macOS (دعم محدود)

> [!NOTE] 
> دعم macOS حاليًا في مرحلة المعاينة. تحقق من الوثائق الرسمية للحصول على أحدث المعلومات.

إذا كان متاحًا، قم بالتثبيت باستخدام Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**بديل لمستخدمي macOS:**
- استخدم Windows 11 VM (Parallels/UTM) واتبع خطوات ويندوز
- قم بتشغيله عبر الحاوية إذا كان متاحًا وقم بتكوين `FOUNDRY_LOCAL_ENDPOINT`

### الخطوة 2: التحقق من التثبيت (3 دقائق)

بعد التثبيت، أعد تشغيل الطرفية وتحقق من عمل Foundry Local:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

يجب أن يظهر الإخراج المتوقع معلومات الإصدار والأوامر المتاحة.

### الخطوة 3: إعداد بيئة بايثون (5 دقائق)

قم بإنشاء بيئة بايثون مخصصة لهذه الورشة:

**ويندوز:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### الخطوة 4: تشغيل النموذج الأول (7 دقائق)

الآن دعونا نشغل أول نموذج ذكاء اصطناعي محلي!

#### البدء مع Phi-4 Mini (النموذج الأول الموصى به)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> يقوم هذا الأمر بتنزيل النموذج (لأول مرة) ويبدأ خدمة Foundry Local تلقائيًا.

#### التحقق مما يتم تشغيله

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### تجربة نماذج مختلفة

بمجرد تشغيل phi-4-mini، جرب نماذج أخرى:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### الخطوة 5: بناء أول تطبيق دردشة (10 دقائق)

الآن دعونا ننشئ تطبيق بايثون يستخدم النماذج التي بدأناها للتو.

#### إنشاء سكريبت الدردشة

قم بإنشاء ملف جديد يسمى `my_first_chat.py` (أو استخدم العينة المقدمة):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **أمثلة ذات صلة**: للاستخدام المتقدم، انظر:
>
> - **عينة بايثون**: `Workshop/samples/session01/chat_bootstrap.py` - يتضمن استجابات متدفقة ومعالجة الأخطاء
> - **دفتر Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - نسخة تفاعلية مع شروحات مفصلة

#### اختبار تطبيق الدردشة الخاص بك

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

بديل: استخدم العينات المقدمة مباشرة

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

أو استكشف الدفتر التفاعلي
افتح Workshop/notebooks/session01_chat_bootstrap.ipynb في VS Code

جرب هذه المحادثات النموذجية:

- "ما هو Microsoft Foundry Local؟"
- "اذكر 3 فوائد لتشغيل نماذج الذكاء الاصطناعي محليًا"
- "ساعدني في فهم الذكاء الاصطناعي الطرفي"

## ما الذي أنجزته

تهانينا! لقد نجحت في:

1. ✅ **تثبيت Foundry Local** والتحقق من عمله
2. ✅ **تشغيل أول نموذج ذكاء اصطناعي** (phi-4-mini) محليًا
3. ✅ **اختبار نماذج مختلفة** عبر سطر الأوامر
4. ✅ **بناء تطبيق دردشة** يتصل بالذكاء الاصطناعي المحلي
5. ✅ **تجربة الاستدلال المحلي للذكاء الاصطناعي** بدون الاعتماد على السحابة

## فهم ما حدث

### الاستدلال المحلي للذكاء الاصطناعي

- تعمل نماذج الذكاء الاصطناعي بالكامل على جهازك
- لا يتم إرسال أي بيانات إلى السحابة
- يتم إنشاء الاستجابات محليًا باستخدام وحدة المعالجة المركزية/وحدة معالجة الرسومات الخاصة بك
- يتم الحفاظ على الخصوصية والأمان

### إدارة النماذج

- `foundry model run` يقوم بتنزيل وتشغيل النماذج
- **FoundryLocalManager SDK** يتعامل تلقائيًا مع بدء الخدمة وتحميل النموذج
- يتم تخزين النماذج محليًا للاستخدام المستقبلي
- يمكن تنزيل نماذج متعددة ولكن عادةً يتم تشغيل نموذج واحد في كل مرة
- تقوم الخدمة بإدارة دورة حياة النموذج تلقائيًا

### مقارنة بين SDK وCLI

- **نهج CLI**: إدارة النماذج يدويًا باستخدام `foundry model run <model>`
- **نهج SDK**: إدارة الخدمة والنماذج تلقائيًا باستخدام `FoundryLocalManager(alias)`
- **التوصية**: استخدم SDK للتطبيقات، CLI للاختبار والاستكشاف

## مرجع الأوامر الشائعة

### أوامر CLI الأساسية

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### توصيات النماذج

- **phi-4-mini**: أفضل نموذج للمبتدئين - سريع، خفيف الوزن، جودة جيدة
- **qwen2.5-0.5b**: أسرع استدلال، استخدام ذاكرة منخفض
- **gpt-oss-20b**: استجابات بجودة أعلى، يحتاج موارد أكثر
- **deepseek-coder-1.3b**: مُحسن للبرمجة والمهام البرمجية

## استكشاف الأخطاء وإصلاحها

### "لم يتم العثور على أمر Foundry"

**الحل:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "فشل تحميل النموذج"

**الحل:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "رفض الاتصال على localhost"

**الحل:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## الخطوات التالية

### الإجراءات الفورية التالية

1. **جرب** نماذج ومطالبات مختلفة
2. **عدل** تطبيق الدردشة الخاص بك لتجربة نماذج مختلفة
3. **أنشئ** مطالباتك الخاصة واختبر الاستجابات
4. **استكشف** الجلسة الثانية: بناء تطبيقات RAG

### مسار التعلم المتقدم

1. **الجلسة الثانية**: بناء حلول الذكاء الاصطناعي باستخدام RAG (الاسترجاع المعزز بالتوليد)
2. **الجلسة الثالثة**: مقارنة بين نماذج مفتوحة المصدر المختلفة
3. **الجلسة الرابعة**: العمل مع نماذج متقدمة
4. **الجلسة الخامسة**: بناء أنظمة ذكاء اصطناعي متعددة الوكلاء

## متغيرات البيئة (اختياري)

للاستخدام المتقدم، يمكنك إعداد متغيرات البيئة التالية:

| المتغير | الغرض | المثال |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | النموذج الافتراضي للاستخدام | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | تجاوز عنوان URL للنقطة النهائية | `http://localhost:5273/v1` |

قم بإنشاء ملف `.env` في دليل المشروع الخاص بك:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## موارد إضافية

### الوثائق

- [مرجع Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [دليل تثبيت Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [كتالوج النماذج](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### عينات الكود

- **عينة بايثون للجلسة الأولى**: `Workshop/samples/session01/chat_bootstrap.py` - تطبيق دردشة كامل مع استجابات متدفقة
- **دفتر الجلسة الأولى**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - دليل تفاعلي  
- [عينة Module08 الأولى](../Module08/samples/01/README.md) - بدء سريع للدردشة عبر REST
- [عينة Module08 الثانية](../Module08/samples/02/README.md) - تكامل OpenAI SDK
- [عينة Module08 الثالثة](../Module08/samples/03/README.md) - اكتشاف النماذج واختبار الأداء

### المجتمع

- [مناقشات GitHub لـ Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [مجتمع Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**مدة الجلسة**: 30 دقيقة عملي + 15 دقيقة أسئلة وأجوبة  
**مستوى الصعوبة**: مبتدئ  
**المتطلبات الأساسية**: Windows 11/macOS 11+، Python 3.10+، صلاحيات المسؤول

## سيناريو مثال ورشة العمل

### السياق الواقعي

**السيناريو**: فريق تكنولوجيا المعلومات في شركة يحتاج إلى تقييم الاستدلال الذاتي للذكاء الاصطناعي لمعالجة ملاحظات الموظفين الحساسة دون إرسال البيانات إلى خدمات خارجية.

**هدفك**: إثبات أن نماذج الذكاء الاصطناعي المحلية يمكن أن تقدم استجابات بجودة عالية مع زمن استجابة أقل من الثانية مع الحفاظ على الخصوصية الكاملة للبيانات.

### مطالبات الاختبار

استخدم هذه المطالبات للتحقق من إعدادك:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### معايير النجاح

- ✅ جميع المطالبات تحصل على استجابات في أقل من ثانيتين
- ✅ لا يتم إرسال أي بيانات خارج جهازك المحلي
- ✅ الاستجابات ذات صلة ومفيدة
- ✅ يعمل تطبيق الدردشة الخاص بك بسلاسة

يضمن هذا التحقق أن إعداد Foundry Local الخاص بك جاهز للورش المتقدمة في الجلسات 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->