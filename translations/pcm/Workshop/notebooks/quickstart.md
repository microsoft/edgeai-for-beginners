# Workshop Notebooks - Quick Start Guide

## Table of Contents

- [Prerequisites](../../../../Workshop/notebooks)
- [Initial Setup](../../../../Workshop/notebooks)
- [Session 04: Model Comparison](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent Orchestrator](../../../../Workshop/notebooks)
- [Session 06: Intent-Based Model Routing](../../../../Workshop/notebooks)
- [Environment Variables](../../../../Workshop/notebooks)
- [Common Commands](../../../../Workshop/notebooks)

---

## Prerequisites

### 1. Install Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verify Installation:**
```bash
foundry --version
```

### 2. Install Python Dependencies

```bash
cd Workshop
pip install -r requirements.txt
```

Or install one by one:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Initial Setup

### Start Foundry Local Service

**You gatz start dis one before you fit run any notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Expected output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Download and Load Models

Di notebooks dey use dis models by default:

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

### Verify Setup

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Model Comparison

### Purpose
Make comparison between Small Language Models (SLM) and Large Language Models (LLM) performance.

### Quick Setup

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Running the Notebook

1. **Open** `session04_model_compare.ipynb` for VS Code or Jupyter
2. **Restart kernel** (Kernel → Restart Kernel)
3. **Run all cells** one by one

### Key Configuration

**Default Models:**
- **SLM:** `phi-4-mini` (~4GB RAM, e dey fast)
- **LLM:** `qwen2.5-3b` (~3GB RAM, memory dey optimized)

**Environment Variables (optional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Expected Output

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

### Customization

**Use different models:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Custom prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Validation Checklist

- [ ] Cell 12 show correct models (phi-4-mini, qwen2.5-3b)
- [ ] Cell 12 show correct endpoint (port 59959)
- [ ] Cell 16 diagnostic pass (✅ Service dey run)
- [ ] Cell 20 pre-flight check pass (both models dey ok)
- [ ] Cell 22 comparison complete wit latency values
- [ ] Cell 24 validation show 🎉 ALL CHECKS PASSED!

### Time Estimate
- **First run:** 5-10 minutes (including model downloads)
- **Subsequent runs:** 1-2 minutes

---

## Session 05: Multi-Agent Orchestrator

### Purpose
Show how multi-agent dey work together using Foundry Local SDK - agents go join hand to produce better results.

### Quick Setup

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Running the Notebook

1. **Open** `session05_agents_orchestrator.ipynb`
2. **Restart kernel**
3. **Run all cells** one by one

### Key Configuration

**Default Setup (Same Model for Both Agents):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Advanced Setup (Different Models):**
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

### Expected Output

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

**Add more agents:**
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

### Time Estimate
- **First run:** 3-5 minutes
- **Subsequent runs:** 1-2 minutes per question

---

## Session 06: Intent-Based Model Routing

### Purpose
Route prompts go specialized models based on di detected intent.

### Quick Setup

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Note:** Session 06 dey use CPU models by default for better compatibility.

### Running the Notebook

1. **Open** `session06_models_router.ipynb`
2. **Restart kernel**
3. **Run all cells** one by one

### Key Configuration

**Default Catalog (CPU Models):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternative (GPU Models):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Intent Detection

Di router dey use regex patterns to detect intent:

| Intent | Pattern Examples | Routed To |
|--------|-----------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Everything else | phi-4-mini-cpu |

### Expected Output

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

### Customization

**Add custom intent:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Enable token tracking:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Switching to GPU Models

If you get 8GB+ VRAM:

1. For **Cell #6**, comment CPU catalog
2. Uncomment GPU catalog
3. Load GPU models:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Restart kernel and re-run notebook

### Time Estimate
- **First run:** 5-10 minutes (model loading)
- **Subsequent runs:** 30-60 seconds per test

---

## Environment Variables

### Global Configuration

Set am before you start Jupyter/VS Code:

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

### In-Notebook Configuration

Set am for di start of any notebook:

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

## Common Commands

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

### Testing Endpoints

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

## Best Practices

### Before Starting Any Notebook

1. **Check say service dey run:**
   ```bash
   foundry service status
   ```

2. **Verify say models dey loaded:**
   ```bash
   foundry model ls
   ```

3. **Restart notebook kernel** if you dey re-run

4. **Clear all outputs** for clean run

### Resource Management

1. **Use CPU models by default** for compatibility
2. **Switch to GPU models** only if you get 8GB+ VRAM
3. **Close other GPU applications** before you run
4. **Keep service dey run** between notebook sessions
5. **Monitor resource usage** wit Task Manager / nvidia-smi

### Troubleshooting

1. **Always check service first** before you debug code
2. **Restart kernel** if you see stale configuration
3. **Re-run diagnostic cells** after any changes
4. **Check model names** match wetin dey loaded
5. **Verify endpoint port** match service status

---

## Quick Reference: Model Aliases

### Common Models

| Alias | Size | Best For | RAM/VRAM | Variants |
|-------|------|----------|----------|----------|
| `phi-4-mini` | ~4B | General chat, summarization | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Code generation, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | General tasks, efficient | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Fast, low resource | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classification, minimal resource | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variant Naming

- **Base name** (e.g., `phi-4-mini`): E go auto-select di best variant for your hardware
- **`-cpu`**: CPU-optimized, e dey work everywhere
- **`-cuda-gpu`**: NVIDIA GPU optimized, e need 8GB+ VRAM
- **`-npu`**: Qualcomm NPU optimized, e need NPU drivers

**Recommendation:** Use base names (without suffix) and make Foundry Local auto-select di best variant.

---

## Success Indicators

You dey ready when you see:

✅ `foundry service status` show "running"
✅ `foundry model ls` show di models wey you need
✅ Service dey accessible for di correct endpoint
✅ Health check return 200 OK
✅ Notebook diagnostic cells pass
✅ No connection errors for output

---

## Getting Help

### Documentation
- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting**: Check `troubleshooting.md` for dis directory

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Last Updated:** October 8, 2025
**Version:** Workshop Notebooks 2.0

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, e better make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->