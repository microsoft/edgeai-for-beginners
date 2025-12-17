<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-12-16T00:37:18+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "te"
}
-->
# సెషన్ 5 నమూనా: బహుళ-ఏజెంట్ సమన్వయం

ఈ నమూనా Foundry Local యొక్క OpenAI-అనుకూల ఎండ్‌పాయింట్ ఉపయోగించి కోఆర్డినేటర్ + నిపుణుల నమూనాను చూపిస్తుంది.

## రన్ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## ధృవీకరణ
```cmd
curl http://localhost:8000/v1/models
```

## సమస్య పరిష్కారం
- VS Code `coordinator.py` లో `import specialists` అనేది అనిర్వచితంగా చూపిస్తే, మీరు మాడ్యూల్‌గా నడపడం మరియు ఇంటర్‌ప్రెటర్ `Module08/.venv` ను సూచిస్తున్నదని నిర్ధారించుకోండి:
	- నడపండి: `python -m samples.05.agents.coordinator`
	- ఇంటర్‌ప్రెటర్ ఎంచుకోండి: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## సూచనలు
- Foundry Local (తెలుసుకోండి): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI ఏజెంట్లు అవలోకనం: https://learn.microsoft.com/azure/ai-services/agents/overview
- ఫంక్షన్ కాలింగ్ నమూనా (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->