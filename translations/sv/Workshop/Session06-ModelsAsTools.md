# Session 6: Foundry Local – Modeller som Verktyg

## Sammanfattning

Behandla modeller som sammansättningsbara verktyg inom ett lokalt AI-operativlager. Denna session visar hur man kan kedja flera specialiserade SLM/LLM-anrop, selektivt dirigera uppgifter och exponera en enhetlig SDK-yta för applikationer. Du kommer att bygga en lättviktig modellrouter + uppgiftsplanerare, integrera den i ett appskript och skissera vägen för skalning till Azure AI Foundry för produktionsarbetsbelastningar.

## Lärandemål

- **Konceptualisera** modeller som atomära verktyg med deklarerade kapaciteter
- **Dirigera** förfrågningar baserat på avsikt / heuristisk poängsättning
- **Kedja** utdata över flerstegsuppgifter (bryt ner → lös → förfina)
- **Integrera** en enhetlig klient-API för nedströmsapplikationer
- **Skala** designen till molnet (samma OpenAI-kompatibla kontrakt)

## Förkunskaper

- Sessioner 1–5 genomförda
- Flera lokala modeller cachade (t.ex. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet för Plattformar

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

Fjärr-/VM-tjänståtkomst från macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-flöde (30 min)

### 1. Deklaration av Verktygskapacitet (5 min)

Skapa `samples/06-tools/models_catalog.py`:

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


### 2. Avsiktsdetektion & Routing (8 min)

Skapa `samples/06-tools/router.py`:

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


### 3. Flerstegsuppgiftskedjning (7 min)

Skapa `samples/06-tools/pipeline.py`:

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


### 4. Startprojekt: Anpassa `06-models-as-tools` (5 min)

Förbättringar:
- Lägg till stöd för strömmande token (progressiv UI-uppdatering)
- Lägg till poängsättning för förtroende: lexikal överlappning eller promptmall
- Exportera spårnings-JSON (avsikt → modell → latens → tokenanvändning)
- Implementera cache-återanvändning för upprepade delsteg

### 5. Skalningsväg till Azure (5 min)

| Lager | Lokalt (Foundry) | Moln (Azure AI Foundry) | Övergångsstrategi |
|-------|------------------|-------------------------|-------------------|
| Routing | Heuristisk Python | Hållbar mikrotjänst | Containerisera & distribuera API |
| Modeller | Cachade SLM | Hanterade distributioner | Mappa lokala namn till distributions-ID |
| Observabilitet | CLI-statistik/manuell | Central loggning & mätvärden | Lägg till strukturerade spårningshändelser |
| Säkerhet | Endast lokal värd | Azure-autentisering / nätverk | Introducera nyckelvalv för hemligheter |
| Kostnad | Enhetsresurser | Konsumtionsfakturering | Lägg till budgetgränser |

## Valideringschecklista

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Förvänta dig avsiktsbaserad modellval och slutligt förfinat resultat.

## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| Alla uppgifter dirigeras till samma modell | Svaga regler | Berika INTENT_RULES regex-uppsättning |
| Pipeline misslyckas mitt i ett steg | Saknad modell laddad | Kör `foundry model run <model>` |
| Låg sammanhållning i utdata | Ingen förfiningsfas | Lägg till sammanfattnings-/valideringspass |

## Referenser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Promptkvalitetsmönster: Se Session 2

---

**Sessionens längd**: 30 min  
**Svårighetsgrad**: Expert

## Exempelscenario & Workshopkartläggning

| Workshopskript / Anteckningsböcker | Scenario | Mål | Dataset / Katalogkälla |
|------------------------------------|----------|-----|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Utvecklarassistent som hanterar blandade avsikts-promptar (omstrukturera, sammanfatta, klassificera) | Heuristisk avsikt → modellalias-routing med tokenanvändning | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Flerstegsplanering & förfining för komplex kodassistansuppgift | Bryt ner → specialiserad exekvering → sammanfattningsförfiningssteg | Samma `CATALOG`; steg härledda från planutdata |

### Scenarioberättelse
Ett verktyg för ingenjörsproduktivitet tar emot heterogena uppgifter: omstrukturera kod, sammanfatta arkitektoniska anteckningar, klassificera feedback. För att minimera latens och resursanvändning planerar och sammanfattar en liten generell modell, en kodspecialiserad modell hanterar omstrukturering, och en lätt klassificeringskapabel modell märker feedback. Pipelineskriptet demonstrerar kedjning + förfining; routerskriptet isolerar adaptiv enkel-prompt-routing.

### Katalogöversikt
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Exempeltestpromptar
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Spårningsförlängning (Valfritt)
Lägg till spårnings-JSON-rader per steg för `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskaleringsheuristik (Idé)
Om planen innehåller nyckelord som "optimera", "säkerhet", eller steglängd > 280 tecken → eskalera till större modell (t.ex. `gpt-oss-20b`) endast för det steget.

### Valfria Förbättringar

| Område | Förbättring | Värde | Tips |
|--------|-------------|-------|------|
| Caching | Återanvänd hanterare + klientobjekt | Lägre latens, mindre overhead | Använd `workshop_utils.get_client` |
| Användningsmätning | Fånga tokens & latens per steg | Profilering & optimering | Tidtag varje dirigerat anrop; lagra i spårningslista |
| Adaptiv Routing | Medveten om förtroende / kostnad | Bättre kvalitet-kostnadsbalans | Lägg till poängsättning: om prompt > N tecken eller regex matchar domän → eskalera till större modell |
| Dynamisk Kapacitetsregister | Hot reload-katalog | Ingen omstart eller omdistribution | Ladda `catalog.json` vid runtime; övervaka filens tidsstämpel |
| Reservstrategi | Robusthet vid fel | Högre tillgänglighet | Försök primär → vid undantag reservalias |
| Strömmande Pipeline | Tidig feedback | Förbättrad användarupplevelse | Strömma varje steg och buffra slutlig förfiningsinmatning |
| Vektoravsiktsinbäddningar | Mer nyanserad routing | Högre avsiktsnoggrannhet | Bädda in prompt, klustra & mappa centroid → kapacitet |
| Spårningsexport | Auditerbar kedja | Efterlevnad/rapportering | Emittera JSON-rader: steg, avsikt, modell, latens_ms, tokens |
| Kostnadssimulering | Förmoln-beräkning | Budgetplanering | Tilldela nominell kostnad/token per modell & summera per uppgift |
| Deterministiskt läge | Reproducerbarhet | Stabil benchmarking | Miljö: `temperature=0`, fast antal steg |

#### Exempel på Spårningsstruktur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Skiss för Adaptiv Eskalering

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot Reload för Modellkatalog

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

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.