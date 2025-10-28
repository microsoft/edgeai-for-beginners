<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:24:58+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "tl"
}
-->
# Session 1: Pagsisimula sa Foundry Local

## Abstrak

Simulan ang iyong paglalakbay sa Foundry Local sa pamamagitan ng pag-install at pag-configure nito sa Windows 11. Matutunan kung paano i-set up ang CLI, paganahin ang hardware acceleration, at i-cache ang mga modelo para sa mabilis na lokal na inference. Ang hands-on na sesyon na ito ay magpapakita kung paano patakbuhin ang mga modelo tulad ng Phi, Qwen, DeepSeek, at GPT-OSS-20B gamit ang mga reproducible na CLI command.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng sesyon na ito, magagawa mo ang sumusunod:

- **Mag-install at Mag-configure**: I-set up ang Foundry Local sa Windows 11 gamit ang optimal na performance settings
- **Masterin ang CLI Operations**: Gamitin ang Foundry Local CLI para sa pamamahala at deployment ng modelo
- **Paganahin ang Hardware Acceleration**: I-configure ang GPU acceleration gamit ang ONNXRuntime o WebGPU
- **Mag-deploy ng Maramihang Modelo**: Patakbuhin ang phi-4, GPT-OSS-20B, Qwen, at DeepSeek na mga modelo nang lokal
- **Bumuo ng Iyong Unang App**: I-adapt ang mga umiiral na sample upang magamit ang Foundry Local Python SDK

# Subukan ang modelo (non-interactive single prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 o mas bago)
# Ilista ang mga available na modelo sa catalog (lumalabas ang mga loaded na modelo kapag na-run na)
foundry model list
## NOTE: Sa kasalukuyan, walang dedikadong `--running` flag; upang makita kung alin ang loaded, mag-initiate ng chat o i-inspect ang service logs.
- Nakainstall ang Python 3.10+
- Visual Studio Code na may Python extension
- Administrator privileges para sa pag-install

### (Opsyonal) Mga Environment Variable

Gumawa ng `.env` (o i-set sa shell) upang gawing portable ang mga script:
# Ihambing ang mga sagot (non-interactive)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variable | Layunin | Halimbawa |
|----------|---------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Preferred na alias ng modelo (ang catalog ay awtomatikong pumipili ng pinakamahusay na variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Override endpoint (kung hindi, awtomatikong mula sa manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Paganahin ang streaming demo | `true` |

> Kung `FOUNDRY_LOCAL_ENDPOINT=auto` (o hindi naka-set), kukunin ito mula sa SDK manager.

## Daloy ng Demo (30 minuto)

### 1. I-install ang Foundry Local at I-verify ang CLI Setup (10 minuto)

# Ilista ang mga cached na modelo
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / Kung Suportado)**

Kung may native na macOS package (tingnan ang opisyal na dokumento para sa pinakabago):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Kung ang macOS native binaries ay hindi pa available, maaari mo pa ring gawin ang sumusunod: 
1. Gumamit ng Windows 11 ARM/Intel VM (Parallels / UTM) at sundin ang mga hakbang sa Windows. 
2. Patakbuhin ang mga modelo gamit ang container (kung may published na container image) at i-set ang `FOUNDRY_LOCAL_ENDPOINT` sa exposed na port. 

**Gumawa ng Python Virtual Environment (Cross‑Platform)**

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

I-upgrade ang pip at i-install ang mga pangunahing dependencies:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Hakbang 1.2: I-verify ang Pag-install

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Hakbang 1.3: I-configure ang Environment

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Inirerekomenda)

Sa halip na manu-manong simulan ang serbisyo at patakbuhin ang mga modelo, ang **Foundry Local Python SDK** ay maaaring mag-bootstrap ng lahat:

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

Kung mas gusto mo ang explicit na kontrol, maaari mo pa ring gamitin ang CLI + OpenAI client tulad ng ipinakita sa ibang bahagi.

### 2. Patakbuhin ang Mga Modelo Lokal gamit ang CLI (10 minuto)

#### Hakbang 3.1: I-deploy ang Phi-4 Model

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Hakbang 3.2: I-deploy ang GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Hakbang 3.3: I-load ang Karagdagang Mga Modelo

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Starter Project: I-adapt ang 01-run-phi para sa Foundry Local (5 minuto)

#### Hakbang 4.1: Gumawa ng Basic Chat Application

Gumawa ng `samples/01-foundry-quickstart/chat_quickstart.py` (na-update upang gamitin ang manager kung available):

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

#### Hakbang 4.2: Subukan ang Application

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Mga Pangunahing Konseptong Tinalakay

### 1. Arkitektura ng Foundry Local

- **Local Inference Engine**: Pinapatakbo ang mga modelo nang buo sa iyong device
- **OpenAI SDK Compatibility**: Seamless na integrasyon sa umiiral na OpenAI code
- **Pamamahala ng Modelo**: I-download, i-cache, at patakbuhin ang maramihang mga modelo nang epektibo
- **Hardware Optimization**: Gamitin ang GPU, NPU, at CPU acceleration

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

