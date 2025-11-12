<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T22:22:47+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "bn"
}
-->
# সেশন ৩: ফাউন্ড্রি লোকাল-এ ওপেন-সোর্স মডেল

## সারসংক্ষেপ

ফাউন্ড্রি লোকাল-এ Hugging Face এবং অন্যান্য ওপেন-সোর্স মডেল কীভাবে আনা যায় তা আবিষ্কার করুন। মডেল নির্বাচন কৌশল, কমিউনিটি কন্ট্রিবিউশন ওয়ার্কফ্লো, পারফরম্যান্স তুলনা পদ্ধতি এবং কাস্টম মডেল রেজিস্ট্রেশনের মাধ্যমে ফাউন্ড্রি সম্প্রসারণের উপায় শিখুন। এই সেশনটি সাপ্তাহিক "মডেল মানডেস" অনুসন্ধান থিমের সাথে মানানসই এবং আপনাকে ওপেন-সোর্স মডেলগুলোকে স্থানীয়ভাবে মূল্যায়ন ও পরিচালনা করতে সক্ষম করে, Azure-এ স্কেল করার আগে।

## শেখার লক্ষ্যসমূহ

শেষে আপনি সক্ষম হবেন:

- **আবিষ্কার ও মূল্যায়ন**: গুণমান বনাম রিসোর্সের ভারসাম্য ব্যবহার করে সম্ভাব্য মডেল (mistral, gemma, qwen, deepseek) চিহ্নিত করতে।
- **লোড ও চালনা**: ফাউন্ড্রি লোকাল CLI ব্যবহার করে কমিউনিটি মডেল ডাউনলোড, ক্যাশ এবং চালনা করতে।
- **বেঞ্চমার্ক**: সামঞ্জস্যপূর্ণ লেটেন্সি + টোকেন থ্রুপুট + গুণমান হিউরিস্টিক প্রয়োগ করতে।
- **সম্প্রসারণ**: SDK-সামঞ্জস্যপূর্ণ প্যাটার্ন অনুসরণ করে কাস্টম মডেল র‍্যাপার রেজিস্টার বা অ্যাডাপ্ট করতে।
- **তুলনা**: SLM বনাম মাঝারি আকারের LLM নির্বাচন সিদ্ধান্তের জন্য গঠনমূলক তুলনা তৈরি করতে।

## পূর্বশর্ত

- সেশন ১ ও ২ সম্পন্ন
- `foundry-local-sdk` ইনস্টল করা Python পরিবেশ
- একাধিক মডেল ক্যাশের জন্য অন্তত ১৫GB ফ্রি ডিস্ক

### ক্রস-প্ল্যাটফর্ম পরিবেশ দ্রুত শুরু

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS থেকে Windows হোস্ট সার্ভিসে বেঞ্চমার্কিং করার সময় সেট করুন:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ডেমো ফ্লো (৩০ মিনিট)

### ১. CLI ব্যবহার করে Hugging Face মডেল লোড (৮ মিনিট)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### ২. চালনা ও দ্রুত প্রোব (৫ মিনিট)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### ৩. বেঞ্চমার্ক স্ক্রিপ্ট (৮ মিনিট)

`samples/03-oss-models/benchmark_models.py` তৈরি করুন:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

চালান:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### ৪. পারফরম্যান্স তুলনা (৫ মিনিট)

লোড টাইম, মেমোরি ফুটপ্রিন্ট (Task Manager / `nvidia-smi` / OS রিসোর্স মনিটর পর্যবেক্ষণ করুন), আউটপুট গুণমান বনাম গতি নিয়ে আলোচনা করুন। Python বেঞ্চমার্ক স্ক্রিপ্ট (সেশন ৩) ব্যবহার করে লেটেন্সি ও থ্রুপুট পরীক্ষা করুন; GPU অ্যাক্সিলারেশন সক্রিয় করার পর পুনরায় চালান।

### ৫. স্টার্টার প্রজেক্ট (৪ মিনিট)

