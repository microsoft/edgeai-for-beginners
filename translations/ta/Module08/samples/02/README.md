# மாதிரி 02: OpenAI SDK ஒருங்கிணைப்பு

OpenAI Python SDK-யுடன் மேம்பட்ட ஒருங்கிணைப்பை விளக்குகிறது, Microsoft Foundry Local மற்றும் Azure OpenAI ஆகியவற்றுடன் ஸ்ட்ரீமிங் பதில்கள் மற்றும் சரியான பிழை கையாளுதலை ஆதரிக்கிறது.

## கண்ணோட்டம்

இந்த மாதிரி காட்டுகிறது:
- Foundry Local மற்றும் Azure OpenAI இடையே எளிதான மாறுதல்
- பயனர் அனுபவத்தை மேம்படுத்த ஸ்ட்ரீமிங் உரையாடல் முடிவுகள்
- FoundryLocalManager SDK-யின் சரியான பயன்பாடு
- வலுவான பிழை கையாளுதல் மற்றும் மாற்று வழிகள்
- உற்பத்திக்கு தயாரான குறியீட்டு முறை

## முன் தேவைகள்

- **Foundry Local**: நிறுவப்பட்டு இயங்க வேண்டும் (உள்ளூர் கணிப்பு)
- **Python**: 3.8 அல்லது அதற்கு மேல் OpenAI SDK உடன்
- **Azure OpenAI**: செல்லுபடியாகும் முடிவுநிலை மற்றும் API விசை (மேக கணிப்பு)

## நிறுவல்

1. **Python சூழலை அமைக்கவும்:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **தேவையானவை நிறுவவும்:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ஐ தொடங்கவும் (உள்ளூர் முறைக்கு):**
   ```cmd
   foundry model run phi-4-mini
   ```


## பயன்பாட்டு சூழல்கள்

### Foundry Local (இயல்புநிலை)

**விருப்பம் 1: FoundryLocalManager பயன்படுத்துதல் (பரிந்துரைக்கப்படுகிறது)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**விருப்பம் 2: கையேடு அமைப்பு**
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


## குறியீட்டு கட்டமைப்பு

### கிளையன்ட் ஃபாக்டரி முறை

இந்த மாதிரி சரியான கிளையன்டுகளை உருவாக்க ஃபாக்டரி முறையை பயன்படுத்துகிறது:

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


### ஸ்ட்ரீமிங் பதில்கள்

உடனடி பதில்களை உருவாக்க ஸ்ட்ரீமிங் முறையை இந்த மாதிரி விளக்குகிறது:

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


## சூழல் மாறிகள்

### Foundry Local அமைப்பு

| மாறி | விளக்கம் | இயல்புநிலை | தேவை |
|------|----------|------------|-------|
| `MODEL` | பயன்படுத்த வேண்டிய மாடல் பெயர் | `phi-4-mini` | இல்லை |
| `BASE_URL` | Foundry Local முடிவுநிலை | `http://localhost:8000` | இல்லை |
| `API_KEY` | API விசை (உள்ளூருக்கு விருப்பமானது) | `""` | இல்லை |

### Azure OpenAI அமைப்பு

| மாறி | விளக்கம் | இயல்புநிலை | தேவை |
|------|----------|------------|-------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI வள முடிவுநிலை | - | ஆம் |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API விசை | - | ஆம் |
| `AZURE_OPENAI_API_VERSION` | API பதிப்பு | `2024-08-01-preview` | இல்லை |
| `MODEL` | Azure பிரிவின் பெயர் | `your-deployment-name` | ஆம் |

## மேம்பட்ட அம்சங்கள்

### தானியங்கி சேவை கண்டறிதல்

சூழல் மாறிகளை அடிப்படையாகக் கொண்டு சரியான சேவையை இந்த மாதிரி தானாகவே கண்டறிகிறது:

1. **Azure முறையில்**: `AZURE_OPENAI_ENDPOINT` மற்றும் `AZURE_OPENAI_API_KEY` அமைக்கப்பட்டால்
2. **Foundry SDK முறையில்**: Foundry Local SDK கிடைத்தால்
3. **கையேடு முறையில்**: கையேடு அமைப்புக்கு மாற்று வழி

### பிழை கையாளுதல்

- SDK-யிலிருந்து கையேடு அமைப்புக்கு மாறுதல்
- பிழை தீர்க்க தெளிவான செய்திகள்
- நெட்வொர்க் பிரச்சினைகளுக்கு சரியான εξαίρεை கையாளுதல்
- தேவையான சூழல் மாறிகளை சரிபார்த்தல்

## செயல்திறன் கருத்துக்கள்

### உள்ளூர் மற்றும் மேகத்தின் இடையிலான விலகல்கள்

**Foundry Local நன்மைகள்:**
- ✅ API செலவுகள் இல்லை
- ✅ தரவின் தனியுரிமை (தரவு சாதனத்தை விட்டு வெளியே செல்லாது)
- ✅ ஆதரிக்கப்படும் மாடல்களுக்கு குறைந்த தாமதம்
- ✅ ஆஃப்லைனில் வேலை செய்கிறது

**Azure OpenAI நன்மைகள்:**
- ✅ புதிய பெரிய மாடல்களுக்கு அணுகல்
- ✅ அதிக துரிதம்
- ✅ உள்ளூர் கணினி தேவைகள் இல்லை
- ✅ நிறுவன தர SLA

## பிழை தீர்வு

### பொதுவான பிரச்சினைகள்

1. **"Foundry SDK ஐ பயன்படுத்த முடியவில்லை" எச்சரிக்கை:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure அங்கீகார பிழைகள்:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **மாடல் கிடைக்கவில்லை:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### ஆரோக்கிய சோதனைகள்

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## அடுத்த படிகள்

- **மாதிரி 03**: மாடல் கண்டறிதல் மற்றும் தரவுத்திறன் சோதனை
- **மாதிரி 04**: Chainlit RAG பயன்பாட்டை உருவாக்குதல்
- **மாதிரி 05**: பல முகவர்களின் ஒருங்கிணைப்பு
- **மாதிரி 06**: கருவிகளாக மாடல்களை வழிமாற்றுதல்

## குறிப்புகள்

- [Azure OpenAI ஆவணங்கள்](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK குறிப்பு](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ஆவணங்கள்](https://github.com/openai/openai-python)
- [ஸ்ட்ரீமிங் முடிவுகள் வழிகாட்டி](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.