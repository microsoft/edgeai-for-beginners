<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T22:24:41+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "nl"
}
-->
# Sessie 6: Foundry Local – Modellen als Tools

## Samenvatting

Behandel modellen als samenstelbare tools binnen een lokale AI-operatielaag. Deze sessie laat zien hoe je meerdere gespecialiseerde SLM/LLM-aanroepen kunt koppelen, taken selectief kunt routeren en een uniforme SDK-interface kunt aanbieden aan applicaties. Je gaat een lichte modelrouter + taakplanner bouwen, deze integreren in een app-script en de schaalbaarheid naar Azure AI Foundry voor productieomgevingen schetsen.

## Leerdoelen

- **Conceptualiseer** modellen als atomische tools met gedefinieerde mogelijkheden
- **Routeer** verzoeken op basis van intentie / heuristische scoring
- **Koppel** outputs over meerstaps taken (decomponeren → oplossen → verfijnen)
- **Integreer** een uniforme client-API voor downstream applicaties
- **Schaal** ontwerp naar de cloud (zelfde OpenAI-compatibele contract)

## Vereisten

- Sessies 1–5 voltooid
- Meerdere lokale modellen in cache (bijv. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Cross-platform omgevingsfragment

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

Toegang tot Remote/VM-service vanaf macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Declaratie van toolmogelijkheden (5 min)

Maak `samples/06-tools/models_catalog.py`:

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


### 2. Intentiedetectie & routering (8 min)

Maak `samples/06-tools/router.py`:

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


### 3. Meerstaps taakketening (7 min)

Maak `samples/06-tools/pipeline.py`:

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


### 4. Starterproject: Pas `06-models-as-tools` aan (5 min)

Verbeteringen:
- Voeg ondersteuning voor streaming tokens toe (progressieve UI-update)
- Voeg vertrouwensscore toe: lexicale overlap of prompt-rubriek
- Exporteer trace JSON (intentie → model → latentie → tokengebruik)
- Implementeer cache-hergebruik voor herhaalde substappen

### 5. Schaalpad naar Azure (5 min)

| Laag | Lokaal (Foundry) | Cloud (Azure AI Foundry) | Transitiestrategie |
|------|------------------|--------------------------|---------------------|
| Routering | Heuristische Python | Duurzame microservice | Containeriseer & implementeer API |
| Modellen | SLM's in cache | Beheerde implementaties | Map lokale namen naar implementatie-ID's |
| Observatie | CLI-statistieken/handmatig | Centrale logging & metrics | Voeg gestructureerde trace-evenementen toe |
| Beveiliging | Alleen lokale host | Azure-authenticatie / netwerk | Introduceer key vault voor geheimen |
| Kosten | Apparaatbronnen | Verbruiksfacturering | Voeg budgetbewaking toe |

## Validatiechecklist

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
Verwacht modelselectie op basis van intentie en een verfijnde eindoutput.

## Probleemoplossing

| Probleem | Oorzaak | Oplossing |
|----------|--------|-----------|
| Alle taken worden naar hetzelfde model gerouteerd | Zwakke regels | Verrijk INTENT_RULES regex-set |
| Pipeline faalt halverwege | Ontbrekend geladen model | Voer `foundry model run <model>` uit |
| Lage outputcohesie | Geen verfijnfase | Voeg samenvattings-/validatiepassage toe |

## Referenties

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Promptkwaliteitspatronen: Zie Sessie 2

---

**Duur van de sessie**: 30 min  
**Moeilijkheidsgraad**: Expert

## Voorbeeldscenario & workshopmapping

| Workshop scripts / Notebooks | Scenario | Doel | Dataset / Catalogusbron |
|------------------------------|----------|------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Ontwikkelaarshulp bij gemengde intentieprompts (refactoren, samenvatten, classificeren) | Heuristische intentie → modelalias-routering met tokengebruik | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Meerstaps planning & verfijning voor complexe coderingstaken | Decomponeren → gespecialiseerde uitvoering → samenvattingsverfijningsstap | Zelfde `CATALOG`; stappen afgeleid van planoutput |

### Scenarioverhaal
Een productiviteitstool voor engineers ontvangt heterogene taken: code refactoren, architectuurnotities samenvatten, feedback classificeren. Om latentie en resourcegebruik te minimaliseren, plant en vat een klein algemeen model samen, een code-gespecialiseerd model behandelt refactoren, en een lichtgewicht classificatiemodel labelt feedback. Het pipelinescript demonstreert ketening + verfijning; het routerscript isoleert adaptieve routering van enkele prompts.

### Catalogusoverzicht
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Voorbeeldtestprompts
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace-uitbreiding (optioneel)
Voeg per stap trace JSON-regels toe voor `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Escalatieheuristiek (idee)
Als het plan trefwoorden bevat zoals "optimaliseren", "beveiliging", of staplengte > 280 tekens → escaleren naar groter model (bijv. `gpt-oss-20b`) alleen voor die stap.

### Optionele verbeteringen

| Gebied | Verbetering | Waarde | Hint |
|-------|-------------|--------|------|
| Caching | Hergebruik manager + clientobjecten | Lagere latentie, minder overhead | Gebruik `workshop_utils.get_client` |
| Gebruiksstatistieken | Tokens & latentie per stap vastleggen | Profilering & optimalisatie | Meet elke gerouteerde oproep; sla op in tracelijst |
| Adaptieve routering | Vertrouwen / kostenbewust | Betere kwaliteit-kostenafweging | Voeg scoring toe: als prompt > N tekens of regex matcht domein → escaleren naar groter model |
| Dynamisch capaciteitsregister | Catalogus hot reload | Geen herstart herimplementatie | Laad `catalog.json` tijdens runtime; controleer bestandstijdstempel |
| Fallbackstrategie | Robuustheid bij storingen | Hogere beschikbaarheid | Probeer primair → bij uitzondering fallback-alias |
| Streamingpipeline | Vroege feedback | UX-verbetering | Stream elke stap en buffer de uiteindelijke verfijningsinput |
| Vector intentie-embeddings | Meer genuanceerde routering | Hogere intentienauwkeurigheid | Embed prompt, cluster & map centroid → capaciteit |
| Trace-export | Auditeerbare keten | Compliance/rapportage | Exporteer JSON-regels: stap, intentie, model, latentie_ms, tokens |
| Kostenraming | Schatting pre-cloud | Budgetplanning | Wijs notionele kosten/token per model toe & aggregeer per taak |
| Deterministische modus | Reproduceerbaarheid | Stabiele benchmarking | Omgeving: `temperature=0`, vast aantal stappen |

#### Voorbeeld van tracestructuur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Schets voor adaptieve escalatie

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot reload van modelcatalogus

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

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.