# Pavyzdys 01: Greitas pokalbis naudojant OpenAI SDK

Paprastas pokalbio pavyzdys, parodantis, kaip naudoti OpenAI SDK su Microsoft Foundry Local vietinei AI analizei.

## Apžvalga

Šiame pavyzdyje parodoma, kaip:
- Naudoti OpenAI Python SDK su Foundry Local
- Tvarkyti tiek Azure OpenAI, tiek vietines Foundry konfigūracijas
- Įgyvendinti tinkamą klaidų tvarkymą ir atsarginės strategijas
- Naudoti FoundryLocalManager paslaugų valdymui

## Reikalavimai

- **Foundry Local**: Įdiegta ir pasiekiama per PATH
- **Python**: 3.8 ar naujesnė versija
- **Modelis**: Modelis, įkeltas į Foundry Local (pvz., `phi-4-mini`)

## Įdiegimas

1. **Sukurkite Python aplinką:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Įdiekite priklausomybes:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Paleiskite Foundry Local paslaugą ir įkelkite modelį:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Naudojimas

### Foundry Local (Numatytasis)

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


## Kodo funkcijos

### FoundryLocalManager integracija

Pavyzdyje naudojamas oficialus Foundry Local SDK tinkamam paslaugų valdymui:

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


### Klaidų tvarkymas

Patikimas klaidų tvarkymas su atsargine galimybe rankinei konfigūracijai:
- Automatinis paslaugų aptikimas
- Sklandus veikimas, jei SDK nepasiekiamas
- Aiškūs klaidų pranešimai problemų sprendimui

## Aplinkos kintamieji

| Kintamasis | Aprašymas | Numatytoji reikšmė | Privaloma |
|------------|-----------|--------------------|-----------|
| `MODEL` | Modelio alias arba pavadinimas | `phi-4-mini` | Ne |
| `BASE_URL` | Foundry Local bazinis URL | `http://localhost:8000` | Ne |
| `API_KEY` | API raktas (dažniausiai nereikalingas vietiniam naudojimui) | `""` | Ne |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI galinis taškas | - | Azure atveju |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API raktas | - | Azure atveju |
| `AZURE_OPENAI_API_VERSION` | Azure API versija | `2024-08-01-preview` | Ne |

## Problemų sprendimas

### Dažnos problemos

1. **Įspėjimas "Nepavyko naudoti Foundry SDK":**
   - Įdiekite foundry-local-sdk: `pip install foundry-local-sdk`
   - Arba nustatykite aplinkos kintamuosius rankinei konfigūracijai

2. **Ryšys atmestas:**
   - Įsitikinkite, kad Foundry Local veikia: `foundry service status`
   - Patikrinkite, ar modelis įkeltas: `foundry service ps`

3. **Modelis nerastas:**
   - Peržiūrėkite galimus modelius: `foundry model list`
   - Įkelkite modelį: `foundry model run phi-4-mini`

### Patikrinimas

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Nuorodos

- [Foundry Local dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI suderinamos API nuorodos](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

