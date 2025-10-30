<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:28:34+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "pa"
}
-->
# ਫਾਊਂਡਰੀ ਲੋਕਲ SDK ਮਾਈਗ੍ਰੇਸ਼ਨ ਨੋਟਸ

## ਝਲਕ

ਵਰਕਸ਼ਾਪ ਫੋਲਡਰ ਵਿੱਚ ਸਾਰੇ ਪਾਇਥਨ ਫਾਈਲਾਂ ਨੂੰ ਅਧਿਕਾਰਤ [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) ਦੇ ਨਵੇਂ ਪੈਟਰਨਾਂ ਦੇ ਅਨੁਸਾਰ ਅਪਡੇਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਬਦਲਾਅ ਦਾ ਸਾਰ

### ਕੋਰ ਢਾਂਚਾ (`workshop_utils.py`)

#### ਵਧੇਰੇ ਫੀਚਰ:
- **ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ**: `FOUNDRY_LOCAL_ENDPOINT` ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- **ਬਿਹਤਰ ਗਲਤੀ ਸੰਭਾਲ**: ਵਿਸਤ੍ਰਿਤ ਗਲਤੀ ਸੁਨੇਹਿਆਂ ਨਾਲ ਬਿਹਤਰ ਐਕਸਪਸ਼ਨ ਹੈਂਡਲਿੰਗ
- **ਵਧੇਰੇ ਕੈਸ਼ਿੰਗ**: ਕੈਸ਼ ਕੀਜ਼ ਹੁਣ ਮਲਟੀ-ਐਂਡਪੌਇੰਟ ਸਥਿਤੀਆਂ ਲਈ ਐਂਡਪੌਇੰਟ ਸ਼ਾਮਲ ਕਰਦੇ ਹਨ
- **ਐਕਸਪੋਨੈਂਸ਼ਲ ਬੈਕੌਫ**: ਬਿਹਤਰ ਭਰੋਸੇਯੋਗਤਾ ਲਈ ਰਿਟ੍ਰਾਈ ਲੌਜਿਕ ਹੁਣ ਐਕਸਪੋਨੈਂਸ਼ਲ ਬੈਕੌਫ ਵਰਤਦਾ ਹੈ
- **ਟਾਈਪ ਐਨੋਟੇਸ਼ਨ**: ਬਿਹਤਰ IDE ਸਹਾਇਤਾ ਲਈ ਵਿਸਤ੍ਰਿਤ ਟਾਈਪ ਹਿੰਟਸ ਸ਼ਾਮਲ ਕੀਤੇ

#### ਨਵੇਂ ਸਮਰੱਥਾ:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ

#### ਸੈਸ਼ਨ 01: ਚੈਟ ਬੂਟਸਟ੍ਰੈਪ (`chat_bootstrap.py`)
- ਡਿਫਾਲਟ ਮਾਡਲ ਨੂੰ `phi-3.5-mini` ਤੋਂ `phi-4-mini` ਵਿੱਚ ਅਪਡੇਟ ਕੀਤਾ
- ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- SDK ਰਿਫਰੈਂਸ ਨਾਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ

#### ਸੈਸ਼ਨ 02: RAG ਪਾਈਪਲਾਈਨ (`rag_pipeline.py`)
- ਡਿਫਾਲਟ ਵਜੋਂ `phi-4-mini` ਵਰਤਣ ਲਈ ਅਪਡੇਟ ਕੀਤਾ
- ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਵੇਰਵੇ ਨਾਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ

#### ਸੈਸ਼ਨ 02: RAG ਮੁਲਾਂਕਣ (`rag_eval_ragas.py`)
- ਮਾਡਲ ਡਿਫਾਲਟਸ ਅਪਡੇਟ ਕੀਤੇ
- ਐਂਡਪੌਇੰਟ ਕਨਫਿਗਰੇਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਗਲਤੀ ਸੰਭਾਲ ਵਧਾਈ

#### ਸੈਸ਼ਨ 03: ਬੈਂਚਮਾਰਕਿੰਗ (`benchmark_oss_models.py`)
- ਡਿਫਾਲਟ ਮਾਡਲ ਸੂਚੀ ਨੂੰ `phi-4-mini` ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਅਪਡੇਟ ਕੀਤਾ
- ਵਿਸਤ੍ਰਿਤ ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਫੰਕਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ
- ਸਾਰੇ ਵਿੱਚ ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ

