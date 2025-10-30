<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:28:08+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "pa"
}
-->
# ਵਰਕਸ਼ਾਪ ਨਮੂਨੇ - ਫਾਉਂਡਰੀ ਲੋਕਲ SDK ਅਪਡੇਟ ਸਾਰ

## ਝਲਕ

`Workshop/samples` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸਾਰੇ Python ਨਮੂਨਿਆਂ ਨੂੰ ਫਾਉਂਡਰੀ ਲੋਕਲ SDK ਦੀਆਂ ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਦੇ ਅਨੁਸਾਰ ਅਪਡੇਟ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਵਰਕਸ਼ਾਪ ਵਿੱਚ ਸਥਿਰਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਇਆ ਗਿਆ ਹੈ।

**ਤਾਰੀਖ**: ਅਕਤੂਬਰ 8, 2025  
**ਸ਼੍ਰੇਣੀ**: 6 ਵਰਕਸ਼ਾਪ ਸੈਸ਼ਨਾਂ ਵਿੱਚ 9 Python ਫਾਈਲਾਂ  
**ਮੁੱਖ ਧਿਆਨ**: ਗਲਤੀ ਸੰਭਾਲ, ਦਸਤਾਵੇਜ਼, SDK ਪੈਟਰਨ, ਉਪਭੋਗਤਾ ਅਨੁਭਵ

---

## ਅਪਡੇਟ ਕੀਤੀਆਂ ਫਾਈਲਾਂ

### ਸੈਸ਼ਨ 01: ਸ਼ੁਰੂਆਤ ਕਰਨਾ
- ✅ `chat_bootstrap.py` - ਬੁਨਿਆਦੀ ਚੈਟ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਉਦਾਹਰਨਾਂ

### ਸੈਸ਼ਨ 02: RAG ਹੱਲ
- ✅ `rag_pipeline.py` - embeddings ਨਾਲ RAG ਲਾਗੂ ਕਰਨਾ
- ✅ `rag_eval_ragas.py` - RAGAS ਮਾਪਦੰਡਾਂ ਨਾਲ RAG ਮੁਲਾਂਕਣ

### ਸੈਸ਼ਨ 03: ਓਪਨ ਸੋਰਸ ਮਾਡਲ
- ✅ `benchmark_oss_models.py` - ਬਹੁ-ਮਾਡਲ ਬੈਂਚਮਾਰਕਿੰਗ

### ਸੈਸ਼ਨ 04: ਅਗਲੇ ਪੱਧਰ ਦੇ ਮਾਡਲ
- ✅ `model_compare.py` - SLM ਅਤੇ LLM ਦੀ ਤੁਲਨਾ

### ਸੈਸ਼ਨ 05: AI-ਚਲਿਤ ਏਜੰਟ
- ✅ `agents_orchestrator.py` - ਬਹੁ-ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ

### ਸੈਸ਼ਨ 06: ਮਾਡਲ ਟੂਲ ਵਜੋਂ
- ✅ `models_router.py` - ਇਰਾਦੇ-ਅਧਾਰਿਤ ਮਾਡਲ ਰੂਟਿੰਗ
- ✅ `models_pipeline.py` - ਬਹੁ-ਕਦਮ ਰੂਟ ਕੀਤੀ ਪਾਈਪਲਾਈਨ

### ਸਹਾਇਕ ਢਾਂਚਾ
- ✅ `workshop_utils.py` - ਪਹਿਲਾਂ ਹੀ ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਦਾ ਪਾਲਣ ਕਰ ਰਿਹਾ ਹੈ (ਕੋਈ ਬਦਲਾਅ ਦੀ ਲੋੜ ਨਹੀਂ)

---

## ਮੁੱਖ ਸੁਧਾਰ

### 1. ਗਲਤੀ ਸੰਭਾਲ ਵਿੱਚ ਸੁਧਾਰ

**ਪਹਿਲਾਂ:**
```python
manager, client, model_id = get_client(alias)
```

**ਬਾਅਦ:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**ਫਾਇਦੇ:**
- ਸਪਸ਼ਟ ਗਲਤੀ ਸੁਨੇਹਿਆਂ ਨਾਲ ਸੁਗਮ ਗਲਤੀ ਸੰਭਾਲ
- ਕਾਰਗਰ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਸੰਕੇਤ
- ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ ਸਹੀ ਐਗਜ਼ਿਟ ਕੋਡ

