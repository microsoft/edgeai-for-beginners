# Foundry Local API-esimerkki

Tämä esimerkki näyttää, kuinka Microsoft Foundry Localia voidaan käyttää REST API -palveluna ilman OpenAI SDK:ta. Se esittelee suorat HTTP-integraatiomallit maksimaalisen hallinnan ja räätälöinnin saavuttamiseksi.

## Yleiskatsaus

Microsoftin virallisiin Foundry Local -malleihin perustuen tämä esimerkki tarjoaa:
- Suoran REST API -integraation FoundryLocalManagerin kanssa
- Mukautetun HTTP-asiakasohjelman toteutuksen
- Mallien hallinnan ja terveyden seurannan
- Vastausten käsittelyn suoratoistolla ja ilman suoratoistoa
- Tuotantovalmiin virheenkäsittelyn ja uudelleenyrittämislogiikan

## Esivaatimukset

1. **Foundry Local -asennus**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-riippuvuudet**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arkkitehtuuri

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Keskeiset ominaisuudet

### 1. **Suora HTTP-integraatio**
- Pelkät REST API -kutsut ilman SDK-riippuvuuksia
- Mukautettu autentikointi ja otsikot
- Täysi hallinta pyyntöjen ja vastausten käsittelyssä

### 2. **Mallien hallinta**
- Dynaaminen mallien lataus ja poisto
- Terveyden seuranta ja tilan tarkistukset
- Suorituskykymetriikoiden kerääminen

### 3. **Tuotantokäytännöt**
- Uudelleenyrittämismekanismit eksponentiaalisella viiveellä
- Piirikatkaisija vikasietoisuutta varten
- Kattava lokitus ja seuranta

### 4. **Joustava vastausten käsittely**
- Suoratoistovastaukset reaaliaikaisiin sovelluksiin
- Eräkäsittely korkean läpimenon skenaarioihin
- Mukautettu vastausten jäsennys ja validointi

## Käyttöesimerkit

### Perus API-integraatio
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Suoratoistointegraatio
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Terveyden seuranta
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Tiedostorakenne

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local -integraatio

Tämä esimerkki noudattaa Microsoftin virallisia malleja:

1. **SDK-integraatio**: Käyttää `FoundryLocalManager`-luokkaa palvelun hallintaan
2. **REST-päätepisteet**: Suorat kutsut `/v1/chat/completions` ja muihin päätepisteisiin
3. **Autentikointi**: Oikea API-avaimen käsittely paikallisille palveluille
4. **Mallien hallinta**: Katalogin listaus, lataus ja latausmallit
5. **Virheenkäsittely**: Microsoftin suosittelemiin virhekoodeihin ja vastauksiin perustuva käsittely

## Aloitus

1. **Asenna riippuvuudet**
   ```bash
   pip install -r requirements.txt
   ```

2. **Suorita perusesimerkki**
   ```bash
   python examples/basic_usage.py
   ```

3. **Kokeile suoratoistoa**
   ```bash
   python examples/streaming.py
   ```

4. **Tuotantokokoonpano**
   ```bash
   python examples/production.py
   ```

## Konfiguraatio

Ympäristömuuttujat mukautusta varten:
- `FOUNDRY_MODEL`: Oletusmalli (oletus: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Pyynnön aikakatkaisu sekunneissa (oletus: 30)
- `FOUNDRY_RETRIES`: Uudelleenyrittämiskertojen määrä (oletus: 3)
- `FOUNDRY_LOG_LEVEL`: Lokitustaso (oletus: "INFO")

## Parhaat käytännöt

1. **Yhteydenhallinta**: Käytä uudelleen HTTP-yhteyksiä paremman suorituskyvyn saavuttamiseksi
2. **Virheenkäsittely**: Toteuta oikea uudelleenyrittämislogiikka eksponentiaalisella viiveellä
3. **Resurssien seuranta**: Seuraa mallien muistinkäyttöä ja suorituskykyä
4. **Turvallisuus**: Käytä asianmukaista autentikointia myös paikallisissa palveluissa
5. **Testaus**: Sisällytä sekä yksikkö- että integraatiotestit

## Vianmääritys

### Yleiset ongelmat

**Palvelu ei käynnissä**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Mallien latausongelmat**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Yhteysvirheet**
- Varmista, että Foundry Local toimii oikealla portilla
- Tarkista palomuuriasetukset
- Varmista, että autentikointiotsoissa ei ole virheitä

## Suorituskyvyn optimointi

1. **Yhteyspoolaus**: Käytä istunto-objekteja useisiin pyyntöihin
2. **Asynkroniset toiminnot**: Hyödynnä asyncioa rinnakkaisiin pyyntöihin
3. **Välimuisti**: Välimuistita mallivastaukset tarvittaessa
4. **Seuranta**: Seuraa vasteaikoja ja säädä aikakatkaisuja

## Oppimistulokset

Tämän esimerkin jälkeen ymmärrät:
- Suoran REST API -integraation Foundry Localin kanssa
- Mukautetut HTTP-asiakasohjelman toteutusmallit
- Tuotantovalmiin virheenkäsittelyn ja seurannan
- Microsoft Foundry Local -palvelun arkkitehtuurin
- Suorituskyvyn optimointitekniikat paikallisille AI-palveluille

## Seuraavat askeleet

- Tutustu esimerkkiin 08: Windows 11 -keskustelusovellus
- Kokeile esimerkkiä 09: Moniagenttiorganisointi
- Opi esimerkistä 10: Foundry Local työkalujen integraationa

---

