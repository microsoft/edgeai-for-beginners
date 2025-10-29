<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:39:34+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "my"
}
-->
# Workshop Samples - Foundry Local SDK Update အကျဉ်းချုပ်

## အကျဉ်းချုပ်

`Workshop/samples` ဖိုဒါထဲရှိ Python နမူနာအားလုံးကို Foundry Local SDK အကောင်းဆုံးအလေ့အကျင့်များနှင့်အညီ ပြင်ဆင်ပြီး workshop တစ်ခုလုံးတွင် တူညီမှုရှိစေရန် အာရုံစိုက်ထားပါသည်။

**ရက်စွဲ**: 2025 ခုနှစ် အောက်တိုဘာလ 8 ရက်  
**အကျယ်အဝန်း**: workshop အစည်းအဝေး ၆ ခုအတွင်း Python ဖိုင် ၉ ခု  
**အဓိကအာရုံစိုက်မှု**: အမှားကိုင်တွယ်မှု၊ documentation၊ SDK ပုံစံများ၊ အသုံးပြုသူအတွေ့အကြုံ

---

## ပြင်ဆင်ထားသော ဖိုင်များ

### Session 01: စတင်ခြင်း
- ✅ `chat_bootstrap.py` - Chat အခြေခံနှင့် streaming နမူနာများ

### Session 02: RAG Solutions
- ✅ `rag_pipeline.py` - Embeddings ဖြင့် RAG အကောင်အထည်ဖော်မှု
- ✅ `rag_eval_ragas.py` - RAGAS metrics ဖြင့် RAG အကဲဖြတ်မှု

### Session 03: Open Source Models
- ✅ `benchmark_oss_models.py` - Multi-model benchmarking

### Session 04: Cutting Edge Models
- ✅ `model_compare.py` - SLM နှင့် LLM နှိုင်းယှဉ်မှု

### Session 05: AI-Powered Agents
- ✅ `agents_orchestrator.py` - Multi-agent ကိုယ်စားလှယ်များကို စီမံခန့်ခွဲခြင်း

### Session 06: Models as Tools
- ✅ `models_router.py` - ရည်ရွယ်ချက်အခြေခံသော model routing
- ✅ `models_pipeline.py` - Multi-step routed pipeline

### Supporting Infrastructure
- ✅ `workshop_utils.py` - အကောင်းဆုံးအလေ့အကျင့်များကို အရင်ကတည်းက လိုက်နာထားပြီး (ပြင်ဆင်မှုမလိုအပ်ပါ)

---

## အဓိကတိုးတက်မှုများ

### 1. အမှားကိုင်တွယ်မှု တိုးတက်မှု

**အရင်**:  
```python
manager, client, model_id = get_client(alias)
```
  
**နောက်**:  
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**အကျိုးကျေးဇူးများ**:  
- အမှားကိုင်တွယ်မှုကို သေချာစွာလုပ်ဆောင်ခြင်း  
- အမှားများကိုရှင်းလင်းစွာ ဖော်ပြခြင်း  
- Script များအတွက် exit code များကို သေချာစွာထုတ်ပေးခြင်း  

### 2. Import စီမံခန့်ခွဲမှု တိုးတက်မှု

**အရင်**:  
```python
from sentence_transformers import SentenceTransformer
```
  
**နောက်**:  
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**အကျိုးကျေးဇူးများ**:  
- Dependency များမရှိပါက သေချာစွာအကြံပေးခြင်း  
- Import အမှားများကို ကာကွယ်ခြင်း  
- အသုံးပြုသူများအတွက် installation လမ်းညွှန်ချက်များပေးခြင်း  

### 3. Documentation အပြည့်အစုံ

**နမူနာအားလုံးတွင် ထည့်သွင်းထားသည်**:  
- Environment variable documentation ကို docstrings တွင်ထည့်သွင်းထားသည်  
- SDK ကိုရည်ညွှန်းသော link များ  
- အသုံးပြုမှုနမူနာများ  
- Function/parameter documentation အသေးစိတ်  
- IDE အထောက်အကူပြုသော type hints  

