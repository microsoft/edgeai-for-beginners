# Workshop Notebooks - Mwongozo wa Kutatua Matatizo

## Jedwali la Maudhui

- [Masuala ya Kawaida na Suluhisho](../../../../Workshop/notebooks)
- [Masuala Maalum ya Kipindi cha 04](../../../../Workshop/notebooks)
- [Masuala Maalum ya Kipindi cha 05](../../../../Workshop/notebooks)
- [Masuala Maalum ya Kipindi cha 06](../../../../Workshop/notebooks)
- [Masuala Maalum ya Vifaa](../../../../Workshop/notebooks)
- [Amri za Uchunguzi](../../../../Workshop/notebooks)
- [Kupata Msaada](../../../../Workshop/notebooks)

---

## Masuala ya Kawaida na Suluhisho

### 🔴 CUDA Out of Memory

**Ujumbe wa Kosa:**
```
CUDA failure 2: out of memory
```

**Chanzo:** GPU haina VRAM ya kutosha kupakia modeli.

**Suluhisho:**

#### Chaguo 1: Tumia Aina za CPU (Inapendekezwa)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Chaguo 2: Tumia Modeli Ndogo kwenye GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Chaguo 3: Futa Kumbukumbu ya GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Chaguo 4: Ongeza Kumbukumbu ya GPU (ikiwa inawezekana)
- Funga tabo za kivinjari, wahariri wa video, au programu nyingine za GPU
- Punguza athari za kuona za Windows
- Tumia GPU iliyojitolea ikiwa una GPU iliyojumuishwa + iliyojitolea

---

### 🔴 APIConnectionError: Connection Error

**Ujumbe wa Kosa:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Chanzo:** Huduma ya Foundry Local haifanyi kazi au haifikiki.

**Suluhisho:**

#### Hatua 1: Angalia Hali ya Huduma
```bash
foundry service status
```

#### Hatua 2: Anzisha Huduma Ikiwa Imezimwa
```bash
foundry service start
```

#### Hatua 3: Thibitisha Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Hatua 4: Pakia Modeli Zinazohitajika
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Hatua 5: Washa Upya Kernel ya Notebook
Baada ya kuanzisha huduma na kupakia modeli, washa upya kernel ya notebook na uendeshe seli zote tena.

---

### 🔴 Model Not Found in Catalog

**Ujumbe wa Kosa:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Chanzo:** Modeli haijapakuliwa au kupakiwa kwenye Foundry Local.

**Suluhisho:**

#### Chaguo 1: Pakua na Pakia Modeli
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

