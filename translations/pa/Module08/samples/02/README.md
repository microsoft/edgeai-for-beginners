# ਨਮੂਨਾ 02: OpenAI SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ

OpenAI Python SDK ਨਾਲ ਉੱਚ-ਸਤ੍ਹਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦਿਖਾਉਂਦਾ ਹੈ, ਜੋ Microsoft Foundry Local ਅਤੇ Azure OpenAI ਦੋਵਾਂ ਨੂੰ ਸਹਾਇਕ ਹੈ, ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬਾਂ ਅਤੇ ਸਹੀ ਤਰ੍ਹਾਂ ਐਰਰ ਹੈਂਡਲਿੰਗ ਦੇ ਨਾਲ।

## ਝਲਕ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ:
- Foundry Local ਅਤੇ Azure OpenAI ਦੇ ਵਿਚਕਾਰ ਆਸਾਨ ਸਵਿੱਚਿੰਗ
- ਵਧੀਆ ਯੂਜ਼ਰ ਅਨੁਭਵ ਲਈ ਸਟ੍ਰੀਮਿੰਗ ਚੈਟ ਕਮਪਲੀਸ਼ਨ
- FoundryLocalManager SDK ਦੀ ਸਹੀ ਵਰਤੋਂ
- ਮਜ਼ਬੂਤ ਐਰਰ ਹੈਂਡਲਿੰਗ ਅਤੇ ਫਾਲਬੈਕ ਮਕੈਨਿਜ਼ਮ
- ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਕੋਡ ਪੈਟਰਨ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- **Foundry Local**: ਇੰਸਟਾਲ ਅਤੇ ਚਲ ਰਿਹਾ (ਲੋਕਲ ਇੰਫਰੈਂਸ ਲਈ)
- **Python**: 3.8 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ OpenAI SDK ਦੇ ਨਾਲ
- **Azure OpenAI**: ਵੈਧ ਐਂਡਪੌਇੰਟ ਅਤੇ API ਕੁੰਜੀ (ਕਲਾਉਡ ਇੰਫਰੈਂਸ ਲਈ)

## ਇੰਸਟਾਲੇਸ਼ਨ

1. **Python ਐਨਵਾਇਰਮੈਂਟ ਸੈਟਅੱਪ ਕਰੋ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ਸ਼ੁਰੂ ਕਰੋ (ਲੋਕਲ ਮੋਡ ਲਈ):**
   ```cmd
   foundry model run phi-4-mini
   ```


## ਵਰਤੋਂ ਦੇ ਸਥਿਤੀਆਂ

### Foundry Local (ਡਿਫਾਲਟ)