**နမူနာ**:  
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```
  

### 4. အသုံးပြုသူအကြောင်းပြန်သတင်းပို့မှု တိုးတက်မှု

**သတင်းပို့မှုများ ထည့်သွင်းထားသည်**:  
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**တိုးတက်မှုအညွှန်းများ**:  
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**ဖွဲ့စည်းထားသော output**:  
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Benchmarking တိုးတက်မှု

**Session 03 တိုးတက်မှုများ**:  
- Model တစ်ခုချင်းစီအမှားကိုင်တွယ်မှု (အမှားဖြစ်ပျက်လျှင် ဆက်လက်လုပ်ဆောင်နိုင်သည်)  
- တိုးတက်မှုအခြေအနေကို အသေးစိတ်ဖော်ပြခြင်း  
- Warmup round များကို သေချာစွာလုပ်ဆောင်ခြင်း  
- First-token latency ကိုတိုင်းတာနိုင်မှု  
- အဆင့်များကို သေချာစွာခွဲခြားထားခြင်း  

### 6. Type Hints တူညီမှု

**အတစ်လျှောက်လုံး ထည့်သွင်းထားသည်**:  
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**အကျိုးကျေးဇူးများ**:  
- IDE autocomplete ကိုပိုမိုကောင်းမွန်စေခြင်း  
- အမှားများကိုစောစောမတိုင်မီ ရှာဖွေတွေ့ရှိနိုင်ခြင်း  
- ကိုယ်တိုင်ကိုယ်တိုင် documentation ဖြစ်စေခြင်း  

### 7. Model Router တိုးတက်မှု

**Session 06 တိုးတက်မှုများ**:  
- ရည်ရွယ်ချက်ကိုသေချာစွာဖော်ပြထားသော documentation  
- Model ရွေးချယ်မှု algorithm ရှင်းလင်းချက်  
- Routing log အသေးစိတ်  
- Test output formatting  
- Batch testing တွင် အမှားပြန်လည်ထိန်းသိမ်းမှု  

### 8. Multi-Agent Orchestration

**Session 05 တိုးတက်မှုများ**:  
- အဆင့်တစ်ခုချင်းစီအခြေအနေကို ဖော်ပြခြင်း  
- Agent တစ်ခုချင်းစီအမှားကိုင်တွယ်မှု  
- Pipeline ဖွဲ့စည်းမှုကို သေချာစွာဖော်ပြခြင်း  
- Memory management documentation ကိုပိုမိုကောင်းမွန်စေခြင်း  

---

## စမ်းသပ်မှု စစ်ဆေးရန်စာရင်း

### လိုအပ်ချက်များ  
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### နမူနာတစ်ခုချင်းစီကို စမ်းသပ်ပါ  

#### Session 01  
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```
  
#### Session 02  
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```
  
#### Session 03  
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```
  
#### Session 04  
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```
  
#### Session 05  
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```
  
#### Session 06  
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```
  

---

## Environment Variables ရည်ညွှန်းချက်

### Global (နမူနာအားလုံးအတွက်)
| Variable | ဖော်ပြချက် | ပုံမှန် |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | အသုံးပြုမည့် Model alias | နမူနာအလိုက် မတူညီပါသည် |
| `FOUNDRY_LOCAL_ENDPOINT` | Service endpoint ကို override လုပ်ရန် | Auto-detected |
| `SHOW_USAGE` | Token အသုံးပြုမှုကို ဖော်ပြရန် | `0` |
| `RETRY_ON_FAIL` | Retry logic ကိုဖွင့်ရန် | `1` |
| `RETRY_BACKOFF` | Retry အချိန်နှောင့်နှေးမှု | `1.0` |

### နမူနာအလိုက်
| Variable | အသုံးပြုသူ | ဖော်ပြချက် |
|----------|---------|-------------|
| `EMBED_MODEL` | Session 02 | Embedding model အမည် |
| `RAG_QUESTION` | Session 02 | RAG အတွက် စမ်းသပ်မေးခွန်း |
| `BENCH_MODELS` | Session 03 | Benchmark လုပ်ရန် model များ (comma-separated) |
| `BENCH_ROUNDS` | Session 03 | Benchmark round အရေအတွက် |
| `BENCH_PROMPT` | Session 03 | Benchmark အတွက် စမ်းသပ် prompt |
| `BENCH_STREAM` | Session 03 | First-token latency ကိုတိုင်းတာရန် |
| `SLM_ALIAS` | Session 04 | Small language model |
| `LLM_ALIAS` | Session 04 | Large language model |
| `COMPARE_PROMPT` | Session 04 | နှိုင်းယှဉ်မှု စမ်းသပ် prompt |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primary agent model |
| `AGENT_MODEL_EDITOR` | Session 05 | Editor agent model |
| `AGENT_QUESTION` | Session 05 | Agent များအတွက် စမ်းသပ်မေးခွန်း |
| `PIPELINE_TASK` | Session 06 | Pipeline အတွက် Task |

---

## Breaking Changes

**မရှိပါ** - ပြင်ဆင်မှုအားလုံးသည် အတိတ်နှင့်အညီအတိုင်း လိုက်ဖက်မှုရှိသည်။

ရရှိပြီးသား script များသည် ဆက်လက်အလုပ်လုပ်နိုင်ပါသည်။ အသစ်ထည့်သွင်းထားသောအင်္ဂါရပ်များမှာ:  
- Optional environment variables  
- အမှားများကိုပိုမိုရှင်းလင်းစွာဖော်ပြခြင်း (လုပ်ဆောင်မှုကိုမဖျက်ဆီးပါ)  
- ထပ်ဆင့် logging (ပိတ်ထားနိုင်သည်)  
- Type hints တိုးတက်မှု (runtime အပေါ်သက်ရောက်မှုမရှိပါ)  

---

## အကောင်းဆုံးအလေ့အကျင့်များ

### 1. Workshop Utils ကို အမြဲအသုံးပြုပါ  
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. အမှားကိုင်တွယ်မှု ပုံစံကို သေချာစွာလိုက်နာပါ  
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. သတင်းပို့မှုများကို သတိရဖွယ်ရှိစေပါ  
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Type Hints  
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Docstrings အပြည့်အစုံ  
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```
  
