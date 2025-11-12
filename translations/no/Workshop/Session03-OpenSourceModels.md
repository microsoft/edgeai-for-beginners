<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:23:32+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "no"
}
-->
# Sesjon 3: Åpen kildekode-modeller i Foundry Local

## Sammendrag

Lær hvordan du kan integrere Hugging Face og andre modeller med åpen kildekode i Foundry Local. Utforsk strategier for modellutvelgelse, arbeidsflyter for bidrag fra fellesskapet, metodikk for ytelsessammenligning, og hvordan du kan utvide Foundry med tilpassede modellregistreringer. Denne sesjonen knytter seg til de ukentlige "Model Mondays"-temaene og gir deg verktøyene til å evaluere og operasjonalisere modeller med åpen kildekode lokalt før du skalerer til Azure.

## Læringsmål

Ved slutten av sesjonen vil du kunne:

- **Oppdage & Evaluere**: Identifisere aktuelle modeller (mistral, gemma, qwen, deepseek) basert på kvalitet kontra ressursbruk.
- **Laste & Kjøre**: Bruke Foundry Local CLI til å laste ned, cache og starte fellesskapsmodeller.
- **Benchmarke**: Anvende konsistente heuristikker for latenstid, token-gjennomstrømning og kvalitet.
- **Utvide**: Registrere eller tilpasse en tilpasset modellwrapper i henhold til SDK-kompatible mønstre.
- **Sammenligne**: Lage strukturerte sammenligninger for valg mellom SLM og mellomstore LLM-modeller.

## Forutsetninger

- Fullført sesjon 1 og 2
- Python-miljø med `foundry-local-sdk` installert
- Minst 15GB ledig diskplass for flere modell-cacher

### Hurtigstart for tverrplattform-miljø

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

Ved benchmarking fra macOS mot en Windows-hosttjeneste, sett:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-flyt (30 min)

### 1. Last Hugging Face-modeller via CLI (8 min)

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


### 2. Kjør & Rask Sjekk (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmark-skript (8 min)

Opprett `samples/03-oss-models/benchmark_models.py`:

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

Kjør:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Sammenlign Ytelse (5 min)

Diskuter avveininger: lastetid, minnebruk (observer Oppgavebehandling / `nvidia-smi` / OS ressursmonitor), outputkvalitet kontra hastighet. Bruk Python benchmark-skriptet (Sesjon 3) for latenstid og gjennomstrømning; gjenta etter å ha aktivert GPU-akselerasjon.

### 5. Startprosjekt (4 min)

Lag en rapportgenerator for modell-sammenligning (utvid benchmark-skriptet med eksport til markdown).

## Startprosjekt: Utvid `03-huggingface-models`

Forbedre det eksisterende eksempelet ved å:

1. Legge til benchmark-aggregering + CSV/Markdown-eksport.
2. Implementere enkel kvalitativ scoring (prompt-parsett + manuell annoteringsfil).
3. Introdusere en JSON-konfigurasjon (`models.json`) for pluggbar modelliste og prompt-sett.

## Valideringssjekkliste

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Alle målmodeller skal vises og svare på en forespørsel om chat.

## Eksempelscenario & Workshop-kartlegging

| Workshop-skript | Scenario | Mål | Prompt / Dataset-kilde |
|-----------------|----------|-----|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge-plattformteam som velger standard SLM for innebygd oppsummeringsfunksjon | Produsere sammenligning av latenstid + p95 + tokens/sekund for aktuelle modeller | Inline `PROMPT`-variabel + miljø `BENCH_MODELS`-liste |

### Scenariofortelling
Produktutvikling må velge en standard lettvekts oppsummeringsmodell for en offline møte-notatfunksjon. De kjører kontrollerte deterministiske benchmarks (temperature=0) over et fast prompt-sett (se eksempel nedenfor) og samler inn latenstid + gjennomstrømningsmetrikker med og uten GPU-akselerasjon.

### Eksempel på JSON-prompt-sett (utvidbart)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop hver prompt per modell, fang opp latenstid per prompt for å utlede distribusjonsmetrikker og oppdage avvik.

## Rammeverk for modellutvelgelse

| Dimensjon | Metrikk | Hvorfor det er viktig |
|----------|--------|------------------------|
| Latenstid | gj.snitt / p95 | Konsistens i brukeropplevelse |
| Gjennomstrømning | tokens/sekund | Skalerbarhet for batch & streaming |
| Minne | resident størrelse | Enhetskompatibilitet & samtidighet |
| Kvalitet | rubrikk-prompt | Oppgaveegnethet |
| Fotavtrykk | disk-cache | Distribusjon & oppdateringer |
| Lisens | bruksrettigheter | Kommersiell samsvar |

## Utvidelse med tilpasset modell

Høynivåmønster (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Se den offisielle repoen for utviklende adaptergrensesnitt:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Feilsøking

| Problem | Årsak | Løsning |
|---------|-------|---------|
| OOM på mistral-7b | Utilstrekkelig RAM/GPU | Stopp andre modeller; prøv mindre variant |
| Langsom første respons | Kald last | Hold varm med et periodisk lettvekts-prompt |
| Nedlastingsproblemer | Nettverksinstabilitet | Prøv igjen; forhåndshent under lavtrafikk |

## Referanser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Sesjonsvarighet**: 30 min (+ valgfri dypdykk)  
**Vanskelighetsgrad**: Middels

### Valgfrie forbedringer

| Forbedring | Fordel | Hvordan |
|------------|--------|---------|
| Streaming av første-token-latenstid | Måler opplevd responsivitet | Kjør benchmark med `BENCH_STREAM=1` (utvidet skript i `Workshop/samples/session03`) |
| Deterministisk modus | Stabil regresjonssammenligning | `temperature=0`, fast prompt-sett, fang JSON-utganger under versjonskontroll |
| Kvalitetsrubrikk-scoring | Legger til kvalitativ dimensjon | Vedlikehold `prompts.json` med forventede aspekter; annoter score (1–5) manuelt eller via sekundær modell |
| CSV / Markdown-eksport | Delbar rapport | Utvid skriptet til å skrive `benchmark_report.md` med tabell & høydepunkter |
| Modellkapabilitets-tagger | Hjelper med automatisert ruting senere | Vedlikehold `models.json` med `{alias: {capabilities:[], size_mb:..}}` |
| Cache-oppvarmingsfase | Reduser kaldstart-bias | Utfør en varm runde før tidsmåling (allerede implementert) |
| Percentil-nøyaktighet | Robust tail-latenstid | Bruk numpy percentil (allerede i refaktorert skript) |
| Token-kostnadsestimering | Økonomisk sammenligning | Omtrentlig kostnad = (tokens/sek * gj.snitt tokens per forespørsel) * energiheuristikk |
| Automatisk hopping over mislykkede modeller | Robusthet i batch-kjøringer | Pakk hver benchmark i try/except og marker statusfelt |

#### Minimal Markdown-eksportutdrag

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Eksempel på deterministisk prompt-sett

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop den statiske listen i stedet for tilfeldige prompts for sammenlignbare metrikker på tvers av commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->