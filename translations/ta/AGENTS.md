# AGENTS.md

> **EdgeAI ஆரம்பக்கட்ட பயிற்சிகளுக்கான டெவலப்பர் வழிகாட்டி**
> 
> இந்த ஆவணம் இந்த களஞ்சியத்துடன் பணிபுரியும் டெவலப்பர்கள், AI முகவர்கள் மற்றும் பங்களிப்பாளர்களுக்கு விரிவான தகவல்களை வழங்குகிறது. இது அமைப்பு, மேம்பாட்டு பணிகள், சோதனை மற்றும் சிறந்த நடைமுறைகளை உள்ளடக்கியது.
> 
> **கடைசியாக புதுப்பிக்கப்பட்ட தேதி**: அக்டோபர் 30, 2025 | **ஆவண பதிப்பு**: 3.0

## உள்ளடக்க அட்டவணை

- [திட்டத்தின் மேற்பார்வை](../..)
- [களஞ்சிய அமைப்பு](../..)
- [முன்னோட்டங்கள்](../..)
- [அமைப்பு கட்டளைகள்](../..)
- [மேம்பாட்டு பணிகள்](../..)
- [சோதனை வழிகாட்டிகள்](../..)
- [குறியீட்டு பாணி வழிகாட்டிகள்](../..)
- [புல் கோரிக்கை வழிகாட்டிகள்](../..)
- [மொழிபெயர்ப்பு அமைப்பு](../..)
- [Foundry Local ஒருங்கிணைப்பு](../..)
- [கட்டமைப்பு மற்றும் வெளியீடு](../..)
- [பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்](../..)
- [கூடுதல் வளங்கள்](../..)
- [திட்டத்திற்கு குறிப்பிட்ட குறிப்புகள்](../..)
- [உதவி பெறுதல்](../..)

## திட்டத்தின் மேற்பார்வை

EdgeAI ஆரம்பக்கட்ட பயிற்சிகள் என்பது சிறிய மொழி மாதிரிகளை (SLMs) கொண்டு Edge AI மேம்பாட்டத்தை கற்பதற்கான விரிவான கல்வி களஞ்சியம் ஆகும். இந்த பாடநெறி EdgeAI அடிப்படைகள், மாதிரி வெளியீடு, மேம்பாட்டு உத்திகள் மற்றும் Microsoft Foundry Local மற்றும் பல AI கட்டமைப்புகளைப் பயன்படுத்தி தயாரிப்பு தயாராகும் செயல்பாடுகளை உள்ளடக்கியது.

**முக்கிய தொழில்நுட்பங்கள்:**
- Python 3.8+ (AI/ML மாதிரிகளுக்கான முதன்மை மொழி)
- .NET C# (AI/ML மாதிரிகள்)
- JavaScript/Node.js மற்றும் Electron (டெஸ்க்டாப் பயன்பாடுகளுக்காக)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI கட்டமைப்புகள்: LangChain, Semantic Kernel, Chainlit
- மாதிரி மேம்பாடு: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**களஞ்சிய வகை:** 8 தொகுதிகள் மற்றும் 10 விரிவான மாதிரி பயன்பாடுகளுடன் கல்வி உள்ளடக்க களஞ்சியம்

**கட்டமைப்பு:** Edge AI வெளியீட்டு முறைமைகளை விளக்கும் நடைமுறை மாதிரிகளுடன் பல தொகுதி கற்றல் பாதை

## களஞ்சிய அமைப்பு

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

## முன்னோட்டங்கள்

### தேவையான கருவிகள்

- **Python 3.8+** - AI/ML மாதிரிகள் மற்றும் நோட்புக்குகளுக்காக
- **Node.js 16+** - Electron மாதிரி பயன்பாட்டுக்காக
- **Git** - பதிப்பு கட்டுப்பாட்டுக்காக
- **Microsoft Foundry Local** - AI மாதிரிகளை உள்ளூரில் இயக்க

### பரிந்துரைக்கப்படும் கருவிகள்

- **Visual Studio Code** - Python, Jupyter மற்றும் Pylance நீட்டிப்புகளுடன்
- **Windows Terminal** - Windows பயனர்களுக்கான சிறந்த கட்டளைகள் அனுபவம்
- **Docker** - கெண்டைனர்ஸ் மேம்பாட்டுக்காக (விருப்பம்)

