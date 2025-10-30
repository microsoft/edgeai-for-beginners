<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:04:58+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "hi"
}
-->
# फाउंड्री लोकल SDK माइग्रेशन नोट्स

## अवलोकन

वर्कशॉप फ़ोल्डर में सभी Python फाइलें आधिकारिक [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) के नवीनतम पैटर्न का पालन करने के लिए अपडेट की गई हैं।

## बदलावों का सारांश

### कोर इंफ्रास्ट्रक्चर (`workshop_utils.py`)

#### उन्नत सुविधाएँ:
- **एंडपॉइंट ओवरराइड सपोर्ट**: `FOUNDRY_LOCAL_ENDPOINT` एनवायरनमेंट वेरिएबल सपोर्ट जोड़ा गया
- **बेहतर एरर हैंडलिंग**: विस्तृत एरर संदेशों के साथ बेहतर अपवाद हैंडलिंग
- **उन्नत कैशिंग**: मल्टी-एंडपॉइंट परिदृश्यों के लिए कैश कुंजियों में अब एंडपॉइंट शामिल है
- **एक्सपोनेंशियल बैकऑफ**: बेहतर विश्वसनीयता के लिए रिट्री लॉजिक में एक्सपोनेंशियल बैकऑफ का उपयोग
- **टाइप एनोटेशन**: बेहतर IDE सपोर्ट के लिए व्यापक टाइप हिंट्स जोड़े गए

#### नई क्षमताएँ:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### सैंपल एप्लिकेशन

#### सत्र 01: चैट बूटस्ट्रैप (`chat_bootstrap.py`)
- डिफ़ॉल्ट मॉडल को `phi-3.5-mini` से `phi-4-mini` में अपडेट किया गया
- एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया
- SDK संदर्भों के साथ दस्तावेज़ीकरण को बेहतर बनाया गया

#### सत्र 02: RAG पाइपलाइन (`rag_pipeline.py`)
- डिफ़ॉल्ट के रूप में `phi-4-mini` का उपयोग करने के लिए अपडेट किया गया
- एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया
- एनवायरनमेंट वेरिएबल विवरण के साथ दस्तावेज़ीकरण को बेहतर बनाया गया

#### सत्र 02: RAG मूल्यांकन (`rag_eval_ragas.py`)
- मॉडल डिफ़ॉल्ट्स को अपडेट किया गया
- एंडपॉइंट कॉन्फ़िगरेशन जोड़ा गया
- एरर हैंडलिंग को बेहतर बनाया गया

#### सत्र 03: बेंचमार्किंग (`benchmark_oss_models.py`)
- डिफ़ॉल्ट मॉडल सूची को `phi-4-mini` शामिल करने के लिए अपडेट किया गया
- व्यापक एनवायरनमेंट वेरिएबल दस्तावेज़ीकरण जोड़ा गया
- फ़ंक्शन दस्तावेज़ीकरण को बेहतर बनाया गया
- पूरे में एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया

#### सत्र 04: मॉडल तुलना (`model_compare.py`)
- डिफ़ॉल्ट LLM को `gpt-oss-20b` से `qwen2.5-7b` में अपडेट किया गया
- एंडपॉइंट कॉन्फ़िगरेशन जोड़ा गया
- दस्तावेज़ीकरण को बेहतर बनाया गया

#### सत्र 05: मल्टी-एजेंट ऑर्केस्ट्रेशन (`agents_orchestrator.py`)
- टाइप हिंट्स जोड़े गए (जैसे `str | None` को `Optional[str]` में बदला गया)
- एजेंट क्लास दस्तावेज़ीकरण को बेहतर बनाया गया
- एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया
- इनिशियलाइज़ेशन पैटर्न को बेहतर बनाया गया

#### सत्र 06: मॉडल राउटर (`models_router.py`)
- एंडपॉइंट कॉन्फ़िगरेशन जोड़ा गया
- इंटेंट डिटेक्शन दस्तावेज़ीकरण को बेहतर बनाया गया
- राउटिंग लॉजिक दस्तावेज़ीकरण को बेहतर बनाया गया

