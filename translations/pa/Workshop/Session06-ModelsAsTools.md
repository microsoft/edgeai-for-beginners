# ਸੈਸ਼ਨ 6: ਫਾਊਂਡਰੀ ਲੋਕਲ – ਮਾਡਲਾਂ ਨੂੰ ਟੂਲ ਵਜੋਂ ਵਰਤਣਾ

## ਸਾਰ

ਮਾਡਲਾਂ ਨੂੰ ਇੱਕ ਸਥਾਨਕ AI ਓਪਰੇਟਿੰਗ ਲੇਅਰ ਦੇ ਅੰਦਰ ਸੰਯੋਜਕ ਟੂਲ ਵਜੋਂ ਵਰਤੋ। ਇਸ ਸੈਸ਼ਨ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ ਕਿ ਕਿਵੇਂ ਕਈ ਵਿਸ਼ੇਸ਼ SLM/LLM ਕਾਲਾਂ ਨੂੰ ਜੋੜਨਾ, ਕੰਮਾਂ ਨੂੰ ਚੁਣਿੰਦਾ ਰੂਪ ਵਿੱਚ ਰੂਟ ਕਰਨਾ, ਅਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਇੱਕ ਇਕਰੂਪ SDK ਸਤਹ ਨੂੰ ਉਜਾਗਰ ਕਰਨਾ ਹੈ। ਤੁਸੀਂ ਇੱਕ ਹਲਕਾ ਮਾਡਲ ਰੂਟਰ + ਟਾਸਕ ਪਲਾਨਰ ਬਣਾਉਗੇ, ਇਸਨੂੰ ਇੱਕ ਐਪ ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋਗੇ, ਅਤੇ ਉਤਪਾਦਨ ਵਰਕਲੋਡ ਲਈ Azure AI Foundry ਤੱਕ ਸਕੇਲਿੰਗ ਪਾਥ ਦਾ ਰੂਪਰੇਖਾ ਤਿਆਰ ਕਰੋਗੇ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

