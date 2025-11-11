<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fb649a75048715165e76e20b366620a9",
  "translation_date": "2025-11-11T18:00:52+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "pcm"
}
-->
# Sample 01: Quick Chat wit OpenAI SDK

Dis na simple chat example wey dey show how pesin fit use OpenAI SDK wit Microsoft Foundry Local for local AI inference.

## Overview

Dis sample dey show how to:
- Use OpenAI Python SDK wit Foundry Local
- Manage both Azure OpenAI and local Foundry configurations
- Do correct error handling and fallback strategies
- Use FoundryLocalManager for service management

## Prerequisites

- **Foundry Local**: E don dey installed and dey available for PATH
- **Python**: Version 3.8 or higher
- **Model**: Model wey don load for Foundry Local (e.g., `phi-4-mini`)

## Installation

1. **Set up Python environment:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local service and load model:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Usage

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

## Code Features

### FoundryLocalManager Integration

Dis sample dey use official Foundry Local SDK for correct service management:

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

E get strong error handling wit fallback to manual configuration:
- Automatic service discovery
- Graceful degradation if SDK no dey available
- Clear error messages for troubleshooting

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MODEL` | Model alias or name | `phi-4-mini` | No |
| `BASE_URL` | Foundry Local base URL | `http://localhost:8000` | No |
| `API_KEY` | API key (normally no dey needed for local) | `""` | No |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | For Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | For Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API version | `2024-08-01-preview` | No |

## Troubleshooting

### Common Issues

1. **"Fit no use Foundry SDK" warning:**
   - Install foundry-local-sdk: `pip install foundry-local-sdk`
   - Or set environment variables for manual configuration

2. **Connection refused:**
   - Make sure say Foundry Local dey run: `foundry service status`
   - Check if model don load: `foundry service ps`

3. **Model no dey:**
   - List available models: `foundry model list`
   - Load model: `foundry model run phi-4-mini`

### Verification

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## References

- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-compatible API Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no correct well. Di original dokyument wey dey im native language na di one wey you go take as di correct source. For important informashun, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->