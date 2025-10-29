<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T23:52:44+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ta"
}
-->
# அமர்வு 1: Foundry Local உடன் தொடங்குதல்

## சுருக்கம்

Windows 11-ல் Foundry Local-ஐ நிறுவி அமைப்பதன் மூலம் உங்கள் பயணத்தை தொடங்குங்கள். CLI அமைப்பது, ஹார்ட்வேரின் வேகத்தை அதிகரிப்பது மற்றும் மாடல்களை வேகமான உள்ளூர் முடிவுகளுக்காக சேமிப்பது போன்றவற்றை அறிக. இந்த நடைமுறை அமர்வு, Phi, Qwen, DeepSeek மற்றும் GPT-OSS-20B போன்ற மாடல்களை மீண்டும் உருவாக்கக்கூடிய CLI கட்டளைகளைப் பயன்படுத்தி இயக்குவதற்கான வழிமுறைகளை விளக்குகிறது.

## கற்றல் நோக்கங்கள்

இந்த அமர்வு முடிவில், நீங்கள்:

- **நிறுவல் மற்றும் அமைப்பு**: Foundry Local-ஐ Windows 11-ல் சிறந்த செயல்திறன் அமைப்புகளுடன் அமைக்கவும்
- **CLI செயல்பாடுகளை கற்றுக்கொள்ளுங்கள்**: மாடல் மேலாண்மை மற்றும் பரப்பலுக்காக Foundry Local CLI-ஐ பயன்படுத்தவும்
- **ஹார்ட்வேரின் வேகத்தை அதிகரிக்கவும்**: ONNXRuntime அல்லது WebGPU மூலம் GPU வேகத்தை அமைக்கவும்
- **பல மாடல்களை பரப்பவும்**: phi-4, GPT-OSS-20B, Qwen மற்றும் DeepSeek மாடல்களை உள்ளூரில் இயக்கவும்
- **உங்கள் முதல் பயன்பாட்டை உருவாக்கவும்**: Foundry Local Python SDK-ஐ பயன்படுத்தி உள்ள மாதிரிகளைத் தழுவவும்

# மாடலை சோதிக்கவும் (இயங்காத தனிப்பட்ட கேள்வி)
foundry model run phi-4-mini --prompt "வணக்கம், உங்களை அறிமுகப்படுத்துங்கள்"

- Windows 11 (22H2 அல்லது அதற்கு மேல்)
# கிடைக்கக்கூடிய மாடல்களின் பட்டியலை காண்க (இயக்கப்பட்ட மாடல்கள் இயக்கப்பட்ட பிறகு தோன்றும்)
foundry model list
## NOTE: தற்போது தனிப்பட்ட `--running` கொடுப்பனவு இல்லை; எந்தவை ஏற்றப்பட்டுள்ளன என்பதைப் பார்க்க, ஒரு உரையாடலைத் தொடங்கவும் அல்லது சேவை பதிவுகளை ஆய்வு செய்யவும்.
- Python 3.10+ நிறுவப்பட்டுள்ளது
- Visual Studio Code Python நீட்டிப்புடன்
- நிறுவலுக்கான நிர்வாக அனுமதிகள்

### (விருப்பத்தேர்வு) சூழல் மாறிகள்

ஸ்கிரிப்ட்களை எளிதாக மாற்ற `.env` (அல்லது ஷெல்-ல் அமைக்கவும்) உருவாக்கவும்:
# பதில்களை ஒப்பிடவும் (இயங்காத)
foundry model run gpt-oss-20b --prompt "எட்ஜ் AI-ஐ எளிய சொற்களில் விளக்கவும்"
| மாறி | நோக்கம் | உதாரணம் |
|------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | விருப்ப மாடல் பெயர் (கேட்டலாக் சிறந்த மாறுபாட்டை தானாகத் தேர்ந்தெடுக்கிறது) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | முடிவுகளை மாற்றவும் (இல்லையெனில் மேலாளர் மூலம் தானாக) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | ஸ்ட்ரீமிங் டெமோவை இயக்கவும் | `true` |

