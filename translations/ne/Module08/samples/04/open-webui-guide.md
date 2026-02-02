# Open WebUI + Foundry Local एकीकृत मार्गदर्शन

यो मार्गदर्शनले Open WebUI लाई Microsoft Foundry Local सँग कसरी जोड्ने भन्ने देखाउँछ, जसले तपाईंको स्थानीय AI मोडेलहरूद्वारा संचालित एक पेशेवर ChatGPT-जस्तो इन्टरफेस प्रदान गर्दछ।

## अवलोकन

Open WebUI ले आधुनिक, प्रयोगकर्ता-अनुकूल च्याट इन्टरफेस प्रदान गर्दछ जुन कुनै पनि OpenAI-संगत API सँग जडान गर्न सकिन्छ। यसलाई Foundry Local सँग जोड्दा तपाईंले निम्न फाइदाहरू प्राप्त गर्नुहुन्छ:

- **पेशेवर UI**: आधुनिक डिजाइनसहित ChatGPT-जस्तो इन्टरफेस
- **स्थानीय गोपनीयता**: सबै प्रक्रिया तपाईंको उपकरणमा मात्र हुन्छ
- **मोडेल स्विचिङ**: विभिन्न स्थानीय मोडेलहरू बीच सजिलै स्विच गर्न सकिने
- **वार्तालाप इतिहास**: स्थायी च्याट इतिहास र सन्दर्भ
- **फाइल अपलोडहरू**: दस्तावेज विश्लेषण र फाइल प्रशोधन क्षमता
- **कस्टम पर्सोना**: प्रणाली प्रॉम्प्टहरू र भूमिका अनुकूलन

## आवश्यकताहरू

### आवश्यक सफ्टवेयर

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### मोडेल लोड गर्नुहोस्

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## छिटो सेटअप (सिफारिस गरिएको)

### चरण १: Docker प्रयोग गरेर Open WebUI चलाउनुहोस्

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

### चरण २: प्रारम्भिक सेटअप

1. **ब्राउजर खोल्नुहोस्**: `http://localhost:3000` मा जानुहोस्
2. **खाता सिर्जना गर्नुहोस्**: एडमिन प्रयोगकर्ता सेटअप गर्नुहोस् (पहिलो प्रयोगकर्ता एडमिन बन्छ)
3. **जडान पुष्टि गर्नुहोस्**: मोडेलहरू स्वचालित रूपमा ड्रपडाउनमा देखिनु पर्छ

### चरण ३: जडान परीक्षण गर्नुहोस्

1. ड्रपडाउनबाट आफ्नो मोडेल चयन गर्नुहोस् (जस्तै, "phi-4-mini")
2. परीक्षण सन्देश टाइप गर्नुहोस्: "नमस्ते! के तपाईं आफ्नो परिचय दिन सक्नुहुन्छ?"
3. तपाईंले आफ्नो स्थानीय मोडेलबाट स्ट्रिमिङ प्रतिक्रिया देख्नुहुनेछ

## उन्नत कन्फिगरेसन

### वातावरण चरहरू

| चर | उद्देश्य | डिफल्ट | उदाहरण |
|----|---------|--------|---------|
| `OPENAI_API_BASE_URL` | Foundry Local अन्त बिन्दु | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API कुञ्जी (आवश्यक तर स्थानीय रूपमा प्रयोग हुँदैन) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | सत्र इन्क्रिप्शन कुञ्जी | स्वतः उत्पन्न | `your-secret-key` |
| `ENABLE_SIGNUP` | नयाँ प्रयोगकर्ता दर्ता अनुमति दिनुहोस् | `True` | `False` |

### म्यानुअल कन्फिगरेसन (वैकल्पिक)

यदि वातावरण चरहरू काम गर्दैनन् भने, म्यानुअल रूपमा कन्फिगर गर्नुहोस्:

1. **सेटिङ खोल्नुहोस्**: सेटिङ (गियर आइकन) क्लिक गर्नुहोस्
2. **जडानहरूमा जानुहोस्**: सेटिङ → जडानहरू → OpenAI
3. **API विवरण सेट गर्नुहोस्**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (कुनै पनि मान्य मान काम गर्छ)
4. **सेभ र परीक्षण गर्नुहोस्**: "सेभ" क्लिक गर्नुहोस् र मोडेलसँग परीक्षण गर्नुहोस्

### स्थायी डेटा भण्डारण

वार्तालाप र सेटिङहरू स्थायी बनाउन:

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

## समस्या समाधान

### जडान समस्या

**समस्या**: "Connection refused" वा मोडेलहरू लोड हुँदैनन्

**समाधानहरू**:
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

### मोडेल देखिँदैन

**समस्या**: Open WebUI मा ड्रपडाउनमा कुनै मोडेल देखिँदैन

