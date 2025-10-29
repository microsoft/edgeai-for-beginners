<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:15:55+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "mr"
}
-->
# फाउंड्री लोकल SDK स्थलांतर नोट्स

## आढावा

वर्कशॉप फोल्डरमधील सर्व Python फाइल्स अधिकृत [फाउंड्री लोकल Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) च्या नवीनतम पद्धतींचे अनुसरण करण्यासाठी अद्यतनित केल्या आहेत.

## बदलांचा सारांश

### मुख्य पायाभूत सुविधा (`workshop_utils.py`)

#### सुधारित वैशिष्ट्ये:
- **एंडपॉइंट ओव्हरराइड समर्थन**: `FOUNDRY_LOCAL_ENDPOINT` पर्यावरणीय व्हेरिएबलसाठी समर्थन जोडले
- **सुधारित त्रुटी हाताळणी**: तपशीलवार त्रुटी संदेशांसह चांगली अपवाद हाताळणी
- **सुधारित कॅशिंग**: मल्टी-एंडपॉइंट परिस्थितीसाठी कॅश की आता एंडपॉइंट समाविष्ट करते
- **एक्स्पोनेंशियल बॅकऑफ**: चांगल्या विश्वासार्हतेसाठी पुनर्प्रयत्न लॉजिक आता एक्स्पोनेंशियल बॅकऑफ वापरते
- **टाइप अ‍ॅनोटेशन्स**: चांगल्या IDE समर्थनासाठी व्यापक प्रकाराच्या सूचनांचा समावेश

#### नवीन क्षमता:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### नमुना अनुप्रयोग

#### सत्र 01: चॅट बूटस्ट्रॅप (`chat_bootstrap.py`)
- डीफॉल्ट मॉडेल `phi-3.5-mini` वरून `phi-4-mini` मध्ये अद्यतनित केले
- एंडपॉइंट ओव्हरराइड समर्थन जोडले
- SDK संदर्भांसह प्रलेखन सुधारित केले

#### सत्र 02: RAG पाइपलाइन (`rag_pipeline.py`)
- डीफॉल्ट मॉडेल म्हणून `phi-4-mini` वापरण्यास अद्यतनित केले
- एंडपॉइंट ओव्हरराइड समर्थन जोडले
- पर्यावरणीय व्हेरिएबल तपशीलांसह प्रलेखन सुधारित केले

#### सत्र 02: RAG मूल्यांकन (`rag_eval_ragas.py`)
- मॉडेल डीफॉल्ट्स अद्यतनित केले
- एंडपॉइंट कॉन्फिगरेशन जोडले
- त्रुटी हाताळणी सुधारित केली

#### सत्र 03: बेंचमार्किंग (`benchmark_oss_models.py`)
- डीफॉल्ट मॉडेल यादीत `phi-4-mini` समाविष्ट केली
- व्यापक पर्यावरणीय व्हेरिएबल प्रलेखन जोडले
- फंक्शन प्रलेखन सुधारित केले
- संपूर्ण एंडपॉइंट ओव्हरराइड समर्थन जोडले

#### सत्र 04: मॉडेल तुलना (`model_compare.py`)
- डीफॉल्ट LLM `gpt-oss-20b` वरून `qwen2.5-7b` मध्ये अद्यतनित केले
- एंडपॉइंट कॉन्फिगरेशन जोडले
- प्रलेखन सुधारित केले

#### सत्र 05: मल्टी-एजंट ऑर्केस्ट्रेशन (`agents_orchestrator.py`)
- प्रकाराच्या सूचनांचा समावेश ( `str | None` वरून `Optional[str]` मध्ये बदल)
- एजंट वर्ग प्रलेखन सुधारित केले
- एंडपॉइंट ओव्हरराइड समर्थन जोडले
- प्रारंभिक पॅटर्न सुधारित केला

