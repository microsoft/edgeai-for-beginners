# Foundry Local bilang Halimbawa ng API

Ang halimbawang ito ay nagpapakita kung paano gamitin ang Microsoft Foundry Local bilang REST API service nang hindi umaasa sa OpenAI SDK. Ipinapakita nito ang mga direktang pattern ng HTTP integration para sa maximum na kontrol at pagpapasadya.

## Pangkalahatang-ideya

Batay sa mga opisyal na pattern ng Microsoft Foundry Local, ang halimbawang ito ay nagbibigay ng:
- Direktang REST API integration gamit ang FoundryLocalManager
- Pasadyang HTTP client implementation
- Pamamahala ng modelo at pagsubaybay sa kalusugan
- Paghawak ng streaming at non-streaming na tugon
- Error handling at retry logic na handa para sa produksyon

## Mga Kinakailangan

1. **Pag-install ng Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Mga Dependency ng Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arkitektura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Mga Pangunahing Tampok

### 1. **Direktang HTTP Integration**
- Purong REST API calls nang walang dependency sa SDK
- Pasadyang authentication at headers
- Buong kontrol sa paghawak ng request/response

### 2. **Pamamahala ng Modelo**
- Dynamic na pag-load at pag-unload ng modelo
- Pagsubaybay sa kalusugan at status checks
- Koleksyon ng performance metrics

### 3. **Mga Pattern para sa Produksyon**
- Retry mechanisms na may exponential backoff
- Circuit breaker para sa fault tolerance
- Komprehensibong logging at monitoring

### 4. **Flexible na Paghawak ng Tugon**
- Streaming responses para sa real-time na aplikasyon
- Batch processing para sa high-throughput na mga senaryo
- Pasadyang parsing at validation ng tugon

## Mga Halimbawa ng Paggamit

### Pangunahing API Integration
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

### Streaming Integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Pagsubaybay sa Kalusugan
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Istruktura ng File

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

Ang halimbawang ito ay sumusunod sa mga opisyal na pattern ng Microsoft:

1. **SDK Integration**: Gumagamit ng `FoundryLocalManager` para sa pamamahala ng serbisyo
2. **REST Endpoints**: Direktang tawag sa `/v1/chat/completions` at iba pang endpoints
3. **Authentication**: Tamang paghawak ng API key para sa mga lokal na serbisyo
4. **Pamamahala ng Modelo**: Catalog listing, pag-download, at pag-load ng mga pattern
5. **Error Handling**: Mga error code at tugon na inirerekomenda ng Microsoft

## Pagsisimula

1. **I-install ang Mga Dependency**
   ```bash
   pip install -r requirements.txt
   ```

2. **Patakbuhin ang Pangunahing Halimbawa**
   ```bash
   python examples/basic_usage.py
   ```

3. **Subukan ang Streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Setup para sa Produksyon**
   ```bash
   python examples/production.py
   ```

## Konpigurasyon

Mga environment variable para sa pagpapasadya:
- `FOUNDRY_MODEL`: Default na modelong gagamitin (default: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Timeout ng request sa segundo (default: 30)
- `FOUNDRY_RETRIES`: Bilang ng mga retry attempt (default: 3)
- `FOUNDRY_LOG_LEVEL`: Logging level (default: "INFO")

## Mga Pinakamahusay na Kasanayan

1. **Pamamahala ng Koneksyon**: Gamitin muli ang mga HTTP connection para sa mas mahusay na performance
2. **Error Handling**: Magpatupad ng tamang retry logic na may exponential backoff
3. **Pagsubaybay sa Resource**: Subaybayan ang paggamit ng memorya ng modelo at performance
4. **Seguridad**: Gumamit ng tamang authentication kahit para sa mga lokal na serbisyo
5. **Pagsusuri**: Isama ang parehong unit at integration tests

## Pag-aayos ng Problema

### Karaniwang Mga Isyu

**Hindi Tumatakbo ang Serbisyo**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Mga Isyu sa Pag-load ng Modelo**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Mga Error sa Koneksyon**
- Siguraduhing tumatakbo ang Foundry Local sa tamang port
- Suriin ang mga setting ng firewall
- Siguraduhing tama ang authentication headers

## Pag-optimize ng Performance

1. **Connection Pooling**: Gumamit ng session objects para sa maraming request
2. **Async Operations**: Gamitin ang asyncio para sa sabay-sabay na mga request
3. **Caching**: I-cache ang mga tugon ng modelo kung naaangkop
4. **Pagsubaybay**: Subaybayan ang response times at ayusin ang timeouts

## Mga Natutunan

Pagkatapos makumpleto ang halimbawang ito, mauunawaan mo:
- Direktang REST API integration gamit ang Foundry Local
- Mga pattern ng pasadyang HTTP client implementation
- Error handling at monitoring na handa para sa produksyon
- Arkitektura ng serbisyo ng Microsoft Foundry Local
- Mga teknik sa pag-optimize ng performance para sa lokal na AI services

## Mga Susunod na Hakbang

- Tuklasin ang Halimbawa 08: Windows 11 Chat Application
- Subukan ang Halimbawa 09: Multi-Agent Orchestration
- Alamin ang Halimbawa 10: Foundry Local bilang Tools Integration

---

