# Mwongozo wa Haraka wa Workshop Notebooks

## Jedwali la Maudhui

- [Mahitaji ya Awali](../../../../Workshop/notebooks)
- [Usanidi wa Awali](../../../../Workshop/notebooks)
- [Kikao 04: Ulinganisho wa Miundo](../../../../Workshop/notebooks)
- [Kikao 05: Msimamizi wa Wakala Wengi](../../../../Workshop/notebooks)
- [Kikao 06: Uelekezaji wa Miundo kwa Msingi wa Nia](../../../../Workshop/notebooks)
- [Vigezo vya Mazingira](../../../../Workshop/notebooks)
- [Amri za Kawaida](../../../../Workshop/notebooks)

---

## Mahitaji ya Awali

### 1. Sakinisha Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Thibitisha Usakinishaji:**
```bash
foundry --version
```

### 2. Sakinisha Maktaba za Python

```bash
cd Workshop
pip install -r requirements.txt
```

Au sakinisha moja moja:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Usanidi wa Awali

### Anzisha Huduma ya Foundry Local

**Inahitajika kabla ya kuendesha daftari lolote:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Matokeo yanayotarajiwa:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Pakua na Pakia Miundo

Daftari hutumia miundo hii kwa chaguo-msingi:

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

### Thibitisha Usanidi

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Kikao 04: Ulinganisho wa Miundo

### Kusudi
Linganisheni utendaji kati ya Miundo Midogo ya Lugha (SLM) na Miundo Mikubwa ya Lugha (LLM).

### Usanidi wa Haraka

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Kuendesha Daftari

1. **Fungua** `session04_model_compare.ipynb` kwenye VS Code au Jupyter
2. **Anzisha upya kernel** (Kernel → Restart Kernel)
3. **Endesha seli zote** kwa mpangilio

### Usanidi Muhimu

**Miundo ya Chaguo-msingi:**
- **SLM:** `phi-4-mini` (~4GB RAM, haraka)
- **LLM:** `qwen2.5-3b` (~3GB RAM, imeboreshwa kwa kumbukumbu)

**Vigezo vya Mazingira (hiari):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Matokeo Yanayotarajiwa

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

### Kubinafsisha

**Tumia miundo tofauti:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Mwongozo maalum:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Orodha ya Uthibitishaji

- [ ] Seli ya 12 inaonyesha miundo sahihi (phi-4-mini, qwen2.5-3b)
- [ ] Seli ya 12 inaonyesha endpoint sahihi (bandari 59959)
- [ ] Seli ya 16 uchunguzi unafaulu (✅ Huduma inaendesha)
- [ ] Seli ya 20 ukaguzi wa awali unafaulu (miundo yote sawa)
- [ ] Seli ya 22 ulinganisho unakamilika na thamani za ucheleweshaji
- [ ] Seli ya 24 uthibitishaji unaonyesha 🎉 UKAGUZI WOTE UMEPITA!

### Makadirio ya Muda
- **Mara ya kwanza:** Dakika 5-10 (pamoja na upakuaji wa miundo)
- **Mara zinazofuata:** Dakika 1-2

---

## Kikao 05: Msimamizi wa Wakala Wengi

### Kusudi
Onyesha ushirikiano wa wakala wengi kwa kutumia Foundry Local SDK - mawakala hufanya kazi pamoja kutoa matokeo yaliyoboreshwa.

### Usanidi wa Haraka

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Kuendesha Daftari

1. **Fungua** `session05_agents_orchestrator.ipynb`
2. **Anzisha upya kernel**
3. **Endesha seli zote** kwa mpangilio

### Usanidi Muhimu

**Usanidi wa Chaguo-msingi (Model Moja kwa Mawakala Wote):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Usanidi wa Juu (Miundo Tofauti):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Muundo

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

### Matokeo Yanayotarajiwa

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

### Nyongeza

**Ongeza mawakala zaidi:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Upimaji wa kundi:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Makadirio ya Muda
- **Mara ya kwanza:** Dakika 3-5
- **Mara zinazofuata:** Dakika 1-2 kwa swali

---

## Kikao 06: Uelekezaji wa Miundo kwa Msingi wa Nia

### Kusudi
Elekeza kwa busara maelekezo kwa miundo maalum kulingana na nia iliyogunduliwa.

### Usanidi wa Haraka

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Kumbuka:** Kikao cha 06 kinatumia miundo ya CPU kwa utangamano wa juu zaidi.

### Kuendesha Daftari

1. **Fungua** `session06_models_router.ipynb`
2. **Anzisha upya kernel**
3. **Endesha seli zote** kwa mpangilio

### Usanidi Muhimu

