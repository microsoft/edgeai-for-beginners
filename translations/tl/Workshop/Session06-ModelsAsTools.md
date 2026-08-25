# Session 6: Foundry Local – Mga Modelo bilang mga Kasangkapan

## Abstrak

Ituring ang mga modelo bilang mga komposableng kasangkapan sa loob ng lokal na AI operating layer. Ipinapakita ng sesyon na ito kung paano i-chain ang maraming espesyalisadong tawag sa SLM/LLM, piliing i-route ang mga gawain, at i-expose ang isang pinag-isang SDK surface sa mga aplikasyon. Bubuo ka ng magaan na model router + task planner, isasama ito sa isang app script, at ilalahad ang scaling path patungo sa Azure AI Foundry para sa mga production workload.

## Mga Layunin sa Pagkatuto

- **I-konsepto** ang mga modelo bilang atomic na kasangkapan na may ideklara na kakayahan
- **I-route** ang mga kahilingan base sa intensyon / heuristic scoring
- **I-chain** ang mga output sa multi-step na mga gawain (i-decompose → lutasin → pinuhin)
- **I-integrate** ang isang pinag-isang client API para sa downstream na mga aplikasyon
- **I-scale** ang disenyo sa cloud (parehong OpenAI-compatible contract)

## Mga Kinakailangan