#### सत्र 06: मॉडेल राउटर (`models_router.py`)
- एंडपॉइंट कॉन्फिगरेशन जोडले
- हेतू शोध प्रलेखन सुधारित केले
- राउटिंग लॉजिक प्रलेखन सुधारित केले

#### सत्र 06: पाइपलाइन (`models_pipeline.py`)
- व्यापक फंक्शन प्रलेखन जोडले
- चरण-दर-चरण प्रलेखन सुधारित केले
- त्रुटी हाताळणी सुधारित केली

### स्क्रिप्ट्स

#### बेंचमार्क निर्यात (`export_benchmark_markdown.py`)
- एंडपॉइंट ओव्हरराइड समर्थन जोडले
- डीफॉल्ट मॉडेल अद्यतनित केले
- फंक्शन प्रलेखन सुधारित केले
- त्रुटी हाताळणी सुधारित केली

#### CLI लिंटर (`lint_markdown_cli.py`)
- SDK संदर्भ दुवे जोडले
- वापर प्रलेखन सुधारित केले

### चाचण्या

#### स्मोक चाचण्या (`smoke.py`)
- एंडपॉइंट ओव्हरराइड समर्थन जोडले
- प्रलेखन सुधारित केले
- चाचणी प्रकरण प्रलेखन सुधारित केले
- चांगले त्रुटी अहवाल

## पर्यावरणीय व्हेरिएबल्स

सर्व नमुने आता खालील पर्यावरणीय व्हेरिएबल्सला समर्थन देतात:

### मुख्य कॉन्फिगरेशन
- `FOUNDRY_LOCAL_ALIAS` - वापरण्यासाठी मॉडेल उपनाम (डीफॉल्ट नमुन्यानुसार बदलते)
- `FOUNDRY_LOCAL_ENDPOINT` - सेवा एंडपॉइंट ओव्हरराइड करा (पर्यायी)
- `SHOW_USAGE` - टोकन वापर आकडेवारी दर्शवा (डीफॉल्ट: "0")
- `RETRY_ON_FAIL` - पुनर्प्रयत्न लॉजिक सक्षम करा (डीफॉल्ट: "1")
- `RETRY_BACKOFF` - सेकंदांमध्ये प्रारंभिक पुनर्प्रयत्न विलंब (डीफॉल्ट: "1.0")

### नमुना-विशिष्ट
- `EMBED_MODEL` - RAG नमुन्यांसाठी एम्बेडिंग मॉडेल
- `BENCH_MODELS` - बेंचमार्किंगसाठी अल्पविरामाने विभाजित मॉडेल्स
- `BENCH_ROUNDS` - बेंचमार्क फेऱ्यांची संख्या
- `BENCH_PROMPT` - बेंचमार्कसाठी चाचणी प्रॉम्प्ट
- `BENCH_STREAM` - पहिल्या टोकन विलंबाचा मोजमाप
- `RAG_QUESTION` - RAG नमुन्यांसाठी चाचणी प्रश्न
- `AGENT_MODEL_PRIMARY` - प्राथमिक एजंट मॉडेल
- `AGENT_MODEL_EDITOR` - संपादक एजंट मॉडेल
- `SLM_ALIAS` - लहान भाषा मॉडेल उपनाम
- `LLM_ALIAS` - मोठ्या भाषा मॉडेल उपनाम

## SDK सर्वोत्तम पद्धती लागू केल्या

### 1. योग्य क्लायंट प्रारंभ
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

### 2. मॉडेल माहिती पुनर्प्राप्ती
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. त्रुटी हाताळणी
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. एक्स्पोनेंशियल बॅकऑफसह पुनर्प्रयत्न लॉजिक
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

### 5. स्ट्रीमिंग समर्थन
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

## कस्टम नमुन्यांसाठी स्थलांतर मार्गदर्शक

जर तुम्ही नवीन नमुने तयार करत असाल किंवा विद्यमान अद्यतनित करत असाल:

