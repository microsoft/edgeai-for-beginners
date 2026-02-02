# Foundry Local को API के रूप में उपयोग करने का नमूना

यह नमूना दिखाता है कि Microsoft Foundry Local को REST API सेवा के रूप में OpenAI SDK पर निर्भर हुए बिना कैसे उपयोग किया जा सकता है। यह अधिकतम नियंत्रण और अनुकूलन के लिए सीधे HTTP एकीकरण पैटर्न प्रस्तुत करता है।

## अवलोकन

Microsoft के आधिकारिक Foundry Local पैटर्न पर आधारित, यह नमूना प्रदान करता है:
- FoundryLocalManager के साथ सीधे REST API एकीकरण
- कस्टम HTTP क्लाइंट कार्यान्वयन
- मॉडल प्रबंधन और स्वास्थ्य निगरानी
- स्ट्रीमिंग और गैर-स्ट्रीमिंग प्रतिक्रिया हैंडलिंग
- उत्पादन-तैयार त्रुटि हैंडलिंग और पुनः प्रयास तर्क

## आवश्यकताएँ

1. **Foundry Local इंस्टॉलेशन**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python डिपेंडेंसी**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## आर्किटेक्चर

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## मुख्य विशेषताएँ

### 1. **सीधा HTTP एकीकरण**
- SDK निर्भरता के बिना शुद्ध REST API कॉल
- कस्टम प्रमाणीकरण और हेडर
- अनुरोध/प्रतिक्रिया हैंडलिंग पर पूर्ण नियंत्रण

### 2. **मॉडल प्रबंधन**
- डायनामिक मॉडल लोडिंग और अनलोडिंग
- स्वास्थ्य निगरानी और स्थिति जांच
- प्रदर्शन मेट्रिक्स संग्रह

### 3. **उत्पादन पैटर्न**
- एक्सपोनेंशियल बैकऑफ के साथ पुनः प्रयास तंत्र
- फॉल्ट टॉलरेंस के लिए सर्किट ब्रेकर
- व्यापक लॉगिंग और निगरानी

### 4. **लचीली प्रतिक्रिया हैंडलिंग**
- रीयल-टाइम एप्लिकेशन के लिए स्ट्रीमिंग प्रतिक्रियाएँ
- उच्च-थ्रूपुट परिदृश्यों के लिए बैच प्रोसेसिंग
- कस्टम प्रतिक्रिया पार्सिंग और सत्यापन

## उपयोग के उदाहरण

### बेसिक API एकीकरण
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

### स्ट्रीमिंग एकीकरण
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### स्वास्थ्य निगरानी
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## फ़ाइल संरचना

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

## Microsoft Foundry Local एकीकरण

यह नमूना Microsoft के आधिकारिक पैटर्न का अनुसरण करता है:

1. **SDK एकीकरण**: सेवा प्रबंधन के लिए `FoundryLocalManager` का उपयोग करता है
2. **REST एंडपॉइंट्स**: `/v1/chat/completions` और अन्य एंडपॉइंट्स पर सीधे कॉल करता है
3. **प्रमाणीकरण**: स्थानीय सेवाओं के लिए उचित API कुंजी हैंडलिंग
4. **मॉडल प्रबंधन**: कैटलॉग सूची, डाउनलोडिंग, और लोडिंग पैटर्न
5. **त्रुटि हैंडलिंग**: Microsoft द्वारा अनुशंसित त्रुटि कोड और प्रतिक्रियाएँ

## आरंभ करना

1. **डिपेंडेंसी इंस्टॉल करें**
   ```bash
   pip install -r requirements.txt
   ```

2. **बेसिक उदाहरण चलाएँ**
   ```bash
   python examples/basic_usage.py
   ```

3. **स्ट्रीमिंग आज़माएँ**
   ```bash
   python examples/streaming.py
   ```

4. **उत्पादन सेटअप**
   ```bash
   python examples/production.py
   ```

## कॉन्फ़िगरेशन

अनुकूलन के लिए पर्यावरण चर:
- `FOUNDRY_MODEL`: उपयोग करने के लिए डिफ़ॉल्ट मॉडल (डिफ़ॉल्ट: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: अनुरोध टाइमआउट सेकंड में (डिफ़ॉल्ट: 30)
- `FOUNDRY_RETRIES`: पुनः प्रयासों की संख्या (डिफ़ॉल्ट: 3)
- `FOUNDRY_LOG_LEVEL`: लॉगिंग स्तर (डिफ़ॉल्ट: "INFO")

## सर्वोत्तम अभ्यास

1. **कनेक्शन प्रबंधन**: बेहतर प्रदर्शन के लिए HTTP कनेक्शन को पुनः उपयोग करें
2. **त्रुटि हैंडलिंग**: एक्सपोनेंशियल बैकऑफ के साथ उचित पुनः प्रयास तर्क लागू करें
3. **संसाधन निगरानी**: मॉडल मेमोरी उपयोग और प्रदर्शन को ट्रैक करें
4. **सुरक्षा**: स्थानीय सेवाओं के लिए भी उचित प्रमाणीकरण का उपयोग करें
5. **परीक्षण**: यूनिट और इंटीग्रेशन परीक्षण दोनों शामिल करें

## समस्या निवारण

### सामान्य समस्याएँ

**सेवा चालू नहीं है**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**मॉडल लोडिंग समस्याएँ**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**कनेक्शन त्रुटियाँ**
- सुनिश्चित करें कि Foundry Local सही पोर्ट पर चल रहा है
- फ़ायरवॉल सेटिंग्स की जाँच करें
- उचित प्रमाणीकरण हेडर सुनिश्चित करें

## प्रदर्शन अनुकूलन

1. **कनेक्शन पूलिंग**: कई अनुरोधों के लिए सत्र ऑब्जेक्ट का उपयोग करें
2. **आसिंक ऑपरेशन**: समवर्ती अनुरोधों के लिए asyncio का लाभ उठाएँ
3. **कैशिंग**: जहाँ उपयुक्त हो, मॉडल प्रतिक्रियाओं को कैश करें
4. **निगरानी**: प्रतिक्रिया समय को ट्रैक करें और टाइमआउट समायोजित करें

## सीखने के परिणाम

इस नमूने को पूरा करने के बाद, आप समझेंगे:
- Foundry Local के साथ सीधे REST API एकीकरण
- कस्टम HTTP क्लाइंट कार्यान्वयन पैटर्न
- उत्पादन-तैयार त्रुटि हैंडलिंग और निगरानी
- Microsoft Foundry Local सेवा आर्किटेक्चर
- स्थानीय AI सेवाओं के लिए प्रदर्शन अनुकूलन तकनीकें

## अगले कदम

- नमूना 08: Windows 11 चैट एप्लिकेशन का अन्वेषण करें
- नमूना 09: मल्टी-एजेंट ऑर्केस्ट्रेशन आज़माएँ
- नमूना 10: Foundry Local को टूल्स के साथ एकीकृत करना सीखें

---

