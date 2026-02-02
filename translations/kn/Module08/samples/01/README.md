# ಮಾದರಿ 01: OpenAI SDK ಮೂಲಕ ತ್ವರಿತ ಚಾಟ್

ಸ್ಥಳೀಯ AI ನಿರ್ಣಯಕ್ಕಾಗಿ Microsoft Foundry Local ಜೊತೆಗೆ OpenAI SDK ಅನ್ನು ಹೇಗೆ ಬಳಸುವುದು ಎಂಬುದನ್ನು ತೋರಿಸುವ ಸರಳ ಚಾಟ್ ಉದಾಹರಣೆ.

## ಅವಲೋಕನ

ಈ ಮಾದರಿ ಹೇಗೆ ಮಾಡುವುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತದೆ:
- Foundry Local ಜೊತೆಗೆ OpenAI Python SDK ಬಳಸುವುದು
- Azure OpenAI ಮತ್ತು ಸ್ಥಳೀಯ Foundry ಸಂರಚನೆಗಳನ್ನು ಎರಡನ್ನೂ ನಿರ್ವಹಿಸುವುದು
- ಸರಿಯಾದ ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಬ್ಯಾಕ್ಅಪ್ ತಂತ್ರಗಳನ್ನು ಜಾರಿಗೆ ತರುವುದು
- ಸೇವೆ ನಿರ್ವಹಣೆಗೆ FoundryLocalManager ಬಳಸುವುದು

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- **Foundry Local**: PATH ನಲ್ಲಿ ಸ್ಥಾಪಿತ ಮತ್ತು ಲಭ್ಯವಿದೆ
- **Python**: 3.8 ಅಥವಾ ನಂತರದ ಆವೃತ್ತಿ
- **ಮಾದರಿ**: Foundry Local ನಲ್ಲಿ ಲೋಡ್ ಮಾಡಲಾದ ಮಾದರಿ (ಉದಾ., `phi-4-mini`)

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

3. **Foundry Local ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ:**
   ```cmd
   foundry model run phi-4-mini
   ```

## ಬಳಕೆ

### Foundry Local (ಡೀಫಾಲ್ಟ್)

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

## ಕೋಡ್ ವೈಶಿಷ್ಟ್ಯಗಳು

### FoundryLocalManager ಏಕೀಕರಣ

ಸರಿಯಾದ ಸೇವೆ ನಿರ್ವಹಣೆಗೆ ಅಧಿಕೃತ Foundry Local SDK ಅನ್ನು ಈ ಮಾದರಿ ಬಳಸುತ್ತದೆ:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸಿ
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### ದೋಷ ನಿರ್ವಹಣೆ

ಮ್ಯಾನುಯಲ್ ಸಂರಚನೆಗೆ ಬ್ಯಾಕ್ಅಪ್ ಜೊತೆಗೆ ಬಲವಾದ ದೋಷ ನಿರ್ವಹಣೆ:
- ಸ್ವಯಂಚಾಲಿತ ಸೇವೆ ಪತ್ತೆಹಚ್ಚುವಿಕೆ
- SDK ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ ಸೌಮ್ಯ ಕುಸಿತ
- ಸಮಸ್ಯೆ ಪರಿಹಾರಕ್ಕಾಗಿ ಸ್ಪಷ್ಟ ದೋಷ ಸಂದೇಶಗಳು

## ಪರಿಸರ ಚರಗಳು

| ಚರ | ವಿವರಣೆ | ಡೀಫಾಲ್ಟ್ | ಅಗತ್ಯವಿದೆ |
|----------|-------------|---------|----------|
| `MODEL` | ಮಾದರಿ ಉಪನಾಮ ಅಥವಾ ಹೆಸರು | `phi-4-mini` | ಇಲ್ಲ |
| `BASE_URL` | Foundry Local ಮೂಲ URL | `http://localhost:8000` | ಇಲ್ಲ |
| `API_KEY` | API ಕೀ (ಸಾಮಾನ್ಯವಾಗಿ ಸ್ಥಳೀಯಕ್ಕೆ ಅಗತ್ಯವಿಲ್ಲ) | `""` | ಇಲ್ಲ |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ಎಂಡ್ಪಾಯಿಂಟ್ | - | Azure ಗಾಗಿ |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API ಕೀ | - | Azure ಗಾಗಿ |
| `AZURE_OPENAI_API_VERSION` | Azure API ಆವೃತ್ತಿ | `2024-08-01-preview` | ಇಲ್ಲ |

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು

1. **"Foundry SDK ಬಳಸಲಾಗಲಿಲ್ಲ" ಎಚ್ಚರಿಕೆ:**
   - foundry-local-sdk ಅನ್ನು ಸ್ಥಾಪಿಸಿ: `pip install foundry-local-sdk`
   - ಅಥವಾ ಮ್ಯಾನುಯಲ್ ಸಂರಚನೆಗಾಗಿ ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿಸಿ

2. **ಸಂಪರ್ಕ ನಿರಾಕರಿಸಲಾಗಿದೆ:**
   - Foundry Local ಚಾಲನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿ: `foundry service status`
   - ಮಾದರಿ ಲೋಡ್ ಆಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ: `foundry service ps`

3. **ಮಾದರಿ ಕಂಡುಬರಲಿಲ್ಲ:**
   - ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ: `foundry model list`
   - ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ: `foundry model run phi-4-mini`

### ಪರಿಶೀಲನೆ

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## ಉಲ್ಲೇಖಗಳು

- [Foundry Local ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-ಸಮ್ಮತ API ಉಲ್ಲೇಖ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->