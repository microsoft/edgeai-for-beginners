# Foundry Local ਨੂੰ API ਨਮੂਨਾ ਵਜੋਂ ਵਰਤਣਾ

ਇਹ ਨਮੂਨਾ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ Microsoft Foundry Local ਨੂੰ REST API ਸੇਵਾ ਵਜੋਂ OpenAI SDK 'ਤੇ ਨਿਰਭਰ ਕੀਤੇ ਬਿਨਾਂ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਵੱਧ ਤੋਂ ਵੱਧ ਕੰਟਰੋਲ ਅਤੇ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ ਲਈ ਸਿੱਧੇ HTTP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪੈਟਰਨ ਦਿਖਾਉਂਦਾ ਹੈ।

## ਝਲਕ

Microsoft ਦੇ ਅਧਿਕਾਰਕ Foundry Local ਪੈਟਰਨਾਂ ਦੇ ਆਧਾਰ 'ਤੇ, ਇਹ ਨਮੂਨਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:
- FoundryLocalManager ਨਾਲ ਸਿੱਧੀ REST API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- ਕਸਟਮ HTTP ਕਲਾਇੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ
- ਮਾਡਲ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸਿਹਤ ਦੀ ਨਿਗਰਾਨੀ
- ਸਟ੍ਰੀਮਿੰਗ ਅਤੇ ਨਾਨ-ਸਟ੍ਰੀਮਿੰਗ ਰਿਸਪਾਂਸ ਹੈਂਡਲਿੰਗ
- ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਰਿਟ੍ਰਾਈ ਲਾਜਿਕ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

1. **Foundry Local ਇੰਸਟਾਲੇਸ਼ਨ**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Dependencies**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## ਆਰਕੀਟੈਕਚਰ

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

### 1. **ਸਿੱਧੀ HTTP ਇੰਟੀਗ੍ਰੇਸ਼ਨ**
- SDK ਨਿਰਭਰਤਾ ਤੋਂ ਬਿਨਾਂ ਖਾਲੀ REST API ਕਾਲਾਂ
- ਕਸਟਮ ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਹੈਡਰ
- ਰਿਕਵੈਸਟ/ਰਿਸਪਾਂਸ ਹੈਂਡਲਿੰਗ 'ਤੇ ਪੂਰਾ ਕੰਟਰੋਲ

### 2. **ਮਾਡਲ ਪ੍ਰਬੰਧਨ**
- ਡਾਇਨਾਮਿਕ ਮਾਡਲ ਲੋਡਿੰਗ ਅਤੇ ਅਨਲੋਡਿੰਗ
- ਸਿਹਤ ਦੀ ਨਿਗਰਾਨੀ ਅਤੇ ਸਥਿਤੀ ਚੈੱਕ
- ਪ੍ਰਦਰਸ਼ਨ ਮੈਟ੍ਰਿਕਸ ਇਕੱਠਾ ਕਰਨਾ

### 3. **ਪ੍ਰੋਡਕਸ਼ਨ ਪੈਟਰਨ**
- ਐਕਸਪੋਨੈਂਸ਼ਲ ਬੈਕਆਫ ਨਾਲ ਰਿਟ੍ਰਾਈ ਮਕੈਨਿਜ਼ਮ
- ਫਾਲਟ ਟੋਲਰੈਂਸ ਲਈ ਸਰਕਿਟ ਬ੍ਰੇਕਰ
- ਵਿਸਤ੍ਰਿਤ ਲੌਗਿੰਗ ਅਤੇ ਮਾਨੀਟਰਿੰਗ

### 4. **ਲਚਕਦਾਰ ਰਿਸਪਾਂਸ ਹੈਂਡਲਿੰਗ**
- ਰੀਅਲ-ਟਾਈਮ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਸਟ੍ਰੀਮਿੰਗ ਰਿਸਪਾਂਸ
- ਹਾਈ-ਥਰੂਪੁੱਟ ਸਨਰੀਓਜ਼ ਲਈ ਬੈਚ ਪ੍ਰੋਸੈਸਿੰਗ
- ਕਸਟਮ ਰਿਸਪਾਂਸ ਪਾਰਸਿੰਗ ਅਤੇ ਵੈਲੀਡੇਸ਼ਨ

## ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ

### ਬੇਸਿਕ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### ਸਟ੍ਰੀਮਿੰਗ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### ਸਿਹਤ ਦੀ ਨਿਗਰਾਨੀ
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## ਫਾਈਲ ਸਟ੍ਰਕਚਰ

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਇਹ ਨਮੂਨਾ Microsoft ਦੇ ਅਧਿਕਾਰਕ ਪੈਟਰਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ:

1. **SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਸੇਵਾ ਪ੍ਰਬੰਧਨ ਲਈ `FoundryLocalManager` ਵਰਤਦਾ ਹੈ
2. **REST Endpoints**: `/v1/chat/completions` ਅਤੇ ਹੋਰ ਐਂਡਪੋਇੰਟਸ ਲਈ ਸਿੱਧੇ ਕਾਲ
3. **ਪ੍ਰਮਾਣਿਕਤਾ**: ਸਥਾਨਕ ਸੇਵਾਵਾਂ ਲਈ ਸਹੀ API ਕੁੰਜੀ ਸੰਭਾਲ
4. **ਮਾਡਲ ਪ੍ਰਬੰਧਨ**: ਕੈਟਾਲੌਗ ਲਿਸਟਿੰਗ, ਡਾਊਨਲੋਡਿੰਗ, ਅਤੇ ਲੋਡਿੰਗ ਪੈਟਰਨ
5. **ਗਲਤੀ ਸੰਭਾਲ**: Microsoft-ਸੁਝਾਏ ਗਲਤੀ ਕੋਡ ਅਤੇ ਰਿਸਪਾਂਸ

