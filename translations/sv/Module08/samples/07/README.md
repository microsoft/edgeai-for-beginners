# Foundry Local som API-exempel

Det här exemplet visar hur man använder Microsoft Foundry Local som en REST API-tjänst utan att förlita sig på OpenAI SDK. Det demonstrerar direkta HTTP-integrationsmönster för maximal kontroll och anpassning.

## Översikt

Baserat på Microsofts officiella Foundry Local-mönster erbjuder detta exempel:
- Direkt REST API-integration med FoundryLocalManager
- Anpassad implementation av HTTP-klient
- Modellhantering och hälsokontroll
- Hantering av både strömmande och icke-strömmande svar
- Produktionsklara felhanterings- och återförsökslogik

## Förutsättningar

1. **Foundry Local Installation**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-beroenden**
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

## Nyckelfunktioner

### 1. **Direkt HTTP-integration**
- Enbart REST API-anrop utan SDK-beroenden
- Anpassad autentisering och headers
- Full kontroll över begäran/svarshantering

### 2. **Modellhantering**
- Dynamisk laddning och avladdning av modeller
- Hälsokontroll och statusövervakning
- Insamling av prestandamått

### 3. **Produktionsmönster**
- Återförsöksmekanismer med exponentiell backoff
- Circuit breaker för felhantering
- Omfattande loggning och övervakning

### 4. **Flexibel svarshantering**
- Strömmande svar för realtidsapplikationer
- Batchbearbetning för hög genomströmning
- Anpassad svarsparsing och validering

## Användningsexempel

### Grundläggande API-integration
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

### Strömmande integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Hälsokontroll
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

Detta exempel följer Microsofts officiella mönster:

1. **SDK-integration**: Använder `FoundryLocalManager` för tjänstehantering
2. **REST-endpoints**: Direkta anrop till `/v1/chat/completions` och andra endpoints
3. **Autentisering**: Korrekt hantering av API-nycklar för lokala tjänster
4. **Modellhantering**: Kataloglistning, nedladdning och laddningsmönster
5. **Felhantering**: Microsoft-rekommenderade felkoder och svar

## Komma igång

1. **Installera beroenden**
   ```bash
   pip install -r requirements.txt
   ```

2. **Kör grundläggande exempel**
   ```bash
   python examples/basic_usage.py
   ```

3. **Testa strömning**
   ```bash
   python examples/streaming.py
   ```

4. **Produktionsinställning**
   ```bash
   python examples/production.py
   ```

## Konfiguration

Miljövariabler för anpassning:
- `FOUNDRY_MODEL`: Standardmodell att använda (standard: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Begäran timeout i sekunder (standard: 30)
- `FOUNDRY_RETRIES`: Antal återförsöksförsök (standard: 3)
- `FOUNDRY_LOG_LEVEL`: Loggnivå (standard: "INFO")

## Bästa praxis

1. **Anslutningshantering**: Återanvänd HTTP-anslutningar för bättre prestanda
2. **Felhantering**: Implementera korrekt återförsökslogik med exponentiell backoff
3. **Resursövervakning**: Spåra modellens minnesanvändning och prestanda
4. **Säkerhet**: Använd korrekt autentisering även för lokala tjänster
5. **Testning**: Inkludera både enhets- och integrationstester

## Felsökning

### Vanliga problem

**Tjänsten körs inte**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problem med modellens laddning**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Anslutningsfel**
- Kontrollera att Foundry Local körs på rätt port
- Kontrollera brandväggsinställningar
- Säkerställ korrekta autentiseringsheaders

## Prestandaoptimering

1. **Anslutningspoolning**: Använd sessionsobjekt för flera begäranden
2. **Asynkrona operationer**: Utnyttja asyncio för samtidiga begäranden
3. **Caching**: Cacha modellsvar där det är lämpligt
4. **Övervakning**: Spåra svarstider och justera timeouts

## Lärandemål

Efter att ha genomfört detta exempel kommer du att förstå:
- Direkt REST API-integration med Foundry Local
- Mönster för anpassad implementation av HTTP-klient
- Produktionsklar felhantering och övervakning
- Microsoft Foundry Local tjänstearkitektur
- Prestandaoptimeringstekniker för lokala AI-tjänster

## Nästa steg

- Utforska Exempel 08: Windows 11 Chat-applikation
- Testa Exempel 09: Multi-Agent Orchestration
- Lär dig Exempel 10: Foundry Local som verktygsintegration

---

