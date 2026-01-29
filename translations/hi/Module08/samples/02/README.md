# नमूना 02: OpenAI SDK इंटीग्रेशन

OpenAI Python SDK के साथ उन्नत इंटीग्रेशन को प्रदर्शित करता है, जो Microsoft Foundry Local और Azure OpenAI दोनों का समर्थन करता है, साथ ही स्ट्रीमिंग प्रतिक्रियाओं और उचित त्रुटि प्रबंधन के साथ।

## अवलोकन

यह नमूना निम्नलिखित को प्रदर्शित करता है:
- Foundry Local और Azure OpenAI के बीच सहज स्विचिंग
- बेहतर उपयोगकर्ता अनुभव के लिए स्ट्रीमिंग चैट प्रतिक्रियाएं
- FoundryLocalManager SDK का सही उपयोग
- मजबूत त्रुटि प्रबंधन और बैकअप तंत्र
- उत्पादन-तैयार कोड पैटर्न

## आवश्यकताएँ

- **Foundry Local**: इंस्टॉल और चालू (स्थानीय अनुमान के लिए)
- **Python**: 3.8 या बाद का संस्करण OpenAI SDK के साथ
- **Azure OpenAI**: मान्य एंडपॉइंट और API कुंजी (क्लाउड अनुमान के लिए)

## इंस्टॉलेशन

1. **Python वातावरण सेट करें:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **डिपेंडेंसी इंस्टॉल करें:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local शुरू करें (स्थानीय मोड के लिए):**
   ```cmd
   foundry model run phi-4-mini
   ```


## उपयोग परिदृश्य

### Foundry Local (डिफ़ॉल्ट)

**विकल्प 1: FoundryLocalManager का उपयोग करना (अनुशंसित)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**विकल्प 2: मैनुअल कॉन्फ़िगरेशन**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## कोड आर्किटेक्चर

### क्लाइंट फैक्टरी पैटर्न

नमूना उपयुक्त क्लाइंट बनाने के लिए फैक्टरी पैटर्न का उपयोग करता है:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### स्ट्रीमिंग प्रतिक्रियाएं

नमूना वास्तविक समय प्रतिक्रिया उत्पन्न करने के लिए स्ट्रीमिंग को प्रदर्शित करता है:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## पर्यावरण चर

### Foundry Local कॉन्फ़िगरेशन

| चर | विवरण | डिफ़ॉल्ट | आवश्यक |
|-----|--------|---------|---------|
| `MODEL` | उपयोग करने के लिए मॉडल उपनाम | `phi-4-mini` | नहीं |
| `BASE_URL` | Foundry Local एंडपॉइंट | `http://localhost:8000` | नहीं |
| `API_KEY` | API कुंजी (स्थानीय के लिए वैकल्पिक) | `""` | नहीं |

### Azure OpenAI कॉन्फ़िगरेशन

| चर | विवरण | डिफ़ॉल्ट | आवश्यक |
|-----|--------|---------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI संसाधन एंडपॉइंट | - | हाँ |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API कुंजी | - | हाँ |
| `AZURE_OPENAI_API_VERSION` | API संस्करण | `2024-08-01-preview` | नहीं |
| `MODEL` | Azure डिप्लॉयमेंट नाम | `your-deployment-name` | हाँ |

## उन्नत सुविधाएँ

### स्वचालित सेवा खोज

नमूना पर्यावरण चर के आधार पर उपयुक्त सेवा का स्वतः पता लगाता है:

1. **Azure मोड**: यदि `AZURE_OPENAI_ENDPOINT` और `AZURE_OPENAI_API_KEY` सेट हैं
2. **Foundry SDK मोड**: यदि Foundry Local SDK उपलब्ध है
3. **मैनुअल मोड**: मैनुअल कॉन्फ़िगरेशन पर बैकअप

### त्रुटि प्रबंधन

- SDK से मैनुअल कॉन्फ़िगरेशन पर सहज बैकअप
- समस्या निवारण के लिए स्पष्ट त्रुटि संदेश
- नेटवर्क समस्याओं के लिए उचित अपवाद प्रबंधन
- आवश्यक पर्यावरण चर का सत्यापन

## प्रदर्शन विचार

### स्थानीय बनाम क्लाउड ट्रेड-ऑफ

**Foundry Local के लाभ:**
- ✅ कोई API लागत नहीं
- ✅ डेटा गोपनीयता (कोई डेटा डिवाइस से बाहर नहीं जाता)
- ✅ समर्थित मॉडलों के लिए कम विलंबता
- ✅ ऑफलाइन काम करता है

**Azure OpenAI के लाभ:**
- ✅ नवीनतम बड़े मॉडलों तक पहुंच
- ✅ उच्च थ्रूपुट
- ✅ कोई स्थानीय कंप्यूट आवश्यकताएँ नहीं
- ✅ एंटरप्राइज़-ग्रेड SLA

## समस्या निवारण

### सामान्य समस्याएँ

1. **"Foundry SDK का उपयोग नहीं कर सके" चेतावनी:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure प्रमाणीकरण त्रुटियाँ:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **मॉडल उपलब्ध नहीं है:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### स्वास्थ्य जांच

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## अगले चरण

- **नमूना 03**: मॉडल खोज और बेंचमार्किंग
- **नमूना 04**: एक Chainlit RAG एप्लिकेशन बनाना
- **नमूना 05**: मल्टी-एजेंट ऑर्केस्ट्रेशन
- **नमूना 06**: टूल्स के रूप में मॉडल रूटिंग

## संदर्भ

- [Azure OpenAI दस्तावेज़](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK संदर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK दस्तावेज़](https://github.com/openai/openai-python)
- [स्ट्रीमिंग प्रतिक्रियाओं गाइड](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

