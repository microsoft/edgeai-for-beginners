# Eksempel 01: Rask Chat via OpenAI SDK

Et enkelt chatteeksempel som demonstrerer hvordan man bruker OpenAI SDK med Microsoft Foundry Local for lokal AI-inferens.

## Oversikt

Dette eksemplet viser hvordan man:
- Bruker OpenAI Python SDK med Foundry Local
- Håndterer både Azure OpenAI- og lokale Foundry-konfigurasjoner
- Implementerer riktig feilhåndtering og fallback-strategier
- Bruker FoundryLocalManager for tjenestestyring

## Forutsetninger

- **Foundry Local**: Installert og tilgjengelig på PATH
- **Python**: Versjon 3.8 eller nyere
- **Modell**: En modell lastet inn i Foundry Local (f.eks. `phi-4-mini`)

## Installasjon

1. **Sett opp Python-miljø:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installer avhengigheter:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local-tjenesten og last inn en modell:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Bruk

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

## Kodefunksjoner

### FoundryLocalManager-integrasjon

Eksemplet bruker den offisielle Foundry Local SDK for riktig tjenestestyring:

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

### Feilhåndtering

Robust feilhåndtering med fallback til manuell konfigurasjon:
- Automatisk tjenesteoppdagelse
- Grasiøs degradering hvis SDK ikke er tilgjengelig
- Klare feilmeldinger for feilsøking

## Miljøvariabler

| Variabel | Beskrivelse | Standard | Påkrevd |
|----------|-------------|----------|---------|
| `MODEL` | Modellalias eller navn | `phi-4-mini` | Nei |
| `BASE_URL` | Foundry Local base-URL | `http://localhost:8000` | Nei |
| `API_KEY` | API-nøkkel (vanligvis ikke nødvendig lokalt) | `""` | Nei |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI-endepunkt | - | For Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nøkkel | - | For Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API-versjon | `2024-08-01-preview` | Nei |

## Feilsøking

### Vanlige problemer

1. **Advarsel: "Kunne ikke bruke Foundry SDK":**
   - Installer foundry-local-sdk: `pip install foundry-local-sdk`
   - Eller sett miljøvariabler for manuell konfigurasjon

2. **Tilkobling nektet:**
   - Sørg for at Foundry Local kjører: `foundry service status`
   - Sjekk om en modell er lastet inn: `foundry service ps`

3. **Modell ikke funnet:**
   - List tilgjengelige modeller: `foundry model list`
   - Last inn en modell: `foundry model run phi-4-mini`

### Verifisering

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referanser

- [Foundry Local Dokumentasjon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-kompatibel API-referanse](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

