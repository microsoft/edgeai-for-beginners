<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:17:15+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "bn"
}
-->
# সেশন ১: ফাউন্ড্রি লোকাল দিয়ে শুরু করা

## সারসংক্ষেপ

ফাউন্ড্রি লোকাল দিয়ে আপনার যাত্রা শুরু করুন Windows 11-এ এটি ইনস্টল এবং কনফিগার করে। CLI সেট আপ করা, হার্ডওয়্যার অ্যাক্সেলারেশন সক্রিয় করা এবং দ্রুত লোকাল ইনফারেন্সের জন্য মডেল ক্যাশ করার পদ্ধতি শিখুন। এই হাতে-কলম সেশনটি পুনরায় ব্যবহারযোগ্য CLI কমান্ড ব্যবহার করে Phi, Qwen, DeepSeek এবং GPT-OSS-20B মডেল চালানোর প্রক্রিয়া দেখায়।

## শেখার লক্ষ্যসমূহ

এই সেশনের শেষে, আপনি:

- **ইনস্টল এবং কনফিগার**: Windows 11-এ ফাউন্ড্রি লোকাল সেট আপ করুন সর্বোত্তম পারফরম্যান্স সেটিংস সহ
- **CLI অপারেশন আয়ত্ত করুন**: মডেল ম্যানেজমেন্ট এবং ডিপ্লয়মেন্টের জন্য ফাউন্ড্রি লোকাল CLI ব্যবহার করুন
- **হার্ডওয়্যার অ্যাক্সেলারেশন সক্রিয় করুন**: ONNXRuntime বা WebGPU দিয়ে GPU অ্যাক্সেলারেশন কনফিগার করুন
- **একাধিক মডেল ডিপ্লয় করুন**: phi-4, GPT-OSS-20B, Qwen এবং DeepSeek মডেল লোকালভাবে চালান
- **আপনার প্রথম অ্যাপ তৈরি করুন**: বিদ্যমান নমুনাগুলি ফাউন্ড্রি লোকাল Python SDK ব্যবহার করার জন্য মানিয়ে নিন

# মডেল পরীক্ষা করুন (নন-ইন্টারঅ্যাকটিভ একক প্রম্পট)
foundry model run phi-4-mini --prompt "হ্যালো, নিজেকে পরিচয় করিয়ে দিন"

- Windows 11 (22H2 বা পরবর্তী)
# উপলব্ধ ক্যাটালগ মডেল তালিকা করুন (লোড করা মডেলগুলি চালানোর পরে প্রদর্শিত হয়)
foundry model list
## NOTE: বর্তমানে কোনও নির্দিষ্ট `--running` ফ্ল্যাগ নেই; কোনটি লোড হয়েছে তা দেখতে, একটি চ্যাট শুরু করুন বা সার্ভিস লগ পরিদর্শন করুন।
- Python 3.10+ ইনস্টল করা
- Visual Studio Code Python এক্সটেনশন সহ
- ইনস্টলেশনের জন্য অ্যাডমিনিস্ট্রেটর প্রিভিলেজ

### (ঐচ্ছিক) পরিবেশ ভেরিয়েবল

`.env` তৈরি করুন (বা শেলে সেট করুন) স্ক্রিপ্টগুলিকে পোর্টেবল করতে:
# প্রতিক্রিয়া তুলনা করুন (নন-ইন্টারঅ্যাকটিভ)
foundry model run gpt-oss-20b --prompt "সাধারণ ভাষায় এজ AI ব্যাখ্যা করুন"
| ভেরিয়েবল | উদ্দেশ্য | উদাহরণ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | পছন্দের মডেল এলিয়াস (ক্যাটালগ সেরা ভ্যারিয়েন্ট নির্বাচন করে) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | এন্ডপয়েন্ট ওভাররাইড করুন (অন্যথায় ম্যানেজার থেকে স্বয়ংক্রিয়) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | স্ট্রিমিং ডেমো সক্রিয় করুন | `true` |

