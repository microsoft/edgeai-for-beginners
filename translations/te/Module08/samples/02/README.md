# నమూనా 02: OpenAI SDK ఇంటిగ్రేషన్

OpenAI Python SDKతో అధునాతన ఇంటిగ్రేషన్‌ను ప్రదర్శిస్తుంది, Microsoft Foundry Local మరియు Azure OpenAI రెండింటినీ స్ట్రీమింగ్ ప్రతిస్పందనలతో మరియు సరైన లోపాల నిర్వహణతో మద్దతు ఇస్తుంది.

## అవలోకనం

ఈ నమూనా చూపిస్తుంది:
- Foundry Local మరియు Azure OpenAI మధ్య సులభమైన మార్పిడి
- మెరుగైన వినియోగదారు అనుభవం కోసం స్ట్రీమింగ్ చాట్ పూర్తి
- FoundryLocalManager SDK యొక్క సరైన ఉపయోగం
- బలమైన లోపాల నిర్వహణ మరియు ఫాల్బ్యాక్ యంత్రాంగాలు
- ఉత్పత్తి-సిద్ధమైన కోడ్ నమూనాలు

## ముందస్తు అవసరాలు

- **Foundry Local**: ఇన్‌స్టాల్ చేసి నడుస్తోంది (స్థానిక ఇన్ఫరెన్స్ కోసం)
- **Python**: 3.8 లేదా తరువాత OpenAI SDKతో
- **Azure OpenAI**: చెల్లుబాటు అయ్యే ఎండ్‌పాయింట్ మరియు API కీ (క్లౌడ్ ఇన్ఫరెన్స్ కోసం)

## ఇన్‌స్టాలేషన్

1. **Python పరిసరాన్ని సెట్ చేయండి:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ఆవశ్యకతలను ఇన్‌స్టాల్ చేయండి:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ప్రారంభించండి (స్థానిక మోడ్ కోసం):**
   ```cmd
   foundry model run phi-4-mini
   ```

## ఉపయోగం సందర్భాలు

### Foundry Local (డిఫాల్ట్)

**ఎంపిక 1: FoundryLocalManager ఉపయోగించడం (సిఫార్సు చేయబడింది)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ఎంపిక 2: మాన్యువల్ కాన్ఫిగరేషన్**
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

## కోడ్ నిర్మాణం

### క్లయింట్ ఫ్యాక్టరీ నమూనా

నమూనా సరైన క్లయింట్లను సృష్టించడానికి ఫ్యాక్టరీ నమూనాను ఉపయోగిస్తుంది:

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

### స్ట్రీమింగ్ ప్రతిస్పందనలు

నమూనా రియల్-టైమ్ ప్రతిస్పందన ఉత్పత్తికి స్ట్రీమింగ్‌ను ప్రదర్శిస్తుంది:

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

## పరిసర వేరియబుల్స్

### Foundry Local కాన్ఫిగరేషన్

| వేరియబుల్ | వివరణ | డిఫాల్ట్ | అవసరం |
|----------|-------------|---------|----------|
| `MODEL` | ఉపయోగించాల్సిన మోడల్ అలియాస్ | `phi-4-mini` | కాదు |
| `BASE_URL` | Foundry Local ఎండ్‌పాయింట్ | `http://localhost:8000` | కాదు |
| `API_KEY` | API కీ (స్థానికానికి ఐచ్ఛికం) | `""` | కాదు |

### Azure OpenAI కాన్ఫిగరేషన్

| వేరియబుల్ | వివరణ | డిఫాల్ట్ | అవసరం |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI వనరు ఎండ్‌పాయింట్ | - | అవును |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API కీ | - | అవును |
| `AZURE_OPENAI_API_VERSION` | API వెర్షన్ | `2024-08-01-preview` | కాదు |
| `MODEL` | Azure డిప్లాయ్‌మెంట్ పేరు | `your-deployment-name` | అవును |

## అధునాతన ఫీచర్లు

### ఆటోమేటిక్ సర్వీస్ డిస్కవరీ

పరిసర వేరియబుల్స్ ఆధారంగా సరైన సర్వీస్‌ను ఆటోమేటిక్‌గా గుర్తిస్తుంది:

1. **Azure మోడ్**: `AZURE_OPENAI_ENDPOINT` మరియు `AZURE_OPENAI_API_KEY` సెట్ అయితే
2. **Foundry SDK మోడ్**: Foundry Local SDK అందుబాటులో ఉంటే
3. **మాన్యువల్ మోడ్**: మాన్యువల్ కాన్ఫిగరేషన్‌కు ఫాల్బ్యాక్

### లోపాల నిర్వహణ

- SDK నుండి మాన్యువల్ కాన్ఫిగరేషన్‌కు సున్నితమైన ఫాల్బ్యాక్
- సమస్య పరిష్కారానికి స్పష్టమైన లోప సందేశాలు
- నెట్‌వర్క్ సమస్యల కోసం సరైన ఎక్సెప్షన్ హ్యాండ్లింగ్
- అవసరమైన పరిసర వేరియబుల్స్ ధృవీకరణ

## పనితీరు పరిగణనలు

### స్థానిక vs క్లౌడ్ ట్రేడ్-ఆఫ్స్

**Foundry Local లాభాలు:**
- ✅ ఏ API ఖర్చులు లేవు
- ✅ డేటా గోప్యత (డేటా పరికరం నుండి బయటకు పోవదు)
- ✅ మద్దతు ఉన్న మోడల్స్ కోసం తక్కువ ఆలస్యం
- ✅ ఆఫ్‌లైన్‌లో పనిచేస్తుంది

**Azure OpenAI లాభాలు:**
- ✅ తాజా పెద్ద మోడల్స్‌కు ప్రాప్యత
- ✅ అధిక థ్రూపుట్
- ✅ స్థానిక కంప్యూట్ అవసరాలు లేవు
- ✅ ఎంటర్ప్రైజ్-గ్రేడ్ SLA

## సమస్య పరిష్కారం

### సాధారణ సమస్యలు

1. **"Foundry SDK ఉపయోగించలేకపోయింది" హెచ్చరిక:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure ధృవీకరణ లోపాలు:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **మోడల్ అందుబాటులో లేదు:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### ఆరోగ్య తనిఖీలు

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## తదుపరి దశలు

- **నమూనా 03**: మోడల్ డిస్కవరీ మరియు బెంచ్‌మార్కింగ్
- **నమూనా 04**: చైన్‌లిట్ RAG అప్లికేషన్ నిర్మాణం
- **నమూనా 05**: బహుళ ఏజెంట్ ఆర్కెస్ట్రేషన్
- **నమూనా 06**: మోడల్స్-అస్-టూల్స్ రౌటింగ్

## సూచనలు

- [Azure OpenAI డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK రిఫరెన్స్](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK డాక్యుమెంటేషన్](https://github.com/openai/openai-python)
- [స్ట్రీమింగ్ కంప్లీషన్స్ గైడ్](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->