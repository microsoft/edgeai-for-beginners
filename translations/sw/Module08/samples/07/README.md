# Foundry Local kama Mfano wa API

Mfano huu unaonyesha jinsi ya kutumia Microsoft Foundry Local kama huduma ya REST API bila kutegemea SDK ya OpenAI. Unaonyesha mifano ya ushirikiano wa moja kwa moja wa HTTP kwa udhibiti na ubinafsishaji wa juu.

## Muhtasari

Kulingana na mifano rasmi ya Microsoft Foundry Local, mfano huu unatoa:
- Ushirikiano wa moja kwa moja wa REST API na FoundryLocalManager
- Utekelezaji wa mteja wa HTTP ulio kubinafsishwa
- Usimamizi wa mfano na ufuatiliaji wa afya
- Ushughulikiaji wa majibu ya kuonyesha mtiririko na yasiyo mtiririko
- Ushughulikiaji wa makosa unaoandaliwa kwa ajili ya uzalishaji na mantiki ya jaribio la upya

## Mahitaji ya awali

1. **Usanidi wa Foundry Local**
   ```powershell
   # Sakinisha kutoka kwa matoleo ya GitHub
   winget install Microsoft.FoundryLocal
   ```

2. **Vitegemezi vya Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Miundo

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Sifa Muhimu

### 1. **Ushirikiano wa Moja kwa Moja wa HTTP**
- Maita halisi ya REST API bila utegemezi wa SDK
- Uthibitishaji na vichwa vya habari vilivyobinafsishwa
- Udhibiti kamili juu ya usindikaji wa ombi/jibu

### 2. **Usimamizi wa Mfano**
- Kupakia na kutoa mifano kwa mdundo
- Ufuatiliaji wa afya na ukaguzi wa hali
- Ukusanyaji wa vipimo vya utendaji

### 3. **Mifano ya Uzalishaji**
- Mifumo ya jaribio la upya na malengo yanayoongezeka
- Kivunja mzunguko kwa kustahimili hitilafu
- Kumbukumbu na ufuatiliaji kamili

### 4. **Ushughulikiaji Rahisi wa Majibu**
- Majibu ya mtiririko kwa matumizi ya wakati halisi
- Usindikaji wa kikundi kwa hali za mtiririko wa juu
- Utambuzi na uhakiki wa majibu vilivyobinafsishwa

## Mifano ya Matumizi

### Ushirikiano wa API wa Msingi
```python
from api_client import FoundryAPIClient

# Anzisha mteja wa API
client = FoundryAPIClient()

# Ukomo rahisi
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Ushirikiano wa Mtiririko
```python
# Tumia majibu ya mtiririko kwa programu za wakati halisi
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Ufuatiliaji wa Afya
```python
# Angalia afya ya huduma
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

Mfano huu unafuata mifano rasmi ya Microsoft:

1. **Ushirikiano wa SDK**: Inatumia `FoundryLocalManager` kwa usimamizi wa huduma
2. **Mifumo ya REST**: Maita ya moja kwa moja kwa `/v1/chat/completions` na mifumo mingine
3. **Uthibitishaji**: Ushughulikiaji sahihi wa funguo za API kwa huduma za ndani
4. **Usimamizi wa Mfano**: Orodha ya saraka, download, na mifano ya upakiaji
5. **Ushughulikiaji wa Makosa**: Nambari za makosa na majibu zilizo pendekezwa na Microsoft

## Kuanzisha

1. **Sakinisha Vitegemezi**
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

4. **Mipangilio ya Uzalishaji**
   ```bash
   python examples/production.py
   ```

## Usanidi

Mabadiliko ya mazingira kwa ubinafsishaji:
- `FOUNDRY_MODEL`: Mfano chaguo-msingi wa kutumia (chaguo-msingi: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Muda wa kusubiri ombi kwa sekunde (chaguo-msingi: 30)
- `FOUNDRY_RETRIES`: Idadi ya jaribio la upya (chaguo-msingi: 3)
- `FOUNDRY_LOG_LEVEL`: Kiwango cha kumbukumbu ya matukio (chaguo-msingi: "INFO")

## Mbinu Bora

1. **Usimamizi wa Muunganisho**: Tumia tena muunganisho wa HTTP kwa utendaji bora
2. **Ushughulikiaji wa Makosa**: Tekeleza mantiki ya jaribio la upya kwa malengo yanayoongezeka
3. **Ufuatiliaji wa Rasilimali**: Fuata matumizi ya kumbukumbu ya mfano na utendaji
4. **Usalama**: Tumia uthibitishaji sawa hata kwa huduma za ndani
5. **Upimaji**: Jumuisha majaribio ya kitengo na ushirikiano

## Utatuzi wa Matatizo

### Masuala ya Kawaida

**Huduma Haifanyi Kazi**
```bash
# Kagua hali ya Foundry Local
foundry status

# Anza ikiwa inahitajika
foundry start
```

**Matatizo ya Upakiaji Mfano**
```bash
# Orodha ya mifano inayopatikana
foundry model list

# Pakua mfano maalum
foundry model download phi-4-mini
```

**Makosa ya Muunganisho**
- Hakikisha Foundry Local inaendesha kwenye bandari sahihi
- Angalia mipangilio ya ukuta wa moto
- Hakikisha vichwa vya uthibitishaji ni sahihi

## Uboreshaji wa Utendaji

1. **Ukusanyaji wa Muunganisho**: Tumia vitu vya kikao kwa maombi mengi
2. **Operesheni za Async**: Tumia asyncio kwa maombi yanayoendeshwa kwa pamoja
3. **Caching**: Hifadhi majibu ya mfano pale inapofaa
4. **Ufuatiliaji**: Fuata nyakati za majibu na rekebisha muda wa kusubiri

## Matokeo ya Kujifunza

Baada ya kumaliza mfano huu, utakuwa unaelewa:
- Ushirikiano wa moja kwa moja wa REST API na Foundry Local
- Mifano ya utekelezaji wa mteja wa HTTP ulio kubinafsishwa
- Ushughulikiaji wa makosa unaoandaliwa kwa ajili ya uzalishaji na ufuatiliaji
- Miundombinu ya huduma za Microsoft Foundry Local
- Mbinu za uboreshaji wa utendaji kwa huduma za AI za ndani

## Hatua Zinazofuata

- Chunguza Mfano 08: Programu ya Chat ya Windows 11
- Jaribu Mfano 09: Usimamizi wa Wakala Wengi
- Jifunze Mfano 10: Foundry Local kama Ushirikiano wa Zana

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->