## Pag-troubleshoot ng Karaniwang Mga Isyu

### Isyu 1: "Foundry command not found"

**Solusyon:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Isyu 2: "Model failed to load"

**Solusyon:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Isyu 3: "Connection refused on localhost:5273"

**Solusyon:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Mga Tip sa Pag-optimize ng Performance

### 1. Estratehiya sa Pagpili ng Modelo

- **Phi-4-mini**: Pinakamahusay para sa pangkalahatang gawain, mababang memory usage
- **Qwen2.5-0.5b**: Pinakamabilis na inference, minimal na resources
- **GPT-OSS-20B**: Pinakamataas na kalidad, nangangailangan ng mas maraming resources
- **DeepSeek-Coder**: Na-optimize para sa mga programming task

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

### 3. Pagsubaybay sa Performance

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

### Opsyonal na Mga Pagpapahusay

| Pagpapahusay | Ano | Paano |
|-------------|-----|-------|
| Shared Utilities | Tanggalin ang duplicate na client/bootstrap logic | Gamitin ang `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibility ng Token Usage | Turuan ang cost/efficiency thinking nang maaga | I-set ang `SHOW_USAGE=1` upang ipakita ang prompt/completion/total tokens |
| Deterministic Comparisons | Stable na benchmarking at regression checks | Gamitin ang `temperature=0`, `top_p=1`, consistent na prompt text |
| First-Token Latency | Sukatin ang perceived responsiveness | I-adapt ang benchmark script gamit ang streaming (`BENCH_STREAM=1`) |
| Retry on Transient Errors | Resilient na demo sa cold start | `RETRY_ON_FAIL=1` (default) at i-adjust ang `RETRY_BACKOFF` |
| Smoke Testing | Mabilis na sanity check sa mga pangunahing flow | Patakbuhin ang `python Workshop/tests/smoke.py` bago ang workshop |
| Model Alias Profiles | Mabilis na pag-pivot ng model set sa pagitan ng mga makina | Panatilihin ang `.env` na may `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Caching Efficiency | Iwasan ang paulit-ulit na warmups sa multi-sample run | Utilities cache managers; i-reuse sa mga script/notebooks |
| First Run Warmup | Bawasan ang p95 latency spikes | Magpatakbo ng maliit na prompt pagkatapos ng `FoundryLocalManager` creation |

Halimbawa ng deterministic warm baseline (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Makikita mo ang katulad na output at pare-parehong bilang ng token sa pangalawang run, na nagpapatunay ng determinism.

## Mga Susunod na Hakbang

Pagkatapos makumpleto ang sesyon na ito:

1. **I-explore ang Session 2**: Bumuo ng AI solutions gamit ang Azure AI Foundry RAG
2. **Subukan ang Iba't Ibang Modelo**: Mag-eksperimento sa Qwen, DeepSeek, at iba pang pamilya ng modelo
3. **I-optimize ang Performance**: I-fine-tune ang mga setting para sa iyong partikular na hardware
4. **Bumuo ng Custom na Mga Application**: Gamitin ang Foundry Local SDK sa iyong sariling mga proyekto

## Karagdagang Mga Mapagkukunan

### Dokumentasyon
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Sample Code
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Komunidad
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Tagal ng Sisyon**: 30 minuto hands-on + 15 minuto Q&A  
**Antas ng Kahirapan**: Baguhan  
**Mga Kinakailangan**: Windows 11, Python 3.10+, Administrator access  

## Sample Scenario & Workshop Mapping

| Workshop Script / Notebook | Scenario | Layunin | Halimbawa ng Input(s) | Dataset na Kailangan |
|----------------------------|----------|---------|-----------------------|----------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internal IT team na nag-evaluate ng on‑device inference para sa privacy assessment portal | Patunayan na ang lokal na SLM ay tumutugon sa sub‑second latency sa standard prompts | "List two benefits of local inference." | Wala (single prompt) |
| Quickstart adaptation code block | Developer na nagmamigrate ng umiiral na OpenAI script sa Foundry Local | Ipakita ang drop‑in compatibility | "Give two benefits of local inference." | Inline prompt lamang |

### Narrative ng Scenario
Ang security & compliance squad ay kailangang mag-validate kung ang sensitibong prototype data ay maaaring iproseso nang lokal. Pinapatakbo nila ang bootstrap script gamit ang ilang prompt (privacy, latency, cost) gamit ang deterministic na temperature=0 mode upang makuha ang baseline outputs para sa susunod na comparison (Session 3 benchmarking at Session 4 SLM vs LLM contrast).

### Minimal Prompt Set JSON (opsyonal)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Gamitin ang listahan na ito upang gumawa ng reproducible evaluation loop o upang mag-seed ng future regression test harness.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.