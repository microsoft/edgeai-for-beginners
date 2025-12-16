<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba4a0e432e3b6bfed9026383b0b56cf4",
  "translation_date": "2025-12-15T20:19:37+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ml"
}
-->
# Windows & Mac-ൽ Foundry Local

Windows-ലും Mac-ലും Microsoft Foundry Local ഇൻസ്റ്റാൾ ചെയ്യാനും, പ്രവർത്തിപ്പിക്കാനും, സംയോജിപ്പിക്കാനും ഈ ഗൈഡ് സഹായിക്കുന്നു. എല്ലാ ഘട്ടങ്ങളും കമാൻഡുകളും Microsoft Learn ഡോക്യുമെന്റേഷനുമായി സ്ഥിരീകരിച്ചവയാണ്.

- ആരംഭിക്കുക: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ആർക്കിടെക്ചർ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI റഫറൻസ്: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKകൾ സംയോജിപ്പിക്കുക: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF മോഡലുകൾ കമ്പൈൽ ചെയ്യുക (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: ലോക്കൽ vs ക്ലൗഡ്: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows-ൽ ഇൻസ്റ്റാൾ / അപ്ഗ്രേഡ് ചെയ്യുക

- ഇൻസ്റ്റാൾ:
```cmd
winget install Microsoft.FoundryLocal
```
- അപ്ഗ്രേഡ്:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- വേർഷൻ പരിശോധിക്കുക:
```cmd
foundry --version
```
     
**ഇൻസ്റ്റാൾ / Mac**

**MacOS**: 
ഒരു ടെർമിനൽ തുറന്ന് താഴെ കാണുന്ന കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI അടിസ്ഥാനങ്ങൾ (മൂന്ന് വിഭാഗങ്ങൾ)

- മോഡൽ:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- സർവീസ്:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- കാഷെ:
```cmd
foundry cache --help
foundry cache list
```

കുറിപ്പുകൾ:
- സർവീസ് OpenAI-സമാനമായ REST API ഒരു എക്സ്പോസ് ചെയ്യുന്നു. എൻഡ്‌പോയിന്റ് പോർട്ട് ഡൈനാമിക് ആയി അനുവദിക്കപ്പെടുന്നു; കണ്ടെത്താൻ `foundry service status` ഉപയോഗിക്കുക.
- സൗകര്യത്തിനായി SDKകൾ ഉപയോഗിക്കുക; അവ പിന്തുണയ്ക്കുന്നിടത്ത് എൻഡ്‌പോയിന്റ് കണ്ടെത്തൽ സ്വയം കൈകാര്യം ചെയ്യും.

## 3) ലോക്കൽ എൻഡ്‌പോയിന്റ് കണ്ടെത്തുക (ഡൈനാമിക് പോർട്ട്)

Foundry Local സർവീസ് ആരംഭിക്കുമ്പോൾ ഓരോ തവണയും ഒരു ഡൈനാമിക് പോർട്ട് അനുവദിക്കുന്നു:
```cmd
foundry service status
```
റിപ്പോർട്ട് ചെയ്ത `http://localhost:<PORT>` OpenAI-സമാനമായ പാതകളുമായി (ഉദാഹരണത്തിന്, `/v1/chat/completions`) നിങ്ങളുടെ `base_url` ആയി ഉപയോഗിക്കുക.

## 4) OpenAI Python SDK വഴി ക്വിക്ക് ടെസ്റ്റ്

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
റഫറൻസുകൾ:
- SDK സംയോജനം: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Bring Your Own Model (Olive ഉപയോഗിച്ച് കമ്പൈൽ ചെയ്യുക)

കാറ്റലോഗിൽ ഇല്ലാത്ത മോഡൽ ആവശ്യമെങ്കിൽ, Olive ഉപയോഗിച്ച് Foundry Local-ക്കായി ONNX ആയി കമ്പൈൽ ചെയ്യുക.

ഉയർന്ന തലത്തിലുള്ള പ്രവാഹം (ഘട്ടങ്ങൾക്കായി ഡോക്യുമെന്റേഷൻ കാണുക):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ഡോക്സ്:
- BYOM കമ്പൈൽ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) പ്രശ്നപരിഹാരം

- സർവീസ് സ്റ്റാറ്റസ്, ലോഗുകൾ പരിശോധിക്കുക:
```cmd
foundry service status
foundry service diag
```
- കാഷെ ക്ലിയർ ചെയ്യുക അല്ലെങ്കിൽ മാറ്റുക:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- ഏറ്റവും പുതിയ പ്രിവ്യൂ അപ്ഡേറ്റ് ചെയ്യുക:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) ബന്ധപ്പെട്ട Windows ഡെവലപ്പർ അനുഭവം

- Windows ലോക്കൽ vs ക്ലൗഡ് AI തിരഞ്ഞെടുപ്പുകൾ, Foundry Local, Windows ML ഉൾപ്പെടെ:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI ടൂൾകിറ്റ് Foundry Local-നൊപ്പം (`foundry service status` ഉപയോഗിച്ച് ചാറ്റ് എൻഡ്‌പോയിന്റ് URL നേടുക):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[അടുത്ത Windows ഡെവലപ്പർ](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->