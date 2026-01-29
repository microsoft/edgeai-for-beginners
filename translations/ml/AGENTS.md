# AGENTS.md

> **ആരംഭക്കാർക്കായി EdgeAI-യിൽ സംഭാവന നൽകുന്നതിനുള്ള ഡെവലപ്പർ ഗൈഡ്**
> 
> ഈ ഡോക്യുമെന്റ് ഈ റിപോസിറ്ററിയുമായി പ്രവർത്തിക്കുന്ന ഡെവലപ്പർമാർക്ക്, AI ഏജന്റുകൾക്കും, സംഭാവനക്കാർക്കും സമഗ്രമായ വിവരങ്ങൾ നൽകുന്നു. ഇത് സെറ്റപ്പ്, ഡെവലപ്പ്മെന്റ് വർക്ക്‌ഫ്ലോകൾ, ടെസ്റ്റിംഗ്, മികച്ച പ്രാക്ടീസുകൾ എന്നിവ ഉൾക്കൊള്ളുന്നു.
> 
> **അവസാനമായി അപ്ഡേറ്റ് ചെയ്തത്**: ഒക്ടോബർ 30, 2025 | **ഡോക്യുമെന്റ് പതിപ്പ്**: 3.0

## ഉള്ളടക്ക പട്ടിക

- [പ്രോജക്ട് അവലോകനം](../..)
- [റിപോസിറ്ററി ഘടന](../..)
- [ആവശ്യമായ മുൻ‌പരിചയങ്ങൾ](../..)
- [സെറ്റപ്പ് കമാൻഡുകൾ](../..)
- [ഡെവലപ്പ്മെന്റ് വർക്ക്‌ഫ്ലോ](../..)
- [ടെസ്റ്റിംഗ് നിർദ്ദേശങ്ങൾ](../..)
- [കോഡ് സ്റ്റൈൽ മാർഗ്ഗനിർദ്ദേശങ്ങൾ](../..)
- [പുൾ റിക്വസ്റ്റ് മാർഗ്ഗനിർദ്ദേശങ്ങൾ](../..)
- [ഭാഷാന്തര സംവിധാനം](../..)
- [Foundry Local ഇന്റഗ്രേഷൻ](../..)
- [ബിൽഡ് ആൻഡ് ഡിപ്ലോയ്മെന്റ്](../..)
- [സാധാരണ പ്രശ്നങ്ങളും പരിഹാരങ്ങളും](../..)
- [അധിക വിഭവങ്ങൾ](../..)
- [പ്രോജക്ട്-നിർദ്ദിഷ്ട കുറിപ്പുകൾ](../..)
- [സഹായം നേടുക](../..)

## Project Overview

EdgeAI for Beginners എന്നത് Edge AI വികസനം Small Language Models (SLMs) ഉപയോഗിച്ച് പഠിപ്പിക്കുന്ന സമഗ്രമായ വിദ്യാഭ്യാസ റിപോസിറ്ററിയാണ്. കോഴ്സ് EdgeAI അടിസ്ഥാനങ്ങൾ, മോഡൽ ഡിപ്ലോയ്മെന്റ്, ഒപ്റ്റിമൈസേഷൻ സാങ്കേതികവിദ്യകൾ, Microsoft Foundry Local, വിവിധ AI ഫ്രെയിംവർക്ക് എന്നിവ ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ-റെഡി നടപ്പാക്കലുകൾ ഉൾക്കൊള്ളുന്നു.

**പ്രധാന സാങ്കേതികവിദ്യകൾ:**
- Python 3.8+ (AI/ML സാമ്പിളുകൾക്കുള്ള പ്രാഥമിക ഭാഷ)
- .NET C# (AI/ML സാമ്പിളുകൾ)
- JavaScript/Node.js with Electron (ഡെസ്ക്ടോപ്പ് ആപ്ലിക്കേഷനുകൾക്കായി)
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI Toolkit
- OpenAI SDK
- AI ഫ്രെയിംവർക്ക്: LangChain, Semantic Kernel, Chainlit
- മോഡൽ ഒപ്റ്റിമൈസേഷൻ: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**റിപോസിറ്ററി തരം:** 8 മോഡ്യൂളുകളും 10 സമഗ്ര സാമ്പിൾ ആപ്ലിക്കേഷനുകളും ഉള്ള വിദ്യാഭ്യാസ ഉള്ളടക്ക റിപോസിറ്ററി

**ആർക്കിടെക്ചർ:** എഡ്ജ് AI ഡിപ്ലോയ്മെന്റ് പാറ്റേണുകൾ പ്രദർശിപ്പിക്കുന്ന പ്രായോഗിക സാമ്പിളുകളുള്ള മൾട്ടി-മോഡ്യൂൾ പഠന പാത

## Repository Structure

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

## Prerequisites

### ആവശ്യമായ ടൂളുകൾ

- **Python 3.8+** - AI/ML സാമ്പിളുകൾക്കും നോട്ട്‌ബുക്കുകൾക്കും
- **Node.js 16+** - Electron സാമ്പിൾ ആപ്ലിക്കേഷനിനായി
- **Git** - വേർഷൻ കൺട്രോളിനായി
- **Microsoft Foundry Local** - AI മോഡലുകൾ ലോക്കലായി ഓടിക്കാൻ

### ശുപാർശ ചെയ്ത ടൂളുകൾ

