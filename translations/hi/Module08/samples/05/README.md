# सत्र 5 नमूना: मल्टी-एजेंट ऑर्केस्ट्रेशन

यह नमूना Foundry Local के OpenAI-संगत एंडपॉइंट का उपयोग करके एक समन्वयक + विशेषज्ञ पैटर्न को प्रदर्शित करता है।

## चलाएं (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## सत्यापन करें
```cmd
curl http://localhost:8000/v1/models
```

## समस्या निवारण
- यदि VS Code `coordinator.py` में `import specialists` को अनसुलझा दिखाता है, तो सुनिश्चित करें कि आप इसे एक मॉड्यूल के रूप में चला रहे हैं और इंटरप्रेटर `Module08/.venv` की ओर इशारा कर रहा है:
	- चलाएं: `python -m samples.05.agents.coordinator`
	- इंटरप्रेटर चुनें: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## संदर्भ
- Foundry Local (सीखें): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents का अवलोकन: https://learn.microsoft.com/azure/ai-services/agents/overview
- फ़ंक्शन कॉलिंग नमूना (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

