<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a52481fe75c7692d785aef8da50e5e7",
  "translation_date": "2025-12-15T21:08:59+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_QUICKREF.md",
  "language_code": "ml"
}
-->
# Foundry Local SDK - ക്വിക്ക് റഫറൻസ്

## ഇൻസ്റ്റലേഷൻ

```bash
# SDK ഇൻസ്റ്റാൾ ചെയ്യുക
pip install foundry-local-sdk openai

# Foundry Local സേവനം ഇൻസ്റ്റാൾ ചെയ്യുക
# വിൻഡോസ്
winget install Microsoft.FoundryLocal

# മാക്‌ഓഎസ്
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## സർവീസ് മാനേജ്മെന്റ്

```bash
# സേവനം ആരംഭിക്കുക
foundry service start

# നില പരിശോധിക്കുക
foundry service status

# സേവനം നിർത്തുക
foundry service stop

# മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model ls

# മോഡൽ ഡൗൺലോഡ് ചെയ്യുക
foundry model download phi-4-mini

# മോഡൽ വിവരങ്ങൾ നേടുക
foundry model info phi-4-mini
```

## അടിസ്ഥാന ഉപയോഗ പാറ്റേൺ

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# മാനേജർ ആരംഭിക്കുക (ആവശ്യമായാൽ സർവീസ് ആരംഭിക്കും)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# OpenAI-സമാനമായ ക്ലയന്റ് സൃഷ്ടിക്കുക
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# മോഡൽ ഐഡി നേടുക
model_id = manager.get_model_info(alias).id

# ചാറ്റ് പൂർത്തീകരണം
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## സ്ട്രീമിംഗ് പ്രതികരണം

```python
stream = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## വർക്‌ഷോപ്പ് ഉപകരണങ്ങൾ (സരളീകരിച്ചത്)

```python
from workshop_utils import chat_once

# കാഷിംഗ് மற்றும் റിട്രൈയുമായി ഒറ്റ കോൾ
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## പരിസ്ഥിതി വേരിയബിളുകൾ

```python
import os

# ടോക്കൺ ഉപയോഗം കാണിക്കുക
os.environ['SHOW_USAGE'] = '1'

# പുനരായാസം സജ്ജമാക്കുക
os.environ['RETRY_ON_FAIL'] = '1'

# പുനരായാസം വൈകിപ്പ് സജ്ജമാക്കുക
os.environ['RETRY_BACKOFF'] = '2.0'

# ഇഷ്ടാനുസൃത എന്റ്പോയിന്റ്
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## സാധാരണ മോഡൽ അലിയാസുകൾ

| അലിയാസ് | വലുപ്പം | ഏറ്റവും അനുയോജ്യം |
|-------|------|----------|
| `phi-4-mini` | ~4B | പൊതുവായി, സംഗ്രഹം |
| `phi-3.5-mini` | ~3.5B | കോഡ്, പുനഃസംഘടനം |
| `qwen2.5-0.5b` | ~0.5B | വേഗത്തിലുള്ള വർഗ്ഗീകരണം |
| `qwen2.5-coder-0.5b` | ~0.5B | കോഡ് സൃഷ്ടി |
| `gemma-2b` | ~2B | സൃഷ്ടിപരമായ എഴുത്ത് |

## പിശക് കൈകാര്യം ചെയ്യൽ

```python
from openai import OpenAIError

try:
    text, usage = chat_once('phi-4-mini', messages=[...])
except RuntimeError as e:
    print(f"Manager initialization failed: {e}")
    print("Check: foundry service status")
except OpenAIError as e:
    print(f"API call failed: {e}")
    print("Check: foundry model ls")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## പ്രശ്നപരിഹാരം

### കണക്ഷൻ പിശക്
```bash
# സേവനം പരിശോധിക്കുക
foundry service status

# പുനരാരംഭിക്കുക
foundry service stop
foundry service start

# എൻഡ്‌പോയിന്റ് പരിശോധന നടത്തുക
curl http://localhost:55769/health
```

### മോഡൽ കണ്ടെത്തിയില്ല
```bash
# ലഭ്യമായ ലിസ്റ്റ്
foundry model ls

# ആവശ്യമെങ്കിൽ ഡൗൺലോഡ് ചെയ്യുക
foundry model download phi-4-mini
```

### ഇറക്കുമതി പിശക്
```bash
# SDK പുനഃസ്ഥാപിക്കുക
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## ഉയർന്ന തലത്തിൽ: ബഹുമുഖ മോഡലുകൾ

```python
from workshop_utils import get_client

# പല മോഡലുകളും ആരംഭിക്കുക
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# വ്യത്യസ്ത മോഡലുകൾ ഉപയോഗിക്കുക
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## പ്രകടന ടിപ്പുകൾ

1. **കാഷെ ക്ലയന്റുകൾ**: `FoundryLocalManager` ഉദാഹരണങ്ങൾ പുനരുപയോഗിക്കുക
2. **ബാച്ച് അഭ്യർത്ഥനകൾ**: ഒന്നിലധികം പ്രോംപ്റ്റുകൾ ക്രമമായി പ്രോസസ്സ് ചെയ്യുക
3. **max_tokens ക്രമീകരിക്കുക**: കുറവായാൽ വേഗത്തിലുള്ള പ്രതികരണങ്ങൾ
4. **മോഡലുകൾ മുൻകൂട്ടി ലോഡ് ചെയ്യുക**: ഉത്പാദന ഉപയോഗത്തിന് മുമ്പ് ഡൗൺലോഡ് ചെയ്യുക
5. **ഉപയോഗം നിരീക്ഷിക്കുക**: `SHOW_USAGE=1` ഉപയോഗിച്ച് ടോക്കണുകൾ ട്രാക്ക് ചെയ്യുക

## വിഭവങ്ങൾ

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**ക്വിക്ക് സ്റ്റാർട്ട്:**
```bash
# എല്ലാം ഇൻസ്റ്റാൾ ചെയ്യുക
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# സർവീസ് ആരംഭിക്കുക
foundry service start

# പൈത്തണിൽ പരീക്ഷിക്കുക
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->