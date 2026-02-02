# အစည်းအဝေး ၆: Foundry Local – မော်ဒယ်များကို ကိရိယာများအဖြစ် အသုံးပြုခြင်း

## အကျဉ်းချုပ်

မော်ဒယ်များကို ဒေသခံ AI လုပ်ဆောင်မှုအလွှာအတွင်းတွင် ပေါင်းစပ်နိုင်သော ကိရိယာများအဖြစ် သတ်မှတ်ပါ။ ဒီအစည်းအဝေးမှာ အထူးပြု SLM/LLM ခေါ်ဆိုမှုများကို ချိတ်ဆက်ခြင်း၊ တာဝန်များကို ရွေးချယ်၍ လမ်းကြောင်းသတ်မှတ်ခြင်း၊ အက်ပလီကေးရှင်းများအတွက် SDK မျက်နှာပြင်ကို ပေါင်းစပ်ဖော်ထုတ်ခြင်း စသည်တို့ကို ပြသပါမည်။ သင်သည် အလွယ်တကူ မော်ဒယ်လမ်းကြောင်း + တာဝန်အစီအစဉ်ရေးဆွဲသူတစ်ခုကို တည်ဆောက်ပြီး၊ အက်ပလီကေးရှင်း script အတွင်းတွင် ပေါင်းစပ်ပြီး Azure AI Foundry သို့ ပရိုဒတ်ရှင်းလုပ်ငန်းများအတွက် အရွယ်အစားချဲ့ထွင်ခြင်းလမ်းကြောင်းကို အကြမ်းဖျင်းဖော်ပြပါမည်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

- **အယူအဆဖော်ဆောင်ခြင်း** မော်ဒယ်များကို အစိတ်အပိုင်းအဖြစ် သတ်မှတ်နိုင်သော ကိရိယာများအဖြစ်
- **လမ်းကြောင်းသတ်မှတ်ခြင်း** ရည်ရွယ်ချက် / ဟေဋ္ဌာန်အဆင့်သတ်မှတ်မှုအပေါ် အခြေခံ၍ တောင်းဆိုမှုများ
- **ချိတ်ဆက်ခြင်း** အဆင့်များစွာသော တာဝန်များအတွက် အထွေထွေထွက်ကုန်များ (ခွဲခြား → ဖြေရှင်း → ပြုပြင်)
- **ပေါင်းစပ်ခြင်း** အောက်ခြေရှိ အက်ပလီကေးရှင်းများအတွက် client API တစ်ခုတည်း
- **အရွယ်အစားချဲ့ထွင်ခြင်း** Cloud သို့ ဒီဇိုင်း (OpenAI-compatible contract တူညီမှု)

## ကြိုတင်လိုအပ်ချက်များ

