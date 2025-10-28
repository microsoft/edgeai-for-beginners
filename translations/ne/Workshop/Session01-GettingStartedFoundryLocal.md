<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:18:07+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ne"
}
-->
# सत्र १: फाउन्ड्री लोकलसँग सुरु गर्दै

## सारांश

Windows 11 मा फाउन्ड्री लोकल स्थापना र कन्फिगर गरेर आफ्नो यात्रा सुरु गर्नुहोस्। CLI सेटअप गर्ने, हार्डवेयर एक्सेलेरेशन सक्षम गर्ने, र मोडेलहरू क्यास गरेर छिटो स्थानीय इनफरेन्स सिक्नुहोस्। यो व्यावहारिक सत्रले Phi, Qwen, DeepSeek, र GPT-OSS-20B जस्ता मोडेलहरू पुन: प्रयोग गर्न मिल्ने CLI कमाण्डहरू प्रयोग गरेर चलाउने प्रक्रिया देखाउँछ।

## सिक्ने उद्देश्यहरू

यो सत्रको अन्त्यसम्म, तपाईं:

- **स्थापना र कन्फिगर गर्नुहोस्**: Windows 11 मा फाउन्ड्री लोकललाई उत्कृष्ट प्रदर्शन सेटिङहरूसँग सेटअप गर्नुहोस्।
- **CLI अपरेशनहरूमा महारत हासिल गर्नुहोस्**: मोडेल व्यवस्थापन र डिप्लोयमेन्टका लागि फाउन्ड्री लोकल CLI प्रयोग गर्नुहोस्।
- **हार्डवेयर एक्सेलेरेशन सक्षम गर्नुहोस्**: ONNXRuntime वा WebGPU प्रयोग गरेर GPU एक्सेलेरेशन कन्फिगर गर्नुहोस्।
- **धेरै मोडेलहरू डिप्लोय गर्नुहोस्**: phi-4, GPT-OSS-20B, Qwen, र DeepSeek मोडेलहरू स्थानीय रूपमा चलाउनुहोस्।
- **आफ्नो पहिलो एप निर्माण गर्नुहोस्**: फाउन्ड्री लोकल Python SDK प्रयोग गरेर विद्यमान नमूनाहरू अनुकूलन गर्नुहोस्।

# मोडेल परीक्षण गर्नुहोस् (गैर-इन्टरएक्टिभ एकल प्रम्प्ट)
foundry model run phi-4-mini --prompt "नमस्ते, आफ्नो बारेमा परिचय दिनुहोस्"

- Windows 11 (22H2 वा पछिल्लो)
# उपलब्ध क्याटलग मोडेलहरूको सूची बनाउनुहोस् (लोड गरिएका मोडेलहरू चलाएपछि देखिन्छन्)
foundry model list
## NOTE: हाल कुनै समर्पित `--running` फ्ल्याग छैन; कुन मोडेलहरू लोड भएका छन् हेर्नको लागि च्याट सुरु गर्नुहोस् वा सेवा लगहरू जाँच गर्नुहोस्।
- Python 3.10+ स्थापना गरिएको
- Visual Studio Code Python एक्सटेन्सनसहित
- स्थापना गर्नका लागि एडमिनिस्ट्रेटर अधिकारहरू

### (वैकल्पिक) वातावरण चरहरू

`.env` बनाउनुहोस् (वा शेलमा सेट गर्नुहोस्) स्क्रिप्टहरू पोर्टेबल बनाउन:
# प्रतिक्रियाहरू तुलना गर्नुहोस् (गैर-इन्टरएक्टिभ)
foundry model run gpt-oss-20b --prompt "सजिलो भाषामा एज AI को व्याख्या गर्नुहोस्"
| Variable | उद्देश्य | उदाहरण |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | मनपर्ने मोडेल उपनाम (क्याटलगले स्वत: उत्कृष्ट भेरियन्ट चयन गर्छ) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | अन्त बिन्दु ओभरराइड गर्नुहोस् (अन्यथा म्यानेजरबाट स्वत: प्राप्त हुन्छ) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | स्ट्रिमिङ डेमो सक्षम गर्नुहोस् | `true` |