> যদি `FOUNDRY_LOCAL_ENDPOINT=auto` (বা আনসেট) হয়, আমরা এটি SDK ম্যানেজার থেকে নির্ধারণ করি।

## ডেমো প্রবাহ (৩০ মিনিট)

### ১. ফাউন্ড্রি লোকাল ইনস্টল এবং CLI সেটআপ যাচাই করুন (১০ মিনিট)

# ক্যাশ করা মডেল তালিকা করুন
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (প্রিভিউ / যদি সমর্থিত হয়)**

যদি একটি নেটিভ macOS প্যাকেজ প্রদান করা হয় (সর্বশেষ অফিসিয়াল ডক চেক করুন):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

যদি macOS নেটিভ বাইনারি এখনও উপলব্ধ না হয়, আপনি এখনও করতে পারেন: 
1. Windows 11 ARM/Intel VM (Parallels / UTM) ব্যবহার করুন এবং Windows ধাপগুলি অনুসরণ করুন। 
2. কন্টেইনারের মাধ্যমে মডেল চালান (যদি কন্টেইনার ইমেজ প্রকাশিত হয়) এবং `FOUNDRY_LOCAL_ENDPOINT` সেট করুন প্রকাশিত পোর্টে।

**Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন (ক্রস-প্ল্যাটফর্ম)**

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

pip আপগ্রেড করুন এবং মূল ডিপেন্ডেন্সি ইনস্টল করুন:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### ধাপ ১.২: ইনস্টলেশন যাচাই করুন

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### ধাপ ১.৩: পরিবেশ কনফিগার করুন

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK বুটস্ট্র্যাপিং (প্রস্তাবিত)

সার্ভিস ম্যানুয়ালি শুরু এবং মডেল চালানোর পরিবর্তে, **Foundry Local Python SDK** সবকিছু বুটস্ট্র্যাপ করতে পারে:

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

যদি আপনি স্পষ্ট নিয়ন্ত্রণ পছন্দ করেন তবে আপনি এখনও CLI + OpenAI ক্লায়েন্ট ব্যবহার করতে পারেন যা পরে দেখানো হয়েছে।

### ২. CLI এর মাধ্যমে লোকাল মডেল চালান (১০ মিনিট)

#### ধাপ ৩.১: Phi-4 মডেল ডিপ্লয় করুন

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### ধাপ ৩.২: GPT-OSS-20B ডিপ্লয় করুন

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### ধাপ ৩.৩: অতিরিক্ত মডেল লোড করুন

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### ৪. স্টার্টার প্রজেক্ট: Foundry Local এর জন্য ০১-run-phi মানিয়ে নিন (৫ মিনিট)

#### ধাপ ৪.১: একটি বেসিক চ্যাট অ্যাপ্লিকেশন তৈরি করুন

`samples/01-foundry-quickstart/chat_quickstart.py` তৈরি করুন (যদি ম্যানেজার উপলব্ধ থাকে তাহলে ব্যবহার করার জন্য আপডেট করা হয়েছে):

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

#### ধাপ ৪.২: অ্যাপ্লিকেশন পরীক্ষা করুন

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## মূল ধারণাগুলি আচ্ছাদিত

### ১. ফাউন্ড্রি লোকাল আর্কিটেকচার

- **লোকাল ইনফারেন্স ইঞ্জিন**: সম্পূর্ণরূপে আপনার ডিভাইসে মডেল চালায়
- **OpenAI SDK সামঞ্জস্য**: বিদ্যমান OpenAI কোডের সাথে সহজ ইন্টিগ্রেশন
- **মডেল ম্যানেজমেন্ট**: একাধিক মডেল দক্ষতার সাথে ডাউনলোড, ক্যাশ এবং চালান
- **হার্ডওয়্যার অপ্টিমাইজেশন**: GPU, NPU এবং CPU অ্যাক্সেলারেশন ব্যবহার করুন

