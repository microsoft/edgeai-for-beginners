# အပိုင်း ၁: Foundry Local ကို စတင်အသုံးပြုခြင်း

## အကျဉ်းချုပ်

Microsoft Foundry Local ကို အသုံးပြု၍ AI မော်ဒယ်များကို တပ်ဆင်ခြင်း၊ ဖွဲ့စည်းခြင်းနှင့် အလုပ်လုပ်စေခြင်းကို လေ့လာပါ။ ဒီလက်တွေ့အပိုင်းမှာ တပ်ဆင်ခြင်းမှ စတင်ပြီး Phi-4, Qwen, နှင့် DeepSeek မော်ဒယ်များကို အသုံးပြု၍ ပထမဆုံး chat application တစ်ခုကို တည်ဆောက်ခြင်းအထိ လိုက်လျောညီထွေ လမ်းညွှန်မှုကို ပေးပါသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီအပိုင်းအပြီးမှာ သင်သည်-

- **တပ်ဆင်ခြင်းနှင့် ဖွဲ့စည်းခြင်း**: Foundry Local ကို တပ်ဆင်ပြီး အတည်ပြုခြင်း
- **CLI လုပ်ဆောင်မှုများကို ကျွမ်းကျင်ခြင်း**: Foundry Local CLI ကို အသုံးပြု၍ မော်ဒယ်များကို စီမံခန့်ခွဲခြင်းနှင့် တင်သွင်းခြင်း
- **ပထမဆုံး မော်ဒယ်ကို အလုပ်လုပ်စေခြင်း**: ဒေသခံ AI မော်ဒယ်တစ်ခုကို အောင်မြင်စွာ တင်သွင်းပြီး အပြန်အလှန်လုပ်ဆောင်ခြင်း
- **Chat App တစ်ခု တည်ဆောက်ခြင်း**: Foundry Local Python SDK ကို အသုံးပြု၍ chat application အခြေခံတစ်ခုကို ဖန်တီးခြင်း
- **ဒေသခံ AI ကို နားလည်ခြင်း**: ဒေသခံ inference နှင့် မော်ဒယ်စီမံခန့်ခွဲမှု၏ အခြေခံအချက်များကို နားလည်ခြင်း

## ကြိုတင်လိုအပ်ချက်များ

### စနစ်လိုအပ်ချက်များ

- **Windows**: Windows 11 (22H2 သို့မဟုတ် အထက်) OR **macOS**: macOS 11+ (အကန့်အသတ်ရှိသော ပံ့ပိုးမှု)
- **RAM**: အနည်းဆုံး 8GB၊ အကြံပြုချက် 16GB+
- **သိုလှောင်မှု**: မော်ဒယ်များအတွက် အခမဲ့နေရာ 10GB+
- **Python**: 3.10 သို့မဟုတ် အထက်တင်ထားရှိရမည်
- **Admin Access**: တပ်ဆင်ရန် အုပ်ချုပ်သူအခွင့်အာဏာ

### ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်

- Python extension ပါရှိသော Visual Studio Code (အကြံပြုချက်)
- Command line access (Windows တွင် PowerShell၊ macOS တွင် Terminal)
- Git (optional) ကို အသုံးပြု၍ repository များကို clone လုပ်ခြင်း

## အလုပ်ရုံဆွေးနွေးမှု အစီအစဉ် (၃၀ မိနစ်)

### အဆင့် ၁: Foundry Local ကို တပ်ဆင်ခြင်း (၅ မိနစ်)

#### Windows တွင် တပ်ဆင်ခြင်း

Windows package manager ကို အသုံးပြု၍ Foundry Local ကို တပ်ဆင်ပါ:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

အခြားနည်းလမ်း: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) မှ တိုက်ရိုက်ဒေါင်းလုပ်ဆွဲပါ

#### macOS တွင် တပ်ဆင်ခြင်း (အကန့်အသတ်ရှိသော ပံ့ပိုးမှု)

> [!NOTE]  
> macOS ပံ့ပိုးမှုသည် လက်ရှိတွင် preview အဆင့်တွင် ရှိနေပါသည်။ နောက်ဆုံးရရှိနိုင်မှုအတွက် တရားဝင်စာရွက်စာတမ်းကို စစ်ဆေးပါ။

