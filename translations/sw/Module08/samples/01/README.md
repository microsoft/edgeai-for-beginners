# Mfano 01: Mazungumzo ya Haraka kupitia OpenAI SDK

Mfano rahisi wa mazungumzo unaoonyesha jinsi ya kutumia OpenAI SDK na Microsoft Foundry Local kwa utambuzi wa AI wa ndani.

## Muhtasari

Mfano huu unaonyesha jinsi ya:
- Kutumia OpenAI Python SDK na Foundry Local
- Kushughulikia mipangilio ya Azure OpenAI na Foundry ya ndani
- Kutekeleza utunzaji sahihi wa makosa na mikakati ya mbadala
- Kutumia FoundryLocalManager kwa usimamizi wa huduma

## Mahitaji ya Awali

- **Foundry Local**: Imewekwa na inapatikana kwenye PATH
- **Python**: Toleo la 3.8 au baadaye
- **Modeli**: Modeli iliyopakiwa kwenye Foundry Local (mfano, `phi-4-mini`)

## Usakinishaji

1. **Sanidi mazingira ya Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Sakinisha mahitaji:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Anzisha huduma ya Foundry Local na pakia modeli:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Matumizi

### Foundry Local (Chaguo la Kawaida)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Vipengele vya Msimbo

### Ujumuishaji wa FoundryLocalManager

Mfano huu unatumia Foundry Local SDK rasmi kwa usimamizi sahihi wa huduma:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Utunzaji wa Makosa

Utunzaji wa makosa wenye nguvu na mbadala wa usanidi wa mwongozo:
- Ugunduzi wa huduma kiotomatiki
- Kupungua kwa utendaji kwa neema ikiwa SDK haipatikani
- Ujumbe wa makosa wazi kwa utatuzi wa matatizo

## Vigezo vya Mazingira

| Kigezo | Maelezo | Chaguo-msingi | Inahitajika |
|--------|---------|--------------|-------------|
| `MODEL` | Jina au alias ya modeli | `phi-4-mini` | Hapana |
| `BASE_URL` | URL ya msingi ya Foundry Local | `http://localhost:8000` | Hapana |
| `API_KEY` | API key (kawaida haitahitajika kwa ndani) | `""` | Hapana |
| `AZURE_OPENAI_ENDPOINT` | Endpoint ya Azure OpenAI | - | Kwa Azure |
| `AZURE_OPENAI_API_KEY` | API key ya Azure OpenAI | - | Kwa Azure |
| `AZURE_OPENAI_API_VERSION` | Toleo la API ya Azure | `2024-08-01-preview` | Hapana |

## Utatuzi wa Matatizo

### Masuala ya Kawaida

1. **Onyo: "Haikuweza kutumia Foundry SDK":**
   - Sakinisha foundry-local-sdk: `pip install foundry-local-sdk`
   - Au weka vigezo vya mazingira kwa usanidi wa mwongozo

2. **Muunganisho umekataliwa:**
   - Hakikisha Foundry Local inaendesha: `foundry service status`
   - Angalia kama modeli imepakiwa: `foundry service ps`

3. **Modeli haikupatikana:**
   - Orodhesha modeli zinazopatikana: `foundry model list`
   - Pakia modeli: `foundry model run phi-4-mini`

### Uthibitishaji

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Marejeleo

- [Nyaraka za Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Marejeleo ya API inayolingana na OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

