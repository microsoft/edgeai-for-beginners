# विंडोज और मैक पर Foundry Local

यह गाइड आपको Microsoft Foundry Local को विंडोज और मैक पर इंस्टॉल, रन और इंटीग्रेट करने में मदद करता है। सभी चरण और कमांड Microsoft Learn डॉक्यूमेंट्स के अनुसार सत्यापित हैं।

- शुरुआत करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI संदर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs को इंटीग्रेट करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मॉडल्स को कंपाइल करें (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local बनाम Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) विंडोज पर इंस्टॉल / अपग्रेड करें

- इंस्टॉल:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- वर्जन चेक करें:
```cmd
foundry --version
```
     
**इंस्टॉल / मैक**

**MacOS**: 
एक टर्मिनल खोलें और निम्नलिखित कमांड चलाएं:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI बेसिक्स (तीन श्रेणियां)

- मॉडल:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- सर्विस:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- कैश:
```cmd
foundry cache --help
foundry cache list
```

नोट्स:
- सर्विस एक OpenAI-संगत REST API को एक्सपोज़ करती है। एंडपॉइंट पोर्ट डायनामिक रूप से अलॉट किया जाता है; इसे खोजने के लिए `foundry service status` का उपयोग करें।
- सुविधा के लिए SDKs का उपयोग करें; ये समर्थित जगहों पर एंडपॉइंट डिस्कवरी को स्वचालित रूप से संभालते हैं।

## 3) लोकल एंडपॉइंट खोजें (डायनामिक पोर्ट)

Foundry Local हर बार सर्विस शुरू होने पर एक डायनामिक पोर्ट असाइन करता है:
```cmd
foundry service status
```
रिपोर्ट किए गए `http://localhost:<PORT>` का उपयोग OpenAI-संगत पाथ्स (जैसे, `/v1/chat/completions`) के साथ `base_url` के रूप में करें।

## 4) OpenAI Python SDK के माध्यम से त्वरित परीक्षण

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
- SDK इंटीग्रेशन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) अपना मॉडल लाएं (Olive के साथ कंपाइल करें)

यदि आपको कैटलॉग में उपलब्ध मॉडल की आवश्यकता नहीं है, तो इसे Olive का उपयोग करके Foundry Local के लिए ONNX में कंपाइल करें।

उच्च-स्तरीय फ्लो (चरणों के लिए डॉक्यूमेंट्स देखें):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
डॉक्यूमेंट्स:
- BYOM कंपाइल: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) समस्या निवारण

- सर्विस स्टेटस और लॉग्स चेक करें:
```cmd
foundry service status
foundry service diag
```
- कैश को साफ करें या स्थानांतरित करें:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- नवीनतम प्रीव्यू में अपडेट करें:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) संबंधित विंडोज डेवलपर अनुभव

- विंडोज लोकल बनाम क्लाउड AI विकल्प, जिसमें Foundry Local और Windows ML शामिल हैं:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI टूलकिट Foundry Local के साथ (चैट एंडपॉइंट URL प्राप्त करने के लिए `foundry service status` का उपयोग करें):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[अगला विंडोज डेवलपर](./windowdeveloper.md)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।