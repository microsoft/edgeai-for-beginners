<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "254150b7d7854ec87ffcd88824d98079",
  "translation_date": "2025-12-16T01:03:07+00:00",
  "source_file": "Module08/samples/07/README.md",
  "language_code": "te"
}
-->
# Foundry Local as API Sample

ఈ నమూనా Microsoft Foundry Local ను OpenAI SDK పై ఆధారపడకుండా REST API సేవగా ఎలా ఉపయోగించాలో చూపిస్తుంది. ఇది గరిష్ట నియంత్రణ మరియు అనుకూలీకరణ కోసం ప్రత్యక్ష HTTP ఇంటిగ్రేషన్ నమూనాలను చూపిస్తుంది.

## అవలోకనం

Microsoft యొక్క అధికారిక Foundry Local నమూనాల ఆధారంగా, ఈ నమూనా అందిస్తుంది:
- FoundryLocalManager తో ప్రత్యక్ష REST API ఇంటిగ్రేషన్
- కస్టమ్ HTTP క్లయింట్ అమలు
- మోడల్ నిర్వహణ మరియు ఆరోగ్య పర్యవేక్షణ
- స్ట్రీమింగ్ మరియు నాన్-స్ట్రీమింగ్ ప్రతిస్పందన నిర్వహణ
- ఉత్పత్తి-సిద్ధమైన లోప నిర్వహణ మరియు రీట్రై లాజిక్

## ముందస్తు అవసరాలు

1. **Foundry Local ఇన్‌స్టాలేషన్**
   ```powershell
   # GitHub విడుదలల నుండి ఇన్‌స్టాల్ చేయండి
   winget install Microsoft.FoundryLocal
   ```

2. **Python ఆధారాలు**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## నిర్మాణం

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## ముఖ్య లక్షణాలు

### 1. **ప్రత్యక్ష HTTP ఇంటిగ్రేషన్**
- SDK ఆధారపడకుండా శుద్ధ REST API కాల్స్
- కస్టమ్ ప్రామాణీకరణ మరియు హెడ్డర్లు
- అభ్యర్థన/ప్రతిస్పందన నిర్వహణపై పూర్తి నియంత్రణ

### 2. **మోడల్ నిర్వహణ**
- డైనమిక్ మోడల్ లోడింగ్ మరియు అన్‌లోడింగ్
- ఆరోగ్య పర్యవేక్షణ మరియు స్థితి తనిఖీలు
- పనితీరు మెట్రిక్స్ సేకరణ

### 3. **ఉత్పత్తి నమూనాలు**
- ఎక్స్‌పోనెన్షియల్ బ్యాక్‌ఆఫ్‌తో రీట్రై మెకానిజంలు
- లోప సహనానికి సర్క్యూట్ బ్రేకర్
- సమగ్ర లాగింగ్ మరియు పర్యవేక్షణ

### 4. **అనుకూల ప్రతిస్పందన నిర్వహణ**
- రియల్-టైమ్ అప్లికేషన్ల కోసం స్ట్రీమింగ్ ప్రతిస్పందనలు
- అధిక-థ్రూపుట్ పరిస్థితుల కోసం బ్యాచ్ ప్రాసెసింగ్
- కస్టమ్ ప్రతిస్పందన పార్సింగ్ మరియు ధృవీకరణ

## ఉపయోగ ఉదాహరణలు

