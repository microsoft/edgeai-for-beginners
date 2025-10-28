<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:30:02+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ta"
}
-->
# அமர்வு 1: Foundry Local உடன் தொடங்குதல்

## சுருக்கம்

Windows 11-ல் Foundry Local ஐ நிறுவி, அமைப்பதன் மூலம் உங்கள் பயணத்தை தொடங்குங்கள். CLI அமைப்பது, ஹார்ட்வேர் வேகத்தை இயக்குவது மற்றும் மாடல்களை வேகமான உள்ளூர் முடிவுகளுக்காக காட்சியமைப்பது போன்றவற்றை கற்றுக்கொள்ளுங்கள். இந்த கைக்கூலி அமர்வு, Phi, Qwen, DeepSeek, மற்றும் GPT-OSS-20B போன்ற மாடல்களை CLI கட்டளைகளை பயன்படுத்தி இயக்குவதற்கான வழிமுறைகளை விளக்குகிறது.

## கற்றல் நோக்கங்கள்

இந்த அமர்வின் முடிவில், நீங்கள்:

- **நிறுவல் மற்றும் அமைப்பு**: Windows 11-ல் Foundry Local ஐ சிறந்த செயல்திறன் அமைப்புகளுடன் அமைக்கவும்
- **CLI செயல்பாடுகளை கற்றுக்கொள்ளுங்கள்**: மாடல் மேலாண்மை மற்றும் பிரயோகத்திற்காக Foundry Local CLI ஐ பயன்படுத்தவும்
- **ஹார்ட்வேர் வேகத்தை இயக்கவும்**: ONNXRuntime அல்லது WebGPU உடன் GPU வேகத்தை அமைக்கவும்
- **பல மாடல்களை பிரயோகிக்கவும்**: phi-4, GPT-OSS-20B, Qwen, மற்றும் DeepSeek மாடல்களை உள்ளூரில் இயக்கவும்
- **உங்கள் முதல் பயன்பாட்டை உருவாக்கவும்**: Foundry Local Python SDK ஐ பயன்படுத்தி உள்ள மாதிரிகளை மாற்றவும்

# மாடலை சோதிக்கவும் (இணையமற்ற ஒற்றை உந்துதல்)
foundry model run phi-4-mini --prompt "வணக்கம், உங்களை அறிமுகப்படுத்துங்கள்"

- Windows 11 (22H2 அல்லது அதற்கு மேல்)
# கிடைக்கக்கூடிய மாடல்களின் பட்டியலை காண்க (இயக்கப்பட்ட மாடல்கள் இயக்கப்பட்ட பிறகு தோன்றும்)
foundry model list
## குறிப்பு: தற்போது தனித்துவமான `--running` கொடி இல்லை; எந்தவை ஏற்றப்பட்டுள்ளன என்பதை காண, ஒரு உரையாடலை தொடங்கவும் அல்லது சேவை பதிவுகளை ஆய்வு செய்யவும்.
- Python 3.10+ நிறுவப்பட்டுள்ளது
- Python நீட்டிப்புடன் Visual Studio Code
- நிறுவலுக்கான நிர்வாக அனுமதிகள்

### (விருப்பத்தேர்வு) சூழல் மாறிகள்

ஸ்கிரிப்ட்களை தாங்கக்கூடியதாக மாற்ற `.env` (அல்லது ஷெல்லில் அமைக்கவும்):
# பதில்களை ஒப்பிடவும் (இணையமற்றது)
foundry model run gpt-oss-20b --prompt "எட்ஜ் AI ஐ எளிய சொற்களில் விளக்கவும்"
| மாறி | நோக்கம் | உதாரணம் |
|------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | விருப்ப மாடல் பெயர் (சுயமாக சிறந்த மாறுபாட்டை தேர்ந்தெடுக்கிறது) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | முடிவுக்கான முகவரியை மாற்றவும் (இல்லையெனில் மேலாளரிடமிருந்து சுயமாக) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | ஸ்ட்ரீமிங் டெமோவை இயக்கவும் | `true` |

