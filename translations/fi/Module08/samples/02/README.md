# Esimerkki 02: OpenAI SDK -integraatio

Esittelee edistyneen integraation OpenAI Python SDK:n kanssa, tukien sekä Microsoft Foundry Localia että Azure OpenAI:ta suoratoistovastauksilla ja asianmukaisella virheenkäsittelyllä.

## Yleiskatsaus

Tämä esimerkki esittelee:
- Saumattoman siirtymisen Foundry Localin ja Azure OpenAI:n välillä
- Suoratoistochat-vastaukset paremman käyttökokemuksen saavuttamiseksi
- FoundryLocalManager SDK:n asianmukaisen käytön
- Vankan virheenkäsittelyn ja varajärjestelmät
- Tuotantovalmiit koodimallit

## Esivaatimukset

- **Foundry Local**: Asennettu ja käynnissä (paikallista inferenssiä varten)
- **Python**: Versio 3.8 tai uudempi OpenAI SDK:lla
- **Azure OpenAI**: Voimassa oleva päätepiste ja API-avain (pilvi-inferenssiä varten)

## Asennus

1. **Luo Python-ympäristö:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Asenna riippuvuudet:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Käynnistä Foundry Local (paikallista tilaa varten):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Käyttötilanteet

### Foundry Local (Oletus)

**Vaihtoehto 1: Käyttämällä FoundryLocalManageria (suositeltu)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Vaihtoehto 2: Manuaalinen konfigurointi**
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


## Koodin arkkitehtuuri

### Client Factory -malli

Esimerkki käyttää tehdasmallia luodakseen sopivat asiakkaat:

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


### Suoratoistovastaukset

Esimerkki näyttää suoratoiston reaaliaikaisen vastausten tuottamisen:

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


## Ympäristömuuttujat

### Foundry Local -konfiguraatio

| Muuttuja | Kuvaus | Oletus | Pakollinen |
|----------|--------|--------|------------|
| `MODEL` | Käytettävä mallialias | `phi-4-mini` | Ei |
| `BASE_URL` | Foundry Local -päätepiste | `http://localhost:8000` | Ei |
| `API_KEY` | API-avain (valinnainen paikallisesti) | `""` | Ei |

### Azure OpenAI -konfiguraatio

| Muuttuja | Kuvaus | Oletus | Pakollinen |
|----------|--------|--------|------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI -resurssin päätepiste | - | Kyllä |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-avain | - | Kyllä |
| `AZURE_OPENAI_API_VERSION` | API-versio | `2024-08-01-preview` | Ei |
| `MODEL` | Azure-jakelun nimi | `your-deployment-name` | Kyllä |

## Edistyneet ominaisuudet

### Automaattinen palvelun tunnistus

Esimerkki tunnistaa automaattisesti sopivan palvelun ympäristömuuttujien perusteella:

1. **Azure-tila**: Jos `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_API_KEY` on asetettu
2. **Foundry SDK -tila**: Jos Foundry Local SDK on saatavilla
3. **Manuaalinen tila**: Palautuu manuaaliseen konfigurointiin

### Virheenkäsittely

- Sulava siirtyminen SDK:sta manuaaliseen konfigurointiin
- Selkeät virheilmoitukset vianmääritystä varten
- Asianmukainen poikkeusten käsittely verkkoyhteysongelmissa
- Pakollisten ympäristömuuttujien validointi

## Suorituskykyhuomiot

### Paikallisen ja pilvipalvelun vertailu

**Foundry Local -edut:**
- ✅ Ei API-kustannuksia
- ✅ Tietosuoja (data ei poistu laitteelta)
- ✅ Matala viive tuetuilla malleilla
- ✅ Toimii offline-tilassa

**Azure OpenAI -edut:**
- ✅ Pääsy uusimpiin suuriin malleihin
- ✅ Korkeampi läpimeno
- ✅ Ei paikallisia laskentavaatimuksia
- ✅ Yritystason SLA

## Vianmääritys

### Yleiset ongelmat

1. **"Foundry SDK:ta ei voitu käyttää" -varoitus:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure-todennusvirheet:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Malli ei saatavilla:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Terveystarkistukset

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Seuraavat askeleet

- **Esimerkki 03**: Mallien tunnistus ja suorituskykytestaus
- **Esimerkki 04**: Chainlit RAG -sovelluksen rakentaminen
- **Esimerkki 05**: Moniagenttien orkestrointi
- **Esimerkki 06**: Mallien reititys työkaluna

## Viitteet

- [Azure OpenAI -dokumentaatio](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK -viite](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK -dokumentaatio](https://github.com/openai/openai-python)
- [Suoratoistovastausten opas](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

