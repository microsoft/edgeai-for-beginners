# Foundry Local kama Mfano wa API

Mfano huu unaonyesha jinsi ya kutumia Microsoft Foundry Local kama huduma ya REST API bila kutegemea OpenAI SDK. Unatoa mifumo ya moja kwa moja ya ushirikiano wa HTTP kwa udhibiti na ubinafsishaji wa hali ya juu.

## Muhtasari

Kulingana na mifumo rasmi ya Microsoft Foundry Local, mfano huu unatoa:
- Ushirikiano wa moja kwa moja wa REST API na FoundryLocalManager
- Utekelezaji wa mteja wa HTTP wa kawaida
- Usimamizi wa modeli na ufuatiliaji wa afya
- Ushughulikiaji wa majibu ya mtiririko na yasiyo ya mtiririko
- Ushughulikiaji wa makosa ulio tayari kwa uzalishaji na mantiki ya kurudia

## Mahitaji ya Awali

1. **Usakinishaji wa Foundry Local**  
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```
  
2. **Mategemezi ya Python**  
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```
  

## Muundo

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```
  

## Vipengele Muhimu

### 1. **Ushirikiano wa Moja kwa Moja wa HTTP**
- Simu za REST API bila utegemezi wa SDK
- Uthibitishaji wa kawaida na vichwa
- Udhibiti kamili wa usindikaji wa ombi/majibu

### 2. **Usimamizi wa Modeli**
- Upakiaji na upakuaji wa modeli kwa njia ya nguvu
- Ufuatiliaji wa afya na ukaguzi wa hali
- Ukusanyaji wa metriki za utendaji

### 3. **Mifumo ya Uzalishaji**
- Mifumo ya kurudia yenye kurudi nyuma kwa kasi
- Circuit breaker kwa uvumilivu wa makosa
- Ufuatiliaji na ukaguzi wa kina

### 4. **Ushughulikiaji wa Majibu wa Kubadilika**
- Majibu ya mtiririko kwa programu za wakati halisi
- Usindikaji wa kundi kwa hali ya juu ya mtiririko
- Uchanganuzi wa majibu wa kawaida na uthibitishaji

## Mifano ya Matumizi

### Ushirikiano wa Msingi wa API  
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
  

### Ushirikiano wa Mtiririko  
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```
  

### Ufuatiliaji wa Afya  
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```
  

## Muundo wa Faili

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
  

## Ushirikiano wa Microsoft Foundry Local

Mfano huu unafuata mifumo rasmi ya Microsoft:

1. **Ushirikiano wa SDK**: Inatumia `FoundryLocalManager` kwa usimamizi wa huduma  
2. **Njia za REST**: Simu za moja kwa moja kwa `/v1/chat/completions` na njia nyingine  
3. **Uthibitishaji**: Ushughulikiaji sahihi wa funguo za API kwa huduma za ndani  
4. **Usimamizi wa Modeli**: Orodha ya katalogi, upakuaji, na mifumo ya upakiaji  
5. **Ushughulikiaji wa Makosa**: Nambari za makosa na majibu yanayopendekezwa na Microsoft  

## Kuanza

1. **Sakinisha Mategemezi**  
   ```bash
   pip install -r requirements.txt
   ```
  

2. **Endesha Mfano wa Msingi**  
   ```bash
   python examples/basic_usage.py
   ```
  

3. **Jaribu Mtiririko**  
   ```bash
   python examples/streaming.py
   ```
  

4. **Usanidi wa Uzalishaji**  
   ```bash
   python examples/production.py
   ```
  

## Usanidi

Vigezo vya mazingira kwa ubinafsishaji:  
- `FOUNDRY_MODEL`: Modeli chaguo-msingi ya kutumia (chaguo-msingi: "phi-4-mini")  
- `FOUNDRY_TIMEOUT`: Muda wa kusubiri ombi kwa sekunde (chaguo-msingi: 30)  
- `FOUNDRY_RETRIES`: Idadi ya majaribio ya kurudia (chaguo-msingi: 3)  
- `FOUNDRY_LOG_LEVEL`: Kiwango cha ukaguzi (chaguo-msingi: "INFO")  

## Mazoea Bora

1. **Usimamizi wa Muunganisho**: Tumia muunganisho wa HTTP mara kwa mara kwa utendaji bora  
2. **Ushughulikiaji wa Makosa**: Tekeleza mantiki sahihi ya kurudia yenye kurudi nyuma kwa kasi  
3. **Ufuatiliaji wa Rasilimali**: Fuata matumizi ya kumbukumbu ya modeli na utendaji  
4. **Usalama**: Tumia uthibitishaji sahihi hata kwa huduma za ndani  
5. **Upimaji**: Jumuisha majaribio ya kitengo na ushirikiano  

## Utatuzi wa Shida

### Masuala ya Kawaida

**Huduma Haifanyi Kazi**  
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```
  

**Masuala ya Upakiaji wa Modeli**  
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```
  

**Makosa ya Muunganisho**  
- Hakikisha Foundry Local inafanya kazi kwenye bandari sahihi  
- Angalia mipangilio ya firewall  
- Hakikisha vichwa vya uthibitishaji sahihi  

## Uboreshaji wa Utendaji

1. **Uwekaji wa Muunganisho**: Tumia vitu vya kikao kwa maombi mengi  
2. **Operesheni za Async**: Tumia asyncio kwa maombi yanayofanyika kwa wakati mmoja  
3. **Uwekaji Akiba**: Weka akiba ya majibu ya modeli pale inapofaa  
4. **Ufuatiliaji**: Fuata muda wa majibu na rekebisha muda wa kusubiri  

## Matokeo ya Kujifunza

Baada ya kukamilisha mfano huu, utaelewa:  
- Ushirikiano wa moja kwa moja wa REST API na Foundry Local  
- Mifumo ya utekelezaji wa mteja wa HTTP wa kawaida  
- Ushughulikiaji wa makosa ulio tayari kwa uzalishaji na ufuatiliaji  
- Muundo wa huduma ya Microsoft Foundry Local  
- Mbinu za uboreshaji wa utendaji kwa huduma za AI za ndani  

## Hatua Zifuatazo

- Chunguza Mfano 08: Programu ya Gumzo ya Windows 11  
- Jaribu Mfano 09: Uratibu wa Wakala Wengi  
- Jifunze Mfano 10: Foundry Local kama Ushirikiano wa Zana  

---

