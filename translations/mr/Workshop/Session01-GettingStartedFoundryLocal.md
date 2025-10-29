<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:12:27+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "mr"
}
-->
# सत्र 1: Foundry Local सह सुरुवात करा

## सारांश

Windows 11 वर Foundry Local स्थापित करून आणि कॉन्फिगर करून तुमचा प्रवास सुरू करा. CLI सेटअप कसे करायचे, हार्डवेअर प्रवेग सक्षम कसा करायचा आणि जलद स्थानिक अनुमानासाठी मॉडेल्स कॅशे कसे करायचे ते शिका. हे प्रात्यक्षिक सत्र Phi, Qwen, DeepSeek आणि GPT-OSS-20B सारख्या मॉडेल्स चालवण्यासाठी पुनरुत्पादक CLI आदेशांद्वारे मार्गदर्शन करते.

## शिकण्याची उद्दिष्टे

या सत्राच्या शेवटी, तुम्ही:

- **स्थापना आणि कॉन्फिगरेशन**: Windows 11 वर Foundry Local सेट करा आणि कार्यक्षमतेसाठी सर्वोत्तम सेटिंग्ज वापरा
- **CLI ऑपरेशन्समध्ये प्रावीण्य मिळवा**: मॉडेल व्यवस्थापन आणि तैनातीसाठी Foundry Local CLI वापरा
- **हार्डवेअर प्रवेग सक्षम करा**: ONNXRuntime किंवा WebGPU सह GPU प्रवेग कॉन्फिगर करा
- **अनेक मॉडेल्स तैनात करा**: phi-4, GPT-OSS-20B, Qwen आणि DeepSeek मॉडेल्स स्थानिक स्तरावर चालवा
- **तुमचा पहिला अ‍ॅप तयार करा**: विद्यमान नमुन्यांना Foundry Local Python SDK वापरण्यासाठी अनुकूल करा

# मॉडेल चाचणी करा (नॉन-इंटरएक्टिव सिंगल प्रॉम्प्ट)
foundry model run phi-4-mini --prompt "नमस्कार, स्वतःची ओळख करून द्या"

- Windows 11 (22H2 किंवा नंतरचे)
# उपलब्ध कॅटलॉग मॉडेल्स सूचीबद्ध करा (लोड केलेली मॉडेल्स चालवल्यानंतर दिसतील)
foundry model list
## NOTE: सध्या समर्पित `--running` फ्लॅग नाही; कोणती मॉडेल्स लोड झाली आहेत हे पाहण्यासाठी चॅट सुरू करा किंवा सेवा लॉग तपासा.
- Python 3.10+ स्थापित
- Visual Studio Code Python विस्तारासह
- स्थापनेसाठी प्रशासक विशेषाधिकार

### (पर्यायी) पर्यावरणीय व्हेरिएबल्स

स्क्रिप्ट्स पोर्टेबल बनवण्यासाठी `.env` तयार करा (किंवा शेलमध्ये सेट करा):
# प्रतिसादांची तुलना करा (नॉन-इंटरएक्टिव)
foundry model run gpt-oss-20b --prompt "एज AI सोप्या शब्दांत समजावून सांगा"
| व्हेरिएबल | उद्देश | उदाहरण |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | प्राधान्य दिलेला मॉडेल उपनाम (कॅटलॉग सर्वोत्तम प्रकार निवडतो) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | एंडपॉइंट ओव्हरराइड करा (अन्यथा व्यवस्थापकाकडून स्वयंचलित) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | स्ट्रीमिंग डेमो सक्षम करा | `true` |

> जर `FOUNDRY_LOCAL_ENDPOINT=auto` (किंवा सेट केलेले नाही) असेल तर आम्ही ते SDK व्यवस्थापकाकडून प्राप्त करतो.

## डेमो फ्लो (30 मिनिटे)

### 1. Foundry Local स्थापित करा आणि CLI सेटअप सत्यापित करा (10 मिनिटे)

# कॅशे केलेली मॉडेल्स सूचीबद्ध करा
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (पूर्वावलोकन / जर समर्थित असेल)**

जर मूळ macOS पॅकेज प्रदान केले असेल (नवीनतमसाठी अधिकृत दस्तऐवज तपासा):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

जर macOS मूळ बायनरी अद्याप उपलब्ध नसतील, तर तुम्ही:
1. Windows 11 ARM/Intel VM (Parallels / UTM) वापरू शकता आणि Windows चरणांचे अनुसरण करू शकता.
2. कंटेनरद्वारे मॉडेल्स चालवा (जर कंटेनर प्रतिमा प्रकाशित केली असेल) आणि `FOUNDRY_LOCAL_ENDPOINT` उघडलेल्या पोर्टवर सेट करा.