#### Chaguo 2: Tumia Hali ya Uchaguzi wa Kiotomatiki
Sasisha CATALOG yako kutumia majina ya modeli ya msingi (bila kiambishi awali `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK itachagua kiotomatiki aina bora (CPU, GPU, au NPU) kwa vifaa vyako.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Ujumbe wa Kosa:**
```
HttpResponseError: 500 - Failed loading model
```

**Chanzo:** Faili ya modeli imeharibika au haipatani na vifaa.

**Suluhisho:**

#### Pakua Modeli Tena
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Tumia Aina Tofauti
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Ujumbe wa Kosa:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Chanzo:** kifurushi cha foundry-local-sdk hakijasakinishwa.

**Suluhisho:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Ombi la Kwanza Lenye Polepole

**Dalili:** Kukamilisha kwa mara ya kwanza kunachukua sekunde 30+, maombi yanayofuata ni ya haraka.

**Chanzo:** Hii ni tabia ya kawaida - huduma inapakua modeli kwenye kumbukumbu kwa ombi la kwanza.

**Suluhisho:**

#### Pakia Modeli Kabla
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Weka Huduma Ikiwa Inaendelea
```bash
# Start service manually and leave it running
foundry service start
```

---

## Masuala Maalum ya Kipindi cha 04

### Usanidi Mbaya wa Bandari

**Tatizo:** Notebook inaunganisha kwenye bandari isiyo sahihi (55769 vs 59959 vs 57127)

**Suluhisho:**

1. Angalia ni bandari gani Foundry Local inatumia:
```bash
foundry service status
# Note the port number displayed
```

2. Sasisha Seli ya 10 kwenye notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Washa upya kernel na uendeshe seli 6, 8, 10, 12, 16, 20, 22 tena

---

### Uchaguzi Mbaya wa Modeli

**Tatizo:** Notebook inaonyesha gpt-oss-20b au qwen2.5-7b badala ya qwen2.5-3b

**Suluhisho:**

1. Washa upya kernel ya notebook (inafuta hali ya zamani ya variable)
2. Endesha Seli ya 10 tena (Weka Majina ya Modeli)
3. Endesha Seli ya 12 tena (Onyesha Usanidi)
4. **Thibitisha:** Seli ya 12 inapaswa kuonyesha `LLM Model: qwen2.5-3b`

---

### Seli ya Uchunguzi Inashindwa

**Tatizo:** Seli ya 16 inaonyesha "❌ Foundry Local service not found!"

**Suluhisho:**

1. Thibitisha huduma inafanya kazi:
```bash
foundry service status
```

2. Jaribu endpoint kwa mkono:
```bash
curl http://localhost:59959/v1/models
```

3. Ikiwa curl inafanya kazi lakini notebook haifanyi:
   - Washa upya kernel ya notebook
   - Endesha seli kwa mpangilio: 6, 8, 10, 12, 14, 16

4. Ikiwa curl inashindwa:
   - Anzisha huduma: `foundry service start`
   - Pakia modeli: `foundry model run phi-4-mini` na `foundry model run qwen2.5-3b`

---

### Ukaguzi wa Awali Unashindwa

**Tatizo:** Seli ya 20 inaonyesha makosa ya muunganisho ingawa uchunguzi umepita

**Suluhisho:**

1. Angalia modeli zimepakiwa:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Ikiwa modeli hazipo:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Endesha Seli ya 20 tena baada ya modeli kupakiwa

---

### Ulinganisho Unashindwa na Thamani za None

**Tatizo:** Seli ya 22 inakamilika lakini inaonyesha latency kama None

**Suluhisho:**

1. Angalia kwamba ukaguzi wa awali umepita kwanza (Seli ya 20)
2. Endesha Seli ya 22 tena - modeli zinaweza kuhitaji kupasha moto kwa ombi la kwanza
3. Thibitisha modeli zote zimepakiwa: `foundry model ls`

---

## Masuala Maalum ya Kipindi cha 05

### Wakala Anatumia Modeli Mbaya

**Tatizo:** Wakala hatumii modeli inayotarajiwa

**Suluhisho:**

Thibitisha usanidi:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Washa upya kernel ikiwa modeli si sahihi.

---

### Kumbukumbu ya Muktadha Inazidi

**Tatizo:** Majibu ya wakala yanapungua ubora kadri muda unavyosonga

**Suluhisho:** Tayari imeshughulikiwa kiotomatiki - mawakala wanahifadhi tu ujumbe 6 wa mwisho kwenye kumbukumbu.

---

## Masuala Maalum ya Kipindi cha 06

### Mkanganyiko wa Modeli ya CPU vs GPU

**Tatizo:** Kupata makosa ya CUDA wakati wa kutumia usanidi wa chaguo-msingi

**Suluhisho:** Usanidi wa chaguo-msingi sasa unatumia modeli za CPU. Ikiwa unaona makosa ya CUDA:

1. Thibitisha unatumia katalogi ya CPU ya chaguo-msingi:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Washa upya kernel na uendeshe seli zote tena

---

### Utambuzi wa Nia Haufanyi Kazi

**Tatizo:** Maelekezo yanapelekwa kwenye modeli zisizo sahihi

**Suluhisho:**

Jaribu utambuzi wa nia:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Sasisha RULES ikiwa mifumo inahitaji marekebisho.

---

## Masuala Maalum ya Vifaa

### NVIDIA GPU

**Angalia Hali ya GPU:**
```bash
nvidia-smi
```

**Masuala ya Kawaida:**
- **Dereva imepitwa na wakati**: Sasisha madereva ya NVIDIA
- **Toleo la CUDA halilingani**: Sakinisha tena Foundry Local
- **Kumbukumbu ya GPU imegawanyika**: Washa upya mfumo

### Qualcomm NPU

**Angalia Hali ya NPU:**
```bash
foundry device info
```

**Masuala ya Kawaida:**
- **Madereva ya NPU hayajasakinishwa**: Sakinisha madereva ya Qualcomm NPU
- **Aina ya NPU haipatikani**: Tumia aina ya CPU
- **Toleo la Windows ni la zamani sana**: Sasisha hadi Windows 11 ya hivi karibuni

### Mifumo ya CPU Pekee

**Modeli Zinazopendekezwa:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Vidokezo vya Utendaji:**
- Tumia modeli ndogo zaidi
- Punguza max_tokens
- Kuwa na subira kwa ombi la kwanza

---

## Amri za Uchunguzi

### Angalia Kila Kitu
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

### Katika Python
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

## Kupata Msaada

### 1. Angalia Magogo
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Masuala ya GitHub
- Tafuta masuala yaliyopo: https://github.com/microsoft/Foundry-Local/issues
- Unda suala jipya na:
  - Ujumbe wa kosa (maandishi kamili)
  - Matokeo ya `foundry service status`
  - Matokeo ya `foundry --version`
  - Taarifa za GPU/NPU (nvidia-smi, nk.)
  - Hatua za kuzalisha tatizo

### 3. Nyaraka
- **Hifadhi Kuu**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Marejeleo ya CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Kutatua Matatizo**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Orodha ya Haraka ya Marekebisho

Wakati mambo yanakwenda vibaya, jaribu haya kwa mpangilio:

- [ ] Angalia huduma inafanya kazi: `foundry service status`
- [ ] Anzisha upya huduma: `foundry service stop && foundry service start`
- [ ] Thibitisha modeli ipo: `foundry model ls | grep phi-4-mini`
- [ ] Pakia modeli zinazohitajika: `foundry model run phi-4-mini`
- [ ] Angalia kumbukumbu ya GPU: `nvidia-smi` (ikiwa NVIDIA)
- [ ] Jaribu aina ya CPU: Tumia `phi-4-mini-cpu` badala ya `phi-4-mini`
- [ ] Washa upya kernel ya notebook
- [ ] Futa matokeo ya notebook na uendeshe seli zote tena
- [ ] Sakinisha tena SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Washa upya mfumo (hatua ya mwisho)

---

## Vidokezo vya Kuzuia

### Mazoea Bora

1. **Daima angalia huduma kwanza:**
   ```bash
   foundry service status
   ```

2. **Tumia aina za CPU kwa chaguo-msingi:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pakia modeli kabla ya kuendesha notebook:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Weka huduma ikiwa inaendelea:**
   - Usizime/anzishe huduma bila sababu
   - Iache iendelee kufanya kazi nyuma kati ya vipindi

5. **Fuatilia rasilimali:**
   - Angalia kumbukumbu ya GPU kabla ya kuendesha
   - Funga programu za GPU zisizo za lazima
   - Tumia Task Manager / nvidia-smi

6. **Sasisha mara kwa mara:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Ilisasishwa Mwisho:** Oktoba 8, 2025

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.