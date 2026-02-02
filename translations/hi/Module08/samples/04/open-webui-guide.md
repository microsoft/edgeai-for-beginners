# Open WebUI + Foundry Local इंटीग्रेशन गाइड

यह गाइड दिखाता है कि Open WebUI को Microsoft Foundry Local से कैसे कनेक्ट करें ताकि आपके लोकल AI मॉडल्स द्वारा संचालित एक पेशेवर ChatGPT जैसा इंटरफेस प्राप्त हो सके।

## अवलोकन

Open WebUI एक आधुनिक, उपयोगकर्ता-अनुकूल चैट इंटरफेस प्रदान करता है जो किसी भी OpenAI-संगत API से कनेक्ट हो सकता है। इसे Foundry Local से जोड़कर आप प्राप्त करते हैं:

- **पेशेवर UI**: ChatGPT जैसा इंटरफेस आधुनिक डिज़ाइन के साथ
- **लोकल प्राइवेसी**: सभी प्रोसेसिंग आपके डिवाइस पर होती है
- **मॉडल स्विचिंग**: विभिन्न लोकल मॉडल्स के बीच आसानी से स्विच करें
- **कन्वर्सेशन हिस्ट्री**: स्थायी चैट इतिहास और संदर्भ
- **फाइल अपलोड्स**: दस्तावेज़ विश्लेषण और फाइल प्रोसेसिंग की क्षमता
- **कस्टम पर्सनाज**: सिस्टम प्रॉम्प्ट्स और रोल कस्टमाइज़ेशन

## आवश्यकताएँ

### आवश्यक सॉफ़्टवेयर

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### मॉडल लोड करें

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## त्वरित सेटअप (अनुशंसित)

### चरण 1: Open WebUI को Docker के साथ चलाएँ

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

1. **ब्राउज़र खोलें**: `http://localhost:3000` पर जाएँ
2. **खाता बनाएं**: एडमिन उपयोगकर्ता सेट करें (पहला उपयोगकर्ता एडमिन बनता है)
3. **कनेक्शन सत्यापित करें**: मॉडल्स स्वतः ड्रॉपडाउन में दिखाई देने चाहिए

### चरण 3: कनेक्शन का परीक्षण करें

1. ड्रॉपडाउन से अपना मॉडल चुनें (जैसे, "phi-4-mini")
2. एक परीक्षण संदेश टाइप करें: "नमस्ते! क्या आप अपना परिचय दे सकते हैं?"
3. आपको अपने लोकल मॉडल से स्ट्रीमिंग प्रतिक्रिया दिखाई देनी चाहिए

## उन्नत कॉन्फ़िगरेशन

### एनवायरनमेंट वेरिएबल्स

| वेरिएबल | उद्देश्य | डिफ़ॉल्ट | उदाहरण |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local का एंडपॉइंट | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API कुंजी (लोकल उपयोग के लिए आवश्यक नहीं) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | सत्र एन्क्रिप्शन कुंजी | स्वतः उत्पन्न | `your-secret-key` |
| `ENABLE_SIGNUP` | नए उपयोगकर्ता पंजीकरण की अनुमति दें | `True` | `False` |

### मैनुअल कॉन्फ़िगरेशन (वैकल्पिक)

यदि एनवायरनमेंट वेरिएबल्स काम नहीं करते हैं, तो मैनुअल कॉन्फ़िगर करें:

1. **सेटिंग्स खोलें**: सेटिंग्स (गियर आइकन) पर क्लिक करें
2. **कनेक्शन्स पर जाएं**: सेटिंग्स → कनेक्शन्स → OpenAI
3. **API विवरण सेट करें**:
   - API बेस URL: `http://host.docker.internal:51211/v1`
   - API कुंजी: `foundry-local-key` (कोई भी मान काम करेगा)
4. **सेव और टेस्ट करें**: "सेव" पर क्लिक करें और फिर मॉडल के साथ परीक्षण करें

### स्थायी डेटा स्टोरेज

कन्वर्सेशन और सेटिंग्स को स्थायी बनाने के लिए:

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

### कनेक्शन समस्याएँ

**समस्या**: "कनेक्शन अस्वीकृत" या मॉडल्स लोड नहीं हो रहे

**समाधान**:
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

