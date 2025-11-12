<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T21:14:23+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "en"
}
-->
# Workshop Quick Start Guide

## Prerequisites

### 1. Install Foundry Local

Follow the official installation guide:
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

From the Workshop directory:

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

## Running Workshop Samples

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

**Note**: Requires additional dependencies installed via `requirements.txt`

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

**Output**: JSON with latency, throughput, and first-token metrics

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

**Tests routing logic** with multiple intents (code, summarize, classification)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Complex multi-step pipeline** with planning, execution, and refinement

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

**Purpose**: Detect deprecated CLI patterns in documentation

## Testing

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Tests**: Basic functionality of key samples

## Troubleshooting

### Service Not Running

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

### Model Not Found

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
| `FOUNDRY_LOCAL_ALIAS` | Varies | Model alias to use |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Override service endpoint |
| `SHOW_USAGE` | `0` | Show token usage stats |
| `RETRY_ON_FAIL` | `1` | Enable retry logic |
| `RETRY_BACKOFF` | `1.0` | Initial retry delay (seconds) |

### Session-Specific
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | See sample | RAG test question |
| `BENCH_MODELS` | Varies | Comma-separated models |
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
- **phi-4-mini** - Balanced quality and speed
- **qwen2.5-0.5b** - Very fast for classification
- **gemma-2-2b** - Good quality, moderate speed

### Production Scenarios
- **phi-4-mini** - General purpose
- **deepseek-coder-1.3b** - Code generation
- **qwen2.5-7b** - High quality responses

## SDK Documentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Getting Help

1. Check service status: `foundry service status`
2. View logs: Check Foundry Local service logs
3. Check SDK docs: https://github.com/microsoft/Foundry-Local
4. Review sample code: All samples have detailed docstrings

## Next Steps

1. Complete all workshop sessions in order
2. Experiment with different models
3. Modify samples for your use cases

---

**Last Updated**: 2025-01-08  
**Workshop Version**: Latest  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->