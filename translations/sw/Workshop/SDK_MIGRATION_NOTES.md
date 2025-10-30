<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:53:20+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sw"
}
-->
# Vidokezo vya Kuhama kwa Foundry Local SDK

## Muhtasari

Faili zote za Python katika folda ya Workshop zimesasishwa kufuata mifumo ya hivi karibuni kutoka kwa [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Muhtasari wa Mabadiliko

### Miundombinu ya Msingi (`workshop_utils.py`)

#### Vipengele Vilivyoboreshwa:
- **Msaada wa Kubadilisha Endpoint**: Imeongezwa msaada wa mazingira ya `FOUNDRY_LOCAL_ENDPOINT`
- **Ushughulikiaji Bora wa Makosa**: Ushughulikiaji bora wa makosa na ujumbe wa kina wa makosa
- **Uboreshaji wa Uwekaji Kache**: Funguo za kache sasa zinajumuisha endpoint kwa hali za multi-endpoint
- **Exponential Backoff**: Mantiki ya kurudia sasa inatumia exponential backoff kwa uaminifu bora
- **Maelezo ya Aina**: Imeongezwa maelezo ya aina kwa kina kwa msaada bora wa IDE

#### Uwezo Mpya:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Programu za Mfano

#### Kipindi 01: Chat Bootstrap (`chat_bootstrap.py`)
- Model ya msingi imesasishwa kutoka `phi-3.5-mini` hadi `phi-4-mini`
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa na marejeleo ya SDK

#### Kipindi 02: RAG Pipeline (`rag_pipeline.py`)
- Imesasishwa kutumia `phi-4-mini` kama default
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa na maelezo ya mazingira ya mazingira

#### Kipindi 02: RAG Evaluation (`rag_eval_ragas.py`)
- Default za model zimesasishwa
- Imeongezwa usanidi wa endpoint
- Ushughulikiaji wa makosa umeboreshwa

#### Kipindi 03: Benchmarking (`benchmark_oss_models.py`)
- Orodha ya model za msingi imesasishwa kujumuisha `phi-4-mini`
- Nyaraka za mazingira zimeboreshwa kwa kina
- Nyaraka za kazi zimeboreshwa
- Imeongezwa msaada wa kubadilisha endpoint kote

#### Kipindi 04: Ulinganisho wa Model (`model_compare.py`)
- LLM ya msingi imesasishwa kutoka `gpt-oss-20b` hadi `qwen2.5-7b`
- Imeongezwa usanidi wa endpoint
- Nyaraka zimeboreshwa

#### Kipindi 05: Uratibu wa Multi-Agent (`agents_orchestrator.py`)
- Imeongezwa maelezo ya aina (imebadilishwa `str | None` hadi `Optional[str]`)
- Nyaraka za darasa la Agent zimeboreshwa
- Imeongezwa msaada wa kubadilisha endpoint
- Muundo wa uanzishaji umeboreshwa

#### Kipindi 06: Model Router (`models_router.py`)
- Imeongezwa usanidi wa endpoint
- Nyaraka za utambuzi wa nia zimeboreshwa
- Nyaraka za mantiki ya uratibu zimeboreshwa

#### Kipindi 06: Pipeline (`models_pipeline.py`)
- Nyaraka za kazi zimeboreshwa kwa kina
- Nyaraka za hatua kwa hatua zimeboreshwa
- Ushughulikiaji wa makosa umeboreshwa

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Imeongezwa msaada wa kubadilisha endpoint
- Model za msingi zimesasishwa
- Nyaraka za kazi zimeboreshwa
- Ushughulikiaji wa makosa umeboreshwa

#### CLI Linter (`lint_markdown_cli.py`)
- Imeongezwa viungo vya marejeleo ya SDK
- Nyaraka za matumizi zimeboreshwa

### Majaribio

#### Smoke Tests (`smoke.py`)
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa
- Nyaraka za kesi za majaribio zimeboreshwa
- Utoaji bora wa ripoti za makosa

## Mazingira ya Mazingira

Sampuli zote sasa zinaunga mkono mazingira haya:

### Usanidi wa Msingi
- `FOUNDRY_LOCAL_ALIAS` - Alias ya model ya kutumia (default inatofautiana kwa sampuli)
- `FOUNDRY_LOCAL_ENDPOINT` - Kubadilisha endpoint ya huduma (hiari)
- `SHOW_USAGE` - Onyesha takwimu za matumizi ya tokeni (default: "0")
- `RETRY_ON_FAIL` - Washa mantiki ya kurudia (default: "1")
- `RETRY_BACKOFF` - Muda wa kuchelewa wa kurudia kwa sekunde (default: "1.0")

### Sampuli Maalum
- `EMBED_MODEL` - Model ya embedding kwa sampuli za RAG
- `BENCH_MODELS` - Model zilizotenganishwa kwa koma kwa benchmarking
- `BENCH_ROUNDS` - Idadi ya raundi za benchmarking
- `BENCH_PROMPT` - Maandishi ya majaribio kwa benchmarking
- `BENCH_STREAM` - Pima latency ya tokeni ya kwanza
- `RAG_QUESTION` - Swali la majaribio kwa sampuli za RAG
- `AGENT_MODEL_PRIMARY` - Model ya wakala wa msingi
- `AGENT_MODEL_EDITOR` - Model ya wakala wa mhariri
- `SLM_ALIAS` - Alias ya model ndogo ya lugha
- `LLM_ALIAS` - Alias ya model kubwa ya lugha

## Mazoea Bora ya SDK Yaliyotekelezwa

### 1. Uanzishaji Sahihi wa Mteja
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

### 2. Upataji wa Taarifa za Model
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Ushughulikiaji wa Makosa
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Mantiki ya Kurudia na Exponential Backoff
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

### 5. Msaada wa Streaming
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

## Mwongozo wa Kuhama kwa Sampuli Maalum

Ikiwa unaunda sampuli mpya au unasasisha zilizopo:

1. **Tumia wasaidizi wa `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Saidia kubadilisha endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Ongeza nyaraka za kina**:
   - Mazingira ya mazingira katika docstring
   - Kiungo cha marejeleo ya SDK
   - Mifano ya matumizi

4. **Tumia maelezo ya aina**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Tekeleza ushughulikiaji sahihi wa makosa**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Upimaji

Sampuli zote zinaweza kupimwa kwa:

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

## Marejeleo ya Nyaraka za SDK

- **Hifadhi Kuu**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Nyaraka za API**: Angalia hifadhi ya SDK kwa nyaraka za API za hivi karibuni

## Mabadiliko Makubwa

### Hakuna Yanayotarajiwa
Mabadiliko yote yanalingana na yaliyopita. Sasisho hizi kimsingi:
- Ongeza vipengele vipya vya hiari (kubadilisha endpoint)
- Boresha ushughulikiaji wa makosa
- Boresha nyaraka
- Sasisha majina ya model za msingi kwa mapendekezo ya sasa

### Uboreshaji wa Hiari
Unaweza kutaka kusasisha msimbo wako kutumia:
- `FOUNDRY_LOCAL_ENDPOINT` kwa udhibiti wa endpoint wazi
- `SHOW_USAGE=1` kwa mwonekano wa matumizi ya tokeni
- Default za model zilizosasishwa (`phi-4-mini` badala ya `phi-3.5-mini`)

## Masuala ya Kawaida na Suluhisho

### Tatizo: "Uanzishaji wa mteja umeshindwa"
**Suluhisho**: Hakikisha huduma ya Foundry Local inafanya kazi:
```bash
foundry service start
foundry model run phi-4-mini
```

### Tatizo: "Model haikupatikana"
**Suluhisho**: Angalia model zinazopatikana:
```bash
foundry model list
```

### Tatizo: Makosa ya muunganisho wa endpoint
**Suluhisho**: Hakikisha endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Hatua Zifuatazo

1. **Sasisha sampuli za Module08**: Tumia mifumo sawa kwa Module08/samples
2. **Ongeza majaribio ya ujumuishaji**: Unda seti ya majaribio ya kina
3. **Upimaji wa utendaji**: Linganisha utendaji kabla/baada ya mabadiliko
4. **Sasisho za nyaraka**: Sasisha README kuu na mifumo mipya

## Miongozo ya Mchango

Unapoongeza sampuli mpya:
1. Tumia `workshop_utils.py` kwa uthabiti
2. Fuata muundo katika sampuli zilizopo
3. Ongeza docstrings za kina
4. Jumuisha viungo vya marejeleo ya SDK
5. Saidia kubadilisha endpoint
6. Ongeza maelezo sahihi ya aina
7. Jumuisha mifano ya matumizi katika docstring

## Utangamano wa Toleo

Sasisho hizi zinaendana na:
- `foundry-local-sdk` (ya hivi karibuni)
- `openai>=1.30.0`
- Python 3.8+

---

**Imesasishwa Mwisho**: 2025-01-08  
**Msimamizi**: Timu ya EdgeAI Workshop  
**Toleo la SDK**: Foundry Local SDK (ya hivi karibuni 0.7.117+67073234e7)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.