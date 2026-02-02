# Foundry Local kao API primjer

Ovaj primjer pokazuje kako koristiti Microsoft Foundry Local kao REST API uslugu bez oslanjanja na OpenAI SDK. Prikazuje izravne obrasce integracije putem HTTP-a za maksimalnu kontrolu i prilagodbu.

## Pregled

Na temelju službenih obrazaca Microsoft Foundry Local, ovaj primjer pruža:
- Izravnu REST API integraciju s FoundryLocalManager
- Prilagođenu implementaciju HTTP klijenta
- Upravljanje modelima i praćenje stanja
- Obradu odgovora u stvarnom vremenu i bez strujanja
- Logiku za rukovanje greškama i ponovnim pokušajima spremnu za produkciju

## Preduvjeti

1. **Instalacija Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python ovisnosti**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arhitektura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Ključne značajke

### 1. **Izravna HTTP integracija**
- Čisti REST API pozivi bez ovisnosti o SDK-u
- Prilagođena autentifikacija i zaglavlja
- Potpuna kontrola nad obradom zahtjeva i odgovora

### 2. **Upravljanje modelima**
- Dinamičko učitavanje i uklanjanje modela
- Praćenje stanja i provjere statusa
- Prikupljanje metrika performansi

### 3. **Obrasci za produkciju**
- Mehanizmi ponovnog pokušaja s eksponencijalnim povratom
- Circuit breaker za otpornost na greške
- Sveobuhvatno logiranje i praćenje

### 4. **Fleksibilna obrada odgovora**
- Odgovori u stvarnom vremenu za aplikacije u stvarnom vremenu
- Obrada u serijama za scenarije visokog kapaciteta
- Prilagođeno parsiranje i validacija odgovora

## Primjeri korištenja

### Osnovna API integracija
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

### Integracija strujanja
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Praćenje stanja
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktura datoteka

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

## Integracija Microsoft Foundry Local

Ovaj primjer slijedi službene obrasce Microsofta:

1. **SDK integracija**: Koristi `FoundryLocalManager` za upravljanje uslugama
2. **REST krajnje točke**: Izravni pozivi na `/v1/chat/completions` i druge krajnje točke
3. **Autentifikacija**: Ispravno rukovanje API ključem za lokalne usluge
4. **Upravljanje modelima**: Popis kataloga, preuzimanje i obrasci učitavanja
5. **Rukovanje greškama**: Preporučeni Microsoft kodovi grešaka i odgovori

## Početak rada

1. **Instalirajte ovisnosti**
   ```bash
   pip install -r requirements.txt
   ```

2. **Pokrenite osnovni primjer**
   ```bash
   python examples/basic_usage.py
   ```

3. **Isprobajte strujanje**
   ```bash
   python examples/streaming.py
   ```

4. **Postavljanje za produkciju**
   ```bash
   python examples/production.py
   ```

## Konfiguracija

Varijable okruženja za prilagodbu:
- `FOUNDRY_MODEL`: Zadani model za korištenje (zadano: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Vrijeme čekanja zahtjeva u sekundama (zadano: 30)
- `FOUNDRY_RETRIES`: Broj pokušaja ponavljanja (zadano: 3)
- `FOUNDRY_LOG_LEVEL`: Razina logiranja (zadano: "INFO")

## Najbolje prakse

1. **Upravljanje vezama**: Ponovno korištenje HTTP veza za bolje performanse
2. **Rukovanje greškama**: Implementirajte ispravnu logiku ponovnog pokušaja s eksponencijalnim povratom
3. **Praćenje resursa**: Pratite korištenje memorije modela i performanse
4. **Sigurnost**: Koristite ispravnu autentifikaciju čak i za lokalne usluge
5. **Testiranje**: Uključite i jedinične i integracijske testove

## Rješavanje problema

### Uobičajeni problemi

**Usluga ne radi**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemi s učitavanjem modela**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Greške u vezi**
- Provjerite radi li Foundry Local na ispravnom portu
- Provjerite postavke vatrozida
- Osigurajte ispravna zaglavlja za autentifikaciju

## Optimizacija performansi

1. **Pool veze**: Koristite objekte sesije za više zahtjeva
2. **Asinkrone operacije**: Iskoristite asyncio za istovremene zahtjeve
3. **Keširanje**: Keširajte odgovore modela gdje je prikladno
4. **Praćenje**: Pratite vrijeme odgovora i prilagodite vrijeme čekanja

## Ishodi učenja

Nakon završetka ovog primjera, razumjet ćete:
- Izravnu REST API integraciju s Foundry Local
- Obrasce implementacije prilagođenog HTTP klijenta
- Rukovanje greškama i praćenje spremno za produkciju
- Arhitekturu usluge Microsoft Foundry Local
- Tehnike optimizacije performansi za lokalne AI usluge

## Sljedeći koraci

- Istražite Primjer 08: Windows 11 aplikacija za chat
- Isprobajte Primjer 09: Orkestracija više agenata
- Naučite Primjer 10: Foundry Local kao integracija alata

---

