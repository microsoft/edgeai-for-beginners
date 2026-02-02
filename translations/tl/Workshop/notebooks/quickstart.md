# Workshop Notebooks - Gabay sa Mabilisang Pagsisimula

## Talaan ng Nilalaman

- [Mga Kinakailangan](../../../../Workshop/notebooks)
- [Paunang Setup](../../../../Workshop/notebooks)
- [Session 04: Paghahambing ng Modelo](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent Orchestrator](../../../../Workshop/notebooks)
- [Session 06: Intent-Based Model Routing](../../../../Workshop/notebooks)
- [Mga Variable ng Kapaligiran](../../../../Workshop/notebooks)
- [Karaniwang Utos](../../../../Workshop/notebooks)

---

## Mga Kinakailangan

### 1. I-install ang Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**I-verify ang Pag-install:**
```bash
foundry --version
```

### 2. I-install ang Mga Dependency ng Python

```bash
cd Workshop
pip install -r requirements.txt
```

O i-install nang paisa-isa:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Paunang Setup

### Simulan ang Foundry Local Service

**Kinakailangan bago magpatakbo ng anumang notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Inaasahang output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### I-download at I-load ang Mga Modelo

Ang mga notebook ay gumagamit ng mga modelong ito bilang default:

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

### I-verify ang Setup

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Paghahambing ng Modelo

### Layunin
Ihambing ang performance ng Small Language Models (SLM) at Large Language Models (LLM).

### Mabilisang Setup

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Pagpapatakbo ng Notebook

1. **Buksan** ang `session04_model_compare.ipynb` sa VS Code o Jupyter
2. **I-restart ang kernel** (Kernel → Restart Kernel)
3. **Patakbuhin ang lahat ng cells** nang sunod-sunod

### Pangunahing Konfigurasyon

**Default na Mga Modelo:**
- **SLM:** `phi-4-mini` (~4GB RAM, mas mabilis)
- **LLM:** `qwen2.5-3b` (~3GB RAM, memory-optimized)

**Mga Variable ng Kapaligiran (opsyonal):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Inaasahang Output

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

### Pag-customize

**Gumamit ng ibang mga modelo:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Pasadyang prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Checklist ng Pagpapatunay

- [ ] Ang Cell 12 ay nagpapakita ng tamang mga modelo (phi-4-mini, qwen2.5-3b)
- [ ] Ang Cell 12 ay nagpapakita ng tamang endpoint (port 59959)
- [ ] Ang Cell 16 diagnostic ay pumasa (✅ Naka-on ang serbisyo)
- [ ] Ang Cell 20 pre-flight check ay pumasa (parehong modelo ay ok)
- [ ] Ang Cell 22 paghahambing ay nakumpleto na may mga latency values
- [ ] Ang Cell 24 validation ay nagpapakita 🎉 LAHAT NG CHECKS PASSED!

### Tinatayang Oras
- **Unang takbo:** 5-10 minuto (kasama ang pag-download ng modelo)
- **Mga susunod na takbo:** 1-2 minuto

---

## Session 05: Multi-Agent Orchestrator

### Layunin
Ipakita ang pakikipagtulungan ng multi-agent gamit ang Foundry Local SDK - nagtutulungan ang mga agent upang makagawa ng mas pinong output.

### Mabilisang Setup

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Pagpapatakbo ng Notebook

1. **Buksan** ang `session05_agents_orchestrator.ipynb`
2. **I-restart ang kernel**
3. **Patakbuhin ang lahat ng cells** nang sunod-sunod

### Pangunahing Konfigurasyon

