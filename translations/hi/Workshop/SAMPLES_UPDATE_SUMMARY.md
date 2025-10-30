<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:04:40+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "hi"
}
-->
# वर्कशॉप नमूने - फाउंड्री लोकल SDK अपडेट सारांश

## अवलोकन

`Workshop/samples` डायरेक्टरी में सभी Python नमूनों को फाउंड्री लोकल SDK के सर्वोत्तम प्रथाओं का पालन करने और वर्कशॉप में निरंतरता सुनिश्चित करने के लिए अपडेट किया गया है।

**तारीख**: 8 अक्टूबर, 2025  
**क्षेत्र**: 6 वर्कशॉप सत्रों में 9 Python फाइलें  
**मुख्य ध्यान**: त्रुटि प्रबंधन, दस्तावेज़ीकरण, SDK पैटर्न, उपयोगकर्ता अनुभव

---

## अपडेट की गई फाइलें

### सत्र 01: शुरुआत करना
- ✅ `chat_bootstrap.py` - बेसिक चैट और स्ट्रीमिंग उदाहरण

### सत्र 02: RAG समाधान
- ✅ `rag_pipeline.py` - एम्बेडिंग के साथ RAG कार्यान्वयन
- ✅ `rag_eval_ragas.py` - RAGAS मेट्रिक्स के साथ RAG मूल्यांकन

### सत्र 03: ओपन सोर्स मॉडल
- ✅ `benchmark_oss_models.py` - मल्टी-मॉडल बेंचमार्किंग

### सत्र 04: अत्याधुनिक मॉडल
- ✅ `model_compare.py` - SLM बनाम LLM तुलना

### सत्र 05: AI-संचालित एजेंट
- ✅ `agents_orchestrator.py` - मल्टी-एजेंट समन्वय

### सत्र 06: उपकरण के रूप में मॉडल
- ✅ `models_router.py` - इरादा-आधारित मॉडल रूटिंग
- ✅ `models_pipeline.py` - मल्टी-स्टेप रूटेड पाइपलाइन

### सहायक इंफ्रास्ट्रक्चर
- ✅ `workshop_utils.py` - पहले से ही सर्वोत्तम प्रथाओं का पालन कर रहा है (कोई बदलाव आवश्यक नहीं)

---

## मुख्य सुधार

### 1. उन्नत त्रुटि प्रबंधन

**पहले:**
```python
manager, client, model_id = get_client(alias)
```

**बाद में:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**लाभ:**
- स्पष्ट त्रुटि संदेशों के साथ सहज त्रुटि प्रबंधन
- समस्या निवारण के लिए उपयोगी सुझाव
- स्क्रिप्टिंग के लिए उचित एग्जिट कोड

### 2. बेहतर इम्पोर्ट प्रबंधन

**पहले:**
```python
from sentence_transformers import SentenceTransformer
```

**बाद में:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**लाभ:**
- निर्भरता गायब होने पर स्पष्ट मार्गदर्शन
- अस्पष्ट इम्पोर्ट त्रुटियों को रोकता है
- उपयोगकर्ता-अनुकूल इंस्टॉलेशन निर्देश

### 3. व्यापक दस्तावेज़ीकरण

**सभी नमूनों में जोड़ा गया:**
- डॉकस्ट्रिंग में पर्यावरण चर का दस्तावेज़ीकरण
- SDK संदर्भ लिंक
- उपयोग के उदाहरण
- विस्तृत फ़ंक्शन/पैरामीटर दस्तावेज़ीकरण
- बेहतर IDE समर्थन के लिए टाइप हिंट्स

**उदाहरण:**
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

### 4. बेहतर उपयोगकर्ता प्रतिक्रिया

**जानकारीपूर्ण लॉगिंग जोड़ी गई:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**प्रगति संकेतक:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**संरचित आउटपुट:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. मजबूत बेंचमार्किंग

**सत्र 03 सुधार:**
- प्रति-मॉडल त्रुटि प्रबंधन (विफलता पर जारी रहता है)
- विस्तृत प्रगति रिपोर्टिंग
- वार्मअप राउंड सही तरीके से निष्पादित
- फर्स्ट-टोकन लेटेंसी मापन समर्थन
- चरणों का स्पष्ट विभाजन

