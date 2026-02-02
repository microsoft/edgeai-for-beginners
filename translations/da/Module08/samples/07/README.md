# Foundry Local som API Eksempel

Dette eksempel demonstrerer, hvordan man bruger Microsoft Foundry Local som en REST API-tjeneste uden at være afhængig af OpenAI SDK. Det viser direkte HTTP-integrationsmønstre for maksimal kontrol og tilpasning.

## Oversigt

Baseret på Microsofts officielle Foundry Local-mønstre tilbyder dette eksempel:
- Direkte REST API-integration med FoundryLocalManager
- Implementering af en tilpasset HTTP-klient
- Modelstyring og overvågning af sundhedstilstand
- Håndtering af streaming- og ikke-streaming-svar
- Produktionsklar fejlbehandling og retry-logik

## Forudsætninger

1. **Foundry Local Installation**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-afhængigheder**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arkitektur

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Nøglefunktioner

### 1. **Direkte HTTP-integration**
- Rene REST API-kald uden SDK-afhængigheder
- Tilpasset autentifikation og headers
- Fuld kontrol over anmodnings-/svarhåndtering

### 2. **Modelstyring**
- Dynamisk indlæsning og aflastning af modeller
- Overvågning af sundhedstilstand og statuskontroller
- Indsamling af præstationsmålinger

### 3. **Produktionsmønstre**
- Retry-mekanismer med eksponentiel backoff
- Circuit breaker for fejltolerance
- Omfattende logning og overvågning

### 4. **Fleksibel svarhåndtering**
- Streaming-svar til realtidsapplikationer
- Batch-behandling til scenarier med høj gennemstrømning
- Tilpasset parsing og validering af svar

## Eksempler på brug

### Grundlæggende API-integration
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

### Streaming-integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Overvågning af sundhedstilstand
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Filstruktur

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

## Microsoft Foundry Local Integration

Dette eksempel følger Microsofts officielle mønstre:

1. **SDK-integration**: Bruger `FoundryLocalManager` til tjenestestyring
2. **REST-endpoints**: Direkte kald til `/v1/chat/completions` og andre endpoints
3. **Autentifikation**: Korrekt håndtering af API-nøgler til lokale tjenester
4. **Modelstyring**: Kataloglister, download og indlæsningsmønstre
5. **Fejlbehandling**: Microsoft-anbefalede fejlkoder og svar

## Kom godt i gang

1. **Installer afhængigheder**
   ```bash
   pip install -r requirements.txt
   ```

2. **Kør grundlæggende eksempel**
   ```bash
   python examples/basic_usage.py
   ```

3. **Prøv streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Produktionsopsætning**
   ```bash
   python examples/production.py
   ```

## Konfiguration

Miljøvariabler til tilpasning:
- `FOUNDRY_MODEL`: Standardmodel der skal bruges (standard: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Timeout for anmodninger i sekunder (standard: 30)
- `FOUNDRY_RETRIES`: Antal retry-forsøg (standard: 3)
- `FOUNDRY_LOG_LEVEL`: Logniveau (standard: "INFO")

## Bedste praksis

1. **Forbindelseshåndtering**: Genbrug HTTP-forbindelser for bedre ydeevne
2. **Fejlbehandling**: Implementer korrekt retry-logik med eksponentiel backoff
3. **Ressourceovervågning**: Spor modelhukommelsesbrug og præstation
4. **Sikkerhed**: Brug korrekt autentifikation, selv for lokale tjenester
5. **Testning**: Inkluder både enhedstest og integrationstest

## Fejlfinding

### Almindelige problemer

**Tjenesten kører ikke**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemer med modellastning**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Forbindelsesfejl**
- Bekræft, at Foundry Local kører på den korrekte port
- Tjek firewall-indstillinger
- Sørg for korrekte autentifikationsheaders

## Optimering af ydeevne

1. **Forbindelsespooling**: Brug session-objekter til flere anmodninger
2. **Asynkrone operationer**: Udnyt asyncio til samtidige anmodninger
3. **Caching**: Cache model-svar, hvor det er passende
4. **Overvågning**: Spor svartider og juster timeouts

## Læringsmål

Efter at have gennemført dette eksempel vil du forstå:
- Direkte REST API-integration med Foundry Local
- Mønstre for implementering af tilpassede HTTP-klienter
- Produktionsklar fejlbehandling og overvågning
- Microsoft Foundry Local tjenestearkitektur
- Teknikker til optimering af ydeevne for lokale AI-tjenester

## Næste skridt

- Udforsk Eksempel 08: Windows 11 Chat-applikation
- Prøv Eksempel 09: Multi-Agent Orkestrering
- Lær Eksempel 10: Foundry Local som værktøjsintegration

---