**Python व्हर्च्युअल एन्व्हायर्नमेंट तयार करा (क्रॉस-प्लॅटफॉर्म)**

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

pip अपग्रेड करा आणि मुख्य अवलंबित्व स्थापित करा:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### चरण 1.2: स्थापना सत्यापित करा

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### चरण 1.3: पर्यावरण कॉन्फिगर करा

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK बूटस्ट्रॅपिंग (शिफारस केलेले)

सेवा मॅन्युअली सुरू करण्याऐवजी आणि मॉडेल्स चालवण्याऐवजी, **Foundry Local Python SDK** सर्वकाही बूटस्ट्रॅप करू शकते:

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

जर तुम्हाला स्पष्ट नियंत्रण हवे असेल तर तुम्ही CLI + OpenAI क्लायंट वापरू शकता, जसे नंतर दाखवले आहे.

### 2. CLI द्वारे स्थानिक स्तरावर मॉडेल्स चालवा (10 मिनिटे)

#### चरण 3.1: Phi-4 मॉडेल तैनात करा

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### चरण 3.2: GPT-OSS-20B तैनात करा

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### चरण 3.3: अतिरिक्त मॉडेल्स लोड करा

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. स्टार्टर प्रोजेक्ट: Foundry Local साठी 01-run-phi अनुकूल करा (5 मिनिटे)

#### चरण 4.1: मूलभूत चॅट अ‍ॅप्लिकेशन तयार करा

`samples/01-foundry-quickstart/chat_quickstart.py` तयार करा (जर व्यवस्थापक उपलब्ध असेल तर अद्यतनित करा):

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

#### चरण 4.2: अ‍ॅप्लिकेशन चाचणी करा

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## मुख्य संकल्पना समाविष्ट

### 1. Foundry Local आर्किटेक्चर

- **स्थानिक अनुमान इंजिन**: मॉडेल्स पूर्णपणे तुमच्या डिव्हाइसवर चालवते
- **OpenAI SDK सुसंगतता**: विद्यमान OpenAI कोडसह अखंड एकत्रीकरण
- **मॉडेल व्यवस्थापन**: अनेक मॉडेल्स कार्यक्षमतेने डाउनलोड, कॅशे आणि चालवा
- **हार्डवेअर ऑप्टिमायझेशन**: GPU, NPU आणि CPU प्रवेगाचा लाभ घ्या

### 2. CLI कमांड संदर्भ

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK एकत्रीकरण

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

## सामान्य समस्यांचे निराकरण

### समस्या 1: "Foundry कमांड सापडले नाही"

**उपाय:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### समस्या 2: "मॉडेल लोड करण्यात अयशस्वी"

**उपाय:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### समस्या 3: "localhost:5273 वर कनेक्शन नाकारले"

**उपाय:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## कार्यक्षमतेसाठी टिप्स

### 1. मॉडेल निवड धोरण

- **Phi-4-mini**: सामान्य कार्यांसाठी सर्वोत्तम, कमी मेमरी वापर
- **Qwen2.5-0.5b**: जलद अनुमान, कमी संसाधने
- **GPT-OSS-20B**: उच्च दर्जा, अधिक संसाधने आवश्यक
- **DeepSeek-Coder**: प्रोग्रामिंग कार्यांसाठी अनुकूलित

### 2. हार्डवेअर ऑप्टिमायझेशन

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. कार्यक्षमता निरीक्षण

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### पर्यायी सुधारणा

