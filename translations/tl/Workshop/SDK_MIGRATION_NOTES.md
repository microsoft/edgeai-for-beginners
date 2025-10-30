<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:48:00+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "tl"
}
-->
# Foundry Local SDK Mga Tala sa Paglipat

## Pangkalahatang-ideya

Ang lahat ng Python files sa Workshop folder ay na-update upang sundin ang pinakabagong mga pattern mula sa opisyal na [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Buod ng mga Pagbabago

### Pangunahing Imprastraktura (`workshop_utils.py`)

#### Pinahusay na Mga Tampok:
- **Suporta sa Endpoint Override**: Idinagdag ang suporta para sa environment variable na `FOUNDRY_LOCAL_ENDPOINT`
- **Pinahusay na Paghawak ng Error**: Mas mahusay na paghawak ng exception na may detalyadong mga mensahe ng error
- **Pinahusay na Caching**: Ang mga cache key ay ngayon kasama ang endpoint para sa mga multi-endpoint na senaryo
- **Exponential Backoff**: Ang retry logic ay gumagamit na ng exponential backoff para sa mas maaasahang operasyon
- **Type Annotations**: Idinagdag ang komprehensibong type hints para sa mas mahusay na suporta sa IDE

#### Mga Bagong Kakayahan:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Mga Halimbawang Aplikasyon

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Na-update ang default na modelo mula sa `phi-3.5-mini` patungo sa `phi-4-mini`
- Idinagdag ang suporta sa endpoint override
- Pinahusay ang dokumentasyon na may mga reference sa SDK

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Na-update upang gamitin ang `phi-4-mini` bilang default
- Idinagdag ang suporta sa endpoint override
- Pinahusay ang dokumentasyon na may mga detalye ng environment variable

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- Na-update ang mga default na modelo
- Idinagdag ang configuration ng endpoint
- Pinahusay ang paghawak ng error

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Na-update ang default na listahan ng modelo upang isama ang `phi-4-mini`
- Idinagdag ang komprehensibong dokumentasyon ng environment variable
- Pinahusay ang dokumentasyon ng function
- Idinagdag ang suporta sa endpoint override sa kabuuan

#### Session 04: Model Comparison (`model_compare.py`)
- Na-update ang default na LLM mula sa `gpt-oss-20b` patungo sa `qwen2.5-7b`
- Idinagdag ang configuration ng endpoint
- Pinahusay ang dokumentasyon

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Idinagdag ang type hints (binago ang `str | None` patungo sa `Optional[str]`)
- Pinahusay ang dokumentasyon ng Agent class
- Idinagdag ang suporta sa endpoint override
- Pinahusay ang pattern ng initialization

#### Session 06: Model Router (`models_router.py`)
- Idinagdag ang configuration ng endpoint
- Pinahusay ang dokumentasyon ng intent detection
- Pinahusay ang dokumentasyon ng routing logic

#### Session 06: Pipeline (`models_pipeline.py`)
- Idinagdag ang komprehensibong dokumentasyon ng function
- Pinahusay ang step-by-step na dokumentasyon
- Pinahusay ang paghawak ng error

### Mga Script

#### Benchmark Export (`export_benchmark_markdown.py`)
- Idinagdag ang suporta sa endpoint override
- Na-update ang mga default na modelo
- Pinahusay ang dokumentasyon ng function
- Pinahusay ang paghawak ng error

#### CLI Linter (`lint_markdown_cli.py`)
- Idinagdag ang mga reference link sa SDK
- Pinahusay ang dokumentasyon ng paggamit

### Mga Pagsubok

#### Smoke Tests (`smoke.py`)
- Idinagdag ang suporta sa endpoint override
- Pinahusay ang dokumentasyon
- Pinahusay ang dokumentasyon ng test case
- Mas mahusay na pag-uulat ng error

## Mga Environment Variable

Ang lahat ng mga halimbawa ay ngayon sumusuporta sa mga environment variable na ito:

### Pangunahing Configuration
- `FOUNDRY_LOCAL_ALIAS` - Model alias na gagamitin (default ay nag-iiba depende sa halimbawa)
- `FOUNDRY_LOCAL_ENDPOINT` - Override ng service endpoint (opsyonal)
- `SHOW_USAGE` - Ipakita ang mga istatistika ng paggamit ng token (default: "0")
- `RETRY_ON_FAIL` - Paganahin ang retry logic (default: "1")
- `RETRY_BACKOFF` - Paunang delay ng retry sa segundo (default: "1.0")

### Para sa Partikular na Halimbawa
- `EMBED_MODEL` - Embedding model para sa mga halimbawa ng RAG
- `BENCH_MODELS` - Mga modelong pinaghihiwalay ng comma para sa benchmarking
- `BENCH_ROUNDS` - Bilang ng mga benchmark rounds
- `BENCH_PROMPT` - Test prompt para sa benchmarks
- `BENCH_STREAM` - Sukatin ang latency ng unang token
- `RAG_QUESTION` - Test question para sa mga halimbawa ng RAG
- `AGENT_MODEL_PRIMARY` - Pangunahing modelo ng agent
- `AGENT_MODEL_EDITOR` - Editor na modelo ng agent
- `SLM_ALIAS` - Maliit na language model alias
- `LLM_ALIAS` - Malaking language model alias

## Mga Pinakamahusay na Praktis sa SDK na Naipatupad

### 1. Tamang Initialization ng Client
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

### 2. Pagkuha ng Impormasyon ng Modelo
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Paghawak ng Error
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry Logic na may Exponential Backoff
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

### 5. Suporta sa Streaming
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

## Gabay sa Paglipat para sa Mga Custom na Halimbawa

Kung gumagawa ka ng mga bagong halimbawa o nag-a-update ng mga umiiral na:

1. **Gamitin ang mga helper ng `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Suportahan ang endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Magdagdag ng komprehensibong dokumentasyon**:
   - Mga environment variable sa docstring
   - Reference link sa SDK
   - Mga halimbawa ng paggamit

4. **Gumamit ng type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Ipapatupad ang tamang paghawak ng error**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Pagsubok

Ang lahat ng mga halimbawa ay maaaring subukan gamit ang:

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

## Mga Reference sa Dokumentasyon ng SDK

- **Pangunahing Repositoryo**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentasyon**: Tingnan ang repositoryo ng SDK para sa pinakabagong API docs

## Mga Pagbabagong Nakakasira

### Walang Inaasahan
Ang lahat ng mga pagbabago ay backward compatible. Ang mga update ay pangunahing:
- Nagdaragdag ng mga bagong opsyonal na tampok (endpoint override)
- Pinahusay ang paghawak ng error
- Pinahusay ang dokumentasyon
- Na-update ang mga default na pangalan ng modelo sa kasalukuyang mga rekomendasyon

### Opsyonal na Mga Pagpapahusay
Maaaring gusto mong i-update ang iyong code upang gamitin:
- `FOUNDRY_LOCAL_ENDPOINT` para sa malinaw na kontrol sa endpoint
- `SHOW_USAGE=1` para sa visibility ng paggamit ng token
- Na-update na mga default na modelo (`phi-4-mini` sa halip na `phi-3.5-mini`)

## Mga Karaniwang Isyu at Solusyon

### Isyu: "Nabigo ang initialization ng client"
**Solusyon**: Siguraduhing tumatakbo ang Foundry Local service:
```bash
foundry service start
foundry model run phi-4-mini
```

### Isyu: "Hindi natagpuan ang modelo"
**Solusyon**: Suriin ang mga available na modelo:
```bash
foundry model list
```

### Isyu: Mga error sa koneksyon ng endpoint
**Solusyon**: I-verify ang endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Mga Susunod na Hakbang

1. **I-update ang Module08 samples**: Ipatupad ang mga katulad na pattern sa Module08/samples
2. **Magdagdag ng mga integration tests**: Gumawa ng komprehensibong test suite
3. **Benchmarking ng performance**: Ihambing ang performance bago/ pagkatapos
4. **Mga update sa dokumentasyon**: I-update ang pangunahing README gamit ang mga bagong pattern

## Mga Alituntunin sa Kontribusyon

Kapag nagdaragdag ng mga bagong halimbawa:
1. Gamitin ang `workshop_utils.py` para sa pagkakapare-pareho
2. Sundin ang pattern sa mga umiiral na halimbawa
3. Magdagdag ng komprehensibong docstrings
4. Isama ang mga reference link sa SDK
5. Suportahan ang endpoint override
6. Magdagdag ng tamang type hints
7. Isama ang mga halimbawa ng paggamit sa docstring

## Compatibility ng Bersyon

Ang mga update na ito ay compatible sa:
- `foundry-local-sdk` (pinakabago)
- `openai>=1.30.0`
- Python 3.8+

---

**Huling Na-update**: 2025-01-08  
**Tagapangalaga**: EdgeAI Workshop Team  
**Bersyon ng SDK**: Foundry Local SDK (pinakabago 0.7.117+67073234e7)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.