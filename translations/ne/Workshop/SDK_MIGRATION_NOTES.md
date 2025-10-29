<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:21:20+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ne"
}
-->
# फाउन्ड्री लोकल SDK माइग्रेशन नोट्स

## अवलोकन

वर्कशप फोल्डरका सबै Python फाइलहरूलाई आधिकारिक [फाउन्ड्री लोकल Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) का पछिल्ला ढाँचाहरू अनुसरण गर्न अद्यावधिक गरिएको छ।

## परिवर्तनहरूको सारांश

### कोर इन्फ्रास्ट्रक्चर (`workshop_utils.py`)

#### सुधारिएको सुविधाहरू:
- **एन्डप्वाइन्ट ओभरराइड समर्थन**: `FOUNDRY_LOCAL_ENDPOINT` वातावरण चरको समर्थन थपियो
- **सुधारिएको त्रुटि ह्यान्डलिङ**: विस्तृत त्रुटि सन्देशसहित राम्रो अपवाद ह्यान्डलिङ
- **सुधारिएको क्यासिङ**: बहु-एन्डप्वाइन्ट परिदृश्यहरूको लागि क्यास कुञ्जीहरूमा एन्डप्वाइन्ट समावेश गरियो
- **एक्स्पोनेंशियल ब्याकअफ**: विश्वसनीयता सुधार गर्न पुन: प्रयास तर्कले अब एक्स्पोनेंशियल ब्याकअफ प्रयोग गर्दछ
- **टाइप एनोटेसनहरू**: राम्रो IDE समर्थनको लागि व्यापक टाइप हिन्टहरू थपियो

#### नयाँ क्षमताहरू:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### नमूना एप्लिकेसनहरू

#### सत्र ०१: च्याट बुटस्ट्र्याप (`chat_bootstrap.py`)
- डिफल्ट मोडेललाई `phi-3.5-mini` बाट `phi-4-mini` मा अद्यावधिक गरियो
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो
- SDK सन्दर्भहरूसहित दस्तावेजीकरण सुधारियो

#### सत्र ०२: RAG पाइपलाइन (`rag_pipeline.py`)
- डिफल्ट मोडेललाई `phi-4-mini` मा अद्यावधिक गरियो
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो
- वातावरण चर विवरणसहित दस्तावेजीकरण सुधारियो

#### सत्र ०२: RAG मूल्याङ्कन (`rag_eval_ragas.py`)
- मोडेल डिफल्टहरू अद्यावधिक गरियो
- एन्डप्वाइन्ट कन्फिगरेसन थपियो
- त्रुटि ह्यान्डलिङ सुधारियो

#### सत्र ०३: बेंचमार्किङ (`benchmark_oss_models.py`)
- डिफल्ट मोडेल सूचीलाई `phi-4-mini` समावेश गर्न अद्यावधिक गरियो
- व्यापक वातावरण चर दस्तावेजीकरण थपियो
- फङ्सन दस्तावेजीकरण सुधारियो
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो

#### सत्र ०४: मोडेल तुलना (`model_compare.py`)
- डिफल्ट LLM लाई `gpt-oss-20b` बाट `qwen2.5-7b` मा अद्यावधिक गरियो
- एन्डप्वाइन्ट कन्फिगरेसन थपियो
- दस्तावेजीकरण सुधारियो

#### सत्र ०५: मल्टि-एजेन्ट अर्केस्ट्रेसन (`agents_orchestrator.py`)
- टाइप हिन्टहरू थपियो ( `str | None` लाई `Optional[str]` मा परिवर्तन गरियो)
- एजेन्ट क्लास दस्तावेजीकरण सुधारियो
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो
- आरम्भिक ढाँचामा सुधार गरियो

#### सत्र ०६: मोडेल राउटर (`models_router.py`)
- एन्डप्वाइन्ट कन्फिगरेसन थपियो
- उद्देश्य पत्ता लगाउने दस्तावेजीकरण सुधारियो
- राउटिङ तर्क दस्तावेजीकरण सुधारियो

#### सत्र ०६: पाइपलाइन (`models_pipeline.py`)
- व्यापक फङ्सन दस्तावेजीकरण थपियो
- चरण-दर-चरण दस्तावेजीकरण सुधारियो
- त्रुटि ह्यान्डलिङ सुधारियो