1. **`workshop_utils.py` सहाय्यक वापरा**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **एंडपॉइंट ओव्हरराइड समर्थन द्या**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **विस्तृत प्रलेखन जोडा**:
   - पर्यावरणीय व्हेरिएबल्स डॉक्स्ट्रिंगमध्ये
   - SDK संदर्भ दुवा
   - वापर उदाहरणे

4. **प्रकाराच्या सूचनांचा वापर करा**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **योग्य त्रुटी हाताळणी लागू करा**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## चाचणी

सर्व नमुने खालीलप्रमाणे चाचणी केली जाऊ शकतात:

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

## SDK प्रलेखन संदर्भ

- **मुख्य रिपॉझिटरी**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API प्रलेखन**: नवीनतम API डॉक्ससाठी SDK रिपॉझिटरी तपासा

## ब्रेकिंग बदल

### अपेक्षित नाही
सर्व बदल मागील आवृत्त्यांशी सुसंगत आहेत. अद्यतन मुख्यतः:
- नवीन पर्यायी वैशिष्ट्ये जोडणे (एंडपॉइंट ओव्हरराइड)
- त्रुटी हाताळणी सुधारित करणे
- प्रलेखन सुधारित करणे
- डीफॉल्ट मॉडेल नावे सध्याच्या शिफारसींनुसार अद्यतनित करणे

### पर्यायी सुधारणा
तुम्हाला तुमचा कोड अद्यतनित करायचा असेल तर:
- स्पष्ट एंडपॉइंट नियंत्रणासाठी `FOUNDRY_LOCAL_ENDPOINT` वापरा
- टोकन वापर दृश्यमानतेसाठी `SHOW_USAGE=1` वापरा
- अद्यतनित मॉडेल डीफॉल्ट्स (`phi-4-mini` ऐवजी `phi-3.5-mini`)

## सामान्य समस्या आणि उपाय

### समस्या: "क्लायंट प्रारंभ अयशस्वी"
**उपाय**: फाउंड्री लोकल सेवा चालू असल्याची खात्री करा:
```bash
foundry service start
foundry model run phi-4-mini
```

### समस्या: "मॉडेल सापडले नाही"
**उपाय**: उपलब्ध मॉडेल्स तपासा:
```bash
foundry model list
```

### समस्या: एंडपॉइंट कनेक्शन त्रुटी
**उपाय**: एंडपॉइंट सत्यापित करा:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## पुढील पायऱ्या

1. **Module08 नमुने अद्यतनित करा**: Module08/samples मध्ये समान पद्धती लागू करा
2. **समाकलन चाचण्या जोडा**: व्यापक चाचणी संच तयार करा
3. **कामगिरी बेंचमार्किंग**: अद्यतनापूर्वी/नंतर कामगिरीची तुलना करा
4. **प्रलेखन अद्यतन**: नवीन पद्धतींसह मुख्य README अद्यतनित करा

## योगदान मार्गदर्शक तत्त्वे

नवीन नमुने जोडताना:
1. सुसंगततेसाठी `workshop_utils.py` वापरा
2. विद्यमान नमुन्यांमधील पद्धती अनुसरण करा
3. विस्तृत डॉक्स्ट्रिंग्स जोडा
4. SDK संदर्भ दुवे समाविष्ट करा
5. एंडपॉइंट ओव्हरराइड समर्थन द्या
6. योग्य प्रकाराच्या सूचनांचा समावेश करा
7. डॉक्स्ट्रिंगमध्ये वापर उदाहरणे समाविष्ट करा

## आवृत्ती सुसंगतता

ही अद्यतने सुसंगत आहेत:
- `foundry-local-sdk` (नवीनतम)
- `openai>=1.30.0`
- Python 3.8+

---

**शेवटचे अद्यतन**: 2025-01-08  
**देखभाल करणारे**: EdgeAI वर्कशॉप टीम  
**SDK आवृत्ती**: फाउंड्री लोकल SDK (नवीनतम 0.7.117+67073234e7)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात घ्या की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.