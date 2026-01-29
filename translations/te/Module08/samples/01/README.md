# నమూనా 01: OpenAI SDK ద్వారా త్వరిత చాట్

స్థానిక AI ఇన్ఫరెన్స్ కోసం Microsoft Foundry Local తో OpenAI SDK ను ఎలా ఉపయోగించాలో చూపించే ఒక సాదా చాట్ ఉదాహరణ.

## అవలోకనం

ఈ నమూనా ఎలా చేయాలో చూపిస్తుంది:
- Foundry Local తో OpenAI Python SDK ఉపయోగించడం
- Azure OpenAI మరియు స్థానిక Foundry కాన్ఫిగరేషన్లను రెండింటినీ నిర్వహించడం
- సరైన లోప నిర్వహణ మరియు fallback వ్యూహాలను అమలు చేయడం
- సర్వీస్ నిర్వహణ కోసం FoundryLocalManager ఉపయోగించడం

## ముందస్తు అవసరాలు

- **Foundry Local**: PATH లో ఇన్‌స్టాల్ చేసి అందుబాటులో ఉండాలి
- **Python**: 3.8 లేదా తరువాతి సంస్కరణ
- **మోడల్**: Foundry Local లో లోడ్ చేసిన మోడల్ (ఉదా: `phi-4-mini`)

## ఇన్‌స్టాలేషన్

1. **Python వాతావరణాన్ని సెట్ చేయండి:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ఆవశ్యక డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local సర్వీస్ ప్రారంభించి మోడల్ లోడ్ చేయండి:**
   ```cmd
   foundry model run phi-4-mini
   ```

## ఉపయోగం

### Foundry Local (డిఫాల్ట్)

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

## కోడ్ లక్షణాలు

### FoundryLocalManager ఇంటిగ్రేషన్

సరైన సర్వీస్ నిర్వహణ కోసం అధికారిక Foundry Local SDK ఉపయోగిస్తుంది:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ఫౌండ్రీ లోకల్‌ను ప్రారంభించండి
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# OpenAI క్లయింట్‌ను కాన్ఫిగర్ చేయండి
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### లోప నిర్వహణ

మాన్యువల్ కాన్ఫిగరేషన్ కు fallback తో బలమైన లోప నిర్వహణ:
- ఆటోమేటిక్ సర్వీస్ కనుగొనడం
- SDK అందుబాటులో లేకపోతే సున్నితమైన తగ్గింపు
- సమస్య పరిష్కారానికి స్పష్టమైన లోప సందేశాలు

## వాతావరణ వేరియబుల్స్

| వేరియబుల్ | వివరణ | డిఫాల్ట్ | అవసరం |
|----------|-------------|---------|----------|
| `MODEL` | మోడల్ అలియాస్ లేదా పేరు | `phi-4-mini` | కాదు |
| `BASE_URL` | Foundry Local బేస్ URL | `http://localhost:8000` | కాదు |
| `API_KEY` | API కీ (సాధారణంగా స్థానికానికి అవసరం లేదు) | `""` | కాదు |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ఎండ్‌పాయింట్ | - | Azure కోసం |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API కీ | - | Azure కోసం |
| `AZURE_OPENAI_API_VERSION` | Azure API సంస్కరణ | `2024-08-01-preview` | కాదు |

## సమస్య పరిష్కారం

### సాధారణ సమస్యలు

1. **"Foundry SDK ఉపయోగించలేకపోయాం" హెచ్చరిక:**
   - foundry-local-sdk ఇన్‌స్టాల్ చేయండి: `pip install foundry-local-sdk`
   - లేదా మాన్యువల్ కాన్ఫిగరేషన్ కోసం వాతావరణ వేరియబుల్స్ సెట్ చేయండి

2. **కనెక్షన్ తిరస్కరించబడింది:**
   - Foundry Local నడుస్తుందో లేదో నిర్ధారించుకోండి: `foundry service status`
   - మోడల్ లోడ్ అయిందో లేదో తనిఖీ చేయండి: `foundry service ps`

3. **మోడల్ కనుగొనబడలేదు:**
   - అందుబాటులో ఉన్న మోడల్స్ జాబితా చేయండి: `foundry model list`
   - మోడల్ లోడ్ చేయండి: `foundry model run phi-4-mini`

### ధృవీకరణ

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## సూచనలు

- [Foundry Local డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-అనుకూల API సూచిక](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->