Homebrew ကို အသုံးပြု၍ တပ်ဆင်ပါ:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS အသုံးပြုသူများအတွက် အခြားနည်းလမ်းများ:**
- Windows 11 VM (Parallels/UTM) ကို အသုံးပြု၍ Windows အဆင့်များကို လိုက်နာပါ
- container ကို အသုံးပြု၍ `FOUNDRY_LOCAL_ENDPOINT` ကို ဖွဲ့စည်းပါ

### အဆင့် ၂: တပ်ဆင်မှုကို အတည်ပြုခြင်း (၃ မိနစ်)

တပ်ဆင်ပြီးနောက် terminal ကို ပြန်စပြီး Foundry Local အလုပ်လုပ်နေသည်ကို အတည်ပြုပါ:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

မျှော်မှန်းထားသော output တွင် version အချက်အလက်နှင့် ရရှိနိုင်သော command များကို ပြသရမည်။

### အဆင့် ၃: Python ပတ်ဝန်းကျင်ကို ဖွဲ့စည်းခြင်း (၅ မိနစ်)

ဒီ workshop အတွက် သီးသန့် Python ပတ်ဝန်းကျင်တစ်ခုကို ဖန်တီးပါ:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### အဆင့် ၄: ပထမဆုံး မော်ဒယ်ကို အလုပ်လုပ်စေခြင်း (၇ မိနစ်)

အခုတော့ AI မော်ဒယ်တစ်ခုကို ဒေသခံတွင် အလုပ်လုပ်စေကြပါစို့!

#### Phi-4 Mini ဖြင့် စတင်ပါ (အကြံပြုထားသော ပထမဆုံး မော်ဒယ်)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> ဒီ command သည် မော်ဒယ်ကို (ပထမဆုံးအကြိမ်) ဒေါင်းလုပ်ဆွဲပြီး Foundry Local service ကို အလိုအလျောက် စတင်ပေးပါသည်။

#### အလုပ်လုပ်နေသည်ကို စစ်ဆေးပါ

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### မော်ဒယ်အမျိုးမျိုးကို စမ်းသပ်ပါ

phi-4-mini အလုပ်လုပ်နေပြီးပါက အခြားမော်ဒယ်များကို စမ်းသပ်ပါ:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### အဆင့် ၅: ပထမဆုံး Chat Application ကို တည်ဆောက်ခြင်း (၁၀ မိနစ်)

အခုတော့ ကျွန်ုပ်တို့ စတင်ထားသော မော်ဒယ်များကို အသုံးပြုသော Python application တစ်ခုကို ဖန်တီးကြပါစို့။

#### Chat Script ကို ဖန်တီးပါ

`my_first_chat.py` ဟုခေါ်သော ဖိုင်အသစ်တစ်ခုကို ဖန်တီးပါ (သို့မဟုတ် ပေးထားသော နမူနာကို အသုံးပြုပါ):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]  
> **သက်ဆိုင်သော နမူနာများ**: ပိုမိုအဆင့်မြင့်အသုံးပြုမှုအတွက် ကြည့်ပါ:
>
> - **Python နမူနာ**: `Workshop/samples/session01/chat_bootstrap.py` - streaming response နှင့် error handling ပါဝင်သည်
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - အသေးစိတ်ရှင်းလင်းချက်များပါရှိသော interactive version

#### Chat Application ကို စမ်းသပ်ပါ

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

အခြားနည်းလမ်း: ပေးထားသော နမူနာများကို တိုက်ရိုက်အသုံးပြုပါ

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

သို့မဟုတ် interactive notebook ကို စမ်းသပ်ပါ  
Workshop/notebooks/session01_chat_bootstrap.ipynb ကို VS Code တွင် ဖွင့်ပါ

ဒီဥပမာစကားပြောများကို စမ်းသပ်ပါ:

- "Microsoft Foundry Local ဆိုတာ ဘာလဲ?"
- "AI မော်ဒယ်များကို ဒေသခံတွင် အလုပ်လုပ်စေခြင်း၏ အကျိုးကျေးဇူး ၃ ခုကို ဖော်ပြပါ"
- "edge AI ကို နားလည်စေပါ"

## သင်အောင်မြင်စွာ ပြီးမြောက်ခဲ့သည့်အရာများ

