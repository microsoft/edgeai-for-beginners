# ಸೆಷನ್ 6: ಫೌಂಡ್ರಿ ಲೋಕಲ್ – ಮಾದರಿಗಳನ್ನು ಉಪಕರಣಗಳಾಗಿ ಬಳಸುವುದು

## ಸಾರಾಂಶ

ಮಾದರಿಗಳನ್ನು ಸ್ಥಳೀಯ AI ಕಾರ್ಯಾಚರಣೆ ಪದರದ ಒಳಗೆ ಸಂಯೋಜನೀಯ ಉಪಕರಣಗಳಾಗಿ ಪರಿಗಣಿಸಿ. ಈ ಸೆಷನ್ ಹಲವಾರು ವಿಶೇಷ SLM/LLM ಕರೆಗಳನ್ನು ಸರಪಳಿಯಾಗಿ ಜೋಡಿಸುವುದು, ಕಾರ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ ಮಾರ್ಗದರ್ಶನ ಮಾಡುವುದು ಮತ್ತು ಅನ್ವಯಿಕೆಗಳಿಗೆ ಏಕೀಕೃತ SDK ಮೇಲ್ಮೈ ಅನ್ನು ಬಹಿರಂಗಪಡಿಸುವುದನ್ನು ತೋರಿಸುತ್ತದೆ. ನೀವು ಒಂದು ಲಘು ತೂಕದ ಮಾದರಿ ರೌಟರ್ + ಕಾರ್ಯ ಯೋಜಕವನ್ನು ನಿರ್ಮಿಸಿ, ಅದನ್ನು ಅಪ್ಲಿಕೇಶನ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗೆ ಸಂಯೋಜಿಸಿ, ಮತ್ತು ಉತ್ಪಾದನಾ ಕಾರ್ಯಭಾರಗಳಿಗೆ Azure AI Foundry ಗೆ ವಿಸ್ತರಣೆಯ ಮಾರ್ಗವನ್ನು ರೂಪಿಸುವಿರಿ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