### 6. सुसंगत टाइप हिंट्स

**संपूर्ण में जोड़ा गया:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**लाभ:**
- बेहतर IDE ऑटो-कम्प्लीट
- प्रारंभिक त्रुटि का पता लगाना
- आत्म-दस्तावेज़ीकरण कोड

### 7. उन्नत मॉडल राउटर

**सत्र 06 सुधार:**
- व्यापक इरादा पहचान दस्तावेज़ीकरण
- मॉडल चयन एल्गोरिदम व्याख्या
- विस्तृत रूटिंग लॉग्स
- परीक्षण आउटपुट स्वरूपण
- बैच परीक्षण में त्रुटि पुनर्प्राप्ति

### 8. मल्टी-एजेंट ऑर्केस्ट्रेशन

**सत्र 05 सुधार:**
- चरण-दर-चरण प्रगति रिपोर्टिंग
- प्रति-एजेंट त्रुटि प्रबंधन
- स्पष्ट पाइपलाइन संरचना
- बेहतर मेमोरी प्रबंधन दस्तावेज़ीकरण

---

## परीक्षण चेकलिस्ट

### आवश्यकताएँ
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### प्रत्येक नमूने का परीक्षण करें

#### सत्र 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### सत्र 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### सत्र 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### सत्र 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### सत्र 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### सत्र 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## पर्यावरण चर संदर्भ

### ग्लोबल (सभी नमूने)
| चर | विवरण | डिफ़ॉल्ट |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | उपयोग करने के लिए मॉडल उपनाम | नमूने के अनुसार भिन्न |
| `FOUNDRY_LOCAL_ENDPOINT` | सेवा एंडपॉइंट ओवरराइड करें | स्वचालित रूप से पता लगाया गया |
| `SHOW_USAGE` | टोकन उपयोग दिखाएं | `0` |
| `RETRY_ON_FAIL` | पुनः प्रयास लॉजिक सक्षम करें | `1` |
| `RETRY_BACKOFF` | प्रारंभिक पुनः प्रयास देरी | `1.0` |

### नमूना-विशिष्ट
| चर | उपयोगकर्ता | विवरण |
|----------|---------|-------------|
| `EMBED_MODEL` | सत्र 02 | एम्बेडिंग मॉडल का नाम |
| `RAG_QUESTION` | सत्र 02 | RAG के लिए परीक्षण प्रश्न |
| `BENCH_MODELS` | सत्र 03 | बेंचमार्क करने के लिए कॉमा-सेपरेटेड मॉडल |
| `BENCH_ROUNDS` | सत्र 03 | बेंचमार्क राउंड की संख्या |
| `BENCH_PROMPT` | सत्र 03 | बेंचमार्क के लिए परीक्षण प्रॉम्प्ट |
| `BENCH_STREAM` | सत्र 03 | फर्स्ट-टोकन लेटेंसी मापें |
| `SLM_ALIAS` | सत्र 04 | छोटा भाषा मॉडल |
| `LLM_ALIAS` | सत्र 04 | बड़ा भाषा मॉडल |
| `COMPARE_PROMPT` | सत्र 04 | तुलना परीक्षण प्रॉम्प्ट |
| `AGENT_MODEL_PRIMARY` | सत्र 05 | प्राथमिक एजेंट मॉडल |
| `AGENT_MODEL_EDITOR` | सत्र 05 | संपादक एजेंट मॉडल |
| `AGENT_QUESTION` | सत्र 05 | एजेंट्स के लिए परीक्षण प्रश्न |
| `PIPELINE_TASK` | सत्र 06 | पाइपलाइन के लिए कार्य |

---

## ब्रेकिंग बदलाव

**कोई नहीं** - सभी बदलाव पिछली संगतता बनाए रखते हैं।

मौजूदा स्क्रिप्ट काम करना जारी रखेंगी। नए फीचर्स हैं:
- वैकल्पिक पर्यावरण चर
- उन्नत त्रुटि संदेश (कार्यक्षमता को बाधित नहीं करते)
- अतिरिक्त लॉगिंग (दबाई जा सकती है)
- बेहतर टाइप हिंट्स (कोई रनटाइम प्रभाव नहीं)

---

## लागू सर्वोत्तम प्रथाएँ

