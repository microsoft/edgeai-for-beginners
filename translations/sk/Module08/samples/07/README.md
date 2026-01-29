# Foundry Local ako API ukážka

Táto ukážka demonštruje, ako používať Microsoft Foundry Local ako REST API službu bez závislosti na OpenAI SDK. Ukazuje priame integračné vzory cez HTTP pre maximálnu kontrolu a prispôsobenie.

## Prehľad

Na základe oficiálnych vzorov Microsoft Foundry Local táto ukážka poskytuje:
- Priamu integráciu REST API s FoundryLocalManager
- Vlastnú implementáciu HTTP klienta
- Správu modelov a monitorovanie stavu
- Spracovanie odpovedí v režime streamovania aj bez streamovania
- Pripravené na produkciu: spracovanie chýb a logika opakovania

## Predpoklady

1. **Inštalácia Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python závislosti**
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

## Kľúčové vlastnosti

### 1. **Priama HTTP integrácia**
- Čisté REST API volania bez závislosti na SDK
- Vlastná autentifikácia a hlavičky
- Plná kontrola nad spracovaním požiadaviek a odpovedí

### 2. **Správa modelov**
- Dynamické načítanie a odstraňovanie modelov
- Monitorovanie stavu a kontrola zdravia
- Zber výkonnostných metrík

### 3. **Produkčné vzory**
- Mechanizmy opakovania s exponenciálnym oneskorením
- Circuit breaker pre odolnosť voči chybám
- Komplexné logovanie a monitorovanie

### 4. **Flexibilné spracovanie odpovedí**
- Streamované odpovede pre aplikácie v reálnom čase
- Batch spracovanie pre scenáre s vysokou priepustnosťou
- Vlastné parsovanie a validácia odpovedí

## Príklady použitia

### Základná API integrácia
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

### Streamovaná integrácia
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitorovanie stavu
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Štruktúra súborov

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

## Integrácia Microsoft Foundry Local

Táto ukážka nasleduje oficiálne vzory Microsoftu:

1. **SDK integrácia**: Používa `FoundryLocalManager` na správu služieb
2. **REST endpointy**: Priame volania na `/v1/chat/completions` a ďalšie endpointy
3. **Autentifikácia**: Správne spracovanie API kľúčov pre lokálne služby
4. **Správa modelov**: Zoznam katalógu, sťahovanie a načítanie modelov
5. **Spracovanie chýb**: Odporúčané chybové kódy a odpovede od Microsoftu

## Začíname

1. **Inštalujte závislosti**
   ```bash
   pip install -r requirements.txt
   ```

2. **Spustite základný príklad**
   ```bash
   python examples/basic_usage.py
   ```

3. **Vyskúšajte streamovanie**
   ```bash
   python examples/streaming.py
   ```

4. **Produkčné nastavenie**
   ```bash
   python examples/production.py
   ```

## Konfigurácia

Premenné prostredia na prispôsobenie:
- `FOUNDRY_MODEL`: Predvolený model na použitie (predvolené: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Časový limit požiadavky v sekundách (predvolené: 30)
- `FOUNDRY_RETRIES`: Počet pokusov o opakovanie (predvolené: 3)
- `FOUNDRY_LOG_LEVEL`: Úroveň logovania (predvolené: "INFO")

## Najlepšie postupy

1. **Správa pripojení**: Opätovné použitie HTTP pripojení pre lepší výkon
2. **Spracovanie chýb**: Implementujte správnu logiku opakovania s exponenciálnym oneskorením
3. **Monitorovanie zdrojov**: Sledujte využitie pamäte modelu a výkon
4. **Bezpečnosť**: Používajte správnu autentifikáciu aj pre lokálne služby
5. **Testovanie**: Zahrňte jednotkové aj integračné testy

## Riešenie problémov

### Bežné problémy

**Služba nebeží**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problémy s načítaním modelu**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Chyby pripojenia**
- Overte, či Foundry Local beží na správnom porte
- Skontrolujte nastavenia firewallu
- Uistite sa, že používate správne autentifikačné hlavičky

## Optimalizácia výkonu

1. **Pooling pripojení**: Používajte objekty session pre viacero požiadaviek
2. **Asynchrónne operácie**: Využívajte asyncio pre súbežné požiadavky
3. **Caching**: Cacheujte odpovede modelu, kde je to vhodné
4. **Monitorovanie**: Sledujte časy odpovedí a upravujte časové limity

## Výsledky učenia

Po dokončení tejto ukážky budete rozumieť:
- Priamej integrácii REST API s Foundry Local
- Vzorom implementácie vlastného HTTP klienta
- Produkčnému spracovaniu chýb a monitorovaniu
- Architektúre služby Microsoft Foundry Local
- Technikám optimalizácie výkonu pre lokálne AI služby

## Ďalšie kroky

- Preskúmajte Ukážku 08: Chat aplikácia pre Windows 11
- Vyskúšajte Ukážku 09: Orchestrácia viacerých agentov
- Naučte sa Ukážku 10: Foundry Local ako integrácia nástrojov

---

