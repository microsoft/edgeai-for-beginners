# AGENTS.md

> **ایج ای آئی کے لیے ابتدائی افراد کے لیے ڈویلپر گائیڈ**
> 
> یہ دستاویز ان ڈویلپرز، اے آئی ایجنٹس، اور شراکت داروں کے لیے جامع معلومات فراہم کرتی ہے جو اس ریپوزیٹری کے ساتھ کام کر رہے ہیں۔ اس میں سیٹ اپ، ترقیاتی ورک فلو، ٹیسٹنگ، اور بہترین طریقے شامل ہیں۔
> 
> **آخری اپ ڈیٹ**: 30 اکتوبر 2025 | **دستاویز ورژن**: 3.0

## فہرستِ مواد

- [پروجیکٹ کا جائزہ](../..)
- [ریپوزیٹری کا ڈھانچہ](../..)
- [ضروریات](../..)
- [سیٹ اپ کمانڈز](../..)
- [ترقیاتی ورک فلو](../..)
- [ٹیسٹنگ ہدایات](../..)
- [کوڈ اسٹائل گائیڈ لائنز](../..)
- [پُل ریکویسٹ گائیڈ لائنز](../..)
- [ترجمہ نظام](../..)
- [فاؤنڈری لوکل انٹیگریشن](../..)
- [بلڈ اور ڈیپلائمنٹ](../..)
- [عام مسائل اور ان کے حل](../..)
- [اضافی وسائل](../..)
- [پروجیکٹ کے مخصوص نوٹس](../..)
- [مدد حاصل کریں](../..)

## پروجیکٹ کا جائزہ

ایج ای آئی فار بیگنرز ایک جامع تعلیمی ریپوزیٹری ہے جو چھوٹے لینگویج ماڈلز (SLMs) کے ساتھ ایج اے آئی ڈیولپمنٹ سکھاتی ہے۔ کورس میں ایج اے آئی کے بنیادی اصول، ماڈل ڈیپلائمنٹ، آپٹیمائزیشن تکنیک، اور پروڈکشن ریڈی امپلیمنٹیشن شامل ہیں، جو مائیکروسافٹ فاؤنڈری لوکل اور مختلف اے آئی فریم ورک استعمال کرتے ہیں۔

**اہم ٹیکنالوجیز:**
- Python 3.8+ (اے آئی/ایم ایل سیمپلز کے لیے بنیادی زبان)
- .NET C# (اے آئی/ایم ایل سیمپلز)
- JavaScript/Node.js with Electron (ڈیسک ٹاپ ایپلیکیشنز کے لیے)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI فریم ورک: LangChain, Semantic Kernel, Chainlit
- ماڈل آپٹیمائزیشن: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ریپوزیٹری کی قسم:** تعلیمی مواد کی ریپوزیٹری جس میں 8 ماڈیولز اور 10 جامع سیمپل ایپلیکیشنز شامل ہیں

**آرکیٹیکچر:** ملٹی ماڈیول لرننگ پاتھ جس میں ایج اے آئی ڈیپلائمنٹ پیٹرنز کو عملی طور پر دکھایا گیا ہے

## ریپوزیٹری کا ڈھانچہ

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

## ضروریات

### مطلوبہ ٹولز

- **Python 3.8+** - اے آئی/ایم ایل سیمپلز اور نوٹ بکس کے لیے
- **Node.js 16+** - الیکٹران سیمپل ایپلیکیشن کے لیے
- **Git** - ورژن کنٹرول کے لیے
- **Microsoft Foundry Local** - اے آئی ماڈلز کو لوکل چلانے کے لیے

### تجویز کردہ ٹولز

- **Visual Studio Code** - Python، Jupyter، اور Pylance ایکسٹینشنز کے ساتھ
- **Windows Terminal** - بہتر کمانڈ لائن تجربے کے لیے (ونڈوز صارفین)
- **Docker** - کنٹینرائزڈ ڈیولپمنٹ کے لیے (اختیاری)

### سسٹم کی ضروریات

- **RAM**: کم از کم 8GB، ملٹی ماڈل سیناریوز کے لیے 16GB+ تجویز کردہ
- **Storage**: ماڈلز اور ڈیپینڈنسیز کے لیے 10GB+ خالی جگہ
- **OS**: Windows 10/11، macOS 11+، یا Linux (Ubuntu 20.04+)
- **Hardware**: AVX2 سپورٹ کے ساتھ CPU؛ GPU (CUDA، Qualcomm NPU) اختیاری لیکن تجویز کردہ

