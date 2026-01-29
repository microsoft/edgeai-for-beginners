# AGENTS.md

> **डेव्हलपर मार्गदर्शक EdgeAI for Beginners मध्ये योगदान देण्यासाठी**
> 
> हा दस्तऐवज या रिपॉझिटरीसह काम करणाऱ्या डेव्हलपर, AI एजंट्स आणि योगदानकर्त्यांसाठी व्यापक माहिती प्रदान करतो. यात सेटअप, विकास कार्यप्रवाह, चाचणी आणि सर्वोत्तम पद्धतींचा समावेश आहे.
> 
> **शेवटचे अद्यतन**: 30 ऑक्टोबर 2025 | **दस्तऐवज आवृत्ती**: 3.0

## विषय सूची

- [प्रकल्पाचा आढावा](../..)
- [रिपॉझिटरी संरचना](../..)
- [पूर्वापेक्षित अटी](../..)
- [सेटअप कमांड्स](../..)
- [विकास कार्यप्रवाह](../..)
- [चाचणी सूचना](../..)
- [कोड शैली मार्गदर्शक](../..)
- [पुल रिक्वेस्ट मार्गदर्शक](../..)
- [भाषांतर प्रणाली](../..)
- [Foundry Local एकत्रीकरण](../..)
- [बिल्ड आणि डिप्लॉयमेंट](../..)
- [सामान्य समस्या आणि निराकरण](../..)
- [अतिरिक्त संसाधने](../..)
- [प्रकल्प-विशिष्ट टीप](../..)
- [मदत मिळवणे](../..)

## प्रकल्पाचा आढावा

EdgeAI for Beginners हा एक व्यापक शैक्षणिक रिपॉझिटरी आहे जो Small Language Models (SLMs) सह Edge AI विकास शिकवतो. हा कोर्स EdgeAI मूलभूत गोष्टी, मॉडेल डिप्लॉयमेंट, ऑप्टिमायझेशन तंत्र आणि Microsoft Foundry Local आणि विविध AI फ्रेमवर्क्स वापरून उत्पादन-तयार अंमलबजावणी कव्हर करतो.

**मुख्य तंत्रज्ञान:**
- Python 3.8+ (AI/ML नमुन्यांसाठी प्राथमिक भाषा)
- .NET C# (AI/ML नमुने)
- JavaScript/Node.js सह Electron (डेस्कटॉप अनुप्रयोगांसाठी)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्क्स: LangChain, Semantic Kernel, Chainlit
- मॉडेल ऑप्टिमायझेशन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**रिपॉझिटरी प्रकार:** 8 मॉड्यूल्स आणि 10 व्यापक नमुना अनुप्रयोगांसह शैक्षणिक सामग्री रिपॉझिटरी

**आर्किटेक्चर:** व्यावहारिक नमुन्यांसह मल्टी-मॉड्यूल शिक्षण पथ जो Edge AI डिप्लॉयमेंट पॅटर्न प्रदर्शित करतो

## रिपॉझिटरी संरचना

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

## पूर्वापेक्षित अटी

### आवश्यक साधने

- **Python 3.8+** - AI/ML नमुने आणि नोटबुक्ससाठी
- **Node.js 16+** - Electron नमुना अनुप्रयोगासाठी
- **Git** - आवृत्ती नियंत्रणासाठी
- **Microsoft Foundry Local** - AI मॉडेल्स स्थानिक पातळीवर चालवण्यासाठी

### शिफारस केलेली साधने

- **Visual Studio Code** - Python, Jupyter, आणि Pylance एक्सटेंशन्ससह
- **Windows Terminal** - चांगल्या कमांड-लाइन अनुभवासाठी (Windows वापरकर्ते)
- **Docker** - कंटेनराइज्ड विकासासाठी (पर्यायी)

### प्रणाली आवश्यकता

- **RAM**: किमान 8GB, मल्टी-मॉडेल परिस्थितीसाठी 16GB+ शिफारस केलेले
- **स्टोरेज**: मॉडेल्स आणि डिपेंडन्सीसाठी 10GB+ मोकळी जागा
- **OS**: Windows 10/11, macOS 11+, किंवा Linux (Ubuntu 20.04+)
- **हार्डवेअर**: AVX2 समर्थनासह CPU; GPU (CUDA, Qualcomm NPU) पर्यायी परंतु शिफारस केलेले

