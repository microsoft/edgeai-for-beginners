# Session 6: Foundry Local – Modely ako nástroje

## Abstrakt

Považujte modely za skladateľné nástroje v lokálnej AI operačnej vrstve. Táto relácia ukazuje, ako reťaziť viaceré špecializované volania SLM/LLM, selektívne smerovať úlohy a vystaviť jednotné SDK rozhranie aplikáciám. Vytvoríte ľahký router modelov + plánovač úloh, integrujete ho do skriptu aplikácie a načrtnete cestu škálovania na Azure AI Foundry pre produkčné pracovné zaťaženie.

## Ciele učenia

- **Konceptualizovať** modely ako atomické nástroje s deklarovanými schopnosťami
- **Smerovať** požiadavky na základe zámeru / heuristického skórovania
- **Reťaziť** výstupy cez viacstupňové úlohy (rozložiť → vyriešiť → zdokonaliť)
- **Integrovať** jednotné klientské API pre aplikácie
- **Škálovať** dizajn do cloudu (rovnaký OpenAI-kompatibilný kontrakt)

## Predpoklady

- Dokončené relácie 1–5
- Viaceré lokálne modely uložené (napr. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet pre multiplatformové prostredie

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

Prístup k vzdialenej službe/VM z macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo priebeh (30 min)

### 1. Deklarácia schopností nástrojov (5 min)

Vytvorte `samples/06-tools/models_catalog.py`:

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


### 2. Detekcia zámeru a smerovanie (8 min)

Vytvorte `samples/06-tools/router.py`:

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


### 3. Reťazenie viacstupňových úloh (7 min)

Vytvorte `samples/06-tools/pipeline.py`:

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


### 4. Štartovací projekt: Adaptácia `06-models-as-tools` (5 min)

Vylepšenia:
- Pridajte podporu pre streamovanie tokenov (progresívna aktualizácia UI)
- Pridajte skórovanie dôveryhodnosti: lexikálny prekryv alebo rubrika promptu
- Exportujte JSON trasovanie (zámer → model → latencia → použitie tokenov)
- Implementujte opätovné použitie cache pre opakované podúlohy

### 5. Cesta škálovania na Azure (5 min)

| Vrstva | Lokálne (Foundry) | Cloud (Azure AI Foundry) | Stratégia prechodu |
|--------|-------------------|--------------------------|--------------------|
| Smerovanie | Heuristický Python | Trvalá mikroslužba | Kontajnerizácia & nasadenie API |
| Modely | Uložené SLM | Spravované nasadenia | Mapovanie lokálnych názvov na ID nasadení |
| Pozorovateľnosť | Štatistiky CLI/manuálne | Centrálne logovanie & metriky | Pridanie štruktúrovaných trasovacích udalostí |
| Bezpečnosť | Iba lokálny hostiteľ | Azure autentifikácia / sieťovanie | Zavedenie key vault pre tajomstvá |
| Náklady | Zdroje zariadenia | Fakturácia za spotrebu | Pridanie rozpočtových obmedzení |

## Kontrolný zoznam validácie

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Očakávajte výber modelu na základe zámeru a finálny zdokonalený výstup.

## Riešenie problémov

| Problém | Príčina | Riešenie |
|---------|---------|----------|
| Všetky úlohy smerované na rovnaký model | Slabé pravidlá | Obohatiť regex sadu INTENT_RULES |
| Pipeline zlyhá v strede kroku | Chýbajúci načítaný model | Spustiť `foundry model run <model>` |
| Nízka súdržnosť výstupu | Chýba fáza zdokonalenia | Pridať fázu sumarizácie/validácie |

## Referencie

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Vzory kvality promptov: Pozrite si reláciu 2

---

**Trvanie relácie**: 30 min  
**Náročnosť**: Expert

## Ukážkový scenár & mapovanie workshopu

| Skripty workshopu / Notebooks | Scenár | Cieľ | Zdroj datasetu / katalógu |
|-------------------------------|--------|------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistent vývojára spracovávajúci zmiešané zámerové prompty (refaktorovanie, sumarizácia, klasifikácia) | Heuristický zámer → smerovanie aliasu modelu s použitím tokenov | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Viacstupňové plánovanie & zdokonalenie pre komplexnú úlohu asistencie pri kódovaní | Rozložiť → špecializovaná exekúcia → krok sumarizácie a zdokonalenia | Rovnaký `CATALOG`; kroky odvodené z výstupu plánu |

### Naratív scenára
Nástroj na zvýšenie produktivity inžinierov prijíma heterogénne úlohy: refaktorovanie kódu, sumarizácia architektonických poznámok, klasifikácia spätnej väzby. Na minimalizáciu latencie a využitia zdrojov malý všeobecný model plánuje a sumarizuje, špecializovaný model na kód sa zaoberá refaktorovaním a ľahký model schopný klasifikácie označuje spätnú väzbu. Skript pipeline demonštruje reťazenie + zdokonalenie; skript router izoluje adaptívne smerovanie jedného promptu.

### Snímka katalógu
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Príklady testovacích promptov
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Rozšírenie trasovania (voliteľné)
Pridajte riadky JSON trasovania pre každý krok v `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristika eskalácie (nápad)
Ak plán obsahuje kľúčové slová ako "optimalizovať", "bezpečnosť" alebo dĺžka kroku > 280 znakov → eskalovať na väčší model (napr. `gpt-oss-20b`) iba pre daný krok.

### Voliteľné vylepšenia

| Oblasť | Vylepšenie | Hodnota | Nápoveda |
|--------|------------|---------|----------|
| Cache | Opätovné použitie manažéra + klientských objektov | Nižšia latencia, menšia záťaž | Použite `workshop_utils.get_client` |
| Metriky používania | Zachytenie tokenov & latencie na krok | Profilovanie & optimalizácia | Zmerajte každý smerovaný hovor; uložte do zoznamu trasovania |
| Adaptívne smerovanie | Dôvera / náklady | Lepší pomer kvality a nákladov | Pridajte skórovanie: ak prompt > N znakov alebo regex zodpovedá doméne → eskalovať na väčší model |
| Dynamický register schopností | Hot reload katalógu | Bez reštartu nasadenia | Načítajte `catalog.json` za behu; sledujte časovú pečiatku súboru |
| Záložná stratégia | Robustnosť pri zlyhaniach | Vyššia dostupnosť | Skúste primárny → pri výnimke záložný alias |
| Streamovacia pipeline | Skorá spätná väzba | Zlepšenie UX | Streamujte každý krok a bufferujte vstup pre finálne zdokonalenie |
| Vektorové vkladanie zámerov | Jemnejšie smerovanie | Vyššia presnosť zámeru | Vložte prompt, zoskupte & mapujte centroid → schopnosť |
| Export trasovania | Auditovateľný reťazec | Súlad/správy | Emitujte JSON riadky: krok, zámer, model, latencia_ms, tokeny |
| Simulácia nákladov | Odhad pred cloudom | Plánovanie rozpočtu | Priraďte notional cost/token na model & agregujte na úlohu |
| Deterministický režim | Reprodukcia reprodukovateľnosti | Stabilné benchmarkovanie | Env: `temperature=0`, fixný počet krokov |

#### Príklad štruktúry trasovania

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Náčrt adaptívnej eskalácie

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot Reload katalógu modelov

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

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.