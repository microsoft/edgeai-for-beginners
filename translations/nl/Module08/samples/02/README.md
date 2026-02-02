# Voorbeeld 02: OpenAI SDK-integratie

Toont geavanceerde integratie met de OpenAI Python SDK, met ondersteuning voor zowel Microsoft Foundry Local als Azure OpenAI, inclusief streamingreacties en correcte foutafhandeling.

## Overzicht

Dit voorbeeld laat zien:
- Naadloos schakelen tussen Foundry Local en Azure OpenAI
- Streaming chatcompleties voor een betere gebruikerservaring
- Correct gebruik van de FoundryLocalManager SDK
- Robuuste foutafhandeling en fallbackmechanismen
- Productieklaar codepatroon

## Vereisten

- **Foundry Local**: Geïnstalleerd en actief (voor lokale inferentie)
- **Python**: Versie 3.8 of later met OpenAI SDK
- **Azure OpenAI**: Geldige endpoint en API-sleutel (voor cloud-inferentie)

## Installatie

1. **Python-omgeving instellen:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Afhankelijkheden installeren:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local (voor lokale modus):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Gebruiksscenario's

### Foundry Local (Standaard)

**Optie 1: Gebruik FoundryLocalManager (Aanbevolen)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Optie 2: Handmatige configuratie**
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


## Codearchitectuur

### Client Factory Pattern

Het voorbeeld gebruikt een factory-patroon om geschikte clients te maken:

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


### Streamingreacties

Het voorbeeld demonstreert streaming voor realtime reactie-generatie:

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


## Omgevingsvariabelen

### Foundry Local Configuratie

| Variabele | Beschrijving | Standaard | Vereist |
|-----------|--------------|-----------|---------|
| `MODEL` | Modelalias om te gebruiken | `phi-4-mini` | Nee |
| `BASE_URL` | Foundry Local endpoint | `http://localhost:8000` | Nee |
| `API_KEY` | API-sleutel (optioneel voor lokaal) | `""` | Nee |

### Azure OpenAI Configuratie

| Variabele | Beschrijving | Standaard | Vereist |
|-----------|--------------|-----------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI resource endpoint | - | Ja |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-sleutel | - | Ja |
| `AZURE_OPENAI_API_VERSION` | API-versie | `2024-08-01-preview` | Nee |
| `MODEL` | Azure implementatienaam | `your-deployment-name` | Ja |

## Geavanceerde functies

### Automatische serviceherkenning

Het voorbeeld detecteert automatisch de juiste service op basis van omgevingsvariabelen:

1. **Azure-modus**: Als `AZURE_OPENAI_ENDPOINT` en `AZURE_OPENAI_API_KEY` zijn ingesteld
2. **Foundry SDK-modus**: Als Foundry Local SDK beschikbaar is
3. **Handmatige modus**: Terugval naar handmatige configuratie

### Foutafhandeling

- Soepele terugval van SDK naar handmatige configuratie
- Duidelijke foutmeldingen voor probleemoplossing
- Correcte uitzonderingafhandeling voor netwerkproblemen
- Validatie van vereiste omgevingsvariabelen

## Prestatieoverwegingen

### Lokale versus cloud-afwegingen

**Voordelen van Foundry Local:**
- ✅ Geen API-kosten
- ✅ Gegevensprivacy (geen gegevens verlaten het apparaat)
- ✅ Lage latentie voor ondersteunde modellen
- ✅ Werkt offline

**Voordelen van Azure OpenAI:**
- ✅ Toegang tot de nieuwste grote modellen
- ✅ Hogere doorvoersnelheid
- ✅ Geen lokale computereisen
- ✅ Enterprise-grade SLA

## Probleemoplossing

### Veelvoorkomende problemen

1. **"Kon Foundry SDK niet gebruiken" waarschuwing:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure-authenticatiefouten:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model niet beschikbaar:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Gezondheidscontroles

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Volgende stappen

- **Voorbeeld 03**: Modelherkenning en benchmarking
- **Voorbeeld 04**: Een Chainlit RAG-applicatie bouwen
- **Voorbeeld 05**: Multi-agent orkestratie
- **Voorbeeld 06**: Modellen-als-tools routering

## Referenties

- [Azure OpenAI Documentatie](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referentie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Documentatie](https://github.com/openai/openai-python)
- [Streaming Completions Handleiding](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