> `FOUNDRY_LOCAL_ENDPOINT=auto` (அல்லது அமைக்கப்படவில்லை) என்றால், அதை SDK மேலாளரிடமிருந்து பெறுகிறோம்.

## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. Foundry Local ஐ நிறுவி CLI அமைப்பை சரிபார்க்கவும் (10 நிமிடங்கள்)

# காட்சியமைக்கப்பட்ட மாடல்களின் பட்டியல்
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (முன்னோடி / ஆதரவு இருந்தால்)**

ஒரு சொந்த macOS தொகுப்பு வழங்கப்பட்டால் (சமீபத்தியதை அதிகாரப்பூர்வ ஆவணங்களில் சரிபார்க்கவும்):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

macOS சொந்த பைனரிகள் இன்னும் கிடைக்கவில்லை என்றால், நீங்கள் இன்னும் செய்யலாம்: 
1. Windows 11 ARM/Intel VM (Parallels / UTM) ஐ பயன்படுத்தி Windows படிகளை பின்பற்றவும். 
2. கன்டெய்னர் வழியாக மாடல்களை இயக்கவும் (கன்டெய்னர் படிமம் வெளியிடப்பட்டால்) மற்றும் `FOUNDRY_LOCAL_ENDPOINT` ஐ வெளிப்படுத்தப்பட்ட போர்ட்டுக்கு அமைக்கவும். 

**Python மெய்நிகர் சூழலை உருவாக்கவும் (குறுக்கு-தளம்)**

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

pip ஐ மேம்படுத்தி முக்கிய சார்புகளை நிறுவவும்:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### படி 1.2: நிறுவலை சரிபார்க்கவும்

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

நீங்கள் தெளிவான கட்டுப்பாட்டை விரும்பினால், CLI + OpenAI கிளையண்டை பின்னர் காட்டப்பட்டபடி இன்னும் பயன்படுத்தலாம்.

### 2. CLI வழியாக உள்ளூரில் மாடல்களை இயக்கவும் (10 நிமிடங்கள்)

#### படி 3.1: Phi-4 மாடலை பிரயோகிக்கவும்

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### படி 3.2: GPT-OSS-20B ஐ பிரயோகிக்கவும்

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

### 4. தொடக்க திட்டம்: Foundry Local க்கு 01-run-phi ஐ மாற்றவும் (5 நிமிடங்கள்)

#### படி 4.1: அடிப்படை உரையாடல் பயன்பாட்டை உருவாக்கவும்

`samples/01-foundry-quickstart/chat_quickstart.py` ஐ உருவாக்கவும் (மாற்றியமைக்கப்பட்ட மேலாளரைப் பயன்படுத்த):

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

#### படி 4.2: பயன்பாட்டை சோதிக்கவும்

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## முக்கிய கருத்துக்கள்

### 1. Foundry Local கட்டமைப்பு

- **உள்ளூர் முடிவு இயந்திரம்**: மாடல்களை முழுமையாக உங்கள் சாதனத்தில் இயக்குகிறது
- **OpenAI SDK இணக்கத்தன்மை**: ஏற்கனவே உள்ள OpenAI குறியீட்டுடன் எளிதாக ஒருங்கிணைக்கிறது
- **மாடல் மேலாண்மை**: பல மாடல்களை பதிவிறக்கம், காட்சி மற்றும் திறமையாக இயக்குகிறது
- **ஹார்ட்வேர் மேம்பாடு**: GPU, NPU, மற்றும் CPU வேகத்தை பயன்படுத்துகிறது

### 2. CLI கட்டளை குறிப்பு

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK ஒருங்கிணைப்பு

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

## பொதுவான பிரச்சினைகளை சரிசெய்தல்

### பிரச்சினை 1: "Foundry command not found"

