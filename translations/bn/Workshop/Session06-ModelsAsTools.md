<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T21:09:29+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "bn"
}
-->
# সেশন ৬: ফাউন্ড্রি লোকাল – টুল হিসেবে মডেল

## সারসংক্ষেপ

মডেলগুলোকে স্থানীয় AI অপারেটিং স্তরের মধ্যে সংযোজিত টুল হিসেবে বিবেচনা করুন। এই সেশনে দেখানো হয়েছে কীভাবে একাধিক বিশেষায়িত SLM/LLM কল চেইন করা যায়, কাজগুলোকে বেছে বেছে রুট করা যায় এবং অ্যাপ্লিকেশনগুলোর জন্য একটি একীভূত SDK সারফেস প্রকাশ করা যায়। আপনি একটি হালকা মডেল রাউটার + টাস্ক প্ল্যানার তৈরি করবেন, এটি একটি অ্যাপ স্ক্রিপ্টে সংযুক্ত করবেন এবং প্রোডাকশন ওয়ার্কলোডের জন্য Azure AI Foundry-তে স্কেলিং পথ নির্ধারণ করবেন।

## শেখার লক্ষ্যসমূহ

- **ধারণা করুন** মডেলগুলোকে ঘোষিত সক্ষমতাসম্পন্ন পরমাণু টুল হিসেবে
- **রুট করুন** অনুপ্রেরণা / হিউরিস্টিক স্কোরিংয়ের ভিত্তিতে অনুরোধ
- **চেইন করুন** আউটপুটগুলোকে বহু-ধাপের কাজের মধ্যে (বিভাজন → সমাধান → পরিমার্জন)
- **সংযুক্ত করুন** ডাউনস্ট্রিম অ্যাপ্লিকেশনগুলোর জন্য একীভূত ক্লায়েন্ট API
- **স্কেল করুন** ক্লাউডে ডিজাইন (একই OpenAI-সামঞ্জস্যপূর্ণ চুক্তি)

## পূর্বশর্ত

