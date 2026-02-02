# Kipindi cha 6: Foundry Local – Miundo kama Zana

## Muhtasari

Tumia miundo kama zana zinazoweza kuunganishwa ndani ya safu ya uendeshaji ya AI ya ndani. Kipindi hiki kinaonyesha jinsi ya kuunganisha miito mingi ya SLM/LLM maalum, kuelekeza majukumu kwa kuchagua, na kufichua uso wa SDK uliounganishwa kwa programu. Utajenga router nyepesi ya modeli + mpangaji wa majukumu, kuunganisha kwenye script ya programu, na kuelezea njia ya kupanua hadi Azure AI Foundry kwa mzigo wa kazi wa uzalishaji.

## Malengo ya Kujifunza

- **Fikiria** miundo kama zana za atomiki zenye uwezo ulioelezwa
- **Elekeza** maombi kulingana na nia / alama za heuristiki
- **Unganisha** matokeo katika majukumu ya hatua nyingi (gawanya → suluhisha → rekebisha)
- **Unganisha** API ya mteja iliyounganishwa kwa programu za chini
- **Panua** muundo hadi wingu (mkataba sawa unaoendana na OpenAI)

## Mahitaji ya Awali

- Vipindi 1–5 vimekamilika
- Miundo mingi ya ndani imehifadhiwa (mfano, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Kipande cha Mazingira ya Msalaba Jukwaa

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

Huduma ya ufikiaji wa mbali/VM kutoka macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Mtiririko wa Demo (Dakika 30)

### 1. Tamko la Uwezo wa Zana (Dakika 5)

Unda `samples/06-tools/models_catalog.py`:

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


### 2. Kugundua Nia & Uelekezaji (Dakika 8)

Unda `samples/06-tools/router.py`:

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


### 3. Kuunganisha Majukumu ya Hatua Nyingi (Dakika 7)

Unda `samples/06-tools/pipeline.py`:

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


### 4. Mradi wa Kuanza: Badilisha `06-models-as-tools` (Dakika 5)

Maboresho:
- Ongeza msaada wa tokeni za kutiririsha (sasisho la UI la maendeleo)
- Ongeza alama za kujiamini: kufanana kwa leksika au rubriki ya maelezo
- Hamisha JSON ya ufuatiliaji (nia → modeli → ucheleweshaji → matumizi ya tokeni)
- Tekeleza matumizi ya cache kwa hatua ndogo zinazojirudia

### 5. Njia ya Kupanua hadi Azure (Dakika 5)

| Safu | Local (Foundry) | Cloud (Azure AI Foundry) | Mkakati wa Mpito |
|------|-----------------|--------------------------|------------------|
| Uelekezaji | Heuristiki Python | Huduma ndogo ya kudumu | Fanya kontena & peleka API |
| Miundo | SLMs imehifadhiwa | Utekelezaji unaosimamiwa | Panga majina ya ndani kwa vitambulisho vya utekelezaji |
| Ufuatiliaji | Takwimu za CLI/mwongozo | Kumbukumbu kuu & vipimo | Ongeza matukio ya ufuatiliaji yaliyopangwa |
| Usalama | Mwenyeji wa ndani pekee | Uthibitisho wa Azure / mtandao | Tumia hifadhi ya funguo kwa siri |
| Gharama | Rasilimali ya kifaa | Malipo ya matumizi | Ongeza vizuizi vya bajeti |

## Orodha ya Ukaguzi wa Uthibitishaji

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Tegemea uteuzi wa modeli kulingana na nia na matokeo ya mwisho yaliyorekebishwa.

## Utatuzi wa Matatizo

| Tatizo | Sababu | Suluhisho |
|--------|--------|----------|
| Majukumu yote yanaelekezwa kwa modeli moja | Sheria dhaifu | Boresha seti ya regex ya INTENT_RULES |
| Njia ya kazi inashindwa katikati ya hatua | Hakuna modeli iliyopakiwa | Endesha `foundry model run <model>` |
| Ushirikiano wa matokeo mdogo | Hakuna awamu ya kurekebisha | Ongeza hatua ya muhtasari/kuthibitisha |

## Marejeleo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Mifumo ya Ubora wa Maelezo: Tazama Kipindi cha 2

---

**Muda wa Kipindi**: Dakika 30  
**Ugumu**: Mtaalamu

## Mfano wa Hali & Ulinganisho wa Warsha

| Script za Warsha / Notebooks | Hali | Lengo | Chanzo cha Dataset / Katalogi |
|------------------------------|------|-------|-------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Msaidizi wa msanidi programu anayeshughulikia maelezo ya nia mchanganyiko (rekebisha, muhtasari, weka daraja) | Nia ya heuristiki → uelekezaji wa alias ya modeli na matumizi ya tokeni | `CATALOG` ya ndani + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Mipango ya hatua nyingi & marekebisho kwa kazi ngumu ya msaada wa usimbaji | Gawanya → utekelezaji maalum → hatua ya muhtasari wa kurekebisha | `CATALOG` ile ile; hatua zinatokana na matokeo ya mpango |

### Maelezo ya Hali
Zana ya uzalishaji wa uhandisi inapokea majukumu mchanganyiko: rekebisha msimbo, fupisha maelezo ya usanifu, weka daraja maoni. Ili kupunguza ucheleweshaji & matumizi ya rasilimali, modeli ndogo ya jumla inapanga na kufupisha, modeli maalum ya msimbo inashughulikia marekebisho, na modeli nyepesi inayoweza kuainisha inaweka daraja maoni. Script ya njia inaonyesha kuunganisha + kurekebisha; script ya router inatenga uelekezaji wa nia moja.

### Muhtasari wa Katalogi
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Mfano wa Maelezo ya Mtihani
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Ugani wa Ufuatiliaji (Hiari)
Ongeza mistari ya JSON ya ufuatiliaji kwa kila hatua kwa `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristiki ya Kupandisha (Wazo)
Ikiwa mpango una maneno muhimu kama "boresha", "usalama", au urefu wa hatua > herufi 280 → pandisha hadi modeli kubwa (mfano, `gpt-oss-20b`) kwa hatua hiyo pekee.

### Maboresho ya Hiari

| Eneo | Uboreshaji | Thamani | Kidokezo |
|------|------------|---------|----------|
| Kuhifadhi | Tumia meneja + vitu vya mteja | Ucheleweshaji mdogo, mzigo mdogo | Tumia `workshop_utils.get_client` |
| Vipimo vya Matumizi | Kamatia tokeni & ucheleweshaji wa kila hatua | Uboreshaji wa wasifu | Pima kila mwito uliotumwa; hifadhi kwenye orodha ya ufuatiliaji |
| Uelekezaji wa Adaptive | Uelewa wa kujiamini / gharama | Usawa bora wa ubora-gharama | Ongeza alama: ikiwa maelezo > herufi N au regex inalingana na uwanja → pandisha hadi modeli kubwa |
| Usajili wa Uwezo wa Kielezo | Pakia katalogi bila kuzima | Hakuna kuanzisha upya tena | Pakia `catalog.json` wakati wa kukimbia; angalia timestamp ya faili |
| Mkakati wa Kurejea | Uimara chini ya kushindwa | Upatikanaji wa juu | Jaribu msingi → kwenye ubaguzi alias ya kurejea |
| Njia ya Kutiririsha | Maoni ya mapema | Uboreshaji wa UX | Tuma kila hatua na weka akiba ya pembejeo la mwisho la kurekebisha |
| Uwekaji wa Nia ya Vector | Uelekezaji wa kina zaidi | Usahihi wa juu wa nia | Weka maelezo, cluster & panga centroid → uwezo |
| Hamisha Ufuatiliaji | Mnyororo unaoweza kukaguliwa | Uzingatiaji/kuripoti | Tuma mistari ya JSON: hatua, nia, modeli, latency_ms, tokeni |
| Simulizi ya Gharama | Makadirio ya kabla ya wingu | Mipango ya bajeti | Weka gharama ya dhahania/tokeni kwa modeli & jumlisha kwa kila kazi |
| Hali ya Kiamua | Urejeleaji wa kurudia | Upimaji thabiti | Mazingira: `temperature=0`, idadi ya hatua zilizowekwa |

#### Mfano wa Muundo wa Ufuatiliaji

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Mchoro wa Kupandisha Adaptive

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Upakiaji wa Katalogi ya Modeli

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

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.