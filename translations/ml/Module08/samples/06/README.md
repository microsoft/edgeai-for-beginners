# സെഷൻ 6 സാമ്പിൾ: മോഡലുകൾ ടൂളുകളായി

ഈ സാമ്പിൾ ഒരു ലഘു റൂട്ടർ + ടൂൾ രജിസ്ട്രി നടപ്പിലാക്കുന്നു, ഇത് ഉപയോക്തൃ പ്രോംപ്റ്റിന്റെ അടിസ്ഥാനത്തിൽ ഒരു മോഡൽ തിരഞ്ഞെടുക്കുകയും Foundry Local-ന്റെ OpenAI-സമാനമായ എന്റ്പോയിന്റ് വിളിക്കുകയും ചെയ്യുന്നു.

## ഫയലുകൾ
- `router.py`: ലളിതമായ രജിസ്ട്രി மற்றும் ഹ്യൂറിസ്റ്റിക് റൂട്ടിംഗ്; എന്റ്പോയിന്റ് കണ്ടെത്തൽ + ഹെൽത്ത് ചെക്ക്.

## റൺ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## കുറിപ്പുകൾ
- റൂട്ടർ ലളിതമായ കീവേഡ് ഹ്യൂറിസ്റ്റിക്സ് ഉപയോഗിച്ച് `general`, `reasoning`, `code` ടൂളുകൾക്കിടയിൽ തിരഞ്ഞെടുക്കുന്നു, ആരംഭത്തിൽ `/v1/models` പ്രിന്റ് ചെയ്യുന്നു.
- പരിസ്ഥിതി വേരിയബിളുകൾ വഴി കോൺഫിഗർ ചെയ്യുക:
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

## റഫറൻസുകൾ
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ഇൻഫറൻസ് SDK-കളുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുക: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->