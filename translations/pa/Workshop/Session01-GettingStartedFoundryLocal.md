<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:23:51+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 1: Foundry Local ਨਾਲ ਸ਼ੁਰੂਆਤ

## ਸਾਰ

Foundry Local ਨਾਲ ਆਪਣਾ ਸਫਰ ਸ਼ੁਰੂ ਕਰੋ, Windows 11 'ਤੇ ਇਸਨੂੰ ਇੰਸਟਾਲ ਅਤੇ ਕਨਫਿਗਰ ਕਰਕੇ। CLI ਸੈਟਅੱਪ ਕਰਨ, ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਨੂੰ ਐਨਬਲ ਕਰਨ ਅਤੇ ਤੇਜ਼ ਸਥਾਨਕ ਇੰਫਰੈਂਸ ਲਈ ਮਾਡਲਾਂ ਨੂੰ ਕੈਸ਼ ਕਰਨ ਦਾ ਤਰੀਕਾ ਸਿੱਖੋ। ਇਹ ਹੱਥ-ਅਨੁਭਵ ਸੈਸ਼ਨ ਫਾਈ, Qwen, DeepSeek, ਅਤੇ GPT-OSS-20B ਵਰਗੇ ਮਾਡਲਾਂ ਨੂੰ ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਵਾਲੇ CLI ਕਮਾਂਡਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਲਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦਿਖਾਉਂਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਸੈਸ਼ਨ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ:

- **ਇੰਸਟਾਲ ਅਤੇ ਕਨਫਿਗਰ ਕਰੋ**: Windows 11 'ਤੇ Foundry Local ਨੂੰ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਸੈਟਿੰਗਾਂ ਨਾਲ ਸੈਟਅੱਪ ਕਰੋ
- **CLI ਓਪਰੇਸ਼ਨ ਵਿੱਚ ਮਾਹਰ ਬਣੋ**: ਮਾਡਲ ਮੈਨੇਜਮੈਂਟ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਲਈ Foundry Local CLI ਦੀ ਵਰਤੋਂ ਕਰੋ
- **ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਐਨਬਲ ਕਰੋ**: ONNXRuntime ਜਾਂ WebGPU ਨਾਲ GPU ਐਕਸਲੇਰੇਸ਼ਨ ਕਨਫਿਗਰ ਕਰੋ
- **ਕਈ ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ**: phi-4, GPT-OSS-20B, Qwen, ਅਤੇ DeepSeek ਮਾਡਲਾਂ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚਲਾਓ
- **ਆਪਣਾ ਪਹਿਲਾ ਐਪ ਬਣਾਓ**: Foundry Local Python SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੌਜੂਦਾ ਨਮੂਨਿਆਂ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ

# ਮਾਡਲ ਦੀ ਜਾਂਚ ਕਰੋ (ਗੈਰ-ਇੰਟਰੈਕਟਿਵ ਸਿੰਗਲ ਪ੍ਰੌਮਪਟ)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 ਜਾਂ ਇਸ ਤੋਂ ਬਾਅਦ)
# ਉਪਲਬਧ ਕੈਟਾਲੌਗ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ (ਲੋਡ ਕੀਤੇ ਮਾਡਲ ਚਲਾਏ ਜਾਣ ਤੋਂ ਬਾਅਦ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ)
foundry model list
## NOTE: ਇਸ ਸਮੇਂ ਕੋਈ ਸਮਰਪਿਤ `--running` ਫਲੈਗ ਨਹੀਂ ਹੈ; ਇਹ ਦੇਖਣ ਲਈ ਕਿ ਕਿਹੜੇ ਲੋਡ ਕੀਤੇ ਗਏ ਹਨ, ਚੈਟ ਸ਼ੁਰੂ ਕਰੋ ਜਾਂ ਸੇਵਾ ਲੌਗ ਦੀ ਜਾਂਚ ਕਰੋ।
- Python 3.10+ ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਇਆ
- Visual Studio Code Python ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ
- ਇੰਸਟਾਲੇਸ਼ਨ ਲਈ ਐਡਮਿਨਿਸਟ੍ਰੇਟਰ ਅਧਿਕਾਰ