| सुधारणा | काय | कसे |
|-------------|------|-----|
| सामायिक उपयुक्तता | क्लायंट/बूटस्ट्रॅप लॉजिकची पुनरावृत्ती काढा | `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) वापरा |
| टोकन वापर दृश्यमानता | खर्च/कार्यक्षमता विचार शिकवा | `SHOW_USAGE=1` सेट करा जेणेकरून प्रॉम्प्ट/पूर्णता/एकूण टोकन प्रिंट होईल |
| निर्धारक तुलना | स्थिर बेंचमार्किंग आणि पुनरावृत्ती तपासणी | `temperature=0`, `top_p=1`, सुसंगत प्रॉम्प्ट मजकूर वापरा |
| पहिला-टोकन विलंब | प्रतिसादाची धारणा मेट्रिक | स्ट्रीमिंगसह बेंचमार्क स्क्रिप्ट अनुकूल करा (`BENCH_STREAM=1`) |
| तात्पुरत्या त्रुटींवर पुनर्प्रयत्न | थंड सुरुवातीसाठी लवचिक डेमो | `RETRY_ON_FAIL=1` (डीफॉल्ट) आणि `RETRY_BACKOFF` समायोजित करा |
| स्मोक टेस्टिंग | मुख्य प्रवाहांवर जलद शुद्धता | कार्यशाळेपूर्वी `python Workshop/tests/smoke.py` चालवा |
| मॉडेल उपनाम प्रोफाइल | मशीन दरम्यान मॉडेल सेट जलद बदलणे | `.env` मध्ये `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` ठेवा |
| कॅशे कार्यक्षमता | मल्टी-सॅम्पल रनमध्ये वारंवार वॉर्मअप टाळा | उपयुक्तता कॅशे व्यवस्थापक; स्क्रिप्ट्स/नोटबुक्समध्ये पुन्हा वापरा |
| पहिला रन वॉर्मअप | p95 विलंब स्पाइक्स कमी करा | `FoundryLocalManager` तयार केल्यानंतर एक छोटा प्रॉम्प्ट फायर करा |

निर्धारक वॉर्म बेसलाइनचे उदाहरण (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

तुम्हाला दुसऱ्या रनवर समान आउटपुट आणि समान टोकन संख्या दिसेल, ज्यामुळे निर्धारकता पुष्टी होते.

## पुढील चरण

हे सत्र पूर्ण केल्यानंतर:

1. **सत्र 2 एक्सप्लोर करा**: Azure AI Foundry RAG सह AI सोल्यूशन्स तयार करा
2. **विविध मॉडेल्स वापरून पहा**: Qwen, DeepSeek आणि इतर मॉडेल कुटुंबे वापरून प्रयोग करा
3. **कार्यक्षमता ऑप्टिमाइझ करा**: तुमच्या विशिष्ट हार्डवेअरसाठी सेटिंग्ज सुधारित करा
4. **कस्टम अ‍ॅप्लिकेशन्स तयार करा**: तुमच्या स्वतःच्या प्रकल्पांमध्ये Foundry Local SDK वापरा

## अतिरिक्त संसाधने

### दस्तऐवज
- [Foundry Local Python SDK संदर्भ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local स्थापना मार्गदर्शक](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [मॉडेल कॅटलॉग](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### नमुना कोड
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### समुदाय
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**सत्र कालावधी**: 30 मिनिटे प्रात्यक्षिक + 15 मिनिटे प्रश्नोत्तर
**अडचणीची पातळी**: सुरुवातीची
**पूर्वापेक्षिते**: Windows 11, Python 3.10+, प्रशासक प्रवेश

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा स्क्रिप्ट / नोटबुक | परिस्थिती | उद्दिष्ट | उदाहरण इनपुट | आवश्यक डेटासेट |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | गोपनीयता मूल्यांकन पोर्टलसाठी ऑन-डिव्हाइस अनुमानाचे मूल्यांकन करणारी अंतर्गत IT टीम | स्थानिक SLM मानक प्रॉम्प्टवर उप-सेकंद विलंबात प्रतिसाद देते हे सिद्ध करा | "स्थानिक अनुमानाचे दोन फायदे सूचीबद्ध करा." | नाही (सिंगल प्रॉम्प्ट) |
| क्विकस्टार्ट अ‍ॅडॉप्टेशन कोड ब्लॉक | विद्यमान OpenAI स्क्रिप्ट Foundry Local मध्ये स्थलांतरित करणारा विकसक | ड्रॉप-इन सुसंगतता दर्शवा | "स्थानिक अनुमानाचे दोन फायदे सांगा." | फक्त इनलाइन प्रॉम्प्ट |

### परिस्थिती कथन
सुरक्षा आणि अनुपालन पथकाला संवेदनशील प्रोटोटाइप डेटा स्थानिक स्तरावर प्रक्रिया करता येतो का हे सत्यापित करणे आवश्यक आहे. ते बूटस्ट्रॅप स्क्रिप्ट अनेक प्रॉम्प्ट्स (गोपनीयता, विलंब, खर्च) सह deterministic temperature=0 मोडमध्ये चालवतात जेणेकरून नंतरच्या तुलनेसाठी बेसलाइन आउटपुट कॅप्चर करता येतील (सत्र 3 बेंचमार्किंग आणि सत्र 4 SLM vs LLM तुलना).

### मिनिमल प्रॉम्प्ट सेट JSON (पर्यायी)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

या यादीचा वापर पुनरुत्पादक मूल्यांकन लूप तयार करण्यासाठी किंवा भविष्यातील पुनरावृत्ती चाचणीसाठी बियाणे म्हणून करा.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृप्टिम भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.