## ਸ਼ੁਰੂਆਤ ਕਰਨਾ

1. **Dependencies ਇੰਸਟਾਲ ਕਰੋ**
   ```bash
   pip install -r requirements.txt
   ```

2. **ਬੇਸਿਕ ਉਦਾਹਰਨ ਚਲਾਓ**
   ```bash
   python examples/basic_usage.py
   ```

3. **ਸਟ੍ਰੀਮਿੰਗ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ**
   ```bash
   python examples/streaming.py
   ```

4. **ਪ੍ਰੋਡਕਸ਼ਨ ਸੈਟਅਪ**
   ```bash
   python examples/production.py
   ```

## ਕਨਫਿਗਰੇਸ਼ਨ

ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ:
- `FOUNDRY_MODEL`: ਵਰਤਣ ਲਈ ਡਿਫਾਲਟ ਮਾਡਲ (ਡਿਫਾਲਟ: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: ਸੈਕਿੰਡ ਵਿੱਚ ਰਿਕਵੈਸਟ ਟਾਈਮਆਉਟ (ਡਿਫਾਲਟ: 30)
- `FOUNDRY_RETRIES`: ਰਿਟ੍ਰਾਈ ਦੇ ਪ੍ਰਯਾਸਾਂ ਦੀ ਗਿਣਤੀ (ਡਿਫਾਲਟ: 3)
- `FOUNDRY_LOG_LEVEL`: ਲੌਗਿੰਗ ਲੈਵਲ (ਡਿਫਾਲਟ: "INFO")

## ਵਧੀਆ ਅਭਿਆਸ

1. **ਕਨੈਕਸ਼ਨ ਪ੍ਰਬੰਧਨ**: ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਲਈ HTTP ਕਨੈਕਸ਼ਨ ਦੁਬਾਰਾ ਵਰਤੋ
2. **ਗਲਤੀ ਸੰਭਾਲ**: ਐਕਸਪੋਨੈਂਸ਼ਲ ਬੈਕਆਫ ਨਾਲ ਸਹੀ ਰਿਟ੍ਰਾਈ ਲਾਜਿਕ ਲਾਗੂ ਕਰੋ
3. **ਸੰਸਾਧਨ ਨਿਗਰਾਨੀ**: ਮਾਡਲ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ
4. **ਸੁਰੱਖਿਆ**: ਸਥਾਨਕ ਸੇਵਾਵਾਂ ਲਈ ਵੀ ਸਹੀ ਪ੍ਰਮਾਣਿਕਤਾ ਵਰਤੋ
5. **ਟੈਸਟਿੰਗ**: ਯੂਨਿਟ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟ ਦੋਵੇਂ ਸ਼ਾਮਲ ਕਰੋ

## ਸਮੱਸਿਆ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

**ਸੇਵਾ ਚਲ ਰਹੀ ਨਹੀਂ**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**ਮਾਡਲ ਲੋਡਿੰਗ ਸਮੱਸਿਆਵਾਂ**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਸਹੀ ਪੋਰਟ 'ਤੇ ਚਲ ਰਿਹਾ ਹੈ
- ਫਾਇਰਵਾਲ ਸੈਟਿੰਗਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
- ਸਹੀ ਪ੍ਰਮਾਣਿਕਤਾ ਹੈਡਰ ਯਕੀਨੀ ਬਣਾਓ

## ਪ੍ਰਦਰਸ਼ਨ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ

1. **ਕਨੈਕਸ਼ਨ ਪੂਲਿੰਗ**: ਕਈ ਰਿਕਵੈਸਟਾਂ ਲਈ ਸੈਸ਼ਨ ਆਬਜੈਕਟ ਵਰਤੋ
2. **ਐਸਿੰਕ ਓਪਰੇਸ਼ਨ**: ਸਮਕਾਲੀ ਰਿਕਵੈਸਟਾਂ ਲਈ asyncio ਵਰਤੋ
3. **ਕੈਸ਼ਿੰਗ**: ਜਿੱਥੇ ਜ਼ਰੂਰੀ ਹੋਵੇ ਮਾਡਲ ਰਿਸਪਾਂਸ ਕੈਸ਼ ਕਰੋ
4. **ਮਾਨੀਟਰਿੰਗ**: ਰਿਸਪਾਂਸ ਸਮਿਆਂ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ ਅਤੇ ਟਾਈਮਆਉਟਸ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ

## ਸਿੱਖਣ ਦੇ ਨਤੀਜੇ

ਇਸ ਨਮੂਨੇ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਝ ਪਾਉਗੇ:
- Foundry Local ਨਾਲ ਸਿੱਧੀ REST API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- ਕਸਟਮ HTTP ਕਲਾਇੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਪੈਟਰਨ
- ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਮਾਨੀਟਰਿੰਗ
- Microsoft Foundry Local ਸੇਵਾ ਆਰਕੀਟੈਕਚਰ
- ਸਥਾਨਕ AI ਸੇਵਾਵਾਂ ਲਈ ਪ੍ਰਦਰਸ਼ਨ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ

## ਅਗਲੇ ਕਦਮ

- ਨਮੂਨਾ 08: Windows 11 ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਖੋਜ ਕਰੋ
- ਨਮੂਨਾ 09: ਮਲਟੀ-ਏਜੰਟ ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
- ਨਮੂਨਾ 10: Foundry Local ਨੂੰ ਟੂਲਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵਜੋਂ ਸਿੱਖੋ

---