### (ਵਿਕਲਪਿਕ) ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਪੋਰਟੇਬਲ ਬਣਾਉਣ ਲਈ `.env` ਬਣਾਓ (ਜਾਂ ਸ਼ੈਲ ਵਿੱਚ ਸੈਟ ਕਰੋ):
# ਜਵਾਬਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ (ਗੈਰ-ਇੰਟਰੈਕਟਿਵ)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | ਪਸੰਦੀਦਾ ਮਾਡਲ ਅਲਿਆਸ (ਕੈਟਾਲੌਗ ਵਧੀਆ ਵੈਰੀਐਂਟ ਨੂੰ ਆਟੋ-ਚੁਣਦਾ ਹੈ) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਕਰੋ (ਨਹੀਂ ਤਾਂ ਮੈਨੇਜਰ ਤੋਂ ਆਟੋ) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | ਸਟ੍ਰੀਮਿੰਗ ਡੈਮੋ ਐਨਬਲ ਕਰੋ | `true` |

> ਜੇ `FOUNDRY_LOCAL_ENDPOINT=auto` (ਜਾਂ ਅਨਸੈਟ) ਹੈ ਤਾਂ ਅਸੀਂ ਇਸਨੂੰ SDK ਮੈਨੇਜਰ ਤੋਂ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਾਂ।

## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. Foundry Local ਇੰਸਟਾਲ ਕਰੋ ਅਤੇ CLI ਸੈਟਅੱਪ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ (10 ਮਿੰਟ)

# ਕੈਸ਼ ਕੀਤੇ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (ਪ੍ਰੀਵਿਊ / ਜੇ ਸਪੋਰਟ ਕੀਤਾ ਗਿਆ)**

ਜੇਕਰ ਕੋਈ ਮੂਲ macOS ਪੈਕੇਜ ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ (ਤਾਜ਼ਾ ਲਈ ਅਧਿਕਾਰਤ ਦਸਤਾਵੇਜ਼ਾਂ ਦੀ ਜਾਂਚ ਕਰੋ):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

ਜੇ macOS ਮੂਲ ਬਾਈਨਰੀ ਅਜੇ ਉਪਲਬਧ ਨਹੀਂ ਹਨ, ਤਾਂ ਤੁਸੀਂ ਅਜੇ ਵੀ ਕਰ ਸਕਦੇ ਹੋ: 
1. Windows 11 ARM/Intel VM (Parallels / UTM) ਦੀ ਵਰਤੋਂ ਕਰੋ ਅਤੇ Windows ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। 
2. ਮਾਡਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਰਾਹੀਂ ਚਲਾਓ (ਜੇ ਕੰਟੇਨਰ ਚਿੱਤਰ ਪ੍ਰਕਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ) ਅਤੇ `FOUNDRY_LOCAL_ENDPOINT` ਨੂੰ ਉਘਾਏ ਪੋਰਟ 'ਤੇ ਸੈਟ ਕਰੋ। 

**Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ (ਕਰਾਸ-ਪਲੇਟਫਾਰਮ)**

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

pip ਨੂੰ ਅਪਗ੍ਰੇਡ ਕਰੋ ਅਤੇ ਕੋਰ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### ਕਦਮ 1.2: ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### ਕਦਮ 1.3: ਵਾਤਾਵਰਣ ਕਨਫਿਗਰ ਕਰੋ

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK ਬੂਟਸਟ੍ਰੈਪਿੰਗ (ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ)

ਸੇਵਾ ਨੂੰ ਮੈਨੂਅਲੀ ਤੌਰ 'ਤੇ ਸ਼ੁਰੂ ਕਰਨ ਅਤੇ ਮਾਡਲਾਂ ਨੂੰ ਚਲਾਉਣ ਦੀ ਬਜਾਏ, **Foundry Local Python SDK** ਸਭ ਕੁਝ ਬੂਟਸਟ੍ਰੈਪ ਕਰ ਸਕਦਾ ਹੈ:

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

ਜੇ ਤੁਸੀਂ ਸਪਸ਼ਟ ਕੰਟਰੋਲ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੇ ਹੋ ਤਾਂ ਤੁਸੀਂ CLI + OpenAI ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ ਜਿਵੇਂ ਕਿ ਬਾਅਦ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ।

### 2. ਮਾਡਲਾਂ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ CLI ਰਾਹੀਂ ਚਲਾਓ (10 ਮਿੰਟ)

#### ਕਦਮ 3.1: Phi-4 ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### ਕਦਮ 3.2: GPT-OSS-20B ਡਿਪਲੌਇ ਕਰੋ

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### ਕਦਮ 3.3: ਵਾਧੂ ਮਾਡਲ ਲੋਡ ਕਰੋ

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ: Foundry Local ਲਈ 01-run-phi ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ (5 ਮਿੰਟ)

