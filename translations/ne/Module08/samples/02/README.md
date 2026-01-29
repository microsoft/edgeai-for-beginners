# नमूना ०२: OpenAI SDK एकीकरण

OpenAI Python SDK सँग उन्नत एकीकरण प्रदर्शन गर्दछ, जसले Microsoft Foundry Local र Azure OpenAI दुवैलाई समर्थन गर्दछ, स्ट्रिमिङ प्रतिक्रियाहरू र उचित त्रुटि व्यवस्थापन सहित।

## अवलोकन

यो नमूनाले निम्न कुराहरू प्रदर्शन गर्दछ:
- Foundry Local र Azure OpenAI बीच सहज स्विचिङ
- प्रयोगकर्ताको अनुभव सुधार गर्न स्ट्रिमिङ च्याट कम्प्लिशनहरू
- FoundryLocalManager SDK को उचित प्रयोग
- बलियो त्रुटि व्यवस्थापन र फलब्याक मेकानिजमहरू
- उत्पादन-तयार कोड ढाँचाहरू

## पूर्वापेक्षाहरू

- **Foundry Local**: स्थापना गरिएको र चलिरहेको (स्थानीय इनफरेन्सका लागि)
- **Python**: 3.8 वा पछिल्लो संस्करण OpenAI SDK सहित
- **Azure OpenAI**: मान्य अन्त बिन्दु र API कुञ्जी (क्लाउड इनफरेन्सका लागि)

## स्थापना

1. **Python वातावरण सेटअप गर्नुहोस्:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **आवश्यकताहरू स्थापना गर्नुहोस्:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local सुरु गर्नुहोस् (स्थानीय मोडका लागि):**
   ```cmd
   foundry model run phi-4-mini
   ```


## प्रयोग परिदृश्यहरू

### Foundry Local (डिफल्ट)

**विकल्प १: FoundryLocalManager प्रयोग गर्दै (सिफारिस गरिएको)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**विकल्प २: म्यानुअल कन्फिगरेसन**
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

### क्लाइन्ट फ्याक्टरी ढाँचा

नमूनाले उपयुक्त क्लाइन्टहरू सिर्जना गर्न फ्याक्टरी ढाँचाको प्रयोग गर्दछ:

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


### स्ट्रिमिङ प्रतिक्रियाहरू

नमूनाले वास्तविक-समय प्रतिक्रिया उत्पादनका लागि स्ट्रिमिङ प्रदर्शन गर्दछ:

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


## वातावरण चरहरू

### Foundry Local कन्फिगरेसन

| चर | विवरण | डिफल्ट | आवश्यक |
|-----|--------|---------|---------|
| `MODEL` | प्रयोग गर्न मोडेल उपनाम | `phi-4-mini` | होइन |
| `BASE_URL` | Foundry Local अन्त बिन्दु | `http://localhost:8000` | होइन |
| `API_KEY` | API कुञ्जी (स्थानीयका लागि वैकल्पिक) | `""` | होइन |

### Azure OpenAI कन्फिगरेसन

| चर | विवरण | डिफल्ट | आवश्यक |
|-----|--------|---------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI स्रोत अन्त बिन्दु | - | हो |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API कुञ्जी | - | हो |
| `AZURE_OPENAI_API_VERSION` | API संस्करण | `2024-08-01-preview` | होइन |
| `MODEL` | Azure डिप्लोयमेन्ट नाम | `your-deployment-name` | हो |

## उन्नत सुविधाहरू

### स्वचालित सेवा पत्ता लगाउने

नमूनाले वातावरण चरहरूको आधारमा उपयुक्त सेवा स्वचालित रूपमा पत्ता लगाउँछ:

1. **Azure मोड**: यदि `AZURE_OPENAI_ENDPOINT` र `AZURE_OPENAI_API_KEY` सेट गरिएको छ
2. **Foundry SDK मोड**: यदि Foundry Local SDK उपलब्ध छ
3. **म्यानुअल मोड**: म्यानुअल कन्फिगरेसनमा फलब्याक

### त्रुटि व्यवस्थापन

- SDK बाट म्यानुअल कन्फिगरेसनमा सहज फलब्याक
- समस्या समाधानका लागि स्पष्ट त्रुटि सन्देशहरू
- नेटवर्क समस्याहरूका लागि उचित अपवाद व्यवस्थापन
- आवश्यक वातावरण चरहरूको मान्यता

## प्रदर्शन विचारहरू

### स्थानीय बनाम क्लाउड व्यापार-सम्झौता

**Foundry Local फाइदाहरू:**
- ✅ कुनै API लागत छैन
- ✅ डाटा गोपनीयता (डाटा उपकरण बाहिर जान्दैन)
- ✅ समर्थित मोडेलहरूको लागि कम विलम्बता
- ✅ अफलाइन काम गर्दछ

**Azure OpenAI फाइदाहरू:**
- ✅ पछिल्लो ठूला मोडेलहरूमा पहुँच
- ✅ उच्च थ्रुपुट
- ✅ स्थानीय कम्प्युट आवश्यकताहरू छैन
- ✅ उद्यम-ग्रेड SLA

## समस्या समाधान

### सामान्य समस्याहरू

1. **"Foundry SDK प्रयोग गर्न सकिएन" चेतावनी:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure प्रमाणीकरण त्रुटिहरू:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **मोडेल उपलब्ध छैन:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### स्वास्थ्य जाँचहरू

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## आगामी कदमहरू

- **नमूना ०३**: मोडेल पत्ता लगाउने र बेंचमार्किङ
- **नमूना ०४**: Chainlit RAG एप्लिकेसन निर्माण
- **नमूना ०५**: बहु-एजेन्ट समन्वय
- **नमूना ०६**: उपकरणको रूपमा मोडेल रुटिङ

## सन्दर्भहरू

- [Azure OpenAI दस्तावेज](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK सन्दर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK दस्तावेज](https://github.com/openai/openai-python)
- [स्ट्रिमिङ कम्प्लिशन गाइड](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

