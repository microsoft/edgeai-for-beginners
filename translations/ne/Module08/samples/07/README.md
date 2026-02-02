# Foundry Local as API Sample

यो नमूनाले Microsoft Foundry Local लाई REST API सेवा रूपमा OpenAI SDK मा निर्भर नगरी प्रयोग गर्ने तरिका देखाउँछ। यसले अधिकतम नियन्त्रण र अनुकूलनको लागि प्रत्यक्ष HTTP एकीकरण ढाँचाहरू प्रस्तुत गर्दछ।

## अवलोकन

Microsoft को आधिकारिक Foundry Local ढाँचाहरूमा आधारित, यो नमूनाले प्रदान गर्दछ:
- FoundryLocalManager सँग प्रत्यक्ष REST API एकीकरण
- अनुकूलित HTTP क्लाइन्ट कार्यान्वयन
- मोडेल व्यवस्थापन र स्वास्थ्य निगरानी
- स्ट्रिमिङ र गैर-स्ट्रिमिङ प्रतिक्रिया ह्यान्डलिङ
- उत्पादन-तयार त्रुटि ह्यान्डलिङ र पुन: प्रयास गर्ने तर्क

## आवश्यकताहरू

1. **Foundry Local स्थापना**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Dependencies**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## वास्तुकला

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## मुख्य विशेषताहरू

### 1. **प्रत्यक्ष HTTP एकीकरण**
- SDK निर्भरता बिना शुद्ध REST API कलहरू
- अनुकूलित प्रमाणीकरण र हेडरहरू
- अनुरोध/प्रतिक्रिया ह्यान्डलिङमा पूर्ण नियन्त्रण

### 2. **मोडेल व्यवस्थापन**
- गतिशील मोडेल लोडिङ र अनलोडिङ
- स्वास्थ्य निगरानी र स्थिति जाँच
- प्रदर्शन मेट्रिक्स सङ्कलन

### 3. **उत्पादन ढाँचाहरू**
- एक्सपोनेंशियल ब्याकअफको साथ पुन: प्रयास गर्ने संयन्त्र
- दोष सहिष्णुता लागि सर्किट ब्रेकर
- व्यापक लगिङ र निगरानी

### 4. **लचिलो प्रतिक्रिया ह्यान्डलिङ**
- वास्तविक-समय अनुप्रयोगहरूको लागि स्ट्रिमिङ प्रतिक्रियाहरू
- उच्च-थ्रुपुट परिदृश्यहरूको लागि ब्याच प्रशोधन
- अनुकूलित प्रतिक्रिया पार्सिङ र मान्यता

## प्रयोगका उदाहरणहरू

### आधारभूत API एकीकरण
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

### स्ट्रिमिङ एकीकरण
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

## Microsoft Foundry Local एकीकरण

यो नमूनाले Microsoft को आधिकारिक ढाँचाहरू अनुसरण गर्दछ:

1. **SDK एकीकरण**: सेवा व्यवस्थापनको लागि `FoundryLocalManager` प्रयोग गर्दछ
2. **REST अन्त बिन्दुहरू**: `/v1/chat/completions` र अन्य अन्त बिन्दुहरूमा प्रत्यक्ष कलहरू
3. **प्रमाणीकरण**: स्थानीय सेवाहरूको लागि उचित API कुञ्जी ह्यान्डलिङ
4. **मोडेल व्यवस्थापन**: सूचीकरण, डाउनलोडिङ, र लोडिङ ढाँचाहरू
5. **त्रुटि ह्यान्डलिङ**: Microsoft द्वारा सिफारिस गरिएका त्रुटि कोडहरू र प्रतिक्रियाहरू

## सुरु गर्ने तरिका

1. **Dependencies स्थापना गर्नुहोस्**
   ```bash
   pip install -r requirements.txt
   ```

2. **आधारभूत उदाहरण चलाउनुहोस्**
   ```bash
   python examples/basic_usage.py
   ```

3. **स्ट्रिमिङ प्रयास गर्नुहोस्**
   ```bash
   python examples/streaming.py
   ```

4. **उत्पादन सेटअप**
   ```bash
   python examples/production.py
   ```

## कन्फिगरेसन

अनुकूलनको लागि वातावरण चरहरू:
- `FOUNDRY_MODEL`: प्रयोग गर्नुपर्ने डिफल्ट मोडेल (डिफल्ट: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: अनुरोध टाइमआउट सेकेन्डमा (डिफल्ट: 30)
- `FOUNDRY_RETRIES`: पुन: प्रयास गर्ने संख्या (डिफल्ट: 3)
- `FOUNDRY_LOG_LEVEL`: लगिङ स्तर (डिफल्ट: "INFO")

## उत्कृष्ट अभ्यासहरू

1. **कनेक्शन व्यवस्थापन**: राम्रो प्रदर्शनको लागि HTTP कनेक्शनहरू पुन: प्रयोग गर्नुहोस्
2. **त्रुटि ह्यान्डलिङ**: एक्सपोनेंशियल ब्याकअफको साथ उचित पुन: प्रयास तर्क कार्यान्वयन गर्नुहोस्
3. **स्रोत निगरानी**: मोडेल मेमोरी प्रयोग र प्रदर्शन ट्र्याक गर्नुहोस्
4. **सुरक्षा**: स्थानीय सेवाहरूको लागि पनि उचित प्रमाणीकरण प्रयोग गर्नुहोस्
5. **परीक्षण**: युनिट र एकीकरण परीक्षणहरू समावेश गर्नुहोस्

## समस्या समाधान

### सामान्य समस्याहरू

**सेवा चलिरहेको छैन**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**मोडेल लोडिङ समस्याहरू**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**कनेक्शन त्रुटिहरू**
- सुनिश्चित गर्नुहोस् Foundry Local सही पोर्टमा चलिरहेको छ
- फायरवाल सेटिङहरू जाँच गर्नुहोस्
- उचित प्रमाणीकरण हेडरहरू सुनिश्चित गर्नुहोस्

## प्रदर्शन अनुकूलन

1. **कनेक्शन पूलिङ**: धेरै अनुरोधहरूको लागि सेसन वस्तुहरू प्रयोग गर्नुहोस्
2. **एसिंक्रोनस अपरेसनहरू**: समवर्ती अनुरोधहरूको लागि asyncio प्रयोग गर्नुहोस्
3. **क्यासिङ**: उपयुक्त ठाउँमा मोडेल प्रतिक्रियाहरू क्यास गर्नुहोस्
4. **निगरानी**: प्रतिक्रिया समय ट्र्याक गर्नुहोस् र टाइमआउट समायोजन गर्नुहोस्

## सिकाइ परिणामहरू

यो नमूना पूरा गरेपछि, तपाईं बुझ्नुहुनेछ:
- Foundry Local सँग प्रत्यक्ष REST API एकीकरण
- अनुकूलित HTTP क्लाइन्ट कार्यान्वयन ढाँचाहरू
- उत्पादन-तयार त्रुटि ह्यान्डलिङ र निगरानी
- Microsoft Foundry Local सेवा वास्तुकला
- स्थानीय AI सेवाहरूको लागि प्रदर्शन अनुकूलन प्रविधिहरू

## अर्को कदमहरू

- नमूना 08 अन्वेषण गर्नुहोस्: Windows 11 च्याट अनुप्रयोग
- नमूना 09 प्रयास गर्नुहोस्: बहु-एजेन्ट समन्वय
- नमूना 10 सिक्नुहोस्: Foundry Local लाई उपकरण एकीकरणको रूपमा प्रयोग गर्नुहोस्

---

