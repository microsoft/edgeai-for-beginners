# Foundry Local SDK - త్వరిత సూచిక

## ఇన్‌స్టాలేషన్

```bash
# SDK ను ఇన్‌స్టాల్ చేయండి
pip install foundry-local-sdk openai

# Foundry Local సేవను ఇన్‌స్టాల్ చేయండి
# విండోస్
winget install Microsoft.FoundryLocal

# మాక్‌ఓఎస్
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## సర్వీస్ నిర్వహణ

```bash
# సేవ ప్రారంభించండి
foundry service start

# స్థితిని తనిఖీ చేయండి
foundry service status

# సేవ నిలిపివేయండి
foundry service stop

# మోడల్స్ జాబితా
foundry model ls

# మోడల్ డౌన్లోడ్ చేయండి
foundry model download phi-4-mini

# మోడల్ సమాచారం పొందండి
foundry model info phi-4-mini
```

## ప్రాథమిక ఉపయోగ నమూనా

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# మేనేజర్‌ను ప్రారంభించండి (అవసరమైతే సర్వీస్ ప్రారంభిస్తుంది)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# OpenAI-సమర్థమైన క్లయింట్‌ను సృష్టించండి
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# మోడల్ ID పొందండి
model_id = manager.get_model_info(alias).id

# చాట్ పూర్తి చేయడం
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## స్ట్రీమింగ్ స్పందన

```python
stream = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## వర్క్‌షాప్ యుటిల్స్ (సరళీకృతం)

```python
from workshop_utils import chat_once

# క్యాచింగ్ మరియు రీట్రైతో ఒకే కాల్
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## పర్యావరణ వేరియబుల్స్

```python
import os

# టోకెన్ వినియోగాన్ని చూపించండి
os.environ['SHOW_USAGE'] = '1'

# మళ్లీ ప్రయత్నాలను ప్రారంభించండి
os.environ['RETRY_ON_FAIL'] = '1'

# మళ్లీ ప్రయత్నించే ఆలస్యం సెట్ చేయండి
os.environ['RETRY_BACKOFF'] = '2.0'

# కస్టమ్ ఎండ్‌పాయింట్
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## సాధారణ మోడల్ అలియాసులు

| అలియాస్ | పరిమాణం | ఉత్తమం కోసం |
|-------|------|----------|
| `phi-4-mini` | ~4B | సాధారణ, సారాంశం |
| `phi-3.5-mini` | ~3.5B | కోడ్, పునఃరూపకల్పన |
| `qwen2.5-0.5b` | ~0.5B | వేగవంతమైన వర్గీకరణ |
| `qwen2.5-coder-0.5b` | ~0.5B | కోడ్ ఉత్పత్తి |
| `gemma-2b` | ~2B | సృజనాత్మక రచన |

## లోపాల నిర్వహణ

```python
from openai import OpenAIError

try:
    text, usage = chat_once('phi-4-mini', messages=[...])
except RuntimeError as e:
    print(f"Manager initialization failed: {e}")
    print("Check: foundry service status")
except OpenAIError as e:
    print(f"API call failed: {e}")
    print("Check: foundry model ls")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## సమస్య పరిష్కారం

### కనెక్షన్ లోపం
```bash
# సేవను తనిఖీ చేయండి
foundry service status

# మళ్లీ ప్రారంభించండి
foundry service stop
foundry service start

# ఎండ్‌పాయింట్‌ను పరీక్షించండి
curl http://localhost:55769/health
```

### మోడల్ కనుగొనబడలేదు
```bash
# అందుబాటులో ఉన్న జాబితా
foundry model ls

# అవసరమైతే డౌన్లోడ్ చేయండి
foundry model download phi-4-mini
```

### దిగుమతి లోపం
```bash
# SDKను మళ్లీ ఇన్‌స్టాల్ చేయండి
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## అధునాతన: బహుళ మోడల్స్

```python
from workshop_utils import get_client

# బహుళ మోడల్స్‌ను ప్రారంభించండి
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# వేర్వేరు మోడల్స్‌ను ఉపయోగించండి
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## పనితీరు సూచనలు

1. **క్యాష్ క్లయింట్లు**: `FoundryLocalManager` ఉదాహరణలను పునఃఉపయోగించండి
2. **బ్యాచ్ అభ్యర్థనలు**: అనేక ప్రాంప్ట్‌లను వరుసగా ప్రాసెస్ చేయండి
3. **max_tokens సర్దుబాటు**: తక్కువ = వేగవంతమైన స్పందనలు
4. **మోడల్స్‌ను ముందుగా లోడ్ చేయండి**: ఉత్పత్తి ఉపయోగానికి ముందు డౌన్‌లోడ్ చేయండి
5. **వినియోగాన్ని పర్యవేక్షించండి**: `SHOW_USAGE=1` తో టోకెన్లను ట్రాక్ చేయండి

## వనరులు

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**త్వరిత ప్రారంభం:**
```bash
# అన్నీ ఇన్‌స్టాల్ చేయండి
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# సర్వీస్ ప్రారంభించండి
foundry service start

# పైథాన్‌లో పరీక్షించండి
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->