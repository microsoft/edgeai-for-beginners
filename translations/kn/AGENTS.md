# AGENTS.md

> **ಆರಂಭಿಕರಿಗಾಗಿ EdgeAI ಗೆ ಕೊಡುಗೆ ನೀಡುವ ಡೆವಲಪರ್ ಮಾರ್ಗದರ್ಶಿ**
> 
> ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಈ ರೆಪೊಸಿಟರಿಯೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುವ ಡೆವಲಪರ್‌ಗಳು, AI ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಕೊಡುಗೆದಾರರಿಗೆ ಸಮಗ್ರ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು ಸೆಟಪ್, ಅಭಿವೃದ್ಧಿ ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಪರೀಕ್ಷೆ ಮತ್ತು ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.
> 
> **ಕೊನೆಯದಾಗಿ ನವೀಕರಿಸಲಾಗಿದೆ**: ಅಕ್ಟೋಬರ್ 30, 2025 | **ಡಾಕ್ಯುಮೆಂಟ್ ಆವೃತ್ತಿ**: 3.0

## ವಿಷಯಗಳ ಪಟ್ಟಿಕೆ

- [ಪ್ರಾಜೆಕ್ಟ್ ಅವಲೋಕನ](../..)
- [ರೆಪೊಸಿಟರಿ ರಚನೆ](../..)
- [ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು](../..)
- [ಸೆಟಪ್ ಕಮಾಂಡ್‌ಗಳು](../..)
- [ಅಭಿವೃದ್ಧಿ ಕಾರ್ಯಪ್ರವಾಹ](../..)
- [ಪರೀಕ್ಷಾ ಸೂಚನೆಗಳು](../..)
- [ಕೋಡ್ ಶೈಲಿ ಮಾರ್ಗದರ್ಶಿಗಳು](../..)
- [ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಮಾರ್ಗದರ್ಶಿಗಳು](../..)
- [ಅನುವಾದ ವ್ಯವಸ್ಥೆ](../..)
- [Foundry Local ಏಕೀಕರಣ](../..)
- [ಬಿಲ್ಡ್ ಮತ್ತು ನಿಯೋಜನೆ](../..)
- [ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರ](../..)
- [ಹೆಚ್ಚಿನ ಸಂಪನ್ಮೂಲಗಳು](../..)
- [ಪ್ರಾಜೆಕ್ಟ್-ನಿರ್ದಿಷ್ಟ ಟಿಪ್ಪಣಿಗಳು](../..)
- [ಸಹಾಯ ಪಡೆಯುವುದು](../..)

## Project Overview

EdgeAI for Beginners ಒಂದು ಸಮಗ್ರ ಶೈಕ್ಷಣಿಕ ರೆಪೊಸಿಟರಿ ಆಗಿದ್ದು, ಸ್ಮಾಲ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿಗಳ (SLMs)ೊಂದಿಗೆ ಎಡ್ಜ್ AI ಅಭಿವೃದ್ಧಿಯನ್ನು ಕಲಿಸುತ್ತದೆ. ಈ ಕೋರ್ಸ್ EdgeAI ಮೂಲಭೂತಗಳು, ಮಾದರಿ ನಿಯೋಜನೆ, ಆಪ್ಟಿಮೈಜೆಷನ್ ತಂತ್ರಗಳು ಮತ್ತು Microsoft Foundry Local ಮತ್ತು ವಿವಿಧ AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಬಳಸಿ ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ ಅನುಷ್ಠಾನಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.

