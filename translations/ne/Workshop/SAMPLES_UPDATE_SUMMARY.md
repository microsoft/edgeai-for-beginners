<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:21:00+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ne"
}
-->
# कार्यशाला नमूनाहरू - फाउन्ड्री लोकल SDK अद्यावधिक सारांश

## अवलोकन

`Workshop/samples` निर्देशिकामा रहेका सबै Python नमूनाहरू फाउन्ड्री लोकल SDK को उत्कृष्ट अभ्यासहरू अनुसरण गर्न र कार्यशालामा निरन्तरता सुनिश्चित गर्न अद्यावधिक गरिएको छ।

**मिति**: अक्टोबर ८, २०२५  
**क्षेत्र**: ६ कार्यशाला सत्रहरूमा ९ Python फाइलहरू  
**मुख्य ध्यान**: त्रुटि व्यवस्थापन, दस्तावेजीकरण, SDK ढाँचा, प्रयोगकर्ता अनुभव

---

## अद्यावधिक फाइलहरू

### सत्र ०१: सुरुवात
- ✅ `chat_bootstrap.py` - आधारभूत च्याट र स्ट्रिमिङ उदाहरणहरू

### सत्र ०२: RAG समाधानहरू
- ✅ `rag_pipeline.py` - embeddings सहित RAG कार्यान्वयन
- ✅ `rag_eval_ragas.py` - RAGAS मेट्रिक्सको साथ RAG मूल्याङ्कन

### सत्र ०३: खुला स्रोत मोडेलहरू
- ✅ `benchmark_oss_models.py` - बहु-मोडेल बेंचमार्किङ

### सत्र ०४: अत्याधुनिक मोडेलहरू
- ✅ `model_compare.py` - SLM बनाम LLM तुलना

### सत्र ०५: AI-संचालित एजेन्टहरू
- ✅ `agents_orchestrator.py` - बहु-एजेन्ट समन्वय

### सत्र ०६: उपकरणको रूपमा मोडेलहरू
- ✅ `models_router.py` - उद्देश्य-आधारित मोडेल राउटिङ
- ✅ `models_pipeline.py` - बहु-चरण राउटेड पाइपलाइन

### सहायक पूर्वाधार
- ✅ `workshop_utils.py` - पहिले नै उत्कृष्ट अभ्यासहरू अनुसरण गर्दै (कुनै परिवर्तन आवश्यक छैन)

---

## मुख्य सुधारहरू

### १. सुधारिएको त्रुटि व्यवस्थापन

**पहिले:**
```python
manager, client, model_id = get_client(alias)
```

**पछि:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**फाइदा:**
- स्पष्ट त्रुटि सन्देशहरू सहित सौम्य त्रुटि व्यवस्थापन
- समाधानयोग्य समस्या समाधान सुझावहरू
- स्क्रिप्टिङका लागि उचित निकास कोडहरू

### २. राम्रो आयात व्यवस्थापन

**पहिले:**
```python
from sentence_transformers import SentenceTransformer
```

**पछि:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**फाइदा:**
- निर्भरता हराएको बेला स्पष्ट मार्गदर्शन
- अस्पष्ट आयात त्रुटिहरू रोक्छ
- प्रयोगकर्ता-अनुकूल स्थापना निर्देशनहरू

### ३. व्यापक दस्तावेजीकरण

**सबै नमूनाहरूमा थपिएको:**
- docstrings मा वातावरण चर दस्तावेजीकरण
- SDK सन्दर्भ लिंकहरू
- प्रयोग उदाहरणहरू
- विस्तृत कार्य/प्यारामिटर दस्तावेजीकरण
- IDE समर्थनका लागि प्रकार संकेतहरू

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

### ४. सुधारिएको प्रयोगकर्ता प्रतिक्रिया

**जानकारीमूलक लगिङ थपिएको:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**प्रगति सूचकहरू:**
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

### ५. मजबुत बेंचमार्किङ

**सत्र ०३ सुधारहरू:**
- प्रति-मोडेल त्रुटि व्यवस्थापन (असफलतामा जारी राख्छ)
- विस्तृत प्रगति रिपोर्टिङ
- वार्मअप राउन्डहरू ठीकसँग कार्यान्वयन
- पहिलो-टोकन विलम्ब मापन समर्थन
- चरणहरूको स्पष्ट विभाजन

### ६. सुसंगत प्रकार संकेतहरू

**सबैतिर थपिएको:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**फाइदा:**
- राम्रो IDE स्वतः पूर्णता
- प्रारम्भिक त्रुटि पत्ता लगाउने
- आत्म-दस्तावेजीकरण कोड