### ప్రాథమిక API ఇంటిగ్రేషన్
```python
from api_client import FoundryAPIClient

# API క్లయింట్‌ను ప్రారంభించండి
client = FoundryAPIClient()

# సాదా పూర్తి చేయడం
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### స్ట్రీమింగ్ ఇంటిగ్రేషన్
```python
# రియల్-టైమ్ అప్లికేషన్ల కోసం స్ట్రీమ్ ప్రతిస్పందనలు
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### ఆరోగ్య పర్యవేక్షణ
```python
# సేవా ఆరోగ్యాన్ని తనిఖీ చేయండి
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## ఫైల్ నిర్మాణం

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

## Microsoft Foundry Local ఇంటిగ్రేషన్

ఈ నమూనా Microsoft అధికారిక నమూనాలను అనుసరిస్తుంది:

1. **SDK ఇంటిగ్రేషన్**: సేవ నిర్వహణ కోసం `FoundryLocalManager` ఉపయోగిస్తుంది
2. **REST ఎండ్‌పాయింట్లు**: `/v1/chat/completions` మరియు ఇతర ఎండ్‌పాయింట్లకు ప్రత్యక్ష కాల్స్
3. **ప్రామాణీకరణ**: స్థానిక సేవల కోసం సరైన API కీ నిర్వహణ
4. **మోడల్ నిర్వహణ**: క్యాటలాగ్ జాబితా, డౌన్లోడ్ మరియు లోడింగ్ నమూనాలు
5. **లోప నిర్వహణ**: Microsoft సిఫార్సు చేసిన లోప కోడ్లు మరియు ప్రతిస్పందనలు

## ప్రారంభించడం

1. **ఆధారాలు ఇన్‌స్టాల్ చేయండి**
   ```bash
   pip install -r requirements.txt
   ```

2. **ప్రాథమిక ఉదాహరణ నడపండి**
   ```bash
   python examples/basic_usage.py
   ```

3. **స్ట్రీమింగ్ ప్రయత్నించండి**
   ```bash
   python examples/streaming.py
   ```

4. **ఉత్పత్తి సెటప్**
   ```bash
   python examples/production.py
   ```

## కాన్ఫిగరేషన్

అనుకూలీకరణ కోసం వాతావరణ చరాలు:
- `FOUNDRY_MODEL`: ఉపయోగించాల్సిన డిఫాల్ట్ మోడల్ (డిఫాల్ట్: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: అభ్యర్థన టైమౌట్ సెకన్లలో (డిఫాల్ట్: 30)
- `FOUNDRY_RETRIES`: రీట్రై ప్రయత్నాల సంఖ్య (డిఫాల్ట్: 3)
- `FOUNDRY_LOG_LEVEL`: లాగింగ్ స్థాయి (డిఫాల్ట్: "INFO")

## ఉత్తమ ఆచారాలు

1. **కనెక్షన్ నిర్వహణ**: మెరుగైన పనితీరు కోసం HTTP కనెక్షన్లను పునర్వినియోగం చేయండి
2. **లోప నిర్వహణ**: ఎక్స్‌పోనెన్షియల్ బ్యాక్‌ఆఫ్‌తో సరైన రీట్రై లాజిక్ అమలు చేయండి
3. **వనరుల పర్యవేక్షణ**: మోడల్ మెమరీ వినియోగం మరియు పనితీరు ట్రాక్ చేయండి
4. **భద్రత**: స్థానిక సేవలకూ సరైన ప్రామాణీకరణ ఉపయోగించండి
5. **పరీక్షలు**: యూనిట్ మరియు ఇంటిగ్రేషన్ పరీక్షలను రెండింటినీ చేర్చండి

## సమస్య పరిష్కారం

### సాధారణ సమస్యలు

**సేవ నడుస్తున్న లేదు**
```bash
# ఫౌండ్రీ లోకల్ స్థితిని తనిఖీ చేయండి
foundry status

# అవసరమైతే ప్రారంభించండి
foundry start
```

**మోడల్ లోడింగ్ సమస్యలు**
```bash
# అందుబాటులో ఉన్న మోడల్స్ జాబితా
foundry model list

# నిర్దిష్ట మోడల్ డౌన్లోడ్ చేయండి
foundry model download phi-4-mini
```

**కనెక్షన్ లోపాలు**
- Foundry Local సరైన పోర్ట్‌లో నడుస్తున్నదని నిర్ధారించుకోండి
- ఫైర్వాల్ సెట్టింగులను తనిఖీ చేయండి
- సరైన ప్రామాణీకరణ హెడ్డర్లు ఉన్నాయో చూసుకోండి

## పనితీరు మెరుగుదల

1. **కనెక్షన్ పూలింగ్**: బహుళ అభ్యర్థనల కోసం సెషన్ ఆబ్జెక్టులను ఉపయోగించండి
2. **అసింక్రోనస్ ఆపరేషన్లు**: సమాంతర అభ్యర్థనల కోసం asyncio ఉపయోగించండి
3. **క్యాషింగ్**: అవసరమైన చోట మోడల్ ప్రతిస్పందనలను క్యాష్ చేయండి
4. **పర్యవేక్షణ**: ప్రతిస్పందన సమయాలను ట్రాక్ చేసి టైమౌట్లను సర్దుబాటు చేయండి

## నేర్చుకునే ఫలితాలు

ఈ నమూనా పూర్తి చేసిన తర్వాత, మీరు అర్థం చేసుకుంటారు:
- Foundry Local తో ప్రత్యక్ష REST API ఇంటిగ్రేషన్
- కస్టమ్ HTTP క్లయింట్ అమలు నమూనాలు
- ఉత్పత్తి-సిద్ధమైన లోప నిర్వహణ మరియు పర్యవేక్షణ
- Microsoft Foundry Local సేవా నిర్మాణం
- స్థానిక AI సేవల కోసం పనితీరు మెరుగుదల సాంకేతికతలు

## తదుపరి దశలు

- నమూనా 08: Windows 11 చాట్ అప్లికేషన్ అన్వేషించండి
- నమూనా 09: మల్టీ-ఏజెంట్ ఆర్కెస్ట్రేషన్ ప్రయత్నించండి
- నమూనా 10: Foundry Local as Tools ఇంటిగ్రేషన్ నేర్చుకోండి

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->