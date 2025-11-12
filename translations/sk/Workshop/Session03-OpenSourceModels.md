<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T00:15:56+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "sk"
}
-->
# Session 3: Open-Source Modely vo Foundry Local

## Abstrakt

Zistite, ako integrovať modely Hugging Face a ďalšie open-source modely do Foundry Local. Naučte sa stratégie výberu, pracovné postupy prispievania do komunity, metodológiu porovnávania výkonu a ako rozšíriť Foundry pomocou registrácie vlastných modelov. Táto relácia sa zameriava na týždenné témy "Model Mondays" a poskytne vám nástroje na hodnotenie a prevádzkovanie open-source modelov lokálne pred ich škálovaním na Azure.

## Ciele vzdelávania

Na konci budete schopní:

- **Objaviť a hodnotiť**: Identifikovať kandidátske modely (mistral, gemma, qwen, deepseek) na základe kompromisov medzi kvalitou a zdrojmi.
- **Načítať a spustiť**: Použiť Foundry Local CLI na stiahnutie, ukladanie do cache a spustenie komunitných modelov.
- **Benchmarkovať**: Použiť konzistentné heuristiky latencie + priepustnosti tokenov + kvality.
- **Rozšíriť**: Registrovať alebo prispôsobiť vlastný wrapper modelu podľa vzorov kompatibilných so SDK.
- **Porovnať**: Vytvoriť štruktúrované porovnania pre rozhodovanie medzi SLM a stredne veľkými LLM.

## Predpoklady

- Dokončené relácie 1 a 2
- Prostredie Python s nainštalovaným `foundry-local-sdk`
- Minimálne 15GB voľného miesta na disku pre cache viacerých modelov

### Rýchly štart pre multiplatformové prostredie

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

Pri benchmarkovaní z macOS voči hostiteľskej službe na Windows nastavte:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo priebeh (30 min)

### 1. Načítanie modelov Hugging Face cez CLI (8 min)

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

### 2. Spustenie a rýchla kontrola (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Benchmarkovací skript (8 min)

Vytvorte `samples/03-oss-models/benchmark_models.py`:

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

Spustite:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Porovnanie výkonu (5 min)

Diskutujte o kompromisoch: čas načítania, pamäťová náročnosť (pozorujte Správcu úloh / `nvidia-smi` / monitor zdrojov OS), kvalita výstupu vs rýchlosť. Použite Python benchmarkovací skript (Session 3) na latenciu a priepustnosť; zopakujte po zapnutí akcelerácie GPU.

### 5. Začiatočný projekt (4 min)

Vytvorte generátor správ o porovnaní modelov (rozšírte benchmarkovací skript o export do markdown).

## Začiatočný projekt: Rozšírenie `03-huggingface-models`

Vylepšite existujúci príklad pridaním:

1. Agregácie benchmarkov + výstupu do CSV/Markdown.
2. Implementácie jednoduchého kvalitatívneho hodnotenia (súbor párov promptov + manuálny anotovací stub).
3. Zavedenia JSON konfigurácie (`models.json`) pre zoznam modelov a sadu promptov.

## Kontrolný zoznam validácie

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Všetky cieľové modely by sa mali zobraziť a reagovať na požiadavku na chat.

## Ukážkový scenár a mapovanie workshopu

| Skript workshopu | Scenár | Cieľ | Zdroj promptov / datasetu |
|------------------|--------|------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Tím platformy Edge vyberá predvolený SLM pre zabudovaný sumarizátor | Vytvoriť porovnanie latencie + p95 + tokenov/sekundu medzi kandidátskymi modelmi | Inline `PROMPT` var + zoznam prostredia `BENCH_MODELS` |

### Naratív scenára
Produktový inžiniering musí vybrať predvolený ľahký sumarizačný model pre offline funkciu poznámok zo stretnutí. Vykonávajú kontrolované deterministické benchmarky (temperature=0) na pevnej sade promptov (pozri príklad nižšie) a zhromažďujú metriky latencie + priepustnosti s a bez akcelerácie GPU.

### Príklad JSON sady promptov (rozšíriteľné)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Prejdite každý prompt pre každý model, zachyťte latenciu na prompt na odvodenie distribučných metrík a detekciu odchýlok.

## Rámec výberu modelu

| Dimenzia | Metrika | Prečo je dôležitá |
|----------|---------|-------------------|
| Latencia | priemer / p95 | Konzistentnosť používateľskej skúsenosti |
| Priepustnosť | tokeny/sekundu | Škálovateľnosť dávok a streamovania |
| Pamäť | rezidentná veľkosť | Vhodnosť pre zariadenie a súbežnosť |
| Kvalita | rubrikové prompty | Vhodnosť pre úlohu |
| Stopa | cache na disku | Distribúcia a aktualizácie |
| Licencia | povolenie použitia | Komerčná zhoda |

## Rozšírenie s vlastným modelom

Vysoká úroveň vzoru (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konzultujte oficiálne repo pre vyvíjajúce sa rozhrania adaptérov:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Riešenie problémov

| Problém | Príčina | Riešenie |
|---------|---------|----------|
| OOM na mistral-7b | Nedostatok RAM/GPU | Zastavte iné modely; skúste menší variant |
| Pomalá prvá odpoveď | Studené načítanie | Udržujte teplé pomocou pravidelného ľahkého promptu |
| Zastavenie sťahovania | Nestabilita siete | Opakujte; prednačítajte počas mimo špičky |

## Referencie

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Objavovanie modelov Hugging Face: https://huggingface.co/models

---

**Trvanie relácie**: 30 min (+ voliteľné podrobné preskúmanie)  
**Náročnosť**: Stredne pokročilá

### Voliteľné vylepšenia

| Vylepšenie | Výhoda | Ako |
|------------|--------|-----|
| Latencia prvého tokenu pri streamovaní | Meria vnímanú odozvu | Spustite benchmark s `BENCH_STREAM=1` (vylepšený skript v `Workshop/samples/session03`) |
| Deterministický režim | Stabilné regresné porovnania | `temperature=0`, pevná sada promptov, zachyťte výstupy JSON pod kontrolou verzií |
| Hodnotenie kvality podľa rubriky | Pridáva kvalitatívny rozmer | Udržujte `prompts.json` s očakávanými aspektmi; anotujte skóre (1–5) manuálne alebo pomocou sekundárneho modelu |
| Export do CSV / Markdown | Zdieľateľná správa | Rozšírte skript na zápis `benchmark_report.md` s tabuľkou a zvýrazneniami |
| Tagy schopností modelu | Pomáha automatizovanému smerovaniu neskôr | Udržujte `models.json` s `{alias: {capabilities:[], size_mb:..}}` |
| Fáza zahrievania cache | Zníženie zaujatosti studeného štartu | Vykonajte jedno zahrievacie kolo pred časovacou slučkou (už implementované) |
| Percentilová presnosť | Robustná latencia na konci | Použite numpy percentil (už v refaktorovanom skripte) |
| Odhad nákladov na tokeny | Ekonomické porovnanie | Odhad nákladov = (tokeny/sekundu * priemerné tokeny na požiadavku) * energetická heuristika |
| Automatické preskakovanie zlyhaných modelov | Odolnosť pri dávkových spusteniach | Zabaľte každý benchmark do try/except a označte pole stavu |

#### Minimálny snippet exportu do Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Príklad deterministickej sady promptov

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Prejdite statický zoznam namiesto náhodných promptov pre porovnateľné metriky medzi commitmi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->