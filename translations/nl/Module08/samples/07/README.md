# Foundry Local als API Voorbeeld

Dit voorbeeld laat zien hoe je Microsoft Foundry Local kunt gebruiken als een REST API-service zonder afhankelijk te zijn van de OpenAI SDK. Het toont directe HTTP-integratiepatronen voor maximale controle en maatwerk.

## Overzicht

Gebaseerd op de officiële Foundry Local-patronen van Microsoft biedt dit voorbeeld:
- Directe REST API-integratie met FoundryLocalManager
- Eigen implementatie van een HTTP-client
- Modelbeheer en gezondheidsmonitoring
- Streaming- en niet-streamingresponsverwerking
- Productieklaar foutafhandelings- en retry-logica

## Vereisten

1. **Foundry Local Installatie**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Afhankelijkheden**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architectuur

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Belangrijke Kenmerken

### 1. **Directe HTTP-integratie**
- Pure REST API-aanroepen zonder SDK-afhankelijkheden
- Eigen authenticatie en headers
- Volledige controle over verzoek- en responsverwerking

### 2. **Modelbeheer**
- Dynamisch laden en ontladen van modellen
- Gezondheidsmonitoring en statuscontroles
- Verzameling van prestatiemetrics

### 3. **Productiepatronen**
- Retry-mechanismen met exponentiële backoff
- Circuit breaker voor fouttolerantie
- Uitgebreide logging en monitoring

### 4. **Flexibele Responsverwerking**
- Streamingresponsen voor realtime toepassingen
- Batchverwerking voor scenario's met hoge doorvoer
- Eigen responsparsing en validatie

## Gebruik Voorbeelden

### Basis API-integratie
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

### Streaming-integratie
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Gezondheidsmonitoring
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Bestandsstructuur

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

## Microsoft Foundry Local Integratie

Dit voorbeeld volgt de officiële patronen van Microsoft:

1. **SDK-integratie**: Gebruikt `FoundryLocalManager` voor servicemanagement
2. **REST Endpoints**: Directe aanroepen naar `/v1/chat/completions` en andere endpoints
3. **Authenticatie**: Correcte API-sleutelverwerking voor lokale services
4. **Modelbeheer**: Cataloguslijst, downloaden en laadpatronen
5. **Foutafhandeling**: Door Microsoft aanbevolen foutcodes en responsen

## Aan de slag

1. **Installeer Afhankelijkheden**
   ```bash
   pip install -r requirements.txt
   ```

2. **Voer Basisvoorbeeld Uit**
   ```bash
   python examples/basic_usage.py
   ```

3. **Probeer Streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Productie Setup**
   ```bash
   python examples/production.py
   ```

## Configuratie

Omgevingsvariabelen voor aanpassing:
- `FOUNDRY_MODEL`: Standaardmodel om te gebruiken (standaard: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Verzoek-timeout in seconden (standaard: 30)
- `FOUNDRY_RETRIES`: Aantal retry-pogingen (standaard: 3)
- `FOUNDRY_LOG_LEVEL`: Logniveau (standaard: "INFO")

## Beste Praktijken

1. **Verbindingsbeheer**: Hergebruik HTTP-verbindingen voor betere prestaties
2. **Foutafhandeling**: Implementeer correcte retry-logica met exponentiële backoff
3. **Resource Monitoring**: Houd het geheugengebruik en de prestaties van modellen bij
4. **Beveiliging**: Gebruik correcte authenticatie, zelfs voor lokale services
5. **Testen**: Voeg zowel unit- als integratietests toe

## Probleemoplossing

### Veelvoorkomende Problemen

**Service Niet Actief**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemen met Model Laden**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Verbindingsfouten**
- Controleer of Foundry Local actief is op de juiste poort
- Controleer firewallinstellingen
- Zorg voor correcte authenticatieheaders

## Prestatieoptimalisatie

1. **Verbindingspooling**: Gebruik sessieobjecten voor meerdere verzoeken
2. **Async Operaties**: Maak gebruik van asyncio voor gelijktijdige verzoeken
3. **Caching**: Cache modelresponsen waar nodig
4. **Monitoring**: Houd responstijden bij en pas timeouts aan

## Leerresultaten

Na het voltooien van dit voorbeeld begrijp je:
- Directe REST API-integratie met Foundry Local
- Patronen voor eigen HTTP-clientimplementatie
- Productieklaar foutafhandelings- en monitoringsmechanismen
- Microsoft Foundry Local servicearchitectuur
- Technieken voor prestatieoptimalisatie voor lokale AI-services

## Volgende Stappen

- Verken Voorbeeld 08: Windows 11 Chat Applicatie
- Probeer Voorbeeld 09: Multi-Agent Orchestratie
- Leer Voorbeeld 10: Foundry Local als Tools Integratie

---

