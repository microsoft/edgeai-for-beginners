# Exempel 01: Snabbchatt via OpenAI SDK

Ett enkelt chatt-exempel som visar hur man använder OpenAI SDK med Microsoft Foundry Local för lokal AI-inferens.

## Översikt

Det här exemplet visar hur man:
- Använder OpenAI Python SDK med Foundry Local
- Hanterar både Azure OpenAI och lokala Foundry-konfigurationer
- Implementerar korrekt felhantering och fallback-strategier
- Använder FoundryLocalManager för tjänstehantering

## Förutsättningar

- **Foundry Local**: Installerat och tillgängligt på PATH
- **Python**: Version 3.8 eller senare
- **Modell**: En modell laddad i Foundry Local (t.ex. `phi-4-mini`)

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

3. **Starta Foundry Local-tjänsten och ladda en modell:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Användning

### Foundry Local (Standard)

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


## Kodfunktioner

### FoundryLocalManager Integration

Exemplet använder den officiella Foundry Local SDK för korrekt tjänstehantering:

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


### Felhantering

Robust felhantering med fallback till manuell konfiguration:
- Automatisk tjänstupptäckt
- Smidig nedgradering om SDK inte är tillgängligt
- Tydliga felmeddelanden för felsökning

## Miljövariabler

| Variabel | Beskrivning | Standard | Obligatorisk |
|----------|-------------|----------|--------------|
| `MODEL` | Modellalias eller namn | `phi-4-mini` | Nej |
| `BASE_URL` | Foundry Local bas-URL | `http://localhost:8000` | Nej |
| `API_KEY` | API-nyckel (vanligtvis inte nödvändig för lokal användning) | `""` | Nej |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI-endpoint | - | För Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nyckel | - | För Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API-version | `2024-08-01-preview` | Nej |

## Felsökning

### Vanliga problem

1. **"Kunde inte använda Foundry SDK"-varning:**
   - Installera foundry-local-sdk: `pip install foundry-local-sdk`
   - Eller ställ in miljövariabler för manuell konfiguration

2. **Anslutning nekad:**
   - Kontrollera att Foundry Local körs: `foundry service status`
   - Kontrollera att en modell är laddad: `foundry service ps`

3. **Modell hittades inte:**
   - Lista tillgängliga modeller: `foundry model list`
   - Ladda en modell: `foundry model run phi-4-mini`

### Verifiering

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Referenser

- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-kompatibel API-referens](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

