# Foundry Local kot API vzorec

Ta vzorec prikazuje, kako uporabljati Microsoft Foundry Local kot REST API storitev brez uporabe OpenAI SDK. Prikazuje neposredne vzorce integracije prek HTTP za maksimalen nadzor in prilagoditev.

## Pregled

Na podlagi uradnih vzorcev Microsoft Foundry Local ta vzorec omogoča:
- Neposredno REST API integracijo z FoundryLocalManager
- Implementacijo prilagojenega HTTP odjemalca
- Upravljanje modelov in spremljanje stanja
- Obdelavo pretočnih in nepretočnih odgovorov
- Pripravljene vzorce za obravnavo napak in logiko ponovnih poskusov

## Predpogoji

1. **Namestitev Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python odvisnosti**
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

## Ključne funkcije

### 1. **Neposredna HTTP integracija**
- Čisti REST API klici brez odvisnosti od SDK
- Prilagojena avtentikacija in glave
- Popoln nadzor nad obdelavo zahtevkov in odgovorov

### 2. **Upravljanje modelov**
- Dinamično nalaganje in razkladanje modelov
- Spremljanje stanja in preverjanje statusa
- Zbiranje podatkov o zmogljivosti

### 3. **Produkcijski vzorci**
- Mehanizmi ponovnih poskusov z eksponentnim povečevanjem časa
- Circuit breaker za odpornost na napake
- Celovito beleženje in spremljanje

### 4. **Prilagodljiva obdelava odgovorov**
- Pretočni odgovori za aplikacije v realnem času
- Obdelava v serijah za scenarije z visokim pretokom
- Prilagojeno razčlenjevanje in validacija odgovorov

## Primeri uporabe

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

### Pretočna integracija
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Spremljanje stanja
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktura datotek

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

## Microsoft Foundry Local integracija

Ta vzorec sledi uradnim vzorcem Microsofta:

1. **SDK integracija**: Uporablja `FoundryLocalManager` za upravljanje storitev
2. **REST končne točke**: Neposredni klici na `/v1/chat/completions` in druge končne točke
3. **Avtentikacija**: Pravilno ravnanje z API ključem za lokalne storitve
4. **Upravljanje modelov**: Seznam katalogov, prenos in vzorci nalaganja
5. **Obravnava napak**: Priporočene kode napak in odgovori Microsofta

## Začetek

1. **Namestite odvisnosti**
   ```bash
   pip install -r requirements.txt
   ```

2. **Zaženite osnovni primer**
   ```bash
   python examples/basic_usage.py
   ```

3. **Preizkusite pretočno obdelavo**
   ```bash
   python examples/streaming.py
   ```

4. **Produkcijska nastavitev**
   ```bash
   python examples/production.py
   ```

## Konfiguracija

Spremenljivke okolja za prilagoditev:
- `FOUNDRY_MODEL`: Privzeti model za uporabo (privzeto: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Časovna omejitev zahtevka v sekundah (privzeto: 30)
- `FOUNDRY_RETRIES`: Število poskusov ponovitev (privzeto: 3)
- `FOUNDRY_LOG_LEVEL`: Raven beleženja (privzeto: "INFO")

## Najboljše prakse

1. **Upravljanje povezav**: Ponovna uporaba HTTP povezav za boljšo zmogljivost
2. **Obravnava napak**: Implementirajte ustrezno logiko ponovnih poskusov z eksponentnim povečevanjem časa
3. **Spremljanje virov**: Spremljajte porabo pomnilnika modelov in zmogljivost
4. **Varnost**: Uporabljajte ustrezno avtentikacijo tudi za lokalne storitve
5. **Testiranje**: Vključite tako enotske kot integracijske teste

## Odpravljanje težav

### Pogoste težave

**Storitev ne deluje**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Težave pri nalaganju modelov**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Napake pri povezavi**
- Preverite, ali Foundry Local deluje na pravilnem portu
- Preverite nastavitve požarnega zidu
- Zagotovite pravilne avtentikacijske glave

## Optimizacija zmogljivosti

1. **Upravljanje povezav**: Uporabljajte sejne objekte za več zahtevkov
2. **Asinhrone operacije**: Izkoristite asyncio za sočasne zahtevke
3. **Predpomnjenje**: Predpomnite odgovore modelov, kjer je to primerno
4. **Spremljanje**: Spremljajte odzivne čase in prilagodite časovne omejitve

## Cilji učenja

Po zaključku tega vzorca boste razumeli:
- Neposredno REST API integracijo z Foundry Local
- Vzorce implementacije prilagojenega HTTP odjemalca
- Produkcijsko pripravljeno obravnavo napak in spremljanje
- Arhitekturo storitev Microsoft Foundry Local
- Tehnike optimizacije zmogljivosti za lokalne AI storitve

## Naslednji koraki

- Raziščite vzorec 08: Windows 11 aplikacija za klepet
- Preizkusite vzorec 09: Orkestracija več agentov
- Naučite se vzorca 10: Foundry Local kot integracija orodij

---