#### ਸੈਸ਼ਨ 04: ਮਾਡਲ ਤੁਲਨਾ (`model_compare.py`)
- ਡਿਫਾਲਟ LLM ਨੂੰ `gpt-oss-20b` ਤੋਂ `qwen2.5-7b` ਵਿੱਚ ਅਪਡੇਟ ਕੀਤਾ
- ਐਂਡਪੌਇੰਟ ਕਨਫਿਗਰੇਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ

#### ਸੈਸ਼ਨ 05: ਮਲਟੀ-ਏਜੰਟ ਆਰਕੇਸਟ੍ਰੇਸ਼ਨ (`agents_orchestrator.py`)
- ਟਾਈਪ ਹਿੰਟਸ ਸ਼ਾਮਲ ਕੀਤੇ (ਬਦਲਿਆ `str | None` ਨੂੰ `Optional[str]`)
- ਏਜੰਟ ਕਲਾਸ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ
- ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- ਸ਼ੁਰੂਆਤੀ ਪੈਟਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ

#### ਸੈਸ਼ਨ 06: ਮਾਡਲ ਰਾਊਟਰ (`models_router.py`)
- ਐਂਡਪੌਇੰਟ ਕਨਫਿਗਰੇਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਇਰਾਦਾ ਪਛਾਣ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ
- ਰਾਊਟਿੰਗ ਲੌਜਿਕ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ

#### ਸੈਸ਼ਨ 06: ਪਾਈਪਲਾਈਨ (`models_pipeline.py`)
- ਵਿਸਤ੍ਰਿਤ ਫੰਕਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਕਦਮ-ਦਰ-ਕਦਮ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ਗਲਤੀ ਸੰਭਾਲ ਵਧਾਈ

### ਸਕ੍ਰਿਪਟਸ

#### ਬੈਂਚਮਾਰਕ ਐਕਸਪੋਰਟ (`export_benchmark_markdown.py`)
- ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- ਡਿਫਾਲਟ ਮਾਡਲ ਅਪਡੇਟ ਕੀਤੇ
- ਫੰਕਸ਼ਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ
- ਗਲਤੀ ਸੰਭਾਲ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ

#### CLI ਲਿੰਟਰ (`lint_markdown_cli.py`)
- SDK ਰਿਫਰੈਂਸ ਲਿੰਕ ਸ਼ਾਮਲ ਕੀਤੇ
- ਵਰਤੋਂ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ

### ਟੈਸਟਸ

#### ਸਮੋਕ ਟੈਸਟਸ (`smoke.py`)
- ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕੀਤੀ
- ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਇਆ
- ਟੈਸਟ ਕੇਸ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ਬਿਹਤਰ ਗਲਤੀ ਰਿਪੋਰਟਿੰਗ

## ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ

ਸਾਰੇ ਨਮੂਨੇ ਹੁਣ ਇਹ ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਨ:

### ਕੋਰ ਕਨਫਿਗਰੇਸ਼ਨ
- `FOUNDRY_LOCAL_ALIAS` - ਵਰਤਣ ਲਈ ਮਾਡਲ ਅਲਿਆਸ (ਨਮੂਨੇ ਅਨੁਸਾਰ ਡਿਫਾਲਟ ਵੱਖ-ਵੱਖ)
- `FOUNDRY_LOCAL_ENDPOINT` - ਸੇਵਾ ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ (ਵਿਕਲਪਿਕ)
- `SHOW_USAGE` - ਟੋਕਨ ਵਰਤੋਂ ਅੰਕੜੇ ਦਿਖਾਓ (ਡਿਫਾਲਟ: "0")
- `RETRY_ON_FAIL` - ਰਿਟ੍ਰਾਈ ਲੌਜਿਕ ਚਾਲੂ ਕਰੋ (ਡਿਫਾਲਟ: "1")
- `RETRY_BACKOFF` - ਸਕਿੰਟ ਵਿੱਚ ਸ਼ੁਰੂਆਤੀ ਰਿਟ੍ਰਾਈ ਡਿਲੇ (ਡਿਫਾਲਟ: "1.0")