মডেল তুলনা রিপোর্ট জেনারেটর তৈরি করুন (বেঞ্চমার্কিং স্ক্রিপ্টের সাথে markdown এক্সপোর্ট সম্প্রসারণ করুন)।

## স্টার্টার প্রজেক্ট: `03-huggingface-models` সম্প্রসারণ

বিদ্যমান নমুনা উন্নত করুন:

1. বেঞ্চমার্ক অ্যাগ্রিগেশন + CSV/Markdown আউটপুট যোগ করুন।
2. সহজ গুণগত স্কোরিং বাস্তবায়ন করুন (প্রম্পট পেয়ার সেট + ম্যানুয়াল অ্যানোটেশন স্টাব ফাইল)।
3. JSON কনফিগ (`models.json`) পরিচিত করুন প্লাগযোগ্য মডেল তালিকা ও প্রম্পট সেটের জন্য।

## ভ্যালিডেশন চেকলিস্ট

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

সব লক্ষ্য মডেল উপস্থিত থাকা উচিত এবং প্রোব চ্যাট অনুরোধে সাড়া দেওয়া উচিত।

## নমুনা পরিস্থিতি ও ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট | পরিস্থিতি | লক্ষ্য | প্রম্পট / ডেটাসেট উৎস |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | এজ প্ল্যাটফর্ম টিম এম্বেডেড সামারাইজারের জন্য ডিফল্ট SLM নির্বাচন করছে | প্রার্থী মডেলগুলোর মধ্যে লেটেন্সি + p95 + টোকেন/সেকেন্ড তুলনা তৈরি করুন | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### পরিস্থিতি বিবরণ
প্রোডাক্ট ইঞ্জিনিয়ারিংকে অফলাইন মিটিং-নোট ফিচারের জন্য একটি ডিফল্ট লাইটওয়েট সামারাইজেশন মডেল নির্বাচন করতে হবে। তারা নির্ধারিত ডিটারমিনিস্টিক বেঞ্চমার্ক (temperature=0) চালায় একটি নির্দিষ্ট প্রম্পট সেটের উপর (নিচের উদাহরণ দেখুন) এবং GPU অ্যাক্সিলারেশন সহ ও ছাড়া লেটেন্সি + থ্রুপুট মেট্রিক সংগ্রহ করে।

### উদাহরণ প্রম্পট সেট JSON (বিস্তৃতযোগ্য)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

প্রতিটি মডেলের জন্য প্রতিটি প্রম্পট লুপ করুন, প্রতি-প্রম্পট লেটেন্সি ক্যাপচার করুন, ডিস্ট্রিবিউশন মেট্রিক নির্ধারণ করুন এবং আউটলিয়ার সনাক্ত করুন।

## মডেল নির্বাচন কাঠামো

| মাত্রা | মেট্রিক | কেন গুরুত্বপূর্ণ |
|----------|--------|----------------|
| লেটেন্সি | avg / p95 | ব্যবহারকারীর অভিজ্ঞতার সামঞ্জস্য |
| থ্রুপুট | টোকেন/সেকেন্ড | ব্যাচ ও স্ট্রিমিং স্কেলেবিলিটি |
| মেমোরি | রেসিডেন্ট সাইজ | ডিভাইস ফিট ও কনকারেন্সি |
| গুণমান | রুব্রিক প্রম্পট | টাস্ক উপযুক্ততা |
| ফুটপ্রিন্ট | ডিস্ক ক্যাশ | বিতরণ ও আপডেট |
| লাইসেন্স | ব্যবহার অনুমতি | বাণিজ্যিক সম্মতি |

## কাস্টম মডেল দিয়ে সম্প্রসারণ

উচ্চ-স্তরের প্যাটার্ন (ছদ্ম):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

অফিশিয়াল রিপোজিটরি থেকে অ্যাডাপ্টার ইন্টারফেসের বিবর্তন পরামর্শ করুন:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## সমস্যা সমাধান

