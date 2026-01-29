# Eksempel 01: Hurtig Chat via OpenAI SDK

Et simpelt chat-eksempel, der demonstrerer, hvordan man bruger OpenAI SDK med Microsoft Foundry Local til lokal AI-inferens.

## Oversigt

Dette eksempel viser, hvordan man:
- Bruger OpenAI Python SDK med Foundry Local
- Håndterer både Azure OpenAI og lokale Foundry-konfigurationer
- Implementerer korrekt fejlhåndtering og fallback-strategier
- Bruger FoundryLocalManager til servicestyring

## Forudsætninger

- **Foundry Local**: Installeret og tilgængelig på PATH
- **Python**: Version 3.8 eller nyere
- **Model**: En model indlæst i Foundry Local (f.eks. `phi-4-mini`)

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

3. **Start Foundry Local-service og indlæs en model:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Brug

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

## Kodefunktioner

### FoundryLocalManager Integration

Eksemplet bruger den officielle Foundry Local SDK til korrekt servicestyring:

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

### Fejlhåndtering

Robust fejlhåndtering med fallback til manuel konfiguration:
- Automatisk serviceopdagelse
- Graciøs nedgradering, hvis SDK ikke er tilgængelig
- Klare fejlmeddelelser til fejlfinding

## Miljøvariabler

| Variabel | Beskrivelse | Standard | Påkrævet |
|----------|-------------|----------|----------|
| `MODEL` | Model-alias eller navn | `phi-4-mini` | Nej |
| `BASE_URL` | Foundry Local base-URL | `http://localhost:8000` | Nej |
| `API_KEY` | API-nøgle (normalt ikke nødvendig lokalt) | `""` | Nej |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint | - | For Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nøgle | - | For Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API-version | `2024-08-01-preview` | Nej |

## Fejlfinding

### Almindelige Problemer

1. **Advarsel: "Kunne ikke bruge Foundry SDK":**
   - Installer foundry-local-sdk: `pip install foundry-local-sdk`
   - Eller opsæt miljøvariabler til manuel konfiguration

2. **Forbindelse nægtet:**
   - Sørg for, at Foundry Local kører: `foundry service status`
   - Tjek om en model er indlæst: `foundry service ps`

3. **Model ikke fundet:**
   - List tilgængelige modeller: `foundry model list`
   - Indlæs en model: `foundry model run phi-4-mini`

### Verifikation

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referencer

- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-kompatibel API Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

