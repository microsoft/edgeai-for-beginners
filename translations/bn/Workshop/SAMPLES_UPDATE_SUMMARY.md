<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:09:58+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "bn"
}
-->
# ওয়ার্কশপ নমুনা - ফাউন্ড্রি লোকাল SDK আপডেট সারাংশ

## সংক্ষিপ্ত বিবরণ

`Workshop/samples` ডিরেক্টরির সমস্ত পাইথন নমুনা ফাউন্ড্রি লোকাল SDK-এর সেরা অনুশীলন অনুসরণ করতে এবং ওয়ার্কশপ জুড়ে সামঞ্জস্য নিশ্চিত করতে আপডেট করা হয়েছে।

**তারিখ**: ৮ অক্টোবর, ২০২৫  
**পরিধি**: ৬টি ওয়ার্কশপ সেশনের মধ্যে ৯টি পাইথন ফাইল  
**প্রধান লক্ষ্য**: ত্রুটি পরিচালনা, ডকুমেন্টেশন, SDK প্যাটার্ন, ব্যবহারকারীর অভিজ্ঞতা

---

## আপডেট করা ফাইলসমূহ

### সেশন ০১: শুরু করা
- ✅ `chat_bootstrap.py` - বেসিক চ্যাট এবং স্ট্রিমিং উদাহরণ

### সেশন ০২: RAG সমাধান
- ✅ `rag_pipeline.py` - এম্বেডিং সহ RAG বাস্তবায়ন
- ✅ `rag_eval_ragas.py` - RAGAS মেট্রিক্স সহ RAG মূল্যায়ন

### সেশন ০৩: ওপেন সোর্স মডেল
- ✅ `benchmark_oss_models.py` - মাল্টি-মডেল বেঞ্চমার্কিং

### সেশন ০৪: আধুনিক মডেল
- ✅ `model_compare.py` - SLM বনাম LLM তুলনা

### সেশন ০৫: AI-চালিত এজেন্ট
- ✅ `agents_orchestrator.py` - মাল্টি-এজেন্ট সমন্বয়

### সেশন ০৬: টুল হিসেবে মডেল
- ✅ `models_router.py` - ইন্টেন্ট-ভিত্তিক মডেল রাউটিং
- ✅ `models_pipeline.py` - মাল্টি-স্টেপ রাউটেড পাইপলাইন

### সহায়ক অবকাঠামো
- ✅ `workshop_utils.py` - ইতিমধ্যেই সেরা অনুশীলন অনুসরণ করছে (কোন পরিবর্তন প্রয়োজন নেই)

---

## প্রধান উন্নতি

### ১. উন্নত ত্রুটি পরিচালনা

**আগে:**
```python
manager, client, model_id = get_client(alias)
```

**পরে:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**সুবিধা:**
- স্পষ্ট ত্রুটি বার্তাসহ সুন্দর ত্রুটি পরিচালনা
- কার্যকরী সমস্যা সমাধানের নির্দেশনা
- স্ক্রিপ্টিংয়ের জন্য সঠিক প্রস্থান কোড

### ২. উন্নত ইমপোর্ট ব্যবস্থাপনা

**আগে:**
```python
from sentence_transformers import SentenceTransformer
```

**পরে:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**সুবিধা:**
- নির্ভরতা অনুপস্থিত থাকলে স্পষ্ট নির্দেশনা
- অস্পষ্ট ইমপোর্ট ত্রুটি প্রতিরোধ
- ব্যবহারকারী-বান্ধব ইনস্টলেশন নির্দেশনা

### ৩. ব্যাপক ডকুমেন্টেশন

**সমস্ত নমুনায় যোগ করা হয়েছে:**
- ডকস্ট্রিং-এ পরিবেশ ভেরিয়েবল ডকুমেন্টেশন
- SDK রেফারেন্স লিঙ্ক
- ব্যবহার উদাহরণ
- বিস্তারিত ফাংশন/প্যারামিটার ডকুমেন্টেশন
- ভালো IDE সাপোর্টের জন্য টাইপ হিন্ট

**উদাহরণ:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### ৪. উন্নত ব্যবহারকারী প্রতিক্রিয়া

**তথ্যপূর্ণ লগিং যোগ করা হয়েছে:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**প্রগতি সূচক:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**গঠনমূলক আউটপুট:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### ৫. শক্তিশালী বেঞ্চমার্কিং

**সেশন ০৩ উন্নতি:**
- প্রতি-মডেল ত্রুটি পরিচালনা (ব্যর্থতার পরেও চলতে থাকে)
- বিস্তারিত প্রগতি রিপোর্টিং
- সঠিকভাবে ওয়ার্মআপ রাউন্ড সম্পন্ন
- প্রথম-টোকেন লেটেন্সি পরিমাপের সমর্থন
- ধাপগুলির স্পষ্ট বিভাজন

### ৬. সামঞ্জস্যপূর্ণ টাইপ হিন্ট