| সমস্যা | কারণ | সমাধান |
|-------|-------|-----|
| OOM on mistral-7b | পর্যাপ্ত RAM/GPU নেই | অন্যান্য মডেল বন্ধ করুন; ছোট ভ্যারিয়েন্ট চেষ্টা করুন |
| প্রথম সাড়া ধীর | ঠান্ডা লোড | একটি পর্যায়ক্রমিক লাইটওয়েট প্রম্পট দিয়ে উষ্ণ রাখুন |
| ডাউনলোড স্থগিত | নেটওয়ার্ক অস্থিতিশীলতা | পুনরায় চেষ্টা করুন; অফ-পিক সময়ে প্রিফেচ করুন |

## রেফারেন্স

- ফাউন্ড্রি লোকাল SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- মডেল মানডেস: https://aka.ms/model-mondays
- Hugging Face মডেল আবিষ্কার: https://huggingface.co/models

---

**সেশন সময়কাল**: ৩০ মিনিট (+ ঐচ্ছিক গভীর অনুসন্ধান)  
**কঠিনতা**: মধ্যম

### ঐচ্ছিক উন্নয়ন

| উন্নয়ন | সুবিধা | কিভাবে |
|-------------|---------|-----|
| স্ট্রিমিং প্রথম-টোকেন লেটেন্সি | উপলব্ধি করা প্রতিক্রিয়া পরিমাপ করে | `BENCH_STREAM=1` দিয়ে বেঞ্চমার্ক চালান (`Workshop/samples/session03`-এ উন্নত স্ক্রিপ্ট) |
| ডিটারমিনিস্টিক মোড | স্থিতিশীল রিগ্রেশন তুলনা | `temperature=0`, নির্দিষ্ট প্রম্পট সেট, JSON আউটপুট সংস্করণ নিয়ন্ত্রণে ক্যাপচার করুন |
| গুণমান রুব্রিক স্কোরিং | গুণগত মাত্রা যোগ করে | `prompts.json` বজায় রাখুন প্রত্যাশিত ফ্যাসেট সহ; স্কোর (১–৫) ম্যানুয়ালি বা সেকেন্ডারি মডেলের মাধ্যমে অ্যানোটেট করুন |
| CSV / Markdown এক্সপোর্ট | শেয়ারযোগ্য রিপোর্ট | স্ক্রিপ্ট সম্প্রসারণ করে `benchmark_report.md` টেবিল ও হাইলাইট সহ লিখুন |
| মডেল সক্ষমতা ট্যাগ | পরবর্তী সময়ে স্বয়ংক্রিয় রাউটিংয়ে সাহায্য করে | `models.json` বজায় রাখুন `{alias: {capabilities:[], size_mb:..}}` সহ |
| ক্যাশ ওয়ার্মআপ ফেজ | ঠান্ডা-স্টার্ট পক্ষপাত কমায় | টাইমিং লুপের আগে একটি উষ্ণ রাউন্ড চালান (ইতিমধ্যে বাস্তবায়িত) |
| পার্সেন্টাইল সঠিকতা | শক্তিশালী টেল লেটেন্সি | numpy পার্সেন্টাইল ব্যবহার করুন (ইতিমধ্যে পুনর্গঠিত স্ক্রিপ্টে) |
| টোকেন খরচ অনুমান | অর্থনৈতিক তুলনা | আনুমানিক খরচ = (টোকেন/সেকেন্ড * প্রতি অনুরোধে গড় টোকেন) * এনার্জি হিউরিস্টিক |
| ব্যাচ রান-এ ব্যর্থ মডেল স্বয়ংক্রিয়ভাবে স্কিপ করা | স্থিতিস্থাপকতা | প্রতিটি বেঞ্চমার্ক try/except-এ মোড়ান এবং স্ট্যাটাস ফিল্ড চিহ্নিত করুন |

#### মিনিমাল Markdown এক্সপোর্ট স্নিপেট

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### ডিটারমিনিস্টিক প্রম্পট সেট উদাহরণ

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

স্ট্যাটিক তালিকা লুপ করুন র‍্যান্ডম প্রম্পটের পরিবর্তে, কমিটের মধ্যে তুলনাযোগ্য মেট্রিকের জন্য।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->