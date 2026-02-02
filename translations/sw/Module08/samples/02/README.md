# Mfano 02: Ujumuishaji wa OpenAI SDK

Inaonyesha ujumuishaji wa hali ya juu na OpenAI Python SDK, ikisaidia Microsoft Foundry Local na Azure OpenAI kwa majibu ya mtiririko na usimamizi sahihi wa makosa.

## Muhtasari

Mfano huu unaonyesha:
- Kubadilisha kwa urahisi kati ya Foundry Local na Azure OpenAI
- Majibu ya mazungumzo ya mtiririko kwa uzoefu bora wa mtumiaji
- Matumizi sahihi ya FoundryLocalManager SDK
- Usimamizi thabiti wa makosa na mifumo ya kurudi nyuma
- Mifumo ya msimbo inayofaa kwa uzalishaji

## Mahitaji

- **Foundry Local**: Imewekwa na inafanya kazi (kwa utabiri wa ndani)
- **Python**: Toleo la 3.8 au baadaye na OpenAI SDK
- **Azure OpenAI**: Endpoint halali na API key (kwa utabiri wa wingu)

## Usakinishaji

1. **Sanidi mazingira ya Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Sakinisha utegemezi:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Anzisha Foundry Local (kwa hali ya ndani):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Matumizi ya Hali

### Foundry Local (Chaguo-msingi)

**Chaguo 1: Kutumia FoundryLocalManager (Inapendekezwa)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Chaguo 2: Usanidi wa Mwongozo**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```

## Muundo wa Msimbo

### Muundo wa Kiwanda cha Wateja

Mfano hutumia muundo wa kiwanda kuunda wateja sahihi:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```

### Majibu ya Mtiririko

Mfano unaonyesha mtiririko wa majibu kwa kizazi cha majibu ya wakati halisi:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Vigezo vya Mazingira

### Usanidi wa Foundry Local

| Kigezo | Maelezo | Chaguo-msingi | Inahitajika |
|--------|----------|--------------|-------------|
| `MODEL` | Jina la mfano wa kutumia | `phi-4-mini` | Hapana |
| `BASE_URL` | Endpoint ya Foundry Local | `http://localhost:8000` | Hapana |
| `API_KEY` | API key (hiari kwa ndani) | `""` | Hapana |

### Usanidi wa Azure OpenAI

| Kigezo | Maelezo | Chaguo-msingi | Inahitajika |
|--------|----------|--------------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint ya rasilimali ya Azure OpenAI | - | Ndio |
| `AZURE_OPENAI_API_KEY` | API key ya Azure OpenAI | - | Ndio |
| `AZURE_OPENAI_API_VERSION` | Toleo la API | `2024-08-01-preview` | Hapana |
| `MODEL` | Jina la usambazaji wa Azure | `your-deployment-name` | Ndio |

## Vipengele vya Juu

### Ugunduzi wa Huduma Kiotomatiki

Mfano hugundua kiotomatiki huduma inayofaa kulingana na vigezo vya mazingira:

1. **Hali ya Azure**: Ikiwa `AZURE_OPENAI_ENDPOINT` na `AZURE_OPENAI_API_KEY` zimewekwa
2. **Hali ya Foundry SDK**: Ikiwa Foundry Local SDK inapatikana
3. **Hali ya Mwongozo**: Kurudi nyuma kwa usanidi wa mwongozo

### Usimamizi wa Makosa

- Kurudi nyuma kwa neema kutoka SDK hadi usanidi wa mwongozo
- Ujumbe wa makosa wazi kwa utatuzi wa matatizo
- Ushughulikiaji sahihi wa hali za kipekee za mtandao
- Uthibitishaji wa vigezo vya mazingira vinavyohitajika

## Mazingatio ya Utendaji

### Faida za Ndani vs Wingu

**Faida za Foundry Local:**
- ✅ Hakuna gharama za API
- ✅ Faragha ya data (hakuna data inayotoka kwenye kifaa)
- ✅ Muda mfupi wa kusubiri kwa mifano inayoungwa mkono
- ✅ Inafanya kazi bila mtandao

**Faida za Azure OpenAI:**
- ✅ Ufikiaji wa mifano mikubwa ya hivi karibuni
- ✅ Uwezo wa juu wa usindikaji
- ✅ Hakuna mahitaji ya kompyuta ya ndani
- ✅ SLA ya daraja la biashara

## Utatuzi wa Matatizo

### Masuala ya Kawaida

1. **"Haiwezi kutumia Foundry SDK" onyo:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Makosa ya uthibitishaji wa Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Mfano haupatikani:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Ukaguzi wa Afya

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Hatua Zifuatazo

- **Mfano 03**: Ugunduzi wa mifano na upimaji wa utendaji
- **Mfano 04**: Kujenga programu ya Chainlit RAG
- **Mfano 05**: Uratibu wa mawakala wengi
- **Mfano 06**: Uelekezaji wa mifano kama zana

## Marejeleo

- [Nyaraka za Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Rejeleo la Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Nyaraka za OpenAI Python SDK](https://github.com/openai/openai-python)
- [Mwongozo wa Majibu ya Mtiririko](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

