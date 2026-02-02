# പരിസ്ഥിതി കോൺഫിഗറേഷൻ ഗൈഡ്

## അവലോകനം

വർക്ക്ഷോപ്പ് സാമ്പിളുകൾ കോൺഫിഗറേഷനായി പരിസ്ഥിതി വേരിയബിളുകൾ ഉപയോഗിക്കുന്നു, റിപോസിറ്ററി റൂട്ടിലുള്ള `.env` ഫയലിൽ കേന്ദ്രീകൃതമാണ്. ഇത് കോഡ് മാറ്റാതെ എളുപ്പത്തിൽ ഇഷ്ടാനുസൃതമാക്കാൻ അനുവദിക്കുന്നു.

## ക്വിക്ക് സ്റ്റാർട്ട്

### 1. മുൻകൂർ ആവശ്യകതകൾ പരിശോധിക്കുക

```bash
# ഫൗണ്ട്രി ലോക്കൽ ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
foundry --version

# സർവീസ് പ്രവർത്തനക്ഷമമാണോ എന്ന് പരിശോധിക്കുക
foundry service status

# ഒരു മോഡൽ ലോഡ് ചെയ്യുക
foundry model run phi-4-mini
```

### 2. പരിസ്ഥിതി കോൺഫിഗർ ചെയ്യുക

`.env` ഫയൽ ഇതിനകം തന്നെ ബുദ്ധിമുട്ടില്ലാത്ത ഡിഫോൾട്ടുകളോടെ കോൺഫിഗർ ചെയ്തിട്ടുണ്ട്. അധികം ഉപയോക്താക്കൾക്ക് ഒന്നും മാറ്റേണ്ടതില്ല.

**ഐച്ഛികം**: ക്രമീകരണങ്ങൾ പരിശോധിച്ച് ഇഷ്ടാനുസൃതമാക്കുക:
```bash
# .env ഫയൽ എഡിറ്റ് ചെയ്യുക
notepad .env  # വിൻഡോസ്
nano .env     # മാക്‌ഒഎസ്/ലിനക്സ്
```

### 3. കോൺഫിഗറേഷൻ പ്രയോഗിക്കുക

**Python സ്ക്രിപ്റ്റുകൾക്കായി:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സ്വയം ലോഡ് ചെയ്യുന്നു
```

**നോട്ട്ബുക്കുകൾക്കായി:**
```python
# .env മാറ്റങ്ങൾക്കുശേഷം കർണൽ പുനരാരംഭിക്കുക
# സെല്ലുകൾ പ്രവർത്തിപ്പിക്കുമ്പോൾ വേരിയബിളുകൾ ലോഡ് ചെയ്യപ്പെടുന്നു
```

## പരിസ്ഥിതി വേരിയബിളുകൾ റഫറൻസ്

### കോർ കോൺഫിഗറേഷൻ

| വേരിയബിള്‍ | ഡിഫോൾട്ട് | വിവരണം |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | സാമ്പിളുകൾക്കുള്ള ഡിഫോൾട്ട് മോഡൽ |
| `FOUNDRY_LOCAL_ENDPOINT` | (ശൂന്യം) | സർവീസ് എൻഡ്‌പോയിന്റ് ഓവർറൈഡ് ചെയ്യുക |
| `PYTHONPATH` | വർക്ക്ഷോപ്പ് പാതകൾ | Python മോഡ്യൂൾ തിരയൽ പാത |

**FOUNDRY_LOCAL_ENDPOINT സെറ്റ് ചെയ്യേണ്ടപ്പോൾ:**
- റിമോട്ട് ഫൗണ്ട്രി ലോക്കൽ ഇൻസ്റ്റൻസ്
- കസ്റ്റം പോർട്ട് കോൺഫിഗറേഷൻ
- ഡെവലപ്പ്മെന്റ്/പ്രൊഡക്ഷൻ വേർതിരിവ്

**ഉദാഹരണം:**
```bash
# പ്രാദേശിക കസ്റ്റം പോർട്ട്
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# ദൂരസ്ഥ ഇൻസ്റ്റൻസ്
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### സെഷൻ-സ്പെസിഫിക് വേരിയബിളുകൾ