- **Visual Studio Code** - Python, Jupyter, Pylance എക്സ്റ്റൻഷനുകളോടുകൂടി
- **Windows Terminal** - മെച്ചപ്പെട്ട കമാൻഡ്-ലൈൻ അനുഭവത്തിനായി (Windows ഉപയോക്താക്കൾക്ക്)
- **Docker** - കണ്ടെയ്‌നറൈസ്ഡ് ഡെവലപ്പ്മെന്റിനായി (ഐച്ഛികം)

### സിസ്റ്റം ആവശ്യകതകൾ

- **RAM**: കുറഞ്ഞത് 8GB, മൾട്ടി-മോഡൽ സീനാരിയോകൾക്കായി 16GB+ ശുപാർശ
- **സ്റ്റോറേജ്**: മോഡലുകൾക്കും ഡിപ്പെൻഡൻസികൾക്കും 10GB+ ഫ്രീ സ്പേസ്
- **ഓപ്പറേറ്റിംഗ് സിസ്റ്റം**: Windows 10/11, macOS 11+, അല്ലെങ്കിൽ Linux (Ubuntu 20.04+)
- **ഹാർഡ്‌വെയർ**: AVX2 പിന്തുണയുള്ള CPU; GPU (CUDA, Qualcomm NPU) ഐച്ഛികം എന്നാൽ ശുപാർശ ചെയ്യുന്നു

### അറിവ് മുൻ‌പരിചയങ്ങൾ

- Python പ്രോഗ്രാമിംഗിന്റെ അടിസ്ഥാന അറിവ്
- കമാൻഡ്-ലൈൻ ഇന്റർഫേസുകളുമായി പരിചയം
- AI/ML ആശയങ്ങളുടെ ബോധം (സാമ്പിൾ ഡെവലപ്പ്മെന്റിനായി)
- Git വർക്ക്‌ഫ്ലോകളും പുൾ റിക്വസ്റ്റ് പ്രക്രിയകളും

## Setup Commands

### Repository Setup

```bash
# റിപ്പോസിറ്ററി ക്ലോൺ ചെയ്യുക
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# ബിൽഡ് ഘട്ടം ആവശ്യമില്ല - ഇത് പ്രധാനമായും വിദ്യാഭ്യാസ ഉള്ളടക്ക റിപ്പോസിറ്ററിയാണ്
```

### Python സാമ്പിൾ സെറ്റപ്പ് (Module08 and Workshop സാമ്പിളുകൾ)

```bash
# വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ച് സജീവമാക്കുക
python -m venv .venv
# വിൻഡോസ്-ൽ
.venv\Scripts\activate
# മാക്‌ഓഎസ്/ലിനക്സ്-ൽ
source .venv/bin/activate

# ഫൗണ്ട്രി ലോക്കൽ SDKയും ആശ്രിതങ്ങളും ഇൻസ്റ്റാൾ ചെയ്യുക
pip install foundry-local-sdk openai

# Module08 സാമ്പിളുകൾക്കായി അധിക ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക
cd Module08
pip install -r requirements.txt

# വർക്‌ഷോപ്പ് ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക
cd ../Workshop
pip install -r requirements.txt
```

### Node.js സാമ്പിൾ സെറ്റപ്പ് (Sample 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# വികസന മോഡിൽ ആരംഭിക്കുക
npm run dev

# ഉത്പാദനത്തിനായി നിർമ്മിക്കുക
npm run build

# ഇൻസ്റ്റാളർ സൃഷ്ടിക്കുക
npm run dist
```

### Foundry Local സെറ്റപ്പ്

സാമ്പിളുകൾ ഓടിക്കാൻ Foundry Local ആവശ്യമാണ്. ഔദ്യോഗിക റിപോസിറ്ററിയിൽ നിന്ന് ഡൗൺലോഡ് ചെയ്ത് ഇൻസ്റ്റാൾ ചെയ്യുക:

**ഇൻസ്റ്റലേഷൻ:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **മാനുവൽ**: [releases page](https://github.com/microsoft/Foundry-Local/releases) ൽ നിന്ന് ഡൗൺലോഡ് ചെയ്യുക

**ക്വിക്ക് സ്റ്റാർട്ട്:**
```bash
# നിങ്ങളുടെ ആദ്യ മോഡൽ പ്രവർത്തിപ്പിക്കുക (ആവശ്യമായാൽ സ്വയം ഡൗൺലോഡ് ചെയ്യും)
foundry model run phi-4-mini

# ലഭ്യമായ മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model ls

