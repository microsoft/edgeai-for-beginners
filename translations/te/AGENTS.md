<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-12-15T17:02:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "te"
}
-->
# AGENTS.md

> **ఆరంభదారుల కోసం EdgeAI కి సహకరించడానికి డెవలపర్ గైడ్**
> 
> ఈ డాక్యుమెంట్ ఈ రిపోజిటరీతో పని చేసే డెవలపర్లు, AI ఏజెంట్లు మరియు సహకారదారులకు సమగ్ర సమాచారం అందిస్తుంది. ఇది సెటప్, అభివృద్ధి వర్క్‌ఫ్లోలు, పరీక్షలు మరియు ఉత్తమ పద్ధతులను కవర్ చేస్తుంది.
> 
> **చివరిసారిగా నవీకరించబడింది**: అక్టోబర్ 30, 2025 | **డాక్యుమెంట్ వెర్షన్**: 3.0

## Table of Contents

- [ప్రాజెక్ట్ అవలోకనం](../..)
- [రిపోజిటరీ నిర్మాణం](../..)
- [ముందస్తు అవసరాలు](../..)
- [సెట్టప్ కమాండ్లు](../..)
- [అభివృద్ధి వర్క్‌ఫ్లో](../..)
- [పరీక్షా సూచనలు](../..)
- [కోడ్ శైలి మార్గదర్శకాలు](../..)
- [పుల్ రిక్వెస్ట్ మార్గదర్శకాలు](../..)
- [అనువాద వ్యవస్థ](../..)
- [Foundry Local ఇంటిగ్రేషన్](../..)
- [బిల్డ్ మరియు డిప్లాయ్‌మెంట్](../..)
- [సాధారణ సమస్యలు మరియు సమస్య పరిష్కారం](../..)
- [అదనపు వనరులు](../..)
- [ప్రాజెక్ట్-స్పెసిఫిక్ నోట్స్](../..)
- [సహాయం పొందడం](../..)

## Project Overview

EdgeAI for Beginners అనేది Small Language Models (SLMs) తో Edge AI అభివృద్ధిని బోధించే సమగ్ర విద్యా రిపోజిటరీ. ఈ కోర్సు EdgeAI ప్రాథమికాలు, మోడల్ డిప్లాయ్‌మెంట్, ఆప్టిమైజేషన్ సాంకేతికతలు మరియు Microsoft Foundry Local మరియు వివిధ AI ఫ్రేమ్‌వర్క్‌లను ఉపయోగించి ప్రొడక్షన్-రెడీ అమలు విధానాలను కవర్ చేస్తుంది.

**ప్రధాన సాంకేతికతలు:**
- Python 3.8+ (AI/ML నమూనాల కోసం ప్రాథమిక భాష)
- .NET C# (AI/ML నమూనాలు)
- JavaScript/Node.js తో Electron (డెస్క్‌టాప్ అప్లికేషన్ల కోసం)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ఫ్రేమ్‌వర్క్‌లు: LangChain, Semantic Kernel, Chainlit
- మోడల్ ఆప్టిమైజేషన్: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**రిపోజిటరీ రకం:** 8 మాడ్యూల్స్ మరియు 10 సమగ్ర నమూనా అప్లికేషన్లతో విద్యా కంటెంట్ రిపోజిటరీ

**ఆర్కిటెక్చర్:** ఎడ్జ్ AI డిప్లాయ్‌మెంట్ నమూనాలను ప్రదర్శించే బహుమాడ్యూల్ లెర్నింగ్ పాత్ మరియు ప్రాక్టికల్ నమూనాలు

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

### Required Tools

- **Python 3.8+** - AI/ML నమూనాలు మరియు నోట్‌బుక్స్ కోసం
- **Node.js 16+** - Electron నమూనా అప్లికేషన్ కోసం
- **Git** - వెర్షన్ కంట్రోల్ కోసం
- **Microsoft Foundry Local** - AI మోడల్స్ స్థానికంగా నడపడానికి

### Recommended Tools

- **Visual Studio Code** - Python, Jupyter, మరియు Pylance ఎక్స్‌టెన్షన్లతో
- **Windows Terminal** - మెరుగైన కమాండ్-లైన్ అనుభవం కోసం (Windows వినియోగదారులు)
- **Docker** - కంటైనరైజ్డ్ అభివృద్ధి కోసం (ఐచ్ఛికం)

