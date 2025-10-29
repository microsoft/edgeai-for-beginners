<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T21:21:57+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "pa"
}
-->
# ਵਰਕਸ਼ਾਪ ਸ਼ੁਰੂਆਤੀ ਗਾਈਡ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

### 1. Foundry Local ਇੰਸਟਾਲ ਕਰੋ

ਅਧਿਕਾਰਤ ਇੰਸਟਾਲੇਸ਼ਨ ਗਾਈਡ ਦੀ ਪਾਲਨਾ ਕਰੋ:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python Dependencies ਇੰਸਟਾਲ ਕਰੋ

ਵਰਕਸ਼ਾਪ ਡਾਇਰੈਕਟਰੀ ਤੋਂ:

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

## ਵਰਕਸ਼ਾਪ ਸੈਂਪਲ ਚਲਾਉਣਾ

### ਸੈਸ਼ਨ 01: ਬੇਸਿਕ ਚੈਟ

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਜ਼:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### ਸੈਸ਼ਨ 02: RAG ਪਾਈਪਲਾਈਨ

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਜ਼:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### ਸੈਸ਼ਨ 02: RAG ਮੁਲਾਂਕਣ (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**ਨੋਟ**: ਵਾਧੂ dependencies ਦੀ ਲੋੜ ਹੈ ਜੋ `requirements.txt` ਰਾਹੀਂ ਇੰਸਟਾਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ

### ਸੈਸ਼ਨ 03: ਬੈਂਚਮਾਰਕਿੰਗ

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਜ਼:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**ਆਉਟਪੁੱਟ**: JSON ਜਿਸ ਵਿੱਚ latency, throughput, ਅਤੇ ਪਹਿਲਾ-ਟੋਕਨ ਮੈਟ੍ਰਿਕਸ ਹਨ

### ਸੈਸ਼ਨ 04: ਮਾਡਲ ਤੁਲਨਾ

```bash
cd Workshop/samples
python -m session04.model_compare
```

**ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਜ਼:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### ਸੈਸ਼ਨ 05: ਮਲਟੀ-ਏਜੰਟ ਆਰਕਸਟਰੈਸ਼ਨ

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਜ਼:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### ਸੈਸ਼ਨ 06: ਮਾਡਲ ਰਾਊਟਰ

```bash
cd Workshop/samples
python -m session06.models_router
```

**ਰੂਟਿੰਗ ਲਾਜਿਕ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ** ਕਈ ਇਰਾਦਿਆਂ ਨਾਲ (ਕੋਡ, ਸੰਖੇਪ, ਵਰਗੀਕਰਨ)

### ਸੈਸ਼ਨ 06: ਪਾਈਪਲਾਈਨ

```bash
python -m session06.models_pipeline
```

**ਜਟਿਲ ਬਹੁ-ਕਦਮ ਪਾਈਪਲਾਈਨ** ਯੋਜਨਾ, ਕਾਰਜ, ਅਤੇ ਸੁਧਾਰ ਨਾਲ

## ਸਕ੍ਰਿਪਟਸ

### ਬੈਂਚਮਾਰਕ ਰਿਪੋਰਟ ਐਕਸਪੋਰਟ ਕਰੋ

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**ਆਉਟਪੁੱਟ**: Markdown ਟੇਬਲ + JSON ਮੈਟ੍ਰਿਕਸ

### Markdown CLI ਪੈਟਰਨਜ਼ ਲਿੰਟ ਕਰੋ

```bash
python lint_markdown_cli.py --verbose
```

**ਉਦੇਸ਼**: ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਵਿੱਚ ਪੁਰਾਣੇ CLI ਪੈਟਰਨਜ਼ ਦੀ ਪਛਾਣ ਕਰੋ

## ਟੈਸਟਿੰਗ

### ਸਮੋਕ ਟੈਸਟਸ

```bash
cd Workshop
python -m tests.smoke
```

**ਟੈਸਟਸ**: ਮੁੱਖ ਸੈਂਪਲਜ਼ ਦੀ ਬੁਨਿਆਦੀ ਕਾਰਗੁਜ਼ਾਰੀ

## ਸਮੱਸਿਆ ਹੱਲ

### ਸਰਵਿਸ ਚਲ ਰਹੀ ਨਹੀਂ

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### ਮੋਡਿਊਲ ਇੰਪੋਰਟ ਐਰਰਸ

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### ਕਨੈਕਸ਼ਨ ਐਰਰਸ

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## ਇਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਰਿਫਰੈਂਸ

