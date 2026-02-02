# AGENTS.md

> **डेवलपर गाइड: EdgeAI के लिए शुरुआती योगदानकर्ता**
> 
> यह दस्तावेज़ इस रिपॉजिटरी के साथ काम करने वाले डेवलपर्स, AI एजेंट्स और योगदानकर्ताओं के लिए विस्तृत जानकारी प्रदान करता है। इसमें सेटअप, विकास वर्कफ़्लो, परीक्षण और सर्वोत्तम प्रथाओं को शामिल किया गया है।
> 
> **अंतिम अपडेट**: 30 अक्टूबर, 2025 | **दस्तावेज़ संस्करण**: 3.0

## सामग्री तालिका

- [प्रोजेक्ट का अवलोकन](../..)
- [रिपॉजिटरी संरचना](../..)
- [पूर्व आवश्यकताएँ](../..)
- [सेटअप कमांड्स](../..)
- [विकास वर्कफ़्लो](../..)
- [परीक्षण निर्देश](../..)
- [कोड शैली दिशानिर्देश](../..)
- [पुल अनुरोध दिशानिर्देश](../..)
- [अनुवाद प्रणाली](../..)
- [Foundry Local इंटीग्रेशन](../..)
- [बिल्ड और परिनियोजन](../..)
- [सामान्य समस्याएँ और समाधान](../..)
- [अतिरिक्त संसाधन](../..)
- [प्रोजेक्ट-विशिष्ट नोट्स](../..)
- [मदद प्राप्त करना](../..)

## प्रोजेक्ट का अवलोकन

EdgeAI for Beginners एक व्यापक शैक्षिक रिपॉजिटरी है जो छोटे भाषा मॉडल (SLMs) के साथ Edge AI विकास सिखाती है। यह कोर्स EdgeAI की मूल बातें, मॉडल परिनियोजन, अनुकूलन तकनीक और उत्पादन-तैयार कार्यान्वयन को Microsoft Foundry Local और विभिन्न AI फ्रेमवर्क्स का उपयोग करके कवर करता है।

**मुख्य तकनीकें:**
- Python 3.8+ (AI/ML नमूनों के लिए प्राथमिक भाषा)
- .NET C# (AI/ML नमूने)
- JavaScript/Node.js और Electron (डेस्कटॉप एप्लिकेशन के लिए)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्क्स: LangChain, Semantic Kernel, Chainlit
- मॉडल अनुकूलन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**रिपॉजिटरी प्रकार:** शैक्षिक सामग्री रिपॉजिटरी जिसमें 8 मॉड्यूल और 10 व्यापक नमूना एप्लिकेशन हैं

**आर्किटेक्चर:** मल्टी-मॉड्यूल लर्निंग पथ जिसमें Edge AI परिनियोजन पैटर्न को प्रदर्शित करने वाले व्यावहारिक नमूने शामिल हैं

## रिपॉजिटरी संरचना

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

## पूर्व आवश्यकताएँ

### आवश्यक उपकरण

- **Python 3.8+** - AI/ML नमूनों और नोटबुक्स के लिए
- **Node.js 16+** - Electron नमूना एप्लिकेशन के लिए
- **Git** - संस्करण नियंत्रण के लिए
- **Microsoft Foundry Local** - AI मॉडल्स को स्थानीय रूप से चलाने के लिए

### अनुशंसित उपकरण

- **Visual Studio Code** - Python, Jupyter, और Pylance एक्सटेंशन्स के साथ
- **Windows Terminal** - बेहतर कमांड-लाइन अनुभव के लिए (Windows उपयोगकर्ताओं के लिए)
- **Docker** - कंटेनरयुक्त विकास के लिए (वैकल्पिक)

### सिस्टम आवश्यकताएँ

- **RAM**: न्यूनतम 8GB, मल्टी-मॉडल परिदृश्यों के लिए 16GB+ अनुशंसित
- **स्टोरेज**: मॉडल्स और डिपेंडेंसीज़ के लिए 10GB+ खाली स्थान
- **OS**: Windows 10/11, macOS 11+, या Linux (Ubuntu 20.04+)
- **हार्डवेयर**: AVX2 सपोर्ट वाला CPU; GPU (CUDA, Qualcomm NPU) वैकल्पिक लेकिन अनुशंसित

### ज्ञान आवश्यकताएँ

