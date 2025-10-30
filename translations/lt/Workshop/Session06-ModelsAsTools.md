<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T23:49:41+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "lt"
}
-->
# Sesija 6: Foundry Local – Modeliai kaip įrankiai

## Santrauka

Traktuokite modelius kaip sudedamuosius įrankius vietiniame AI operaciniame sluoksnyje. Šioje sesijoje parodysime, kaip sujungti kelis specializuotus SLM/LLM kvietimus, selektyviai nukreipti užduotis ir pateikti vieningą SDK paviršių programoms. Jūs sukursite lengvą modelių maršrutizatorių + užduočių planuotoją, integruosite jį į programos scenarijų ir apžvelgsite mastelio didinimo kelią į Azure AI Foundry, skirtą gamybos darbo krūviams.

## Mokymosi tikslai

- **Suprasti** modelius kaip atominius įrankius su deklaruotomis galimybėmis
- **Nukreipti** užklausas pagal ketinimą / euristinio vertinimo rezultatus
- **Sujungti** rezultatus per daugiapakopes užduotis (suskaidyti → išspręsti → patobulinti)
- **Integruoti** vieningą klientų API žemyninėms programoms
- **Mastelio didinimas** dizaino perkėlimas į debesį (tas pats OpenAI suderinamas kontraktas)

## Būtinos sąlygos