- အစည်းအဝေး ၁–၅ ပြီးစီးထား
- ဒေသခံမော်ဒယ်များစွာကို cache လုပ်ထား (ဥပမာ `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Cross-Platform Environment Snippet

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

Remote/VM service access from macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (၃၀ မိနစ်)

### ၁. ကိရိယာစွမ်းရည်ကြေညာချက် (၅ မိနစ်)

`samples/06-tools/models_catalog.py` ဖန်တီးပါ:

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


### ၂. ရည်ရွယ်ချက်ရှာဖွေခြင်းနှင့် လမ်းကြောင်းသတ်မှတ်ခြင်း (၈ မိနစ်)

`samples/06-tools/router.py` ဖန်တီးပါ:

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


### ၃. အဆင့်များစွာသော တာဝန်ချိတ်ဆက်ခြင်း (၇ မိနစ်)

`samples/06-tools/pipeline.py` ဖန်တီးပါ:

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


### ၄. Starter Project: `06-models-as-tools` ကို အဆင့်မြှင့်တင်ခြင်း (၅ မိနစ်)

တိုးတက်မှုများ:
- Streaming token ပံ့ပိုးမှု ထည့်သွင်းပါ (UI အဆင့်ဆင့် update)
- ယုံကြည်မှုအဆင့်သတ်မှတ်ခြင်း ထည့်သွင်းပါ: lexical overlap သို့မဟုတ် prompt rubric
- trace JSON ကို export လုပ်ပါ (intent → model → latency → token usage)
- ထပ်တလဲလဲ substeps များအတွက် cache ကို အသုံးပြုမှု ပြုလုပ်ပါ

### ၅. Azure သို့ အရွယ်အစားချဲ့ထွင်ခြင်းလမ်းကြောင်း (၅ မိနစ်)

| အလွှာ | ဒေသခံ (Foundry) | Cloud (Azure AI Foundry) | အပြောင်းအလဲ မဟာဗျူဟာ |
|-------|-----------------|--------------------------|---------------------|
| Routing | Heuristic Python | Durable microservice | Containerize & deploy API |
| Models | SLMs cached | Managed deployments | Map local names to deployment IDs |
| Observability | CLI stats/manual | Central logging & metrics | Add structured trace events |
| Security | Local host only | Azure auth / networking | Introduce key vault for secrets |
| Cost | Device resource | Consumption billing | Add budget guardrails |

## Validation Checklist

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

ရည်ရွယ်ချက်အပေါ် မော်ဒယ်ရွေးချယ်မှုနှင့် နောက်ဆုံး ပြုပြင်ထားသော ထွက်ကုန်ကို မျှော်လင့်ပါ။

## Troubleshooting

| ပြဿနာ | အကြောင်းရင်း | ဖြေရှင်းနည်း |
|---------|-------|-----|
| တာဝန်အားလုံးကို တစ်မော်ဒယ်တည်းသို့ လမ်းကြောင်းသတ်မှတ် | အချက်အလက်အနည်းငယ် | INTENT_RULES regex set ကို တိုးချဲ့ပါ |
| Pipeline အလယ်အဆင့်တွင် မအောင်မြင် | မော်ဒယ်မတင်ထား | `foundry model run <model>` ကို run လုပ်ပါ |
| ထွက်ကုန်အညီအမျှနည်း | ပြုပြင်ခြင်းအဆင့်မရှိ | စုစည်းခြင်း/အတည်ပြုခြင်းအဆင့် ထည့်ပါ |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Quality Patterns: See Session 2

---

**အစည်းအဝေးကြာမြင့်ချိန်**: ၃၀ မိနစ်  
**အဆင့်**: ကျွမ်းကျင်

## နမူနာအခြေအနေ & အလုပ်ရုံဆွေးနွေးမှု Mapping

| Workshop Scripts / Notebooks | အခြေအနေ | ရည်ရွယ်ချက် | Dataset / Catalog Source |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Developer assistant အမျိုးမျိုးသော ရည်ရွယ်ချက် prompt များကို ကိုင်တွယ်ခြင်း (refactor, summarize, classify) | Heuristic intent → model alias routing with token usage | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | အဆင့်များစွာသော အစီအစဉ်ရေးဆွဲခြင်းနှင့် ပြုပြင်ခြင်း coding assistance task အတွက် | Decompose → specialized execution → summarization refine step | အတူတူသော `CATALOG`; steps derived from plan output |

### အခြေအနေအကြောင်းအရာ
Engineering productivity tool တစ်ခုသည် အမျိုးမျိုးသော တာဝန်များကို လက်ခံရရှိသည်: ကုဒ်ပြုပြင်ခြင်း၊ အဆောက်အအုံမှတ်စုများကို အကျဉ်းချုပ်ခြင်း၊ အကြံပြုချက်များကို အမျိုးအစားခွဲခြင်း။ latency နှင့် အရင်းအမြစ်အသုံးပြုမှုကို လျှော့ချရန်၊ အထွေထွေမော်ဒယ်ငယ်တစ်ခုသည် အစီအစဉ်ရေးဆွဲခြင်းနှင့် အကျဉ်းချုပ်ခြင်းကို လုပ်ဆောင်ပြီး၊ ကုဒ်အထူးပြုမော်ဒယ်သည် ပြုပြင်ခြင်းကို လုပ်ဆောင်ပြီး၊ classification စွမ်းရည်ရှိသော မော်ဒယ်ငယ်တစ်ခုသည် အကြံပြုချက်များကို label လုပ်သည်။ pipeline script သည် ချိတ်ဆက်ခြင်း + ပြုပြင်ခြင်းကို ပြသပြီး၊ router script သည် adaptive single‑prompt routing ကို ခွဲခြားပြသသည်။

### Catalog Snapshot
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### နမူနာ စမ်းသပ် Prompt များ
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace Extension (Optional)
`models_pipeline.py` အတွက် အဆင့်တစ်ခုချင်းစီ trace JSON lines ထည့်ပါ:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Escalation Heuristic (Idea)
အစီအစဉ်တွင် "optimize", "security" စသည့် keyword များပါဝင်ပါက သို့မဟုတ် အဆင့်အရှည် > 280 characters ဖြစ်ပါက → အကြီးမော်ဒယ် (ဥပမာ `gpt-oss-20b`) သို့ escalation လုပ်ပါ။

### Optional Enhancements

| အပိုင်း | အဆင့်မြှင့်တင်မှု | အကျိုးကျေးဇူး | အကြံပြုချက် |
|------|-------------|-------|------|
| Caching | Reuse manager + client objects | latency လျှော့ချခြင်း၊ အလွယ်တကူ | `workshop_utils.get_client` ကို အသုံးပြုပါ |
| Usage Metrics | tokens & per-step latency ကို ဖမ်းယူပါ | Profiling & optimization | Routed call တစ်ခုချင်းစီကို အချိန်တွက်ပါ; trace list တွင် သိမ်းဆည်းပါ |
| Adaptive Routing | ယုံကြည်မှု / ကုန်ကျစရိတ်ကို သိရှိခြင်း | အရည်အသွေး-ကုန်ကျစရိတ် trade-off ကောင်းမွန်ခြင်း | Scoring ထည့်ပါ: prompt > N characters သို့မဟုတ် regex domain ကို တွေ့ပါက → မော်ဒယ်ကြီးသို့ escalation |
| Dynamic Capability Registry | catalog ကို hot reload လုပ်ပါ | restart redeploy မလိုအပ် | runtime တွင် `catalog.json` ကို load လုပ်ပါ; file timestamp ကို စောင့်ကြည့်ပါ |
| Fallback Strategy | Failures အောက်တွင် တည်ငြိမ်မှု | availability မြင့်မားခြင်း | Primary → exception ဖြစ်ပါက fallback alias |
| Streaming Pipeline | အစောပိုင်း feedback | UX တိုးတက်မှု | အဆင့်တစ်ခုချင်းစီ stream လုပ်ပြီး နောက်ဆုံး refine input ကို buffer လုပ်ပါ |
| Vector Intent Embeddings | Routing ပိုမိုသေချာမှု | ရည်ရွယ်ချက်တိကျမှု မြင့်မားခြင်း | Prompt ကို embed လုပ်ပြီး cluster & map centroid → capability |
| Trace Export | Auditable chain | Compliance/reporting | JSON lines ထုတ်ပေးပါ: step, intent, model, latency_ms, tokens |
| Cost Simulation | Pre-cloud estimation | Budget planning | မော်ဒယ်တစ်ခုချင်းစီအတွက် notional cost/token သတ်မှတ်ပြီး တာဝန်တစ်ခုချင်းစီအတွက် စုစုပေါင်း |
| Deterministic Mode | Repro reproducibility | Stable benchmarking | Env: `temperature=0`, fixed steps count |

#### Trace Structure နမူနာ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptive Escalation Sketch

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Model Catalog Hot Reload

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

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။