### علم کی ضروریات

- Python پروگرامنگ کی بنیادی سمجھ
- کمانڈ لائن انٹرفیسز سے واقفیت
- اے آئی/ایم ایل تصورات کی سمجھ (سیمپل ڈیولپمنٹ کے لیے)
- Git ورک فلو اور پُل ریکویسٹ پروسیسز

## سیٹ اپ کمانڈز

### ریپوزیٹری سیٹ اپ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python سیمپل سیٹ اپ (Module08 اور ورکشاپ سیمپلز)

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

### Node.js سیمپل سیٹ اپ (سیمپل 08 - ونڈوز چیٹ ایپ)

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

### فاؤنڈری لوکل سیٹ اپ

فاؤنڈری لوکل سیمپلز کو چلانے کے لیے ضروری ہے۔ آفیشل ریپوزیٹری سے ڈاؤنلوڈ اور انسٹال کریں:

**انسٹالیشن:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: [ریلیز پیج](https://github.com/microsoft/Foundry-Local/releases) سے ڈاؤنلوڈ کریں

**کوئیک اسٹارٹ:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**نوٹ**: فاؤنڈری لوکل خود بخود آپ کے ہارڈویئر کے لیے بہترین ماڈل ویریئنٹ منتخب کرتا ہے (CUDA GPU، Qualcomm NPU، یا CPU)۔

## ترقیاتی ورک فلو

### مواد کی ترقی

یہ ریپوزیٹری بنیادی طور پر **مارک ڈاؤن تعلیمی مواد** پر مشتمل ہے۔ تبدیلیاں کرتے وقت:

1. مناسب ماڈیول ڈائریکٹریز میں `.md` فائلز کو ایڈٹ کریں
2. موجودہ فارمیٹنگ پیٹرنز کی پیروی کریں
3. کوڈ کے نمونے درست اور ٹیسٹ شدہ ہونے کو یقینی بنائیں
4. اگر ضروری ہو تو متعلقہ ترجمہ شدہ مواد کو اپ ڈیٹ کریں (یا آٹومیشن کو اس کا خیال رکھنے دیں)

### سیمپل ایپلیکیشن ڈیولپمنٹ

Module08 Python سیمپلز کے لیے (سیمپلز 01-07، 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

ورکشاپ Python سیمپلز کے لیے:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

الیکٹران سیمپل (سیمپل 08) کے لیے:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### سیمپل ایپلیکیشنز کی ٹیسٹنگ

Python سیمپلز کے لیے آٹومیٹڈ ٹیسٹس نہیں ہیں لیکن انہیں چلانے سے ویلیڈیٹ کیا جا سکتا ہے:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

الیکٹران سیمپل کے پاس ٹیسٹ انفراسٹرکچر موجود ہے:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## ٹیسٹنگ ہدایات

### مواد کی ویلیڈیشن

ریپوزیٹری آٹومیٹڈ ترجمہ ورک فلو استعمال کرتی ہے۔ ترجموں کے لیے کوئی دستی ٹیسٹنگ ضروری نہیں۔

**مواد کی تبدیلیوں کے لیے دستی ویلیڈیشن:**
1. مارک ڈاؤن رینڈرنگ کا جائزہ لیں `.md` فائلز کو پریویو کر کے
2. تمام لنکس کو درست ٹارگٹس کی طرف اشارہ کرنے کی تصدیق کریں
3. دستاویز میں شامل کوڈ کے نمونوں کو ٹیسٹ کریں
4. تصاویر کے صحیح طریقے سے لوڈ ہونے کو چیک کریں

### سیمپل ایپلیکیشنز کی ٹیسٹنگ

**Module08/samples/08 (الیکٹران ایپ) کے پاس جامع ٹیسٹنگ موجود ہے:**
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

**Python سیمپلز کو دستی طور پر ٹیسٹ کیا جانا چاہیے:**
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

## کوڈ اسٹائل گائیڈ لائنز

### مارک ڈاؤن مواد

- مستقل ہیڈنگ ہائیرارکی استعمال کریں (# عنوان کے لیے، ## اہم سیکشنز کے لیے، ### ذیلی سیکشنز کے لیے)
- کوڈ بلاکس میں زبان کے اسپیسفائر شامل کریں: ```python, ```bash, ```javascript
- ٹیبلز، لسٹس، اور ایمفیسس کے لیے موجودہ فارمیٹنگ کی پیروی کریں
- لائنز کو پڑھنے کے قابل رکھیں (~80-100 کریکٹرز کا ہدف رکھیں، لیکن سخت نہیں)
- اندرونی حوالوں کے لیے ریلیٹو لنکس استعمال کریں

### Python کوڈ اسٹائل

- PEP 8 کنونشنز کی پیروی کریں
- جہاں مناسب ہو ٹائپ ہنٹس استعمال کریں
- فنکشنز اور کلاسز کے لیے ڈاکسٹرنگز شامل کریں
- معنی خیز ویریبل نام استعمال کریں
- فنکشنز کو مرکوز اور مختصر رکھیں

### JavaScript/Node.js کوڈ اسٹائل

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**اہم کنونشنز:**
- سیمپل 08 میں فراہم کردہ ESLint کنفیگریشن
- کوڈ فارمیٹنگ کے لیے Prettier
- جدید ES6+ سینٹیکس استعمال کریں
- کوڈ بیس میں موجودہ پیٹرنز کی پیروی کریں

## پُل ریکویسٹ گائیڈ لائنز

### شراکت کا ورک فلو

1. **ریپوزیٹری کو فورک کریں** اور `main` سے ایک نئی برانچ بنائیں
2. **اپنی تبدیلیاں کریں** کوڈ اسٹائل گائیڈ لائنز کی پیروی کرتے ہوئے
3. **اوپر دی گئی ٹیسٹنگ ہدایات کے مطابق مکمل ٹیسٹ کریں**
4. **واضح پیغامات کے ساتھ کمیٹ کریں** کنونشنل کمیٹس فارمیٹ کی پیروی کرتے ہوئے
5. **اپنے فورک پر پش کریں** اور ایک پُل ریکویسٹ بنائیں
6. **ریویو کے دوران مینٹینرز کے فیڈبیک کا جواب دیں**

### برانچ نام رکھنے کا کنونشن

- `feature/<module>-<description>` - نئی خصوصیات یا مواد کے لیے
- `fix/<module>-<description>` - بگ فکسز کے لیے
- `docs/<description>` - دستاویزات میں بہتری کے لیے
- `refactor/<description>` - کوڈ ریفیکٹرنگ کے لیے

### کمیٹ میسج فارمیٹ

[Conventional Commits](https://www.conventionalcommits.org/) کی پیروی کریں:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**مثالیں:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### عنوان فارمیٹ
```
[ModuleXX] Brief description of change
```
یا
```
[Module08/samples/XX] Description for sample changes
```

### ضابطہ اخلاق

تمام شراکت داروں کو [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) کی پیروی کرنی چاہیے۔ شراکت سے پہلے [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) کا جائزہ لیں۔

### جمع کرانے سے پہلے

**مواد کی تبدیلیوں کے لیے:**
- تمام ترمیم شدہ مارک ڈاؤن فائلز کا پریویو کریں
- لنکس اور تصاویر کے کام کرنے کی تصدیق کریں
- ٹائپوز اور گرامر کی غلطیوں کو چیک کریں

**سیمپل کوڈ کی تبدیلیوں کے لیے (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python سیمپل تبدیلیوں کے لیے:**
- سیمپل کے کامیابی سے چلنے کی تصدیق کریں
- ایرر ہینڈلنگ کے کام کرنے کی تصدیق کریں
- فاؤنڈری لوکل کے ساتھ مطابقت چیک کریں

### ریویو پروسیس

- تعلیمی مواد کی تبدیلیوں کو درستگی اور وضاحت کے لیے ریویو کیا جاتا ہے
- کوڈ سیمپلز کو فعالیت کے لیے ٹیسٹ کیا جاتا ہے
- ترجمہ اپ ڈیٹس کو GitHub Actions کے ذریعے خودکار طور پر ہینڈل کیا جاتا ہے

## ترجمہ نظام

**اہم:** یہ ریپوزیٹری GitHub Actions کے ذریعے خودکار ترجمہ استعمال کرتی ہے۔

- ترجمے `/translations/` ڈائریکٹری میں موجود ہیں (50+ زبانیں)
- `co-op-translator.yml` ورک فلو کے ذریعے خودکار
- **ترجمہ فائلز کو دستی طور پر ایڈٹ نہ کریں** - یہ اووررائٹ ہو جائیں گی
- صرف روٹ اور ماڈیول ڈائریکٹریز میں موجود انگریزی سورس فائلز کو ایڈٹ کریں
- ترجمے `main` برانچ پر پش کرنے پر خودکار طور پر جنریٹ ہوتے ہیں

## فاؤنڈری لوکل انٹیگریشن

زیادہ تر Module08 سیمپلز کے لیے Microsoft Foundry Local کا چلنا ضروری ہے۔

### انسٹالیشن اور سیٹ اپ

**فاؤنڈری لوکل انسٹال کریں:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK انسٹال کریں:**
```bash
pip install foundry-local-sdk openai
```

### فاؤنڈری لوکل شروع کرنا
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

### SDK استعمال (Python)
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

### فاؤنڈری لوکل کی تصدیق
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### سیمپلز کے لیے انوائرمنٹ ویریبلز

زیادہ تر سیمپلز یہ انوائرمنٹ ویریبلز استعمال کرتے ہیں:
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

**نوٹ**: جب `FoundryLocalManager` استعمال کیا جاتا ہے، SDK خودکار طور پر سروس ڈسکوری اور ماڈل لوڈنگ کو ہینڈل کرتا ہے۔ ماڈل الیاسز (جیسے `phi-3.5-mini`) آپ کے ہارڈویئر کے لیے بہترین ویریئنٹ کو یقینی بناتے ہیں۔

## بلڈ اور ڈیپلائمنٹ

### مواد کی ڈیپلائمنٹ

یہ ریپوزیٹری بنیادی طور پر دستاویزات پر مشتمل ہے - مواد کے لیے کوئی بلڈ پروسیس ضروری نہیں۔

### سیمپل ایپلیکیشن بلڈنگ

**الیکٹران ایپلیکیشن (Module08/samples/08):**
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

**Python سیمپلز:**
کوئی بلڈ پروسیس نہیں - سیمپلز کو براہ راست Python انٹرپریٹر کے ساتھ چلایا جاتا ہے۔

## عام مسائل اور ان کے حل

> **ٹپ**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) پر معلوم مسائل اور حل چیک کریں۔

### اہم مسائل (رکاوٹیں)

#### فاؤنڈری لوکل نہیں چل رہا
**مسئلہ:** سیمپلز کنکشن ایرر کے ساتھ ناکام ہو رہے ہیں

**حل:**
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

### عام مسائل (درمیانی)

#### Python ورچوئل انوائرمنٹ کے مسائل
**مسئلہ:** ماڈیول امپورٹ ایررز

**حل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### الیکٹران بلڈ کے مسائل
**مسئلہ:** npm انسٹال یا بلڈ کی ناکامی

**حل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ورک فلو کے مسائل (معمولی)

#### ترجمہ ورک فلو کے تنازعات
**مسئلہ:** ترجمہ PR آپ کی تبدیلیوں کے ساتھ تنازعہ پیدا کرتا ہے

**حل:**
- صرف انگریزی سورس فائلز کو ایڈٹ کریں
- خودکار ترجمہ ورک فلو کو ترجمے ہینڈل کرنے دیں
- اگر تنازعات پیدا ہوں، تو ترجمے کے ضم ہونے کے بعد `main` کو اپنی برانچ میں ضم کریں

#### ماڈل ڈاؤنلوڈ کی ناکامی
**مسئلہ:** فاؤنڈری لوکل ماڈلز ڈاؤنلوڈ کرنے میں ناکام ہو رہا ہے

**حل:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## اضافی وسائل

### لرننگ پاتھز
- **ابتدائی پاتھ:** ماڈیولز 01-02 (7-9 گھنٹے)
- **درمیانی پاتھ:** ماڈیولز 03-04 (9-11 گھنٹے)
- **اعلیٰ پاتھ:** ماڈیولز 05-07 (12-15 گھنٹے)
- **ماہر پاتھ:** ماڈیول 08 (8-10 گھنٹے)
- **ہینڈز آن ورکشاپ:** ورکشاپ مواد (6-8 گھنٹے)

### اہم ماڈیول مواد
- **Module01:** ایج اے آئی کے بنیادی اصول اور حقیقی دنیا کے کیس اسٹڈیز
- **Module02:** چھوٹے لینگویج ماڈلز (SLM) کے خاندان اور آرکیٹیکچرز
- **Module03:** لوکل اور کلاؤڈ ڈیپلائمنٹ حکمت عملی
- **Module04:** متعدد فریم ورک کے ساتھ ماڈل آپٹیمائزیشن (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - پروڈکشن آپریشنز
- **Module06:** اے آئی ایجنٹس اور فنکشن کالنگ
- **Module07:** پلیٹ فارم کے مخصوص امپلیمنٹیشنز
- **Module08:** فاؤنڈری لوکل ٹول کٹ کے ساتھ 10 جامع سیمپلز

### بیرونی ڈیپینڈنسیز
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - لوکل اے آئی ماڈل رن ٹائم OpenAI-کمپیٹیبل API کے ساتھ
  - [دستاویزات](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - آپٹیمائزیشن فریم ورک
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ماڈل آپٹیمائز
10. **10-فاؤنڈری ٹولز فریم ورک** - LangChain/Semantic Kernel انضمام

### ورکشاپ کے نمونہ ایپلیکیشنز

ورکشاپ میں 6 ترقی پسند سیشنز شامل ہیں جن میں عملی نفاذ شامل ہیں:

1. **سیشن 01** - چیٹ بوٹ اسٹیپ اپ فاؤنڈری لوکل انضمام کے ساتھ
2. **سیشن 02** - RAG پائپ لائن اور RAGAS کے ساتھ تشخیص
3. **سیشن 03** - اوپن سورس ماڈلز کی بینچ مارکنگ
4. **سیشن 04** - ماڈل کا موازنہ اور انتخاب
5. **سیشن 05** - ملٹی ایجنٹ آرکسٹریشن سسٹمز
6. **سیشن 06** - ماڈل روٹنگ اور پائپ لائن مینجمنٹ

ہر نمونہ فاؤنڈری لوکل کے ساتھ ایج AI کی ترقی کے مختلف پہلوؤں کو ظاہر کرتا ہے۔

### کارکردگی کے پہلو

- SLMs ایج ڈپلائمنٹ کے لیے بہتر بنائے گئے ہیں (2-16GB RAM)
- لوکل انفرنس 50-500ms کے ردعمل کا وقت فراہم کرتا ہے
- کوانٹائزیشن تکنیک 75% سائز کی کمی کے ساتھ 85% کارکردگی برقرار رکھتی ہیں
- لوکل ماڈلز کے ساتھ حقیقی وقت کی گفتگو کی صلاحیتیں

### سیکیورٹی اور پرائیویسی

- تمام پروسیسنگ لوکل ہوتی ہے - کوئی ڈیٹا کلاؤڈ کو نہیں بھیجا جاتا
- پرائیویسی حساس ایپلیکیشنز کے لیے موزوں (صحت، مالیات)
- ڈیٹا خودمختاری کی ضروریات کو پورا کرتا ہے
- فاؤنڈری لوکل مکمل طور پر لوکل ہارڈویئر پر چلتا ہے

## مدد حاصل کریں

### دستاویزات

- **مین README**: [README.md](README.md) - ریپوزیٹری کا جائزہ اور سیکھنے کے راستے
- **مطالعہ گائیڈ**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - سیکھنے کے وسائل اور ٹائم لائن
- **سپورٹ**: [SUPPORT.md](SUPPORT.md) - مدد حاصل کرنے کا طریقہ
- **سیکیورٹی**: [SECURITY.md](SECURITY.md) - سیکیورٹی مسائل کی رپورٹنگ

### کمیونٹی سپورٹ

- **GitHub Issues**: [بگز رپورٹ کریں یا فیچرز کی درخواست کریں](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [سوالات پوچھیں اور خیالات شیئر کریں](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [فاؤنڈری لوکل کے تکنیکی مسائل](https://github.com/microsoft/Foundry-Local/issues)

### رابطہ

- **مینٹینرز**: دیکھیں [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **سیکیورٹی مسائل**: ذمہ دارانہ انکشاف کے لیے [SECURITY.md](SECURITY.md) پر عمل کریں
- **Microsoft Support**: انٹرپرائز سپورٹ کے لیے، مائیکروسافٹ کسٹمر سروس سے رابطہ کریں

### اضافی وسائل

- **Microsoft Learn**: [AI اور مشین لرننگ کے سیکھنے کے راستے](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Documentation**: [سرکاری دستاویزات](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **کمیونٹی نمونے**: کمیونٹی کی شراکت کے لیے [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) دیکھیں

---

**یہ ایک تعلیمی ریپوزیٹری ہے جو ایج AI کی ترقی سکھانے پر مرکوز ہے۔ بنیادی شراکت کا نمونہ تعلیمی مواد کو بہتر بنانا اور ایج AI کے تصورات کو ظاہر کرنے والے نمونہ ایپلیکیشنز کو شامل/بہتر کرنا ہے۔**

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