<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "03a45997306e55f466aa93ae0d4a1e25",
  "translation_date": "2025-12-16T00:41:13+00:00",
  "source_file": "Module08/samples/02/README.md",
  "language_code": "kn"
}
-->
# ಮಾದರಿ 02: OpenAI SDK ಏಕೀಕರಣ

OpenAI Python SDK ನೊಂದಿಗೆ ಉನ್ನತ ಮಟ್ಟದ ಏಕೀಕರಣವನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ, Microsoft Foundry Local ಮತ್ತು Azure OpenAI ಎರಡನ್ನೂ ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳೊಂದಿಗೆ ಮತ್ತು ಸರಿಯಾದ ದೋಷ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಬೆಂಬಲಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

ಈ ಮಾದರಿ ತೋರಿಸುತ್ತದೆ:
- Foundry Local ಮತ್ತು Azure OpenAI ನಡುವೆ ನಿರಂತರ ಸ್ವಿಚಿಂಗ್
- ಉತ್ತಮ ಬಳಕೆದಾರ ಅನುಭವಕ್ಕಾಗಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಚಾಟ್ ಪೂರ್ಣತೆಗಳು
- FoundryLocalManager SDK ಯ ಸರಿಯಾದ ಬಳಕೆ
- ಬಲವಾದ ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಬ್ಯಾಕ್ಅಪ್ ಯಂತ್ರಗಳು
- ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ ಕೋಡ್ ಮಾದರಿಗಳು

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- **Foundry Local**: ಸ್ಥಾಪಿತ ಮತ್ತು ಚಾಲನೆಯಲ್ಲಿದೆ (ಸ್ಥಳೀಯ ನಿರ್ಣಯಕ್ಕಾಗಿ)
- **Python**: 3.8 ಅಥವಾ ನಂತರದ OpenAI SDK ಜೊತೆಗೆ
- **Azure OpenAI**: ಮಾನ್ಯ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು API ಕೀ (ಮೇಘ ನಿರ್ಣಯಕ್ಕಾಗಿ)

## ಸ್ಥಾಪನೆ

1. **Python ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸಿ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ಆವಶ್ಯಕತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ಪ್ರಾರಂಭಿಸಿ (ಸ್ಥಳೀಯ ಮೋಡ್‌ಗಾಗಿ):**
   ```cmd
   foundry model run phi-4-mini
   ```

## ಬಳಕೆ ದೃಶ್ಯಗಳು

### Foundry Local (ಡೀಫಾಲ್ಟ್)

**ಆಯ್ಕೆ 1: FoundryLocalManager ಬಳಕೆ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ಆಯ್ಕೆ 2: ಕೈಯಿಂದ ಸಂರಚನೆ**
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

## ಕೋಡ್ ವಾಸ್ತುಶಿಲ್ಪ

### ಕ್ಲೈಂಟ್ ಫ್ಯಾಕ್ಟರಿ ಮಾದರಿ

ಮಾದರಿ ಸೂಕ್ತ ಕ್ಲೈಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಫ್ಯಾಕ್ಟರಿ ಮಾದರಿಯನ್ನು ಬಳಸುತ್ತದೆ:

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

### ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳು

ಮಾದರಿ ನೈಜ-ಸಮಯ ಪ್ರತಿಕ್ರಿಯೆ ಉತ್ಪಾದನೆಗಾಗಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಅನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ:

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

## ಪರಿಸರ ಚರಗಳು

### Foundry Local ಸಂರಚನೆ

| ಚರ | ವಿವರಣೆ | ಡೀಫಾಲ್ಟ್ | ಅಗತ್ಯವಿದೆ |
|----------|-------------|---------|----------|
| `MODEL` | ಬಳಸುವ ಮಾದರಿ ಅಲಿಯಾಸ್ | `phi-4-mini` | ಇಲ್ಲ |
| `BASE_URL` | Foundry Local ಎಂಡ್‌ಪಾಯಿಂಟ್ | `http://localhost:8000` | ಇಲ್ಲ |
| `API_KEY` | API ಕೀ (ಸ್ಥಳೀಯಕ್ಕೆ ಐಚ್ಛಿಕ) | `""` | ಇಲ್ಲ |

### Azure OpenAI ಸಂರಚನೆ

| ಚರ | ವಿವರಣೆ | ಡೀಫಾಲ್ಟ್ | ಅಗತ್ಯವಿದೆ |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ಸಂಪನ್ಮೂಲ ಎಂಡ್‌ಪಾಯಿಂಟ್ | - | ಹೌದು |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API ಕೀ | - | ಹೌದು |
| `AZURE_OPENAI_API_VERSION` | API ಆವೃತ್ತಿ | `2024-08-01-preview` | ಇಲ್ಲ |
| `MODEL` | Azure ನಿಯೋಜನೆ ಹೆಸರು | `your-deployment-name` | ಹೌದು |

