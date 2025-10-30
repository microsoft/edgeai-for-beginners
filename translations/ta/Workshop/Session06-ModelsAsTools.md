<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T23:55:25+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ta"
}
-->
# அமர்வு 6: Foundry Local – மாடல்கள் கருவிகளாக

## சுருக்கம்

மாடல்களை உள்ளூர் AI செயல்பாட்டு அடுக்கு உள்ளே இணைக்கக்கூடிய கருவிகளாக கருதுங்கள். இந்த அமர்வு பல சிறப்பு SLM/LLM அழைப்புகளை இணைத்து, பணிகளை தேர்ந்தெடுத்து வழிமாற்றி, பயன்பாடுகளுக்கு ஒருங்கிணைந்த SDK மேற்பரப்பை வெளிப்படுத்துவது எப்படி என்பதை காட்டுகிறது. நீங்கள் ஒரு எளிய மாடல் வழிமாற்றி + பணித் திட்டமிடுபவரை உருவாக்கி, அதை ஒரு பயன்பாட்டு ஸ்கிரிப்டில் ஒருங்கிணைத்து, Azure AI Foundryக்கு உற்பத்தி பணிகளுக்கான அளவீட்டு பாதையை சுருக்கமாக விளக்குவீர்கள்.

## கற்றல் நோக்கங்கள்

- **கற்பனை செய்யுங்கள்** மாடல்களை அறிவிக்கப்பட்ட திறன்களுடன் அணுக்கமான கருவிகளாக
- **வழிமாற்றுங்கள்** கோரிக்கைகளை நோக்கம் / ஹியூரிஸ்டிக் மதிப்பீட்டின் அடிப்படையில்
- **செயல்படுத்துங்கள்** பல படி பணிகளின் வெளியீடுகளை (பகுத்து → தீர்வு காணுங்கள் → மேம்படுத்துங்கள்)
- **ஒருங்கிணைக்கவும்** கீழ்மட்ட பயன்பாடுகளுக்கு ஒருங்கிணைந்த கிளையன்ட் API
- **அளவீட்டம்** மேகத்திற்கான வடிவமைப்பு (அதே OpenAI-இக்கு இணக்கமான ஒப்பந்தம்)

## முன் தேவைகள்

