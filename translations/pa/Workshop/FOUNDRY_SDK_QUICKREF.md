# Foundry Local SDK - ਤੁਰੰਤ ਸਹਾਇਕ

## ਇੰਸਟਾਲੇਸ਼ਨ

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

## ਸੇਵਾ ਪ੍ਰਬੰਧਨ

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

## ਬੁਨਿਆਦੀ ਵਰਤੋਂ ਦਾ ਪੈਟਰਨ

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

## ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ

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

## ਵਰਕਸ਼ਾਪ ਯੂਟਿਲਿਟੀਜ਼ (ਸਰਲ)

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

## ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

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

## ਆਮ ਮਾਡਲ ਉਪਨਾਮ

| ਉਪਨਾਮ | ਆਕਾਰ | ਸਭ ਤੋਂ ਵਧੀਆ |
|-------|------|----------|
| `phi-4-mini` | ~4B | ਜਨਰਲ, ਸੰਖੇਪ |
| `phi-3.5-mini` | ~3.5B | ਕੋਡ, ਰੀਫੈਕਟਰੀੰਗ |
| `qwen2.5-0.5b` | ~0.5B | ਤੇਜ਼ ਵਰਗੀਕਰਨ |
| `qwen2.5-coder-0.5b` | ~0.5B | ਕੋਡ ਜਨਰੇਸ਼ਨ |
| `gemma-2b` | ~2B | ਰਚਨਾਤਮਕ ਲਿਖਤ |

## ਗਲਤੀ ਸੰਭਾਲ

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

## ਸਮੱਸਿਆ ਹੱਲ

### ਕਨੈਕਸ਼ਨ ਗਲਤੀ
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### ਇੰਪੋਰਟ ਗਲਤੀ
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## ਉन्नਤ: ਕਈ ਮਾਡਲ

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

## ਪ੍ਰਦਰਸ਼ਨ ਸੁਝਾਅ

1. **ਕੈਸ਼ ਕਲਾਇੰਟਸ**: `FoundryLocalManager` ਇੰਸਟੈਂਸ ਨੂੰ ਦੁਬਾਰਾ ਵਰਤੋ
2. **ਬੈਚ ਰਿਕਵੈਸਟਸ**: ਕਈ ਪ੍ਰੋੰਪਟਸ ਨੂੰ ਲਗਾਤਾਰ ਪ੍ਰੋਸੈਸ ਕਰੋ
3. **max_tokens ਨੂੰ ਸਮਾਯੋਜਿਤ ਕਰੋ**: ਘੱਟ = ਤੇਜ਼ ਜਵਾਬ
4. **ਮਾਡਲ ਪਹਿਲਾਂ ਲੋਡ ਕਰੋ**: ਉਤਪਾਦਨ ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ
5. **ਵਰਤੋਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ**: ਟੋਕਨ ਨੂੰ `SHOW_USAGE=1` ਨਾਲ ਟ੍ਰੈਕ ਕਰੋ

## ਸਰੋਤ

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ:**
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

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।