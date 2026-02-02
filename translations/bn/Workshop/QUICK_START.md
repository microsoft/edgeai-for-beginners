# ওয়ার্কশপ দ্রুত শুরু করার গাইড

## প্রয়োজনীয়তা

### ১. Foundry Local ইনস্টল করুন

অফিশিয়াল ইনস্টলেশন গাইড অনুসরণ করুন:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### ২. Python ডিপেনডেন্সি ইনস্টল করুন

Workshop ডিরেক্টরি থেকে:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## ওয়ার্কশপ স্যাম্পল চালানো

### সেশন ০১: বেসিক চ্যাট

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**এনভায়রনমেন্ট ভেরিয়েবল:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### সেশন ০২: RAG পাইপলাইন

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**এনভায়রনমেন্ট ভেরিয়েবল:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### সেশন ০২: RAG ইভালুয়েশন (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**নোট**: `requirements.txt` এর মাধ্যমে অতিরিক্ত ডিপেনডেন্সি ইনস্টল প্রয়োজন

### সেশন ০৩: বেঞ্চমার্কিং

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**এনভায়রনমেন্ট ভেরিয়েবল:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**আউটপুট**: লেটেন্সি, থ্রুপুট এবং ফার্স্ট-টোকেন মেট্রিক্স সহ JSON

### সেশন ০৪: মডেল তুলনা

```bash
cd Workshop/samples
python -m session04.model_compare
```

**এনভায়রনমেন্ট ভেরিয়েবল:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### সেশন ০৫: মাল্টি-এজেন্ট অর্কেস্ট্রেশন

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**এনভায়রনমেন্ট ভেরিয়েবল:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### সেশন ০৬: মডেল রাউটার

```bash
cd Workshop/samples
python -m session06.models_router
```

**রাউটিং লজিক পরীক্ষা করে** বিভিন্ন ইন্টেন্ট (কোড, সারাংশ, শ্রেণীবিভাগ)

### সেশন ০৬: পাইপলাইন

```bash
python -m session06.models_pipeline
```

**জটিল মাল্টি-স্টেপ পাইপলাইন** পরিকল্পনা, কার্যকর এবং পরিমার্জন সহ

## স্ক্রিপ্ট

### বেঞ্চমার্ক রিপোর্ট এক্সপোর্ট করুন

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**আউটপুট**: Markdown টেবিল + JSON মেট্রিক্স

### Markdown CLI প্যাটার্ন লিন্ট করুন

```bash
python lint_markdown_cli.py --verbose
```

**উদ্দেশ্য**: ডকুমেন্টেশনে পুরনো CLI প্যাটার্ন সনাক্ত করা

## টেস্টিং

### স্মোক টেস্ট

```bash
cd Workshop
python -m tests.smoke
```

**টেস্ট**: মূল স্যাম্পলের বেসিক কার্যকারিতা

## সমস্যা সমাধান

### সার্ভিস চালু নয়

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### মডিউল ইমপোর্ট ত্রুটি

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### সংযোগ ত্রুটি

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### মডেল পাওয়া যায়নি

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## এনভায়রনমেন্ট ভেরিয়েবল রেফারেন্স

### কোর কনফিগারেশন
| ভেরিয়েবল | ডিফল্ট | বিবরণ |
|-----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | বিভিন্ন | ব্যবহৃত মডেল এলিয়াস |
| `FOUNDRY_LOCAL_ENDPOINT` | অটো | সার্ভিস এন্ডপয়েন্ট ওভাররাইড |
| `SHOW_USAGE` | `0` | টোকেন ব্যবহারের পরিসংখ্যান দেখান |
| `RETRY_ON_FAIL` | `1` | পুনরায় চেষ্টা করার লজিক সক্রিয় করুন |
| `RETRY_BACKOFF` | `1.0` | প্রাথমিক পুনরায় চেষ্টা বিলম্ব (সেকেন্ড) |

### সেশন-নির্দিষ্ট
| ভেরিয়েবল | ডিফল্ট | বিবরণ |
|-----------|--------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | এমবেডিং মডেল |
| `RAG_QUESTION` | স্যাম্পল দেখুন | RAG টেস্ট প্রশ্ন |
| `BENCH_MODELS` | বিভিন্ন | কমা-সেপারেটেড মডেল |
| `BENCH_ROUNDS` | `3` | বেঞ্চমার্ক ইটারেশন |
| `BENCH_PROMPT` | স্যাম্পল দেখুন | বেঞ্চমার্ক প্রম্পট |
| `BENCH_STREAM` | `0` | ফার্স্ট-টোকেন লেটেন্সি পরিমাপ |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | প্রাইমারি এজেন্ট মডেল |
| `AGENT_MODEL_EDITOR` | প্রাইমারি | এডিটর এজেন্ট মডেল |
| `SLM_ALIAS` | `phi-4-mini` | ছোট ভাষা মডেল |
| `LLM_ALIAS` | `qwen2.5-7b` | বড় ভাষা মডেল |
| `COMPARE_PROMPT` | স্যাম্পল দেখুন | তুলনা প্রম্পট |

## সুপারিশকৃত মডেল

### ডেভেলপমেন্ট ও টেস্টিং
- **phi-4-mini** - গুণমান এবং গতি ব্যালেন্সড
- **qwen2.5-0.5b** - শ্রেণীবিভাগের জন্য খুব দ্রুত
- **gemma-2-2b** - ভালো গুণমান, মাঝারি গতি

### প্রোডাকশন পরিস্থিতি
- **phi-4-mini** - সাধারণ উদ্দেশ্য
- **deepseek-coder-1.3b** - কোড জেনারেশন
- **qwen2.5-7b** - উচ্চ গুণমানের উত্তর

## SDK ডকুমেন্টেশন

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## সাহায্য পাওয়া

1. সার্ভিস স্ট্যাটাস চেক করুন: `foundry service status`
2. লগ দেখুন: Foundry Local সার্ভিস লগ চেক করুন
3. SDK ডকস চেক করুন: https://github.com/microsoft/Foundry-Local
4. স্যাম্পল কোড রিভিউ করুন: সব স্যাম্পলে বিস্তারিত ডকস্ট্রিং রয়েছে

## পরবর্তী পদক্ষেপ

1. সমস্ত ওয়ার্কশপ সেশন ক্রমানুসারে সম্পন্ন করুন
2. বিভিন্ন মডেলের সাথে পরীক্ষা করুন
3. আপনার ব্যবহারের জন্য স্যাম্পল পরিবর্তন করুন

---

**শেষ আপডেট**: ২০২৫-০১-০৮  
**ওয়ার্কশপ সংস্করণ**: সর্বশেষ  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->