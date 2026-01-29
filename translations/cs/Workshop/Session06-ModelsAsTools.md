# Sezení 6: Foundry Local – Modely jako nástroje

## Abstrakt

Považujte modely za složitelné nástroje uvnitř lokální vrstvy AI. Toto sezení ukazuje, jak propojit více specializovaných SLM/LLM volání, selektivně směrovat úkoly a zpřístupnit jednotné SDK rozhraní aplikacím. Vytvoříte lehký router modelů + plánovač úkolů, integrujete jej do skriptu aplikace a nastíníte cestu ke škálování na Azure AI Foundry pro produkční zátěže.

## Cíle učení

- **Pochopit** modely jako atomické nástroje s deklarovanými schopnostmi
- **Směrovat** požadavky na základě záměru / heuristického skórování
- **Propojovat** výstupy napříč vícekrokovými úkoly (rozložit → vyřešit → zpřesnit)
- **Integrovat** jednotné API klienta pro aplikace
- **Škálovat** návrh do cloudu (stejný OpenAI-kompatibilní kontrakt)

## Předpoklady

- Dokončené sezení 1–5
- Více lokálních modelů uložených (např. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Ukázka prostředí napříč platformami

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

Vzdálený přístup / přístup k VM službě z macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Průběh ukázky (30 min)

### 1. Deklarace schopností nástrojů (5 min)

Vytvořte `samples/06-tools/models_catalog.py`:

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


### 2. Detekce záměru a směrování (8 min)

Vytvořte `samples/06-tools/router.py`:

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


### 3. Propojování vícekrokových úkolů (7 min)

Vytvořte `samples/06-tools/pipeline.py`:

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


### 4. Startovací projekt: Adaptace `06-models-as-tools` (5 min)

Vylepšení:
- Přidání podpory streamování tokenů (progresivní aktualizace UI)
- Přidání skórování důvěryhodnosti: lexikální překryv nebo rubrika promptu
- Export trace JSON (záměr → model → latence → využití tokenů)
- Implementace opětovného využití cache pro opakované podkroky

### 5. Cesta ke škálování na Azure (5 min)

| Vrstva | Lokální (Foundry) | Cloud (Azure AI Foundry) | Strategie přechodu |
|--------|-------------------|--------------------------|---------------------|
| Směrování | Heuristický Python | Odolný mikroslužba | Kontejnerizace & nasazení API |
| Modely | Uložené SLM | Spravované nasazení | Mapování lokálních názvů na ID nasazení |
| Pozorovatelnost | CLI statistiky / manuální | Centrální logování & metriky | Přidání strukturovaných trace událostí |
| Bezpečnost | Pouze lokální host | Azure autentizace / síťování | Zavedení key vault pro tajné klíče |
| Náklady | Zdroje zařízení | Účtování spotřeby | Přidání rozpočtových limitů |

## Kontrolní seznam validace

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Očekávejte výběr modelu na základě záměru a finální zpřesněný výstup.

## Řešení problémů

| Problém | Příčina | Řešení |
|---------|---------|--------|
| Všechny úkoly směrovány na stejný model | Slabá pravidla | Obohaťte regex sadu INTENT_RULES |
| Pipeline selže uprostřed kroku | Chybějící načtený model | Spusťte `foundry model run <model>` |
| Nízká soudržnost výstupu | Chybí fáze zpřesnění | Přidejte fázi sumarizace / validace |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentace Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Vzory kvality promptů: Viz sezení 2

---

**Délka sezení**: 30 min  
**Obtížnost**: Expert

## Ukázkový scénář & mapování workshopu

| Skripty workshopu / Notebooky | Scénář | Cíl | Zdroj datasetu / katalogu |
|-------------------------------|--------|-----|----------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistent vývojáře zpracovávající smíšené záměry promptů (refaktorování, sumarizace, klasifikace) | Heuristické směrování záměru → alias modelu s využitím tokenů | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Vícekrokové plánování & zpřesnění pro komplexní úkol asistence při kódování | Rozložit → specializované provedení → krok zpřesnění sumarizace | Stejný `CATALOG`; kroky odvozené z výstupu plánu |

### Narativ scénáře
Nástroj pro zvýšení produktivity inženýrů přijímá heterogenní úkoly: refaktorování kódu, sumarizace architektonických poznámek, klasifikace zpětné vazby. Pro minimalizaci latence & využití zdrojů malý obecný model plánuje a sumarizuje, model specializovaný na kód se stará o refaktorování a lehký model schopný klasifikace označuje zpětnou vazbu. Skript pipeline demonstruje propojení + zpřesnění; skript routeru izoluje adaptivní směrování jednoho promptu.

### Snímek katalogu
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Ukázkové testovací prompty
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Rozšíření trace (volitelné)
Přidejte JSON řádky trace pro každý krok do `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristika eskalace (nápad)
Pokud plán obsahuje klíčová slova jako "optimalizace", "bezpečnost" nebo délka kroku > 280 znaků → eskalujte na větší model (např. `gpt-oss-20b`) pouze pro tento krok.

### Volitelná vylepšení

| Oblast | Vylepšení | Hodnota | Nápověda |
|--------|-----------|---------|----------|
| Cache | Opětovné použití objektů manažera + klienta | Nižší latence, menší režie | Použijte `workshop_utils.get_client` |
| Metriky využití | Zachycení tokenů & latence na krok | Profilování & optimalizace | Měřte každý směrovaný hovor; ukládejte do seznamu trace |
| Adaptivní směrování | Důvěryhodnost / nákladová efektivita | Lepší poměr kvality a nákladů | Přidejte skórování: pokud prompt > N znaků nebo regex odpovídá doméně → eskalujte na větší model |
| Dynamický registr schopností | Hot reload katalogu | Bez restartu / znovunasazení | Načtěte `catalog.json` za běhu; sledujte časovou značku souboru |
| Strategie zálohy | Robustnost při selhání | Vyšší dostupnost | Zkuste primární → při výjimce záložní alias |
| Streamovací pipeline | Rychlá zpětná vazba | Zlepšení UX | Streamujte každý krok a bufferujte vstup pro finální zpřesnění |
| Vektorové embedování záměru | Jemnější směrování | Vyšší přesnost záměru | Embedujte prompt, seskupte & mapujte centroid → schopnost |
| Export trace | Auditovatelný řetězec | Soulad / reportování | Emitujte JSON řádky: krok, záměr, model, latence_ms, tokeny |
| Simulace nákladů | Odhad před nasazením do cloudu | Plánování rozpočtu | Přiřaďte nominální náklady/token na model & agregujte na úkol |
| Deterministický režim | Reprodukovatelnost | Stabilní benchmarking | Env: `temperature=0`, pevný počet kroků |

#### Příklad struktury trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Náčrt adaptivní eskalace

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot reload katalogu modelů

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

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.