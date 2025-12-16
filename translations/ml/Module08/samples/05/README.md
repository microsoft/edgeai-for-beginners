<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-12-16T00:37:35+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "ml"
}
-->
# സെഷൻ 5 സാമ്പിൾ: മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ

ഈ സാമ്പിൾ ഫൗണ്ടറി ലോക്കലിന്റെ OpenAI-സമാനമായ എന്റ്പോയിന്റ് ഉപയോഗിച്ച് കോഓർഡിനേറ്റർ + സ്പെഷ്യലിസ്റ്റുകൾ പാറ്റേൺ കാണിക്കുന്നു.

## റൺ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## സാധുത പരിശോധിക്കുക
```cmd
curl http://localhost:8000/v1/models
```

## പ്രശ്നപരിഹാരം
- VS കോഡ് `coordinator.py`യിൽ `import specialists` അന്യമായതായി കാണിച്ചാൽ, നിങ്ങൾ മോഡ്യൂളായി റൺ ചെയ്യുന്നതും ഇന്റർപ്രിറ്റർ `Module08/.venv` കാണിക്കുന്നതും ഉറപ്പാക്കുക:
	- റൺ ചെയ്യുക: `python -m samples.05.agents.coordinator`
	- ഇന്റർപ്രിറ്റർ തിരഞ്ഞെടുക്കുക: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## റഫറൻസുകൾ
- ഫൗണ്ടറി ലോക്കൽ (കഴിവ് നേടുക): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- അസ്യൂർ AI ഏജന്റുകൾ അവലോകനം: https://learn.microsoft.com/azure/ai-services/agents/overview
- ഫംഗ്ഷൻ കോളിംഗ് സാമ്പിൾ (ഫൗണ്ടറി ലോക്കൽ): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->