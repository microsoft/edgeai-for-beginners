# Session 6: Foundry Local – Models as Tools

## Abstract

Make models work like tools wey fit join body for local AI operating layer. Dis session go show how to connect many special SLM/LLM calls, choose task route well, and show one SDK surface wey apps fit use. You go build one light model router + task planner, put am inside app script, and plan how e go scale reach Azure AI Foundry for production work.

## Learning Objectives

- **Understand** models as small tools wey get specific work wey dem fit do
- **Route** requests based on wetin person wan do or heuristic scoring
- **Connect** outputs for tasks wey get many steps (break down → solve → refine)
- **Join** one client API wey apps fit use for downstream
- **Scale** design go cloud (same OpenAI-compatible contract)

## Prerequisites

- Sessions 1–5 don complete
- Many local models don dey cache (e.g., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

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

## Demo Flow (30 min)

### 1. Tool Capability Declaration (5 min)

Create `samples/06-tools/models_catalog.py`:

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

### 2. Intent Detection & Routing (8 min)

Create `samples/06-tools/router.py`:

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

Create `samples/06-tools/pipeline.py`:

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

### 4. Starter Project: Adapt `06-models-as-tools` (5 min)

Enhancements:
- Add streaming token support (progressive UI update)
- Add confidence scoring: lexical overlap or prompt rubric
- Export trace JSON (intent → model → latency → token usage)
- Implement cache reuse for repeated substeps

### 5. Scaling Path to Azure (5 min)

| Layer | Local (Foundry) | Cloud (Azure AI Foundry) | Transition Strategy |
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

Expect say model go select based on wetin person wan do and final output go dey refined.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| All tasks dey go same model | Weak rules | Add more INTENT_RULES regex set |
| Pipeline dey fail for middle | Model no load | Run `foundry model run <model>` |
| Output no dey make sense | No refine phase | Add summarization/validation pass |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Quality Patterns: See Session 2

---

**Session Duration**: 30 min  
**Difficulty**: Expert

## Sample Scenario & Workshop Mapping

| Workshop Scripts / Notebooks | Scenario | Objective | Dataset / Catalog Source |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Developer assistant wey dey handle mixed intent prompts (refactor, summarize, classify) | Heuristic intent → model alias routing with token usage | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Multi-step planning & refinement for complex coding assistance task | Break down → specialized execution → summarization refine step | Same `CATALOG`; steps derived from plan output |

### Scenario Narrative
One engineering productivity tool dey receive different tasks: refactor code, summarize architectural notes, classify feedback. To reduce latency & resource usage, one small general model go plan and summarize, one code-specialized model go handle refactoring, and one lightweight classification-capable model go label feedback. The pipeline script dey show how to connect + refine; the router script dey show adaptive single-prompt routing.

### Catalog Snapshot
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### Example Test Prompts
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Trace Extension (Optional)
Add per-step trace JSON lines for `models_pipeline.py`:
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
If plan get keywords like "optimize", "security", or step length pass 280 chars → escalate to bigger model (e.g., `gpt-oss-20b`) for that step only.

### Optional Enhancements

| Area | Enhancement | Value | Hint |
|------|-------------|-------|------|
| Caching | Reuse manager + client objects | Lower latency, less overhead | Use `workshop_utils.get_client` |
| Usage Metrics | Capture tokens & per-step latency | Profiling & optimization | Time each routed call; store in trace list |
| Adaptive Routing | Confidence / cost aware | Better quality-cost trade-off | Add scoring: if prompt pass N chars or regex match domain → escalate to larger model |
| Dynamic Capability Registry | Hot reload catalog | No restart redeploy | Load `catalog.json` at runtime; watch file timestamp |
| Fallback Strategy | Robustness under failures | Higher availability | Try primary → on exception fallback alias |
| Streaming Pipeline | Early feedback | UX improvement | Stream each step and buffer final refine input |
| Vector Intent Embeddings | More nuanced routing | Higher intent accuracy | Embed prompt, cluster & map centroid → capability |
| Trace Export | Auditable chain | Compliance/reporting | Emit JSON lines: step, intent, model, latency_ms, tokens |
| Cost Simulation | Pre-cloud estimation | Budget planning | Assign notional cost/token per model & aggregate per task |
| Deterministic Mode | Repro reproducibility | Stable benchmarking | Env: `temperature=0`, fixed steps count |

#### Trace Structure Example

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshun service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshun. Even as we dey try make am accurate, abeg make you sabi say automatik transleshun fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di main source. For important mata, na beta make you use professional human transleshun. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshun.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->