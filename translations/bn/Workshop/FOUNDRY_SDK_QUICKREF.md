# Foundry Local SDK - দ্রুত রেফারেন্স

## ইনস্টলেশন

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

## সার্ভিস ম্যানেজমেন্ট

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

## মৌলিক ব্যবহার প্যাটার্ন

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

## স্ট্রিমিং রেসপন্স

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

## ওয়ার্কশপ ইউটিলস (সরলীকৃত)

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

## পরিবেশ ভেরিয়েবল

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

## সাধারণ মডেল এলিয়াস

| এলিয়াস | আকার | সেরা ব্যবহারের ক্ষেত্র |
|---------|------|-------------------------|
| `phi-4-mini` | ~4B | সাধারণ, সারসংক্ষেপ |
| `phi-3.5-mini` | ~3.5B | কোড, পুনর্গঠন |
| `qwen2.5-0.5b` | ~0.5B | দ্রুত শ্রেণীবিভাগ |
| `qwen2.5-coder-0.5b` | ~0.5B | কোড জেনারেশন |
| `gemma-2b` | ~2B | সৃজনশীল লেখা |

## ত্রুটি পরিচালনা

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

## সমস্যা সমাধান

### সংযোগ ত্রুটি
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### মডেল পাওয়া যায়নি
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### ইমপোর্ট ত্রুটি
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## উন্নত: একাধিক মডেল

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

## পারফরম্যান্স টিপস

1. **ক্লায়েন্ট ক্যাশ করুন**: `FoundryLocalManager` ইনস্ট্যান্স পুনরায় ব্যবহার করুন
2. **ব্যাচ অনুরোধ**: একাধিক প্রম্পট ধারাবাহিকভাবে প্রক্রিয়া করুন
3. **max_tokens সামঞ্জস্য করুন**: কম = দ্রুত রেসপন্স
4. **মডেল প্রি-লোড করুন**: প্রোডাকশন ব্যবহারের আগে ডাউনলোড করুন
5. **ব্যবহার পর্যবেক্ষণ করুন**: টোকেন ট্র্যাক করতে `SHOW_USAGE=1` ব্যবহার করুন

## রিসোর্স

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**দ্রুত শুরু:**
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

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।