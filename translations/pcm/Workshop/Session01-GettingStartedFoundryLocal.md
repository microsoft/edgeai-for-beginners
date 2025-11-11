<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-11-11T17:38:45+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pcm"
}
-->
# Session 1: How to Start with Foundry Local

## Abstract

Make we start our journey with Foundry Local by install am and set am up for Windows 11. You go learn how to set up CLI, enable hardware acceleration, and cache models so local inference go fast. This session go show you how to run models like Phi, Qwen, DeepSeek, and GPT-OSS-20B with CLI commands wey you fit repeat.

## Learning Objectives

By the end of this session, you go sabi:

- **Install and Configure**: How to set up Foundry Local for Windows 11 with better performance settings
- **Master CLI Operations**: Use Foundry Local CLI to manage and deploy models
- **Enable Hardware Acceleration**: Set GPU acceleration with ONNXRuntime or WebGPU
- **Deploy Multiple Models**: Run phi-4, GPT-OSS-20B, Qwen, and DeepSeek models for your machine
- **Build Your First App**: Change existing samples to use Foundry Local Python SDK

# Test the model (non-interactive single prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 or later)
# List available catalog models (loaded models go show after you run them)
foundry model list
## NOTE: No `--running` flag dey now; to see which models dey loaded, start chat or check service logs.
- Python 3.10+ installed
- Visual Studio Code with Python extension
- Administrator privileges to install am

### (Optional) Environment Variables

Create `.env` file (or set am for shell) so scripts go dey portable:
# Compare responses (non-interactive)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Model alias wey you like (catalog go auto-select better variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Change endpoint (if you no wan use auto from manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Enable streaming demo | `true` |

> If `FOUNDRY_LOCAL_ENDPOINT=auto` (or you no set am), we go get am from SDK manager.

## Demo Flow (30 minutes)

### 1. Install Foundry Local and Check CLI Setup (10 minutes)

# List cached models
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / If Supported)**

If native macOS package dey (check official docs for latest):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

If macOS native binaries no dey yet, you fit still: 
1. Use Windows 11 ARM/Intel VM (Parallels / UTM) and follow Windows steps. 
2. Run models with container (if container image dey) and set `FOUNDRY_LOCAL_ENDPOINT` to the port wey dey exposed. 

**Create Python Virtual Environment (Cross‑Platform)**

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

Upgrade pip and install core dependencies:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Step 1.2: Check Installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Step 1.3: Set Environment

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Recommended)

Instead of starting service manually & running models, the **Foundry Local Python SDK** fit help you start everything:

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

If you wan control am yourself, you fit still use CLI + OpenAI client as we go show later.

### 2. Run Models Locally with CLI (10 minutes)

#### Step 3.1: Deploy Phi-4 Model

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Step 3.2: Deploy GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Step 3.3: Load More Models

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Starter Project: Change 01-run-phi for Foundry Local (5 minutes)

#### Step 4.1: Create Simple Chat App

Create `samples/01-foundry-quickstart/chat_quickstart.py` (update am to use manager if e dey):

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

#### Step 4.2: Test the App

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Key Concepts We Cover

### 1. Foundry Local Architecture

- **Local Inference Engine**: Models go run for your device
- **OpenAI SDK Compatibility**: Fit work well with OpenAI code wey dey already
- **Model Management**: Download, cache, and run plenty models well
- **Hardware Optimization**: Use GPU, NPU, and CPU acceleration

### 2. CLI Command Reference

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK Integration

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

## How to Solve Common Problems

### Problem 1: "Foundry command no dey"

**Solution:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Model no load"

**Solution:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Connection no work for localhost:5273"

**Solution:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips to Make Performance Better

### 1. How to Choose Model

- **Phi-4-mini**: Good for general tasks, e no use plenty memory
- **Qwen2.5-0.5b**: Fast inference, e no need plenty resources
- **GPT-OSS-20B**: Best quality, but e need more resources
- **DeepSeek-Coder**: E dey good for programming tasks

### 2. Hardware Optimization

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Check Performance

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

### Optional Improvements

| Improvement | Wetin e do | How |
|-------------|------------|-----|
| Shared Utilities | Remove duplicate client/bootstrap logic | Use `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Token Usage Visibility | Teach cost/efficiency thinking early | Set `SHOW_USAGE=1` to print prompt/completion/total tokens |
| Deterministic Comparisons | Stable benchmarking & regression checks | Use `temperature=0`, `top_p=1`, consistent prompt text |
| First-Token Latency | Perceived responsiveness metric | Adapt benchmark script with streaming (`BENCH_STREAM=1`) |
| Retry on Transient Errors | Resilient demos on cold start | `RETRY_ON_FAIL=1` (default) & adjust `RETRY_BACKOFF` |
| Smoke Testing | Quick sanity across key flows | Run `python Workshop/tests/smoke.py` before a workshop |
| Model Alias Profiles | Quickly pivot model set between machines | Maintain `.env` with `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Caching Efficiency | Avoid repeated warmups in multi-sample run | Utilities cache managers; reuse across scripts/notebooks |
| First Run Warmup | Reduce p95 latency spikes | Fire a tiny prompt after `FoundryLocalManager` creation |

Example deterministic warm baseline (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

You suppose see similar output & same token counts for second run, e mean say e dey stable.

## Wetin Next?

After you finish this session:

1. **Check Session 2**: Build AI solutions with Azure AI Foundry RAG
2. **Try Different Models**: Play with Qwen, DeepSeek, and other model families
3. **Make Performance Better**: Adjust settings for your hardware
4. **Build Your Own Apps**: Use Foundry Local SDK for your projects

## Extra Resources

### Documentation
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Sample Code
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Community
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Session Duration**: 30 minutes hands-on + 15 minutes Q&A
**Difficulty Level**: Beginner
**Prerequisites**: Windows 11, Python 3.10+, Administrator access

## Sample Scenario & Workshop Mapping

| Workshop Script / Notebook | Scenario | Goal | Example Input(s) | Dataset Needed |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internal IT team wey dey check on‑device inference for privacy assessment portal | Prove say local SLM dey respond fast for standard prompts | "List two benefits of local inference." | None (single prompt) |
| Quickstart adaptation code block | Developer wey dey move OpenAI script to Foundry Local | Show say e fit work well | "Give two benefits of local inference." | Inline prompt only |

### Scenario Narrative
The security & compliance team wan check if sensitive prototype data fit process locally. Dem go run the bootstrap script with different prompts (privacy, latency, cost) using deterministic temperature=0 mode to get baseline outputs for later comparison (Session 3 benchmarking and Session 4 SLM vs LLM contrast).

### Minimal Prompt Set JSON (optional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Use this list to create reproducible evaluation loop or to plan future regression test harness.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->