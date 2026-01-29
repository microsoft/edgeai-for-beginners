# Open WebUI + Foundry Local एकत्रीकरण मार्गदर्शक

ही मार्गदर्शिका Open WebUI ला Microsoft Foundry Local शी जोडण्याची प्रक्रिया स्पष्ट करते, ज्यामुळे तुमच्या स्थानिक AI मॉडेल्सद्वारे समर्थित व्यावसायिक ChatGPT-सदृश इंटरफेस तयार होतो.

## आढावा

Open WebUI एक आधुनिक, वापरकर्ता-अनुकूल चॅट इंटरफेस प्रदान करते जो कोणत्याही OpenAI-सुसंगत API शी कनेक्ट होऊ शकतो. Foundry Local शी जोडल्याने तुम्हाला मिळते:

- **व्यावसायिक UI**: आधुनिक डिझाइनसह ChatGPT-सदृश इंटरफेस
- **स्थानिक गोपनीयता**: सर्व प्रक्रिया तुमच्या डिव्हाइसवर होते
- **मॉडेल स्विचिंग**: वेगवेगळ्या स्थानिक मॉडेल्समध्ये सहज स्विचिंग
- **संवाद इतिहास**: टिकाऊ चॅट इतिहास आणि संदर्भ
- **फाइल अपलोड्स**: दस्तऐवज विश्लेषण आणि फाइल प्रक्रिया क्षमता
- **कस्टम व्यक्तिमत्वे**: सिस्टम प्रॉम्प्ट्स आणि भूमिका सानुकूलन

## पूर्वतयारी

### आवश्यक सॉफ्टवेअर

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### मॉडेल लोड करा

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## जलद सेटअप (शिफारस केलेले)

### चरण 1: Docker सह Open WebUI चालवा

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

### चरण 2: प्रारंभिक सेटअप

1. **ब्राउझर उघडा**: `http://localhost:3000` वर जा
2. **खाते तयार करा**: प्रशासक वापरकर्ता सेट करा (पहिला वापरकर्ता प्रशासक बनतो)
3. **कनेक्शन सत्यापित करा**: मॉडेल्स स्वयंचलितपणे ड्रॉपडाउनमध्ये दिसायला हवे

### चरण 3: कनेक्शन चाचणी करा

1. ड्रॉपडाउनमधून तुमचे मॉडेल निवडा (उदा., "phi-4-mini")
2. एक चाचणी संदेश टाइप करा: "हॅलो! तुम्ही स्वतःची ओळख करून देऊ शकता का?"
3. तुम्हाला तुमच्या स्थानिक मॉडेलकडून प्रवाहित प्रतिसाद दिसायला हवा

## प्रगत कॉन्फिगरेशन

### पर्यावरणीय व्हेरिएबल्स

| व्हेरिएबल | उद्देश | डीफॉल्ट | उदाहरण |
|-----------|--------|---------|---------|
| `OPENAI_API_BASE_URL` | Foundry Local एंडपॉइंट | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API की (स्थानिकपणे आवश्यक नाही) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | सत्र एन्क्रिप्शन की | स्वयंचलितपणे तयार केलेली | `your-secret-key` |
| `ENABLE_SIGNUP` | नवीन वापरकर्ता नोंदणीला परवानगी द्या | `True` | `False` |

### मॅन्युअल कॉन्फिगरेशन (पर्याय)

जर पर्यावरणीय व्हेरिएबल्स कार्य करत नसतील, तर मॅन्युअल कॉन्फिगरेशन करा:

1. **सेटिंग्स उघडा**: सेटिंग्स (गियर आयकॉन) वर क्लिक करा
2. **कनेक्शन्सकडे जा**: सेटिंग्स → कनेक्शन्स → OpenAI
3. **API तपशील सेट करा**:
   - API बेस URL: `http://host.docker.internal:51211/v1`
   - API की: `foundry-local-key` (कोणतीही किंमत चालेल)
4. **सेव्ह करा आणि चाचणी करा**: "सेव्ह" वर क्लिक करा आणि मॉडेलसह चाचणी करा

### टिकाऊ डेटा स्टोरेज

संवाद आणि सेटिंग्ज टिकवण्यासाठी:

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

## समस्या निवारण

### कनेक्शन समस्या

**समस्या**: "कनेक्शन नाकारले" किंवा मॉडेल्स लोड होत नाहीत

**उपाय**:
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

### मॉडेल दिसत नाही