> `FOUNDRY_LOCAL_ENDPOINT=auto` (அல்லது அமைக்கப்படவில்லை) என்றால், அதை SDK மேலாளரிடமிருந்து பெறுகிறோம்.

## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. Foundry Local-ஐ நிறுவி CLI அமைப்பைச் சரிபார்க்கவும் (10 நிமிடங்கள்)

# சேமிக்கப்பட்ட மாடல்களின் பட்டியலை காண்க
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (முன்னோட்டம் / ஆதரிக்கப்பட்டால்)**

ஒரு இயற்கை macOS தொகுப்பு வழங்கப்பட்டால் (சமீபத்தியவை அதிகாரப்பூர்வ ஆவணங்களில் சரிபார்க்கவும்):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

macOS இயற்கை பைனரிகள் இன்னும் கிடைக்கவில்லை என்றால், நீங்கள் இதை செய்யலாம்: 
1. Windows 11 ARM/Intel VM (Parallels / UTM) பயன்படுத்தி Windows படிகள் பின்பற்றவும். 
2. கன்டெய்னர் மூலம் மாடல்களை இயக்கவும் (கன்டெய்னர் படிமம் வெளியிடப்பட்டால்) மற்றும் `FOUNDRY_LOCAL_ENDPOINT`-ஐ வெளிப்படுத்தப்பட்ட போர்ட்டுக்கு அமைக்கவும். 

**Python மெய்நிகர் சூழலை உருவாக்கவும் (குறுக்குவழி‑தளம்)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pip-ஐ மேம்படுத்தி முக்கிய தேவைகளை நிறுவவும்:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### படி 1.2: நிறுவலைச் சரிபார்க்கவும்

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### படி 1.3: சூழலை அமைக்கவும்

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK தொடங்குதல் (பரிந்துரைக்கப்படுகிறது)

சேவையை கையால் தொடங்குவதற்கும் மாடல்களை இயக்குவதற்கும் பதிலாக, **Foundry Local Python SDK** அனைத்தையும் தொடங்க முடியும்:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

நீங்கள் தெளிவான கட்டுப்பாட்டை விரும்பினால், CLI + OpenAI கிளையண்டை பின்னர் காட்டப்படும் முறையில் பயன்படுத்தலாம்.

### 2. மாடல்களை உள்ளூரில் CLI மூலம் இயக்கவும் (10 நிமிடங்கள்)

#### படி 3.1: Phi-4 மாடலை பரப்பவும்

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### படி 3.2: GPT-OSS-20B-ஐ பரப்பவும்

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### படி 3.3: கூடுதல் மாடல்களை ஏற்றவும்

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. தொடக்க திட்டம்: Foundry Local-க்கு 01-run-phi-ஐ தழுவவும் (5 நிமிடங்கள்)

#### படி 4.1: அடிப்படை உரையாடல் பயன்பாட்டை உருவாக்கவும்

`samples/01-foundry-quickstart/chat_quickstart.py` உருவாக்கவும் (மீண்டும் மேலாளரைப் பயன்படுத்த புதுப்பிக்கப்பட்டது):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### படி 4.2: பயன்பாட்டைச் சோதிக்கவும்

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## முக்கிய கருத்துகள்

### 1. Foundry Local கட்டமைப்பு

- **உள்ளூர் முடிவு இயந்திரம்**: மாடல்களை முழுமையாக உங்கள் சாதனத்தில் இயக்குகிறது
- **OpenAI SDK இணக்கத்தன்மை**: உள்ள OpenAI குறியீட்டுடன் எளிதாக ஒருங்கிணைவு
- **மாடல் மேலாண்மை**: பல மாடல்களை திறம்பட பதிவிறக்கி, சேமித்து, இயக்கவும்
- **ஹார்ட்வேரின் மேம்பாடு**: GPU, NPU மற்றும் CPU வேகத்தைப் பயன்படுத்தவும்

