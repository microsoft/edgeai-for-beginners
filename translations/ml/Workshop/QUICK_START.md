<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-12-15T20:33:52+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ml"
}
-->
# വർക്‌ഷോപ്പ് ക്വിക്ക് സ്റ്റാർട്ട് ഗൈഡ്

## മുൻ‌വശം ആവശ്യങ്ങൾ

### 1. ഫൗണ്ട്രി ലോക്കൽ ഇൻസ്റ്റാൾ ചെയ്യുക

അധികൃത ഇൻസ്റ്റലേഷൻ ഗൈഡ് പിന്തുടരുക:  
https://github.com/microsoft/Foundry-Local

```bash
# ഫൗണ്ട്രി ലോക്കൽ സർവീസ് ആരംഭിക്കുക
foundry service start

# ഒരു മോഡൽ ലോഡ് ചെയ്യുക (വർക്ക്‌ഷോപ്പിനായി phi-4-mini ശുപാർശ ചെയ്യുന്നു)
foundry model run phi-4-mini

# സർവീസ് പ്രവർത്തിക്കുന്നുണ്ടെന്ന് സ്ഥിരീകരിക്കുക
foundry service status
```

### 2. പൈത്തൺ ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

വർക്‌ഷോപ്പ് ഡയറക്ടറിയിൽ നിന്ന്:

```bash
# വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക (ശുപാർശ ചെയ്യുന്നു)
python -m venv .venv

# വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കുക
# വിൻഡോസ്:
.venv\Scripts\activate
# മാക്‌ഓഎസ്/ലിനക്സ്:
source .venv/bin/activate

# ആവശ്യകതകൾ ഇൻസ്റ്റാൾ ചെയ്യുക
pip install -r requirements.txt
```

## വർക്‌ഷോപ്പ് സാമ്പിളുകൾ പ്രവർത്തിപ്പിക്കൽ

### സെഷൻ 01: അടിസ്ഥാന ചാറ്റ്

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**പരിസ്ഥിതി വേരിയബിളുകൾ:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### സെഷൻ 02: RAG പൈപ്പ്‌ലൈൻ

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**പരിസ്ഥിതി വേരിയബിളുകൾ:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### സെഷൻ 02: RAG മൂല്യനിർണ്ണയം (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**കുറിപ്പ്**: `requirements.txt` വഴി അധിക ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യേണ്ടതാണ്

### സെഷൻ 03: ബെഞ്ച്മാർക്കിംഗ്

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**പരിസ്ഥിതി വേരിയബിളുകൾ:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**ഔട്ട്പുട്ട്**: ലാറ്റൻസി, ത്രൂപുട്ട്, ആദ്യ ടോക്കൺ മെട്രിക്‌സ് എന്നിവയുള്ള JSON

### സെഷൻ 04: മോഡൽ താരതമ്യം

```bash
cd Workshop/samples
python -m session04.model_compare
```

**പരിസ്ഥിതി വേരിയബിളുകൾ:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### സെഷൻ 05: മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**പരിസ്ഥിതി വേരിയബിളുകൾ:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### സെഷൻ 06: മോഡൽ റൂട്ടർ

```bash
cd Workshop/samples
python -m session06.models_router
```

**പരീക്ഷണങ്ങൾ**: കോഡ്, സംഗ്രഹം, ക്ലാസിഫിക്കേഷൻ തുടങ്ങിയ പല ഉദ്ദേശ്യങ്ങളുള്ള റൂട്ടിംഗ് ലജിക്

### സെഷൻ 06: പൈപ്പ്‌ലൈൻ

```bash
python -m session06.models_pipeline
```

**സങ്കീർണ്ണമായ മൾട്ടി-സ്റ്റെപ്പ് പൈപ്പ്‌ലൈൻ** പ്ലാനിംഗ്, എക്സിക്യൂഷൻ, റിഫൈൻമെന്റ് എന്നിവയോടെ

## സ്ക്രിപ്റ്റുകൾ

### ബെഞ്ച്മാർക്ക് റിപ്പോർട്ട് എക്സ്പോർട്ട് ചെയ്യുക

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**ഔട്ട്പുട്ട്**: മാർക്ക്‌ഡൗൺ ടേബിൾ + JSON മെട്രിക്‌സ്

### മാർക്ക്‌ഡൗൺ CLI പാറ്റേണുകൾ ലിന്റ് ചെയ്യുക

```bash
python lint_markdown_cli.py --verbose
```

**ഉദ്ദേശ്യം**: ഡോക്യുമെന്റേഷനിൽ പഴയ CLI പാറ്റേണുകൾ കണ്ടെത്തുക

## ടെസ്റ്റിംഗ്

### സ്മോക്ക് ടെസ്റ്റുകൾ

```bash
cd Workshop
python -m tests.smoke
```

**ടെസ്റ്റുകൾ**: പ്രധാന സാമ്പിളുകളുടെ അടിസ്ഥാന പ്രവർത്തനം

## പ്രശ്‌നപരിഹാരം

### സർവീസ് പ്രവർത്തിക്കുന്നില്ല

```bash
# നില പരിശോധിക്കുക
foundry service status

# പ്രവർത്തനരഹിതമായാൽ ആരംഭിക്കുക
foundry service start

# ഒരു മോഡൽ ലോഡ് ചെയ്യുക
foundry model run phi-4-mini
```

### മോഡ്യൂൾ ഇംപോർട്ട് പിശകുകൾ

```bash
# വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കിയിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക
.venv\Scripts\activate  # വിൻഡോസ്
source .venv/bin/activate  # മാക്‌ഒഎസ്/ലിനക്സ്

# ആശ്രിതങ്ങൾ പുനഃസ്ഥാപിക്കുക
pip install -r requirements.txt
```

