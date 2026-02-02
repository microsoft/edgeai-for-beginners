# AGENTS.md

> **EdgeAI အတွက် Developer လမ်းညွှန် - အခြေခံများအတွက်**
> 
> ဒီစာရွက်စာတမ်းမှာ ဒီ repository ကို အသုံးပြုနေတဲ့ developer, AI agent, နဲ့ contributor တွေအတွက် အပြည့်အစုံသော အချက်အလက်များကို ပေးထားပါတယ်။ Setup, development workflow, testing, နဲ့ အကောင်းဆုံး လုပ်ဆောင်မှုများကို ဖော်ပြထားပါတယ်။
> 
> **နောက်ဆုံးအပ်ဒိတ်**: အောက်တိုဘာ ၃၀၊ ၂၀၂၅ | **စာရွက်စာတမ်းဗားရှင်း**: ၃.၀

## အကြောင်းအရာများ

- [Project အကျဉ်းချုပ်](../..)
- [Repository ဖွဲ့စည်းပုံ](../..)
- [လိုအပ်ချက်များ](../..)
- [Setup Commands](../..)
- [Development Workflow](../..)
- [Testing လမ်းညွှန်ချက်များ](../..)
- [Code Style လမ်းညွှန်ချက်များ](../..)
- [Pull Request လမ်းညွှန်ချက်များ](../..)
- [Translation System](../..)
- [Foundry Local Integration](../..)
- [Build နဲ့ Deployment](../..)
- [Common Issues နဲ့ Troubleshooting](../..)
- [အပိုဆောင်း Resources](../..)
- [Project-Specific မှတ်ချက်များ](../..)
- [အကူအညီရယူခြင်း](../..)

## Project အကျဉ်းချုပ်

EdgeAI for Beginners သည် Small Language Models (SLMs) အသုံးပြု၍ Edge AI ဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားပေးသည့် comprehensive educational repository ဖြစ်သည်။ ဒီ course မှာ EdgeAI အခြေခံများ, model deployment, optimization နည်းလမ်းများ, နဲ့ Microsoft Foundry Local နဲ့ အခြား AI frameworks အသုံးပြု၍ production-ready implementation များကို ဖော်ပြထားသည်။

**အဓိက နည်းပညာများ:**
- Python 3.8+ (AI/ML sample များအတွက် အဓိက programming language)
- .NET C# (AI/ML sample များ)
- JavaScript/Node.js နဲ့ Electron (desktop application များအတွက်)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Model Optimization: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository အမျိုးအစား:** ၈ ခု module နဲ့ ၁၀ ခု comprehensive sample application များပါဝင်သော သင်ကြားရေးအကြောင်းအရာ repository

**Architecture:** Multi-module learning path နဲ့ edge AI deployment pattern များကို practical sample များဖြင့် ဖော်ပြထားသည်

## Repository ဖွဲ့စည်းပုံ

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

## လိုအပ်ချက်များ

### လိုအပ်သော Tools

- **Python 3.8+** - AI/ML sample များနဲ့ notebook များအတွက်
- **Node.js 16+** - Electron sample application အတွက်
- **Git** - Version control အတွက်
- **Microsoft Foundry Local** - AI model များကို locally run လုပ်ရန်

### အကြံပြုသော Tools

- **Visual Studio Code** - Python, Jupyter, နဲ့ Pylance extensions ပါဝင်သော
- **Windows Terminal** - Command-line အတွေ့အကြုံကို ပိုမိုကောင်းမွန်စေရန် (Windows အသုံးပြုသူများအတွက်)
- **Docker** - Containerized development အတွက် (optional)

### System Requirements

- **RAM**: အနည်းဆုံး ၈GB, multi-model scenario များအတွက် ၁၆GB+ အကြံပြု
- **Storage**: Model နဲ့ dependency များအတွက် အနည်းဆုံး ၁၀GB+ အခမဲ့နေရာ
- **OS**: Windows 10/11, macOS 11+, Linux (Ubuntu 20.04+)
- **Hardware**: AVX2 support ပါသော CPU; GPU (CUDA, Qualcomm NPU) optional ဖြစ်သော်လည်း အကြံပြု

### Knowledge Requirements

- Python programming အခြေခံကို နားလည်မှု
- Command-line interface များကို အသုံးပြုနိုင်မှု
- AI/ML အကြောင်းအရာများကို နားလည်မှု (sample development အတွက်)
- Git workflow နဲ့ pull request လုပ်ငန်းစဉ်များကို နားလည်မှု

