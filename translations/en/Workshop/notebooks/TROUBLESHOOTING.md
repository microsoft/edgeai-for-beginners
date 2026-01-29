# Workshop Notebooks - Troubleshooting Guide

## Table of Contents

- [Common Issues and Solutions](../../../../Workshop/notebooks)
- [Session 04 Specific Issues](../../../../Workshop/notebooks)
- [Session 05 Specific Issues](../../../../Workshop/notebooks)
- [Session 06 Specific Issues](../../../../Workshop/notebooks)
- [Hardware-Specific Issues](../../../../Workshop/notebooks)
- [Diagnostic Commands](../../../../Workshop/notebooks)
- [Getting Help](../../../../Workshop/notebooks)

---

## Common Issues and Solutions

### 🔴 CUDA Out of Memory

**Error Message:**
```
CUDA failure 2: out of memory
```
  
**Root Cause:** The GPU does not have enough VRAM to load the model.

**Solutions:**

#### Option 1: Use CPU Variants (Recommended)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Option 2: Use Smaller Models on GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Option 3: Clear GPU Memory
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Option 4: Increase GPU Memory (if possible)
- Close browser tabs, video editors, or other GPU-intensive applications.
- Reduce Windows visual effects.
- Use a dedicated GPU if you have both integrated and dedicated GPUs.

---

### 🔴 APIConnectionError: Connection Error

**Error Message:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Root Cause:** The Foundry Local service is not running or is inaccessible.

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
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
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
  
**Root Cause:** The model is not downloaded or loaded in Foundry Local.

**Solutions:**

#### Option 1: Download and Load Models
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
  
#### Option 2: Use Auto-Selection Mode  
Update your CATALOG to use base model names (without the `-cpu` suffix):

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
  
**Root Cause:** The model file is corrupted or incompatible with the hardware.

**Solutions:**

#### Redownload Model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Use Different Variant
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
  
**Root Cause:** The `foundry-local-sdk` package is not installed.

**Solutions:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  

---

### � Slow First Request

**Symptom:** The first completion takes 30+ seconds, while subsequent requests are faster.

**Root Cause:** This is expected behavior—the service is loading the model into memory during the first request.

**Solutions:**

#### Pre-load Models
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Keep Service Running
```bash
# Start service manually and leave it running
foundry service start
```
  

---

## Session 04 Specific Issues

### Wrong Port Configuration

**Issue:** The notebook is connecting to the wrong port (e.g., 55769 vs 59959 vs 57127).

**Solution:**

1. Check which port Foundry Local is using:
```bash
foundry service status
# Note the port number displayed
```
  
2. Update Cell 10 in the notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Restart the kernel and re-run cells 6, 8, 10, 12, 16, 20, 22.

---

### Wrong Model Selection

**Issue:** The notebook is showing `gpt-oss-20b` or `qwen2.5-7b` instead of `qwen2.5-3b`.

**Solution:**

1. Restart the notebook kernel (to clear old variable states).
2. Re-run Cell 10 (Set Model Aliases).
3. Re-run Cell 12 (Display Configuration).
4. **Verify:** Cell 12 should display `LLM Model: qwen2.5-3b`.

---

### Diagnostic Cell Fails

**Issue:** Cell 16 shows "❌ Foundry Local service not found!"

**Solution:**

1. Verify the service is running:
```bash
foundry service status
```
  
2. Test the endpoint manually:
```bash
curl http://localhost:59959/v1/models
```
  
3. If `curl` works but the notebook does not:
   - Restart the notebook kernel.
   - Re-run cells in order: 6, 8, 10, 12, 14, 16.

4. If `curl` fails:
   - Start the service: `foundry service start`.
   - Load models: `foundry model run phi-4-mini` and `foundry model run qwen2.5-3b`.

---

### Pre-flight Check Fails

**Issue:** Cell 20 shows connection errors even though diagnostics passed.

**Solution:**

1. Check if models are loaded:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. If models are missing:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Re-run Cell 20 after models are loaded.

---

### Comparison Fails with None Values

**Issue:** Cell 22 completes but shows latency as `None`.

**Solution:**

1. Ensure the pre-flight check passed first (Cell 20).
2. Re-run Cell 22—models may need to warm up during the first request.
3. Verify both models are loaded: `foundry model ls`.

---

## Session 05 Specific Issues

### Agent Using Wrong Model

**Issue:** The agent is not using the expected model.

**Solution:**

Verify the configuration:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Restart the kernel if the models are incorrect.

---

### Memory Context Overflow

**Issue:** Agent responses degrade over time.

**Solution:** This is already handled automatically—agents retain only the last 6 messages in memory.

---

## Session 06 Specific Issues

### CPU vs GPU Model Confusion

**Issue:** CUDA errors occur when using the default configuration.

**Solution:** The default configuration now uses CPU models. If you encounter CUDA errors:

1. Verify you are using the default CPU catalog:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Restart the kernel and re-run all cells.

---

### Intent Detection Not Working

**Issue:** Prompts are being routed to the wrong models.

**Solution:**

Test intent detection:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Update RULES if patterns need adjustment.

---

## Hardware-Specific Issues

### NVIDIA GPU

**Check GPU Status:**
```bash
nvidia-smi
```
  
**Common Issues:**
- **Driver outdated:** Update NVIDIA drivers.
- **CUDA version mismatch:** Reinstall Foundry Local.
- **GPU memory fragmented:** Restart the system.

### Qualcomm NPU

**Check NPU Status:**
```bash
foundry device info
```
  
**Common Issues:**
- **NPU drivers not installed:** Install Qualcomm NPU drivers.
- **NPU variant not available:** Use the CPU variant.
- **Windows version too old:** Update to the latest Windows 11.

### CPU-Only Systems

**Recommended Models:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Performance Tips:**
- Use the smallest models.
- Reduce `max_tokens`.
- Be patient with the first request.

---

## Diagnostic Commands

### Check Everything
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
  
### In Python
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

## Getting Help

### 1. Check Logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub Issues
- Search existing issues: https://github.com/microsoft/Foundry-Local/issues
- Create a new issue with:
  - Error message (full text).
  - Output of `foundry service status`.
  - Output of `foundry --version`.
  - GPU/NPU information (e.g., `nvidia-smi`).
  - Steps to reproduce the issue.

### 3. Documentation
- **Main Repository:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Quick Fixes Checklist

When issues arise, try these steps in order:

- [ ] Check if the service is running: `foundry service status`.
- [ ] Restart the service: `foundry service stop && foundry service start`.
- [ ] Verify the model exists: `foundry model ls | grep phi-4-mini`.
- [ ] Load required models: `foundry model run phi-4-mini`.
- [ ] Check GPU memory: `nvidia-smi` (if using NVIDIA).
- [ ] Try the CPU variant: Use `phi-4-mini-cpu` instead of `phi-4-mini`.
- [ ] Restart the notebook kernel.
- [ ] Clear notebook outputs and re-run all cells.
- [ ] Reinstall the SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`.
- [ ] Reboot the system (as a last resort).

---

## Prevention Tips

### Best Practices

1. **Always check the service first:**
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
  
4. **Keep the service running:**
   - Avoid stopping/starting the service unnecessarily.
   - Let it run in the background between sessions.

5. **Monitor resources:**
   - Check GPU memory before running.
   - Close unnecessary GPU applications.
   - Use Task Manager or `nvidia-smi`.

6. **Update regularly:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  

---

**Last Updated:** October 8, 2025

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.