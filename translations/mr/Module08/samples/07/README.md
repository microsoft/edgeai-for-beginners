# Foundry Local as API Sample

हा नमुना Microsoft Foundry Local ला REST API सेवा म्हणून OpenAI SDK वर अवलंबून न राहता कसे वापरायचे हे दर्शवितो. हे जास्तीत जास्त नियंत्रण आणि सानुकूलनासाठी थेट HTTP एकत्रीकरण नमुने दाखवते.

## आढावा

Microsoft च्या अधिकृत Foundry Local नमुन्यांवर आधारित, हा नमुना प्रदान करतो:
- FoundryLocalManager सह थेट REST API एकत्रीकरण
- सानुकूल HTTP क्लायंट अंमलबजावणी
- मॉडेल व्यवस्थापन आणि आरोग्य निरीक्षण
- स्ट्रीमिंग आणि नॉन-स्ट्रीमिंग प्रतिसाद हाताळणी
- उत्पादनासाठी तयार त्रुटी हाताळणी आणि पुन्हा प्रयत्न करण्याचे तर्कशास्त्र

## पूर्वअट

1. **Foundry Local इंस्टॉलेशन**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Dependencies**
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

## मुख्य वैशिष्ट्ये

### 1. **थेट HTTP एकत्रीकरण**
- SDK अवलंबित्वांशिवाय शुद्ध REST API कॉल्स
- सानुकूल प्रमाणीकरण आणि हेडर्स
- विनंती/प्रतिसाद हाताळणीवर पूर्ण नियंत्रण

### 2. **मॉडेल व्यवस्थापन**
- डायनॅमिक मॉडेल लोडिंग आणि अनलोडिंग
- आरोग्य निरीक्षण आणि स्थिती तपासणी
- कार्यक्षमता मेट्रिक्स संग्रह

### 3. **उत्पादन नमुने**
- घसरत्या बॅकऑफसह पुन्हा प्रयत्न यंत्रणा
- दोष सहनशीलतेसाठी सर्किट ब्रेकर
- सर्वसमावेशक लॉगिंग आणि निरीक्षण

### 4. **लवचिक प्रतिसाद हाताळणी**
- रिअल-टाइम अनुप्रयोगांसाठी स्ट्रीमिंग प्रतिसाद
- उच्च-थ्रूपुट परिस्थितीसाठी बॅच प्रक्रिया
- सानुकूल प्रतिसाद पार्सिंग आणि पडताळणी

## वापर उदाहरणे

### मूलभूत API एकत्रीकरण
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

### स्ट्रीमिंग एकत्रीकरण
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### आरोग्य निरीक्षण
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## फाइल संरचना

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

## Microsoft Foundry Local एकत्रीकरण

हा नमुना Microsoft च्या अधिकृत नमुन्यांचे अनुसरण करतो:

1. **SDK एकत्रीकरण**: सेवा व्यवस्थापनासाठी `FoundryLocalManager` वापरतो
2. **REST एंडपॉइंट्स**: `/v1/chat/completions` आणि इतर एंडपॉइंट्ससाठी थेट कॉल्स
3. **प्रमाणीकरण**: स्थानिक सेवांसाठी योग्य API की हाताळणी
4. **मॉडेल व्यवस्थापन**: कॅटलॉग लिस्टिंग, डाउनलोडिंग आणि लोडिंग नमुने
5. **त्रुटी हाताळणी**: Microsoft-शिफारस केलेले त्रुटी कोड्स आणि प्रतिसाद

## सुरुवात कशी करावी

1. **Dependencies इंस्टॉल करा**
   ```bash
   pip install -r requirements.txt
   ```

2. **मूलभूत उदाहरण चालवा**
   ```bash
   python examples/basic_usage.py
   ```

3. **स्ट्रीमिंग प्रयत्न करा**
   ```bash
   python examples/streaming.py
   ```

4. **उत्पादन सेटअप**
   ```bash
   python examples/production.py
   ```

## कॉन्फिगरेशन

सानुकूलनासाठी पर्यावरणीय चल:
- `FOUNDRY_MODEL`: वापरण्यासाठी डीफॉल्ट मॉडेल (डीफॉल्ट: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: सेकंदांमध्ये विनंती टाइमआउट (डीफॉल्ट: 30)
- `FOUNDRY_RETRIES`: पुन्हा प्रयत्नांची संख्या (डीफॉल्ट: 3)
- `FOUNDRY_LOG_LEVEL`: लॉगिंग स्तर (डीफॉल्ट: "INFO")

## सर्वोत्तम पद्धती

1. **कनेक्शन व्यवस्थापन**: चांगल्या कार्यक्षमतेसाठी HTTP कनेक्शन पुन्हा वापरा
2. **त्रुटी हाताळणी**: घसरत्या बॅकऑफसह योग्य पुन्हा प्रयत्न तर्कशास्त्र अंमलात आणा
3. **संसाधन निरीक्षण**: मॉडेल मेमरी वापर आणि कार्यक्षमता ट्रॅक करा
4. **सुरक्षा**: स्थानिक सेवांसाठी योग्य प्रमाणीकरण वापरा
5. **चाचणी**: युनिट आणि एकत्रीकरण चाचण्या समाविष्ट करा

## समस्या निवारण

### सामान्य समस्या

**सेवा चालू नाही**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**मॉडेल लोडिंग समस्या**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**कनेक्शन त्रुटी**
- Foundry Local योग्य पोर्टवर चालू आहे का ते सत्यापित करा
- फायरवॉल सेटिंग्ज तपासा
- योग्य प्रमाणीकरण हेडर्स सुनिश्चित करा

## कार्यक्षमता ऑप्टिमायझेशन

1. **कनेक्शन पूलिंग**: एकाधिक विनंत्यांसाठी सत्र ऑब्जेक्ट्स वापरा
2. **असिंक्रोनस ऑपरेशन्स**: समांतर विनंत्यांसाठी asyncio चा लाभ घ्या
3. **कॅशिंग**: योग्य ठिकाणी मॉडेल प्रतिसाद कॅश करा
4. **निरीक्षण**: प्रतिसाद वेळा ट्रॅक करा आणि टाइमआउट समायोजित करा

## शिकण्याचे परिणाम

हा नमुना पूर्ण केल्यानंतर, तुम्हाला समजेल:
- Foundry Local सह थेट REST API एकत्रीकरण
- सानुकूल HTTP क्लायंट अंमलबजावणी नमुने
- उत्पादनासाठी तयार त्रुटी हाताळणी आणि निरीक्षण
- Microsoft Foundry Local सेवा आर्किटेक्चर
- स्थानिक AI सेवांसाठी कार्यक्षमता ऑप्टिमायझेशन तंत्र

## पुढील पावले

- नमुना 08: Windows 11 चॅट अनुप्रयोग एक्सप्लोर करा
- नमुना 09: मल्टी-एजंट ऑर्केस्ट्रेशन प्रयत्न करा
- नमुना 10: Foundry Local as Tools Integration शिकणे

---