### 1. हमेशा वर्कशॉप यूटिल्स का उपयोग करें
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. उचित त्रुटि प्रबंधन पैटर्न
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. जानकारीपूर्ण लॉगिंग
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. टाइप हिंट्स
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. व्यापक डॉकस्ट्रिंग्स
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

### 6. पर्यावरण चर समर्थन
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. सहज गिरावट
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

## सामान्य समस्याएँ और समाधान

### समस्या: इम्पोर्ट त्रुटियाँ
**समाधान:** गायब निर्भरता स्थापित करें
```bash
pip install sentence-transformers ragas datasets numpy
```

### समस्या: कनेक्शन त्रुटियाँ
**समाधान:** सुनिश्चित करें कि फाउंड्री लोकल चल रहा है
```bash
foundry service status
foundry model run phi-4-mini
```

### समस्या: मॉडल नहीं मिला
**समाधान:** उपलब्ध मॉडलों की जाँच करें
```bash
foundry model ls
foundry model download <alias>
```

### समस्या: धीमा प्रदर्शन
**समाधान:** छोटे मॉडल का उपयोग करें या पैरामीटर समायोजित करें
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## अगले कदम

### 1. सभी नमूनों का परीक्षण करें
ऊपर दिए गए परीक्षण चेकलिस्ट के माध्यम से चलें और सुनिश्चित करें कि सभी नमूने सही ढंग से काम कर रहे हैं।

### 2. दस्तावेज़ीकरण अपडेट करें
- नए उदाहरणों के साथ सत्र मार्कडाउन फाइलें अपडेट करें
- मुख्य README में समस्या निवारण अनुभाग जोड़ें
- त्वरित संदर्भ गाइड बनाएं

### 3. एकीकरण परीक्षण बनाएं
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. प्रदर्शन बेंचमार्क जोड़ें
त्रुटि प्रबंधन सुधारों से प्रदर्शन सुधारों को ट्रैक करें।

### 5. उपयोगकर्ता प्रतिक्रिया
वर्कशॉप प्रतिभागियों से प्रतिक्रिया एकत्र करें:
- त्रुटि संदेश स्पष्टता
- दस्तावेज़ीकरण पूर्णता
- उपयोग में आसानी

---

## संसाधन

- **फाउंड्री लोकल SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **त्वरित संदर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **माइग्रेशन नोट्स**: `Workshop/SDK_MIGRATION_NOTES.md`
- **मुख्य रिपॉजिटरी**: https://github.com/microsoft/Foundry-Local

---

## रखरखाव

### नए नमूने जोड़ना
नए नमूने बनाते समय इन पैटर्न का पालन करें:

1. क्लाइंट प्रबंधन के लिए `workshop_utils` का उपयोग करें
2. व्यापक त्रुटि प्रबंधन जोड़ें
3. पर्यावरण चर समर्थन शामिल करें
4. टाइप हिंट्स और डॉकस्ट्रिंग्स जोड़ें
5. जानकारीपूर्ण लॉगिंग प्रदान करें
6. डॉकस्ट्रिंग में उपयोग के उदाहरण शामिल करें
7. SDK दस्तावेज़ीकरण से लिंक करें

### अपडेट की समीक्षा करना
नमूना अपडेट की समीक्षा करते समय, जाँचें:
- [ ] सभी I/O ऑपरेशन्स पर त्रुटि प्रबंधन
- [ ] सार्वजनिक फ़ंक्शन्स पर टाइप हिंट्स
- [ ] व्यापक डॉकस्ट्रिंग्स
- [ ] पर्यावरण चर दस्तावेज़ीकरण
- [ ] जानकारीपूर्ण उपयोगकर्ता प्रतिक्रिया
- [ ] SDK संदर्भ लिंक
- [ ] सुसंगत कोड शैली

---

**सारांश**: सभी वर्कशॉप Python नमूने अब फाउंड्री लोकल SDK सर्वोत्तम प्रथाओं का पालन करते हैं, जिसमें उन्नत त्रुटि प्रबंधन, व्यापक दस्तावेज़ीकरण, और बेहतर उपयोगकर्ता अनुभव शामिल है। कोई ब्रेकिंग बदलाव नहीं - सभी मौजूदा कार्यक्षमता संरक्षित और उन्नत की गई है।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।