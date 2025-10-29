<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:56:18+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ta"
}
-->
# Foundry Local SDK மாற்றம் குறிப்பு

## மேலோட்டம்

Workshop கோப்பகத்தில் உள்ள அனைத்து Python கோப்புகளும் [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) இன் சமீபத்திய முறைமைகளை பின்பற்ற புதுப்பிக்கப்பட்டுள்ளது.

## மாற்றங்களின் சுருக்கம்

### மைய அடுக்கமைப்பு (`workshop_utils.py`)

#### மேம்பட்ட அம்சங்கள்:
- **எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவு**: `FOUNDRY_LOCAL_ENDPOINT` சூழல் மாறி ஆதரவு சேர்க்கப்பட்டது
- **மேம்பட்ட பிழை கையாளுதல்**: விரிவான பிழை செய்திகளுடன் சிறந்த εξαίρεση கையாளுதல்
- **மேம்பட்ட கேஷிங்**: பல எண்ட்பாயிண்ட் சூழல்களுக்கு கேஷ் கீகளை சேர்க்கும்
- **எக்ஸ்போனென்ஷியல் பாக்க்ஆஃப்**: சிறந்த நம்பகத்தன்மைக்காக எக்ஸ்போனென்ஷியல் பாக்க்ஆஃப் பயன்படுத்தும் மீண்டும் முயற்சி செய்யும் தர்க்கம்
- **வகை குறிப்புகள்**: IDE ஆதரவை மேம்படுத்த விரிவான வகை குறிப்புகள் சேர்க்கப்பட்டது

#### புதிய திறன்கள்:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### மாதிரி பயன்பாடுகள்

#### அமர்வு 01: சாட் பூட்ஸ்ட்ராப் (`chat_bootstrap.py`)
- இயல்புநிலை மாடல் `phi-3.5-mini`-இல் இருந்து `phi-4-mini`-க்கு புதுப்பிக்கப்பட்டது
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவு சேர்க்கப்பட்டது
- SDK குறிப்பு கொண்ட ஆவணங்களை மேம்படுத்தியது

#### அமர்வு 02: RAG பைப்லைன் (`rag_pipeline.py`)
- `phi-4-mini`-ஐ இயல்புநிலை மாடலாக புதுப்பித்தது
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவு சேர்க்கப்பட்டது
- சூழல் மாறி விவரங்களுடன் ஆவணங்களை மேம்படுத்தியது

#### அமர்வு 02: RAG மதிப்பீடு (`rag_eval_ragas.py`)
- மாடல் இயல்புநிலைகளை புதுப்பித்தது
- எண்ட்பாயிண்ட் கட்டமைப்பை சேர்த்தது
- பிழை கையாளுதலை மேம்படுத்தியது

#### அமர்வு 03: பெஞ்ச்மார்க்கிங் (`benchmark_oss_models.py`)
- `phi-4-mini` உட்பட இயல்புநிலை மாடல் பட்டியலை புதுப்பித்தது
- விரிவான சூழல் மாறி ஆவணங்களை சேர்த்தது
- செயல்பாட்டு ஆவணங்களை மேம்படுத்தியது
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை முழுவதும் சேர்த்தது

#### அமர்வு 04: மாடல் ஒப்பீடு (`model_compare.py`)
- இயல்புநிலை LLM-ஐ `gpt-oss-20b`-இல் இருந்து `qwen2.5-7b`-க்கு புதுப்பித்தது
- எண்ட்பாயிண்ட் கட்டமைப்பை சேர்த்தது
- ஆவணங்களை மேம்படுத்தியது

#### அமர்வு 05: மல்டி-ஏஜென்ட் ஒர்கெஸ்ட்ரேஷன் (`agents_orchestrator.py`)
- வகை குறிப்புகளை சேர்த்தது (`str | None`-ஐ `Optional[str]`-க்கு மாற்றியது)
- ஏஜென்ட் வகை ஆவணங்களை மேம்படுத்தியது
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை சேர்த்தது
- ஆரம்ப முறைமையை மேம்படுத்தியது

#### அமர்வு 06: மாடல் ரவுட்டர் (`models_router.py`)
- எண்ட்பாயிண்ட் கட்டமைப்பை சேர்த்தது
- நோக்கத்தை கண்டறிதல் ஆவணங்களை மேம்படுத்தியது
- ரவுட்டிங் தர்க்கம் ஆவணங்களை மேம்படுத்தியது

#### அமர்வு 06: பைப்லைன் (`models_pipeline.py`)
- விரிவான செயல்பாட்டு ஆவணங்களை சேர்த்தது
- படிப்படியாக ஆவணங்களை மேம்படுத்தியது
- பிழை கையாளுதலை மேம்படுத்தியது