- Python प्रोग्रामिंग की बुनियादी समझ
- कमांड-लाइन इंटरफेस से परिचितता
- AI/ML अवधारणाओं की समझ (नमूना विकास के लिए)
- Git वर्कफ़्लो और पुल अनुरोध प्रक्रियाएँ

## सेटअप कमांड्स

### रिपॉजिटरी सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python नमूना सेटअप (Module08 और Workshop नमूने)

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

### Node.js नमूना सेटअप (नमूना 08 - Windows Chat App)

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

Foundry Local नमूनों को चलाने के लिए आवश्यक है। आधिकारिक रिपॉजिटरी से डाउनलोड और इंस्टॉल करें:

**इंस्टॉलेशन:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **मैनुअल**: [रिलीज़ पेज](https://github.com/microsoft/Foundry-Local/releases) से डाउनलोड करें

**त्वरित प्रारंभ:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**नोट**: Foundry Local स्वचालित रूप से आपके हार्डवेयर के लिए सबसे अच्छा मॉडल वेरिएंट चुनता है (CUDA GPU, Qualcomm NPU, या CPU)।

## विकास वर्कफ़्लो

### सामग्री विकास

यह रिपॉजिटरी मुख्य रूप से **Markdown शैक्षिक सामग्री** को शामिल करती है। परिवर्तन करते समय:

1. संबंधित मॉड्यूल डायरेक्टरी में `.md` फाइलें संपादित करें
2. मौजूदा स्वरूपण पैटर्न का पालन करें
3. सुनिश्चित करें कि कोड उदाहरण सटीक और परीक्षण किए गए हैं
4. यदि आवश्यक हो तो संबंधित अनुवादित सामग्री को अपडेट करें (या स्वचालन को इसे संभालने दें)

### नमूना एप्लिकेशन विकास

Module08 Python नमूनों (नमूने 01-07, 09-10) के लिए:
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python नमूनों के लिए:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron नमूना (नमूना 08) के लिए:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमूना एप्लिकेशन परीक्षण

Python नमूनों में स्वचालित परीक्षण नहीं हैं लेकिन इन्हें चलाकर सत्यापित किया जा सकता है:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron नमूने में परीक्षण अवसंरचना है:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## परीक्षण निर्देश

### सामग्री सत्यापन

रिपॉजिटरी स्वचालित अनुवाद वर्कफ़्लो का उपयोग करती है। अनुवादों के लिए कोई मैनुअल परीक्षण आवश्यक नहीं है।

**सामग्री परिवर्तनों के लिए मैनुअल सत्यापन:**
1. Markdown रेंडरिंग की समीक्षा करें `.md` फाइलों का पूर्वावलोकन करके
2. सुनिश्चित करें कि सभी लिंक वैध लक्ष्यों की ओर इशारा करते हैं
3. दस्तावेज़ में शामिल कोड स्निपेट्स का परीक्षण करें
4. जांचें कि छवियाँ सही ढंग से लोड हो रही हैं

### नमूना एप्लिकेशन परीक्षण

**Module08/samples/08 (Electron ऐप) में व्यापक परीक्षण हैं:**
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

**Python नमूनों को मैनुअल रूप से परीक्षण किया जाना चाहिए:**
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

## कोड शैली दिशानिर्देश

### Markdown सामग्री

- सुसंगत शीर्षक पदानुक्रम का उपयोग करें (# शीर्षक के लिए, ## मुख्य अनुभागों के लिए, ### उप-अनुभागों के लिए)
- कोड ब्लॉक्स में भाषा निर्दिष्ट करें: ```python, ```bash, ```javascript
- तालिकाओं, सूचियों और जोर देने के लिए मौजूदा स्वरूपण का पालन करें
- पंक्तियों को पठनीय रखें (~80-100 वर्णों का लक्ष्य रखें, लेकिन सख्त नहीं)
- आंतरिक संदर्भों के लिए सापेक्ष लिंक का उपयोग करें

### Python कोड शैली

- PEP 8 सम्मेलनों का पालन करें
- जहाँ उपयुक्त हो, टाइप हिंट्स का उपयोग करें
- फ़ंक्शन्स और क्लासेस के लिए डॉकस्ट्रिंग्स शामिल करें
- सार्थक वेरिएबल नामों का उपयोग करें
- फ़ंक्शन्स को केंद्रित और संक्षिप्त रखें

### JavaScript/Node.js कोड शैली

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**मुख्य सम्मेलन:**
- नमूना 08 में प्रदान की गई ESLint कॉन्फ़िगरेशन
- कोड स्वरूपण के लिए Prettier का उपयोग करें
- आधुनिक ES6+ सिंटैक्स का उपयोग करें
- कोडबेस में मौजूदा पैटर्न का पालन करें

## पुल अनुरोध दिशानिर्देश

### योगदान वर्कफ़्लो

1. **रिपॉजिटरी को फोर्क करें** और `main` से एक नई शाखा बनाएं
2. **अपने परिवर्तन करें** कोड शैली दिशानिर्देशों का पालन करते हुए
3. **परीक्षण करें** ऊपर दिए गए परीक्षण निर्देशों का उपयोग करके
4. **स्पष्ट संदेशों के साथ कमिट करें** पारंपरिक कमिट्स प्रारूप का पालन करते हुए
5. **अपने फोर्क पर पुश करें** और एक पुल अनुरोध बनाएं
6. **समीक्षा के दौरान मेंटेनर्स की प्रतिक्रिया का उत्तर दें**

### शाखा नामकरण सम्मेलन

- `feature/<module>-<description>` - नई सुविधाओं या सामग्री के लिए
- `fix/<module>-<description>` - बग फिक्स के लिए
- `docs/<description>` - दस्तावेज़ सुधार के लिए
- `refactor/<description>` - कोड पुनर्गठन के लिए

### कमिट संदेश प्रारूप

[Conventional Commits](https://www.conventionalcommits.org/) का पालन करें:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**उदाहरण:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### शीर्षक प्रारूप
```
[ModuleXX] Brief description of change
```
या
```
[Module08/samples/XX] Description for sample changes
```

### आचार संहिता

सभी योगदानकर्ताओं को [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) का पालन करना चाहिए। कृपया योगदान करने से पहले [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) की समीक्षा करें।

### सबमिट करने से पहले

**सामग्री परिवर्तनों के लिए:**
- सभी संशोधित Markdown फाइलों का पूर्वावलोकन करें
- सुनिश्चित करें कि लिंक और छवियाँ काम कर रही हैं
- टाइपो और व्याकरण संबंधी त्रुटियों की जाँच करें

**नमूना कोड परिवर्तनों के लिए (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमूना परिवर्तनों के लिए:**
- सुनिश्चित करें कि नमूना सफलतापूर्वक चलता है
- त्रुटि हैंडलिंग की जाँच करें
- Foundry Local के साथ संगतता की जाँच करें

### समीक्षा प्रक्रिया

- शैक्षिक सामग्री परिवर्तनों की सटीकता और स्पष्टता के लिए समीक्षा की जाती है
- कोड नमूनों की कार्यक्षमता के लिए परीक्षण किया जाता है
- अनुवाद अपडेट स्वचालित रूप से GitHub Actions द्वारा संभाले जाते हैं

## अनुवाद प्रणाली

**महत्वपूर्ण:** यह रिपॉजिटरी GitHub Actions के माध्यम से स्वचालित अनुवाद का उपयोग करती है।

- अनुवाद `/translations/` डायरेक्टरी में हैं (50+ भाषाएँ)
- `co-op-translator.yml` वर्कफ़्लो के माध्यम से स्वचालित
- **अनुवाद फाइलों को मैनुअल रूप से संपादित न करें** - वे अधिलेखित हो जाएँगी
- केवल रूट और मॉड्यूल डायरेक्टरी में अंग्रेजी स्रोत फाइलों को संपादित करें
- `main` शाखा पर पुश करने पर अनुवाद स्वचालित रूप से उत्पन्न होते हैं

## Foundry Local इंटीग्रेशन

अधिकांश Module08 नमूनों को Microsoft Foundry Local चलाने की आवश्यकता होती है।

### इंस्टॉलेशन और सेटअप

**Foundry Local इंस्टॉल करें:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK इंस्टॉल करें:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local प्रारंभ करना
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

### SDK उपयोग (Python)
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

### Foundry Local सत्यापन
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### नमूनों के लिए पर्यावरण चर

अधिकांश नमूने इन पर्यावरण चर का उपयोग करते हैं:
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

**नोट**: जब `FoundryLocalManager` का उपयोग किया जाता है, तो SDK स्वचालित रूप से सेवा खोज और मॉडल लोडिंग को संभालता है। मॉडल उपनाम (जैसे `phi-3.5-mini`) सुनिश्चित करते हैं कि आपके हार्डवेयर के लिए सबसे अच्छा वेरिएंट चुना गया है।

## बिल्ड और परिनियोजन

### सामग्री परिनियोजन

यह रिपॉजिटरी मुख्य रूप से दस्तावेज़ीकरण है - सामग्री के लिए कोई बिल्ड प्रक्रिया आवश्यक नहीं है।

### नमूना एप्लिकेशन बिल्डिंग

**Electron एप्लिकेशन (Module08/samples/08):**
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

**Python नमूने:**
कोई बिल्ड प्रक्रिया नहीं - नमूने सीधे Python इंटरप्रेटर के साथ चलाए जाते हैं।

## सामान्य समस्याएँ और समाधान

> **टिप**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) पर ज्ञात समस्याओं और समाधानों की जाँच करें।

### गंभीर समस्याएँ (ब्लॉकिंग)

#### Foundry Local नहीं चल रहा
**समस्या:** नमूने कनेक्शन त्रुटियों के साथ विफल हो जाते हैं

**समाधान:**
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

### सामान्य समस्याएँ (मध्यम)

#### Python वर्चुअल एनवायरनमेंट समस्याएँ
**समस्या:** मॉड्यूल आयात त्रुटियाँ

**समाधान:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron बिल्ड समस्याएँ
**समस्या:** npm इंस्टॉल या बिल्ड विफलताएँ

**समाधान:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### वर्कफ़्लो समस्याएँ (मामूली)

#### अनुवाद वर्कफ़्लो संघर्ष
**समस्या:** अनुवाद PR आपके परिवर्तनों के साथ संघर्ष करता है

**समाधान:**
- केवल अंग्रेजी स्रोत फाइलों को संपादित करें
- स्वचालित अनुवाद वर्कफ़्लो को अनुवाद संभालने दें
- यदि संघर्ष होता है, तो अनुवादों के विलय के बाद `main` को अपनी शाखा में मर्ज करें

#### मॉडल डाउनलोड विफलताएँ
**समस्या:** Foundry Local मॉडल डाउनलोड करने में विफल रहता है

**समाधान:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## अतिरिक्त संसाधन

### लर्निंग पथ
- **शुरुआती पथ:** मॉड्यूल 01-02 (7-9 घंटे)
- **मध्यम पथ:** मॉड्यूल 03-04 (9-11 घंटे)
- **उन्नत पथ:** मॉड्यूल 05-07 (12-15 घंटे)
- **विशेषज्ञ पथ:** मॉड्यूल 08 (8-10 घंटे)
- **हैंड्स-ऑन वर्कशॉप:** वर्कशॉप सामग्री (6-8 घंटे)

### प्रमुख मॉड्यूल सामग्री
- **Module01:** EdgeAI की मूल बातें और वास्तविक दुनिया के केस स्टडीज़
- **Module02:** छोटे भाषा मॉडल (SLM) परिवार और आर्किटेक्चर
- **Module03:** स्थानीय और क्लाउड परिनियोजन रणनीतियाँ
- **Module04:** कई फ्रेमवर्क्स के साथ मॉडल अनुकूलन (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - उत्पादन संचालन
- **Module06:** AI एजेंट्स और फ़ंक्शन कॉलिंग
- **Module07:** प्लेटफ़ॉर्म-विशिष्ट कार्यान्वयन
- **Module08:** Foundry Local टूलकिट के साथ 10 व्यापक नमूने

### बाहरी निर्भरताएँ
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-संगत API के साथ स्थानीय AI मॉडल रनटाइम
  - [दस्तावेज़](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - अनुकूलन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मॉडल अनुकूलन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel का अनुकूलन टूलकिट

## प्रोजेक्ट-विशिष्ट नोट्स

### Module08 नमूना एप्लिकेशन

रिपॉजिटरी में 10 व्यापक नमूना एप्लिकेशन शामिल हैं:

1. **01-REST Chat Quickstart** - बुनियादी OpenAI SDK इंटीग्रेशन
2. **02-OpenAI SDK Integration** - उन्नत SDK सुविधाएँ
3. **03-Model Discovery & Benchmarking** - मॉडल तुलना उपकरण
4. **04-Chainlit RAG Application** - पुनःप्राप्ति-संवर्धित पीढ़ी
5. **05-Multi-Agent Orchestration** - बुनियादी एजेंट समन्वय
6. **06-Models-as-Tools Router** - बुद्धिमान मॉडल रूटिंग
7. **07-Direct API Client** - निम्न-स्तरीय API इंटीग्रेशन
8. **08-Windows 11 Chat App** - मूल Electron डेस्कटॉप एप्लिकेशन
9. **09-Advanced Multi-Agent System** - जटिल
10. **10-फाउंड्री टूल्स फ्रेमवर्क** - LangChain/Semantic Kernel इंटीग्रेशन

### वर्कशॉप नमूना एप्लिकेशन

वर्कशॉप में 6 प्रगतिशील सत्र शामिल हैं, जिनमें व्यावहारिक कार्यान्वयन हैं:

1. **सत्र 01** - फाउंड्री लोकल इंटीग्रेशन के साथ चैट बूटस्ट्रैप
2. **सत्र 02** - RAG पाइपलाइन और RAGAS के साथ मूल्यांकन
3. **सत्र 03** - ओपन-सोर्स मॉडल्स का बेंचमार्किंग
4. **सत्र 04** - मॉडल तुलना और चयन
5. **सत्र 05** - मल्टी-एजेंट ऑर्केस्ट्रेशन सिस्टम्स
6. **सत्र 06** - मॉडल रूटिंग और पाइपलाइन प्रबंधन

प्रत्येक नमूना फाउंड्री लोकल के साथ एज AI विकास के विभिन्न पहलुओं को प्रदर्शित करता है।

### प्रदर्शन विचार

- SLMs को एज डिप्लॉयमेंट के लिए अनुकूलित किया गया है (2-16GB RAM)
- लोकल इंफरेंस 50-500ms प्रतिक्रिया समय प्रदान करता है
- क्वांटाइजेशन तकनीकें 75% आकार में कमी और 85% प्रदर्शन बनाए रखती हैं
- लोकल मॉडल्स के साथ रियल-टाइम बातचीत की क्षमता

### सुरक्षा और गोपनीयता

- सभी प्रोसेसिंग लोकल स्तर पर होती है - कोई डेटा क्लाउड पर नहीं भेजा जाता
- गोपनीयता-संवेदनशील एप्लिकेशन (स्वास्थ्य सेवा, वित्त) के लिए उपयुक्त
- डेटा संप्रभुता आवश्यकताओं को पूरा करता है
- फाउंड्री लोकल पूरी तरह से लोकल हार्डवेयर पर चलता है

## सहायता प्राप्त करना

### दस्तावेज़

- **मुख्य README**: [README.md](README.md) - रिपॉजिटरी का अवलोकन और सीखने के मार्ग
- **अध्ययन गाइड**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - सीखने के संसाधन और समयरेखा
- **सहायता**: [SUPPORT.md](SUPPORT.md) - सहायता कैसे प्राप्त करें
- **सुरक्षा**: [SECURITY.md](SECURITY.md) - सुरक्षा मुद्दों की रिपोर्टिंग

### सामुदायिक सहायता

- **GitHub Issues**: [बग रिपोर्ट करें या फीचर्स का अनुरोध करें](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [प्रश्न पूछें और विचार साझा करें](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **फाउंड्री लोकल Issues**: [फाउंड्री लोकल के साथ तकनीकी समस्याएं](https://github.com/microsoft/Foundry-Local/issues)

### संपर्क करें

- **रखरखावकर्ता**: देखें [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **सुरक्षा मुद्दे**: [SECURITY.md](SECURITY.md) में जिम्मेदार प्रकटीकरण का पालन करें
- **Microsoft Support**: एंटरप्राइज समर्थन के लिए, Microsoft ग्राहक सेवा से संपर्क करें

### अतिरिक्त संसाधन

- **Microsoft Learn**: [AI और मशीन लर्निंग सीखने के मार्ग](https://learn.microsoft.com/training/browse/?products=ai-services)
- **फाउंड्री लोकल दस्तावेज़**: [आधिकारिक दस्तावेज़](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **सामुदायिक नमूने**: सामुदायिक योगदान के लिए [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) देखें

---

**यह एक शैक्षिक रिपॉजिटरी है जो एज AI विकास सिखाने पर केंद्रित है। प्राथमिक योगदान पैटर्न शैक्षिक सामग्री को बेहतर बनाना और एज AI अवधारणाओं को प्रदर्शित करने वाले नमूना एप्लिकेशन जोड़ना/सुधारना है।**

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।