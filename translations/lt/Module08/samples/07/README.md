# Foundry Local kaip API pavyzdys

Šis pavyzdys parodo, kaip naudoti Microsoft Foundry Local kaip REST API paslaugą, nesiremiant OpenAI SDK. Jis demonstruoja tiesioginio HTTP integracijos modelius, siekiant maksimalaus valdymo ir pritaikymo.

## Apžvalga

Remiantis oficialiais Microsoft Foundry Local modeliais, šis pavyzdys suteikia:
- Tiesioginę REST API integraciją su FoundryLocalManager
- Individualų HTTP kliento įgyvendinimą
- Modelių valdymą ir būklės stebėjimą
- Srautinių ir nesrautinių atsakymų apdorojimą
- Gamybai paruoštą klaidų tvarkymą ir pakartojimo logiką

## Reikalavimai

1. **Foundry Local diegimas**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python priklausomybės**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architektūra

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Pagrindinės savybės

### 1. **Tiesioginė HTTP integracija**
- Gryni REST API skambučiai be SDK priklausomybių
- Individualus autentifikavimas ir antraštės
- Visiška užklausų/atsakymų apdorojimo kontrolė

### 2. **Modelių valdymas**
- Dinaminis modelių įkėlimas ir iškėlimas
- Būklės stebėjimas ir patikrinimai
- Našumo metrikų rinkimas

### 3. **Gamybiniai modeliai**
- Pakartojimo mechanizmai su eksponentiniu atidėjimu
- Apsauginis mechanizmas gedimų tolerancijai
- Išsamus žurnalinimas ir stebėjimas

### 4. **Lankstus atsakymų apdorojimas**
- Srautiniai atsakymai realaus laiko programoms
- Partijų apdorojimas didelio pralaidumo scenarijams
- Individualus atsakymų analizavimas ir tikrinimas

## Naudojimo pavyzdžiai

### Pagrindinė API integracija
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

### Srautinė integracija
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Būklės stebėjimas
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Failų struktūra

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

Šis pavyzdys laikosi oficialių Microsoft modelių:

1. **SDK integracija**: Naudojamas `FoundryLocalManager` paslaugų valdymui
2. **REST galiniai taškai**: Tiesioginiai skambučiai į `/v1/chat/completions` ir kitus galinius taškus
3. **Autentifikavimas**: Tinkamas API raktų tvarkymas vietinėms paslaugoms
4. **Modelių valdymas**: Katalogo sąrašų sudarymas, atsisiuntimas ir įkėlimo modeliai
5. **Klaidų tvarkymas**: Microsoft rekomenduojami klaidų kodai ir atsakymai

## Pradžia

1. **Įdiekite priklausomybes**
   ```bash
   pip install -r requirements.txt
   ```

2. **Paleiskite pagrindinį pavyzdį**
   ```bash
   python examples/basic_usage.py
   ```

3. **Išbandykite srautą**
   ```bash
   python examples/streaming.py
   ```

4. **Gamybinė sąranka**
   ```bash
   python examples/production.py
   ```

## Konfigūracija

Aplinkos kintamieji pritaikymui:
- `FOUNDRY_MODEL`: Numatytoji naudojama modelis (numatyta: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Užklausos laiko limitas sekundėmis (numatyta: 30)
- `FOUNDRY_RETRIES`: Pakartojimų bandymų skaičius (numatyta: 3)
- `FOUNDRY_LOG_LEVEL`: Žurnalinimo lygis (numatyta: "INFO")

## Geriausios praktikos

1. **Ryšių valdymas**: Pakartotinai naudokite HTTP ryšius, kad pagerintumėte našumą
2. **Klaidų tvarkymas**: Įgyvendinkite tinkamą pakartojimo logiką su eksponentiniu atidėjimu
3. **Išteklių stebėjimas**: Sekite modelio atminties naudojimą ir našumą
4. **Saugumas**: Naudokite tinkamą autentifikavimą net vietinėms paslaugoms
5. **Testavimas**: Įtraukite tiek vienetinius, tiek integracinius testus

## Trikčių šalinimas

### Dažnos problemos

**Paslauga neveikia**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Modelio įkėlimo problemos**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Ryšio klaidos**
- Patikrinkite, ar Foundry Local veikia tinkamu prievadu
- Patikrinkite užkardos nustatymus
- Įsitikinkite, kad naudojamos tinkamos autentifikavimo antraštės

## Našumo optimizavimas

1. **Ryšių telkimas**: Naudokite sesijos objektus kelioms užklausoms
2. **Asinchroninės operacijos**: Naudokite asyncio lygiagrečioms užklausoms
3. **Kešavimas**: Kešuokite modelio atsakymus, kur tai tinkama
4. **Stebėjimas**: Sekite atsakymo laikus ir koreguokite laiko limitus

## Mokymosi rezultatai

Baigę šį pavyzdį, suprasite:
- Tiesioginę REST API integraciją su Foundry Local
- Individualius HTTP kliento įgyvendinimo modelius
- Gamybai paruoštą klaidų tvarkymą ir stebėjimą
- Microsoft Foundry Local paslaugų architektūrą
- Našumo optimizavimo metodus vietinėms AI paslaugoms

## Kiti žingsniai

- Išbandykite 08 pavyzdį: Windows 11 pokalbių programa
- Išbandykite 09 pavyzdį: Daugiaagentinė orkestracija
- Sužinokite 10 pavyzdį: Foundry Local kaip įrankių integracija

---

