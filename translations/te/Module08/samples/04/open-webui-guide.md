<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b64f4a8cbb9b8d57863b1101b111b05d",
  "translation_date": "2025-12-16T01:06:14+00:00",
  "source_file": "Module08/samples/04/open-webui-guide.md",
  "language_code": "te"
}
-->
# Open WebUI + Foundry Local ఇంటిగ్రేషన్ గైడ్

ఈ గైడ్ Open WebUIని Microsoft Foundry Localకి ఎలా కనెక్ట్ చేయాలో చూపిస్తుంది, మీ స్థానిక AI మోడల్స్ ద్వారా శక్తివంతమైన ప్రొఫెషనల్ ChatGPT-లాగా ఇంటర్‌ఫేస్ కోసం.

## అవలోకనం

Open WebUI ఆధునిక, వినియోగదారులకు స్నేహపూర్వకమైన చాట్ ఇంటర్‌ఫేస్‌ను అందిస్తుంది, ఇది ఏ OpenAI-అనుకూల APIకి కనెక్ట్ కావచ్చు. Foundry Localకి కనెక్ట్ చేయడం ద్వారా మీరు పొందుతారు:

- **ప్రొఫెషనల్ UI**: ఆధునిక డిజైన్‌తో ChatGPT-లాగా ఇంటర్‌ఫేస్  
- **స్థానిక గోప్యత**: అన్ని ప్రాసెసింగ్ మీ పరికరంలో జరుగుతుంది  
- **మోడల్ మార్పిడి**: వివిధ స్థానిక మోడల్స్ మధ్య సులభ మార్పిడి  
- **సంభాషణ చరిత్ర**: స్థిరమైన చాట్ చరిత్ర మరియు సందర్భం  
- **ఫైల్ అప్‌లోడ్లు**: డాక్యుమెంట్ విశ్లేషణ మరియు ఫైల్ ప్రాసెసింగ్ సామర్థ్యాలు  
- **కస్టమ్ పర్సోనాస్**: సిస్టమ్ ప్రాంప్ట్స్ మరియు పాత్ర అనుకూలీకరణ  

## ముందస్తు అవసరాలు

### అవసరమైన సాఫ్ట్‌వేర్

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### మోడల్ లోడ్ చేయడం

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## త్వరిత సెటప్ (సిఫార్సు చేయబడింది)

### దశ 1: Dockerతో Open WebUI నడపండి

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

### దశ 2: ప్రారంభ సెటప్

1. **బ్రౌజర్ ఓపెన్ చేయండి**: `http://localhost:3000`కి వెళ్లండి  
2. **ఖాతా సృష్టించండి**: అడ్మిన్ యూజర్ సెట్ చేయండి (మొదటి యూజర్ అడ్మిన్ అవుతాడు)  
3. **కనెక్షన్ నిర్ధారించండి**: మోడల్స్ ఆటోమేటిక్‌గా డ్రాప్‌డౌన్‌లో కనిపించాలి  

### దశ 3: కనెక్షన్ పరీక్షించండి

1. డ్రాప్‌డౌన్ నుండి మీ మోడల్ ఎంచుకోండి (ఉదా: "phi-4-mini")  
2. ఒక పరీక్ష సందేశం టైప్ చేయండి: "హలో! మీరు మీ గురించి పరిచయం చేయగలరా?"  
3. మీ స్థానిక మోడల్ నుండి స్ట్రీమింగ్ స్పందన కనిపించాలి  

## అధునాతన కాన్ఫిగరేషన్

### ఎన్విరాన్‌మెంట్ వేరియబుల్స్

| వేరియబుల్ | ప్రయోజనం | డిఫాల్ట్ | ఉదాహరణ |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local ఎండ్‌పాయింట్ | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API కీ (స్థానికంగా ఉపయోగించబడదు కానీ అవసరం) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | సెషన్ ఎన్‌క్రిప్షన్ కీ | ఆటో-జనరేట్ | `your-secret-key` |
| `ENABLE_SIGNUP` | కొత్త యూజర్ రిజిస్ట్రేషన్ అనుమతించు | `True` | `False` |

### మాన్యువల్ కాన్ఫిగరేషన్ (వికల్పం)

ఎన్విరాన్‌మెంట్ వేరియబుల్స్ పనిచేయకపోతే, మాన్యువల్‌గా సెటప్ చేయండి:

1. **సెట్టింగ్స్ ఓపెన్ చేయండి**: సెట్టింగ్స్ (గేర్ ఐకాన్) క్లిక్ చేయండి  
2. **కనెక్షన్స్‌కు వెళ్లండి**: సెట్టింగ్స్ → కనెక్షన్స్ → OpenAI  
3. **API వివరాలు సెట్ చేయండి**:  
   - API బేస్ URL: `http://host.docker.internal:51211/v1`  
   - API కీ: `foundry-local-key` (ఏ విలువ సరిపోతుంది)  
4. **సేవ్ చేసి పరీక్షించండి**: "సేవ్" క్లిక్ చేసి మోడల్‌తో పరీక్షించండి  

### స్థిరమైన డేటా నిల్వ

సంభాషణలు మరియు సెట్టింగ్స్ నిల్వ చేయడానికి:

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

## సమస్య పరిష్కారం

### కనెక్షన్ సమస్యలు

**సమస్య**: "కనెక్షన్ నిరాకరించబడింది" లేదా మోడల్స్ లోడ్ కావడం లేదు

**పరిష్కారాలు**:  
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

### మోడల్ కనిపించకపోవడం

**సమస్య**: Open WebUI డ్రాప్‌డౌన్‌లో మోడల్స్ కనిపించవు

