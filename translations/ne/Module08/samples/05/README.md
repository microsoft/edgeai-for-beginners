# सत्र ५ नमूना: बहु-एजेन्ट समन्वय

यो नमूनाले Foundry Local को OpenAI-संग मिल्दो अन्तर्क्रियात्मक अन्त्य बिन्दु प्रयोग गर्दै समन्वयकर्ता + विशेषज्ञहरूको ढाँचा प्रदर्शन गर्दछ।

## चलाउनुहोस् (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## प्रमाणित गर्नुहोस्
```cmd
curl http://localhost:8000/v1/models
```

## समस्या समाधान
- यदि VS Code ले `coordinator.py` मा `import specialists` लाई अनसुलझिएको देखाउँछ भने, सुनिश्चित गर्नुहोस् कि तपाईंले यसलाई मोड्युलको रूपमा चलाउनु भएको छ र इन्टरप्रेटर `Module08/.venv` मा संकेत गर्दछ:
	- चलाउनुहोस्: `python -m samples.05.agents.coordinator`
	- इन्टरप्रेटर चयन गर्नुहोस्: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## सन्दर्भहरू
- Foundry Local (शिक्षा): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents अवलोकन: https://learn.microsoft.com/azure/ai-services/agents/overview
- फङ्सन कलिङ नमूना (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