### ২. CLI কমান্ড রেফারেন্স

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### ৩. Python SDK ইন্টিগ্রেশন

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

## সাধারণ সমস্যার সমাধান

### সমস্যা ১: "Foundry কমান্ড পাওয়া যায়নি"

**সমাধান:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### সমস্যা ২: "মডেল লোড করতে ব্যর্থ হয়েছে"

**সমাধান:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### সমস্যা ৩: "localhost:5273-এ সংযোগ প্রত্যাখ্যান করা হয়েছে"

**সমাধান:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## পারফরম্যান্স অপ্টিমাইজেশন টিপস

### ১. মডেল নির্বাচন কৌশল

- **Phi-4-mini**: সাধারণ কাজের জন্য সেরা, কম মেমরি ব্যবহার
- **Qwen2.5-0.5b**: দ্রুততম ইনফারেন্স, ন্যূনতম রিসোর্স
- **GPT-OSS-20B**: সর্বোচ্চ গুণমান, আরও রিসোর্স প্রয়োজন
- **DeepSeek-Coder**: প্রোগ্রামিং কাজের জন্য অপ্টিমাইজড

### ২. হার্ডওয়্যার অপ্টিমাইজেশন

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### ৩. পারফরম্যান্স পর্যবেক্ষণ

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

### ঐচ্ছিক উন্নতি

| উন্নতি | কী | কিভাবে |
|-------------|------|-----|
| শেয়ারড ইউটিলিটি | ক্লায়েন্ট/বুটস্ট্র্যাপ লজিকের ডুপ্লিকেট সরান | `Workshop/samples/workshop_utils.py` ব্যবহার করুন (`get_client`, `chat_once`) |
| টোকেন ব্যবহারের দৃশ্যমানতা | খরচ/দক্ষতা চিন্তা শেখান | `SHOW_USAGE=1` সেট করুন প্রম্পট/কমপ্লিশন/মোট টোকেন প্রিন্ট করতে |
| নির্ধারিত তুলনা | স্থিতিশীল বেঞ্চমার্কিং এবং রিগ্রেশন চেক | `temperature=0`, `top_p=1`, ধারাবাহিক প্রম্পট টেক্সট ব্যবহার করুন |
| প্রথম-টোকেন লেটেন্সি | প্রতিক্রিয়ার উপলব্ধি মেট্রিক | স্ট্রিমিং দিয়ে বেঞ্চমার্ক স্ক্রিপ্ট মানিয়ে নিন (`BENCH_STREAM=1`) |
| সাময়িক ত্রুটিতে পুনরায় চেষ্টা করুন | ঠান্ডা শুরুতে স্থিতিস্থাপক ডেমো | `RETRY_ON_FAIL=1` (ডিফল্ট) এবং `RETRY_BACKOFF` সামঞ্জস্য করুন |
| স্মোক টেস্টিং | মূল প্রবাহের দ্রুত স্যানিটি | ওয়ার্কশপের আগে `python Workshop/tests/smoke.py` চালান |
| মডেল এলিয়াস প্রোফাইল | মেশিনের মধ্যে দ্রুত মডেল সেট পরিবর্তন | `.env` বজায় রাখুন `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` সহ |
| ক্যাশিং দক্ষতা | একাধিক নমুনা চালানোর সময় পুনরাবৃত্তি ওয়ার্মআপ এড়ান | ইউটিলিটি ক্যাশ ম্যানেজার; স্ক্রিপ্ট/নোটবুক জুড়ে পুনরায় ব্যবহার করুন |
| প্রথম রান ওয়ার্মআপ | p95 লেটেন্সি স্পাইক কমান | `FoundryLocalManager` তৈরি করার পরে একটি ছোট প্রম্পট চালান |