**డీబగ్గింగ్ దశలు**:  
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**పరిష్కారం**: మోడల్ సరిగ్గా లోడ్ అయ్యిందని నిర్ధారించండి:  
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker నెట్‌వర్క్ సమస్యలు

**సమస్య**: `host.docker.internal` పరిష్కరించబడడం లేదు

**Windows పరిష్కారం**:  
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

**వికల్పం**: మీ మెషీన్ IP కనుగొనండి:  
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### పనితీరు సమస్యలు

**మందగతి స్పందనలు**:  
1. మోడల్ GPU యాక్సిలరేషన్ ఉపయోగిస్తున్నదో చూడండి: `foundry service ps`  
2. సరిపడా సిస్టమ్ వనరులు (RAM/GPU మెమరీ) ఉన్నాయో నిర్ధారించండి  
3. పరీక్ష కోసం చిన్న మోడల్ ఉపయోగించండి  

**మెమరీ సమస్యలు**:  
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## ఉపయోగం గైడ్

### ప్రాథమిక చాట్

1. **మోడల్ ఎంచుకోండి**: డ్రాప్‌డౌన్ నుండి ఎంచుకోండి (Foundry Local మోడల్స్ చూపిస్తుంది)  
2. **సందేశం టైప్ చేయండి**: దిగువ టెక్స్ట్ ఇన్‌పుట్ ఉపయోగించండి  
3. **పంపండి**: ఎంటర్ నొక్కండి లేదా పంపు బటన్ క్లిక్ చేయండి  
4. **స్పందన చూడండి**: రియల్-టైమ్‌లో స్ట్రీమింగ్ స్పందన చూడండి  

### అధునాతన ఫీచర్లు

**ఫైల్ అప్‌లోడ్**:  
1. పేపర్క్లిప్ ఐకాన్ క్లిక్ చేయండి  
2. డాక్యుమెంట్ అప్‌లోడ్ చేయండి (PDF, TXT, మొదలైనవి)  
3. కంటెంట్ గురించి ప్రశ్నలు అడగండి  
4. మోడల్ డాక్యుమెంట్ ఆధారంగా విశ్లేషించి స్పందిస్తుంది  

**కస్టమ్ సిస్టమ్ ప్రాంప్ట్స్**:  
1. సెట్టింగ్స్ → పర్సనలైజేషన్  
2. కస్టమ్ సిస్టమ్ ప్రాంప్ట్ సెట్ చేయండి  
3. స్థిరమైన AI వ్యక్తిత్వం/ప్రవర్తన సృష్టిస్తుంది  

**సంభాషణ నిర్వహణ**:  
- **కొత్త చాట్**: "+" క్లిక్ చేసి కొత్త సంభాషణ ప్రారంభించండి  
- **చాట్ చరిత్ర**: సైడ్‌బార్ నుండి పూర్వపు సంభాషణలు యాక్సెస్ చేయండి  
- **ఎగుమతి**: చాట్ చరిత్రను టెక్స్ట్/JSONగా డౌన్లోడ్ చేయండి  

**మోడల్ పోలిక**:  
1. ఒకే Open WebUIకి బహుళ బ్రౌజర్ ట్యాబ్స్ ఓపెన్ చేయండి  
2. ప్రతి ట్యాబ్‌లో వేర్వేరు మోడల్స్ ఎంచుకోండి  
3. ఒకే ప్రాంప్ట్స్‌కు స్పందనలను పోల్చండి  

### ఇంటిగ్రేషన్ నమూనాలు

**డెవలప్‌మెంట్ వర్క్‌ఫ్లో**:  
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

## ప్రొడక్షన్ డిప్లాయ్‌మెంట్

### సురక్షిత సెటప్

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

### బహుళ యూజర్ సెటప్

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

### మానిటరింగ్ మరియు లాగింగ్

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## క్లీనప్

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

## తదుపరి దశలు

### అభివృద్ధి ఆలోచనలు

1. **కస్టమ్ మోడల్స్**: మీ స్వంత ఫైన్-ట్యూన్ చేసిన మోడల్స్‌ను Foundry Localకి జోడించండి  
2. **API ఇంటిగ్రేషన్**: Open WebUI ఫంక్షన్స్ ద్వారా బాహ్య APIsకి కనెక్ట్ అవ్వండి  
3. **డాక్యుమెంట్ ప్రాసెసింగ్**: అధునాతన RAG పైప్లైన్స్ సెటప్ చేయండి  
4. **బహుముఖ**: చిత్రం విశ్లేషణ కోసం విజన్ మోడల్స్ కాన్ఫిగర్ చేయండి  

### స్కేలింగ్ పరిగణనలు

- **లోడ్ బ్యాలెన్సింగ్**: రివర్స్ ప్రాక్సీ వెనుక బహుళ Foundry Local ఇన్స్టాన్సులు  
- **మోడల్ రౌటింగ్**: వేర్వేరు ఉపయోగాల కోసం వేర్వేరు మోడల్స్  
- **వనరు నిర్వహణ**: సమకాలీన యూజర్ల కోసం GPU మెమరీ ఆప్టిమైజేషన్  
- **బ్యాకప్ వ్యూహం**: సంభాషణ డేటా మరియు కాన్ఫిగరేషన్లను నియమితంగా బ్యాకప్ చేయడం  

## సూచనలు

- [Open WebUI డాక్యుమెంటేషన్](https://docs.openwebui.com/)  
- [Open WebUI GitHub రిపోజిటరీ](https://github.com/open-webui/open-webui)  
- [Foundry Local డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)  
- [Docker ఇన్‌స్టాలేషన్ గైడ్](https://docs.docker.com/get-docker/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->