ဂုဏ်ယူပါတယ်! သင်အောင်မြင်စွာ-

1. ✅ **Foundry Local ကို တပ်ဆင်ပြီး အတည်ပြုခဲ့သည်**
2. ✅ **ပထမဆုံး AI မော်ဒယ်** (phi-4-mini) ကို ဒေသခံတွင် စတင်ခဲ့သည်
3. ✅ **မော်ဒယ်အမျိုးမျိုးကို စမ်းသပ်ခဲ့သည်** command line မှတစ်ဆင့်
4. ✅ **Chat application တစ်ခုကို တည်ဆောက်ခဲ့သည်** ဒေသခံ AI ကို ချိတ်ဆက်ထားသော
5. ✅ **Cloud မရှိဘဲ ဒေသခံ AI inference ကို အတွေ့အကြုံရခဲ့သည်**

## ဖြစ်ပျက်ခဲ့သည့်အရာကို နားလည်ခြင်း

### ဒေသခံ AI Inference

- သင်၏ AI မော်ဒယ်များသည် သင်၏ကွန်ပျူတာပေါ်တွင် အပြည့်အဝ အလုပ်လုပ်သည်
- အချက်အလက်များကို cloud သို့ မပို့ပါ
- အပြန်အလှန်များကို သင်၏ CPU/GPU ကို အသုံးပြု၍ ဒေသခံတွင် ဖန်တီးသည်
- ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေးကို ထိန်းသိမ်းထားသည်

### မော်ဒယ်စီမံခန့်ခွဲမှု

- `foundry model run` သည် မော်ဒယ်များကို ဒေါင်းလုပ်ဆွဲပြီး စတင်သည်
- **FoundryLocalManager SDK** သည် service စတင်ခြင်းနှင့် မော်ဒယ်တင်သွင်းခြင်းကို အလိုအလျောက် စီမံခန့်ခွဲသည်
- မော်ဒယ်များကို အနာဂတ်အသုံးပြုမှုအတွက် ဒေသခံတွင် cache လုပ်ထားသည်
- မော်ဒယ်များကို များစွာ ဒေါင်းလုပ်ဆွဲနိုင်သော်လည်း 通常 တစ်ခုသာ အလုပ်လုပ်သည်
- service သည် မော်ဒယ်၏ အသက်တာကို အလိုအလျောက် စီမံခန့်ခွဲသည်

### SDK နှင့် CLI လမ်းလျှောက်မှုများ

- **CLI လမ်းလျှောက်မှု**: `foundry model run <model>` ဖြင့် မော်ဒယ်စီမံခန့်ခွဲမှုကို လက်ဖြင့်လုပ်ဆောင်ခြင်း
- **SDK လမ်းလျှောက်မှု**: `FoundryLocalManager(alias)` ဖြင့် service + မော်ဒယ်စီမံခန့်ခွဲမှုကို အလိုအလျောက်လုပ်ဆောင်ခြင်း
- **အကြံပြုချက်**: application များအတွက် SDK ကို အသုံးပြုပါ၊ စမ်းသပ်ခြင်းနှင့် ရှာဖွေခြင်းအတွက် CLI ကို အသုံးပြုပါ

## အရေးကြီးသော Command များကို ရှင်းလင်းခြင်း

