<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-11-11T17:42:53+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "pcm"
}
-->
# Foundry Local SDK Migration Notes

## Overview

All Python files wey dey Workshop folder don update to follow di latest pattern wey dey official [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Changes Summary

### Core Infrastructure (`workshop_utils.py`)

#### Better Features:
- **Endpoint Override Support**: Add `FOUNDRY_LOCAL_ENDPOINT` environment variable support
- **Beta Error Handling**: Better way to handle exception wit detailed error message
- **Beta Caching**: Cache keys now dey include endpoint for multi-endpoint scenarios
- **Exponential Backoff**: Retry logic now dey use exponential backoff for better reliability
- **Type Annotations**: Add full type hints for better IDE support

#### New Things:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Sample Applications

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Change default model from `phi-3.5-mini` to `phi-4-mini`
- Add endpoint override support
- Better documentation wit SDK references

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Change to use `phi-4-mini` as default
- Add endpoint override support
- Better documentation wit environment variable details

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- Change model defaults
- Add endpoint configuration
- Better error handling

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Change default model list to include `phi-4-mini`
- Add full environment variable documentation
- Better function documentation
- Add endpoint override support everywhere

#### Session 04: Model Comparison (`model_compare.py`)
- Change default LLM from `gpt-oss-20b` to `qwen2.5-7b`
- Add endpoint configuration
- Better documentation

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Add type hints (change `str | None` to `Optional[str]`)
- Better Agent class documentation
- Add endpoint override support
- Better initialization pattern

#### Session 06: Model Router (`models_router.py`)
- Add endpoint configuration
- Better intent detection documentation
- Better routing logic documentation

#### Session 06: Pipeline (`models_pipeline.py`)
- Add full function documentation
- Better step-by-step documentation
- Better error handling

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Add endpoint override support
- Change default models
- Better function documentation
- Better error handling

#### CLI Linter (`lint_markdown_cli.py`)
- Add SDK reference links
- Better usage documentation

### Tests

#### Smoke Tests (`smoke.py`)
- Add endpoint override support
- Better documentation
- Better test case documentation
- Better error reporting

## Environment Variables

All samples now dey support dis environment variables:

### Core Configuration
- `FOUNDRY_LOCAL_ALIAS` - Model alias wey you go use (default dey different for each sample)
- `FOUNDRY_LOCAL_ENDPOINT` - Override service endpoint (optional)
- `SHOW_USAGE` - Show token usage statistics (default: "0")
- `RETRY_ON_FAIL` - Enable retry logic (default: "1")
- `RETRY_BACKOFF` - Initial retry delay in seconds (default: "1.0")

### Sample-Specific
- `EMBED_MODEL` - Embedding model for RAG samples
- `BENCH_MODELS` - Comma-separated models for benchmarking
- `BENCH_ROUNDS` - Number of benchmark rounds
- `BENCH_PROMPT` - Test prompt for benchmarks
- `BENCH_STREAM` - Measure first-token latency
- `RAG_QUESTION` - Test question for RAG samples
- `AGENT_MODEL_PRIMARY` - Primary agent model
- `AGENT_MODEL_EDITOR` - Editor agent model
- `SLM_ALIAS` - Small language model alias
- `LLM_ALIAS` - Large language model alias

## SDK Best Practices Implemented

### 1. Correct Client Initialization
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Model Info Retrieval
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Error Handling
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry Logic wit Exponential Backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Streaming Support
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Migration Guide for Custom Samples

If you dey create new samples or dey update old ones:

1. **Use `workshop_utils.py` helpers**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Support endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Add full documentation**:
   - Environment variables for docstring
   - SDK reference link
   - Usage examples

4. **Use type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Do correct error handling**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testing

You fit test all samples wit:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK Documentation References

- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentation**: Check SDK repository for latest API docs

## Breaking Changes

### None Expected
All di changes dey backward compatible. Di updates mainly:
- Add new optional features (endpoint override)
- Better error handling
- Better documentation
- Change default model names to current recommendations

### Optional Enhancements
You fit wan update your code to use:
- `FOUNDRY_LOCAL_ENDPOINT` for clear endpoint control
- `SHOW_USAGE=1` for token usage visibility
- Updated model defaults (`phi-4-mini` instead of `phi-3.5-mini`)

## Common Issues & Solutions

### Issue: "Client initialization failed"
**Solution**: Make sure say Foundry Local service dey run:
```bash
foundry service start
foundry model run phi-4-mini
```

### Issue: "Model not found"
**Solution**: Check available models:
```bash
foundry model list
```

### Issue: Endpoint connection errors
**Solution**: Confirm endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Next Steps

1. **Update Module08 samples**: Apply di same pattern to Module08/samples
2. **Add integration tests**: Create full test suite
3. **Performance benchmarking**: Compare before/after performance
4. **Documentation updates**: Update main README wit new patterns

## Contribution Guidelines

When you dey add new samples:
1. Use `workshop_utils.py` for consistency
2. Follow di pattern wey dey existing samples
3. Add full docstrings
4. Include SDK reference links
5. Support endpoint override
6. Add correct type hints
7. Include usage examples for docstring

## Version Compatibility

Dis updates dey compatible wit:
- `foundry-local-sdk` (latest)
- `openai>=1.30.0`
- Python 3.8+

---

**Last Updated**: 2025-01-08  
**Maintainer**: EdgeAI Workshop Team  
**SDK Version**: Foundry Local SDK (latest 0.7.117+67073234e7)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di main source. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->