### கணினி தேவைகள்

- **RAM**: குறைந்தபட்சம் 8GB, பல மாதிரி சூழல்களுக்கு 16GB+ பரிந்துரைக்கப்படுகிறது
- **சேமிப்பு**: மாதிரிகள் மற்றும் சார்ந்தவை 10GB+ இலவச இடம்
- **OS**: Windows 10/11, macOS 11+, அல்லது Linux (Ubuntu 20.04+)
- **ஹார்ட்வேர்கள்**: AVX2 ஆதரவு கொண்ட CPU; GPU (CUDA, Qualcomm NPU) விருப்பமானது ஆனால் பரிந்துரைக்கப்படுகிறது

### அறிவு முன்னோட்டங்கள்

- Python நிரலாக்கத்தின் அடிப்படை புரிதல்
- கட்டளை வரி இடைமுகங்களின் பரிச்சயம்
- AI/ML கருத்துக்களின் புரிதல் (மாதிரி மேம்பாட்டுக்காக)
- Git பணிகள் மற்றும் புல் கோரிக்கை செயல்முறைகள்

## அமைப்பு கட்டளைகள்

### களஞ்சிய அமைப்பு

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python மாதிரி அமைப்பு (Module08 மற்றும் Workshop மாதிரிகள்)

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

### Node.js மாதிரி அமைப்பு (மாதிரி 08 - Windows Chat App)

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

### Foundry Local அமைப்பு

Foundry Local மாதிரிகளை இயக்க தேவையானது. அதிகாரப்பூர்வ களஞ்சியத்திலிருந்து பதிவிறக்கி நிறுவவும்:

