<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T22:20:29+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "bn"
}
-->
# পরিবেশ কনফিগারেশন গাইড

## সংক্ষিপ্ত বিবরণ

ওয়ার্কশপের নমুনাগুলি কনফিগারেশনের জন্য পরিবেশ ভেরিয়েবল ব্যবহার করে, যা `.env` ফাইলের মাধ্যমে রিপোজিটরির মূল অংশে কেন্দ্রীভূত। এটি কোড পরিবর্তন না করেই সহজে কাস্টমাইজেশন করতে দেয়।

## দ্রুত শুরু

### ১. প্রয়োজনীয়তা যাচাই করুন

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### ২. পরিবেশ কনফিগার করুন

`.env` ফাইলটি ইতিমধ্যে যুক্তিসঙ্গত ডিফল্ট সেটিংস সহ কনফিগার করা আছে। বেশিরভাগ ব্যবহারকারীর কিছু পরিবর্তন করার প্রয়োজন হবে না।

**ঐচ্ছিক**: সেটিংস পর্যালোচনা এবং কাস্টমাইজ করুন:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### ৩. কনফিগারেশন প্রয়োগ করুন

**পাইথন স্ক্রিপ্টের জন্য:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**নোটবুকের জন্য:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## পরিবেশ ভেরিয়েবল রেফারেন্স

### মূল কনফিগারেশন

| ভেরিয়েবল | ডিফল্ট | বিবরণ |
|-----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | নমুনার জন্য ডিফল্ট মডেল |
| `FOUNDRY_LOCAL_ENDPOINT` | (ফাঁকা) | সার্ভিস এন্ডপয়েন্ট ওভাররাইড |
| `PYTHONPATH` | ওয়ার্কশপ পাথ | পাইথন মডিউল অনুসন্ধান পাথ |

**যখন FOUNDRY_LOCAL_ENDPOINT সেট করবেন:**
- রিমোট ফাউন্ড্রি লোকাল ইনস্ট্যান্স
- কাস্টম পোর্ট কনফিগারেশন
- ডেভেলপমেন্ট/প্রোডাকশন পৃথকীকরণ

**উদাহরণ:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### সেশন-নির্দিষ্ট ভেরিয়েবল

#### সেশন ০২: RAG পাইপলাইন
| ভেরিয়েবল | ডিফল্ট | উদ্দেশ্য |
|-----------|--------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | এমবেডিং মডেল |
| `RAG_QUESTION` | প্রি-কনফিগারড | টেস্ট প্রশ্ন |

#### সেশন ০৩: বেঞ্চমার্কিং
| ভেরিয়েবল | ডিফল্ট | উদ্দেশ্য |
|-----------|--------|----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | বেঞ্চমার্ক করার মডেল |
| `BENCH_ROUNDS` | `3` | প্রতি মডেলের জন্য পুনরাবৃত্তি |
| `BENCH_PROMPT` | প্রি-কনফিগারড | টেস্ট প্রম্পট |
| `BENCH_STREAM` | `0` | প্রথম টোকেন লেটেন্সি পরিমাপ |

#### সেশন ০৪: মডেল তুলনা
| ভেরিয়েবল | ডিফল্ট | উদ্দেশ্য |
|-----------|--------|----------|
| `SLM_ALIAS` | `phi-4-mini` | ছোট ভাষা মডেল |
| `LLM_ALIAS` | `qwen2.5-7b` | বড় ভাষা মডেল |
| `COMPARE_PROMPT` | প্রি-কনফিগারড | তুলনা প্রম্পট |
| `COMPARE_RETRIES` | `2` | পুনরায় চেষ্টা |

#### সেশন ০৫: মাল্টি-এজেন্ট অর্কেস্ট্রেশন
| ভেরিয়েবল | ডিফল্ট | উদ্দেশ্য |
|-----------|--------|----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | গবেষক এজেন্ট মডেল |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | সম্পাদক এজেন্ট মডেল |
| `AGENT_QUESTION` | প্রি-কনফিগারড | টেস্ট প্রশ্ন |

### নির্ভরযোগ্যতা কনফিগারেশন