**தீர்வு:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### பிரச்சினை 2: "Model failed to load"

**தீர்வு:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### பிரச்சினை 3: "Connection refused on localhost:5273"

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
- **Qwen2.5-0.5b**: மிக வேகமான முடிவு, குறைந்த வளங்கள்
- **GPT-OSS-20B**: மிக உயர்ந்த தரம், அதிக வளங்கள் தேவை
- **DeepSeek-Coder**: நிரலாக்க பணிகளுக்கு மேம்படுத்தப்பட்டது

### 2. ஹார்ட்வேர் மேம்பாடு

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
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### விருப்ப மேம்பாடுகள்

| மேம்பாடு | என்ன | எப்படி |
|----------|------|-------|
| பகிரப்பட்ட பயன்பாடுகள் | மறு பயன்பாட்டுக்கான கிளையண்ட்/தொடக்கத் தரவுகளை நீக்கவும் | `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) ஐப் பயன்படுத்தவும் |
| டோக்கன் பயன்பாட்டு காட்சி | செலவு/திறன் சிந்தனையை ஆரம்பத்தில் கற்றுக்கொள்ளுங்கள் | `SHOW_USAGE=1` ஐ அமைத்து உந்துதல்/முடிவு/மொத்த டோக்கன்களை அச்சிடவும் |
| தீர்மானமான ஒப்பீடுகள் | நிலையான பெஞ்ச்மார்க்கிங் மற்றும் பின்வாங்கல் சரிபார்ப்பு | `temperature=0`, `top_p=1`, நிலையான உந்துதல் உரை பயன்படுத்தவும் |
| முதல்-டோக்கன் தாமதம் | உணரப்பட்ட பதிலளிப்பு அளவுகோல் | ஸ்ட்ரீமிங் மூலம் பெஞ்ச்மார்க் ஸ்கிரிப்டை மாற்றவும் (`BENCH_STREAM=1`) |
| தற்காலிக பிழைகளில் மீண்டும் முயற்சி | குளிர்ந்த தொடக்கத்தில் உறுதியான டெமோக்கள் | `RETRY_ON_FAIL=1` (இயல்புநிலை) மற்றும் `RETRY_BACKOFF` ஐ சரிசெய்க |
| புகை சோதனை | முக்கிய ஓட்டங்களில் விரைவான சான்றுகள் | ஒரு பணிக்கூட்டத்திற்கு முன் `python Workshop/tests/smoke.py` ஐ இயக்கவும் |
| மாடல் பெயர் சுயவிவரங்கள் | இயந்திரங்களுக்கு இடையில் மாடல் தொகுப்பை விரைவாக மாற்றவும் | `.env` ஐ `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` உடன் பராமரிக்கவும் |
| காட்சி திறன் | பல மாதிரி இயக்கத்தில் மீண்டும் மீண்டும் காட்சியமைப்புகளை தவிர்க்கவும் | காட்சி மேலாளர்களை பயன்படுத்தவும்; ஸ்கிரிப்ட்கள்/குறிப்புகள் முழுவதும் மீண்டும் பயன்படுத்தவும் |
| முதல் இயக்க காட்சி | p95 தாமத உச்சங்களை குறைக்கவும் | `FoundryLocalManager` உருவாக்கத்தின் பிறகு சிறிய உந்துதலை இயக்கவும் |

தீர்மானமான வெப்ப அடிப்படையை உருவாக்க உதாரணம் (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

இரண்டாவது இயக்கத்தில் ஒரே மாதிரியான வெளியீடு மற்றும் ஒரே டோக்கன் எண்ணிக்கைகளை நீங்கள் காண வேண்டும், இது தீர்மானத்தைக் கண்டறிகிறது.

## அடுத்த படிகள்

இந்த அமர்வை முடித்த பிறகு:

1. **அமர்வு 2 ஐ ஆராயுங்கள்**: Azure AI Foundry RAG உடன் AI தீர்வுகளை உருவாக்கவும்
2. **வேறு மாடல்களை முயற்சிக்கவும்**: Qwen, DeepSeek மற்றும் பிற மாடல் குடும்பங்களை ஆராயவும்
3. **செயல்திறனை மேம்படுத்தவும்**: உங்கள் குறிப்பிட்ட ஹார்ட்வேருக்கான அமைப்புகளை நயமாக்கவும்
4. **தனிப்பயன் பயன்பாடுகளை உருவாக்கவும்**: Foundry Local SDK ஐ உங்கள் சொந்த திட்டங்களில் பயன்படுத்தவும்

## கூடுதல் வளங்கள்

### ஆவணங்கள்
- [Foundry Local Python SDK குறிப்பு](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local நிறுவல் வழிகாட்டி](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [மாடல் பட்டியல்](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### மாதிரி குறியீடு
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK ஒருங்கிணைப்பு
- [Module08 Sample 03](./samples/03/README.md) - மாடல் கண்டுபிடிப்பு & பெஞ்ச்மார்க்கிங்

### சமூகம்
- [Foundry Local GitHub விவாதங்கள்](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI சமூகம்](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**அமர்வு காலம்**: 30 நிமிடங்கள் கைக்கூலி + 15 நிமிடங்கள் கேள்வி & பதில்
**சிரம நிலை**: தொடக்க நிலை
**முன் தேவைகள்**: Windows 11, Python 3.10+, நிர்வாக அணுகல்

## மாதிரி சூழ்நிலை & பணிக்கூட்டம் வரைபடம்

| பணிக்கூட்டு ஸ்கிரிப்ட் / குறிப்பு | சூழ்நிலை | நோக்கம் | உதாரண உள்ளீடுகள் | தேவைப்படும் தரவுத்தொகுப்பு |
|----------------------------------|----------|---------|------------------|----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | தனியார் மதிப்பீடு போர்டலுக்கான உள்ளூர் SLM பதிலளிப்பு சோதனை | உள்ளூர் SLM சுயவிவரங்களை நிரூபிக்கவும் | "உள்ளூர் முடிவின் இரண்டு நன்மைகளை பட்டியலிடுங்கள்." | இல்லை (ஒற்றை உந்துதல்) |
| Quickstart மாற்றம் குறியீட்டு தொகுதி | ஒரு OpenAI ஸ்கிரிப்டை Foundry Local க்கு மாற்றும் டெவலப்பர் | இணக்கத்தன்மையை நிரூபிக்கவும் | "உள்ளூர் முடிவின் இரண்டு நன்மைகளை கொடுக்கவும்." | உள்ளமைந்த உந்துதல் மட்டும் |

### சூழ்நிலை விளக்கம்
பாதுகாப்பு மற்றும் இணக்கத்தன்மை குழு, உணர்திறன் கொண்ட தரவுகளை உள்ளூரில் செயலாக்க முடியும் என்பதை சரிபார்க்க வேண்டும். அவர்கள் பல உந்துதல்களுடன் (தனியுரிமை, தாமதம், செலவு) தொடக்க ஸ்கிரிப்டை இயக்குகிறார்கள், தீர்மானமான temperature=0 முறையைப் பயன்படுத்தி பின்னர் ஒப்பீட்டிற்கான அடிப்படை வெளியீடுகளைப் பதிவு செய்கிறார்கள் (அமர்வு 3 பெஞ்ச்மார்க்கிங் மற்றும் அமர்வு 4 SLM மற்றும் LLM மாறுபாடு).

### குறைந்தபட்ச உந்துதல் தொகுப்பு JSON (விருப்பத்தேர்வு)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

இந்த பட்டியலை மீண்டும் உருவாக்கக்கூடிய மதிப்பீட்டு சுற்றுக்கோப்பை உருவாக்க அல்லது எதிர்கால பின்வாங்கல் சோதனை கருவியை விதைக்க பயன்படுத்தவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.