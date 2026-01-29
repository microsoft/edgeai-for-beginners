# Foundry Local SDK - விரைவான குறிப்புகள்

## நிறுவல்

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

## சேவை மேலாண்மை

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

## அடிப்படை பயன்பாட்டு முறை

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

## ஸ்ட்ரீமிங் பதில்

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

## வொர்க்ஷாப் உதவிகள் (எளிமைப்படுத்தப்பட்டது)

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

## சூழல் மாறிகள்

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

## பொதுவான மாடல் மாற்றுப்பெயர்கள்

| மாற்றுப்பெயர் | அளவு | சிறந்த பயன்பாடு |
|--------------|------|------------------|
| `phi-4-mini` | ~4B | பொதுவானது, சுருக்கம் |
| `phi-3.5-mini` | ~3.5B | குறியீடு, மறுசீரமைப்பு |
| `qwen2.5-0.5b` | ~0.5B | வேகமான வகைப்படுத்தல் |
| `qwen2.5-coder-0.5b` | ~0.5B | குறியீடு உருவாக்கம் |
| `gemma-2b` | ~2B | படைப்பாற்றல் எழுத்து |

## பிழை கையாளுதல்

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

## சிக்கல்களை சரிசெய்தல்

### இணைப்பு பிழை
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### மாடல் கிடைக்கவில்லை
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### இறக்குமதி பிழை
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## மேம்பட்டது: பல மாடல்கள்

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

## செயல்திறன் குறிப்புகள்

1. **கிளையன்ட்களை காசே செய்யவும்**: `FoundryLocalManager` உதாரணங்களை மீண்டும் பயன்படுத்தவும்
2. **தொகுதி கோரிக்கைகள்**: பல கேள்விகளை தொடர்ச்சியாக செயல்படுத்தவும்
3. **max_tokens ஐ சரிசெய்யவும்**: குறைவானது = வேகமான பதில்கள்
4. **மாடல்களை முன்கூட்டியே ஏற்றவும்**: உற்பத்தி பயன்பாட்டிற்கு முன் பதிவிறக்கவும்
5. **பயன்பாட்டை கண்காணிக்கவும்**: `SHOW_USAGE=1` மூலம் டோக்கன்களை கண்காணிக்கவும்

## வளங்கள்

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**விரைவான தொடக்கம்:**
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

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.