# सत्र ६ नमूना: उपकरणको रूपमा मोडेलहरू

यो नमूनाले न्यूनतम राउटर + उपकरण रजिस्ट्री कार्यान्वयन गर्दछ जसले प्रयोगकर्ताको प्रम्प्टको आधारमा मोडेल चयन गर्दछ र Foundry Local को OpenAI-संग मिल्दो अन्त बिन्दुमा कल गर्दछ।

## फाइलहरू
- `router.py`: साधारण रजिस्ट्री र ह्युरिस्टिक राउटिङ; अन्त बिन्दु पत्ता लगाउने + स्वास्थ्य जाँच।

## चलाउनुहोस् (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## नोटहरू
- राउटरले साधारण कीवर्ड ह्युरिस्टिक्स प्रयोग गरेर `general`, `reasoning`, र `code` उपकरणहरू बीच चयन गर्दछ र सुरुमा `/v1/models` प्रिन्ट गर्दछ।
- वातावरण चरहरू मार्फत कन्फिगर गर्नुहोस्:
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

## सन्दर्भहरू
- Foundry Local (शिक्षा): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- अनुमान SDKs सँग एकीकृत गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।