**সর্বত্র যোগ করা হয়েছে:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**সুবিধা:**
- ভালো IDE অটোকমপ্লিট
- প্রাথমিক ত্রুটি সনাক্তকরণ
- স্বয়ং-ডকুমেন্টিং কোড

### ৭. উন্নত মডেল রাউটার

**সেশন ০৬ উন্নতি:**
- ব্যাপক ইন্টেন্ট সনাক্তকরণ ডকুমেন্টেশন
- মডেল নির্বাচন অ্যালগরিদম ব্যাখ্যা
- বিস্তারিত রাউটিং লগ
- টেস্ট আউটপুট ফরম্যাটিং
- ব্যাচ টেস্টিংয়ে ত্রুটি পুনরুদ্ধার

### ৮. মাল্টি-এজেন্ট অর্কেস্ট্রেশন

**সেশন ০৫ উন্নতি:**
- ধাপে ধাপে প্রগতি রিপোর্টিং
- প্রতি-এজেন্ট ত্রুটি পরিচালনা
- স্পষ্ট পাইপলাইন গঠন
- ভালো মেমরি ব্যবস্থাপনা ডকুমেন্টেশন

---

## টেস্টিং চেকলিস্ট

### পূর্বশর্ত
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### প্রতিটি নমুনা পরীক্ষা করুন

#### সেশন ০১
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### সেশন ০২
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### সেশন ০৩
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### সেশন ০৪
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### সেশন ০৫
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### সেশন ০৬
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## পরিবেশ ভেরিয়েবল রেফারেন্স

### গ্লোবাল (সমস্ত নমুনা)
| ভেরিয়েবল | বিবরণ | ডিফল্ট |
|-----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | ব্যবহৃত মডেলের নাম | নমুনা অনুযায়ী পরিবর্তনশীল |
| `FOUNDRY_LOCAL_ENDPOINT` | সার্ভিস এন্ডপয়েন্ট ওভাররাইড করুন | স্বয়ংক্রিয়ভাবে সনাক্ত |
| `SHOW_USAGE` | টোকেন ব্যবহারের প্রদর্শন | `0` |
| `RETRY_ON_FAIL` | পুনরায় চেষ্টা করার লজিক সক্রিয় করুন | `1` |
| `RETRY_BACKOFF` | প্রাথমিক পুনরায় চেষ্টা বিলম্ব | `1.0` |

### নমুনা-নির্দিষ্ট
| ভেরিয়েবল | ব্যবহৃত দ্বারা | বিবরণ |
|-----------|---------------|--------|
| `EMBED_MODEL` | সেশন ০২ | এম্বেডিং মডেলের নাম |
| `RAG_QUESTION` | সেশন ০২ | RAG-এর জন্য টেস্ট প্রশ্ন |
| `BENCH_MODELS` | সেশন ০৩ | বেঞ্চমার্ক করার জন্য কমা-আলাদা মডেল |
| `BENCH_ROUNDS` | সেশন ০৩ | বেঞ্চমার্ক রাউন্ডের সংখ্যা |
| `BENCH_PROMPT` | সেশন ০৩ | বেঞ্চমার্কের জন্য টেস্ট প্রম্পট |
| `BENCH_STREAM` | সেশন ০৩ | প্রথম-টোকেন লেটেন্সি পরিমাপ |
| `SLM_ALIAS` | সেশন ০৪ | ছোট ভাষা মডেল |
| `LLM_ALIAS` | সেশন ০৪ | বড় ভাষা মডেল |
| `COMPARE_PROMPT` | সেশন ০৪ | তুলনা টেস্ট প্রম্পট |
| `AGENT_MODEL_PRIMARY` | সেশন ০৫ | প্রাথমিক এজেন্ট মডেল |
| `AGENT_MODEL_EDITOR` | সেশন ০৫ | এডিটর এজেন্ট মডেল |
| `AGENT_QUESTION` | সেশন ০৫ | এজেন্টের জন্য টেস্ট প্রশ্ন |
| `PIPELINE_TASK` | সেশন ০৬ | পাইপলাইনের জন্য টাস্ক |

---

## ব্রেকিং পরিবর্তন

**কোনো পরিবর্তন নেই** - সমস্ত পরিবর্তন ব্যাকওয়ার্ড কম্প্যাটিবল।

বিদ্যমান স্ক্রিপ্টগুলি কাজ চালিয়ে যাবে। নতুন বৈশিষ্ট্যগুলি:
- ঐচ্ছিক পরিবেশ ভেরিয়েবল
- উন্নত ত্রুটি বার্তা (কার্যকারিতা ভাঙে না)
- অতিরিক্ত লগিং (দমন করা যেতে পারে)
- ভালো টাইপ হিন্ট (কোনও রানটাইম প্রভাব নেই)

---

## সেরা অনুশীলন বাস্তবায়ন

