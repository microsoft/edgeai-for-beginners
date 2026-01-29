# Windows आणि Mac वर Foundry Local

ही मार्गदर्शिका तुम्हाला Windows आणि Mac वर Microsoft Foundry Local स्थापित, चालवणे आणि समाकलित करण्यास मदत करते. सर्व चरण आणि आदेश Microsoft Learn दस्तऐवजांनुसार सत्यापित केले आहेत.

- सुरुवात करा: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI संदर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs समाकलित करा: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मॉडेल्स संकलित करा (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: स्थानिक vs क्लाउड: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows वर स्थापित / अपग्रेड करा

- स्थापित:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- आवृत्ती तपासा:
```cmd
foundry --version
```
     
**स्थापित / Mac**

**MacOS**: 
टर्मिनल उघडा आणि खालील आदेश चालवा:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI मूलभूत गोष्टी (तीन श्रेणी)

- मॉडेल:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- सेवा:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- कॅशे:
```cmd
foundry cache --help
foundry cache list
```

टीप:
- सेवा OpenAI-सुसंगत REST API उघडते. एंडपॉइंट पोर्ट डायनॅमिकली नियुक्त केला जातो; `foundry service status` वापरून तो शोधा.
- सोयीसाठी SDKs वापरा; ते समर्थित ठिकाणी एंडपॉइंट शोध आपोआप हाताळतात.

## 3) स्थानिक एंडपॉइंट शोधा (डायनॅमिक पोर्ट)

Foundry Local प्रत्येक वेळी सेवा सुरू झाल्यावर डायनॅमिक पोर्ट नियुक्त करते:
```cmd
foundry service status
```
`http://localhost:<PORT>` वापरा तुमच्या `base_url` म्हणून OpenAI-सुसंगत पथांसह (उदाहरणार्थ, `/v1/chat/completions`).

## 4) OpenAI Python SDK द्वारे जलद चाचणी

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
संदर्भ:
- SDK समाकलन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) तुमचे स्वतःचे मॉडेल आणा (Olive सह संकलित करा)

जर तुम्हाला कॅटलॉगमध्ये नसलेले मॉडेल आवश्यक असेल, तर ते Foundry Local साठी ONNX मध्ये संकलित करा Olive वापरून.

उच्च-स्तरीय प्रवाह (पायऱ्यांसाठी दस्तऐवज पहा):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
दस्तऐवज:
- BYOM संकलन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) समस्या सोडवणे

- सेवा स्थिती आणि लॉग तपासा:
```cmd
foundry service status
foundry service diag
```
- कॅशे साफ करा किंवा हलवा:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- नवीनतम प्रीव्ह्यूमध्ये अपडेट करा:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) संबंधित Windows विकसक अनुभव

- Windows स्थानिक vs क्लाउड AI पर्याय, ज्यामध्ये Foundry Local आणि Windows ML समाविष्ट आहे:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local सह (चॅट एंडपॉइंट URL मिळवण्यासाठी `foundry service status` वापरा):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[पुढील Windows विकसक](./windowdeveloper.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.