**ಪ್ರಮುಖ ತಂತ್ರಜ್ಞಾನಗಳು:**
- Python 3.8+ (AI/ML ಮಾದರಿಗಳಿಗಾಗಿ ಪ್ರಾಥಮಿಕ ಭಾಷೆ)
- .NET C# (AI/ML ಮಾದರಿಗಳು)
- JavaScript/Node.js ಮತ್ತು Electron (ಡೆಸ್ಕ್‌ಟಾಪ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI Toolkit
- OpenAI SDK
- AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು: LangChain, Semantic Kernel, Chainlit
- ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಷನ್: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ರೆಪೊಸಿಟರಿ ಪ್ರಕಾರ:** 8 ಮಡ್ಯೂಲ್‌ಗಳು ಮತ್ತು 10 ಸಮಗ್ರ ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗಳೊಂದಿಗೆ ಶೈಕ್ಷಣಿಕ ವಿಷಯ ರೆಪೊಸಿಟರಿ

**ವಾಸ್ತುಶಿಲ್ಪ:** ಬಹು-ಮಡ್ಯೂಲ್ ಕಲಿಕೆ ಮಾರ್ಗ ಮತ್ತು ಪ್ರಾಯೋಗಿಕ ಮಾದರಿಗಳೊಂದಿಗೆ ಎಡ್ಜ್ AI ನಿಯೋಜನೆ ಮಾದರಿಗಳನ್ನು ತೋರಿಸುವುದು

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

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

### ಅಗತ್ಯ ಸಾಧನಗಳು

- **Python 3.8+** - AI/ML ಮಾದರಿಗಳು ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ
- **Node.js 16+** - Electron ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ
- **Git** - ಆವೃತ್ತಿ ನಿಯಂತ್ರಣಕ್ಕೆ
- **Microsoft Foundry Local** - AI ಮಾದರಿಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಚಾಲನೆ ಮಾಡಲು

### ಶಿಫಾರಸು ಮಾಡಿದ ಸಾಧನಗಳು

- **Visual Studio Code** - Python, Jupyter, ಮತ್ತು Pylance ವಿಸ್ತರಣೆಗಳೊಂದಿಗೆ
- **Windows Terminal** - ಉತ್ತಮ ಕಮಾಂಡ್ ಲೈನ್ ಅನುಭವಕ್ಕಾಗಿ (Windows ಬಳಕೆದಾರರಿಗೆ)
- **Docker** - ಕಂಟೈನರ್ ಆಧಾರಿತ ಅಭಿವೃದ್ಧಿಗೆ (ಐಚ್ಛಿಕ)

### ವ್ಯವಸ್ಥೆ ಅಗತ್ಯಗಳು

- **RAM**: ಕನಿಷ್ಠ 8GB, ಬಹು-ಮಾದರಿ ಸಂದರ್ಭಗಳಿಗೆ 16GB+ ಶಿಫಾರಸು
- **ಸಂಗ್ರಹಣೆ**: ಮಾದರಿಗಳು ಮತ್ತು ಅವಲಂಬನೆಗಳಿಗೆ 10GB+ ಖಾಲಿ ಜಾಗ
- **OS**: Windows 10/11, macOS 11+, ಅಥವಾ Linux (Ubuntu 20.04+)
- **ಹಾರ್ಡ್‌ವೇರ್**: AVX2 ಬೆಂಬಲದ CPU; GPU (CUDA, Qualcomm NPU) ಐಚ್ಛಿಕ ಆದರೆ ಶಿಫಾರಸು

### ಜ್ಞಾನ ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- Python ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮೂಲಭೂತ ತಿಳಿವು
- ಕಮಾಂಡ್ ಲೈನ್ ಇಂಟರ್ಫೇಸ್‌ಗಳ ಪರಿಚಯ
- AI/ML ತತ್ವಗಳ ಅರಿವು (ಮಾದರಿ ಅಭಿವೃದ್ಧಿಗಾಗಿ)
- Git ಕಾರ್ಯಪ್ರವಾಹಗಳು ಮತ್ತು ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಪ್ರಕ್ರಿಯೆಗಳು

## Setup Commands

### ರೆಪೊಸಿಟರಿ ಸೆಟಪ್

```bash
# ರೆಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# ಯಾವುದೇ ನಿರ್ಮಾಣ ಹಂತ ಅಗತ್ಯವಿಲ್ಲ - ಇದು ಮುಖ್ಯವಾಗಿ ಶೈಕ್ಷಣಿಕ ವಿಷಯ ರೆಪೊಸಿಟರಿ
```

### Python ಮಾದರಿ ಸೆಟಪ್ (Module08 ಮತ್ತು ವರ್ಕ್‌ಶಾಪ್ ಮಾದರಿಗಳು)

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ
python -m venv .venv
# ವಿಂಡೋಸ್‌ನಲ್ಲಿ
.venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನಲ್ಲಿ
source .venv/bin/activate

# ಫೌಂಡ್ರಿ ಲೋಕಲ್ SDK ಮತ್ತು ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install foundry-local-sdk openai

# Module08 ಮಾದರಿಗಳಿಗಾಗಿ ಹೆಚ್ಚುವರಿ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
cd Module08
pip install -r requirements.txt

# ವರ್ಕ್‌ಶಾಪ್ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
cd ../Workshop
pip install -r requirements.txt
```

### Node.js ಮಾದರಿ ಸೆಟಪ್ (Sample 08 - Windows ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್)

```bash
cd Module08/samples/08
npm install

# ಅಭಿವೃದ್ಧಿ ಮೋಡ್‌ನಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿ
npm run dev

# ಉತ್ಪಾದನೆಗಾಗಿ ನಿರ್ಮಿಸಿ
npm run build

# ಸ್ಥಾಪಕವನ್ನು ರಚಿಸಿ
npm run dist
```

### Foundry Local ಸೆಟಪ್

Foundry Local ಮಾದರಿಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ಅಗತ್ಯವಿದೆ. ಅಧಿಕೃತ ರೆಪೊಸಿಟರಿಯಿಂದ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಸ್ಥಾಪಿಸಿ:

**ಸ್ಥಾಪನೆ:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ಮ್ಯಾನುಯಲ್**: [ರಿಲೀಸ್ ಪುಟದಿಂದ](https://github.com/microsoft/Foundry-Local/releases) ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ

**ತ್ವರಿತ ಪ್ರಾರಂಭ:**
```bash
# ನಿಮ್ಮ ಮೊದಲ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿ (ಅವಶ್ಯಕತೆ ಇದ್ದರೆ ಸ್ವಯಂಚಾಲಿತ ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ)
foundry model run phi-4-mini

# ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model ls

# ಸೇವೆಯ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status
```

**ಗಮನಿಸಿ**: Foundry Local ನಿಮ್ಮ ಹಾರ್ಡ್‌ವೇರ್ (CUDA GPU, Qualcomm NPU, ಅಥವಾ CPU) ಗೆ ಅತ್ಯುತ್ತಮ ಮಾದರಿ ರೂಪಾಂತರವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಆಯ್ಕೆಮಾಡುತ್ತದೆ.

## Development Workflow

### ವಿಷಯ ಅಭಿವೃದ್ಧಿ

ಈ ರೆಪೊಸಿಟರಿ ಮುಖ್ಯವಾಗಿ **Markdown ಶೈಕ್ಷಣಿಕ ವಿಷಯ** ಹೊಂದಿದೆ. ಬದಲಾವಣೆ ಮಾಡುವಾಗ:

1. ಸಂಬಂಧಿತ ಮಡ್ಯೂಲ್ ಡೈರೆಕ್ಟರಿಗಳಲ್ಲಿ `.md` ಫೈಲ್‌ಗಳನ್ನು ಸಂಪಾದಿಸಿ
2. ಇತ್ತೀಚಿನ ಫಾರ್ಮ್ಯಾಟಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಅನುಸರಿಸಿ
3. ಕೋಡ್ ಉದಾಹರಣೆಗಳು ಸರಿಯಾಗಿದ್ದು ಪರೀಕ್ಷಿಸಲ್ಪಟ್ಟಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ
4. ಅಗತ್ಯವಿದ್ದರೆ ಅನುವಾದಿತ ವಿಷಯವನ್ನು ನವೀಕರಿಸಿ (ಅಥವಾ ಸ್ವಯಂಚಾಲಿತ ವ್ಯವಸ್ಥೆಗೆ ಬಿಡಿ)

### ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್ ಅಭಿವೃದ್ಧಿ

Module08 Python ಮಾದರಿಗಳಿಗಾಗಿ (ಮಾದರಿ 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

ವರ್ಕ್‌ಶಾಪ್ Python ಮಾದರಿಗಳಿಗಾಗಿ:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron ಮಾದರಿ (ಮಾದರಿ 08)ಗಾಗಿ:
```bash
cd Module08/samples/08
npm run dev  # ಹಾಟ್ ರಿಲೋಡ್‌ನೊಂದಿಗೆ ಅಭಿವೃದ್ಧಿ
```

### ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ಪರೀಕ್ಷೆ

Python ಮಾದರಿಗಳಿಗೆ ಸ್ವಯಂಚಾಲಿತ ಪರೀಕ್ಷೆಗಳು ಇಲ್ಲ, ಆದರೆ ಅವುಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ ಪರಿಶೀಲಿಸಬಹುದು:
```bash
# ಮೂಲ ಚಾಟ್ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ
python samples/01/chat_quickstart.py "Hello"

# ನಿರ್ದಿಷ್ಟ ಮಾದರಿಯೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron ಮಾದರಿಗೆ ಪರೀಕ್ಷಾ ಮೂಲಸೌಕರ್ಯ ಇದೆ:
```bash
cd Module08/samples/08
npm test           # ಯೂನಿಟ್ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
npm run test:e2e   # ಅಂತ್ಯದಿಂದ ಅಂತ್ಯವರೆಗೆ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
npm run lint       # ಕೋಡ್ ಶೈಲಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
```

## Testing Instructions

### ವಿಷಯ ಮಾನ್ಯತೆ

ರೆಪೊಸಿಟರಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಬಳಸುತ್ತದೆ. ಅನುವಾದಗಳಿಗೆ ಕೈಯಿಂದ ಪರೀಕ್ಷೆ ಅಗತ್ಯವಿಲ್ಲ.

**ವಿಷಯ ಬದಲಾವಣೆಗಳಿಗೆ ಕೈಯಿಂದ ಮಾನ್ಯತೆ:**
1. `.md` ಫೈಲ್‌ಗಳನ್ನು ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ Markdown ರೆಂಡರಿಂಗ್ ಪರಿಶೀಲಿಸಿ
2. ಎಲ್ಲಾ ಲಿಂಕ್‌ಗಳು ಮಾನ್ಯ ಗುರಿಗಳನ್ನು ಸೂಚಿಸುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿ
3. ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ನಲ್ಲಿ ಸೇರಿಸಿರುವ ಯಾವುದೇ ಕೋಡ್ ತುಣುಕುಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ
4. ಚಿತ್ರಗಳು ಸರಿಯಾಗಿ ಲೋಡ್ ಆಗುತ್ತವೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ

### ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್ ಪರೀಕ್ಷೆ

**Module08/samples/08 (Electron ಅಪ್ಲಿಕೇಶನ್) ಗೆ ಸಮಗ್ರ ಪರೀಕ್ಷೆ ಇದೆ:**
```bash
cd Module08/samples/08

# ಎಲ್ಲಾ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
npm test

# ಯೂನಿಟ್ ಪರೀಕ್ಷೆಗಳನ್ನು ಮಾತ್ರ ನಡೆಸಿ
npm test -- --testPathPattern=unit

# ಇಂಟಿಗ್ರೇಶನ್ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
npm run test:integration

# E2E ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
npm run test:e2e

# ಪರೀಕ್ಷಾ ವ್ಯಾಪ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
npm test -- --coverage
```

**Python ಮಾದರಿಗಳನ್ನು ಕೈಯಿಂದ ಪರೀಕ್ಷಿಸಬೇಕು:**
```bash
# Module08 ಮಾದರಿಗಳು
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# ಕಾರ್ಯಾಗಾರ ಮಾದರಿಗಳು
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# ಕಾರ್ಯಾಗಾರ ಮಾನ್ಯತೆ ಸಾಧನಗಳನ್ನು ಬಳಸಿ
cd Workshop/scripts
python validate_samples.py  # ವ್ಯಾಕರಣ ಮತ್ತು ಆಮದುಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
python test_samples.py      # ಸ್ಮೋಕ್ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ
```

## Code Style Guidelines

### Markdown ವಿಷಯ

- ಶೀರ್ಷಿಕೆ ಹೈರಾರ್ಕಿಯನ್ನು ಸತತವಾಗಿ ಬಳಸಿ (# ಶೀರ್ಷಿಕೆಗಾಗಿ, ## ಮುಖ್ಯ ವಿಭಾಗಗಳಿಗೆ, ### ಉಪವಿಭಾಗಗಳಿಗೆ)
- ಭಾಷಾ ಸೂಚಕಗಳೊಂದಿಗೆ ಕೋಡ್ ಬ್ಲಾಕ್‌ಗಳನ್ನು ಸೇರಿಸಿ: ```python, ```bash, ```javascript
- ಟೇಬಲ್‌ಗಳು, ಪಟ್ಟಿ ಮತ್ತು ಒತ್ತಡಕ್ಕೆ ಇತ್ತೀಚಿನ ಫಾರ್ಮ್ಯಾಟಿಂಗ್ ಅನುಸರಿಸಿ
- ಸಾಲುಗಳನ್ನು ಓದಲು ಸುಲಭವಾಗಿರಿಸಿ (~80-100 ಅಕ್ಷರಗಳ ಗುರಿ, ಆದರೆ ಕಟ್ಟುನಿಟ್ಟಿಲ್ಲ)
- ಆಂತರಿಕ ಉಲ್ಲೇಖಗಳಿಗೆ ಸಂಬಂಧಿತ ಲಿಂಕ್‌ಗಳನ್ನು ಬಳಸಿ

### Python ಕೋಡ್ ಶೈಲಿ

- PEP 8 ನಿಯಮಗಳನ್ನು ಅನುಸರಿಸಿ
- ಅಗತ್ಯವಿದ್ದಲ್ಲಿ ಟೈಪ್ ಸೂಚನೆಗಳನ್ನು ಬಳಸಿ
- ಫಂಕ್ಷನ್‌ಗಳು ಮತ್ತು ಕ್ಲಾಸ್‌ಗಳಿಗೆ ಡಾಕ್ಸ್ಟ್ರಿಂಗ್‌ಗಳನ್ನು ಸೇರಿಸಿ
- ಅರ್ಥಪೂರ್ಣ ಚರಗಳ ಹೆಸರುಗಳನ್ನು ಬಳಸಿ
- ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಕೇಂದ್ರೀಕರಿಸಿ ಮತ್ತು ಸಂಕ್ಷಿಪ್ತವಾಗಿರಿಸಿ

### JavaScript/Node.js ಕೋಡ್ ಶೈಲಿ

```bash
# ಎಲೆಕ್ಟ್ರಾನ್ ಮಾದರಿ ESLint ಸಂರಚನೆಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ
cd Module08/samples/08
npm run lint        # ಶೈಲಿ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
npm run lint:fix    # ಶೈಲಿ ಸಮಸ್ಯೆಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸರಿಪಡಿಸಿ
npm run format      # ಪ್ರಿಟಿಯರ್‌ನೊಂದಿಗೆ ಸ್ವರೂಪಗೊಳಿಸಿ
```

**ಪ್ರಮುಖ ನಿಯಮಗಳು:**
- ಮಾದರಿ 08 ರಲ್ಲಿ ESLint ಸಂರಚನೆ ನೀಡಲಾಗಿದೆ
- ಕೋಡ್ ಫಾರ್ಮ್ಯಾಟಿಂಗ್‌ಗೆ Prettier ಬಳಸಿ
- ಆಧುನಿಕ ES6+ ಸಿಂಟ್ಯಾಕ್ಸ್ ಬಳಸಿ
- ಕೋಡ್‌ಬೇಸ್‌ನ ಇತ್ತೀಚಿನ ಮಾದರಿಗಳನ್ನು ಅನುಸರಿಸಿ

## Pull Request Guidelines

### ಕೊಡುಗೆ ಕಾರ್ಯಪ್ರವಾಹ

1. **ರೆಪೊಸಿಟರಿಯನ್ನು ಫೋರ್ಕ್ ಮಾಡಿ** ಮತ್ತು `main` ನಿಂದ ಹೊಸ ಶಾಖೆಯನ್ನು ರಚಿಸಿ
2. **ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡಿ** ಕೋಡ್ ಶೈಲಿ ಮಾರ್ಗದರ್ಶಿಗಳನ್ನು ಅನುಸರಿಸಿ
3. **ಮೆಚ್ಚಿನ ಪರೀಕ್ಷೆ ಮಾಡಿ** ಮೇಲಿನ ಪರೀಕ್ಷಾ ಸೂಚನೆಗಳನ್ನು ಬಳಸಿ
4. **ಸ್ಪಷ್ಟ ಸಂದೇಶಗಳೊಂದಿಗೆ ಕಮಿಟ್ ಮಾಡಿ** ಸಂಪ್ರದಾಯಬದ್ಧ ಕಮಿಟ್ ಫಾರ್ಮ್ಯಾಟ್ ಅನುಸರಿಸಿ
5. **ನಿಮ್ಮ ಫೋರ್ಕ್‌ಗೆ ಪುಷ್ ಮಾಡಿ** ಮತ್ತು ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ರಚಿಸಿ
6. **ಪರಿಶೀಲನೆ ಸಮಯದಲ್ಲಿ ನಿರ್ವಹಕರ ಪ್ರತಿಕ್ರಿಯೆಗೆ ಪ್ರತಿಕ್ರಿಯಿಸಿ**

### ಶಾಖೆ ಹೆಸರು ನಿಯಮ

- `feature/<module>-<description>` - ಹೊಸ ವೈಶಿಷ್ಟ್ಯಗಳು ಅಥವಾ ವಿಷಯಗಳಿಗೆ
- `fix/<module>-<description>` - ದೋಷ ಸರಿಪಡಿಸಲು
- `docs/<description>` - ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಸುಧಾರಣೆಗಳಿಗೆ
- `refactor/<description>` - ಕೋಡ್ ಪುನರ್‌ರಚನೆಗೆ

### ಕಮಿಟ್ ಸಂದೇಶ ಫಾರ್ಮ್ಯಾಟ್

[Conventional Commits](https://www.conventionalcommits.org/) ಅನುಸರಿಸಿ:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ಉದಾಹರಣೆಗಳು:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### ಶೀರ್ಷಿಕೆ ಫಾರ್ಮ್ಯಾಟ್
```
[ModuleXX] Brief description of change
```
ಅಥವಾ
```
[Module08/samples/XX] Description for sample changes
```

### ವರ್ತನೆ ನಿಯಮ

ಎಲ್ಲಾ ಕೊಡುಗೆದಾರರು [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ಅನ್ನು ಅನುಸರಿಸಬೇಕು. ದಯವಿಟ್ಟು ಕೊಡುಗೆ ನೀಡುವ ಮೊದಲು [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ಪರಿಶೀಲಿಸಿ.

### ಸಲ್ಲಿಸುವ ಮೊದಲು

**ವಿಷಯ ಬದಲಾವಣೆಗಳಿಗೆ:**
- ಎಲ್ಲಾ ಬದಲಾಯಿಸಿದ Markdown ಫೈಲ್‌ಗಳನ್ನು ಪೂರ್ವದೃಶ್ಯ ಮಾಡಿ
- ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಚಿತ್ರಗಳು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿ
- ಟೈಪೋಗಳು ಮತ್ತು ವ್ಯಾಕರಣ ದೋಷಗಳಿಗಾಗಿ ಪರಿಶೀಲಿಸಿ

**ಮಾದರಿ ಕೋಡ್ ಬದಲಾವಣೆಗಳಿಗೆ (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python ಮಾದರಿ ಬದಲಾವಣೆಗಳಿಗೆ:**
- ಮಾದರಿ ಯಶಸ್ವಿಯಾಗಿ ಚಾಲನೆ ಆಗುತ್ತದೆಯೇ ಪರೀಕ್ಷಿಸಿ
- ದೋಷ ನಿರ್ವಹಣೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆಯೇ ಪರಿಶೀಲಿಸಿ
- Foundry Local ಜೊತೆಗೆ ಹೊಂದಾಣಿಕೆ ಪರಿಶೀಲಿಸಿ

### ಪರಿಶೀಲನೆ ಪ್ರಕ್ರಿಯೆ

- ಶೈಕ್ಷಣಿಕ ವಿಷಯ ಬದಲಾವಣೆಗಳನ್ನು ನಿಖರತೆ ಮತ್ತು ಸ್ಪಷ್ಟತೆಗಾಗಿ ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ
- ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಕಾರ್ಯಕ್ಷಮತೆಗಾಗಿ ಪರೀಕ್ಷಿಸಲಾಗುತ್ತದೆ
- ಅನುವಾದ ನವೀಕರಣಗಳನ್ನು GitHub Actions ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ

## Translation System

**ಮುಖ್ಯ:** ಈ ರೆಪೊಸಿಟರಿ GitHub Actions ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದವನ್ನು ಬಳಸುತ್ತದೆ.

- ಅನುವಾದಗಳು `/translations/` ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇವೆ (50+ ಭಾಷೆಗಳು)
- `co-op-translator.yml` ಕಾರ್ಯಪ್ರವಾಹದಿಂದ ಸ್ವಯಂಚಾಲಿತ
- **ಅನುವಾದ ಫೈಲ್‌ಗಳನ್ನು ಕೈಯಿಂದ ಸಂಪಾದಿಸಬೇಡಿ** - ಅವು ಮರುಬರೆಯಲ್ಪಡುತ್ತವೆ
- ಮೂಲ ಮತ್ತು ಮಡ್ಯೂಲ್ ಡೈರೆಕ್ಟರಿಗಳಲ್ಲಿ ಕೇವಲ ಇಂಗ್ಲಿಷ್ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸಂಪಾದಿಸಿ
- ಅನುವಾದಗಳು `main` ಶಾಖೆಗೆ ಪುಷ್ ಮಾಡಿದಾಗ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಚಿಸಲಾಗುತ್ತದೆ

## Foundry Local Integration

ಬಹುತೇಕ Module08 ಮಾದರಿಗಳಿಗೆ Microsoft Foundry Local ಚಾಲನೆಯಲ್ಲಿರಬೇಕು.

### ಸ್ಥಾಪನೆ ಮತ್ತು ಸೆಟಪ್

**Foundry Local ಅನ್ನು ಸ್ಥಾಪಿಸಿ:**
```bash
# ವಿಂಡೋಸ್
winget install Microsoft.FoundryLocal

# ಮ್ಯಾಕ್‌ಒಎಸ್
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ಅನ್ನು ಸ್ಥಾಪಿಸಿ:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ಪ್ರಾರಂಭಿಸುವುದು
```bash
# ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿ (ಅಗತ್ಯವಿದ್ದರೆ ಸ್ವಯಂಚಾಲಿತ ಡೌನ್‌ಲೋಡ್)
foundry model run phi-3.5-mini

# ಅಥವಾ ಸ್ವಯಂಚಾಲಿತ ಹಾರ್ಡ್‌ವೇರ್ ಆಪ್ಟಿಮೈಜೆಷನ್‌ಗಾಗಿ ಮಾದರಿ ಉಪನಾಮಗಳನ್ನು ಬಳಸಿ
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# ಸೇವೆಯ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model ls
```

### SDK ಬಳಕೆ (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# ಸ್ವಯಂಚಾಲಿತ ಹಾರ್ಡ್‌ವೇರ್ ಆಪ್ಟಿಮೈಜೆಶನ್‌ಗಾಗಿ ಮಾದರಿ ಉಪನಾಮವನ್ನು ಬಳಸಿ
alias = "phi-4-mini"

# ಮ್ಯಾನೇಜರ್ ರಚಿಸಿ (ಸ್ವಯಂ ಪ್ರಾರಂಭ ಸೇವೆ ಮತ್ತು ಮಾದರಿ ಲೋಡ್ ಮಾಡುತ್ತದೆ)
manager = FoundryLocalManager(alias)

# ಸ್ಥಳೀಯ ಫೌಂಡ್ರಿ ಸೇವೆಗೆ OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸಿ
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# ಮಾದರಿಯನ್ನು ಬಳಸಿ
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local ಪರಿಶೀಲನೆ
```bash
# ಸೇವಾ ಸ್ಥಿತಿ ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್
foundry service status

# ಲೋಡ್ ಮಾಡಿದ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ (REST API)
curl http://localhost:<port>/v1/models

# ಟಿಪ್ಪಣಿ: 'foundry service status' ಅನ್ನು ಚಾಲನೆ ಮಾಡಿದಾಗ ಪೋರ್ಟ್ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ
```

### ಮಾದರಿಗಳಿಗಾಗಿ ಪರಿಸರ ಚರಗಳು

ಬಹುತೇಕ ಮಾದರಿಗಳು ಈ ಪರಿಸರ ಚರಗಳನ್ನು ಬಳಸುತ್ತವೆ:
```bash
# ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯ ಸಂರಚನೆ
# ಟಿಪ್ಪಣಿ: SDK (FoundryLocalManager) ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಪತ್ತೆಹಚ್ಚುತ್ತದೆ
set MODEL=phi-4-mini  # ಅಥವಾ phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # ಸ್ಥಳೀಯ ಬಳಕೆಗೆ ಅಗತ್ಯವಿಲ್ಲ

# ಕೈಯಿಂದ ಎಂಡ್ಪಾಯಿಂಟ್ (SDK ಬಳಸದಿದ್ದರೆ)
# ಪೋರ್ಟ್ 'foundry service status' ಮೂಲಕ ತೋರಿಸಲಾಗುತ್ತದೆ
set BASE_URL=http://localhost:<port>

# ಅಜೂರ್ ಓಪನ್‌ಎಐ ಬ್ಯಾಕ್ಅಪ್ (ಐಚ್ಛಿಕ)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**ಗಮನಿಸಿ**: `FoundryLocalManager` ಬಳಕೆ ಮಾಡಿದಾಗ, SDK ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೇವಾ ಅನ್ವೇಷಣೆ ಮತ್ತು ಮಾದರಿ ಲೋಡಿಂಗ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಮಾದರಿ ಬದಲಾವಣೆ ಹೆಸರುಗಳು (ಉದಾ: `phi-3.5-mini`) ನಿಮ್ಮ ಹಾರ್ಡ್‌ವೇರ್‌ಗೆ ಅತ್ಯುತ್ತಮ ರೂಪಾಂತರವನ್ನು ಖಚಿತಪಡಿಸುತ್ತವೆ.

## Build and Deployment

### ವಿಷಯ ನಿಯೋಜನೆ

ಈ ರೆಪೊಸಿಟರಿ ಮುಖ್ಯವಾಗಿ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಆಗಿದ್ದು, ವಿಷಯಕ್ಕೆ ಯಾವುದೇ ಬಿಲ್ಡ್ ಪ್ರಕ್ರಿಯೆ ಅಗತ್ಯವಿಲ್ಲ.

### ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್ ಬಿಲ್ಡಿಂಗ್

**Electron ಅಪ್ಲಿಕೇಶನ್ (Module08/samples/08):**
```bash
cd Module08/samples/08

# ಅಭಿವೃದ್ಧಿ ನಿರ್ಮಾಣ
npm run dev

# ಉತ್ಪಾದನಾ ನಿರ್ಮಾಣ
npm run build

# ವಿಂಡೋಸ್ ಇನ್‌ಸ್ಟಾಲರ್ ರಚಿಸಿ
npm run dist

# ಪೋರ್ಟಬಲ್ ಎಕ್ಸಿಕ್ಯೂಟಬಲ್ ರಚಿಸಿ
npm run pack
```

**Python ಮಾದರಿಗಳು:**
ಬಿಲ್ಡ್ ಪ್ರಕ್ರಿಯೆ ಇಲ್ಲ - Python ಇಂಟರ್ಪ್ರೆಟರ್ ಮೂಲಕ ನೇರವಾಗಿ ಚಾಲನೆ ಮಾಡಲಾಗುತ್ತದೆ.

## Common Issues and Troubleshooting

> **ಸೂಚನೆ**: ಪರಿಚಿತ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳಿಗಾಗಿ [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) ಪರಿಶೀಲಿಸಿ.

### ಗಂಭೀರ ಸಮಸ್ಯೆಗಳು (ತಡೆಗಟ್ಟುವ)

#### Foundry Local ಚಾಲನೆಯಲ್ಲಿಲ್ಲ
**ಸಮಸ್ಯೆ:** ಮಾದರಿಗಳು ಸಂಪರ್ಕ ದೋಷಗಳೊಂದಿಗೆ ವಿಫಲವಾಗುತ್ತವೆ

**ಪರಿಹಾರ:**
```bash
# ಸೇವೆ ಚಾಲನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಮಾದರಿಯೊಂದಿಗೆ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry model run phi-4-mini

# ಅಥವಾ ಸ್ಪಷ್ಟವಾಗಿ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry service start

# ಲೋಡ್ ಮಾಡಿದ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model ls

# REST API ಮೂಲಕ ಪರಿಶೀಲಿಸಿ ('foundry service status' ನಲ್ಲಿ ತೋರಿಸಲಾದ ಪೋರ್ಟ್)
curl http://localhost:<port>/v1/models
```

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು (ಮಧ್ಯಮ)

#### Python ವರ್ಚುವಲ್ ಪರಿಸರ ಸಮಸ್ಯೆಗಳು
**ಸಮಸ್ಯೆ:** ಮಾದರಿ ಆಮದು ದೋಷಗಳು

**ಪರಿಹಾರ:**
```bash
# ವರ್ಚುವಲ್ ಪರಿಸರ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
# ವಿಂಡೋಸ್
.venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ
source .venv/bin/activate

# ಅವಲಂಬನೆಗಳನ್ನು ಮರುಸ್ಥಾಪಿಸಿ
pip install -r requirements.txt
```

#### Electron ಬಿಲ್ಡ್ ಸಮಸ್ಯೆಗಳು
**ಸಮಸ್ಯೆ:** npm install ಅಥವಾ ಬಿಲ್ಡ್ ವಿಫಲತೆಗಳು

**ಪರಿಹಾರ:**
```bash
cd Module08/samples/08
# ಸ್ವಚ್ಛ ಸ್ಥಾಪನೆ
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ಕಾರ್ಯಪ್ರವಾಹ ಸಮಸ್ಯೆಗಳು (ಸಣ್ಣ)

#### ಅನುವಾದ ಕಾರ್ಯಪ್ರವಾಹ ಸಂಘರ್ಷಗಳು
**ಸಮಸ್ಯೆ:** ಅನುವಾದ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ನಿಮ್ಮ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ ಸಂಘರ್ಷಿಸುತ್ತದೆ

**ಪರಿಹಾರ:**
- ಕೇವಲ ಇಂಗ್ಲಿಷ್ ಮೂಲ ಫೈಲ್‌ಗಳನ್ನು ಸಂಪಾದಿಸಿ
- ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಿಡಿ
- ಸಂಘರ್ಷಗಳು ಸಂಭವಿಸಿದರೆ, ಅನುವಾದಗಳು ಮರ್ಜ್ ಆದ ನಂತರ `main` ಅನ್ನು ನಿಮ್ಮ ಶಾಖೆಗೆ ಮರ್ಜ್ ಮಾಡಿ

#### ಮಾದರಿ ಡೌನ್‌ಲೋಡ್ ವಿಫಲತೆಗಳು
**ಸಮಸ್ಯೆ:** Foundry Local ಮಾದರಿಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಲು ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**
```bash
# ಇಂಟರ್ನೆಟ್ ಸಂಪರ್ಕವನ್ನು ಪರಿಶೀಲಿಸಿ
# ಮಾದರಿ ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ ಮತ್ತು ಮರುಪ್ರಯತ್ನಿಸಿ
foundry model remove <model-alias>
foundry model run <model-alias>

# ಲಭ್ಯವಿರುವ ಡಿಸ್ಕ್ ಜಾಗವನ್ನು ಪರಿಶೀಲಿಸಿ (ಮಾದರಿಗಳು 2-16GB ಆಗಿರಬಹುದು)
# ಡೌನ್‌ಲೋಡ್‌ಗಳಿಗೆ ಫೈರ್‌ವಾಲ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳು ಅನುಮತಿಸುತ್ತವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
```

## Additional Resources

### ಕಲಿಕೆ ಮಾರ್ಗಗಳು
- **ಆರಂಭಿಕ ಮಾರ್ಗ:** ಮಡ್ಯೂಲ್ 01-02 (7-9 ಗಂಟೆಗಳು)
- **ಮಧ್ಯಮ ಮಾರ್ಗ:** ಮಡ್ಯೂಲ್ 03-04 (9-11 ಗಂಟೆಗಳು)
- **ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ:** ಮಡ್ಯೂಲ್ 05-07 (12-15 ಗಂಟೆಗಳು)
- **ನಿಪುಣ ಮಾರ್ಗ:** ಮಡ್ಯೂಲ್ 08 (8-10 ಗಂಟೆಗಳು)
- **ಹಸ್ತಚಾಲಿತ ವರ್ಕ್‌ಶಾಪ್:** ವರ್ಕ್‌ಶಾಪ್ ವಸ್ತುಗಳು (6-8 ಗಂಟೆಗಳು)

### ಪ್ರಮುಖ ಮಡ್ಯೂಲ್ ವಿಷಯ
- **Module01:** EdgeAI ಮೂಲಭೂತಗಳು ಮತ್ತು ನೈಜ-ಜಗತ್ತಿನ ಪ್ರಕರಣ ಅಧ್ಯಯನಗಳು
- **Module02:** ಸ್ಮಾಲ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿ (SLM) ಕುಟುಂಬಗಳು ಮತ್ತು ವಾಸ್ತುಶಿಲ್ಪಗಳು
- **Module03:** ಸ್ಥಳೀಯ ಮತ್ತು ಕ್ಲೌಡ್ ನಿಯೋಜನೆ ತಂತ್ರಗಳು
- **Module04:** ಬಹು ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಷನ್ (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - ಉತ್ಪಾದನಾ ಕಾರ್ಯಾಚರಣೆಗಳು
- **Module06:** AI ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್
- **Module07:** ವೇದಿಕೆ-ನಿರ್ದಿಷ್ಟ ಅನುಷ್ಠಾನಗಳು
- **Module08:** Foundry Local ಟೂಲ್‌ಕಿಟ್ ಮತ್ತು 10 ಸಮಗ್ರ ಮಾದರಿಗಳು

### ಬಾಹ್ಯ ಅವಲಂಬನೆಗಳು
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-ಸಮ್ಮತ API ಹೊಂದಿರುವ ಸ್ಥಳೀಯ AI ಮಾದರಿ ರನ್‌ಟೈಮ್
  - [ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ಆಪ್ಟಿಮೈಜೆಷನ್ ಫ್ರೇಮ್ವರ್ಕ್
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಷನ್ ಟೂಲ್‌ಕಿಟ್
- [OpenVINO](https://docs.openvino.ai/) - ಇಂಟೆಲ್ ಆಪ್ಟಿಮೈಜೆಷನ್ ಟೂಲ್‌ಕಿಟ್

## Project-Specific Notes

### Module08 ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು

ರೆಪೊಸಿಟರಿಯಲ್ಲಿ 10 ಸಮಗ್ರ ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿವೆ:

1. **01-REST ಚಾಟ್ ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್** - ಮೂಲ OpenAI SDK ಏಕೀಕರಣ
2. **02-OpenAI SDK ಏಕೀಕರಣ** - ಉನ್ನತ SDK ವೈಶಿಷ್ಟ್ಯಗಳು
3. **03-ಮಾದರಿ ಅನ್ವೇಷಣೆ ಮತ್ತು ಬೆಂಚ್ಮಾರ್ಕಿಂಗ್** - ಮಾದರಿ ಹೋಲಿಕೆ ಸಾಧನಗಳು
4. **04-Chainlit RAG ಅಪ್ಲಿಕೇಶನ್** - ರಿಟ್ರೀವಲ್-ಆಗ್ಮೆಂಟೆಡ್ ಜನರೇಶನ್
5. **05-ಬಹು ಏಜೆಂಟ್ ಸಂಯೋಜನೆ** - ಮೂಲ ಏಜೆಂಟ್ ಸಂಯೋಜನೆ
6. **06-ಮಾದರಿಗಳನ್ನು ಉಪಕರಣಗಳಾಗಿ ರೌಟರ್** - ಬುದ್ಧಿವಂತ ಮಾದರಿ ಮಾರ್ಗದರ್ಶನ
7. **07-ನೇರ API ಕ್ಲೈಂಟ್** - ಕಡಿಮೆ ಮಟ್ಟದ API ಏಕೀಕರಣ
8. **08-Windows 11 ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್** - ಸ್ಥಳೀಯ Electron ಡೆಸ್ಕ್‌ಟಾಪ್ ಅಪ್ಲಿಕೇಶನ್
9. **09-ಅತ್ಯುತ್ತಮ ಬಹು ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆ** - ಸಂಕೀರ್ಣ ಏಜೆಂಟ್ ಸಂಯೋಜನೆ
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel ಸಂಯೋಜನೆ

### ಕಾರ್ಯಾಗಾರ ಮಾದರಿ ಅನ್ವಯಿಕೆಗಳು

ಕಾರ್ಯಾಗಾರವು 6 ಪ್ರಗತಿಶೀಲ ಅಧಿವೇಶನಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಪ್ರಾಯೋಗಿಕ ಅನುಷ್ಠಾನಗಳೊಂದಿಗೆ:

1. **ಅಧಿವೇಶನ 01** - Foundry Local ಸಂಯೋಜನೆಯೊಂದಿಗೆ ಚಾಟ್ ಬೂಟ್‌ಸ್ಟ್ರಾಪ್
2. **ಅಧಿವೇಶನ 02** - RAG ಪೈಪ್ಲೈನ್ ಮತ್ತು RAGAS ಮೂಲಕ ಮೌಲ್ಯಮಾಪನ
3. **ಅಧಿವೇಶನ 03** - ಓಪನ್-ಸೋರ್ಸ್ ಮಾದರಿಗಳ ಬೆಂಚ್ಮಾರ್ಕಿಂಗ್
4. **ಅಧಿವೇಶನ 04** - ಮಾದರಿ ಹೋಲಿಕೆ ಮತ್ತು ಆಯ್ಕೆ
5. **ಅಧಿವೇಶನ 05** - ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನಾ ವ್ಯವಸ್ಥೆಗಳು
6. **ಅಧಿವೇಶನ 06** - ಮಾದರಿ ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ಪೈಪ್ಲೈನ್ ನಿರ್ವಹಣೆ

ಪ್ರತಿ ಮಾದರಿ Foundry Local ನೊಂದಿಗೆ ಎಡ್ಜ್ AI ಅಭಿವೃದ್ಧಿಯ ವಿಭಿನ್ನ ಅಂಶಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.

### ಕಾರ್ಯಕ್ಷಮತೆ ಪರಿಗಣನೆಗಳು

- SLM ಗಳು ಎಡ್ಜ್ ನಿಯೋಜನೆಗಾಗಿ (2-16GB RAM) ಆಪ್ಟಿಮೈಸ್ ಮಾಡಲಾಗಿದೆ
- ಸ್ಥಳೀಯ ನಿರ್ಣಯವು 50-500ms ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ
- ಪ್ರಮಾಣೀಕರಣ ತಂತ್ರಗಳು 75% ಗಾತ್ರ ಕಡಿತ ಮತ್ತು 85% ಕಾರ್ಯಕ್ಷಮತೆ ಉಳಿಸುವಿಕೆಯನ್ನು ಸಾಧಿಸುತ್ತವೆ
- ಸ್ಥಳೀಯ ಮಾದರಿಗಳೊಂದಿಗೆ ರಿಯಲ್-ಟೈಮ್ ಸಂಭಾಷಣೆ ಸಾಮರ್ಥ್ಯಗಳು

### ಭದ್ರತೆ ಮತ್ತು ಗೌಪ್ಯತೆ

- ಎಲ್ಲಾ ಪ್ರಕ್ರಿಯೆ ಸ್ಥಳೀಯವಾಗಿ ನಡೆಯುತ್ತದೆ - ಯಾವುದೇ ಡೇಟಾ ಕ್ಲೌಡ್‌ಗೆ ಕಳುಹಿಸಲಾಗುವುದಿಲ್ಲ
- ಗೌಪ್ಯತೆ-ಸಂವೇದನಶೀಲ ಅನ್ವಯಿಕೆಗಳಿಗೆ ಸೂಕ್ತ (ಆರೋಗ್ಯ, ಹಣಕಾಸು)
- ಡೇಟಾ ಸ್ವಾಯತ್ತತೆ ಅಗತ್ಯಗಳನ್ನು ಪೂರೈಸುತ್ತದೆ
- Foundry Local ಸಂಪೂರ್ಣವಾಗಿ ಸ್ಥಳೀಯ ಹಾರ್ಡ್‌ವೇರ್‌ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ

## ಸಹಾಯ ಪಡೆಯುವುದು

### ಡಾಕ್ಯುಮೆಂಟೇಶನ್

- **ಮುಖ್ಯ README**: [README.md](README.md) - ಸಂಗ್ರಹಣೆಯ ಅವಲೋಕನ ಮತ್ತು ಕಲಿಕೆ ಮಾರ್ಗಗಳು
- **ಅಧ್ಯಯನ ಮಾರ್ಗದರ್ಶಿ**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - ಕಲಿಕೆ ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಮಯರೇಖೆ
- **ಬೆಂಬಲ**: [SUPPORT.md](SUPPORT.md) - ಸಹಾಯ ಪಡೆಯುವ ವಿಧಾನ
- **ಭದ್ರತೆ**: [SECURITY.md](SECURITY.md) - ಭದ್ರತಾ ಸಮಸ್ಯೆಗಳ ವರದಿ

### ಸಮುದಾಯ ಬೆಂಬಲ

- **GitHub Issues**: [ದೋಷಗಳನ್ನು ವರದಿ ಮಾಡಿ ಅಥವಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ವಿನಂತಿಸಿ](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub ಚರ್ಚೆಗಳು**: [ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಿ ಮತ್ತು ಆಲೋಚನೆಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳಿ](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local ನ ತಾಂತ್ರಿಕ ಸಮಸ್ಯೆಗಳು](https://github.com/microsoft/Foundry-Local/issues)

### ಸಂಪರ್ಕ

- **ನಿರ್ವಹಣಾಧಿಕಾರಿಗಳು**: ನೋಡಿ [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **ಭದ್ರತಾ ಸಮಸ್ಯೆಗಳು**: [SECURITY.md](SECURITY.md) ನಲ್ಲಿ ಜವಾಬ್ದಾರಿಯುತ ಬಹಿರಂಗಪಡಿಸುವಿಕೆಯನ್ನು ಅನುಸರಿಸಿ
- **Microsoft ಬೆಂಬಲ**: ಎಂಟರ್‌ಪ್ರೈಸ್ ಬೆಂಬಲಕ್ಕಾಗಿ, Microsoft ಗ್ರಾಹಕ ಸೇವೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ

### ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- **Microsoft Learn**: [AI ಮತ್ತು ಯಂತ್ರ ಅಧ್ಯಯನ ಕಲಿಕೆ ಮಾರ್ಗಗಳು](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ಡಾಕ್ಯುಮೆಂಟೇಶನ್**: [ಅಧಿಕೃತ ಡಾಕ್ಸ್](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **ಸಮುದಾಯ ಮಾದರಿಗಳು**: ಸಮುದಾಯ ಕೊಡುಗೆಗಳಿಗಾಗಿ [GitHub ಚರ್ಚೆಗಳು](https://github.com/microsoft/edgeai-for-beginners/discussions) ಪರಿಶೀಲಿಸಿ

---

**ಇದು ಎಡ್ಜ್ AI ಅಭಿವೃದ್ಧಿಯನ್ನು ಕಲಿಸುವುದಕ್ಕೆ ಕೇಂದ್ರೀಕೃತ ಶೈಕ್ಷಣಿಕ ಸಂಗ್ರಹಣೆ. ಪ್ರಾಥಮಿಕ ಕೊಡುಗೆ ಮಾದರಿ ಶೈಕ್ಷಣಿಕ ವಿಷಯವನ್ನು ಸುಧಾರಿಸುವುದು ಮತ್ತು ಎಡ್ಜ್ AI ತತ್ವಗಳನ್ನು ಪ್ರದರ್ಶಿಸುವ ಮಾದರಿ ಅನ್ವಯಿಕೆಗಳನ್ನು ಸೇರಿಸುವುದು/ಮೆಚ್ಚಿಸುವುದಾಗಿದೆ.**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->