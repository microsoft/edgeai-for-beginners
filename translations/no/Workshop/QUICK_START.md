# Workshop Hurtigstartguide

## Forutsetninger

### 1. Installer Foundry Local

Følg den offisielle installasjonsveiledningen:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Installer Python-avhengigheter

Fra Workshop-katalogen:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Kjøre Workshop-eksempler

### Økt 01: Grunnleggende Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Miljøvariabler:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Økt 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Miljøvariabler:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Økt 02: RAG Evaluering (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Merk**: Krever ekstra avhengigheter installert via `requirements.txt`

### Økt 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Miljøvariabler:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Utdata**: JSON med latenstid, gjennomstrømning og første-token-metrikker

### Økt 04: Modell-sammenligning

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Miljøvariabler:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Økt 05: Multi-agent Orkestrering

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Miljøvariabler:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Økt 06: Modellruter

```bash
cd Workshop/samples
python -m session06.models_router
```

**Tester rutelogikk** med flere intensjoner (kode, oppsummering, klassifisering)

### Økt 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Kompleks flertrinns pipeline** med planlegging, utførelse og forbedring

## Skript

### Eksporter Benchmark-rapport

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Utdata**: Markdown-tabell + JSON-metrikker

### Lint Markdown CLI-mønstre

```bash
python lint_markdown_cli.py --verbose
```

**Formål**: Oppdage utdaterte CLI-mønstre i dokumentasjon

## Testing

### Røyktester

```bash
cd Workshop
python -m tests.smoke
```

**Tester**: Grunnleggende funksjonalitet for nøkkel-eksempler

## Feilsøking

### Tjenesten kjører ikke

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modulimportfeil

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Tilkoblingsfeil

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modell ikke funnet

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referanse for miljøvariabler

### Kjernekonfigurasjon
| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varierer | Modellalias som skal brukes |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Overstyr tjenesteendepunkt |
| `SHOW_USAGE` | `0` | Vis token-bruksstatistikk |
| `RETRY_ON_FAIL` | `1` | Aktiver retry-logikk |
| `RETRY_BACKOFF` | `1.0` | Startforsinkelse for retry (sekunder) |

### Økt-spesifikk
| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding-modell |
| `RAG_QUESTION` | Se eksempel | RAG testspørsmål |
| `BENCH_MODELS` | Varierer | Komma-separerte modeller |
| `BENCH_ROUNDS` | `3` | Benchmark-iterasjoner |
| `BENCH_PROMPT` | Se eksempel | Benchmark-prompt |
| `BENCH_STREAM` | `0` | Måle første-token-latenstid |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primær agentmodell |
| `AGENT_MODEL_EDITOR` | Primær | Editor-agentmodell |
| `SLM_ALIAS` | `phi-4-mini` | Liten språkmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor språkmodell |
| `COMPARE_PROMPT` | Se eksempel | Sammenligningsprompt |

## Anbefalte modeller

### Utvikling og testing
- **phi-4-mini** - Balansert kvalitet og hastighet
- **qwen2.5-0.5b** - Veldig rask for klassifisering
- **gemma-2-2b** - God kvalitet, moderat hastighet

### Produksjonsscenarier
- **phi-4-mini** - Generelt formål
- **deepseek-coder-1.3b** - Kodegenerering
- **qwen2.5-7b** - Høykvalitets svar

## SDK-dokumentasjon

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Få hjelp

1. Sjekk tjenestestatus: `foundry service status`
2. Se logger: Sjekk Foundry Local tjenestelogger
3. Sjekk SDK-dokumentasjon: https://github.com/microsoft/Foundry-Local
4. Gå gjennom eksempelkode: Alle eksempler har detaljerte docstrings

## Neste steg

1. Fullfør alle workshop-økter i rekkefølge
2. Eksperimenter med forskjellige modeller
3. Modifiser eksempler for dine bruksområder

---

**Sist oppdatert**: 2025-01-08  
**Workshop-versjon**: Siste  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->