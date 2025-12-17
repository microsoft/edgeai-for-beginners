<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-12-15T20:41:16+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ml"
}
-->
# സെഷൻ 6: ഫൗണ്ട്രി ലോക്കൽ – മോഡലുകൾ ടൂളുകളായി

## സംഗ്രഹം

മോഡലുകളെ ഒരു ലോക്കൽ AI ഓപ്പറേറ്റിംഗ് ലെയറിനുള്ളിൽ സംയോജ്യമായ ടൂളുകളായി പരിഗണിക്കുക. ഈ സെഷൻ എങ്ങനെ നിരവധി പ്രത്യേക SLM/LLM കോൾസ് ചൈനിൽ ബന്ധിപ്പിക്കാമെന്ന്, തിരഞ്ഞെടുക്കപ്പെട്ട ടാസ്കുകൾ റൂട്ടുചെയ്യാമെന്ന്, ആപ്ലിക്കേഷനുകൾക്ക് ഏകീകൃത SDK സര്ഫേസ് എങ്ങനെ പ്രദർശിപ്പിക്കാമെന്ന് കാണിക്കുന്നു. നിങ്ങൾ ഒരു ലഘുവായ മോഡൽ റൂട്ടർ + ടാസ്‌ക് പ്ലാനർ നിർമ്മിച്ച്, അത് ഒരു ആപ്പ് സ്ക്രിപ്റ്റിൽ സംയോജിപ്പിച്ച്, പ്രൊഡക്ഷൻ വർക്ക്‌ലോഡുകൾക്കായി Azure AI Foundry-യിലേക്ക് സ്കെയിലിംഗ് പാതയുടെ രൂപരേഖ തയ്യാറാക്കും.

## പഠന ലക്ഷ്യങ്ങൾ