**ਵਿਕਲਪ 1: FoundryLocalManager ਦੀ ਵਰਤੋਂ (ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ਵਿਕਲਪ 2: ਮੈਨੁਅਲ ਕਨਫਿਗਰੇਸ਼ਨ**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## ਕੋਡ ਆਰਕੀਟੈਕਚਰ

### ਕਲਾਇੰਟ ਫੈਕਟਰੀ ਪੈਟਰਨ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਫੈਕਟਰੀ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਗਈ ਹੈ ਸਹੀ ਕਲਾਇੰਟ ਬਣਾਉਣ ਲਈ:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਰੀਅਲ-ਟਾਈਮ ਜਵਾਬ ਜਨਰੇਸ਼ਨ ਲਈ ਸਟ੍ਰੀਮਿੰਗ ਦਿਖਾਈ ਗਈ ਹੈ:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ

### Foundry Local ਕਨਫਿਗਰੇਸ਼ਨ

| ਵੈਰੀਏਬਲ | ਵੇਰਵਾ | ਡਿਫਾਲਟ | ਲਾਜ਼ਮੀ |
|----------|-------------|---------|----------|
| `MODEL` | ਵਰਤਣ ਲਈ ਮਾਡਲ ਅਲਿਆਸ | `phi-4-mini` | ਨਹੀਂ |
| `BASE_URL` | Foundry Local ਐਂਡਪੌਇੰਟ | `http://localhost:8000` | ਨਹੀਂ |
| `API_KEY` | API ਕੁੰਜੀ (ਲੋਕਲ ਲਈ ਵਿਕਲਪਿਕ) | `""` | ਨਹੀਂ |

### Azure OpenAI ਕਨਫਿਗਰੇਸ਼ਨ

| ਵੈਰੀਏਬਲ | ਵੇਰਵਾ | ਡਿਫਾਲਟ | ਲਾਜ਼ਮੀ |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ਸਰੋਤ ਐਂਡਪੌਇੰਟ | - | ਹਾਂ |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API ਕੁੰਜੀ | - | ਹਾਂ |
| `AZURE_OPENAI_API_VERSION` | API ਵਰਜਨ | `2024-08-01-preview` | ਨਹੀਂ |
| `MODEL` | Azure ਡਿਪਲੌਇਮੈਂਟ ਨਾਮ | `your-deployment-name` | ਹਾਂ |

## ਉੱਚ-ਸਤ੍ਹਾ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

### ਆਟੋਮੈਟਿਕ ਸਰਵਿਸ ਡਿਸਕਵਰੀ

ਇਹ ਨਮੂਨਾ ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਦੇ ਆਧਾਰ 'ਤੇ ਸਹੀ ਸਰਵਿਸ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਪਛਾਣਦਾ ਹੈ:

1. **Azure ਮੋਡ**: ਜੇ `AZURE_OPENAI_ENDPOINT` ਅਤੇ `AZURE_OPENAI_API_KEY` ਸੈਟ ਕੀਤੇ ਗਏ ਹਨ
2. **Foundry SDK ਮੋਡ**: ਜੇ Foundry Local SDK ਉਪਲਬਧ ਹੈ
3. **ਮੈਨੁਅਲ ਮੋਡ**: ਮੈਨੁਅਲ ਕਨਫਿਗਰੇਸ਼ਨ 'ਤੇ ਫਾਲਬੈਕ

### ਐਰਰ ਹੈਂਡਲਿੰਗ

- SDK ਤੋਂ ਮੈਨੁਅਲ ਕਨਫਿਗਰੇਸ਼ਨ 'ਤੇ ਗ੍ਰੇਸਫੁਲ ਫਾਲਬੈਕ
- ਟਰਬਲਸ਼ੂਟਿੰਗ ਲਈ ਸਪਸ਼ਟ ਐਰਰ ਸੁਨੇਹੇ
- ਨੈਟਵਰਕ ਸਮੱਸਿਆਵਾਂ ਲਈ ਸਹੀ ਤਰ੍ਹਾਂ ਐਕਸਪਸ਼ਨ ਹੈਂਡਲਿੰਗ
- ਲਾਜ਼ਮੀ ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ ਦੀ ਵੈਧਤਾ

## ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਵਿਚਾਰ

### ਲੋਕਲ ਵਿਰੁੱਧ ਕਲਾਉਡ ਟਰੇਡ-ਆਫ

**Foundry Local ਫਾਇਦੇ:**
- ✅ ਕੋਈ API ਖਰਚ ਨਹੀਂ
- ✅ ਡਾਟਾ ਗੋਪਨੀਯਤਾ (ਡਾਟਾ ਡਿਵਾਈਸ ਤੋਂ ਬਾਹਰ ਨਹੀਂ ਜਾਂਦਾ)
- ✅ ਸਹਾਇਕ ਮਾਡਲਾਂ ਲਈ ਘੱਟ ਲੈਟੈਂਸੀ
- ✅ ਆਫਲਾਈਨ ਕੰਮ ਕਰਦਾ ਹੈ

**Azure OpenAI ਫਾਇਦੇ:**
- ✅ ਨਵੇਂ ਵੱਡੇ ਮਾਡਲਾਂ ਤੱਕ ਪਹੁੰਚ
- ✅ ਉੱਚ throughput
- ✅ ਕੋਈ ਲੋਕਲ ਕੰਪਿਊਟ ਦੀ ਲੋੜ ਨਹੀਂ
- ✅ ਐਂਟਰਪ੍ਰਾਈਜ਼-ਗਰੇਡ SLA

## ਟਰਬਲਸ਼ੂਟਿੰਗ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **"Foundry SDK ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕੀ" ਚੇਤਾਵਨੀ:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure ਪ੍ਰਮਾਣਿਕਤਾ ਗਲਤੀਆਂ:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **ਮਾਡਲ ਉਪਲਬਧ ਨਹੀਂ:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### ਹੈਲਥ ਚੈੱਕਸ

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## ਅਗਲੇ ਕਦਮ

- **ਨਮੂਨਾ 03**: ਮਾਡਲ ਡਿਸਕਵਰੀ ਅਤੇ ਬੈਂਚਮਾਰਕਿੰਗ
- **ਨਮੂਨਾ 04**: ਇੱਕ Chainlit RAG ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ
- **ਨਮੂਨਾ 05**: ਮਲਟੀ-ਏਜੰਟ ਆਰਕੇਸਟ੍ਰੇਸ਼ਨ
- **ਨਮੂਨਾ 06**: ਮਾਡਲ-ਐਜ਼-ਟੂਲ ਰੂਟਿੰਗ

## ਸੰਦਰਭ

- [Azure OpenAI ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK ਰਿਫਰੈਂਸ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ਦਸਤਾਵੇਜ਼](https://github.com/openai/openai-python)
- [ਸਟ੍ਰੀਮਿੰਗ ਕਮਪਲੀਸ਼ਨ ਗਾਈਡ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

