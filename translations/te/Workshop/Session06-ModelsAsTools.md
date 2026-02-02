# సెషన్ 6: ఫౌండ్రీ లోకల్ – మోడల్స్ టూల్స్‌గా

## సారాంశం

లోకల్ AI ఆపరేటింగ్ లేయర్‌లో మోడల్స్‌ను కంపోజబుల్ టూల్స్‌గా పరిగణించండి. ఈ సెషన్‌లో మీరు అనేక ప్రత్యేక SLM/LLM కాల్స్‌ను చైన్ చేయడం, టాస్క్‌లను ఎంపికగా రూట్ చేయడం, మరియు యాప్లికేషన్లకు ఏకీకృత SDK సర్ఫేస్‌ను ప్రదర్శించడం ఎలా చేయాలో చూపిస్తుంది. మీరు ఒక లైట్‌వెయిట్ మోడల్ రౌటర్ + టాస్క్ ప్లానర్‌ను నిర్మించి, దాన్ని యాప్ స్క్రిప్ట్‌లో ఇంటిగ్రేట్ చేసి, Azure AI Foundryకి ప్రొడక్షన్ వర్క్‌లోడ్స్ కోసం స్కేలింగ్ మార్గాన్ని వివరించబోతున్నారు.

## నేర్చుకునే లక్ష్యాలు

- **ఆలోచించండి** మోడల్స్‌ను ప్రకటించిన సామర్థ్యాలతో అటామిక్ టూల్స్‌గా
- **రూట్ చేయండి** అభిప్రాయం / హ్యూరిస్టిక్ స్కోరింగ్ ఆధారంగా అభ్యర్థనలను
- **చైన్ చేయండి** బహుళ దశల టాస్క్‌లలో అవుట్పుట్‌లు (విభజించు → పరిష్కరించు → మెరుగుపరచు)
- **ఇంటిగ్రేట్ చేయండి** దిగువ యాప్లికేషన్ల కోసం ఏకీకృత క్లయింట్ API
- **స్కేల్ చేయండి** క్లౌడ్‌కు డిజైన్ (అదే OpenAI-అనుకూల ఒప్పందం)

## ముందస్తు అవసరాలు

