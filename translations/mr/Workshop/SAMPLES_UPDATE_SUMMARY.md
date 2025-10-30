<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:15:33+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "mr"
}
-->
# कार्यशाळा नमुने - फाउंड्री लोकल SDK अद्यतन सारांश

## आढावा

`Workshop/samples` निर्देशिकेतील सर्व Python नमुने फाउंड्री लोकल SDK च्या सर्वोत्तम पद्धतींचे पालन करण्यासाठी आणि कार्यशाळेत सातत्य सुनिश्चित करण्यासाठी अद्यतनित केले गेले आहेत.

**तारीख**: 8 ऑक्टोबर, 2025  
**व्याप्ती**: 6 कार्यशाळा सत्रांतील 9 Python फाइल्स  
**प्राथमिक लक्ष**: त्रुटी हाताळणी, दस्तऐवजीकरण, SDK नमुने, वापरकर्ता अनुभव

---

## अद्यतनित फाइल्स

### सत्र 01: सुरुवात
- ✅ `chat_bootstrap.py` - मूलभूत चॅट आणि स्ट्रीमिंग उदाहरणे

### सत्र 02: RAG सोल्यूशन्स
- ✅ `rag_pipeline.py` - एम्बेडिंगसह RAG अंमलबजावणी
- ✅ `rag_eval_ragas.py` - RAGAS मेट्रिक्ससह RAG मूल्यांकन

### सत्र 03: ओपन सोर्स मॉडेल्स
- ✅ `benchmark_oss_models.py` - मल्टी-मॉडेल बेंचमार्किंग

### सत्र 04: अत्याधुनिक मॉडेल्स
- ✅ `model_compare.py` - SLM विरुद्ध LLM तुलना

### सत्र 05: AI-सक्षम एजंट्स
- ✅ `agents_orchestrator.py` - मल्टी-एजंट समन्वय

### सत्र 06: मॉडेल्स साधन म्हणून
- ✅ `models_router.py` - हेतू-आधारित मॉडेल रूटिंग
- ✅ `models_pipeline.py` - मल्टी-स्टेप रूटेड पाइपलाइन

### सहाय्यक पायाभूत सुविधा
- ✅ `workshop_utils.py` - आधीच सर्वोत्तम पद्धतींचे पालन करत आहे (कोणतेही बदल आवश्यक नाहीत)

---

## मुख्य सुधारणा

### 1. सुधारित त्रुटी हाताळणी

**पूर्वी:**
```python
manager, client, model_id = get_client(alias)
```

**नंतर:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**फायदे:**
- स्पष्ट त्रुटी संदेशांसह सौम्य त्रुटी हाताळणी
- समस्या सोडवण्यासाठी उपयुक्त सूचना
- स्क्रिप्टिंगसाठी योग्य एक्झिट कोड्स

### 2. सुधारित आयात व्यवस्थापन

**पूर्वी:**
```python
from sentence_transformers import SentenceTransformer
```

**नंतर:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**फायदे:**
- अवलंबित्व गहाळ असल्यास स्पष्ट मार्गदर्शन
- गोंधळात टाकणाऱ्या आयात त्रुटी टाळते
- वापरकर्ता-अनुकूल स्थापना सूचना

### 3. व्यापक दस्तऐवजीकरण

**सर्व नमुन्यांमध्ये जोडले:**
- डॉक्स्ट्रिंगमध्ये पर्यावरणीय व्हेरिएबल्सचे दस्तऐवजीकरण
- SDK संदर्भ दुवे
- वापर उदाहरणे
- तपशीलवार फंक्शन/पॅरामीटर दस्तऐवजीकरण
- चांगल्या IDE समर्थनासाठी टाइप हिंट्स

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

### 4. सुधारित वापरकर्ता अभिप्राय

**माहितीपूर्ण लॉगिंग जोडले:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**प्रगती निर्देशक:**
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

**सत्र 03 सुधारणा:**
- प्रति-मॉडेल त्रुटी हाताळणी (अपयशावर पुढे चालू राहते)
- तपशीलवार प्रगती अहवाल
- योग्य प्रकारे वॉर्मअप राउंड्स अंमलात आणले
- फर्स्ट-टोकन लेटन्सी मोजमाप समर्थन
- टप्प्यांचे स्पष्ट विभाजन

