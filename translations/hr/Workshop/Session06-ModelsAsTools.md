# Sesija 6: Foundry Local – Modeli kao alati

## Sažetak

Tretirajte modele kao sastavljive alate unutar lokalnog AI operativnog sloja. Ova sesija pokazuje kako povezati više specijaliziranih SLM/LLM poziva, selektivno usmjeravati zadatke i izložiti objedinjenu SDK površinu aplikacijama. Izradit ćete lagani usmjerivač modela + planer zadataka, integrirati ga u skriptu aplikacije i izložiti put skaliranja prema Azure AI Foundry za produkcijske radne opterećenja.

## Ciljevi učenja

- **Konceptualizirati** modele kao osnovne alate s deklariranim sposobnostima
- **Usmjeravati** zahtjeve na temelju namjere / heurističkog bodovanja
- **Povezivati** izlaze kroz zadatke u više koraka (razložiti → riješiti → doraditi)
- **Integrirati** objedinjeni klijentski API za aplikacije
- **Skalirati** dizajn u oblak (isti ugovor kompatibilan s OpenAI)

## Preduvjeti

- Završene sesije 1–5
- Više lokalnih modela predmemorirano (npr. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet za više platformi

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

Pristup udaljenoj/VM usluzi s macOS-a:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Tijek demonstracije (30 min)

### 1. Deklaracija sposobnosti alata (5 min)

Kreirajte `samples/06-tools/models_catalog.py`:

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


### 2. Detekcija namjere i usmjeravanje (8 min)

Kreirajte `samples/06-tools/router.py`:

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


### 3. Povezivanje zadataka u više koraka (7 min)

Kreirajte `samples/06-tools/pipeline.py`:

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


### 4. Početni projekt: Prilagodite `06-models-as-tools` (5 min)

Poboljšanja:
- Dodajte podršku za tokene u stvarnom vremenu (progresivno ažuriranje UI-a)
- Dodajte bodovanje povjerenja: leksičko preklapanje ili rubrika upita
- Izvezite JSON trag (namjera → model → kašnjenje → korištenje tokena)
- Implementirajte ponovno korištenje predmemorije za ponovljene podkorake

### 5. Put skaliranja prema Azure (5 min)

| Sloj | Lokalno (Foundry) | Oblak (Azure AI Foundry) | Strategija prijelaza |
|------|--------------------|--------------------------|-----------------------|
| Usmjeravanje | Heuristički Python | Trajni mikroservis | Kontejnerizirajte i implementirajte API |
| Modeli | Predmemorirani SLM-ovi | Upravljane implementacije | Mapirajte lokalna imena na ID-ove implementacije |
| Promatranje | CLI statistika/ručno | Centralizirano logiranje i metrike | Dodajte strukturirane događaje traga |
| Sigurnost | Samo lokalni host | Azure autentifikacija / mreža | Uvedite ključni trezor za tajne |
| Trošak | Resursi uređaja | Naplata po potrošnji | Dodajte ograničenja proračuna |

## Popis za provjeru valjanosti

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Očekujte odabir modela temeljen na namjeri i konačni doradeni izlaz.

## Rješavanje problema

| Problem | Uzrok | Rješenje |
|---------|-------|----------|
| Svi zadaci usmjereni na isti model | Slaba pravila | Obogatite regex skup INTENT_RULES |
| Neuspjeh cjevovoda u srednjem koraku | Nedostaje učitani model | Pokrenite `foundry model run <model>` |
| Niska kohezija izlaza | Nema faze dorade | Dodajte fazu sažimanja/validacije |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry dokumentacija: https://learn.microsoft.com/azure/ai-foundry
- Uzorci kvalitete upita: Pogledajte sesiju 2

---

**Trajanje sesije**: 30 min  
**Težina**: Ekspert

## Primjer scenarija i mapiranje radionice

| Skripte / Bilježnice radionice | Scenarij | Cilj | Izvor podataka / kataloga |
|--------------------------------|----------|------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistent za razvoj koji obrađuje upite mješovite namjere (refaktoriranje, sažimanje, klasifikacija) | Heurističko usmjeravanje namjere → alias modela s korištenjem tokena | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planiranje u više koraka i dorada za složeni zadatak pomoći kodiranju | Razlaganje → specijalizirana izvedba → korak dorade sažimanja | Isti `CATALOG`; koraci izvedeni iz izlaza plana |

### Narativ scenarija
Alat za produktivnost inženjeringa prima heterogene zadatke: refaktoriranje koda, sažimanje bilješki o arhitekturi, klasifikacija povratnih informacija. Kako bi se smanjila latencija i korištenje resursa, mali opći model planira i sažima, model specijaliziran za kodiranje obrađuje refaktoriranje, a lagani model za klasifikaciju označava povratne informacije. Skripta cjevovoda demonstrira povezivanje + doradu; skripta usmjerivača izolira adaptivno usmjeravanje jednim upitom.

### Snimka kataloga
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Primjeri testnih upita
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Proširenje traga (opcionalno)
Dodajte linije JSON traga po koraku za `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristika eskalacije (ideja)
Ako plan sadrži ključne riječi poput "optimizacija", "sigurnost" ili duljina koraka > 280 znakova → eskalirajte na veći model (npr. `gpt-oss-20b`) samo za taj korak.

### Opcionalna poboljšanja

| Područje | Poboljšanje | Vrijednost | Savjet |
|----------|-------------|------------|--------|
| Predmemoriranje | Ponovno korištenje objekata upravitelja + klijenta | Niža latencija, manji trošak | Koristite `workshop_utils.get_client` |
| Metrike korištenja | Snimite tokene i kašnjenje po koraku | Profiliranje i optimizacija | Mjerite svaki poziv usmjerenja; spremite u popis traga |
| Adaptivno usmjeravanje | Svjesno povjerenja / troškova | Bolji omjer kvalitete i troškova | Dodajte bodovanje: ako upit > N znakova ili regex odgovara domeni → eskalirajte na veći model |
| Dinamički registar sposobnosti | Vruće učitavanje kataloga | Bez ponovnog pokretanja implementacije | Učitajte `catalog.json` u vrijeme izvođenja; pratite vremensku oznaku datoteke |
| Strategija povratka | Robusnost u slučaju neuspjeha | Veća dostupnost | Pokušajte primarno → u slučaju iznimke povratni alias |
| Streaming cjevovod | Rani povratni podaci | Poboljšanje UX-a | Streamajte svaki korak i međuspremnik za konačni ulaz dorade |
| Vektorske namjenske ugradnje | Preciznije usmjeravanje | Veća točnost namjere | Ugradite upit, grupirajte i mapirajte centroid → sposobnost |
| Izvoz traga | Auditivni lanac | Sukladnost/izvještavanje | Emitirajte JSON linije: korak, namjera, model, kašnjenje_ms, tokeni |
| Simulacija troškova | Procjena prije oblaka | Planiranje proračuna | Dodijelite nominalni trošak/token po modelu i agregirajte po zadatku |
| Deterministički način | Reproducibilnost | Stabilno testiranje | Okruženje: `temperature=0`, fiksni broj koraka |

#### Primjer strukture traga

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Skica adaptivne eskalacije

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Vruće učitavanje kataloga modela

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

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.