#### സെഷൻ 02: RAG പൈപ്പ്‌ലൈൻ
| വേരിയബിള്‍ | ഡിഫോൾട്ട് | ഉദ്ദേശ്യം |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | എംബെഡ്ഡിംഗ് മോഡൽ |
| `RAG_QUESTION` | മുൻകൂർ കോൺഫിഗർ ചെയ്തത് | ടെസ്റ്റ് ചോദ്യം |

#### സെഷൻ 03: ബെഞ്ച്മാർക്കിംഗ്
| വേരിയബിള്‍ | ഡിഫോൾട്ട് | ഉദ്ദേശ്യം |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | ബെഞ്ച്മാർക്ക് ചെയ്യാനുള്ള മോഡലുകൾ |
| `BENCH_ROUNDS` | `3` | ഓരോ മോഡലിനും ആവർത്തനങ്ങൾ |
| `BENCH_PROMPT` | മുൻകൂർ കോൺഫിഗർ ചെയ്തത് | ടെസ്റ്റ് പ്രോംപ്റ്റ് |
| `BENCH_STREAM` | `0` | ആദ്യ ടോക്കൺ ലാറ്റൻസി അളക്കുക |

#### സെഷൻ 04: മോഡൽ താരതമ്യം
| വേരിയബിള്‍ | ഡിഫോൾട്ട് | ഉദ്ദേശ്യം |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | ചെറിയ ഭാഷാ മോഡൽ |
| `LLM_ALIAS` | `qwen2.5-7b` | വലിയ ഭാഷാ മോഡൽ |
| `COMPARE_PROMPT` | മുൻകൂർ കോൺഫിഗർ ചെയ്തത് | താരതമ്യ പ്രോംപ്റ്റ് |
| `COMPARE_RETRIES` | `2` | റിട്രൈ ശ്രമങ്ങൾ |

#### സെഷൻ 05: മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ
| വേരിയബിള്‍ | ഡിഫോൾട്ട് | ഉദ്ദേശ്യം |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | റിസർച്ചർ ഏജന്റ് മോഡൽ |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | എഡിറ്റർ ഏജന്റ് മോഡൽ |
| `AGENT_QUESTION` | മുൻകൂർ കോൺഫിഗർ ചെയ്തത് | ടെസ്റ്റ് ചോദ്യം |

### വിശ്വാസ്യത കോൺഫിഗറേഷൻ

| വേരിയബിള്‍ | ഡിഫോൾട്ട് | ഉദ്ദേശ്യം |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | ടോക്കൺ ഉപയോഗം പ്രിന്റ് ചെയ്യുക |
| `RETRY_ON_FAIL` | `1` | റിട്രൈ ലജിക് സജീവമാക്കുക |
| `RETRY_BACKOFF` | `1.0` | റിട്രൈ വൈകിപ്പ് (സെക്കൻഡുകൾ) |

## സാധാരണ കോൺഫിഗറേഷനുകൾ

