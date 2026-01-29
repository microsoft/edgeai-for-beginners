# 3. szekció: Nyílt forráskódú modellek Foundry Localban

## Összefoglaló

Ismerd meg, hogyan integrálhatod a Hugging Face és más nyílt forráskódú modelleket a Foundry Localba. Tanuld meg a kiválasztási stratégiákat, a közösségi hozzájárulási munkafolyamatokat, a teljesítmény-összehasonlítás módszertanát, valamint azt, hogyan bővítheted a Foundry-t egyedi modellregisztrációkkal. Ez a szekció a heti "Model Mondays" felfedezési témákhoz kapcsolódik, és segít abban, hogy helyben értékelhesd és működtethesd a nyílt forráskódú modelleket, mielőtt Azure-ra skáláznád őket.

## Tanulási célok

A szekció végére képes leszel:

- **Felfedezni és értékelni**: Azonosítani a jelölt modelleket (mistral, gemma, qwen, deepseek) a minőség és erőforrások közötti kompromisszumok alapján.
- **Betölteni és futtatni**: A Foundry Local CLI segítségével letölteni, gyorsítótárazni és elindítani közösségi modelleket.
- **Tesztelni**: Alkalmazni következetes késleltetési + token áteresztési + minőségi heurisztikákat.
- **Bővíteni**: Egyedi modellcsomagolót regisztrálni vagy adaptálni SDK-kompatibilis minták alapján.
- **Összehasonlítani**: Strukturált összehasonlításokat készíteni SLM és közepes méretű LLM kiválasztási döntésekhez.

## Előfeltételek

- Az 1. és 2. szekció teljesítése
- Python környezet `foundry-local-sdk` telepítéssel
- Legalább 15 GB szabad lemezterület több modell gyorsítótárához

### Gyors kezdés több platformon

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

MacOS-on történő tesztelés esetén Windows host szolgáltatás ellen állítsd be:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Bemutató menete (30 perc)

### 1. Hugging Face modellek betöltése CLI-n keresztül (8 perc)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Futtatás és gyors tesztelés (5 perc)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Tesztelő script (8 perc)

Hozd létre a `samples/03-oss-models/benchmark_models.py` fájlt:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Futtatás:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Teljesítmény összehasonlítása (5 perc)

Beszéljétek meg a kompromisszumokat: betöltési idő, memóriahasználat (figyeld a Feladatkezelőt / `nvidia-smi` / OS erőforrásfigyelőt), kimeneti minőség és sebesség. Használjátok a Python tesztelő scriptet (3. szekció) a késleltetés és áteresztés mérésére; ismételjétek meg GPU gyorsítás engedélyezése után.

### 5. Kezdő projekt (4 perc)

Hozz létre egy modell összehasonlító jelentés generátort (bővítsd a tesztelő scriptet markdown exportálással).

## Kezdő projekt: `03-huggingface-models` bővítése

Fejleszd tovább a meglévő mintát az alábbiakkal:

1. Tesztelési eredmények összesítése + CSV/Markdown kimenet hozzáadása.
2. Egyszerű minőségi pontozás megvalósítása (prompt párok + manuális annotációs sablonfájl).
3. JSON konfiguráció (`models.json`) bevezetése a bővíthető modell lista és prompt készlet számára.

## Érvényesítési ellenőrzőlista

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Minden célmodellnek meg kell jelennie, és válaszolnia kell egy tesztelő chat kérésre.

## Példa forgatókönyv és workshop térkép

| Workshop script | Forgatókönyv | Cél | Prompt / Adatkészlet forrás |
|-----------------|--------------|-----|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform csapat alapértelmezett SLM kiválasztása beágyazott összefoglalóhoz | Késleltetés + p95 + token/másodperc összehasonlítás készítése a jelölt modellek között | Inline `PROMPT` változó + környezet `BENCH_MODELS` lista |

### Forgatókönyv narratíva

