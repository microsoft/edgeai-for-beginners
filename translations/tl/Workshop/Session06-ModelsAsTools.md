<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T22:47:15+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "tl"
}
-->
# Session 6: Foundry Local – Mga Modelo bilang Kasangkapan

## Abstrak

Tratuhin ang mga modelo bilang mga kasangkapan na maaaring pagsamahin sa isang lokal na AI operating layer. Sa sesyong ito, ipapakita kung paano pagsamahin ang maraming espesyal na tawag sa SLM/LLM, piliing i-route ang mga gawain, at magbigay ng isang pinagsamang SDK surface para sa mga aplikasyon. Magtatayo ka ng magaan na model router + task planner, isasama ito sa isang app script, at ilalapat ang scaling path sa Azure AI Foundry para sa mga production workload.

## Mga Layunin sa Pagkatuto

- **Pag-isipan** ang mga modelo bilang atomic tools na may deklaradong kakayahan
- **I-route** ang mga kahilingan batay sa intensyon / heuristic scoring
- **Pagsamahin** ang mga output sa multi-step na mga gawain (i-decompose → lutasin → i-refine)
- **Isama** ang isang pinagsamang client API para sa mga downstream application
- **I-scale** ang disenyo sa cloud (parehong OpenAI-compatible na kontrata)

## Mga Kinakailangan

- Nakumpleto ang Sessions 1–5
- Maraming lokal na modelo na naka-cache (hal., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

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

Remote/VM service access mula sa macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Deklarasyon ng Kakayahan ng Kasangkapan (5 min)

Gumawa ng `samples/06-tools/models_catalog.py`:

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


### 2. Pagtukoy ng Intensyon at Routing (8 min)

Gumawa ng `samples/06-tools/router.py`:

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


### 3. Multi-Step Task Chaining (7 min)

Gumawa ng `samples/06-tools/pipeline.py`:

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


### 4. Starter Project: I-adapt ang `06-models-as-tools` (5 min)

Mga Pagpapahusay:
- Magdagdag ng streaming token support (progressive UI update)
- Magdagdag ng confidence scoring: lexical overlap o prompt rubric
- I-export ang trace JSON (intent → model → latency → token usage)
- Ipatupad ang cache reuse para sa mga paulit-ulit na substeps

### 5. Scaling Path sa Azure (5 min)

| Layer | Lokal (Foundry) | Cloud (Azure AI Foundry) | Estratehiya sa Paglipat |
|-------|-----------------|--------------------------|-------------------------|
| Routing | Heuristic Python | Durable microservice | I-containerize at i-deploy ang API |
| Models | SLMs na naka-cache | Managed deployments | I-map ang mga lokal na pangalan sa deployment IDs |
| Observability | CLI stats/manual | Central logging & metrics | Magdagdag ng structured trace events |
| Security | Lokal na host lamang | Azure auth / networking | Magdagdag ng key vault para sa mga lihim |
| Cost | Resource ng device | Consumption billing | Magdagdag ng budget guardrails |

## Validation Checklist

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Asahan ang model selection batay sa intensyon at ang huling refined output.

## Troubleshooting

| Problema | Sanhi | Solusyon |
|----------|-------|----------|
| Lahat ng gawain ay na-route sa parehong modelo | Mahinang mga patakaran | Palawakin ang INTENT_RULES regex set |
| Nabigo ang pipeline sa gitna ng hakbang | Walang na-load na modelo | Patakbuhin ang `foundry model run <model>` |
| Mababa ang cohesion ng output | Walang refine phase | Magdagdag ng summarization/validation pass |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Quality Patterns: Tingnan ang Session 2

---

**Tagal ng Session**: 30 min  
**Kahirapan**: Expert

## Halimbawang Scenario at Workshop Mapping

| Workshop Scripts / Notebooks | Scenario | Layunin | Dataset / Catalog Source |
|------------------------------|----------|---------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Developer assistant na humahawak ng mixed intent prompts (refactor, summarize, classify) | Heuristic intent → model alias routing na may token usage | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Multi-step planning & refinement para sa complex coding assistance task | Decompose → specialized execution → summarization refine step | Parehong `CATALOG`; mga hakbang na nagmula sa plan output |

### Narrative ng Scenario

Isang engineering productivity tool ang tumatanggap ng iba't ibang gawain: pag-refactor ng code, pag-summarize ng architectural notes, pag-classify ng feedback. Upang mabawasan ang latency at paggamit ng resource, isang maliit na general model ang nagpa-plano at nag-summarize, isang code-specialized model ang humahawak sa refactoring, at isang lightweight classification-capable model ang naglalagay ng label sa feedback. Ang pipeline script ay nagpapakita ng chaining + refinement; ang router script ay nag-i-isolate ng adaptive single-prompt routing.

### Catalog Snapshot

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Halimbawa ng Test Prompts

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace Extension (Opsyonal)

Magdagdag ng per-step trace JSON lines para sa `models_pipeline.py`:

```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Escalation Heuristic (Ideya)

Kung ang plano ay naglalaman ng mga keyword tulad ng "optimize", "security", o ang haba ng hakbang ay > 280 chars → i-escalate sa mas malaking modelo (hal., `gpt-oss-20b`) para sa hakbang na iyon lamang.

### Opsyonal na Mga Pagpapahusay

| Lugar | Pagpapahusay | Halaga | Pahiwatig |
|------|--------------|--------|-----------|
| Caching | Reuse manager + client objects | Mas mababang latency, mas kaunting overhead | Gamitin ang `workshop_utils.get_client` |
| Usage Metrics | I-capture ang tokens & per-step latency | Profiling & optimization | I-time ang bawat routed call; i-store sa trace list |
| Adaptive Routing | Confidence / cost aware | Mas mahusay na quality-cost trade-off | Magdagdag ng scoring: kung ang prompt > N chars o regex ay tumutugma sa domain → i-escalate sa mas malaking modelo |
| Dynamic Capability Registry | Hot reload catalog | Walang restart redeploy | I-load ang `catalog.json` sa runtime; bantayan ang file timestamp |
| Fallback Strategy | Robustness sa ilalim ng failures | Mas mataas na availability | Subukan ang primary → sa exception fallback alias |
| Streaming Pipeline | Maagang feedback | Pagpapabuti ng UX | I-stream ang bawat hakbang at i-buffer ang final refine input |
| Vector Intent Embeddings | Mas nuanced na routing | Mas mataas na intent accuracy | I-embed ang prompt, i-cluster & i-map ang centroid → capability |
| Trace Export | Auditable chain | Compliance/reporting | Maglabas ng JSON lines: step, intent, model, latency_ms, tokens |
| Cost Simulation | Pre-cloud estimation | Budget planning | Mag-assign ng notional cost/token bawat modelo & i-aggregate bawat task |
| Deterministic Mode | Repro reproducibility | Stable benchmarking | Env: `temperature=0`, fixed steps count |

#### Halimbawa ng Trace Structure

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

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.