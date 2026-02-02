# 6. ülés: Foundry Local – Modellek mint eszközök

## Összefoglaló

Kezeld a modelleket összetett eszközökként egy helyi AI operációs rétegben. Ez az ülés bemutatja, hogyan lehet láncolni több specializált SLM/LLM hívást, szelektíven irányítani a feladatokat, és egy egységes SDK felületet biztosítani az alkalmazások számára. Készíteni fogsz egy könnyű modellirányítót + feladat-tervezőt, integrálod egy alkalmazás szkriptbe, és felvázolod a skálázási utat az Azure AI Foundry felé a termelési munkaterhelésekhez.

## Tanulási célok

- **Modellek elképzelése** mint deklarált képességekkel rendelkező atomikus eszközök
- **Kérések irányítása** szándék / heurisztikus pontozás alapján
- **Láncolás** több lépéses feladatok között (bontás → megoldás → finomítás)
- **Egységes kliens API integrálása** a downstream alkalmazásokhoz
- **Skálázás** tervezése felhőbe (ugyanaz az OpenAI-kompatibilis szerződés)

## Előfeltételek

- 1–5. ülések elvégzése
- Több helyi modell gyorsítótárazva (pl. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Keresztplatform környezet snippet

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

Távoli/VM szolgáltatás elérése macOS-ről:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Bemutató menete (30 perc)

### 1. Eszköz képességeinek deklarálása (5 perc)

Hozd létre a `samples/06-tools/models_catalog.py` fájlt:

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


### 2. Szándék felismerés és irányítás (8 perc)

Hozd létre a `samples/06-tools/router.py` fájlt:

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


### 3. Többlépéses feladatláncolás (7 perc)

Hozd létre a `samples/06-tools/pipeline.py` fájlt:

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


### 4. Kezdő projekt: Adaptáld a `06-models-as-tools` fájlt (5 perc)

Fejlesztések:
- Streaming token támogatás hozzáadása (progresszív UI frissítés)
- Bizalmi pontozás hozzáadása: lexikai átfedés vagy prompt rubrika
- Trace JSON exportálása (szándék → modell → késleltetés → token használat)
- Gyorsítótár újrahasználat megvalósítása ismételt al-lépésekhez

### 5. Skálázási út az Azure felé (5 perc)

| Réteg | Helyi (Foundry) | Felhő (Azure AI Foundry) | Átmeneti stratégia |
|-------|-----------------|--------------------------|---------------------|
| Irányítás | Heurisztikus Python | Tartós mikroszolgáltatás | API konténerizálása és telepítése |
| Modellek | SLM-ek gyorsítótárazva | Kezelt telepítések | Helyi nevek leképezése telepítési azonosítókra |
| Megfigyelhetőség | CLI statisztikák/kézi | Központi naplózás és metrikák | Strukturált trace események hozzáadása |
| Biztonság | Csak helyi hoszt | Azure hitelesítés / hálózat | Kulcstár bevezetése titkokhoz |
| Költség | Eszköz erőforrás | Fogyasztás alapú számlázás | Költségkorlátok hozzáadása |

## Érvényesítési ellenőrzőlista

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Várható szándék-alapú modellválasztás és végső finomított kimenet.

## Hibakeresés

| Probléma | Ok | Megoldás |
|----------|----|----------|
| Minden feladat ugyanahhoz a modellhez irányítva | Gyenge szabályok | INTENT_RULES regex készlet gazdagítása |
| A pipeline középen elakad | Hiányzó modell betöltve | Futtasd a `foundry model run <model>` parancsot |
| Alacsony kimeneti összhang | Nincs finomítási fázis | Összegzés/validációs lépés hozzáadása |

## Referenciák

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry dokumentáció: https://learn.microsoft.com/azure/ai-foundry
- Prompt minőségi minták: Lásd 2. ülés

---

**Ülés időtartama**: 30 perc  
**Nehézségi szint**: Haladó

## Példa forgatókönyv és workshop térkép

| Workshop szkriptek / jegyzetfüzetek | Forgatókönyv | Célkitűzés | Adatkészlet / katalógus forrás |
|------------------------------------|--------------|------------|-------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Fejlesztői asszisztens vegyes szándékú promptok kezelésére (refaktorálás, összegzés, osztályozás) | Heurisztikus szándék → modell alias irányítás token használattal | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Többlépéses tervezés és finomítás komplex kódolási segítségnyújtási feladathoz | Bontás → specializált végrehajtás → összegzés finomítási lépés | Ugyanaz a `CATALOG`; lépések a terv kimenetéből származnak |

### Forgatókönyv narratíva
Egy mérnöki produktivitási eszköz heterogén feladatokat kap: kód refaktorálása, architekturális jegyzetek összegzése, visszajelzések osztályozása. A késleltetés és az erőforrás-felhasználás minimalizálása érdekében egy kis általános modell tervez és összegzi, egy kódra specializált modell kezeli a refaktorálást, és egy könnyű osztályozásra képes modell címkézi a visszajelzéseket. A pipeline szkript bemutatja a láncolást + finomítást; az irányító szkript az adaptív egyetlen prompt irányítást izolálja.

### Katalógus pillanatkép
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Példa teszt promptok
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace kiterjesztés (opcionális)
Adj hozzá lépésenkénti trace JSON sorokat a `models_pipeline.py` fájlhoz:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eszkalációs heurisztika (ötlet)
Ha a terv kulcsszavakat tartalmaz, mint "optimalizálás", "biztonság", vagy a lépés hossza > 280 karakter → eszkalálás nagyobb modellre (pl. `gpt-oss-20b`) csak arra a lépésre.

### Opcionális fejlesztések

| Terület | Fejlesztés | Érték | Tipp |
|---------|------------|-------|------|
| Gyorsítótárazás | Újrahasználható manager + kliens objektumok | Alacsonyabb késleltetés, kevesebb terhelés | Használj `workshop_utils.get_client` |
| Használati metrikák | Tokenek és lépésenkénti késleltetés rögzítése | Profilozás és optimalizálás | Mérd az egyes irányított hívásokat; tárold a trace listában |
| Adaptív irányítás | Bizalom / költség tudatos | Jobb minőség-költség arány | Pontozás hozzáadása: ha a prompt > N karakter vagy regex illeszkedik a domainhez → eszkalálás nagyobb modellre |
| Dinamikus képesség-regisztráció | Katalógus hot reload | Újratelepítés nélküli frissítés | Töltsd be a `catalog.json` fájlt futásidőben; figyeld a fájl időbélyegét |
| Visszaesési stratégia | Hiba esetén robusztusság | Magasabb rendelkezésre állás | Próbáld meg az elsődlegest → hiba esetén tartalék alias |
| Streaming pipeline | Korai visszajelzés | UX javítás | Streameld az egyes lépéseket és puffereld a végső finomítási bemenetet |
| Vektor szándék beágyazások | Finomabb irányítás | Magasabb szándék pontosság | Ágyazd be a promptot, klaszterezd és térképezd a centroidot → képesség |
| Trace exportálás | Auditálható lánc | Megfelelőség/jelentéskészítés | JSON sorok kibocsátása: lépés, szándék, modell, késleltetés_ms, tokenek |
| Költség szimuláció | Felhő előzetes becslés | Költségtervezés | Rendelj jelképes költséget/token modellenként és összesítsd feladatonként |
| Determinisztikus mód | Reprodukálhatóság | Stabil benchmarking | Környezet: `temperature=0`, fix lépésszám |

#### Trace struktúra példa

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptív eszkaláció vázlat

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Modellkatalógus hot reload

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

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.