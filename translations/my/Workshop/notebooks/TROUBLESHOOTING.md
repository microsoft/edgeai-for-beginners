# Workshop Notebooks - ပြဿနာဖြေရှင်းလမ်းညွှန်

## အကြောင်းအရာများ

- [ပုံမှန်ပြဿနာများနှင့် ဖြေရှင်းနည်းများ](../../../../Workshop/notebooks)
- [Session 04 အထူးပြဿနာများ](../../../../Workshop/notebooks)
- [Session 05 အထူးပြဿနာများ](../../../../Workshop/notebooks)
- [Session 06 အထူးပြဿနာများ](../../../../Workshop/notebooks)
- [Hardware အထူးပြဿနာများ](../../../../Workshop/notebooks)
- [Diagnostic Commands](../../../../Workshop/notebooks)
- [အကူအညီရယူခြင်း](../../../../Workshop/notebooks)

---

## ပုံမှန်ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### 🔴 CUDA Out of Memory

**Error Message:**
```
CUDA failure 2: out of memory
```
  
**Root Cause:** GPU တွင် model ကို load လုပ်ရန် VRAM မလုံလောက်ပါ။

**ဖြေရှင်းနည်းများ:**

#### Option 1: CPU Variants ကို အသုံးပြုပါ (အကြံပြုသည်)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Option 2: GPU တွင် သေးငယ်သော Models ကို အသုံးပြုပါ
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Option 3: GPU Memory ကို ရှင်းလင်းပါ
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Option 4: GPU Memory ကို တိုးမြှင့်ပါ (ဖြစ်နိုင်ပါက)
- Browser tabs, video editors, သို့မဟုတ် GPU apps အခြားများကို ပိတ်ပါ  
- Windows visual effects ကို လျှော့ချပါ  
- Integrated + dedicated GPU ရှိပါက dedicated GPU ကို အသုံးပြုပါ  

---

### 🔴 APIConnectionError: Connection Error

**Error Message:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Root Cause:** Foundry Local service မရရှိနိုင်ခြင်း သို့မဟုတ် မလုပ်ဆောင်နေခြင်း။

**ဖြေရှင်းနည်းများ:**

#### Step 1: Service Status ကို စစ်ဆေးပါ
```bash
foundry service status
```
  
#### Step 2: Service ရပ်နေပါက ပြန်စတင်ပါ
```bash
foundry service start
```
  
#### Step 3: Endpoint ကို အတည်ပြုပါ
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Step 4: လိုအပ်သော Models ကို Load လုပ်ပါ
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Step 5: Notebook Kernel ကို ပြန်စတင်ပါ
Service ကို စတင်ပြီး Models ကို Load လုပ်ပြီးနောက် Notebook Kernel ကို ပြန်စတင်ပြီး Cell အားလုံးကို ပြန်လည် run လုပ်ပါ။

---

### 🔴 Model Not Found in Catalog

**Error Message:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Root Cause:** Model ကို Foundry Local တွင် download သို့မဟုတ် load မလုပ်ထားခြင်း။

**ဖြေရှင်းနည်းများ:**

#### Option 1: Models ကို Download လုပ်ပြီး Load လုပ်ပါ
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Option 2: Auto-Selection Mode ကို အသုံးပြုပါ
CATALOG ကို base model names (e.g., `-cpu` suffix မပါသော) သို့ update လုပ်ပါ:

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK သည် သင့် hardware အတွက် အကောင်းဆုံး variant (CPU, GPU, သို့မဟုတ် NPU) ကို အလိုအလျောက် ရွေးချယ်ပါမည်။

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Error Message:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Root Cause:** Model file သည် corrupted ဖြစ်ခြင်း သို့မဟုတ် hardware နှင့် မကိုက်ညီခြင်း။

**ဖြေရှင်းနည်းများ:**

#### Model ကို ပြန်လည် Download လုပ်ပါ
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### အခြား Variant ကို အသုံးပြုပါ
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  

---

### 🔴 ImportError: No Module Found

**Error Message:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Root Cause:** foundry-local-sdk package မတင်ထားခြင်း။

**ဖြေရှင်းနည်းများ:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  

---

### � Slow First Request

**Symptom:** ပထမဆုံး completion သည် 30+ စက္ကန့်ကြာပြီး နောက်တစ်ကြိမ် request များသည် မြန်ဆန်သည်။

**Root Cause:** ပထမ request တွင် service သည် model ကို memory ထဲသို့ load လုပ်နေသည်။

**ဖြေရှင်းနည်းများ:**

#### Models ကို ကြိုတင် Load လုပ်ပါ
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Service ကို အမြဲ run လုပ်ထားပါ
```bash
# Start service manually and leave it running
foundry service start
```
  

---

## Session 04 အထူးပြဿနာများ

### Wrong Port Configuration