**நிறுவல்:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **கையேடு**: [releases page](https://github.com/microsoft/Foundry-Local/releases) இல் இருந்து பதிவிறக்கவும்

**விரைவான தொடக்கம்:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**குறிப்பு**: Foundry Local உங்கள் ஹார்ட்வேருக்கான சிறந்த மாதிரி மாறுபாட்டை தானாக தேர்ந்தெடுக்கிறது (CUDA GPU, Qualcomm NPU, அல்லது CPU).

## மேம்பாட்டு பணிகள்

### உள்ளடக்க மேம்பாடு

இந்த களஞ்சியம் முதன்மையாக **Markdown கல்வி உள்ளடக்கத்தை** கொண்டுள்ளது. மாற்றங்களைச் செய்யும்போது:

1. உரிய தொகுதி கோப்பகங்களில் `.md` கோப்புகளைத் திருத்தவும்
2. ஏற்கனவே உள்ள வடிவமைப்பு முறைகளை பின்பற்றவும்
3. குறியீட்டு உதாரணங்கள் சரியாகவும் சோதிக்கப்பட்டதாகவும் இருக்க வேண்டும்
4. தேவையானால் தொடர்புடைய மொழிபெயர்ப்பு உள்ளடக்கத்தைப் புதுப்பிக்கவும் (அல்லது தானியக்கத்தை அனுமதிக்கவும்)

### மாதிரி பயன்பாட்டு மேம்பாடு

Module08 Python மாதிரிகளுக்காக (மாதிரிகள் 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python மாதிரிகளுக்காக:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron மாதிரிக்காக (மாதிரி 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### மாதிரி பயன்பாடுகளை சோதனை செய்தல்

Python மாதிரிகளுக்கு தானியக்க சோதனைகள் இல்லை, ஆனால் அவற்றை இயக்குவதன் மூலம் சரிபார்க்கலாம்:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron மாதிரிக்கு சோதனை அமைப்பு உள்ளது:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## சோதனை வழிகாட்டிகள்

### உள்ளடக்க சரிபார்ப்பு

களஞ்சியம் தானியக்க மொழிபெயர்ப்பு பணிகளைப் பயன்படுத்துகிறது. மொழிபெயர்ப்புகளுக்கு கையேடு சோதனை தேவையில்லை.

**உள்ளடக்க மாற்றங்களுக்கு கையேடு சரிபார்ப்பு:**
1. `.md` கோப்புகளை முன்னோட்டமாகக் காணவும்
2. அனைத்து இணைப்புகள் செல்லுபடியாகும் இலக்குகளைச் சோதிக்கவும்
3. ஆவணத்தில் உள்ள குறியீட்டு துணுக்குகளை சோதிக்கவும்
4. படங்கள் சரியாக ஏற்றப்படுகின்றன என்பதை உறுதிப்படுத்தவும்

### மாதிரி பயன்பாட்டு சோதனை

**Module08/samples/08 (Electron பயன்பாடு) விரிவான சோதனைகள் கொண்டது:**
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

**Python மாதிரிகள் கையேடு சோதனை செய்யப்பட வேண்டும்:**
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

## குறியீட்டு பாணி வழிகாட்டிகள்

### Markdown உள்ளடக்கம்

- ஒரே மாதிரியான தலைப்பு வரிசையைப் பயன்படுத்தவும் (# தலைப்பு, ## முக்கிய பிரிவுகள், ### துணைப் பிரிவுகள்)
- மொழி குறிப்புகளுடன் குறியீட்டு தொகுதிகளைச் சேர்க்கவும்: ```python, ```bash, ```javascript
- அட்டவணைகள், பட்டியல்கள் மற்றும் வலியுறுத்தலுக்கான ஏற்கனவே உள்ள வடிவமைப்பைப் பின்பற்றவும்
- வரிகளை வாசிக்கக்கூடியதாக வைத்திருங்கள் (~80-100 எழுத்துகள், ஆனால் கடுமையானது அல்ல)
- உள்நாட்டு குறிப்புகளுக்கான தொடர்புகளுக்கு சார்பு இணைப்புகளைப் பயன்படுத்தவும்

### Python குறியீட்டு பாணி

- PEP 8 ஒழுங்குகளைப் பின்பற்றவும்
- தேவையான இடங்களில் வகை குறிப்புகளைப் பயன்படுத்தவும்
- செயல்பாடுகள் மற்றும் வகுப்புகளுக்கு டாக்ஸ்டிரிங்களைச் சேர்க்கவும்
- அர்த்தமுள்ள மாறி பெயர்களைப் பயன்படுத்தவும்
- செயல்பாடுகளை மையமாகவும் சுருக்கமாகவும் வைத்திருங்கள்

### JavaScript/Node.js குறியீட்டு பாணி

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**முக்கிய ஒழுங்குகள்:**
- மாதிரி 08 இல் வழங்கப்பட்ட ESLint கட்டமைப்பு
- குறியீட்டு வடிவமைப்புக்கான Prettier
- ES6+ நவீன வடிவமைப்பைப் பயன்படுத்தவும்
- குறியீட்டு அடிப்படையில் ஏற்கனவே உள்ள முறைகளைப் பின்பற்றவும்

## புல் கோரிக்கை வழிகாட்டிகள்

### பங்களிப்பு செயல்முறை

1. **களஞ்சியத்தை Fork செய்யவும்** மற்றும் `main` இலிருந்து புதிய கிளையை உருவாக்கவும்
2. **உங்கள் மாற்றங்களைச் செய்யவும்** குறியீட்டு பாணி வழிகாட்டிகளைப் பின்பற்றவும்
3. **முழுமையாக சோதிக்கவும்** மேலே உள்ள சோதனை வழிகாட்டிகளைப் பயன்படுத்தி
4. **தெளிவான செய்திகளுடன் Commit செய்யவும்** வழக்கமான Commit வடிவத்தைப் பின்பற்றவும்
5. **உங்கள் Fork க்கு Push செய்யவும்** மற்றும் புல் கோரிக்கையை உருவாக்கவும்
6. **பராமரிப்பாளர்களின் கருத்துக்கு பதிலளிக்கவும்** மதிப்பீட்டின் போது

### கிளை பெயரிடும் ஒழுங்கு

- `feature/<module>-<description>` - புதிய அம்சங்கள் அல்லது உள்ளடக்கம்
- `fix/<module>-<description>` - பிழை திருத்தங்கள்
- `docs/<description>` - ஆவண மேம்பாடுகள்
- `refactor/<description>` - குறியீட்டு மறுசீரமைப்பு

### Commit செய்தி வடிவம்

[Conventional Commits](https://www.conventionalcommits.org/) ஐ பின்பற்றவும்:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**உதாரணங்கள்:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### தலைப்பு வடிவம்
```
[ModuleXX] Brief description of change
```
 அல்லது
```
[Module08/samples/XX] Description for sample changes
```

### நடத்தை விதிமுறைகள்

அனைத்து பங்களிப்பாளர்களும் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ பின்பற்ற வேண்டும். பங்களிப்பதற்கு முன் [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ஐ மதிப்பாய்வு செய்யவும்.

### சமர்ப்பிப்பதற்கு முன்

**உள்ளடக்க மாற்றங்களுக்கு:**
- மாற்றியமைக்கப்பட்ட அனைத்து Markdown கோப்புகளையும் முன்னோட்டமாகக் காணவும்
- இணைப்புகள் மற்றும் படங்கள் வேலை செய்கின்றன என்பதை உறுதிப்படுத்தவும்
- தப்புகள் மற்றும் இலக்கணப் பிழைகளைச் சரிபார்க்கவும்

**மாதிரி குறியீட்டு மாற்றங்களுக்கு (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python மாதிரி மாற்றங்களுக்கு:**
- மாதிரி வெற்றிகரமாக இயங்குகிறது என்பதை சோதிக்கவும்
- பிழை கையாளுதல் வேலை செய்கிறது என்பதை உறுதிப்படுத்தவும்
- Foundry Local உடன் இணக்கத்தன்மை சரிபார்க்கவும்

### மதிப்பீட்டு செயல்முறை

- கல்வி உள்ளடக்க மாற்றங்கள் துல்லியத்திற்கும் தெளிவிற்கும் மதிப்பீடு செய்யப்படும்
- குறியீட்டு மாதிரிகள் செயல்பாட்டிற்காக சோதிக்கப்படும்
- மொழிபெயர்ப்பு புதுப்பிப்புகள் GitHub Actions மூலம் தானாக கையாளப்படும்

## மொழிபெயர்ப்பு அமைப்பு

**முக்கியம்:** இந்த களஞ்சியம் GitHub Actions மூலம் தானியக்க மொழிபெயர்ப்பைப் பயன்படுத்துகிறது.

- மொழிபெயர்ப்புகள் `/translations/` கோப்பகத்தில் உள்ளன (50+ மொழிகள்)
- `co-op-translator.yml` பணியால் தானியக்கமாக செயல்படுத்தப்படுகிறது
- **மொழிபெயர்ப்பு கோப்புகளை கையேடு திருத்த வேண்டாம்** - அவை மீண்டும் எழுதப்படும்
- மூல ஆங்கில கோப்புகளை மட்டுமே திருத்தவும்
- `main` கிளைக்கு Push செய்தவுடன் மொழிபெயர்ப்புகள் தானாக உருவாக்கப்படும்

## Foundry Local ஒருங்கிணைப்பு

Module08 மாதிரிகள் பெரும்பாலும் Microsoft Foundry Local இயங்க வேண்டும்.

### நிறுவல் & அமைப்பு

**Foundry Local ஐ நிறுவவும்:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ஐ நிறுவவும்:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ஐ தொடங்குதல்
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

### SDK பயன்பாடு (Python)
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

### Foundry Local ஐ சரிபார்த்தல்
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### மாதிரிகளுக்கான சூழல் மாறிகள்

பெரும்பாலான மாதிரிகள் இந்த சூழல் மாறிகளைப் பயன்படுத்துகின்றன:
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

**குறிப்பு**: `FoundryLocalManager` ஐப் பயன்படுத்தும்போது, SDK தானாக சேவை கண்டறிதல் மற்றும் மாதிரி ஏற்றுதலை கையாளுகிறது. மாதிரி பெயரிடல்கள் (உதாரணமாக `phi-3.5-mini`) உங்கள் ஹார்ட்வேருக்கான சிறந்த மாறுபாட்டை உறுதிப்படுத்துகின்றன.

## கட்டமைப்பு மற்றும் வெளியீடு

### உள்ளடக்க வெளியீடு

இந்த களஞ்சியம் முதன்மையாக ஆவணமாகும் - உள்ளடக்கத்திற்கான கட்டமைப்பு செயல்முறை தேவையில்லை.

### மாதிரி பயன்பாட்டு கட்டமைப்பு

**Electron பயன்பாடு (Module08/samples/08):**
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

**Python மாதிரிகள்:**
கட்டமைப்பு செயல்முறை இல்லை - மாதிரிகள் Python interpreter உடன் நேரடியாக இயக்கப்படுகின்றன.

## பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்

> **Tip**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) ஐ சரிபார்க்கவும், அறியப்பட்ட பிரச்சினைகள் மற்றும் தீர்வுகளுக்காக.

### முக்கிய பிரச்சினைகள் (தடைசெய்யும்)

#### Foundry Local இயங்கவில்லை
**பிரச்சினை:** மாதிரிகள் இணைப்பு பிழைகளுடன் தோல்வி அடைகின்றன

**தீர்வு:**
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

### பொதுவான பிரச்சினைகள் (மிதமான)

#### Python மெய்நிகர் சூழல் பிரச்சினைகள்
**பிரச்சினை:** Module import பிழைகள்

**தீர்வு:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron கட்டமைப்பு பிரச்சினைகள்
**பிரச்சினை:** npm install அல்லது build தோல்விகள்

**தீர்வு:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### பணிகள் தொடர்பான பிரச்சினைகள் (சிறிய)

#### மொழிபெயர்ப்பு பணிகள் முரண்பாடுகள்
**பிரச்சினை:** மொழிபெயர்ப்பு PR உங்கள் மாற்றங்களுடன் முரண்படுகிறது

**தீர்வு:**
- ஆங்கில மூல கோப்புகளை மட்டுமே திருத்தவும்
- தானியக்க மொழிபெயர்ப்பு பணியை மொழிபெயர்ப்புகளை கையாள அனுமதிக்கவும்
- முரண்பாடுகள் ஏற்பட்டால், மொழிபெயர்ப்புகள் இணைக்கப்பட்ட பிறகு `main` ஐ உங்கள் கிளையில் இணைக்கவும்

#### மாதிரி பதிவிறக்க தோல்விகள்
**பிரச்சினை:** Foundry Local மாதிரிகளை பதிவிறக்க தோல்வி அடைகிறது

**தீர்வு:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## கூடுதல் வளங்கள்

### கற்றல் பாதைகள்
- **ஆரம்பகட்ட பாதை:** Modules 01-02 (7-9 மணி நேரம்)
- **இடைநிலை பாதை:** Modules 03-04 (9-11 மணி நேரம்)
- **மேம்பட்ட பாதை:** Modules 05-07 (12-15 மணி நேரம்)
- **வல்லுநர் பாதை:** Module 08 (8-10 மணி நேரம்)
- **கைநிறைவு Workshop:** Workshop பொருட்கள் (6-8 மணி நேரம்)

### முக்கிய தொகுதி உள்ளடக்கம்
- **Module01:** EdgeAI அடிப்படைகள் மற்றும் உண்மையான உலகக் கசேஸ்கள்
- **Module02:** சிறிய மொழி மாதிரி (SLM) குடும்பங்கள் மற்றும் கட்டமைப்புகள்
- **Module03:** உள்ளூர் மற்றும் மேக வெளியீட்டு உத்திகள்
- **Module04:** பல கட்டமைப்புகளுடன் மாதிரி மேம்பாடு (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - தயாரிப்பு செயல்பாடுகள்
- **Module06:** AI முகவர்கள் மற்றும் செயல்பாட்டு அழைப்புகள்
- **Module07:** தளத்திற்கு குறிப்பிட்ட செயல்பாடுகள்
- **Module08:** Foundry Local கருவிகள் 10 விரிவான மாதிரிகளுடன்

### வெளிப்புற சார்புகள்
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-இன் இணக்கமான API உடன் உள்ளூர் AI மாதிரி இயக்கம்
  - [ஆவணங்கள்](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - மேம்பாட்டு கட்டமைப்பு

10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel இணைப்பு

### பணிமனை மாதிரிகள்

இந்த பணிமனை 6 முன்னேற்றமான அமர்வுகளை நடைமுறை செயல்பாடுகளுடன் கொண்டுள்ளது:

1. **அமர்வு 01** - Foundry Local இணைப்புடன் உரையாடல் தொடக்கம்
2. **அமர்வு 02** - RAG குழாய் மற்றும் RAGAS மூலம் மதிப்பீடு
3. **அமர்வு 03** - திறந்த மூல மாதிரிகளை ஒப்பீடு செய்தல்
4. **அமர்வு 04** - மாதிரி ஒப்பீடு மற்றும் தேர்வு
5. **அமர்வு 05** - பல முகவர் ஒருங்கிணைப்பு அமைப்புகள்
6. **அமர்வு 06** - மாதிரி வழிமுறை மற்றும் குழாய் மேலாண்மை

ஒவ்வொரு மாதிரியும் Foundry Local உடன் Edge AI மேம்பாட்டின் பல்வேறு அம்சங்களை விளக்குகிறது.

### செயல்திறன் கருத்துக்கள்

- SLMகள் Edge பயன்பாட்டிற்காக (2-16GB RAM) மேம்படுத்தப்பட்டுள்ளன
- உள்ளூர் முன்னறிவிப்பு 50-500ms பதில் நேரத்தை வழங்குகிறது
- அளவீட்டு தொழில்நுட்பங்கள் 75% அளவு குறைப்பை 85% செயல்திறன் தக்கவைத்துக்கொண்டு அடைகின்றன
- உள்ளூர் மாதிரிகளுடன் நேரடி உரையாடல் திறன்கள்

### பாதுகாப்பு மற்றும் தனியுரிமை

- அனைத்து செயலாக்கமும் உள்ளூரில் நடக்கிறது - தரவுகள் மேகத்திற்குப் பரிமாறப்படாது
- தனியுரிமைக்கு முக்கியத்துவம் உள்ள பயன்பாடுகளுக்கு ஏற்றது (மருத்துவம், நிதி)
- தரவின் இறையாண்மை தேவைகளை பூர்த்தி செய்கிறது
- Foundry Local முழுமையாக உள்ளூர் ஹார்ட்வேரில் இயங்குகிறது

## உதவி பெறுதல்

### ஆவணங்கள்

- **முக்கிய README**: [README.md](README.md) - களஞ்சியத்தின் மேற்பார்வை மற்றும் கற்றல் பாதைகள்
- **ஆய்வு வழிகாட்டி**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - கற்றல் வளங்கள் மற்றும் காலக்கெடுகள்
- **ஆதரவு**: [SUPPORT.md](SUPPORT.md) - உதவி பெறுவது எப்படி
- **பாதுகாப்பு**: [SECURITY.md](SECURITY.md) - பாதுகாப்பு பிரச்சினைகளை அறிவிக்க

### சமூக ஆதரவு

- **GitHub Issues**: [பிழைகளை அறிவிக்க அல்லது அம்சங்களை கோருங்கள்](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [கேள்விகளை கேளுங்கள் மற்றும் யோசனைகளை பகிருங்கள்](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local உடன் தொழில்நுட்ப பிரச்சினைகள்](https://github.com/microsoft/Foundry-Local/issues)

### தொடர்பு

- **பராமரிப்பாளர்கள்**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) ஐப் பாருங்கள்
- **பாதுகாப்பு பிரச்சினைகள்**: [SECURITY.md](SECURITY.md) இல் பொறுப்பான வெளிப்பாட்டை பின்பற்றுங்கள்
- **Microsoft ஆதரவு**: நிறுவன ஆதரவுக்கு, Microsoft வாடிக்கையாளர் சேவையை தொடர்பு கொள்ளுங்கள்

### கூடுதல் வளங்கள்

- **Microsoft Learn**: [AI மற்றும் இயந்திர கற்றல் கற்றல் பாதைகள்](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ஆவணங்கள்**: [அதிகாரப்பூர்வ ஆவணங்கள்](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **சமூக மாதிரிகள்**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) இல் சமூக பங்களிப்புகளைப் பாருங்கள்

---

**இது Edge AI மேம்பாட்டை கற்பதற்கான கல்வி களஞ்சியமாகும். முதன்மை பங்களிப்பு முறை கல்வி உள்ளடக்கத்தை மேம்படுத்துதல் மற்றும் Edge AI கருத்துக்களை விளக்கும் மாதிரிகளைச் சேர்த்தல்/மேம்படுத்தல் ஆகும்.**

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.