# Sample 02: OpenAI SDK Integration

E show how to do advanced integration wit OpenAI Python SDK, wey fit work wit Microsoft Foundry Local and Azure OpenAI, plus streaming response and correct way to handle error.

## Overview

Dis sample dey show:
- How to switch well between Foundry Local and Azure OpenAI
- Streaming chat completions wey go make user experience beta
- Correct use of FoundryLocalManager SDK
- Strong error handling and fallback system
- Code wey fit work for production

## Prerequisites

- **Foundry Local**: E don dey installed and dey run (for local inference)
- **Python**: Version 3.8 or higher wey get OpenAI SDK
- **Azure OpenAI**: Valid endpoint and API key (for cloud inference)

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

3. **Start Foundry Local (for local mode):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Usage Scenarios

### Foundry Local (Default)

**Option 1: Use FoundryLocalManager (Recommended)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Option 2: Manual Configuration**
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

## Code Architecture

### Client Factory Pattern

Dis sample dey use factory pattern to create correct clients:

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

### Streaming Responses

Dis sample dey show how to stream for real-time response generation:

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

## Environment Variables

### Foundry Local Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MODEL` | Model alias wey you go use | `phi-4-mini` | No |
| `BASE_URL` | Foundry Local endpoint | `http://localhost:8000` | No |
| `API_KEY` | API key (optional for local) | `""` | No |

### Azure OpenAI Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI resource endpoint | - | Yes |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | Yes |
| `AZURE_OPENAI_API_VERSION` | API version | `2024-08-01-preview` | No |
| `MODEL` | Azure deployment name | `your-deployment-name` | Yes |

## Advanced Features

### Automatic Service Discovery

Dis sample dey automatically detect correct service based on environment variables:

1. **Azure Mode**: If `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` dey set
2. **Foundry SDK Mode**: If Foundry Local SDK dey available
3. **Manual Mode**: E go fallback to manual configuration

### Error Handling

- E go fallback well from SDK to manual configuration
- E dey show clear error message for troubleshooting
- E dey handle exception well for network wahala
- E dey validate required environment variables

## Performance Considerations

### Local vs Cloud Trade-offs

**Foundry Local Advantages:**
- ✅ No API cost
- ✅ Data privacy (data no dey comot from device)
- ✅ Low latency for models wey e support
- ✅ E dey work offline

**Azure OpenAI Advantages:**
- ✅ Access to latest big models
- ✅ Higher throughput
- ✅ No need local compute
- ✅ Enterprise-grade SLA

## Troubleshooting

### Common Issues

1. **"Could not use Foundry SDK" warning:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure authentication errors:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model no dey available:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Health Checks

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Next Steps

- **Sample 03**: Model discovery and benchmarking
- **Sample 04**: How to build Chainlit RAG application
- **Sample 05**: Multi-agent orchestration
- **Sample 06**: Models-as-tools routing

## References

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Documentation](https://github.com/openai/openai-python)
- [Streaming Completions Guide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->