### 2. ਇੰਪੋਰਟ ਮੈਨੇਜਮੈਂਟ ਵਿੱਚ ਸੁਧਾਰ

**ਪਹਿਲਾਂ:**
```python
from sentence_transformers import SentenceTransformer
```

**ਬਾਅਦ:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**ਫਾਇਦੇ:**
- Dependencies ਦੀ ਗੁੰਮਸ਼ੁਦਾ ਹੋਣ 'ਤੇ ਸਪਸ਼ਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼
- ਗੁੰਝਲਦਾਰ ਇੰਪੋਰਟ ਗਲਤੀਆਂ ਤੋਂ ਬਚਾਅ
- ਉਪਭੋਗਤਾ-ਅਨੁਕੂਲ ਇੰਸਟਾਲੇਸ਼ਨ ਹਦਾਇਤਾਂ

### 3. ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼

**ਸਾਰੇ ਨਮੂਨਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ:**
- ਡੌਕਸਟ੍ਰਿੰਗ ਵਿੱਚ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦਸਤਾਵੇਜ਼
- SDK ਰਿਫਰੈਂਸ ਲਿੰਕ
- ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ
- ਵਿਸਤ੍ਰਿਤ ਫੰਕਸ਼ਨ/ਪੈਰਾਮੀਟਰ ਦਸਤਾਵੇਜ਼
- IDE ਸਹਾਇਤਾ ਲਈ ਟਾਈਪ ਹਿੰਟ

**ਉਦਾਹਰਨ:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. ਉਪਭੋਗਤਾ ਫੀਡਬੈਕ ਵਿੱਚ ਸੁਧਾਰ

**ਜਾਣਕਾਰੀਮਈ ਲੌਗਿੰਗ ਸ਼ਾਮਲ ਕੀਤੀ:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**ਪ੍ਰਗਤੀ ਸੂਚਕ:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. ਮਜ਼ਬੂਤ ਬੈਂਚਮਾਰਕਿੰਗ