**Default na Setup (Parehong Modelo para sa Parehong Mga Agent):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Advanced na Setup (Iba't ibang Mga Modelo):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arkitektura

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

### Inaasahang Output

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

### Mga Extension

**Magdagdag ng mas maraming agent:**
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

### Tinatayang Oras
- **Unang takbo:** 3-5 minuto
- **Mga susunod na takbo:** 1-2 minuto bawat tanong

---

## Session 06: Intent-Based Model Routing

### Layunin
Matalinong i-route ang mga prompt sa mga espesyal na modelo batay sa natukoy na intensyon.

### Mabilisang Setup

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Tandaan:** Ang Session 06 ay default na gumagamit ng mga CPU model para sa maximum na compatibility.

### Pagpapatakbo ng Notebook

1. **Buksan** ang `session06_models_router.ipynb`
2. **I-restart ang kernel**
3. **Patakbuhin ang lahat ng cells** nang sunod-sunod

### Pangunahing Konfigurasyon

**Default Catalog (CPU Models):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatibo (GPU Models):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Pagtukoy ng Intensyon

Ang router ay gumagamit ng regex patterns upang matukoy ang intensyon:

| Intensyon | Mga Halimbawa ng Pattern | Ire-route Sa |
|-----------|--------------------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Lahat ng iba pa | phi-4-mini-cpu |

### Inaasahang Output

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

### Pag-customize

**Magdagdag ng pasadyang intensyon:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**I-enable ang token tracking:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Paglipat sa GPU Models

Kung mayroon kang 8GB+ VRAM:

1. Sa **Cell #6**, i-comment out ang CPU catalog
2. I-uncomment ang GPU catalog
3. I-load ang GPU models:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. I-restart ang kernel at i-re-run ang notebook

### Tinatayang Oras
- **Unang takbo:** 5-10 minuto (pag-load ng modelo)
- **Mga susunod na takbo:** 30-60 segundo bawat test

---

## Mga Variable ng Kapaligiran

### Global na Konfigurasyon

Itakda bago simulan ang Jupyter/VS Code:

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

### Konfigurasyon sa Notebook

Itakda sa simula ng anumang notebook:

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

## Karaniwang Utos

### Pamamahala ng Serbisyo

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

### Pamamahala ng Modelo

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

### Pagsubok ng Endpoints

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

### Mga Diagnostic na Utos

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

## Mga Pinakamahusay na Kasanayan

### Bago Simulan ang Anumang Notebook

1. **Suriin kung tumatakbo ang serbisyo:**
   ```bash
   foundry service status
   ```

2. **I-verify na na-load ang mga modelo:**
   ```bash
   foundry model ls
   ```

3. **I-restart ang kernel ng notebook** kung muling magpapatakbo

4. **I-clear ang lahat ng output** para sa malinis na takbo

### Pamamahala ng Resource

1. **Gumamit ng CPU models bilang default** para sa compatibility
2. **Lumipat sa GPU models** kung mayroon kang 8GB+ VRAM
3. **Isara ang ibang GPU applications** bago magpatakbo
4. **Panatilihing tumatakbo ang serbisyo** sa pagitan ng mga session ng notebook
5. **Subaybayan ang paggamit ng resource** gamit ang Task Manager / nvidia-smi

### Pag-aayos ng Problema

1. **Laging suriin ang serbisyo muna** bago mag-debug ng code
2. **I-restart ang kernel** kung may nakikitang lumang konfigurasyon
3. **Muling patakbuhin ang mga diagnostic cells** pagkatapos ng anumang pagbabago
4. **Suriin ang mga pangalan ng modelo** na tumutugma sa na-load
5. **I-verify ang endpoint port** na tumutugma sa status ng serbisyo

---

## Mabilisang Sanggunian: Mga Alias ng Modelo

### Karaniwang Mga Modelo

| Alias | Sukat | Pinakamainam Para sa | RAM/VRAM | Mga Variant |
|-------|-------|----------------------|----------|-------------|
| `phi-4-mini` | ~4B | General chat, summarization | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Code generation, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | General tasks, efficient | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Mabilis, mababang resource | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classification, minimal resource | 1-2GB | `-cpu`, `-cuda-gpu` |

### Pangalan ng Variant

- **Base name** (hal., `phi-4-mini`): Auto-selects ang pinakamahusay na variant para sa iyong hardware
- **`-cpu`**: CPU-optimized, gumagana kahit saan
- **`-cuda-gpu`**: NVIDIA GPU optimized, nangangailangan ng 8GB+ VRAM
- **`-npu`**: Qualcomm NPU optimized, nangangailangan ng NPU drivers

**Rekomendasyon:** Gumamit ng base names (walang suffix) at hayaan ang Foundry Local na auto-select ang pinakamahusay na variant.

---

## Mga Palatandaan ng Tagumpay

Handa ka na kapag nakita mo:

✅ `foundry service status` ay nagpapakita ng "running"  
✅ `foundry model ls` ay nagpapakita ng mga kinakailangang modelo  
✅ Ang serbisyo ay naa-access sa tamang endpoint  
✅ Ang health check ay nagbabalik ng 200 OK  
✅ Ang mga diagnostic cells ng notebook ay pumasa  
✅ Walang mga error sa koneksyon sa output  

---

## Pagkuha ng Tulong

### Dokumentasyon
- **Pangunahing Repositoryo**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Pag-aayos ng Problema**: Tingnan ang `troubleshooting.md` sa direktoryong ito  

### Mga Isyu sa GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**Huling Na-update:** Oktubre 8, 2025  
**Bersyon:** Workshop Notebooks 2.0

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.