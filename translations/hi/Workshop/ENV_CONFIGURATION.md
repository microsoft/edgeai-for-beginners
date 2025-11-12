<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T22:15:17+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "hi"
}
-->
# पर्यावरण कॉन्फ़िगरेशन गाइड

## अवलोकन

वर्कशॉप नमूने पर्यावरण वेरिएबल्स का उपयोग कॉन्फ़िगरेशन के लिए करते हैं, जो रिपॉजिटरी रूट में `.env` फ़ाइल में केंद्रीकृत हैं। यह कोड को संशोधित किए बिना आसान अनुकूलन की अनुमति देता है।

## त्वरित शुरुआत

### 1. आवश्यकताओं की पुष्टि करें

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. पर्यावरण कॉन्फ़िगर करें

`.env` फ़ाइल पहले से ही समझदारी से डिफ़ॉल्ट सेटिंग्स के साथ कॉन्फ़िगर की गई है। अधिकांश उपयोगकर्ताओं को कुछ भी बदलने की आवश्यकता नहीं होगी।

**वैकल्पिक**: सेटिंग्स की समीक्षा करें और अनुकूलित करें:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. कॉन्फ़िगरेशन लागू करें

**पायथन स्क्रिप्ट्स के लिए:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**नोटबुक्स के लिए:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## पर्यावरण वेरिएबल्स संदर्भ

### मुख्य कॉन्फ़िगरेशन

| वेरिएबल | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | नमूनों के लिए डिफ़ॉल्ट मॉडल |
| `FOUNDRY_LOCAL_ENDPOINT` | (खाली) | सेवा एंडपॉइंट ओवरराइड करें |
| `PYTHONPATH` | वर्कशॉप पथ | पायथन मॉड्यूल खोज पथ |

**जब FOUNDRY_LOCAL_ENDPOINT सेट करें:**
- रिमोट Foundry Local इंस्टेंस
- कस्टम पोर्ट कॉन्फ़िगरेशन
- विकास/उत्पादन अलगाव

**उदाहरण:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### सत्र-विशिष्ट वेरिएबल्स

#### सत्र 02: RAG पाइपलाइन
| वेरिएबल | डिफ़ॉल्ट | उद्देश्य |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिंग मॉडल |
| `RAG_QUESTION` | पूर्व-कॉन्फ़िगर | परीक्षण प्रश्न |

#### सत्र 03: बेंचमार्किंग
| वेरिएबल | डिफ़ॉल्ट | उद्देश्य |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | बेंचमार्क करने के लिए मॉडल |
| `BENCH_ROUNDS` | `3` | प्रति मॉडल पुनरावृत्तियाँ |
| `BENCH_PROMPT` | पूर्व-कॉन्फ़िगर | परीक्षण प्रॉम्प्ट |
| `BENCH_STREAM` | `0` | पहले-टोकन विलंबता मापें |

#### सत्र 04: मॉडल तुलना
| वेरिएबल | डिफ़ॉल्ट | उद्देश्य |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | छोटा भाषा मॉडल |
| `LLM_ALIAS` | `qwen2.5-7b` | बड़ा भाषा मॉडल |
| `COMPARE_PROMPT` | पूर्व-कॉन्फ़िगर | तुलना प्रॉम्प्ट |
| `COMPARE_RETRIES` | `2` | पुनः प्रयास |

#### सत्र 05: मल्टी-एजेंट ऑर्केस्ट्रेशन
| वेरिएबल | डिफ़ॉल्ट | उद्देश्य |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | शोधकर्ता एजेंट मॉडल |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | संपादक एजेंट मॉडल |
| `AGENT_QUESTION` | पूर्व-कॉन्फ़िगर | परीक्षण प्रश्न |

### विश्वसनीयता कॉन्फ़िगरेशन

| वेरिएबल | डिफ़ॉल्ट | उद्देश्य |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | टोकन उपयोग प्रिंट करें |
| `RETRY_ON_FAIL` | `1` | पुनः प्रयास लॉजिक सक्षम करें |
| `RETRY_BACKOFF` | `1.0` | पुनः प्रयास विलंब (सेकंड) |

## सामान्य कॉन्फ़िगरेशन

### विकास सेटअप (तेज़ पुनरावृत्ति)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### उत्पादन सेटअप (गुणवत्ता पर ध्यान केंद्रित)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### बेंचमार्किंग सेटअप
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### मल्टी-एजेंट विशेषज्ञता
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### रिमोट विकास
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## अनुशंसित मॉडल

### उपयोग के मामले के अनुसार

**सामान्य उद्देश्य:**
- `phi-4-mini` - गुणवत्ता और गति का संतुलन

**तेज़ प्रतिक्रियाएँ:**
- `qwen2.5-0.5b` - बहुत तेज़, वर्गीकरण के लिए अच्छा
- `phi-4-mini` - तेज़ और अच्छी गुणवत्ता

**उच्च गुणवत्ता:**
- `qwen2.5-7b` - सर्वोत्तम गुणवत्ता, उच्च संसाधन उपयोग
- `phi-4-mini` - अच्छी गुणवत्ता, कम संसाधन

**कोड जनरेशन:**
- `deepseek-coder-1.3b` - कोड के लिए विशेष
- `phi-4-mini` - सामान्य उद्देश्य कोडिंग

### संसाधन उपलब्धता के अनुसार

**कम संसाधन (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**मध्यम संसाधन (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**उच्च संसाधन (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## उन्नत कॉन्फ़िगरेशन

### कस्टम एंडपॉइंट्स

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### तापमान और सैंपलिंग (कोड में ओवरराइड करें)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI हाइब्रिड सेटअप

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## समस्या निवारण

### पर्यावरण वेरिएबल्स लोड नहीं हुए

**लक्षण:**
- स्क्रिप्ट्स गलत मॉडल का उपयोग करती हैं
- कनेक्शन त्रुटियाँ
- वेरिएबल्स मान्यता प्राप्त नहीं

**समाधान:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### सेवा कनेक्शन समस्याएँ

**लक्षण:**
- "कनेक्शन अस्वीकृत" त्रुटियाँ
- "सेवा उपलब्ध नहीं"
- टाइमआउट त्रुटियाँ

**समाधान:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### मॉडल नहीं मिला

**लक्षण:**
- "मॉडल नहीं मिला" त्रुटियाँ
- "उपनाम मान्यता प्राप्त नहीं"

**समाधान:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### आयात त्रुटियाँ

**लक्षण:**
- "मॉड्यूल नहीं मिला" त्रुटियाँ

**समाधान:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन परीक्षण

### पर्यावरण लोडिंग सत्यापित करें

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Foundry Local कनेक्शन परीक्षण करें

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## सुरक्षा सर्वोत्तम प्रथाएँ

### 1. कभी भी गुप्त जानकारी कमिट न करें

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. अलग-अलग .env फ़ाइलों का उपयोग करें

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API कुंजियों को घुमाएँ

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. पर्यावरण-विशिष्ट कॉन्फ़िगरेशन का उपयोग करें

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK दस्तावेज़ीकरण

- **मुख्य रिपॉजिटरी**: https://github.com/microsoft/Foundry-Local
- **पायथन SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API दस्तावेज़ीकरण**: नवीनतम के लिए SDK रिपॉजिटरी देखें

## अतिरिक्त संसाधन

- `QUICK_START.md` - शुरुआत गाइड
- `Workshop/samples/*/README.md` - नमूना-विशिष्ट गाइड

---

**अंतिम अपडेट**: 2025-01-08  
**संस्करण**: 2.0  
**SDK**: Foundry Local Python SDK (नवीनतम)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->