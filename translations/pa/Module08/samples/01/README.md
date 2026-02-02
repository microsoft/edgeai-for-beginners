# ਸੈਂਪਲ 01: OpenAI SDK ਰਾਹੀਂ ਤੇਜ਼ ਗੱਲਬਾਤ

ਇਹ ਸਧਾਰਨ ਗੱਲਬਾਤ ਦਾ ਉਦਾਹਰਨ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ Microsoft Foundry Local ਨਾਲ OpenAI SDK ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।

## ਝਲਕ

ਇਸ ਸੈਂਪਲ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖੋਗੇ:
- Foundry Local ਨਾਲ OpenAI Python SDK ਦੀ ਵਰਤੋਂ
- Azure OpenAI ਅਤੇ ਸਥਾਨਕ Foundry ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਸੰਭਾਲਣਾ
- ਸਹੀ ਤਰ੍ਹਾਂ ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਫਾਲਬੈਕ ਰਣਨੀਤੀਆਂ ਲਾਗੂ ਕਰਨਾ
- FoundryLocalManager ਦੀ ਵਰਤੋਂ ਸੇਵਾ ਪ੍ਰਬੰਧਨ ਲਈ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- **Foundry Local**: ਇੰਸਟਾਲ ਕੀਤੀ ਹੋਈ ਅਤੇ PATH 'ਤੇ ਉਪਲਬਧ
- **Python**: 3.8 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਵਰਜਨ
- **ਮਾਡਲ**: Foundry Local ਵਿੱਚ ਲੋਡ ਕੀਤਾ ਮਾਡਲ (ਜਿਵੇਂ ਕਿ `phi-4-mini`)

## ਇੰਸਟਾਲੇਸ਼ਨ

1. **Python ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰੋ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Dependencies ਇੰਸਟਾਲ ਕਰੋ:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ਸੇਵਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਮਾਡਲ ਲੋਡ ਕਰੋ:**
   ```cmd
   foundry model run phi-4-mini
   ```


## ਵਰਤੋਂ

### Foundry Local (ਡਿਫਾਲਟ)

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


## ਕੋਡ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

### FoundryLocalManager ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਇਸ ਸੈਂਪਲ ਵਿੱਚ Foundry Local SDK ਦੀ ਵਰਤੋਂ ਸੇਵਾ ਪ੍ਰਬੰਧਨ ਲਈ ਕੀਤੀ ਗਈ ਹੈ:

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


### ਗਲਤੀ ਸੰਭਾਲ

ਮਜ਼ਬੂਤ ਗਲਤੀ ਸੰਭਾਲ ਨਾਲ ਹੱਥੋਂ-ਹੱਥ ਸੰਰਚਨਾ ਲਈ ਫਾਲਬੈਕ:
- ਸਵੈਚਾਲਿਤ ਸੇਵਾ ਖੋਜ
- SDK ਉਪਲਬਧ ਨਾ ਹੋਣ 'ਤੇ ਸੁਗਮ ਡਿਗਰੇਡੇਸ਼ਨ
- ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਲਈ ਸਪਸ਼ਟ ਗਲਤੀ ਸੁਨੇਹੇ

## ਵਾਤਾਵਰਣ ਚਰ

| ਚਰ | ਵੇਰਵਾ | ਡਿਫਾਲਟ | ਲਾਜ਼ਮੀ |
|-----|-------|---------|--------|
| `MODEL` | ਮਾਡਲ ਦਾ ਉਪਨਾਮ ਜਾਂ ਨਾਮ | `phi-4-mini` | ਨਹੀਂ |
| `BASE_URL` | Foundry Local ਬੇਸ URL | `http://localhost:8000` | ਨਹੀਂ |
| `API_KEY` | API ਕੁੰਜੀ (ਸਥਾਨਕ ਲਈ ਆਮ ਤੌਰ 'ਤੇ ਲੋੜੀਂਦੀ ਨਹੀਂ) | `""` | ਨਹੀਂ |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ਐਂਡਪੌਇੰਟ | - | Azure ਲਈ |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API ਕੁੰਜੀ | - | Azure ਲਈ |
| `AZURE_OPENAI_API_VERSION` | Azure API ਵਰਜਨ | `2024-08-01-preview` | ਨਹੀਂ |

## ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **"Foundry SDK ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕੀ" ਚੇਤਾਵਨੀ:**
   - Foundry Local SDK ਇੰਸਟਾਲ ਕਰੋ: `pip install foundry-local-sdk`
   - ਜਾਂ ਹੱਥੋਂ-ਹੱਥ ਸੰਰਚਨਾ ਲਈ ਵਾਤਾਵਰਣ ਚਰ ਸੈਟ ਕਰੋ

2. **ਕਨੈਕਸ਼ਨ ਰਿਫਿਊਜ਼ਡ:**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਚੱਲ ਰਿਹਾ ਹੈ: `foundry service status`
   - ਜਾਂਚ ਕਰੋ ਕਿ ਮਾਡਲ ਲੋਡ ਹੈ: `foundry service ps`

3. **ਮਾਡਲ ਨਹੀਂ ਮਿਲਿਆ:**
   - ਉਪਲਬਧ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ: `foundry model list`
   - ਮਾਡਲ ਲੋਡ ਕਰੋ: `foundry model run phi-4-mini`

### ਤਸਦੀਕ

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## ਸੰਦਰਭ

- [Foundry Local ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-ਅਨੁਕੂਲ API ਸੰਦਰਭ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