#### सत्र 06: पाइपलाइन (`models_pipeline.py`)
- व्यापक फ़ंक्शन दस्तावेज़ीकरण जोड़ा गया
- चरण-दर-चरण दस्तावेज़ीकरण को बेहतर बनाया गया
- एरर हैंडलिंग को बेहतर बनाया गया

### स्क्रिप्ट्स

#### बेंचमार्क एक्सपोर्ट (`export_benchmark_markdown.py`)
- एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया
- डिफ़ॉल्ट मॉडल्स को अपडेट किया गया
- फ़ंक्शन दस्तावेज़ीकरण को बेहतर बनाया गया
- एरर हैंडलिंग को बेहतर बनाया गया

#### CLI लिंटर (`lint_markdown_cli.py`)
- SDK संदर्भ लिंक जोड़े गए
- उपयोग दस्तावेज़ीकरण को बेहतर बनाया गया

### टेस्ट्स

#### स्मोक टेस्ट्स (`smoke.py`)
- एंडपॉइंट ओवरराइड सपोर्ट जोड़ा गया
- दस्तावेज़ीकरण को बेहतर बनाया गया
- टेस्ट केस दस्तावेज़ीकरण को बेहतर बनाया गया
- बेहतर एरर रिपोर्टिंग

## एनवायरनमेंट वेरिएबल्स

सभी सैंपल अब इन एनवायरनमेंट वेरिएबल्स को सपोर्ट करते हैं:

### कोर कॉन्फ़िगरेशन
- `FOUNDRY_LOCAL_ALIAS` - उपयोग करने के लिए मॉडल एलियास (डिफ़ॉल्ट सैंपल के अनुसार बदलता है)
- `FOUNDRY_LOCAL_ENDPOINT` - सेवा एंडपॉइंट को ओवरराइड करें (वैकल्पिक)
- `SHOW_USAGE` - टोकन उपयोग सांख्यिकी दिखाएं (डिफ़ॉल्ट: "0")
- `RETRY_ON_FAIL` - रिट्री लॉजिक सक्षम करें (डिफ़ॉल्ट: "1")
- `RETRY_BACKOFF` - सेकंड में प्रारंभिक रिट्री देरी (डिफ़ॉल्ट: "1.0")

### सैंपल-विशिष्ट
- `EMBED_MODEL` - RAG सैंपल्स के लिए एम्बेडिंग मॉडल
- `BENCH_MODELS` - बेंचमार्किंग के लिए कॉमा से अलग किए गए मॉडल्स
- `BENCH_ROUNDS` - बेंचमार्क राउंड्स की संख्या
- `BENCH_PROMPT` - बेंचमार्क्स के लिए टेस्ट प्रॉम्प्ट
- `BENCH_STREAM` - पहले टोकन की लेटेंसी मापें
- `RAG_QUESTION` - RAG सैंपल्स के लिए टेस्ट प्रश्न
- `AGENT_MODEL_PRIMARY` - प्राइमरी एजेंट मॉडल
- `AGENT_MODEL_EDITOR` - एडिटर एजेंट मॉडल
- `SLM_ALIAS` - स्मॉल लैंग्वेज मॉडल एलियास
- `LLM_ALIAS` - लार्ज लैंग्वेज मॉडल एलियास

## लागू किए गए SDK सर्वोत्तम अभ्यास

### 1. उचित क्लाइंट इनिशियलाइज़ेशन
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

### 2. मॉडल जानकारी प्राप्त करना
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. एरर हैंडलिंग
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. एक्सपोनेंशियल बैकऑफ के साथ रिट्री लॉजिक
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

### 5. स्ट्रीमिंग सपोर्ट
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

## कस्टम सैंपल्स के लिए माइग्रेशन गाइड

यदि आप नए सैंपल बना रहे हैं या मौजूदा को अपडेट कर रहे हैं:

