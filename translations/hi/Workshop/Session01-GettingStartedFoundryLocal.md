<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:16:53+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "hi"
}
-->
# सत्र 1: Foundry Local के साथ शुरुआत करना

## सारांश

Windows 11 पर Foundry Local को इंस्टॉल और कॉन्फ़िगर करके अपनी यात्रा शुरू करें। CLI सेटअप करना, हार्डवेयर एक्सेलेरेशन सक्षम करना, और तेज़ लोकल इनफेरेंस के लिए मॉडल कैश करना सीखें। यह प्रैक्टिकल सत्र Phi, Qwen, DeepSeek, और GPT-OSS-20B जैसे मॉडल को पुनरुत्पादक CLI कमांड्स के माध्यम से चलाने की प्रक्रिया को समझाता है।

## सीखने के उद्देश्य

इस सत्र के अंत तक, आप:

- **इंस्टॉल और कॉन्फ़िगर करें**: Windows 11 पर Foundry Local को उच्चतम प्रदर्शन सेटिंग्स के साथ सेटअप करें
- **CLI संचालन में महारत हासिल करें**: मॉडल प्रबंधन और तैनाती के लिए Foundry Local CLI का उपयोग करें
- **हार्डवेयर एक्सेलेरेशन सक्षम करें**: GPU एक्सेलेरेशन को ONNXRuntime या WebGPU के साथ कॉन्फ़िगर करें
- **कई मॉडल तैनात करें**: phi-4, GPT-OSS-20B, Qwen, और DeepSeek मॉडल को लोकल रूप से चलाएं
- **अपना पहला ऐप बनाएं**: Foundry Local Python SDK का उपयोग करके मौजूदा नमूनों को अनुकूलित करें

# मॉडल का परीक्षण करें (गैर-इंटरैक्टिव सिंगल प्रॉम्प्ट)
foundry model run phi-4-mini --prompt "नमस्ते, अपना परिचय दें"

- Windows 11 (22H2 या बाद का संस्करण)
# उपलब्ध कैटलॉग मॉडल सूचीबद्ध करें (लोड किए गए मॉडल रन के बाद दिखाई देते हैं)
foundry model list
## NOTE: वर्तमान में कोई समर्पित `--running` फ्लैग नहीं है; यह देखने के लिए कि कौन से लोड किए गए हैं, चैट शुरू करें या सेवा लॉग का निरीक्षण करें।
- Python 3.10+ इंस्टॉल किया गया
- Visual Studio Code Python एक्सटेंशन के साथ
- इंस्टॉलेशन के लिए एडमिनिस्ट्रेटर अधिकार

### (वैकल्पिक) पर्यावरण वेरिएबल्स

स्क्रिप्ट को पोर्टेबल बनाने के लिए `.env` बनाएं (या शेल में सेट करें):
# प्रतिक्रियाओं की तुलना करें (गैर-इंटरैक्टिव)
foundry model run gpt-oss-20b --prompt "एज AI को सरल शब्दों में समझाएं"
| वेरिएबल | उद्देश्य | उदाहरण |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | पसंदीदा मॉडल उपनाम (कैटलॉग स्वचालित रूप से सर्वश्रेष्ठ वेरिएंट का चयन करता है) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | एंडपॉइंट ओवरराइड करें (अन्यथा मैनेजर से स्वचालित) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | स्ट्रीमिंग डेमो सक्षम करें | `true` |

> यदि `FOUNDRY_LOCAL_ENDPOINT=auto` (या अनसेट) है तो हम इसे SDK मैनेजर से प्राप्त करते हैं।

## डेमो फ्लो (30 मिनट)

### 1. Foundry Local इंस्टॉल करें और CLI सेटअप सत्यापित करें (10 मिनट)

# कैश किए गए मॉडल सूचीबद्ध करें
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (पूर्वावलोकन / यदि समर्थित)**

यदि कोई नेटिव macOS पैकेज प्रदान किया गया है (नवीनतम के लिए आधिकारिक दस्तावेज़ देखें):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

यदि macOS नेटिव बायनरी अभी उपलब्ध नहीं हैं, तो आप अभी भी:
1. Windows 11 ARM/Intel VM (Parallels / UTM) का उपयोग करें और Windows चरणों का पालन करें।
2. कंटेनर के माध्यम से मॉडल चलाएं (यदि कंटेनर इमेज प्रकाशित की गई है) और `FOUNDRY_LOCAL_ENDPOINT` को एक्सपोज़ पोर्ट पर सेट करें।