- **ਸੰਕਲਪਿਤ ਕਰੋ** ਮਾਡਲਾਂ ਨੂੰ ਐਟਮਿਕ ਟੂਲ ਵਜੋਂ ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਘੋਸ਼ਿਤ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ
- **ਰੂਟ** ਇਰਾਦੇ / ਹਿਊਰਿਸਟਿਕ ਸਕੋਰਿੰਗ ਦੇ ਆਧਾਰ 'ਤੇ ਬੇਨਤੀ
- **ਚੇਨ** ਨਤੀਜੇ ਬਹੁ-ਕਦਮ ਕੰਮਾਂ 'ਤੇ (ਵੰਡੋ → ਹੱਲ ਕਰੋ → ਸੁਧਾਰੋ)
- **ਇਕਰੂਪਤਾ** ਕਲਾਇੰਟ API ਨੂੰ ਡਾਊਨਸਟ੍ਰੀਮ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਸ਼ਾਮਲ ਕਰੋ
- **ਸਕੇਲ** ਡਿਜ਼ਾਈਨ ਨੂੰ ਕਲਾਉਡ (ਇੱਕੋ OpenAI-ਅਨੁਕੂਲ ਸੰਬੰਧ)

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਸੈਸ਼ਨ 1–5 ਪੂਰੇ ਹੋਏ
- ਕਈ ਸਥਾਨਕ ਮਾਡਲ ਕੈਸ਼ ਕੀਤੇ ਗਏ (ਜਿਵੇਂ ਕਿ `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਵਾਤਾਵਰਣ ਸਨਿੱਪਟ

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

macOS ਤੋਂ ਰਿਮੋਟ/VM ਸੇਵਾ ਪਹੁੰਚ:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. ਟੂਲ ਸਮਰੱਥਾ ਘੋਸ਼ਣਾ (5 ਮਿੰਟ)

`samples/06-tools/models_catalog.py` ਬਣਾਓ:

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


### 2. ਇਰਾਦਾ ਪਛਾਣ ਅਤੇ ਰੂਟਿੰਗ (8 ਮਿੰਟ)

`samples/06-tools/router.py` ਬਣਾਓ:

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


### 3. ਬਹੁ-ਕਦਮ ਟਾਸਕ ਚੇਨਿੰਗ (7 ਮਿੰਟ)

`samples/06-tools/pipeline.py` ਬਣਾਓ:

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


### 4. ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ: `06-models-as-tools` ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ (5 ਮਿੰਟ)

ਸੁਧਾਰ:
- ਸਟ੍ਰੀਮਿੰਗ ਟੋਕਨ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕਰੋ (ਪ੍ਰਗਤੀਸ਼ੀਲ UI ਅਪਡੇਟ)
- ਭਰੋਸੇਮੰਦ ਸਕੋਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ: ਲੈਕਸਿਕਲ ਓਵਰਲੈਪ ਜਾਂ ਪ੍ਰੋਮਪਟ ਰੂਬ੍ਰਿਕ
- ਟ੍ਰੇਸ JSON ਐਕਸਪੋਰਟ ਕਰੋ (ਇਰਾਦਾ → ਮਾਡਲ → ਲੈਟੈਂਸੀ → ਟੋਕਨ ਵਰਤੋਂ)
- ਦੁਹਰਾਏ ਗਏ ਉਪਕਦਮਾਂ ਲਈ ਕੈਸ਼ ਦੁਬਾਰਾ ਵਰਤੋ

### 5. Azure ਤੱਕ ਸਕੇਲਿੰਗ ਪਾਥ (5 ਮਿੰਟ)

| ਲੇਅਰ | ਸਥਾਨਕ (Foundry) | ਕਲਾਉਡ (Azure AI Foundry) | ਟ੍ਰਾਂਜ਼ੀਸ਼ਨ ਰਣਨੀਤੀ |
|-------|-----------------|--------------------------|---------------------|
| ਰੂਟਿੰਗ | ਹਿਊਰਿਸਟਿਕ ਪਾਇਥਨ | ਡਿਊਰੇਬਲ ਮਾਈਕ੍ਰੋਸਰਵਿਸ | API ਨੂੰ ਕੰਟੇਨਰਾਈਜ਼ ਅਤੇ ਡਿਪਲੌਇ ਕਰੋ |
| ਮਾਡਲ | SLMs ਕੈਸ਼ ਕੀਤੇ | ਪ੍ਰਬੰਧਿਤ ਡਿਪਲੌਇਮੈਂਟ | ਸਥਾਨਕ ਨਾਮਾਂ ਨੂੰ ਡਿਪਲੌਇਮੈਂਟ IDs ਨਾਲ ਮੈਪ ਕਰੋ |
| ਅਵਲੋਕਨਯੋਗਤਾ | CLI ਸਟੈਟਸ/ਮੈਨੂਅਲ | ਕੇਂਦਰੀ ਲੌਗਿੰਗ ਅਤੇ ਮੈਟ੍ਰਿਕਸ | ਸਟ੍ਰਕਚਰਡ ਟ੍ਰੇਸ ਇਵੈਂਟ ਸ਼ਾਮਲ ਕਰੋ |
| ਸੁਰੱਖਿਆ | ਸਿਰਫ਼ ਸਥਾਨਕ ਹੋਸਟ | Azure ਪ੍ਰਮਾਣਿਕਤਾ / ਨੈਟਵਰਕਿੰਗ | ਰਾਜ਼ਾਂ ਲਈ ਕੀ ਵੌਲਟ ਸ਼ਾਮਲ ਕਰੋ |
| ਲਾਗਤ | ਡਿਵਾਈਸ ਸਰੋਤ | ਖਪਤ ਬਿਲਿੰਗ | ਬਜਟ ਗਾਰਡਰੇਲ ਸ਼ਾਮਲ ਕਰੋ |

## ਵੈਧਤਾ ਚੈੱਕਲਿਸਟ

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

ਇਰਾਦਾ-ਅਧਾਰਿਤ ਮਾਡਲ ਚੋਣ ਅਤੇ ਅੰਤਮ ਸੁਧਾਰਿਤ ਨਤੀਜੇ ਦੀ ਉਮੀਦ ਕਰੋ।

## ਸਮੱਸਿਆ ਹੱਲ

| ਸਮੱਸਿਆ | ਕਾਰਨ | ਹੱਲ |
|---------|-------|-----|
| ਸਾਰੇ ਕੰਮ ਇੱਕੋ ਮਾਡਲ ਨੂੰ ਰੂਟ ਕੀਤੇ | ਕਮਜ਼ੋਰ ਨਿਯਮ | INTENT_RULES regex ਸੈੱਟ ਨੂੰ ਵਧਾਓ |
| ਪਾਈਪਲਾਈਨ ਮੱਧ-ਕਦਮ 'ਤੇ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ | ਲੋਡ ਕੀਤਾ ਮਾਡਲ ਗੁੰਮ ਹੈ | `foundry model run <model>` ਚਲਾਓ |
| ਘੱਟ ਨਤੀਜਾ ਸੰਗਠਨ | ਕੋਈ ਸੁਧਾਰ ਫੇਜ਼ ਨਹੀਂ | ਸਮਰੀਕਰਨ/ਵੈਰੀਫਿਕੇਸ਼ਨ ਪਾਸ ਸ਼ਾਮਲ ਕਰੋ |

## ਸੰਦਰਭ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- ਪ੍ਰੋਮਪਟ ਕੁਆਲਿਟੀ ਪੈਟਰਨ: ਸੈਸ਼ਨ 2 ਵੇਖੋ

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ  
**ਮੁਸ਼ਕਲਾਈ ਦਾ ਪੱਧਰ**: ਮਾਹਰ

## ਨਮੂਨਾ ਸਥਿਤੀ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ / ਨੋਟਬੁੱਕ | ਸਥਿਤੀ | ਉਦੇਸ਼ | ਡਾਟਾਸੈਟ / ਕੈਟਾਲੌਗ ਸਰੋਤ |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ਵਿਕਾਸਕ ਸਹਾਇਕ ਜੋ ਮਿਲੇ-ਜੁਲੇ ਇਰਾਦਾ ਪ੍ਰੋਮਪਟਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ (ਰੀਫੈਕਟਰ, ਸਮਰੀਕਰਨ, ਵਰਗੀਕਰਨ) | ਹਿਊਰਿਸਟਿਕ ਇਰਾਦਾ → ਮਾਡਲ ਅਲਿਆਸ ਰੂਟਿੰਗ ਟੋਕਨ ਵਰਤੋਂ ਨਾਲ | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | ਜਟਿਲ ਕੋਡਿੰਗ ਸਹਾਇਤਾ ਕੰਮ ਲਈ ਬਹੁ-ਕਦਮ ਯੋਜਨਾ ਅਤੇ ਸੁਧਾਰ | ਵੰਡੋ → ਵਿਸ਼ੇਸ਼ਤਾਂ ਨਾਲ ਕਾਰਜ → ਸਮਰੀਕਰਨ ਸੁਧਾਰ ਕਦਮ | ਉਹੀ `CATALOG`; ਯੋਜਨਾ ਨਤੀਜੇ ਤੋਂ ਕਦਮ ਲਿਆ |

### ਸਥਿਤੀ ਕਹਾਣੀ
ਇੰਜੀਨੀਅਰਿੰਗ ਉਤਪਾਦਕਤਾ ਟੂਲ ਨੂੰ ਵੱਖ-ਵੱਖ ਕੰਮ ਮਿਲਦੇ ਹਨ: ਕੋਡ ਨੂੰ ਰੀਫੈਕਟਰ ਕਰੋ, ਆਰਕੀਟੈਕਚਰਲ ਨੋਟਸ ਦਾ ਸਮਰੀਕਰਨ ਕਰੋ, ਫੀਡਬੈਕ ਨੂੰ ਵਰਗੀਕਰਤ ਕਰੋ। ਲੈਟੈਂਸੀ ਅਤੇ ਸਰੋਤ ਦੀ ਵਰਤੋਂ ਨੂੰ ਘਟਾਉਣ ਲਈ, ਇੱਕ ਛੋਟਾ ਜਨਰਲ ਮਾਡਲ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਸਮਰੀਕਰਨ ਕਰਦਾ ਹੈ, ਇੱਕ ਕੋਡ-ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਰੀਫੈਕਟੋਰਿੰਗ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ, ਅਤੇ ਇੱਕ ਹਲਕਾ ਵਰਗੀਕਰਨ-ਸਮਰੱਥ ਮਾਡਲ ਫੀਡਬੈਕ ਨੂੰ ਲੇਬਲ ਕਰਦਾ ਹੈ। ਪਾਈਪਲਾਈਨ ਸਕ੍ਰਿਪਟ ਚੇਨਿੰਗ + ਸੁਧਾਰ ਦਿਖਾਉਂਦਾ ਹੈ; ਰੂਟਰ ਸਕ੍ਰਿਪਟ ਅਨੁਕੂਲ ਸਿੰਗਲ-ਪ੍ਰੋਮਪਟ ਰੂਟਿੰਗ ਨੂੰ ਅਲੱਗ ਕਰਦਾ ਹੈ।

### ਕੈਟਾਲੌਗ ਸਨੈਪਸ਼ਾਟ
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### ਉਦਾਹਰਣ ਟੈਸਟ ਪ੍ਰੋਮਪਟ
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### ਟ੍ਰੇਸ ਐਕਸਟੈਂਸ਼ਨ (ਵਿਕਲਪਿਕ)
`models_pipeline.py` ਲਈ ਪ੍ਰਤੀ-ਕਦਮ ਟ੍ਰੇਸ JSON ਲਾਈਨਾਂ ਸ਼ਾਮਲ ਕਰੋ:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### ਐਸਕਲੇਸ਼ਨ ਹਿਊਰਿਸਟਿਕ (ਆਈਡੀਆ)
ਜੇ ਯੋਜਨਾ ਵਿੱਚ "optimize", "security" ਵਰਗੇ ਕੁੰਜੀਸ਼ਬਦ ਸ਼ਾਮਲ ਹਨ ਜਾਂ ਕਦਮ ਦੀ ਲੰਬਾਈ > 280 ਅੱਖਰ ਹੈ → ਉਸ ਕਦਮ ਲਈ ਵੱਡੇ ਮਾਡਲ (ਜਿਵੇਂ `gpt-oss-20b`) ਨੂੰ ਐਸਕਲੇਟ ਕਰੋ।

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਖੇਤਰ | ਸੁਧਾਰ | ਮੁੱਲ | ਸੰਕੇਤ |
|------|-------------|-------|------|
| ਕੈਸ਼ਿੰਗ | ਮੈਨੇਜਰ + ਕਲਾਇੰਟ ਵਸਤੂਆਂ ਦੁਬਾਰਾ ਵਰਤੋ | ਘੱਟ ਲੈਟੈਂਸੀ, ਘੱਟ ਓਵਰਹੈੱਡ | `workshop_utils.get_client` ਵਰਤੋ |
| ਵਰਤੋਂ ਮੈਟ੍ਰਿਕਸ | ਟੋਕਨ ਅਤੇ ਪ੍ਰਤੀ-ਕਦਮ ਲੈਟੈਂਸੀ ਕੈਪਚਰ ਕਰੋ | ਪ੍ਰੋਫਾਈਲਿੰਗ ਅਤੇ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ | ਹਰ ਰੂਟ ਕੀਤੇ ਕਾਲ ਨੂੰ ਸਮਾਂ ਦਿਓ; ਟ੍ਰੇਸ ਸੂਚੀ ਵਿੱਚ ਸਟੋਰ ਕਰੋ |
| ਅਨੁਕੂਲ ਰੂਟਿੰਗ | ਭਰੋਸੇਮੰਦ / ਲਾਗਤ ਜਾਗਰੂਕ | ਵਧੀਆ ਗੁਣਵੱਤਾ-ਲਾਗਤ ਦਾ ਵਪਾਰ | ਸਕੋਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ: ਜੇ ਪ੍ਰੋਮਪਟ > N ਅੱਖਰ ਜਾਂ regex ਡੋਮੇਨ ਨੂੰ ਮੈਚ ਕਰਦਾ ਹੈ → ਵੱਡੇ ਮਾਡਲ ਨੂੰ ਐਸਕਲੇਟ ਕਰੋ |
| ਡਾਇਨਾਮਿਕ ਸਮਰੱਥਾ ਰਜਿਸਟਰੀ | ਕੈਟਾਲੌਗ ਨੂੰ ਹੌਟ ਰੀਲੋਡ ਕਰੋ | ਕੋਈ ਰੀਸਟਾਰਟ ਰੀਡਿਪਲੌਇ ਨਹੀਂ | ਰਨਟਾਈਮ 'ਤੇ `catalog.json` ਲੋਡ ਕਰੋ; ਫਾਈਲ ਟਾਈਮਸਟੈਂਪ ਨੂੰ ਵੇਖੋ |
| ਫਾਲਬੈਕ ਰਣਨੀਤੀ | ਫੇਲ੍ਹ ਹੋਣ 'ਤੇ ਮਜ਼ਬੂਤੀ | ਵਧੇਰੇ ਉਪਲਬਧਤਾ | ਪ੍ਰਾਇਮਰੀ ਨੂੰ ਅਜ਼ਮਾਓ → ਐਕਸਪਸ਼ਨ 'ਤੇ ਫਾਲਬੈਕ ਅਲਿਆਸ |
| ਸਟ੍ਰੀਮਿੰਗ ਪਾਈਪਲਾਈਨ | ਸ਼ੁਰੂਆਤੀ ਫੀਡਬੈਕ | UX ਸੁਧਾਰ | ਹਰ ਕਦਮ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰੋ ਅਤੇ ਅੰਤਮ ਸੁਧਾਰ ਇਨਪੁਟ ਨੂੰ ਬਫਰ ਕਰੋ |
| ਵੈਕਟਰ ਇਰਾਦਾ ਐਮਬੈਡਿੰਗ | ਹੋਰ ਸੁਖਮ ਰੂਟਿੰਗ | ਵਧੇਰੇ ਇਰਾਦਾ ਸਹੀਤਾ | ਪ੍ਰੋਮਪਟ ਨੂੰ ਐਮਬੈਡ ਕਰੋ, ਕਲੱਸਟਰ ਕਰੋ ਅਤੇ ਸੈਂਟਰਾਇਡ → ਸਮਰੱਥਾ ਨੂੰ ਮੈਪ ਕਰੋ |
| ਟ੍ਰੇਸ ਐਕਸਪੋਰਟ | ਚੇਨ ਆਡਿਟੇਬਲ | ਅਨੁਕੂਲਤਾ/ਰਿਪੋਰਟਿੰਗ | JSON ਲਾਈਨਾਂ ਨੂੰ ਨਿਕਾਸ ਕਰੋ: ਕਦਮ, ਇਰਾਦਾ, ਮਾਡਲ, latency_ms, tokens |
| ਲਾਗਤ ਸਿਮੂਲੇਸ਼ਨ | ਪ੍ਰੀ-ਕਲਾਉਡ ਅਨੁਮਾਨ | ਬਜਟ ਯੋਜਨਾ | ਪ੍ਰਤੀ ਮਾਡਲ ਟੋਕਨ/ਲਾਗਤ ਲਈ ਨੋਸ਼ਨਲ ਲਾਗਤ ਦਿਓ ਅਤੇ ਪ੍ਰਤੀ-ਕੰਮ ਕੁਲ ਕਰੋ |
| ਨਿਰਧਾਰਤ ਮੋਡ | ਰੀਪ੍ਰੋ ਦੁਬਾਰਾ ਬਣਾਉਣਯੋਗਤਾ | ਸਥਿਰ ਬੈਂਚਮਾਰਕਿੰਗ | Env: `temperature=0`, ਨਿਰਧਾਰਤ ਕਦਮ ਗਿਣਤੀ |

#### ਟ੍ਰੇਸ ਸਟ੍ਰਕਚਰ ਉਦਾਹਰਣ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### ਅਨੁਕੂਲ ਐਸਕਲੇਸ਼ਨ ਸਕੈਚ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### ਮਾਡਲ ਕੈਟਾਲੌਗ ਹੌਟ ਰੀਲੋਡ

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

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।