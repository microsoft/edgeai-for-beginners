# SDK ya Foundry Local - Muhtasari wa Haraka

## Usakinishaji

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

## Usimamizi wa Huduma

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

## Muundo wa Matumizi ya Msingi

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

## Majibu ya Kutiririsha

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

## Zana za Warsha (Rahisishwa)

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

## Vigezo vya Mazingira

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

## Majina ya Kawaida ya Miundo

| Jina la Alias | Ukubwa | Bora Kwa |
|---------------|--------|----------|
| `phi-4-mini` | ~4B | Kawaida, muhtasari |
| `phi-3.5-mini` | ~3.5B | Nambari, kurekebisha |
| `qwen2.5-0.5b` | ~0.5B | Uainishaji wa haraka |
| `qwen2.5-coder-0.5b` | ~0.5B | Uundaji wa nambari |
| `gemma-2b` | ~2B | Uandishi wa ubunifu |

## Kushughulikia Makosa

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

## Utatuzi wa Shida

### Hitilafu ya Muunganisho
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### Mfano Haujapatikana
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### Hitilafu ya Uingizaji
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## Juu: Miundo Mingi

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

## Vidokezo vya Utendaji

1. **Hifadhi Wateja**: Tumia tena matukio ya `FoundryLocalManager`
2. **Maombi ya Kundi**: Shughulikia maoni mengi mfululizo
3. **Rekebisha max_tokens**: Chini = majibu ya haraka
4. **Pakua Miundo Mapema**: Pakua kabla ya matumizi ya uzalishaji
5. **Fuatilia Matumizi**: Fuata tokeni kwa kutumia `SHOW_USAGE=1`

## Rasilimali

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Masuala**: https://github.com/microsoft/Foundry-Local/issues

---

**Kuanza Haraka:**
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

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kibinadamu ya kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.