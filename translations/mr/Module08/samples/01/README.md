# नमुना 01: OpenAI SDK वापरून जलद चॅट

Microsoft Foundry Local च्या मदतीने स्थानिक AI अनुमानासाठी OpenAI SDK कसे वापरायचे याचे साधे उदाहरण.

## आढावा

या नमुन्यात तुम्हाला खालील गोष्टी शिकायला मिळतील:
- Foundry Local सह OpenAI Python SDK वापरणे
- Azure OpenAI आणि स्थानिक Foundry कॉन्फिगरेशन हाताळणे
- योग्य एरर हँडलिंग आणि फॉलबॅक रणनीती अंमलात आणणे
- सेवा व्यवस्थापनासाठी FoundryLocalManager वापरणे

## पूर्वतयारी

- **Foundry Local**: स्थापित आणि PATH वर उपलब्ध
- **Python**: 3.8 किंवा त्याहून पुढील आवृत्ती
- **मॉडेल**: Foundry Local मध्ये लोड केलेले मॉडेल (उदा. `phi-4-mini`)

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

3. **Foundry Local सेवा सुरू करा आणि मॉडेल लोड करा:**
   ```cmd
   foundry model run phi-4-mini
   ```


## वापर

### Foundry Local (डिफॉल्ट)

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


## कोड वैशिष्ट्ये

### FoundryLocalManager एकत्रीकरण

नमुन्यात सेवा व्यवस्थापनासाठी अधिकृत Foundry Local SDK वापरले आहे:

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


### एरर हँडलिंग

मजबूत एरर हँडलिंग, ज्यामध्ये मॅन्युअल कॉन्फिगरेशनसाठी फॉलबॅक समाविष्ट आहे:
- स्वयंचलित सेवा शोध
- SDK अनुपलब्ध असल्यास सौम्य अपयश
- समस्या सोडवण्यासाठी स्पष्ट एरर संदेश

## पर्यावरणीय व्हेरिएबल्स

| व्हेरिएबल | वर्णन | डिफॉल्ट | आवश्यक |
|----------|-------------|---------|----------|
| `MODEL` | मॉडेल उपनाम किंवा नाव | `phi-4-mini` | नाही |
| `BASE_URL` | Foundry Local बेस URL | `http://localhost:8000` | नाही |
| `API_KEY` | API की (सामान्यतः स्थानिकासाठी आवश्यक नाही) | `""` | नाही |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI एंडपॉइंट | - | Azure साठी |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API की | - | Azure साठी |
| `AZURE_OPENAI_API_VERSION` | Azure API आवृत्ती | `2024-08-01-preview` | नाही |

## समस्या सोडवणे

### सामान्य समस्या

1. **"Foundry SDK वापरता आले नाही" चेतावणी:**
   - Foundry Local SDK स्थापित करा: `pip install foundry-local-sdk`
   - किंवा मॅन्युअल कॉन्फिगरेशनसाठी पर्यावरणीय व्हेरिएबल्स सेट करा

2. **कनेक्शन नाकारले:**
   - Foundry Local चालू आहे याची खात्री करा: `foundry service status`
   - मॉडेल लोड केले आहे का ते तपासा: `foundry service ps`

3. **मॉडेल सापडले नाही:**
   - उपलब्ध मॉडेल्सची यादी पहा: `foundry model list`
   - मॉडेल लोड करा: `foundry model run phi-4-mini`

### पडताळणी

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## संदर्भ

- [Foundry Local दस्तऐवज](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-सुसंगत API संदर्भ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