**Python वर्चुअल एनवायरनमेंट बनाएं (क्रॉस-प्लेटफ़ॉर्म)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pip को अपग्रेड करें और कोर डिपेंडेंसी इंस्टॉल करें:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### चरण 1.2: इंस्टॉलेशन सत्यापित करें

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### चरण 1.3: पर्यावरण कॉन्फ़िगर करें

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK बूटस्ट्रैपिंग (अनुशंसित)

सेवा को मैन्युअल रूप से शुरू करने और मॉडल चलाने के बजाय, **Foundry Local Python SDK** सब कुछ बूटस्ट्रैप कर सकता है:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

यदि आप स्पष्ट नियंत्रण पसंद करते हैं तो आप CLI + OpenAI क्लाइंट का उपयोग कर सकते हैं जैसा कि बाद में दिखाया गया है।

### 2. CLI के माध्यम से लोकल मॉडल चलाएं (10 मिनट)

#### चरण 3.1: Phi-4 मॉडल तैनात करें

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### चरण 3.2: GPT-OSS-20B तैनात करें

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### चरण 3.3: अतिरिक्त मॉडल लोड करें

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. स्टार्टर प्रोजेक्ट: Foundry Local के लिए 01-run-phi को अनुकूलित करें (5 मिनट)

#### चरण 4.1: बेसिक चैट एप्लिकेशन बनाएं

`samples/01-foundry-quickstart/chat_quickstart.py` बनाएं (यदि उपलब्ध हो तो मैनेजर का उपयोग करने के लिए अपडेट किया गया):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### चरण 4.2: एप्लिकेशन का परीक्षण करें

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## मुख्य अवधारणाएं शामिल

### 1. Foundry Local आर्किटेक्चर

- **लोकल इनफेरेंस इंजन**: मॉडल को पूरी तरह से आपके डिवाइस पर चलाता है
- **OpenAI SDK संगतता**: मौजूदा OpenAI कोड के साथ सहज एकीकरण
- **मॉडल प्रबंधन**: कई मॉडलों को कुशलतापूर्वक डाउनलोड, कैश और चलाएं
- **हार्डवेयर अनुकूलन**: GPU, NPU, और CPU एक्सेलेरेशन का लाभ उठाएं

### 2. CLI कमांड संदर्भ

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK एकीकरण

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## सामान्य समस्याओं का समाधान

### समस्या 1: "Foundry कमांड नहीं मिला"

**समाधान:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### समस्या 2: "मॉडल लोड करने में विफल"

**समाधान:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### समस्या 3: "localhost:5273 पर कनेक्शन अस्वीकृत"

**समाधान:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## प्रदर्शन अनुकूलन युक्तियाँ

### 1. मॉडल चयन रणनीति

- **Phi-4-mini**: सामान्य कार्यों के लिए सर्वश्रेष्ठ, कम मेमोरी उपयोग
- **Qwen2.5-0.5b**: सबसे तेज़ इनफेरेंस, न्यूनतम संसाधन
- **GPT-OSS-20B**: उच्चतम गुणवत्ता, अधिक संसाधनों की आवश्यकता
- **DeepSeek-Coder**: प्रोग्रामिंग कार्यों के लिए अनुकूलित

### 2. हार्डवेयर अनुकूलन

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. प्रदर्शन की निगरानी

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### वैकल्पिक सुधार

| सुधार | क्या | कैसे |
|-------|-----|-----|
| साझा उपयोगिताएँ | डुप्लिकेट क्लाइंट/बूटस्ट्रैप लॉजिक हटाएं | `Workshop/samples/workshop_utils.py` का उपयोग करें (`get_client`, `chat_once`) |
| टोकन उपयोग दृश्यता | लागत/क्षमता सोच को जल्दी सिखाएं | `SHOW_USAGE=1` सेट करें ताकि प्रॉम्प्ट/कम्प्लीशन/कुल टोकन प्रिंट हो सकें |
| निर्धारक तुलना | स्थिर बेंचमार्किंग और रिग्रेशन जांच | `temperature=0`, `top_p=1`, सुसंगत प्रॉम्प्ट टेक्स्ट का उपयोग करें |
| पहला-टोकन विलंबता | उत्तरदायीता मीट्रिक का अनुभव | स्ट्रीमिंग के साथ बेंचमार्क स्क्रिप्ट को अनुकूलित करें (`BENCH_STREAM=1`) |
| अस्थायी त्रुटियों पर पुनः प्रयास | ठंडे स्टार्ट पर लचीले डेमो | `RETRY_ON_FAIL=1` (डिफ़ॉल्ट) और `RETRY_BACKOFF` समायोजित करें |
| स्मोक टेस्टिंग | प्रमुख प्रवाहों में त्वरित जांच | कार्यशाला से पहले `python Workshop/tests/smoke.py` चलाएं |
| मॉडल उपनाम प्रोफाइल | मशीनों के बीच मॉडल सेट को जल्दी से बदलें | `.env` बनाए रखें `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` के साथ |
| कैशिंग दक्षता | मल्टी-सैंपल रन में बार-बार वार्मअप से बचें | उपयोगिताएँ कैश मैनेजर; स्क्रिप्ट/नोटबुक्स में पुन: उपयोग करें |
| पहला रन वार्मअप | p95 विलंबता स्पाइक्स को कम करें | `FoundryLocalManager` निर्माण के बाद एक छोटा प्रॉम्प्ट फायर करें |

