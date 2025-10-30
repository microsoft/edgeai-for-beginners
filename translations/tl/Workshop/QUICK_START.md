<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T22:44:09+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "tl"
}
-->
# Mabilisang Gabay sa Workshop

## Mga Kinakailangan

### 1. I-install ang Foundry Local

Sundin ang opisyal na gabay sa pag-install:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. I-install ang Python Dependencies

Mula sa direktoryo ng Workshop:

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

## Pagpapatakbo ng Mga Halimbawa ng Workshop

### Session 01: Pangunahing Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Mga Environment Variable:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Mga Environment Variable:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: RAG Evaluation (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Tandaan**: Nangangailangan ng karagdagang dependencies na naka-install sa pamamagitan ng `requirements.txt`

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Mga Environment Variable:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON na may latency, throughput, at first-token metrics

### Session 04: Paghahambing ng Modelo

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Mga Environment Variable:**
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

**Mga Environment Variable:**
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

**Sinusubukan ang routing logic** gamit ang iba't ibang intents (code, summarize, classification)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Komplikadong multi-step pipeline** na may planning, execution, at refinement

## Mga Script

### I-export ang Benchmark Report

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Markdown table + JSON metrics

### Lint Markdown CLI Patterns

```bash
python lint_markdown_cli.py --verbose
```

**Layunin**: Tukuyin ang mga deprecated na CLI patterns sa dokumentasyon

## Pagsusuri

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Mga Pagsusuri**: Pangunahing functionality ng mga mahalagang halimbawa

## Pag-aayos ng Problema

### Hindi Gumagana ang Serbisyo

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Mga Error sa Module Import

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Mga Error sa Koneksyon

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Hindi Natagpuan ang Modelo

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Sanggunian sa Environment Variable

### Pangunahing Konfigurasyon
| Variable | Default | Deskripsyon |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Nag-iiba | Model alias na gagamitin |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | I-override ang service endpoint |
| `SHOW_USAGE` | `0` | Ipakita ang token usage stats |
| `RETRY_ON_FAIL` | `1` | Paganahin ang retry logic |
| `RETRY_BACKOFF` | `1.0` | Paunang delay sa retry (segundo) |

### Para sa Bawat Session
| Variable | Default | Deskripsyon |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | Tingnan ang halimbawa | RAG test question |
| `BENCH_MODELS` | Nag-iiba | Mga model na pinaghihiwalay ng comma |
| `BENCH_ROUNDS` | `3` | Mga iteration ng benchmark |
| `BENCH_PROMPT` | Tingnan ang halimbawa | Benchmark prompt |
| `BENCH_STREAM` | `0` | Sukatin ang first-token latency |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Pangunahing agent model |
| `AGENT_MODEL_EDITOR` | Pangunahing | Editor agent model |
| `SLM_ALIAS` | `phi-4-mini` | Maliit na language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Malaking language model |
| `COMPARE_PROMPT` | Tingnan ang halimbawa | Comparison prompt |

## Mga Inirerekomendang Modelo

### Para sa Development at Testing
- **phi-4-mini** - Balanseng kalidad at bilis
- **qwen2.5-0.5b** - Napakabilis para sa classification
- **gemma-2-2b** - Magandang kalidad, katamtamang bilis

### Para sa Produksyon
- **phi-4-mini** - Pangkalahatang layunin
- **deepseek-coder-1.3b** - Code generation
- **qwen2.5-7b** - Mataas na kalidad ng mga sagot

## Dokumentasyon ng SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Pagkuha ng Tulong

1. Suriin ang status ng serbisyo: `foundry service status`
2. Tingnan ang mga log: Suriin ang Foundry Local service logs
3. Suriin ang SDK docs: https://github.com/microsoft/Foundry-Local
4. Suriin ang sample code: Ang lahat ng mga halimbawa ay may detalyadong docstrings

## Mga Susunod na Hakbang

1. Kumpletuhin ang lahat ng session ng workshop nang sunod-sunod
2. Subukan ang iba't ibang modelo
3. I-modify ang mga halimbawa para sa iyong mga use case
4. Suriin ang `SDK_MIGRATION_NOTES.md` para sa mga advanced na pattern

---

**Huling Na-update**: 2025-01-08  
**Bersyon ng Workshop**: Pinakabago  
**SDK**: Foundry Local Python SDK

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.