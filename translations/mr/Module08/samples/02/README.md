# नमुना 02: OpenAI SDK एकत्रीकरण

OpenAI Python SDK सह प्रगत एकत्रीकरण दाखवते, ज्यामध्ये Microsoft Foundry Local आणि Azure OpenAI दोन्हींसाठी स्ट्रीमिंग प्रतिसाद आणि योग्य त्रुटी हाताळणीचा समावेश आहे.

## आढावा

या नमुन्यात खालील गोष्टी दाखवल्या आहेत:
- Foundry Local आणि Azure OpenAI दरम्यान सहज स्विचिंग
- वापरकर्ता अनुभव सुधारण्यासाठी स्ट्रीमिंग चॅट पूर्णता
- FoundryLocalManager SDK चा योग्य वापर
- मजबूत त्रुटी हाताळणी आणि फॉलबॅक यंत्रणा
- उत्पादनासाठी तयार कोड नमुने

## पूर्वअट

- **Foundry Local**: स्थापित आणि चालू (स्थानिक अनुमानासाठी)
- **Python**: 3.8 किंवा त्याहून पुढील आवृत्ती OpenAI SDK सह
- **Azure OpenAI**: वैध एंडपॉइंट आणि API की (क्लाउड अनुमानासाठी)

## स्थापना

1. **Python वातावरण सेट करा:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **आवश्यकता स्थापित करा:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local सुरू करा (स्थानिक मोडसाठी):**
   ```cmd
   foundry model run phi-4-mini
   ```


## वापर परिस्थिती

### Foundry Local (डीफॉल्ट)

**पर्याय 1: FoundryLocalManager वापरणे (शिफारस केलेले)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**पर्याय 2: मॅन्युअल कॉन्फिगरेशन**
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

### क्लायंट फॅक्टरी पॅटर्न

नमुन्यात योग्य क्लायंट तयार करण्यासाठी फॅक्टरी पॅटर्न वापरला जातो:

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


### स्ट्रीमिंग प्रतिसाद

नमुन्यात रिअल-टाइम प्रतिसाद निर्मितीसाठी स्ट्रीमिंग दाखवले आहे:

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


## पर्यावरणीय व्हेरिएबल्स

### Foundry Local कॉन्फिगरेशन

| व्हेरिएबल | वर्णन | डीफॉल्ट | आवश्यक |
|-----------|--------|---------|---------|
| `MODEL` | वापरण्यासाठी मॉडेल उपनाम | `phi-4-mini` | नाही |
| `BASE_URL` | Foundry Local एंडपॉइंट | `http://localhost:8000` | नाही |
| `API_KEY` | API की (स्थानिकसाठी पर्यायी) | `""` | नाही |

### Azure OpenAI कॉन्फिगरेशन

| व्हेरिएबल | वर्णन | डीफॉल्ट | आवश्यक |
|-----------|--------|---------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI संसाधन एंडपॉइंट | - | होय |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API की | - | होय |
| `AZURE_OPENAI_API_VERSION` | API आवृत्ती | `2024-08-01-preview` | नाही |
| `MODEL` | Azure डिप्लॉयमेंट नाव | `your-deployment-name` | होय |

## प्रगत वैशिष्ट्ये

### स्वयंचलित सेवा शोध

नमुन्यात पर्यावरणीय व्हेरिएबल्सच्या आधारे योग्य सेवा स्वयंचलितपणे शोधली जाते:

1. **Azure मोड**: जर `AZURE_OPENAI_ENDPOINT` आणि `AZURE_OPENAI_API_KEY` सेट केले असतील
2. **Foundry SDK मोड**: जर Foundry Local SDK उपलब्ध असेल
3. **मॅन्युअल मोड**: मॅन्युअल कॉन्फिगरेशनवर फॉलबॅक

### त्रुटी हाताळणी

- SDK पासून मॅन्युअल कॉन्फिगरेशनवर सौम्य फॉलबॅक
- समस्या सोडवण्यासाठी स्पष्ट त्रुटी संदेश
- नेटवर्क समस्यांसाठी योग्य अपवाद हाताळणी
- आवश्यक पर्यावरणीय व्हेरिएबल्सची पडताळणी

## कार्यक्षमता विचार

### स्थानिक विरुद्ध क्लाउड व्यापार-offs

**Foundry Local फायदे:**
- ✅ API खर्च नाही
- ✅ डेटा गोपनीयता (डेटा डिव्हाइस सोडत नाही)
- ✅ समर्थित मॉडेलसाठी कमी विलंबता
- ✅ ऑफलाइन कार्य करते

**Azure OpenAI फायदे:**
- ✅ नवीनतम मोठ्या मॉडेल्सचा प्रवेश
- ✅ उच्च थ्रूपुट
- ✅ स्थानिक संगणन आवश्यकता नाही
- ✅ एंटरप्राइझ-ग्रेड SLA

## समस्या सोडवणे

### सामान्य समस्या

1. **"Foundry SDK वापरू शकत नाही" चेतावणी:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure प्रमाणीकरण त्रुटी:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **मॉडेल उपलब्ध नाही:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### आरोग्य तपासणी

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## पुढील पायऱ्या

- **नमुना 03**: मॉडेल शोध आणि बेंचमार्किंग
- **नमुना 04**: Chainlit RAG अनुप्रयोग तयार करणे
- **नमुना 05**: मल्टी-एजंट ऑर्केस्ट्रेशन
- **नमुना 06**: मॉडेल्स-आस-टूल्स रूटिंग

## संदर्भ

- [Azure OpenAI दस्तऐवज](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK संदर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK दस्तऐवज](https://github.com/openai/openai-python)
- [स्ट्रीमिंग पूर्णता मार्गदर्शक](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

