# Workshop Quick Start Guide

## Wetin You Need

### 1. Install Foundry Local

Follow di official installation guide:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Install Python Dependencies

From di Workshop directory:

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

## How to Run Workshop Samples

### Session 01: Basic Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Environment Variables:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Environment Variables:**
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

**Note**: E need extra dependencies wey you go install through `requirements.txt`

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Environment Variables:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON wey get latency, throughput, and first-token metrics

### Session 04: Model Comparison

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Environment Variables:**
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

**Environment Variables:**
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

**E dey test routing logic** with plenty intents (code, summarize, classification)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**E be complex multi-step pipeline** wey get planning, execution, and refinement

## Scripts

### Export Benchmark Report

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

**Purpose**: E dey detect old CLI patterns for documentation

## Testing

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Tests**: E dey test di basic functionality of di key samples

## Troubleshooting

### Service No Dey Run

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Module Import Errors

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Connection Errors

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model No Dey

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Environment Variable Reference

### Core Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | E dey change | Model alias wey you go use |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Override service endpoint |
| `SHOW_USAGE` | `0` | Show token usage stats |
| `RETRY_ON_FAIL` | `1` | Enable retry logic |
| `RETRY_BACKOFF` | `1.0` | Initial retry delay (seconds) |

### Session-Specific
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | See sample | RAG test question |
| `BENCH_MODELS` | E dey change | Comma-separated models |
| `BENCH_ROUNDS` | `3` | Benchmark iterations |
| `BENCH_PROMPT` | See sample | Benchmark prompt |
| `BENCH_STREAM` | `0` | Measure first-token latency |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primary agent model |
| `AGENT_MODEL_EDITOR` | Primary | Editor agent model |
| `SLM_ALIAS` | `phi-4-mini` | Small language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Large language model |
| `COMPARE_PROMPT` | See sample | Comparison prompt |

## Recommended Models

### Development & Testing
- **phi-4-mini** - E balance quality and speed
- **qwen2.5-0.5b** - E fast well for classification
- **gemma-2-2b** - E get good quality, moderate speed

### Production Scenarios
- **phi-4-mini** - General purpose
- **deepseek-coder-1.3b** - Code generation
- **qwen2.5-7b** - High quality responses

## SDK Documentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## How to Get Help

1. Check service status: `foundry service status`
2. View logs: Check Foundry Local service logs
3. Check SDK docs: https://github.com/microsoft/Foundry-Local
4. Review sample code: All samples get detailed docstrings

## Next Steps

1. Finish all di workshop sessions one by one
2. Try different models
3. Change di samples to fit your own use cases

---

**Last Updated**: 2025-01-08  
**Workshop Version**: Latest  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->