### System Requirements

- **RAM**: కనీసం 8GB, బహుమోడల్ సన్నివేశాల కోసం 16GB+ సిఫార్సు
- **స్టోరేజ్**: మోడల్స్ మరియు డిపెండెన్సీల కోసం 10GB+ ఖాళీ స్థలం
- **OS**: Windows 10/11, macOS 11+, లేదా Linux (Ubuntu 20.04+)
- **హార్డ్‌వేర్**: AVX2 మద్దతు ఉన్న CPU; GPU (CUDA, Qualcomm NPU) ఐచ్ఛికం కానీ సిఫార్సు చేయబడింది

### Knowledge Prerequisites

- Python ప్రోగ్రామింగ్ ప్రాథమిక అవగాహన
- కమాండ్-లైన్ ఇంటర్‌ఫేస్‌ల పరిచయం
- AI/ML కాన్సెప్ట్‌ల అవగాహన (నమూనా అభివృద్ధి కోసం)
- Git వర్క్‌ఫ్లోలు మరియు పుల్ రిక్వెస్ట్ ప్రక్రియలు

## Setup Commands

### Repository Setup

```bash
# రిపోజిటరీని క్లోన్ చేయండి
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# ఎలాంటి బిల్డ్ దశ అవసరం లేదు - ఇది ప్రధానంగా విద్యా విషయాల రిపోజిటరీ మాత్రమే
```

### Python Sample Setup (Module08 and Workshop samples)

```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి యాక్టివేట్ చేయండి
python -m venv .venv
# విండోస్‌లో
.venv\Scripts\activate
# మాక్‌ఓఎస్/లినక్స్‌లో
source .venv/bin/activate

# ఫౌండ్రీ లోకల్ SDK మరియు ఆధారాలను ఇన్‌స్టాల్ చేయండి
pip install foundry-local-sdk openai

# Module08 నమూనాల కోసం అదనపు ఆధారాలను ఇన్‌స్టాల్ చేయండి
cd Module08
pip install -r requirements.txt

# వర్క్‌షాప్ ఆధారాలను ఇన్‌స్టాల్ చేయండి
cd ../Workshop
pip install -r requirements.txt
```

### Node.js Sample Setup (Sample 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# అభివృద్ధి మోడ్‌లో ప్రారంభించండి
npm run dev

# ఉత్పత్తి కోసం నిర్మించండి
npm run build

# ఇన్‌స్టాలర్ సృష్టించండి
npm run dist
```

### Foundry Local Setup

Foundry Local నమూనాలను నడపడానికి అవసరం. అధికారిక రిపోజిటరీ నుండి డౌన్లోడ్ చేసి ఇన్‌స్టాల్ చేయండి:

**ఇన్‌స్టాలేషన్:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **మాన్యువల్**: [రిలీజెస్ పేజీ](https://github.com/microsoft/Foundry-Local/releases) నుండి డౌన్లోడ్ చేయండి

**త్వరిత ప్రారంభం:**
```bash
# మీ మొదటి మోడల్‌ను నడపండి (అవసరమైతే ఆటో-డౌన్లోడ్ అవుతుంది)
foundry model run phi-4-mini

# అందుబాటులో ఉన్న మోడల్స్ జాబితా
foundry model ls

# సేవ స్థితిని తనిఖీ చేయండి
foundry service status
```

**గమనిక**: Foundry Local మీ హార్డ్‌వేర్ (CUDA GPU, Qualcomm NPU, లేదా CPU) కోసం ఉత్తమ మోడల్ వేరియంట్‌ను ఆటోమేటిక్‌గా ఎంచుకుంటుంది.

## Development Workflow

### Content Development

ఈ రిపోజిటరీ ప్రధానంగా **Markdown విద్యా కంటెంట్** కలిగి ఉంది. మార్పులు చేయేటప్పుడు:

1. సంబంధిత మాడ్యూల్ డైరెక్టరీలలో `.md` ఫైళ్లను ఎడిట్ చేయండి
2. ఉన్న ఫార్మాటింగ్ నమూనాలను అనుసరించండి
3. కోడ్ ఉదాహరణలు ఖచ్చితంగా మరియు పరీక్షించబడినవి కావాలి
4. అవసరమైతే అనువాద కంటెంట్‌ను నవీకరించండి (లేదా ఆటోమేషన్‌కు అనుమతించండి)

### Sample Application Development

Module08 Python నమూనాల కోసం (నమూనాలు 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python నమూనాల కోసం:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron నమూనా (నమూనా 08) కోసం:
```bash
cd Module08/samples/08
npm run dev  # హాట్ రీలోడ్‌తో అభివృద్ధి
```

### Testing Sample Applications

Python నమూనాలకు ఆటోమేటెడ్ పరీక్షలు లేవు కానీ వాటిని నడిపి ధృవీకరించవచ్చు:
```bash
# ప్రాథమిక చాట్ ఫంక్షనాలిటీని పరీక్షించండి
python samples/01/chat_quickstart.py "Hello"

