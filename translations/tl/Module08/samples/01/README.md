# Sample 01: Mabilis na Chat gamit ang OpenAI SDK

Isang simpleng halimbawa ng chat na nagpapakita kung paano gamitin ang OpenAI SDK kasama ang Microsoft Foundry Local para sa lokal na AI inference.

## Pangkalahatang-ideya

Ipinapakita ng sample na ito kung paano:
- Gamitin ang OpenAI Python SDK kasama ang Foundry Local
- Pamahalaan ang parehong Azure OpenAI at lokal na Foundry configurations
- Magpatupad ng tamang error handling at fallback strategies
- Gamitin ang FoundryLocalManager para sa pamamahala ng serbisyo

## Mga Kinakailangan

- **Foundry Local**: Naka-install at available sa PATH
- **Python**: Bersyon 3.8 o mas bago
- **Model**: Isang model na naka-load sa Foundry Local (hal., `phi-4-mini`)

## Pag-install

1. **I-set up ang Python environment:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **I-install ang mga dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **I-start ang Foundry Local service at mag-load ng model:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Paggamit

### Foundry Local (Default)

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


## Mga Tampok ng Code

### FoundryLocalManager Integration

Ginagamit ng sample ang opisyal na Foundry Local SDK para sa tamang pamamahala ng serbisyo:

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


### Error Handling

Matibay na error handling na may fallback sa manual configuration:
- Awtomatikong pagtuklas ng serbisyo
- Maayos na pag-degrade kung hindi available ang SDK
- Malinaw na mga mensahe ng error para sa troubleshooting

## Mga Environment Variable

| Variable | Deskripsyon | Default | Kinakailangan |
|----------|-------------|---------|---------------|
| `MODEL` | Model alias o pangalan | `phi-4-mini` | Hindi |
| `BASE_URL` | Foundry Local base URL | `http://localhost:8000` | Hindi |
| `API_KEY` | API key (karaniwang hindi kailangan para sa lokal) | `""` | Hindi |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | Para sa Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | Para sa Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API version | `2024-08-01-preview` | Hindi |

## Pag-aayos ng Problema

### Karaniwang Isyu

1. **"Hindi magamit ang Foundry SDK" na babala:**
   - I-install ang foundry-local-sdk: `pip install foundry-local-sdk`
   - O i-set ang mga environment variable para sa manual configuration

2. **Connection refused:**
   - Siguraduhing tumatakbo ang Foundry Local: `foundry service status`
   - Suriin kung may naka-load na model: `foundry service ps`

3. **Model hindi natagpuan:**
   - Ilista ang mga available na model: `foundry model list`
   - Mag-load ng model: `foundry model run phi-4-mini`

### Pagpapatunay

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Mga Sanggunian

- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-compatible API Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

