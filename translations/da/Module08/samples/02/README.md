# Eksempel 02: OpenAI SDK Integration

Demonstrerer avanceret integration med OpenAI Python SDK, der understøtter både Microsoft Foundry Local og Azure OpenAI med streaming-svar og korrekt fejlhåndtering.

## Oversigt

Dette eksempel fremhæver:
- Problemfri skift mellem Foundry Local og Azure OpenAI
- Streaming af chat-svar for bedre brugeroplevelse
- Korrekt brug af FoundryLocalManager SDK
- Robust fejlhåndtering og fallback-mekanismer
- Produktionsklare kode-mønstre

## Forudsætninger

- **Foundry Local**: Installeret og kørende (til lokal inferens)
- **Python**: Version 3.8 eller nyere med OpenAI SDK
- **Azure OpenAI**: Gyldig endpoint og API-nøgle (til cloud-inferens)

## Installation

1. **Opsæt Python-miljø:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installer afhængigheder:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local (til lokal tilstand):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Anvendelsesscenarier

### Foundry Local (Standard)

**Mulighed 1: Brug af FoundryLocalManager (Anbefalet)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Mulighed 2: Manuel konfiguration**
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

## Kodearkitektur

### Client Factory Pattern

Eksemplet bruger en factory pattern til at oprette passende klienter:

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

### Streaming-svar

Eksemplet demonstrerer streaming for realtids-generering af svar:

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

## Miljøvariabler

### Foundry Local Konfiguration

| Variabel | Beskrivelse | Standard | Påkrævet |
|----------|-------------|----------|----------|
| `MODEL` | Model-alias der skal bruges | `phi-4-mini` | Nej |
| `BASE_URL` | Foundry Local endpoint | `http://localhost:8000` | Nej |
| `API_KEY` | API-nøgle (valgfri for lokal) | `""` | Nej |

### Azure OpenAI Konfiguration

| Variabel | Beskrivelse | Standard | Påkrævet |
|----------|-------------|----------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ressource endpoint | - | Ja |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nøgle | - | Ja |
| `AZURE_OPENAI_API_VERSION` | API-version | `2024-08-01-preview` | Nej |
| `MODEL` | Azure deployment navn | `your-deployment-name` | Ja |

## Avancerede Funktioner

### Automatisk Service Discovery

Eksemplet registrerer automatisk den passende service baseret på miljøvariabler:

1. **Azure Mode**: Hvis `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_API_KEY` er sat
2. **Foundry SDK Mode**: Hvis Foundry Local SDK er tilgængelig
3. **Manuel Mode**: Fallback til manuel konfiguration

### Fejlhåndtering

- Smidig fallback fra SDK til manuel konfiguration
- Klare fejlmeddelelser til fejlfinding
- Korrekt undtagelseshåndtering for netværksproblemer
- Validering af påkrævede miljøvariabler

## Ydeevneovervejelser

### Lokal vs Cloud Trade-offs

**Fordele ved Foundry Local:**
- ✅ Ingen API-omkostninger
- ✅ Databeskyttelse (ingen data forlader enheden)
- ✅ Lav ventetid for understøttede modeller
- ✅ Fungerer offline

**Fordele ved Azure OpenAI:**
- ✅ Adgang til de nyeste store modeller
- ✅ Højere gennemløb
- ✅ Ingen lokale computerkrav
- ✅ Enterprise-grade SLA

## Fejlfinding

### Almindelige Problemer

1. **"Kunne ikke bruge Foundry SDK" advarsel:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure autentificeringsfejl:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model ikke tilgængelig:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Sundhedstjek

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Næste Skridt

- **Eksempel 03**: Modelopdagelse og benchmarking
- **Eksempel 04**: Opbygning af en Chainlit RAG-applikation
- **Eksempel 05**: Multi-agent orkestrering
- **Eksempel 06**: Routing af modeller som værktøjer

## Referencer

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Dokumentation](https://github.com/openai/openai-python)
- [Streaming Completions Guide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

