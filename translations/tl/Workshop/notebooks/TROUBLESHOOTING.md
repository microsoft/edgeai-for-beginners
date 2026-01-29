# Workshop Notebooks - Gabay sa Pag-aayos ng Problema

## Talaan ng Nilalaman

- [Karaniwang Problema at Solusyon](../../../../Workshop/notebooks)
- [Mga Isyu sa Session 04](../../../../Workshop/notebooks)
- [Mga Isyu sa Session 05](../../../../Workshop/notebooks)
- [Mga Isyu sa Session 06](../../../../Workshop/notebooks)
- [Mga Isyu na Kaugnay sa Hardware](../../../../Workshop/notebooks)
- [Mga Diagnostic Command](../../../../Workshop/notebooks)
- [Pagkuha ng Tulong](../../../../Workshop/notebooks)

---

## Karaniwang Problema at Solusyon

### 🔴 CUDA Out of Memory

**Error Message:**
```
CUDA failure 2: out of memory
```

**Sanhi:** Kulang ang VRAM ng GPU para ma-load ang modelo.

**Mga Solusyon:**

#### Opsyon 1: Gumamit ng CPU Variants (Inirerekomenda)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opsyon 2: Gumamit ng Mas Maliit na Modelo sa GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opsyon 3: I-clear ang GPU Memory
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opsyon 4: Dagdagan ang GPU Memory (kung posible)
- Isara ang mga tab ng browser, video editor, o iba pang GPU apps
- Bawasan ang visual effects ng Windows
- Gumamit ng dedicated GPU kung may integrated + dedicated ka

---

### 🔴 APIConnectionError: Connection Error

**Error Message:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Sanhi:** Hindi tumatakbo o hindi ma-access ang Foundry Local service.

**Mga Solusyon:**

#### Hakbang 1: Suriin ang Status ng Serbisyo
```bash
foundry service status
```

#### Hakbang 2: I-start ang Serbisyo kung Naka-stop
```bash
foundry service start
```

#### Hakbang 3: I-verify ang Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Hakbang 4: I-load ang Kinakailangang Modelo
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Hakbang 5: I-restart ang Notebook Kernel
Pagkatapos i-start ang serbisyo at i-load ang mga modelo, i-restart ang notebook kernel at i-run muli ang lahat ng cells.

---

### 🔴 Model Not Found in Catalog

**Error Message:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Sanhi:** Hindi na-download o na-load ang modelo sa Foundry Local.

**Mga Solusyon:**

#### Opsyon 1: I-download at I-load ang Mga Modelo
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

#### Opsyon 2: Gumamit ng Auto-Selection Mode
I-update ang iyong CATALOG para gumamit ng base model names (walang `-cpu` suffix):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Awtomatikong pipili ang Foundry Local SDK ng pinakamainam na variant (CPU, GPU, o NPU) para sa iyong hardware.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Error Message:**
```
HttpResponseError: 500 - Failed loading model
```

**Sanhi:** Sira o hindi compatible ang model file sa hardware.

**Mga Solusyon:**

#### I-redownload ang Modelo
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Gumamit ng Ibang Variant
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

**Sanhi:** Hindi naka-install ang foundry-local-sdk package.

**Mga Solusyon:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Mabagal na Unang Request

**Sintomas:** Ang unang completion ay tumatagal ng 30+ segundo, mabilis ang mga kasunod na request.

**Sanhi:** Normal ito - niloload ng serbisyo ang modelo sa memory sa unang request.

**Mga Solusyon:**

#### I-pre-load ang Mga Modelo
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Panatilihing Tumatakbo ang Serbisyo
```bash
# Start service manually and leave it running
foundry service start
```

---

## Mga Isyu sa Session 04

### Mali ang Port Configuration

**Isyu:** Notebook kumokonekta sa maling port (55769 vs 59959 vs 57127)

**Solusyon:**

1. Suriin kung anong port ang ginagamit ng Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. I-update ang Cell 10 sa notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. I-restart ang kernel at i-run muli ang cells 6, 8, 10, 12, 16, 20, 22

---

### Mali ang Model Selection

**Isyu:** Notebook nagpapakita ng gpt-oss-20b o qwen2.5-7b sa halip na qwen2.5-3b

**Solusyon:**

1. I-restart ang notebook kernel (nililinis ang lumang variable state)
2. I-run muli ang Cell 10 (Set Model Aliases)
3. I-run muli ang Cell 12 (Display Configuration)
4. **I-verify:** Dapat ipakita ng Cell 12 ang `LLM Model: qwen2.5-3b`

---

### Diagnostic Cell Fails

**Isyu:** Cell 16 nagpapakita ng "❌ Foundry Local service not found!"

**Solusyon:**

1. Suriin kung tumatakbo ang serbisyo:
```bash
foundry service status
```

2. Subukan ang endpoint nang manu-mano:
```bash
curl http://localhost:59959/v1/models
```

3. Kung gumagana ang curl pero hindi ang notebook:
   - I-restart ang notebook kernel
   - I-run muli ang mga cells sa pagkakasunod-sunod: 6, 8, 10, 12, 14, 16

4. Kung hindi gumagana ang curl:
   - I-start ang serbisyo: `foundry service start`
   - I-load ang mga modelo: `foundry model run phi-4-mini` at `foundry model run qwen2.5-3b`