| ভেরিয়েবল | ডিফল্ট | উদ্দেশ্য |
|-----------|--------|----------|
| `SHOW_USAGE` | `1` | টোকেন ব্যবহার প্রিন্ট করুন |
| `RETRY_ON_FAIL` | `1` | পুনরায় চেষ্টা লজিক সক্রিয় করুন |
| `RETRY_BACKOFF` | `1.0` | পুনরায় চেষ্টা বিলম্ব (সেকেন্ড) |

## সাধারণ কনফিগারেশন

### ডেভেলপমেন্ট সেটআপ (দ্রুত পুনরাবৃত্তি)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### প্রোডাকশন সেটআপ (গুণমানের উপর ফোকাস)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### বেঞ্চমার্কিং সেটআপ
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### মাল্টি-এজেন্ট বিশেষীকরণ
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### রিমোট ডেভেলপমেন্ট
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## সুপারিশকৃত মডেল

### ব্যবহার ক্ষেত্রে অনুযায়ী

**সাধারণ উদ্দেশ্য:**
- `phi-4-mini` - গুণমান এবং গতি সমন্বিত

**দ্রুত প্রতিক্রিয়া:**
- `qwen2.5-0.5b` - খুব দ্রুত, শ্রেণীবিভাজনের জন্য ভালো
- `phi-4-mini` - দ্রুত এবং ভালো গুণমান

**উচ্চ গুণমান:**
- `qwen2.5-7b` - সেরা গুণমান, বেশি রিসোর্স ব্যবহার
- `phi-4-mini` - ভালো গুণমান, কম রিসোর্স

**কোড জেনারেশন:**
- `deepseek-coder-1.3b` - কোডের জন্য বিশেষায়িত
- `phi-4-mini` - সাধারণ উদ্দেশ্য কোডিং

### রিসোর্স উপলব্ধতার ভিত্তিতে

**কম রিসোর্স (< ৮GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**মাঝারি রিসোর্স (৮-১৬GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**উচ্চ রিসোর্স (১৬GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## উন্নত কনফিগারেশন

### কাস্টম এন্ডপয়েন্ট

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### টেম্পারেচার এবং স্যাম্পলিং (কোডে ওভাররাইড করুন)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI হাইব্রিড সেটআপ

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## সমস্যা সমাধান

### পরিবেশ ভেরিয়েবল লোড হয়নি

**লক্ষণ:**
- স্ক্রিপ্ট ভুল মডেল ব্যবহার করে
- সংযোগ ত্রুটি
- ভেরিয়েবল স্বীকৃত নয়

**সমাধান:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### সার্ভিস সংযোগ সমস্যা

**লক্ষণ:**
- "Connection refused" ত্রুটি
- "Service not available"
- টাইমআউট ত্রুটি

**সমাধান:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### মডেল পাওয়া যায়নি

**লক্ষণ:**
- "Model not found" ত্রুটি
- "Alias not recognized"

**সমাধান:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ইমপোর্ট ত্রুটি

**লক্ষণ:**
- "Module not found" ত্রুটি

**সমাধান:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## কনফিগারেশন পরীক্ষা

### পরিবেশ লোডিং যাচাই করুন

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### ফাউন্ড্রি লোকাল সংযোগ পরীক্ষা করুন

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## নিরাপত্তা সেরা অনুশীলন

### ১. কখনোই সিক্রেট কমিট করবেন না

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### ২. আলাদা .env ফাইল ব্যবহার করুন

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### ৩. API কী ঘুরিয়ে নিন

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### ৪. পরিবেশ-নির্দিষ্ট কনফিগারেশন ব্যবহার করুন

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK ডকুমেন্টেশন

- **মূল রিপোজিটরি**: https://github.com/microsoft/Foundry-Local
- **পাইথন SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ডকুমেন্টেশন**: সর্বশেষ তথ্যের জন্য SDK রিপোজিটরি দেখুন

## অতিরিক্ত সম্পদ

- `QUICK_START.md` - শুরু করার গাইড
- `Workshop/samples/*/README.md` - নমুনা-নির্দিষ্ট গাইড

---

**শেষ আপডেট**: ২০২৫-০১-০৮  
**সংস্করণ**: ২.০  
**SDK**: ফাউন্ড্রি লোকাল পাইথন SDK (সর্বশেষ)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->