### ഡെവലപ്പ്മെന്റ് സെറ്റപ്പ് (വേഗത്തിലുള്ള ആവർത്തനം)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### പ്രൊഡക്ഷൻ സെറ്റപ്പ് (ഗുണനിലവാരത്തിൽ ശ്രദ്ധ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### ബെഞ്ച്മാർക്കിംഗ് സെറ്റപ്പ്
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### മൾട്ടി-ഏജന്റ് സ്പെഷ്യലൈസേഷൻ
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # ഗവേഷണത്തിനായി വേഗം
AGENT_MODEL_EDITOR=qwen2.5-7b         # എഡിറ്റിംഗിനായി ഗുണമേന്മ
```

### റിമോട്ട് ഡെവലപ്പ്മെന്റ്
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## ശുപാർശ ചെയ്ത മോഡലുകൾ

### ഉപയോഗകേസുകൾ പ്രകാരം

**സാധാരണ ഉപയോഗം:**
- `phi-4-mini` - സമതുലിത ഗുണനിലവാരവും വേഗവും

**വേഗത്തിലുള്ള പ്രതികരണങ്ങൾ:**
- `qwen2.5-0.5b` - വളരെ വേഗം, ക്ലാസിഫിക്കേഷനിന് നല്ലത്
- `phi-4-mini` - വേഗം കൂടാതെ നല്ല ഗുണനിലവാരം

**ഉയർന്ന ഗുണനിലവാരം:**
- `qwen2.5-7b` - മികച്ച ഗുണനിലവാരം, കൂടുതൽ റിസോഴ്‌സ് ഉപയോഗം
- `phi-4-mini` - നല്ല ഗുണനിലവാരം, കുറവ് റിസോഴ്‌സുകൾ

**കോഡ് ജനറേഷൻ:**
- `deepseek-coder-1.3b` - കോഡിനായി പ്രത്യേകിച്ചുള്ളത്
- `phi-4-mini` - പൊതുവായ കോഡിംഗ്

### റിസോഴ്‌സ് ലഭ്യത പ്രകാരം

**കുറഞ്ഞ റിസോഴ്‌സുകൾ (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**മധ്യസ്ഥ റിസോഴ്‌സുകൾ (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**ഉയർന്ന റിസോഴ്‌സുകൾ (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## ഉയർന്ന തലത്തിലുള്ള കോൺഫിഗറേഷൻ

### കസ്റ്റം എൻഡ്‌പോയിന്റുകൾ

```bash
# വികസന പരിസ്ഥിതി
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# സ്റ്റേജിംഗ് പരിസ്ഥിതി
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# ഉത്പാദന പരിസ്ഥിതി
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### താപനില & സാമ്പ്ലിംഗ് (കോഡിൽ ഓവർറൈഡ് ചെയ്യുക)

```python
# നിങ്ങളുടെ സ്ക്രിപ്റ്റുകളിലും/നോട്ട്ബുക്കുകളിലും
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI ഹൈബ്രിഡ് സെറ്റപ്പ്

```bash
# വികസനത്തിനായി ലോക്കൽ ഉപയോഗിക്കുക
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# പ്രൊഡക്ഷൻ ഫാൽബാക്കിനായി അസ്യൂർ കോൺഫിഗർ ചെയ്യുക
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## പ്രശ്നപരിഹാരം

### പരിസ്ഥിതി വേരിയബിളുകൾ ലോഡ് ചെയ്യാത്തത്

**ലക്ഷണങ്ങൾ:**
- സ്ക്രിപ്റ്റുകൾ തെറ്റായ മോഡലുകൾ ഉപയോഗിക്കുന്നു
- കണക്ഷൻ പിശകുകൾ
- വേരിയബിളുകൾ തിരിച്ചറിയപ്പെടുന്നില്ല

**പരിഹാരങ്ങൾ:**
```bash
# 1. റിപോസിറ്ററി റൂട്ടിൽ .env ഉണ്ടെന്ന് സ്ഥിരീകരിക്കുക
ls -la .env  # മാക്‌ഓഎസ്/ലിനക്സ്
dir .env     # വിൻഡോസ്

# 2. ഫയൽ .env.txt അല്ലെന്ന് പരിശോധിക്കുക (വിൻഡോസ്)
# മറഞ്ഞിരിക്കുന്ന എക്സ്റ്റൻഷൻ ഇല്ലെന്ന് ഉറപ്പാക്കുക

# 3. നോട്ട്‌ബുക്കുകൾക്കായി: കർണൽ റീസ്റ്റാർട്ട് ചെയ്യുക
# കർണൽ > റീസ്റ്റാർട്ട്

# 4. സ്ക്രിപ്റ്റുകൾക്കായി: പ്രവർത്തന ഡയറക്ടറി പരിശോധിക്കുക
pwd  # വർക്ക്ഷോപ്പ് അല്ലെങ്കിൽ റിപോസിറ്ററി റൂട്ടിൽ ആയിരിക്കണം
```

### സർവീസ് കണക്ഷൻ പ്രശ്നങ്ങൾ

**ലക്ഷണങ്ങൾ:**
- "Connection refused" പിശകുകൾ
- "Service not available"
- ടൈംഔട്ട് പിശകുകൾ