### स्क्रिप्टहरू

#### बेंचमार्क निर्यात (`export_benchmark_markdown.py`)
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो
- डिफल्ट मोडेलहरू अद्यावधिक गरियो
- फङ्सन दस्तावेजीकरण सुधारियो
- त्रुटि ह्यान्डलिङ सुधारियो

#### CLI लिन्टर (`lint_markdown_cli.py`)
- SDK सन्दर्भ लिंकहरू थपियो
- प्रयोग दस्तावेजीकरण सुधारियो

### परीक्षणहरू

#### स्मोक परीक्षण (`smoke.py`)
- एन्डप्वाइन्ट ओभरराइड समर्थन थपियो
- दस्तावेजीकरण सुधारियो
- परीक्षण केस दस्तावेजीकरण सुधारियो
- राम्रो त्रुटि रिपोर्टिङ

## वातावरण चरहरू

सबै नमूनाहरूले अब यी वातावरण चरहरूको समर्थन गर्दछ:

### कोर कन्फिगरेसन
- `FOUNDRY_LOCAL_ALIAS` - प्रयोग गर्न मोडेल उपनाम (डिफल्ट नमूनाद्वारा फरक हुन्छ)
- `FOUNDRY_LOCAL_ENDPOINT` - सेवा एन्डप्वाइन्ट ओभरराइड गर्नुहोस् (वैकल्पिक)
- `SHOW_USAGE` - टोकन प्रयोगको तथ्याङ्क देखाउनुहोस् (डिफल्ट: "0")
- `RETRY_ON_FAIL` - पुन: प्रयास तर्क सक्षम गर्नुहोस् (डिफल्ट: "1")
- `RETRY_BACKOFF` - सेकेन्डमा प्रारम्भिक पुन: प्रयास ढिलाइ (डिफल्ट: "1.0")

### नमूना-विशिष्ट
- `EMBED_MODEL` - RAG नमूनाहरूको लागि एम्बेडिङ मोडेल
- `BENCH_MODELS` - बेंचमार्किङको लागि कमामा छुट्याइएको मोडेलहरू
- `BENCH_ROUNDS` - बेंचमार्क राउन्डहरूको संख्या
- `BENCH_PROMPT` - बेंचमार्कहरूको लागि परीक्षण प्रम्प्ट
- `BENCH_STREAM` - पहिलो-टोकन विलम्बता मापन गर्नुहोस्
- `RAG_QUESTION` - RAG नमूनाहरूको लागि परीक्षण प्रश्न
- `AGENT_MODEL_PRIMARY` - प्राथमिक एजेन्ट मोडेल
- `AGENT_MODEL_EDITOR` - सम्पादक एजेन्ट मोडेल
- `SLM_ALIAS` - सानो भाषा मोडेल उपनाम
- `LLM_ALIAS` - ठूलो भाषा मोडेल उपनाम

## लागू गरिएका SDK उत्कृष्ट अभ्यासहरू

### १. उचित क्लाइन्ट आरम्भ
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

### २. मोडेल जानकारी पुन: प्राप्ति
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### ३. त्रुटि ह्यान्डलिङ
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### ४. एक्स्पोनेंशियल ब्याकअफसहित पुन: प्रयास तर्क
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

### ५. स्ट्रिमिङ समर्थन
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

## अनुकूलित नमूनाहरूको लागि माइग्रेशन गाइड

यदि तपाईं नयाँ नमूनाहरू सिर्जना गर्दै हुनुहुन्छ वा विद्यमानलाई अद्यावधिक गर्दै हुनुहुन्छ भने:

1. **`workshop_utils.py` सहायकहरू प्रयोग गर्नुहोस्**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **एन्डप्वाइन्ट ओभरराइड समर्थन गर्नुहोस्**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **व्यापक दस्तावेजीकरण थप्नुहोस्**:
   - दस्तावेजीकरणमा वातावरण चरहरू
   - SDK सन्दर्भ लिंक
   - प्रयोग उदाहरणहरू

4. **टाइप हिन्टहरू प्रयोग गर्नुहोस्**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **उचित त्रुटि ह्यान्डलिङ लागू गर्नुहोस्**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## परीक्षण

