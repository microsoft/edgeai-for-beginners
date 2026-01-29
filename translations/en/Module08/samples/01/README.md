# Sample 01: Quick Chat via OpenAI SDK

A simple chat example demonstrating how to use the OpenAI SDK with Microsoft Foundry Local for local AI inference.

## Overview

This sample demonstrates how to:
- Use the OpenAI Python SDK with Foundry Local
- Manage configurations for both Azure OpenAI and local Foundry setups
- Implement effective error handling and fallback strategies
- Utilize FoundryLocalManager for service management

## Prerequisites

- **Foundry Local**: Installed and accessible via PATH
- **Python**: Version 3.8 or later
- **Model**: A model loaded in Foundry Local (e.g., `phi-4-mini`)

## Installation

1. **Set up the Python environment:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install required dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start the Foundry Local service and load a model:**
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

This sample leverages the official Foundry Local SDK for efficient service management:

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

Includes robust error handling with fallback mechanisms:
- Automatic service discovery
- Graceful degradation if the SDK is unavailable
- Clear error messages to aid troubleshooting

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MODEL` | Model alias or name | `phi-4-mini` | No |
| `BASE_URL` | Foundry Local base URL | `http://localhost:8000` | No |
| `API_KEY` | API key (typically not needed for local use) | `""` | No |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | For Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | For Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API version | `2024-08-01-preview` | No |

## Troubleshooting

### Common Issues

1. **"Could not use Foundry SDK" warning:**
   - Install the Foundry Local SDK: `pip install foundry-local-sdk`
   - Alternatively, set environment variables for manual configuration

2. **Connection refused:**
   - Verify Foundry Local is running: `foundry service status`
   - Check if a model is loaded: `foundry service ps`

3. **Model not found:**
   - List available models: `foundry model list`
   - Load a model: `foundry model run phi-4-mini`

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

