# Foundry Local API மாதிரி

இந்த மாதிரி Microsoft Foundry Local-ஐ REST API சேவையாக OpenAI SDK-ஐ நம்பாமல் பயன்படுத்துவது எப்படி என்பதை விளக்குகிறது. இது அதிக கட்டுப்பாடு மற்றும் தனிப்பயனாக்கத்திற்கான நேரடி HTTP ஒருங்கிணைப்பு முறைகளை காட்டுகிறது.

## கண்ணோட்டம்

Microsoft-இன் Foundry Local முறைகளின் அடிப்படையில், இந்த மாதிரி வழங்குகிறது:
- FoundryLocalManager உடன் நேரடி REST API ஒருங்கிணைப்பு
- தனிப்பயன் HTTP கிளையன்ட் செயலாக்கம்
- மாடல் மேலாண்மை மற்றும் ஆரோக்கிய கண்காணிப்பு
- ஸ்ட்ரீமிங் மற்றும் ஸ்ட்ரீமிங் அல்லாத பதில்கள் கையாளுதல்
- உற்பத்திக்கு தயாரான பிழை கையாளுதல் மற்றும் மீண்டும் முயற்சி செய்யும் தரவுகள்

## முன் தேவைகள்

1. **Foundry Local நிறுவல்**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python சார்ந்த பொருட்கள்**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## கட்டமைப்பு

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## முக்கிய அம்சங்கள்

### 1. **நேரடி HTTP ஒருங்கிணைப்பு**
- SDK சார்பில்லாமல் தூய REST API அழைப்புகள்
- தனிப்பயன் அங்கீகாரம் மற்றும் தலைப்புகள்
- கோரிக்கை/பதில் கையாளுதலில் முழு கட்டுப்பாடு

### 2. **மாடல் மேலாண்மை**
- மாறும் மாடல் ஏற்றுதல் மற்றும் இறக்குதல்
- ஆரோக்கிய கண்காணிப்பு மற்றும் நிலை சரிபார்ப்பு
- செயல்திறன் அளவீடுகள் சேகரிப்பு

### 3. **உற்பத்தி முறைகள்**
- பரிமாற்ற பின்வாங்கத்துடன் மீண்டும் முயற்சி செய்யும் முறை
- பிழை சகிப்புத்தன்மைக்கான சுற்று முறையீடு
- விரிவான பதிவு மற்றும் கண்காணிப்பு

### 4. **நெகிழ்வான பதில் கையாளுதல்**
- நேரடி பயன்பாடுகளுக்கான ஸ்ட்ரீமிங் பதில்கள்
- அதிக-திறன் சூழல்களுக்கான தொகுதி செயலாக்கம்
- தனிப்பயன் பதில் பகுப்பாய்வு மற்றும் சரிபார்ப்பு

## பயன்பாட்டு உதாரணங்கள்

### அடிப்படை API ஒருங்கிணைப்பு
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

### ஸ்ட்ரீமிங் ஒருங்கிணைப்பு
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### ஆரோக்கிய கண்காணிப்பு
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## கோப்பு அமைப்பு

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

## Microsoft Foundry Local ஒருங்கிணைப்பு

இந்த மாதிரி Microsoft-இன் அதிகாரப்பூர்வ முறைகளை பின்பற்றுகிறது:

1. **SDK ஒருங்கிணைப்பு**: சேவை மேலாண்மைக்கான `FoundryLocalManager` பயன்படுத்துகிறது
2. **REST முடுக்கங்கள்**: `/v1/chat/completions` மற்றும் பிற முடுக்கங்களுக்கு நேரடி அழைப்புகள்
3. **அங்கீகாரம்**: உள்ளூர் சேவைகளுக்கான சரியான API விசை கையாளுதல்
4. **மாடல் மேலாண்மை**: பட்டியல், பதிவிறக்கம் மற்றும் ஏற்றுதல் முறைகள்
5. **பிழை கையாளுதல்**: Microsoft பரிந்துரைத்த பிழை குறியீடுகள் மற்றும் பதில்கள்

## தொடங்குதல்

1. **சார்ந்த பொருட்களை நிறுவவும்**
   ```bash
   pip install -r requirements.txt
   ```