- সেশন ১–৫ সম্পন্ন
- একাধিক স্থানীয় মডেল ক্যাশ করা (যেমন, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ক্রস-প্ল্যাটফর্ম পরিবেশ স্নিপেট

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Remote/VM সার্ভিস অ্যাক্সেস macOS থেকে:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ডেমো প্রবাহ (৩০ মিনিট)

### ১. টুল সক্ষমতা ঘোষণা (৫ মিনিট)

`samples/06-tools/models_catalog.py` তৈরি করুন:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### ২. অনুপ্রেরণা সনাক্তকরণ ও রাউটিং (৮ মিনিট)

`samples/06-tools/router.py` তৈরি করুন:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### ৩. বহু-ধাপের টাস্ক চেইনিং (৭ মিনিট)

`samples/06-tools/pipeline.py` তৈরি করুন:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### ৪. স্টার্টার প্রজেক্ট: `06-models-as-tools` অভিযোজন (৫ মিনিট)

উন্নয়ন:
- স্ট্রিমিং টোকেন সাপোর্ট যোগ করুন (প্রগ্রেসিভ UI আপডেট)
- আত্মবিশ্বাস স্কোরিং যোগ করুন: লেক্সিকাল ওভারল্যাপ বা প্রম্পট রুব্রিক
- ট্রেস JSON রপ্তানি করুন (অনুপ্রেরণা → মডেল → লেটেন্সি → টোকেন ব্যবহার)
- পুনরাবৃত্তি সাবস্টেপগুলোর জন্য ক্যাশ পুনরায় ব্যবহার বাস্তবায়ন করুন

### ৫. Azure-এ স্কেলিং পথ (৫ মিনিট)

| স্তর | লোকাল (ফাউন্ড্রি) | ক্লাউড (Azure AI Foundry) | ট্রানজিশন কৌশল |
|------|-------------------|---------------------------|----------------|
| রাউটিং | হিউরিস্টিক পাইথন | টেকসই মাইক্রোসার্ভিস | API কন্টেইনারাইজ ও ডিপ্লয় করুন |
| মডেল | SLMs ক্যাশ করা | ম্যানেজড ডিপ্লয়মেন্ট | স্থানীয় নামগুলোকে ডিপ্লয়মেন্ট ID-তে ম্যাপ করুন |
| পর্যবেক্ষণযোগ্যতা | CLI স্ট্যাটস/ম্যানুয়াল | কেন্দ্রীয় লগিং ও মেট্রিক্স | গঠনমূলক ট্রেস ইভেন্ট যোগ করুন |
| নিরাপত্তা | শুধুমাত্র লোকাল হোস্ট | Azure অথ / নেটওয়ার্কিং | সিক্রেটের জন্য কী ভল্ট প্রবর্তন করুন |
| খরচ | ডিভাইস রিসোর্স | কনজাম্পশন বিলিং | বাজেট গার্ডরেল যোগ করুন |

## যাচাইকরণ চেকলিস্ট

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

অনুপ্রেরণা-ভিত্তিক মডেল নির্বাচন এবং চূড়ান্ত পরিমার্জিত আউটপুট প্রত্যাশা করুন।

## সমস্যা সমাধান

| সমস্যা | কারণ | সমাধান |
|-------|------|--------|
| সব কাজ একই মডেলে রাউট করা হচ্ছে | দুর্বল নিয়ম | INTENT_RULES regex সেট সমৃদ্ধ করুন |
| পাইপলাইন মাঝপথে ব্যর্থ | মডেল লোড করা হয়নি | `foundry model run <model>` চালান |
| আউটপুট সংহতি কম | পরিমার্জন ধাপ নেই | সারসংক্ষেপ/যাচাই পাস যোগ করুন |

## রেফারেন্স

- ফাউন্ড্রি লোকাল SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry ডকস: https://learn.microsoft.com/azure/ai-foundry
- প্রম্পট কোয়ালিটি প্যাটার্ন: সেশন ২ দেখুন

---

**সেশনের সময়কাল**: ৩০ মিনিট  
**কঠিনতা**: বিশেষজ্ঞ

## নমুনা পরিস্থিতি ও ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট / নোটবুক | পরিস্থিতি | লক্ষ্য | ডেটাসেট / ক্যাটালগ উৎস |
|-----------------------------|-----------|--------|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | মিশ্র অনুপ্রেরণা প্রম্পট পরিচালনা করার জন্য ডেভেলপার সহকারী (রিফ্যাক্টর, সারসংক্ষেপ, শ্রেণীবদ্ধকরণ) | হিউরিস্টিক অনুপ্রেরণা → মডেল এলিয়াস রাউটিং টোকেন ব্যবহারের সাথে | ইনলাইন `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | জটিল কোডিং সহায়তা কাজের জন্য বহু-ধাপের পরিকল্পনা ও পরিমার্জন | বিভাজন → বিশেষায়িত কার্যকরী → সারসংক্ষেপ পরিমার্জন ধাপ | একই `CATALOG`; ধাপগুলো পরিকল্পনা আউটপুট থেকে প্রাপ্ত |

### পরিস্থিতি বর্ণনা
একটি ইঞ্জিনিয়ারিং উৎপাদনশীলতা টুল বিভিন্ন ধরনের কাজ গ্রহণ করে: কোড রিফ্যাক্টর করা, স্থাপত্য নোট সারসংক্ষেপ করা, প্রতিক্রিয়া শ্রেণীবদ্ধ করা। লেটেন্সি ও রিসোর্স ব্যবহারের পরিমাণ কমানোর জন্য, একটি ছোট সাধারণ মডেল পরিকল্পনা ও সারসংক্ষেপ করে, একটি কোড-স্পেশালাইজড মডেল রিফ্যাক্টরিং পরিচালনা করে এবং একটি হালকা শ্রেণীবদ্ধকরণ-সক্ষম মডেল প্রতিক্রিয়া লেবেল করে। পাইপলাইন স্ক্রিপ্ট চেইনিং + পরিমার্জন প্রদর্শন করে; রাউটার স্ক্রিপ্ট অভিযোজিত একক-প্রম্পট রাউটিংকে আলাদা করে।

### ক্যাটালগ স্ন্যাপশট
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### উদাহরণ টেস্ট প্রম্পট
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### ট্রেস এক্সটেনশন (ঐচ্ছিক)
`models_pipeline.py` এর জন্য প্রতি-ধাপের ট্রেস JSON লাইন যোগ করুন:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### এসকেলেশন হিউরিস্টিক (আইডিয়া)
যদি পরিকল্পনায় "অপ্টিমাইজ", "নিরাপত্তা" এর মতো কীওয়ার্ড থাকে, অথবা ধাপের দৈর্ঘ্য > ২৮০ অক্ষর হয় → সেই ধাপের জন্য বড় মডেলে (যেমন, `gpt-oss-20b`) এসকেলেট করুন।

### ঐচ্ছিক উন্নয়ন

| ক্ষেত্র | উন্নয়ন | মান | ইঙ্গিত |
|-------|---------|-----|-------|
| ক্যাশিং | ম্যানেজার + ক্লায়েন্ট অবজেক্ট পুনরায় ব্যবহার করুন | কম লেটেন্সি, কম ওভারহেড | `workshop_utils.get_client` ব্যবহার করুন |
| ব্যবহারের মেট্রিক্স | টোকেন ও প্রতি-ধাপের লেটেন্সি ক্যাপচার করুন | প্রোফাইলিং ও অপ্টিমাইজেশন | প্রতিটি রাউটেড কল টাইম করুন; ট্রেস তালিকায় সংরক্ষণ করুন |
| অভিযোজিত রাউটিং | আত্মবিশ্বাস / খরচ সচেতন | ভালো মান-খরচ ভারসাম্য | স্কোরিং যোগ করুন: যদি প্রম্পট > N অক্ষর বা regex ডোমেইন মেলে → বড় মডেলে এসকেলেট করুন |
| গতিশীল সক্ষমতা রেজিস্ট্রি | ক্যাটালগ হট রিলোড করুন | পুনরায় চালু বা পুনরায় ডিপ্লয় ছাড়া | রানটাইমে `catalog.json` লোড করুন; ফাইল টাইমস্ট্যাম্প দেখুন |
| ব্যাকআপ কৌশল | ব্যর্থতার ক্ষেত্রে দৃঢ়তা | বেশি প্রাপ্যতা | প্রাথমিক চেষ্টা করুন → ব্যতিক্রম হলে ব্যাকআপ এলিয়াস |
| স্ট্রিমিং পাইপলাইন | প্রাথমিক প্রতিক্রিয়া | UX উন্নয়ন | প্রতিটি ধাপ স্ট্রিম করুন এবং চূড়ান্ত পরিমার্জন ইনপুট বাফার করুন |
| ভেক্টর অনুপ্রেরণা এম্বেডিং | আরও সূক্ষ্ম রাউটিং | বেশি অনুপ্রেরণা নির্ভুলতা | প্রম্পট এম্বেড করুন, ক্লাস্টার করুন এবং সেন্ট্রয়েড ম্যাপ → সক্ষমতা |
| ট্রেস রপ্তানি | অডিটেবল চেইন | সম্মতি/রিপোর্টিং | JSON লাইন প্রকাশ করুন: ধাপ, অনুপ্রেরণা, মডেল, latency_ms, টোকেন |
| খরচ সিমুলেশন | প্রি-ক্লাউড অনুমান | বাজেট পরিকল্পনা | প্রতি মডেলের জন্য টোকেন প্রতি ধারণাগত খরচ বরাদ্দ করুন এবং প্রতি কাজের জন্য যোগ করুন |
| নির্ধারিত মোড | পুনরুত্পাদনযোগ্যতা | স্থিতিশীল বেঞ্চমার্কিং | Env: `temperature=0`, নির্দিষ্ট ধাপের সংখ্যা |

#### ট্রেস স্ট্রাকচার উদাহরণ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### অভিযোজিত এসকেলেশন স্কেচ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### মডেল ক্যাটালগ হট রিলোড

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।