# నిర్దిష్ట మోడల్‌తో పరీక్షించండి
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron నమూనాకు పరీక్షా మౌలిక సదుపాయం ఉంది:
```bash
cd Module08/samples/08
npm test           # యూనిట్ పరీక్షలను నడపండి
npm run test:e2e   # ఎండ్-టు-ఎండ్ పరీక్షలను నడపండి
npm run lint       # కోడ్ శైలిని తనిఖీ చేయండి
```

## Testing Instructions

### Content Validation

రిపోజిటరీ ఆటోమేటెడ్ అనువాద వర్క్‌ఫ్లోలను ఉపయోగిస్తుంది. అనువాదాల కోసం మాన్యువల్ పరీక్ష అవసరం లేదు.

**కంటెంట్ మార్పుల కోసం మాన్యువల్ ధృవీకరణ:**
1. `.md` ఫైళ్లను ప్రివ్యూ చేసి Markdown రెండరింగ్‌ను సమీక్షించండి
2. అన్ని లింకులు సరైన లక్ష్యాలను సూచిస్తున్నాయో తనిఖీ చేయండి
3. డాక్యుమెంటేషన్‌లో ఉన్న కోడ్ స్నిపెట్లను పరీక్షించండి
4. చిత్రాలు సరిగ్గా లోడ్ అవుతున్నాయో తనిఖీ చేయండి

### Sample Application Testing

**Module08/samples/08 (Electron యాప్) కు సమగ్ర పరీక్ష ఉంది:**
```bash
cd Module08/samples/08

# అన్ని పరీక్షలను నడపండి
npm test

# యూనిట్ పరీక్షలను మాత్రమే నడపండి
npm test -- --testPathPattern=unit

# ఇంటిగ్రేషన్ పరీక్షలను నడపండి
npm run test:integration

# E2E పరీక్షలను నడపండి
npm run test:e2e

# పరీక్ష కవరేజ్‌ను తనిఖీ చేయండి
npm test -- --coverage
```

**Python నమూనాలను మాన్యువల్‌గా పరీక్షించాలి:**
```bash
# మాడ్యూల్08 నమూనాలు
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# వర్క్‌షాప్ నమూనాలు
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# వర్క్‌షాప్ ధృవీకరణ సాధనాలను ఉపయోగించండి
cd Workshop/scripts
python validate_samples.py  # సింటాక్స్ మరియు దిగుమతులను ధృవీకరించండి
python test_samples.py      # స్మోక్ పరీక్షలను నిర్వహించండి
```

## Code Style Guidelines

### Markdown Content