- அமர்வுகள் 1–5 முடிக்கப்பட்டது
- பல உள்ளூர் மாடல்கள் சேமிக்கப்பட்டது (எ.கா., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### குறுக்குவெளி சூழல் குறிப்பு

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

Remote/VM சேவை அணுகல் macOS-இல்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## டெமோ ஓட்டம் (30 நிமிடம்)

### 1. கருவி திறன் அறிவிப்பு (5 நிமிடம்)

`samples/06-tools/models_catalog.py` உருவாக்கவும்:

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


### 2. நோக்கம் கண்டறிதல் & வழிமாற்றம் (8 நிமிடம்)

`samples/06-tools/router.py` உருவாக்கவும்:

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


### 3. பல படி பணித் தொடர் (7 நிமிடம்)

`samples/06-tools/pipeline.py` உருவாக்கவும்:

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


### 4. தொடக்க திட்டம்: `06-models-as-tools` ஐ மாற்றவும் (5 நிமிடம்)

மேம்பாடுகள்:
- ஸ்ட்ரீமிங் டோக்கன் ஆதரவு சேர்க்கவும் (முன்னேற்ற UI புதுப்பிப்பு)
- நம்பகத்தன்மை மதிப்பீடு சேர்க்கவும்: சொற்களின் ஒத்திசைவு அல்லது ப்ராம்ட் அளவுகோல்
- டிரேஸ் JSON ஏற்றுமதி (நோக்கம் → மாடல் → தாமதம் → டோக்கன் பயன்பாடு)
- மீண்டும் மீண்டும் துணைநடவடிக்கைகளுக்கு கேஷ் மீண்டும் பயன்படுத்தல் செயல்படுத்தவும்

### 5. Azureக்கு அளவீட்டு பாதை (5 நிமிடம்)

| அடுக்கு | உள்ளூர் (Foundry) | மேகம் (Azure AI Foundry) | மாற்று உத்தி |
|--------|-------------------|--------------------------|--------------|
| வழிமாற்றம் | ஹியூரிஸ்டிக் Python | நிலையான மைக்ரோசேவை | API-ஐ கெண்டெய்னராக்கி வெளியிடவும் |
| மாடல்கள் | SLMs சேமிக்கப்பட்டது | மேலாண்மை வெளியீடுகள் | உள்ளூர் பெயர்களை வெளியீட்டு ID-களுக்கு வரைபடம் செய்யவும் |
| கண்காணிப்பு | CLI புள்ளிவிவரங்கள்/கையேடு | மைய பதிவு மற்றும் அளவீடுகள் | அமைந்த டிரேஸ் நிகழ்வுகளைச் சேர்க்கவும் |
| பாதுகாப்பு | உள்ளூர் ஹோஸ்ட் மட்டும் | Azure அங்கீகாரம் / நெட்வொர்க்கிங் | ரகசியங்களுக்கு முக்கிய காப்பகத்தை அறிமுகப்படுத்தவும் |
| செலவு | சாதன வளம் | நுகர்வு பில்லிங் | பட்ஜெட் பாதுகாப்பு வழிகாட்டிகளைச் சேர்க்கவும் |

## சரிபார்ப்பு சோதனைப்பட்டியல்

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

நோக்கத்தின் அடிப்படையில் மாடல் தேர்வு மற்றும் இறுதியாக மேம்படுத்தப்பட்ட வெளியீட்டை எதிர்பார்க்கவும்.

## சிக்கல் தீர்வு

| பிரச்சினை | காரணம் | தீர்வு |
|----------|--------|-------|
| அனைத்து பணிகளும் ஒரே மாடலுக்கு வழிமாற்றம் செய்யப்படுகிறது | பலவீனமான விதிகள் | INTENT_RULES regex தொகுப்பை செறிவூட்டவும் |
| நடுவில் குழாய் தோல்வியடைகிறது | ஏற்றப்பட்ட மாடல் இல்லை | `foundry model run <model>` இயக்கவும் |
| குறைந்த வெளியீட்டு ஒற்றுமை | மேம்படுத்தும் கட்டம் இல்லை | சுருக்கம்/சரிபார்ப்பு கட்டத்தைச் சேர்க்கவும் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry ஆவணங்கள்: https://learn.microsoft.com/azure/ai-foundry
- ப்ராம்ட் தரம் முறை: அமர்வு 2 ஐப் பார்க்கவும்

---

**அமர்வு காலம்**: 30 நிமிடம்  
**கடினம்**: நிபுணர்

## மாதிரி சூழல் & பணிக்கூட வரைபடம்

| பணிக்கூட ஸ்கிரிப்டுகள் / நோட்புக்குகள் | சூழல் | நோக்கம் | தரவுத்தொகுப்பு / பட்டியல் மூலங்கள் |
|---------------------------------------|-------|---------|------------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | கலந்த நோக்க ப்ராம்ட்களை கையாளும் டெவலப்பர் உதவியாளர் (மறுசீரமைப்பு, சுருக்கம், வகைப்படுத்தல்) | ஹியூரிஸ்டிக் நோக்கம் → மாடல் அலியாஸ் வழிமாற்றம் டோக்கன் பயன்பாட்டுடன் | உள்ளமை `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | சிக்கலான குறியீட்டு உதவிப் பணிக்கான பல படி திட்டமிடல் & மேம்படுத்தல் | பகுத்தல் → சிறப்பு செயல்பாடு → சுருக்கம் மேம்படுத்தும் கட்டம் | அதே `CATALOG`; திட்ட வெளியீட்டிலிருந்து பெறப்பட்ட படிகள் |

### சூழல் கதை
ஒரு பொறியியல் உற்பத்தி கருவி பலவகை பணிகளைப் பெறுகிறது: குறியீட்டை மறுசீரமைத்தல், கட்டமைப்பு குறிப்புகளை சுருக்குதல், கருத்துகளை வகைப்படுத்துதல். தாமதம் மற்றும் வள பயன்பாட்டை குறைக்க, ஒரு சிறிய பொது மாடல் திட்டமிடுகிறது மற்றும் சுருக்குகிறது, குறியீடு‑சிறப்பு மாடல் மறுசீரமைப்பை கையாளுகிறது, மற்றும் ஒரு எளிய வகைப்படுத்தல்‑திறன் மாடல் கருத்துகளை லேபிள் செய்கிறது. குழாய் ஸ்கிரிப்ட் தொடர் + மேம்படுத்தலைக் காட்டுகிறது; வழிமாற்றி ஸ்கிரிப்ட் தனிப்பயன்‑ப்ராம்ட் வழிமாற்றத்தை தனிமைப்படுத்துகிறது.

### பட்டியல் ஸ்னாப்ஷாட்
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### மாதிரி சோதனை ப்ராம்ட்கள்
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### டிரேஸ் நீட்டிப்பு (விருப்பம்)
`models_pipeline.py`க்கு படி‑ஒன்றுக்கு டிரேஸ் JSON வரிகளைச் சேர்க்கவும்:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### உயர்வு ஹியூரிஸ்டிக் (ஆய்வு)
திட்டத்தில் "optimize", "security" போன்ற முக்கிய வார்த்தைகள் அல்லது படி நீளம் > 280 எழுத்துகள் உள்ளதெனில் → அந்த படிக்கே பெரிய மாடலுக்கு (எ.கா., `gpt-oss-20b`) உயர்வு செய்யவும்.

### விருப்ப மேம்பாடுகள்

| பகுதி | மேம்பாடு | மதிப்பு | குறிப்பு |
|-------|----------|---------|---------|
| கேஷிங் | மேலாளர் + கிளையன்ட் பொருட்களை மீண்டும் பயன்படுத்தவும் | குறைந்த தாமதம், குறைந்த மேலதிகச் செலவு | `workshop_utils.get_client` பயன்படுத்தவும் |
| பயன்பாட்டு அளவீடுகள் | டோக்கன்கள் & படி‑ஒன்றுக்கு தாமதத்தைப் பதிவு செய்யவும் | சுயவிவரமிடல் & மேம்பாடு | ஒவ்வொரு வழிமாற்றிய அழைப்பையும் நேரம் பார்க்கவும்; டிரேஸ் பட்டியலில் சேமிக்கவும் |
| தற்காலிக வழிமாற்றம் | நம்பகத்தன்மை / செலவினம் சார்ந்தது | சிறந்த தரம்‑செலவு சமநிலை | மதிப்பீடு சேர்க்கவும்: ப்ராம்ட் > N எழுத்துகள் அல்லது regex டொமைன் பொருந்துகிறது → பெரிய மாடலுக்கு உயர்வு செய்யவும் |
| மாறும் திறன் பதிவேடு | சூழல் பட்டியலை ஹாட் ரீலோட் செய்யவும் | மீண்டும் தொடங்கல் மறுபதிவேற்றம் தேவையில்லை | `catalog.json`ஐ இயக்க நேரத்தில் ஏற்றவும்; கோப்பு நேரத்தைப் பார்க்கவும் |
| பின்வாங்கும் உத்தி | தோல்விகளில் வலிமை | அதிக கிடைப்புத் திறன் | முதன்மை முயற்சி → தவறில் பின்வாங்கும் அலியாஸ் |
| ஸ்ட்ரீமிங் குழாய் | ஆரம்ப கருத்து | UX மேம்பாடு | ஒவ்வொரு படியையும் ஸ்ட்ரீம் செய்யவும் மற்றும் இறுதி மேம்படுத்தும் உள்ளீட்டை பஃபர் செய்யவும் |
| வெக்டர் நோக்கம் எம்பெடிங்ஸ் | மேலும் நுணுக்கமான வழிமாற்றம் | அதிகமான நோக்கம் துல்லியம் | ப்ராம்ட்டை எம்பெட் செய்யவும், கிளஸ்டர் செய்யவும் & மையத்தை வரைபடம் செய்யவும் → திறன் |
| டிரேஸ் ஏற்றுமதி | சரிபார்க்கக்கூடிய தொடர் | இணக்கம்/அறிக்கையிடல் | JSON வரிகளை வெளியிடவும்: படி, நோக்கம், மாடல், latency_ms, tokens |
| செலவு சிமுலேஷன் | மேகத்திற்கு முன் மதிப்பீடு | பட்ஜெட் திட்டமிடல் | மாடல்‑ஒன்றுக்கு டோக்கன்‑ஒன்றுக்கு கற்பனையான செலவை ஒதுக்கவும் & பணிக்கு ஒட்டுமொத்தமாக சேர்க்கவும் |
| தீர்மானமான முறை | மறுபுருவி மீள்திருத்தம் | நிலையான பெஞ்ச்மார்க்கிங் | சூழல்: `temperature=0`, நிர்ணயிக்கப்பட்ட படிகள் எண்ணிக்கை |

#### டிரேஸ் அமைப்பு உதாரணம்

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### தற்காலிக உயர்வு வரைபடம்

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### மாடல் பட்டியல் ஹாட் ரீலோட்

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

**புறக்கணிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.