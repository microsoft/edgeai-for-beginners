<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T00:44:50+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "my"
}
-->
# အစည်းအဝေး ၃: Foundry Local တွင် Open-Source မော်ဒယ်များ

## အကျဉ်းချုပ်

Hugging Face နှင့် အခြားသော Open-Source မော်ဒယ်များကို Foundry Local တွင် အသုံးပြုနည်းကို ရှာဖွေပါ။ မော်ဒယ်ရွေးချယ်မှုနည်းလမ်းများ၊ အသိုင်းအဝိုင်းထည့်သွင်းမှုလုပ်ငန်းစဉ်များ၊ စွမ်းဆောင်ရည်နှိုင်းယှဉ်မှုနည်းလမ်းများနှင့် Foundry ကို မော်ဒယ်မှတ်ပုံတင်မှုအထူးပြုလုပ်နည်းများကို လေ့လာပါ။ ဒီအစည်းအဝေးသည် "Model Mondays" အပတ်စဉ်လေ့လာမှုအကြောင်းအရာများနှင့် ဆက်စပ်ပြီး Open-Source မော်ဒယ်များကို Azure သို့ အဆင့်မြှင့်မတင်မီ ဒေသတွင်းတွင် အကဲဖြတ်ခြင်းနှင့် လုပ်ဆောင်ခြင်းများကို သင်တတ်မြောက်စေပါမည်။

## သင်ယူရမည့်ရည်ရွယ်ချက်များ

အစည်းအဝေးအဆုံးတွင် သင်တတ်မြောက်မည့်အရာများမှာ -

- **ရှာဖွေခြင်းနှင့် အကဲဖြတ်ခြင်း**: အရည်အသွေးနှင့် အရင်းအမြစ်အစားအစာများကို အသုံးပြု၍ မော်ဒယ်များ (mistral, gemma, qwen, deepseek) ရွေးချယ်နိုင်ခြင်း။
- **တင်သွင်းခြင်းနှင့် အလုပ်လုပ်ခြင်း**: Foundry Local CLI ကို အသုံးပြု၍ အသိုင်းအဝိုင်းမော်ဒယ်များကို ဒေါင်းလုဒ်လုပ်ခြင်း၊ cache ထည့်ခြင်းနှင့် စတင်ခြင်း။
- **စမ်းသပ်ခြင်း**: latency + token throughput + quality heuristics များကို တစ်စည်းတစ်လုံးအတိုင်းအတာဖြင့် အသုံးပြုခြင်း။
- **တိုးချဲ့ခြင်း**: SDK-compatible ပုံစံများကို လိုက်နာ၍ မော်ဒယ် wrapper ကို မှတ်ပုံတင်ခြင်း သို့မဟုတ် အထူးပြုလုပ်ခြင်း။
- **နှိုင်းယှဉ်ခြင်း**: SLM နှင့် အလယ်အလတ် LLM မော်ဒယ်ရွေးချယ်မှုဆုံးဖြတ်ချက်များအတွက် ဖွဲ့စည်းထားသော နှိုင်းယှဉ်မှုများကို ထုတ်လုပ်ခြင်း။

## ကြိုတင်လိုအပ်ချက်များ

- အစည်းအဝေး ၁ နှင့် ၂ ကို ပြီးစီးထားရမည်
- `foundry-local-sdk` ထည့်သွင်းထားသော Python ပတ်ဝန်းကျင်
- မော်ဒယ် cache များအတွက် အနည်းဆုံး 15GB အခမဲ့ disk

### Cross-Platform Environment အမြန်စတင်ခြင်း

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

macOS မှ Windows host service ကို benchmark လုပ်မည်ဆိုပါက:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo Flow (30 မိနစ်)

### 1. Hugging Face မော်ဒယ်များကို CLI မှတစ်ဆင့် Load လုပ်ခြင်း (8 မိနစ်)

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

### 2. အလုပ်လုပ်ခြင်းနှင့် အမြန်စမ်းသပ်ခြင်း (5 မိနစ်)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Benchmark Script (8 မိနစ်)

`samples/03-oss-models/benchmark_models.py` ဖိုင်ကို ဖန်တီးပါ:

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

Run:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. စွမ်းဆောင်ရည်နှိုင်းယှဉ်ခြင်း (5 မိနစ်)

အစားအစာများကို ဆွေးနွေးပါ: load အချိန်၊ memory footprint (Task Manager / `nvidia-smi` / OS resource monitor တွင် ကြည့်ရှုပါ), အရည်အသွေးနှင့် အမြန်နှုန်း။ latency & throughput အတွက် Python benchmark script (Session 3) ကို အသုံးပြုပါ; GPU acceleration ကို ဖွင့်ပြီးနောက် ထပ်မံလုပ်ဆောင်ပါ။

### 5. Starter Project (4 မိနစ်)

benchmarking script ကို markdown export ဖြင့် တိုးချဲ့ပြီး မော်ဒယ်နှိုင်းယှဉ်မှုအစီရင်ခံစာ generator ကို ဖန်တီးပါ။

## Starter Project: `03-huggingface-models` ကို တိုးချဲ့ခြင်း

ရရှိထားသော sample ကို တိုးချဲ့ရန် -

1. benchmark aggregation + CSV/Markdown output ထည့်သွင်းပါ။
2. ရိုးရှင်းသော အရည်အသွေးအဆင့်သတ်မှတ်ခြင်း (prompt pair set + manual annotation stub file) ကို အကောင်အထည်ဖော်ပါ။
3. pluggable model list & prompt set အတွက် JSON config (`models.json`) ကို ထည့်သွင်းပါ။

## Validation Checklist

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

မော်ဒယ်များအားလုံးသည် ပေါ်လာပြီး probe chat request ကို တုံ့ပြန်ရမည်။