### 6. सातत्यपूर्ण टाइप हिंट्स

**सर्वत्र जोडले:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**फायदे:**
- चांगले IDE ऑटो-कंप्लीट
- लवकर त्रुटी शोध
- स्व-डॉक्युमेंटिंग कोड

### 7. सुधारित मॉडेल राउटर

**सत्र 06 सुधारणा:**
- व्यापक हेतू शोध दस्तऐवजीकरण
- मॉडेल निवड अल्गोरिदम स्पष्टीकरण
- तपशीलवार रूटिंग लॉग्स
- चाचणी आउटपुट स्वरूपन
- बॅच चाचणीमध्ये त्रुटी पुनर्प्राप्ती

### 8. मल्टी-एजंट ऑर्केस्ट्रेशन

**सत्र 05 सुधारणा:**
- टप्प्याटप्प्याने प्रगती अहवाल
- प्रति-एजंट त्रुटी हाताळणी
- स्पष्ट पाइपलाइन रचना
- चांगले मेमरी व्यवस्थापन दस्तऐवजीकरण

---

## चाचणी तपासणी यादी

### पूर्वतयारी
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### प्रत्येक नमुना चाचणी करा

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

## पर्यावरणीय व्हेरिएबल्स संदर्भ

### जागतिक (सर्व नमुने)
| व्हेरिएबल | वर्णन | डीफॉल्ट |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | वापरण्यासाठी मॉडेल उपनाम | नमुन्यानुसार बदलते |
| `FOUNDRY_LOCAL_ENDPOINT` | सेवा एंडपॉइंट ओव्हरराइड करा | स्वयंचलितपणे शोधले जाते |
| `SHOW_USAGE` | टोकन वापर दर्शवा | `0` |
| `RETRY_ON_FAIL` | पुनर्प्रयत्न लॉजिक सक्षम करा | `1` |
| `RETRY_BACKOFF` | प्रारंभिक पुनर्प्रयत्न विलंब | `1.0` |

### नमुना-विशिष्ट
| व्हेरिएबल | वापरलेले | वर्णन |
|----------|---------|-------------|
| `EMBED_MODEL` | सत्र 02 | एम्बेडिंग मॉडेलचे नाव |
| `RAG_QUESTION` | सत्र 02 | RAG साठी चाचणी प्रश्न |
| `BENCH_MODELS` | सत्र 03 | बेंचमार्कसाठी कॉमा-वेगळे मॉडेल्स |
| `BENCH_ROUNDS` | सत्र 03 | बेंचमार्क राउंड्सची संख्या |
| `BENCH_PROMPT` | सत्र 03 | बेंचमार्कसाठी चाचणी प्रॉम्प्ट |
| `BENCH_STREAM` | सत्र 03 | फर्स्ट-टोकन लेटन्सी मोजा |
| `SLM_ALIAS` | सत्र 04 | लहान भाषा मॉडेल |
| `LLM_ALIAS` | सत्र 04 | मोठे भाषा मॉडेल |
| `COMPARE_PROMPT` | सत्र 04 | तुलना चाचणी प्रॉम्प्ट |
| `AGENT_MODEL_PRIMARY` | सत्र 05 | प्राथमिक एजंट मॉडेल |
| `AGENT_MODEL_EDITOR` | सत्र 05 | संपादक एजंट मॉडेल |
| `AGENT_QUESTION` | सत्र 05 | एजंट्ससाठी चाचणी प्रश्न |
| `PIPELINE_TASK` | सत्र 06 | पाइपलाइनसाठी कार्य |

---

## ब्रेकिंग बदल

**कोणतेही नाहीत** - सर्व बदल मागील आवृत्त्यांशी सुसंगत आहेत.

अस्तित्वातील स्क्रिप्ट्स कार्य करत राहतील. नवीन वैशिष्ट्ये:
- पर्यायी पर्यावरणीय व्हेरिएबल्स
- सुधारित त्रुटी संदेश (कार्यक्षमता बिघडवत नाहीत)
- अतिरिक्त लॉगिंग (दाबले जाऊ शकते)
- चांगले टाइप हिंट्स (कोणताही रनटाइम प्रभाव नाही)

---

## अंमलात आणलेल्या सर्वोत्तम पद्धती