**Issue:** Notebook သည် မှားသော port (55769 vs 59959 vs 57127) သို့ ချိတ်ဆက်နေသည်။

**Solution:**

1. Foundry Local သုံးနေသော port ကို စစ်ဆေးပါ:
```bash
foundry service status
# Note the port number displayed
```
  
2. Notebook ရှိ Cell 10 ကို update လုပ်ပါ:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Kernel ကို ပြန်စတင်ပြီး Cell 6, 8, 10, 12, 16, 20, 22 ကို ပြန်လည် run လုပ်ပါ။

---

### Wrong Model Selection

**Issue:** Notebook တွင် gpt-oss-20b သို့မဟုတ် qwen2.5-7b ကို ပြသနေပြီး qwen2.5-3b မဟုတ်ပါ။

**Solution:**

1. Notebook Kernel ကို ပြန်စတင်ပါ (ဟောင်းသော variable state ကို ရှင်းလင်းသည်)  
2. Cell 10 ကို ပြန်လည် run လုပ်ပါ (Set Model Aliases)  
3. Cell 12 ကို ပြန်လည် run လုပ်ပါ (Display Configuration)  
4. **Verify:** Cell 12 တွင် `LLM Model: qwen2.5-3b` ဟု ပြသရမည်။

---

### Diagnostic Cell Fails

**Issue:** Cell 16 တွင် "❌ Foundry Local service not found!" ဟု ပြသသည်။

**Solution:**

1. Service သည် run လုပ်နေသည်ကို အတည်ပြုပါ:
```bash
foundry service status
```
  
2. Endpoint ကို manual စမ်းသပ်ပါ:
```bash
curl http://localhost:59959/v1/models
```
  
3. curl သည် အလုပ်လုပ်ပြီး notebook မလုပ်ပါက:
   - Notebook Kernel ကို ပြန်စတင်ပါ  
   - Cells များကို အစဉ်လိုက် ပြန်လည် run လုပ်ပါ: 6, 8, 10, 12, 14, 16  

4. curl မအလုပ်လုပ်ပါက:
   - Service ကို စတင်ပါ: `foundry service start`  
   - Models ကို Load လုပ်ပါ: `foundry model run phi-4-mini` နှင့် `foundry model run qwen2.5-3b`  

---

### Pre-flight Check Fails

**Issue:** Cell 20 တွင် connection errors ကို diagnostic pass ဖြစ်သော်လည်း ပြသသည်။

**Solution:**

1. Models များ load လုပ်ထားသည်ကို စစ်ဆေးပါ:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Models မရှိပါက:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Models များ load လုပ်ပြီးနောက် Cell 20 ကို ပြန်လည် run လုပ်ပါ။

---

### Comparison Fails with None Values

**Issue:** Cell 22 သည် ပြီးမြောက်သော်လည်း latency ကို None ဟု ပြသသည်။

**Solution:**

1. Pre-flight pass ဖြစ်ထားသည်ကို စစ်ဆေးပါ (Cell 20)  
2. Cell 22 ကို ပြန်လည် run လုပ်ပါ - ပထမ request တွင် models များ warm up လုပ်ရန် လိုအပ်နိုင်သည်  
3. Models နှစ်ခုလုံး load လုပ်ထားသည်ကို အတည်ပြုပါ: `foundry model ls`  

---

## Session 05 အထူးပြဿနာများ

### Agent Using Wrong Model

**Issue:** Agent သည် မျှော်မှန်းထားသော model ကို မသုံးပါ။

**Solution:**

Configuration ကို အတည်ပြုပါ:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Models မှားနေပါက Kernel ကို ပြန်စတင်ပါ။

---

### Memory Context Overflow

**Issue:** Agent response quality သည် အချိန်ကြာလာသည်နှင့်အမျှ ကျဆင်းနေသည်။

**Solution:** အလိုအလျောက် ဖြေရှင်းထားပြီး - agents သည် memory တွင် နောက်ဆုံး message ၆ ခုသာ ထားရှိသည်။

---

## Session 06 အထူးပြဿနာများ

### CPU vs GPU Model Confusion

**Issue:** ပုံမှန် configuration အသုံးပြုနေစဉ် CUDA errors ရရှိသည်။

**Solution:** ပုံမှန် configuration သည် ယခု CPU models ကို အသုံးပြုနေပါသည်။ CUDA errors ရရှိပါက:

1. Default CPU catalog ကို အသုံးပြုနေသည်ကို အတည်ပြုပါ:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Kernel ကို ပြန်စတင်ပြီး Cell အားလုံးကို ပြန်လည် run လုပ်ပါ။

---

### Intent Detection Not Working

**Issue:** Prompts များကို မှားသော models သို့ ပို့နေသည်။

**Solution:**

Intent detection ကို စမ်းသပ်ပါ:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
RULES ကို update လုပ်ပါ (patterns ကို လိုအပ်သလို ပြင်ဆင်ပါ)။