निर्धारक वार्म बेसलाइन का उदाहरण (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

आपको समान आउटपुट और दूसरे रन पर समान टोकन काउंट्स दिखाई देने चाहिए, जो निर्धारकता की पुष्टि करता है।

## अगले कदम

इस सत्र को पूरा करने के बाद:

1. **सत्र 2 का अन्वेषण करें**: Azure AI Foundry RAG के साथ AI समाधान बनाएं
2. **विभिन्न मॉडलों को आज़माएं**: Qwen, DeepSeek, और अन्य मॉडल परिवारों के साथ प्रयोग करें
3. **प्रदर्शन अनुकूलित करें**: अपने विशिष्ट हार्डवेयर के लिए सेटिंग्स को फाइन-ट्यून करें
4. **कस्टम एप्लिकेशन बनाएं**: अपने प्रोजेक्ट्स में Foundry Local SDK का उपयोग करें

## अतिरिक्त संसाधन

### दस्तावेज़
- [Foundry Local Python SDK संदर्भ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local इंस्टॉलेशन गाइड](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [मॉडल कैटलॉग](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### नमूना कोड
- [Module08 Sample 01](./samples/01/README.md) - REST चैट क्विकस्टार्ट
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK एकीकरण
- [Module08 Sample 03](./samples/03/README.md) - मॉडल डिस्कवरी और बेंचमार्किंग

### समुदाय
- [Foundry Local GitHub चर्चाएँ](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI समुदाय](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**सत्र अवधि**: 30 मिनट प्रैक्टिकल + 15 मिनट प्रश्नोत्तर
**कठिनाई स्तर**: शुरुआती
**पूर्वापेक्षाएँ**: Windows 11, Python 3.10+, एडमिनिस्ट्रेटर एक्सेस

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला स्क्रिप्ट / नोटबुक | परिदृश्य | लक्ष्य | उदाहरण इनपुट(s) | आवश्यक डेटासेट |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | ऑन-डिवाइस इनफेरेंस का मूल्यांकन करने वाली आंतरिक आईटी टीम के लिए गोपनीयता मूल्यांकन पोर्टल | स्थानीय SLM को मान्य करें कि मानक प्रॉम्प्ट पर उप-सेकंड विलंबता के भीतर प्रतिक्रिया देता है | "स्थानीय इनफेरेंस के दो लाभ सूचीबद्ध करें।" | कोई नहीं (सिंगल प्रॉम्प्ट) |
| क्विकस्टार्ट अनुकूलन कोड ब्लॉक | डेवलपर जो मौजूदा OpenAI स्क्रिप्ट को Foundry Local में माइग्रेट कर रहा है | ड्रॉप-इन संगतता दिखाएं | "स्थानीय इनफेरेंस के दो लाभ दें।" | केवल इनलाइन प्रॉम्प्ट |

### परिदृश्य कथा
सुरक्षा और अनुपालन टीम को मान्य करना होगा कि संवेदनशील प्रोटोटाइप डेटा को लोकल रूप से संसाधित किया जा सकता है। वे बूटस्ट्रैप स्क्रिप्ट को कई प्रॉम्प्ट (गोपनीयता, विलंबता, लागत) के साथ चलाते हैं, निर्धारक `temperature=0` मोड का उपयोग करके बेसलाइन आउटपुट को बाद की तुलना के लिए कैप्चर करते हैं (सत्र 3 बेंचमार्किंग और सत्र 4 SLM बनाम LLM कंट्रास्ट)।

### न्यूनतम प्रॉम्प्ट सेट JSON (वैकल्पिक)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

इस सूची का उपयोग पुनरुत्पादक मूल्यांकन लूप बनाने या भविष्य के रिग्रेशन टेस्ट हार्नेस को बीज देने के लिए करें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।