### ஸ்கிரிப்ட்கள்

#### பெஞ்ச்மார்க் ஏக்ஸ்போர்ட் (`export_benchmark_markdown.py`)
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை சேர்த்தது
- இயல்புநிலை மாடல்களை புதுப்பித்தது
- செயல்பாட்டு ஆவணங்களை மேம்படுத்தியது
- பிழை கையாளுதலை மேம்படுத்தியது

#### CLI லின்டர் (`lint_markdown_cli.py`)
- SDK குறிப்பு இணைப்புகளை சேர்த்தது
- பயன்பாட்டு ஆவணங்களை மேம்படுத்தியது

### சோதனைகள்

#### ஸ்மோக் சோதனைகள் (`smoke.py`)
- எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை சேர்த்தது
- ஆவணங்களை மேம்படுத்தியது
- சோதனை வழக்கு ஆவணங்களை மேம்படுத்தியது
- சிறந்த பிழை அறிக்கையை வழங்கியது

## சூழல் மாறிகள்

அனைத்து மாதிரிகளும் இப்போது இந்த சூழல் மாறிகளை ஆதரிக்கின்றன:

### மைய கட்டமைப்பு
- `FOUNDRY_LOCAL_ALIAS` - பயன்படுத்த வேண்டிய மாடல் அலியாஸ் (மாதிரி அடிப்படையில் இயல்புநிலை மாறும்)
- `FOUNDRY_LOCAL_ENDPOINT` - சேவை எண்ட்பாயிண்டை மாற்றவும் (விருப்பத்தேர்வு)
- `SHOW_USAGE` - டோக்கன் பயன்பாட்டு புள்ளிவிவரங்களை காண்பிக்கவும் (இயல்புநிலை: "0")
- `RETRY_ON_FAIL` - மீண்டும் முயற்சி தர்க்கத்தை இயக்கவும் (இயல்புநிலை: "1")
- `RETRY_BACKOFF` - தொடக்க மீண்டும் முயற்சி தாமதம் விநாடிகளில் (இயல்புநிலை: "1.0")

### மாதிரி-சிறப்பு
- `EMBED_MODEL` - RAG மாதிரிகளுக்கான எம்பெடிங் மாடல்
- `BENCH_MODELS` - பெஞ்ச்மார்க்கிங் மாடல்களுக்கான கமா-பிரிக்கப்பட்ட பட்டியல்
- `BENCH_ROUNDS` - பெஞ்ச்மார்க்கிங் சுற்றுகளின் எண்ணிக்கை
- `BENCH_PROMPT` - பெஞ்ச்மார்க்குகளுக்கான சோதனை உந்துதல்
- `BENCH_STREAM` - முதல் டோக்கன் தாமதத்தை அளவிடவும்
- `RAG_QUESTION` - RAG மாதிரிகளுக்கான சோதனை கேள்வி
- `AGENT_MODEL_PRIMARY` - முதன்மை ஏஜென்ட் மாடல்
- `AGENT_MODEL_EDITOR` - எடிட்டர் ஏஜென்ட் மாடல்
- `SLM_ALIAS` - சிறிய மொழி மாடல் அலியாஸ்
- `LLM_ALIAS` - பெரிய மொழி மாடல் அலியாஸ்

## SDK சிறந்த நடைமுறைகள் செயல்படுத்தப்பட்டது

### 1. சரியான கிளையன்ட் ஆரம்பம்
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

### 2. மாடல் தகவல் மீட்பு
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. பிழை கையாளுதல்
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. எக்ஸ்போனென்ஷியல் பாக்க்ஆஃப் கொண்ட மீண்டும் முயற்சி தர்க்கம்
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

### 5. ஸ்ட்ரீமிங் ஆதரவு
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

## தனிப்பயன் மாதிரிகளுக்கான மாற்ற வழிகாட்டி

நீங்கள் புதிய மாதிரிகளை உருவாக்கினால் அல்லது ஏற்கனவே உள்ளவற்றை புதுப்பித்தால்:

1. **`workshop_utils.py` உதவிகளை பயன்படுத்தவும்**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை ஆதரிக்கவும்**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **விரிவான ஆவணங்களை சேர்க்கவும்**:
   - ஆவணத்தில் சூழல் மாறிகள்
   - SDK குறிப்பு இணைப்பு
   - பயன்பாட்டு உதாரணங்கள்

