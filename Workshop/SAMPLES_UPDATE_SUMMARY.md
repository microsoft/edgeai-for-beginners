# Workshop Samples - Foundry Local SDK Update Summary

## Overview

All Python samples in the `Workshop/samples` directory have been updated to follow Foundry Local SDK best practices and ensure consistency across the workshop.

**Date**: October 8, 2025  
**Scope**: 9 Python files across 6 workshop sessions  
**Primary Focus**: Error handling, documentation, SDK patterns, user experience

---

## Updated Files

### Session 01: Getting Started
- ✅ `chat_bootstrap.py` - Basic chat and streaming examples

### Session 02: RAG Solutions
- ✅ `rag_pipeline.py` - RAG implementation with embeddings
- ✅ `rag_eval_ragas.py` - RAG evaluation with RAGAS metrics

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
- ✅ `workshop_utils.py` - Already following best practices (no changes needed)

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
- Graceful error handling with clear error messages
- Actionable troubleshooting hints
- Proper exit codes for scripting

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
- Clear guidance when dependencies are missing
- Prevents cryptic import errors
- User-friendly installation instructions

### 3. Comprehensive Documentation

**Added to all samples:**
- Environment variable documentation in docstrings
- SDK reference links
- Usage examples
- Detailed function/parameter documentation
- Type hints for better IDE support

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
- Per-model error handling (continues on failure)
- Detailed progress reporting
- Warmup rounds properly executed
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
- Self-documenting code

### 7. Enhanced Model Router

**Session 06 improvements:**
- Comprehensive intent detection documentation
- Model selection algorithm explanation
- Detailed routing logs
- Test output formatting
- Error recovery in batch testing

### 8. Multi-Agent Orchestration

**Session 05 improvements:**
- Stage-by-stage progress reporting
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
| `FOUNDRY_LOCAL_ALIAS` | Model alias to use | Varies by sample |
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

**None** - All changes are backward compatible.

Existing scripts will continue to work. New features are:
- Optional environment variables
- Enhanced error messages (don't break functionality)
- Additional logging (can be suppressed)
- Better type hints (no runtime impact)

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
**Solution:** Ensure Foundry Local is running
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
Run through the testing checklist above to verify all samples work correctly.

### 2. Update Documentation
- Update session markdown files with new examples
- Add troubleshooting section to main README
- Create quick reference guide

### 3. Create Integration Tests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Add Performance Benchmarks
Track performance improvements from error handling enhancements.

### 5. User Feedback
Collect feedback from workshop participants on:
- Error message clarity
- Documentation completeness
- Ease of use

---

## Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Main Repository**: https://github.com/microsoft/Foundry-Local

---

## Maintenance

### Adding New Samples
Follow these patterns when creating new samples:

1. Use `workshop_utils` for client management
2. Add comprehensive error handling
3. Include environment variable support
4. Add type hints and docstrings
5. Provide informative logging
6. Include usage examples in docstring
7. Link to SDK documentation

### Reviewing Updates
When reviewing sample updates, check for:
- [ ] Error handling on all I/O operations
- [ ] Type hints on public functions
- [ ] Comprehensive docstrings
- [ ] Environment variable documentation
- [ ] Informative user feedback
- [ ] SDK reference links
- [ ] Consistent code style

---

**Summary**: All Workshop Python samples now follow Foundry Local SDK best practices with enhanced error handling, comprehensive documentation, and improved user experience. No breaking changes - all existing functionality preserved and enhanced.
