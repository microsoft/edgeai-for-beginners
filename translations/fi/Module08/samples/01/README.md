# Esimerkki 01: Nopea keskustelu OpenAI SDK:n avulla

Yksinkertainen keskusteluesimerkki, joka näyttää, miten käyttää OpenAI SDK:ta Microsoft Foundry Localin kanssa paikalliseen AI-päätöksentekoon.

## Yleiskatsaus

Tämä esimerkki näyttää, miten:
- Käyttää OpenAI Python SDK:ta Foundry Localin kanssa
- Käsitellä sekä Azure OpenAI- että paikallisia Foundry-konfiguraatioita
- Toteuttaa asianmukainen virheenkäsittely ja varajärjestelmät
- Käyttää FoundryLocalManageria palvelun hallintaan

## Esivaatimukset

- **Foundry Local**: Asennettu ja saatavilla PATH:ssa
- **Python**: Versio 3.8 tai uudempi
- **Malli**: Malli ladattuna Foundry Localissa (esim. `phi-4-mini`)

## Asennus

1. **Aseta Python-ympäristö:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Asenna riippuvuudet:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Käynnistä Foundry Local -palvelu ja lataa malli:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Käyttö

### Foundry Local (Oletus)

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

## Koodin ominaisuudet

### FoundryLocalManager-integraatio

Esimerkki käyttää virallista Foundry Local SDK:ta palvelun hallintaan:

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

### Virheenkäsittely

Vahva virheenkäsittely varajärjestelmällä manuaaliseen konfigurointiin:
- Automaattinen palvelun tunnistus
- Sulava toiminnan heikentyminen, jos SDK ei ole käytettävissä
- Selkeät virheilmoitukset vianmääritystä varten

## Ympäristömuuttujat

| Muuttuja | Kuvaus | Oletus | Pakollinen |
|----------|-------------|---------|----------|
| `MODEL` | Mallin alias tai nimi | `phi-4-mini` | Ei |
| `BASE_URL` | Foundry Localin perus-URL | `http://localhost:8000` | Ei |
| `API_KEY` | API-avain (yleensä ei tarvita paikallisesti) | `""` | Ei |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI -päätepiste | - | Azurea varten |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI -API-avain | - | Azurea varten |
| `AZURE_OPENAI_API_VERSION` | Azure API -versio | `2024-08-01-preview` | Ei |

## Vianmääritys

### Yleiset ongelmat

1. **"Foundry SDK:ta ei voitu käyttää" -varoitus:**
   - Asenna foundry-local-sdk: `pip install foundry-local-sdk`
   - Tai aseta ympäristömuuttujat manuaalista konfigurointia varten

2. **Yhteys kielletty:**
   - Varmista, että Foundry Local on käynnissä: `foundry service status`
   - Tarkista, onko malli ladattu: `foundry service ps`

3. **Mallia ei löydy:**
   - Listaa saatavilla olevat mallit: `foundry model list`
   - Lataa malli: `foundry model run phi-4-mini`

### Varmistus

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Viitteet

- [Foundry Local -dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-yhteensopiva API-viite](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

