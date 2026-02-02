# Seja 6: Foundry Local – Modeli kot orodja

## Povzetek

Obravnavajte modele kot sestavljiva orodja znotraj lokalne AI operativne plasti. Ta seja prikazuje, kako povezati več specializiranih klicev SLM/LLM, selektivno usmerjati naloge in aplikacijam omogočiti enotno SDK površino. Zgradili boste lahek usmerjevalnik modelov + načrtovalec nalog, ga integrirali v skript aplikacije in začrtali pot za skaliranje na Azure AI Foundry za produkcijske obremenitve.

## Cilji učenja

- **Konceptualizirajte** modele kot osnovna orodja z deklariranimi zmožnostmi
- **Usmerjajte** zahteve na podlagi namena / heurističnega ocenjevanja
- **Povezujte** izhode skozi večstopenjske naloge (razčlenitev → rešitev → izboljšava)
- **Integrirajte** enoten API za odjemalce za aplikacije
- **Skalirajte** zasnovo v oblak (isti OpenAI-kompatibilni pogodbeni okvir)

## Predpogoji

- Zaključene seje 1–5
- Več lokalnih modelov predpomnjenih (npr. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet za okolje na več platformah

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

Oddaljen dostop/VM storitev iz macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Potek demonstracije (30 min)

### 1. Deklaracija zmožnosti orodja (5 min)

Ustvarite `samples/06-tools/models_catalog.py`:

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


### 2. Zaznavanje namena in usmerjanje (8 min)

Ustvarite `samples/06-tools/router.py`:

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


### 3. Povezovanje večstopenjskih nalog (7 min)

Ustvarite `samples/06-tools/pipeline.py`:

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


### 4. Začetni projekt: Prilagodite `06-models-as-tools` (5 min)

Izboljšave:
- Dodajte podporo za pretok tokenov (progresivna posodobitev UI)
- Dodajte ocenjevanje zaupanja: leksikalno prekrivanje ali ocenjevalni kriterij za poziv
- Izvozite sled JSON (namen → model → zakasnitev → uporaba tokenov)
- Implementirajte ponovno uporabo predpomnilnika za ponavljajoče se podkorake

### 5. Pot za skaliranje na Azure (5 min)

| Plast | Lokalno (Foundry) | Oblak (Azure AI Foundry) | Strategija prehoda |
|-------|-------------------|--------------------------|---------------------|
| Usmerjanje | Heuristični Python | Trajnostna mikrostoritev | Kontejnerizirajte in uvedite API |
| Modeli | Predpomnjeni SLM-ji | Upravljane uvedbe | Preslikajte lokalna imena v ID-je uvedb |
| Opazovanje | Statistika CLI/ročna | Centralizirano beleženje in metrike | Dodajte strukturirane sledilne dogodke |
| Varnost | Samo lokalni gostitelj | Azure avtentikacija / omrežje | Uvedite ključni trezor za skrivnosti |
| Stroški | Viri naprave | Obračunavanje porabe | Dodajte varovalke proračuna |

## Preveritveni seznam za validacijo

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Pričakujte izbiro modela na podlagi namena in končni izboljšan izhod.

## Odpravljanje težav

| Težava | Vzrok | Rešitev |
|--------|-------|---------|
| Vse naloge usmerjene na isti model | Šibka pravila | Obogatite regex niz INTENT_RULES |
| Cevovod se ustavi na sredini koraka | Manjka naložen model | Zaženite `foundry model run <model>` |
| Nizka kohezija izhoda | Brez faze izboljšave | Dodajte fazo povzetka/validacije |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Vzorci kakovosti pozivov: Glejte sejo 2

---

**Trajanje seje**: 30 min  
**Težavnost**: Strokovno

## Vzorec scenarija in preslikava delavnice

| Skripti / Zvezki delavnice | Scenarij | Cilj | Vir podatkov / kataloga |
|----------------------------|----------|------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Pomočnik razvijalca, ki obravnava mešane namenske pozive (preoblikovanje, povzetek, razvrščanje) | Heuristično usmerjanje namena → modelni alias z uporabo tokenov | Vgrajen `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Načrtovanje in izboljšanje v več korakih za kompleksno nalogo pomoči pri kodiranju | Razčlenitev → specializirana izvedba → korak povzetka in izboljšave | Isti `CATALOG`; koraki izpeljani iz izhoda načrta |

### Narativ scenarija
Orodje za produktivnost inženirjev prejema heterogene naloge: preoblikovanje kode, povzetek arhitekturnih opomb, razvrščanje povratnih informacij. Za zmanjšanje zakasnitve in porabe virov majhen splošni model načrtuje in povzame, model specializiran za kodo obravnava preoblikovanje, lahek model za razvrščanje pa označuje povratne informacije. Skript cevovoda prikazuje povezovanje + izboljšanje; skript usmerjevalnika izolira prilagodljivo usmerjanje z enim pozivom.

### Posnetek kataloga
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Primeri testnih pozivov
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Razširitev sledi (neobvezno)
Dodajte sled JSON vrstic za vsak korak v `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristika za eskalacijo (ideja)
Če načrt vsebuje ključne besede, kot so "optimizacija", "varnost", ali dolžina koraka > 280 znakov → eskalirajte na večji model (npr. `gpt-oss-20b`) samo za ta korak.

### Neobvezne izboljšave

| Področje | Izboljšava | Vrednost | Namig |
|----------|------------|----------|-------|
| Predpomnjenje | Ponovna uporaba upravitelja + odjemalskih objektov | Nižja zakasnitev, manjša obremenitev | Uporabite `workshop_utils.get_client` |
| Metrike uporabe | Zajemanje tokenov in zakasnitve na korak | Profiliranje in optimizacija | Časovno merite vsak usmerjen klic; shranite v seznam sledi |
| Prilagodljivo usmerjanje | Zaupanje / stroškovna zavest | Boljša kakovostna-stroškovna uravnoteženost | Dodajte ocenjevanje: če je poziv > N znakov ali regex ustreza domeni → eskalirajte na večji model |
| Dinamični register zmožnosti | Vroče nalaganje kataloga | Brez ponovnega zagona uvedbe | Naložite `catalog.json` med izvajanjem; spremljajte časovno oznako datoteke |
| Strategija rezervne možnosti | Robustnost ob napakah | Večja razpoložljivost | Poskusite primarno → ob izjemi rezervni alias |
| Cevovod za pretok | Zgodnje povratne informacije | Izboljšanje uporabniške izkušnje | Pretakajte vsak korak in medpomnilnik za končni vhod za izboljšavo |
| Vektorske namenske vdelave | Bolj natančno usmerjanje | Višja natančnost namena | Vdelajte poziv, razvrstite in preslikajte centroid → zmožnost |
| Izvoz sledi | Verižna revizija | Skladnost/poročanje | Oddajte JSON vrstice: korak, namen, model, zakasnitev_ms, tokeni |
| Simulacija stroškov | Ocena pred oblakom | Načrtovanje proračuna | Dodelite domnevne stroške/token na model in jih združite na nalogo |
| Deterministični način | Reproducibilnost | Stabilno primerjanje | Okolje: `temperature=0`, fiksno število korakov |

#### Primer strukture sledi

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Skica prilagodljive eskalacije

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Vroče nalaganje kataloga modelov

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

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.