### 2. CLI கட்டளை குறிப்பு

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK ஒருங்கிணைவு

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## பொதுவான சிக்கல்களை சரி செய்வது

### சிக்கல் 1: "Foundry command not found"

**தீர்வு:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### சிக்கல் 2: "Model failed to load"

**தீர்வு:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### சிக்கல் 3: "Connection refused on localhost:5273"

**தீர்வு:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## செயல்திறன் மேம்பாட்டு குறிப்புகள்

### 1. மாடல் தேர்வு உத்தி

- **Phi-4-mini**: பொதுவான பணிகளுக்கு சிறந்தது, குறைந்த நினைவக பயன்பாடு
- **Qwen2.5-0.5b**: வேகமான முடிவு, குறைந்த வளங்கள்
- **GPT-OSS-20B**: மிக உயர்ந்த தரம், அதிக வளங்கள் தேவை
- **DeepSeek-Coder**: நிரலாக்க பணிகளுக்கு மேம்படுத்தப்பட்டது

### 2. ஹார்ட்வேரின் மேம்பாடு

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. செயல்திறனை கண்காணித்தல்

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### விருப்ப மேம்பாடுகள்

| மேம்பாடு | என்ன | எப்படி |
|---------|------|------|
| பகிரப்பட்ட பயன்பாடுகள் | மறு பயன்பாட்டு கிளையண்ட்/தொடக்கத் தரவுகளை நீக்கவும் | `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) பயன்படுத்தவும் |
| டோக்கன் பயன்பாட்டு காட்சி | செலவு/திறன் சிந்தனையை ஆரம்பத்தில் கற்றுக்கொடுக்கவும் | `SHOW_USAGE=1` அமைத்து கேள்வி/முடிவு/மொத்த டோக்கன்களை அச்சிடவும் |
| தீர்மானமான ஒப்பீடுகள் | நிலையான பெஞ்ச்மார்க்கிங் மற்றும் பின்வாங்க சோதனை | `temperature=0`, `top_p=1`, ஒரே கேள்வி உரை பயன்படுத்தவும் |
| முதல்-டோக்கன் தாமதம் | உணரப்பட்ட பதிலளிப்பு அளவீடு | ஸ்ட்ரீமிங் மூலம் பெஞ்ச்மார்க்கை மாற்றவும் (`BENCH_STREAM=1`) |
| தற்காலிக பிழைகளில் மீண்டும் முயற்சி | குளிர்ந்த தொடக்கத்தில் உறுதியான டெமோக்கள் | `RETRY_ON_FAIL=1` (இயல்புநிலை) & `RETRY_BACKOFF`-ஐ சரிசெய்க |
| புகை சோதனை | முக்கிய ஓட்டங்களில் விரைவான சான்று | ஒரு பணிக்கூட்டத்திற்கு முன் `python Workshop/tests/smoke.py` இயக்கவும் |
| மாடல் பெயர் சுயவிவரங்கள் | இயந்திரங்களுக்கு இடையில் மாடல் தொகுப்பை விரைவாக மாற்றவும் | `.env`-ஐ `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` உடன் பராமரிக்கவும் |
| சேமிப்பு திறன் | பல மாதிரி ஓட்டத்தில் மீண்டும் தொடக்கங்களைத் தவிர்க்கவும் | பயன்பாடுகள் சேமிப்பு மேலாளர்கள்; ஸ்கிரிப்ட்கள்/குறிப்புகள் முழுவதும் மீண்டும் பயன்படுத்தவும் |
| முதல் ஓட்டம் தொடக்கம் | p95 தாமதம் அதிகரிப்பை குறைக்கவும் | `FoundryLocalManager` உருவாக்கத்திற்குப் பிறகு சிறிய கேள்வியை இயக்கவும் |

PowerShell-ல் தீர்மானமான வெப்ப அடிப்படையை எடுத்துக்காட்டு:

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

இரண்டாவது ஓட்டத்தில் ஒரே டோக்கன் எண்ணிக்கைகளை உறுதிப்படுத்தும், இதே போன்ற வெளியீட்டை நீங்கள் காண வேண்டும்.

## அடுத்த படிகள்

இந்த அமர்வை முடித்த பிறகு:

1. **அமர்வு 2-ஐ ஆராயுங்கள்**: Azure AI Foundry RAG உடன் AI தீர்வுகளை உருவாக்கவும்
2. **வித்தியாசமான மாடல்களை முயற்சிக்கவும்**: Qwen, DeepSeek மற்றும் பிற மாடல் குடும்பங்களை ஆராயவும்
3. **செயல்திறனை மேம்படுத்தவும்**: உங்கள் குறிப்பிட்ட ஹார்ட்வேருக்கான அமைப்புகளை நன்றாக அமைக்கவும்
4. **தனிப்பயன் பயன்பாடுகளை உருவாக்கவும்**: Foundry Local SDK-ஐ உங்கள் சொந்த திட்டங்களில் பயன்படுத்தவும்

## கூடுதல் வளங்கள்

### ஆவணங்கள்
- [Foundry Local Python SDK குறிப்பு](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local நிறுவல் வழிகாட்டி](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [மாடல் கேட்டலாக்](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### மாதிரி குறியீடு
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### சமூகங்கள்
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**அமர்வு காலம்**: 30 நிமிடங்கள் நடைமுறை + 15 நிமிடங்கள் கேள்வி & பதில்
**கடினத்தன்மை நிலை**: தொடக்க நிலை
**முன் தேவைகள்**: Windows 11, Python 3.10+, நிர்வாக அணுகல்

## மாதிரி சூழல் & பணிக்கூட்டம் வரைபடம்

| பணிக்கூட்டம் ஸ்கிரிப்ட் / குறிப்பு | சூழல் | இலக்கு | எடுத்துக்காட்டு உள்ளீடு(கள்) | தேவைப்படும் தரவுத்தொகுப்பு |
|----------------------------------|-------|-------|----------------------------|----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | உள்ள IT குழு ஒரு தனியுரிமை மதிப்பீட்டு போர்டலுக்கான சாதன முடிவுகளை மதிப்பீடு செய்கிறது | உள்ளூர் SLM பொதுவான கேள்விகளுக்கு துணை-வினாடி தாமதத்தில் பதிலளிக்கிறது என்பதை நிரூபிக்கவும் | "உள்ளூர் முடிவின் இரண்டு நன்மைகளை பட்டியலிடுங்கள்." | இல்லை (தனிப்பட்ட கேள்வி) |
| Quickstart தழுவல் குறியீட்டு தொகுதி | ஒரு OpenAI ஸ்கிரிப்டை Foundry Local-க்கு மாற்றும் டெவலப்பர் | ஒருங்கிணைந்த இணக்கத்தன்மையை காட்டவும் | "உள்ளூர் முடிவின் இரண்டு நன்மைகளை கொடுக்கவும்." | உள்ளீடு மட்டும் |

### சூழல் விளக்கம்
பாதுகாப்பு & ஒழுங்குமுறை குழு, நுண்ணறிவு மாதிரிகள் உள்ளூர் முறையில் செயல்படுமா என்பதை உறுதிப்படுத்த வேண்டும். அவர்கள் பல கேள்விகளுடன் (தனியுரிமை, தாமதம், செலவு) bootstrap ஸ்கிரிப்டை இயக்கி, அடிப்படை வெளியீடுகளைப் பதிவு செய்கின்றனர், பின்னர் ஒப்பீட்டிற்காக (அமர்வு 3 பெஞ்ச்மார்க்கிங் மற்றும் அமர்வு 4 SLM vs LLM மாறுபாடு).

### குறைந்தபட்ச கேள்வி தொகுப்பு JSON (விருப்பத்தேர்வு)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

இந்த பட்டியலை மீண்டும் உருவாக்கக்கூடிய மதிப்பீட்டு சுற்று அல்லது எதிர்கால பின்வாங்க சோதனை கருவியை உருவாக்க பயன்படுத்தவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.