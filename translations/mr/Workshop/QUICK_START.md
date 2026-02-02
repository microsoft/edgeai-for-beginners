# कार्यशाळा जलद प्रारंभ मार्गदर्शक

## पूर्वतयारी

### 1. फाउंड्री लोकल स्थापित करा

अधिकृत स्थापना मार्गदर्शकाचे अनुसरण करा:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python Dependencies स्थापित करा

कार्यशाळा डिरेक्टरीमधून:

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

## कार्यशाळा नमुने चालवणे

### सत्र 01: मूलभूत चॅट

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**पर्यावरण व्हेरिएबल्स:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### सत्र 02: RAG पाइपलाइन

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**पर्यावरण व्हेरिएबल्स:**
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

**टीप**: `requirements.txt` द्वारे अतिरिक्त dependencies स्थापित करणे आवश्यक आहे

### सत्र 03: बेंचमार्किंग

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**पर्यावरण व्हेरिएबल्स:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**आउटपुट**: विलंब, थ्रूपुट, आणि पहिल्या टोकन मेट्रिक्ससह JSON

### सत्र 04: मॉडेल तुलना

```bash
cd Workshop/samples
python -m session04.model_compare
```

**पर्यावरण व्हेरिएबल्स:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### सत्र 05: मल्टी-एजंट ऑर्केस्ट्रेशन

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**पर्यावरण व्हेरिएबल्स:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### सत्र 06: मॉडेल राउटर

```bash
cd Workshop/samples
python -m session06.models_router
```

**राउटिंग लॉजिकची चाचणी** अनेक हेतूंसाठी (कोड, सारांश, वर्गीकरण)

### सत्र 06: पाइपलाइन

```bash
python -m session06.models_pipeline
```

**जटिल मल्टी-स्टेप पाइपलाइन** नियोजन, अंमलबजावणी, आणि सुधारणा यासह

## स्क्रिप्ट्स

### बेंचमार्क रिपोर्ट निर्यात करा

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**आउटपुट**: Markdown टेबल + JSON मेट्रिक्स

### Markdown CLI पॅटर्न्स लिंट करा

```bash
python lint_markdown_cli.py --verbose
```

**उद्देश**: दस्तऐवजामध्ये कालबाह्य CLI पॅटर्न्स शोधा

## चाचणी

### स्मोक चाचण्या

```bash
cd Workshop
python -m tests.smoke
```

**चाचण्या**: मुख्य नमुन्यांची मूलभूत कार्यक्षमता

## समस्या निवारण

### सेवा चालू नाही

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### मॉड्यूल आयात त्रुटी

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### कनेक्शन त्रुटी

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### मॉडेल सापडले नाही

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## पर्यावरण व्हेरिएबल संदर्भ

### कोर कॉन्फिगरेशन
| व्हेरिएबल | डीफॉल्ट | वर्णन |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | बदलते | वापरण्यासाठी मॉडेल उपनाम |
| `FOUNDRY_LOCAL_ENDPOINT` | ऑटो | सेवा endpoint ओव्हरराइड करा |
| `SHOW_USAGE` | `0` | टोकन वापर आकडेवारी दर्शवा |
| `RETRY_ON_FAIL` | `1` | पुनर्प्रयत्न लॉजिक सक्षम करा |
| `RETRY_BACKOFF` | `1.0` | प्रारंभिक पुनर्प्रयत्न विलंब (सेकंद) |

### सत्र-विशिष्ट
| व्हेरिएबल | डीफॉल्ट | वर्णन |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिंग मॉडेल |
| `RAG_QUESTION` | नमुना पहा | RAG चाचणी प्रश्न |
| `BENCH_MODELS` | बदलते | अल्पविरामाने वेगळे केलेले मॉडेल्स |
| `BENCH_ROUNDS` | `3` | बेंचमार्क पुनरावृत्ती |
| `BENCH_PROMPT` | नमुना पहा | बेंचमार्क प्रॉम्प्ट |
| `BENCH_STREAM` | `0` | पहिल्या टोकन विलंब मोजा |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | प्राथमिक एजंट मॉडेल |
| `AGENT_MODEL_EDITOR` | प्राथमिक | संपादक एजंट मॉडेल |
| `SLM_ALIAS` | `phi-4-mini` | लहान भाषा मॉडेल |
| `LLM_ALIAS` | `qwen2.5-7b` | मोठे भाषा मॉडेल |
| `COMPARE_PROMPT` | नमुना पहा | तुलना प्रॉम्प्ट |

## शिफारस केलेली मॉडेल्स

### विकास आणि चाचणी
- **phi-4-mini** - गुणवत्ता आणि गती यामध्ये संतुलित
- **qwen2.5-0.5b** - वर्गीकरणासाठी अतिशय जलद
- **gemma-2-2b** - चांगली गुणवत्ता, मध्यम गती

### उत्पादन परिस्थिती
- **phi-4-mini** - सामान्य उद्देश
- **deepseek-coder-1.3b** - कोड जनरेशन
- **qwen2.5-7b** - उच्च गुणवत्ता प्रतिसाद

## SDK दस्तऐवज

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## मदत मिळवणे

1. सेवा स्थिती तपासा: `foundry service status`
2. लॉग पहा: Foundry Local सेवा लॉग तपासा
3. SDK दस्तऐवज तपासा: https://github.com/microsoft/Foundry-Local
4. नमुना कोड पुनरावलोकन करा: सर्व नमुन्यांमध्ये तपशीलवार docstrings आहेत

## पुढील पायऱ्या

1. सर्व कार्यशाळा सत्रे क्रमाने पूर्ण करा
2. वेगवेगळ्या मॉडेल्ससह प्रयोग करा
3. तुमच्या उपयोग प्रकरणांसाठी नमुने सुधारित करा

---

**शेवटचे अद्यतन**: 2025-01-08  
**कार्यशाळा आवृत्ती**: नवीनतम  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->