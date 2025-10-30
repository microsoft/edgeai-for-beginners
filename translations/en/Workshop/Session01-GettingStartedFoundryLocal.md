<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T19:57:43+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "en"
}
-->
# Session 1: Getting Started with Foundry Local

## Abstract

Begin your journey with Foundry Local by installing and configuring it on Windows 11. Learn how to set up the CLI, enable hardware acceleration, and cache models for fast local inference. This hands-on session guides you through running models like Phi, Qwen, DeepSeek, and GPT-OSS-20B using reproducible CLI commands.

## Learning Objectives

By the end of this session, you will:

- **Install and Configure**: Set up Foundry Local on Windows 11 with optimal performance settings
- **Master CLI Operations**: Use Foundry Local CLI for model management and deployment
- **Enable Hardware Acceleration**: Configure GPU acceleration with ONNXRuntime or WebGPU
- **Deploy Multiple Models**: Run phi-4, GPT-OSS-20B, Qwen, and DeepSeek models locally
- **Build Your First App**: Adapt existing samples to use Foundry Local Python SDK

# Test the model (non-interactive single prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 or later)
# List available catalog models (loaded models appear once run)
foundry model list
## NOTE: There is currently no dedicated `--running` flag; to see which are loaded, initiate a chat or inspect service logs.
- Python 3.10+ installed
- Visual Studio Code with Python extension
- Administrator privileges for installation

### (Optional) Environment Variables

Create a `.env` (or set in shell) to make scripts portable:
# Compare responses (non-interactive)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Preferred model alias (catalog auto-selects best variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Override endpoint (otherwise auto from manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Enable streaming demo | `true` |

> If `FOUNDRY_LOCAL_ENDPOINT=auto` (or unset) we derive it from the SDK manager.

## Demo Flow (30 minutes)

### 1. Install Foundry Local and Verify CLI Setup (10 minutes)

# List cached models
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / If Supported)**

If a native macOS package is provided (check official docs for latest):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

If macOS native binaries are not yet available, you can still: 
1. Use a Windows 11 ARM/Intel VM (Parallels / UTM) and follow Windows steps. 
2. Run models via container (if container image published) and set `FOUNDRY_LOCAL_ENDPOINT` to the exposed port. 

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

#### Step 1.2: Verify Installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Step 1.3: Configure Environment

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Recommended)

Instead of manually starting the service & running models, the **Foundry Local Python SDK** can bootstrap everything:

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

If you prefer explicit control you can still use the CLI + OpenAI client as shown later.

### 2. Run Models Locally via CLI (10 minutes)

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

#### Step 3.3: Load Additional Models

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Starter Project: Adapt 01-run-phi for Foundry Local (5 minutes)

#### Step 4.1: Create Basic Chat Application

Create `samples/01-foundry-quickstart/chat_quickstart.py` (updated to use the manager if available):

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

#### Step 4.2: Test the Application

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Key Concepts Covered

### 1. Foundry Local Architecture

- **Local Inference Engine**: Runs models entirely on your device
- **OpenAI SDK Compatibility**: Seamless integration with existing OpenAI code
- **Model Management**: Download, cache, and run multiple models efficiently
- **Hardware Optimization**: Leverage GPU, NPU, and CPU acceleration

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

## Troubleshooting Common Issues

### Issue 1: "Foundry command not found"

**Solution:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Issue 2: "Model failed to load"

**Solution:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Issue 3: "Connection refused on localhost:5273"

**Solution:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Performance Optimization Tips

### 1. Model Selection Strategy

- **Phi-4-mini**: Best for general tasks, lower memory usage
- **Qwen2.5-0.5b**: Fastest inference, minimal resources
- **GPT-OSS-20B**: Highest quality, requires more resources
- **DeepSeek-Coder**: Optimized for programming tasks

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

### 3. Monitoring Performance

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

### Optional Enhancements

| Enhancement | What | How |
|-------------|------|-----|
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

You should see similar output & identical token counts on the second run, confirming determinism.

## Next Steps

After completing this session:

1. **Explore Session 2**: Build AI solutions with Azure AI Foundry RAG
2. **Try Different Models**: Experiment with Qwen, DeepSeek, and other model families
3. **Optimize Performance**: Fine-tune settings for your specific hardware
4. **Build Custom Applications**: Use the Foundry Local SDK in your own projects

## Additional Resources

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
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internal IT team evaluating on‑device inference for a privacy assessment portal | Prove local SLM responds within sub‑second latency on standard prompts | "List two benefits of local inference." | None (single prompt) |
| Quickstart adaptation code block | Developer migrating an existing OpenAI script to Foundry Local | Show drop‑in compatibility | "Give two benefits of local inference." | Inline prompt only |

### Scenario Narrative
The security & compliance squad must validate whether sensitive prototype data can be processed locally. They run the bootstrap script with several prompts (privacy, latency, cost) using a deterministic temperature=0 mode to capture baseline outputs for later comparison (Session 3 benchmarking and Session 4 SLM vs LLM contrast).

### Minimal Prompt Set JSON (optional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Use this list to create a reproducible evaluation loop or to seed a future regression test harness.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.