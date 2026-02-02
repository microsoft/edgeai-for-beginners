# कार्यशाला छिटो सुरु गर्ने मार्गदर्शन

## आवश्यकताहरू

### १. Foundry Local स्थापना गर्नुहोस्

आधिकारिक स्थापना मार्गदर्शन पालना गर्नुहोस्:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### २. Python निर्भरता स्थापना गर्नुहोस्

कार्यशाला निर्देशिका बाट:

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

## कार्यशाला नमूनाहरू चलाउने

### सत्र ०१: आधारभूत च्याट

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**पर्यावरण चरहरू:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### सत्र ०२: RAG पाइपलाइन

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**पर्यावरण चरहरू:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### सत्र ०२: RAG मूल्यांकन (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**नोट**: `requirements.txt` मार्फत थप निर्भरता स्थापना आवश्यक छ

### सत्र ०३: बेंचमार्किङ

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**पर्यावरण चरहरू:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**आउटपुट**: विलम्बता, थ्रूपुट, र पहिलो-टोकन मेट्रिक्स सहित JSON

### सत्र ०४: मोडेल तुलना

```bash
cd Workshop/samples
python -m session04.model_compare
```

**पर्यावरण चरहरू:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### सत्र ०५: बहु-एजेन्ट समन्वय

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**पर्यावरण चरहरू:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### सत्र ०६: मोडेल राउटर

```bash
cd Workshop/samples
python -m session06.models_router
```

**राउटिङ तर्क परीक्षण गर्दछ** विभिन्न उद्देश्यहरू (कोड, सारांश, वर्गीकरण) संग

### सत्र ०६: पाइपलाइन

```bash
python -m session06.models_pipeline
```

**जटिल बहु-चरण पाइपलाइन** योजना, कार्यान्वयन, र सुधार सहित

## स्क्रिप्टहरू

### बेंचमार्क रिपोर्ट निर्यात गर्नुहोस्

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**आउटपुट**: Markdown तालिका + JSON मेट्रिक्स

### Markdown CLI ढाँचाहरू जाँच गर्नुहोस्

```bash
python lint_markdown_cli.py --verbose
```

**उद्देश्य**: दस्तावेजमा पुरानो CLI ढाँचाहरू पत्ता लगाउनुहोस्

## परीक्षण

### स्मोक परीक्षणहरू

```bash
cd Workshop
python -m tests.smoke
```

**परीक्षणहरू**: प्रमुख नमूनाहरूको आधारभूत कार्यक्षमता

## समस्या समाधान

### सेवा चलिरहेको छैन

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### मोड्युल आयात त्रुटिहरू

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### जडान त्रुटिहरू

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### मोडेल फेला परेन

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## पर्यावरण चर सन्दर्भ

### कोर कन्फिगरेसन
| चर | डिफल्ट | विवरण |
|-----|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | फरक-फरक | प्रयोग गर्न मोडेल उपनाम |
| `FOUNDRY_LOCAL_ENDPOINT` | स्वत: | सेवा अन्त बिन्दु अधिलेखन |
| `SHOW_USAGE` | `0` | टोकन प्रयोग तथ्याङ्क देखाउनुहोस् |
| `RETRY_ON_FAIL` | `1` | पुन: प्रयास तर्क सक्षम गर्नुहोस् |
| `RETRY_BACKOFF` | `1.0` | प्रारम्भिक पुन: प्रयास ढिलाइ (सेकेन्ड) |

### सत्र-विशिष्ट
| चर | डिफल्ट | विवरण |
|-----|--------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिङ मोडेल |
| `RAG_QUESTION` | नमूना हेर्नुहोस् | RAG परीक्षण प्रश्न |
| `BENCH_MODELS` | फरक-फरक | अल्पविरामले छुट्याइएका मोडेलहरू |
| `BENCH_ROUNDS` | `3` | बेंचमार्क पुनरावृत्तिहरू |
| `BENCH_PROMPT` | नमूना हेर्नुहोस् | बेंचमार्क प्रम्प्ट |
| `BENCH_STREAM` | `0` | पहिलो-टोकन विलम्बता मापन गर्नुहोस् |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | प्राथमिक एजेन्ट मोडेल |
| `AGENT_MODEL_EDITOR` | प्राथमिक | सम्पादक एजेन्ट मोडेल |
| `SLM_ALIAS` | `phi-4-mini` | सानो भाषा मोडेल |
| `LLM_ALIAS` | `qwen2.5-7b` | ठूलो भाषा मोडेल |
| `COMPARE_PROMPT` | नमूना हेर्नुहोस् | तुलना प्रम्प्ट |

## सिफारिस गरिएका मोडेलहरू

### विकास र परीक्षण
- **phi-4-mini** - गुणस्तर र गति सन्तुलित
- **qwen2.5-0.5b** - वर्गीकरणको लागि धेरै छिटो
- **gemma-2-2b** - राम्रो गुणस्तर, मध्यम गति

### उत्पादन परिदृश्यहरू
- **phi-4-mini** - सामान्य उद्देश्य
- **deepseek-coder-1.3b** - कोड उत्पादन
- **qwen2.5-7b** - उच्च गुणस्तर प्रतिक्रिया

## SDK दस्तावेज

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## सहयोग प्राप्त गर्ने

1. सेवा स्थिति जाँच गर्नुहोस्: `foundry service status`
2. लगहरू हेर्नुहोस्: Foundry Local सेवा लगहरू जाँच गर्नुहोस्
3. SDK दस्तावेज हेर्नुहोस्: https://github.com/microsoft/Foundry-Local
4. नमूना कोड समीक्षा गर्नुहोस्: सबै नमूनाहरूमा विस्तृत डकस्ट्रिङहरू छन्

## आगामी कदमहरू

1. सबै कार्यशाला सत्रहरू क्रमबद्ध रूपमा पूरा गर्नुहोस्
2. विभिन्न मोडेलहरूसँग प्रयोग गर्नुहोस्
3. आफ्नो प्रयोगका लागि नमूनाहरू परिमार्जन गर्नुहोस्

---

**अन्तिम अद्यावधिक**: २०२५-०१-०८  
**कार्यशाला संस्करण**: नवीनतम  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->