- Natapos ang Sessions 1–5
- Maraming lokal na mga modelo ang naka-cache (hal., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

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

## Daloy ng Demo (30 min)

### 1. Pagdeklara ng Kakayahan ng Kasangkapan (5 min)

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

### 2. Pag-detekta ng Intensyon at Routing (8 min)

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
    # Iskor katalogo: unahin ang pagtugma ng kakayahan, pagkatapos ang prayoridad
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Ayusin: unahin ang tumugmang True, pagkatapos ang pinakamababang halaga ng prayoridad
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

### 3. Pagkadena ng Multi-Step na Gawain (7 min)

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
- Magdagdag ng suporta sa streaming token (progressive UI update)
- Magdagdag ng confidence scoring: lexical overlap o prompt rubric
- Mag-export ng trace JSON (intensyon → modelo → latency → paggamit ng token)
- Ipatupad ang reuse ng cache para sa paulit-ulit na mga substep

### 5. Path ng Pag-scale patungo sa Azure (5 min)

| Layer | Lokal (Foundry) | Cloud (Azure AI Foundry) | Estratehiya sa Transisyon |
|-------|-----------------|--------------------------|---------------------|
| Routing | Heuristic Python | Durable microservice | Containerize & mag-deploy ng API |
| Mga Modelo | SLMs na naka-cache | Managed deployments | I-map ang lokal na mga pangalan sa deployment IDs |
| Observability | CLI stats/manwal | Central logging at metrics | Magdagdag ng mga structured trace events |
| Seguridad | Lokal lang ang host | Azure auth / networking | Magpakilala ng key vault para sa mga lihim |
| Gastos | Device resource | Consumption billing | Magdagdag ng mga budget guardrails |

## Checklist sa Pag-validate

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Inaasahan ang intensyon-based na pagpili ng modelo at panghuling pinaayos na output.

## Pag-troubleshoot

| Problema | Sanhi | Solusyon |
|---------|-------|-----|
| Lahat ng gawain ay naka-route sa parehong modelo | Mahinang mga panuntunan | Pagyamanin ang INTENT_RULES regex set |
| Nabibigo ang pipeline sa kalagitnaan ng hakbang | Hindi na-load ang modelo | Patakbuhin ang `foundry model run <model>` |
| Mababa ang pagkakaugnay-ugnay ng output | Walang refine phase | Magdagdag ng summarization/validation pass |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Mga Pattern sa Kalidad ng Prompt: Tingnan ang Session 2

---

**Tagal ng Session**: 30 min  
**Kahirapan**: Eksperto

## Halimbawang Senaryo at Pagsasaayos sa Workshop

| Mga Workshop Script / Notebook | Senaryo | Layunin | Pinagmulan ng Dataset / Katalog |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistant sa developer na humahawak ng halo-halong intensyon na mga prompt (refactor, summarize, classify) | Heuristic intent → model alias routing gamit ang paggamit ng token | Inline na `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Multi-step na pagpaplano & pag-refine para sa komplikadong coding assistance task | I-decompose → espesyalisadong pagpapatupad → hakbang ng summarization refine | Parehong `CATALOG`; mga hakbang na nagmula sa output ng plano |

### Kwento ng Senaryo
Isang kasangkapan sa produktibidad ng engineering ang tumatanggap ng iba't ibang gawain: pag-refactor ng code, pag-summarize ng mga tala sa arkitektura, pag-classify ng feedback. Upang mabawasan ang latency at paggamit ng resource, isang maliit na general na modelo ang nagpaplano at nagsusuma, isang code-specialized na modelo ang humahawak ng refactoring, at isang magaan na modelo na may kakayahan sa classification ang naglalagay ng label sa feedback. Ipinapakita ng pipeline script ang chaining + refinement; ang router script ay nag-iisolate ng adaptive single-prompt routing.

### Snapshot ng Katalogo
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### Mga Halimbawang Test Prompt
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Extension ng Trace (Opsyonal)
Magdagdag ng bawat-hakbang ng trace JSON lines para sa `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### Heuristic ng Escalation (Ideya)
Kung ang plano ay may mga keyword na tulad ng "optimize", "security", o ang haba ng hakbang > 280 na mga character → i-escalate sa mas malaking modelo (hal., `gpt-oss-20b`) para sa hakbang na iyon lamang.

### Opsyonal na mga Pagpapahusay

| Lugar | Pagpapahusay | Halaga | Pahiwatig |
|------|-------------|-------|------|
| Caching | Muling paggamit ng manager + client objects | Mas mababang latency, mas kaunting overhead | Gamitin ang `workshop_utils.get_client` |
| Usage Metrics | Kunin ang tokens & bawat-hakbang latency | Profiling at optimisasyon | Sukatin bawat routed na tawag; itago sa trace list |
| Adaptive Routing | Confidence / kamalayan sa gastos | Mas magandang kalakalan sa kalidad-gastos | Magdagdag ng scoring: kung ang prompt > N na mga character o tumutugma ang regex sa domain → i-escalate sa mas malaking modelo |
| Dynamic Capability Registry | Hot reload ng katalogo | Walang restart na pag-redeploy | I-load ang `catalog.json` sa runtime; bantayan ang timestamp ng file |
| Fallback Strategy | Katatagan sa ilalim ng mga pagkabigo | Mas mataas na availability | Subukan ang pangunahing → sa exception fallback alias |
| Streaming Pipeline | Maagang feedback | Pagpapabuti ng UX | I-stream ang bawat hakbang at i-buffer ang panghuling refine input |
| Vector Intent Embeddings | Mas masalimuot na routing | Mas mataas na katumpakan ng intensyon | I-embed ang prompt, i-cluster at i-map ang centroid → kakayahan |
| Trace Export | Chain na ma-audit | Compliance/pag-uulat | Maglabas ng mga JSON lines: hakbang, intensyon, modelo, latency_ms, tokens |
| Cost Simulation | Estimasyong bago ang cloud | Pagpaplano sa budget | Magtalaga ng notional na gastos/token bawat modelo at i-aggregate bawat gawain |
| Deterministic Mode | Pag-uulit ng reproduktibilidad | Matatag na benchmarking | Env: `temperature=0`, nakapirming bilang ng mga hakbang |

#### Halimbawa ng Estruktura ng Trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### Sketch ng Adaptive Escalation

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # itaas sa mas malaking modelo ng pangangatwiran kung available
    alias = 'gpt-oss-20b'
```

#### Hot Reload ng Model Catalog

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
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->