**Katalogi ya Chaguo-msingi (Miundo ya CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Mbadala (Miundo ya GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Ugunduzi wa Nia

Router hutumia mifumo ya regex kugundua nia:

| Nia | Mifano ya Mifumo | Inaelekezwa Kwa |
|-----|------------------|-----------------|
| `code` | "rekebisha", "tekeleza kazi" | phi-3.5-mini-cpu |
| `classification` | "ainisha", "ainisha hili" | qwen2.5-0.5b-cpu |
| `summarize` | "fupisha", "tl;dr" | phi-4-mini-cpu |
| `general` | Kila kitu kingine | phi-4-mini-cpu |

### Matokeo Yanayotarajiwa

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

### Kubinafsisha

**Ongeza nia maalum:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Wezesha ufuatiliaji wa tokeni:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Kubadilisha Miundo ya GPU

Ikiwa una 8GB+ VRAM:

1. Katika **Seli #6**, toa maoni katalogi ya CPU
2. Ondoa maoni katalogi ya GPU
3. Pakia miundo ya GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Anzisha upya kernel na endesha tena daftari

### Makadirio ya Muda
- **Mara ya kwanza:** Dakika 5-10 (upakiaji wa miundo)
- **Mara zinazofuata:** Sekunde 30-60 kwa kila jaribio

---

## Vigezo vya Mazingira

### Usanidi wa Kimataifa

Weka kabla ya kuanza Jupyter/VS Code:

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

### Usanidi Ndani ya Daftari

Weka mwanzoni mwa daftari lolote:

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

## Amri za Kawaida

### Usimamizi wa Huduma

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

### Usimamizi wa Miundo

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

### Kupima Endpoints

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

### Amri za Uchunguzi

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

## Mazoea Bora

### Kabla ya Kuanza Daftari Lolote

1. **Hakikisha huduma inaendesha:**
   ```bash
   foundry service status
   ```

2. **Thibitisha miundo imepakia:**
   ```bash
   foundry model ls
   ```

3. **Anzisha upya kernel ya daftari** ikiwa unaendesha tena

4. **Futa matokeo yote** kwa uendeshaji safi

### Usimamizi wa Rasilimali

1. **Tumia miundo ya CPU kwa chaguo-msingi** kwa utangamano
2. **Badilisha miundo ya GPU** tu ikiwa una 8GB+ VRAM
3. **Funga programu nyingine za GPU** kabla ya kuendesha
4. **Weka huduma ikiendesha** kati ya vikao vya daftari
5. **Fuatilia matumizi ya rasilimali** kwa Task Manager / nvidia-smi

### Utatuzi wa Matatizo

1. **Kagua huduma kila wakati kwanza** kabla ya kutatua matatizo ya msimbo
2. **Anzisha upya kernel** ikiwa unaona usanidi wa zamani
3. **Endesha tena seli za uchunguzi** baada ya mabadiliko yoyote
4. **Hakikisha majina ya miundo** yanalingana na yaliyo pakia
5. **Thibitisha bandari ya endpoint** inalingana na hali ya huduma

---

## Marejeleo ya Haraka: Majina ya Miundo

### Miundo ya Kawaida

| Jina | Ukubwa | Bora Kwa | RAM/VRAM | Aina |
|------|-------|----------|----------|------|
| `phi-4-mini` | ~4B | Mazungumzo ya jumla, ufupishaji | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Uzalishaji wa msimbo, marekebisho | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Kazi za jumla, ufanisi | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Haraka, rasilimali ndogo | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Uainishaji, rasilimali ndogo | 1-2GB | `-cpu`, `-cuda-gpu` |

### Jina la Aina

- **Jina la msingi** (mfano, `phi-4-mini`): Huchagua kiotomatiki aina bora kwa vifaa vyako
- **`-cpu`**: Imeboreshwa kwa CPU, inafanya kazi kila mahali
- **`-cuda-gpu`**: Imeboreshwa kwa NVIDIA GPU, inahitaji 8GB+ VRAM
- **`-npu`**: Imeboreshwa kwa Qualcomm NPU, inahitaji madereva ya NPU

**Pendekezo:** Tumia majina ya msingi (bila kiambishi) na acha Foundry Local ichague kiotomatiki aina bora.

---

## Viashiria vya Mafanikio

Uko tayari unapoona:

✅ `foundry service status` inaonyesha "inaendesha"
✅ `foundry model ls` inaonyesha miundo unayohitaji
✅ Huduma inapatikana kwenye endpoint sahihi
✅ Ukaguzi wa afya unarudisha 200 OK
✅ Seli za uchunguzi wa daftari zinapita
✅ Hakuna makosa ya muunganisho kwenye matokeo

---

## Kupata Msaada

### Nyaraka
- **Hifadhi Kuu:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Marejeleo ya CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Utatuzi wa Matatizo:** Tazama `troubleshooting.md` kwenye folda hii

### Masuala ya GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Imeboreshwa Mwisho:** Oktoba 8, 2025  
**Toleo:** Workshop Notebooks 2.0

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.