- **സങ്കൽപ്പിക്കുക** മോഡലുകളെ പ്രഖ്യാപിച്ച ശേഷികളുള്ള ആറ്റോമിക് ടൂളുകളായി
- **റൂട്ടുചെയ്യുക** അഭ്യർത്ഥനകൾ ഉദ്ദേശ്യവും ഹ്യൂറിസ്റ്റിക് സ്കോറിംഗും അടിസ്ഥാനമാക്കി
- **ചെയിൻ** ഔട്ട്പുട്ടുകൾ മൾട്ടി-സ്റ്റെപ്പ് ടാസ്കുകളിൽ (വിഭജിക്കുക → പരിഹരിക്കുക → മെച്ചപ്പെടുത്തുക)
- **സംയോജിപ്പിക്കുക** താഴെനിന്നുള്ള ആപ്ലിക്കേഷനുകൾക്കായി ഏകീകൃത ക്ലയന്റ് API
- **സ്കെയിൽ** ഡിസൈൻ ക്ലൗഡിലേക്ക് (ഒരേ OpenAI-സമാന കരാർ)

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- സെഷനുകൾ 1–5 പൂർത്തിയായി
- നിരവധി ലോക്കൽ മോഡലുകൾ കാഷ് ചെയ്തിട്ടുണ്ട് (ഉദാ., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ക്രോസ്-പ്ലാറ്റ്ഫോം പരിസ്ഥിതി സ്നിപ്പറ്റ്

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
  
macOS-ൽ നിന്ന് റിമോട്ട്/VM സർവീസ് ആക്‌സസ്:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ഡെമോ ഫ്ലോ (30 മിനിറ്റ്)

### 1. ടൂൾ ശേഷി പ്രഖ്യാപനം (5 മിനിറ്റ്)

`samples/06-tools/models_catalog.py` സൃഷ്ടിക്കുക:  

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
  
### 2. ഉദ്ദേശ്യ കണ്ടെത്തൽ & റൂട്ടിംഗ് (8 മിനിറ്റ്)

`samples/06-tools/router.py` സൃഷ്ടിക്കുക:  

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
    # സ്കോർ കാറ്റലോഗ്: കഴിവ് പൊരുത്തം ആദ്യം, പിന്നീട് മുൻഗണന
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # ക്രമീകരിക്കുക: പൊരുത്തം സത്യം ആദ്യം, പിന്നീട് ഏറ്റവും കുറഞ്ഞ മുൻഗണന മൂല്യം
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
  
### 3. മൾട്ടി-സ്റ്റെപ്പ് ടാസ്‌ക് ചെയിനിംഗ് (7 മിനിറ്റ്)

`samples/06-tools/pipeline.py` സൃഷ്ടിക്കുക:  

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
  
### 4. സ്റ്റാർട്ടർ പ്രോജക്ട്: `06-models-as-tools` അനുയോജിപ്പിക്കുക (5 മിനിറ്റ്)

ഉന്നതീകരണങ്ങൾ:  
- സ്ട്രീമിംഗ് ടോക്കൺ പിന്തുണ ചേർക്കുക (പ്രോഗ്രസീവ് UI അപ്ഡേറ്റ്)  
- ആത്മവിശ്വാസ സ്കോറിംഗ് ചേർക്കുക: ലെക്സിക്കൽ ഓവർലാപ്പ് അല്ലെങ്കിൽ പ്രോംപ്റ്റ് റൂബ്രിക്  
- ട്രേസ് JSON എക്സ്പോർട്ട് ചെയ്യുക (ഉദ്ദേശ്യം → മോഡൽ → ലാറ്റൻസി → ടോക്കൺ ഉപയോഗം)  
- ആവർത്തിക്കുന്ന ഉപപടികൾക്കായി കാഷ് പുനരുപയോഗം നടപ്പിലാക്കുക  

### 5. Azure-യിലേക്ക് സ്കെയിലിംഗ് പാത (5 മിനിറ്റ്)

| ലെയർ | ലോക്കൽ (ഫൗണ്ട്രി) | ക്ലൗഡ് (Azure AI Foundry) | ട്രാൻസിഷൻ തന്ത്രം |
|-------|-----------------|--------------------------|---------------------|
| റൂട്ടിംഗ് | ഹ്യൂറിസ്റ്റിക് പൈതൺ | ദൈർഘ്യമുള്ള മൈക്രോസർവീസ് | കണ്ടെയ്‌നറൈസ് ചെയ്ത് API ഡിപ്ലോയ് ചെയ്യുക |
| മോഡലുകൾ | SLM കാഷ് ചെയ്തത് | മാനേജ്ഡ് ഡിപ്ലോയ്മെന്റുകൾ | ലോക്കൽ നാമങ്ങൾ ഡിപ്ലോയ്മെന്റ് ഐഡികളിലേക്ക് മാപ്പ് ചെയ്യുക |
| നിരീക്ഷണം | CLI സ്റ്റാറ്റ്സ്/മാനുവൽ | സെൻട്രൽ ലോഗിംഗ് & മെട്രിക്‌സ് | ഘടനാപരമായ ട്രേസ് ഇവന്റുകൾ ചേർക്കുക |
| സുരക്ഷ | ലോക്കൽ ഹോസ്റ്റ് മാത്രം | Azure ഓത്ത് / നെറ്റ്‌വർക്കിംഗ് | രഹസ്യങ്ങൾക്കായി കീ വാൾട്ട് പരിചയപ്പെടുത്തുക |
| ചെലവ് | ഉപകരണം വിഭവം | ഉപഭോഗ ബില്ലിംഗ് | ബജറ്റ് ഗാർഡ്‌റെയിൽസ് ചേർക്കുക |

## സാധുത പരിശോധന പട്ടിക

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
ഉദ്ദേശ്യ അടിസ്ഥാനമാക്കിയ മോഡൽ തിരഞ്ഞെടുപ്പും അന്തിമ മെച്ചപ്പെടുത്തിയ ഔട്ട്പുട്ടും പ്രതീക്ഷിക്കുക.

## പ്രശ്നപരിഹാരം

| പ്രശ്നം | കാരണം | പരിഹാരം |
|---------|-------|-----|
| എല്ലാ ടാസ്കുകളും ഒരേ മോഡലിലേക്ക് റൂട്ടുചെയ്യുന്നു | ദുർബലമായ നിയമങ്ങൾ | INTENT_RULES regex സെറ്റ് സമ്പന്നമാക്കുക |
| പൈപ്പ്‌ലൈൻ മധ്യത്തിൽ പരാജയപ്പെടുന്നു | മോഡൽ ലോഡ് ചെയ്തിട്ടില്ല | `foundry model run <model>` ഓടിക്കുക |
| ഔട്ട്പുട്ട് ഏകോപനം കുറവ് | മെച്ചപ്പെടുത്തൽ ഘട്ടം ഇല്ല | സംഗ്രഹം/സാധുത പരിശോധന പാസ് ചേർക്കുക |

## റഫറൻസുകൾ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry ഡോക്യുമെന്റേഷൻ: https://learn.microsoft.com/azure/ai-foundry  
- പ്രോംപ്റ്റ് ഗുണനിലവാര മാതൃകകൾ: സെഷൻ 2 കാണുക  

---

**സെഷൻ ദൈർഘ്യം**: 30 മിനിറ്റ്  
**പ്രയാസം**: വിദഗ്ധൻ

## സാമ്പിൾ സീനാരിയോ & വർക്ക്‌ഷോപ്പ് മാപ്പിംഗ്

| വർക്ക്‌ഷോപ്പ് സ്ക്രിപ്റ്റുകൾ / നോട്ട്‌ബുക്കുകൾ | സീനാരിയോ | ലക്ഷ്യം | ഡാറ്റാസെറ്റ് / കാറ്റലോഗ് ഉറവിടം |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | മിശ്രിത ഉദ്ദേശ്യ പ്രോംപ്റ്റുകൾ കൈകാര്യം ചെയ്യുന്ന ഡെവലപ്പർ അസിസ്റ്റന്റ് (പുനഃസംഘടനം, സംഗ്രഹം, വർഗ്ഗീകരണം) | ഹ്യൂറിസ്റ്റിക് ഉദ്ദേശ്യം → മോഡൽ അലിയാസ് റൂട്ടിംഗ് ടോക്കൺ ഉപയോഗത്തോടെ | ഇൻലൈൻ `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | സങ്കീർണ്ണ കോഡിംഗ് സഹായ ടാസ്കിനായി മൾട്ടി-സ്റ്റെപ്പ് പ്ലാനിംഗ് & മെച്ചപ്പെടുത്തൽ | വിഭജിക്കുക → പ്രത്യേക നിർവഹണം → സംഗ്രഹം മെച്ചപ്പെടുത്തൽ ഘട്ടം | ഒരേ `CATALOG`; പ്ലാൻ ഔട്ട്പുട്ടിൽ നിന്നുള്ള ഘട്ടങ്ങൾ |

### സീനാരിയോ വിവരണം  
ഒരു എഞ്ചിനീയറിംഗ് ഉൽപാദകത്വ ടൂൾ വ്യത്യസ്ത ടാസ്കുകൾ സ്വീകരിക്കുന്നു: കോഡ് പുനഃസംഘടനം, ആർക്കിടെക്ചറൽ കുറിപ്പുകൾ സംഗ്രഹിക്കൽ, ഫീഡ്ബാക്ക് വർഗ്ഗീകരണം. ലാറ്റൻസി & വിഭവ ഉപയോഗം കുറയ്ക്കാൻ, ഒരു ചെറിയ ജനറൽ മോഡൽ പ്ലാൻ ചെയ്ത് സംഗ്രഹിക്കുന്നു, കോഡ്-പ്രത്യേക മോഡൽ പുനഃസംഘടനം കൈകാര്യം ചെയ്യുന്നു, ലഘുവായ വർഗ്ഗീകരണ ശേഷിയുള്ള മോഡൽ ഫീഡ്ബാക്ക് ലേബൽ ചെയ്യുന്നു. പൈപ്പ്‌ലൈൻ സ്ക്രിപ്റ്റ് ചെയിനിംഗ് + മെച്ചപ്പെടുത്തൽ കാണിക്കുന്നു; റൂട്ടർ സ്ക്രിപ്റ്റ് അനുകൂലമായ സിംഗിൾ-പ്രോംപ്റ്റ് റൂട്ടിംഗ് വേർതിരിക്കുന്നു.

### കാറ്റലോഗ് സ്നാപ്ഷോട്ട്  
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  
### ഉദാഹരണ ടെസ്റ്റ് പ്രോംപ്റ്റുകൾ  
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  
### ട്രേസ് വിപുലീകരണം (ഐച്ഛികം)  
`models_pipeline.py`-ക്കായി ഓരോ ഘട്ടത്തിനും ട്രേസ് JSON ലൈനുകൾ ചേർക്കുക:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  
### ഉയർത്തൽ ഹ്യൂറിസ്റ്റിക് (ആലോചന)  
പ്ലാനിൽ "optimize", "security" പോലുള്ള കീവേഡുകൾ ഉണ്ടെങ്കിൽ അല്ലെങ്കിൽ ഘട്ടം 280 അക്ഷരങ്ങൾക്കു മുകളിൽ ആണെങ്കിൽ → ആ ഘട്ടത്തിന് മാത്രം വലിയ മോഡലിലേക്ക് (ഉദാ., `gpt-oss-20b`) ഉയർത്തുക.

### ഐച്ഛിക ഉന്നതീകരണങ്ങൾ

| മേഖല | ഉന്നതീകരണം | മൂല്യം | സൂചന |
|------|-------------|-------|------|
| കാഷിംഗ് | മാനേജർ + ക്ലയന്റ് ഒബ്ജക്റ്റുകൾ പുനരുപയോഗം | കുറഞ്ഞ ലാറ്റൻസി, കുറവ് ഓവർഹെഡ് | `workshop_utils.get_client` ഉപയോഗിക്കുക |
| ഉപയോഗ മെട്രിക്‌സ് | ടോക്കണുകളും ഘട്ടംപ്രതി ലാറ്റൻസിയും പിടിക്കുക | പ്രൊഫൈലിംഗ് & ഓപ്റ്റിമൈസേഷൻ | ഓരോ റൂട്ടുചെയ്യപ്പെട്ട കോൾ സമയമിടുക; ട്രേസ് ലിസ്റ്റിൽ സൂക്ഷിക്കുക |
| അനുകൂല റൂട്ടിംഗ് | ആത്മവിശ്വാസം / ചെലവ് ബോധമുള്ളത് | മെച്ചപ്പെട്ട ഗുണനിലവാര-ചെലവ് തുല്യനിലവ് | സ്കോറിംഗ് ചേർക്കുക: പ്രോംപ്റ്റ് N അക്ഷരങ്ങൾക്കു മുകളിൽ ആണെങ്കിൽ അല്ലെങ്കിൽ regex ഡൊമെയ്ൻ പൊരുത്തപ്പെടുന്നുവെങ്കിൽ → വലിയ മോഡലിലേക്ക് ഉയർത്തുക |
| ഡൈനാമിക് ശേഷി രജിസ്ട്രി | ഹോട്ട് റീലോഡ് കാറ്റലോഗ് | റീസ്റ്റാർട്ട് / റിഡിപ്ലോയ് ആവശ്യമില്ല | റൺടൈമിൽ `catalog.json` ലോഡ് ചെയ്യുക; ഫയൽ ടൈംസ്റ്റാമ്പ് നിരീക്ഷിക്കുക |
| ഫാൾബാക്ക് തന്ത്രം | പരാജയങ്ങളിൽ ശക്തി | ഉയർന്ന ലഭ്യത | പ്രാഥമികം ശ്രമിക്കുക → എക്സെപ്ഷൻ വന്നാൽ ഫാൾബാക്ക് അലിയാസ് |
| സ്ട്രീമിംഗ് പൈപ്പ്‌ലൈൻ | പ്രാരംഭ ഫീഡ്ബാക്ക് | UX മെച്ചപ്പെടുത്തൽ | ഓരോ ഘട്ടവും സ്ട്രീം ചെയ്ത് അന്തിമ മെച്ചപ്പെടുത്തൽ ഇൻപുട്ട് ബഫർ ചെയ്യുക |
| വെക്ടർ ഉദ്ദേശ്യ എംബെഡ്ഡിംഗുകൾ | കൂടുതൽ സൂക്ഷ്മ റൂട്ടിംഗ് | ഉയർന്ന ഉദ്ദേശ്യ കൃത്യത | പ്രോംപ്റ്റ് എംബെഡ് ചെയ്ത് ക്ലസ്റ്റർ ചെയ്ത് സെൻട്രോയിഡ് → ശേഷി മാപ്പ് ചെയ്യുക |
| ട്രേസ് എക്സ്പോർട്ട് | ഓഡിറ്റബിൾ ചെയിൻ | അനുസരണ/റിപ്പോർട്ടിംഗ് | JSON ലൈനുകൾ പുറപ്പെടുവിക്കുക: ഘട്ടം, ഉദ്ദേശ്യം, മോഡൽ, ലാറ്റൻസി_ms, ടോക്കണുകൾ |
| ചെലവ് സിമുലേഷൻ | ക്ലൗഡിന് മുമ്പുള്ള കണക്കുകൂട്ടൽ | ബജറ്റ് പ്ലാനിംഗ് | മോഡൽപ്രതി നോട്ടീഷ്യൽ ചെലവ്/ടോക്കൺ നിശ്ചയിച്ച് ടാസ്ക് പ്രതി കൂട്ടിച്ചേർക്കുക |
| നിർണ്ണായക മോഡ് | പുനരുത്പാദനക്ഷമത | സ്ഥിരമായ ബെഞ്ച്മാർക്കിംഗ് | പരിസ്ഥിതി: `temperature=0`, നിശ്ചിത ഘട്ടങ്ങൾ എണ്ണം |

#### ട്രേസ് ഘടന ഉദാഹരണം

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  
#### അനുകൂല ഉയർത്തൽ സ്കെച്ച്

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # ലഭ്യമായെങ്കിൽ വലിയ കാരണമാറ്റ് മോഡലിലേക്ക് ഉയർത്തുക
    alias = 'gpt-oss-20b'
```
  
#### മോഡൽ കാറ്റലോഗ് ഹോട്ട് റീലോഡ്

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
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->