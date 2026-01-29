# Foundry Local kui API näidis

See näidis demonstreerib, kuidas kasutada Microsoft Foundry Local'i REST API teenusena ilma OpenAI SDK-le tuginemata. Näidis näitab otsese HTTP integratsiooni mustreid maksimaalse kontrolli ja kohandamise jaoks.

## Ülevaade

Microsofti ametlike Foundry Local mustrite põhjal pakub see näidis:
- Otsest REST API integratsiooni FoundryLocalManageriga
- Kohandatud HTTP kliendi rakendust
- Mudelite haldamist ja tervise jälgimist
- Voogesituse ja mittevoogesituse vastuste käsitlemist
- Tootmiskõlblikku veakäsitlust ja kordusloogikat

## Eeltingimused

1. **Foundry Local'i paigaldamine**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python'i sõltuvused**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arhitektuur

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Põhifunktsioonid

### 1. **Otsene HTTP integratsioon**
- Puhtad REST API päringud ilma SDK sõltuvusteta
- Kohandatud autentimine ja päised
- Täielik kontroll päringute/vastuste käsitlemise üle

### 2. **Mudelite haldamine**
- Dünaamiline mudelite laadimine ja eemaldamine
- Tervise jälgimine ja olekukontrollid
- Jõudlusmõõdikute kogumine

### 3. **Tootmismustrid**
- Kordusmehhanismid eksponentsiaalse tagasipõrkega
- Kaitselüliti vigade taluvuse tagamiseks
- Põhjalik logimine ja jälgimine

### 4. **Paindlik vastuste käsitlemine**
- Voogesituse vastused reaalajas rakenduste jaoks
- Partii töötlemine suure läbilaskevõimega stsenaariumide jaoks
- Kohandatud vastuste parsimine ja valideerimine

## Kasutusnäited

### Põhiline API integratsioon
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

### Voogesituse integratsioon
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Tervise jälgimine
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Failistruktuur

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

## Microsoft Foundry Local'i integratsioon

See näidis järgib Microsofti ametlikke mustreid:

1. **SDK integratsioon**: Kasutab `FoundryLocalManager` teenuse haldamiseks
2. **REST lõpp-punktid**: Otsesed päringud `/v1/chat/completions` ja teistele lõpp-punktidele
3. **Autentimine**: Õige API võtme käsitlemine kohalike teenuste jaoks
4. **Mudelite haldamine**: Kataloogi loetlemine, allalaadimine ja laadimise mustrid
5. **Veakäsitlus**: Microsofti soovitatud veakoodid ja vastused

## Alustamine

1. **Paigalda sõltuvused**
   ```bash
   pip install -r requirements.txt
   ```

2. **Käivita põhinäidis**
   ```bash
   python examples/basic_usage.py
   ```

3. **Proovi voogesitust**
   ```bash
   python examples/streaming.py
   ```

4. **Tootmise seadistus**
   ```bash
   python examples/production.py
   ```

## Konfiguratsioon

Keskkonnamuutujad kohandamiseks:
- `FOUNDRY_MODEL`: Vaikimisi kasutatav mudel (vaikimisi: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Päringu ajalimiit sekundites (vaikimisi: 30)
- `FOUNDRY_RETRIES`: Korduskatsete arv (vaikimisi: 3)
- `FOUNDRY_LOG_LEVEL`: Logimise tase (vaikimisi: "INFO")

## Parimad tavad

1. **Ühenduse haldamine**: Taaskasuta HTTP ühendusi parema jõudluse saavutamiseks
2. **Veakäsitlus**: Rakenda õige kordusloogika eksponentsiaalse tagasipõrkega
3. **Ressursside jälgimine**: Jälgi mudeli mälukasutust ja jõudlust
4. **Turvalisus**: Kasuta õiget autentimist isegi kohalike teenuste puhul
5. **Testimine**: Kaasa nii üksus- kui integratsioonitestid

## Tõrkeotsing

### Levinud probleemid

**Teenust ei käitata**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Mudeli laadimise probleemid**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Ühenduse vead**
- Kontrolli, kas Foundry Local töötab õigel pordil
- Kontrolli tulemüüri seadeid
- Veendu, et autentimispäised on õiged

## Jõudluse optimeerimine

1. **Ühenduse ühendamine**: Kasuta sessiooniobjekte mitme päringu jaoks
2. **Asünkroonsed operatsioonid**: Kasuta asyncio't samaaegsete päringute jaoks
3. **Vahemällu salvestamine**: Salvesta mudeli vastused, kus see on asjakohane
4. **Jälgimine**: Jälgi vastuse aegu ja kohanda ajalimiite

## Õpitulemused

Pärast selle näidise läbimist mõistad:
- Otsest REST API integratsiooni Foundry Local'iga
- Kohandatud HTTP kliendi rakenduse mustreid
- Tootmiskõlblikku veakäsitlust ja jälgimist
- Microsoft Foundry Local'i teenuse arhitektuuri
- Jõudluse optimeerimise tehnikaid kohalike AI teenuste jaoks

## Järgmised sammud

- Uuri näidist 08: Windows 11 vestlusrakendus
- Proovi näidist 09: Multi-Agent Orchestration
- Õpi näidist 10: Foundry Local kui tööriistade integratsioon

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.