### ১. সর্বদা Workshop Utils ব্যবহার করুন
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### ২. সঠিক ত্রুটি পরিচালনার প্যাটার্ন
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ৩. তথ্যপূর্ণ লগিং
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### ৪. টাইপ হিন্ট
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### ৫. ব্যাপক ডকস্ট্রিং
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### ৬. পরিবেশ ভেরিয়েবল সমর্থন
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### ৭. সুন্দর অবনতি
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## সাধারণ সমস্যা ও সমাধান

### সমস্যা: ইমপোর্ট ত্রুটি
**সমাধান:** অনুপস্থিত নির্ভরতা ইনস্টল করুন
```bash
pip install sentence-transformers ragas datasets numpy
```

### সমস্যা: সংযোগ ত্রুটি
**সমাধান:** নিশ্চিত করুন যে ফাউন্ড্রি লোকাল চালু আছে
```bash
foundry service status
foundry model run phi-4-mini
```

### সমস্যা: মডেল পাওয়া যায়নি
**সমাধান:** উপলব্ধ মডেলগুলি পরীক্ষা করুন
```bash
foundry model ls
foundry model download <alias>
```

### সমস্যা: ধীর কর্মক্ষমতা
**সমাধান:** ছোট মডেল ব্যবহার করুন বা প্যারামিটার সামঞ্জস্য করুন
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## পরবর্তী পদক্ষেপ

### ১. সমস্ত নমুনা পরীক্ষা করুন
উপরে দেওয়া টেস্টিং চেকলিস্ট অনুসরণ করে সমস্ত নমুনা সঠিকভাবে কাজ করছে কিনা যাচাই করুন।

### ২. ডকুমেন্টেশন আপডেট করুন
- নতুন উদাহরণ সহ সেশন মার্কডাউন ফাইল আপডেট করুন
- প্রধান README-তে সমস্যা সমাধানের বিভাগ যোগ করুন
- দ্রুত রেফারেন্স গাইড তৈরি করুন

### ৩. ইন্টিগ্রেশন টেস্ট তৈরি করুন
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### ৪. কর্মক্ষমতা বেঞ্চমার্ক যোগ করুন
ত্রুটি পরিচালনার উন্নতির মাধ্যমে কর্মক্ষমতা উন্নতি ট্র্যাক করুন।

### ৫. ব্যবহারকারীর প্রতিক্রিয়া
ওয়ার্কশপ অংশগ্রহণকারীদের কাছ থেকে সংগ্রহ করুন:
- ত্রুটি বার্তার স্পষ্টতা
- ডকুমেন্টেশনের সম্পূর্ণতা
- ব্যবহার সহজতা

---

## রিসোর্স

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **দ্রুত রেফারেন্স**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **মাইগ্রেশন নোটস**: `Workshop/SDK_MIGRATION_NOTES.md`
- **প্রধান রিপোজিটরি**: https://github.com/microsoft/Foundry-Local

---

## রক্ষণাবেক্ষণ

### নতুন নমুনা যোগ করা
নতুন নমুনা তৈরি করার সময় এই প্যাটার্নগুলি অনুসরণ করুন:

1. ক্লায়েন্ট ব্যবস্থাপনার জন্য `workshop_utils` ব্যবহার করুন
2. ব্যাপক ত্রুটি পরিচালনা যোগ করুন
3. পরিবেশ ভেরিয়েবল সমর্থন অন্তর্ভুক্ত করুন
4. টাইপ হিন্ট এবং ডকস্ট্রিং যোগ করুন
5. তথ্যপূর্ণ লগিং প্রদান করুন
6. ডকস্ট্রিং-এ ব্যবহার উদাহরণ অন্তর্ভুক্ত করুন
7. SDK ডকুমেন্টেশনের লিঙ্ক দিন

### আপডেট পর্যালোচনা
নমুনা আপডেট পর্যালোচনা করার সময় পরীক্ষা করুন:
- [ ] সমস্ত I/O অপারেশনে ত্রুটি পরিচালনা
- [ ] পাবলিক ফাংশনে টাইপ হিন্ট
- [ ] ব্যাপক ডকস্ট্রিং
- [ ] পরিবেশ ভেরিয়েবল ডকুমেন্টেশন
- [ ] তথ্যপূর্ণ ব্যবহারকারী প্রতিক্রিয়া
- [ ] SDK রেফারেন্স লিঙ্ক
- [ ] সামঞ্জস্যপূর্ণ কোড স্টাইল

---

**সারাংশ**: সমস্ত ওয়ার্কশপ পাইথন নমুনা এখন ফাউন্ড্রি লোকাল SDK-এর সেরা অনুশীলন অনুসরণ করে, উন্নত ত্রুটি পরিচালনা, ব্যাপক ডকুমেন্টেশন এবং উন্নত ব্যবহারকারীর অভিজ্ঞতা সহ। কোনো ব্রেকিং পরিবর্তন নেই - সমস্ত বিদ্যমান কার্যকারিতা সংরক্ষিত এবং উন্নত করা হয়েছে।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।