## ಉನ್ನತ ವೈಶಿಷ್ಟ್ಯಗಳು

### ಸ್ವಯಂಚಾಲಿತ ಸೇವಾ ಪತ್ತೆ

ಮಾದರಿ ಪರಿಸರ ಚರಗಳ ಆಧಾರದ ಮೇಲೆ ಸೂಕ್ತ ಸೇವೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆಹಚ್ಚುತ್ತದೆ:

1. **Azure ಮೋಡ್**: `AZURE_OPENAI_ENDPOINT` ಮತ್ತು `AZURE_OPENAI_API_KEY` ಸೆಟ್ ಆಗಿದ್ದರೆ
2. **Foundry SDK ಮೋಡ್**: Foundry Local SDK ಲಭ್ಯವಿದ್ದರೆ
3. **ಕೈಯಿಂದ ಮೋಡ್**: ಕೈಯಿಂದ ಸಂರಚನೆಗೆ ಬ್ಯಾಕ್ಅಪ್

### ದೋಷ ನಿರ್ವಹಣೆ

- SDK ನಿಂದ ಕೈಯಿಂದ ಸಂರಚನೆಗೆ ಸೌಮ್ಯ ಬ್ಯಾಕ್ಅಪ್
- ಸಮಸ್ಯೆ ಪರಿಹಾರಕ್ಕಾಗಿ ಸ್ಪಷ್ಟ ದೋಷ ಸಂದೇಶಗಳು
- ನೆಟ್‌ವರ್ಕ್ ಸಮಸ್ಯೆಗಳಿಗೆ ಸರಿಯಾದ wyjąತ ನಿರ್ವಹಣೆ
- ಅಗತ್ಯವಿರುವ ಪರಿಸರ ಚರಗಳ ಮಾನ್ಯತೆ

## ಕಾರ್ಯಕ್ಷಮತೆ ಪರಿಗಣನೆಗಳು

### ಸ್ಥಳೀಯ ಮತ್ತು ಮೇಘ ವ್ಯವಹಾರಗಳು

**Foundry Local ಲಾಭಗಳು:**
- ✅ ಯಾವುದೇ API ವೆಚ್ಚವಿಲ್ಲ
- ✅ ಡೇಟಾ ಗೌಪ್ಯತೆ (ಯಂತ್ರದಿಂದ ಡೇಟಾ ಹೊರಬರದು)
- ✅ ಬೆಂಬಲಿತ ಮಾದರಿಗಳಿಗೆ ಕಡಿಮೆ ವಿಳಂಬ
- ✅ ಆಫ್‌ಲೈನ್ ಕಾರ್ಯಾಚರಣೆ

**Azure OpenAI ಲಾಭಗಳು:**
- ✅ ಇತ್ತೀಚಿನ ದೊಡ್ಡ ಮಾದರಿಗಳಿಗೆ ಪ್ರವೇಶ
- ✅ ಹೆಚ್ಚಿನ ಥ್ರೂಪುಟ್
- ✅ ಸ್ಥಳೀಯ ಗಣನೆ ಅಗತ್ಯವಿಲ್ಲ
- ✅ ಎಂಟರ್‌ಪ್ರೈಸ್-ಗ್ರೇಡ್ SLA

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು

1. **"Foundry SDK ಬಳಸಲಾಗಲಿಲ್ಲ" ಎಚ್ಚರಿಕೆ:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure ಪ್ರಮಾಣೀಕರಣ ದೋಷಗಳು:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **ಮಾದರಿ ಲಭ್ಯವಿಲ್ಲ:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### ಆರೋಗ್ಯ ಪರಿಶೀಲನೆಗಳು

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## ಮುಂದಿನ ಹಂತಗಳು

- **ಮಾದರಿ 03**: ಮಾದರಿ ಪತ್ತೆ ಮತ್ತು ಬೆಂಚ್ಮಾರ್ಕಿಂಗ್
- **ಮಾದರಿ 04**: ಚೈನ್‌ಲಿಟ್ RAG ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಾಣ
- **ಮಾದರಿ 05**: ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ
- **ಮಾದರಿ 06**: ಮಾದರಿಗಳನ್ನು ಉಪಕರಣಗಳಾಗಿ ಮಾರ್ಗದರ್ಶನ

## ಉಲ್ಲೇಖಗಳು

- [Azure OpenAI ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK ಉಲ್ಲೇಖ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/openai/openai-python)
- [ಸ್ಟ್ರೀಮಿಂಗ್ ಪೂರ್ಣತೆಗಳ ಮಾರ್ಗದರ್ಶಿ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->