#### ਕਦਮ 4.1: ਬੇਸਿਕ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓ

`samples/01-foundry-quickstart/chat_quickstart.py` ਬਣਾਓ (ਜੇ ਮੈਨੇਜਰ ਉਪਲਬਧ ਹੋਵੇ ਤਾਂ ਇਸਨੂੰ ਵਰਤੋ):

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

#### ਕਦਮ 4.2: ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## ਕਵਰ ਕੀਤੇ ਮੁੱਖ ਸੰਕਲਪ

### 1. Foundry Local ਆਰਕੀਟੈਕਚਰ

- **ਸਥਾਨਕ ਇੰਫਰੈਂਸ ਇੰਜਨ**: ਮਾਡਲਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਤੁਹਾਡੇ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਂਦਾ ਹੈ
- **OpenAI SDK ਅਨੁਕੂਲਤਾ**: ਮੌਜੂਦਾ OpenAI ਕੋਡ ਨਾਲ ਬੇਰੋਕ ਟਿਕਾਉ
- **ਮਾਡਲ ਮੈਨੇਜਮੈਂਟ**: ਕਈ ਮਾਡਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ, ਕੈਸ਼ ਅਤੇ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਚਲਾਓ
- **ਹਾਰਡਵੇਅਰ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ**: GPU, NPU, ਅਤੇ CPU ਐਕਸਲੇਰੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰੋ

### 2. CLI ਕਮਾਂਡ ਰੈਫਰੈਂਸ

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ

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

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### ਸਮੱਸਿਆ 1: "Foundry ਕਮਾਂਡ ਨਹੀਂ ਮਿਲੀ"

**ਹੱਲ:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### ਸਮੱਸਿਆ 2: "ਮਾਡਲ ਲੋਡ ਕਰਨ ਵਿੱਚ ਅਸਫਲ"

**ਹੱਲ:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### ਸਮੱਸਿਆ 3: "localhost:5273 'ਤੇ ਕਨੈਕਸ਼ਨ ਰਿਫਿਊਜ਼ਡ"

**ਹੱਲ:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## ਪ੍ਰਦਰਸ਼ਨ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਟਿਪਸ

### 1. ਮਾਡਲ ਚੋਣ ਰਣਨੀਤੀ

- **Phi-4-mini**: ਆਮ ਕੰਮਾਂ ਲਈ ਵਧੀਆ, ਘੱਟ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ
- **Qwen2.5-0.5b**: ਸਭ ਤੋਂ ਤੇਜ਼ ਇੰਫਰੈਂਸ, ਘੱਟ ਸਰੋਤਾਂ ਦੀ ਲੋੜ
- **GPT-OSS-20B**: ਸਭ ਤੋਂ ਉੱਚ ਗੁਣਵੱਤਾ, ਵਧੇਰੇ ਸਰੋਤਾਂ ਦੀ ਲੋੜ
- **DeepSeek-Coder**: ਪ੍ਰੋਗਰਾਮਿੰਗ ਕੰਮਾਂ ਲਈ ਅਪਟਿਮਾਈਜ਼ ਕੀਤਾ

