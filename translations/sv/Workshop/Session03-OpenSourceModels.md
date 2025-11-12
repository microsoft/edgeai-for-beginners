<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:15:00+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "sv"
}
-->
# Session 3: Öppen källkod-modeller i Foundry Local

## Sammanfattning

Upptäck hur du kan integrera Hugging Face och andra modeller med öppen källkod i Foundry Local. Lär dig strategier för modellval, arbetsflöden för community-bidrag, metodik för prestandajämförelse och hur du kan utöka Foundry med anpassade modellregistreringar. Denna session kopplas till de veckovisa "Model Mondays"-teman och ger dig verktyg för att utvärdera och använda modeller med öppen källkod lokalt innan du skalar upp till Azure.

## Lärandemål

Efter sessionen kommer du att kunna:

- **Upptäcka & Utvärdera**: Identifiera kandidater (mistral, gemma, qwen, deepseek) baserat på kvalitet kontra resursavvägningar.
- **Ladda & Köra**: Använd Foundry Local CLI för att ladda ner, cachea och köra community-modeller.
- **Benchmarka**: Använd konsekventa heuristiker för latens, token-genomströmning och kvalitet.
- **Utöka**: Registrera eller anpassa en egen modellwrapper enligt SDK-kompatibla mönster.
- **Jämföra**: Skapa strukturerade jämförelser för SLM kontra mellanstora LLM-val.

## Förkunskaper

- Session 1 & 2 genomförda
- Python-miljö med `foundry-local-sdk` installerad
- Minst 15GB ledigt diskutrymme för flera modellcacher

### Snabbstart för plattformsoberoende miljö

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

Vid benchmarking från macOS mot en Windows-värdtjänst, ställ in:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-flöde (30 min)

### 1. Ladda Hugging Face-modeller via CLI (8 min)

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


### 2. Kör & Snabbtesta (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmark-skript (8 min)

Skapa `samples/03-oss-models/benchmark_models.py`:

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

Kör:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Jämför prestanda (5 min)

Diskutera avvägningar: laddningstid, minnesanvändning (observera Aktivitetshanteraren / `nvidia-smi` / OS-resursmonitor), outputkvalitet kontra hastighet. Använd Python-benchmark-skriptet (Session 3) för latens och genomströmning; upprepa efter att ha aktiverat GPU-acceleration.

### 5. Startprojekt (4 min)

Skapa en rapportgenerator för modelljämförelse (utöka benchmark-skriptet med markdown-export).

## Startprojekt: Utöka `03-huggingface-models`

Förbättra det befintliga exemplet genom att:

1. Lägga till benchmark-aggregation + CSV/Markdown-export.
2. Implementera enkel kvalitativ poängsättning (prompt-parset + manuell annoteringsstub-fil).
3. Introducera en JSON-konfiguration (`models.json`) för en pluggbar modellista och prompt-set.

## Valideringschecklista

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Alla målsatta modeller ska visas och svara på en testchattförfrågan.

## Exempelscenario & Workshop-koppling

| Workshop-skript | Scenario | Mål | Prompt / Dataset-källa |
|-----------------|----------|-----|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Team för edge-plattform som väljer standard-SLM för inbyggd sammanfattningsfunktion | Skapa jämförelse av latens + p95 + tokens/sekund mellan kandidater | Inline `PROMPT`-variabel + miljö `BENCH_MODELS`-lista |

### Scenarionarrativ
Produktutvecklingsteamet måste välja en standardmodell för lättvikts-sammanfattning för en offline-funktion för mötesanteckningar. De kör kontrollerade deterministiska benchmarks (temperature=0) över ett fast prompt-set (se exempel nedan) och samlar latens- och genomströmningsdata med och utan GPU-acceleration.

### Exempel på prompt-set JSON (utbyggbart)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop varje prompt per modell, fånga latens per prompt för att härleda distributionsmått och upptäcka avvikelser.

## Ramverk för modellval

| Dimension | Mått | Varför det är viktigt |
|----------|------|------------------------|
| Latens | genomsnitt / p95 | Konsistens i användarupplevelse |
| Genomströmning | tokens/sekund | Skalbarhet för batch och streaming |
| Minne | resident storlek | Passar enheten & samtidighet |
| Kvalitet | rubric prompts | Uppgiftsanpassning |
| Fotavtryck | diskcache | Distribution & uppdateringar |
| Licens | användningstillstånd | Kommersiell efterlevnad |

## Utöka med egen modell

Hög nivå-mönster (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsultera den officiella repot för utvecklande adaptergränssnitt:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| OOM på mistral-7b | Otillräckligt RAM/GPU | Stoppa andra modeller; prova mindre variant |
| Långsam första respons | Kall laddning | Håll varm med ett periodiskt lättvikts-prompt |
| Nedladdning fastnar | Nätverksinstabilitet | Försök igen; förladda under lågtrafik |

## Referenser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Sessionens längd**: 30 min (+ valfri fördjupning)  
**Svårighetsgrad**: Medel

### Valfria förbättringar

| Förbättring | Fördel | Hur |
|-------------|--------|-----|
| Streaming av första-token-latens | Mäta upplevd responsivitet | Kör benchmark med `BENCH_STREAM=1` (förbättrat skript i `Workshop/samples/session03`) |
| Deterministiskt läge | Stabil regression jämförelser | `temperature=0`, fast prompt-set, fånga JSON-utdata under versionskontroll |
| Kvalitativ poängsättning | Lägger till kvalitativ dimension | Underhåll `prompts.json` med förväntade aspekter; annotera poäng (1–5) manuellt eller via sekundär modell |
| CSV / Markdown-export | Delbar rapport | Utöka skriptet för att skriva `benchmark_report.md` med tabell & höjdpunkter |
| Modellkapabilitetstaggar | Hjälper automatiserad routing senare | Underhåll `models.json` med `{alias: {capabilities:[], size_mb:..}}` |
| Cache-uppvärmningsfas | Minska kallstartsbias | Kör en varm runda innan tidsloop (redan implementerat) |
| Percentilnoggrannhet | Robust latens i svansen | Använd numpy percentil (redan i omarbetat skript) |
| Tokenkostnadsberäkning | Ekonomisk jämförelse | Approx kostnad = (tokens/sek * genomsnitt tokens per förfrågan) * energiheuristik |
| Automatisk hoppning av misslyckade modeller | Resiliens i batchkörningar | Omge varje benchmark med try/except och markera statusfält |

#### Minimal Markdown-exportsnutt

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Exempel på deterministiskt prompt-set

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop den statiska listan istället för slumpmässiga prompts för jämförbara mått över commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->