# सत्र 6 नमूना: उपकरण के रूप में मॉडल

यह नमूना एक न्यूनतम राउटर + टूल रजिस्ट्री को लागू करता है, जो उपयोगकर्ता के प्रॉम्प्ट के आधार पर एक मॉडल का चयन करता है और Foundry Local के OpenAI-संगत एंडपॉइंट को कॉल करता है।

## फाइलें
- `router.py`: सरल रजिस्ट्री और हीयुरिस्टिक रूटिंग; एंडपॉइंट खोज + स्वास्थ्य जांच।

## चलाएं (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## नोट्स
- राउटर सरल कीवर्ड हीयुरिस्टिक्स का उपयोग करता है `general`, `reasoning`, और `code` टूल्स के बीच चयन करने के लिए और स्टार्ट पर `/v1/models` प्रिंट करता है।
- पर्यावरण वेरिएबल्स के माध्यम से कॉन्फ़िगर करें:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## संदर्भ
- Foundry Local (सीखें): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- इंफेरेंस SDKs के साथ एकीकरण करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।