## Sample Scenario & Workshop Mapping

| Workshop Script | Scenario | ရည်ရွယ်ချက် | Prompt / Dataset Source |
|-----------------|----------|--------------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform team သည် embedded summarizer အတွက် default SLM ကို ရွေးချယ်ခြင်း | latency + p95 + tokens/sec နှိုင်းယှဉ်မှုကို မော်ဒယ်များအကြား ထုတ်လုပ်ခြင်း | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### Scenario Narrative
Product engineering သည် offline meeting-notes feature အတွက် default lightweight summarization မော်ဒယ်ကို ရွေးချယ်ရမည်။ သူတို့သည် fixed prompt set (အောက်တွင် ဥပမာကို ကြည့်ပါ) ကို အသုံးပြု၍ deterministic benchmarks (temperature=0) ကို ထိန်းချုပ်ပြီး latency + throughput metrics ကို GPU acceleration ရှိ/မရှိဖြင့် စမ်းသပ်ကြသည်။

### Example Prompt Set JSON (တိုးချဲ့နိုင်သည်)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

မော်ဒယ်တစ်ခုစီအတွက် prompt တစ်ခုစီကို loop လုပ်ပြီး per-prompt latency ကို ဖမ်းယူကာ distribution metrics ကို ရယူပြီး outliers များကို ရှာဖွေပါ။

## Model Selection Framework

| Dimension | Metric | အရေးကြီးသောအကြောင်းအရာ |
|----------|--------|---------------------------|
| Latency | avg / p95 | အသုံးပြုသူအတွေ့အကြုံအဆင်ပြေမှု |
| Throughput | tokens/sec | Batch & streaming scalability |
| Memory | resident size | Device fit & concurrency |
| Quality | rubric prompts | Task အတွက် သင့်လျော်မှု |
| Footprint | disk cache | Distribution & updates |
| License | use allowance | Commercial compliance |

## Custom Model ဖြင့် တိုးချဲ့ခြင်း

High-level pattern (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Adapter interfaces များအတွက် တိုးတက်မှုများကို အတည်ပြုရန် အတည်ပြုထားသော repo ကို ကြည့်ပါ:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Troubleshooting

| ပြဿနာ | အကြောင်းအရင်း | ဖြေရှင်းနည်း |
|-------|---------------|-------------|
| mistral-7b တွင် OOM | RAM/GPU မလုံလောက်ခြင်း | အခြားမော်ဒယ်များကို ရပ်ပါ; သေးငယ်သော variant ကို စမ်းပါ |
| ပထမဆုံးတုံ့ပြန်မှုနှေးခြင်း | Cold load | အလေးမရှိသော prompt ကို အကြိမ်ကြိမ်လုပ်ဆောင်ခြင်းဖြင့် အပူထိန်းထားပါ |
| Download ရပ်တန့်ခြင်း | Network မတည်ငြိမ်မှု | ထပ်မံကြိုးစားပါ; off-peak အချိန်တွင် prefetch လုပ်ပါ |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**အစည်းအဝေးကြာချိန်**: 30 မိနစ် (+ အပိုအနက်ရှင်းခြင်း)  
**အဆင့်အတန်း**: အလယ်အလတ်

### Optional Enhancements

| Enhancement | အကျိုးကျေးဇူး | လုပ်နည်း |
|-------------|---------------|----------|
| Streaming First-Token Latency | တုံ့ပြန်မှုကို တိုင်းတာခြင်း | `BENCH_STREAM=1` ဖြင့် benchmark ကို run လုပ်ပါ (`Workshop/samples/session03` တွင် တိုးချဲ့ထားသော script) |
| Deterministic Mode | Regression နှိုင်းယှဉ်မှုများကို တည်ငြိမ်စေခြင်း | `temperature=0`, fixed prompt set, version control အောက်တွင် JSON outputs ကို ဖမ်းယူပါ |
| Quality Rubric Scoring | အရည်အသွေးအတိုင်းအတာ ထည့်သွင်းခြင်း | `prompts.json` ကို ထိန်းသိမ်းပြီး မျှော်မှန်းထားသော facets များနှင့်အတူ; score များ (1–5) ကို လက်ဖြင့် သို့မဟုတ် ဒုတိယမော်ဒယ်ဖြင့် annotate လုပ်ပါ |
| CSV / Markdown Export | အစီရင်ခံစာမျှဝေခြင်း | `benchmark_report.md` ကို table & highlights ဖြင့် ရေးရန် script ကို တိုးချဲ့ပါ |
| Model Capability Tags | နောက်ပိုင်း automated routing အတွက် အထောက်အကူပြုခြင်း | `{alias: {capabilities:[], size_mb:..}}` ဖြင့် `models.json` ကို ထိန်းသိမ်းပါ |
| Cache Warmup Phase | Cold-start bias ကို လျှော့ချခြင်း | timing loop မတိုင်မီ warm round တစ်ခုကို run လုပ်ပါ (ပြီးသား script တွင် အကောင်အထည်ဖော်ထားပြီး) |
| Percentile Accuracy | Robust tail latency | numpy percentile ကို အသုံးပြုပါ (refactored script တွင် ရှိပြီးသား) |
| Token Cost Approximation | စီးပွားရေးနှိုင်းယှဉ်မှု | Approx cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | batch runs တွင် ချို့ယွင်းမှုများကို ရှောင်ရှားခြင်း | try/except ဖြင့် benchmark တစ်ခုစီကို wrap လုပ်ပြီး status field ကို မှတ်ပါ |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Deterministic Prompt Set Example

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

static list ကို loop လုပ်ပြီး commits များအကြား metrics များကို နှိုင်းယှဉ်နိုင်ရန် random prompts များအစား အသုံးပြုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->