<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:07:02+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "bn"
}
-->
# সেশন ১: Foundry Local দিয়ে শুরু করা

## সারসংক্ষেপ

Windows 11-এ Foundry Local ইনস্টল এবং কনফিগার করে আপনার যাত্রা শুরু করুন। CLI সেটআপ করুন, হার্ডওয়্যার অ্যাক্সিলারেশন সক্ষম করুন এবং দ্রুত লোকাল ইনফারেন্সের জন্য মডেল ক্যাশ করুন। এই হাতে-কলমে সেশনটি Phi, Qwen, DeepSeek এবং GPT-OSS-20B মডেল চালানোর জন্য পুনরুত্পাদনযোগ্য CLI কমান্ডের মাধ্যমে নির্দেশনা দেয়।

## শেখার লক্ষ্যসমূহ

এই সেশনের শেষে আপনি:

- **ইনস্টল এবং কনফিগার করুন**: Windows 11-এ Foundry Local সেটআপ করুন এবং পারফরম্যান্স অপ্টিমাইজ করুন
- **CLI অপারেশন শিখুন**: মডেল ম্যানেজমেন্ট এবং ডিপ্লয়মেন্টের জন্য Foundry Local CLI ব্যবহার করুন
- **হার্ডওয়্যার অ্যাক্সিলারেশন সক্ষম করুন**: ONNXRuntime বা WebGPU দিয়ে GPU অ্যাক্সিলারেশন কনফিগার করুন
- **একাধিক মডেল ডিপ্লয় করুন**: phi-4, GPT-OSS-20B, Qwen এবং DeepSeek মডেল লোকালভাবে চালান
- **আপনার প্রথম অ্যাপ তৈরি করুন**: Foundry Local Python SDK ব্যবহার করে বিদ্যমান নমুনাগুলি অ্যাডাপ্ট করুন

# মডেল পরীক্ষা করুন (নন-ইন্টারঅ্যাকটিভ সিঙ্গেল প্রম্পট)
foundry model run phi-4-mini --prompt "হ্যালো, নিজেকে পরিচয় করাও"

- Windows 11 (22H2 বা পরবর্তী)
# উপলব্ধ ক্যাটালগ মডেল তালিকা করুন (লোড করা মডেলগুলি চালানোর পর প্রদর্শিত হয়)
foundry model list
## NOTE: বর্তমানে কোনো নির্দিষ্ট `--running` ফ্ল্যাগ নেই; কোনটি লোড করা আছে তা দেখতে চ্যাট শুরু করুন বা সার্ভিস লগ পরিদর্শন করুন।
- Python 3.10+ ইনস্টল করা
- Visual Studio Code Python এক্সটেনশন সহ
- ইনস্টলেশনের জন্য অ্যাডমিনিস্ট্রেটর প্রিভিলেজ

### (ঐচ্ছিক) পরিবেশ ভেরিয়েবল

`.env` তৈরি করুন (বা শেলে সেট করুন) স্ক্রিপ্টগুলোকে পোর্টেবল করার জন্য:
# প্রতিক্রিয়া তুলনা করুন (নন-ইন্টারঅ্যাকটিভ)
foundry model run gpt-oss-20b --prompt "সাধারণ ভাষায় edge AI ব্যাখ্যা করুন"
| ভেরিয়েবল | উদ্দেশ্য | উদাহরণ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | পছন্দের মডেল এলিয়াস (ক্যাটালগ সেরা ভ্যারিয়েন্ট অটো-সিলেক্ট করে) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | এন্ডপয়েন্ট ওভাররাইড করুন (অন্যথায় ম্যানেজার থেকে অটো) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | স্ট্রিমিং ডেমো সক্ষম করুন | `true` |

> যদি `FOUNDRY_LOCAL_ENDPOINT=auto` (বা আনসেট) থাকে, আমরা এটি SDK ম্যানেজার থেকে নির্ধারণ করি।

## ডেমো ফ্লো (৩০ মিনিট)

### ১. Foundry Local ইনস্টল এবং CLI সেটআপ যাচাই করুন (১০ মিনিট)

# ক্যাশ করা মডেল তালিকা করুন
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (প্রিভিউ / যদি সমর্থিত)**

যদি একটি নেটিভ macOS প্যাকেজ সরবরাহ করা হয় (সর্বশেষ অফিসিয়াল ডক চেক করুন):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

যদি macOS নেটিভ বাইনারি এখনও উপলব্ধ না থাকে, আপনি এখনও:
1. Windows 11 ARM/Intel VM (Parallels / UTM) ব্যবহার করতে পারেন এবং Windows ধাপ অনুসরণ করতে পারেন।
2. কন্টেইনারের মাধ্যমে মডেল চালাতে পারেন (যদি কন্টেইনার ইমেজ প্রকাশিত হয়) এবং `FOUNDRY_LOCAL_ENDPOINT` সেট করুন প্রকাশিত পোর্টে।

**Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন (ক্রস-প্ল্যাটফর্ম)**

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

সার্ভিস ম্যানুয়ালি শুরু এবং মডেল চালানোর পরিবর্তে, **Foundry Local Python SDK** সবকিছু বুটস্ট্র্যাপ করতে পারে:

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

যদি আপনি স্পষ্ট নিয়ন্ত্রণ পছন্দ করেন, আপনি CLI + OpenAI ক্লায়েন্ট ব্যবহার করতে পারেন যা পরে দেখানো হয়েছে।

### ২. CLI দিয়ে লোকাল মডেল চালান (১০ মিনিট)

#### ধাপ ৩.১: Phi-4 মডেল ডিপ্লয় করুন

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### ধাপ ৩.২: GPT-OSS-20B ডিপ্লয় করুন

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

### ৪. স্টার্টার প্রজেক্ট: Foundry Local-এর জন্য 01-run-phi অ্যাডাপ্ট করুন (৫ মিনিট)

#### ধাপ ৪.১: একটি বেসিক চ্যাট অ্যাপ্লিকেশন তৈরি করুন

`samples/01-foundry-quickstart/chat_quickstart.py` তৈরি করুন (যদি ম্যানেজার উপলব্ধ থাকে তাহলে আপডেট করুন):

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

## মূল ধারণাগুলি

### ১. Foundry Local আর্কিটেকচার

- **লোকাল ইনফারেন্স ইঞ্জিন**: সম্পূর্ণ মডেল আপনার ডিভাইসে চালায়
- **OpenAI SDK সামঞ্জস্যপূর্ণ**: বিদ্যমান OpenAI কোডের সাথে সহজ ইন্টিগ্রেশন
- **মডেল ম্যানেজমেন্ট**: একাধিক মডেল দক্ষতার সাথে ডাউনলোড, ক্যাশ এবং চালান
- **হার্ডওয়্যার অপ্টিমাইজেশন**: GPU, NPU এবং CPU অ্যাক্সিলারেশন ব্যবহার করুন

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

### সমস্যা ১: "Foundry কমান্ড পাওয়া যায়নি"

**সমাধান:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### সমস্যা ২: "মডেল লোড করতে ব্যর্থ হয়েছে"

**সমাধান:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### সমস্যা ৩: "localhost:5273-এ সংযোগ প্রত্যাখ্যান করা হয়েছে"

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

- **Phi-4-mini**: সাধারণ কাজের জন্য সেরা, কম মেমোরি ব্যবহার
- **Qwen2.5-0.5b**: দ্রুততম ইনফারেন্স, কম রিসোর্স প্রয়োজন
- **GPT-OSS-20B**: সর্বোচ্চ গুণমান, বেশি রিসোর্স প্রয়োজন
- **DeepSeek-Coder**: প্রোগ্রামিং কাজের জন্য অপ্টিমাইজড

### ২. হার্ডওয়্যার অপ্টিমাইজেশন

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

### ঐচ্ছিক উন্নতি

| উন্নতি | কী | কিভাবে |
|--------|----|--------|
| শেয়ারড ইউটিলিটি | ডুপ্লিকেট ক্লায়েন্ট/বুটস্ট্র্যাপ লজিক সরান | `Workshop/samples/workshop_utils.py` ব্যবহার করুন (`get_client`, `chat_once`) |
| টোকেন ব্যবহারের দৃশ্যমানতা | খরচ/দক্ষতা চিন্তা শেখান | `SHOW_USAGE=1` সেট করুন প্রম্পট/কমপ্লিশন/মোট টোকেন প্রিন্ট করতে |
| নির্ধারিত তুলনা | স্থিতিশীল বেঞ্চমার্কিং এবং রিগ্রেশন চেক | `temperature=0`, `top_p=1`, ধারাবাহিক প্রম্পট টেক্সট ব্যবহার করুন |
| প্রথম টোকেন লেটেন্সি | প্রতিক্রিয়ার উপলব্ধি মেট্রিক | স্ট্রিমিং দিয়ে বেঞ্চমার্ক স্ক্রিপ্ট অ্যাডাপ্ট করুন (`BENCH_STREAM=1`) |
| ট্রানজিয়েন্ট ত্রুটিতে পুনরায় চেষ্টা | ঠান্ডা শুরুতে স্থিতিশীল ডেমো | `RETRY_ON_FAIL=1` (ডিফল্ট) এবং `RETRY_BACKOFF` সামঞ্জস্য করুন |
| স্মোক টেস্টিং | মূল ফ্লোতে দ্রুত স্যানিটি চেক | ওয়ার্কশপের আগে `python Workshop/tests/smoke.py` চালান |
| মডেল এলিয়াস প্রোফাইল | মেশিনের মধ্যে দ্রুত মডেল সেট পরিবর্তন | `.env` বজায় রাখুন `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` সহ |
| ক্যাশিং দক্ষতা | মাল্টি-স্যাম্পল রান-এ পুনরাবৃত্তি ওয়ার্মআপ এড়ান | ইউটিলিটি ক্যাশ ম্যানেজার; স্ক্রিপ্ট/নোটবুক জুড়ে পুনরায় ব্যবহার করুন |
| প্রথম রান ওয়ার্মআপ | p95 লেটেন্সি স্পাইক কমান | `FoundryLocalManager` তৈরি করার পর একটি ছোট প্রম্পট চালান |