### 2. ਹਾਰਡਵੇਅਰ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਨਿਗਰਾਨੀ

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

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਸੁਧਾਰ | ਕੀ ਹੈ | ਕਿਵੇਂ |
|-------|-------|-------|
| ਸਾਂਝੇ ਯੂਟਿਲਿਟੀਜ਼ | ਡੁਪਲੀਕੇਟ ਕਲਾਇੰਟ/ਬੂਟਸਟ੍ਰੈਪ ਲੌਜਿਕ ਨੂੰ ਹਟਾਓ | `Workshop/samples/workshop_utils.py` ਦੀ ਵਰਤੋਂ ਕਰੋ (`get_client`, `chat_once`) |
| ਟੋਕਨ ਵਰਤੋਂ ਦ੍ਰਿਸ਼ਮਾਨਤਾ | ਲਾਗਤ/ਕੁਸ਼ਲਤਾ ਦੀ ਸੋਚ ਸਿਖਾਓ | `SHOW_USAGE=1` ਸੈਟ ਕਰੋ ਤਾਂ ਜੋ ਪ੍ਰੌਮਪਟ/ਕੰਪਲੀਸ਼ਨ/ਕੁੱਲ ਟੋਕਨ ਪ੍ਰਿੰਟ ਹੋਣ |
| ਨਿਰਧਾਰਿਤ ਤੁਲਨਾਵਾਂ | ਸਥਿਰ ਬੈਂਚਮਾਰਕਿੰਗ ਅਤੇ ਰਿਗਰੈਸ਼ਨ ਜਾਂਚ | `temperature=0`, `top_p=1`, ਸਥਿਰ ਪ੍ਰੌਮਪਟ ਟੈਕਸਟ ਦੀ ਵਰਤੋਂ ਕਰੋ |
| ਪਹਿਲਾ-ਟੋਕਨ ਲੇਟੈਂਸੀ | ਮਹਿਸੂਸ ਕੀਤੀ ਗਈ ਪ੍ਰਤੀਕ੍ਰਿਆ ਮੈਟ੍ਰਿਕ | ਸਟ੍ਰੀਮਿੰਗ ਨਾਲ ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ ਅਨੁਕੂਲ ਬਣਾਓ (`BENCH_STREAM=1`) |
| ਅਸਥਾਈ ਗਲਤੀਆਂ 'ਤੇ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ | ਠੰਡੇ ਸ਼ੁਰੂ 'ਤੇ ਲਚੀਲਾਪਨ ਡੈਮੋ | `RETRY_ON_FAIL=1` (ਡਿਫਾਲਟ) ਅਤੇ `RETRY_BACKOFF` ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ |
| ਸਮੋਕ ਟੈਸਟਿੰਗ | ਮੁੱਖ ਫਲੋਜ਼ 'ਤੇ ਤੇਜ਼ ਸੈਨਿਟੀ | ਵਰਕਸ਼ਾਪ ਤੋਂ ਪਹਿਲਾਂ `python Workshop/tests/smoke.py` ਚਲਾਓ |
| ਮਾਡਲ ਅਲਿਆਸ ਪ੍ਰੋਫਾਈਲ | ਮਸ਼ੀਨਾਂ ਦੇ ਵਿਚਕਾਰ ਮਾਡਲ ਸੈੱਟ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪਿਵਟ ਕਰੋ | `.env` ਨੂੰ `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` ਨਾਲ ਰੱਖੋ |
| ਕੈਸ਼ਿੰਗ ਕੁਸ਼ਲਤਾ | ਕਈ-ਨਮੂਨਾ ਚਾਲ ਵਿੱਚ ਦੁਹਰਾਏ ਗਏ ਵਾਰਮਅੱਪ ਤੋਂ ਬਚੋ | ਯੂਟਿਲਿਟੀਜ਼ ਕੈਸ਼ ਮੈਨੇਜਰ; ਸਕ੍ਰਿਪਟ/ਨੋਟਬੁੱਕ ਵਿੱਚ ਦੁਬਾਰਾ ਵਰਤੋਂ ਕਰੋ |
| ਪਹਿਲੀ ਚਾਲ ਵਾਰਮਅੱਪ | p95 ਲੇਟੈਂਸੀ ਸਪਾਈਕ ਨੂੰ ਘਟਾਓ | `FoundryLocalManager` ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਇੱਕ ਛੋਟਾ ਪ੍ਰੌਮਪਟ ਚਲਾਓ |