উদাহরণ নির্ধারিত উষ্ণ বেসলাইন (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

আপনি দ্বিতীয় রান-এ অনুরূপ আউটপুট এবং অভিন্ন টোকেন গণনা দেখতে পাবেন, যা নির্ধারিততা নিশ্চিত করে।

## পরবর্তী পদক্ষেপ

এই সেশন সম্পন্ন করার পরে:

1. **সেশন ২ অন্বেষণ করুন**: Azure AI Foundry RAG দিয়ে AI সমাধান তৈরি করুন
2. **বিভিন্ন মডেল চেষ্টা করুন**: Qwen, DeepSeek এবং অন্যান্য মডেল পরিবার নিয়ে পরীক্ষা করুন
3. **পারফরম্যান্স অপ্টিমাইজ করুন**: আপনার নির্দিষ্ট হার্ডওয়্যারের জন্য সেটিংস ফাইন-টিউন করুন
4. **কাস্টম অ্যাপ্লিকেশন তৈরি করুন**: আপনার নিজস্ব প্রকল্পে Foundry Local SDK ব্যবহার করুন

## অতিরিক্ত সম্পদ

### ডকুমেন্টেশন
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### নমুনা কোড
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### কমিউনিটি
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**সেশন সময়কাল**: ৩০ মিনিট হাতে-কলম + ১৫ মিনিট প্রশ্নোত্তর
**কঠিনতার স্তর**: প্রাথমিক
**প্রয়োজনীয়তা**: Windows 11, Python 3.10+, অ্যাডমিনিস্ট্রেটর অ্যাক্সেস

## নমুনা পরিস্থিতি এবং ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট / নোটবুক | পরিস্থিতি | লক্ষ্য | উদাহরণ ইনপুট(গুলি) | প্রয়োজনীয় ডেটাসেট |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | অভ্যন্তরীণ IT দল একটি গোপনীয়তা মূল্যায়ন পোর্টালের জন্য অন-ডিভাইস ইনফারেন্স মূল্যায়ন করছে | প্রমাণ করুন যে লোকাল SLM স্ট্যান্ডার্ড প্রম্পটে সাব-সেকেন্ড লেটেন্সি সহ প্রতিক্রিয়া জানায় | "লোকাল ইনফারেন্সের দুটি সুবিধা তালিকাভুক্ত করুন।" | কোনও (একক প্রম্পট) |
| Quickstart মানিয়ে নেওয়া কোড ব্লক | একজন ডেভেলপার বিদ্যমান OpenAI স্ক্রিপ্টকে Foundry Local-এ স্থানান্তর করছে | ড্রপ-ইন সামঞ্জস্য দেখান | "লোকাল ইনফারেন্সের দুটি সুবিধা দিন।" | শুধুমাত্র ইনলাইন প্রম্পট |

### পরিস্থিতি বিবরণ
নিরাপত্তা এবং সম্মতি দলকে যাচাই করতে হবে যে সংবেদনশীল প্রোটোটাইপ ডেটা লোকালভাবে প্রক্রিয়া করা যেতে পারে কিনা। তারা বুটস্ট্র্যাপ স্ক্রিপ্টটি বিভিন্ন প্রম্পট (গোপনীয়তা, লেটেন্সি, খরচ) সহ চালায় একটি নির্ধারিত temperature=0 মোড ব্যবহার করে বেসলাইন আউটপুটগুলি পরবর্তী তুলনার জন্য ক্যাপচার করতে (সেশন ৩ বেঞ্চমার্কিং এবং সেশন ৪ SLM বনাম LLM কনট্রাস্ট)।

### ন্যূনতম প্রম্পট সেট JSON (ঐচ্ছিক)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

এই তালিকাটি একটি পুনরায় ব্যবহারযোগ্য মূল্যায়ন লুপ তৈরি করতে বা ভবিষ্যতের রিগ্রেশন টেস্ট হার্নেসে বীজ দিতে ব্যবহার করুন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়ী থাকব না।