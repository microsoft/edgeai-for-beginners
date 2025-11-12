<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T23:15:45+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "da"
}
-->
# Workshop Hurtig Start Guide

## Forudsætninger

### 1. Installer Foundry Local

Følg den officielle installationsguide:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Installer Python-afhængigheder

Fra Workshop-mappen:

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

## Kørsel af Workshop-eksempler

### Session 01: Grundlæggende Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Miljøvariabler:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

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

### Session 02: RAG Evaluering (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Bemærk**: Kræver yderligere afhængigheder installeret via `requirements.txt`

### Session 03: Benchmarking

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

**Output**: JSON med latenstid, gennemløb og første-token-metrics

### Session 04: Model Sammenligning

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

### Session 05: Multi-Agent Orkestrering

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

### Session 06: Model Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Tester routing-logik** med flere intentioner (kode, opsummering, klassifikation)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Kompleks flertrins-pipeline** med planlægning, udførelse og forbedring

## Scripts

### Eksportér Benchmark-rapport

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Markdown-tabel + JSON-metrics

### Lint Markdown CLI-mønstre

```bash
python lint_markdown_cli.py --verbose
```

**Formål**: Registrer forældede CLI-mønstre i dokumentation

## Testning

### Røgtests

```bash
cd Workshop
python -m tests.smoke
```

**Tests**: Grundlæggende funktionalitet af nøgleeksempler

## Fejlfinding

### Tjeneste kører ikke

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modulimportfejl

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Forbindelsesfejl

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model ikke fundet

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Miljøvariabel Reference

### Kernekonfiguration
| Variabel | Standard | Beskrivelse |
|----------|----------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varierer | Modelalias der skal bruges |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Overstyr tjeneste-endpoint |
| `SHOW_USAGE` | `0` | Vis token-brugsstatistik |
| `RETRY_ON_FAIL` | `1` | Aktivér genforsøgslogik |
| `RETRY_BACKOFF` | `1.0` | Indledende forsinkelse ved genforsøg (sekunder) |

### Session-specifik
| Variabel | Standard | Beskrivelse |
|----------|----------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Indlejringsmodel |
| `RAG_QUESTION` | Se eksempel | RAG testspørgsmål |
| `BENCH_MODELS` | Varierer | Kommaseparerede modeller |
| `BENCH_ROUNDS` | `3` | Benchmark-iterationer |
| `BENCH_PROMPT` | Se eksempel | Benchmark-prompt |
| `BENCH_STREAM` | `0` | Mål første-token-latenstid |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primær agentmodel |
| `AGENT_MODEL_EDITOR` | Primær | Editor-agentmodel |
| `SLM_ALIAS` | `phi-4-mini` | Lille sprogmodel |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor sprogmodel |
| `COMPARE_PROMPT` | Se eksempel | Sammenligningsprompt |

## Anbefalede Modeller

### Udvikling & Test
- **phi-4-mini** - Balanceret kvalitet og hastighed
- **qwen2.5-0.5b** - Meget hurtig til klassifikation
- **gemma-2-2b** - God kvalitet, moderat hastighed

### Produktionsscenarier
- **phi-4-mini** - Generelt formål
- **deepseek-coder-1.3b** - Kodegenerering
- **qwen2.5-7b** - Højkvalitets svar

## SDK Dokumentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Få Hjælp

1. Tjek tjenestens status: `foundry service status`  
2. Se logfiler: Tjek Foundry Local tjenestelogfiler  
3. Tjek SDK-dokumentation: https://github.com/microsoft/Foundry-Local  
4. Gennemgå eksempelkode: Alle eksempler har detaljerede docstrings  

## Næste Skridt

1. Gennemfør alle workshop-sessioner i rækkefølge  
2. Eksperimentér med forskellige modeller  
3. Tilpas eksempler til dine brugsscenarier  

---

**Sidst Opdateret**: 2025-01-08  
**Workshop Version**: Seneste  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->