- స్థిరమైన హెడ్డింగ్ హైరార్కీ ఉపయోగించండి (# శీర్షిక కోసం, ## ప్రధాన విభాగాల కోసం, ### ఉపవిభాగాల కోసం)
- భాషా స్పెసిఫైయర్లతో కోడ్ బ్లాక్స్ చేర్చండి: ```python, ```bash, ```javascript
- పట్టికలు, జాబితాలు, మరియు ఎమ్ఫసిస్ కోసం ఉన్న ఫార్మాటింగ్‌ను అనుసరించండి
- పంక్తులు చదవదగినవిగా ఉంచండి (~80-100 అక్షరాలు లక్ష్యం, కానీ కఠినంగా కాదు)
- అంతర్గత సూచనల కోసం రిలేటివ్ లింకులు ఉపయోగించండి

### Python Code Style

- PEP 8 నియమాలను అనుసరించండి
- అవసరమైన చోట టైప్ హింట్స్ ఉపయోగించండి
- ఫంక్షన్లు మరియు క్లాసుల కోసం డాక్స్ట్రింగ్స్ చేర్చండి
- అర్థవంతమైన వేరియబుల్ పేర్లను ఉపయోగించండి
- ఫంక్షన్లు ఫోకస్ చేయబడినవి మరియు సంక్షిప్తంగా ఉంచండి

### JavaScript/Node.js Code Style

```bash
# ఎలక్ట్రాన్ నమూనా ESLint కాన్ఫిగరేషన్‌ను అనుసరిస్తుంది
cd Module08/samples/08
npm run lint        # శైలి సమస్యలను తనిఖీ చేయండి
npm run lint:fix    # శైలి సమస్యలను ఆటో-ఫిక్స్ చేయండి
npm run format      # Prettier తో ఫార్మాట్ చేయండి
```

**ప్రధాన నియమాలు:**
- నమూనా 08 లో ESLint కాన్ఫిగరేషన్ అందించబడింది
- కోడ్ ఫార్మాటింగ్ కోసం Prettier ఉపయోగించండి
- ఆధునిక ES6+ సింటాక్స్ ఉపయోగించండి
- కోడ్‌బేస్‌లో ఉన్న నమూనాలను అనుసరించండి

## Pull Request Guidelines

### Contribution Workflow

1. **రిపోజిటరీని ఫోర్క్ చేసి** `main` నుండి కొత్త బ్రాంచ్ సృష్టించండి
2. **మీ మార్పులను చేయండి** కోడ్ శైలి మార్గదర్శకాలను అనుసరించి
3. **పూర్తిగా పరీక్షించండి** పై పరీక్షా సూచనలను ఉపయోగించి
4. **స్పష్టమైన సందేశాలతో కమిట్ చేయండి** కన్వెన్షనల్ కమిట్స్ ఫార్మాట్ అనుసరించి
5. **మీ ఫోర్క్‌కు పుష్ చేసి** పుల్ రిక్వెస్ట్ సృష్టించండి
6. **సమీక్ష సమయంలో నిర్వహకుల అభిప్రాయాలకు స్పందించండి**

### Branch Naming Convention

- `feature/<module>-<description>` - కొత్త ఫీచర్లు లేదా కంటెంట్ కోసం
- `fix/<module>-<description>` - బగ్ ఫిక్సుల కోసం
- `docs/<description>` - డాక్యుమెంటేషన్ మెరుగుదలల కోసం
- `refactor/<description>` - కోడ్ రిఫాక్టరింగ్ కోసం

### Commit Message Format

[Conventional Commits](https://www.conventionalcommits.org/) ను అనుసరించండి:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ఉదాహరణలు:**
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

అన్ని సహకారదారులు [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ను అనుసరించాలి. దయచేసి సహకరించే ముందు [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ను సమీక్షించండి.

### Before Submitting

**కంటెంట్ మార్పుల కోసం:**
- అన్ని మార్చిన Markdown ఫైళ్లను ప్రివ్యూ చేయండి
- లింకులు మరియు చిత్రాలు పనిచేస్తున్నాయో తనిఖీ చేయండి
- టైపోస్ మరియు వ్యాకరణ తప్పుల కోసం తనిఖీ చేయండి

**సాంపిల్ కోడ్ మార్పుల కోసం (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python సాంపిల్ మార్పుల కోసం:**
- నమూనా విజయవంతంగా నడుస్తుందో పరీక్షించండి
- లోపాల నిర్వహణ పనిచేస్తుందో తనిఖీ చేయండి
- Foundry Local తో అనుకూలతను తనిఖీ చేయండి

### Review Process

- విద్యా కంటెంట్ మార్పులు ఖచ్చితత్వం మరియు స్పష్టత కోసం సమీక్షించబడతాయి
- కోడ్ నమూనాలు ఫంక్షనాలిటీ కోసం పరీక్షించబడతాయి
- అనువాద నవీకరణలు GitHub Actions ద్వారా ఆటోమేటిక్‌గా నిర్వహించబడతాయి

## Translation System

**ముఖ్యమైనది:** ఈ రిపోజిటరీ ఆటోమేటెడ్ అనువాదం కోసం GitHub Actions ఉపయోగిస్తుంది.

- అనువాదాలు `/translations/` డైరెక్టరీలో ఉన్నాయి (50+ భాషలు)
- `co-op-translator.yml` వర్క్‌ఫ్లో ద్వారా ఆటోమేటెడ్
- **అనువాద ఫైళ్లను మాన్యువల్‌గా ఎడిట్ చేయవద్దు** - అవి తిరిగి రాయబడతాయి
- రూట్ మరియు మాడ్యూల్ డైరెక్టరీలలోని ఇంగ్లీష్ మూల ఫైళ్లను మాత్రమే ఎడిట్ చేయండి
- అనువాదాలు `main` బ్రాంచ్‌కు పుష్ చేసినప్పుడు ఆటోమేటిక్‌గా ఉత్పత్తి అవుతాయి

## Foundry Local Integration

అధిక భాగం Module08 నమూనాలు Microsoft Foundry Local నడుస్తున్నదని అవసరం.

### Installation & Setup

**Foundry Local ఇన్‌స్టాల్ చేయండి:**
```bash
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్‌ఓఎస్
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ఇన్‌స్టాల్ చేయండి:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ప్రారంభించడం
```bash
# సేవ ప్రారంభించి మోడల్‌ను నడపండి (అవసరమైతే ఆటో-డౌన్లోడ్ అవుతుంది)
foundry model run phi-3.5-mini

# లేదా ఆటోమేటిక్ హార్డ్‌వేర్ ఆప్టిమైజేషన్ కోసం మోడల్ అలియాసెస్ ఉపయోగించండి
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# సేవ స్థితిని తనిఖీ చేయండి
foundry service status

# అందుబాటులో ఉన్న మోడల్స్ జాబితా చేయండి
foundry model ls
```

### SDK ఉపయోగం (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# ఆటోమేటిక్ హార్డ్‌వేర్ ఆప్టిమైజేషన్ కోసం మోడల్ అలియాస్ ఉపయోగించండి
alias = "phi-4-mini"

# మేనేజర్ సృష్టించండి (సేవను ఆటోమేటిక్‌గా ప్రారంభించి మోడల్‌ను లోడ్ చేస్తుంది)
manager = FoundryLocalManager(alias)

# లోకల్ ఫౌండ్రీ సేవ కోసం OpenAI క్లయింట్‌ను కాన్ఫిగర్ చేయండి
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# మోడల్‌ను ఉపయోగించండి
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local ధృవీకరణ
```bash
# సేవ స్థితి మరియు ఎండ్‌పాయింట్
foundry service status

# లోడ్ చేసిన మోడల్స్ జాబితా (REST API)
curl http://localhost:<port>/v1/models

# గమనిక: 'foundry service status' నడుపుతున్నప్పుడు పోర్ట్ ప్రదర్శించబడుతుంది
```

### నమూనాల కోసం ఎన్విరాన్‌మెంట్ వేరియబుల్స్

అధిక నమూనాలు ఈ ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ఉపయోగిస్తాయి:
```bash
# ఫౌండ్రీ లోకల్ కాన్ఫిగరేషన్
# గమనిక: SDK (FoundryLocalManager) ఆటోమేటిక్‌గా ఎండ్‌పాయింట్‌ను గుర్తిస్తుంది
set MODEL=phi-4-mini  # లేదా phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # లోకల్ ఉపయోగానికి అవసరం లేదు

# మాన్యువల్ ఎండ్‌పాయింట్ (SDK ఉపయోగించకపోతే)
# పోర్ట్ 'foundry service status' ద్వారా చూపబడుతుంది
set BASE_URL=http://localhost:<port>

# Azure OpenAI ఫాల్బ్యాక్ కోసం (ఐచ్ఛికం)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**గమనిక**: `FoundryLocalManager` ఉపయోగించినప్పుడు, SDK ఆటోమేటిక్‌గా సర్వీస్ డిస్కవరీ మరియు మోడల్ లోడింగ్ నిర్వహిస్తుంది. మోడల్ అలియాసులు (ఉదా: `phi-3.5-mini`) మీ హార్డ్‌వేర్‌కు ఉత్తమ వేరియంట్ ఎంచుకోవడాన్ని నిర్ధారిస్తాయి.

## Build and Deployment

### Content Deployment

ఈ రిపోజిటరీ ప్రధానంగా డాక్యుమెంటేషన్ - కంటెంట్ కోసం బిల్డ్ ప్రాసెస్ అవసరం లేదు.

### Sample Application Building

**Electron అప్లికేషన్ (Module08/samples/08):**
```bash
cd Module08/samples/08

# అభివృద్ధి బిల్డ్
npm run dev

# ఉత్పత్తి బిల్డ్
npm run build

# విండోస్ ఇన్‌స్టాలర్ సృష్టించండి
npm run dist

# పోర్టబుల్ ఎగ్జిక్యూటబుల్ సృష్టించండి
npm run pack
```

**Python నమూనాలు:**
బిల్డ్ ప్రాసెస్ లేదు - నమూనాలు నేరుగా Python ఇంటర్‌ప్రెటర్‌తో నడుస్తాయి.

## Common Issues and Troubleshooting

> **సూచన**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) లో తెలిసిన సమస్యలు మరియు పరిష్కారాలను తనిఖీ చేయండి.

### Critical Issues (Blocking)

#### Foundry Local నడవడం లేదు
**సమస్య:** నమూనాలు కనెక్షన్ లోపాలతో విఫలమవుతాయి

**పరిష్కారం:**
```bash
# సర్వీస్ నడుస్తుందో లేదో తనిఖీ చేయండి
foundry service status

# ఒక మోడల్‌తో సర్వీస్ ప్రారంభించండి
foundry model run phi-4-mini

# లేదా స్పష్టంగా సర్వీస్ ప్రారంభించండి
foundry service start

# లోడ్ చేసిన మోడల్స్ జాబితా చేయండి
foundry model ls

# REST API ద్వారా ధృవీకరించండి ('foundry service status'లో పోర్ట్ చూపబడింది)
curl http://localhost:<port>/v1/models
```

### Common Issues (Moderate)

#### Python వర్చువల్ ఎన్విరాన్‌మెంట్ సమస్యలు
**సమస్య:** మాడ్యూల్ ఇంపోర్ట్ లోపాలు

**పరిష్కారం:**
```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సక్రియమై ఉందని నిర్ధారించుకోండి
# విండోస్
.venv\Scripts\activate
# మాక్OS/లినక్స్
source .venv/bin/activate

# ఆధారాలను మళ్లీ ఇన్‌స్టాల్ చేయండి
pip install -r requirements.txt
```

#### Electron బిల్డ్ సమస్యలు
**సమస్య:** npm ఇన్‌స్టాల్ లేదా బిల్డ్ విఫలమవుతుంది

**పరిష్కారం:**
```bash
cd Module08/samples/08
# శుభ్రమైన ఇన్‌స్టాల్
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflow Issues (Minor)

#### అనువాద వర్క్‌ఫ్లో ఘర్షణలు
**సమస్య:** అనువాద పుల్ రిక్వెస్ట్ మీ మార్పులతో ఘర్షణ చెందుతుంది

**పరిష్కారం:**
- ఇంగ్లీష్ మూల ఫైళ్లను మాత్రమే ఎడిట్ చేయండి
- ఆటోమేటెడ్ అనువాద వర్క్‌ఫ్లో అనువాదాలను నిర్వహించనివ్వండి
- ఘర్షణలు సంభవిస్తే, అనువాదాలు విలీనం అయిన తర్వాత `main` ను మీ బ్రాంచ్‌లో విలీనం చేయండి

#### మోడల్ డౌన్లోడ్ విఫలమవుతుంది
**సమస్య:** Foundry Local మోడల్స్ డౌన్లోడ్ చేయడంలో విఫలమవుతుంది

**పరిష్కారం:**
```bash
# ఇంటర్నెట్ కనెక్టివిటీని తనిఖీ చేయండి
# మోడల్ క్యాషేను క్లియర్ చేసి మళ్లీ ప్రయత్నించండి
foundry model remove <model-alias>
foundry model run <model-alias>

# అందుబాటులో ఉన్న డిస్క్ స్థలాన్ని తనిఖీ చేయండి (మోడల్స్ 2-16GB ఉండవచ్చు)
# డౌన్లోడ్లకు ఫైర్వాల్ సెట్టింగ్స్ అనుమతిస్తున్నాయో లేదో నిర్ధారించండి
```

## Additional Resources

### Learning Paths
- **ఆరంభదారుల పాత్:** మాడ్యూల్స్ 01-02 (7-9 గంటలు)
- **మధ్యస్థ పాత్:** మాడ్యూల్స్ 03-04 (9-11 గంటలు)
- **అధునాతన పాత్:** మాడ్యూల్స్ 05-07 (12-15 గంటలు)
- **నిపుణుల పాత్:** మాడ్యూల్ 08 (8-10 గంటలు)
- **హ్యాండ్స్-ఆన్ వర్క్‌షాప్:** వర్క్‌షాప్ మెటీరియల్స్ (6-8 గంటలు)

### Key Module Content
- **Module01:** EdgeAI ప్రాథమికాలు మరియు వాస్తవ ప్రపంచ కేస్ స్టడీస్
- **Module02:** Small Language Model (SLM) కుటుంబాలు మరియు ఆర్కిటెక్చర్లు
- **Module03:** స్థానిక మరియు క్లౌడ్ డిప్లాయ్‌మెంట్ వ్యూహాలు
- **Module04:** బహుళ ఫ్రేమ్‌వర్క్‌లతో మోడల్ ఆప్టిమైజేషన్ (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - ప్రొడక్షన్ ఆపరేషన్స్
- **Module06:** AI ఏజెంట్లు మరియు ఫంక్షన్ కాలింగ్
- **Module07:** ప్లాట్‌ఫారమ్-స్పెసిఫిక్ అమలు
- **Module08:** Foundry Local టూల్‌కిట్ తో 10 సమగ్ర నమూనాలు

### External Dependencies
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-అనుకూల API తో స్థానిక AI మోడల్ రన్‌టైమ్
  - [డాక్యుమెంటేషన్](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ఆప్టిమైజేషన్ ఫ్రేమ్‌వర్క్
- [Microsoft Olive](https://microsoft.github.io/Olive/) - మోడల్ ఆప్టిమైజేషన్ టూల్‌కిట్
- [OpenVINO](https://docs.openvino.ai/) - Intel ఆప్టిమైజేషన్ టూల్‌కిట్

## Project-Specific Notes

### Module08 Sample Applications

రిపోజిటరీ 10 సమగ్ర నమూనా అప్లికేషన్లను కలిగి ఉంది:

1. **01-REST చాట్ క్విక్‌స్టార్ట్** - ప్రాథమిక OpenAI SDK ఇంటిగ్రేషన్
2. **02-OpenAI SDK ఇంటిగ్రేషన్** - అధునాతన SDK ఫీచర్లు
3. **03-మోడల్ డిస్కవరీ & బెంచ్‌మార్కింగ్** - మోడల్ పోలిక టూల్స్
4. **04-Chainlit RAG అప్లికేషన్** - రిట్రీవల్-ఆగ్మెంటెడ్ జనరేషన్
5. **05-మల్టీ-ఏజెంట్ ఆర్కెస్ట్రేషన్** - ప్రాథమిక ఏజెంట్ సమన్వయం
6. **06-మోడల్స్-అస్-టూల్స్ రౌటర్** - తెలివైన మోడల్ రౌటింగ్
7. **07-డైరెక్ట్ API క్లయింట్** - లో-లెవల్ API ఇంటిగ్రేషన్
8. **08-Windows 11 చాట్ యాప్** - స్థానిక Electron డెస్క్‌టాప్ అప్లికేషన్
9. **09-అధునాతన మల్టీ-ఏజెంట్ సిస్టమ్** - సంక్లిష్ట ఏజెంట్ ఆర్కెస్ట్రేషన్
10. **10-Foundry టూల్స్ ఫ్రేమ్‌వర్క్** - LangChain/Semantic Kernel సమీకరణ

### వర్క్‌షాప్ నమూనా అనువర్తనాలు

వర్క్‌షాప్‌లో 6 ప్రగతిశీల సెషన్లు ఉన్నాయి, అవి ప్రాక్టికల్ అమలులతో కూడుకున్నవి:

1. **సెషన్ 01** - Foundry Local సమీకరణతో చాట్ బూట్‌స్ట్రాప్
2. **సెషన్ 02** - RAG పైప్‌లైన్ మరియు RAGAS తో మూల్యాంకనం
3. **సెషన్ 03** - ఓపెన్-సోర్స్ మోడల్స్ బెంచ్‌మార్కింగ్
4. **సెషన్ 04** - మోడల్ తులన మరియు ఎంపిక
5. **సెషన్ 05** - బహుళ-ఏజెంట్ ఆర్కెస్ట్రేషన్ సిస్టమ్స్
6. **సెషన్ 06** - మోడల్ రౌటింగ్ మరియు పైప్‌లైన్ నిర్వహణ

ప్రతి నమూనా Foundry Local తో ఎడ్జ్ AI అభివృద్ధి యొక్క వేర్వేరు అంశాలను ప్రదర్శిస్తుంది.

### పనితీరు పరిగణనలు

- SLMలు ఎడ్జ్ డిప్లాయ్‌మెంట్ కోసం ఆప్టిమైజ్ చేయబడ్డాయి (2-16GB RAM)
- లోకల్ ఇన్ఫరెన్స్ 50-500ms స్పందన సమయాలను అందిస్తుంది
- క్వాంటైజేషన్ సాంకేతికతలు 75% పరిమాణ తగ్గింపుతో 85% పనితీరు నిలుపుదల సాధిస్తాయి
- లోకల్ మోడల్స్ తో రియల్-టైమ్ సంభాషణ సామర్థ్యాలు

### భద్రత మరియు గోప్యత

- అన్ని ప్రాసెసింగ్ లోకల్‌గా జరుగుతుంది - డేటా క్లౌడ్‌కు పంపబడదు
- గోప్యత-సున్నితమైన అనువర్తనాలకు అనుకూలం (ఆరోగ్యం, ఆర్థికం)
- డేటా సార్వభౌమత్వ అవసరాలను తీర్చుతుంది
- Foundry Local పూర్తిగా లోకల్ హార్డ్‌వేర్‌పై నడుస్తుంది

## సహాయం పొందడం

### డాక్యుమెంటేషన్

- **ప్రధాన README**: [README.md](README.md) - రిపోజిటరీ అవలోకనం మరియు నేర్చుకునే మార్గాలు
- **స్టడీ గైడ్**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - నేర్చుకునే వనరులు మరియు టైమ్‌లైన్
- **సపోర్ట్**: [SUPPORT.md](SUPPORT.md) - సహాయం పొందే విధానం
- **భద్రత**: [SECURITY.md](SECURITY.md) - భద్రతా సమస్యలు నివేదించడం

### కమ్యూనిటీ సపోర్ట్

- **GitHub Issues**: [బగ్స్ నివేదించండి లేదా ఫీచర్లను అభ్యర్థించండి](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [ప్రశ్నలు అడగండి మరియు ఆలోచనలు పంచుకోండి](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local సాంకేతిక సమస్యలు](https://github.com/microsoft/Foundry-Local/issues)

### సంప్రదింపు

- **నిర్వాహకులు**: చూడండి [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **భద్రతా సమస్యలు**: [SECURITY.md](SECURITY.md) లో బాధ్యతాయుతమైన వెల్లడింపును అనుసరించండి
- **Microsoft సపోర్ట్**: ఎంటర్‌ప్రైజ్ సపోర్ట్ కోసం Microsoft కస్టమర్ సర్వీస్‌ను సంప్రదించండి

### అదనపు వనరులు

- **Microsoft Learn**: [AI మరియు మెషీన్ లెర్నింగ్ నేర్చుకునే మార్గాలు](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local డాక్యుమెంటేషన్**: [అధికారిక డాక్స్](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **కమ్యూనిటీ నమూనాలు**: కమ్యూనిటీ కాంట్రిబ్యూషన్స్ కోసం [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) చూడండి

---

**ఇది ఎడ్జ్ AI అభివృద్ధి నేర్పడంపై దృష్టి పెట్టిన విద్యా రిపోజిటరీ. ప్రాథమిక కాంట్రిబ్యూషన్ నమూనా విద్యా కంటెంట్ మెరుగుపరచడం మరియు ఎడ్జ్ AI కాన్సెప్ట్‌లను ప్రదర్శించే నమూనా అనువర్తనాలను జోడించడం/పెంపొందించడం.**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->