2. **அடிப்படை உதாரணத்தை இயக்கவும்**
   ```bash
   python examples/basic_usage.py
   ```

3. **ஸ்ட்ரீமிங் முயற்சிக்கவும்**
   ```bash
   python examples/streaming.py
   ```

4. **உற்பத்தி அமைப்பு**
   ```bash
   python examples/production.py
   ```

## கட்டமைப்பு

தனிப்பயனாக்கத்திற்கான சூழல் மாறிகள்:
- `FOUNDRY_MODEL`: பயன்படுத்த வேண்டிய இயல்புநிலை மாடல் (இயல்புநிலை: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: கோரிக்கை நேரம் முடிவடையும் விநாடிகள் (இயல்புநிலை: 30)
- `FOUNDRY_RETRIES`: மீண்டும் முயற்சிக்கும் எண்ணிக்கை (இயல்புநிலை: 3)
- `FOUNDRY_LOG_LEVEL`: பதிவு நிலை (இயல்புநிலை: "INFO")

## சிறந்த நடைமுறைகள்

1. **இணைப்பு மேலாண்மை**: சிறந்த செயல்திறனுக்காக HTTP இணைப்புகளை மீண்டும் பயன்படுத்தவும்
2. **பிழை கையாளுதல்**: பரிமாற்ற பின்வாங்கத்துடன் சரியான மீண்டும் முயற்சி தரவுகளை செயல்படுத்தவும்
3. **வள கண்காணிப்பு**: மாடல் நினைவக பயன்பாடு மற்றும் செயல்திறனை கண்காணிக்கவும்
4. **பாதுகாப்பு**: உள்ளூர் சேவைகளுக்காக சரியான அங்கீகாரத்தை பயன்படுத்தவும்
5. **சோதனை**: யூனிட் மற்றும் ஒருங்கிணைப்பு சோதனைகளை உள்ளடக்கவும்

## சிக்கல்களை சரிசெய்தல்

### பொதுவான பிரச்சினைகள்

**சேவை இயங்கவில்லை**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**மாடல் ஏற்றுதல் பிரச்சினைகள்**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**இணைப்பு பிழைகள்**
- Foundry Local சரியான போர்டில் இயங்குகிறதா என்பதை சரிபார்க்கவும்
- ஃபயர்வால் அமைப்புகளை சரிபார்க்கவும்
- சரியான அங்கீகார தலைப்புகளை உறுதிப்படுத்தவும்

## செயல்திறன் மேம்பாடு

1. **இணைப்பு குவியல்**: பல கோரிக்கைகளுக்காக அமர்வு பொருட்களை பயன்படுத்தவும்
2. **அசிங்க செயல்பாடுகள்**: ஒரே நேரத்தில் கோரிக்கைகளுக்காக asyncio-ஐ பயன்படுத்தவும்
3. **கேஷிங்**: தேவையான இடங்களில் மாடல் பதில்களை கேஷ் செய்யவும்
4. **கண்காணிப்பு**: பதில் நேரங்களை கண்காணித்து நேர முடிவுகளை சரிசெய்யவும்

## கற்றல் முடிவுகள்

இந்த மாதிரியை முடித்த பிறகு, நீங்கள் புரிந்துகொள்வீர்கள்:
- Foundry Local உடன் நேரடி REST API ஒருங்கிணைப்பு
- தனிப்பயன் HTTP கிளையன்ட் செயலாக்க முறைகள்
- உற்பத்திக்கு தயாரான பிழை கையாளுதல் மற்றும் கண்காணிப்பு
- Microsoft Foundry Local சேவை கட்டமைப்பு
- உள்ளூர் AI சேவைகளுக்கான செயல்திறன் மேம்பாட்டு உத்திகள்

## அடுத்த படிகள்

- மாதிரி 08: Windows 11 உரையாடல் பயன்பாட்டை ஆராயவும்
- மாதிரி 09: பல முகவர் ஒருங்கிணைப்பை முயற்சிக்கவும்
- மாதிரி 10: Foundry Local-ஐ கருவிகள் ஒருங்கிணைப்பாக கற்றுக்கொள்ளவும்

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.