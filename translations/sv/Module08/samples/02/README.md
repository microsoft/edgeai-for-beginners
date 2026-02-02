# Exempel 02: OpenAI SDK Integration

Demonstrerar avancerad integration med OpenAI Python SDK, som stödjer både Microsoft Foundry Local och Azure OpenAI med strömmande svar och korrekt felhantering.

## Översikt

Det här exemplet visar:
- Smidig växling mellan Foundry Local och Azure OpenAI
- Strömmande chattkompletteringar för bättre användarupplevelse
- Korrekt användning av FoundryLocalManager SDK
- Robust felhantering och fallback-mekanismer
- Produktionsklara kodmönster

## Förutsättningar

- **Foundry Local**: Installerat och igång (för lokal inferens)
- **Python**: Version 3.8 eller senare med OpenAI SDK
- **Azure OpenAI**: Giltig endpoint och API-nyckel (för molninferens)

## Installation

1. **Ställ in Python-miljö:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installera beroenden:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Starta Foundry Local (för lokalt läge):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Användningsscenarier

### Foundry Local (Standard)

**Alternativ 1: Använd FoundryLocalManager (Rekommenderas)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Alternativ 2: Manuell konfiguration**
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


## Kodarkitektur

### Klientfabriksmönster

Exemplet använder ett fabriksmönster för att skapa lämpliga klienter:

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


### Strömmande svar

Exemplet demonstrerar strömning för realtidsgenerering av svar:

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


## Miljövariabler

### Foundry Local-konfiguration

| Variabel | Beskrivning | Standard | Obligatorisk |
|----------|-------------|----------|--------------|
| `MODEL` | Modellalias att använda | `phi-4-mini` | Nej |
| `BASE_URL` | Foundry Local endpoint | `http://localhost:8000` | Nej |
| `API_KEY` | API-nyckel (valfritt för lokalt) | `""` | Nej |

### Azure OpenAI-konfiguration

| Variabel | Beskrivning | Standard | Obligatorisk |
|----------|-------------|----------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI resurs-endpoint | - | Ja |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nyckel | - | Ja |
| `AZURE_OPENAI_API_VERSION` | API-version | `2024-08-01-preview` | Nej |
| `MODEL` | Azure deployment-namn | `your-deployment-name` | Ja |

## Avancerade funktioner

### Automatisk tjänstupptäckt

Exemplet upptäcker automatiskt lämplig tjänst baserat på miljövariabler:

1. **Azure-läge**: Om `AZURE_OPENAI_ENDPOINT` och `AZURE_OPENAI_API_KEY` är inställda
2. **Foundry SDK-läge**: Om Foundry Local SDK är tillgänglig
3. **Manuellt läge**: Fallback till manuell konfiguration

### Felhantering

- Smidig fallback från SDK till manuell konfiguration
- Tydliga felmeddelanden för felsökning
- Korrekt undantagshantering för nätverksproblem
- Validering av obligatoriska miljövariabler

## Prestandaöverväganden

### Lokalt vs molnfördelar

**Fördelar med Foundry Local:**
- ✅ Inga API-kostnader
- ✅ Dataintegritet (ingen data lämnar enheten)
- ✅ Låg latens för stödda modeller
- ✅ Fungerar offline

**Fördelar med Azure OpenAI:**
- ✅ Tillgång till de senaste stora modellerna
- ✅ Högre genomströmning
- ✅ Inga lokala beräkningskrav
- ✅ Företagsklassad SLA

## Felsökning

### Vanliga problem

1. **"Kunde inte använda Foundry SDK"-varning:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Autentiseringsfel med Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modell ej tillgänglig:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Hälsokontroller

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Nästa steg

- **Exempel 03**: Modellupptäckt och benchmarking
- **Exempel 04**: Bygga en Chainlit RAG-applikation
- **Exempel 05**: Orkestrering av flera agenter
- **Exempel 06**: Modell-som-verktyg-routing

## Referenser

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referens](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Dokumentation](https://github.com/openai/openai-python)
- [Guide för strömmande kompletteringar](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