---

## Hardware အထူးပြဿနာများ

### NVIDIA GPU

**GPU Status ကို စစ်ဆေးပါ:**
```bash
nvidia-smi
```
  
**ပုံမှန်ပြဿနာများ:**
- **Driver မဟောင်းမရှင်း**: NVIDIA drivers ကို update လုပ်ပါ  
- **CUDA version မကိုက်ညီ**: Foundry Local ကို ပြန်လည် install လုပ်ပါ  
- **GPU memory fragmented**: System ကို ပြန်လည်စတင်ပါ  

### Qualcomm NPU

**NPU Status ကို စစ်ဆေးပါ:**
```bash
foundry device info
```
  
**ပုံမှန်ပြဿနာများ:**
- **NPU drivers မတင်ထားခြင်း**: Qualcomm NPU drivers ကို install လုပ်ပါ  
- **NPU variant မရရှိနိုင်ခြင်း**: CPU variant ကို အသုံးပြုပါ  
- **Windows version မဟောင်းနေခြင်း**: Windows 11 အနောက်ဆုံး version သို့ update လုပ်ပါ  

### CPU-Only Systems

**အကြံပြု Models:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Performance Tips:**
- သေးငယ်သော models ကို အသုံးပြုပါ  
- max_tokens ကို လျှော့ချပါ  
- ပထမ request အတွက် အချိန်ပိုပေးပါ  

---

## Diagnostic Commands

### အားလုံးကို စစ်ဆေးပါ
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```
  
### Python တွင်
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```
  

---

## အကူအညီရယူခြင်း

### 1. Logs ကို စစ်ဆေးပါ
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub Issues
- ရှိပြီးသား issues ကို ရှာပါ: https://github.com/microsoft/Foundry-Local/issues  
- အသစ်သော issue တစ်ခုကို ဖန်တီးပါ:
  - Error message (အပြည့်အစုံ)  
  - `foundry service status` ၏ output  
  - `foundry --version` ၏ output  
  - GPU/NPU အချက်အလက် (nvidia-smi, စသည်)  
  - ပြဿနာကို ထပ်မံဖြစ်ပေါ်စေသော လုပ်ဆောင်မှုများ  

### 3. Documentation
- **Main Repository**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

---

## Quick Fixes Checklist

အခက်အခဲများ ဖြစ်ပေါ်ပါက အောက်ပါအဆင့်များကို အစဉ်လိုက် စမ်းသပ်ပါ:

- [ ] Service သည် run လုပ်နေသည်ကို စစ်ဆေးပါ: `foundry service status`  
- [ ] Service ကို ပြန်စတင်ပါ: `foundry service stop && foundry service start`  
- [ ] Model ရှိ/မရှိကို စစ်ဆေးပါ: `foundry model ls | grep phi-4-mini`  
- [ ] လိုအပ်သော Models ကို Load လုပ်ပါ: `foundry model run phi-4-mini`  
- [ ] GPU memory ကို စစ်ဆေးပါ: `nvidia-smi` (NVIDIA ဖြစ်ပါက)  
- [ ] CPU variant ကို စမ်းသပ်ပါ: `phi-4-mini-cpu` ကို အသုံးပြုပါ  
- [ ] Notebook Kernel ကို ပြန်စတင်ပါ  
- [ ] Notebook outputs ကို ရှင်းလင်းပြီး Cell အားလုံးကို ပြန်လည် run လုပ်ပါ  
- [ ] SDK ကို ပြန်လည် install လုပ်ပါ: `pip install --upgrade --force-reinstall foundry-local-sdk`  
- [ ] System ကို ပြန်လည်စတင်ပါ (နောက်ဆုံးအဆင့်)  

---

## ကာကွယ်ရေးအကြံပြုချက်များ

### အကောင်းဆုံး လုပ်ဆောင်နည်းများ

1. **Service ကို အရင်ဆုံး စစ်ဆေးပါ:**
   ```bash
   foundry service status
   ```
  
2. **ပုံမှန်အားဖြင့် CPU variants ကို အသုံးပြုပါ:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Notebook မ run မလုပ်မီ Models ကို ကြိုတင် Load လုပ်ပါ:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Service ကို အမြဲ run လုပ်ထားပါ:**
   - Service ကို မလိုအပ်ဘဲ ရပ်/စတင်မလုပ်ပါနှင့်  
   - Sessions အကြား background တွင် run လုပ်ထားပါ  

5. **Resources ကို စောင့်ကြည့်ပါ:**
   - Notebook မ run မလုပ်မီ GPU memory ကို စစ်ဆေးပါ  
   - မလိုအပ်သော GPU applications ကို ပိတ်ပါ  
   - Task Manager / nvidia-smi ကို အသုံးပြုပါ  

6. **အမြဲ update လုပ်ပါ:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  

---

**နောက်ဆုံး Update:** October 8, 2025  

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။