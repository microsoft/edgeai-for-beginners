# Foundry Local SDK - အမြန်အကျဉ်း

## တပ်ဆင်ခြင်း

```bash
# Install SDK
pip install foundry-local-sdk openai

# Install Foundry Local service
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## ဝန်ဆောင်မှု စီမံခန့်ခွဲမှု

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# List models
foundry model ls

# Download model
foundry model download phi-4-mini

# Get model info
foundry model info phi-4-mini
```

## အခြေခံ အသုံးပြုမှု ပုံစံ

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize manager (starts service if needed)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# Create OpenAI-compatible client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Get model ID
model_id = manager.get_model_info(alias).id

# Chat completion
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## Streaming Response

```python
stream = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Workshop Utils (ရိုးရှင်းထားသော)

```python
from workshop_utils import chat_once

# Single call with caching and retry
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## ပတ်ဝန်းကျင် အပြောင်းအလဲများ

```python
import os

# Show token usage
os.environ['SHOW_USAGE'] = '1'

# Enable retries
os.environ['RETRY_ON_FAIL'] = '1'

# Set retry delay
os.environ['RETRY_BACKOFF'] = '2.0'

# Custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## အများဆုံး အသုံးပြုသော မော်ဒယ် အမည်များ

| အမည် | အရွယ်အစား | အကောင်းဆုံး အသုံးပြုမှု |
|-------|------------|--------------------------|
| `phi-4-mini` | ~4B | အထွေထွေ၊ အကျဉ်းချုပ်ရေး |
| `phi-3.5-mini` | ~3.5B | ကုဒ်၊ ပြန်လည်ပြင်ဆင်မှု |
| `qwen2.5-0.5b` | ~0.5B | အမြန် အမျိုးအစားခွဲခြင်း |
| `qwen2.5-coder-0.5b` | ~0.5B | ကုဒ် ဖန်တီးရေး |
| `gemma-2b` | ~2B | ဖန်တီးမှု စာရေးခြင်း |

## အမှားကို ကိုင်တွယ်ခြင်း

```python
from openai import OpenAIError

try:
    text, usage = chat_once('phi-4-mini', messages=[...])
except RuntimeError as e:
    print(f"Manager initialization failed: {e}")
    print("Check: foundry service status")
except OpenAIError as e:
    print(f"API call failed: {e}")
    print("Check: foundry model ls")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## ပြဿနာများကို ဖြေရှင်းခြင်း

### ချိတ်ဆက်မှု အမှား
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### မော်ဒယ် မတွေ့ရှိ
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### Import အမှား
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## အဆင့်မြင့်: မော်ဒယ်များစွာ အသုံးပြုခြင်း

```python
from workshop_utils import get_client

# Initialize multiple models
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# Use different models
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## လုပ်ဆောင်မှု အကြံပြုချက်များ

1. **Cache Clients**: `FoundryLocalManager` အတန်းများကို ထပ်မံအသုံးပြုပါ
2. **Batch Requests**: အကြောင်းပြချက်များကို အဆက်မပြတ် လုပ်ဆောင်ပါ
3. **max_tokens ကို ချိန်ညှိပါ**: နည်းသော = အမြန်ဆုံး တုံ့ပြန်မှု
4. **မော်ဒယ်များကို ကြိုတင်တင်ပါ**: ထုတ်လုပ်မှုမတိုင်မီ ဒေါင်းလုပ်လုပ်ပါ
5. **အသုံးပြုမှုကို စောင့်ကြည့်ပါ**: `SHOW_USAGE=1` ဖြင့် token များကို စစ်ဆေးပါ

## အရင်းအမြစ်များ

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**အမြန် စတင်ရန်:**
```bash
# Install everything
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# Start service
foundry service start

# Test in Python
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။