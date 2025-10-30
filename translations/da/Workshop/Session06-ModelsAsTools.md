<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T22:10:55+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "da"
}
-->
# Session 6: Foundry Local – Modeller som værktøjer

## Resumé

Behandl modeller som sammensatte værktøjer i et lokalt AI-operativlag. Denne session viser, hvordan man kæder flere specialiserede SLM/LLM-kald sammen, ruter opgaver selektivt og eksponerer en samlet SDK-overflade til applikationer. Du vil bygge en letvægtsmodel-router + opgaveplanlægger, integrere den i et app-script og skitsere skaleringsvejen til Azure AI Foundry for produktionsarbejdsbelastninger.

## Læringsmål

- **Konceptualisere** modeller som atomare værktøjer med deklarerede kapaciteter
- **Rute** forespørgsler baseret på intention / heuristisk scoring
- **Kæde** output på tværs af opgaver i flere trin (dekomponere → løse → forfine)
- **Integrere** en samlet klient-API til downstream-applikationer
- **Skalere** design til skyen (samme OpenAI-kompatible kontrakt)

## Forudsætninger

- Sessioner 1–5 gennemført
- Flere lokale modeller cachet (f.eks. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet til tværplatformsmiljø

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

Fjern-/VM-serviceadgang fra macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Deklaration af værktøjskapacitet (5 min)

Opret `samples/06-tools/models_catalog.py`:

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


### 2. Intentiondetektion og routing (8 min)

Opret `samples/06-tools/router.py`:

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


### 3. Kædning af opgaver i flere trin (7 min)

Opret `samples/06-tools/pipeline.py`:

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


### 4. Startprojekt: Tilpas `06-models-as-tools` (5 min)

Forbedringer:
- Tilføj streaming-token-understøttelse (progressiv UI-opdatering)
- Tilføj tillidsscore: leksikalsk overlap eller prompt-rubrik
- Eksporter trace JSON (intention → model → latenstid → tokenforbrug)
- Implementer cache-genbrug for gentagne deltrin

### 5. Skaleringsvej til Azure (5 min)

| Lag | Lokalt (Foundry) | Skyen (Azure AI Foundry) | Overgangsstrategi |
|-----|------------------|--------------------------|-------------------|
| Routing | Heuristisk Python | Holdbar mikrotjeneste | Containeriser & deploy API |
| Modeller | Cachede SLM'er | Administrerede implementeringer | Map lokale navne til implementerings-ID'er |
| Observabilitet | CLI-statistik/manual | Central logning & metrikker | Tilføj strukturerede trace-hændelser |
| Sikkerhed | Kun lokal vært | Azure-autentificering / netværk | Introducer nøglevault til hemmeligheder |
| Omkostninger | Enhedsressource | Forbrugsafregning | Tilføj budgetbegrænsninger |

## Valideringscheckliste

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Forvent intention-baseret modelvalg og endeligt forfinet output.

## Fejlfinding

| Problem | Årsag | Løsning |
|---------|-------|---------|
| Alle opgaver rutes til samme model | Svage regler | Berig INTENT_RULES regex-sæt |
| Pipeline fejler midt i et trin | Manglende model indlæst | Kør `foundry model run <model>` |
| Lav output-sammenhæng | Ingen forfiningsfase | Tilføj opsummerings-/valideringspassage |

## Referencer

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Quality Patterns: Se Session 2

---

**Sessionens varighed**: 30 min  
**Sværhedsgrad**: Ekspert

## Eksempelscenarie & workshopkortlægning

| Workshop-scripts / Notebooks | Scenarie | Mål | Datasæt / Katalogkilde |
|------------------------------|----------|-----|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Udviklerassistent, der håndterer blandede intention-prompter (refaktorere, opsummere, klassificere) | Heuristisk intention → modelalias-routing med tokenforbrug | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planlægning i flere trin & forfining for kompleks kodningsassistanceopgave | Dekomponere → specialiseret udførelse → opsummeringsforfining | Samme `CATALOG`; trin afledt af planoutput |

### Scenariefortælling
Et værktøj til ingeniørproduktivitet modtager heterogene opgaver: refaktorere kode, opsummere arkitektoniske noter, klassificere feedback. For at minimere latenstid & ressourceforbrug planlægger og opsummerer en lille generel model, en kode-specialiseret model håndterer refaktorering, og en let klassifikationsdygtig model mærker feedback. Pipeline-scriptet demonstrerer kædning + forfining; router-scriptet isolerer adaptiv enkelt-prompt-routing.

### Katalogoversigt
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Eksempeltestprompter
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace-udvidelse (valgfri)
Tilføj JSON-linjer pr. trin til `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskaleringsheuristik (idé)
Hvis planen indeholder nøgleord som "optimere", "sikkerhed" eller trinlængde > 280 tegn → eskaler til større model (f.eks. `gpt-oss-20b`) kun for det trin.

### Valgfrie forbedringer

| Område | Forbedring | Værdi | Tip |
|--------|------------|-------|-----|
| Caching | Genbrug manager + klientobjekter | Lavere latenstid, mindre overhead | Brug `workshop_utils.get_client` |
| Brugsmetrikker | Fang tokens & latenstid pr. trin | Profilering & optimering | Tidsmål hver routed kald; gem i trace-liste |
| Adaptiv routing | Tillid / omkostningsbevidst | Bedre kvalitet-omkostningsafvejning | Tilføj scoring: hvis prompt > N tegn eller regex matcher domæne → eskaler til større model |
| Dynamisk kapacitetsregister | Hot reload katalog | Ingen genstart genimplementering | Indlæs `catalog.json` ved runtime; overvåg filens tidsstempel |
| Faldback-strategi | Robusthed ved fejl | Højere tilgængelighed | Prøv primær → ved undtagelse faldback-alias |
| Streaming-pipeline | Tidlig feedback | UX-forbedring | Stream hvert trin og buffer endelig forfiningsinput |
| Vektorintentionsembeds | Mere nuanceret routing | Højere intentionsnøjagtighed | Embed prompt, cluster & map centroid → kapacitet |
| Trace-eksport | Reviderbar kæde | Overholdelse/rapportering | Udsend JSON-linjer: trin, intention, model, latenstid_ms, tokens |
| Omkostningssimulering | Forudsigelse før skyen | Budgetplanlægning | Tildel skønnede omkostninger/token pr. model & aggreger pr. opgave |
| Deterministisk tilstand | Reproducerbarhed | Stabil benchmarking | Miljø: `temperature=0`, fast antal trin |

#### Eksempel på trace-struktur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Skitse til adaptiv eskalering

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot reload af modelkatalog

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

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.