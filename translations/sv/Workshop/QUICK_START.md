<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T23:11:23+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "sv"
}
-->
# Snabbstartsguide för Workshop

## Förutsättningar

### 1. Installera Foundry Local

Följ den officiella installationsguiden:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Installera Python-beroenden

Från Workshop-katalogen:

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

## Köra Workshop-exempel

### Session 01: Grundläggande Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Miljövariabler:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG-pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Miljövariabler:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: RAG-utvärdering (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Obs**: Kräver ytterligare beroenden installerade via `requirements.txt`

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Miljövariabler:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Utdata**: JSON med latens, genomströmning och första-token-mått

### Session 04: Modelljämförelse

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Miljövariabler:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05: Multi-Agent Orchestration

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Miljövariabler:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06: Modellrouter

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testar routinglogik** med flera avsikter (kod, sammanfatta, klassificering)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Komplex pipeline i flera steg** med planering, utförande och förfining

## Skript

### Exportera Benchmark-rapport

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Utdata**: Markdown-tabell + JSON-mått

### Kontrollera Markdown CLI-mönster

```bash
python lint_markdown_cli.py --verbose
```

**Syfte**: Identifiera föråldrade CLI-mönster i dokumentation

## Testning

### Snabbtester

```bash
cd Workshop
python -m tests.smoke
```

**Tester**: Grundläggande funktionalitet för viktiga exempel

## Felsökning

### Tjänsten körs inte

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modulimportfel

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Anslutningsfel

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modell hittades inte

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referens för miljövariabler

### Grundkonfiguration
| Variabel | Standard | Beskrivning |
|----------|----------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varierar | Modellalias att använda |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Åsidosätt tjänstendpunkt |
| `SHOW_USAGE` | `0` | Visa statistik för tokenanvändning |
| `RETRY_ON_FAIL` | `1` | Aktivera återförsökslogik |
| `RETRY_BACKOFF` | `1.0` | Initial återförsöksfördröjning (sekunder) |

### Sessionsspecifik
| Variabel | Standard | Beskrivning |
|----------|----------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Inbäddningsmodell |
| `RAG_QUESTION` | Se exempel | RAG-testfråga |
| `BENCH_MODELS` | Varierar | Komma-separerade modeller |
| `BENCH_ROUNDS` | `3` | Benchmark-iterationer |
| `BENCH_PROMPT` | Se exempel | Benchmark-prompt |
| `BENCH_STREAM` | `0` | Mäta latens för första token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primär agentmodell |
| `AGENT_MODEL_EDITOR` | Primär | Redigeringsagentmodell |
| `SLM_ALIAS` | `phi-4-mini` | Liten språkmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Stor språkmodell |
| `COMPARE_PROMPT` | Se exempel | Jämförelse-prompt |

## Rekommenderade modeller

### Utveckling & Testning
- **phi-4-mini** - Balanserad kvalitet och hastighet
- **qwen2.5-0.5b** - Mycket snabb för klassificering
- **gemma-2-2b** - Bra kvalitet, måttlig hastighet

### Produktionsscenarier
- **phi-4-mini** - Allmänt ändamål
- **deepseek-coder-1.3b** - Kodgenerering
- **qwen2.5-7b** - Högkvalitativa svar

## SDK-dokumentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Få hjälp

1. Kontrollera tjänstens status: `foundry service status`  
2. Visa loggar: Kontrollera Foundry Local-tjänstens loggar  
3. Kontrollera SDK-dokumentation: https://github.com/microsoft/Foundry-Local  
4. Granska exempel: Alla exempel har detaljerade docstrings  

## Nästa steg

1. Slutför alla workshopsessioner i ordning  
2. Experimentera med olika modeller  
3. Anpassa exempel för dina användningsfall  

---

**Senast uppdaterad**: 2025-01-08  
**Workshopversion**: Senaste  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->