> यदि `FOUNDRY_LOCAL_ENDPOINT=auto` (वा सेट नगरिएको) छ भने हामी यसलाई SDK म्यानेजरबाट प्राप्त गर्छौं।

## डेमो फ्लो (३० मिनेट)

### १. फाउन्ड्री लोकल स्थापना गर्नुहोस् र CLI सेटअप प्रमाणित गर्नुहोस् (१० मिनेट)

# क्यास गरिएका मोडेलहरूको सूची बनाउनुहोस्
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (पूर्वावलोकन / यदि समर्थित)**

यदि कुनै देशी macOS प्याकेज प्रदान गरिएको छ (नवीनतमको लागि आधिकारिक डकहरू जाँच गर्नुहोस्):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

यदि macOS देशी बाइनरीहरू उपलब्ध छैनन् भने, तपाईं अझै:
1. Windows 11 ARM/Intel VM (Parallels / UTM) प्रयोग गर्न सक्नुहुन्छ र Windows चरणहरू पालना गर्न सक्नुहुन्छ।
2. कन्टेनर मार्फत मोडेलहरू चलाउनुहोस् (यदि कन्टेनर इमेज प्रकाशित गरिएको छ) र `FOUNDRY_LOCAL_ENDPOINT` सेट गर्नुहोस्।

**Python भर्चुअल वातावरण सिर्जना गर्नुहोस् (क्रस-प्ल्याटफर्म)**

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

pip अपग्रेड गर्नुहोस् र कोर निर्भरता स्थापना गर्नुहोस्:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### चरण १.२: स्थापना प्रमाणित गर्नुहोस्

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### चरण १.३: वातावरण कन्फिगर गर्नुहोस्

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK बुटस्ट्र्यापिङ (सिफारिस गरिएको)

सेवा म्यानुअली सुरु गर्ने र मोडेलहरू चलाउने सट्टा, **फाउन्ड्री लोकल Python SDK** सबै कुरा बुटस्ट्र्याप गर्न सक्छ:

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

यदि तपाईं स्पष्ट नियन्त्रण चाहनुहुन्छ भने, CLI + OpenAI क्लाइन्ट प्रयोग गर्न सक्नुहुन्छ।

### २. मोडेलहरू स्थानीय रूपमा CLI मार्फत चलाउनुहोस् (१० मिनेट)

#### चरण ३.१: Phi-4 मोडेल डिप्लोय गर्नुहोस्

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### चरण ३.२: GPT-OSS-20B डिप्लोय गर्नुहोस्

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### चरण ३.३: थप मोडेलहरू लोड गर्नुहोस्

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### ४. स्टार्टर प्रोजेक्ट: 01-run-phi लाई फाउन्ड्री लोकलका लागि अनुकूलन गर्नुहोस् (५ मिनेट)

#### चरण ४.१: आधारभूत च्याट एप्लिकेसन सिर्जना गर्नुहोस्

`samples/01-foundry-quickstart/chat_quickstart.py` सिर्जना गर्नुहोस् (म्यानेजर प्रयोग गर्न अद्यावधिक गरिएको):

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

#### चरण ४.२: एप्लिकेसन परीक्षण गर्नुहोस्

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## मुख्य अवधारणाहरू समेटिएका

### १. फाउन्ड्री लोकल आर्किटेक्चर

- **स्थानीय इनफरेन्स इन्जिन**: मोडेलहरू पूर्ण रूपमा तपाईंको उपकरणमा चल्छन्।
- **OpenAI SDK अनुकूलता**: विद्यमान OpenAI कोडसँग सहज एकीकरण।
- **मोडेल व्यवस्थापन**: मोडेलहरू डाउनलोड, क्यास, र कुशलतापूर्वक चलाउनुहोस्।
- **हार्डवेयर अनुकूलन**: GPU, NPU, र CPU एक्सेलेरेशन प्रयोग गर्नुहोस्।