1. **`workshop_utils.py` हेल्पर्स का उपयोग करें**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **एंडपॉइंट ओवरराइड सपोर्ट करें**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **व्यापक दस्तावेज़ीकरण जोड़ें**:
   - एनवायरनमेंट वेरिएबल्स को डॉकस्ट्रींग में शामिल करें
   - SDK संदर्भ लिंक जोड़ें
   - उपयोग के उदाहरण जोड़ें

4. **टाइप हिंट्स का उपयोग करें**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **उचित एरर हैंडलिंग लागू करें**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## परीक्षण

सभी सैंपल्स का परीक्षण इस प्रकार किया जा सकता है:

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

## SDK दस्तावेज़ीकरण संदर्भ

- **मुख्य रिपॉजिटरी**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API दस्तावेज़ीकरण**: नवीनतम API दस्तावेज़ के लिए SDK रिपॉजिटरी देखें

## ब्रेकिंग बदलाव

### अपेक्षित नहीं
सभी बदलाव बैकवर्ड कम्पैटिबल हैं। अपडेट मुख्य रूप से:
- नई वैकल्पिक सुविधाएँ जोड़ते हैं (एंडपॉइंट ओवरराइड)
- एरर हैंडलिंग में सुधार करते हैं
- दस्तावेज़ीकरण को बेहतर बनाते हैं
- डिफ़ॉल्ट मॉडल नामों को वर्तमान सिफारिशों में अपडेट करते हैं

### वैकल्पिक सुधार
आप अपने कोड को निम्नलिखित का उपयोग करने के लिए अपडेट करना चाह सकते हैं:
- स्पष्ट एंडपॉइंट नियंत्रण के लिए `FOUNDRY_LOCAL_ENDPOINT`
- टोकन उपयोग दृश्यता के लिए `SHOW_USAGE=1`
- अपडेटेड मॉडल डिफ़ॉल्ट्स (`phi-3.5-mini` के बजाय `phi-4-mini`)

## सामान्य समस्याएँ और समाधान

### समस्या: "क्लाइंट इनिशियलाइज़ेशन विफल"
**समाधान**: सुनिश्चित करें कि फाउंड्री लोकल सेवा चल रही है:
```bash
foundry service start
foundry model run phi-4-mini
```

### समस्या: "मॉडल नहीं मिला"
**समाधान**: उपलब्ध मॉडल्स की जाँच करें:
```bash
foundry model list
```

### समस्या: एंडपॉइंट कनेक्शन त्रुटियाँ
**समाधान**: एंडपॉइंट सत्यापित करें:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## अगले कदम

1. **मॉड्यूल08 सैंपल्स को अपडेट करें**: मॉड्यूल08/samples में समान पैटर्न लागू करें
2. **इंटीग्रेशन टेस्ट जोड़ें**: व्यापक टेस्ट सूट बनाएं
3. **प्रदर्शन बेंचमार्किंग**: प्रदर्शन की तुलना करें (पहले/बाद में)
4. **दस्तावेज़ीकरण अपडेट्स**: मुख्य README को नए पैटर्न के साथ अपडेट करें

## योगदान दिशानिर्देश

नए सैंपल्स जोड़ते समय:
1. संगति के लिए `workshop_utils.py` का उपयोग करें
2. मौजूदा सैंपल्स में पैटर्न का पालन करें
3. व्यापक डॉकस्ट्रींग जोड़ें
4. SDK संदर्भ लिंक शामिल करें
5. एंडपॉइंट ओवरराइड सपोर्ट करें
6. उचित टाइप हिंट्स जोड़ें
7. डॉकस्ट्रींग में उपयोग के उदाहरण शामिल करें

## संस्करण संगतता

ये अपडेट निम्नलिखित के साथ संगत हैं:
- `foundry-local-sdk` (नवीनतम)
- `openai>=1.30.0`
- Python 3.8+

---

**अंतिम अपडेट**: 2025-01-08  
**रखरखावकर्ता**: EdgeAI वर्कशॉप टीम  
**SDK संस्करण**: Foundry Local SDK (नवीनतम 0.7.117+67073234e7)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।