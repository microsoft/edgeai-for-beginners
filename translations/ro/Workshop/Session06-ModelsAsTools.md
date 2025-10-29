<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T23:12:17+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ro"
}
-->
# Sesiunea 6: Foundry Local – Modele ca Instrumente

## Rezumat

Tratați modelele ca instrumente compozabile într-un strat operațional AI local. Această sesiune arată cum să conectați mai multe apeluri specializate SLM/LLM, să direcționați selectiv sarcinile și să expuneți o suprafață SDK unificată aplicațiilor. Veți construi un router de modele ușor + un planificator de sarcini, îl veți integra într-un script de aplicație și veți contura calea de scalare către Azure AI Foundry pentru sarcini de producție.

## Obiective de învățare

- **Conceptualizați** modelele ca instrumente atomice cu capabilități declarate
- **Direcționați** cererile pe baza intenției / scorului euristic
- **Conectați** ieșirile în sarcini multi-pas (decompoziție → rezolvare → rafinare)
- **Integrați** un API client unificat pentru aplicațiile downstream
- **Scalați** designul către cloud (același contract compatibil OpenAI)

## Cerințe preliminare

- Finalizarea sesiunilor 1–5
- Mai multe modele locale în cache (de exemplu, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Fragment de mediu cross-platform

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

Acces la servicii remote/VM de pe macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flux Demo (30 min)

### 1. Declarația capabilităților instrumentului (5 min)

Creați `samples/06-tools/models_catalog.py`:

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


### 2. Detectarea intenției și direcționare (8 min)

Creați `samples/06-tools/router.py`:

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


### 3. Conectarea sarcinilor multi-pas (7 min)

Creați `samples/06-tools/pipeline.py`:

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


### 4. Proiect de început: Adaptarea `06-models-as-tools` (5 min)

Îmbunătățiri:
- Adăugați suport pentru streaming de token-uri (actualizare progresivă a interfeței)
- Adăugați scorarea încrederii: suprapunere lexicală sau rubrică de prompt
- Exportați JSON de urmărire (intenție → model → latență → utilizare token-uri)
- Implementați reutilizarea cache-ului pentru subpași repetați

### 5. Calea de scalare către Azure (5 min)

| Strat | Local (Foundry) | Cloud (Azure AI Foundry) | Strategie de tranziție |
|-------|-----------------|--------------------------|-------------------------|
| Direcționare | Python euristic | Microserviciu durabil | Containerizare și implementare API |
| Modele | SLM-uri în cache | Implementări gestionate | Maparea numelor locale la ID-uri de implementare |
| Observabilitate | Statistici CLI/manual | Jurnalizare centrală și metrici | Adăugarea evenimentelor structurate de urmărire |
| Securitate | Doar gazdă locală | Autentificare Azure / rețea | Introducerea unui seif de chei pentru secrete |
| Cost | Resurse dispozitiv | Facturare consum | Adăugarea limitelor de buget |

## Lista de verificare pentru validare

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Așteptați selecția modelului bazată pe intenție și ieșirea finală rafinată.

## Depanare

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| Toate sarcinile direcționate către același model | Reguli slabe | Îmbunătățiți setul de regex INTENT_RULES |
| Pipeline-ul eșuează la mijlocul pasului | Model lipsă încărcat | Rulați `foundry model run <model>` |
| Coeziune scăzută a ieșirii | Fază de rafinare lipsă | Adăugați un pas de sumarizare/validare |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentație Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Modele de calitate pentru prompturi: Vezi Sesiunea 2

---

**Durata sesiunii**: 30 min  
**Dificultate**: Expert

## Scenariu de exemplu și mapare workshop

| Scripturi / Notebooks Workshop | Scenariu | Obiectiv | Sursă Dataset / Catalog |
|--------------------------------|----------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistent pentru dezvoltatori care gestionează prompturi cu intenții mixte (refactorizare, sumarizare, clasificare) | Intenție euristică → direcționare alias model cu utilizare token-uri | `CATALOG` inline + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planificare multi-pas și rafinare pentru sarcini complexe de asistență la codare | Decompoziție → execuție specializată → pas de rafinare sumarizare | Același `CATALOG`; pași derivați din ieșirea planului |

### Narațiunea scenariului
Un instrument de productivitate pentru inginerie primește sarcini eterogene: refactorizare cod, sumarizare note arhitecturale, clasificare feedback. Pentru a minimiza latența și utilizarea resurselor, un model general mic planifică și sumarizează, un model specializat pe cod se ocupă de refactorizare, iar un model ușor capabil de clasificare etichetează feedback-ul. Scriptul pipeline demonstrează conectarea + rafinarea; scriptul router izolează direcționarea adaptivă a unui singur prompt.

### Snapshot Catalog
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Exemple de prompturi de test
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Extensie de urmărire (opțional)
Adăugați linii JSON de urmărire per-pas pentru `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Euristică de escaladare (idee)
Dacă planul conține cuvinte cheie precum "optimize", "security" sau lungimea pasului > 280 caractere → escaladare la un model mai mare (de exemplu, `gpt-oss-20b`) doar pentru acel pas.

### Îmbunătățiri opționale

| Zonă | Îmbunătățire | Valoare | Indiciu |
|------|--------------|---------|---------|
| Cache | Reutilizarea managerului + obiectelor client | Latență mai mică, mai puțin overhead | Utilizați `workshop_utils.get_client` |
| Metrici de utilizare | Capturați token-uri și latența per-pas | Profilare și optimizare | Cronometrați fiecare apel direcționat; stocați în lista de urmărire |
| Direcționare adaptivă | Conștient de încredere / cost | Compromis calitate-cost mai bun | Adăugați scorare: dacă promptul > N caractere sau regex-ul se potrivește domeniului → escaladare la model mai mare |
| Registru dinamic de capabilități | Catalog reîncărcabil dinamic | Fără redeploy la restart | Încărcați `catalog.json` la runtime; urmăriți timestamp-ul fișierului |
| Strategie de fallback | Robusteză în caz de eșecuri | Disponibilitate mai mare | Încercați primar → pe excepție fallback alias |
| Pipeline streaming | Feedback timpuriu | Îmbunătățire UX | Stream fiecare pas și buffer pentru intrarea finală de rafinare |
| Vectori de intenție | Direcționare mai nuanțată | Precizie mai mare a intenției | Embed prompt, cluster și mapare centroid → capabilitate |
| Export de urmărire | Lanț auditabil | Conformitate/raportare | Emiteți linii JSON: pas, intenție, model, latență_ms, token-uri |
| Simulare cost | Estimare pre-cloud | Planificare buget | Atribuiți costuri notionale/token per model și agregați per sarcină |
| Mod determinist | Reproducibilitate | Benchmarking stabil | Env: `temperature=0`, număr fix de pași |

#### Exemplu de structură de urmărire

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Schiță de escaladare adaptivă

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Reîncărcare dinamică a catalogului de modele

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

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.