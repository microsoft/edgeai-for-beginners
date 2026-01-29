# സാമ്പിൾ 02: OpenAI SDK ഇന്റഗ്രേഷൻ

OpenAI Python SDK-യുമായി ആധുനിക ഇന്റഗ്രേഷൻ പ്രദർശിപ്പിക്കുന്നു, Microsoft Foundry Local-നും Azure OpenAI-നും സ്ട്രീമിംഗ് പ്രതികരണങ്ങളോടും ശരിയായ പിശക് കൈകാര്യം ചെയ്യലോടും പിന്തുണ നൽകുന്നു.

## അവലോകനം

ഈ സാമ്പിൾ കാണിക്കുന്നു:
- Foundry Local-നും Azure OpenAI-നും ഇടയിൽ സുതാര്യമായ സ്വിച്ച് ചെയ്യൽ
- മെച്ചപ്പെട്ട ഉപയോക്തൃ അനുഭവത്തിനായി സ്ട്രീമിംഗ് ചാറ്റ് പൂർത്തീകരണങ്ങൾ
- FoundryLocalManager SDK-യുടെ ശരിയായ ഉപയോഗം
- ശക്തമായ പിശക് കൈകാര്യം ചെയ്യലും ഫാൾബാക്ക് മെക്കാനിസങ്ങളുമാണ്
- പ്രൊഡക്ഷൻ-സജ്ജമായ കോഡ് മാതൃകകൾ

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- **Foundry Local**: ഇൻസ്റ്റാൾ ചെയ്ത് പ്രവർത്തനക്ഷമമാക്കി (ലോകൽ ഇൻഫറൻസ്‌ക്കായി)
- **Python**: 3.8 അല്ലെങ്കിൽ അതിനുശേഷം OpenAI SDK-യോടുകൂടി
- **Azure OpenAI**: സാധുവായ എൻഡ്‌പോയിന്റും API കീയും (ക്ലൗഡ് ഇൻഫറൻസ്‌ക്കായി)

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

3. **Foundry Local ആരംഭിക്കുക (ലോകൽ മോഡിനായി):**
   ```cmd
   foundry model run phi-4-mini
   ```

## ഉപയോഗ സാഹചര്യങ്ങൾ

### Foundry Local (ഡീഫോൾട്ട്)

**ഓപ്ഷൻ 1: FoundryLocalManager ഉപയോഗിച്ച് (ശുപാർശ ചെയ്യുന്നു)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ഓപ്ഷൻ 2: മാനുവൽ കോൺഫിഗറേഷൻ**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```

## കോഡ് ആർക്കിടെക്ചർ

### ക്ലയന്റ് ഫാക്ടറി മാതൃക

സാമ്പിൾ അനുയോജ്യമായ ക്ലയന്റുകൾ സൃഷ്ടിക്കാൻ ഫാക്ടറി മാതൃക ഉപയോഗിക്കുന്നു:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```

### സ്ട്രീമിംഗ് പ്രതികരണങ്ങൾ

സാമ്പിൾ റിയൽ-ടൈം പ്രതികരണ സൃഷ്ടിക്കായി സ്ട്രീമിംഗ് പ്രദർശിപ്പിക്കുന്നു:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## പരിസ്ഥിതി വേരിയബിളുകൾ

### Foundry Local കോൺഫിഗറേഷൻ

| വേരിയബിള്‍ | വിവരണം | ഡീഫോൾട്ട് | ആവശ്യമാണ് |
|----------|-------------|---------|----------|
| `MODEL` | ഉപയോഗിക്കാനുള്ള മോഡൽ അലിയാസ് | `phi-4-mini` | ഇല്ല |
| `BASE_URL` | Foundry Local എൻഡ്‌പോയിന്റ് | `http://localhost:8000` | ഇല്ല |
| `API_KEY` | API കീ (ലോകലിന് ഓപ്ഷണൽ) | `""` | ഇല്ല |

### Azure OpenAI കോൺഫിഗറേഷൻ