A termékfejlesztési csapatnak ki kell választania egy alapértelmezett könnyű összefoglaló modellt egy offline meeting-jegyzet funkcióhoz. Kontrollált, determinisztikus teszteket futtatnak (hőmérséklet=0) egy fix prompt készleten (lásd az alábbi példát), és gyűjtik a késleltetési + áteresztési metrikákat GPU gyorsítással és anélkül.

### Példa prompt készlet JSON (bővíthető)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Futtasd minden promptot minden modellen, rögzítsd a promptonkénti késleltetést, hogy eloszlási metrikákat származtass és azonosítsd a kiugró értékeket.

## Modell kiválasztási keretrendszer

| Dimenzió | Metrika | Miért fontos |
|----------|---------|--------------|
| Késleltetés | átlag / p95 | Felhasználói élmény következetessége |
| Áteresztés | token/másodperc | Csoportos és streaming skálázhatóság |
| Memória | rezidens méret | Eszköz kompatibilitás és párhuzamosság |
| Minőség | rubrikus promptok | Feladat alkalmassága |
| Lábnyom | gyorsítótár méret | Terjesztés és frissítések |
| Licenc | használati engedély | Kereskedelmi megfelelőség |

## Egyedi modellek bővítése

Magas szintű minta (pszeudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konzultálj a hivatalos repóval a folyamatosan fejlődő adapter interfészekért:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Hibakeresés

| Probléma | Ok | Megoldás |
|----------|----|----------|
| OOM a mistral-7b-nél | Elégtelen RAM/GPU | Állítsd le a többi modellt; próbálj kisebb változatot |
| Lassú első válasz | Hideg betöltés | Tartsd melegen egy időszakos könnyű prompttal |
| Letöltés elakad | Hálózati instabilitás | Próbáld újra; előtöltsd csúcsidőn kívül |

## Hivatkozások

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Szekció időtartama**: 30 perc (+ opcionális mélyebb elemzés)  
**Nehézségi szint**: Középhaladó

### Opcionális fejlesztések

| Fejlesztés | Előny | Hogyan |
|------------|-------|--------|
| Streaming első token késleltetés | Érzékelt válaszkészség mérése | Futtasd a tesztet `BENCH_STREAM=1`-el (fejlesztett script a `Workshop/samples/session03`-ban) |
| Determinisztikus mód | Stabil regressziós összehasonlítások | `temperature=0`, fix prompt készlet, JSON kimenetek rögzítése verziókezelés alatt |
| Minőségi rubrikus pontozás | Minőségi dimenzió hozzáadása | Tartsd karban a `prompts.json` fájlt várt aspektusokkal; annotáld a pontokat (1–5) manuálisan vagy másodlagos modell segítségével |
| CSV / Markdown exportálás | Megosztható jelentés | Bővítsd a scriptet, hogy `benchmark_report.md` táblázatot és kiemeléseket írjon |
| Modell képesség címkék | Segíti az automatizált útvonaltervezést később | Tartsd karban a `models.json` fájlt `{alias: {capabilities:[], size_mb:..}}` formátumban |
| Gyorsítótár előmelegítési fázis | Csökkenti a hidegindítási torzítást | Végezzen egy melegítési kört az időzítési ciklus előtt (már megvalósítva) |
| Percentilis pontosság | Robusztus késleltetési eloszlás | Használj numpy percentilist (már refaktorált scriptben) |
| Token költség becslés | Gazdasági összehasonlítás | Becslés: (token/másodperc * átlagos tokenek kérésenként) * energia heurisztika |
| Hibás modellek automatikus kihagyása | Ellenállóképesség csoportos futtatásoknál | Csomagolj minden tesztet try/except-be, és jelöld meg az állapot mezőt |

#### Minimális Markdown exportálási snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Determinisztikus prompt készlet példa

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Használj statikus listát véletlenszerű promptok helyett, hogy összehasonlítható metrikákat kapj a commitok között.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->