### २. CLI कमाण्ड सन्दर्भ

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### ३. Python SDK एकीकरण

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

## सामान्य समस्याहरू समाधान गर्ने

### समस्या १: "फाउन्ड्री कमाण्ड फेला परेन"

**समाधान:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### समस्या २: "मोडेल लोड गर्न असफल भयो"

**समाधान:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### समस्या ३: "localhost:5273 मा कनेक्शन अस्वीकृत"

**समाधान:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## प्रदर्शन अनुकूलन सुझावहरू

### १. मोडेल चयन रणनीति

- **Phi-4-mini**: सामान्य कार्यहरूको लागि उत्कृष्ट, कम मेमोरी प्रयोग।
- **Qwen2.5-0.5b**: छिटो इनफरेन्स, न्यूनतम स्रोतहरू।
- **GPT-OSS-20B**: उच्चतम गुणस्तर, बढी स्रोतहरू आवश्यक।
- **DeepSeek-Coder**: प्रोग्रामिङ कार्यहरूको लागि अनुकूलित।

### २. हार्डवेयर अनुकूलन

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### ३. प्रदर्शन अनुगमन

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

### वैकल्पिक सुधारहरू

| सुधार | के हो | कसरी |
|-------|-------|------|
| साझा उपयोगिताहरू | दोहोरिएको क्लाइन्ट/बुटस्ट्र्याप तर्क हटाउनुहोस् | `Workshop/samples/workshop_utils.py` प्रयोग गर्नुहोस् (`get_client`, `chat_once`) |
| टोकन प्रयोग दृश्यता | लागत/क्षमता सोच सिकाउनुहोस् | `SHOW_USAGE=1` सेट गर्नुहोस् प्रम्प्ट/समाप्ति/कुल टोकन प्रिन्ट गर्न |
| निर्धारणात्मक तुलना | स्थिर बेंचमार्किङ र रिग्रेसन जाँचहरू | `temperature=0`, `top_p=1`, स्थिर प्रम्प्ट पाठ प्रयोग गर्नुहोस् |
| पहिलो-टोकन विलम्बता | प्रतिक्रिया मेट्रिक महसुस गरियो | स्ट्रिमिङ प्रयोग गरेर बेंचमार्क स्क्रिप्ट अनुकूलन गर्नुहोस् (`BENCH_STREAM=1`) |
| अस्थायी त्रुटिहरूमा पुन: प्रयास | चिसो सुरुमा लचिलो डेमो | `RETRY_ON_FAIL=1` (डिफल्ट) र `RETRY_BACKOFF` समायोजन गर्नुहोस् |
| स्मोक परीक्षण | मुख्य प्रवाहहरूमा छिटो स्यानिटी | कार्यशालाको अघि `python Workshop/tests/smoke.py` चलाउनुहोस् |
| मोडेल उपनाम प्रोफाइलहरू | मेसिनहरू बीच मोडेल सेट छिटो परिवर्तन गर्नुहोस् | `.env` राख्नुहोस् `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| क्यासिङ दक्षता | बहु-नमूना चलानमा दोहोरिएको वार्मअपबाट बच्नुहोस् | उपयोगिताहरू क्यास म्यानेजरहरू; स्क्रिप्टहरू/नोटबुकहरूमा पुन: प्रयोग गर्नुहोस् |
| पहिलो रन वार्मअप | p95 विलम्बता स्पाइकहरू घटाउनुहोस् | `FoundryLocalManager` सिर्जना पछि सानो प्रम्प्ट फायर गर्नुहोस् |

निर्धारणात्मक वार्म बेसलाइन उदाहरण (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

तपाईंले दोस्रो रनमा समान आउटपुट र समान टोकन गणना देख्नु पर्छ, निर्धारण पुष्टि गर्दै।

## आगामी चरणहरू

यो सत्र पूरा गरेपछि:

1. **सत्र २ अन्वेषण गर्नुहोस्**: Azure AI Foundry RAG सँग AI समाधानहरू निर्माण गर्नुहोस्।
2. **विभिन्न मोडेलहरू प्रयास गर्नुहोस्**: Qwen, DeepSeek, र अन्य मोडेल परिवारहरू प्रयोग गर्नुहोस्।
3. **प्रदर्शन अनुकूलन गर्नुहोस्**: तपाईंको विशिष्ट हार्डवेयरको लागि सेटिङहरू परिमार्जन गर्नुहोस्।
4. **अनुकूलित एप्लिकेसनहरू निर्माण गर्नुहोस्**: फाउन्ड्री लोकल SDK प्रयोग गरेर आफ्नै प्रोजेक्टहरूमा काम गर्नुहोस्।

## थप स्रोतहरू

### दस्तावेज
- [फाउन्ड्री लोकल Python SDK सन्दर्भ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [फाउन्ड्री लोकल स्थापना गाइड](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [मोडेल क्याटलग](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### नमूना कोड
- [Module08 Sample 01](./samples/01/README.md) - REST च्याट क्विकस्टार्ट
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK एकीकरण
- [Module08 Sample 03](./samples/03/README.md) - मोडेल डिस्कभरी र बेंचमार्किङ

### समुदाय
- [फाउन्ड्री लोकल GitHub छलफलहरू](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI समुदाय](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**सत्र अवधि**: ३० मिनेट व्यावहारिक + १५ मिनेट प्रश्नोत्तर
**कठिनाई स्तर**: प्रारम्भिक
**पूर्वापेक्षाहरू**: Windows 11, Python 3.10+, एडमिनिस्ट्रेटर पहुँच

## नमूना परिदृश्य र कार्यशाला म्यापिङ

| कार्यशाला स्क्रिप्ट / नोटबुक | परिदृश्य | लक्ष्य | उदाहरण इनपुट(हरू) | आवश्यक डाटासेट |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | आन्तरिक IT टोलीले गोपनीयता मूल्यांकन पोर्टलको लागि उपकरणमा इनफरेन्स मूल्यांकन गर्दै | स्थानीय SLM ले मानक प्रम्प्टहरूमा उप-सेकेन्ड विलम्बतामा प्रतिक्रिया दिन्छ भन्ने प्रमाणित गर्नुहोस् | "स्थानीय इनफरेन्सका दुई फाइदाहरू सूचीबद्ध गर्नुहोस्।" | कुनै पनि छैन (एकल प्रम्प्ट) |
| क्विकस्टार्ट अनुकूलन कोड ब्लक | डेभलपरले विद्यमान OpenAI स्क्रिप्टलाई फाउन्ड्री लोकलमा माइग्रेट गर्दै | ड्रप-इन अनुकूलता देखाउनुहोस् | "स्थानीय इनफरेन्सका दुई फाइदाहरू दिनुहोस्।" | केवल इनलाइन प्रम्प्ट |

### परिदृश्य कथा
सुरक्षा र अनुपालन टोलीले संवेदनशील प्रोटोटाइप डाटा स्थानीय रूपमा प्रशोधन गर्न सकिन्छ कि भनेर प्रमाणित गर्नुपर्छ। उनीहरूले बुटस्ट्र्याप स्क्रिप्टलाई विभिन्न प्रम्प्टहरू (गोपनीयता, विलम्बता, लागत) प्रयोग गरेर चलाउँछन् र निर्धारणात्मक `temperature=0` मोड प्रयोग गरेर आधारभूत आउटपुटहरू समात्छन् जुन पछि तुलना गर्न प्रयोग गरिन्छ (सत्र ३ बेंचमार्किङ र सत्र ४ SLM बनाम LLM तुलना)।

### न्यूनतम प्रम्प्ट सेट JSON (वैकल्पिक)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

यो सूची प्रयोग गरेर पुन: प्रयोग गर्न मिल्ने मूल्यांकन लूप सिर्जना गर्नुहोस् वा भविष्यको रिग्रेसन परीक्षण हार्नेसलाई बीज दिनुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।