**പരിഹാരങ്ങൾ:**
```bash
# 1. സേവനത്തിന്റെ നില പരിശോധിക്കുക
foundry service status

# 2. പ്രവർത്തിക്കുന്നില്ലെങ്കിൽ ആരംഭിക്കുക
foundry service start

# 3. എന്റ്പോയിന്റ് സ്ഥിരീകരിക്കുക
# നില ഔട്ട്പുട്ടിൽ പോർട്ട് പരിശോധിക്കുക
foundry service status | grep "Port"

# 4. ആവശ്യമെങ്കിൽ .env അപ്ഡേറ്റ് ചെയ്യുക
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### മോഡൽ കണ്ടെത്താനാകാത്തത്

**ലക്ഷണങ്ങൾ:**
- "Model not found" പിശകുകൾ
- "Alias not recognized"

**പരിഹാരങ്ങൾ:**
```bash
# 1. ലഭ്യമായ മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model list

# 2. ആവശ്യമായ മോഡൽ ലോഡ് ചെയ്യുക
foundry model run phi-4-mini

# 3. ലഭ്യമായ മോഡലുമായി .env അപ്ഡേറ്റ് ചെയ്യുക
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ഇംപോർട്ട് പിശകുകൾ

**ലക്ഷണങ്ങൾ:**
- "Module not found" പിശകുകൾ

**പരിഹാരങ്ങൾ:**

```bash
# 1. വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കുക
.venv\Scripts\activate  # വിൻഡോസ്
source .venv/bin/activate  # മാക്‌ഒഎസ്/ലിനക്സ്

# 2. ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക
pip install -r requirements.txt
```

## ടെസ്റ്റിംഗ് കോൺഫിഗറേഷൻ

### പരിസ്ഥിതി ലോഡിംഗ് പരിശോധിക്കുക

```python
# ടെസ്റ്റ്_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### ഫൗണ്ട്രി ലോക്കൽ കണക്ഷൻ ടെസ്റ്റ് ചെയ്യുക

```python
# ടെസ്റ്റ്_കണക്ഷൻ.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ

### 1. രഹസ്യങ്ങൾ ഒരിക്കലും കമ്മിറ്റ് ചെയ്യരുത്

```bash
# .gitignore ഉൾപ്പെടുത്തേണ്ടത്:
.env
.env.local
*.key
```

### 2. വേർതിരിച്ച .env ഫയലുകൾ ഉപയോഗിക്കുക

```bash
.env              # ഡിഫോൾട്ട് കോൺഫിഗറേഷൻ
.env.local        # ലോക്കൽ ഓവർറൈഡുകൾ (ഗിറ്റ്‌ഇഗ്നോർഡ്)
.env.production   # പ്രൊഡക്ഷൻ കോൺഫിഗ് (സുരക്ഷിത സംഭരണം)
```

### 3. API കീകൾ റോട്ടേറ്റ് ചെയ്യുക

```bash
# Azure OpenAI അല്ലെങ്കിൽ മറ്റ് ക്ലൗഡ് സേവനങ്ങൾക്കായി
# കീകൾ নিয়മിതമായി മാറ്റി .env അപ്ഡേറ്റ് ചെയ്യുക
```

### 4. പരിസ്ഥിതി-സ്പെസിഫിക് കോൺഫിഗർ ഉപയോഗിക്കുക

```bash
# വികസനം
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# ഉത്പാദനം (രഹസ്യങ്ങൾ മാനേജ്മെന്റ് ഉപയോഗിക്കുക)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK ഡോക്യുമെന്റേഷൻ

- **പ്രധാന റിപോസിറ്ററി**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ഡോക്യുമെന്റേഷൻ**: ഏറ്റവും പുതിയതിനായി SDK റിപോസിറ്ററി പരിശോധിക്കുക

## അധിക വിഭവങ്ങൾ

- `QUICK_START.md` - ആരംഭ ഗൈഡ്
- `Workshop/samples/*/README.md` - സാമ്പിൾ-സ്പെസിഫിക് ഗൈഡുകൾ

---

**അവസാനമായി അപ്ഡേറ്റ് ചെയ്തത്**: 2025-01-08  
**വർഷൻ**: 2.0  
**SDK**: ഫൗണ്ട്രി ലോക്കൽ Python SDK (ഏറ്റവും പുതിയത്)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->