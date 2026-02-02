# AGENTS.md

> **راهنمای توسعه‌دهندگان برای مشارکت در EdgeAI برای مبتدیان**
> 
> این سند اطلاعات جامعی برای توسعه‌دهندگان، عوامل هوش مصنوعی و مشارکت‌کنندگان در این مخزن ارائه می‌دهد. شامل تنظیمات، جریان‌های کاری توسعه، تست و بهترین شیوه‌ها است.
> 
> **آخرین به‌روزرسانی**: 30 اکتبر 2025 | **نسخه سند**: 3.0

## فهرست مطالب

- [نمای کلی پروژه](../..)
- [ساختار مخزن](../..)
- [پیش‌نیازها](../..)
- [دستورات تنظیم](../..)
- [جریان کاری توسعه](../..)
- [دستورالعمل‌های تست](../..)
- [راهنمای سبک کدنویسی](../..)
- [راهنمای درخواست‌های کشش](../..)
- [سیستم ترجمه](../..)
- [ادغام محلی Foundry](../..)
- [ساخت و استقرار](../..)
- [مشکلات رایج و رفع اشکال](../..)
- [منابع اضافی](../..)
- [یادداشت‌های خاص پروژه](../..)
- [دریافت کمک](../..)

## نمای کلی پروژه

EdgeAI برای مبتدیان یک مخزن آموزشی جامع است که توسعه هوش مصنوعی لبه‌ای با مدل‌های زبان کوچک (SLM) را آموزش می‌دهد. این دوره شامل اصول EdgeAI، استقرار مدل، تکنیک‌های بهینه‌سازی و پیاده‌سازی‌های آماده تولید با استفاده از Microsoft Foundry Local و چارچوب‌های مختلف هوش مصنوعی است.

