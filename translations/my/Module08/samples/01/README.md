# Sample 01: OpenAI SDK ကို အသုံးပြု၍ အမြန်စကားပြော

Microsoft Foundry Local ကို အသုံးပြု၍ ဒေသခံ AI အတိအကျကို OpenAI SDK ဖြင့် အသုံးပြုနည်းကို ပြသထားသော ရိုးရှင်းသော စကားပြောနမူနာ။

## အကျဉ်းချုပ်

ဒီနမူနာမှာ အောက်ပါအရာတွေကို ပြသထားပါတယ်။
- Foundry Local နှင့်အတူ OpenAI Python SDK ကို အသုံးပြုနည်း
- Azure OpenAI နှင့် Foundry ဒေသခံ configuration နှစ်ခုလုံးကို ကိုင်တွယ်နည်း
- အမှားကို သင့်တော်စွာ ကိုင်တွယ်ပြီး fallback များကို အကောင်းဆုံး အကောင်အထည်ဖော်နည်း
- FoundryLocalManager ကို အသုံးပြု၍ ဝန်ဆောင်မှုကို စီမံခန့်ခွဲနည်း

## လိုအပ်ချက်များ

- **Foundry Local**: PATH တွင် ထည့်သွင်းပြီး အသုံးပြုနိုင်ရမည်
- **Python**: 3.8 သို့မဟုတ် အထက်
- **Model**: Foundry Local တွင် loaded ဖြစ်သော မော်ဒယ် (ဥပမာ `phi-4-mini`)

## ထည့်သွင်းခြင်း

1. **Python ပတ်ဝန်းကျင်ကို စနစ်တကျ ပြင်ဆင်ပါ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **လိုအပ်သော dependencies များကို ထည့်သွင်းပါ:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ဝန်ဆောင်မှုကို စတင်ပြီး မော်ဒယ်တစ်ခုကို load လုပ်ပါ:**
   ```cmd
   foundry model run phi-4-mini
   ```


## အသုံးပြုနည်း

### Foundry Local (Default)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```


### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## ကုဒ်၏ အထူးအင်္ဂါရပ်များ

### FoundryLocalManager Integration

ဒီနမူနာမှာ Foundry Local SDK ကို အသုံးပြု၍ ဝန်ဆောင်မှုကို သင့်တော်စွာ စီမံခန့်ခွဲထားပါတယ်။

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### အမှားကိုင်တွယ်ခြင်း

အမှားကို သင့်တော်စွာ ကိုင်တွယ်ပြီး fallback များကို အကောင်းဆုံး အကောင်အထည်ဖော်ထားသည်။
- ဝန်ဆောင်မှုကို အလိုအလျောက် ရှာဖွေခြင်း
- SDK မရရှိပါက သက်သာစွာ degrade ဖြစ်ခြင်း
- အမှားများကို ရှင်းလင်းသော troubleshooting အတွက် error message များပေးခြင်း

## ပတ်ဝန်းကျင် Variable များ

| Variable | ဖော်ပြချက် | Default | လိုအပ်ချက် |
|----------|-------------|---------|----------|
| `MODEL` | မော်ဒယ် alias သို့မဟုတ် အမည် | `phi-4-mini` | No |
| `BASE_URL` | Foundry Local base URL | `http://localhost:8000` | No |
| `API_KEY` | API key (ဒေသခံအတွက် မလိုအပ်သည့်အခါများစွာ) | `""` | No |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | Azure အတွက် |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | Azure အတွက် |
| `AZURE_OPENAI_API_VERSION` | Azure API version | `2024-08-01-preview` | No |

## အခက်အခဲများကို ဖြေရှင်းခြင်း

### အများဆုံး ကြုံရသော ပြဿနာများ

1. **"Foundry SDK ကို အသုံးပြု၍ မရနိုင်ပါ" သတိပေးချက်:**
   - foundry-local-sdk ကို ထည့်သွင်းပါ: `pip install foundry-local-sdk`
   - သို့မဟုတ် manual configuration အတွက် environment variables များကို သတ်မှတ်ပါ

2. **Connection refused:**
   - Foundry Local ကို run လုပ်ထားကြောင်း သေချာပါ: `foundry service status`
   - မော်ဒယ်တစ်ခု load လုပ်ထားကြောင်း စစ်ဆေးပါ: `foundry service ps`

3. **မော်ဒယ်ကို မတွေ့ပါ:**
   - ရရှိနိုင်သော မော်ဒယ်များကို စစ်ဆေးပါ: `foundry model list`
   - မော်ဒယ်တစ်ခုကို load လုပ်ပါ: `foundry model run phi-4-mini`

### အတည်ပြုခြင်း

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## ရင်းမြစ်များ

- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-compatible API Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

