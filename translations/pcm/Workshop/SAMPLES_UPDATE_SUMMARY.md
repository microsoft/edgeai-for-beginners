<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-11-11T17:42:23+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "pcm"
}
-->
# Workshop Samples - Foundry Local SDK Update Summary

## Overview

All Python samples wey dey for `Workshop/samples` folder don update to follow Foundry Local SDK best practices and make sure say e dey consistent for di workshop.

**Date**: October 8, 2025  
**Scope**: 9 Python files across 6 workshop sessions  
**Primary Focus**: Error handling, documentation, SDK patterns, user experience

---

## Updated Files

### Session 01: Getting Started
- ✅ `chat_bootstrap.py` - Basic chat and streaming examples

### Session 02: RAG Solutions
- ✅ `rag_pipeline.py` - RAG implementation wit embeddings
- ✅ `rag_eval_ragas.py` - RAG evaluation wit RAGAS metrics

### Session 03: Open Source Models
- ✅ `benchmark_oss_models.py` - Multi-model benchmarking

### Session 04: Cutting Edge Models
- ✅ `model_compare.py` - SLM vs LLM comparison

### Session 05: AI-Powered Agents
- ✅ `agents_orchestrator.py` - Multi-agent coordination

### Session 06: Models as Tools
- ✅ `models_router.py` - Intent-based model routing
- ✅ `models_pipeline.py` - Multi-step routed pipeline

### Supporting Infrastructure
- ✅ `workshop_utils.py` - E already dey follow best practices (no changes needed)

---

## Key Improvements

### 1. Enhanced Error Handling

**Before:**
```python
manager, client, model_id = get_client(alias)
```

**After:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Benefits:**
- Better way to handle errors wit clear error messages
- Tips wey go help troubleshoot
- Correct exit codes for scripting

### 2. Better Import Management

**Before:**
```python
from sentence_transformers import SentenceTransformer
```

**After:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Benefits:**
- Clear instructions if dependencies no dey
- E go stop confusing import errors
- User-friendly installation instructions

### 3. Comprehensive Documentation

**Added to all samples:**
- Environment variable documentation inside docstrings
- SDK reference links
- Usage examples
- Detailed function/parameter documentation
- Type hints wey go help IDE support

**Example:**
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

### 4. Improved User Feedback

**Added informative logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Progress indicators:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Structured output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robust Benchmarking

**Session 03 improvements:**
- Per-model error handling (e go continue if e fail)
- Detailed progress reporting
- Warmup rounds wey dey properly executed
- First-token latency measurement support
- Clear separation of stages

### 6. Consistent Type Hints

**Added throughout:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Benefits:**
- Better IDE autocomplete
- Early error detection
- Code wey dey explain itself

### 7. Enhanced Model Router

**Session 06 improvements:**
- Full documentation for intent detection
- Explanation of model selection algorithm
- Detailed routing logs
- Test output formatting
- Error recovery for batch testing

### 8. Multi-Agent Orchestration

**Session 05 improvements:**
- Progress reporting stage by stage
- Per-agent error handling
- Clear pipeline structure
- Better memory management documentation

---

## Testing Checklist

### Prerequisites
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Test Each Sample

#### Session 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Session 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Session 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Session 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Session 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Session 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Environment Variables Reference

### Global (All Samples)
| Variable | Description | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Model alias wey go dey use | E dey change by sample |
| `FOUNDRY_LOCAL_ENDPOINT` | Override service endpoint | Auto-detected |
| `SHOW_USAGE` | Show token usage | `0` |
| `RETRY_ON_FAIL` | Enable retry logic | `1` |
| `RETRY_BACKOFF` | Initial retry delay | `1.0` |

### Sample-Specific
| Variable | Used By | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | Session 02 | Embedding model name |
| `RAG_QUESTION` | Session 02 | Test question for RAG |
| `BENCH_MODELS` | Session 03 | Comma-separated models to benchmark |
| `BENCH_ROUNDS` | Session 03 | Number of benchmark rounds |
| `BENCH_PROMPT` | Session 03 | Test prompt for benchmarks |
| `BENCH_STREAM` | Session 03 | Measure first-token latency |
| `SLM_ALIAS` | Session 04 | Small language model |
| `LLM_ALIAS` | Session 04 | Large language model |
| `COMPARE_PROMPT` | Session 04 | Comparison test prompt |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primary agent model |
| `AGENT_MODEL_EDITOR` | Session 05 | Editor agent model |
| `AGENT_QUESTION` | Session 05 | Test question for agents |
| `PIPELINE_TASK` | Session 06 | Task for pipeline |

---

## Breaking Changes

**None** - All changes dey backward compatible.

Existing scripts go still dey work. New features na:
- Optional environment variables
- Better error messages (e no go break functionality)
- Extra logging (fit suppress am)
- Better type hints (e no dey affect runtime)

---

## Best Practices Implemented

### 1. Always Use Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Proper Error Handling Pattern
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informative Logging
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type Hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Comprehensive Docstrings
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

### 6. Environment Variable Support
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Graceful Degradation
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

## Common Issues & Solutions

### Issue: Import Errors
**Solution:** Install missing dependencies
```bash
pip install sentence-transformers ragas datasets numpy
```

### Issue: Connection Errors
**Solution:** Make sure say Foundry Local dey run
```bash
foundry service status
foundry model run phi-4-mini
```

### Issue: Model Not Found
**Solution:** Check available models
```bash
foundry model ls
foundry model download <alias>
```

### Issue: Slow Performance
**Solution:** Use smaller models or adjust parameters
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Next Steps

### 1. Test All Samples
Follow di testing checklist wey dey above to confirm say all samples dey work well.

### 2. Update Documentation
- Update session markdown files wit new examples
- Add troubleshooting section to main README
- Create quick reference guide

### 3. Create Integration Tests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Add Performance Benchmarks
Track performance improvements wey come from better error handling.

### 5. User Feedback
Collect feedback from workshop participants about:
- How clear error messages be
- How complete documentation be
- How easy e be to use

---

## Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Main Repository**: https://github.com/microsoft/Foundry-Local

---

## Maintenance

### Adding New Samples
Follow dis pattern when you dey create new samples:

1. Use `workshop_utils` for client management
2. Add better error handling
3. Include environment variable support
4. Add type hints and docstrings
5. Provide informative logging
6. Include usage examples inside docstring
7. Link to SDK documentation

### Reviewing Updates
When you dey review sample updates, check say:
- [ ] Error handling dey for all I/O operations
- [ ] Type hints dey for public functions
- [ ] Docstrings dey complete
- [ ] Environment variable documentation dey
- [ ] User feedback dey informative
- [ ] SDK reference links dey
- [ ] Code style dey consistent

---

**Summary**: All Workshop Python samples don follow Foundry Local SDK best practices wit better error handling, complete documentation, and improved user experience. No breaking changes - all existing functionality dey intact and e don better.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->