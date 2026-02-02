# Voorbeeld 01: Snelle Chat via OpenAI SDK

Een eenvoudig chatvoorbeeld dat laat zien hoe je de OpenAI SDK kunt gebruiken met Microsoft Foundry Local voor lokale AI-inferentie.

## Overzicht

Dit voorbeeld laat zien hoe je:
- De OpenAI Python SDK gebruikt met Foundry Local
- Zowel Azure OpenAI- als lokale Foundry-configuraties beheert
- Correcte foutafhandeling en fallbackstrategieën implementeert
- De FoundryLocalManager gebruikt voor servicemanagement

## Vereisten

- **Foundry Local**: Geïnstalleerd en beschikbaar in PATH
- **Python**: Versie 3.8 of later
- **Model**: Een model geladen in Foundry Local (bijv. `phi-4-mini`)

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

3. **Foundry Local-service starten en een model laden:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Gebruik

### Foundry Local (Standaard)

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

## Codekenmerken

### Integratie met FoundryLocalManager

Het voorbeeld maakt gebruik van de officiële Foundry Local SDK voor correct servicemanagement:

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

### Foutafhandeling

Robuuste foutafhandeling met fallback naar handmatige configuratie:
- Automatische serviceontdekking
- Soepele degradatie als de SDK niet beschikbaar is
- Duidelijke foutmeldingen voor probleemoplossing

## Omgevingsvariabelen

| Variabele | Beschrijving | Standaard | Vereist |
|-----------|--------------|-----------|---------|
| `MODEL` | Modelalias of naam | `phi-4-mini` | Nee |
| `BASE_URL` | Foundry Local basis-URL | `http://localhost:8000` | Nee |
| `API_KEY` | API-sleutel (meestal niet nodig voor lokaal) | `""` | Nee |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | Voor Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-sleutel | - | Voor Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API-versie | `2024-08-01-preview` | Nee |

## Probleemoplossing

### Veelvoorkomende problemen

1. **"Kon Foundry SDK niet gebruiken" waarschuwing:**
   - Installeer foundry-local-sdk: `pip install foundry-local-sdk`
   - Of stel omgevingsvariabelen in voor handmatige configuratie

2. **Verbinding geweigerd:**
   - Zorg ervoor dat Foundry Local actief is: `foundry service status`
   - Controleer of een model is geladen: `foundry service ps`

3. **Model niet gevonden:**
   - Lijst beschikbare modellen op: `foundry model list`
   - Laad een model: `foundry model run phi-4-mini`

### Verificatie

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referenties

- [Foundry Local Documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-compatibele API Referentie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

