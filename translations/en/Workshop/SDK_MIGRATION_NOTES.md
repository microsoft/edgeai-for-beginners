<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T19:59:39+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "en"
}
-->
# Foundry Local SDK Migration Notes

## Overview

All Python files in the Workshop folder have been updated to align with the latest patterns from the official [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Changes Summary

### Core Infrastructure (`workshop_utils.py`)

#### Enhanced Features:
- **Endpoint Override Support**: Added support for the `FOUNDRY_LOCAL_ENDPOINT` environment variable.
- **Improved Error Handling**: Enhanced exception handling with more detailed error messages.
- **Enhanced Caching**: Cache keys now include the endpoint to support multi-endpoint scenarios.
- **Exponential Backoff**: Retry logic now incorporates exponential backoff for improved reliability.
- **Type Annotations**: Comprehensive type hints added for better IDE support.

#### New Capabilities:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Sample Applications

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Default model updated from `phi-3.5-mini` to `phi-4-mini`.
- Added support for endpoint override.
- Improved documentation with references to the SDK.

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Default model updated to `phi-4-mini`.
- Added support for endpoint override.
- Enhanced documentation with details about environment variables.

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- Updated default models.
- Added endpoint configuration.
- Improved error handling.

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Default model list updated to include `phi-4-mini`.
- Added detailed documentation for environment variables.
- Enhanced function documentation.
- Added support for endpoint override throughout.

#### Session 04: Model Comparison (`model_compare.py`)
- Default LLM updated from `gpt-oss-20b` to `qwen2.5-7b`.
- Added endpoint configuration.
- Improved documentation.

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Added type hints (changed `str | None` to `Optional[str]`).
- Enhanced documentation for the Agent class.
- Added support for endpoint override.
- Improved initialization patterns.

#### Session 06: Model Router (`models_router.py`)
- Added endpoint configuration.
- Enhanced documentation for intent detection.
- Improved documentation for routing logic.

#### Session 06: Pipeline (`models_pipeline.py`)
- Added detailed function documentation.
- Improved step-by-step documentation.
- Enhanced error handling.

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Added support for endpoint override.
- Updated default models.
- Enhanced function documentation.
- Improved error handling.

#### CLI Linter (`lint_markdown_cli.py`)
- Added links to SDK references.
- Improved usage documentation.

### Tests

#### Smoke Tests (`smoke.py`)
- Added support for endpoint override.
- Enhanced documentation.
- Improved test case documentation.
- Better error reporting.

## Environment Variables

All samples now support the following environment variables:

### Core Configuration
- `FOUNDRY_LOCAL_ALIAS` - Model alias to use (default varies by sample).
- `FOUNDRY_LOCAL_ENDPOINT` - Override service endpoint (optional).
- `SHOW_USAGE` - Display token usage statistics (default: "0").
- `RETRY_ON_FAIL` - Enable retry logic (default: "1").
- `RETRY_BACKOFF` - Initial retry delay in seconds (default: "1.0").

### Sample-Specific
- `EMBED_MODEL` - Embedding model for RAG samples.
- `BENCH_MODELS` - Comma-separated models for benchmarking.
- `BENCH_ROUNDS` - Number of benchmark rounds.
- `BENCH_PROMPT` - Test prompt for benchmarks.
- `BENCH_STREAM` - Measure first-token latency.
- `RAG_QUESTION` - Test question for RAG samples.
- `AGENT_MODEL_PRIMARY` - Primary agent model.
- `AGENT_MODEL_EDITOR` - Editor agent model.
- `SLM_ALIAS` - Small language model alias.
- `LLM_ALIAS` - Large language model alias.

## SDK Best Practices Implemented

### 1. Proper Client Initialization
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

### 4. Retry Logic with Exponential Backoff
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

If you are creating new samples or updating existing ones:

1. **Use `workshop_utils.py` helpers**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Support endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Add comprehensive documentation**:
   - Include environment variables in the docstring.
   - Provide SDK reference links.
   - Add usage examples.

4. **Use type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implement proper error handling**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testing

All samples can be tested using:

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
- **API Documentation**: Refer to the SDK repository for the latest API documentation.

## Breaking Changes

### None Expected
All changes are backward compatible. The updates primarily:
- Introduce new optional features (e.g., endpoint override).
- Improve error handling.
- Enhance documentation.
- Update default model names to current recommendations.

### Optional Enhancements
You may consider updating your code to use:
- `FOUNDRY_LOCAL_ENDPOINT` for explicit endpoint control.
- `SHOW_USAGE=1` for visibility into token usage.
- Updated default models (`phi-4-mini` instead of `phi-3.5-mini`).

## Common Issues & Solutions

### Issue: "Client initialization failed"
**Solution**: Ensure the Foundry Local service is running:
```bash
foundry service start
foundry model run phi-4-mini
```

### Issue: "Model not found"
**Solution**: Verify available models:
```bash
foundry model list
```

### Issue: Endpoint connection errors
**Solution**: Check the endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Next Steps

1. **Update Module08 samples**: Apply similar patterns to Module08/samples.
2. **Add integration tests**: Develop a comprehensive test suite.
3. **Performance benchmarking**: Compare performance before and after updates.
4. **Documentation updates**: Revise the main README with new patterns.

## Contribution Guidelines

When adding new samples:
1. Use `workshop_utils.py` for consistency.
2. Follow the patterns in existing samples.
3. Add detailed docstrings.
4. Include SDK reference links.
5. Support endpoint override.
6. Add proper type hints.
7. Provide usage examples in the docstring.

## Version Compatibility

These updates are compatible with:
- `foundry-local-sdk` (latest version).
- `openai>=1.30.0`.
- Python 3.8+.

---

**Last Updated**: 2025-01-08  
**Maintainer**: EdgeAI Workshop Team  
**SDK Version**: Foundry Local SDK (latest 0.7.117+67073234e7)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.