### ਨਮੂਨਾ-ਵਿਸ਼ੇਸ਼
- `EMBED_MODEL` - RAG ਨਮੂਨਿਆਂ ਲਈ ਐਮਬੈਡਿੰਗ ਮਾਡਲ
- `BENCH_MODELS` - ਬੈਂਚਮਾਰਕਿੰਗ ਲਈ ਕਾਮਾ-ਵੱਖਰੇ ਮਾਡਲ
- `BENCH_ROUNDS` - ਬੈਂਚਮਾਰਕ ਰਾਊਂਡ ਦੀ ਗਿਣਤੀ
- `BENCH_PROMPT` - ਬੈਂਚਮਾਰਕ ਲਈ ਟੈਸਟ ਪ੍ਰੋਮਪਟ
- `BENCH_STREAM` - ਪਹਿਲੇ-ਟੋਕਨ ਲੈਟੈਂਸੀ ਮਾਪੋ
- `RAG_QUESTION` - RAG ਨਮੂਨਿਆਂ ਲਈ ਟੈਸਟ ਸਵਾਲ
- `AGENT_MODEL_PRIMARY` - ਪ੍ਰਾਇਮਰੀ ਏਜੰਟ ਮਾਡਲ
- `AGENT_MODEL_EDITOR` - ਐਡੀਟਰ ਏਜੰਟ ਮਾਡਲ
- `SLM_ALIAS` - ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ ਅਲਿਆਸ
- `LLM_ALIAS` - ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ ਅਲਿਆਸ

## SDK ਬਿਹਤਰ ਅਭਿਆਸ ਲਾਗੂ ਕੀਤੇ

### 1. ਸਹੀ ਕਲਾਇੰਟ ਸ਼ੁਰੂਆਤ
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

### 2. ਮਾਡਲ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤੀ
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. ਗਲਤੀ ਸੰਭਾਲ
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. ਐਕਸਪੋਨੈਂਸ਼ਲ ਬੈਕੌਫ ਨਾਲ ਰਿਟ੍ਰਾਈ ਲੌਜਿਕ
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

### 5. ਸਟ੍ਰੀਮਿੰਗ ਸਹਾਇਤਾ
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

## ਕਸਟਮ ਨਮੂਨਿਆਂ ਲਈ ਮਾਈਗ੍ਰੇਸ਼ਨ ਗਾਈਡ

ਜੇ ਤੁਸੀਂ ਨਵੇਂ ਨਮੂਨੇ ਬਣਾਉਣ ਜਾਂ ਮੌਜੂਦਾ ਨੂੰ ਅਪਡੇਟ ਕਰ ਰਹੇ ਹੋ:

1. **`workshop_utils.py` ਹੈਲਪਰ ਵਰਤੋ**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਕਰੋ**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਸ਼ਾਮਲ ਕਰੋ**:
   - ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਡੌਕਸਟ੍ਰਿੰਗ ਵਿੱਚ
   - SDK ਰਿਫਰੈਂਸ ਲਿੰਕ
   - ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ

4. **ਟਾਈਪ ਹਿੰਟਸ ਵਰਤੋ**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **ਸਹੀ ਗਲਤੀ ਸੰਭਾਲ ਲਾਗੂ ਕਰੋ**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## ਟੈਸਟਿੰਗ

ਸਾਰੇ ਨਮੂਨੇ ਇਸ ਨਾਲ ਟੈਸਟ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

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

## SDK ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਰਿਫਰੈਂਸ

- **ਮੁੱਖ ਰਿਪੋਜ਼ਟਰੀ**: https://github.com/microsoft/Foundry-Local
- **ਪਾਇਥਨ SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ਦਸਤਾਵੇਜ਼ੀਕਰਨ**: SDK ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਤਾਜ਼ਾ API ਡੌਕਸ ਚੈੱਕ ਕਰੋ

## ਤੋੜਨ ਵਾਲੇ ਬਦਲਾਅ

