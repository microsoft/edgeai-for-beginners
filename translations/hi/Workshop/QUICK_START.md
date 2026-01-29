# वर्कशॉप त्वरित प्रारंभ गाइड

## आवश्यकताएँ

### 1. Foundry Local इंस्टॉल करें

आधिकारिक इंस्टॉलेशन गाइड का पालन करें:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python डिपेंडेंसी इंस्टॉल करें

वर्कशॉप डायरेक्टरी से:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## वर्कशॉप सैंपल्स चलाना

### सत्र 01: बेसिक चैट

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**एनवायरनमेंट वेरिएबल्स:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### सत्र 02: RAG पाइपलाइन

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**एनवायरनमेंट वेरिएबल्स:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### सत्र 02: RAG मूल्यांकन (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**नोट**: अतिरिक्त डिपेंडेंसी की आवश्यकता है, जिसे `requirements.txt` के माध्यम से इंस्टॉल किया जा सकता है

### सत्र 03: बेंचमार्किंग

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**एनवायरनमेंट वेरिएबल्स:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**आउटपुट**: JSON जिसमें लेटेंसी, थ्रूपुट, और फर्स्ट-टोकन मेट्रिक्स शामिल हैं

### सत्र 04: मॉडल तुलना

```bash
cd Workshop/samples
python -m session04.model_compare
```

**एनवायरनमेंट वेरिएबल्स:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### सत्र 05: मल्टी-एजेंट ऑर्केस्ट्रेशन

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**एनवायरनमेंट वेरिएबल्स:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### सत्र 06: मॉडल राउटर

```bash
cd Workshop/samples
python -m session06.models_router
```

**रूटिंग लॉजिक का परीक्षण करें** विभिन्न इंटेंट्स (कोड, सारांश, वर्गीकरण) के साथ

### सत्र 06: पाइपलाइन

```bash
python -m session06.models_pipeline
```

**जटिल मल्टी-स्टेप पाइपलाइन** जिसमें योजना, निष्पादन, और सुधार शामिल है

## स्क्रिप्ट्स

### बेंचमार्क रिपोर्ट निर्यात करें

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**आउटपुट**: मार्कडाउन टेबल + JSON मेट्रिक्स

### Markdown CLI पैटर्न्स की जांच करें

```bash
python lint_markdown_cli.py --verbose
```

**उद्देश्य**: दस्तावेज़ में पुराने CLI पैटर्न का पता लगाना

## परीक्षण

### स्मोक टेस्ट्स

```bash
cd Workshop
python -m tests.smoke
```

**टेस्ट्स**: मुख्य सैंपल्स की बुनियादी कार्यक्षमता

## समस्या निवारण

### सेवा चालू नहीं है

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### मॉड्यूल इंपोर्ट त्रुटियाँ

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### कनेक्शन त्रुटियाँ

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### मॉडल नहीं मिला

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## एनवायरनमेंट वेरिएबल संदर्भ

### कोर कॉन्फ़िगरेशन
| वेरिएबल | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | अलग-अलग | उपयोग करने के लिए मॉडल उपनाम |
| `FOUNDRY_LOCAL_ENDPOINT` | ऑटो | सेवा एंडपॉइंट ओवरराइड करें |
| `SHOW_USAGE` | `0` | टोकन उपयोग आँकड़े दिखाएँ |
| `RETRY_ON_FAIL` | `1` | पुनः प्रयास लॉजिक सक्षम करें |
| `RETRY_BACKOFF` | `1.0` | प्रारंभिक पुनः प्रयास विलंब (सेकंड) |

### सत्र-विशिष्ट
| वेरिएबल | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिंग मॉडल |
| `RAG_QUESTION` | सैंपल देखें | RAG परीक्षण प्रश्न |
| `BENCH_MODELS` | अलग-अलग | कॉमा से अलग मॉडल्स |
| `BENCH_ROUNDS` | `3` | बेंचमार्क पुनरावृत्तियाँ |
| `BENCH_PROMPT` | सैंपल देखें | बेंचमार्क प्रॉम्प्ट |
| `BENCH_STREAM` | `0` | फर्स्ट-टोकन लेटेंसी मापें |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | प्राथमिक एजेंट मॉडल |
| `AGENT_MODEL_EDITOR` | प्राथमिक | संपादक एजेंट मॉडल |
| `SLM_ALIAS` | `phi-4-mini` | छोटा भाषा मॉडल |
| `LLM_ALIAS` | `qwen2.5-7b` | बड़ा भाषा मॉडल |
| `COMPARE_PROMPT` | सैंपल देखें | तुलना प्रॉम्प्ट |

## अनुशंसित मॉडल्स

### विकास और परीक्षण
- **phi-4-mini** - गुणवत्ता और गति का संतुलन
- **qwen2.5-0.5b** - वर्गीकरण के लिए बहुत तेज़
- **gemma-2-2b** - अच्छी गुणवत्ता, मध्यम गति

### उत्पादन परिदृश्य
- **phi-4-mini** - सामान्य उपयोग
- **deepseek-coder-1.3b** - कोड जनरेशन
- **qwen2.5-7b** - उच्च गुणवत्ता वाले उत्तर

## SDK दस्तावेज़

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## सहायता प्राप्त करना

1. सेवा स्थिति जांचें: `foundry service status`
2. लॉग देखें: Foundry Local सेवा लॉग जांचें
3. SDK दस्तावेज़ देखें: https://github.com/microsoft/Foundry-Local
4. सैंपल कोड की समीक्षा करें: सभी सैंपल्स में विस्तृत डॉकस्ट्रिंग्स हैं

## अगले कदम

1. सभी वर्कशॉप सत्र क्रम में पूरा करें
2. विभिन्न मॉडल्स के साथ प्रयोग करें
3. अपने उपयोग मामलों के लिए सैंपल्स संशोधित करें

---

**अंतिम अपडेट**: 2025-01-08  
**वर्कशॉप संस्करण**: नवीनतम  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->