ਨਿਰਧਾਰਿਤ ਵਾਰਮ ਬੇਸਲਾਈਨ ਦਾ ਉਦਾਹਰਨ (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

ਤੁਹਾਨੂੰ ਦੂਜੇ ਚਾਲ 'ਤੇ ਸਮਾਨ ਆਉਟਪੁੱਟ ਅਤੇ ਇੱਕੋ ਜਿਹੇ ਟੋਕਨ ਗਿਣਤੀ ਦੇਖਣੀ ਚਾਹੀਦੀ ਹੈ, ਜੋ ਨਿਰਧਾਰਿਤਤਾ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ।

## ਅਗਲੇ ਕਦਮ

ਇਸ ਸੈਸ਼ਨ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ:

1. **ਸੈਸ਼ਨ 2 ਦੀ ਖੋਜ ਕਰੋ**: Azure AI Foundry RAG ਨਾਲ AI ਹੱਲ ਬਣਾਓ
2. **ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ**: Qwen, DeepSeek, ਅਤੇ ਹੋਰ ਮਾਡਲ ਪਰਿਵਾਰਾਂ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰੋ
3. **ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਅਪਟਿਮਾਈਜ਼ ਕਰੋ**: ਆਪਣੇ ਵਿਸ਼ੇਸ਼ ਹਾਰਡਵੇਅਰ ਲਈ ਸੈਟਿੰਗਾਂ ਨੂੰ ਸੁਧਾਰੋ
4. **ਕਸਟਮ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓ**: Foundry Local SDK ਦੀ ਵਰਤੋਂ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟਾਂ ਵਿੱਚ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

### ਦਸਤਾਵੇਜ਼
- [Foundry Local Python SDK ਰੈਫਰੈਂਸ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local ਇੰਸਟਾਲੇਸ਼ਨ ਗਾਈਡ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [ਮਾਡਲ ਕੈਟਾਲੌਗ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### ਨਮੂਨਾ ਕੋਡ
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### ਕਮਿਊਨਿਟੀ
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ ਹੱਥ-ਅਨੁਭਵ + 15 ਮਿੰਟ Q&A
**ਮੁਸ਼ਕਲ ਪੱਧਰ**: ਸ਼ੁਰੂਆਤੀ
**ਪੂਰਵ ਸ਼ਰਤਾਂ**: Windows 11, Python 3.10+, ਐਡਮਿਨਿਸਟ੍ਰੇਟਰ ਐਕਸੈਸ

## ਨਮੂਨਾ ਸਥਿਤੀ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ / ਨੋਟਬੁੱਕ | ਸਥਿਤੀ | ਲਕਸ਼ | ਉਦਾਹਰਨ ਇਨਪੁੱਟ | ਲੋੜੀਂਦਾ ਡਾਟਾਸੈਟ |
|----------------------------|--------|------|----------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | ਡਿਵੈਲਪਰ ਟੀਮ ਜੋ ਡਿਵਾਈਸ ਇੰਫਰੈਂਸ ਨੂੰ ਪ੍ਰਾਈਵੇਸੀ ਅਸੈਸਮੈਂਟ ਪੋਰਟਲ ਲਈ ਅਨੁਕੂਲ ਬਣਾਉਣ ਦੀ ਜਾਂਚ ਕਰ ਰਹੀ ਹੈ | ਸਥਾਨਕ SLM ਨੂੰ ਸਾਬਤ ਕਰੋ ਕਿ ਸਟੈਂਡਰਡ ਪ੍ਰੌਮਪਟ 'ਤੇ ਸਬ-ਸੈਕੰਡ ਲੇਟੈਂਸੀ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ | "List two benefits of local inference." | ਕੋਈ ਨਹੀਂ (ਸਿੰਗਲ ਪ੍ਰੌਮਪਟ) |
| Quickstart adaptation code block | ਡਿਵੈਲਪਰ ਜੋ ਮੌਜੂਦਾ OpenAI ਸਕ੍ਰਿਪਟ ਨੂੰ Foundry Local ਵਿੱਚ ਮਾਈਗਰੇਟ ਕਰ ਰਿਹਾ ਹੈ | ਡ੍ਰੌਪ-ਇਨ ਅਨੁਕੂਲਤਾ ਦਿਖਾਓ | "Give two benefits of local inference." | ਸਿਰਫ ਇਨਲਾਈਨ ਪ੍ਰੌਮਪਟ |

### ਸਥਿਤੀ ਕਹਾਣੀ
ਸੁਰੱਖਿਆ ਅਤੇ ਕੰਪਲਾਇੰਸ ਸਕੁਐਡ ਨੂੰ ਇਹ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਸੰਵੇਦਨਸ਼ੀਲ ਪ੍ਰੋਟੋਟਾਈਪ ਡਾਟਾ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਉਹ ਬੂਟਸਟ੍ਰੈਪ ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਈ ਪ੍ਰੌਮਪਟਾਂ (ਪ੍ਰਾਈਵੇਸੀ, ਲੇਟੈਂਸੀ, ਲਾਗਤ) ਨਾਲ ਚਲਾਉਂਦੇ ਹਨ ਜੋ ਨਿਰਧਾਰਿਤ temperature=0 ਮੋਡ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਬਾਅਦ ਵਿੱਚ ਤੁਲਨਾ ਲਈ ਬੇਸਲਾਈਨ ਆਉਟਪੁੱਟ ਕੈਪਚਰ ਕੀਤਾ ਜਾ ਸਕੇ (ਸੈਸ਼ਨ 3 ਬੈਂਚਮਾਰਕਿੰਗ ਅਤੇ ਸੈਸ਼ਨ 4 SLM ਵਿਰੁੱਧ LLM ਵਿਰੋਧ).

### ਘੱਟੋ-ਘੱਟ ਪ੍ਰੌਮਪਟ ਸੈੱਟ JSON (ਵਿਕਲਪਿਕ)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

ਇਸ ਸੂਚੀ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।