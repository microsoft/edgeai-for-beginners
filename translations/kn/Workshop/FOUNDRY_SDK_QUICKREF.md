# Foundry ಸ್ಥಳೀಯ SDK - ತ್ವರಿತ ಉಲ್ಲೇಖ

## ಸ್ಥಾಪನೆ

```bash
# SDK ಅನ್ನು ಸ್ಥಾಪಿಸಿ
pip install foundry-local-sdk openai

# Foundry Local ಸೇವೆಯನ್ನು ಸ್ಥಾಪಿಸಿ
# ವಿಂಡೋಸ್
winget install Microsoft.FoundryLocal

# ಮ್ಯಾಕ್‌ಒಎಸ್
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## ಸೇವೆ ನಿರ್ವಹಣೆ

```bash
# ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry service start

# ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಸೇವೆಯನ್ನು ನಿಲ್ಲಿಸಿ
foundry service stop

# ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model ls

# ಮಾದರಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
foundry model download phi-4-mini

# ಮಾದರಿ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಿರಿ
foundry model info phi-4-mini
```

## ಮೂಲ ಬಳಕೆ ಮಾದರಿ

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ವ್ಯವಸ್ಥಾಪಕನನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಅವಶ್ಯಕತೆ ಇದ್ದರೆ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# OpenAI-ಸಮ್ಮತ ಗ್ರಾಹಕವನ್ನು ರಚಿಸಿ
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# ಮಾದರಿ ID ಪಡೆಯಿರಿ
model_id = manager.get_model_info(alias).id

# ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆ

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

## ವರ್ಕ್‌ಶಾಪ್ ಉಪಕರಣಗಳು (ಸರಳೀಕೃತ)

```python
from workshop_utils import chat_once

# ಕ್ಯಾಶಿಂಗ್ ಮತ್ತು ಮರುಪ್ರಯತ್ನದೊಂದಿಗೆ ಏಕಕಾಲದ ಕರೆ
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## ಪರಿಸರ ಚರಗಳು

```python
import os

# ಟೋಕನ್ ಬಳಕೆಯನ್ನು ತೋರಿಸಿ
os.environ['SHOW_USAGE'] = '1'

# ಮರುಪ್ರಯತ್ನಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
os.environ['RETRY_ON_FAIL'] = '1'

# ಮರುಪ್ರಯತ್ನ ವಿಳಂಬವನ್ನು ಹೊಂದಿಸಿ
os.environ['RETRY_BACKOFF'] = '2.0'

# ಕಸ್ಟಮ್ ಎಂಡ್ಪಾಯಿಂಟ್
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## ಸಾಮಾನ್ಯ ಮಾದರಿ ಪರ್ಯಾಯ ಹೆಸರುಗಳು

| ಪರ್ಯಾಯ ಹೆಸರು | ಗಾತ್ರ | ಉತ್ತಮವಾಗಿದೆ |
|-------|------|----------|
| `phi-4-mini` | ~4B | ಸಾಮಾನ್ಯ, ಸಾರಾಂಶ |
| `phi-3.5-mini` | ~3.5B | ಕೋಡ್, ಪುನರ್‌ರಚನೆ |
| `qwen2.5-0.5b` | ~0.5B | ವೇಗದ ವರ್ಗೀಕರಣ |
| `qwen2.5-coder-0.5b` | ~0.5B | ಕೋಡ್ ರಚನೆ |
| `gemma-2b` | ~2B | ಸೃಜನಾತ್ಮಕ ಬರವಣಿಗೆ |

## ದೋಷ ನಿರ್ವಹಣೆ

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

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸಂಪರ್ಕ ದೋಷ
```bash
# ಸೇವೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಮರುಪ್ರಾರಂಭಿಸಿ
foundry service stop
foundry service start

# ಎಂಡ್‌ಪಾಯಿಂಟ್ ಪರೀಕ್ಷಿಸಿ
curl http://localhost:55769/health
```

### ಮಾದರಿ ಕಂಡುಬಂದಿಲ್ಲ
```bash
# ಲಭ್ಯವಿರುವ ಪಟ್ಟಿಯನ್ನು ತೋರಿಸಿ
foundry model ls

# ಅಗತ್ಯವಿದ್ದರೆ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
foundry model download phi-4-mini
```

### ಆಮದು ದೋಷ
```bash
# SDK ಅನ್ನು ಮರುಸ್ಥಾಪಿಸಿ
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## ಉನ್ನತ: ಬಹು ಮಾದರಿಗಳು

```python
from workshop_utils import get_client

# ಹಲವಾರು ಮಾದರಿಗಳನ್ನು ಪ್ರಾರಂಭಿಸಿ
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# ವಿಭಿನ್ನ ಮಾದರಿಗಳನ್ನು ಬಳಸಿ
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## ಕಾರ್ಯಕ್ಷಮತೆ ಸಲಹೆಗಳು

1. **ಕ್ಯಾಶೆ ಕ್ಲೈಂಟ್‌ಗಳು**: `FoundryLocalManager` ಉದಾಹರಣೆಗಳನ್ನು ಮರುಬಳಕೆ ಮಾಡಿ
2. **ಬ್ಯಾಚ್ ವಿನಂತಿಗಳು**: ಅನೇಕ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಕ್ರಮವಾಗಿ ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ
3. **max_tokens ಹೊಂದಿಸಿ**: ಕಡಿಮೆ = ವೇಗವಾದ ಪ್ರತಿಕ್ರಿಯೆಗಳು
4. **ಮಾದರಿಗಳನ್ನು ಪೂರ್ವ-ಲೋಡ್ ಮಾಡಿ**: ಉತ್ಪಾದನಾ ಬಳಕೆಗೆ ಮುಂಚಿತವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
5. **ಬಳಕೆಯನ್ನು ಗಮನಿಸಿ**: `SHOW_USAGE=1` ಮೂಲಕ ಟೋಕನ್‌ಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ

## ಸಂಪನ್ಮೂಲಗಳು

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**ತ್ವರಿತ ಪ್ರಾರಂಭ:**
```bash
# ಎಲ್ಲವನ್ನೂ ಸ್ಥಾಪಿಸಿ
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry service start

# ಪೈಥಾನ್‌ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->