- **ಧಾರಣಾತ್ಮಕವಾಗಿ** ಮಾದರಿಗಳನ್ನು ಘೋಷಿತ ಸಾಮರ್ಥ್ಯಗಳ atomic ಉಪಕರಣಗಳಾಗಿ ಪರಿಗಣಿಸುವುದು  
- **ಮಾರ್ಗದರ್ಶನ** ಉದ್ದೇಶ / heuristic ಅಂಕಗಳ ಆಧಾರದ ಮೇಲೆ ವಿನಂತಿಗಳನ್ನು  
- **ಸರಪಳಿ** ಬಹು ಹಂತದ ಕಾರ್ಯಗಳ ಮೂಲಕ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು (ವಿಭಜಿಸಿ → ಪರಿಹರಿಸಿ → ಸುಧಾರಿಸಿ)  
- **ಸಂಯೋಜನೆ** ಕೆಳಗಿನ ಅನ್ವಯಿಕೆಗಳಿಗೆ ಏಕೀಕೃತ ಕ್ಲೈಂಟ್ API  
- **ವಿಸ್ತರಣೆ** ವಿನ್ಯಾಸವನ್ನು ಕ್ಲೌಡ್‌ಗೆ (ಒಂದೇ OpenAI-ಸಮ್ಮತ ಒಪ್ಪಂದ)

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- ಸೆಷನ್‌ಗಳು 1–5 ಪೂರ್ಣಗೊಂಡಿವೆ  
- ಹಲವಾರು ಸ್ಥಳೀಯ ಮಾದರಿಗಳು ಕ್ಯಾಶ್ ಮಾಡಲಾಗಿದೆ (ಉದಾ., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ಸ্নಿಪೆಟ್

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
  
macOS ನಿಂದ ರಿಮೋಟ್/VM ಸೇವೆ ಪ್ರವೇಶ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ಡೆಮೊ ಫ್ಲೋ (30 ನಿಮಿಷ)

### 1. ಉಪಕರಣ ಸಾಮರ್ಥ್ಯ ಘೋಷಣೆ (5 ನಿಮಿಷ)

` samples/06-tools/models_catalog.py` ರಚಿಸಿ:  

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
  
### 2. ಉದ್ದೇಶ ಪತ್ತೆ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ (8 ನಿಮಿಷ)

`samples/06-tools/router.py` ರಚಿಸಿ:  

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
    # ಸ್ಕೋರ್ ಕ್ಯಾಟಲಾಗ್: ಸಾಮರ್ಥ್ಯ ಹೊಂದಾಣಿಕೆ ಮೊದಲು, ನಂತರ ಪ್ರಾಥಮಿಕತೆ
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # ವಿಂಗಡಿಸಿ: ಮೊದಲಿಗೆ ಹೊಂದಾಣಿಕೆ ಸತ್ಯ, ನಂತರ ಕನಿಷ್ಠ ಪ್ರಾಥಮಿಕತೆ ಮೌಲ್ಯ
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
  
### 3. ಬಹು ಹಂತದ ಕಾರ್ಯ ಸರಪಳಿ (7 ನಿಮಿಷ)

`samples/06-tools/pipeline.py` ರಚಿಸಿ:  

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
  
### 4. ಪ್ರಾರಂಭಿಕ ಪ್ರಾಜೆಕ್ಟ್: `06-models-as-tools` ಅನ್ನು ಹೊಂದಿಸಿ (5 ನಿಮಿಷ)

ಸುಧಾರಣೆಗಳು:  
- ಸ್ಟ್ರೀಮಿಂಗ್ ಟೋಕನ್ ಬೆಂಬಲ ಸೇರಿಸಿ (ಪ್ರಗತಿಶೀಲ UI ನವೀಕರಣ)  
- ವಿಶ್ವಾಸ ಅಂಕಗಳನ್ನು ಸೇರಿಸಿ: ಲೆಕ್ಸಿಕಲ್ ಓವರ್‌ಲ್ಯಾಪ್ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್ ರೂಬ್ರಿಕ್  
- ಟ್ರೇಸ್ JSON ರಫ್ತು (ಉದ್ದೇಶ → ಮಾದರಿ → ವಿಳಂಬ → ಟೋಕನ್ ಬಳಕೆ)  
- ಪುನರಾವರ್ತಿತ ಉಪಹಂತಗಳಿಗೆ ಕ್ಯಾಶ್ ಮರುಬಳಕೆ ಅನುಷ್ಠಾನಗೊಳಿಸಿ

### 5. Azure ಗೆ ವಿಸ್ತರಣೆ ಮಾರ್ಗ (5 ನಿಮಿಷ)

| ಪದರ | ಸ್ಥಳೀಯ (ಫೌಂಡ್ರಿ) | ಕ್ಲೌಡ್ (Azure AI Foundry) | ಪರಿವರ್ತನೆ ತಂತ್ರ |  
|-------|-----------------|--------------------------|---------------------|  
| ಮಾರ್ಗದರ್ಶನ | heuristic Python | ದೀರ್ಘಕಾಲಿಕ ಮೈಕ್ರೋಸರ್ವಿಸ್ | ಕಂಟೈನರೈಸ್ ಮಾಡಿ API ನಿಯೋಜಿಸಿ |  
| ಮಾದರಿಗಳು | SLM ಗಳು ಕ್ಯಾಶ್ ಮಾಡಲಾಗಿದೆ | ನಿರ್ವಹಿತ ನಿಯೋಜನೆಗಳು | ಸ್ಥಳೀಯ ಹೆಸರುಗಳನ್ನು ನಿಯೋಜನೆ ID ಗಳಿಗೆ ನಕ್ಷೆ ಮಾಡಿ |  
| ವೀಕ್ಷಣೆ | CLI ಅಂಕಿಅಂಶಗಳು/ಮ್ಯಾನುಯಲ್ | ಕೇಂದ್ರಿತ ಲಾಗಿಂಗ್ ಮತ್ತು ಮೆಟ್ರಿಕ್ಸ್ | ರಚನಾತ್ಮಕ ಟ್ರೇಸ್ ಘಟನೆಗಳನ್ನು ಸೇರಿಸಿ |  
| ಭದ್ರತೆ | ಸ್ಥಳೀಯ ಹೋಸ್ಟ್ ಮಾತ್ರ | Azure ಪ್ರಾಮಾಣೀಕರಣ / ನೆಟ್ವರ್ಕಿಂಗ್ | ರಹಸ್ಯಗಳಿಗಾಗಿ ಕೀ ವಾಲ್ಟ್ ಪರಿಚಯಿಸಿ |  
| ವೆಚ್ಚ | ಸಾಧನ ಸಂಪನ್ಮೂಲ | ಬಳಕೆ ಬಿಲ್ಲಿಂಗ್ | ಬಜೆಟ್ ಗಾರ್ಡ್‌ರೈಲ್ಸ್ ಸೇರಿಸಿ |

## ಮಾನ್ಯತೆ ಪರಿಶೀಲನಾ ಪಟ್ಟಿಕೆ

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
ಉದ್ದೇಶ ಆಧಾರಿತ ಮಾದರಿ ಆಯ್ಕೆ ಮತ್ತು ಅಂತಿಮ ಸುಧಾರಿತ ಔಟ್‌ಪುಟ್ ನಿರೀಕ್ಷಿಸಿ.

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

| ಸಮಸ್ಯೆ | ಕಾರಣ | ಪರಿಹಾರ |  
|---------|-------|-----|  
| ಎಲ್ಲಾ ಕಾರ್ಯಗಳು ಒಂದೇ ಮಾದರಿಗೆ ಮಾರ್ಗದರ್ಶಿತ | ದುರ್ಬಲ ನಿಯಮಗಳು | INTENT_RULES regex ಸೆಟ್ ಅನ್ನು ಶ್ರೀಮಂತಗೊಳಿಸಿ |  
| ಪೈಪ್ಲೈನ್ ಮಧ್ಯ ಹಂತದಲ್ಲಿ ವಿಫಲ | ಮಾದರಿ ಲೋಡ್ ಆಗಿಲ್ಲ | `foundry model run <model>` ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ |  
| ಕಡಿಮೆ ಔಟ್‌ಪುಟ್ ಸಮ್ಮಿಲನ | ಸುಧಾರಣಾ ಹಂತವಿಲ್ಲ | ಸಾರಾಂಶ/ಮಾನ್ಯತೆ ಹಂತ ಸೇರಿಸಿ |

## ಉಲ್ಲೇಖಗಳು

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry ಡಾಕ್ಯುಮೆಂಟೇಶನ್: https://learn.microsoft.com/azure/ai-foundry  
- ಪ್ರಾಂಪ್ಟ್ ಗುಣಮಟ್ಟ ಮಾದರಿಗಳು: ಸೆಷನ್ 2 ನೋಡಿ

---

**ಸೆಷನ್ ಅವಧಿ**: 30 ನಿಮಿಷ  
**ಕಷ್ಟದ ಮಟ್ಟ**: ಪರಿಣತಿ

## ಮಾದರಿ ದೃಶ್ಯ ಮತ್ತು ಕಾರ್ಯಾಗಾರ ನಕ್ಷೆ

| ಕಾರ್ಯಾಗಾರ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು / ನೋಟ್ಬುಕ್‌ಗಳು | ದೃಶ್ಯ | ಉದ್ದೇಶ | ಡೇಟಾಸೆಟ್ / ಕ್ಯಾಟಲಾಗ್ ಮೂಲ |  
|------------------------------|----------|-----------|---------------------------|  
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ಮಿಶ್ರ ಉದ್ದೇಶ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಡೆವಲಪರ್ ಸಹಾಯಕ (ಪುನರ್‌ರಚನೆ, ಸಾರಾಂಶ, ವರ್ಗೀಕರಣ) | heuristic ಉದ್ದೇಶ → ಮಾದರಿ_ALIAS ಮಾರ್ಗದರ್ಶನ ಟೋಕನ್ ಬಳಕೆಯೊಂದಿಗೆ | ಇನ್‌ಲೈನ್ `CATALOG` + regex `RULES` |  
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | ಸಂಕೀರ್ಣ ಕೋಡಿಂಗ್ ಸಹಾಯ ಕಾರ್ಯಕ್ಕಾಗಿ ಬಹು ಹಂತದ ಯೋಜನೆ ಮತ್ತು ಸುಧಾರಣೆ | ವಿಭಜನೆ → ವಿಶೇಷ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ → ಸಾರಾಂಶ ಸುಧಾರಣೆ ಹಂತ | ಅದೇ `CATALOG`; ಹಂತಗಳು ಯೋಜನೆ ಔಟ್‌ಪುಟ್‌ನಿಂದ ಪಡೆದವು |

### ದೃಶ್ಯ ಕಥನ  
ಒಂದು ಎಂಜಿನಿಯರಿಂಗ್ ಉತ್ಪಾದಕತೆ ಉಪಕರಣವು ವಿಭಿನ್ನ ಕಾರ್ಯಗಳನ್ನು ಸ್ವೀಕರಿಸುತ್ತದೆ: ಕೋಡ್ ಪುನರ್‌ರಚನೆ, ವಾಸ್ತುಶಿಲ್ಪ ಟಿಪ್ಪಣಿಗಳ ಸಾರಾಂಶ, ಪ್ರತಿಕ್ರಿಯೆ ವರ್ಗೀಕರಣ. ವಿಳಂಬ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಬಳಕೆಯನ್ನು ಕಡಿಮೆ ಮಾಡಲು, ಒಂದು ಸಣ್ಣ ಸಾಮಾನ್ಯ ಮಾದರಿ ಯೋಜನೆ ಮಾಡುತ್ತದೆ ಮತ್ತು ಸಾರಾಂಶ ನೀಡುತ್ತದೆ, ಒಂದು ಕೋಡ್-ವಿಶೇಷ ಮಾದರಿ ಪುನರ್‌ರಚನೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ಒಂದು ಲಘು ತೂಕದ ವರ್ಗೀಕರಣ ಸಾಮರ್ಥ್ಯವಿರುವ ಮಾದರಿ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಲೇಬಲ್ ಮಾಡುತ್ತದೆ. ಪೈಪ್ಲೈನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಸರಪಳಿಯನ್ನು ಮತ್ತು ಸುಧಾರಣೆಯನ್ನು ತೋರಿಸುತ್ತದೆ; ರೌಟರ್ ಸ್ಕ್ರಿಪ್ಟ್ ಹೊಂದಿಕೊಳ್ಳುವ ಏಕ-ಪ್ರಾಂಪ್ಟ್ ಮಾರ್ಗದರ್ಶನವನ್ನು ವಿಭಜಿಸುತ್ತದೆ.

### ಕ್ಯಾಟಲಾಗ್ ಸ্ন್ಯಾಪ್‌ಶಾಟ್  
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  
### ಉದಾಹರಣಾ ಪರೀಕ್ಷಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳು  
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  
### ಟ್ರೇಸ್ ವಿಸ್ತರಣೆ (ಐಚ್ಛಿಕ)  
`models_pipeline.py` ಗೆ ಪ್ರತಿ ಹಂತದ ಟ್ರೇಸ್ JSON ಸಾಲುಗಳನ್ನು ಸೇರಿಸಿ:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  
### ಏರಿಕೆ heuristic (ಕಲ್ಪನೆ)  
ಯೋಜನೆಯಲ್ಲಿ "optimize", "security" ಎಂಬ ಕೀವರ್ಡ್‌ಗಳು ಅಥವಾ ಹಂತದ ಉದ್ದ 280 ಅಕ್ಷರಗಳಿಗಿಂತ ಹೆಚ್ಚು ಇದ್ದರೆ → ಆ ಹಂತಕ್ಕೆ ಮಾತ್ರ ದೊಡ್ಡ ಮಾದರಿ (ಉದಾ., `gpt-oss-20b`) ಗೆ ಏರಿಕೆ ಮಾಡಿ.

### ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳು

| ಕ್ಷೇತ್ರ | ಸುಧಾರಣೆ | ಮೌಲ್ಯ | ಸೂಚನೆ |  
|------|-------------|-------|------|  
| ಕ್ಯಾಶಿಂಗ್ | ಮ್ಯಾನೇಜರ್ + ಕ್ಲೈಂಟ್ ವಸ್ತುಗಳ ಮರುಬಳಕೆ | ಕಡಿಮೆ ವಿಳಂಬ, ಕಡಿಮೆ ಓವರ್‌ಹೆಡ್ | `workshop_utils.get_client` ಬಳಸಿ |  
| ಬಳಕೆ ಮೆಟ್ರಿಕ್ಸ್ | ಟೋಕನ್‌ಗಳು ಮತ್ತು ಪ್ರತಿ ಹಂತದ ವಿಳಂಬವನ್ನು ಸೆರೆಹಿಡಿಯುವುದು | ಪ್ರೊಫೈಲಿಂಗ್ ಮತ್ತು ಆಪ್ಟಿಮೈಜೆಷನ್ | ಪ್ರತಿ ಮಾರ್ಗದರ್ಶಿತ ಕರೆ ಸಮಯ; ಟ್ರೇಸ್ ಪಟ್ಟಿಯಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ |  
| ಹೊಂದಿಕೊಳ್ಳುವ ಮಾರ್ಗದರ್ಶನ | ವಿಶ್ವಾಸ / ವೆಚ್ಚ ಜಾಗೃತಿ | ಉತ್ತಮ ಗುಣಮಟ್ಟ-ವೆಚ್ಚ ಸಮತೋಲನ | ಅಂಕಗಳನ್ನು ಸೇರಿಸಿ: ಪ್ರಾಂಪ್ಟ್ > N ಅಕ್ಷರಗಳು ಅಥವಾ regex ಡೊಮೇನ್ ಹೊಂದಿದ್ದರೆ → ದೊಡ್ಡ ಮಾದರಿಗೆ ಏರಿಕೆ |  
| ಡೈನಾಮಿಕ್ ಸಾಮರ್ಥ್ಯ ರಿಜಿಸ್ಟ್ರಿ | ಹಾಟ್ ರಿಲೋಡ್ ಕ್ಯಾಟಲಾಗ್ | ಮರುಪ್ರಾರಂಭವಿಲ್ಲದೆ ಪುನರ್ ನಿಯೋಜನೆ | ರನ್‌ಟೈಮ್‌ನಲ್ಲಿ `catalog.json` ಲೋಡ್ ಮಾಡಿ; ಫೈಲ್ ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್ ವೀಕ್ಷಿಸಿ |  
| ಫಾಲ್ಬ್ಯಾಕ್ ತಂತ್ರ | ವೈಫಲ್ಯಗಳ ಸಂದರ್ಭದಲ್ಲಿ ದೃಢತೆ | ಹೆಚ್ಚಿನ ಲಭ್ಯತೆ | ಪ್ರಾಥಮಿಕ ಪ್ರಯತ್ನಿಸಿ → ಅಪವಾದದಲ್ಲಿ ಫಾಲ್ಬ್ಯಾಕ್_ALIAS |  
| ಸ್ಟ್ರೀಮಿಂಗ್ ಪೈಪ್ಲೈನ್ | ಮೊದಲಿನ ಪ್ರತಿಕ್ರಿಯೆ | ಬಳಕೆದಾರ ಅನುಭವ ಸುಧಾರಣೆ | ಪ್ರತಿ ಹಂತವನ್ನು ಸ್ಟ್ರೀಮ್ ಮಾಡಿ ಮತ್ತು ಅಂತಿಮ ಸುಧಾರಿತ ಇನ್‌ಪುಟ್ ಬಫರ್ ಮಾಡಿ |  
| ವೆಕ್ಟರ್ ಉದ್ದೇಶ ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳು | ಹೆಚ್ಚು ಸೂಕ್ಷ್ಮ ಮಾರ್ಗದರ್ಶನ | ಹೆಚ್ಚಿನ ಉದ್ದೇಶ ನಿಖರತೆ | ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಎಂಬೆಡ್ ಮಾಡಿ, ಕ್ಲಸ್ಟರ್ ಮಾಡಿ ಮತ್ತು ಸೆಂಟ್ರಾಯ್ಡ್ ನಕ್ಷೆ ಮಾಡಿ → ಸಾಮರ್ಥ್ಯ |  
| ಟ್ರೇಸ್ ರಫ್ತು | ಪರಿಶೀಲನೀಯ ಸರಪಳಿ | ಅನುಕೂಲತೆ/ವರದಿ | JSON ಸಾಲುಗಳನ್ನು ಹೊರತುಪಡಿಸಿ: ಹಂತ, ಉದ್ದೇಶ, ಮಾದರಿ, ವಿಳಂಬ_ms, ಟೋಕನ್ಸ್ |  
| ವೆಚ್ಚ ಅನುಕರಣ | ಕ್ಲೌಡ್ ಮುಂಚಿತ ಅಂದಾಜು | ಬಜೆಟ್ ಯೋಜನೆ | ಮಾದರಿ ಪ್ರತಿ ಟೋಕನ್ ನೋಟನಲ್ ವೆಚ್ಚವನ್ನು ನಿಯೋಜಿಸಿ ಮತ್ತು ಕಾರ್ಯಕ್ಕೆ ಒಟ್ಟು ಮಾಡಿ |  
| ನಿರ್ಧಾರಾತ್ಮಕ ಮೋಡ್ | ಪುನರಾವರ್ತನೆ ಸಾಧ್ಯತೆ | ಸ್ಥಿರ ಬೆಂಚ್ಮಾರ್ಕಿಂಗ್ | ಪರಿಸರ: `temperature=0`, ನಿಶ್ಚಿತ ಹಂತಗಳ ಸಂಖ್ಯೆ |

#### ಟ್ರೇಸ್ ರಚನೆ ಉದಾಹರಣೆ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  
#### ಹೊಂದಿಕೊಳ್ಳುವ ಏರಿಕೆ ರೇಖಾಚಿತ್ರ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # ಲಭ್ಯವಿದ್ದರೆ ದೊಡ್ಡ ತರ್ಕ ಮಾದರಿಗೆ ಏರಿಕೆ ಮಾಡಿ
    alias = 'gpt-oss-20b'
```
  
#### ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್ ಹಾಟ್ ರಿಲೋಡ್

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
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->