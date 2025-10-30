<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T10:49:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ar"
}
-->
# AGENTS.md

> **دليل المطورين للمساهمة في EdgeAI للمبتدئين**

> يوفر هذا المستند معلومات شاملة للمطورين، وكلاء الذكاء الاصطناعي، والمساهمين الذين يعملون مع هذا المستودع. يغطي الإعداد، سير العمل التطويري، الاختبار، وأفضل الممارسات.

> **آخر تحديث**: 30 أكتوبر 2025 | **إصدار المستند**: 3.0

## جدول المحتويات

- [نظرة عامة على المشروع](../..)
- [هيكل المستودع](../..)
- [المتطلبات الأساسية](../..)
- [أوامر الإعداد](../..)
- [سير العمل التطويري](../..)
- [تعليمات الاختبار](../..)
- [إرشادات نمط الكود](../..)
- [إرشادات طلب السحب](../..)
- [نظام الترجمة](../..)
- [تكامل Foundry Local](../..)
- [البناء والنشر](../..)
- [المشاكل الشائعة واستكشاف الأخطاء وإصلاحها](../..)
- [الموارد الإضافية](../..)
- [ملاحظات خاصة بالمشروع](../..)
- [الحصول على المساعدة](../..)

## نظرة عامة على المشروع

EdgeAI للمبتدئين هو مستودع تعليمي شامل يهدف إلى تعليم تطوير الذكاء الاصطناعي الطرفي باستخدام نماذج اللغة الصغيرة (SLMs). يغطي الدورة أساسيات EdgeAI، نشر النماذج، تقنيات التحسين، وتنفيذات جاهزة للإنتاج باستخدام Microsoft Foundry Local ومجموعة من أطر الذكاء الاصطناعي.

**التقنيات الرئيسية:**
- Python 3.8+ (اللغة الأساسية لعينات الذكاء الاصطناعي/التعلم الآلي)
- .NET C# (عينات الذكاء الاصطناعي/التعلم الآلي)
- JavaScript/Node.js مع Electron (لتطبيقات سطح المكتب)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- أطر الذكاء الاصطناعي: LangChain، Semantic Kernel، Chainlit
- تحسين النماذج: Llama.cpp، Microsoft Olive، OpenVINO، Apple MLX

**نوع المستودع:** مستودع محتوى تعليمي يحتوي على 8 وحدات و10 تطبيقات عينة شاملة

**الهيكلية:** مسار تعلم متعدد الوحدات مع عينات عملية توضح أنماط نشر الذكاء الاصطناعي الطرفي

## هيكل المستودع

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## المتطلبات الأساسية

### الأدوات المطلوبة

- **Python 3.8+** - لعينات الذكاء الاصطناعي/التعلم الآلي والمفكرات
- **Node.js 16+** - لتطبيق العينة Electron
- **Git** - للتحكم في الإصدارات
- **Microsoft Foundry Local** - لتشغيل نماذج الذكاء الاصطناعي محليًا

### الأدوات الموصى بها

- **Visual Studio Code** - مع إضافات Python، Jupyter، وPylance
- **Windows Terminal** - لتجربة أفضل مع سطر الأوامر (لمستخدمي Windows)
- **Docker** - للتطوير داخل الحاويات (اختياري)

### متطلبات النظام

- **RAM**: 8GB كحد أدنى، يوصى بـ 16GB+ للسيناريوهات متعددة النماذج
- **التخزين**: مساحة خالية 10GB+ للنماذج والاعتماديات
- **نظام التشغيل**: Windows 10/11، macOS 11+، أو Linux (Ubuntu 20.04+)
- **المعدات**: وحدة معالجة مركزية تدعم AVX2؛ وحدة معالجة رسومات (CUDA، Qualcomm NPU) اختيارية ولكن يوصى بها

### المتطلبات المعرفية

- فهم أساسي لبرمجة Python
- الإلمام بواجهات سطر الأوامر
- فهم مفاهيم الذكاء الاصطناعي/التعلم الآلي (لتطوير العينات)
- سير عمل Git وعمليات طلب السحب

## أوامر الإعداد

### إعداد المستودع

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### إعداد عينات Python (الوحدة 08 وعينات ورشة العمل)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### إعداد عينات Node.js (العينة 08 - تطبيق دردشة Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### إعداد Foundry Local

Foundry Local مطلوب لتشغيل العينات. قم بتنزيله وتثبيته من المستودع الرسمي:

