# Sesjon 6: Foundry Local – Modeller som Verktøy

## Sammendrag

Behandle modeller som sammensatte verktøy innenfor et lokalt AI-operativlag. Denne sesjonen viser hvordan man kan kjede flere spesialiserte SLM/LLM-kall, selektivt rute oppgaver, og eksponere en enhetlig SDK-overflate til applikasjoner. Du vil bygge en lettvekts modellruter + oppgaveplanlegger, integrere den i et appskript, og skissere skaleringsveien til Azure AI Foundry for produksjonsarbeidsbelastninger.

## Læringsmål

- **Konseptualisere** modeller som atomære verktøy med deklarerte kapabiliteter
- **Rute** forespørsler basert på intensjon / heuristisk vurdering
- **Kjede** utdata på tvers av oppgaver i flere steg (dekomponere → løse → forbedre)
- **Integrere** en enhetlig klient-API for nedstrøms applikasjoner
- **Skalere** design til skyen (samme OpenAI-kompatible kontrakt)

## Forutsetninger

- Sesjoner 1–5 fullført
- Flere lokale modeller lagret (f.eks., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Tverrplattform Miljøutdrag

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

Fjern-/VM-tjenestetilgang fra macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flyt (30 min)

### 1. Deklarasjon av Verktøykapasitet (5 min)

Opprett `samples/06-tools/models_catalog.py`:

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


### 2. Intensjonsdeteksjon og Ruting (8 min)

Opprett `samples/06-tools/router.py`:

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


### 3. Kjeding av Oppgaver i Flere Steg (7 min)

Opprett `samples/06-tools/pipeline.py`:

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


### 4. Startprosjekt: Tilpass `06-models-as-tools` (5 min)

Forbedringer:
- Legg til støtte for streaming av tokens (progressiv UI-oppdatering)
- Legg til tillitsscore: leksikalsk overlapp eller prompt-rubrik
- Eksporter sporings-JSON (intensjon → modell → ventetid → tokenbruk)
- Implementer gjenbruk av cache for gjentatte delsteg

### 5. Skaleringsvei til Azure (5 min)

| Lag | Lokalt (Foundry) | Skyen (Azure AI Foundry) | Overgangsstrategi |
|-----|------------------|--------------------------|--------------------|
| Ruting | Heuristisk Python | Holdbar mikrotjeneste | Containeriser & deploy API |
| Modeller | SLMs lagret | Administrerte distribusjoner | Kartlegg lokale navn til distribusjons-IDer |
| Observabilitet | CLI-statistikk/manuell | Sentral logging & metrikker | Legg til strukturerte sporingshendelser |
| Sikkerhet | Kun lokal vert | Azure-autentisering / nettverk | Introduksjon av nøkkelhvelv for hemmeligheter |
| Kostnad | Enhetsressurs | Forbruksfakturering | Legg til budsjettkontroller |

## Valideringssjekkliste

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Forvent intensjonsbasert modellvalg og endelig forbedret utdata.

## Feilsøking

| Problem | Årsak | Løsning |
|---------|-------|---------|
| Alle oppgaver rutet til samme modell | Svake regler | Berik INTENT_RULES regex-sett |
| Pipeline feiler midt i et steg | Manglende modell lastet | Kjør `foundry model run <model>` |
| Lav utdata-sammenheng | Ingen forbedringsfase | Legg til oppsummerings-/valideringspass |

## Referanser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Kvalitetsmønstre: Se Sesjon 2

---

**Sesjonsvarighet**: 30 min  
**Vanskelighetsgrad**: Ekspert

## Eksempelscenario & Workshop Kartlegging

| Workshop Skript / Notebooks | Scenario | Mål | Datasett / Katalogkilde |
|-----------------------------|----------|-----|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Utviklerassistent som håndterer blandede intensjonsforespørsler (refaktorere, oppsummere, klassifisere) | Heuristisk intensjon → modellalias-ruting med tokenbruk | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planlegging i flere steg & forbedring for kompleks oppgave med kodeassistanse | Dekomponere → spesialisert utførelse → oppsummeringsforbedringssteg | Samme `CATALOG`; steg avledet fra planutdata |

### Scenariofortelling
Et verktøy for ingeniørproduktivitet mottar heterogene oppgaver: refaktorere kode, oppsummere arkitektoniske notater, klassifisere tilbakemeldinger. For å minimere ventetid & ressursbruk, planlegger og oppsummerer en liten generell modell, en kode-spesialisert modell håndterer refaktorering, og en lettvekts klassifiseringsmodell merker tilbakemeldinger. Pipeline-skriptet demonstrerer kjeding + forbedring; router-skriptet isolerer adaptiv enkel-prompt-ruting.

### Katalogoversikt
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Eksempel Testprompter
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Sporingsutvidelse (Valgfritt)
Legg til sporings-JSON-linjer per steg for `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskaleringsheuristikk (Ide)
Hvis planen inneholder nøkkelord som "optimalisere", "sikkerhet", eller steglengde > 280 tegn → eskaler til større modell (f.eks., `gpt-oss-20b`) kun for det steget.

### Valgfrie Forbedringer

| Område | Forbedring | Verdi | Hint |
|--------|------------|-------|------|
| Caching | Gjenbruk manager + klientobjekter | Lavere ventetid, mindre overhead | Bruk `workshop_utils.get_client` |
| Bruksmetrikker | Fang tokens & ventetid per steg | Profilering & optimalisering | Tid hver rutet kall; lagre i sporingsliste |
| Adaptiv Ruting | Tillit / kostnadsbevisst | Bedre kvalitet-kostnadsforhold | Legg til scoring: hvis prompt > N tegn eller regex matcher domene → eskaler til større modell |
| Dynamisk Kapabilitetsregister | Hot reload katalog | Ingen omstart eller ny distribusjon | Last `catalog.json` ved runtime; overvåk filens tidsstempel |
| Fallback Strategi | Robusthet ved feil | Høyere tilgjengelighet | Prøv primær → ved unntak fallback-alias |
| Streaming Pipeline | Tidlig tilbakemelding | Forbedret brukeropplevelse | Stream hvert steg og buffer endelig forbedringsinput |
| Vektorintensjons-embedding | Mer nyansert ruting | Høyere intensjonsnøyaktighet | Embed prompt, cluster & map centroid → kapabilitet |
| Sporingsutdrag | Auditerbar kjede | Samsvar/rapportering | Emit JSON-linjer: steg, intensjon, modell, ventetid_ms, tokens |
| Kostnadssimulering | Estimering før skyen | Budsjettplanlegging | Tildel nominell kostnad/token per modell & aggreger per oppgave |
| Deterministisk Modus | Repro-reproduserbarhet | Stabil benchmarking | Miljø: `temperature=0`, fast antall steg |

#### Eksempel på Sporingsstruktur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptiv Eskaleringsskisse

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Modellkatalog Hot Reload

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
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.