### ७. सुधारिएको मोडेल राउटर

**सत्र ०६ सुधारहरू:**
- उद्देश्य पत्ता लगाउने व्यापक दस्तावेजीकरण
- मोडेल चयन एल्गोरिदम व्याख्या
- विस्तृत राउटिङ लगहरू
- परीक्षण आउटपुट ढाँचा
- ब्याच परीक्षणमा त्रुटि पुनःप्राप्ति

### ८. बहु-एजेन्ट समन्वय

**सत्र ०५ सुधारहरू:**
- चरण-दर-चरण प्रगति रिपोर्टिङ
- प्रति-एजेन्ट त्रुटि व्यवस्थापन
- स्पष्ट पाइपलाइन संरचना
- राम्रो मेमोरी व्यवस्थापन दस्तावेजीकरण

---

## परीक्षण चेकलिस्ट

### पूर्वापेक्षाहरू
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### प्रत्येक नमूना परीक्षण गर्नुहोस्

#### सत्र ०१
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### सत्र ०२
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### सत्र ०३
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### सत्र ०४
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### सत्र ०५
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### सत्र ०६
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## वातावरण चर सन्दर्भ

### विश्वव्यापी (सबै नमूनाहरू)
| चर | विवरण | पूर्वनिर्धारित |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | प्रयोग गर्न मोडेल उपनाम | नमूनाद्वारा फरक |
| `FOUNDRY_LOCAL_ENDPOINT` | सेवा अन्त बिन्दु अधिलेखन | स्वतः पत्ता लगाइएको |
| `SHOW_USAGE` | टोकन प्रयोग देखाउनुहोस् | `0` |
| `RETRY_ON_FAIL` | पुनः प्रयास तर्क सक्षम गर्नुहोस् | `1` |
| `RETRY_BACKOFF` | प्रारम्भिक पुनः प्रयास ढिलाइ | `1.0` |

### नमूना-विशिष्ट
| चर | प्रयोग गरिएको | विवरण |
|----------|---------|-------------|
| `EMBED_MODEL` | सत्र ०२ | embedding मोडेल नाम |
| `RAG_QUESTION` | सत्र ०२ | RAG का लागि परीक्षण प्रश्न |
| `BENCH_MODELS` | सत्र ०३ | बेंचमार्क गर्न मोडेलहरूको सूची |
| `BENCH_ROUNDS` | सत्र ०३ | बेंचमार्क राउन्डहरूको संख्या |
| `BENCH_PROMPT` | सत्र ०३ | बेंचमार्कका लागि परीक्षण प्रम्प्ट |
| `BENCH_STREAM` | सत्र ०३ | पहिलो-टोकन विलम्ब मापन |
| `SLM_ALIAS` | सत्र ०४ | सानो भाषा मोडेल |
| `LLM_ALIAS` | सत्र ०४ | ठूलो भाषा मोडेल |
| `COMPARE_PROMPT` | सत्र ०४ | तुलना परीक्षण प्रम्प्ट |
| `AGENT_MODEL_PRIMARY` | सत्र ०५ | प्राथमिक एजेन्ट मोडेल |
| `AGENT_MODEL_EDITOR` | सत्र ०५ | सम्पादक एजेन्ट मोडेल |
| `AGENT_QUESTION` | सत्र ०५ | एजेन्टहरूको लागि परीक्षण प्रश्न |
| `PIPELINE_TASK` | सत्र ०६ | पाइपलाइनका लागि कार्य |

---

## ब्रेकिङ परिवर्तनहरू

**कुनै छैन** - सबै परिवर्तनहरू पछाडि सुसंगत छन्।

अस्तित्वमा रहेका स्क्रिप्टहरू काम गर्न जारी रहनेछन्। नयाँ सुविधाहरू:
- वैकल्पिक वातावरण चरहरू
- सुधारिएको त्रुटि सन्देशहरू (कार्यक्षमता भङ्ग गर्दैन)
- थप लगिङ (दबाउन सकिन्छ)
- राम्रो प्रकार संकेतहरू (कुनै रनटाइम प्रभाव छैन)

---

## लागू गरिएका उत्कृष्ट अभ्यासहरू

### १. सधैं कार्यशाला युटिल्स प्रयोग गर्नुहोस्
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### २. उचित त्रुटि व्यवस्थापन ढाँचा
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ३. जानकारीमूलक लगिङ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### ४. प्रकार संकेतहरू
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### ५. व्यापक docstrings
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

