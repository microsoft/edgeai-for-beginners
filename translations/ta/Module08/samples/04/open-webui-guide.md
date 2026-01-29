# Open WebUI + Foundry Local இணைப்பு வழிகாட்டி

இந்த வழிகாட்டி Open WebUI-யை Microsoft Foundry Local-க்கு இணைப்பதற்கான வழிமுறைகளை விளக்குகிறது, இது உங்கள் உள்ளூர் AI மாதிரிகளால் இயக்கப்படும் ஒரு தொழில்முறை ChatGPT போன்ற இடைமுகத்தை வழங்குகிறது.

## மேற்பார்வை

Open WebUI ஒரு நவீன, பயனர் நட்பு உரையாடல் இடைமுகத்தை வழங்குகிறது, இது எந்த OpenAI-இன் இணக்கமான API-க்கும் இணைக்க முடியும். Foundry Local-க்கு இதை இணைப்பதன் மூலம், நீங்கள் பெறுகிறீர்கள்:

- **தொழில்முறை UI**: ChatGPT போன்ற நவீன வடிவமைப்புடன் கூடிய இடைமுகம்
- **உள்ளூர் தனியுரிமை**: அனைத்து செயலாக்கமும் உங்கள் சாதனத்தில் நடைபெறும்
- **மாதிரி மாறுதல்**: வெவ்வேறு உள்ளூர் மாதிரிகளை எளிதாக மாறுதல்
- **உரையாடல் வரலாறு**: நிலையான உரையாடல் வரலாறு மற்றும் சூழல்
- **கோப்பு பதிவேற்றங்கள்**: ஆவண பகுப்பாய்வு மற்றும் கோப்பு செயலாக்க திறன்கள்
- **தனிப்பயன் ஆளுமைகள்**: அமைப்பு உந்துதல்கள் மற்றும் பாத்திர தனிப்பயனாக்கம்

## முன் தேவைகள்

### தேவையான மென்பொருள்

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ஒரு மாதிரியை ஏற்றவும்

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## விரைவான அமைப்பு (பரிந்துரைக்கப்படுகிறது)

### படி 1: Docker மூலம் Open WebUI-யை இயக்கவும்

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### படி 2: ஆரம்ப அமைப்பு

1. **உலாவியை திறக்கவும்**: `http://localhost:3000`-க்கு செல்லவும்
2. **கணக்கை உருவாக்கவும்**: நிர்வாக பயனரை அமைக்கவும் (முதல் பயனர் நிர்வாகியாக மாறுவார்)
3. **இணைப்பை சரிபார்க்கவும்**: மாதிரிகள் தானாகவே dropdown-ல் தோன்ற வேண்டும்

### படி 3: இணைப்பை சோதிக்கவும்

1. உங்கள் மாதிரியை dropdown-ல் தேர்ந்தெடுக்கவும் (எ.கா., "phi-4-mini")
2. ஒரு சோதனை செய்தியை உள்ளிடவும்: "வணக்கம்! நீங்கள் உங்களை அறிமுகப்படுத்த முடியுமா?"
3. உங்கள் உள்ளூர் மாதிரியில் இருந்து ஒரு ஸ்ட்ரீமிங் பதிலை நீங்கள் காண வேண்டும்

## மேம்பட்ட கட்டமைப்பு

### சூழல் மாறிகள்

| மாறி | நோக்கம் | இயல்புநிலை | உதாரணம் |
|------|---------|-----------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local இறுதிப்புள்ளி | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API விசை (தேவை, ஆனால் உள்ளூரில் பயன்படுத்தப்படவில்லை) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | அமர்வு குறியாக்க விசை | தானாக உருவாக்கப்படும் | `your-secret-key` |
| `ENABLE_SIGNUP` | புதிய பயனர் பதிவு அனுமதி | `True` | `False` |

### கையேடு அமைப்பு (மாற்று)

சூழல் மாறிகள் வேலை செய்யவில்லை என்றால், கையேடு மூலம் அமைக்கவும்:

1. **அமைப்புகளை திறக்கவும்**: Settings (கியர் ஐகான்) கிளிக் செய்யவும்
2. **Connections-க்கு செல்லவும்**: Settings → Connections → OpenAI
3. **API விவரங்களை அமைக்கவும்**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (எந்த மதிப்பும் வேலை செய்யும்)
4. **சேமித்து சோதிக்கவும்**: "Save" கிளிக் செய்து, மாதிரியுடன் சோதிக்கவும்

### நிலையான தரவுத்தொகுப்பு சேமிப்பு

உரையாடல்கள் மற்றும் அமைப்புகளை நிலையாகச் சேமிக்க:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## சிக்கல் தீர்வு

### இணைப்பு சிக்கல்கள்

**சிக்கல்**: "Connection refused" அல்லது மாதிரிகள் ஏற்றப்படவில்லை

**தீர்வுகள்**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### மாதிரி தோன்றவில்லை

**சிக்கல்**: Open WebUI dropdown-ல் எந்த மாதிரியும் காட்டவில்லை