4. **வகை குறிப்புகளை பயன்படுத்தவும்**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **சரியான பிழை கையாளுதலை செயல்படுத்தவும்**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## சோதனை

அனைத்து மாதிரிகளும் சோதிக்கப்படலாம்:

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

## SDK ஆவண குறிப்பு

- **முக்கிய களஞ்சியம்**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ஆவணம்**: சமீபத்திய API ஆவணங்களை SDK களஞ்சியத்தில் சரிபார்க்கவும்

## முக்கிய மாற்றங்கள்

### எதிர்பார்க்கப்படவில்லை
அனைத்து மாற்றங்களும் பின்தங்கிய இணக்கத்துடன் உள்ளன. புதுப்பிப்புகள் முக்கியமாக:
- புதிய விருப்ப அம்சங்களைச் சேர்க்கிறது (எண்ட்பாயிண்ட் ஓவர்ரைடு)
- பிழை கையாளுதலை மேம்படுத்துகிறது
- ஆவணங்களை மேம்படுத்துகிறது
- இயல்புநிலை மாடல் பெயர்களை தற்போதைய பரிந்துரைகளுக்கு புதுப்பிக்கிறது

### விருப்ப மேம்பாடுகள்
உங்கள் குறியீட்டை புதுப்பிக்க விரும்பலாம்:
- `FOUNDRY_LOCAL_ENDPOINT`-ஐ தெளிவான எண்ட்பாயிண்ட் கட்டுப்பாட்டிற்காக
- டோக்கன் பயன்பாட்டு காட்சித்திறனுக்கு `SHOW_USAGE=1`
- புதுப்பிக்கப்பட்ட மாடல் இயல்புநிலைகள் (`phi-4-mini` `phi-3.5-mini`-க்கு பதிலாக)

## பொதுவான பிரச்சினைகள் & தீர்வுகள்

### பிரச்சினை: "கிளையன்ட் ஆரம்பம் தோல்வியடைந்தது"
**தீர்வு**: Foundry Local சேவை இயங்குகிறது என்பதை உறுதிப்படுத்தவும்:
```bash
foundry service start
foundry model run phi-4-mini
```

### பிரச்சினை: "மாடல் கிடைக்கவில்லை"
**தீர்வு**: கிடைக்கக்கூடிய மாடல்களைச் சரிபார்க்கவும்:
```bash
foundry model list
```

### பிரச்சினை: எண்ட்பாயிண்ட் இணைப்பு பிழைகள்
**தீர்வு**: எண்ட்பாயிண்டை சரிபார்க்கவும்:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## அடுத்த படிகள்

1. **Module08 மாதிரிகளை புதுப்பிக்கவும்**: Module08/samples-க்கு இதே முறைமைகளைப் பயன்படுத்தவும்
2. **ஒருங்கிணைப்பு சோதனைகளைச் சேர்க்கவும்**: விரிவான சோதனை தொகுப்பை உருவாக்கவும்
3. **செயல்திறன் பெஞ்ச்மார்க்கிங்**: முன்/பின் செயல்திறனை ஒப்பிடவும்
4. **ஆவண புதுப்பிப்புகள்**: புதிய முறைமைகளுடன் முக்கிய README-ஐ புதுப்பிக்கவும்

## பங்களிப்பு வழிகாட்டுதல்கள்

புதிய மாதிரிகளைச் சேர்க்கும்போது:
1. `workshop_utils.py`-ஐ ஒத்திசைவிற்காக பயன்படுத்தவும்
2. ஏற்கனவே உள்ள மாதிரிகளில் உள்ள முறைமையை பின்பற்றவும்
3. விரிவான டாக்ஸ்ட்ரிங்களைச் சேர்க்கவும்
4. SDK குறிப்பு இணைப்புகளைச் சேர்க்கவும்
5. எண்ட்பாயிண்ட் ஓவர்ரைடு ஆதரவை ஆதரிக்கவும்
6. சரியான வகை குறிப்புகளைச் சேர்க்கவும்
7. டாக்ஸ்ட்ரிங்-இல் பயன்பாட்டு உதாரணங்களைச் சேர்க்கவும்

## பதிப்பு இணக்கத்தன்மை

இந்த புதுப்பிப்புகள் இணக்கமானவை:
- `foundry-local-sdk` (சமீபத்தியது)
- `openai>=1.30.0`
- Python 3.8+

---

**கடைசியாக புதுப்பிக்கப்பட்டது**: 2025-01-08  
**பராமரிப்பாளர்**: EdgeAI Workshop குழு  
**SDK பதிப்பு**: Foundry Local SDK (சமீபத்திய 0.7.117+67073234e7)

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.