### ६. वातावरण चर समर्थन
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### ७. सौम्य ह्रास
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

## सामान्य समस्या र समाधानहरू

### समस्या: आयात त्रुटिहरू
**समाधान:** हराएका निर्भरता स्थापना गर्नुहोस्
```bash
pip install sentence-transformers ragas datasets numpy
```

### समस्या: जडान त्रुटिहरू
**समाधान:** सुनिश्चित गर्नुहोस् कि फाउन्ड्री लोकल चलिरहेको छ
```bash
foundry service status
foundry model run phi-4-mini
```

### समस्या: मोडेल फेला परेन
**समाधान:** उपलब्ध मोडेलहरू जाँच गर्नुहोस्
```bash
foundry model ls
foundry model download <alias>
```

### समस्या: ढिलो प्रदर्शन
**समाधान:** साना मोडेलहरू प्रयोग गर्नुहोस् वा प्यारामिटरहरू समायोजन गर्नुहोस्
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## आगामी कदमहरू

### १. सबै नमूनाहरू परीक्षण गर्नुहोस्
माथि दिइएको परीक्षण चेकलिस्ट मार्फत जानुहोस् र सबै नमूनाहरू ठीकसँग काम गरिरहेको सुनिश्चित गर्नुहोस्।

### २. दस्तावेजीकरण अद्यावधिक गर्नुहोस्
- नयाँ उदाहरणहरू सहित सत्र markdown फाइलहरू अद्यावधिक गर्नुहोस्
- मुख्य README मा समस्या समाधान खण्ड थप्नुहोस्
- छिटो सन्दर्भ मार्गदर्शक बनाउनुहोस्

### ३. एकीकरण परीक्षणहरू बनाउनुहोस्
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### ४. प्रदर्शन बेंचमार्कहरू थप्नुहोस्
त्रुटि व्यवस्थापन सुधारबाट प्रदर्शन सुधारहरू ट्र्याक गर्नुहोस्।

### ५. प्रयोगकर्ता प्रतिक्रिया
कार्यशाला सहभागीहरूबाट प्रतिक्रिया सङ्कलन गर्नुहोस्:
- त्रुटि सन्देश स्पष्टता
- दस्तावेजीकरण पूर्णता
- प्रयोगको सजिलोपन

---

## स्रोतहरू

- **फाउन्ड्री लोकल SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **छिटो सन्दर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **माइग्रेशन नोट्स**: `Workshop/SDK_MIGRATION_NOTES.md`
- **मुख्य रिपोजिटरी**: https://github.com/microsoft/Foundry-Local

---

## मर्मतसम्भार

### नयाँ नमूनाहरू थप्दै
नयाँ नमूनाहरू बनाउँदा यी ढाँचाहरू अनुसरण गर्नुहोस्:

1. ग्राहक व्यवस्थापनका लागि `workshop_utils` प्रयोग गर्नुहोस्
2. व्यापक त्रुटि व्यवस्थापन थप्नुहोस्
3. वातावरण चर समर्थन समावेश गर्नुहोस्
4. प्रकार संकेतहरू र docstrings थप्नुहोस्
5. जानकारीमूलक लगिङ प्रदान गर्नुहोस्
6. docstring मा प्रयोग उदाहरणहरू समावेश गर्नुहोस्
7. SDK दस्तावेजीकरणमा लिंक गर्नुहोस्

### अद्यावधिक समीक्षा गर्दै
नमूना अद्यावधिक समीक्षा गर्दा, जाँच गर्नुहोस्:
- [ ] सबै I/O अपरेशनहरूमा त्रुटि व्यवस्थापन
- [ ] सार्वजनिक कार्यहरूमा प्रकार संकेतहरू
- [ ] व्यापक docstrings
- [ ] वातावरण चर दस्तावेजीकरण
- [ ] जानकारीमूलक प्रयोगकर्ता प्रतिक्रिया
- [ ] SDK सन्दर्भ लिंकहरू
- [ ] सुसंगत कोड शैली

---

**सारांश**: सबै कार्यशाला Python नमूनाहरू अब फाउन्ड्री लोकल SDK को उत्कृष्ट अभ्यासहरू अनुसरण गर्छन्, सुधारिएको त्रुटि व्यवस्थापन, व्यापक दस्तावेजीकरण, र सुधारिएको प्रयोगकर्ता अनुभव सहित। कुनै ब्रेकिङ परिवर्तन छैन - सबै अस्तित्वमा रहेको कार्यक्षमता सुरक्षित र सुधारिएको।

---

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।