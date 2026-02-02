# Sezení 3: Open-Source modely ve Foundry Local

## Abstrakt

Zjistěte, jak integrovat modely Hugging Face a další open-source modely do Foundry Local. Naučte se strategie výběru, pracovní postupy pro přispívání do komunity, metodologii porovnávání výkonu a jak rozšířit Foundry pomocí registrace vlastních modelů. Toto sezení se váže na týdenní témata "Model Mondays" a poskytne vám nástroje pro hodnocení a provozování open-source modelů lokálně před jejich škálováním na Azure.

## Cíle učení

Na konci budete schopni:

- **Objevit & Hodnotit**: Identifikovat kandidátní modely (mistral, gemma, qwen, deepseek) na základě kompromisu mezi kvalitou a zdroji.
- **Načíst & Spustit**: Použít Foundry Local CLI k stažení, uložení do mezipaměti a spuštění komunitních modelů.
- **Benchmarkovat**: Aplikovat konzistentní heuristiky latence + průchodnosti tokenů + kvality.
- **Rozšířit**: Registrovat nebo přizpůsobit vlastní obal modelu podle vzorů kompatibilních se SDK.
- **Porovnat**: Vytvořit strukturované porovnání pro rozhodování mezi SLM a středně velkými LLM.

## Předpoklady

- Dokončené sezení 1 a 2
- Python prostředí s nainstalovaným `foundry-local-sdk`
- Minimálně 15 GB volného místa na disku pro mezipaměti modelů

### Rychlý start pro multiplatformní prostředí

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

Při benchmarkování z macOS proti hostitelské službě na Windows nastavte:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Průběh ukázky (30 min)

### 1. Načtení modelů Hugging Face přes CLI (8 min)

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


### 2. Spuštění & Rychlá kontrola (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmarkovací skript (8 min)

Vytvořte `samples/03-oss-models/benchmark_models.py`:

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

Spusťte:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Porovnání výkonu (5 min)

Diskutujte kompromisy: doba načítání, paměťová náročnost (pozorujte Správce úloh / `nvidia-smi` / monitor zdrojů OS), kvalita výstupu vs rychlost. Použijte Python benchmarkovací skript (Sezení 3) pro latenci & průchodnost; opakujte po zapnutí akcelerace GPU.

### 5. Startovací projekt (4 min)

Vytvořte generátor zpráv pro porovnání modelů (rozšiřte benchmarkovací skript o export do markdown).

## Startovací projekt: Rozšíření `03-huggingface-models`

Vylepšete existující vzorek:

1. Přidáním agregace benchmarků + výstupu do CSV/Markdown.
2. Implementací jednoduchého kvalitativního hodnocení (sada dvojic promptů + soubor pro manuální anotaci).
3. Zavedením JSON konfigurace (`models.json`) pro seznam modelů a sadu promptů.

## Kontrolní seznam validace

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Všechny cílové modely by se měly objevit a reagovat na požadavek na chat.

## Ukázkový scénář & Mapování workshopu

| Skript workshopu | Scénář | Cíl | Zdroj promptů / datasetu |
|------------------|--------|-----|--------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Tým platformy Edge vybírá výchozí SLM pro vestavěný sumarizátor | Vytvořit porovnání latence + p95 + tokenů/sec mezi kandidátními modely | Inline `PROMPT` var + seznam `BENCH_MODELS` prostředí |

### Narativ scénáře
Produktový tým musí vybrat výchozí lehký sumarizační model pro offline funkci poznámek ze schůzek. Provádějí kontrolované deterministické benchmarky (teplota=0) na pevné sadě promptů (viz příklad níže) a sbírají metriky latence & průchodnosti s a bez akcelerace GPU.

### Příklad JSON sady promptů (rozšiřitelný)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Projděte každý prompt pro každý model, zachyťte latenci na prompt a odvoďte distribuční metriky a detekujte odlehlé hodnoty.

## Rámec pro výběr modelu

| Dimenze | Metrika | Proč je důležitá |
|---------|---------|------------------|
| Latence | průměr / p95 | Konzistence uživatelského zážitku |
| Průchodnost | tokeny/sec | Škálovatelnost dávkového & streamovacího režimu |
| Paměť | rezidentní velikost | Vhodnost pro zařízení & souběžnost |
| Kvalita | promptová kritéria | Vhodnost pro úkol |
| Stopa | mezipaměť na disku | Distribuce & aktualizace |
| Licence | povolení k použití | Soulad s komerčními podmínkami |

## Rozšíření s vlastním modelem

Vysoká úroveň vzoru (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konzultujte oficiální repozitář pro vyvíjející se rozhraní adaptérů:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Řešení problémů

| Problém | Příčina | Řešení |
|---------|---------|--------|
| OOM na mistral-7b | Nedostatečná RAM/GPU | Zastavte jiné modely; zkuste menší variantu |
| Pomalejší první odpověď | Studené načítání | Udržujte v teple pomocí periodického lehkého promptu |
| Zaseknutí stahování | Nestabilita sítě | Opakujte; přednačtěte během mimo špičku |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Objevování modelů Hugging Face: https://huggingface.co/models

---

**Délka sezení**: 30 min (+ volitelný hlubší ponor)  
**Obtížnost**: Střední

### Volitelná vylepšení

| Vylepšení | Přínos | Jak |
|-----------|--------|-----|
| Latence prvního tokenu při streamování | Měří vnímanou odezvu | Spusťte benchmark s `BENCH_STREAM=1` (vylepšený skript v `Workshop/samples/session03`) |
| Deterministický režim | Stabilní regresní porovnání | `teplota=0`, pevná sada promptů, zachyťte JSON výstupy pod verzovací kontrolou |
| Hodnocení podle kvalitativních kritérií | Přidává kvalitativní rozměr | Udržujte `prompts.json` s očekávanými aspekty; anotujte skóre (1–5) ručně nebo pomocí sekundárního modelu |
| Export do CSV / Markdown | Sdílitelná zpráva | Rozšiřte skript pro zápis `benchmark_report.md` s tabulkou & zvýrazněními |
| Štítky schopností modelu | Pomáhá automatizovanému směrování později | Udržujte `models.json` s `{alias: {capabilities:[], size_mb:..}}` |
| Fáze zahřátí mezipaměti | Snižuje zkreslení studeného startu | Proveďte jedno zahřívací kolo před časovací smyčkou (již implementováno) |
| Percentilová přesnost | Robustní latence na konci | Použijte numpy percentil (již v refaktorovaném skriptu) |
| Odhad nákladů na tokeny | Ekonomické porovnání | Přibližné náklady = (tokeny/sec * průměrný počet tokenů na požadavek) * energetická heuristika |
| Automatické přeskočení neúspěšných modelů | Odolnost při dávkovém spuštění | Zabalte každý benchmark do try/except a označte stavové pole |

#### Minimální úryvek pro export do Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Příklad deterministické sady promptů

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Projděte statický seznam místo náhodných promptů pro srovnatelné metriky napříč commity.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->