### ਕੋਰ ਕਨਫਿਗਰੇਸ਼ਨ
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਵੇਰਵਾ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | ਵੱਖ-ਵੱਖ | ਵਰਤਣ ਲਈ ਮਾਡਲ ਅਲਿਆਸ |
| `FOUNDRY_LOCAL_ENDPOINT` | ਆਟੋ | ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਨੂੰ ਓਵਰਰਾਈਡ ਕਰੋ |
| `SHOW_USAGE` | `0` | ਟੋਕਨ ਵਰਤੋਂ ਦੇ ਅੰਕੜੇ ਦਿਖਾਓ |
| `RETRY_ON_FAIL` | `1` | ਰੀਟ੍ਰਾਈ ਲਾਜਿਕ ਨੂੰ ਐਨਬਲ ਕਰੋ |
| `RETRY_BACKOFF` | `1.0` | ਸ਼ੁਰੂਆਤੀ ਰੀਟ੍ਰਾਈ ਡਿਲੇ (ਸਕਿੰਟ) |

### ਸੈਸ਼ਨ-ਵਿਸ਼ੇਸ਼
| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਵੇਰਵਾ |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ਐਮਬੈਡਿੰਗ ਮਾਡਲ |
| `RAG_QUESTION` | ਸੈਂਪਲ ਵੇਖੋ | RAG ਟੈਸਟ ਪ੍ਰਸ਼ਨ |
| `BENCH_MODELS` | ਵੱਖ-ਵੱਖ | ਕਾਮਾ-ਅਲੱਗ ਮਾਡਲ |
| `BENCH_ROUNDS` | `3` | ਬੈਂਚਮਾਰਕ ਇਟਰੇਸ਼ਨ |
| `BENCH_PROMPT` | ਸੈਂਪਲ ਵੇਖੋ | ਬੈਂਚਮਾਰਕ ਪ੍ਰੋਮਪਟ |
| `BENCH_STREAM` | `0` | ਪਹਿਲਾ-ਟੋਕਨ latency ਮਾਪੋ |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ਪ੍ਰਾਇਮਰੀ ਏਜੰਟ ਮਾਡਲ |
| `AGENT_MODEL_EDITOR` | ਪ੍ਰਾਇਮਰੀ | ਐਡੀਟਰ ਏਜੰਟ ਮਾਡਲ |
| `SLM_ALIAS` | `phi-4-mini` | ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `LLM_ALIAS` | `qwen2.5-7b` | ਵੱਡਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `COMPARE_PROMPT` | ਸੈਂਪਲ ਵੇਖੋ | ਤੁਲਨਾ ਪ੍ਰੋਮਪਟ |

## ਸਿਫਾਰਸ਼ੀ ਮਾਡਲ

### ਵਿਕਾਸ ਅਤੇ ਟੈਸਟਿੰਗ
- **phi-4-mini** - ਗੁਣਵੱਤਾ ਅਤੇ ਗਤੀ ਵਿੱਚ ਸੰਤੁਲਨ
- **qwen2.5-0.5b** - ਵਰਗੀਕਰਨ ਲਈ ਬਹੁਤ ਤੇਜ਼
- **gemma-2-2b** - ਚੰਗੀ ਗੁਣਵੱਤਾ, ਮਧਮ ਗਤੀ

### ਉਤਪਾਦਨ ਸਥਿਤੀਆਂ
- **phi-4-mini** - ਆਮ ਉਦੇਸ਼
- **deepseek-coder-1.3b** - ਕੋਡ ਜਨਰੇਸ਼ਨ
- **qwen2.5-7b** - ਉੱਚ ਗੁਣਵੱਤਾ ਜਵਾਬ

## SDK ਡੌਕੂਮੈਂਟੇਸ਼ਨ

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

1. ਸਰਵਿਸ ਸਥਿਤੀ ਚੈੱਕ ਕਰੋ: `foundry service status`
2. ਲੌਗ ਵੇਖੋ: Foundry Local ਸਰਵਿਸ ਲੌਗ ਚੈੱਕ ਕਰੋ
3. SDK ਡੌਕਸ ਚੈੱਕ ਕਰੋ: https://github.com/microsoft/Foundry-Local
4. ਸੈਂਪਲ ਕੋਡ ਦੀ ਸਮੀਖਿਆ ਕਰੋ: ਸਾਰੇ ਸੈਂਪਲਜ਼ ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਡੌਕਸਟ੍ਰਿੰਗਸ ਹਨ

## ਅਗਲੇ ਕਦਮ

1. ਸਾਰੇ ਵਰਕਸ਼ਾਪ ਸੈਸ਼ਨ ਕ੍ਰਮਵਾਰ ਪੂਰੇ ਕਰੋ
2. ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰੋ
3. ਆਪਣੇ ਉਦੇਸ਼ਾਂ ਲਈ ਸੈਂਪਲਜ਼ ਨੂੰ ਸੋਧੋ
4. `SDK_MIGRATION_NOTES.md` ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਜਟਿਲ ਪੈਟਰਨਜ਼ ਲਈ

---

**ਆਖਰੀ ਅਪਡੇਟ**: 2025-01-08  
**ਵਰਕਸ਼ਾਪ ਵਰਜਨ**: ਨਵੀਂਤਮ  
**SDK**: Foundry Local Python SDK

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।