- Užbaigtos sesijos 1–5
- Keletas vietinių modelių talpykloje (pvz., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Kryžminės platformos aplinkos fragmentas

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

Nuotolinė/VM paslauga iš macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demonstracijos eiga (30 min)

### 1. Įrankių galimybių deklaracija (5 min)

Sukurkite `samples/06-tools/models_catalog.py`:

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


### 2. Ketinimų aptikimas ir maršrutizavimas (8 min)

Sukurkite `samples/06-tools/router.py`:

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


### 3. Daugiapakopė užduočių grandinė (7 min)

Sukurkite `samples/06-tools/pipeline.py`:

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


### 4. Pradinis projektas: pritaikykite `06-models-as-tools` (5 min)

Patobulinimai:
- Pridėkite srautinio žetonų palaikymą (progresyvus UI atnaujinimas)
- Pridėkite pasitikėjimo vertinimą: leksinis sutapimas arba raginimo rubrika
- Eksportuokite sekimo JSON (ketinimas → modelis → vėlavimas → žetonų naudojimas)
- Įgyvendinkite talpyklos pakartotinį naudojimą pasikartojantiems subžingsniams

### 5. Mastelio didinimo kelias į Azure (5 min)

| Sluoksnis | Vietinis (Foundry) | Debesis (Azure AI Foundry) | Perėjimo strategija |
|-----------|--------------------|----------------------------|---------------------|
| Maršrutizavimas | Euristinis Python | Patvarus mikroservisas | Konteinerizuokite ir diekite API |
| Modeliai | SLM talpyklos | Valdomi diegimai | Susiekite vietinius pavadinimus su diegimo ID |
| Stebėjimas | CLI statistika/rankinis | Centrinis žurnalavimas ir metrika | Pridėkite struktūrizuotus sekimo įvykius |
| Saugumas | Tik vietinis kompiuteris | Azure autentifikacija / tinklas | Įdiekite raktų saugyklą paslaptims |
| Kaina | Įrenginio resursai | Vartojimo sąskaitos | Pridėkite biudžeto apsaugos priemones |

## Patikrinimo kontrolinis sąrašas

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Tikėkitės ketinimų pagrindu parinkto modelio ir galutinio patobulinto rezultato.

## Trikčių šalinimas

| Problema | Priežastis | Sprendimas |
|----------|------------|------------|
| Visos užduotys nukreipiamos į tą patį modelį | Silpnos taisyklės | Praturtinkite INTENT_RULES regex rinkinį |
| Vamzdynas sugenda viduryje žingsnio | Trūksta įkeltų modelių | Paleiskite `foundry model run <model>` |
| Mažas rezultatų nuoseklumas | Nėra patobulinimo fazės | Pridėkite apibendrinimo/patikrinimo etapą |

## Nuorodos

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry dokumentacija: https://learn.microsoft.com/azure/ai-foundry
- Raginimų kokybės šablonai: žr. 2 sesiją

---

**Sesijos trukmė**: 30 min  
**Sudėtingumas**: Ekspertas

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių scenarijai / užrašų knygelės | Situacija | Tikslas | Duomenų rinkinys / katalogo šaltinis |
|---------------------------------------|----------|---------|-------------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Kūrėjo asistentas, tvarkantis mišrius ketinimų raginimus (perrašyti, apibendrinti, klasifikuoti) | Euristinis ketinimas → modelio alias maršrutizavimas su žetonų naudojimu | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Daugiapakopis planavimas ir patobulinimas sudėtingai kodavimo pagalbos užduočiai | Suskaidyti → specializuotas vykdymas → apibendrinimo patobulinimo etapas | Tas pats `CATALOG`; žingsniai išvesti iš plano rezultato |

### Situacijos pasakojimas
Inžinerinio produktyvumo įrankis gauna įvairias užduotis: perrašyti kodą, apibendrinti architektūrines pastabas, klasifikuoti atsiliepimus. Siekiant sumažinti vėlavimą ir resursų naudojimą, mažas bendras modelis planuoja ir apibendrina, kodui specializuotas modelis tvarko perrašymą, o lengvas klasifikavimo modelis žymi atsiliepimus. Vamzdyno scenarijus demonstruoja grandinę + patobulinimą; maršrutizatoriaus scenarijus izoliuoja adaptacinį vieno raginimo maršrutizavimą.

### Katalogo momentinė nuotrauka
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Pavyzdiniai testavimo raginimai
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Sekimo plėtinys (pasirinktinai)
Pridėkite kiekvieno žingsnio sekimo JSON eilutes `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskalacijos euristika (idėja)
Jei plane yra tokių raktinių žodžių kaip "optimizuoti", "saugumas" arba žingsnio ilgis > 280 simbolių → eskaluokite į didesnį modelį (pvz., `gpt-oss-20b`) tik tam žingsniui.

### Pasirinktiniai patobulinimai

| Sritis | Patobulinimas | Vertė | Pasiūlymas |
|--------|--------------|-------|-----------|
| Talpyklos naudojimas | Pakartotinis valdytojo + kliento objektų naudojimas | Mažesnis vėlavimas, mažesnės sąnaudos | Naudokite `workshop_utils.get_client` |
| Naudojimo metrika | Fiksuokite žetonus ir kiekvieno žingsnio vėlavimą | Profilaktika ir optimizavimas | Laikykite kiekvieną nukreiptą kvietimą; saugokite sekimo sąraše |
| Adaptacinis maršrutizavimas | Pasitikėjimo / sąnaudų vertinimas | Geresnis kokybės ir sąnaudų balansas | Pridėkite vertinimą: jei raginimas > N simbolių arba regex atitinka domeną → eskaluokite į didesnį modelį |
| Dinaminis galimybių registras | Karštas katalogo perkrovimas | Be perkrovimo diegimo | Įkelkite `catalog.json` vykdymo metu; stebėkite failo laiko žymą |
| Atsarginė strategija | Atsparumas gedimams | Didesnis prieinamumas | Bandykite pirminį → gedimo atveju atsarginį alias |
| Srautinė grandinė | Ankstyvas grįžtamasis ryšys | UX patobulinimas | Srautu perduokite kiekvieną žingsnį ir buferiuokite galutinį patobulinimo įvestį |
| Vektoriniai ketinimų įterpimai | Daugiau niuansų maršrutizavime | Didesnis ketinimų tikslumas | Įterpkite raginimą, grupuokite ir susiekite centroidą → galimybė |
| Sekimo eksportas | Grandinės auditas | Atitiktis/ataskaitų teikimas | Išveskite JSON eilutes: žingsnis, ketinimas, modelis, vėlavimas_ms, žetonai |
| Sąnaudų simuliacija | Prieš debesį įvertinimas | Biudžeto planavimas | Priskirkite nominalias sąnaudas/žetoną kiekvienam modeliui ir sumuokite užduočiai |
| Deterministinis režimas | Atkuriamumas | Stabilus palyginimas | Aplinka: `temperature=0`, fiksuotas žingsnių skaičius |

#### Sekimo struktūros pavyzdys

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptacinės eskalacijos eskizas

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Modelio katalogo karštas perkrovimas

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

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.