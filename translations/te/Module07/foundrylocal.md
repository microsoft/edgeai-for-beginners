# Windows & Mac పై Foundry Local

ఈ గైడ్ Windows మరియు Mac పై Microsoft Foundry Local ను ఇన్‌స్టాల్ చేయడం, నడపడం మరియు ఇంటిగ్రేట్ చేయడంలో మీకు సహాయపడుతుంది. అన్ని దశలు మరియు కమాండ్లు Microsoft Learn డాక్స్‌తో ధృవీకరించబడ్డాయి.

- ప్రారంభించండి: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ఆర్కిటెక్చర్: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI సూచిక: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKలను ఇంటిగ్రేట్ చేయండి: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF మోడల్స్ కంపైల్ చేయండి (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: లోకల్ vs క్లౌడ్: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows పై ఇన్‌స్టాల్ / అప్‌గ్రేడ్ చేయండి

- ఇన్‌స్టాల్ చేయండి:
```cmd
winget install Microsoft.FoundryLocal
```
- అప్‌గ్రేడ్ చేయండి:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- వెర్షన్ తనిఖీ:
```cmd
foundry --version
```
     
**ఇన్‌స్టాల్ / Mac**

**MacOS**: 
ఒక టెర్మినల్ తెరవండి మరియు క్రింది కమాండ్ నడపండి:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI ప్రాథమికాలు (మూడు వర్గాలు)

- మోడల్:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- సర్వీస్:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- క్యాష్:
```cmd
foundry cache --help
foundry cache list
```

గమనికలు:
- సర్వీస్ ఒక OpenAI-అనుకూల REST APIని అందిస్తుంది. ఎండ్‌పాయింట్ పోర్ట్ డైనమిక్‌గా కేటాయించబడుతుంది; దాన్ని కనుగొనడానికి `foundry service status` ఉపయోగించండి.
- సౌకర్యం కోసం SDKలను ఉపయోగించండి; అవి ఎండ్‌పాయింట్ కనుగొనడాన్ని ఆటోమేటిక్‌గా నిర్వహిస్తాయి, మద్దతు ఉన్న చోట్ల.

## 3) లోకల్ ఎండ్‌పాయింట్ కనుగొనండి (డైనమిక్ పోర్ట్)

Foundry Local ప్రతి సారి సర్వీస్ ప్రారంభించినప్పుడు డైనమిక్ పోర్ట్ కేటాయిస్తుంది:
```cmd
foundry service status
```
రిపోర్ట్ చేసిన `http://localhost:<PORT>` ను OpenAI-అనుకూల మార్గాలతో (ఉదాహరణకు, `/v1/chat/completions`) మీ `base_url` గా ఉపయోగించండి.

## 4) OpenAI Python SDK ద్వారా త్వరిత పరీక్ష

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
సూచనలు:
- SDK ఇంటిగ్రేషన్: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) మీ స్వంత మోడల్ తీసుకురండి (Olive తో కంపైల్ చేయండి)

క్యాటలాగ్‌లో లేని మోడల్ అవసరమైతే, దాన్ని Foundry Local కోసం ONNX గా Olive ఉపయోగించి కంపైల్ చేయండి.

హై-లెవల్ ఫ్లో (దశల కోసం డాక్స్ చూడండి):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
డాక్స్:
- BYOM కంపైల్: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) సమస్య పరిష్కారం

- సర్వీస్ స్థితి మరియు లాగ్‌లను తనిఖీ చేయండి:
```cmd
foundry service status
foundry service diag
```
- క్యాష్ క్లియర్ చేయండి లేదా తరలించండి:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- తాజా ప్రివ్యూ కి అప్‌డేట్ చేయండి:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) సంబంధిత Windows డెవలపర్ అనుభవం

- Windows లోకల్ vs క్లౌడ్ AI ఎంపికలు, అందులో Foundry Local మరియు Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI టూల్‌కిట్ తో Foundry Local (చాట్ ఎండ్‌పాయింట్ URL పొందడానికి `foundry service status` ఉపయోగించండి):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[తరువాత Windows డెవలపర్](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->