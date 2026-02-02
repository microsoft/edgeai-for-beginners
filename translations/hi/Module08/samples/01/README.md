# नमूना 01: OpenAI SDK के माध्यम से त्वरित चैट

Microsoft Foundry Local के साथ स्थानीय AI अनुमान के लिए OpenAI SDK का उपयोग करने का एक सरल चैट उदाहरण।

## अवलोकन

यह नमूना दिखाता है कि कैसे:
- Foundry Local के साथ OpenAI Python SDK का उपयोग करें
- Azure OpenAI और स्थानीय Foundry कॉन्फ़िगरेशन को संभालें
- उचित त्रुटि प्रबंधन और फॉलबैक रणनीतियों को लागू करें
- सेवा प्रबंधन के लिए FoundryLocalManager का उपयोग करें

## आवश्यकताएँ

- **Foundry Local**: इंस्टॉल किया हुआ और PATH पर उपलब्ध
- **Python**: 3.8 या उससे नया संस्करण
- **मॉडल**: Foundry Local में लोड किया गया एक मॉडल (जैसे, `phi-4-mini`)

## इंस्टॉलेशन

1. **Python वातावरण सेट करें:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **आवश्यकताएँ इंस्टॉल करें:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local सेवा शुरू करें और एक मॉडल लोड करें:**
   ```cmd
   foundry model run phi-4-mini
   ```


## उपयोग

### Foundry Local (डिफ़ॉल्ट)

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


## कोड विशेषताएँ

### FoundryLocalManager एकीकरण

यह नमूना सेवा प्रबंधन के लिए आधिकारिक Foundry Local SDK का उपयोग करता है:

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


### त्रुटि प्रबंधन

मजबूत त्रुटि प्रबंधन के साथ मैनुअल कॉन्फ़िगरेशन पर फॉलबैक:
- स्वचालित सेवा खोज
- SDK अनुपलब्ध होने पर ग्रेसफुल डिग्रेडेशन
- समस्या निवारण के लिए स्पष्ट त्रुटि संदेश

## पर्यावरणीय वेरिएबल्स

| वेरिएबल | विवरण | डिफ़ॉल्ट | आवश्यक |
|----------|-------------|---------|----------|
| `MODEL` | मॉडल उपनाम या नाम | `phi-4-mini` | नहीं |
| `BASE_URL` | Foundry Local बेस URL | `http://localhost:8000` | नहीं |
| `API_KEY` | API कुंजी (आमतौर पर स्थानीय के लिए आवश्यक नहीं) | `""` | नहीं |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI एंडपॉइंट | - | Azure के लिए |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API कुंजी | - | Azure के लिए |
| `AZURE_OPENAI_API_VERSION` | Azure API संस्करण | `2024-08-01-preview` | नहीं |

## समस्या निवारण

### सामान्य समस्याएँ

1. **"Foundry SDK का उपयोग नहीं कर सके" चेतावनी:**
   - Foundry Local SDK इंस्टॉल करें: `pip install foundry-local-sdk`
   - या मैनुअल कॉन्फ़िगरेशन के लिए पर्यावरणीय वेरिएबल्स सेट करें

2. **कनेक्शन अस्वीकृत:**
   - सुनिश्चित करें कि Foundry Local चल रहा है: `foundry service status`
   - जांचें कि कोई मॉडल लोड किया गया है: `foundry service ps`

3. **मॉडल नहीं मिला:**
   - उपलब्ध मॉडलों की सूची देखें: `foundry model list`
   - एक मॉडल लोड करें: `foundry model run phi-4-mini`

### सत्यापन

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## संदर्भ

- [Foundry Local दस्तावेज़](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-संगत API संदर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