### 6. Environment Variable အထောက်အပံ့  
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Graceful Degradation  
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```
  

---

## အများဆုံးဖြစ်နိုင်သော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### ပြဿနာ: Import အမှားများ  
**ဖြေရှင်းနည်း**: လိုအပ်သော dependency များကို install လုပ်ပါ  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### ပြဿနာ: Connection အမှားများ  
**ဖြေရှင်းနည်း**: Foundry Local ကို run လုပ်ထားကြောင်း သေချာစေပါ  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### ပြဿနာ: Model မတွေ့ပါ  
**ဖြေရှင်းနည်း**: ရရှိနိုင်သော model များကိုစစ်ဆေးပါ  
```bash
foundry model ls
foundry model download <alias>
```
  

### ပြဿနာ: အလုပ်လုပ်ဆောင်မှုနှေးကွေးမှု  
**ဖြေရှင်းနည်း**: Model များကိုသေးငယ်သော model များသို့ပြောင်းပါ သို့မဟုတ် parameter များကိုပြင်ဆင်ပါ  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## နောက်တစ်ဆင့်လုပ်ဆောင်ရန်

### 1. နမူနာအားလုံးကို စမ်းသပ်ပါ  
အထက်ပါ စမ်းသပ်မှု စစ်ဆေးရန်စာရင်းကို အသုံးပြု၍ နမူနာအားလုံးကို သေချာစွာစမ်းသပ်ပါ။

### 2. Documentation ကို ပြင်ဆင်ပါ  
- Session markdown ဖိုင်များကို နမူနာအသစ်များဖြင့် update လုပ်ပါ  
- Main README တွင် troubleshooting အပိုင်းကို ထည့်သွင်းပါ  
- Quick reference guide တစ်ခု ဖန်တီးပါ  

### 3. Integration Tests ဖန်တီးပါ  
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Performance Benchmarks ထည့်သွင်းပါ  
Error handling တိုးတက်မှုများမှ ရရှိသော performance တိုးတက်မှုများကို စစ်ဆေးပါ။

### 5. အသုံးပြုသူအကြောင်းပြန်သတင်း  
Workshop ပါဝင်သူများထံမှ အောက်ပါအကြောင်းအရာများအပေါ် feedback ရယူပါ:  
- အမှား message ရှင်းလင်းမှု  
- Documentation အပြည့်အစုံ  
- အသုံးပြုရလွယ်ကူမှု  

---

## Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Main Repository**: https://github.com/microsoft/Foundry-Local  

---

## Maintenance

### နမူနာအသစ်များ ထည့်သွင်းခြင်း  
နမူနာအသစ်များဖန်တီးသောအခါ အောက်ပါပုံစံများကိုလိုက်နာပါ:  

1. `workshop_utils` ကို client စီမံခန့်ခွဲမှုအတွက် အသုံးပြုပါ  
2. အမှားကိုင်တွယ်မှုကို အပြည့်အဝထည့်သွင်းပါ  
3. Environment variable အထောက်အပံ့ကို ထည့်သွင်းပါ  
4. Type hints နှင့် docstrings ကို ထည့်သွင်းပါ  
5. သတင်းပို့မှုများကို သတိရဖွယ်ရှိစေပါ  
6. Docstring တွင် အသုံးပြုမှုနမူနာများကို ထည့်သွင်းပါ  
7. SDK documentation ကိုရည်ညွှန်းပါ  

### ပြင်ဆင်မှုများကို ပြန်လည်သုံးသပ်ခြင်း  
နမူနာပြင်ဆင်မှုများကို ပြန်လည်သုံးသပ်သောအခါ အောက်ပါအချက်များကို စစ်ဆေးပါ:  
- [ ] I/O လုပ်ဆောင်မှုအားလုံးတွင် အမှားကိုင်တွယ်မှု  
- [ ] Public function များတွင် Type hints  
- [ ] Docstrings အပြည့်အစုံ  
- [ ] Environment variable documentation  
- [ ] အသုံးပြုသူအတွက် သတင်းပို့မှုများ  
- [ ] SDK ကိုရည်ညွှန်းသော link များ  
- [ ] Code style တူညီမှု  

---

**အကျဉ်းချုပ်**: Workshop Python နမူနာအားလုံးသည် Foundry Local SDK အကောင်းဆုံးအလေ့အကျင့်များကို လိုက်နာပြီး အမှားကိုင်တွယ်မှု၊ documentation အပြည့်အစုံနှင့် အသုံးပြုသူအတွေ့အကြုံကို တိုးတက်စေပါသည်။ Breaking changes မရှိပါ - ရရှိပြီးသားလုပ်ဆောင်မှုအားလုံးကို ထိန်းသိမ်းထားပြီး တိုးတက်မှုများကို ထည့်သွင်းထားပါသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။