# Näidis 01: Kiirvestlus OpenAI SDK kaudu

Lihtne vestluse näide, mis demonstreerib, kuidas kasutada OpenAI SDK-d koos Microsoft Foundry Localiga lokaalse AI järelduse jaoks.

## Ülevaade

See näidis näitab, kuidas:
- Kasutada OpenAI Python SDK-d koos Foundry Localiga
- Hallata nii Azure OpenAI kui ka lokaalse Foundry konfiguratsioone
- Rakendada korrektset veakäsitlust ja varuplaanistrateegiaid
- Kasutada FoundryLocalManageri teenuse haldamiseks

## Eeltingimused

- **Foundry Local**: Paigaldatud ja PATH-is saadaval
- **Python**: Versioon 3.8 või uuem
- **Mudel**: Foundry Localis laaditud mudel (nt `phi-4-mini`)

## Paigaldamine

1. **Seadista Python keskkond:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Paigalda sõltuvused:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Käivita Foundry Local teenus ja laadi mudel:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Kasutamine

### Foundry Local (Vaikimisi)

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

## Koodi omadused

### FoundryLocalManageri integreerimine

Näidis kasutab ametlikku Foundry Local SDK-d korrektseks teenuse haldamiseks:

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

### Veakäsitlus

Tugev veakäsitlus koos varuplaaniga käsitsi konfiguratsioonile:
- Automaatne teenuse avastamine
- Sujuv degradeerumine, kui SDK pole saadaval
- Selged veateated tõrkeotsinguks

## Keskkonnamuutujad

| Muutuja | Kirjeldus | Vaikimisi | Nõutav |
|---------|-----------|-----------|--------|
| `MODEL` | Mudeli alias või nimi | `phi-4-mini` | Ei |
| `BASE_URL` | Foundry Locali baas-URL | `http://localhost:8000` | Ei |
| `API_KEY` | API võti (tavaliselt pole lokaalse jaoks vajalik) | `""` | Ei |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI lõpp-punkt | - | Azure jaoks |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API võti | - | Azure jaoks |
| `AZURE_OPENAI_API_VERSION` | Azure API versioon | `2024-08-01-preview` | Ei |

## Tõrkeotsing

### Levinud probleemid

1. **"Ei saanud kasutada Foundry SDK-d" hoiatus:**
   - Paigalda foundry-local-sdk: `pip install foundry-local-sdk`
   - Või määra keskkonnamuutujad käsitsi konfiguratsiooniks

2. **Ühendus keelatud:**
   - Veendu, et Foundry Local töötab: `foundry service status`
   - Kontrolli, kas mudel on laaditud: `foundry service ps`

3. **Mudelit ei leitud:**
   - Kuva saadaval olevad mudelid: `foundry model list`
   - Laadi mudel: `foundry model run phi-4-mini`

### Kontrollimine

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Viited

- [Foundry Local dokumentatsioon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-ühilduva API viide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.