### ਕੋਈ ਉਮੀਦ ਨਹੀਂ
ਸਾਰੇ ਬਦਲਾਅ ਪਿਛਲੇ ਵਰਜਨ ਨਾਲ ਅਨੁਕੂਲ ਹਨ। ਅਪਡੇਟ ਮੁੱਖ ਤੌਰ 'ਤੇ:
- ਨਵੇਂ ਵਿਕਲਪਿਕ ਫੀਚਰ ਸ਼ਾਮਲ ਕਰੋ (ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ)
- ਗਲਤੀ ਸੰਭਾਲ ਵਿੱਚ ਸੁਧਾਰ
- ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਧਾਓ
- ਮੌਜੂਦਾ ਸਿਫਾਰਸ਼ਾਂ ਲਈ ਡਿਫਾਲਟ ਮਾਡਲ ਨਾਮ ਅਪਡੇਟ ਕਰੋ

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ
ਤੁਹਾਨੂੰ ਆਪਣਾ ਕੋਡ ਅਪਡੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ:
- `FOUNDRY_LOCAL_ENDPOINT` ਸਪਸ਼ਟ ਐਂਡਪੌਇੰਟ ਕੰਟਰੋਲ ਲਈ
- `SHOW_USAGE=1` ਟੋਕਨ ਵਰਤੋਂ ਦ੍ਰਿਸ਼ਤਾ ਲਈ
- ਅਪਡੇਟ ਕੀਤੇ ਮਾਡਲ ਡਿਫਾਲਟਸ (`phi-4-mini` ਬਦਲੇ `phi-3.5-mini`)

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

### ਸਮੱਸਿਆ: "ਕਲਾਇੰਟ ਸ਼ੁਰੂਆਤ ਫੇਲ੍ਹ ਹੋਈ"
**ਹੱਲ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਸੇਵਾ ਚੱਲ ਰਹੀ ਹੈ:
```bash
foundry service start
foundry model run phi-4-mini
```

### ਸਮੱਸਿਆ: "ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ"
**ਹੱਲ**: ਉਪਲਬਧ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ ਕਰੋ:
```bash
foundry model list
```

### ਸਮੱਸਿਆ: ਐਂਡਪੌਇੰਟ ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ
**ਹੱਲ**: ਐਂਡਪੌਇੰਟ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## ਅਗਲੇ ਕਦਮ

1. **Module08 ਨਮੂਨੇ ਅਪਡੇਟ ਕਰੋ**: Module08/samples ਵਿੱਚ ਸਮਾਨ ਪੈਟਰਨ ਲਾਗੂ ਕਰੋ
2. **ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟਸ ਸ਼ਾਮਲ ਕਰੋ**: ਵਿਸਤ੍ਰਿਤ ਟੈਸਟ ਸੂਟ ਬਣਾਓ
3. **ਪ੍ਰਦਰਸ਼ਨ ਬੈਂਚਮਾਰਕਿੰਗ**: ਪਹਿਲਾਂ/ਬਾਅਦ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਤੁਲਨਾ ਕਰੋ
4. **ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਪਡੇਟਸ**: ਨਵੇਂ ਪੈਟਰਨਾਂ ਨਾਲ ਮੁੱਖ README ਅਪਡੇਟ ਕਰੋ

## ਯੋਗਦਾਨ ਦੇ ਨਿਯਮ

ਨਵੇਂ ਨਮੂਨੇ ਸ਼ਾਮਲ ਕਰਦੇ ਸਮੇਂ:
1. ਸਥਿਰਤਾ ਲਈ `workshop_utils.py` ਵਰਤੋ
2. ਮੌਜੂਦਾ ਨਮੂਨਿਆਂ ਵਿੱਚ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
3. ਵਿਸਤ੍ਰਿਤ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
4. SDK ਰਿਫਰੈਂਸ ਲਿੰਕ ਸ਼ਾਮਲ ਕਰੋ
5. ਐਂਡਪੌਇੰਟ ਓਵਰਰਾਈਡ ਸਹਾਇਤਾ ਕਰੋ
6. ਸਹੀ ਟਾਈਪ ਹਿੰਟਸ ਸ਼ਾਮਲ ਕਰੋ
7. ਡੌਕਸਟ੍ਰਿੰਗ ਵਿੱਚ ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਕਰੋ

## ਵਰਜਨ ਅਨੁਕੂਲਤਾ

ਇਹ ਅਪਡੇਟਸ ਅਨੁਕੂਲ ਹਨ:
- `foundry-local-sdk` (ਤਾਜ਼ਾ)
- `openai>=1.30.0`
- ਪਾਇਥਨ 3.8+

---

**ਆਖਰੀ ਅਪਡੇਟ**: 2025-01-08  
**ਮੈਂਟੇਨਰ**: EdgeAI ਵਰਕਸ਼ਾਪ ਟੀਮ  
**SDK ਵਰਜਨ**: Foundry Local SDK (ਤਾਜ਼ਾ 0.7.117+67073234e7)

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।