| വേരിയബിള്‍ | വിവരണം | ഡീഫോൾട്ട് | ആവശ്യമാണ് |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI റിസോഴ്‌സ് എൻഡ്‌പോയിന്റ് | - | അത്യാവശ്യമാണ് |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API കീ | - | അത്യാവശ്യമാണ് |
| `AZURE_OPENAI_API_VERSION` | API പതിപ്പ് | `2024-08-01-preview` | ഇല്ല |
| `MODEL` | Azure ഡിപ്ലോയ്മെന്റ് പേര് | `your-deployment-name` | അത്യാവശ്യമാണ് |

## ആധുനിക സവിശേഷതകൾ

### ഓട്ടോമാറ്റിക് സർവീസ് കണ്ടെത്തൽ

പരിസ്ഥിതി വേരിയബിളുകളുടെ അടിസ്ഥാനത്തിൽ അനുയോജ്യമായ സർവീസ് സ്വയം കണ്ടെത്തുന്നു:

1. **Azure മോഡ്**: `AZURE_OPENAI_ENDPOINT`യും `AZURE_OPENAI_API_KEY`യും സജ്ജമെങ്കിൽ
2. **Foundry SDK മോഡ്**: Foundry Local SDK ലഭ്യമായാൽ
3. **മാനുവൽ മോഡ്**: മാനുവൽ കോൺഫിഗറേഷനിലേക്ക് ഫാൾബാക്ക്

### പിശക് കൈകാര്യം ചെയ്യൽ

- SDK-യിൽ നിന്ന് മാനുവൽ കോൺഫിഗറേഷനിലേക്ക് സുതാര്യമായ ഫാൾബാക്ക്
- പ്രശ്നപരിഹാരത്തിനായി വ്യക്തമായ പിശക് സന്ദേശങ്ങൾ
- നെറ്റ്‌വർക്ക് പ്രശ്നങ്ങൾക്ക് ശരിയായ എക്സെപ്ഷൻ കൈകാര്യം ചെയ്യൽ
- ആവശ്യമായ പരിസ്ഥിതി വേരിയബിളുകളുടെ സാധുത പരിശോധന

## പ്രകടന പരിഗണനകൾ

### ലോകൽ vs ക്ലൗഡ് ട്രേഡ്-ഓഫുകൾ

**Foundry Local ന്റെ ഗുണങ്ങൾ:**
- ✅ API ചെലവുകൾ ഇല്ല
- ✅ ഡാറ്റ സ്വകാര്യത (ഡാറ്റ ഉപകരണത്തിൽ നിന്ന് പുറത്തേക്ക് പോവില്ല)
- ✅ പിന്തുണയുള്ള മോഡലുകൾക്ക് കുറഞ്ഞ ലാറ്റൻസി
- ✅ ഓഫ്‌ലൈൻ പ്രവർത്തനം

**Azure OpenAI ന്റെ ഗുണങ്ങൾ:**
- ✅ ഏറ്റവും പുതിയ വലിയ മോഡലുകളിലേക്ക് ആക്‌സസ്
- ✅ ഉയർന്ന ത്രൂപുട്ട്
- ✅ ലോക്കൽ കംപ്യൂട്ട് ആവശ്യകതകളില്ല
- ✅ എന്റർപ്രൈസ്-ഗ്രേഡ് SLA

## പ്രശ്നപരിഹാരം

### സാധാരണ പ്രശ്നങ്ങൾ

1. **"Foundry SDK ഉപയോഗിക്കാൻ കഴിഞ്ഞില്ല" മുന്നറിയിപ്പ്:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure ഓതന്റിക്കേഷൻ പിശകുകൾ:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **മോഡൽ ലഭ്യമല്ല:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### ഹെൽത്ത് ചെക്കുകൾ

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## അടുത്ത ഘട്ടങ്ങൾ

- **സാമ്പിൾ 03**: മോഡൽ കണ്ടെത്തലും ബെഞ്ച്മാർക്കിംഗും
- **സാമ്പിൾ 04**: Chainlit RAG അപ്ലിക്കേഷൻ നിർമ്മാണം
- **സാമ്പിൾ 05**: മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ
- **സാമ്പിൾ 06**: മോഡലുകൾ-ആസ്-ടൂൾസ് റൂട്ടിംഗ്

## റഫറൻസുകൾ

- [Azure OpenAI ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK റഫറൻസ്](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ഡോക്യുമെന്റേഷൻ](https://github.com/openai/openai-python)
- [Streaming Completions ഗൈഡ്](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->