### കണക്ഷൻ പിശകുകൾ

```bash
# എന്റ്പോയിന്റ് പരിശോധിക്കുക
foundry service status

# ആവശ്യമെങ്കിൽ വ്യക്തമായ എന്റ്പോയിന്റ് സജ്ജമാക്കുക
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### മോഡൽ കണ്ടെത്താനായില്ല

```bash
# ലഭ്യമായ മോഡലുകൾ പട്ടികപ്പെടുത്തുക
foundry model list

# ഒരു മോഡൽ ഡൗൺലോഡ് ചെയ്ത് പ്രവർത്തിപ്പിക്കുക
foundry model run phi-4-mini
```

## പരിസ്ഥിതി വേരിയബിൾ റഫറൻസ്

### കോർ കോൺഫിഗറേഷൻ
| വേരിയബിൾ | ഡിഫോൾട്ട് | വിവരണം |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | വ്യത്യസ്തം | ഉപയോഗിക്കാനുള്ള മോഡൽ അലിയാസ് |
| `FOUNDRY_LOCAL_ENDPOINT` | ഓട്ടോ | സർവീസ് എൻഡ്‌പോയിന്റ് ഓവർറൈഡ് ചെയ്യുക |
| `SHOW_USAGE` | `0` | ടോക്കൺ ഉപയോഗം കാണിക്കുക |
| `RETRY_ON_FAIL` | `1` | റിട്രൈ ലജിക് സജീവമാക്കുക |
| `RETRY_BACKOFF` | `1.0` | പ്രാഥമിക റിട്രൈ വൈകിപ്പ് (സെക്കൻഡ്) |

### സെഷൻ-സ്പെസിഫിക്
| വേരിയബിൾ | ഡിഫോൾട്ട് | വിവരണം |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | എംബെഡ്ഡിംഗ് മോഡൽ |
| `RAG_QUESTION` | സാമ്പിൾ കാണുക | RAG ടെസ്റ്റ് ചോദ്യങ്ങൾ |
| `BENCH_MODELS` | വ്യത്യസ്തം | കോമാ വേർതിരിച്ച മോഡലുകൾ |
| `BENCH_ROUNDS` | `3` | ബെഞ്ച്മാർക്ക് ആവർത്തനങ്ങൾ |
| `BENCH_PROMPT` | സാമ്പിൾ കാണുക | ബെഞ്ച്മാർക്ക് പ്രോംപ്റ്റ് |
| `BENCH_STREAM` | `0` | ആദ്യ ടോക്കൺ ലാറ്റൻസി അളക്കുക |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | പ്രൈമറി ഏജന്റ് മോഡൽ |
| `AGENT_MODEL_EDITOR` | പ്രൈമറി | എഡിറ്റർ ഏജന്റ് മോഡൽ |
| `SLM_ALIAS` | `phi-4-mini` | ചെറിയ ഭാഷാ മോഡൽ |
| `LLM_ALIAS` | `qwen2.5-7b` | വലിയ ഭാഷാ മോഡൽ |
| `COMPARE_PROMPT` | സാമ്പിൾ കാണുക | താരതമ്യ പ്രോംപ്റ്റ് |

## ശുപാർശ ചെയ്ത മോഡലുകൾ

### ഡെവലപ്പ്മെന്റ് & ടെസ്റ്റിംഗ്
- **phi-4-mini** - ഗുണനിലവാരവും വേഗവും സമതുലിതം
- **qwen2.5-0.5b** - ക്ലാസിഫിക്കേഷനിൽ വളരെ വേഗം
- **gemma-2-2b** - നല്ല ഗുണനിലവാരം, മിതമായ വേഗം

### പ്രൊഡക്ഷൻ സീനാരിയോകൾ
- **phi-4-mini** - പൊതുവായ ഉപയോഗം
- **deepseek-coder-1.3b** - കോഡ് ജനറേഷൻ
- **qwen2.5-7b** - ഉയർന്ന ഗുണനിലവാരമുള്ള പ്രതികരണങ്ങൾ

## SDK ഡോക്യുമെന്റേഷൻ

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## സഹായം നേടുക

1. സർവീസ് സ്റ്റാറ്റസ് പരിശോധിക്കുക: `foundry service status`  
2. ലോഗുകൾ കാണുക: ഫൗണ്ട്രി ലോക്കൽ സർവീസ് ലോഗുകൾ പരിശോധിക്കുക  
3. SDK ഡോക്യുമെന്റേഷൻ പരിശോധിക്കുക: https://github.com/microsoft/Foundry-Local  
4. സാമ്പിൾ കോഡ് അവലോകനം ചെയ്യുക: എല്ലാ സാമ്പിളുകൾക്കും വിശദമായ ഡോക്സ്ട്രിംഗ്‌സ് ഉണ്ട്

## അടുത്ത ഘട്ടങ്ങൾ

1. എല്ലാ വർക്‌ഷോപ്പ് സെഷനുകളും ക്രമത്തിൽ പൂർത്തിയാക്കുക  
2. വ്യത്യസ്ത മോഡലുകൾ പരീക്ഷിക്കുക  
3. നിങ്ങളുടെ ഉപയോഗത്തിനായി സാമ്പിളുകൾ മാറ്റി എഴുതുക

---

**അവസാനമായി അപ്ഡേറ്റ് ചെയ്തത്**: 2025-01-08  
**വർക്‌ഷോപ്പ് പതിപ്പ്**: ഏറ്റവും പുതിയത്  
**SDK**: ഫൗണ്ട്രി ലോക്കൽ പൈത്തൺ SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->