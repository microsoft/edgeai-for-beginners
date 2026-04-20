# កំណត់សៀវភៅសិក្ខាសាលា - មគ្គុទេសក៍ដោះស្រាយបញ្ហា

## តារាងមាតិកា

- [បញ្ហាទូទៅ និងដំណោះស្រាយ](#បញ្ហាទូទៅ-និងដំណោះស្រាយ)
- [បញ្ហាពិសេស​សម្រាប់សម័យ 04](#pre-load-models)
- [បញ្ហាពិសេស​សម្រាប់សម័យ 05](#diagnostic-cell-fails)
- [បញ្ហាពិសេស​សម្រាប់សម័យ 06](#ករណីសម័យ-05-បញ្ហាពិសេស)
- [បញ្ហាសម្ភារៈជាក់លាក់](#ករណីសម័យ-06-បញ្ហាពិសេស)
- [ពាក្យបញ្ជាវិភាគ](#nvidia-gpu)
- [របៀបទទួលជំនួយ](#ពាក្យបញ្ជាវិភាគ)

---

## បញ្ហាទូទៅ និងដំណោះស្រាយ

### 🔴 CUDA Out of Memory

**Error Message:**
```
CUDA failure 2: out of memory
```

**Root Cause:** GPU doesn't have enough VRAM to load the model.

**Solutions:**

#### Option 1: Use CPU Variants (Recommended)
```python
# នៅក្នុងសៀវភៅកំណត់ត្រារបស់អ្នក ធ្វើបច្ចុប្បន្នភាព CATALOG ដើម្បីប្រើប្រភេទ CPU ផ្សេងៗ
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Option 2: Use Smaller Models on GPU
```python
# ប្រើតែម៉ូឌែលតូចបំផុត
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Option 3: Clear GPU Memory
```bash
# បិទកម្មវិធីផ្សេងទៀតដែលប្រើ GPU យ៉ាងខ្លាំង
# ពិនិត្យការប្រើប្រាស់មេម៉ូរី GPU
nvidia-smi

# ចាប់ផ្ដើមឡើងវិញសេវាកម្ម Foundry Local
foundry service stop
foundry service start
```

#### Option 4: Increase GPU Memory (if possible)
- Close browser tabs, video editors, or other GPU apps
- Reduce Windows visual effects
- Use dedicated GPU if you have integrated + dedicated

---

### 🔴 APIConnectionError: Connection Error

**Error Message:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Root Cause:** Foundry Local service is not running or not accessible.

**Solutions:**

#### Step 1: Check Service Status
```bash
foundry service status
```

#### Step 2: Start Service if Stopped
```bash
foundry service start
```

#### Step 3: Verify Endpoint
```bash
# ពិនិត្យមើលថាសេវាកម្មកំពុងប្រើច្រកណា
foundry service status

# សាកល្បងជាមួយ curl (កែច្រកប្រសិនបើខុស)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Step 4: Load Required Models
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Step 5: Restart Notebook Kernel
After starting the service and loading models, restart the notebook kernel and re-run all cells.

---

### 🔴 Model Not Found in Catalog

**Error Message:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Root Cause:** Model isn't downloaded or loaded in Foundry Local.

**Solutions:**

#### Option 1: Download and Load Models
```bash
# បញ្ជីម៉ូដែលដែលអាចប្រើបាន
foundry model ls

# ទាញយកម៉ូដែល ប្រសិនបើវាមិនមាន
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# ផ្ទុកម៉ូដែលចូលទៅក្នុងអង្គចងចាំ
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Option 2: Use Auto-Selection Mode
Update your CATALOG to use base model names (without `-cpu` suffix):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK will automatically select the best variant (CPU, GPU, or NPU) for your hardware.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Error Message:**
```
HttpResponseError: 500 - Failed loading model
```

**Root Cause:** Model file is corrupted or incompatible with hardware.

**Solutions:**

#### Redownload Model
```bash
# លុបម៉ូឌែលខូច
foundry model remove phi-3.5-mini

# ទាញយកចម្លងថ្មី
foundry model download phi-3.5-mini
```

#### Use Different Variant
```bash
# សាកល្បងកំណែ CPU ជំនួស
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Error Message:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Root Cause:** foundry-local-sdk package not installed.

**Solutions:**

```bash
# ដំឡើង SDK
pip install foundry-local-sdk

# ផ្ទៀងផ្ទាត់ការតម្លើង
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Slow First Request

**Symptom:** First completion takes 30+ seconds, subsequent requests are fast.

**Root Cause:** This is normal behavior - the service is loading the model into memory on first request.

**Solutions:**

#### Pre-load Models
```bash
# ទាញយក និងផ្ទុកម៉ូដែលទាំងអស់ដែលអ្នកនឹងប្រើ មុនពេលរត់សៀវភៅកូដ (notebooks)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Keep Service Running
```bash
# ចាប់ផ្តើមសេវាកម្មដោយដៃ ហើយទុកឲ្យវាដំណើរការ
foundry service start
```

---

## បញ្ហាពិសេស​សម្រាប់សម័យ 04

### Wrong Port Configuration

**Issue:** Notebook connecting to wrong port (55769 vs 59959 vs 57127)

**Solution:**

1. Check which port Foundry Local is using:
```bash
foundry service status
# ចំណាំលេខច្រកដែលបង្ហាញ
```

2. Update Cell 10 in the notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# ប្តូរ 59959 ទៅជា​ច្រក​ពិត​របស់អ្នក
```

3. Restart kernel and re-run cells 6, 8, 10, 12, 16, 20, 22

---

### Wrong Model Selection

**Issue:** Notebook showing gpt-oss-20b or qwen2.5-7b instead of qwen2.5-3b

**Solution:**

1. Restart notebook kernel (clears old variable state)
2. Re-run Cell 10 (Set Model Aliases)
3. Re-run Cell 12 (Display Configuration)
4. **Verify:** Cell 12 should show `LLM Model: qwen2.5-3b`

---

### Diagnostic Cell Fails

**Issue:** Cell 16 shows "❌ Foundry Local service not found!"

**Solution:**

1. Verify service is running:
```bash
foundry service status
```

2. Test endpoint manually:
```bash
curl http://localhost:59959/v1/models
```

3. If curl works but notebook doesn't:
   - Restart notebook kernel
   - Re-run cells in order: 6, 8, 10, 12, 14, 16

4. If curl fails:
   - Start service: `foundry service start`
   - Load models: `foundry model run phi-4-mini` and `foundry model run qwen2.5-3b`

---

### Pre-flight Check Fails

**Issue:** Cell 20 shows connection errors even though diagnostic passed

**Solution:**

1. Check models are loaded:
```bash
foundry model ls
# គួរតែបង្ហាញ phi-4-mini និង qwen2.5-3b
```

2. If models missing:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Re-run Cell 20 after models are loaded

---

### Comparison Fails with None Values

**Issue:** Cell 22 completes but shows latency as None

**Solution:**

1. Check that pre-flight passed first (Cell 20)
2. Re-run Cell 22 - models may need to warm up on first request
3. Verify both models are loaded: `foundry model ls`

---

## ករណីសម័យ 05 - បញ្ហាពិសេស

### Agent Using Wrong Model

**Issue:** Agent not using expected model

**Solution:**

Verify configuration:
```python
# ពិនិត្យមើលម៉ូដែលណាខ្លះដែលត្រូវបានចាត់តាំង
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Restart kernel if models are incorrect.

---

### Memory Context Overflow

**Issue:** Agent responses degrading over time

**Solution:** Already handled automatically - agents keep only last 6 messages in memory.

---

## ករណីសម័យ 06 - បញ្ហាពិសេស

### CPU vs GPU Model Confusion

**Issue:** Getting CUDA errors when using default configuration

**Solution:** The default configuration now uses CPU models. If you see CUDA errors:

1. Verify you're using the default CPU catalog:
```python
# កោសិកានោះគួរតែបង្ហាញប្រភេទ CPU ផ្សេងៗ
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Restart kernel and re-run all cells

---

### Intent Detection Not Working

**Issue:** Prompts being routed to wrong models

**Solution:**

Test intent detection:
```python
# រត់កោសิกាសាកល្បងសម្រាប់ចាប់សម្គាល់ចេតនា
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Update RULES if patterns need adjustment.

---

## បញ្ហាសម្ភារៈជាក់លាក់

### NVIDIA GPU

**Check GPU Status:**
```bash
nvidia-smi
```

**Common Issues:**
- **Driver outdated**: Update NVIDIA drivers
- **CUDA version mismatch**: Reinstall Foundry Local
- **GPU memory fragmented**: Restart system

### Qualcomm NPU

**Check NPU Status:**
```bash
foundry device info
```

**Common Issues:**
- **NPU drivers not installed**: Install Qualcomm NPU drivers
- **NPU variant not available**: Use CPU variant
- **Windows version too old**: Update to latest Windows 11

### CPU-Only Systems

**Recommended Models:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Performance Tips:**
- Use smallest models
- Reduce max_tokens
- Increase patience for first request

---

## ពាក្យបញ្ជាវិភាគ

### Check Everything
```bash
# ស្ថានភាពសេវា
foundry service status

# បញ្ជីម៉ូដែល
foundry model ls

# ព័ត៌មានឧបករណ៍
foundry device info

# ព័ត៌មានកំណែ
foundry --version

# ត្រួតពិនិត្យសុខភាព
curl http://localhost:55769/health
```

### In Python
```python
# ពិនិត្យការនាំចូល SDK
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# ពិនិត្យការតភ្ជាប់សេវាកម្ម
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## របៀបទទួលជំនួយ

### 1. Check Logs
```bash
# វីនដូ
foundry service logs

# ឬពិនិត្យកម្មវិធីមើលព្រឹត្តិការណ៍របស់ Windows
# កំណត់ហេតុកម្មវិធី -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Search existing issues: https://github.com/microsoft/Foundry-Local/issues
- Create new issue with:
  - Error message (full text)
  - Output of `foundry service status`
  - Output of `foundry --version`
  - GPU/NPU info (nvidia-smi, etc.)
  - Steps to reproduce

### 3. Documentation
- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## បញ្ជីពិនិត្យជំហRapid Fixes

When things go wrong, try these in order:

- [ ] Check service is running: `foundry service status`
- [ ] Restart service: `foundry service stop && foundry service start`
- [ ] Verify model exists: `foundry model ls | grep phi-4-mini`
- [ ] Load required models: `foundry model run phi-4-mini`
- [ ] Check GPU memory: `nvidia-smi` (if NVIDIA)
- [ ] Try CPU variant: Use `phi-4-mini-cpu` instead of `phi-4-mini`
- [ ] Restart notebook kernel
- [ ] Clear notebook outputs and re-run all cells
- [ ] Reinstall SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Reboot system (last resort)

---

## វិធានការការពារ

### គោលការណ៍អនុវត្តិល្អ

1. **Always check service first:**
   ```bash
   foundry service status
   ```

2. **Use CPU variants by default:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pre-load models before running notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Keep service running:**
   - Don't stop/start service unnecessarily
   - Let it run in background between sessions

5. **Monitor resources:**
   - Check GPU memory before running
   - Close unnecessary GPU applications
   - Use Task Manager / nvidia-smi

6. **Update regularly:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**បានធ្វើបច្ចុប្បន្នភាពចុងក្រោយ៖** October 8, 2025

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមចំណាំថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានចាត់ទុកជាប្រភពដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឱ្យប្រើការបកប្រែដោយអ្នកបកប្រែអាជីព។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->