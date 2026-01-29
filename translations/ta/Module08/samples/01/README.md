# மாதிரி 01: OpenAI SDK மூலம் விரைவான உரையாடல்

Microsoft Foundry Local உடன் உள்ளூர் AI கணிப்பு செய்ய OpenAI SDK ஐ எப்படி பயன்படுத்துவது என்பதை விளக்கும் ஒரு எளிய உரையாடல் எடுத்துக்காட்டு.

## மேலோட்டம்

இந்த எடுத்துக்காட்டில் நீங்கள் எப்படி:
- Foundry Local உடன் OpenAI Python SDK ஐ பயன்படுத்துவது
- Azure OpenAI மற்றும் Foundry உள்ளூர் அமைப்புகளை கையாளுவது
- சரியான பிழை கையாளல் மற்றும் மாற்று உத்திகளை செயல்படுத்துவது
- FoundryLocalManager ஐ சேவை மேலாண்மைக்கு பயன்படுத்துவது என்பதைப் பார்க்கலாம்

## முன் தேவைகள்

- **Foundry Local**: நிறுவப்பட்டு PATH இல் கிடைக்க வேண்டும்
- **Python**: 3.8 அல்லது அதற்கு மேல்
- **மாடல்**: Foundry Local இல் ஏற்றப்பட்ட மாடல் (எ.கா., `phi-4-mini`)

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

3. **Foundry Local சேவையை தொடங்கி ஒரு மாடலை ஏற்றவும்:**
   ```cmd
   foundry model run phi-4-mini
   ```

## பயன்பாடு

### Foundry Local (இயல்புநிலை)

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

## குறியீட்டு அம்சங்கள்

### FoundryLocalManager ஒருங்கிணைப்பு

சேவை மேலாண்மைக்கு Foundry Local SDK ஐ எடுத்துக்காட்டில் பயன்படுத்தப்பட்டுள்ளது:

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

### பிழை கையாளல்

மிகவும் வலுவான பிழை கையாளல் மற்றும் கையேடு அமைப்புக்கு மாற்று:
- தானியங்கி சேவை கண்டறிதல்
- SDK கிடைக்காதபோது மென்மையான செயலிழப்பு
- பிழை தீர்க்க தெளிவான செய்திகள்

## சூழல் மாறிகள்

| மாறி | விளக்கம் | இயல்புநிலை | தேவைப்படும் |
|------|----------|------------|-------------|
| `MODEL` | மாடல் பெயர் அல்லது குறிச்சொல் | `phi-4-mini` | இல்லை |
| `BASE_URL` | Foundry Local அடிப்படை URL | `http://localhost:8000` | இல்லை |
| `API_KEY` | API விசை (உள்ளூருக்கு பொதுவாக தேவையில்லை) | `""` | இல்லை |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI இறுதிப்புள்ளி | - | Azure க்கு |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API விசை | - | Azure க்கு |
| `AZURE_OPENAI_API_VERSION` | Azure API பதிப்பு | `2024-08-01-preview` | இல்லை |

## பிழை தீர்வு

### பொதுவான சிக்கல்கள்

1. **"Foundry SDK ஐ பயன்படுத்த முடியவில்லை" எச்சரிக்கை:**
   - foundry-local-sdk ஐ நிறுவவும்: `pip install foundry-local-sdk`
   - அல்லது கையேடு அமைப்புக்கு சூழல் மாறிகளை அமைக்கவும்

2. **இணைப்பு மறுக்கப்பட்டது:**
   - Foundry Local இயங்குகிறதா என்பதை உறுதிப்படுத்தவும்: `foundry service status`
   - ஒரு மாடல் ஏற்றப்பட்டுள்ளதா என்பதை சரிபார்க்கவும்: `foundry service ps`

3. **மாடல் கிடைக்கவில்லை:**
   - கிடைக்கக்கூடிய மாடல்களை பட்டியலிடவும்: `foundry model list`
   - ஒரு மாடலை ஏற்றவும்: `foundry model run phi-4-mini`

### சரிபார்ப்பு

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## குறிப்புகள்

- [Foundry Local ஆவணங்கள்](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-இன் இணக்கமான API குறிப்பு](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.