### 1. नेहमी Workshop Utils वापरा
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. योग्य त्रुटी हाताळणी नमुना
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. माहितीपूर्ण लॉगिंग
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

### 5. व्यापक डॉक्स्ट्रिंग्स
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

### 6. पर्यावरणीय व्हेरिएबल्स समर्थन
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. सौम्य अपयश
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

## सामान्य समस्या आणि उपाय

### समस्या: आयात त्रुटी
**उपाय:** गहाळ अवलंबित्व स्थापित करा
```bash
pip install sentence-transformers ragas datasets numpy
```

### समस्या: कनेक्शन त्रुटी
**उपाय:** फाउंड्री लोकल चालू असल्याची खात्री करा
```bash
foundry service status
foundry model run phi-4-mini
```

### समस्या: मॉडेल सापडले नाही
**उपाय:** उपलब्ध मॉडेल्स तपासा
```bash
foundry model ls
foundry model download <alias>
```

### समस्या: धीमे कार्यप्रदर्शन
**उपाय:** लहान मॉडेल्स वापरा किंवा पॅरामीटर्स समायोजित करा
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## पुढील पावले

### 1. सर्व नमुने चाचणी करा
वरील चाचणी तपासणी यादीद्वारे सर्व नमुने योग्यरित्या कार्य करत असल्याची खात्री करा.

### 2. दस्तऐवजीकरण अद्यतनित करा
- नवीन उदाहरणांसह सत्र मार्कडाउन फाइल्स अद्यतनित करा
- मुख्य README मध्ये समस्या सोडवण्याचा विभाग जोडा
- जलद संदर्भ मार्गदर्शक तयार करा

### 3. एकत्रीकरण चाचण्या तयार करा
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. कार्यप्रदर्शन बेंचमार्क जोडा
त्रुटी हाताळणी सुधारण्यामुळे कार्यप्रदर्शन सुधारणा ट्रॅक करा.

### 5. वापरकर्ता अभिप्राय
कार्यशाळेतील सहभागींकडून अभिप्राय गोळा करा:
- त्रुटी संदेश स्पष्टता
- दस्तऐवजीकरण पूर्णता
- वापरण्याची सुलभता

---

## संसाधने

- **फाउंड्री लोकल SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **जलद संदर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **मायग्रेशन नोट्स**: `Workshop/SDK_MIGRATION_NOTES.md`
- **मुख्य रिपॉझिटरी**: https://github.com/microsoft/Foundry-Local

---

## देखभाल

### नवीन नमुने जोडणे
नवीन नमुने तयार करताना या नमुन्यांचे अनुसरण करा:

1. क्लायंट व्यवस्थापनासाठी `workshop_utils` वापरा
2. व्यापक त्रुटी हाताळणी जोडा
3. पर्यावरणीय व्हेरिएबल्स समर्थन समाविष्ट करा
4. टाइप हिंट्स आणि डॉक्स्ट्रिंग्स जोडा
5. माहितीपूर्ण लॉगिंग प्रदान करा
6. डॉक्स्ट्रिंगमध्ये वापर उदाहरणे समाविष्ट करा
7. SDK दस्तऐवजीकरणाशी लिंक करा

### अद्यतन पुनरावलोकन
नमुना अद्यतन पुनरावलोकन करताना, तपासा:
- [ ] सर्व I/O ऑपरेशन्सवर त्रुटी हाताळणी
- [ ] सार्वजनिक फंक्शन्सवर टाइप हिंट्स
- [ ] व्यापक डॉक्स्ट्रिंग्स
- [ ] पर्यावरणीय व्हेरिएबल्स दस्तऐवजीकरण
- [ ] माहितीपूर्ण वापरकर्ता अभिप्राय
- [ ] SDK संदर्भ दुवे
- [ ] सातत्यपूर्ण कोड शैली

---

**सारांश**: सर्व कार्यशाळा Python नमुने आता फाउंड्री लोकल SDK च्या सर्वोत्तम पद्धतींचे पालन करतात, ज्यामध्ये सुधारित त्रुटी हाताळणी, व्यापक दस्तऐवजीकरण आणि सुधारित वापरकर्ता अनुभव आहे. कोणतेही ब्रेकिंग बदल नाहीत - सर्व विद्यमान कार्यक्षमता संरक्षित आणि सुधारित केली गेली आहे.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.