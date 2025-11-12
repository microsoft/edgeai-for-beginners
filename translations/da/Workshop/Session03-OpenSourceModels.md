<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:19:16+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "da"
}
-->
# Session 3: Open-Source Modeller i Foundry Local

## Resumé

Lær hvordan du kan integrere Hugging Face og andre open-source modeller i Foundry Local. Få indsigt i udvælgelsesstrategier, workflows for bidrag fra fællesskabet, metoder til sammenligning af ydeevne, og hvordan du kan udvide Foundry med registrering af brugerdefinerede modeller. Denne session knytter sig til de ugentlige "Model Mondays"-temaer og giver dig værktøjer til at evaluere og operationalisere open-source modeller lokalt, før du skalerer til Azure.

## Læringsmål

Ved afslutningen vil du kunne:

- **Opdage & Evaluere**: Identificere kandidater (mistral, gemma, qwen, deepseek) baseret på kvalitet kontra ressourceforbrug.
- **Indlæse & Køre**: Bruge Foundry Local CLI til at downloade, cache og starte fællesskabsmodeller.
- **Benchmarke**: Anvende konsistente heuristikker for latenstid, token-gennemstrømning og kvalitet.
- **Udvide**: Registrere eller tilpasse en brugerdefineret model-wrapper efter SDK-kompatible mønstre.
- **Sammenligne**: Udarbejde strukturerede sammenligninger for SLM kontra mellemstore LLM-valg.

## Forudsætninger

- Session 1 & 2 gennemført
- Python-miljø med `foundry-local-sdk` installeret
- Mindst 15GB ledig diskplads til flere model-caches

### Hurtig start på tværs af platforme

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

Ved benchmarking fra macOS mod en Windows-hosttjeneste, indstil:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo Flow (30 min)

### 1. Indlæs Hugging Face-modeller via CLI (8 min)

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

### 2. Kør & Hurtig Test (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Benchmark Script (8 min)

Opret `samples/03-oss-models/benchmark_models.py`:

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

Kør:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Sammenlign Ydeevne (5 min)

Diskuter kompromiser: indlæsningstid, hukommelsesforbrug (observer Task Manager / `nvidia-smi` / OS ressourceovervågning), outputkvalitet kontra hastighed. Brug Python-benchmark-scriptet (Session 3) til latenstid og gennemstrømning; gentag efter aktivering af GPU-acceleration.

### 5. Startprojekt (4 min)

Opret en rapportgenerator til model-sammenligning (udvid benchmark-scriptet med markdown-eksport).

## Startprojekt: Udvid `03-huggingface-models`

Forbedr det eksisterende eksempel ved at:

1. Tilføje benchmark-aggregation + CSV/Markdown-eksport.
2. Implementere simpel kvalitativ scoring (prompt-par-sæt + manuel annoteringsstub-fil).
3. Introducere en JSON-konfiguration (`models.json`) til en plug-and-play modelliste og prompt-sæt.

## Valideringscheckliste

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Alle målmodeller skal vises og reagere på en test-chatforespørgsel.

## Eksempelscenarie & Workshop-mapping

| Workshop Script | Scenarie | Mål | Prompt / Dataset-kilde |
|-----------------|----------|-----|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge-platformteam vælger standard SLM til indlejret opsummeringsfunktion | Udarbejd latenstid + p95 + tokens/sek sammenligning på tværs af kandidatmodeller | Inline `PROMPT` var + miljø `BENCH_MODELS` liste |

### Scenariefortælling
Produktudvikling skal vælge en standard letvægts-opsummeringsmodel til en offline mødenotatfunktion. De udfører kontrollerede deterministiske benchmarks (temperature=0) på tværs af et fast prompt-sæt (se eksempel nedenfor) og indsamler latenstid + gennemstrømningsmålinger med og uden GPU-acceleration.

### Eksempel på Prompt-sæt JSON (udvideligt)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop hver prompt pr. model, registrer latenstid pr. prompt for at udlede distributionsmålinger og opdage outliers.

## Modeludvælgelsesramme

| Dimension | Metric | Hvorfor det er vigtigt |
|----------|--------|-------------------------|
| Latenstid | gennemsnit / p95 | Konsistens i brugeroplevelse |
| Gennemstrømning | tokens/sek | Batch- og streaming-skalerbarhed |
| Hukommelse | resident størrelse | Enhedstilpasning & samtidighed |
| Kvalitet | rubric prompts | Opgaveegnethed |
| Footprint | disk-cache | Distribution & opdateringer |
| Licens | brugsbetingelser | Kommerciel overholdelse |

## Udvidelse med brugerdefineret model

Overordnet mønster (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsulter det officielle repo for udviklende adapterinterfaces:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Fejlfinding

| Problem | Årsag | Løsning |
|---------|-------|---------|
| OOM på mistral-7b | Utilstrækkelig RAM/GPU | Stop andre modeller; prøv mindre variant |
| Langsom første respons | Kold indlæsning | Hold varm med en periodisk let prompt |
| Download går i stå | Netværksinstabilitet | Prøv igen; forudhent under lavtrafik |

## Referencer

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Sessionsvarighed**: 30 min (+ valgfri dybdegående gennemgang)  
**Sværhedsgrad**: Mellem

### Valgfrie forbedringer

| Forbedring | Fordel | Hvordan |
|------------|--------|---------|
| Streaming af første-token-latenstid | Måler oplevet responsivitet | Kør benchmark med `BENCH_STREAM=1` (forbedret script i `Workshop/samples/session03`) |
| Deterministisk tilstand | Stabil regression sammenligninger | `temperature=0`, fast prompt-sæt, registrer JSON-outputs under versionskontrol |
| Kvalitetsrubrikscoring | Tilføjer kvalitativ dimension | Vedligehold `prompts.json` med forventede facetter; annoter scores (1–5) manuelt eller via sekundær model |
| CSV / Markdown-eksport | Delbar rapport | Udvid scriptet til at skrive `benchmark_report.md` med tabel & højdepunkter |
| Modelkapabilitet-tags | Hjælper med automatiseret routing senere | Vedligehold `models.json` med `{alias: {capabilities:[], size_mb:..}}` |
| Cache-opvarmningsfase | Reducer bias fra koldstart | Udfør en varm runde før timing-loop (allerede implementeret) |
| Percentil-nøjagtighed | Robust tail-latenstid | Brug numpy percentil (allerede i refaktoreret script) |
| Token-omkostningsberegning | Økonomisk sammenligning | Omkostning ≈ (tokens/sek * gennemsnit tokens pr. forespørgsel) * energiheuristik |
| Automatisk spring over fejlede modeller | Robusthed i batch-kørsler | Indpak hver benchmark i try/except og marker statusfelt |

#### Minimal Markdown-eksport snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Eksempel på deterministisk prompt-sæt

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop den statiske liste i stedet for tilfældige prompts for sammenlignelige målinger på tværs af commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->