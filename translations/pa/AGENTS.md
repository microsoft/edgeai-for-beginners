<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T12:06:39+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pa"
}
-->
# AGENTS.md

> **ਡਿਵੈਲਪਰ ਗਾਈਡ ਸ਼ੁਰੂਆਤੀ ਲਈ EdgeAI ਵਿੱਚ ਯੋਗਦਾਨ ਪਾਉਣ ਲਈ**
> 
> ਇਹ ਦਸਤਾਵੇਜ਼ ਡਿਵੈਲਪਰਾਂ, AI ਏਜੰਟਾਂ ਅਤੇ ਯੋਗਦਾਨਕਰਤਿਆਂ ਲਈ ਵਿਸਤ੍ਰਿਤ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹਨ। ਇਹ ਸੈਟਅਪ, ਵਿਕਾਸ ਵਰਕਫਲੋਜ਼, ਟੈਸਟਿੰਗ ਅਤੇ ਵਧੀਆ ਅਭਿਆਸਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।
> 
> **ਆਖਰੀ ਅਪਡੇਟ**: 30 ਅਕਤੂਬਰ, 2025 | **ਦਸਤਾਵੇਜ਼ ਵਰਜਨ**: 3.0

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- [ਪ੍ਰੋਜੈਕਟ ਝਲਕ](../..)
- [ਰਿਪੋਜ਼ਟਰੀ ਸਟ੍ਰਕਚਰ](../..)
- [ਪ੍ਰੀ-ਰੀਕੁਇਜ਼ਿਟਸ](../..)
- [ਸੈਟਅਪ ਕਮਾਂਡ](../..)
- [ਵਿਕਾਸ ਵਰਕਫਲੋ](../..)
- [ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼](../..)
- [ਕੋਡ ਸਟਾਈਲ ਗਾਈਡਲਾਈਨ](../..)
- [ਪੁਲ ਰਿਕਵੇਸਟ ਗਾਈਡਲਾਈਨ](../..)
- [ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ](../..)
- [Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ](../..)
- [ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ](../..)
- [ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ](../..)
- [ਵਾਧੂ ਸਰੋਤ](../..)
- [ਪ੍ਰੋਜੈਕਟ-ਵਿਸ਼ੇਸ਼ ਨੋਟਸ](../..)
- [ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ](../..)

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