---

### Pre-flight Check Fails

**Isyu:** Cell 20 nagpapakita ng connection errors kahit pumasa ang diagnostic

**Solusyon:**

1. Suriin kung na-load ang mga modelo:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Kung kulang ang mga modelo:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. I-run muli ang Cell 20 pagkatapos ma-load ang mga modelo

---

### Comparison Fails with None Values

**Isyu:** Cell 22 natapos pero nagpapakita ng latency bilang None

**Solusyon:**

1. Suriin kung pumasa ang pre-flight (Cell 20)
2. I-run muli ang Cell 22 - maaaring kailangan mag-warm up ang mga modelo sa unang request
3. I-verify na parehong modelo ay na-load: `foundry model ls`

---

## Mga Isyu sa Session 05

### Agent Gumagamit ng Mali na Modelo

**Isyu:** Agent hindi gumagamit ng inaasahang modelo

**Solusyon:**

I-verify ang configuration:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

I-restart ang kernel kung mali ang mga modelo.

---

### Memory Context Overflow

**Isyu:** Bumaba ang kalidad ng mga sagot ng agent sa paglipas ng panahon

**Solusyon:** Awtomatikong inaayos - ang mga agent ay nagtatago lamang ng huling 6 na mensahe sa memory.

---

## Mga Isyu sa Session 06

### CPU vs GPU Model Confusion

**Isyu:** Nakakakuha ng CUDA errors kapag ginagamit ang default configuration

**Solusyon:** Ang default configuration ngayon ay gumagamit ng CPU models. Kung makakita ka ng CUDA errors:

1. I-verify na ginagamit mo ang default CPU catalog:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. I-restart ang kernel at i-run muli ang lahat ng cells

---

### Intent Detection Hindi Gumagana

**Isyu:** Ang mga prompt ay napupunta sa maling modelo

**Solusyon:**

Subukan ang intent detection:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

I-update ang RULES kung kailangan ng adjustment sa patterns.

---

## Mga Isyu na Kaugnay sa Hardware

### NVIDIA GPU

**Suriin ang Status ng GPU:**
```bash
nvidia-smi
```

**Karaniwang Isyu:**
- **Driver luma na**: I-update ang NVIDIA drivers
- **CUDA version mismatch**: I-reinstall ang Foundry Local
- **GPU memory fragmented**: I-restart ang system

### Qualcomm NPU

**Suriin ang Status ng NPU:**
```bash
foundry device info
```

**Karaniwang Isyu:**
- **NPU drivers hindi naka-install**: I-install ang Qualcomm NPU drivers
- **NPU variant hindi available**: Gumamit ng CPU variant
- **Windows version luma na**: Mag-update sa pinakabagong Windows 11

### CPU-Only Systems

**Inirerekomendang Mga Modelo:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Mga Tip sa Performance:**
- Gumamit ng pinakamaliit na modelo
- Bawasan ang max_tokens
- Dagdagan ang pasensya para sa unang request

---

## Mga Diagnostic Command

### Suriin ang Lahat
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

### Sa Python
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

## Pagkuha ng Tulong

### 1. Suriin ang Logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Maghanap ng umiiral na mga isyu: https://github.com/microsoft/Foundry-Local/issues
- Gumawa ng bagong isyu gamit ang:
  - Error message (buong teksto)
  - Output ng `foundry service status`
  - Output ng `foundry --version`
  - GPU/NPU info (nvidia-smi, etc.)
  - Mga hakbang para ma-reproduce

### 3. Dokumentasyon
- **Pangunahing Repositoryo**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Checklist ng Mabilisang Pag-aayos

Kapag may problema, subukan ang mga ito sa pagkakasunod-sunod:

- [ ] Suriin kung tumatakbo ang serbisyo: `foundry service status`
- [ ] I-restart ang serbisyo: `foundry service stop && foundry service start`
- [ ] I-verify ang modelo: `foundry model ls | grep phi-4-mini`
- [ ] I-load ang kinakailangang modelo: `foundry model run phi-4-mini`
- [ ] Suriin ang GPU memory: `nvidia-smi` (kung NVIDIA)
- [ ] Subukan ang CPU variant: Gumamit ng `phi-4-mini-cpu` sa halip na `phi-4-mini`
- [ ] I-restart ang notebook kernel
- [ ] I-clear ang notebook outputs at i-run muli ang lahat ng cells
- [ ] I-reinstall ang SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] I-reboot ang system (pinakahuling opsyon)

---

## Mga Tip sa Pag-iwas

### Mga Pinakamahusay na Praktis

1. **Laging suriin ang serbisyo muna:**
   ```bash
   foundry service status
   ```

2. **Gumamit ng CPU variants bilang default:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **I-pre-load ang mga modelo bago mag-run ng notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Panatilihing tumatakbo ang serbisyo:**
   - Huwag basta-basta mag-stop/start ng serbisyo
   - Hayaan itong tumakbo sa background sa pagitan ng mga session

5. **I-monitor ang resources:**
   - Suriin ang GPU memory bago mag-run
   - Isara ang mga hindi kinakailangang GPU applications
   - Gumamit ng Task Manager / nvidia-smi

6. **Mag-update nang regular:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Huling Na-update:** Oktubre 8, 2025

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.