सबै नमूनाहरू निम्न तरिकाले परीक्षण गर्न सकिन्छ:

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

## SDK दस्तावेजीकरण सन्दर्भहरू

- **मुख्य रिपोजिटरी**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API दस्तावेजीकरण**: पछिल्लो API दस्तावेजहरूको लागि SDK रिपोजिटरी जाँच गर्नुहोस्

## ब्रेकिङ परिवर्तनहरू

### कुनै अपेक्षित छैन
सबै परिवर्तनहरू पछाडि अनुकूल छन्। अद्यावधिकहरूले मुख्यत:
- नयाँ वैकल्पिक सुविधाहरू थप्छ (एन्डप्वाइन्ट ओभरराइड)
- त्रुटि ह्यान्डलिङ सुधार गर्दछ
- दस्तावेजीकरण सुधार गर्दछ
- डिफल्ट मोडेल नामहरूलाई हालको सिफारिसहरूमा अद्यावधिक गर्दछ

### वैकल्पिक सुधारहरू
तपाईं आफ्नो कोडलाई निम्न प्रयोग गर्न अद्यावधिक गर्न चाहनुहुन्छ:
- स्पष्ट एन्डप्वाइन्ट नियन्त्रणको लागि `FOUNDRY_LOCAL_ENDPOINT`
- टोकन प्रयोग दृश्यताका लागि `SHOW_USAGE=1`
- अद्यावधिक मोडेल डिफल्टहरू (`phi-4-mini` `phi-3.5-mini` को सट्टा)

## सामान्य समस्याहरू र समाधानहरू

### समस्या: "क्लाइन्ट आरम्भ असफल भयो"
**समाधान**: सुनिश्चित गर्नुहोस् कि फाउन्ड्री लोकल सेवा चलिरहेको छ:
```bash
foundry service start
foundry model run phi-4-mini
```

### समस्या: "मोडेल फेला परेन"
**समाधान**: उपलब्ध मोडेलहरू जाँच गर्नुहोस्:
```bash
foundry model list
```

### समस्या: एन्डप्वाइन्ट कनेक्शन त्रुटिहरू
**समाधान**: एन्डप्वाइन्ट प्रमाणित गर्नुहोस्:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## आगामी कदमहरू

1. **मोड्युल०८ नमूनाहरू अद्यावधिक गर्नुहोस्**: मोड्युल०८/नमूनाहरूमा समान ढाँचाहरू लागू गर्नुहोस्
2. **एकीकृत परीक्षणहरू थप्नुहोस्**: व्यापक परीक्षण सूट सिर्जना गर्नुहोस्
3. **प्रदर्शन बेंचमार्किङ**: प्रदर्शनको तुलना गर्नुहोस् (पहिले/पछि)
4. **दस्तावेजीकरण अद्यावधिकहरू**: नयाँ ढाँचाहरूको साथ मुख्य README अद्यावधिक गर्नुहोस्

## योगदान दिशानिर्देशहरू

नयाँ नमूनाहरू थप्दा:
1. निरन्तरता सुनिश्चित गर्न `workshop_utils.py` प्रयोग गर्नुहोस्
2. विद्यमान नमूनाहरूको ढाँचालाई अनुसरण गर्नुहोस्
3. व्यापक डकस्ट्रिङहरू थप्नुहोस्
4. SDK सन्दर्भ लिंकहरू समावेश गर्नुहोस्
5. एन्डप्वाइन्ट ओभरराइड समर्थन गर्नुहोस्
6. उचित टाइप हिन्टहरू थप्नुहोस्
7. डकस्ट्रिङमा प्रयोग उदाहरणहरू समावेश गर्नुहोस्

## संस्करण अनुकूलता

यी अद्यावधिकहरू निम्नसँग अनुकूल छन्:
- `foundry-local-sdk` (पछिल्लो)
- `openai>=1.30.0`
- Python 3.8+

---

**अन्तिम अद्यावधिक**: २०२५-०१-०८  
**रखवाला**: EdgeAI वर्कशप टिम  
**SDK संस्करण**: फाउन्ड्री लोकल SDK (पछिल्लो 0.7.117+67073234e7)

---

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।