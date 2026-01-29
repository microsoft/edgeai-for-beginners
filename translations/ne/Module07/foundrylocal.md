# Foundry Local Windows र Mac मा

यो मार्गदर्शनले तपाईंलाई Microsoft Foundry Local Windows र Mac मा स्थापना, सञ्चालन, र एकीकृत गर्न मद्दत गर्दछ। सबै चरणहरू र आदेशहरू Microsoft Learn दस्तावेजहरूसँग प्रमाणित छन्।

- सुरु गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI सन्दर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs एकीकृत गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मोडेलहरू कम्पाइल गर्नुहोस् (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: स्थानीय बनाम क्लाउड: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## १) Windows मा स्थापना / अपग्रेड गर्नुहोस्

- स्थापना:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- संस्करण जाँच:
```cmd
foundry --version
```
     
**स्थापना / Mac**

**MacOS**: 
टर्मिनल खोल्नुहोस् र निम्न आदेश चलाउनुहोस्:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## २) CLI आधारभूत (तीन श्रेणीहरू)

- मोडेल:
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
- क्यास:
```cmd
foundry cache --help
foundry cache list
```

नोटहरू:
- सेवाले OpenAI-संगत REST API प्रदान गर्दछ। अन्त बिन्दुको पोर्ट गतिशील रूपमा छुट्याइन्छ; यसलाई पत्ता लगाउन `foundry service status` प्रयोग गर्नुहोस्।
- सुविधा को लागि SDKs प्रयोग गर्नुहोस्; तिनीहरूले अन्त बिन्दु पत्ता लगाउने प्रक्रिया स्वचालित रूपमा व्यवस्थापन गर्छन् जहाँ समर्थित छ।

## ३) स्थानीय अन्त बिन्दु पत्ता लगाउनुहोस् (डायनामिक पोर्ट)

Foundry Local ले प्रत्येक पटक सेवा सुरु हुँदा गतिशील पोर्ट छुट्याउँछ:
```cmd
foundry service status
```
रिपोर्ट गरिएको `http://localhost:<PORT>` लाई OpenAI-संगत पथहरूसँग `base_url` को रूपमा प्रयोग गर्नुहोस् (उदाहरणका लागि, `/v1/chat/completions`)।

## ४) OpenAI Python SDK मार्फत छिटो परीक्षण

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
सन्दर्भहरू:
- SDK एकीकरण: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## ५) आफ्नो मोडेल ल्याउनुहोस् (Olive प्रयोग गरेर कम्पाइल गर्नुहोस्)

यदि तपाईंलाई क्याटलगमा नभएको मोडेल चाहिन्छ भने, Olive प्रयोग गरेर Foundry Local को लागि यसलाई ONNX मा कम्पाइल गर्नुहोस्।

उच्च-स्तरीय प्रवाह (चरणहरूको लागि दस्तावेज हेर्नुहोस्):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
दस्तावेजहरू:
- BYOM कम्पाइल: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## ६) समस्या समाधान

- सेवा स्थिति र लगहरू जाँच गर्नुहोस्:
```cmd
foundry service status
foundry service diag
```
- क्यास खाली वा सार्नुहोस्:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- पछिल्लो प्रिभ्यूमा अपडेट गर्नुहोस्:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## ७) सम्बन्धित Windows विकासकर्ता अनुभव

- Windows स्थानीय बनाम क्लाउड AI विकल्पहरू, जसमा Foundry Local र Windows ML समावेश छ:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local सँग (च्याट अन्त बिन्दु URL प्राप्त गर्न `foundry service status` प्रयोग गर्नुहोस्):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[अर्को Windows विकासकर्ता](./windowdeveloper.md)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।