### CLI Command များ

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```


### မော်ဒယ်အကြံပြုချက်များ

- **phi-4-mini**: စတင်ရန်အကောင်းဆုံး မော်ဒယ် - မြန်ဆန်၊ အလေးမရှိ၊ အရည်အသွေးကောင်း
- **qwen2.5-0.5b**: အမြန်ဆုံး inference၊ memory အသုံးပြုမှု အနည်းဆုံး
- **gpt-oss-20b**: အရည်အသွေးမြင့်သော အပြန်အလှန်များ၊ အရင်းအမြစ်များ ပိုမိုလိုအပ်
- **deepseek-coder-1.3b**: programming နှင့် code အလုပ်များအတွက် အထူးပြုထားသည်

## ပြဿနာများကို ဖြေရှင်းခြင်း

### "Foundry command not found"

**ဖြေရှင်းနည်း:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "Model failed to load"

**ဖြေရှင်းနည်း:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### "Connection refused on localhost"

**ဖြေရှင်းနည်း:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## နောက်တစ်ဆင့်များ

### ချက်ချင်းလုပ်ဆောင်ရန်

1. **မော်ဒယ်များနှင့် prompt များကို စမ်းသပ်ပါ**
2. **သင်၏ chat application ကို ပြင်ဆင်ပြီး မော်ဒယ်အမျိုးမျိုးကို စမ်းသပ်ပါ**
3. **သင်၏ကိုယ်ပိုင် prompt များကို ဖန်တီးပြီး အပြန်အလှန်များကို စမ်းသပ်ပါ**
4. **Session 2**: RAG application များကို တည်ဆောက်ခြင်းကို ရှာဖွေပါ

### အဆင့်မြင့် သင်ယူမှုလမ်းကြောင်း

1. **Session 2**: RAG (Retrieval-Augmented Generation) ဖြင့် AI ဖြေရှင်းချက်များကို တည်ဆောက်ခြင်း
2. **Session 3**: အခြား open-source မော်ဒယ်များကို နှိုင်းယှဉ်ခြင်း
3. **Session 4**: နောက်ဆုံးပေါ် မော်ဒယ်များနှင့် အလုပ်လုပ်ခြင်း
4. **Session 5**: multi-agent AI စနစ်များကို တည်ဆောက်ခြင်း

## ပတ်ဝန်းကျင် Variable များ (optional)

ပိုမိုအဆင့်မြင့်အသုံးပြုမှုအတွက် ဒီပတ်ဝန်းကျင် variable များကို သတ်မှတ်နိုင်သည်:

| Variable | ရည်ရွယ်ချက် | ဥပမာ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | အသုံးပြုရန် မော်ဒယ် default | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | endpoint URL ကို override | `http://localhost:5273/v1` |

သင်၏ project directory တွင် `.env` ဖိုင်တစ်ခု ဖန်တီးပါ:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## ထပ်ဆောင်းအရင်းအမြစ်များ

### စာရွက်စာတမ်းများ

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### နမူနာ Code

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - streaming response ပါရှိသော chat app အပြည့်အစုံ
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - interactive tutorial  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Community

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Session ကြာမြင့်ချိန်**: လက်တွေ့ ၃၀ မိနစ် + Q&A ၁၅ မိနစ်  
**အဆင့်အတန်း**: Beginner  
**ကြိုတင်လိုအပ်ချက်များ**: Windows 11/macOS 11+, Python 3.10+, Admin access

## Workshop ဥပမာအခြေအနေ

### အမှန်တကယ်အခြေအနေ

**အခြေအနေ**: အဖွဲ့အစည်း IT အဖွဲ့တစ်ခုသည် sensitive employee feedback များကို အပြင်ပဝန်ဆောင်မှုများသို့ အချက်အလက်မပို့ဘဲ device ပေါ်တွင် AI inference ကို စမ်းသပ်ရန် လိုအပ်သည်။

**သင်၏ရည်မှန်းချက်**: ဒေသခံ AI မော်ဒယ်များသည် sub-second latency ဖြင့် အရည်အသွေးမြင့် အပြန်အလှန်များကို ပေးနိုင်ပြီး အချက်အလက်လုံခြုံရေးကို ထိန်းသိမ်းထားနိုင်သည်ကို ပြသပါ။

### Test Prompts

ဒီ prompt များကို သင်၏ setup ကို အတည်ပြုရန် အသုံးပြုပါ:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### အောင်မြင်မှုအချက်အလက်များ

- ✅ prompt များအားလုံးသည် ၂ စက္ကန့်အောက်တွင် အပြန်အလှန်ရရှိသည်
- ✅ အချက်အလက်များသည် သင်၏ local machine ကို မထွက်သွားပါ
- ✅ အပြန်အလှန်များသည် သက်ဆိုင်ပြီး အကျိုးရှိသည်
- ✅ သင်၏ chat application သည် ချောမွေ့စွာ အလုပ်လုပ်သည်

ဒီအတည်ပြုမှုသည် Sessions 2-6 တွင် အဆင့်မြင့် workshop များအတွက် သင်၏ Foundry Local setup အဆင်သင့်ဖြစ်ကြောင်း အတည်ပြုသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->