### मॉडल दिखाई नहीं दे रहा

**समस्या**: Open WebUI ड्रॉपडाउन में कोई मॉडल नहीं दिखा रहा

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

**समाधान**: सुनिश्चित करें कि मॉडल सही तरीके से लोड हुआ है:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker नेटवर्क समस्याएँ

**समस्या**: `host.docker.internal` हल नहीं हो रहा

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

**वैकल्पिक**: अपने मशीन का IP पता खोजें:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### प्रदर्शन समस्याएँ

**धीमी प्रतिक्रियाएँ**:
1. जांचें कि मॉडल GPU एक्सेलेरेशन का उपयोग कर रहा है: `foundry service ps`
2. पर्याप्त सिस्टम संसाधनों (RAM/GPU मेमोरी) की पुष्टि करें
3. परीक्षण के लिए छोटे मॉडल का उपयोग करने पर विचार करें

**मेमोरी समस्याएँ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## उपयोग गाइड

### बेसिक चैट

1. **मॉडल चुनें**: ड्रॉपडाउन से चुनें (Foundry Local मॉडल्स दिखाता है)
2. **संदेश टाइप करें**: नीचे टेक्स्ट इनपुट का उपयोग करें
3. **भेजें**: Enter दबाएँ या Send बटन पर क्लिक करें
4. **प्रतिक्रिया देखें**: वास्तविक समय में स्ट्रीमिंग प्रतिक्रिया देखें

### उन्नत सुविधाएँ

**फाइल अपलोड**:
1. पेपरक्लिप आइकन पर क्लिक करें
2. दस्तावेज़ अपलोड करें (PDF, TXT, आदि)
3. सामग्री के बारे में प्रश्न पूछें
4. मॉडल दस्तावेज़ का विश्लेषण करेगा और उत्तर देगा

**कस्टम सिस्टम प्रॉम्प्ट्स**:
1. सेटिंग्स → पर्सनलाइज़ेशन
2. कस्टम सिस्टम प्रॉम्प्ट सेट करें
3. एक सुसंगत AI व्यक्तित्व/व्यवहार बनाता है

**कन्वर्सेशन प्रबंधन**:
- **नई चैट**: ताज़ा कन्वर्सेशन शुरू करने के लिए "+" पर क्लिक करें
- **चैट इतिहास**: साइडबार से पिछले कन्वर्सेशन एक्सेस करें
- **एक्सपोर्ट**: चैट इतिहास को टेक्स्ट/JSON के रूप में डाउनलोड करें

**मॉडल तुलना**:
1. Open WebUI को एक ही ब्राउज़र में कई टैब्स में खोलें
2. प्रत्येक टैब में अलग-अलग मॉडल चुनें
3. समान प्रॉम्प्ट्स के लिए प्रतिक्रियाओं की तुलना करें

### इंटीग्रेशन पैटर्न

**डेवलपमेंट वर्कफ़्लो**:
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

## प्रोडक्शन डिप्लॉयमेंट

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

### मल्टी-यूजर सेटअप

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

### मॉनिटरिंग और लॉगिंग

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## सफाई

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

## अगले चरण

### सुधार के विचार

1. **कस्टम मॉडल्स**: Foundry Local में अपने स्वयं के फाइन-ट्यून किए गए मॉडल्स जोड़ें
2. **API इंटीग्रेशन**: Open WebUI फंक्शन्स के माध्यम से बाहरी APIs से कनेक्ट करें
3. **दस्तावेज़ प्रोसेसिंग**: उन्नत RAG पाइपलाइन्स सेट करें
4. **मल्टी-मोडल**: इमेज एनालिसिस के लिए विज़न मॉडल्स कॉन्फ़िगर करें

### स्केलिंग विचार

- **लोड बैलेंसिंग**: रिवर्स प्रॉक्सी के पीछे कई Foundry Local इंस्टेंस
- **मॉडल रूटिंग**: विभिन्न उपयोग मामलों के लिए अलग-अलग मॉडल्स
- **संसाधन प्रबंधन**: समवर्ती उपयोगकर्ताओं के लिए GPU मेमोरी का अनुकूलन
- **बैकअप रणनीति**: कन्वर्सेशन डेटा और कॉन्फ़िगरेशन का नियमित बैकअप

## संदर्भ

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