**ਸੈਸ਼ਨ 03 ਸੁਧਾਰ:**
- ਪ੍ਰਤੀ-ਮਾਡਲ ਗਲਤੀ ਸੰਭਾਲ (ਫੇਲ੍ਹ ਹੋਣ 'ਤੇ ਜਾਰੀ)
- ਵਿਸਤ੍ਰਿਤ ਪ੍ਰਗਤੀ ਰਿਪੋਰਟਿੰਗ
- ਵਾਰਮਅੱਪ ਰਾਊਂਡ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਕੀਤੇ
- ਪਹਿਲੇ ਟੋਕਨ ਦੀ ਲੈਟੈਂਸੀ ਮਾਪਣ ਸਹਾਇਤਾ
- ਚਰਨਾਂ ਦੀ ਸਪਸ਼ਟ ਵੰਡ

### 6. ਸਥਿਰ ਟਾਈਪ ਹਿੰਟ

**ਸਾਰੇ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**ਫਾਇਦੇ:**
- ਬਿਹਤਰ IDE ਆਟੋਕੰਪਲੀਟ
- ਸ਼ੁਰੂਆਤੀ ਗਲਤੀ ਪਛਾਣ
- ਸਵੈ-ਦਸਤਾਵੇਜ਼ੀ ਕੋਡ

### 7. ਮਾਡਲ ਰੂਟਰ ਵਿੱਚ ਸੁਧਾਰ

**ਸੈਸ਼ਨ 06 ਸੁਧਾਰ:**
- ਵਿਸਤ੍ਰਿਤ ਇਰਾਦਾ ਪਛਾਣ ਦਸਤਾਵੇਜ਼
- ਮਾਡਲ ਚੋਣ ਐਲਗੋਰਿਦਮ ਦੀ ਵਿਆਖਿਆ
- ਵਿਸਤ੍ਰਿਤ ਰੂਟਿੰਗ ਲੌਗ
- ਟੈਸਟ ਆਉਟਪੁੱਟ ਫਾਰਮੈਟਿੰਗ
- ਬੈਚ ਟੈਸਟਿੰਗ ਵਿੱਚ ਗਲਤੀ ਰਿਕਵਰੀ

### 8. ਬਹੁ-ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ

**ਸੈਸ਼ਨ 05 ਸੁਧਾਰ:**
- ਚਰਨ-ਦਰ-ਚਰਨ ਪ੍ਰਗਤੀ ਰਿਪੋਰਟਿੰਗ
- ਪ੍ਰਤੀ-ਏਜੰਟ ਗਲਤੀ ਸੰਭਾਲ
- ਸਪਸ਼ਟ ਪਾਈਪਲਾਈਨ ਢਾਂਚਾ
- ਬਿਹਤਰ ਮੈਮਰੀ ਮੈਨੇਜਮੈਂਟ ਦਸਤਾਵੇਜ਼

---

## ਟੈਸਟਿੰਗ ਚੈੱਕਲਿਸਟ

### ਪੂਰਵ ਸ਼ਰਤਾਂ
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### ਹਰ ਨਮੂਨੇ ਦੀ ਜਾਂਚ ਕਰੋ

#### ਸੈਸ਼ਨ 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### ਸੈਸ਼ਨ 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### ਸੈਸ਼ਨ 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### ਸੈਸ਼ਨ 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### ਸੈਸ਼ਨ 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### ਸੈਸ਼ਨ 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦਸਤਾਵੇਜ਼

### ਗਲੋਬਲ (ਸਾਰੇ ਨਮੂਨੇ)
| ਵੈਰੀਏਬਲ | ਵੇਰਵਾ | ਡਿਫਾਲਟ |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | ਵਰਤਣ ਲਈ ਮਾਡਲ ਉਪਨਾਮ | ਨਮੂਨੇ ਅਨੁਸਾਰ |
| `FOUNDRY_LOCAL_ENDPOINT` | ਸੇਵਾ ਐਂਡਪੌਇੰਟ ਨੂੰ ਓਵਰਰਾਈਡ ਕਰੋ | ਆਟੋ-ਡਿਟੈਕਟ |
| `SHOW_USAGE` | ਟੋਕਨ ਵਰਤੋਂ ਦਿਖਾਓ | `0` |
| `RETRY_ON_FAIL` | ਰੀਟ੍ਰਾਈ ਲੌਜਿਕ ਨੂੰ ਚਾਲੂ ਕਰੋ | `1` |
| `RETRY_BACKOFF` | ਸ਼ੁਰੂਆਤੀ ਰੀਟ੍ਰਾਈ ਡਿਲੇ | `1.0` |

### ਨਮੂਨਾ-ਵਿਸ਼ੇਸ਼
| ਵੈਰੀਏਬਲ | ਵਰਤਿਆ ਗਿਆ | ਵੇਰਵਾ |
|----------|---------|-------------|
| `EMBED_MODEL` | ਸੈਸ਼ਨ 02 | embedding ਮਾਡਲ ਦਾ ਨਾਮ |
| `RAG_QUESTION` | ਸੈਸ਼ਨ 02 | RAG ਲਈ ਟੈਸਟ ਸਵਾਲ |
| `BENCH_MODELS` | ਸੈਸ਼ਨ 03 | ਬੈਂਚਮਾਰਕ ਕਰਨ ਲਈ ਮਾਡਲਾਂ ਦੀ ਕਾਮਾ-ਅਲੱਗ ਕੀਤੀ ਸੂਚੀ |
| `BENCH_ROUNDS` | ਸੈਸ਼ਨ 03 | ਬੈਂਚਮਾਰਕ ਰਾਊਂਡ ਦੀ ਗਿਣਤੀ |
| `BENCH_PROMPT` | ਸੈਸ਼ਨ 03 | ਬੈਂਚਮਾਰਕ ਲਈ ਟੈਸਟ ਪ੍ਰੋਮਪਟ |
| `BENCH_STREAM` | ਸੈਸ਼ਨ 03 | ਪਹਿਲੇ-ਟੋਕਨ ਲੈਟੈਂਸੀ ਮਾਪੋ |
| `SLM_ALIAS` | ਸੈਸ਼ਨ 04 | ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `LLM_ALIAS` | ਸੈਸ਼ਨ 04 | ਵੱਡਾ ਭਾਸ਼ਾ ਮਾਡਲ |
| `COMPARE_PROMPT` | ਸੈਸ਼ਨ 04 | ਤੁਲਨਾ ਟੈਸਟ ਪ੍ਰੋਮਪਟ |
| `AGENT_MODEL_PRIMARY` | ਸੈਸ਼ਨ 05 | ਪ੍ਰਾਇਮਰੀ ਏਜੰਟ ਮਾਡਲ |
| `AGENT_MODEL_EDITOR` | ਸੈਸ਼ਨ 05 | ਐਡੀਟਰ ਏਜੰਟ ਮਾਡਲ |
| `AGENT_QUESTION` | ਸੈਸ਼ਨ 05 | ਏਜੰਟਾਂ ਲਈ ਟੈਸਟ ਸਵਾਲ |
| `PIPELINE_TASK` | ਸੈਸ਼ਨ 06 | ਪਾਈਪਲਾਈਨ ਲਈ ਟਾਸਕ |

---

## ਤੋੜਨ ਵਾਲੇ ਬਦਲਾਅ

**ਕੋਈ ਨਹੀਂ** - ਸਾਰੇ ਬਦਲਾਅ ਪਿਛਲੇ ਵਰਜਨ ਨਾਲ ਅਨੁਕੂਲ ਹਨ।

ਮੌਜੂਦਾ ਸਕ੍ਰਿਪਟ ਕੰਮ ਕਰਦੇ ਰਹਿਣਗੇ। ਨਵੇਂ ਫੀਚਰ ਹਨ:
- ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ
- ਵਧੀਆ ਗਲਤੀ ਸੁਨੇਹੇ (ਫੰਕਸ਼ਨਲਿਟੀ ਨੂੰ ਖਰਾਬ ਨਹੀਂ ਕਰਦੇ)
- ਵਾਧੂ ਲੌਗਿੰਗ (ਦਬਾਈ ਜਾ ਸਕਦੀ ਹੈ)
- ਬਿਹਤਰ ਟਾਈਪ ਹਿੰਟ (ਕੋਈ ਰਨਟਾਈਮ ਪ੍ਰਭਾਵ ਨਹੀਂ)

---

## ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਲਾਗੂ ਕੀਤੀਆਂ

### 1. ਹਮੇਸ਼ਾ ਵਰਕਸ਼ਾਪ ਯੂਟਿਲਸ ਵਰਤੋ
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. ਸਹੀ ਗਲਤੀ ਸੰਭਾਲ ਪੈਟਰਨ
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. ਜਾਣਕਾਰੀਮਈ ਲੌਗਿੰਗ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. ਟਾਈਪ ਹਿੰਟ
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. ਵਿਸਤ੍ਰਿਤ ਡੌਕਸਟ੍ਰਿੰਗ
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸਹਾਇਤਾ
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. ਸੁਗਮ ਘਟਾਓ
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

### ਸਮੱਸਿਆ: ਇੰਪੋਰਟ ਗਲਤੀਆਂ
**ਹੱਲ:** ਗੁੰਮਸ਼ੁਦਾ Dependencies ਇੰਸਟਾਲ ਕਰੋ
```bash
pip install sentence-transformers ragas datasets numpy
```

### ਸਮੱਸਿਆ: ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ
**ਹੱਲ:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਚੱਲ ਰਿਹਾ ਹੈ
```bash
foundry service status
foundry model run phi-4-mini
```

### ਸਮੱਸਿਆ: ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ
**ਹੱਲ:** ਉਪਲਬਧ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
```bash
foundry model ls
foundry model download <alias>
```

### ਸਮੱਸਿਆ: ਧੀਮੀ ਪ੍ਰਦਰਸ਼ਨ
**ਹੱਲ:** ਛੋਟੇ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਾਂ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸਮਾਧਾਨ ਕਰੋ
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## ਅਗਲੇ ਕਦਮ

### 1. ਸਾਰੇ ਨਮੂਨਿਆਂ ਦੀ ਜਾਂਚ ਕਰੋ
ਉਪਰ ਦਿੱਤੇ ਟੈਸਟਿੰਗ ਚੈੱਕਲਿਸਟ ਦੁਆਰਾ ਚੱਲੋ ਤਾਂ ਜੋ ਸਾਰੇ ਨਮੂਨੇ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਨ।

### 2. ਦਸਤਾਵੇਜ਼ ਅਪਡੇਟ ਕਰੋ
- ਨਵੇਂ ਉਦਾਹਰਨਾਂ ਨਾਲ ਸੈਸ਼ਨ ਮਾਰਕਡਾਊਨ ਫਾਈਲਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ
- ਮੁੱਖ README ਵਿੱਚ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਸੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ
- ਤੇਜ਼ ਰਿਫਰੈਂਸ ਗਾਈਡ ਬਣਾਓ

### 3. ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟ ਬਣਾਓ
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. ਪ੍ਰਦਰਸ਼ਨ ਬੈਂਚਮਾਰਕ ਸ਼ਾਮਲ ਕਰੋ
ਗਲਤੀ ਸੰਭਾਲ ਸੁਧਾਰਾਂ ਤੋਂ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸੁਧਾਰਾਂ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ।

### 5. ਉਪਭੋਗਤਾ ਫੀਡਬੈਕ
ਵਰਕਸ਼ਾਪ ਦੇ ਭਾਗੀਦਾਰਾਂ ਤੋਂ ਫੀਡਬੈਕ ਇਕੱਠਾ ਕਰੋ:
- ਗਲਤੀ ਸੁਨੇਹੇ ਦੀ ਸਪਸ਼ਟਤਾ
- ਦਸਤਾਵੇਜ਼ ਦੀ ਪੂਰਨਤਾ
- ਵਰਤਣ ਦੀ ਸਹੂਲਤ

---

## ਸਰੋਤ

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **ਤੇਜ਼ ਰਿਫਰੈਂਸ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **ਮਾਈਗ੍ਰੇਸ਼ਨ ਨੋਟਸ**: `Workshop/SDK_MIGRATION_NOTES.md`
- **ਮੁੱਖ ਰਿਪੋਜ਼ਟਰੀ**: https://github.com/microsoft/Foundry-Local

---

## ਰਖਰਖਾਅ

### ਨਵੇਂ ਨਮੂਨੇ ਸ਼ਾਮਲ ਕਰਨਾ
ਨਵੇਂ ਨਮੂਨੇ ਬਣਾਉਣ ਸਮੇਂ ਇਹ ਪੈਟਰਨ ਫਾਲੋ ਕਰੋ:

1. ਕਲਾਇੰਟ ਮੈਨੇਜਮੈਂਟ ਲਈ `workshop_utils` ਦੀ ਵਰਤੋਂ ਕਰੋ
2. ਵਿਸਤ੍ਰਿਤ ਗਲਤੀ ਸੰਭਾਲ ਸ਼ਾਮਲ ਕਰੋ
3. ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕਰੋ
4. ਟਾਈਪ ਹਿੰਟ ਅਤੇ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
5. ਜਾਣਕਾਰੀਮਈ ਲੌਗਿੰਗ ਪ੍ਰਦਾਨ ਕਰੋ
6. ਡੌਕਸਟ੍ਰਿੰਗ ਵਿੱਚ ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਕਰੋ
7. SDK ਦਸਤਾਵੇਜ਼ ਲਈ ਲਿੰਕ ਸ਼ਾਮਲ ਕਰੋ

### ਅਪਡੇਟ ਦੀ ਸਮੀਖਿਆ ਕਰਨਾ
ਨਮੂਨਾ ਅਪਡੇਟ ਦੀ ਸਮੀਖਿਆ ਕਰਦੇ ਸਮੇਂ, ਇਹ ਚੈੱਕ ਕਰੋ:
- [ ] ਸਾਰੇ I/O ਕਾਰਵਾਈਆਂ 'ਤੇ ਗਲਤੀ ਸੰਭਾਲ
- [ ] ਪਬਲਿਕ ਫੰਕਸ਼ਨਾਂ 'ਤੇ ਟਾਈਪ ਹਿੰਟ
- [ ] ਵਿਸਤ੍ਰਿਤ ਡੌਕਸਟ੍ਰਿੰਗ
- [ ] ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦਸਤਾਵੇਜ਼
- [ ] ਜਾਣਕਾਰੀਮਈ ਉਪਭੋਗਤਾ ਫੀਡਬੈਕ
- [ ] SDK ਰਿਫਰੈਂਸ ਲਿੰਕ
- [ ] ਸਥਿਰ ਕੋਡ ਸ਼ੈਲੀ

---

**ਸਾਰ**: ਸਾਰੇ ਵਰਕਸ਼ਾਪ Python ਨਮੂਨੇ ਹੁਣ ਫਾਉਂਡਰੀ ਲੋਕਲ SDK ਦੀਆਂ ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਦਾ ਪਾਲਣ ਕਰਦੇ ਹਨ, ਗਲਤੀ ਸੰਭਾਲ, ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼, ਅਤੇ ਬਿਹਤਰ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਨਾਲ। ਕੋਈ ਤੋੜਨ ਵਾਲੇ ਬਦਲਾਅ ਨਹੀਂ - ਸਾਰੀ ਮੌਜੂਦਾ ਫੰਕਸ਼ਨਲਿਟੀ ਸੁਰੱਖਿਅਤ ਅਤੇ ਵਧੀਆ ਕੀਤੀ ਗਈ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।