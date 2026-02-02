# Foundry Local jako ukázka API

Tento příklad ukazuje, jak používat Microsoft Foundry Local jako REST API službu bez závislosti na OpenAI SDK. Demonstruje přímé integrační vzory HTTP pro maximální kontrolu a přizpůsobení.

## Přehled

Na základě oficiálních vzorů Microsoft Foundry Local tento příklad poskytuje:
- Přímou integraci REST API s FoundryLocalManager
- Vlastní implementaci HTTP klienta
- Správu modelů a monitorování stavu
- Zpracování odpovědí ve streamovacím i nestreamovacím režimu
- Produkčně připravené zpracování chyb a logiku opakování

## Předpoklady

1. **Instalace Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python závislosti**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architektura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Klíčové vlastnosti

### 1. **Přímá integrace HTTP**
- Čisté REST API volání bez závislosti na SDK
- Vlastní autentizace a hlavičky
- Plná kontrola nad zpracováním požadavků a odpovědí

### 2. **Správa modelů**
- Dynamické načítání a uvolňování modelů
- Monitorování stavu a kontrola zdraví
- Sběr výkonových metrik

### 3. **Produkční vzory**
- Mechanismy opakování s exponenciálním zpožděním
- Circuit breaker pro odolnost vůči chybám
- Komplexní logování a monitorování

### 4. **Flexibilní zpracování odpovědí**
- Streamovací odpovědi pro aplikace v reálném čase
- Dávkové zpracování pro scénáře s vysokou propustností
- Vlastní analýza a validace odpovědí

## Příklady použití

### Základní integrace API
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

### Streamovací integrace
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitorování stavu
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktura souborů

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

## Integrace Microsoft Foundry Local

Tento příklad se řídí oficiálními vzory Microsoftu:

1. **Integrace SDK**: Používá `FoundryLocalManager` pro správu služeb
2. **REST Endpointy**: Přímé volání na `/v1/chat/completions` a další endpointy
3. **Autentizace**: Správné zpracování API klíče pro lokální služby
4. **Správa modelů**: Výpis katalogu, stahování a vzory načítání
5. **Zpracování chyb**: Doporučené chybové kódy a odpovědi od Microsoftu

## Začínáme

1. **Instalace závislostí**
   ```bash
   pip install -r requirements.txt
   ```

2. **Spuštění základního příkladu**
   ```bash
   python examples/basic_usage.py
   ```

3. **Vyzkoušení streamování**
   ```bash
   python examples/streaming.py
   ```

4. **Produkční nastavení**
   ```bash
   python examples/production.py
   ```

## Konfigurace

Proměnné prostředí pro přizpůsobení:
- `FOUNDRY_MODEL`: Výchozí model k použití (výchozí: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Časový limit požadavku v sekundách (výchozí: 30)
- `FOUNDRY_RETRIES`: Počet pokusů o opakování (výchozí: 3)
- `FOUNDRY_LOG_LEVEL`: Úroveň logování (výchozí: "INFO")

## Nejlepší postupy

1. **Správa připojení**: Znovu používejte HTTP připojení pro lepší výkon
2. **Zpracování chyb**: Implementujte správnou logiku opakování s exponenciálním zpožděním
3. **Monitorování zdrojů**: Sledujte využití paměti modelu a výkon
4. **Bezpečnost**: Používejte správnou autentizaci i pro lokální služby
5. **Testování**: Zahrňte jak jednotkové, tak integrační testy

## Řešení problémů

### Běžné problémy

**Služba neběží**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problémy s načítáním modelu**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Chyby připojení**
- Ověřte, že Foundry Local běží na správném portu
- Zkontrolujte nastavení firewallu
- Ujistěte se, že používáte správné autentizační hlavičky

## Optimalizace výkonu

1. **Pooling připojení**: Používejte objekty session pro více požadavků
2. **Asynchronní operace**: Využívejte asyncio pro souběžné požadavky
3. **Caching**: Cacheujte odpovědi modelu, kde je to vhodné
4. **Monitorování**: Sledujte časy odpovědí a upravujte časové limity

## Výsledky učení

Po dokončení tohoto příkladu budete rozumět:
- Přímé integraci REST API s Foundry Local
- Vzorům implementace vlastního HTTP klienta
- Produkčně připravenému zpracování chyb a monitorování
- Architektuře služby Microsoft Foundry Local
- Technikám optimalizace výkonu pro lokální AI služby

## Další kroky

- Prozkoumejte Ukázku 08: Chatovací aplikace pro Windows 11
- Vyzkoušejte Ukázku 09: Orchestrace více agentů
- Naučte se Ukázku 10: Integrace Foundry Local jako nástroje

---