উদাহরণ নির্ধারিত ওয়ার্ম বেসলাইন (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

আপনি দ্বিতীয় রান-এ একই আউটপুট এবং অভিন্ন টোকেন গণনা দেখতে পাবেন, যা নির্ধারিততা নিশ্চিত করে।

## পরবর্তী পদক্ষেপ

এই সেশন সম্পন্ন করার পর:

1. **সেশন ২ অন্বেষণ করুন**: Azure AI Foundry RAG দিয়ে AI সমাধান তৈরি করুন
2. **বিভিন্ন মডেল চেষ্টা করুন**: Qwen, DeepSeek এবং অন্যান্য মডেল পরিবার নিয়ে পরীক্ষা করুন
3. **পারফরম্যান্স অপ্টিমাইজ করুন**: আপনার নির্দিষ্ট হার্ডওয়্যারের জন্য সেটিংস ফাইন-টিউন করুন
4. **কাস্টম অ্যাপ্লিকেশন তৈরি করুন**: Foundry Local SDK ব্যবহার করে আপনার নিজস্ব প্রজেক্টে কাজ করুন

## অতিরিক্ত রিসোর্স

### ডকুমেন্টেশন
- [Foundry Local Python SDK রেফারেন্স](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local ইনস্টলেশন গাইড](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [মডেল ক্যাটালগ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### নমুনা কোড
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### কমিউনিটি
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**সেশনের সময়কাল**: ৩০ মিনিট হাতে-কলমে + ১৫ মিনিট প্রশ্নোত্তর
**কঠিনতার স্তর**: প্রাথমিক
**প্রয়োজনীয় যোগ্যতা**: Windows 11, Python 3.10+, অ্যাডমিনিস্ট্রেটর অ্যাক্সেস

## নমুনা পরিস্থিতি এবং ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট / নোটবুক | পরিস্থিতি | লক্ষ্য | উদাহরণ ইনপুট(গুলি) | প্রয়োজনীয় ডেটাসেট |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | অভ্যন্তরীণ IT দল একটি গোপনীয়তা মূল্যায়ন পোর্টালের জন্য অন-ডিভাইস ইনফারেন্স মূল্যায়ন করছে | প্রমাণ করুন লোকাল SLM স্ট্যান্ডার্ড প্রম্পটে সাব-সেকেন্ড লেটেন্সিতে সাড়া দেয় | "লোকাল ইনফারেন্সের দুটি সুবিধা তালিকাভুক্ত করুন।" | কোনো ডেটাসেট নয় (সিঙ্গেল প্রম্পট) |
| Quickstart অ্যাডাপ্টেশন কোড ব্লক | ডেভেলপার একটি বিদ্যমান OpenAI স্ক্রিপ্ট Foundry Local-এ স্থানান্তর করছে | ড্রপ-ইন সামঞ্জস্যতা দেখান | "লোকাল ইনফারেন্সের দুটি সুবিধা দিন।" | শুধুমাত্র ইনলাইন প্রম্পট |

### পরিস্থিতি বিবরণ
নিরাপত্তা এবং কমপ্লায়েন্স স্কোয়াডকে যাচাই করতে হবে যে সংবেদনশীল প্রোটোটাইপ ডেটা লোকালভাবে প্রক্রিয়া করা যেতে পারে কিনা। তারা বুটস্ট্র্যাপ স্ক্রিপ্ট চালায় বিভিন্ন প্রম্পট (গোপনীয়তা, লেটেন্সি, খরচ) ব্যবহার করে নির্ধারিত `temperature=0` মোডে বেসলাইন আউটপুট ক্যাপচার করার জন্য (সেশন ৩ বেঞ্চমার্কিং এবং সেশন ৪ SLM বনাম LLM তুলনা)।

### মিনিমাল প্রম্পট সেট JSON (ঐচ্ছিক)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

এই তালিকা ব্যবহার করে একটি পুনরুত্পাদনযোগ্য মূল্যায়ন লুপ তৈরি করুন বা ভবিষ্যতের রিগ্রেশন টেস্ট হারনেসে বীজ হিসেবে ব্যবহার করুন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা আসল সংস্করণকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।