**समस्या**: Open WebUI ड्रॉपडाउनमध्ये कोणतेही मॉडेल दाखवत नाही

**डिबगिंग चरण**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**दुरुस्ती**: सुनिश्चित करा की मॉडेल योग्य प्रकारे लोड केले आहे:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker नेटवर्क समस्या

**समस्या**: `host.docker.internal` रिझॉल्व होत नाही

**Windows उपाय**:
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

**पर्याय**: तुमच्या मशीनचा IP शोधा:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### कार्यक्षमता समस्या

**मंद प्रतिसाद**:
1. तपासा की मॉडेल GPU प्रवेग वापरत आहे: `foundry service ps`
2. पुरेसे सिस्टम संसाधने (RAM/GPU मेमरी) सत्यापित करा
3. चाचणीसाठी लहान मॉडेल वापरण्याचा विचार करा

**मेमरी समस्या**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## वापर मार्गदर्शक

### मूलभूत चॅट

1. **मॉडेल निवडा**: ड्रॉपडाउनमधून निवडा (Foundry Local मॉडेल्स दर्शवते)
2. **संदेश टाइप करा**: तळाशी टेक्स्ट इनपुट वापरा
3. **पाठवा**: Enter दाबा किंवा Send बटणावर क्लिक करा
4. **प्रतिसाद पहा**: रिअल-टाइममध्ये प्रवाहित प्रतिसाद पहा

### प्रगत वैशिष्ट्ये

**फाइल अपलोड**:
1. पेपरक्लिप आयकॉनवर क्लिक करा
2. दस्तऐवज अपलोड करा (PDF, TXT, इ.)
3. सामग्रीबद्दल प्रश्न विचारा
4. मॉडेल दस्तऐवजाचे विश्लेषण करून प्रतिसाद देईल

**कस्टम सिस्टम प्रॉम्प्ट्स**:
1. सेटिंग्स → वैयक्तिकरण
2. कस्टम सिस्टम प्रॉम्प्ट सेट करा
3. सुसंगत AI व्यक्तिमत्व/वर्तन तयार करते

**संवाद व्यवस्थापन**:
- **नवीन चॅट**: नवीन संवाद सुरू करण्यासाठी "+" क्लिक करा
- **चॅट इतिहास**: साइडबारमधून मागील संवादांमध्ये प्रवेश करा
- **निर्यात करा**: चॅट इतिहास टेक्स्ट/JSON म्हणून डाउनलोड करा

**मॉडेल तुलना**:
1. Open WebUI च्या एकाच ब्राउझर टॅबमध्ये जा
2. प्रत्येक टॅबमध्ये वेगवेगळे मॉडेल निवडा
3. समान प्रॉम्प्ट्ससाठी प्रतिसादांची तुलना करा

### एकत्रीकरण नमुने

**विकसन कार्यप्रवाह**:
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

### बहु-वापरकर्ता सेटअप

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

### मॉनिटरिंग आणि लॉगिंग

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## साफसफाई

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

## पुढील चरण

### सुधारणा कल्पना

1. **कस्टम मॉडेल्स**: Foundry Local मध्ये तुमची स्वतःची फाइन-ट्यून केलेली मॉडेल्स जोडा
2. **API एकत्रीकरण**: Open WebUI फंक्शन्सद्वारे बाह्य API शी कनेक्ट करा
3. **दस्तऐवज प्रक्रिया**: प्रगत RAG पाइपलाइन्स सेट करा
4. **मल्टी-मोडल**: इमेज विश्लेषणासाठी व्हिजन मॉडेल्स कॉन्फिगर करा

### स्केलिंग विचार

- **लोड बॅलन्सिंग**: रिव्हर्स प्रॉक्सी मागे अनेक Foundry Local उदाहरणे
- **मॉडेल रूटिंग**: वेगवेगळ्या वापर प्रकरणांसाठी वेगवेगळे मॉडेल्स
- **संसाधन व्यवस्थापन**: एकत्रित वापरकर्त्यांसाठी GPU मेमरी ऑप्टिमायझेशन
- **बॅकअप धोरण**: संवाद डेटा आणि कॉन्फिगरेशन्सचे नियमित बॅकअप

## संदर्भ

- [Open WebUI दस्तऐवज](https://docs.openwebui.com/)
- [Open WebUI GitHub रिपॉझिटरी](https://github.com/open-webui/open-webui)
- [Foundry Local दस्तऐवज](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker इंस्टॉलेशन मार्गदर्शक](https://docs.docker.com/get-docker/)

---