**डिबगिङ चरणहरू**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**समाधान**: सुनिश्चित गर्नुहोस् कि मोडेल ठीकसँग लोड गरिएको छ:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker नेटवर्क समस्या

**समस्या**: `host.docker.internal` समाधान हुँदैन

**Windows समाधान**:
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

**वैकल्पिक**: आफ्नो मेसिनको IP पत्ता लगाउनुहोस्:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### प्रदर्शन समस्या

**ढिलो प्रतिक्रिया**:
1. सुनिश्चित गर्नुहोस् कि मोडेल GPU एक्सेलेरेशन प्रयोग गर्दैछ: `foundry service ps`
2. पर्याप्त प्रणाली स्रोतहरू (RAM/GPU मेमोरी) जाँच गर्नुहोस्
3. परीक्षणको लागि सानो मोडेल प्रयोग गर्ने विचार गर्नुहोस्

**मेमोरी समस्या**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## प्रयोग मार्गदर्शन

### आधारभूत च्याट

1. **मोडेल चयन गर्नुहोस्**: ड्रपडाउनबाट चयन गर्नुहोस् (Foundry Local मोडेलहरू देखाउँछ)
2. **सन्देश टाइप गर्नुहोस्**: तलको टेक्स्ट इनपुट प्रयोग गर्नुहोस्
3. **पठाउनुहोस्**: Enter थिच्नुहोस् वा Send बटन क्लिक गर्नुहोस्
4. **प्रतिक्रिया हेर्नुहोस्**: वास्तविक समयमा स्ट्रिमिङ प्रतिक्रिया हेर्नुहोस्

### उन्नत सुविधाहरू

**फाइल अपलोड**:
1. पेपरक्लिप आइकन क्लिक गर्नुहोस्
2. दस्तावेज अपलोड गर्नुहोस् (PDF, TXT, आदि)
3. सामग्रीबारे प्रश्न सोध्नुहोस्
4. मोडेलले दस्तावेजको आधारमा विश्लेषण र प्रतिक्रिया दिनेछ

**कस्टम प्रणाली प्रॉम्प्टहरू**:
1. सेटिङ → व्यक्तिगतकरण
2. कस्टम प्रणाली प्रॉम्प्ट सेट गर्नुहोस्
3. स्थिर AI व्यक्तित्व/व्यवहार सिर्जना गर्दछ

**वार्तालाप व्यवस्थापन**:
- **नयाँ च्याट**: "+" क्लिक गरेर नयाँ वार्तालाप सुरु गर्नुहोस्
- **च्याट इतिहास**: साइडबारबाट अघिल्लो वार्तालापहरू पहुँच गर्नुहोस्
- **एक्सपोर्ट**: च्याट इतिहासलाई टेक्स्ट/JSON रूपमा डाउनलोड गर्नुहोस्

**मोडेल तुलना**:
1. Open WebUI को एउटै इन्टरफेसमा धेरै ब्राउजर ट्याबहरू खोल्नुहोस्
2. प्रत्येक ट्याबमा फरक मोडेल चयन गर्नुहोस्
3. एउटै प्रॉम्प्टहरूमा प्रतिक्रिया तुलना गर्नुहोस्

### एकीकरण ढाँचा

**विकास कार्यप्रवाह**:
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

## उत्पादन परिनियोजन

### सुरक्षित सेटअप

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

### बहु-प्रयोगकर्ता सेटअप

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

### निगरानी र लगिङ

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## सफाइ

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

## आगामी चरणहरू

### सुधारका विचारहरू

1. **कस्टम मोडेलहरू**: Foundry Local मा आफ्नै फाइन-ट्युन गरिएको मोडेलहरू थप्नुहोस्
2. **API एकीकरण**: Open WebUI कार्यहरू मार्फत बाह्य API हरूसँग जडान गर्नुहोस्
3. **दस्तावेज प्रशोधन**: उन्नत RAG पाइपलाइनहरू सेटअप गर्नुहोस्
4. **मल्टी-मोडल**: छवि विश्लेषणको लागि भिजन मोडेलहरू कन्फिगर गर्नुहोस्

### स्केलिङ विचारहरू

- **लोड ब्यालेन्सिङ**: रिभर्स प्रोक्सी पछाडि धेरै Foundry Local उदाहरणहरू
- **मोडेल रुटिङ**: विभिन्न प्रयोगका लागि फरक मोडेलहरू
- **स्रोत व्यवस्थापन**: GPU मेमोरी अनुकूलन धेरै प्रयोगकर्ताहरूका लागि
- **ब्याकअप रणनीति**: वार्तालाप डेटा र कन्फिगरेसनहरूको नियमित ब्याकअप

## सन्दर्भहरू

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