- సెషన్లు 1–5 పూర్తి చేయబడినవి
- అనేక లోకల్ మోడల్స్ క్యాష్ చేయబడ్డాయి (ఉదా: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### క్రాస్-ప్లాట్‌ఫారమ్ ఎన్విరాన్‌మెంట్ స్నిపెట్

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
  
macOS నుండి Remote/VM సర్వీస్ యాక్సెస్:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## డెమో ఫ్లో (30 నిమిషాలు)

### 1. టూల్ సామర్థ్య ప్రకటన (5 నిమిషాలు)

`samples/06-tools/models_catalog.py` సృష్టించండి:

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
  
### 2. అభిప్రాయం గుర్తింపు & రూటింగ్ (8 నిమిషాలు)

`samples/06-tools/router.py` సృష్టించండి:

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
    # స్కోర్ క్యాటలాగ్: మొదట సామర్థ్య సరిపోలిక, ఆపై ప్రాధాన్యత
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # సార్టు: మొదట True సరిపోలిక, ఆపై తక్కువ ప్రాధాన్యత విలువ
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
  
### 3. బహుళ దశల టాస్క్ చైనింగ్ (7 నిమిషాలు)

`samples/06-tools/pipeline.py` సృష్టించండి:

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
  
### 4. స్టార్టర్ ప్రాజెక్ట్: `06-models-as-tools` అనుకూలీకరణ (5 నిమిషాలు)

పరిష్కారాలు:  
- స్ట్రీమింగ్ టోకెన్ మద్దతు జోడించండి (ప్రోగ్రెసివ్ UI అప్‌డేట్)  
- విశ్వాస స్కోరింగ్ జోడించండి: లెక్సికల్ ఓవర్‌లాప్ లేదా ప్రాంప్ట్ రూబ్రిక్  
- ట్రేస్ JSON ఎగుమతి (అభిప్రాయం → మోడల్ → లేటెన్సీ → టోకెన్ వినియోగం)  
- పునరావృత ఉపదశల కోసం క్యాష్ పునర్వినియోగం అమలు చేయండి  

### 5. Azureకి స్కేలింగ్ మార్గం (5 నిమిషాలు)

| లేయర్ | లోకల్ (ఫౌండ్రీ) | క్లౌడ్ (Azure AI Foundry) | మార్పిడి వ్యూహం |
|-------|-----------------|--------------------------|---------------------|
| రూటింగ్ | హ్యూరిస్టిక్ పైథాన్ | డ్యూరబుల్ మైక్రోసర్వీస్ | కంటైనరైజ్ చేసి APIని డిప్లాయ్ చేయండి |
| మోడల్స్ | క్యాష్ చేసిన SLMలు | నిర్వహించబడే డిప్లాయ్‌మెంట్లు | లోకల్ పేర్లను డిప్లాయ్‌మెంట్ IDsకి మ్యాప్ చేయండి |
| ఆబ్జర్వబిలిటీ | CLI గణాంకాలు/మాన్యువల్ | సెంట్రల్ లాగింగ్ & మెట్రిక్స్ | నిర్మిత ట్రేస్ ఈవెంట్స్ జోడించండి |
| భద్రత | లోకల్ హోస్ట్ మాత్రమే | Azure ఆథ్ / నెట్‌వర్కింగ్ | సీక్రెట్స్ కోసం కీ వాల్ట్ ప్రవేశపెట్టండి |
| ఖర్చు | డివైస్ వనరు | వినియోగ బిల్లింగ్ | బడ్జెట్ గార్డ్రెయిల్స్ జోడించండి |

## ధృవీకరణ చెక్లిస్ట్

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
అభిప్రాయం ఆధారిత మోడల్ ఎంపిక మరియు తుది మెరుగైన అవుట్పుట్ ఆశించండి.

## సమస్య పరిష్కారం

| సమస్య | కారణం | పరిష్కారం |
|---------|-------|-----|
| అన్ని టాస్క్‌లు ఒకే మోడల్‌కు రూట్ అవుతున్నాయి | బలహీన నియమాలు | INTENT_RULES regex సెట్‌ను సమృద్ధి పరచండి |
| పైప్‌లైన్ మధ్య దశలో విఫలమవుతుంది | మోడల్ లోడ్ కాలేదు | `foundry model run <model>` ను నడపండి |
| తక్కువ అవుట్పుట్ సమగ్రత | మెరుగుదల దశ లేదు | సారాంశం/ధృవీకరణ దశ జోడించండి |

## సూచనలు

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry డాక్స్: https://learn.microsoft.com/azure/ai-foundry  
- ప్రాంప్ట్ క్వాలిటీ ప్యాటర్న్స్: సెషన్ 2 చూడండి

---

**సెషన్ వ్యవధి**: 30 నిమిషాలు  
**కష్టత**: నిపుణుడు

## నమూనా సన్నివేశం & వర్క్‌షాప్ మ్యాపింగ్

| వర్క్‌షాప్ స్క్రిప్ట్స్ / నోట్‌బుక్స్ | సన్నివేశం | లక్ష్యం | డేటాసెట్ / క్యాటలాగ్ మూలం |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | మిక్స్ చేసిన అభిప్రాయం ప్రాంప్ట్‌లను నిర్వహించే డెవలపర్ అసిస్టెంట్ (రిఫాక్టర్, సారాంశం, వర్గీకరణ) | హ్యూరిస్టిక్ అభిప్రాయం → మోడల్ అలియాస్ రూటింగ్ టోకెన్ వినియోగంతో | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | సంక్లిష్ట కోడింగ్ సహాయం టాస్క్ కోసం బహుళ దశల ప్లానింగ్ & మెరుగుదల | విభజన → ప్రత్యేక అమలు → సారాంశ మెరుగుదల దశ | అదే `CATALOG`; ప్లాన్ అవుట్పుట్ నుండి దశలు పొందబడినవి |

### సన్నివేశ కథనం  
ఇంజనీరింగ్ ఉత్పాదకత టూల్ వివిధ రకాల టాస్క్‌లను అందుకుంటుంది: కోడ్ రిఫాక్టర్ చేయడం, ఆర్కిటెక్చరల్ నోట్స్ సారాంశం, ఫీడ్‌బ్యాక్ వర్గీకరణ. ఆలస్యం & వనరు వినియోగాన్ని తగ్గించడానికి, ఒక చిన్న సాధారణ మోడల్ ప్లాన్ చేసి సారాంశం చేస్తుంది, కోడ్-ప్రత్యేక మోడల్ రిఫాక్టరింగ్ నిర్వహిస్తుంది, మరియు ఒక లైట్‌వెయిట్ వర్గీకరణ సామర్థ్యంతో మోడల్ ఫీడ్‌బ్యాక్‌ను లేబుల్ చేస్తుంది. పైప్‌లైన్ స్క్రిప్ట్ చైనింగ్ + మెరుగుదల చూపిస్తుంది; రౌటర్ స్క్రిప్ట్ అనుకూల సింగిల్-ప్రాంప్ట్ రూటింగ్‌ను వేరుచేస్తుంది.

### క్యాటలాగ్ స్నాప్‌షాట్  
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  
### ఉదాహరణ పరీక్ష ప్రాంప్ట్‌లు  
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  
### ట్రేస్ విస్తరణ (ఐచ్ఛికం)  
`models_pipeline.py` కోసం ప్రతి దశ ట్రేస్ JSON లైన్లు జోడించండి:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  
### ఎస్కలేషన్ హ్యూరిస్టిక్ (ఆలోచన)  
ప్లాన్‌లో "optimize", "security" వంటి కీవర్డ్స్ లేదా దశ పొడవు 280 అక్షరాల కంటే ఎక్కువ ఉంటే → ఆ దశకు మాత్రమే పెద్ద మోడల్ (ఉదా: `gpt-oss-20b`)కి ఎస్కలేట్ చేయండి.

### ఐచ్ఛిక అభివృద్ధులు

| ప్రాంతం | అభివృద్ధి | విలువ | సూచన |
|------|-------------|-------|------|
| క్యాషింగ్ | మేనేజర్ + క్లయింట్ ఆబ్జెక్ట్స్ పునర్వినియోగం | తక్కువ లేటెన్సీ, తక్కువ ఓవర్‌హెడ్ | `workshop_utils.get_client` ఉపయోగించండి |
| వినియోగ మెట్రిక్స్ | టోకెన్లు & ప్రతి దశ లేటెన్సీ క్యాప్చర్ | ప్రొఫైలింగ్ & ఆప్టిమైజేషన్ | ప్రతి రూట్ చేసిన కాల్ టైమ్ చేయండి; ట్రేస్ జాబితాలో నిల్వ చేయండి |
| అనుకూల రూటింగ్ | విశ్వాసం / ఖర్చు అవగాహన | మెరుగైన నాణ్యత-ఖర్చు సమతుల్యత | స్కోరింగ్ జోడించండి: ప్రాంప్ట్ > N అక్షరాలు లేదా regex డొమైన్ సరిపోతే → పెద్ద మోడల్‌కు ఎస్కలేట్ చేయండి |
| డైనమిక్ సామర్థ్య రిజిస్ట్రీ | హాట్ రీలోడ్ క్యాటలాగ్ | రీస్టార్ట్ లేకుండా రీడిప్లాయ్ | రన్‌టైమ్‌లో `catalog.json` లోడ్ చేయండి; ఫైల్ టైమ్‌స్టాంప్‌ను గమనించండి |
| ఫాల్‌బ్యాక్ వ్యూహం | వైఫల్యాలపై రాబస్ట్నెస్ | ఎక్కువ అందుబాటు | ప్రాథమిక → ఎక్సెప్షన్ వస్తే ఫాల్‌బ్యాక్ అలియాస్ ప్రయత్నించండి |
| స్ట్రీమింగ్ పైప్‌లైన్ | తొందరగా ఫీడ్‌బ్యాక్ | UX మెరుగుదల | ప్రతి దశను స్ట్రీమ్ చేసి తుది మెరుగుదల ఇన్‌పుట్‌ను బఫర్ చేయండి |
| వెక్టర్ అభిప్రాయం ఎంబెడ్డింగ్స్ | మరింత సున్నితమైన రూటింగ్ | అధిక అభిప్రాయం ఖచ్చితత్వం | ప్రాంప్ట్‌ను ఎంబెడ్ చేసి, క్లస్టర్ చేసి, సెంట్రాయిడ్‌ను సామర్థ్యానికి మ్యాప్ చేయండి |
| ట్రేస్ ఎగుమతి | ఆడిటబుల్ చైన్ | అనుగుణత/రిపోర్టింగ్ | JSON లైన్లు విడుదల చేయండి: దశ, అభిప్రాయం, మోడల్, లేటెన్సీ_ms, టోకెన్లు |
| ఖర్చు సిమ్యులేషన్ | క్లౌడ్ ముందు అంచనా | బడ్జెట్ ప్లానింగ్ | ప్రతి మోడల్‌కు ప్రతీ టోకెన్ ఖర్చును కేటాయించి, టాస్క్‌కు సమ్మిళితం చేయండి |
| డిటర్మినిస్టిక్ మోడ్ | పునరుత్పత్తి సాధ్యం | స్థిరమైన బెంచ్‌మార్కింగ్ | ఎన్విరాన్: `temperature=0`, స్థిరమైన దశల సంఖ్య |

#### ట్రేస్ నిర్మాణం ఉదాహరణ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  
#### అనుకూల ఎస్కలేషన్ స్కెచ్

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # అందుబాటులో ఉంటే పెద్ద తర్క మోడల్‌కు పెంచండి
    alias = 'gpt-oss-20b'
```
  
#### మోడల్ క్యాటలాగ్ హాట్ రీలోడ్

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
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->