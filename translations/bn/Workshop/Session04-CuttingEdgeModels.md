# সেশন ৪: আধুনিক মডেলগুলি অন্বেষণ করুন – LLMs, SLMs এবং অন-ডিভাইস ইনফারেন্স

## সারসংক্ষেপ

স্থানীয় বনাম ক্লাউড ইনফারেন্স পরিস্থিতির জন্য বড় ভাষার মডেল (LLMs) এবং ছোট ভাষার মডেল (SLMs) তুলনা করুন। ONNX Runtime অ্যাক্সিলারেশন, WebGPU এক্সিকিউশন এবং হাইব্রিড RAG অভিজ্ঞতা ব্যবহার করে ডিপ্লয়মেন্ট প্যাটার্ন শিখুন। একটি চেইনলিট RAG ডেমো অন্তর্ভুক্ত রয়েছে যেখানে একটি স্থানীয় মডেল এবং একটি ঐচ্ছিক OpenWebUI অন্বেষণ রয়েছে। আপনি একটি WebGPU ইনফারেন্স স্টার্টার অ্যাডাপ্ট করবেন এবং Phi বনাম GPT-OSS-20B এর সক্ষমতা এবং খরচ/পারফরম্যান্স ট্রেড-অফ মূল্যায়ন করবেন।

## শেখার লক্ষ্যসমূহ

- **তুলনা করুন** SLM বনাম LLM লেটেন্সি, মেমরি, এবং গুণমানের দিক থেকে
- **মডেল ডিপ্লয় করুন** ONNXRuntime এবং (যেখানে সমর্থিত) WebGPU ব্যবহার করে
- **ব্রাউজার-ভিত্তিক ইনফারেন্স চালান** (গোপনীয়তা-সংরক্ষণকারী ইন্টারেক্টিভ ডেমো)
- **একীভূত করুন** একটি চেইনলিট RAG পাইপলাইন একটি স্থানীয় SLM ব্যাকএন্ডের সাথে
- **মূল্যায়ন করুন** হালকা গুণমান + খরচ হিউরিস্টিক ব্যবহার করে

## পূর্বশর্ত

- সেশন ১–৩ সম্পন্ন
- `chainlit` ইনস্টল করা (ইতিমধ্যে Module08 এর `requirements.txt` এ অন্তর্ভুক্ত)
- WebGPU-সক্ষম ব্রাউজার (Windows 11-এ Edge / Chrome এর সর্বশেষ সংস্করণ)
- Foundry Local চালু (`foundry service status`)

### ক্রস-প্ল্যাটফর্ম নোট

Windows প্রধান লক্ষ্য পরিবেশ হিসেবে রয়ে গেছে। macOS ডেভেলপারদের জন্য যারা নেটিভ বাইনারি অপেক্ষা করছেন:
1. Windows 11 VM (Parallels / UTM) অথবা একটি রিমোট Windows ওয়ার্কস্টেশনে Foundry Local চালান।
2. সার্ভিসটি প্রকাশ করুন (ডিফল্ট পোর্ট 5273) এবং macOS-এ সেট করুন:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. পূর্ববর্তী সেশনগুলির মতো একই Python ভার্চুয়াল পরিবেশের ধাপগুলি ব্যবহার করুন।

Chainlit ইনস্টল (উভয় প্ল্যাটফর্মে):
```bash
pip install chainlit
```

## ডেমো প্রবাহ (৩০ মিনিট)

### ১. Phi (SLM) বনাম GPT-OSS-20B (LLM) তুলনা করুন (৬ মিনিট)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

ট্র্যাক করুন: প্রতিক্রিয়ার গভীরতা, তথ্যগত সঠিকতা, শৈলীর সমৃদ্ধি, লেটেন্সি।

GPU সক্রিয় করার পরে থ্রুপুট পরিবর্তনগুলি পর্যবেক্ষণ করুন বনাম শুধুমাত্র CPU।

### ৩. ব্রাউজারে WebGPU ইনফারেন্স (৬ মিনিট)