# സേവന നില പരിശോധിക്കുക
foundry service status
```

**കുറിപ്പ്**: Foundry Local നിങ്ങളുടെ ഹാർഡ്‌വെയറിനായി (CUDA GPU, Qualcomm NPU, അല്ലെങ്കിൽ CPU) ഏറ്റവും മികച്ച മോഡൽ വേരിയന്റ് സ്വയം തിരഞ്ഞെടുക്കും.

## Development Workflow

### ഉള്ളടക്ക വികസനം

ഈ റിപോസിറ്ററി പ്രധാനമായും **Markdown വിദ്യാഭ്യാസ ഉള്ളടക്കം** അടങ്ങിയതാണ്. മാറ്റങ്ങൾ വരുത്തുമ്പോൾ:

1. അനുയോജ്യമായ മോഡ്യൂൾ ഡയറക്ടറികളിൽ `.md` ഫയലുകൾ എഡിറ്റ് ചെയ്യുക
2. നിലവിലുള്ള ഫോർമാറ്റിംഗ് മാതൃകകൾ പാലിക്കുക
3. കോഡ് ഉദാഹരണങ്ങൾ ശരിയായതും ടെസ്റ്റ് ചെയ്തതുമായിരിക്കണം
4. ആവശ്യമായെങ്കിൽ അനുബന്ധമായ വിവർത്തന ഉള്ളടക്കം അപ്ഡേറ്റ് ചെയ്യുക (അല്ലെങ്കിൽ ഓട്ടോമേഷൻ കൈകാര്യം ചെയ്യട്ടെ)

### സാമ്പിൾ ആപ്ലിക്കേഷൻ വികസനം

Module08 Python സാമ്പിളുകൾക്കായി (സാമ്പിളുകൾ 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python സാമ്പിളുകൾക്കായി:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron സാമ്പിൾ (സാമ്പിൾ 08)ക്കായി:
```bash
cd Module08/samples/08
npm run dev  # ഹോട്ട് റീലോഡുമായി വികസനം
```

### സാമ്പിൾ ആപ്ലിക്കേഷനുകളുടെ ടെസ്റ്റിംഗ്

Python സാമ്പിളുകൾക്ക് ഓട്ടോമേറ്റഡ് ടെസ്റ്റുകൾ ഇല്ല, എന്നാൽ ഓടിച്ച് സാധുത പരിശോധിക്കാം:
```bash
# അടിസ്ഥാന ചാറ്റ് പ്രവർത്തനം പരിശോധിക്കുക
python samples/01/chat_quickstart.py "Hello"

# പ്രത്യേക മോഡലുമായി പരിശോധന നടത്തുക
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron സാമ്പിളിന് ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ ഉണ്ട്:
```bash
cd Module08/samples/08
npm test           # യൂണിറ്റ് ടെസ്റ്റുകൾ നടത്തുക
npm run test:e2e   # എന്റ്-ടു-എന്റ് ടെസ്റ്റുകൾ നടത്തുക
npm run lint       # കോഡ് സ്റ്റൈൽ പരിശോധിക്കുക
```

## Testing Instructions

### ഉള്ളടക്കം സാധുത പരിശോധന

റിപോസിറ്ററി ഓട്ടോമേറ്റഡ് വിവർത്തന വർക്ക്‌ഫ്ലോകൾ ഉപയോഗിക്കുന്നു. വിവർത്തനങ്ങൾക്ക് മാനുവൽ ടെസ്റ്റിംഗ് ആവശ്യമില്ല.

**ഉള്ളടക്ക മാറ്റങ്ങൾക്ക് മാനുവൽ പരിശോധന:**
1. `.md` ഫയലുകൾ പ്രിവ്യൂ ചെയ്ത് Markdown റെൻഡറിംഗ് പരിശോധിക്കുക
2. എല്ലാ ലിങ്കുകളും സാധുവായ ലക്ഷ്യങ്ങളിലേക്കാണെന്ന് ഉറപ്പാക്കുക
3. ഡോക്യുമെന്റേഷനിൽ ഉൾപ്പെടുത്തിയ കോഡ് സ്നിപ്പറ്റുകൾ പരീക്ഷിക്കുക
4. ചിത്രങ്ങൾ ശരിയായി ലോഡ് ആകുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക

### സാമ്പിൾ ആപ്ലിക്കേഷൻ ടെസ്റ്റിംഗ്

**Module08/samples/08 (Electron ആപ്പ്) സമഗ്രമായ ടെസ്റ്റിംഗ് ഉണ്ട്:**
```bash
cd Module08/samples/08

# എല്ലാ ടെസ്റ്റുകളും നടത്തുക
npm test

# യൂണിറ്റ് ടെസ്റ്റുകൾ മാത്രം നടത്തുക
npm test -- --testPathPattern=unit

# ഇന്റഗ്രേഷൻ ടെസ്റ്റുകൾ നടത്തുക
npm run test:integration

# E2E ടെസ്റ്റുകൾ നടത്തുക
npm run test:e2e

# ടെസ്റ്റ് കവറേജ് പരിശോധിക്കുക
npm test -- --coverage
```

**Python സാമ്പിളുകൾ മാനുവലായി ടെസ്റ്റ് ചെയ്യണം:**
```bash
# മോഡ്യൂൾ08 സാമ്പിളുകൾ
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# വർക്‌ഷോപ്പ് സാമ്പിളുകൾ
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# വർക്‌ഷോപ്പ് സാധുത പരിശോധന ഉപകരണങ്ങൾ ഉപയോഗിക്കുക
cd Workshop/scripts
python validate_samples.py  # സിന്റാക്സ്, ഇറക്കുമതികൾ സാധുത പരിശോധിക്കുക
python test_samples.py      # സ്മോക്ക് ടെസ്റ്റുകൾ നടത്തുക
```

## Code Style Guidelines

### Markdown ഉള്ളടക്കം