**Debugging Steps**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Fix**: மாதிரி சரியாக ஏற்றப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker நெட்வொர்க் சிக்கல்கள்

**சிக்கல்**: `host.docker.internal` தீர்மானிக்கப்படவில்லை

**Windows தீர்வு**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**மாற்று**: உங்கள் கணினியின் IP-ஐ கண்டறியவும்:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### செயல்திறன் சிக்கல்கள்

**மெதுவான பதில்கள்**:
1. மாதிரி GPU வேகப்படுத்தலைப் பயன்படுத்துகிறதா என்பதை சரிபார்க்கவும்: `foundry service ps`
2. போதுமான கணினி வளங்களை உறுதிப்படுத்தவும் (RAM/GPU நினைவகம்)
3. சோதனைக்காக சிறிய மாதிரியைப் பயன்படுத்த பரிந்துரைக்கப்படுகிறது

**நினைவக சிக்கல்கள்**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## பயன்பாட்டு வழிகாட்டி

### அடிப்படை உரையாடல்

1. **மாதிரியைத் தேர்ந்தெடுக்கவும்**: Dropdown-ல் Foundry Local மாதிரிகளைத் தேர்ந்தெடுக்கவும்
2. **செய்தியை உள்ளிடவும்**: கீழே உள்ள உரை உள்ளீட்டை பயன்படுத்தவும்
3. **அனுப்பவும்**: Enter அழுத்தவும் அல்லது Send பொத்தானை கிளிக் செய்யவும்
4. **பதில் பார்க்கவும்**: நேரடி ஸ்ட்ரீமிங் பதிலை காணவும்

### மேம்பட்ட அம்சங்கள்

**கோப்பு பதிவேற்றம்**:
1. காகித கிளிப்பை ஐகானை கிளிக் செய்யவும்
2. ஆவணத்தை பதிவேற்றவும் (PDF, TXT, போன்றவை)
3. உள்ளடக்கத்தைப் பற்றி கேள்விகள் கேட்கவும்
4. மாதிரி ஆவணத்தை பகுப்பாய்வு செய்து பதிலளிக்கும்

**தனிப்பயன் அமைப்பு உந்துதல்கள்**:
1. Settings → Personalization
2. தனிப்பயன் அமைப்பு உந்துதலை அமைக்கவும்
3. AI-யின் தனித்துவமான ஆளுமை/நடத்தை உருவாக்குகிறது

**உரையாடல் மேலாண்மை**:
- **புதிய உரையாடல்**: புதிய உரையாடலைத் தொடங்க "+" கிளிக் செய்யவும்
- **உரையாடல் வரலாறு**: பக்கப்பட்டியில் முந்தைய உரையாடல்களை அணுகவும்
- **ஏற்றுமதி**: உரையாடல் வரலாற்றை text/JSON வடிவில் பதிவிறக்கவும்

**மாதிரி ஒப்பீடு**:
1. ஒரே Open WebUI-யை பல உலாவி தாவல்கள் திறக்கவும்
2. ஒவ்வொரு தாவலிலும் வெவ்வேறு மாதிரிகளைத் தேர்ந்தெடுக்கவும்
3. ஒரே உந்துதல்களுக்கு பதில்களை ஒப்பிடவும்

### ஒருங்கிணைப்பு முறை

**வளர்ச்சி பணியாளர்கள்**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## உற்பத்தி பரிணாமம்

### பாதுகாப்பான அமைப்பு

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### பல பயனர் அமைப்பு

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### கண்காணிப்பு மற்றும் பதிவு

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## சுத்தம் செய்யுதல்

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## அடுத்த படிகள்

### மேம்பாட்டு யோசனைகள்

1. **தனிப்பயன் மாதிரிகள்**: Foundry Local-க்கு உங்கள் சொந்த fine-tuned மாதிரிகளைச் சேர்க்கவும்
2. **API ஒருங்கிணைப்பு**: Open WebUI செயல்பாடுகள் மூலம் வெளிப்புற API-க்களை இணைக்கவும்
3. **ஆவண செயலாக்கம்**: மேம்பட்ட RAG குழாய்களை அமைக்கவும்
4. **பலவகை முறை**: படங்களை பகுப்பாய்வு செய்ய காட்சி மாதிரிகளை அமைக்கவும்

### அளவீட்டு கருத்துக்கள்

- **சுமை சமநிலை**: Reverse proxy பின்னால் பல Foundry Local நிகழ்வுகள்
- **மாதிரி வழிமுறைகள்**: வெவ்வேறு பயன்பாடுகளுக்கு வெவ்வேறு மாதிரிகள்
- **வள மேலாண்மை**: ஒரே நேரத்தில் பல பயனர்களுக்கு GPU நினைவகத்தை மேம்படுத்துதல்
- **காப்பு உத்தி**: உரையாடல் தரவுகள் மற்றும் அமைப்புகளின் வழக்கமான காப்பு

## குறிப்புகள்

- [Open WebUI ஆவணங்கள்](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local ஆவணங்கள்](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker நிறுவல் வழிகாட்டி](https://docs.docker.com/get-docker/)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.