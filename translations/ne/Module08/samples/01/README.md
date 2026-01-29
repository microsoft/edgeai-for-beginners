# नमूना ०१: OpenAI SDK मार्फत छिटो कुराकानी

Microsoft Foundry Local को साथमा स्थानीय AI इनफरेन्सको लागि OpenAI SDK प्रयोग गर्ने तरिका देखाउने एउटा साधारण कुराकानी उदाहरण।

## अवलोकन

यस नमूनाले देखाउँछ:
- Foundry Local को साथमा OpenAI Python SDK प्रयोग गर्ने तरिका
- Azure OpenAI र स्थानीय Foundry कन्फिगरेसनहरूलाई कसरी व्यवस्थापन गर्ने
- उचित त्रुटि व्यवस्थापन र फलब्याक रणनीतिहरू कार्यान्वयन गर्ने तरिका
- सेवा व्यवस्थापनको लागि FoundryLocalManager प्रयोग गर्ने तरिका

## आवश्यकताहरू

- **Foundry Local**: स्थापना गरिएको र PATH मा उपलब्ध
- **Python**: 3.8 वा पछिल्लो संस्करण
- **मोडेल**: Foundry Local मा लोड गरिएको मोडेल (जस्तै, `phi-4-mini`)

## स्थापना

1. **Python वातावरण सेटअप गर्नुहोस्:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **आवश्यकता स्थापना गर्नुहोस्:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local सेवा सुरु गर्नुहोस् र मोडेल लोड गर्नुहोस्:**
   ```cmd
   foundry model run phi-4-mini
   ```


## प्रयोग

### Foundry Local (डिफल्ट)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## कोड विशेषताहरू

### FoundryLocalManager एकीकरण

नमूनाले उचित सेवा व्यवस्थापनको लागि आधिकारिक Foundry Local SDK प्रयोग गर्दछ:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### त्रुटि व्यवस्थापन

म्यानुअल कन्फिगरेसनमा फलब्याकको साथमा मजबुत त्रुटि व्यवस्थापन:
- स्वचालित सेवा खोज
- SDK अनुपलब्ध हुँदा सहज डिग्रेडेसन
- समस्या समाधानको लागि स्पष्ट त्रुटि सन्देशहरू

## वातावरण चरहरू

| चर | विवरण | डिफल्ट | आवश्यक |
|-----|--------|---------|---------|
| `MODEL` | मोडेल उपनाम वा नाम | `phi-4-mini` | होइन |
| `BASE_URL` | Foundry Local आधार URL | `http://localhost:8000` | होइन |
| `API_KEY` | API कुञ्जी (सामान्यतया स्थानीयको लागि आवश्यक छैन) | `""` | होइन |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI अन्त बिन्दु | - | Azure को लागि |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API कुञ्जी | - | Azure को लागि |
| `AZURE_OPENAI_API_VERSION` | Azure API संस्करण | `2024-08-01-preview` | होइन |

## समस्या समाधान

### सामान्य समस्याहरू

1. **"Foundry SDK प्रयोग गर्न सकिएन" चेतावनी:**
   - Foundry Local SDK स्थापना गर्नुहोस्: `pip install foundry-local-sdk`
   - वा म्यानुअल कन्फिगरेसनको लागि वातावरण चरहरू सेट गर्नुहोस्

2. **जडान अस्वीकृत:**
   - सुनिश्चित गर्नुहोस् Foundry Local चलिरहेको छ: `foundry service status`
   - मोडेल लोड गरिएको छ कि छैन जाँच गर्नुहोस्: `foundry service ps`

3. **मोडेल फेला परेन:**
   - उपलब्ध मोडेलहरूको सूची बनाउनुहोस्: `foundry model list`
   - मोडेल लोड गर्नुहोस्: `foundry model run phi-4-mini`

### प्रमाणिकरण

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## सन्दर्भहरू

- [Foundry Local दस्तावेज](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-संगत API सन्दर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