- തലക്കെട്ടുകൾക്കായി ഏകീകൃത തലമുറ ക്രമം ഉപയോഗിക്കുക (# തലക്കെട്ടിനായി, ## പ്രധാന വിഭാഗങ്ങൾക്കായി, ### ഉപവിഭാഗങ്ങൾക്കായി)
- ഭാഷാ നിർദ്ദേശകങ്ങളോടുകൂടിയ കോഡ് ബ്ലോക്കുകൾ ഉൾപ്പെടുത്തുക: ```python, ```bash, ```javascript
- പട്ടികകൾ, ലിസ്റ്റുകൾ, ഊന്നൽ എന്നിവയ്ക്ക് നിലവിലുള്ള ഫോർമാറ്റിംഗ് പാലിക്കുക
- വരികൾ വായിക്കാൻ എളുപ്പമുള്ളവയാക്കുക (~80-100 അക്ഷരങ്ങൾ ലക്ഷ്യം വയ്ക്കുക, കർശനമല്ല)
- ആന്തരിക റഫറൻസുകൾക്കായി സാപേക്ഷ ലിങ്കുകൾ ഉപയോഗിക്കുക

### Python കോഡ് സ്റ്റൈൽ

- PEP 8 മാനദണ്ഡങ്ങൾ പാലിക്കുക
- ആവശ്യമായിടത്ത് ടൈപ്പ് ഹിന്റുകൾ ഉപയോഗിക്കുക
- ഫംഗ്ഷനുകൾക്കും ക്ലാസുകൾക്കും ഡോക്സ്ട്രിംഗുകൾ ഉൾപ്പെടുത്തുക
- അർത്ഥമുള്ള വേരിയബിൾ നാമങ്ങൾ ഉപയോഗിക്കുക
- ഫംഗ്ഷനുകൾ കേന്ദ്രീകരിച്ചും സംക്ഷിപ്തവുമാകണം

### JavaScript/Node.js കോഡ് സ്റ്റൈൽ

```bash
# ഇലക്ട്രോൺ സാമ്പിൾ ESLint കോൺഫിഗറേഷൻ പിന്തുടരുന്നു
cd Module08/samples/08
npm run lint        # സ്റ്റൈൽ പ്രശ്നങ്ങൾ പരിശോധിക്കുക
npm run lint:fix    # സ്റ്റൈൽ പ്രശ്നങ്ങൾ സ്വയം പരിഹരിക്കുക
npm run format      # പ്രിറ്റിയർ ഉപയോഗിച്ച് ഫോർമാറ്റ് ചെയ്യുക
```

**പ്രധാന മാനദണ്ഡങ്ങൾ:**
- സാമ്പിൾ 08-ൽ ESLint കോൺഫിഗറേഷൻ നൽകിയിട്ടുണ്ട്
- കോഡ് ഫോർമാറ്റിംഗിനായി Prettier ഉപയോഗിക്കുക
- ആധുനിക ES6+ സിന്റാക്സ് ഉപയോഗിക്കുക
- കോഡ്‌ബേസിലെ നിലവിലുള്ള മാതൃകകൾ പാലിക്കുക

## Pull Request Guidelines

### സംഭാവന വർക്ക്‌ഫ്ലോ

1. **റിപോസിറ്ററി ഫോർക്ക് ചെയ്യുക** പിന്നെ `main` ബ്രാഞ്ചിൽ നിന്ന് പുതിയ ബ്രാഞ്ച് സൃഷ്ടിക്കുക
2. **കോഡ് സ്റ്റൈൽ മാർഗ്ഗനിർദ്ദേശങ്ങൾ പാലിച്ച് മാറ്റങ്ങൾ വരുത്തുക**
3. **മുകളിൽ നൽകിയ ടെസ്റ്റിംഗ് നിർദ്ദേശങ്ങൾ അനുസരിച്ച് പൂർണ്ണമായും ടെസ്റ്റ് ചെയ്യുക**
4. **ക്ലിയർ മെസ്സേജുകളോടെ കമ്മിറ്റ് ചെയ്യുക** (conventional commits ഫോർമാറ്റ് പാലിച്ച്)
5. **ഫോർക്കിലേക്ക് പുഷ് ചെയ്ത് പുൾ റിക്വസ്റ്റ് സൃഷ്ടിക്കുക**
6. **റിവ്യൂ സമയത്ത് മെയിന്റെയ്‌നർമാരുടെ ഫീഡ്ബാക്കിന് പ്രതികരിക്കുക**

### ബ്രാഞ്ച് നാമകരണം

- `feature/<module>-<description>` - പുതിയ ഫീച്ചറുകൾക്കോ ഉള്ളടക്കത്തിനോ
- `fix/<module>-<description>` - ബഗ് ഫിക്സുകൾക്കായി
- `docs/<description>` - ഡോക്യുമെന്റേഷൻ മെച്ചപ്പെടുത്തലുകൾക്കായി
- `refactor/<description>` - കോഡ് റിഫാക്ടറിംഗിനായി

### കമ്മിറ്റ് മെസ്സേജ് ഫോർമാറ്റ്

[Conventional Commits](https://www.conventionalcommits.org/) പാലിക്കുക:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ഉദാഹരണങ്ങൾ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### തലക്കെട്ട് ഫോർമാറ്റ്
```
[ModuleXX] Brief description of change
```
 അല്ലെങ്കിൽ
```
[Module08/samples/XX] Description for sample changes
```

### പെരുമാറ്റ നയം

എല്ലാ സംഭാവനക്കാർക്കും [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) പാലിക്കണം. സംഭാവന നൽകുന്നതിന് മുമ്പ് [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) പരിശോധിക്കുക.

### സമർപ്പിക്കുന്നതിന് മുമ്പ്

**ഉള്ളടക്ക മാറ്റങ്ങൾക്കായി:**
- മാറ്റിയ എല്ലാ Markdown ഫയലുകളും പ്രിവ്യൂ ചെയ്യുക
- ലിങ്കുകളും ചിത്രങ്ങളും ശരിയായി പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് ഉറപ്പാക്കുക
- ടൈപ്പോയും വ്യാകരണ പിശകുകളും പരിശോധിക്കുക

**സാമ്പിൾ കോഡ് മാറ്റങ്ങൾക്കായി (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python സാമ്പിൾ മാറ്റങ്ങൾക്കായി:**
- സാമ്പിൾ വിജയകരമായി ഓടുന്നുണ്ടോ എന്ന് ടെസ്റ്റ് ചെയ്യുക
- പിശക് കൈകാര്യം ശരിയായി നടക്കുന്നതായി ഉറപ്പാക്കുക
- Foundry Local-നൊപ്പം പൊരുത്തപ്പെടുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക

### റിവ്യൂ പ്രക്രിയ

- വിദ്യാഭ്യാസ ഉള്ളടക്ക മാറ്റങ്ങൾ കൃത്യതക്കും വ്യക്തതക്കും റിവ്യൂ ചെയ്യപ്പെടുന്നു
- കോഡ് സാമ്പിളുകൾ പ്രവർത്തനക്ഷമതക്കായി ടെസ്റ്റ് ചെയ്യപ്പെടുന്നു
- വിവർത്തന അപ്ഡേറ്റുകൾ GitHub Actions ഓട്ടോമാറ്റിക്കായി കൈകാര്യം ചെയ്യുന്നു

## Translation System

**മഹത്ത്വം:** ഈ റിപോസിറ്ററി GitHub Actions വഴി ഓട്ടോമേറ്റഡ് വിവർത്തനം ഉപയോഗിക്കുന്നു.

- വിവർത്തനങ്ങൾ `/translations/` ഡയറക്ടറിയിൽ (50+ ഭാഷകൾ)
- `co-op-translator.yml` വർക്ക്‌ഫ്ലോ വഴി ഓട്ടോമേറ്റഡ്
- **വിവർത്തന ഫയലുകൾ മാനുവലായി എഡിറ്റ് ചെയ്യരുത്** - അവ മായ്ക്കപ്പെടും
- റൂട്ട്, മോഡ്യൂൾ ഡയറക്ടറികളിലെ ഇംഗ്ലീഷ് സോഴ്‌സ് ഫയലുകൾ മാത്രം എഡിറ്റ് ചെയ്യുക
- `main` ബ്രാഞ്ചിലേക്ക് പുഷ് ചെയ്യുമ്പോൾ വിവർത്തനങ്ങൾ സ്വയം സൃഷ്ടിക്കപ്പെടും

## Foundry Local Integration

മിക്ക Module08 സാമ്പിളുകൾക്കും Microsoft Foundry Local ഓടിക്കേണ്ടതാണ്.

### ഇൻസ്റ്റലേഷൻ & സെറ്റപ്പ്

**Foundry Local ഇൻസ്റ്റാൾ ചെയ്യുക:**
```bash
# വിൻഡോസ്
winget install Microsoft.FoundryLocal

# മാക്‌ഓഎസ്
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ഇൻസ്റ്റാൾ ചെയ്യുക:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ആരംഭിക്കൽ
```bash
# സേവനം ആരംഭിച്ച് ഒരു മോഡൽ പ്രവർത്തിപ്പിക്കുക (ആവശ്യമായാൽ സ്വയം ഡൗൺലോഡ് ചെയ്യും)
foundry model run phi-3.5-mini

# അല്ലെങ്കിൽ സ്വയം ഹാർഡ്‌വെയർ ഓപ്റ്റിമൈസേഷനായി മോഡൽ അലിയാസുകൾ ഉപയോഗിക്കുക
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# സേവനത്തിന്റെ നില പരിശോധിക്കുക
foundry service status

# ലഭ്യമായ മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model ls
```

### SDK ഉപയോഗം (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# സ്വയം ഹാർഡ്‌വെയർ ഓപ്റ്റിമൈസേഷനായി മോഡൽ അലിയാസ് ഉപയോഗിക്കുക
alias = "phi-4-mini"

# മാനേജർ സൃഷ്ടിക്കുക (സേവനം സ്വയം ആരംഭിക്കുകയും മോഡൽ ലോഡ് ചെയ്യുകയും ചെയ്യുന്നു)
manager = FoundryLocalManager(alias)

# ലോക്കൽ ഫൗണ്ട്രി സേവനത്തിനായി OpenAI ക്ലയന്റ് കോൺഫിഗർ ചെയ്യുക
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# മോഡൽ ഉപയോഗിക്കുക
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local സ്ഥിരീകരിക്കൽ
```bash
# സേവന നിലയും എന്റ്പോയിന്റും
foundry service status

# ലോഡ് ചെയ്ത മോഡലുകളുടെ പട്ടിക (REST API)
curl http://localhost:<port>/v1/models

# കുറിപ്പ്: 'foundry service status' പ്രവർത്തിപ്പിക്കുമ്പോൾ പോർട്ട് പ്രദർശിപ്പിക്കും
```

### സാമ്പിളുകൾക്കുള്ള പരിസ്ഥിതി വേരിയബിളുകൾ

മിക്ക സാമ്പിളുകളും ഈ പരിസ്ഥിതി വേരിയബിളുകൾ ഉപയോഗിക്കുന്നു:
```bash
# ഫൗണ്ട്രി ലോക്കൽ കോൺഫിഗറേഷൻ
# കുറിപ്പ്: SDK (FoundryLocalManager) സ്വയം എൻഡ്‌പോയിന്റ് കണ്ടെത്തുന്നു
set MODEL=phi-4-mini  # അല്ലെങ്കിൽ phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # ലോക്കൽ ഉപയോഗത്തിന് ആവശ്യമായില്ല

# മാനുവൽ എൻഡ്‌പോയിന്റ് (SDK ഉപയോഗിക്കാത്ത പക്ഷം)
# പോർട്ട് 'foundry service status' വഴി കാണിക്കുന്നു
set BASE_URL=http://localhost:<port>

# Azure OpenAI ഫാൾബാക്ക് (ഐച്ഛികം)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**കുറിപ്പ്**: `FoundryLocalManager` ഉപയോഗിക്കുമ്പോൾ SDK സേവന കണ്ടെത്തലും മോഡൽ ലോഡിംഗും സ്വയം കൈകാര്യം ചെയ്യും. മോഡൽ അലിയാസുകൾ (ഉദാ: `phi-3.5-mini`) നിങ്ങളുടെ ഹാർഡ്‌വെയറിനായി ഏറ്റവും മികച്ച വേരിയന്റ് തിരഞ്ഞെടുക്കാൻ സഹായിക്കുന്നു.

## Build and Deployment

### ഉള്ളടക്കം ഡിപ്ലോയ്മെന്റ്

ഈ റിപോസിറ്ററി പ്രധാനമായും ഡോക്യുമെന്റേഷൻ ആണ് - ഉള്ളടക്കത്തിന് ബിൽഡ് പ്രക്രിയ ആവശ്യമില്ല.

### സാമ്പിൾ ആപ്ലിക്കേഷൻ ബിൽഡിംഗ്

**Electron ആപ്ലിക്കേഷൻ (Module08/samples/08):**
```bash
cd Module08/samples/08

# വികസന ബിൽഡ്
npm run dev

# ഉത്പാദന ബിൽഡ്
npm run build

# വിൻഡോസ് ഇൻസ്റ്റാളർ സൃഷ്ടിക്കുക
npm run dist

# പോർട്ടബിൾ എക്സിക്യൂട്ടബിൾ സൃഷ്ടിക്കുക
npm run pack
```

**Python സാമ്പിളുകൾ:**
ബിൽഡ് പ്രക്രിയ ഇല്ല - Python ഇന്റർപ്രിറ്റർ ഉപയോഗിച്ച് നേരിട്ട് ഓടിക്കുന്നു.

## Common Issues and Troubleshooting

> **ടിപ്പ്**: അറിയപ്പെട്ട പ്രശ്നങ്ങളും പരിഹാരങ്ങളും അറിയാൻ [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) പരിശോധിക്കുക.

### ഗുരുതര പ്രശ്നങ്ങൾ (അടിയന്തര തടസ്സങ്ങൾ)

#### Foundry Local ഓടുന്നില്ല
**പ്രശ്നം:** സാമ്പിളുകൾ കണക്ഷൻ പിശകുകളോടെ പരാജയപ്പെടുന്നു

**പരിഹാരം:**
```bash
# സേവനം പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക
foundry service status

# ഒരു മോഡലുമായി സേവനം ആരംഭിക്കുക
foundry model run phi-4-mini

# അല്ലെങ്കിൽ വ്യക്തമായി സേവനം ആരംഭിക്കുക
foundry service start

# ലോഡ് ചെയ്ത മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model ls

# REST API വഴി സ്ഥിരീകരിക്കുക ('foundry service status' ൽ കാണിച്ച പോർട്ട്)
curl http://localhost:<port>/v1/models
```

### സാധാരണ പ്രശ്നങ്ങൾ (മധ്യസ്ഥരം)

#### Python വെർച്വൽ എൻവയോൺമെന്റ് പ്രശ്നങ്ങൾ
**പ്രശ്നം:** മോഡ്യൂൾ ഇമ്പോർട്ട് പിശകുകൾ

**പരിഹാരം:**
```bash
# വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കിയിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക
# വിൻഡോസ്
.venv\Scripts\activate
# മാക്‌ഒഎസ്/ലിനക്സ്
source .venv/bin/activate

# ആശ്രിതങ്ങൾ പുനഃസ്ഥാപിക്കുക
pip install -r requirements.txt
```

#### Electron ബിൽഡ് പ്രശ്നങ്ങൾ
**പ്രശ്നം:** npm ഇൻസ്റ്റാൾ അല്ലെങ്കിൽ ബിൽഡ് പരാജയങ്ങൾ

**പരിഹാരം:**
```bash
cd Module08/samples/08
# ശുദ്ധമായ ഇൻസ്റ്റാൾ
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### വർക്ക്‌ഫ്ലോ പ്രശ്നങ്ങൾ (ചെറിയത്)

#### വിവർത്തന വർക്ക്‌ഫ്ലോ സംഘർഷങ്ങൾ
**പ്രശ്നം:** വിവർത്തന പുൾ റിക്വസ്റ്റ് നിങ്ങളുടെ മാറ്റങ്ങളുമായി സംഘർഷിക്കുന്നു

**പരിഹാരം:**
- ഇംഗ്ലീഷ് സോഴ്‌സ് ഫയലുകൾ മാത്രം എഡിറ്റ് ചെയ്യുക
- ഓട്ടോമേറ്റഡ് വിവർത്തന വർക്ക്‌ഫ്ലോ വിവർത്തനങ്ങൾ കൈകാര്യം ചെയ്യട്ടെ
- സംഘർഷങ്ങൾ ഉണ്ടെങ്കിൽ, വിവർത്തനങ്ങൾ മർജ് ചെയ്ത ശേഷം `main` ബ്രാഞ്ച് നിങ്ങളുടെ ബ്രാഞ്ചിലേക്ക് മർജ് ചെയ്യുക

#### മോഡൽ ഡൗൺലോഡ് പരാജയങ്ങൾ
**പ്രശ്നം:** Foundry Local മോഡലുകൾ ഡൗൺലോഡ് ചെയ്യാൻ പരാജയപ്പെടുന്നു

**പരിഹാരം:**
```bash
# ഇന്റർനെറ്റ് കണക്ഷൻ പരിശോധിക്കുക
# മോഡൽ കാഷെ ക്ലിയർ ചെയ്ത് വീണ്ടും ശ്രമിക്കുക
foundry model remove <model-alias>
foundry model run <model-alias>

# ലഭ്യമായ ഡിസ്ക് സ്പേസ് പരിശോധിക്കുക (മോഡലുകൾ 2-16GB വരെ ആകാം)
# ഡൗൺലോഡുകൾ അനുവദിക്കുന്നതായി ഫയർവാൾ ക്രമീകരണങ്ങൾ സ്ഥിരീകരിക്കുക
```

## Additional Resources

### പഠന പാതകൾ
- **ആരംഭക പാത:** മോഡ്യൂളുകൾ 01-02 (7-9 മണിക്കൂർ)
- **മധ്യസ്ഥ പാത:** മോഡ്യൂളുകൾ 03-04 (9-11 മണിക്കൂർ)
- **ഉന്നത പാത:** മോഡ്യൂളുകൾ 05-07 (12-15 മണിക്കൂർ)
- **വിദഗ്ധ പാത:** മോഡ്യൂൾ 08 (8-10 മണിക്കൂർ)
- **ഹാൻഡ്‌സ്-ഓൺ വർക്ക്‌ഷോപ്പ്:** വർക്ക്‌ഷോപ്പ് മെറ്റീരിയലുകൾ (6-8 മണിക്കൂർ)

### പ്രധാന മോഡ്യൂൾ ഉള്ളടക്കം
- **Module01:** EdgeAI അടിസ്ഥാനങ്ങൾ, യാഥാർത്ഥ്യ കേസുകൾ
- **Module02:** Small Language Model (SLM) കുടുംബങ്ങളും ആർക്കിടെക്ചറുകളും
- **Module03:** ലോക്കൽ, ക്ലൗഡ് ഡിപ്ലോയ്മെന്റ് തന്ത്രങ്ങൾ
- **Module04:** മോഡൽ ഒപ്റ്റിമൈസേഷൻ വിവിധ ഫ്രെയിംവർക്കുകളുമായി (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - പ്രൊഡക്ഷൻ ഓപ്പറേഷനുകൾ
- **Module06:** AI ഏജന്റുകളും ഫംഗ്ഷൻ കോളിംഗും
- **Module07:** പ്ലാറ്റ്ഫോം-നിർദ്ദിഷ്ട നടപ്പാക്കലുകൾ
- **Module08:** Foundry Local ടൂൾകിറ്റ് 10 സമഗ്ര സാമ്പിളുകളോടെ

### ബാഹ്യ ആശ്രിതങ്ങൾ
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-സമാനമായ API ഉള്ള ലോക്കൽ AI മോഡൽ റൺടൈം
  - [ഡോക്യുമെന്റേഷൻ](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ഒപ്റ്റിമൈസേഷൻ ഫ്രെയിംവർക്ക്
- [Microsoft Olive](https://microsoft.github.io/Olive/) - മോഡൽ ഒപ്റ്റിമൈസേഷൻ ടൂൾകിറ്റ്
- [OpenVINO](https://docs.openvino.ai/) - Intel-ന്റെ ഒപ്റ്റിമൈസേഷൻ ടൂൾകിറ്റ്

## Project-Specific Notes

### Module08 സാമ്പിൾ ആപ്ലിക്കേഷനുകൾ

റിപോസിറ്ററിയിൽ 10 സമഗ്ര സാമ്പിൾ ആപ്ലിക്കേഷനുകൾ ഉൾക്കൊള്ളുന്നു:

1. **01-REST Chat Quickstart** - അടിസ്ഥാന OpenAI SDK ഇന്റഗ്രേഷൻ
2. **02-OpenAI SDK Integration** - പുരോഗമിച്ച SDK ഫീച്ചറുകൾ
3. **03-Model Discovery & Benchmarking** - മോഡൽ താരതമ്യ ഉപകരണങ്ങൾ
4. **04-Chainlit RAG Application** - റിട്രീവൽ-ഓഗ്മെന്റഡ് ജനറേഷൻ
5. **05-Multi-Agent Orchestration** - അടിസ്ഥാന ഏജന്റ് കോർഡിനേഷൻ
6. **06-Models-as-Tools Router** - ബുദ്ധിമുട്ടുള്ള മോഡൽ റൂട്ടിംഗ്
7. **07-Direct API Client** - ലോ-ലെവൽ API ഇന്റഗ്രേഷൻ
8. **08-Windows 11 Chat App** - നേറ്റീവ് Electron ഡെസ്ക്ടോപ്പ് ആപ്ലിക്കേഷൻ
9. **09-Advanced Multi-Agent System** - സങ്കീർണ്ണ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel സംയോജനം

### വർക്‌ഷോപ്പ് സാമ്പിൾ അപ്ലിക്കേഷനുകൾ

വർക്‌ഷോപ്പിൽ പ്രായോഗിക നടപ്പിലാക്കലുകളുള്ള 6 പുരോഗമന സെഷനുകൾ ഉൾപ്പെടുന്നു:

1. **സെഷൻ 01** - Foundry Local സംയോജനത്തോടെ ചാറ്റ് ബൂട്ട്‌സ്റ്റ്രാപ്പ്
2. **സെഷൻ 02** - RAG പൈപ്പ്‌ലൈൻയും RAGAS ഉപയോഗിച്ചുള്ള മൂല്യനിർണയവും
3. **സെഷൻ 03** - ഓപ്പൺ-സോഴ്‌സ് മോഡലുകളുടെ ബെഞ്ച്മാർക്കിംഗ്
4. **സെഷൻ 04** - മോഡൽ താരതമ്യം ചെയ്യലും തിരഞ്ഞെടുപ്പും
5. **സെഷൻ 05** - മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ സിസ്റ്റങ്ങൾ
6. **സെഷൻ 06** - മോഡൽ റൂട്ടിംഗ്‌വും പൈപ്പ്‌ലൈൻ മാനേജ്മെന്റും

Foundry Local ഉപയോഗിച്ച് എഡ്ജ് AI വികസനത്തിന്റെ വ്യത്യസ്ത വശങ്ങൾ ഓരോ സാമ്പിളും പ്രദർശിപ്പിക്കുന്നു.

### പ്രകടന പരിഗണനകൾ

- SLMകൾ എഡ്ജ് ഡിപ്ലോയ്മെന്റിനായി (2-16GB RAM) ഒപ്റ്റിമൈസ് ചെയ്തിരിക്കുന്നു
- ലോക്കൽ ഇൻഫറൻസ് 50-500ms പ്രതികരണ സമയം നൽകുന്നു
- ക്വാണ്ടൈസേഷൻ സാങ്കേതികവിദ്യകൾ 75% വലിപ്പം കുറയ്ക്കുകയും 85% പ്രകടനം നിലനിർത്തുകയും ചെയ്യുന്നു
- ലോക്കൽ മോഡലുകളുമായി റിയൽ-ടൈം സംഭാഷണ ശേഷി

### സുരക്ഷയും സ്വകാര്യതയും

- എല്ലാ പ്രോസസ്സിംഗും ലോക്കലായി നടക്കുന്നു - ക്ലൗഡിലേക്ക് ഡാറ്റ അയയ്ക്കുന്നില്ല
- സ്വകാര്യതാ-സെൻസിറ്റീവ് അപ്ലിക്കേഷനുകൾക്ക് അനുയോജ്യം (ആരോഗ്യം, ധനകാര്യ)
- ഡാറ്റ സോവർൻറിറ്റി ആവശ്യകതകൾ പാലിക്കുന്നു
- Foundry Local പൂർണ്ണമായും ലോക്കൽ ഹാർഡ്‌വെയറിൽ പ്രവർത്തിക്കുന്നു

## സഹായം നേടുക

### ഡോക്യുമെന്റേഷൻ

- **പ്രധാന README**: [README.md](README.md) - റിപോസിറ്ററി അവലോകനവും പഠന പാതകളും
- **സ്റ്റഡി ഗൈഡ്**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - പഠന വിഭവങ്ങളും സമയരേഖയും
- **സപ്പോർട്ട്**: [SUPPORT.md](SUPPORT.md) - സഹായം എങ്ങനെ നേടാം
- **സുരക്ഷ**: [SECURITY.md](SECURITY.md) - സുരക്ഷാ പ്രശ്നങ്ങൾ റിപ്പോർട്ട് ചെയ്യുക

### കമ്മ്യൂണിറ്റി സപ്പോർട്ട്

- **GitHub Issues**: [ബഗുകൾ റിപ്പോർട്ട് ചെയ്യുക അല്ലെങ്കിൽ ഫീച്ചറുകൾ അഭ്യർത്ഥിക്കുക](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [ചോദ്യങ്ങൾ ചോദിക്കുക, ആശയങ്ങൾ പങ്കുവെക്കുക](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local-ന്റെ സാങ്കേതിക പ്രശ്നങ്ങൾ](https://github.com/microsoft/Foundry-Local/issues)

### ബന്ധപ്പെടുക

- **മെന്റെയ്‌നർമാർ**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) കാണുക
- **സുരക്ഷാ പ്രശ്നങ്ങൾ**: [SECURITY.md](SECURITY.md) ൽ ഉത്തരവാദിത്വമുള്ള വെളിപ്പെടുത്തൽ പാലിക്കുക
- **Microsoft Support**: എന്റർപ്രൈസ് സപ്പോർട്ടിനായി Microsoft കസ്റ്റമർ സർവീസ് ബന്ധപ്പെടുക

### അധിക വിഭവങ്ങൾ

- **Microsoft Learn**: [AI and Machine Learning Learning Paths](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ഡോക്യുമെന്റേഷൻ**: [അധികൃത ഡോക്സ്](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **കമ്മ്യൂണിറ്റി സാമ്പിളുകൾ**: കമ്മ്യൂണിറ്റി സംഭാവനകൾക്കായി [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) പരിശോധിക്കുക

---

**ഇത് എഡ്ജ് AI വികസനം പഠിപ്പിക്കുന്നതിനുള്ള ഒരു വിദ്യാഭ്യാസ റിപോസിറ്ററിയാണ്. പ്രധാന സംഭാവനാ മാതൃക വിദ്യാഭ്യാസ ഉള്ളടക്കം മെച്ചപ്പെടുത്തലും എഡ്ജ് AI ആശയങ്ങൾ പ്രദർശിപ്പിക്കുന്ന സാമ്പിൾ അപ്ലിക്കേഷനുകൾ ചേർക്കലും മെച്ചപ്പെടുത്തലും ആണ്.**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->