**التثبيت:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **يدويًا**: قم بالتنزيل من [صفحة الإصدارات](https://github.com/microsoft/Foundry-Local/releases)

**البدء السريع:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**ملاحظة**: يقوم Foundry Local تلقائيًا باختيار أفضل نموذج مناسب لمعداتك (CUDA GPU، Qualcomm NPU، أو CPU).

## سير العمل التطويري

### تطوير المحتوى

يحتوي هذا المستودع بشكل أساسي على **محتوى تعليمي Markdown**. عند إجراء تغييرات:

1. قم بتحرير ملفات `.md` في أدلة الوحدات المناسبة
2. اتبع أنماط التنسيق الحالية
3. تأكد من أن أمثلة الكود دقيقة ومختبرة
4. قم بتحديث المحتوى المترجم المقابل إذا لزم الأمر (أو دع الأتمتة تتولى ذلك)

### تطوير تطبيقات العينة

لعينات Python في الوحدة 08 (العينات 01-07، 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

لعينات ورشة العمل Python:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

للعينة Electron (العينة 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### اختبار تطبيقات العينة

عينات Python لا تحتوي على اختبارات آلية ولكن يمكن التحقق منها عن طريق تشغيلها:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

العينة Electron تحتوي على بنية اختبار:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## تعليمات الاختبار

### التحقق من المحتوى

يستخدم المستودع سير عمل ترجمة آلي. لا يتطلب اختبار يدوي للترجمات.

**التحقق اليدوي لتغييرات المحتوى:**
1. معاينة عرض Markdown لملفات `.md`
2. التحقق من أن جميع الروابط تشير إلى أهداف صحيحة
3. اختبار أي مقتطفات كود مضمنة في الوثائق
4. التأكد من تحميل الصور بشكل صحيح

### اختبار تطبيقات العينة

**العينة Module08/samples/08 (تطبيق Electron) تحتوي على اختبارات شاملة:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**يجب اختبار عينات Python يدويًا:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## إرشادات نمط الكود

### محتوى Markdown

- استخدم تسلسل هرمي متسق للعناوين (# للعنوان، ## للأقسام الرئيسية، ### للأقسام الفرعية)
- قم بتضمين كتل الكود مع محددات اللغة: ```python، ```bash، ```javascript
- اتبع التنسيق الحالي للجداول، القوائم، والتأكيد
- اجعل السطور قابلة للقراءة (استهدف ~80-100 حرفًا، ولكن ليس بشكل صارم)
- استخدم الروابط النسبية للإشارات الداخلية

### نمط كود Python

- اتبع اتفاقيات PEP 8
- استخدم تلميحات النوع حيثما كان ذلك مناسبًا
- قم بتضمين docstrings للوظائف والفئات
- استخدم أسماء متغيرات ذات معنى
- اجعل الوظائف مركزة ومختصرة

### نمط كود JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**الاتفاقيات الرئيسية:**
- تم توفير تكوين ESLint في العينة 08
- Prettier لتنسيق الكود
- استخدم بناء الجملة الحديث ES6+
- اتبع الأنماط الحالية في قاعدة الكود

## إرشادات طلب السحب

### سير عمل المساهمة

1. **قم بتفريع المستودع** وأنشئ فرعًا جديدًا من `main`
2. **قم بإجراء تغييراتك** باتباع إرشادات نمط الكود
3. **اختبر بدقة** باستخدام تعليمات الاختبار أعلاه
4. **قم بالالتزام برسائل واضحة** باتباع تنسيق الالتزامات التقليدية
5. **ادفع إلى تفريعك** وأنشئ طلب سحب
6. **استجب للتعليقات** من المشرفين أثناء المراجعة

### اتفاقية تسمية الفروع

- `feature/<module>-<description>` - للميزات الجديدة أو المحتوى
- `fix/<module>-<description>` - لإصلاح الأخطاء
- `docs/<description>` - لتحسين الوثائق
- `refactor/<description>` - لإعادة هيكلة الكود

### تنسيق رسالة الالتزام

اتبع [الالتزامات التقليدية](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**أمثلة:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### تنسيق العنوان
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### قواعد السلوك

يجب على جميع المساهمين اتباع [قواعد السلوك مفتوحة المصدر من Microsoft](https://opensource.microsoft.com/codeofconduct/). يرجى مراجعة [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) قبل المساهمة.

### قبل التقديم

**لتغييرات المحتوى:**
- معاينة جميع ملفات Markdown المعدلة
- التحقق من الروابط والصور
- التحقق من الأخطاء الإملائية والنحوية

**لتغييرات كود العينة (Module08/samples/08):**
```bash
npm run lint
npm test
```

**لتغييرات عينات Python:**
- اختبار تشغيل العينة بنجاح
- التحقق من عمل معالجة الأخطاء
- التحقق من التوافق مع Foundry Local

### عملية المراجعة

- يتم مراجعة تغييرات المحتوى التعليمي من حيث الدقة والوضوح
- يتم اختبار عينات الكود من حيث الوظائف
- يتم التعامل مع تحديثات الترجمة تلقائيًا بواسطة GitHub Actions

## نظام الترجمة

**هام:** يستخدم هذا المستودع ترجمة آلية عبر GitHub Actions.

- توجد الترجمات في دليل `/translations/` (50+ لغة)
- يتم تشغيلها تلقائيًا عبر سير العمل `co-op-translator.yml`
- **لا تقم بتحرير ملفات الترجمة يدويًا** - سيتم الكتابة فوقها
- قم بتحرير ملفات المصدر الإنجليزية فقط في الدليل الجذر وأدلة الوحدات
- يتم إنشاء الترجمات تلقائيًا عند الدفع إلى الفرع `main`

## تكامل Foundry Local

تتطلب معظم عينات الوحدة 08 تشغيل Microsoft Foundry Local.

### التثبيت والإعداد

**تثبيت Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**تثبيت Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### بدء تشغيل Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### استخدام SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### التحقق من Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### متغيرات البيئة للعينات

تستخدم معظم العينات هذه المتغيرات البيئية:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**ملاحظة**: عند استخدام `FoundryLocalManager`، يقوم SDK تلقائيًا بمعالجة اكتشاف الخدمة وتحميل النموذج. تضمن أسماء النماذج المستعارة (مثل `phi-3.5-mini`) اختيار أفضل نموذج مناسب لمعداتك.

## البناء والنشر

### نشر المحتوى

هذا المستودع هو في الأساس وثائق - لا توجد عملية بناء مطلوبة للمحتوى.

### بناء تطبيقات العينة

**تطبيق Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**عينات Python:**
لا توجد عملية بناء - يتم تشغيل العينات مباشرة باستخدام مترجم Python.

## المشاكل الشائعة واستكشاف الأخطاء وإصلاحها

> **نصيحة**: تحقق من [مشاكل GitHub](https://github.com/microsoft/edgeai-for-beginners/issues) للحصول على المشاكل والحلول المعروفة.

### المشاكل الحرجة (المعوقة)

#### Foundry Local لا يعمل
**المشكلة:** تفشل العينات مع أخطاء الاتصال

**الحل:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### المشاكل الشائعة (المتوسطة)

#### مشاكل بيئة Python الافتراضية
**المشكلة:** أخطاء استيراد الوحدات

**الحل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### مشاكل بناء Electron
**المشكلة:** فشل npm install أو البناء

**الحل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### مشاكل سير العمل (البسيطة)

#### تعارضات سير عمل الترجمة
**المشكلة:** تعارض طلبات الترجمة مع تغييراتك

**الحل:**
- قم بتحرير ملفات المصدر الإنجليزية فقط
- دع سير عمل الترجمة الآلي يتولى الترجمة
- إذا حدثت تعارضات، قم بدمج `main` في فرعك بعد دمج الترجمات

#### فشل تنزيل النموذج
**المشكلة:** يفشل Foundry Local في تنزيل النماذج

**الحل:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## الموارد الإضافية

### مسارات التعلم
- **مسار المبتدئين:** الوحدات 01-02 (7-9 ساعات)
- **مسار المتوسطين:** الوحدات 03-04 (9-11 ساعات)
- **مسار المتقدمين:** الوحدات 05-07 (12-15 ساعات)
- **مسار الخبراء:** الوحدة 08 (8-10 ساعات)
- **ورشة العمل العملية:** مواد الورشة (6-8 ساعات)

### محتوى الوحدات الرئيسية
- **Module01:** أساسيات EdgeAI ودراسات الحالة الواقعية
- **Module02:** عائلات نماذج اللغة الصغيرة (SLM) والهياكل
- **Module03:** استراتيجيات النشر المحلي والسحابي
- **Module04:** تحسين النماذج باستخدام أطر متعددة (Llama.cpp، Microsoft Olive، OpenVINO، Qualcomm QNN، Apple MLX)
- **Module05:** SLMOps - عمليات الإنتاج
- **Module06:** وكلاء الذكاء الاصطناعي واستدعاء الوظائف
- **Module07:** تنفيذات خاصة بالمنصات
- **Module08:** أدوات Foundry Local مع 10 عينات شاملة

### الاعتماديات الخارجية
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - تشغيل نماذج الذكاء الاصطناعي محليًا مع واجهة API متوافقة مع OpenAI
  - [الوثائق](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - إطار تحسين
- [Microsoft Olive](https://microsoft.github.io/Olive/) - مجموعة أدوات تحسين النماذج
- [OpenVINO](https://docs.openvino.ai/) - مجموعة أدوات تحسين Intel

## ملاحظات خاصة بالمشروع

### تطبيقات العينة للوحدة 08

يتضمن المستودع 10 تطبيقات عينة شاملة:

1. **01-REST Chat Quickstart** - تكامل أساسي مع OpenAI SDK
2. **02-OpenAI SDK Integration** - ميزات متقدمة لـ SDK
3. **03-Model Discovery & Benchmarking** - أدوات مقارنة النماذج
4. **04-Chainlit RAG Application** - توليد معزز بالاسترجاع
5. **05-Multi-Agent Orchestration** - تنسيق الوكلاء الأساسي
6. **06-Models-as-Tools Router** - توجيه النماذج الذكي
7. **07-Direct API Client** - تكامل API منخفض المستوى
8. **08-Windows 11 Chat App** - تطبيق سطح مكتب Electron أصلي
9. **09-Advanced Multi-Agent System** - تنسيق وكلاء معقد
10. **إطار أدوات Foundry** - تكامل LangChain/Semantic Kernel

### تطبيقات ورش العمل النموذجية

تتضمن ورشة العمل 6 جلسات متدرجة مع تطبيقات عملية:

1. **الجلسة 01** - إعداد الدردشة مع تكامل Foundry Local
2. **الجلسة 02** - خط أنابيب RAG والتقييم باستخدام RAGAS
3. **الجلسة 03** - قياس أداء النماذج مفتوحة المصدر
4. **الجلسة 04** - مقارنة النماذج واختيار الأنسب
5. **الجلسة 05** - أنظمة تنسيق متعددة الوكلاء
6. **الجلسة 06** - توجيه النماذج وإدارة خطوط الأنابيب

كل نموذج يوضح جوانب مختلفة من تطوير الذكاء الاصطناعي الطرفي باستخدام Foundry Local.

### اعتبارات الأداء

- تم تحسين SLMs للنشر الطرفي (2-16 جيجابايت من ذاكرة الوصول العشوائي)
- يوفر الاستدلال المحلي أوقات استجابة تتراوح بين 50-500 مللي ثانية
- تقنيات التكميم تحقق تقليل الحجم بنسبة 75% مع الاحتفاظ بنسبة 85% من الأداء
- قدرات المحادثة في الوقت الفعلي باستخدام النماذج المحلية

### الأمن والخصوصية

- تتم جميع المعالجة محليًا - لا يتم إرسال البيانات إلى السحابة
- مناسب للتطبيقات الحساسة للخصوصية (الرعاية الصحية، المالية)
- يلبي متطلبات سيادة البيانات
- يعمل Foundry Local بالكامل على الأجهزة المحلية

## الحصول على المساعدة

### الوثائق

- **الملف الرئيسي README**: [README.md](README.md) - نظرة عامة على المستودع ومسارات التعلم
- **دليل الدراسة**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - موارد التعلم والجدول الزمني
- **الدعم**: [SUPPORT.md](SUPPORT.md) - كيفية الحصول على المساعدة
- **الأمان**: [SECURITY.md](SECURITY.md) - الإبلاغ عن مشكلات الأمان

### دعم المجتمع

- **مشكلات GitHub**: [الإبلاغ عن الأخطاء أو طلب الميزات](https://github.com/microsoft/edgeai-for-beginners/issues)
- **مناقشات GitHub**: [طرح الأسئلة ومشاركة الأفكار](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **مشكلات Foundry Local**: [مشكلات تقنية مع Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### الاتصال

- **المشرفون**: انظر [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **مشكلات الأمان**: اتبع الإبلاغ المسؤول في [SECURITY.md](SECURITY.md)
- **دعم Microsoft**: للحصول على دعم المؤسسات، تواصل مع خدمة عملاء Microsoft

### موارد إضافية

- **Microsoft Learn**: [مسارات تعلم الذكاء الاصطناعي وتعلم الآلة](https://learn.microsoft.com/training/browse/?products=ai-services)
- **وثائق Foundry Local**: [الوثائق الرسمية](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **نماذج المجتمع**: تحقق من [مناقشات GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) للحصول على مساهمات المجتمع

---

**هذا مستودع تعليمي يركز على تعليم تطوير الذكاء الاصطناعي الطرفي. النمط الأساسي للمساهمة هو تحسين المحتوى التعليمي وإضافة/تعزيز التطبيقات النموذجية التي توضح مفاهيم الذكاء الاصطناعي الطرفي.**

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.