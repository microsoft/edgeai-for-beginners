<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T19:59:07+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "en"
}
-->
# Session 6: Foundry Local – Models as Tools

## Abstract

Treat models as modular tools within a local AI operating layer. This session demonstrates how to chain multiple specialized SLM/LLM calls, route tasks selectively, and provide a unified SDK interface for applications. You will build a lightweight model router and task planner, integrate it into an application script, and outline the scaling path to Azure AI Foundry for production workloads.

## Learning Objectives

- **Understand** models as atomic tools with defined capabilities
- **Route** requests based on intent or heuristic scoring
- **Chain** outputs across multi-step tasks (decompose → solve → refine)
- **Integrate** a unified client API for downstream applications
- **Scale** design to the cloud (using the same OpenAI-compatible contract)

## Prerequisites

- Completion of Sessions 1–5
- Multiple local models cached (e.g., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

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
- Add streaming token support (progressive UI updates)
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

Expect intent-based model selection and final refined output.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| All tasks routed to same model | Weak rules | Enrich INTENT_RULES regex set |
| Pipeline fails mid-step | Missing model loaded | Run `foundry model run <model>` |
| Low output cohesion | No refine phase | Add summarization/validation pass |

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
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Developer assistant handling mixed intent prompts (refactor, summarize, classify) | Heuristic intent → model alias routing with token usage | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Multi-step planning & refinement for complex coding assistance task | Decompose → specialized execution → summarization refine step | Same `CATALOG`; steps derived from plan output |

### Scenario Narrative
An engineering productivity tool receives diverse tasks: refactor code, summarize architectural notes, classify feedback. To minimize latency and resource usage, a small general model plans and summarizes, a code-specialized model handles refactoring, and a lightweight classification-capable model labels feedback. The pipeline script demonstrates chaining and refinement; the router script isolates adaptive single-prompt routing.

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
If the plan contains keywords like "optimize", "security", or step length > 280 characters → escalate to a larger model (e.g., `gpt-oss-20b`) for that step only.

### Optional Enhancements

| Area | Enhancement | Value | Hint |
|------|-------------|-------|------|
| Caching | Reuse manager + client objects | Lower latency, less overhead | Use `workshop_utils.get_client` |
| Usage Metrics | Capture tokens & per-step latency | Profiling & optimization | Time each routed call; store in trace list |
| Adaptive Routing | Confidence / cost aware | Better quality-cost trade-off | Add scoring: if prompt > N chars or regex matches domain → escalate to larger model |
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

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.