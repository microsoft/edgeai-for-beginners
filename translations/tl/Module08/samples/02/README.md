# Sample 02: OpenAI SDK Integration

Nagpapakita ng advanced na integrasyon gamit ang OpenAI Python SDK, na sumusuporta sa parehong Microsoft Foundry Local at Azure OpenAI na may streaming responses at tamang paghawak ng error.

## Overview

Ipinapakita ng sample na ito:
- Madaling paglipat sa pagitan ng Foundry Local at Azure OpenAI
- Streaming chat completions para sa mas magandang karanasan ng user
- Tamang paggamit ng FoundryLocalManager SDK
- Matibay na paghawak ng error at fallback mechanisms
- Mga code pattern na handa para sa produksyon

## Mga Kinakailangan

- **Foundry Local**: Naka-install at tumatakbo (para sa lokal na inference)
- **Python**: Bersyon 3.8 o mas bago na may OpenAI SDK
- **Azure OpenAI**: Valid na endpoint at API key (para sa cloud inference)

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

3. **Simulan ang Foundry Local (para sa lokal na mode):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Mga Scenario ng Paggamit

### Foundry Local (Default)

**Opsyon 1: Gamit ang FoundryLocalManager (Inirerekomenda)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opsyon 2: Manual na Konfigurasyon**
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

## Arkitektura ng Code

### Client Factory Pattern

Ginagamit ng sample ang factory pattern para gumawa ng angkop na mga kliyente:

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

Ipinapakita ng sample ang streaming para sa real-time na pagbuo ng mga sagot:

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

## Mga Environment Variable

### Konfigurasyon ng Foundry Local

| Variable | Deskripsyon | Default | Kinakailangan |
|----------|-------------|---------|---------------|
| `MODEL` | Model alias na gagamitin | `phi-4-mini` | Hindi |
| `BASE_URL` | Foundry Local endpoint | `http://localhost:8000` | Hindi |
| `API_KEY` | API key (opsyonal para sa lokal) | `""` | Hindi |

### Konfigurasyon ng Azure OpenAI

| Variable | Deskripsyon | Default | Kinakailangan |
|----------|-------------|---------|---------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI resource endpoint | - | Oo |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | - | Oo |
| `AZURE_OPENAI_API_VERSION` | Bersyon ng API | `2024-08-01-preview` | Hindi |
| `MODEL` | Azure deployment name | `your-deployment-name` | Oo |

## Mga Advanced na Tampok

### Automatic Service Discovery

Awtomatikong natutukoy ng sample ang angkop na serbisyo batay sa mga environment variable:

1. **Azure Mode**: Kapag naka-set ang `AZURE_OPENAI_ENDPOINT` at `AZURE_OPENAI_API_KEY`
2. **Foundry SDK Mode**: Kapag available ang Foundry Local SDK
3. **Manual Mode**: Fallback sa manual na konfigurasyon

### Paghawak ng Error

- Maayos na fallback mula SDK patungo sa manual na konfigurasyon
- Malinaw na mga mensahe ng error para sa troubleshooting
- Tamang paghawak ng exception para sa mga isyu sa network
- Pag-validate ng mga kinakailangang environment variable

## Mga Pagsasaalang-alang sa Performance

### Lokal vs Cloud Trade-offs

**Mga Bentahe ng Foundry Local:**
- ✅ Walang gastos sa API
- ✅ Privacy ng data (walang data na lumalabas sa device)
- ✅ Mababang latency para sa mga suportadong modelo
- ✅ Gumagana offline

**Mga Bentahe ng Azure OpenAI:**
- ✅ Access sa pinakabagong malalaking modelo
- ✅ Mas mataas na throughput
- ✅ Walang kinakailangang lokal na compute
- ✅ Enterprise-grade SLA

## Pag-troubleshoot

### Mga Karaniwang Isyu

1. **"Could not use Foundry SDK" warning:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Mga error sa Azure authentication:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model hindi available:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Mga Health Check

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Mga Susunod na Hakbang

- **Sample 03**: Pagdiskubre ng modelo at benchmarking
- **Sample 04**: Pagbuo ng Chainlit RAG application
- **Sample 05**: Multi-agent orchestration
- **Sample 06**: Models-as-tools routing

## Mga Sanggunian

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Documentation](https://github.com/openai/openai-python)
- [Streaming Completions Guide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