### ज्ञान पूर्वापेक्षित अटी

- Python प्रोग्रामिंगची मूलभूत समज
- कमांड-लाइन इंटरफेसची ओळख
- AI/ML संकल्पनांची समज (नमुना विकासासाठी)
- Git कार्यप्रवाह आणि पुल रिक्वेस्ट प्रक्रिया

## सेटअप कमांड्स

### रिपॉझिटरी सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python नमुना सेटअप (Module08 आणि कार्यशाळा नमुने)

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

### Node.js नमुना सेटअप (नमुना 08 - Windows Chat App)

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

### Foundry Local सेटअप

नमुने चालवण्यासाठी Foundry Local आवश्यक आहे. अधिकृत रिपॉझिटरीमधून डाउनलोड आणि इंस्टॉल करा:

**इंस्टॉलेशन:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **मॅन्युअल**: [रिलीज पृष्ठ](https://github.com/microsoft/Foundry-Local/releases) वरून डाउनलोड करा

**जलद प्रारंभ:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**टीप**: Foundry Local आपल्यासाठी हार्डवेअर (CUDA GPU, Qualcomm NPU, किंवा CPU) साठी सर्वोत्तम मॉडेल प्रकार आपोआप निवडतो.

## विकास कार्यप्रवाह

### सामग्री विकास

ही रिपॉझिटरी प्रामुख्याने **Markdown शैक्षणिक सामग्री** समाविष्ट करते. बदल करताना:

1. योग्य मॉड्यूल निर्देशिकांमध्ये `.md` फाइल्स संपादित करा
2. विद्यमान स्वरूपन नमुन्यांचे अनुसरण करा
3. कोड उदाहरणे अचूक आणि चाचणी केलेली आहेत याची खात्री करा
4. आवश्यक असल्यास संबंधित भाषांतरित सामग्री अद्यतनित करा (किंवा ऑटोमेशनला ते हाताळू द्या)

### नमुना अनुप्रयोग विकास

Module08 Python नमुन्यांसाठी (नमुने 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

कार्यशाळा Python नमुन्यांसाठी:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron नमुना (नमुना 08) साठी:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमुना अनुप्रयोग चाचणी

Python नमुन्यांमध्ये स्वयंचलित चाचण्या नाहीत परंतु त्यांची वैधता चालवून तपासली जाऊ शकते:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron नमुन्यांमध्ये चाचणी पायाभूत सुविधा आहे:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## चाचणी सूचना

### सामग्री वैधता

रिपॉझिटरी स्वयंचलित भाषांतर कार्यप्रवाह वापरते. भाषांतरांसाठी कोणतीही मॅन्युअल चाचणी आवश्यक नाही.

**मॅन्युअल वैधता सामग्री बदलांसाठी:**
1. Markdown रेंडरिंग `.md` फाइल्स प्रीव्ह्यू करून पुनरावलोकन करा
2. सर्व दुवे वैध लक्ष्यांकडे निर्देशित आहेत याची खात्री करा
3. दस्तऐवजामध्ये समाविष्ट केलेले कोड स्निपेट्स चाचणी करा
4. प्रतिमा योग्यरित्या लोड होतात याची खात्री करा

### नमुना अनुप्रयोग चाचणी

**Module08/samples/08 (Electron app) मध्ये व्यापक चाचणी आहे:**
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

**Python नमुने मॅन्युअली चाचणी करावेत:**
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

## कोड शैली मार्गदर्शक

### Markdown सामग्री

- सुसंगत शीर्षक श्रेणी वापरा (# शीर्षकासाठी, ## मुख्य विभागांसाठी, ### उपविभागांसाठी)
- भाषा निर्दिष्ट करणाऱ्या कोड ब्लॉक्स समाविष्ट करा: ```python, ```bash, ```javascript
- टेबल्स, यादी आणि जोर देण्यासाठी विद्यमान स्वरूपनाचे अनुसरण करा
- ओळी वाचनीय ठेवा (~80-100 वर्णांचे लक्ष्य ठेवा, परंतु कठोर नाही)
- अंतर्गत संदर्भांसाठी सापेक्ष दुवे वापरा

### Python कोड शैली

- PEP 8 नियमांचे अनुसरण करा
- योग्य ठिकाणी प्रकार संकेत वापरा
- फंक्शन्स आणि वर्गांसाठी डॉक्स्ट्रिंग्स समाविष्ट करा
- अर्थपूर्ण व्हेरिएबल नावे वापरा
- फंक्शन्स लक्ष केंद्रित आणि संक्षिप्त ठेवा

### JavaScript/Node.js कोड शैली

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**मुख्य नियम:**
- नमुना 08 मध्ये प्रदान केलेली ESLint कॉन्फिगरेशन
- कोड स्वरूपनासाठी Prettier वापरा
- आधुनिक ES6+ सिंटॅक्स वापरा
- कोडबेसमधील विद्यमान नमुन्यांचे अनुसरण करा

## पुल रिक्वेस्ट मार्गदर्शक

### योगदान कार्यप्रवाह

1. **रिपॉझिटरी फोर्क करा** आणि `main` वरून नवीन शाखा तयार करा
2. **आपले बदल करा** कोड शैली मार्गदर्शकांचे अनुसरण करून
3. **वर नमूद केलेल्या चाचणी सूचनांचा वापर करून पूर्णपणे चाचणी करा**
4. **स्पष्ट संदेशांसह कमिट करा** पारंपरिक कमिट्स स्वरूपाचे अनुसरण करून
5. **आपल्या फोर्कवर पुश करा** आणि पुल रिक्वेस्ट तयार करा
6. **पुनरावलोकन दरम्यान मेंटेनर्सकडून फीडबॅकला प्रतिसाद द्या**

### शाखा नावाचे स्वरूप

- `feature/<module>-<description>` - नवीन वैशिष्ट्ये किंवा सामग्रीसाठी
- `fix/<module>-<description>` - बग फिक्सेससाठी
- `docs/<description>` - दस्तऐवज सुधारण्यासाठी
- `refactor/<description>` - कोड पुनर्रचना करण्यासाठी

### कमिट संदेश स्वरूप

[Conventional Commits](https://www.conventionalcommits.org/) चे अनुसरण करा:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**उदाहरणे:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### शीर्षक स्वरूप
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### आचारसंहिता

सर्व योगदानकर्त्यांनी [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) चे अनुसरण करणे आवश्यक आहे. कृपया योगदान देण्यापूर्वी [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) पुनरावलोकन करा.

### सबमिट करण्यापूर्वी

**सामग्री बदलांसाठी:**
- सर्व सुधारित Markdown फाइल्स प्रीव्ह्यू करा
- दुवे आणि प्रतिमा कार्यरत आहेत याची खात्री करा
- टायपो आणि व्याकरणाच्या चुका तपासा

**नमुना कोड बदलांसाठी (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमुना बदलांसाठी:**
- नमुना यशस्वीरित्या चालतो याची चाचणी करा
- त्रुटी हाताळणी कार्यरत आहे याची खात्री करा
- Foundry Local सह सुसंगतता तपासा

### पुनरावलोकन प्रक्रिया

- शैक्षणिक सामग्री बदल अचूकता आणि स्पष्टतेसाठी पुनरावलोकन केले जातात
- कोड नमुने कार्यक्षमतेसाठी चाचणी केले जातात
- भाषांतर अद्यतने GitHub Actions द्वारे स्वयंचलितपणे हाताळली जातात

## भाषांतर प्रणाली

**महत्त्वाचे:** ही रिपॉझिटरी GitHub Actions द्वारे स्वयंचलित भाषांतर वापरते.

- भाषांतरे `/translations/` निर्देशिकेत आहेत (50+ भाषा)
- `co-op-translator.yml` कार्यप्रवाहाद्वारे स्वयंचलित
- **भाषांतर फाइल्स मॅन्युअली संपादित करू नका** - त्या अधिलिखित केल्या जातील
- मूळ आणि मॉड्यूल निर्देशिकांमधील फक्त इंग्रजी स्रोत फाइल्स संपादित करा
- `main` शाखेत पुश केल्यावर भाषांतरे स्वयंचलितपणे तयार केली जातात

## Foundry Local एकत्रीकरण

बहुतेक Module08 नमुन्यांसाठी Microsoft Foundry Local चालू असणे आवश्यक आहे.

### इंस्टॉलेशन आणि सेटअप

**Foundry Local इंस्टॉल करा:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK इंस्टॉल करा:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local सुरू करणे
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

### SDK वापर (Python)
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

### Foundry Local सत्यापित करणे
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### नमुन्यांसाठी पर्यावरणीय व्हेरिएबल्स

बहुतेक नमुने या पर्यावरणीय व्हेरिएबल्स वापरतात:
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

**टीप**: `FoundryLocalManager` वापरताना, SDK आपोआप सेवा शोध आणि मॉडेल लोडिंग हाताळते. मॉडेल उपनाम (जसे `phi-3.5-mini`) आपल्यासाठी सर्वोत्तम प्रकार निवडण्याची खात्री करतात.

## बिल्ड आणि डिप्लॉयमेंट

### सामग्री डिप्लॉयमेंट

ही रिपॉझिटरी प्रामुख्याने दस्तऐवज आहे - सामग्रीसाठी कोणतीही बिल्ड प्रक्रिया आवश्यक नाही.

### नमुना अनुप्रयोग बिल्डिंग

**Electron अनुप्रयोग (Module08/samples/08):**
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

**Python नमुने:**
कोणतीही बिल्ड प्रक्रिया नाही - नमुने थेट Python इंटरप्रिटरसह चालवले जातात.

## सामान्य समस्या आणि निराकरण

> **टीप**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) तपासा ज्ञात समस्या आणि निराकरणांसाठी.

### गंभीर समस्या (ब्लॉकिंग)

#### Foundry Local चालू नाही
**समस्या:** नमुने कनेक्शन त्रुटींसह अयशस्वी होतात

**निराकरण:**
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

### सामान्य समस्या (मध्यम)

#### Python व्हर्च्युअल एन्व्हायर्नमेंट समस्या
**समस्या:** मॉड्यूल आयात त्रुटी

**निराकरण:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron बिल्ड समस्या
**समस्या:** npm इंस्टॉल किंवा बिल्ड अयशस्वी

**निराकरण:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### कार्यप्रवाह समस्या (लहान)

#### भाषांतर कार्यप्रवाह संघर्ष
**समस्या:** भाषांतर PR आपल्या बदलांशी संघर्ष करते

**निराकरण:**
- फक्त इंग्रजी स्रोत फाइल्स संपादित करा
- स्वयंचलित भाषांतर कार्यप्रवाह भाषांतर हाताळू द्या
- जर संघर्ष झाला, तर भाषांतर विलीन झाल्यानंतर `main` आपल्या शाखेत विलीन करा

#### मॉडेल डाउनलोड अयशस्वी
**समस्या:** Foundry Local मॉडेल्स डाउनलोड करण्यात अयशस्वी

**निराकरण:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## अतिरिक्त संसाधने

### शिक्षण पथ
- **Beginner Path:** मॉड्यूल्स 01-02 (7-9 तास)
- **Intermediate Path:** मॉड्यूल्स 03-04 (9-11 तास)
- **Advanced Path:** मॉड्यूल्स 05-07 (12-15 तास)
- **Expert Path:** मॉड्यूल 08 (8-10 तास)
- **हँड्स-ऑन कार्यशाळा:** कार्यशाळा सामग्री (6-8 तास)

### मुख्य मॉड्यूल सामग्री
- **Module01:** EdgeAI मूलभूत गोष्टी आणि वास्तविक-जगातील केस स्टडीज
- **Module02:** Small Language Model (SLM) कुटुंबे आणि आर्किटेक्चर
- **Module03:** स्थानिक आणि क्लाउड डिप्लॉयमेंट रणनीती
- **Module04:** अनेक फ्रेमवर्कसह मॉडेल ऑप्टिमायझेशन (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - उत्पादन ऑपरेशन्स
- **Module06:** AI एजंट्स आणि फंक्शन कॉलिंग
- **Module07:** प्लॅटफॉर्म-विशिष्ट अंमलबजावणी
- **Module08:** Foundry Local टूलकिटसह 10 व्यापक नमुने

### बाह्य अवलंबित्वे
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-सुसंगत API सह स्थानिक AI मॉडेल रनटाइम
  - [दस्तऐवज](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ऑप्टिमायझेशन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मॉडेल ऑप्टिमायझेशन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel चे ऑप्टिमायझेशन टूलकिट

## प्रकल्प-विशिष्ट टीप

### Module08 नमुना अनुप्रयोग

रिपॉझिटरीमध्ये 10 व्यापक नमुना अनुप्रयोग समाविष्ट आहेत:

1. **01-REST Chat Quickstart** - मूलभूत OpenAI SDK एकत्रीकरण
2. **02-OpenAI SDK Integration** - प्रगत SDK वैश
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel एकत्रीकरण

### कार्यशाळेतील नमुना अनुप्रयोग

कार्यशाळेमध्ये 6 प्रगत सत्रे समाविष्ट आहेत ज्यामध्ये व्यावहारिक अंमलबजावणी आहे:

1. **सत्र 01** - Foundry Local एकत्रीकरणासह चॅट बूटस्ट्रॅप
2. **सत्र 02** - RAG पाइपलाइन आणि RAGAS सह मूल्यांकन
3. **सत्र 03** - ओपन-सोर्स मॉडेल्सचे बेंचमार्किंग
4. **सत्र 04** - मॉडेल तुलना आणि निवड
5. **सत्र 05** - मल्टी-एजंट ऑर्केस्ट्रेशन प्रणाली
6. **सत्र 06** - मॉडेल रूटिंग आणि पाइपलाइन व्यवस्थापन

प्रत्येक नमुना Foundry Local सह एज AI विकासाचे विविध पैलू दर्शवतो.

### कार्यक्षमता विचार

- SLMs एज डिप्लॉयमेंटसाठी अनुकूलित आहेत (2-16GB RAM)
- स्थानिक अनुमान 50-500ms प्रतिसाद वेळा प्रदान करते
- क्वांटायझेशन तंत्रज्ञान 75% आकार कमी करते आणि 85% कार्यक्षमता टिकवून ठेवते
- स्थानिक मॉडेल्ससह रिअल-टाइम संवाद क्षमता

### सुरक्षा आणि गोपनीयता

- सर्व प्रक्रिया स्थानिक स्तरावर होते - कोणतेही डेटा क्लाउडवर पाठवले जात नाही
- गोपनीयतेसाठी संवेदनशील अनुप्रयोगांसाठी योग्य (आरोग्यसेवा, वित्त)
- डेटा सार्वभौमत्व आवश्यकता पूर्ण करते
- Foundry Local पूर्णपणे स्थानिक हार्डवेअरवर चालते

## मदत मिळवणे

### दस्तऐवजीकरण

- **मुख्य README**: [README.md](README.md) - रिपॉझिटरीचा आढावा आणि शिकण्याचे मार्ग
- **अभ्यास मार्गदर्शक**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - शिकण्याची संसाधने आणि वेळापत्रक
- **सपोर्ट**: [SUPPORT.md](SUPPORT.md) - मदत कशी मिळवायची
- **सुरक्षा**: [SECURITY.md](SECURITY.md) - सुरक्षा समस्या कशा रिपोर्ट करायच्या

### समुदाय समर्थन

- **GitHub Issues**: [बग्स रिपोर्ट करा किंवा फीचर्सची विनंती करा](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [प्रश्न विचारा आणि कल्पना शेअर करा](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local संबंधित तांत्रिक समस्या](https://github.com/microsoft/Foundry-Local/issues)

### संपर्क

- **देखरेख करणारे**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) येथे पहा
- **सुरक्षा समस्या**: [SECURITY.md](SECURITY.md) मध्ये जबाबदार प्रकटीकरणाचे अनुसरण करा
- **Microsoft Support**: एंटरप्राइझ समर्थनासाठी, Microsoft ग्राहक सेवेशी संपर्क साधा

### अतिरिक्त संसाधने

- **Microsoft Learn**: [AI आणि मशीन लर्निंग शिकण्याचे मार्ग](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local दस्तऐवजीकरण**: [अधिकृत दस्तऐवज](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **समुदाय नमुने**: समुदाय योगदानासाठी [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) तपासा

---

**हे एज AI विकास शिकवण्यावर केंद्रित शैक्षणिक रिपॉझिटरी आहे. प्राथमिक योगदान नमुना शैक्षणिक सामग्री सुधारण्यात आणि एज AI संकल्पना दर्शवणारे नमुना अनुप्रयोग जोडणे/सुधारणे आहे.**

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.