EdgeAI for Beginners ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਸਿੱਖਿਆ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜੋ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLMs) ਨਾਲ Edge AI ਵਿਕਾਸ ਸਿਖਾਉਂਦਾ ਹੈ। ਕੋਰਸ EdgeAI ਮੂਲਭੂਤ, ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ, ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ ਅਤੇ Microsoft Foundry Local ਅਤੇ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਤਪਾਦਨ-ਤਿਆਰ ਕਾਰਜਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- Python 3.8+ (AI/ML ਨਮੂਨਿਆਂ ਲਈ ਮੁੱਖ ਭਾਸ਼ਾ)
- .NET C# (AI/ML ਨਮੂਨੇ)
- JavaScript/Node.js ਨਾਲ Electron (ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ ਲਈ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ਫਰੇਮਵਰਕ: LangChain, Semantic Kernel, Chainlit
- ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ਰਿਪੋਜ਼ਟਰੀ ਕਿਸਮ:** ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਰਿਪੋਜ਼ਟਰੀ ਜਿਸ ਵਿੱਚ 8 ਮੋਡੀਊਲ ਅਤੇ 10 ਵਿਸਤ੍ਰਿਤ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਹਨ

**ਆਰਕੀਟੈਕਚਰ:** ਬਹੁ-ਮੋਡੀਊਲ ਸਿੱਖਣ ਪਾਥ ਜਿਸ ਵਿੱਚ Edge AI ਡਿਪਲੌਇਮੈਂਟ ਪੈਟਰਨ ਦਿਖਾਉਣ ਵਾਲੇ ਪ੍ਰੈਕਟਿਕਲ ਨਮੂਨੇ ਹਨ

## ਰਿਪੋਜ਼ਟਰੀ ਸਟ੍ਰਕਚਰ

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

## ਪ੍ਰੀ-ਰੀਕੁਇਜ਼ਿਟਸ

### ਲੋੜੀਂਦੇ ਟੂਲ

- **Python 3.8+** - AI/ML ਨਮੂਨਿਆਂ ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਲਈ
- **Node.js 16+** - Electron ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਲਈ
- **Git** - ਵਰਜਨ ਕੰਟਰੋਲ ਲਈ
- **Microsoft Foundry Local** - AI ਮਾਡਲਾਂ ਨੂੰ ਲੋਕਲ ਚਲਾਉਣ ਲਈ

### ਸਿਫਾਰਸ਼ੀ ਟੂਲ

- **Visual Studio Code** - Python, Jupyter, ਅਤੇ Pylance ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ
- **Windows Terminal** - ਬਿਹਤਰ ਕਮਾਂਡ-ਲਾਈਨ ਅਨੁਭਵ ਲਈ (Windows ਉਪਭੋਗਤਾ)
- **Docker** - ਕੰਟੇਨਰਾਈਜ਼ਡ ਵਿਕਾਸ ਲਈ (ਵਿਕਲਪਿਕ)

### ਸਿਸਟਮ ਦੀਆਂ ਲੋੜਾਂ

- **RAM**: ਘੱਟੋ-ਘੱਟ 8GB, ਬਹੁ-ਮਾਡਲ ਸਨਰੀਓਜ਼ ਲਈ 16GB+ ਸਿਫਾਰਸ਼ੀ
- **ਸਟੋਰੇਜ**: ਮਾਡਲਾਂ ਅਤੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਲਈ 10GB+ ਖਾਲੀ ਸਥਾਨ
- **OS**: Windows 10/11, macOS 11+, ਜਾਂ Linux (Ubuntu 20.04+)
- **ਹਾਰਡਵੇਅਰ**: AVX2 ਸਪੋਰਟ ਵਾਲਾ CPU; GPU (CUDA, Qualcomm NPU) ਵਿਕਲਪਿਕ ਪਰ ਸਿਫਾਰਸ਼ੀ

### ਗਿਆਨ ਦੀਆਂ ਲੋੜਾਂ

- Python ਪ੍ਰੋਗਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ
- ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸਾਂ ਨਾਲ ਜਾਣੂ
- AI/ML ਸੰਕਲਪਾਂ ਦੀ ਸਮਝ (ਨਮੂਨਾ ਵਿਕਾਸ ਲਈ)
- Git ਵਰਕਫਲੋਜ਼ ਅਤੇ ਪੁਲ ਰਿਕਵੇਸਟ ਪ੍ਰਕਿਰਿਆਵਾਂ

## ਸੈਟਅਪ ਕਮਾਂਡ

### ਰਿਪੋਜ਼ਟਰੀ ਸੈਟਅਪ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python ਨਮੂਨਾ ਸੈਟਅਪ (Module08 ਅਤੇ ਵਰਕਸ਼ਾਪ ਨਮੂਨੇ)

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

### Node.js ਨਮੂਨਾ ਸੈਟਅਪ (Sample 08 - Windows Chat App)

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

### Foundry Local ਸੈਟਅਪ

Foundry Local ਨਮੂਨਿਆਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਲੋੜੀਂਦਾ ਹੈ। ਅਧਿਕਾਰਤ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਡਾਊਨਲੋਡ ਅਤੇ ਇੰਸਟਾਲ ਕਰੋ:

**ਇੰਸਟਾਲੇਸ਼ਨ:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ਮੈਨੂਅਲ**: [ਰਿਲੀਜ਼ ਪੇਜ](https://github.com/microsoft/Foundry-Local/releases) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ

**ਕੁਇਕ ਸਟਾਰਟ:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**ਨੋਟ**: Foundry Local ਤੁਹਾਡੇ ਹਾਰਡਵੇਅਰ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਵੈਰੀਐਂਟ ਨੂੰ ਆਪਣੇ ਆਪ ਚੁਣਦਾ ਹੈ (CUDA GPU, Qualcomm NPU, ਜਾਂ CPU)।

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### ਸਮੱਗਰੀ ਵਿਕਾਸ

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਮੁੱਖ ਤੌਰ 'ਤੇ **Markdown ਸਿੱਖਿਆ ਸਮੱਗਰੀ** ਸ਼ਾਮਲ ਹੈ। ਤਬਦੀਲੀਆਂ ਕਰਦੇ ਸਮੇਂ:

1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਸਹੀ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਸੋਧੋ
2. ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਪੈਟਰਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
3. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕੋਡ ਉਦਾਹਰਣਾਂ ਸਹੀ ਅਤੇ ਟੈਸਟ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ
4. ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਸੰਬੰਧਿਤ ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਨੂੰ ਅਪਡੇਟ ਕਰੋ (ਜਾਂ ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਇਸਦਾ ਧਿਆਨ ਰੱਖਣ ਦਿਓ)

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ

Module08 Python ਨਮੂਨਿਆਂ ਲਈ (ਨਮੂਨੇ 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

ਵਰਕਸ਼ਾਪ Python ਨਮੂਨਿਆਂ ਲਈ:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron ਨਮੂਨਾ (ਨਮੂਨਾ 08) ਲਈ:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

Python ਨਮੂਨਿਆਂ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਟੈਸਟ ਨਹੀਂ ਹਨ ਪਰ ਇਨ੍ਹਾਂ ਨੂੰ ਚਲਾਕੇ ਵੈਰੀਫਾਈ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron ਨਮੂਨੇ ਵਿੱਚ ਟੈਸਟ ਇੰਫਰਾਸਟਰਕਚਰ ਹੈ:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼

### ਸਮੱਗਰੀ ਵੈਰੀਫਿਕੇਸ਼ਨ

ਰਿਪੋਜ਼ਟਰੀ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਰਕਫਲੋਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਅਨੁਵਾਦਾਂ ਲਈ ਕੋਈ ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ ਦੀ ਲੋੜ ਨਹੀਂ।

**ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਲਈ ਮੈਨੂਅਲ ਵੈਰੀਫਿਕੇਸ਼ਨ:**
1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰਕੇ Markdown ਰੈਂਡਰਿੰਗ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
2. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੇ ਲਿੰਕ ਸਹੀ ਟਾਰਗਟਾਂ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦੇ ਹਨ
3. ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੇ ਕੋਡ ਸਨਿੱਪਟਾਂ ਨੂੰ ਟੈਸਟ ਕਰੋ
4. ਚੈੱਕ ਕਰੋ ਕਿ ਚਿੱਤਰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਲੋਡ ਹੋ ਰਹੇ ਹਨ

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

**Module08/nmūne/08 (Electron ਐਪ) ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਟੈਸਟਿੰਗ ਹੈ:**
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

**Python ਨਮੂਨਿਆਂ ਨੂੰ ਮੈਨੂਅਲ ਟੈਸਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ:**
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

## ਕੋਡ ਸਟਾਈਲ ਗਾਈਡਲਾਈਨ

### Markdown ਸਮੱਗਰੀ

- ਸਥਿਰ ਹੈਡਿੰਗ ਹਾਇਰਾਰਕੀ ਦੀ ਵਰਤੋਂ ਕਰੋ (# ਸਿਰਲੇਖ ਲਈ, ## ਮੁੱਖ ਸੈਕਸ਼ਨ ਲਈ, ### ਉਪ-ਸੈਕਸ਼ਨ ਲਈ)
- ਕੋਡ ਬਲਾਕਾਂ ਵਿੱਚ ਭਾਸ਼ਾ ਨਿਰਧਾਰਕ ਸ਼ਾਮਲ ਕਰੋ: ```python, ```bash, ```javascript
- ਟੇਬਲਾਂ, ਸੂਚੀਆਂ ਅਤੇ ਜ਼ੋਰ ਦੇਣ ਲਈ ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਲਾਈਨਾਂ ਨੂੰ ਪੜ੍ਹਨਯੋਗ ਰੱਖੋ (~80-100 ਅੱਖਰਾਂ ਦਾ ਲਕਸ਼, ਪਰ ਸਖ਼ਤ ਨਹੀਂ)
- ਅੰਦਰੂਨੀ ਹਵਾਲਿਆਂ ਲਈ ਰਿਸ਼ਤੇਦਾਰ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰੋ

### Python ਕੋਡ ਸਟਾਈਲ

- PEP 8 ਕਨਵੈਨਸ਼ਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਟਾਈਪ ਹਿੰਟ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਫੰਕਸ਼ਨ ਅਤੇ ਕਲਾਸਾਂ ਲਈ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
- ਅਰਥਪੂਰਨ ਵੈਰੀਏਬਲ ਨਾਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕੇਂਦਰਿਤ ਅਤੇ ਸੰਖੇਪ ਰੱਖੋ

### JavaScript/Node.js ਕੋਡ ਸਟਾਈਲ

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**ਮੁੱਖ ਕਨਵੈਨਸ਼ਨ:**
- ESLint ਕਨਫਿਗਰੇਸ਼ਨ ਨਮੂਨਾ 08 ਵਿੱਚ ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ
- Prettier ਕੋਡ ਫਾਰਮੈਟਿੰਗ ਲਈ
- ਆਧੁਨਿਕ ES6+ ਸਿੰਟੈਕਸ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਕੋਡਬੇਸ ਵਿੱਚ ਮੌਜੂਦਾ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰੋ

## ਪੁਲ ਰਿਕਵੇਸਟ ਗਾਈਡਲਾਈਨ

### ਯੋਗਦਾਨ ਵਰਕਫਲੋ

1. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ** ਅਤੇ `main` ਤੋਂ ਨਵੀਂ ਸ਼ਾਖਾ ਬਣਾਓ
2. **ਆਪਣੀਆਂ ਤਬਦੀਲੀਆਂ ਕਰੋ** ਕੋਡ ਸਟਾਈਲ ਗਾਈਡਲਾਈਨ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ
3. **ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਟੈਸਟ ਕਰੋ**
4. **ਸਪਸ਼ਟ ਸੁਨੇਹਿਆਂ ਨਾਲ ਕਮਿਟ ਕਰੋ** ਕਨਵੈਨਸ਼ਨਲ ਕਮਿਟ ਫਾਰਮੈਟ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ
5. **ਆਪਣੇ ਫੋਰਕ ਵਿੱਚ ਪੁਸ਼ ਕਰੋ** ਅਤੇ ਪੁਲ ਰਿਕਵੇਸਟ ਬਣਾਓ
6. **ਸਮੀਖਿਆ ਦੌਰਾਨ ਮੈਨਟੇਨਰਾਂ ਤੋਂ ਪ੍ਰਾਪਤ ਫੀਡਬੈਕ ਦਾ ਜਵਾਬ ਦਿਓ**

### ਸ਼ਾਖਾ ਨਾਮਕਰਨ ਕਨਵੈਨਸ਼ਨ

- `feature/<module>-<description>` - ਨਵੀਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜਾਂ ਸਮੱਗਰੀ ਲਈ
- `fix/<module>-<description>` - ਬੱਗ ਫਿਕਸ ਲਈ
- `docs/<description>` - ਦਸਤਾਵੇਜ਼ ਸੁਧਾਰਾਂ ਲਈ
- `refactor/<description>` - ਕੋਡ ਰੀਫੈਕਟਰੀਂਗ ਲਈ

### ਕਮਿਟ ਸੁਨੇਹਾ ਫਾਰਮੈਟ

[Conventional Commits](https://www.conventionalcommits.org/) ਦੀ ਪਾਲਣਾ ਕਰੋ:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ਉਦਾਹਰਣ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### ਸਿਰਲੇਖ ਫਾਰਮੈਟ
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### ਆਚਰ ਸੰਹਿਤਾ

ਸਾਰੇ ਯੋਗਦਾਨਕਰਤਾ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ਦੀ ਪਾਲਣਾ ਕਰਨ। ਯੋਗਦਾਨ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ਦੀ ਸਮੀਖਿਆ ਕਰੋ।

### ਪੇਸ਼ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਲਈ:**
- ਸਾਰੇ ਸੋਧੇ ਹੋਏ Markdown ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰੋ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਲਿੰਕ ਅਤੇ ਚਿੱਤਰ ਸਹੀ ਕੰਮ ਕਰਦੇ ਹਨ
- ਟਾਈਪੋ ਅਤੇ ਵਿਆਕਰਣ ਦੀਆਂ ਗਲਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ

**ਨਮੂਨਾ ਕੋਡ ਤਬਦੀਲੀਆਂ ਲਈ (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python ਨਮੂਨਾ ਤਬਦੀਲੀਆਂ ਲਈ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਨਮੂਨਾ ਸਫਲਤਾਪੂਰਵਕ ਚਲਦਾ ਹੈ
- ਗਲਤੀ ਸੰਭਾਲਣ ਦੀ ਜਾਂਚ ਕਰੋ
- Foundry Local ਨਾਲ ਅਨੁਕੂਲਤਾ ਦੀ ਜਾਂਚ ਕਰੋ

### ਸਮੀਖਿਆ ਪ੍ਰਕਿਰਿਆ

- ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਦੀ ਸਹੀਤਾ ਅਤੇ ਸਪਸ਼ਟਤਾ ਲਈ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਂਦੀ ਹੈ
- ਕੋਡ ਨਮੂਨਿਆਂ ਨੂੰ ਕਾਰਗਰਤਾ ਲਈ ਟੈਸਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ
- ਅਨੁਵਾਦ ਅਪਡੇਟ GitHub Actions ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ

## ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ

**ਮਹੱਤਵਪੂਰਨ:** ਇਹ ਰਿਪੋਜ਼ਟਰੀ GitHub Actions ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

- ਅਨੁਵਾਦ `/translations/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹਨ (50+ ਭਾਸ਼ਾਵਾਂ)
- `co-op-translator.yml` ਵਰਕਫਲੋ ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ
- **ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨੂੰ ਮੈਨੂਅਲ ਤੌਰ 'ਤੇ ਸੋਧੋ ਨਾ** - ਇਹਨਾਂ ਨੂੰ ਓਵਰਰਾਈਟ ਕੀਤਾ ਜਾਵੇਗਾ
- ਰੂਟ ਅਤੇ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਸਿਰਫ਼ ਅੰਗਰੇਜ਼ੀ ਸਰੋਤ ਫਾਈਲਾਂ ਸੋਧੋ
- ਅਨੁਵਾਦ `main` ਸ਼ਾਖਾ ਵਿੱਚ ਪੁਸ਼ ਕਰਨ 'ਤੇ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਜਨਰੇਟ ਹੁੰਦੇ ਹਨ

## Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਅਧਿਕਤਮ Module08 ਨਮੂਨਿਆਂ ਨੂੰ Microsoft Foundry Local ਚਲਾਉਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

### ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਸੈਟਅਪ

**Foundry Local ਇੰਸਟਾਲ ਕਰੋ:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ਇੰਸਟਾਲ ਕਰੋ:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ਸ਼ੁਰੂ ਕਰਨਾ
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

### SDK ਵਰਤੋਂ (Python)
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

### Foundry Local ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### ਨਮੂਨਿਆਂ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਅਧਿਕਤਮ ਨਮੂਨੇ ਇਹ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ:
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

**ਨੋਟ**: ਜਦੋਂ `FoundryLocalManager` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, SDK ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸੇਵਾ ਖੋਜ ਅਤੇ ਮਾਡਲ ਲੋਡਿੰਗ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਮਾਡਲ ਅਲੀਅਸ (ਜਿਵੇਂ `phi-3.5-mini`) ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਕਿ ਤੁਹਾਡੇ ਹਾਰਡਵੇਅਰ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਵੈਰੀਐਂਟ ਚੁਣਿਆ ਗਿਆ ਹੈ।

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

### ਸਮੱਗਰੀ ਡਿਪਲੌਇਮੈਂਟ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਮੁੱਖ ਤੌਰ 'ਤੇ ਦਸਤਾਵੇਜ਼ ਹੈ - ਸਮ
10. **10-ਫਾਊਂਡਰੀ ਟੂਲਜ਼ ਫਰੇਮਵਰਕ** - LangChain/Semantic Kernel ਇੰਟੀਗ੍ਰੇਸ਼ਨ

### ਵਰਕਸ਼ਾਪ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ

ਵਰਕਸ਼ਾਪ ਵਿੱਚ 6 ਤਰੱਕੀਸ਼ੀਲ ਸੈਸ਼ਨ ਸ਼ਾਮਲ ਹਨ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਵਿਹੰਗਮ ਅਮਲ ਹਨ:

1. **ਸੈਸ਼ਨ 01** - Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ ਚੈਟ ਬੂਟਸਟ੍ਰੈਪ
2. **ਸੈਸ਼ਨ 02** - RAG ਪਾਈਪਲਾਈਨ ਅਤੇ RAGAS ਨਾਲ ਮੁਲਾਂਕਣ
3. **ਸੈਸ਼ਨ 03** - ਖੁੱਲ੍ਹੇ-ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਬੈਂਚਮਾਰਕਿੰਗ
4. **ਸੈਸ਼ਨ 04** - ਮਾਡਲ ਤੁਲਨਾ ਅਤੇ ਚੋਣ
5. **ਸੈਸ਼ਨ 05** - ਮਲਟੀ-ਏਜੰਟ ਆਰਕੇਸਟ੍ਰੇਸ਼ਨ ਸਿਸਟਮ
6. **ਸੈਸ਼ਨ 06** - ਮਾਡਲ ਰੂਟਿੰਗ ਅਤੇ ਪਾਈਪਲਾਈਨ ਪ੍ਰਬੰਧਨ

ਹਰ ਨਮੂਨਾ Foundry Local ਨਾਲ ਐਜ AI ਵਿਕਾਸ ਦੇ ਵੱਖ-ਵੱਖ ਪਹਲੂਆਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

### ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਵਿਚਾਰ

- SLMs ਐਜ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਅਨੁਕੂਲਿਤ ਹਨ (2-16GB RAM)
- ਸਥਾਨਕ ਇੰਫਰੈਂਸ 50-500ms ਜਵਾਬ ਸਮਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
- ਕੁਆਂਟੀਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ 75% ਆਕਾਰ ਘਟਾਉਣ ਅਤੇ 85% ਪ੍ਰਦਰਸ਼ਨ ਰਿਟੇਨਸ਼ਨ ਹਾਸਲ ਕਰਦੀਆਂ ਹਨ
- ਸਥਾਨਕ ਮਾਡਲਾਂ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਗੱਲਬਾਤ ਦੀ ਸਮਰੱਥਾ

### ਸੁਰੱਖਿਆ ਅਤੇ ਗੋਪਨੀਯਤਾ

- ਸਾਰਾ ਪ੍ਰੋਸੈਸਿੰਗ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਹੁੰਦਾ ਹੈ - ਕੋਈ ਡਾਟਾ ਕਲਾਉਡ ਨੂੰ ਨਹੀਂ ਭੇਜਿਆ ਜਾਂਦਾ
- ਗੋਪਨੀਯਤਾ-ਸੰਵੇਦਨਸ਼ੀਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਚਿਤ (ਹੈਲਥਕੇਅਰ, ਫਾਇਨੈਂਸ)
- ਡਾਟਾ ਸਰਵਰੈਂਟੀ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ
- Foundry Local ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਥਾਨਕ ਹਾਰਡਵੇਅਰ 'ਤੇ ਚਲਦਾ ਹੈ

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

### ਦਸਤਾਵੇਜ਼

- **ਮੁੱਖ README**: [README.md](README.md) - ਰਿਪੋਜ਼ਿਟਰੀ ਝਲਕ ਅਤੇ ਸਿੱਖਣ ਦੇ ਰਾਹ
- **ਅਧਿਐਨ ਗਾਈਡ**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - ਸਿੱਖਣ ਦੇ ਸਰੋਤ ਅਤੇ ਸਮਾਂ-ਸਾਰਣੀ
- **ਸਹਾਇਤਾ**: [SUPPORT.md](SUPPORT.md) - ਮਦਦ ਕਿਵੇਂ ਪ੍ਰਾਪਤ ਕਰਨੀ ਹੈ
- **ਸੁਰੱਖਿਆ**: [SECURITY.md](SECURITY.md) - ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ ਦੀ ਰਿਪੋਰਟਿੰਗ

### ਕਮਿਊਨਿਟੀ ਸਹਾਇਤਾ

- **GitHub Issues**: [ਬੱਗ ਰਿਪੋਰਟ ਕਰੋ ਜਾਂ ਫੀਚਰ ਦੀ ਮੰਗ ਕਰੋ](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [ਸਵਾਲ ਪੁੱਛੋ ਅਤੇ ਵਿਚਾਰ ਸਾਂਝੇ ਕਰੋ](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local ਨਾਲ ਤਕਨੀਕੀ ਸਮੱਸਿਆਵਾਂ](https://github.com/microsoft/Foundry-Local/issues)

### ਸੰਪਰਕ

- **ਮੈਂਟੇਨਰਜ਼**: ਵੇਖੋ [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ**: [SECURITY.md](SECURITY.md) ਵਿੱਚ ਜਿੰਮੇਵਾਰ ਖੁਲਾਸੇ ਦੀ ਪਾਲਣਾ ਕਰੋ
- **Microsoft Support**: ਕਾਰੋਬਾਰੀ ਸਹਾਇਤਾ ਲਈ, Microsoft ਗਾਹਕ ਸੇਵਾ ਨਾਲ ਸੰਪਰਕ ਕਰੋ

### ਵਾਧੂ ਸਰੋਤ

- **Microsoft Learn**: [AI ਅਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸਿੱਖਣ ਦੇ ਰਾਹ](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ਦਸਤਾਵੇਜ਼**: [ਆਧਿਕਾਰਿਕ ਦਸਤਾਵੇਜ਼](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **ਕਮਿਊਨਿਟੀ ਨਮੂਨੇ**: ਕਮਿਊਨਿਟੀ ਯੋਗਦਾਨਾਂ ਲਈ [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) ਚੈੱਕ ਕਰੋ

---

**ਇਹ ਇੱਕ ਸਿੱਖਣ ਲਈ ਰਿਪੋਜ਼ਿਟਰੀ ਹੈ ਜੋ ਐਜ AI ਵਿਕਾਸ ਸਿਖਾਉਣ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਹੈ। ਮੁੱਖ ਯੋਗਦਾਨ ਪੈਟਰਨ ਸਿੱਖਣ ਦੇ ਸਮੱਗਰੀ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣਾ ਅਤੇ ਐਜ AI ਸੰਕਲਪਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਸ਼ਾਮਲ/ਵਧਾਉਣਾ ਹੈ।**

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।