## Setup Commands

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Sample Setup (Module08 နဲ့ Workshop sample များ)

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

### Node.js Sample Setup (Sample 08 - Windows Chat App)

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

### Foundry Local Setup

Foundry Local သည် sample များကို run လုပ်ရန် လိုအပ်သည်။ အောက်ပါ link မှာ download နဲ့ install လုပ်ပါ:

**Installation:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: [releases page](https://github.com/microsoft/Foundry-Local/releases) မှ download လုပ်ပါ

**Quick Start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Note**: Foundry Local သည် hardware (CUDA GPU, Qualcomm NPU, CPU) အတွက် အကောင်းဆုံး model variant ကို အလိုအလျောက် ရွေးချယ်ပေးသည်။

## Development Workflow

### Content Development

ဒီ repository မှာ အဓိကအားဖြင့် **Markdown educational content** ပါဝင်သည်။ ပြင်ဆင်မှုများလုပ်စဉ်:

1. သင့် module directory တွင် `.md` ဖိုင်များကို ပြင်ဆင်ပါ
2. ရှိပြီးသား formatting pattern များကို လိုက်နာပါ
3. Code example များကို မှန်ကန်မှုရှိစေရန် စမ်းသပ်ပါ
4. လိုအပ်ပါက အခြေခံ content translation ကို update လုပ်ပါ (သို့မဟုတ် automation ကို အားထားပါ)

### Sample Application Development

Module08 Python sample များအတွက် (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python sample များအတွက်:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron sample (sample 08) အတွက်:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Sample Application များကို စမ်းသပ်ခြင်း

Python sample များတွင် automated test များမပါဝင်သော်လည်း run လုပ်ခြင်းဖြင့် စမ်းသပ်နိုင်သည်:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron sample တွင် test infrastructure ပါဝင်သည်:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testing လမ်းညွှန်ချက်များ

### Content Validation

Repository သည် automated translation workflow များကို အသုံးပြုသည်။ Translation များအတွက် manual testing မလိုအပ်ပါ။

**Manual validation for content changes:**
1. Markdown rendering ကို `.md` ဖိုင်များ preview လုပ်၍ စစ်ဆေးပါ
2. Link များသည် မှန်ကန်သော target များကို ရောက်ရှိမှုရှိစေရန် စစ်ဆေးပါ
3. Documentation တွင်ပါဝင်သော code snippet များကို စမ်းသပ်ပါ
4. Image များသည် မှန်ကန်စွာ load ဖြစ်မှုရှိစေရန် စစ်ဆေးပါ

### Sample Application Testing

**Module08/samples/08 (Electron app) တွင် comprehensive testing ပါဝင်သည်:**
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

**Python sample များကို manual စမ်းသပ်မှု လိုအပ်သည်:**
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

## Code Style လမ်းညွှန်ချက်များ

### Markdown Content

- Heading hierarchy (# title, ## main section, ### subsection) ကို တိကျစွာ အသုံးပြုပါ
- Code block များကို language specifier ဖြင့် ထည့်သွင်းပါ: ```python, ```bash, ```javascript
- Table, list, နဲ့ emphasis များအတွက် ရှိပြီးသား formatting ကို လိုက်နာပါ
- Line များကို ~80-100 character အတွင်းထားရန် ကြိုးစားပါ (strict မဟုတ်ပါ)
- Internal reference များအတွက် relative link များကို အသုံးပြုပါ

### Python Code Style

- PEP 8 convention များကို လိုက်နာပါ
- Type hint များကို သင့်တော်သောနေရာတွင် အသုံးပြုပါ
- Function နဲ့ class များအတွက် docstring များထည့်သွင်းပါ
- အဓိကကျသော variable name များကို အသုံးပြုပါ
- Function များကို အဓိကကျသောအကြောင်းအရာများအတွက် အတိုချုပ်ထားပါ

### JavaScript/Node.js Code Style

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**အဓိက convention များ:**
- ESLint configuration ကို sample 08 တွင် ပေးထားသည်
- Prettier ကို code formatting အတွက် အသုံးပြုပါ
- ES6+ syntax ကို အသုံးပြုပါ
- Codebase တွင် ရှိပြီးသား pattern များကို လိုက်နာပါ

## Pull Request လမ်းညွှန်ချက်များ

### Contribution Workflow

1. **Repository ကို fork လုပ်ပါ** နဲ့ `main` branch မှ branch အသစ်တစ်ခု ဖန်တီးပါ
2. **သင့်ပြင်ဆင်မှုများကို** code style လမ်းညွှန်ချက်များကို လိုက်နာ၍ ပြုလုပ်ပါ
3. **Testing လမ်းညွှန်ချက်များကို အသုံးပြု၍** စမ်းသပ်ပါ
4. **Conventional commits format ကို လိုက်နာ၍** commit message များကို ရေးပါ
5. **သင့် fork သို့ push လုပ်ပြီး** pull request တစ်ခု ဖန်တီးပါ
6. **Maintainer များ၏ feedback ကို** review အတွင်း အကြောင်းပြန်ပါ

### Branch Naming Convention

- `feature/<module>-<description>` - အခြား feature များအတွက်
- `fix/<module>-<description>` - Bug fix များအတွက်
- `docs/<description>` - Documentation တိုးတက်မှုများအတွက်
- `refactor/<description>` - Code refactoring အတွက်

### Commit Message Format

[Conventional Commits](https://www.conventionalcommits.org/) ကို လိုက်နာပါ:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ဥပမာများ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Title Format
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Code of Conduct

Contributor အားလုံးသည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ကို လိုက်နာရမည်။ Contribution မပြုမီ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ကို ပြန်လည်သုံးသပ်ပါ။

### Submit မပြုမီ

**Content ပြင်ဆင်မှုများအတွက်:**
- ပြင်ဆင်ထားသော Markdown ဖိုင်များကို preview လုပ်ပါ
- Link နဲ့ image များကို စစ်ဆေးပါ
- Typo နဲ့ grammar error များကို စစ်ဆေးပါ

**Sample code ပြင်ဆင်မှုများအတွက် (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python sample ပြင်ဆင်မှုများအတွက်:**
- Sample သည် အောင်မြင်စွာ run ဖြစ်မှုရှိစေရန် စမ်းသပ်ပါ
- Error handling သည် မှန်ကန်စွာ လုပ်ဆောင်မှုရှိစေရန် စစ်ဆေးပါ
- Foundry Local နှင့် အညီဖြစ်မှုကို စစ်ဆေးပါ

### Review Process

- Educational content ပြင်ဆင်မှုများကို တိကျမှုနဲ့ ရှင်းလင်းမှုအတွက် ပြန်လည်သုံးသပ်သည်
- Code sample များကို functionality အတွက် စမ်းသပ်သည်
- Translation update များကို GitHub Actions မှ အလိုအလျောက် လုပ်ဆောင်သည်

## Translation System

**အရေးကြီး:** Repository သည် GitHub Actions မှ automated translation ကို အသုံးပြုသည်။

- Translation များသည် `/translations/` directory တွင် (၅၀+ ဘာသာစကား) ပါဝင်သည်
- `co-op-translator.yml` workflow မှ အလိုအလျောက် translation လုပ်ဆောင်သည်
- **Translation ဖိုင်များကို manual ပြင်ဆင်မလုပ်ပါနှင့်** - overwrite ဖြစ်မည်
- Root နဲ့ module directory တွင် English source ဖိုင်များကိုသာ ပြင်ဆင်ပါ
- Translation များသည် `main` branch သို့ push လုပ်ပြီးနောက် အလိုအလျောက် ဖန်တီးသည်

## Foundry Local Integration

Module08 sample များအများစုသည် Microsoft Foundry Local ကို run လုပ်ရန် လိုအပ်သည်။

### Installation & Setup

**Foundry Local ကို Install လုပ်ပါ:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ကို Install လုပ်ပါ:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ကို စတင်ရန်
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

### SDK Usage (Python)
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

### Foundry Local ကို Verify လုပ်ခြင်း
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Sample များအတွက် Environment Variables

Sample များအများစုသည် အောက်ပါ environment variable များကို အသုံးပြုသည်:
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

**Note**: `FoundryLocalManager` ကို အသုံးပြုသောအခါ SDK သည် service discovery နဲ့ model loading ကို အလိုအလျောက် handle လုပ်သည်။ Model alias များ (ဥပမာ `phi-3.5-mini`) သည် hardware အတွက် အကောင်းဆုံး variant ကို ရွေးချယ်ပေးသည်။

## Build နဲ့ Deployment

### Content Deployment

ဒီ repository သည် documentation ဖြစ်သောကြောင့် content အတွက် build လုပ်စဉ်မလိုအပ်ပါ။

### Sample Application Building

**Electron Application (Module08/samples/08):**
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

**Python Samples:**
Build လုပ်စဉ်မလိုအပ်ပါ - Python interpreter ဖြင့် sample များကို တိုက်ရိုက် run လုပ်နိုင်သည်။

## Common Issues နဲ့ Troubleshooting

> **Tip**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) တွင် သိရှိထားသော ပြဿနာများနဲ့ ဖြေရှင်းနည်းများကို စစ်ဆေးပါ။

### Critical Issues (Blocking)

#### Foundry Local မရရှိခြင်း
**Issue:** Sample များသည် connection error များဖြင့် fail ဖြစ်သည်

**Solution:**
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

### Common Issues (Moderate)

#### Python Virtual Environment Issues
**Issue:** Module import error များ

**Solution:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron Build Issues
**Issue:** npm install သို့မဟုတ် build fail ဖြစ်သည်

**Solution:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflow Issues (Minor)

#### Translation Workflow Conflicts
**Issue:** Translation PR သည် သင့်ပြင်ဆင်မှုများနှင့် conflict ဖြစ်သည်

**Solution:**
- English source ဖိုင်များကိုသာ ပြင်ဆင်ပါ
- Automated translation workflow ကို translation များ handle လုပ်စေပါ
- Conflict ဖြစ်ပါက translation များ merge ပြီးနောက် `main` ကို သင့် branch သို့ merge လုပ်ပါ

#### Model Download Failures
**Issue:** Foundry Local သည် model များကို download လုပ်ရန် fail ဖြစ်သည်

**Solution:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## အပိုဆောင်း Resources

### Learning Paths
- **Beginner Path:** Module 01-02 (၇-၉ နာရီ)
- **Intermediate Path:** Module 03-04 (၉-၁၁ နာရီ)
- **Advanced Path:** Module 05-07 (၁၂-၁၅ နာရီ)
- **Expert Path:** Module 08 (၈-၁၀ နာရီ)
- **Hands-On Workshop:** Workshop materials (၆-၈ နာရီ)

### Key Module Content
- **Module01:** EdgeAI အခြေခံနဲ့ အမှန်တကယ် case study များ
- **Module02:** Small Language Model (SLM) များ၏ မျိုးစဉ်နဲ့ architecture များ
- **Module03:** Local နဲ့ cloud deployment strategy များ
- **Module04:** Framework များဖြင့် model optimization (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - production operation များ
- **Module06:** AI agent များနဲ့ function calling
- **Module07:** Platform-specific implementation များ
- **Module08:** Foundry Local toolkit နဲ့ ၁၀ ခု comprehensive sample များ

### External Dependencies
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-compatible API ပါသော Local AI model runtime
  - [Documentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimization framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Model optimization toolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel ရဲ့ optimization toolkit

## Project-Specific မှတ်ချက်များ

### Module08 Sample Applications

Repository တွင် ၁၀ ခု comprehensive sample application များပါဝင်သည်:

1. **01-REST Chat Quickstart** - OpenAI SDK integration အခြေခံ
2. **02-OpenAI SDK Integration** - Advanced SDK features
3. **03-Model Discovery & Benchmarking** - Model များကို နှိုင်းယှ
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel ပေါင်းစပ်မှု

### Workshop နမူနာ အက်ပလီကေးရှင်းများ

Workshop တွင် လက်တွေ့အကောင်အထည်ဖော်မှုများပါဝင်သော အဆင့်ဆင့် အစည်းအဝေး ၆ ခုပါဝင်သည် -

1. **Session 01** - Foundry Local ပေါင်းစပ်မှုဖြင့် Chat bootstrap
2. **Session 02** - RAG pipeline နှင့် RAGAS ဖြင့် အကဲဖြတ်ခြင်း
3. **Session 03** - အခမဲ့အသုံးပြုနိုင်သော မော်ဒယ်များကို Benchmarking ပြုလုပ်ခြင်း
4. **Session 04** - မော်ဒယ်များကို နှိုင်းယှဉ်ခြင်းနှင့် ရွေးချယ်ခြင်း
5. **Session 05** - Multi-agent orchestration systems
6. **Session 06** - မော်ဒယ်များကို လမ်းကြောင်းချခြင်းနှင့် pipeline စီမံခန့်ခွဲမှု

နမူနာတစ်ခုစီသည် Foundry Local ဖြင့် edge AI ဖွံ့ဖြိုးတိုးတက်မှု၏ အမျိုးမျိုးသော အချက်အလက်များကို ပြသသည်။

### စွမ်းဆောင်ရည်အရေးပါချက်များ

- SLMs များကို edge deployment အတွက် အထူးပြု optimize လုပ်ထားသည် (2-16GB RAM)
- Local inference သည် 50-500ms အတွင်း အဖြေများပေးနိုင်သည်
- Quantization နည်းလမ်းများသည် 75% အရွယ်အစားလျှော့ချပြီး 85% စွမ်းဆောင်ရည်ကို ထိန်းသိမ်းထားနိုင်သည်
- Local မော်ဒယ်များဖြင့် အချိန်နှင့်တပြေးညီ စကားဝိုင်းပြုလုပ်နိုင်မှု

### လုံခြုံရေးနှင့် ကိုယ်ရေးအချက်အလက်

- အားလုံးကို တိုင်းရင်းဒေတာပေါ်တွင်သာ အ処理လုပ်ဆောင်သည် - cloud သို့ ဒေတာမပို့ပါ
- ကိုယ်ရေးအချက်အလက်ကို အထူးဂရုစိုက်ရမည့် အက်ပလီကေးရှင်းများ (ကျန်းမာရေး၊ ဘဏ္ဍာရေး) အတွက် သင့်တော်သည်
- ဒေတာပိုင်ဆိုင်မှုလိုအပ်ချက်များကို ဖြည့်ဆည်းနိုင်သည်
- Foundry Local သည် တိုင်းရင်း hardware ပေါ်တွင်သာ အပြည့်အဝ လည်ပတ်သည်

## အကူအညီရယူခြင်း

### Documentation

- **Main README**: [README.md](README.md) - Repository အကြောင်းအရာနှင့် သင်ကြားမှုလမ်းကြောင်းများ
- **Study Guide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - သင်ကြားမှုအရင်းအမြစ်များနှင့် အချိန်ဇယား
- **Support**: [SUPPORT.md](SUPPORT.md) - အကူအညီရယူရန် နည်းလမ်းများ
- **Security**: [SECURITY.md](SECURITY.md) - လုံခြုံရေးပြဿနာများကို အကြောင်းကြားခြင်း

### Community Support

- **GitHub Issues**: [အမှားများကို အကြောင်းကြားရန် သို့မဟုတ် အင်္ဂါရပ်များကို တောင်းဆိုရန်](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [မေးခွန်းများမေးရန်နှင့် အကြံဉာဏ်များမျှဝေရန်](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local နှင့်ပတ်သက်သော နည်းပညာပြဿနာများ](https://github.com/microsoft/Foundry-Local/issues)

### ဆက်သွယ်ရန်

- **Maintainers**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) တွင် ကြည့်ပါ
- **Security Issues**: [SECURITY.md](SECURITY.md) တွင် တာဝန်ရှိသော အကြောင်းကြားမှုကို လိုက်နာပါ
- **Microsoft Support**: စီးပွားရေးအကူအညီအတွက် Microsoft ဖောက်သည်ဝန်ဆောင်မှုကို ဆက်သွယ်ပါ

### အပိုအရင်းအမြစ်များ

- **Microsoft Learn**: [AI နှင့် Machine Learning သင်ကြားမှုလမ်းကြောင်းများ](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Documentation**: [တရားဝင် Docs](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Community Samples**: Community မှ ပံ့ပိုးမှုများကို [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) တွင် ကြည့်ပါ

---

**ဤသည်မှာ Edge AI ဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားရန်အတွက် အဓိကထားသော ပညာရေးဆိုင်ရာ repository ဖြစ်သည်။ အဓိကပံ့ပိုးမှုပုံစံမှာ ပညာရေးအကြောင်းအရာများကို တိုးတက်အောင်လုပ်ခြင်းနှင့် Edge AI အယူအဆများကို ပြသသော နမူနာအက်ပလီကေးရှင်းများကို ထည့်သွင်းခြင်း/တိုးတက်အောင်လုပ်ခြင်းဖြစ်သည်။**

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။