স্টার্টার `04-webgpu-inference` অ্যাডাপ্ট করুন (তৈরি করুন `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

ফাইলটি ব্রাউজারে খুলুন; কম লেটেন্সি স্থানীয় রাউন্ডট্রিপ পর্যবেক্ষণ করুন।

### ৪. চেইনলিট RAG চ্যাট অ্যাপ (৭ মিনিট)

ন্যূনতম `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

চালান:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### ৫. স্টার্টার প্রজেক্ট: `04-webgpu-inference` অ্যাডাপ্ট করুন (৬ মিনিট)

ডেলিভারেবল:
- প্লেসহোল্ডার ফেচ লজিকটি স্ট্রিমিং টোকেন দিয়ে প্রতিস্থাপন করুন (একবার `stream=True` এন্ডপয়েন্ট ভ্যারিয়েন্ট সক্রিয় হলে ব্যবহার করুন)
- লেটেন্সি চার্ট যোগ করুন (ক্লায়েন্ট-সাইড) phi বনাম gpt-oss-20b টগলগুলির জন্য
- RAG কনটেক্সট ইনলাইন এম্বেড করুন (রেফারেন্স ডকুমেন্টের জন্য টেক্সট এরিয়া)

## মূল্যায়ন হিউরিস্টিক

| বিভাগ | Phi-4-mini | GPT-OSS-20B | পর্যবেক্ষণ |
|-------|-----------|-------------|-------------|
| লেটেন্সি (ঠান্ডা) | দ্রুত | ধীর | SLM দ্রুত উষ্ণ হয় |
| মেমরি | কম | বেশি | ডিভাইসের সম্ভাব্যতা |
| কনটেক্সট আনুগত্য | ভালো | শক্তিশালী | বড় মডেলটি আরও বিস্তারিত হতে পারে |
| খরচ (স্থানীয়) | ন্যূনতম | বেশি (রিসোর্স) | শক্তি/সময় ট্রেড-অফ |
| সেরা ব্যবহার ক্ষেত্র | এজ অ্যাপস | গভীর যুক্তি | হাইব্রিড পাইপলাইন সম্ভব |

## পরিবেশ যাচাই

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## সমস্যা সমাধান

| লক্ষণ | কারণ | পদক্ষেপ |
|-------|------|---------|
| ওয়েব পেজ ফেচ ব্যর্থ | CORS বা সার্ভিস ডাউন | এন্ডপয়েন্ট যাচাই করতে `curl` ব্যবহার করুন; প্রয়োজনে CORS প্রক্সি সক্রিয় করুন |
| চেইনলিট ফাঁকা | পরিবেশ সক্রিয় নয় | venv সক্রিয় করুন এবং ডিপস পুনরায় ইনস্টল করুন |
| উচ্চ লেটেন্সি | মডেলটি সদ্য লোড হয়েছে | ছোট প্রম্পট সিকোয়েন্স দিয়ে উষ্ণ করুন |

## রেফারেন্স

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG মূল্যায়ন (Ragas): https://docs.ragas.io

---

**সেশন সময়কাল**: ৩০ মিনিট  
**কঠিনতা**: উন্নত

## নমুনা পরিস্থিতি এবং কর্মশালা ম্যাপিং

| কর্মশালা সামগ্রী | পরিস্থিতি | লক্ষ্য | ডেটা / প্রম্পট উৎস |
|------------------|-----------|--------|--------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | নির্বাহী সারসংক্ষেপ জেনারেটরের জন্য SLM বনাম LLM মূল্যায়নকারী আর্কিটেকচার দল | লেটেন্সি + টোকেন ব্যবহারের পার্থক্য পরিমাপ করুন | একক `COMPARE_PROMPT` পরিবেশ ভেরিয়েবল |
| `chainlit_app.py` (RAG ডেমো) | অভ্যন্তরীণ জ্ঞান সহকারী প্রোটোটাইপ | সংক্ষিপ্ত উত্তরগুলি ন্যূনতম লেক্সিকাল রিট্রিভাল দিয়ে ভিত্তি করুন | ফাইলের মধ্যে ইনলাইন `DOCS` তালিকা |
| `webgpu_demo.html` | ভবিষ্যত অন-ডিভাইস ব্রাউজার ইনফারেন্স প্রিভিউ | কম লেটেন্সি স্থানীয় রাউন্ডট্রিপ + UX বর্ণনা দেখান | শুধুমাত্র লাইভ ব্যবহারকারীর প্রম্পট |

### পরিস্থিতি বর্ণনা
প্রোডাক্ট অর্গানাইজেশন একটি নির্বাহী ব্রিফিং জেনারেটর চায়। একটি হালকা SLM (phi‑4‑mini) সারসংক্ষেপ তৈরি করে; একটি বড় LLM (gpt‑oss‑20b) শুধুমাত্র উচ্চ-প্রাধান্য রিপোর্টগুলি পরিমার্জন করতে পারে। সেশন স্ক্রিপ্টগুলি হাইব্রিড ডিজাইনকে ন্যায্যতা দেওয়ার জন্য অভিজ্ঞ লেটেন্সি এবং টোকেন মেট্রিকগুলি ক্যাপচার করে, যখন চেইনলিট ডেমোটি দেখায় কিভাবে ভিত্তিক রিট্রিভাল ছোট মডেলের উত্তরগুলি তথ্যগত রাখে। WebGPU ধারণা পৃষ্ঠাটি ব্রাউজার অ্যাক্সিলারেশন পরিপক্ক হলে সম্পূর্ণ ক্লায়েন্ট-সাইড প্রসেসিংয়ের জন্য একটি ভিশন পথ প্রদান করে।

### ন্যূনতম RAG কনটেক্সট (চেইনলিট)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### হাইব্রিড ড্রাফট→রিফাইন প্রবাহ (ছদ্ম)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

উভয় লেটেন্সি উপাদান ট্র্যাক করুন মিশ্রিত গড় খরচ রিপোর্ট করতে।

### ঐচ্ছিক উন্নতি

| ফোকাস | উন্নতি | কেন | বাস্তবায়ন ইঙ্গিত |
|-------|--------|-----|------------------|
| তুলনামূলক মেট্রিক | টোকেন ব্যবহার + প্রথম-টোকেন লেটেন্সি ট্র্যাক করুন | সামগ্রিক পারফরম্যান্স দৃশ্য | উন্নত বেঞ্চমার্ক স্ক্রিপ্ট ব্যবহার করুন (সেশন ৩) `BENCH_STREAM=1` সহ |
| হাইব্রিড পাইপলাইন | SLM ড্রাফট → LLM রিফাইন | লেটেন্সি এবং খরচ কমান | phi-4-mini দিয়ে তৈরি করুন, gpt-oss-20b দিয়ে সারসংক্ষেপ পরিমার্জন করুন |
| স্ট্রিমিং UI | চেইনলিটে ভালো UX | ধাপে ধাপে প্রতিক্রিয়া | একবার স্থানীয় স্ট্রিমিং প্রকাশিত হলে `stream=True` ব্যবহার করুন; অংশগুলি জমা করুন |
| WebGPU ক্যাশিং | দ্রুত JS ইনিট | পুনরায় কম্পাইল ওভারহেড কমান | সংকলিত শেডার আর্টিফ্যাক্টগুলি ক্যাশ করুন (ভবিষ্যত রানটাইম সক্ষমতা) |
| নির্ধারিত QA সেট | ন্যায্য মডেল তুলনা | বৈচিত্র্য সরান | নির্দিষ্ট প্রম্পট তালিকা + মূল্যায়ন রানগুলির জন্য `temperature=0` |
| আউটপুট স্কোরিং | গঠনমূলক গুণমান লেন্স | গল্পের বাইরে যান | সহজ রুব্রিক: সংহতি / তথ্যগততা / সংক্ষিপ্ততা (১–৫) |
| শক্তি / রিসোর্স নোট | শ্রেণীকক্ষ আলোচনা | ট্রেড-অফ দেখান | OS মনিটর ব্যবহার করুন (টাস্ক ম্যানেজার, `nvidia-smi`) + বেঞ্চমার্ক স্ক্রিপ্ট আউটপুট |
| খরচ এমুলেশন | প্রি-ক্লাউড ন্যায্যতা | স্কেলিং পরিকল্পনা | টোকেনগুলিকে হাইপোথেটিকাল ক্লাউড প্রাইসিংয়ে ম্যাপ করুন TCO বর্ণনার জন্য |
| লেটেন্সি ডিকম্পোজিশন | বোতলনেক চিহ্নিত করুন | অপ্টিমাইজেশন লক্ষ্য করুন | প্রম্পট প্রস্তুতি, অনুরোধ পাঠানো, প্রথম টোকেন, সম্পূর্ণ সম্পন্ন পরিমাপ করুন |
| RAG + LLM ফলব্যাক | গুণমান নিরাপত্তা নেট | কঠিন প্রশ্ন উন্নত করুন | যদি SLM উত্তর দৈর্ঘ্য < থ্রেশহোল্ড বা কম আত্মবিশ্বাস → উন্নত করুন |

#### উদাহরণ হাইব্রিড ড্রাফট/রিফাইন প্যাটার্ন

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### লেটেন্সি ব্রেকডাউন স্কেচ

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

ন্যায্য তুলনার জন্য মডেলগুলির মধ্যে ধারাবাহিক পরিমাপ কাঠামো ব্যবহার করুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->