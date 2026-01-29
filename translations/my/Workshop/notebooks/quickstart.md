# Workshop Notebooks - အမြန်စတင်ရန်လမ်းညွှန်

## အကြောင်းအရာများ

- [လိုအပ်ချက်များ](../../../../Workshop/notebooks)
- [မူလတပ်ဆင်မှု](../../../../Workshop/notebooks)
- [Session 04: မော်ဒယ်နှိုင်းယှဉ်မှု](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent Orchestrator](../../../../Workshop/notebooks)
- [Session 06: Intent-Based Model Routing](../../../../Workshop/notebooks)
- [ပတ်ဝန်းကျင် Variables](../../../../Workshop/notebooks)
- [အများဆုံးအသုံးပြုသော Commands](../../../../Workshop/notebooks)

---

## လိုအပ်ချက်များ

### 1. Foundry Local ကိုတပ်ဆင်ပါ

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**တပ်ဆင်မှုကိုအတည်ပြုပါ:**
```bash
foundry --version
```

### 2. Python Dependencies ကိုတပ်ဆင်ပါ

```bash
cd Workshop
pip install -r requirements.txt
```

သို့မဟုတ် တစ်ခုချင်းစီတပ်ဆင်ပါ:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## မူလတပ်ဆင်မှု

### Foundry Local Service ကိုစတင်ပါ

**Notebook မည်သည့်အရာမဆိုမလုပ်မီလိုအပ်သည်:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

မျှော်မှန်းထားသော output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### မော်ဒယ်များကိုဒေါင်းလုဒ်လုပ်ပြီး Load လုပ်ပါ

Notebook များသည်အောက်ပါမော်ဒယ်များကို default အဖြစ်အသုံးပြုသည်:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### တပ်ဆင်မှုကိုအတည်ပြုပါ

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: မော်ဒယ်နှိုင်းယှဉ်မှု

### ရည်ရွယ်ချက်
Small Language Models (SLM) နှင့် Large Language Models (LLM) တို့၏ performance ကိုနှိုင်းယှဉ်ပါ။

### အမြန်တပ်ဆင်မှု

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Notebook ကို run လုပ်ခြင်း

1. **ဖွင့်ပါ** `session04_model_compare.ipynb` ကို VS Code သို့မဟုတ် Jupyter တွင်
2. **Kernel ကို restart လုပ်ပါ** (Kernel → Restart Kernel)
3. **Cell အားလုံးကိုအဆင့်လိုက် run လုပ်ပါ**

### အဓိက Configuration

**Default မော်ဒယ်များ:**
- **SLM:** `phi-4-mini` (~4GB RAM, ပိုမြန်)
- **LLM:** `qwen2.5-3b` (~3GB RAM, memory-optimized)

