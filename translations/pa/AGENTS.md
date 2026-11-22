# AGENTS.md

> **ਨਵੀਆਂ ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ EdgeAI ਵਿੱਚ ਯੋਗਦਾਨ ਦੇਣ ਵਾਲਿਆਂ ਲਈ ਡਿਵੈਲਪਰ ਗਾਈਡ**
> 
> ਇਹ ਦਸਤਾਵੇਜ਼ ਵਿਕਾਸਕਾਰਾਂ, AI ਏਜੰਟਾਂ ਅਤੇ ਇਸ ਰਿਪੋਜ਼ੀਟਰੀ ਨਾਲ ਕੰਮ ਕਰਨ ਵਾਲੇ ਯੋਗਦਾਨਕਾਰੀਆਂ ਲਈ ਵਿਸ਼ਤ੍ਰਿਤ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਹ ਸੈੱਟਅੱਪ, ਵਿਕਾਸ ਵਰਕਫਲੋਜ਼, ਟੈਸਟਿੰਗ ਅਤੇ ਸ੍ਰੇਸ਼ਠ ਅਭਿਆਸਾਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।
> 
> **ਆਖਰੀ ਅਪਡੇਟ**: 30 ਅਕਤੂਬਰ, 2025 | **ਦਸਤਾਵੇਜ਼ ਸੰਸਕਰਣ**: 3.0

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- [ਪਰਿਯੋਜਨਾ ਜਾਇਜ਼ਾ](#ਪਰਿਯੋਜਨਾ-ਜਾਇਜ਼ਾ)
- [ਰਿਪੋਜ਼ੀਟਰੀ ਬਣਤਰ](#ਰਿਪੋਜ਼ੀਟਰੀ-ਬਣਤਰ)
- [ਜ਼ਰੂਰੀ ਪਹਿਲਾਂ ਦੀਆਂਆਂ ਸ਼ਰਤਾਂ](#ਜ਼ਰੂਰੀ-ਪਹਿਲਾਂ-ਦੀਆਂਆਂ-ਸ਼ਰਤਾਂ)
- [ਸੈੱਟਅੱਪ ਕਮਾਂਡਾਂ](#ਸੈੱਟਅੱਪ-ਕਮਾਂਡਾਂ)
- [ਵਿਕਾਸ ਵਰਕਫਲੋ](#ਵਿਕਾਸ-ਵਰਕਫਲੋ)
- [ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼](#ਟੈਸਟਿੰਗ-ਨਿਰਦੇਸ਼)
- [ਕੋਡ ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼](#ਕੋਡ-ਸਟਾਈਲ-ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼)
- [ਪੁਲ ਰਿਕਵੇਸਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼](#ਪੁਲ-ਰਿਕਵੇਸਟ-ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼)
- [ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ](#ਅਨੁਵਾਦ-ਪ੍ਰਣਾਲੀ)
- [Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ](#foundry-local-ਇੰਟੀਗ੍ਰੇਸ਼ਨ)
- [ਬਿਲਡ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ](#ਬਿਲਡ-ਅਤੇ-ਡਿਪਲੋਇਮੈਂਟ)
- [ਆਮ ਮੁੱਦੇ ਅਤੇ ਸਮੱਸਿਆ-ਸੁਲਝਾਉ](#ਆਮ-ਮੁੱਦੇ-ਅਤੇ-ਸਮੱਸਿਆ-ਸੁਲਝਾਉ)
- [ਵਾਧੂ ਸਰੋਤ](#ਵਾਧੂ-ਸਰੋਤ)
- [ਪਰਿਯੋਜਨਾ-ਖਾਸ ਨੋਟਸ](#ਪਰਿਯੋਜਨਾ-ਖਾਸ-ਨੋਟਸ)
- [ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ](#ਮਦਦ-ਪ੍ਰਾਪਤ-ਕਰਨਾ)

## ਪਰਿਯੋਜਨਾ ਜਾਇਜ਼ਾ

EdgeAI for Beginners ਇੱਕ ਵਿਸ਼ਤ੍ਰਿਤ ਸ਼ੈක්ෂਣਕ ਰਿਪੋਜ਼ੀਟਰੀ ਹੈ ਜੋ Смਾਲ ਲੈਂਗਵੇਜ ਮਾਡਲਾਂ (SLMs) ਨਾਲ Edge AI ਵਿਕਾਸ ਸਿਖਾਉਂਦਾ ਹੈ। ਇਹ ਕੋਰਸ EdgeAI ਦੇ ਮੁਢਲੀ ਗੱਲਾਂ, ਮਾਡਲ ਤैनਾਤੀ, ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ ਅਤੇ Microsoft Foundry Local ਅਤੇ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਤਪਾਦਨ-ਤਿਆਰ ਅਮਲ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- Python 3.8+ (AI/ML ਨਮੂਨੇ ਲਈ ਪ੍ਰਮੁੱਖ ਭਾਸ਼ਾ)
- .NET C# (AI/ML ਨਮੂਨੇ)
- JavaScript/Node.js ਇਲੈਕਟ੍ਰਾਨ ਨਾਲ (ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI ਟੂਲਕਿਟ
- OpenAI SDK
- AI ਫਰੇਮਵਰਕ: LangChain, Semantic Kernel, Chainlit
- ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ਰਿਪੋਜ਼ੀਟਰੀ ਕਿਸਮ:** 8 ਮਾਡਿਊਲ ਅਤੇ 10 ਵਿਸ਼ਤ੍ਰਿਤ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਸਿਖਲਾਈ ਰਿਪੋਜ਼ੀਟਰੀ

**ਆਰਕੀਟੈਕਚਰ:** ਪ੍ਰੈਕਟਿਕਲ ਨਮੂਨਿਆਂ ਨਾਲ ਇੱਕ ਬਹੁ-ਮੋਡੀਊਲ ਸਿੱਖਣ ਦਾ ਰਸਤਾ ਜੋ एज AI ਦੀ ਤੈਨਾਤੀ ਦੇ ਪੈਟਰਨ ਦਿਖਾਉਂਦਾ ਹੈ

## ਰਿਪੋਜ਼ੀਟਰੀ ਬਣਤਰ

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

## ਜ਼ਰੂਰੀ ਪਹਿਲਾਂ ਦੀਆਂਆਂ ਸ਼ਰਤਾਂ

### ਲੋੜੀਂਦੇ ਸੰਦ

- **Python 3.8+** - AI/ML ਨਮੂਨੇ ਅਤੇ ਨੋਟਬੁੱਕਸ ਲਈ
- **Node.js 16+** - ਇਲੈਕਟ੍ਰਾਨ ਨਮੂਨੇ ਐਪ ਲਈ
- **Git** - ਵਰਜ਼ਨ ਕੰਟਰੋਲ ਲਈ
- **Microsoft Foundry Local** - AI ਮਾਡਲਾਂ ਨੂੰ ਲੋਕਲੀ ਚਲਾਉਣ ਲਈ

### ਸਿਫਾਰਸ਼ੀ ਸੰਦ

- **Visual Studio Code** - Python, Jupyter, ਅਤੇ Pylance ਐਕਸਟेंसਨਜ਼ ਨਾਲ
- **Windows Terminal** - ਬਿਹਤਰ ਕਮਾਂਡ-ਲਾਈਨ ਅਨਭਵ ਲਈ (Windows ਉਪਭੋਗਤਾਵਾਂ ਲਈ)
- **Docker** - ਕੰਟੇਨਰਾਇਜ਼ਡ ਵਿਕਾਸ ਲਈ (ਆਪਸ਼ਨਲ)

### ਪ੍ਰਣਾਲੀ ਦੀਆਂ ਮੰਗਾਂ

- **RAM**: ਘੱਟੋ-ਘੱਟ 8GB, ਬਹੁ-ਮਾਡਲ ਸਥਿਤੀਆਂ ਲਈ 16GB+ ਸਿਫਾਰਸ਼ੀ
- **ਸੰਚਾਰਣ ਸਥਾਨ**: ਮਾਡਲਾਂ ਅਤੇ ਨਿਰਭਰਤਾ ਲਈ 10GB+ ਖਾਲੀ ਜਗ੍ਹਾ
- **ਓਐਸ**: Windows 10/11, macOS 11+, ਜਾਂ Linux (Ubuntu 20.04+)
- **ਹਾਰਡਵੇਅਰ**: AVX2 ਸਮਰਥਿਤ CPU; GPU (CUDA, Qualcomm NPU) ਵਿਕਲਪਕ ਪਰ ਸਿਫਾਰਸ਼ੀ

### ਗਿਆਨ ਦੀਆਂ ਮੰਗਾਂ

- Python ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ
- ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸਾਂ ਨਾਲ ਜਾਣੂ ਹੋਣਾ
- AI/ML ਧਾਰਣਾਵਾਂ ਦੀ ਸਮਝ (ਨਮੂਨਾ ਵਿਕਾਸ ਲਈ)
- Git ਵਰਕਫਲੋ ਅਤੇ ਪੁਲ ਰਿਕਵੇਸਟ ਪ੍ਰਕਿਰਿਆਵਾਂ

## ਸੈੱਟਅੱਪ ਕਮਾਂਡਾਂ

### ਰਿਪੋਜ਼ੀਟਰੀ ਸੈੱਟਅੱਪ

```bash
# ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# ਕੋਈ ਬਿਲਡ ਕਦਮ ਲੋੜੀਂਦਾ ਨਹੀਂ - ਇਹ ਮੁੱਖ ਰੂਪ ਵਿੱਚ ਇੱਕ ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਰਿਪੋਜ਼ਟਰੀ ਹੈ
```

### Python ਨਮੂਨਾ ਸੈੱਟਅੱਪ (Module08 ਅਤੇ ਵਰਕਸ਼ਾਪ ਨਮੂਨੇ)

```bash
# ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਐਕਟੀਵੇਟ ਕਰੋ
python -m venv .venv
# ਵਿੰਡੋਜ਼ 'ਤੇ
.venv\Scripts\activate
# ਮੈਕਓਐਸ/ਲਿਨਕਸ 'ਤੇ
source .venv/bin/activate

# ਫਾਊਂਡਰੀ ਲੋਕਲ SDK ਅਤੇ ਨਿਰਭਰਤਾਵਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ
pip install foundry-local-sdk openai

# ਮੋਡੀਊਲ08 ਨਮੂਨਿਆਂ ਲਈ ਵਾਧੂ ਨਿਰਭਰਤਾਵਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ
cd Module08
pip install -r requirements.txt

# ਵਰਕਸ਼ਾਪ ਦੀਆਂ ਨਿਰਭਰਤਾਵਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ
cd ../Workshop
pip install -r requirements.txt
```

### Node.js ਨਮੂਨਾ ਸੈੱਟਅੱਪ (ਨਮੂਨਾ 08 - Windows ਚੈੱਟ ਐਪ)

```bash
cd Module08/samples/08
npm install

# ਵਿਕਾਸ ਮੋਡ ਵਿੱਚ ਸ਼ੁਰੂ ਕਰੋ
npm run dev

# ਉਤਪਾਦਨ ਲਈ ਬਣਾਓ
npm run build

# ਇੰਸਟਾਲਰ ਬਣਾਓ
npm run dist
```

### Foundry Local ਸੈੱਟਅੱਪ

Foundry Local ਸੈਂਪਲ ਚਲਾਉਣ ਲਈ ਲਾਜ਼ਮੀ ਹੈ। ਅਧਿਕਾਰਿਤ ਰਿਪੋਜ਼ੀਟਰੀ ਤੋਂ ਡਾਊਨਲੋਡ ਅਤੇ ਸਥਾਪਿਤ ਕਰੋ:

**ਸਥਾਪਨਾ:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ਮੈਨੂਅਲ**: [ਰਿਲੀਜ਼ ਪੇਜ](https://github.com/microsoft/Foundry-Local/releases) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ

**ਤੇਜ਼ ਸ਼ੁਰੂਆਤ:**
```bash
# ਆਪਣਾ ਪਹਿਲਾ ਮਾਡਲ ਚਲਾਓ (ਜ਼ਰੂਰਤ ਪੈਣ 'ਤੇ ਆਟੋ-ਡਾਊਨਲੋਡ ਹੋ ਜਾਂਦਾ ਹੈ)
foundry model run phi-4-mini

# ਉਪਲਬਧ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
foundry model ls

# ਸੇਵਾ ਹਾਲਤ ਚੈੱਕ ਕਰੋ
foundry service status
```

**ਟਿੱਪਣੀ**: Foundry Local ਆਪਣੇ ਹਾਰਡਵੇਅਰ (CUDA GPU, Qualcomm NPU, ਜਾਂ CPU) ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਵੈਰੀਅੰਟ автоматически ਚੁਣਦਾ ਹੈ।

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### ਸਮੱਗਰੀ ਦਾ ਵਿਕਾਸ

ਇਹ ਰਿਪੋਜ਼ੀਟਰੀ ਮੁੱਖ ਤੌਰ 'ਤੇ **Markdown ਸਿੱਖਣ ਵਾਲੀ ਸਮੱਗਰੀ** ਹੈ। ਜਦੋਂ ਤਬਦੀਲੀਆਂ ਕਰੋ:

1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਸੰਪਾਦਿਤ ਕਰੋ
2. ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਪੈਟਰਨ ਦਾ ਪਾਲਣ ਕਰੋ
3. ਕੋਡ ਉਦਾਹਰਣਾਂ ਨੂੰ ਸਹੀ ਅਤੇ ਪਰਖਿਆ ਹੋਇਆ ਬਣਾਓ
4. ਜ਼ਰੂਰਤ ਪੈਣ ਤੇ ਟ੍ਰਾਂਸਲੇਟ ਕੀਤੀ ਸਮੱਗਰੀ ਨੂੰ ਅਪਡੇਟ ਕਰੋ (ਜਾਂ ਆਪੋ-ਆਪ ਨੂੰਸਾਰ ਕੰਮ ਹੋਣ ਦਿਓ)

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ

ਮੋਡੀਊਲ08 Python ਨਮੂਨਾਂ (ਨਮੂਨਾ 01-07, 09-10) ਲਈ:
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

ਵਰਕਸ਼ਾਪ Python ਨਮੂਨਾਂ ਲਈ:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

ਇਲੈਕਟ੍ਰਾਨ ਨਮੂਨਾ (ਨਮੂਨਾ 08) ਲਈ:
```bash
cd Module08/samples/08
npm run dev  # ਹੌਟ ਰੀਲੋਡ ਨਾਲ ਵਿਕਾਸ
```

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

Python ਨਮੂਨਾਂ ਲਈ ਕੋਈ ਸਵਚਾਲਿਤ ਟੈਸਟਾਂ ਨਹੀਂ ਹਨ ਪਰ ਇਹਨਾਂ ਨੂੰ ਚਲਾਕੇ ਵੈਧ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:
```bash
# ਬੁਨਿਆਦੀ ਗੱਲਬਾਤ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਜਾਂਚ ਕਰੋ
python samples/01/chat_quickstart.py "Hello"

# ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਨਾਲ ਜਾਂਚ ਕਰੋ
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

ਇਲੈਕਟ੍ਰਾਨ ਨਮੂਨਾ ਵਿੱਚ ਟੈਸਟਾਂ ਦਾ ਢਾਂਚਾ ਹੈ:
```bash
cd Module08/samples/08
npm test           # ਯੂਨਿਟ ਟੈਸਟ ਚਲਾਓ
npm run test:e2e   # ਅੰਤ ਤੋਂ ਅੰਤ ਤੱਕ ਟੈਸਟ ਚਲਾਓ
npm run lint       # ਕੋਡ ਸਟਾਈਲ ਚੈੱਕ ਕਰੋ
```

## ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼

### ਸਮੱਗਰੀ ਦੀ ਵੈਧਤਾ

ਇਹ ਰਿਪੋਜ਼ੀਟਰੀ ਸਵਚਾਲਿਤ ਅਨੁਵਾਦ ਵਰਕਫਲੋਜ਼ ਵਰਤਦਾ ਹੈ। ਅਨੁਵਾਦਾਂ ਲਈ ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ ਦੀ ਲੋੜ ਨਹੀਂ।

**ਸਮੱਗਰੀ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਲਈ ਮੈਨੂਅਲ ਵੈਧਤਾ:**
1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰਕੇ Markdown ਰੈਂਡਰਿੰਗ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
2. ਸਾਰੇ ਲਿੰਕ ਸਹੀ ਟਾਰਗਟਾਂ ਵੱਲ ਜਾ ਰਹੇ ਹਨ ਇਹ ਪੱਕਾ ਕਰੋ
3. ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕੋਡ ਸਨਿੱਪਿਟਾਂ ਨੂੰ ਟੈਸਟ ਕਰੋ
4. ਤਸਵੀਰਾਂ ਸਹੀ ਤਰ੍ਹਾਂ ਲੋਡ ਹੋ ਰਹੀਆਂ ਹਨ ਜਾਂ ਨਹੀਂ ਦੇਖੋ

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

**Module08/samples/08 (ਇਲੈਕਟ੍ਰਾਨ ਐਪ) ਵਿੱਚ ਵਿਸ਼ਤ੍ਰਿਤ ਟੈਸਟਿੰਗ ਹੈ:**
```bash
cd Module08/samples/08

# ਸਾਰੇ ਟੈਸਟ ਚਲਾਓ
npm test

# ਸਿਰਫ ਯੂਨਿਟ ਟੈਸਟ ਚਲਾਓ
npm test -- --testPathPattern=unit

# ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟ ਚਲਾਓ
npm run test:integration

# E2E ਟੈਸਟ ਚਲਾਓ
npm run test:e2e

# ਟੈਸਟ ਕਵਰੇਜ ਦੀ ਜਾਂਚ ਕਰੋ
npm test -- --coverage
```

**Python ਨਮੂਨਾਂ ਨੂੰ ਮੈਨੂਅਲ ਟੈਸਟ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ:**
```bash
# ਮੋਡੀਊਲ08 ਨਮੂਨੇ
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# ਵਰਕਸ਼ਾਪ ਨਮੂਨੇ
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# ਵਰਕਸ਼ਾਪ ਪ੍ਰਮਾਣਕਰਨ ਸੰਦ ਵਰਤੋ
cd Workshop/scripts
python validate_samples.py  # ਵਾਕਰਚਨਾ ਅਤੇ ਇੰਪੋਰਟਸ ਦਾ ਪ੍ਰਮਾਣਕਰਨ ਕਰੋ
python test_samples.py      # ਸ್ಮੋਕ ਟੈਸਟ ਚਲਾਓ
```

## ਕੋਡ ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### Markdown ਸਮੱਗਰੀ

- ਇੱਕਸਾਰ ਹੈਡਿੰਗ ਹਾਇਰਾਰਕੀ ਵਰਤੋਂ (# ਸਿਰਲੇਖ ਲਈ, ## ਮੁੱਖ ਭਾਗਾਂ ਲਈ, ### ਉਪਭਾਗਾਂ ਲਈ)
- ਭਾਸ਼ਾ ਵਿਸ਼ੇਸ਼ਕਰਾਂ ਵਾਲੇ ਕੋਡ ਬਲਾਕ ਸ਼ਾਮਲ ਕਰੋ: ```python, ```bash, ```javascript
- ਮੇਜੂਲ, ਸੂਚੀਆਂ ਅਤੇ ਜ਼ੋਰ ਦੇਣ ਲਈ ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਫਾਲੋ ਕਰੋ
- ਲਾਈਨਾਂ ਨੂੰ ਪੜ੍ਹਨਯੋਗ ਰੱਖੋ (ਲਗਭਗ 80-100 ਅੱਖਰ, ਪਰ ਕਠੋਰ ਨਹੀਂ)
- ਅੰਦਰੂਨੀ ਹਵਾਲਿਆਂ ਲਈ ਸਪੰਧਤ ਲਿੰਕ ਵਰਤੋਂ

### Python ਕੋਡ ਸਟਾਈਲ

- PEP 8 ਰੀਤੀਆਂ ਪਾਲੋ
- ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ, ਤਾਈਪ ਸੂਚਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਫੰਕਸ਼ਨ ਅਤੇ ਕਲਾਸਾਂ ਲਈ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
- ਮਤਲਬਪੂਰਨ ਵੇਰੀਏਬਲ ਨਾਮ ਵਰਤੋਂ
- ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕੇਂਦਰਿਤ ਅਤੇ ਸੰਕੁਚਿਤ ਰੱਖੋ

### JavaScript/Node.js ਕੋਡ ਸਟਾਈਲ

```bash
# ਇਲੈਕਟ੍ਰਾਨ ਨਮੂਨਾ ESLint ਕনਫਿਗਰੇਸ਼ਨ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ
cd Module08/samples/08
npm run lint        # ਸਟਾਇਲ ਸਮੱਸਿਆਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
npm run lint:fix    # ਸਵੈ-ਸੁਧਾਰ ਸਟਾਇਲ ਸਮੱਸਿਆਵਾਂ
npm run format      # ਪ੍ਰੀਟੀਅਰ ਨਾਲ ਫਾਰਮੈਟ ਕਰੋ
```

**ਮੁੱਖ ਰੀਤੀਆਂ:**
- ਨਮੂਨਾ 08 ਵਿੱਚ ESLint ਸੰਰਚਨਾ ਦਿੱਤੀ ਗਈ ਹੈ
- ਕੋਡ ਫਾਰਮੈਟਿੰਗ ਲਈ Prettier
- ਆਧੁਨਿਕ ES6+ ਵਿਆਕਰਨ ਦੀ ਵਰਤੋਂ
- ਕੋਡਬੇਸ ਵਿੱਚ ਮੌਜੂਦਾ ਨਮੂਨਿਆਂ ਦੀ ਪਾਲਣਾ

## ਪੁਲ ਰਿਕਵੇਸਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### ਯੋਗਦਾਨ ਵਰਕਫਲੋ

1. **ਰਿਪੋਜ਼ੀਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ** ਅਤੇ `main` ਤੋਂ ਨਵੀਂ ਬਰਾਂਚ ਬਣਾਓ
2. **ਆਪਣੀਆਂ ਤਬਦੀਲੀਆਂ ਕਰੋ** ਕੋਡ ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ
3. **ਚੰਗੀ ਤਰ੍ਹਾਂ ਟੈਸਟ ਕਰੋ** ਉਪਰ ਦਿੱਤੇ ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ
4. **ਸਪਸ਼ਟ ਸੁਨੇਹਿਆਂ ਨਾਲ ਕਮਿਟ ਕਰੋ** ਪ੍ਰਚਲਿਤ ਕਮਿਟ ਫਾਰਮੈਟ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ
5. **ਆਪਣੇ ਫੋਰਕ 'ਤੇ ਪੁਸ਼ ਕਰੋ** ਅਤੇ ਪੁਲ ਰਿਕਵੇਸਟ ਬਣਾਓ
6. **ਸਮੀਖਿਆ ਦੌਰਾਨ ਮਾਈਨਟੇਨਰਾਂ ਤੋਂ ਪ੍ਰਤੀਕ੍ਰਿਆ ਦੇਵੋ**

### ਬਰਾਂਚ ਨੇਮਿੰਗ ਪ੍ਰਣਾਲੀ

- `feature/<module>-<description>` - ਨਵੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜਾਂ ਸਮੱਗਰੀ ਲਈ
- `fix/<module>-<description>` - ਬਗ ਫਿਕਸ ਲਈ
- `docs/<description>` - ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਸੁਧਾਰ ਲਈ
- `refactor/<description>` - ਕੋਡ ਰੀਫੈਕਟਰਨਿੰਗ ਲਈ

### ਕਮਿਟ ਸੁਨੇਹਾ ਫਾਰਮੈਟ

[Conventional Commits](https://www.conventionalcommits.org/) ਦੀ ਪਾਲਣਾ ਕਰੋ:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ਉਦਾਹਰਣਾਂ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### ਸਿਰਲੇਖ ਫਾਰਮੈਟ
```
[ModuleXX] Brief description of change
```
 ਜਾਂ
```
[Module08/samples/XX] Description for sample changes
```

### ਆਚਰਨ ਕੋਡ

ਸਾਰੇ ਯੋਗਦਾਨਕਾਰੀਆਂ ਨੂੰ [Microsoft Open Source ਦੇ ਆਚਰਨ ਕੋਡ](https://opensource.microsoft.com/codeofconduct/) ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਯੋਗਦਾਨ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ਨੂੰ ਦੇਖੋ।

### ਜਮ੍ਹਾਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਸਮੱਗਰੀ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਲਈ:**
- ਸਾਰੇ ਸੋਧੇ ਗਏ Markdown ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰੋ
- ਲਿੰਕਾਂ ਅਤੇ ਤਸਵੀਰਾਂ ਦੀ ਜਾਂਚ ਕਰੋ ਕਿ ਠੀਕ ਕੰਮ ਕਰ ਰਹੀਆਂ ਹਨ
- ਟਾਈਪੋ ਅਤੇ ਵਿਆਕਰਨ ਗਲਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ

**ਨਮੂਨਾ ਕੋਡ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਲਈ (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python ਨਮੂਨਿਆਂ ਲਈ:**
- ਨਮੂਨਾ ਸਫਲਤਾਪੂਰਵਕ ਚੱਲਦਾ ਹੈ ਇਹ ਟੈਸਟ ਕਰੋ
- ਗਲਤੀ ਸਹਿਣਸ਼ੀਲਤਾ ਨੂੰ ਜਾਂਚੋ
- Foundry Local ਨਾਲ ਅਨੁਕੂਲਤਾ ਦੀ ਜਾਂਚ ਕਰੋ

### ਸਮੀਖਿਆ ਪ੍ਰਕਿਰਿਆ

- ਸਿੱਖਣ ਸਮੱਗਰੀ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਨੂੰ ਸਹੀ ਅਤੇ ਸਪਸ਼ਟਤਾ ਲਈ ਸਮੀਖਿਆ ਕੀਤਾ ਜਾਂਦਾ ਹੈ
- ਕੋਡ ਨਮੂਨਿਆਂ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਲਈ ਟੈਸਟਿੰਗ ਹੋਦੀ ਹੈ
- ਅਨੁਵਾਦ ਅਪਡੇਟ ਗਿਟਹੱਬ ਐਕਸ਼ਨਜ਼ ਦੁਆਰਾ ਸਵੈਚਾਲਿਤ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ

## ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ

**ਮਹੱਤਵਪੂਰਨ:** ਇਹ ਰਿਪੋਜ਼ੀਟਰੀ ਗਿਟਹੱਬ ਐਕਸ਼ਨਜ਼ ਰਾਹੀਂ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦ ਵਰਤਦਾ ਹੈ।

- ਅਨੁਵਾਦ `/translations/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹਨ (50+ ਭਾਸ਼ਾਵਾਂ)
- `co-op-translator.yml` ਵਰਕਫਲੋ ਰਾਹੀਂ ਸਵੈਚਾਲਿਤ
- **ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨੂੰ ਹੱਥੋਂ ਸੋਧੋ ਨਹੀਂ** - ਇਨ੍ਹਾਂ ਨੂੰ ਓਵਰਰਾਈਟ ਕਰ ਦਿੱਤਾ ਜਾਵੇਗਾ
- ਸਿਰਫ ਅੰਗਰੇਜ਼ੀ ਸੋਰਸ ਫਾਈਲਾਂ ਨੂੰ ਰੂਟ ਅਤੇ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸੋਧੋ
- ਅਨੁਵਾਦ `main` ਬਰਾਂਚ ਤੇ ਪੁਸ਼ ਹੋਣ 'ਤੇ ਆਪੋ-ਆਪ ਬਣਦੇ ਹਨ

## Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਜ਼ਿਆਦਾਤਰ Module08 ਨਮੂਨਿਆਂ ਨੂੰ Microsoft Foundry Local ਨੂੰ ਚੱਲਦੇ ਹੋਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

### ਸਥਾਪਨਾ ਅਤੇ ਸੈੱਟਅੱਪ

**Foundry Local ਇੰਸਟਾਲ ਕਰੋ:**
```bash
# ਵਿੰਡੋਜ਼
winget install Microsoft.FoundryLocal

# ਮੈਕਓਐਸ
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ਇੰਸਟਾਲ ਕਰੋ:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local ਸ਼ੁਰੂ ਕਰਨਾ
```bash
# ਸੇਵਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਮਾਡਲ ਚਲਾਓ (ਲੋੜ ਪੈਣ ‘ਤੇ ਆਟੋ-ਡਾਊਨਲੋਡ ਹੁੰਦਾ ਹੈ)
foundry model run phi-3.5-mini

# ਜਾਂ ਆਟੋਮੈਟਿਕ ਹਾਰਡਵੇਅਰ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਲਈ ਮਾਡਲ ਅਲੀਅਸ ਵਰਤੋਂ
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# ਸੇਵਾ ਦੀ ਹਾਲਤ ਚੈਕ ਕਰੋ
foundry service status

# ਉਪਲਬਧ ਮਾਡਲ ਦੀ ਸੂਚੀ ਬਣਾਓ
foundry model ls
```

### SDK ਵਰਤੋਂ (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# ਆਟੋਮੈਟਿਕ ਹਾਰਡਵੇਅਰ ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਲਈ ਮਾਡਲ ਉਪਨਾਮ ਵਰਤੋ
alias = "phi-4-mini"

# ਮੈਨੇਜਰ ਬਣਾਓ (ਸੇਵਾ ਆਪਣੇ ਆਪ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ ਅਤੇ ਮਾਡਲ ਲੋਡ ਕਰਦੀ ਹੈ)
manager = FoundryLocalManager(alias)

# ਸਥਾਨਕ ਫਾਊਂਡਰੀ ਸੇਵਾ ਲਈ OpenAI ਕਲਾਇੰਟ ਸੈੱਟ ਕਰੋ
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰੋ
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ
```bash
# ਸੇਵਾ ਦੀ ਸਥਿਤੀ ਅਤੇ ਐਂਡਪੌਇੰਟ
foundry service status

# ਲੋਡ ਕੀਤੇ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ (REST API)
curl http://localhost:<port>/v1/models

# ਨੋਟ: 'foundry service status' ਚਲਾਉਂਦੇ ਸਮੇਂ ਪੋਰਟ ਦਿਖਾਈ ਜਾਂਦੀ ਹੈ
```

### ਨਮੂਨਿਆਂ ਲਈ Environment Variables

ਜ਼ਿਆਦਾਤਰ ਨਮੂਨੇ ਇਹਨਾਂ Environment Variables ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ:
```bash
# ਫਾਉਂਡਰੀ ਲੋਕਲ ਕਨਫਿਗਰੇਸ਼ਨ
# ਧਿਆਨ ਦਿਓ: SDK (FoundryLocalManager) ਸਾਹਮਣੇ ਆਏ ਐਂਡਪੋਇੰਟ ਨੂੰ ਆਪਣੇ ਆਪ ਪਛਾਣਦਾ ਹੈ
set MODEL=phi-4-mini  # ਜਾਂ phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # ਸਥਾਨਕ ਵਰਤੋਂ ਲਈ ਲੋੜੀਂਦਾ ਨਹੀਂ

# ਹੱਥੋਂ ਐਂਡਪੋਇੰਟ (ਜੇ SDK ਨਹੀਂ ਵਰਤ ਰਹੇ)
# ਪੋਰਟ 'foundry service status' ਰਾਹੀਂ ਦਿਖਾਇਆ ਗਿਆ ਹੈ
set BASE_URL=http://localhost:<port>

# ਅਜ਼ੂਰ ਓਪਨਏਆਈ ਫੈਲਬੈਕ ਲਈ (ਵਿਕਲਪੀ)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**ਟਿੱਪਣੀ**: ਜਦੋਂ `FoundryLocalManager` ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਤਾਂ SDK ਆਪੇ ਸੇਵਾ ਖੋਜ ਅਤੇ ਮਾਡਲ ਲੋਡਿੰਗ ਸੰਭਾਲਦਾ ਹੈ। ਮਾਡਲ ਨਾਂ (ਜਿਵੇਂ `phi-3.5-mini`) ਤੁਹਾਡੇ ਹਾਰਡਵੇਅਰ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਵੈਰੀਅੰਟ ਚੁਣਨ ਦੀ ਗਾਰੰਟੀ ਦਿੰਦੇ ਹਨ।

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ

### ਸਮੱਗਰੀ ਡਿਪਲੋਇਮੈਂਟ

ਇਹ ਰਿਪੋਜ਼ੀਟਰੀ ਮੁੱਖ ਤੌਰ ਤੇ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਹੈ - ਸਮੱਗਰੀ ਲਈ ਕਿਸੇ ਬਿਲਡ ਪ੍ਰਕਿਰਿਆ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।

### ਨਮੂਨਾ ਐਪਲੀਕੈਸ਼ਨ ਬਿਲਡਿੰਗ

**ਇਲੈਕਟ੍ਰਾਨ ਐਪਲੀਕੇਸ਼ਨ (Module08/samples/08):**
```bash
cd Module08/samples/08

# ਵਿਕਾਸ ਬਿਲਡ
npm run dev

# ਉਤਪਾਦਨ ਬਿਲਡ
npm run build

# ਵਿਂਡੋਜ਼ ਇੰਸਟਾਲਰ ਬਣਾਓ
npm run dist

# ਪੋਰਟੇਬਲ ਐਗਜ਼ਿਕਿਊਟেবল ਬਣਾਓ
npm run pack
```

**Python ਨਮੂਨੇ:**
ਕੋਈ ਬਿਲਡ ਪ੍ਰਕਿਰਿਆ ਨਹੀਂ - ਨਮੂਨੇ ਸਿੱਧੇ Python ਇੰਟਰਪ੍ਰੀਟਰ ਨਾਲ ਚਲਾਏ ਜਾਂਦੇ ਹਨ।

## ਆਮ ਮੁੱਦੇ ਅਤੇ ਸਮੱਸਿਆ-ਸੁਲਝਾਉ

> **ਟਿੱਪ**: ਜਾਣੇ ਮਸਲਿਆਂ ਅਤੇ ਸਮਾਧਾਨਾਂ ਲਈ [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) ਚੈੱਕ ਕਰੋ।

### ਗੰਭੀਰ ਮੁੱਦੇ (ਅਵਰੋਧਕ)

#### Foundry Local ਨਾ ਚਲਣਾ
**ਮੁੱਦਾ:** ਨਮੂਨੇ ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ ਨਾਲ ਫੇਲ ਹੋ ਜਾਂਦੇ ਹਨ

**ਸਮਾਧਾਨ:**
```bash
# ਜਾਂਚੋ ਕਿ ਸੇਵਾ ਚੱਲ ਰਹੀ ਹੈ ਜਾਂ ਨਹੀਂ
foundry service status

# ਕਿਸੇ ਮਾਡਲ ਨਾਲ ਸੇਵਾ ਸ਼ੁਰੂ ਕਰੋ
foundry model run phi-4-mini

# ਜਾਂ ਖੁਦ ਸੇਵਾ ਸ਼ੁਰੂ ਕਰੋ
foundry service start

# ਲੋਡ ਕੀਤੇ ਮਾਡਲ ਦੀ ਸੂਚੀ ਦਿੱਖਾਓ
foundry model ls

# REST API ਰਾਹੀਂ ਪੁਸ਼ਟੀ ਕਰੋ (ਪੋਰਟ 'foundry service status' ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ)
curl http://localhost:<port>/v1/models
```

### ਆਮ ਮੁੱਦੇ (ਮਧ्यम)

#### Python ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਮੁੱਦੇ
**ਮੁੱਦਾ:** ਮੋਡੀਊਲ ਆਯਾਤ ਗਲਤੀਆਂ

**ਸਮਾਧਾਨ:**
```bash
# ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਿਰਚੁਅਲ ਵਾਤਾਵਰਨ ਸක්ਰਿਯ ਹੈ
# ਵਿਂਡੋਜ਼
.venv\Scripts\activate
# ਮੈਕਓਐਸ/Linux
source .venv/bin/activate

# ਡਿਪੈਂਡੇਨਸੀਜ਼ ਨੂੰ ਮੁੜ ਇੰਸਟਾਲ ਕਰੋ
pip install -r requirements.txt
```

#### ਇਲੈਕਟ੍ਰਾਨ ਬਿਲਡ ਮੁੱਦੇ
**ਮੁੱਦਾ:** npm ਇੰਸਟਾਲ ਜਾਂ ਬਿਲਡ ਫੇਲ੍ਹ ਹੋਣਾ

**ਸਮਾਧਾਨ:**
```bash
cd Module08/samples/08
# ਸਾਫ ਇੰਸਟਾਲ
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ਵਰਕਫਲੋ ਮੁੱਦੇ (ਛੋਟੇ)

#### ਅਨੁਵਾਦ ਵਰਕਫਲੋ ਟਕਰਾਅ
**ਮੁੱਦਾ:** ਅਨੁਵਾਦ ਪੁਲ ਰਿਕਵੇਸਟ ਤੁਹਾਡੇ ਬਦਲਾਵਾਂ ਨਾਲ ਟਕਰਾਉਂਦਾ ਹੈ

**ਸਮਾਧਾਨ:**
- ਸਿਰਫ ਅੰਗਰੇਜ਼ੀ ਸੋਰਸ ਫਾਈਲਾਂ ਸੋਧੋ
- ਅਨੁਵਾਦ ਵਰਕਫਲੋ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕੰਮ ਕਰਨ ਦਿਓ
- ਜੇ ਟਕਰਾਅ ਹੋਵੇ ਤਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਮੰਗਲ ਜਮ੍ਹਾਂ ਹੋਣ ਤੋਂ ਬਾਅਦ `main` ਨੂੰ ਆਪਣੀ ਬਰਾਂਚ 'ਚ ਮਰਜ ਕਰੋ

#### ਮਾਡਲ ਡਾਊਨਲੋਡ ਅਸਫਲ
**ਮੁੱਦਾ:** Foundry Local ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਨ ਵਿੱਚ ਅਸਫਲ

**ਸਮਾਧਾਨ:**
```bash
# ਇੰਟਰਨੈਟ ਕਨੈਕਟਿਵਿਟੀ ਦੀ ਜਾਂਚ ਕਰੋ
# ਮਾਡਲ ਕੈਸ਼ ਸਾਫ਼ ਕਰੋ ਅਤੇ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ
foundry model remove <model-alias>
foundry model run <model-alias>

# ਉਪਲਬਧ ਡਿਸਕ ਸਥਾਨਕਤਾ ਦੀ ਜਾਂਚ ਕਰੋ (ਮਾਡਲ 2-16GB ਹੋ ਸਕਦੇ ਹਨ)
# ਫਾਇਰਵਾਲ ਸੈਟਿੰਗਸ ਨੂੰ ਡਾਊਨਲੋਡ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ, ਇਸ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
```

## ਵਾਧੂ ਸਰੋਤ

### ਸਿੱਖਣ ਦੇ ਰਸਤੇ
- **ਬਿਗਿਨਰ ਰਸਤਾ:** ਮੋਡੀਊਲ 01-02 (7-9 ਘੰਟੇ)
- **ਦਰਮਿਆਨਾ ਦਰਜੇ ਦਾ ਰਸਤਾ:** ਮੋਡੀਊਲ 03-04 (9-11 ਘੰਟੇ)
- **ਉੱਚ ਦਰਜੇ ਦਾ ਰਸਤਾ:** ਮੋਡੀਊਲ 05-07 (12-15 ਘੰਟੇ)
- **ਮਾਹਿਰ ਰਸਤਾ:** Module 08 (8-10 ਘੰਟੇ)
- **ਹੈਂਡਜ਼-ਆਨ ਵਰਕਸ਼ਾਪ:** ਵਰਕਸ਼ਾਪ ਦੇ ਸਮੱਗਰੀ (6-8 ਘੰਟੇ)

### ਮੁੱਖ ਮੋਡੀਊਲ ਸਮੱਗਰੀ
- **Module01:** EdgeAI ਦੇ ਮੁਢਲਾ ਗਿਆਨ ਅਤੇ ਅਸਲੀ ਕਾਂਢੇ ਪ੍ਰਯੋਗ
- **Module02:** ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਪਰਿਵਾਰ ਅਤੇ ਬਣਤਰਾਂ
- **Module03:** ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ ਤੈਨਾਤੀ ਰਣਨੀਤੀਆਂ
- **Module04:** ਕਈ ਫਰੇਮਵਰਕਾਂ (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX) ਨਾਲ ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ
- **Module05:** SLMOps - ਉਤਪਾਦਨ ਓਪਰੇਸ਼ਨਜ਼
- **Module06:** AI ਏਜੰਟ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ
- **Module07:** ਪਲੇਟਫਾਰਮ-ਖਾਸ ਅਮਲ
- **Module08:** Foundry Local ਟੂਲਕਿਟ ਨਾਲ 10 ਵਿਸ਼ਤ੍ਰਿਤ ਨਮੂਨੇ

### ਬਾਹਰੀ ਨਿਰਭਰਤਾਵਾਂ
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-ਅਨੁਕੂਲ API ਵਾਲਾ ਲੋਕਲ AI ਮਾਡਲ ਰਨਟਾਈਮ
  - [ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਫਰੇਮਵਰਕ
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲਕਿਟ
- [OpenVINO](https://docs.openvino.ai/) - ਇੰਟਲ ਦਾ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲਕਿਟ

## ਪਰਿਯੋਜਨਾ-ਖਾਸ ਨੋਟਸ

### Module08 ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ

ਰਿਪੋਜ਼ੀਟਰੀ ਵਿੱਚ 10 ਵਿਸ਼ਤ੍ਰਿਤ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਸ਼ਾਮਲ ਹਨ:

1. **01-REST ਚੈੱਟ ਕੁਇਕਸਟਾਰਟ** - ਬੁਨਿਆਦੀ OpenAI SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ
2. **02-OpenAI SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ** - ਉन्नਤ SDK ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ
3. **03-ਮਾਡਲ ਖੋਜ ਅਤੇ ਬੈਂਚਮਾਰਕਿੰਗ** - ਮਾਡਲ ਤੁਲਨਾ ਟੂਲਜ਼
4. **04-ਚੇਨਲਿਟ RAG ਐਪਲੀਕੇਸ਼ਨ** - ਰੀਟਰੀਵਲ-ਅਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ
5. **05-ਮਲਟੀ-ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ** - ਬੁਨਿਆਦੀ ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ
6. **06-ਮਾਡਲ-ਅਜ਼-ਟੂਲਸ ਰਾਊਟਰ** - ਬੁੱਧੀਮਾਨ ਮਾਡਲ ਰਾਊਟਿੰਗ
7. **07-ਡਾਇਰੈਕਟ API ਕਲਾਇੰਟ** - ਨੀਵਾਂ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
8. **08-Windows 11 ਚੈੱਟ ਐਪ** - ਥੈਲਾ ਇਲੈਕਟ੍ਰਾਨ ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ
9. **09-ਉੱਨਤ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ** - ਜਟਿਲ ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ
10. **10-Foundry ਟੂਲਜ਼ ਫਰੇਮਵਰਕ** - LangChain/Semantic Kernel ਇੰਟੀਗ੍ਰੇਸ਼ਨ

### ਵਰਕਸ਼ਾਪ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ


ਵਰਕਸ਼ਾਪ ਵਿੱਚ ਆਮਲ ਵਿਚਕਾਰ 6 ਪ੍ਰਗਟਿਸ਼ੀਲ ਸੈਸ਼ਨ ਸ਼ਾਮਲ ਹਨ:

1. **ਸੈਸ਼ਨ 01** - ਫਾਊਂਡਰੀ ਲੋਕਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਾਲ ਚੈਟ ਬੂਟਸਟਰੈਪ
2. **ਸੈਸ਼ਨ 02** - RAG ਪਾਈਪਲਾਈਨ ਅਤੇ RAGAS ਨਾਲ ਮੁਲਾਂਕਣ
3. **ਸੈਸ਼ਨ 03** - ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਬੈਂਚਮਾਰਕਿੰਗ
4. **ਸੈਸ਼ਨ 04** - ਮਾਡਲ ਦੀ ਤੁਲਨਾ ਅਤੇ ਚੋਣ
5. **ਸੈਸ਼ਨ 05** - ਮਲਟੀ-ਏਜੰਟ ਔਰਕੇਸਟ੍ਰੇਸ਼ਨ ਸਿਸਟਮਾਂ
6. **ਸੈਸ਼ਨ 06** - ਮਾਡਲ ਰਾਊਟਿੰਗ ਅਤੇ ਪਾਈਪਲਾਈਨ ਪ੍ਰਬੰਧਨ

ਹਰ ਨਮੂਨਾ ਫਾਊਂਡਰੀ ਲੋਕਲ ਨਾਲ ਏਜ AI ਵਿਕਾਸ ਦੇ ਵੱਖ-ਵੱਖ ਪੱਖ ਦਿਖਾਉਂਦਾ ਹੈ।

### ਪ੍ਰਦਰਸ਼ਨ ਸਬੰਧੀ ਵਿਚਾਰ

- SLMs ਏਜ ਡਿਪਲੋਇਮੈਂਟ ਲਈ ਅਪਟੀਮਾਈਜ਼ਡ ਹਨ (2-16GB ਰੈਮ)
- ਲੋਕਲ ਇਨਫਰੈਂਸ 50-500ms ਜਵਾਬ ਦੇ ਸਮੇਂ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ
- ਕੁਐਂਟੀਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ 75% ਸਾਈਜ਼ ਕਟੌਤੀ ਅਤੇ 85% ਪ੍ਰਦਰਸ਼ਨ ਰੱਖਣਕਾਰ ਹਨ
- ਲੋਕਲ ਮਾਡਲਾਂ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਗੱਲਬਾਤ ਦੀ ਸਮਰੱਥਾ

### ਸੁਰੱਖਿਆ ਅਤੇ ਨਿੱਜਤਾ

- ਸਾਰਾ ਪ੍ਰੋਸੈਸਿੰਗ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਹੁੰਦਾ ਹੈ - ਕੋਈ ਡਾਟਾ ਕਲਾਉਡ ਨੂੰ ਨਹੀਂ ਭੇਜਿਆ ਜਾਂਦਾ
- ਨਿੱਜਤਾ-ਸੰਵੇਦਨਸ਼ੀਲ ਐਪਲੀਕੇਸ਼ਨਾਂ (ਹੈਲਥਕੇਅਰ, ਵਿੱਤੀ) ਲਈ ਉਚਿਤ
- ਡਾਟਾ ਸਰਕਾਰਦਾਰੀ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ
- ਫਾਊਂਡਰੀ ਲੋਕਲ ਸਿਰਫ ਸਥਾਨਕ ਹਾਰਡਵੇਅਰ 'ਤੇ ਚੱਲਦਾ ਹੈ

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

### ਡੌਕੂਮੈਂਟੇਸ਼ਨ

- **ਮੁੱਖ README**: [README.md](README.md) - ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਝਲਕ ਅਤੇ ਸਿਖਣ ਦੇ ਰਾਹ
- **ਸਟਡੀ ਗਾਈਡ**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - ਸਿਖਣ ਸਾਧਨ ਅਤੇ ਸਮਾਂ-ਰੇਖਾ
- **ਸਹਾਇਤਾ**: [SUPPORT.md](SUPPORT.md) - ਮਦਦ ਕਿਵੇਂ ਲੈਣੀ ਹੈ
- **ਸੁਰੱਖਿਆ**: [SECURITY.md](SECURITY.md) - ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ ਦੀ ਰਿਪੋਰਟਿੰਗ

### ਕਮਿਊਨਿਟੀ ਸਹਾਇਤਾ

- **GitHub Issues**: [ਬੱਗ ਰਿਪੋਰਟ ਕਰੋ ਜਾਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਈ ਬੇਨਤੀ ਕਰੋ](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [ਸਵਾਲ ਪੁੱਛੋ ਅਤੇ ਵਿਚਾਰ ਸਾਂਝੇ ਕਰੋ](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [ਫਾਊਂਡਰੀ ਲੋਕਲ ਨਾਲ ਤਕਨੀਕੀ ਸਮੱਸਿਆਵਾਂ](https://github.com/microsoft/Foundry-Local/issues)

### ਸੰਪਰਕ

- **ਮੈਂਟੇਨਰਜ਼**: ਵੇਖੋ [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ**: ਇੰਜਾਣੂ ਦਿਸਕਲੋਜ਼ਰ ਲਈ [SECURITY.md](SECURITY.md) ਦੀ ਪਾਲਣਾ ਕਰੋ
- **ਮਾਈਕ੍ਰੋਸੌਫਟ ਸਹਾਇਤਾ**: ਏਂਟਰਪਰਾਈਜ਼ ਸਹਾਇਤਾ ਲਈ, ਮਾਈਕ੍ਰੋਸੌਫਟ ਗਾਹਕ ਸੇਵਾ ਨਾਲ ਸੰਪਰਕ ਕਰੋ

### ਵਾਧੂ ਸਰੋਤ

- **Microsoft Learn**: [AI ਅਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸਿਖਣ ਦੇ ਰਾਹ](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ਡੌਕੂਮੈਂਟੇਸ਼ਨ**: [ਅਧਿਕਾਰਿਕ ਦਸਤਾਵੇਜ਼](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **ਕਮਿਊਨਿਟੀ ਨਮੂਨੇ**: ਕਮਿਊਨਿਟੀ ਯੋਗਦਾਨ ਲਈ [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) ਚੈੱਕ ਕਰੋ

---

**ਇਹ ਇੱਕ ਸਿੱਖਿਆ ਸੰਬੰਧੀ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜੋ ਏਜ AI ਵਿਕਾਸ ਸਿੱਖਾਉਣ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦੀ ਹੈ। ਮੁੱਖ ਯੋਗਦਾਨ ਦਾ ਤਰੀਕਾ ਸਿੱਖਣ ਵਾਲੇ ਸਮੱਗਰੀ ਵਿੱਚ ਸੁਧਾਰ ਅਤੇ ਏਜ AI ਸੰਕਲਪਾਂ ਨੂੰ ਦਿਖਾਉਂਦੇ ਸੈਂਪਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਜੋੜਣਾ/ਵਧਾਉਣਾ ਹੈ।**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->