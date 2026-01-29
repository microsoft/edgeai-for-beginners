# Foundry Local mint API példa

Ez a példa bemutatja, hogyan használható a Microsoft Foundry Local REST API szolgáltatásként az OpenAI SDK használata nélkül. Közvetlen HTTP integrációs mintákat mutat be a maximális irányítás és testreszabás érdekében.

## Áttekintés

A Microsoft hivatalos Foundry Local mintái alapján ez a példa biztosítja:
- Közvetlen REST API integrációt a FoundryLocalManager-rel
- Egyedi HTTP kliens implementációt
- Modellkezelést és állapotfigyelést
- Streaming és nem-streaming válaszok kezelését
- Gyártásra kész hibakezelést és újrapróbálkozási logikát

## Előfeltételek

1. **Foundry Local telepítése**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python függőségek**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architektúra

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Főbb jellemzők

### 1. **Közvetlen HTTP integráció**
- Tiszta REST API hívások SDK függőségek nélkül
- Egyedi hitelesítés és fejlécek
- Teljes irányítás a kérés/válasz kezelés felett

### 2. **Modellkezelés**
- Dinamikus modell betöltés és eltávolítás
- Állapotfigyelés és ellenőrzések
- Teljesítménymetrikák gyűjtése

### 3. **Gyártási minták**
- Újrapróbálkozási mechanizmusok exponenciális visszalépéssel
- Áramkör-megszakító a hibatűrés érdekében
- Átfogó naplózás és monitorozás

### 4. **Rugalmas válaszkezelés**
- Streaming válaszok valós idejű alkalmazásokhoz
- Batch feldolgozás nagy áteresztőképességű forgatókönyvekhez
- Egyedi válaszfeldolgozás és validáció

## Használati példák

### Alapvető API integráció
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

### Streaming integráció
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Állapotfigyelés
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Fájlstruktúra

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

## Microsoft Foundry Local integráció

Ez a példa követi a Microsoft hivatalos mintáit:

1. **SDK integráció**: A `FoundryLocalManager` használata a szolgáltatás kezeléséhez
2. **REST végpontok**: Közvetlen hívások a `/v1/chat/completions` és más végpontokhoz
3. **Hitelesítés**: Megfelelő API kulcskezelés helyi szolgáltatásokhoz
4. **Modellkezelés**: Katalóguslistázás, letöltés és betöltési minták
5. **Hibakezelés**: Microsoft által ajánlott hibakódok és válaszok

## Első lépések

1. **Függőségek telepítése**
   ```bash
   pip install -r requirements.txt
   ```

2. **Alapvető példa futtatása**
   ```bash
   python examples/basic_usage.py
   ```

3. **Streaming kipróbálása**
   ```bash
   python examples/streaming.py
   ```

4. **Gyártási beállítás**
   ```bash
   python examples/production.py
   ```

## Konfiguráció

Környezeti változók testreszabáshoz:
- `FOUNDRY_MODEL`: Alapértelmezett modell (alapértelmezett: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Kérés időkorlátja másodpercben (alapértelmezett: 30)
- `FOUNDRY_RETRIES`: Újrapróbálkozások száma (alapértelmezett: 3)
- `FOUNDRY_LOG_LEVEL`: Naplózási szint (alapértelmezett: "INFO")

## Legjobb gyakorlatok

1. **Kapcsolatkezelés**: HTTP kapcsolatok újrahasználata a jobb teljesítmény érdekében
2. **Hibakezelés**: Megfelelő újrapróbálkozási logika implementálása exponenciális visszalépéssel
3. **Erőforrás-figyelés**: Modell memóriahasználat és teljesítmény nyomon követése
4. **Biztonság**: Megfelelő hitelesítés használata még helyi szolgáltatások esetén is
5. **Tesztelés**: Egység- és integrációs tesztek beépítése

## Hibakeresés

### Gyakori problémák

**Szolgáltatás nem fut**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Modell betöltési problémák**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Kapcsolati hibák**
- Ellenőrizze, hogy a Foundry Local a megfelelő porton fut-e
- Ellenőrizze a tűzfal beállításait
- Győződjön meg a megfelelő hitelesítési fejlécekről

## Teljesítményoptimalizálás

1. **Kapcsolat pooling**: Session objektumok használata több kéréshez
2. **Aszinkron műveletek**: Az asyncio használata párhuzamos kérésekhez
3. **Gyorsítótárazás**: Modell válaszok gyorsítótárazása, ahol megfelelő
4. **Monitorozás**: Válaszidők nyomon követése és időkorlátok beállítása

## Tanulási eredmények

A minta befejezése után megérti:
- Közvetlen REST API integrációt a Foundry Local-lal
- Egyedi HTTP kliens implementációs mintákat
- Gyártásra kész hibakezelést és monitorozást
- Microsoft Foundry Local szolgáltatás architektúráját
- Teljesítményoptimalizálási technikákat helyi AI szolgáltatásokhoz

## Következő lépések

- Fedezze fel a 08-as mintát: Windows 11 Chat alkalmazás
- Próbálja ki a 09-es mintát: Többügynökös orkestráció
- Tanulja meg a 10-es mintát: Foundry Local mint eszközök integrációja

---