**Environment Variables (optional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### မျှော်မှန်းထားသော Output

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Customize လုပ်ခြင်း

**မော်ဒယ်များကိုအခြားအရာများအသုံးပြုပါ:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Custom prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Validation Checklist

- [ ] Cell 12 တွင်မှန်ကန်သောမော်ဒယ်များ (phi-4-mini, qwen2.5-3b) ပြပါ
- [ ] Cell 12 တွင်မှန်ကန်သော endpoint (port 59959) ပြပါ
- [ ] Cell 16 diagnostic pass (✅ Service is running)
- [ ] Cell 20 pre-flight check pass (မော်ဒယ်နှစ်ခုစလုံးအဆင်ပြေ)
- [ ] Cell 22 နှိုင်းယှဉ်မှုပြီးစီးပြီး latency values ပြပါ
- [ ] Cell 24 validation တွင် 🎉 ALL CHECKS PASSED! ပြပါ

### အချိန်ခန့်မှန်းချက်
- **ပထမဆုံး run:** 5-10 မိနစ် (မော်ဒယ်များကိုဒေါင်းလုဒ်လုပ်ခြင်းအပါအဝင်)
- **နောက်တစ်ကြိမ် run:** 1-2 မိနစ်

---

## Session 05: Multi-Agent Orchestrator

### ရည်ရွယ်ချက်
Foundry Local SDK ကိုအသုံးပြုပြီး Multi-Agent တွေကိုပေါင်းစည်းခြင်း - အေးဂျင့်များသည် output များကိုပိုမိုကောင်းမွန်အောင်လုပ်ဆောင်ပါသည်။

### အမြန်တပ်ဆင်မှု

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Notebook ကို run လုပ်ခြင်း

1. **ဖွင့်ပါ** `session05_agents_orchestrator.ipynb`
2. **Kernel ကို restart လုပ်ပါ**
3. **Cell အားလုံးကိုအဆင့်လိုက် run လုပ်ပါ**

### အဓိက Configuration

**Default Setup (အေးဂျင့်နှစ်ခုစလုံးအတွက်တူညီသောမော်ဒယ်):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Advanced Setup (မော်ဒယ်များကွဲပြားခြင်း):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architecture

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### မျှော်မှန်းထားသော Output

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Extensions

**အေးဂျင့်များကိုပိုမိုထည့်ပါ:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch testing:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### အချိန်ခန့်မှန်းချက်
- **ပထမ run:** 3-5 မိနစ်
- **နောက်တစ်ကြိမ် run:** မေးခွန်းတစ်ခုလျှင် 1-2 မိနစ်

---

## Session 06: Intent-Based Model Routing

### ရည်ရွယ်ချက်
Detected intent အပေါ်မူတည်ပြီး prompt များကိုအထူးပြုမော်ဒယ်များသို့အလိုအလျောက်ပို့ခြင်း။

### အမြန်တပ်ဆင်မှု

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**မှတ်ချက်:** Session 06 သည် CPU မော်ဒယ်များကို default အဖြစ်အသုံးပြုသည်။

### Notebook ကို run လုပ်ခြင်း

1. **ဖွင့်ပါ** `session06_models_router.ipynb`
2. **Kernel ကို restart လုပ်ပါ**
3. **Cell အားလုံးကိုအဆင့်လိုက် run လုပ်ပါ

### အဓိက Configuration

**Default Catalog (CPU မော်ဒယ်များ):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternative (GPU မော်ဒယ်များ):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Intent Detection

Router သည် regex patterns ကိုအသုံးပြုပြီး intent ကို detect လုပ်သည်:

| Intent | Pattern ဥပမာများ | Routed To |
|--------|-----------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | အခြားအားလုံး | phi-4-mini-cpu |

### မျှော်မှန်းထားသော Output

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Customize လုပ်ခြင်း

**Custom intent ထည့်ပါ:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Token tracking ကို enable လုပ်ပါ:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPU မော်ဒယ်များသို့ပြောင်းခြင်း

8GB+ VRAM ရှိပါက:

1. **Cell #6** တွင် CPU catalog ကို comment out လုပ်ပါ
2. GPU catalog ကို uncomment လုပ်ပါ
3. GPU မော်ဒယ်များကို load လုပ်ပါ:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Kernel ကို restart လုပ်ပြီး notebook ကိုပြန် run လုပ်ပါ

### အချိန်ခန့်မှန်းချက်
- **ပထမ run:** 5-10 မိနစ် (မော်ဒယ်များကို load လုပ်ခြင်း)
- **နောက်တစ်ကြိမ် run:** စမ်းသပ်မှုတစ်ခုလျှင် 30-60 စက္ကန့်

---

## ပတ်ဝန်းကျင် Variables

### Global Configuration

Jupyter/VS Code ကိုစတင်မီ set လုပ်ပါ:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Notebook အတွင်း Configuration

Notebook မည်သည့်အရာမဆိုအစမှာ set လုပ်ပါ:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## အများဆုံးအသုံးပြုသော Commands

### Service Management

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Model Management

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Endpoint စမ်းသပ်ခြင်း

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Diagnostic Commands

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## အကောင်းဆုံးအကြံပြုချက်များ

### Notebook မည်သည့်အရာမဆိုစတင်မီ

1. **Service run လုပ်နေသည်ကိုစစ်ဆေးပါ:**
   ```bash
   foundry service status
   ```

2. **မော်ဒယ်များ load လုပ်ထားသည်ကိုအတည်ပြုပါ:**
   ```bash
   foundry model ls
   ```

3. **Notebook kernel ကို restart လုပ်ပါ** run ပြန်လုပ်မည်ဆိုပါက

4. **Output အားလုံးကိုရှင်းလင်းပါ** run အသစ်အတွက်

### Resource Management

1. **CPU မော်ဒယ်များကို default အဖြစ်အသုံးပြုပါ** compatibility အတွက်
2. **GPU မော်ဒယ်များသို့ပြောင်းပါ** 8GB+ VRAM ရှိပါကသာ
3. **GPU application အခြားများကိုပိတ်ပါ** run မလုပ်မီ
4. **Service ကို run လုပ်နေပါစေ** notebook session များအကြား
5. **Resource usage ကိုစောင့်ကြည့်ပါ** Task Manager / nvidia-smi ဖြင့်

### Troubleshooting

1. **Code ကို debug မလုပ်မီ service ကိုစစ်ဆေးပါ**
2. **Stale configuration တွေ့ပါက kernel ကို restart လုပ်ပါ**
3. **Cell diagnostic များကိုပြန် run လုပ်ပါ** ပြောင်းလဲမှုများအပြီး
4. **မော်ဒယ်အမည်များကိုစစ်ဆေးပါ** load လုပ်ထားသောအရာနှင့်ကိုက်ညီမှုရှိသည်ကို
5. **Endpoint port ကိုစစ်ဆေးပါ** service status နှင့်ကိုက်ညီမှုရှိသည်ကို

---

## အမြန်ရယူရန်: Model Aliases

### အများဆုံးအသုံးပြုသောမော်ဒယ်များ

| Alias | Size | အကောင်းဆုံးအသုံးပြုမှု | RAM/VRAM | Variants |
|-------|------|----------------|----------|----------|
| `phi-4-mini` | ~4B | General chat, summarization | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Code generation, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | General tasks, efficient | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Fast, low resource | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classification, minimal resource | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variant Naming

- **Base name** (ဥပမာ `phi-4-mini`): Hardware အတွက်အကောင်းဆုံး variant ကို auto-select လုပ်သည်
- **`-cpu`**: CPU-optimized, မည်သည့်နေရာတွင်မဆိုအလုပ်လုပ်သည်
- **`-cuda-gpu`**: NVIDIA GPU optimized, 8GB+ VRAM လိုအပ်သည်
- **`-npu`**: Qualcomm NPU optimized, NPU drivers လိုအပ်သည်

**အကြံပြုချက်:** Base name များ (suffix မပါ) ကိုအသုံးပြုပြီး Foundry Local ကိုအကောင်းဆုံး variant ကို auto-select လုပ်ပါ။

---

## အောင်မြင်မှုအညွှန်းများ

သင်အဆင်သင့်ဖြစ်နေပြီဆိုပါက:

✅ `foundry service status` တွင် "running" ပြပါ
✅ `foundry model ls` တွင်လိုအပ်သောမော်ဒယ်များပြပါ
✅ Service သည်မှန်ကန်သော endpoint တွင်ရရှိနိုင်ပါသည်
✅ Health check သည် 200 OK ပြန်ပေးပါသည်
✅ Notebook diagnostic cells pass
✅ Output တွင် connection error မရှိပါ

---

## အကူအညီရယူခြင်း

### Documentation
- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting**: ဒီ directory ထဲရှိ `troubleshooting.md` ကိုကြည့်ပါ

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**နောက်ဆုံးအပ်ဒိတ်:** October 8, 2025  
**ဗားရှင်း:** Workshop Notebooks 2.0

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။