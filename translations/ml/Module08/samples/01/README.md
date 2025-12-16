<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fb649a75048715165e76e20b366620a9",
  "translation_date": "2025-12-16T00:38:50+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ml"
}
-->
# സാമ്പിൾ 01: OpenAI SDK വഴി വേഗത്തിലുള്ള ചാറ്റ്

പ്രാദേശിക AI ഇൻഫറൻസിനായി Microsoft Foundry Local ഉപയോഗിച്ച് OpenAI SDK എങ്ങനെ ഉപയോഗിക്കാമെന്ന് കാണിക്കുന്ന ഒരു ലളിതമായ ചാറ്റ് ഉദാഹരണം.

## അവലോകനം

ഈ സാമ്പിൾ കാണിക്കുന്നു:
- Foundry Local ഉപയോഗിച്ച് OpenAI Python SDK എങ്ങനെ ഉപയോഗിക്കാമെന്ന്
- Azure OpenAIയും പ്രാദേശിക Foundry കോൺഫിഗറേഷനുകളും എങ്ങനെ കൈകാര്യം ചെയ്യാമെന്ന്
- ശരിയായ പിശക് കൈകാര്യം ചെയ്യലും ഫാൾബാക്ക് തന്ത്രങ്ങളും എങ്ങനെ നടപ്പിലാക്കാമെന്ന്
- സർവീസ് മാനേജ്മെന്റിനായി FoundryLocalManager എങ്ങനെ ഉപയോഗിക്കാമെന്ന്

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- **Foundry Local**: ഇൻസ്റ്റാൾ ചെയ്ത് PATH-ൽ ലഭ്യമായിരിക്കണം
- **Python**: 3.8 അല്ലെങ്കിൽ അതിനുശേഷം
- **മോഡൽ**: Foundry Local-ൽ ലോഡ് ചെയ്ത മോഡൽ (ഉദാ., `phi-4-mini`)

## ഇൻസ്റ്റലേഷൻ

1. **Python പരിസ്ഥിതി സജ്ജമാക്കുക:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local സർവീസ് ആരംഭിച്ച് മോഡൽ ലോഡ് ചെയ്യുക:**
   ```cmd
   foundry model run phi-4-mini
   ```

## ഉപയോഗം

### Foundry Local (ഡീഫോൾട്ട്)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## കോഡ് സവിശേഷതകൾ

### FoundryLocalManager ഇന്റഗ്രേഷൻ

ശരിയായ സർവീസ് മാനേജ്മെന്റിനായി ഔദ്യോഗിക Foundry Local SDK ഉപയോഗിക്കുന്നു:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ഫൗണ്ട്രി ലോക്കൽ ആരംഭിക്കുക
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# OpenAI ക്ലയന്റ് ക്രമീകരിക്കുക
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### പിശക് കൈകാര്യം ചെയ്യൽ

മാനുവൽ കോൺഫിഗറേഷനിലേക്ക് ഫാൾബാക്ക് ഉള്ള ശക്തമായ പിശക് കൈകാര്യം ചെയ്യൽ:
- സ്വയം സർവീസ് കണ്ടെത്തൽ
- SDK ലഭ്യമല്ലെങ്കിൽ സുഖപ്രദമായ ഡിഗ്രേഡേഷൻ
- പ്രശ്നപരിഹാരത്തിനായി വ്യക്തമായ പിശക് സന്ദേശങ്ങൾ

## പരിസ്ഥിതി വ്യത്യാസങ്ങൾ

| വ്യത്യാസം | വിവരണം | ഡീഫോൾട്ട് | ആവശ്യമാണ് |
|----------|-------------|---------|----------|
| `MODEL` | മോഡൽ ആലിയാസ് അല്ലെങ്കിൽ പേര് | `phi-4-mini` | ഇല്ല |
| `BASE_URL` | Foundry Local അടിസ്ഥാന URL | `http://localhost:8000` | ഇല്ല |
| `API_KEY` | API കീ (സാധാരണ പ്രാദേശികത്തിന് ആവശ്യമില്ല) | `""` | ഇല്ല |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI എൻഡ്‌പോയിന്റ് | - | Azure-ക്കായി |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API കീ | - | Azure-ക്കായി |
| `AZURE_OPENAI_API_VERSION` | Azure API പതിപ്പ് | `2024-08-01-preview` | ഇല്ല |

## പ്രശ്നപരിഹാരം

### സാധാരണ പ്രശ്നങ്ങൾ

1. **"Foundry SDK ഉപയോഗിക്കാൻ കഴിഞ്ഞില്ല" മുന്നറിയിപ്പ്:**
   - foundry-local-sdk ഇൻസ്റ്റാൾ ചെയ്യുക: `pip install foundry-local-sdk`
   - അല്ലെങ്കിൽ മാനുവൽ കോൺഫിഗറേഷനായി പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സജ്ജമാക്കുക

2. **കണക്ഷൻ നിരസിച്ചു:**
   - Foundry Local പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക: `foundry service status`
   - മോഡൽ ലോഡ് ചെയ്തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക: `foundry service ps`

3. **മോഡൽ കണ്ടെത്താനായില്ല:**
   - ലഭ്യമായ മോഡലുകൾ പട്ടികപ്പെടുത്തുക: `foundry model list`
   - മോഡൽ ലോഡ് ചെയ്യുക: `foundry model run phi-4-mini`

### സ്ഥിരീകരണം

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## റഫറൻസുകൾ

- [Foundry Local ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-സഹജമായ API റഫറൻസ്](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->