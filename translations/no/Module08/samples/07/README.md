# Foundry Local som API-eksempel

Dette eksempelet viser hvordan man kan bruke Microsoft Foundry Local som en REST API-tjeneste uten å være avhengig av OpenAI SDK. Det demonstrerer direkte HTTP-integrasjonsmønstre for maksimal kontroll og tilpasning.

## Oversikt

Basert på Microsofts offisielle Foundry Local-mønstre, gir dette eksempelet:
- Direkte REST API-integrasjon med FoundryLocalManager
- Tilpasset implementering av HTTP-klient
- Modelladministrasjon og helsesjekk
- Håndtering av streaming- og ikke-streaming-responser
- Produksjonsklare feilhåndterings- og retry-mekanismer

## Forutsetninger

1. **Foundry Local-installasjon**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-avhengigheter**
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

## Nøkkelfunksjoner

### 1. **Direkte HTTP-integrasjon**
- Rene REST API-kall uten SDK-avhengigheter
- Tilpasset autentisering og headers
- Full kontroll over forespørsels-/responsbehandling

### 2. **Modelladministrasjon**
- Dynamisk innlasting og avlasting av modeller
- Helsesjekk og statuskontroller
- Innsamling av ytelsesmetrikker

### 3. **Produksjonsmønstre**
- Retry-mekanismer med eksponentiell backoff
- Circuit breaker for feiltoleranse
- Omfattende logging og overvåking

### 4. **Fleksibel responsbehandling**
- Streaming-responser for sanntidsapplikasjoner
- Batch-prosessering for høy gjennomstrømning
- Tilpasset responsparsing og validering

## Brukseksempler

### Grunnleggende API-integrasjon
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

### Streaming-integrasjon
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Helsesjekk
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

## Microsoft Foundry Local-integrasjon

Dette eksempelet følger Microsofts offisielle mønstre:

1. **SDK-integrasjon**: Bruker `FoundryLocalManager` for tjenesteadministrasjon
2. **REST-endepunkter**: Direkte kall til `/v1/chat/completions` og andre endepunkter
3. **Autentisering**: Riktig håndtering av API-nøkler for lokale tjenester
4. **Modelladministrasjon**: Kataloglisting, nedlasting og innlastingsmønstre
5. **Feilhåndtering**: Microsoft-anbefalte feilkoder og responser

## Komme i gang

1. **Installer avhengigheter**
   ```bash
   pip install -r requirements.txt
   ```

2. **Kjør grunnleggende eksempel**
   ```bash
   python examples/basic_usage.py
   ```

3. **Prøv streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Produksjonsoppsett**
   ```bash
   python examples/production.py
   ```

## Konfigurasjon

Miljøvariabler for tilpasning:
- `FOUNDRY_MODEL`: Standardmodell som skal brukes (standard: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Forespørselstimeout i sekunder (standard: 30)
- `FOUNDRY_RETRIES`: Antall retry-forsøk (standard: 3)
- `FOUNDRY_LOG_LEVEL`: Loggnivå (standard: "INFO")

## Beste praksis

1. **Tilkoblingsadministrasjon**: Gjenbruk HTTP-tilkoblinger for bedre ytelse
2. **Feilhåndtering**: Implementer riktig retry-logikk med eksponentiell backoff
3. **Ressursovervåking**: Spor modellens minnebruk og ytelse
4. **Sikkerhet**: Bruk riktig autentisering selv for lokale tjenester
5. **Testing**: Inkluder både enhetstester og integrasjonstester

## Feilsøking

### Vanlige problemer

**Tjenesten kjører ikke**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemer med modellinnlasting**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Tilkoblingsfeil**
- Verifiser at Foundry Local kjører på riktig port
- Sjekk brannmurinnstillinger
- Sørg for riktige autentiseringsheaders

## Ytelsesoptimalisering

1. **Tilkoblingspooling**: Bruk sesjonsobjekter for flere forespørsler
2. **Asynkrone operasjoner**: Utnytt asyncio for samtidige forespørsler
3. **Caching**: Cache modellresponser der det er hensiktsmessig
4. **Overvåking**: Spor responstider og juster timeouts

## Læringsutbytte

Etter å ha fullført dette eksempelet, vil du forstå:
- Direkte REST API-integrasjon med Foundry Local
- Mønstre for implementering av tilpasset HTTP-klient
- Produksjonsklare feilhåndterings- og overvåkingsmetoder
- Microsoft Foundry Local-tjenestearkitektur
- Ytelsesoptimaliseringsteknikker for lokale AI-tjenester

## Neste steg

- Utforsk eksempel 08: Windows 11 Chat-applikasjon
- Prøv eksempel 09: Multi-Agent Orkestrering
- Lær eksempel 10: Foundry Local som verktøyintegrasjon

---