**فناوری‌های کلیدی:**
- Python 3.8+ (زبان اصلی برای نمونه‌های AI/ML)
- .NET C# (نمونه‌های AI/ML)
- JavaScript/Node.js با Electron (برای برنامه‌های دسکتاپ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- چارچوب‌های هوش مصنوعی: LangChain، Semantic Kernel، Chainlit
- بهینه‌سازی مدل: Llama.cpp، Microsoft Olive، OpenVINO، Apple MLX

**نوع مخزن:** مخزن محتوای آموزشی با 8 ماژول و 10 نمونه برنامه جامع

**معماری:** مسیر یادگیری چندماژوله با نمونه‌های عملی که الگوهای استقرار هوش مصنوعی لبه‌ای را نشان می‌دهند

## ساختار مخزن

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

## پیش‌نیازها

### ابزارهای مورد نیاز

- **Python 3.8+** - برای نمونه‌ها و نوت‌بوک‌های AI/ML
- **Node.js 16+** - برای برنامه نمونه Electron
- **Git** - برای کنترل نسخه
- **Microsoft Foundry Local** - برای اجرای مدل‌های هوش مصنوعی به صورت محلی

### ابزارهای پیشنهادی

- **Visual Studio Code** - با افزونه‌های Python، Jupyter و Pylance
- **Windows Terminal** - برای تجربه بهتر خط فرمان (کاربران ویندوز)
- **Docker** - برای توسعه کانتینری (اختیاری)

### نیازمندی‌های سیستم

- **RAM**: حداقل 8 گیگابایت، 16 گیگابایت یا بیشتر برای سناریوهای چندمدلی توصیه می‌شود
- **فضای ذخیره‌سازی**: حداقل 10 گیگابایت فضای آزاد برای مدل‌ها و وابستگی‌ها
- **سیستم‌عامل**: Windows 10/11، macOS 11+ یا Linux (Ubuntu 20.04+)
- **سخت‌افزار**: پردازنده با پشتیبانی از AVX2؛ GPU (CUDA، Qualcomm NPU) اختیاری اما توصیه‌شده

### پیش‌نیازهای دانش

- درک پایه‌ای از برنامه‌نویسی Python
- آشنایی با رابط‌های خط فرمان
- درک مفاهیم AI/ML (برای توسعه نمونه‌ها)
- جریان‌های کاری Git و فرآیندهای درخواست کشش

## دستورات تنظیم

### تنظیم مخزن

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### تنظیم نمونه‌های Python (ماژول08 و نمونه‌های کارگاهی)

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

### تنظیم نمونه‌های Node.js (نمونه 08 - برنامه چت ویندوز)

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

### تنظیم Foundry Local

Foundry Local برای اجرای نمونه‌ها مورد نیاز است. از مخزن رسمی دانلود و نصب کنید:

**نصب:**
- **ویندوز**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **دستی**: دانلود از [صفحه انتشار](https://github.com/microsoft/Foundry-Local/releases)

**شروع سریع:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**توجه**: Foundry Local به طور خودکار بهترین نوع مدل را برای سخت‌افزار شما انتخاب می‌کند (GPU CUDA، NPU Qualcomm یا CPU).

## جریان کاری توسعه

### توسعه محتوا

این مخزن عمدتاً شامل **محتوای آموزشی Markdown** است. هنگام ایجاد تغییرات:

1. فایل‌های `.md` را در دایرکتوری‌های ماژول مناسب ویرایش کنید
2. الگوهای قالب‌بندی موجود را دنبال کنید
3. اطمینان حاصل کنید که نمونه‌های کد دقیق و تست‌شده هستند
4. در صورت لزوم محتوای ترجمه‌شده مربوطه را به‌روزرسانی کنید (یا اجازه دهید اتوماسیون این کار را انجام دهد)

### توسعه برنامه نمونه

برای نمونه‌های Python ماژول08 (نمونه‌های 01-07، 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

برای نمونه‌های کارگاهی Python:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

برای نمونه Electron (نمونه 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### تست برنامه‌های نمونه

نمونه‌های Python تست‌های خودکار ندارند اما می‌توان با اجرای آن‌ها اعتبارسنجی کرد:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

نمونه Electron دارای زیرساخت تست است:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## دستورالعمل‌های تست

### اعتبارسنجی محتوا

مخزن از جریان‌های کاری ترجمه خودکار استفاده می‌کند. برای ترجمه‌ها نیازی به تست دستی نیست.

**اعتبارسنجی دستی برای تغییرات محتوا:**
1. رندر Markdown را با پیش‌نمایش فایل‌های `.md` بررسی کنید
2. اطمینان حاصل کنید که همه لینک‌ها به اهداف معتبر اشاره دارند
3. هر قطعه کد موجود در مستندات را تست کنید
4. بررسی کنید که تصاویر به درستی بارگذاری شوند

### تست برنامه‌های نمونه

**Module08/samples/08 (برنامه Electron) دارای تست جامع است:**
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

**نمونه‌های Python باید به صورت دستی تست شوند:**
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

## راهنمای سبک کدنویسی

### محتوای Markdown

- از سلسله‌مراتب عنوان ثابت استفاده کنید (# برای عنوان، ## برای بخش‌های اصلی، ### برای زیرمجموعه‌ها)
- بلوک‌های کد را با مشخص‌کننده زبان درج کنید: ```python, ```bash, ```javascript
- قالب‌بندی موجود برای جداول، لیست‌ها و تأکید را دنبال کنید
- خطوط را خوانا نگه دارید (هدف ~80-100 کاراکتر، اما سخت‌گیرانه نیست)
- از لینک‌های نسبی برای ارجاعات داخلی استفاده کنید

### سبک کدنویسی Python

- از کنوانسیون‌های PEP 8 پیروی کنید
- در صورت امکان از نوع‌دهی استفاده کنید
- برای توابع و کلاس‌ها توضیحات اضافه کنید
- از نام‌های متغیر معنادار استفاده کنید
- توابع را متمرکز و مختصر نگه دارید

### سبک کدنویسی JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**کنوانسیون‌های کلیدی:**
- پیکربندی ESLint در نمونه 08 ارائه شده است
- Prettier برای قالب‌بندی کد
- از سینتکس مدرن ES6+ استفاده کنید
- الگوهای موجود در کدبیس را دنبال کنید

## راهنمای درخواست‌های کشش

### جریان کاری مشارکت

1. **مخزن را فورک کنید** و یک شاخه جدید از `main` ایجاد کنید
2. **تغییرات خود را اعمال کنید** با پیروی از راهنمای سبک کدنویسی
3. **به طور کامل تست کنید** با استفاده از دستورالعمل‌های تست بالا
4. **با پیام‌های واضح کامیت کنید** با فرمت کامیت‌های متعارف
5. **به فورک خود پوش کنید** و یک درخواست کشش ایجاد کنید
6. **به بازخوردها پاسخ دهید** از سوی نگهدارندگان در طول بررسی

### کنوانسیون نام‌گذاری شاخه‌ها

- `feature/<module>-<description>` - برای ویژگی‌ها یا محتواهای جدید
- `fix/<module>-<description>` - برای رفع اشکالات
- `docs/<description>` - برای بهبود مستندات
- `refactor/<description>` - برای بازسازی کد

### فرمت پیام کامیت

از [کامیت‌های متعارف](https://www.conventionalcommits.org/) پیروی کنید:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**نمونه‌ها:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### فرمت عنوان
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### کد اخلاقی

تمام مشارکت‌کنندگان باید از [کد اخلاقی منبع باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/) پیروی کنند. لطفاً قبل از مشارکت [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) را مرور کنید.

### قبل از ارسال

**برای تغییرات محتوا:**
- تمام فایل‌های Markdown اصلاح‌شده را پیش‌نمایش کنید
- لینک‌ها و تصاویر را بررسی کنید
- خطاهای تایپی و گرامری را بررسی کنید

**برای تغییرات کد نمونه (Module08/samples/08):**
```bash
npm run lint
npm test
```

**برای تغییرات نمونه‌های Python:**
- بررسی کنید که نمونه به درستی اجرا شود
- اطمینان حاصل کنید که مدیریت خطا کار می‌کند
- سازگاری با Foundry Local را بررسی کنید

### فرآیند بررسی

- تغییرات محتوای آموزشی از نظر دقت و وضوح بررسی می‌شوند
- نمونه‌های کد از نظر عملکرد تست می‌شوند
- به‌روزرسانی‌های ترجمه به‌طور خودکار توسط GitHub Actions مدیریت می‌شوند

## سیستم ترجمه

**مهم:** این مخزن از ترجمه خودکار از طریق GitHub Actions استفاده می‌کند.

- ترجمه‌ها در دایرکتوری `/translations/` (50+ زبان) قرار دارند
- به‌طور خودکار از طریق جریان کاری `co-op-translator.yml` انجام می‌شود
- **فایل‌های ترجمه را به صورت دستی ویرایش نکنید** - آنها بازنویسی خواهند شد
- فقط فایل‌های منبع انگلیسی را در دایرکتوری‌های ریشه و ماژول ویرایش کنید
- ترجمه‌ها به‌طور خودکار با هر پوش به شاخه `main` ایجاد می‌شوند

## ادغام محلی Foundry

بیشتر نمونه‌های ماژول08 نیاز به اجرای Microsoft Foundry Local دارند.

### نصب و تنظیم

**نصب Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**نصب Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### شروع Foundry Local
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

### استفاده از SDK (Python)
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

### اعتبارسنجی Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### متغیرهای محیطی برای نمونه‌ها

بیشتر نمونه‌ها از این متغیرهای محیطی استفاده می‌کنند:
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

**توجه**: هنگام استفاده از `FoundryLocalManager`، SDK به‌طور خودکار کشف سرویس و بارگذاری مدل را مدیریت می‌کند. نام مستعار مدل‌ها (مانند `phi-3.5-mini`) بهترین نوع را برای سخت‌افزار شما تضمین می‌کند.

## ساخت و استقرار

### استقرار محتوا

این مخزن عمدتاً مستندات است - فرآیند ساخت برای محتوا مورد نیاز نیست.

### ساخت برنامه نمونه

**برنامه Electron (Module08/samples/08):**
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

**نمونه‌های Python:**
فرآیند ساخت ندارد - نمونه‌ها مستقیماً با مفسر Python اجرا می‌شوند.

## مشکلات رایج و رفع اشکال

> **نکته**: مشکلات شناخته‌شده و راه‌حل‌ها را در [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) بررسی کنید.

### مشکلات بحرانی (مسدودکننده)

#### Foundry Local اجرا نمی‌شود
**مشکل:** نمونه‌ها با خطاهای اتصال شکست می‌خورند

**راه‌حل:**
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

### مشکلات رایج (متوسط)

#### مشکلات محیط مجازی Python
**مشکل:** خطاهای وارد کردن ماژول

**راه‌حل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### مشکلات ساخت Electron
**مشکل:** شکست نصب npm یا ساخت

**راه‌حل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### مشکلات جریان کاری (جزئی)

#### تعارض‌های جریان کاری ترجمه
**مشکل:** درخواست کشش ترجمه با تغییرات شما تعارض دارد

**راه‌حل:**
- فقط فایل‌های منبع انگلیسی را ویرایش کنید
- اجازه دهید جریان کاری ترجمه خودکار ترجمه‌ها را مدیریت کند
- اگر تعارض رخ داد، پس از ادغام ترجمه‌ها، شاخه `main` را با شاخه خود ادغام کنید

#### شکست دانلود مدل
**مشکل:** Foundry Local نمی‌تواند مدل‌ها را دانلود کند

**راه‌حل:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## منابع اضافی

### مسیرهای یادگیری
- **مسیر مبتدی:** ماژول‌های 01-02 (7-9 ساعت)
- **مسیر متوسط:** ماژول‌های 03-04 (9-11 ساعت)
- **مسیر پیشرفته:** ماژول‌های 05-07 (12-15 ساعت)
- **مسیر متخصص:** ماژول 08 (8-10 ساعت)
- **کارگاه عملی:** مواد کارگاهی (6-8 ساعت)

### محتوای کلیدی ماژول‌ها
- **ماژول01:** اصول EdgeAI و مطالعات موردی دنیای واقعی
- **ماژول02:** خانواده‌ها و معماری‌های مدل‌های زبان کوچک (SLM)
- **ماژول03:** استراتژی‌های استقرار محلی و ابری
- **ماژول04:** بهینه‌سازی مدل با چارچوب‌های مختلف (Llama.cpp، Microsoft Olive، OpenVINO، Qualcomm QNN، Apple MLX)
- **ماژول05:** SLMOps - عملیات تولید
- **ماژول06:** عوامل هوش مصنوعی و فراخوانی توابع
- **ماژول07:** پیاده‌سازی‌های خاص پلتفرم
- **ماژول08:** ابزار Foundry Local با 10 نمونه جامع

### وابستگی‌های خارجی
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - زمان اجرای مدل هوش مصنوعی محلی با API سازگار با OpenAI
  - [مستندات](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - چارچوب بهینه‌سازی
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ابزار بهینه‌سازی مدل
- [OpenVINO](https://docs.openvino.ai/) - ابزار بهینه‌سازی Intel

## یادداشت‌های خاص پروژه

### برنامه‌های نمونه ماژول08

مخزن شامل 10 نمونه برنامه جامع است:

1. **01-REST Chat Quickstart** - ادغام اولیه OpenAI SDK
2. **02-OpenAI SDK Integration** - ویژگی‌های پیشرفته SDK
3. **03-Model Discovery & Benchmarking** - ابزارهای مقایسه مدل
4. **04-Chainlit RAG Application** - تولید تقویت‌شده با بازیابی
5. **05-Multi-Agent Orchestration** - هماهنگی عوامل پایه
6. **06-Models-as-Tools Router** - مسیریابی هوشمند مدل
7. **07-Direct API Client** - ادغام API سطح پایین
8. **08-Windows 11 Chat App** - برنامه دسکتاپ Electron بومی
9. **09-Advanced Multi-Agent System** - هماهنگی پیچیده عوامل
10. **چارچوب ابزارهای Foundry** - ادغام LangChain/Semantic Kernel

### نمونه‌های کاربردی کارگاه

این کارگاه شامل ۶ جلسه پیشرفته با پیاده‌سازی‌های عملی است:

1. **جلسه ۰۱** - راه‌اندازی چت با ادغام Foundry Local
2. **جلسه ۰۲** - خط لوله RAG و ارزیابی با RAGAS
3. **جلسه ۰۳** - ارزیابی مدل‌های متن‌باز
4. **جلسه ۰۴** - مقایسه و انتخاب مدل‌ها
5. **جلسه ۰۵** - سیستم‌های هماهنگی چند عاملی
6. **جلسه ۰۶** - مدیریت مسیر مدل و خط لوله

هر نمونه جنبه‌های مختلف توسعه هوش مصنوعی لبه‌ای با Foundry Local را نشان می‌دهد.

### ملاحظات عملکردی

- SLM‌ها برای استقرار در لبه بهینه‌سازی شده‌اند (۲-۱۶ گیگابایت RAM)
- استنتاج محلی زمان پاسخ‌دهی ۵۰-۵۰۰ میلی‌ثانیه را فراهم می‌کند
- تکنیک‌های کمینه‌سازی اندازه تا ۷۵٪ کاهش حجم با حفظ ۸۵٪ عملکرد را ممکن می‌سازند
- قابلیت مکالمه در زمان واقعی با مدل‌های محلی

### امنیت و حریم خصوصی

- تمام پردازش‌ها به صورت محلی انجام می‌شود - هیچ داده‌ای به ابر ارسال نمی‌شود
- مناسب برای کاربردهای حساس به حریم خصوصی (مانند سلامت، امور مالی)
- الزامات حاکمیت داده را برآورده می‌کند
- Foundry Local به طور کامل بر روی سخت‌افزار محلی اجرا می‌شود

## دریافت کمک

### مستندات

- **README اصلی**: [README.md](README.md) - نمای کلی مخزن و مسیرهای یادگیری
- **راهنمای مطالعه**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - منابع یادگیری و جدول زمانی
- **پشتیبانی**: [SUPPORT.md](SUPPORT.md) - نحوه دریافت کمک
- **امنیت**: [SECURITY.md](SECURITY.md) - گزارش مسائل امنیتی

### پشتیبانی جامعه

- **مشکلات GitHub**: [گزارش اشکالات یا درخواست ویژگی‌ها](https://github.com/microsoft/edgeai-for-beginners/issues)
- **بحث‌های GitHub**: [پرسش سوالات و به اشتراک‌گذاری ایده‌ها](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **مشکلات Foundry Local**: [مسائل فنی مربوط به Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### تماس

- **نگهدارندگان**: مشاهده [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **مسائل امنیتی**: پیروی از افشای مسئولانه در [SECURITY.md](SECURITY.md)
- **پشتیبانی مایکروسافت**: برای پشتیبانی سازمانی، با خدمات مشتریان مایکروسافت تماس بگیرید

### منابع اضافی

- **Microsoft Learn**: [مسیرهای یادگیری هوش مصنوعی و یادگیری ماشین](https://learn.microsoft.com/training/browse/?products=ai-services)
- **مستندات Foundry Local**: [مستندات رسمی](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **نمونه‌های جامعه**: نمونه‌های مشارکتی جامعه را در [بحث‌های GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) بررسی کنید

---

**این مخزن آموزشی بر آموزش توسعه هوش مصنوعی لبه‌ای تمرکز دارد. الگوی اصلی مشارکت شامل بهبود محتوای آموزشی و افزودن/تقویت نمونه‌های کاربردی است که مفاهیم هوش مصنوعی لبه‌ای را نشان می‌دهند.**

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.