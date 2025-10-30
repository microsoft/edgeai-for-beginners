<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T21:11:32+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "mr"
}
-->
# पर्यावरण कॉन्फिगरेशन मार्गदर्शक

## आढावा

वर्कशॉप नमुने कॉन्फिगरेशनसाठी पर्यावरणीय व्हेरिएबल्स वापरतात, जे रिपॉझिटरीच्या मूळ `.env` फाइलमध्ये केंद्रीकृत आहेत. यामुळे कोड बदलल्याशिवाय सुलभ सानुकूलन शक्य होते.

## जलद प्रारंभ

### 1. पूर्वअटी सत्यापित करा

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. पर्यावरण कॉन्फिगर करा

`.env` फाइल आधीच योग्य डीफॉल्ट्ससह कॉन्फिगर केलेली आहे. बहुतेक वापरकर्त्यांना काहीही बदलण्याची गरज नाही.

**ऐच्छिक**: सेटिंग्ज पुनरावलोकन करा आणि सानुकूलित करा:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. कॉन्फिगरेशन लागू करा

**पायथन स्क्रिप्टसाठी:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**नोटबुकसाठी:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## पर्यावरणीय व्हेरिएबल्स संदर्भ

### मुख्य कॉन्फिगरेशन

| व्हेरिएबल | डीफॉल्ट | वर्णन |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | नमुन्यांसाठी डीफॉल्ट मॉडेल |
| `FOUNDRY_LOCAL_ENDPOINT` | (रिक्त) | सेवा एंडपॉइंट ओव्हरराइड करा |
| `PYTHONPATH` | वर्कशॉप पथ | पायथन मॉड्यूल शोध पथ |

**FOUNDRY_LOCAL_ENDPOINT कधी सेट करावे:**
- रिमोट फाउंड्री लोकल इंस्टन्स
- कस्टम पोर्ट कॉन्फिगरेशन
- विकास/उत्पादन वेगळे करणे

**उदाहरण:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### सत्र-विशिष्ट व्हेरिएबल्स

#### सत्र 02: RAG पाइपलाइन
| व्हेरिएबल | डीफॉल्ट | उद्देश |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिंग मॉडेल |
| `RAG_QUESTION` | पूर्व-कॉन्फिगर केलेले | चाचणी प्रश्न |

#### सत्र 03: बेंचमार्किंग
| व्हेरिएबल | डीफॉल्ट | उद्देश |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | बेंचमार्कसाठी मॉडेल्स |
| `BENCH_ROUNDS` | `3` | प्रत्येक मॉडेलसाठी पुनरावृत्ती |
| `BENCH_PROMPT` | पूर्व-कॉन्फिगर केलेले | चाचणी प्रॉम्प्ट |
| `BENCH_STREAM` | `0` | पहिल्या टोकनची विलंबता मोजा |

#### सत्र 04: मॉडेल तुलना
| व्हेरिएबल | डीफॉल्ट | उद्देश |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | लहान भाषा मॉडेल |
| `LLM_ALIAS` | `qwen2.5-7b` | मोठे भाषा मॉडेल |
| `COMPARE_PROMPT` | पूर्व-कॉन्फिगर केलेले | तुलना प्रॉम्प्ट |
| `COMPARE_RETRIES` | `2` | पुन्हा प्रयत्न करण्याचे वेळा |

#### सत्र 05: मल्टी-एजंट ऑर्केस्ट्रेशन
| व्हेरिएबल | डीफॉल्ट | उद्देश |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | संशोधक एजंट मॉडेल |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | संपादक एजंट मॉडेल |
| `AGENT_QUESTION` | पूर्व-कॉन्फिगर केलेले | चाचणी प्रश्न |

### विश्वसनीयता कॉन्फिगरेशन

| व्हेरिएबल | डीफॉल्ट | उद्देश |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | टोकन वापर प्रिंट करा |
| `RETRY_ON_FAIL` | `1` | पुन्हा प्रयत्न लॉजिक सक्षम करा |
| `RETRY_BACKOFF` | `1.0` | पुन्हा प्रयत्न विलंब (सेकंद) |

## सामान्य कॉन्फिगरेशन्स

### विकास सेटअप (जलद पुनरावृत्ती)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### उत्पादन सेटअप (गुणवत्ता लक्ष केंद्रित)
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

### मल्टी-एजंट स्पेशलायझेशन
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### रिमोट विकास
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## शिफारस केलेली मॉडेल्स

### वापर प्रकरणानुसार

**सामान्य उद्देश:**
- `phi-4-mini` - गुणवत्ता आणि गती यामध्ये संतुलन

**जलद प्रतिसाद:**
- `qwen2.5-0.5b` - खूप जलद, वर्गीकरणासाठी चांगले
- `phi-4-mini` - चांगल्या गुणवत्तेसह जलद

**उच्च गुणवत्ता:**
- `qwen2.5-7b` - सर्वोत्तम गुणवत्ता, उच्च संसाधन वापर
- `phi-4-mini` - चांगली गुणवत्ता, कमी संसाधने

**कोड जनरेशन:**
- `deepseek-coder-1.3b` - कोडसाठी विशेषीकृत
- `phi-4-mini` - सामान्य उद्देश कोडिंग

### संसाधन उपलब्धतेनुसार

**कमी संसाधने (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**मध्यम संसाधने (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**उच्च संसाधने (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## प्रगत कॉन्फिगरेशन

### कस्टम एंडपॉइंट्स

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### तापमान आणि सॅम्पलिंग (कोडमध्ये ओव्हरराइड करा)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI हायब्रिड सेटअप

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## समस्या निवारण

### पर्यावरणीय व्हेरिएबल्स लोड झाले नाहीत

**लक्षणे:**
- स्क्रिप्ट चुकीची मॉडेल्स वापरतात
- कनेक्शन त्रुटी
- व्हेरिएबल्स ओळखले जात नाहीत

**उपाय:**
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

### सेवा कनेक्शन समस्या

**लक्षणे:**
- "कनेक्शन नाकारले" त्रुटी
- "सेवा उपलब्ध नाही"
- टाइमआउट त्रुटी

**उपाय:**
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

### मॉडेल सापडले नाही

**लक्षणे:**
- "मॉडेल सापडले नाही" त्रुटी
- "अलियास ओळखला गेला नाही"

**उपाय:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### आयात त्रुटी

**लक्षणे:**
- "मॉड्यूल सापडले नाही" त्रुटी

**उपाय:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## कॉन्फिगरेशन चाचणी

### पर्यावरण लोडिंग सत्यापित करा

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

### फाउंड्री लोकल कनेक्शन चाचणी करा

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

## सुरक्षा सर्वोत्तम पद्धती

### 1. कधीही गुपिते कमिट करू नका

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. वेगळ्या .env फाइल्स वापरा

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API कीज फिरवा

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. पर्यावरण-विशिष्ट कॉन्फिग वापरा

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK दस्तऐवजीकरण

- **मुख्य रिपॉझिटरी**: https://github.com/microsoft/Foundry-Local
- **पायथन SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API दस्तऐवजीकरण**: नवीनतमसाठी SDK रिपॉझिटरी तपासा

## अतिरिक्त संसाधने

- `QUICK_START.md` - सुरुवातीसाठी मार्गदर्शक
- `SDK_MIGRATION_NOTES.md` - SDK अद्यतन तपशील
- `Workshop/samples/*/README.md` - नमुना-विशिष्ट मार्गदर्शक

---

**शेवटचे अद्यतन**: 2025-01-08  
**आवृत्ती**: 2.0  
**SDK**: फाउंड्री लोकल पायथन SDK (नवीनतम)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.