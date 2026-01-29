# Töötuba Märkmikud - Tõrkeotsingu juhend

## Sisukord

- [Levinumad probleemid ja lahendused](../../../../Workshop/notebooks)
- [Sessioon 04 spetsiifilised probleemid](../../../../Workshop/notebooks)
- [Sessioon 05 spetsiifilised probleemid](../../../../Workshop/notebooks)
- [Sessioon 06 spetsiifilised probleemid](../../../../Workshop/notebooks)
- [Riistvaraspetsiifilised probleemid](../../../../Workshop/notebooks)
- [Diagnostika käsud](../../../../Workshop/notebooks)
- [Abi saamine](../../../../Workshop/notebooks)

---

## Levinumad probleemid ja lahendused

### 🔴 CUDA mälu otsas

**Veateade:**
```
CUDA failure 2: out of memory
```

**Põhjus:** GPU-l pole piisavalt VRAM-i mudeli laadimiseks.

**Lahendused:**

#### Variant 1: Kasuta CPU versioone (soovitatav)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Variant 2: Kasuta väiksemaid mudeleid GPU-l
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Variant 3: Tühjenda GPU mälu
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Variant 4: Suurenda GPU mälu (kui võimalik)
- Sulge brauseri vahekaardid, video redaktorid või muud GPU rakendused
- Vähenda Windowsi visuaalseid efekte
- Kasuta eraldiseisvat GPU-d, kui sul on integreeritud + eraldiseisev GPU

---

### 🔴 APIConnectionError: Ühenduse viga

**Veateade:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Põhjus:** Foundry Local teenus ei tööta või pole kättesaadav.

**Lahendused:**

#### Samm 1: Kontrolli teenuse olekut
```bash
foundry service status
```

#### Samm 2: Käivita teenus, kui see on peatatud
```bash
foundry service start
```

#### Samm 3: Kontrolli lõpp-punkti
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Samm 4: Laadi vajalikud mudelid
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Samm 5: Taaskäivita märkmiku kernel
Pärast teenuse käivitamist ja mudelite laadimist taaskäivita märkmiku kernel ja käivita kõik lahtrid uuesti.

---

### 🔴 Mudelit ei leitud kataloogist

**Veateade:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Põhjus:** Mudel pole alla laaditud või Foundry Localis laaditud.

**Lahendused:**

#### Variant 1: Laadi ja käivita mudelid
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

#### Variant 2: Kasuta automaatse valiku režiimi
Uuenda oma CATALOG-i, et kasutada baasmudeli nimesid (ilma `-cpu` järelliiteta):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK valib automaatselt parima variandi (CPU, GPU või NPU) vastavalt riistvarale.

---

### 🔴 HttpResponseError: 500 - Mudeli laadimine ebaõnnestus

**Veateade:**
```
HttpResponseError: 500 - Failed loading model
```

**Põhjus:** Mudelifail on rikutud või riistvaraga kokkusobimatu.

**Lahendused:**

#### Laadi mudel uuesti
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Kasuta teist varianti
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Moodulit ei leitud

**Veateade:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Põhjus:** foundry-local-sdk pakett pole installitud.

**Lahendused:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Esimene päring aeglane

**Sümptom:** Esimene päring võtab 30+ sekundit, järgnevad päringud on kiired.

**Põhjus:** See on normaalne käitumine - teenus laadib mudeli mällu esimesel päringul.

**Lahendused:**

#### Laadi mudelid ette
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Hoia teenus töös
```bash
# Start service manually and leave it running
foundry service start
```

---

## Sessioon 04 spetsiifilised probleemid

### Vale pordi konfiguratsioon

**Probleem:** Märkmik ühendub vale porti (55769 vs 59959 vs 57127)

**Lahendus:**

1. Kontrolli, millist porti Foundry Local kasutab:
```bash
foundry service status
# Note the port number displayed
```

2. Uuenda lahtrit 10 märkmikus:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Taaskäivita kernel ja käivita lahtrid 6, 8, 10, 12, 16, 20, 22 uuesti

---

### Vale mudeli valik

**Probleem:** Märkmik kuvab gpt-oss-20b või qwen2.5-7b asemel qwen2.5-3b

**Lahendus:**

1. Taaskäivita märkmiku kernel (kustutab vana muutujate oleku)
2. Käivita lahter 10 uuesti (Määra mudeli aliased)
3. Käivita lahter 12 uuesti (Kuva konfiguratsioon)
4. **Kontrolli:** Lahter 12 peaks näitama `LLM Model: qwen2.5-3b`

---

### Diagnostika lahter ebaõnnestub

**Probleem:** Lahter 16 kuvab "❌ Foundry Local teenust ei leitud!"

**Lahendus:**

1. Kontrolli, kas teenus töötab:
```bash
foundry service status
```

2. Testi lõpp-punkti käsitsi:
```bash
curl http://localhost:59959/v1/models
```

3. Kui curl töötab, aga märkmik ei tööta:
   - Taaskäivita märkmiku kernel
   - Käivita lahtrid järjekorras: 6, 8, 10, 12, 14, 16

4. Kui curl ei tööta:
   - Käivita teenus: `foundry service start`
   - Laadi mudelid: `foundry model run phi-4-mini` ja `foundry model run qwen2.5-3b`

---

### Eelkontroll ebaõnnestub

**Probleem:** Lahter 20 kuvab ühenduse vead, kuigi diagnostika õnnestus

**Lahendus:**

1. Kontrolli, kas mudelid on laaditud:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Kui mudelid puuduvad:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Käivita lahter 20 uuesti pärast mudelite laadimist

---

### Võrdlus ebaõnnestub None väärtustega

**Probleem:** Lahter 22 lõpetab, kuid kuvab latentsuse kui None

**Lahendus:**

1. Kontrolli, et eelkontroll õnnestus (lahter 20)
2. Käivita lahter 22 uuesti - mudelid võivad vajada esimesel päringul soojenemist
3. Kontrolli, et mõlemad mudelid on laaditud: `foundry model ls`

---

## Sessioon 05 spetsiifilised probleemid

### Agent kasutab vale mudelit

**Probleem:** Agent ei kasuta oodatud mudelit

**Lahendus:**

Kontrolli konfiguratsiooni:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Taaskäivita kernel, kui mudelid on valed.

---

### Mälu konteksti ületäitumine

**Probleem:** Agendi vastused halvenevad aja jooksul

**Lahendus:** Juba automaatselt lahendatud - agendid hoiavad mälus ainult viimased 6 sõnumit.

---

## Sessioon 06 spetsiifilised probleemid

### CPU vs GPU mudeli segadus

**Probleem:** CUDA vead ilmnevad, kui kasutatakse vaikekonfiguratsiooni

**Lahendus:** Vaikekonfiguratsioon kasutab nüüd CPU mudeleid. Kui näed CUDA vigu:

1. Kontrolli, et kasutad vaikimisi CPU kataloogi:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Taaskäivita kernel ja käivita kõik lahtrid uuesti

---

### Kavatsuste tuvastamine ei tööta

**Probleem:** Käsud suunatakse valedele mudelitele

**Lahendus:**

Testi kavatsuste tuvastamist:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Uuenda REEGLID, kui mustrid vajavad kohandamist.

---

## Riistvaraspetsiifilised probleemid

### NVIDIA GPU

**Kontrolli GPU olekut:**
```bash
nvidia-smi
```

**Levinumad probleemid:**
- **Draiver aegunud**: Uuenda NVIDIA draivereid
- **CUDA versiooni sobimatus**: Paigalda Foundry Local uuesti
- **GPU mälu killustunud**: Taaskäivita süsteem

### Qualcomm NPU

**Kontrolli NPU olekut:**
```bash
foundry device info
```

**Levinumad probleemid:**
- **NPU draiverid pole installitud**: Paigalda Qualcomm NPU draiverid
- **NPU variant pole saadaval**: Kasuta CPU varianti
- **Windowsi versioon liiga vana**: Uuenda uusimale Windows 11 versioonile

### Ainult CPU süsteemid

**Soovitatud mudelid:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Jõudluse näpunäited:**
- Kasuta väikseimaid mudeleid
- Vähenda max_tokens väärtust
- Ole kannatlik esimese päringu puhul

---

## Diagnostika käsud

### Kontrolli kõike
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

### Pythonis
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

## Abi saamine

### 1. Kontrolli logisid
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHubi probleemid
- Otsi olemasolevaid probleeme: https://github.com/microsoft/Foundry-Local/issues
- Loo uus probleem koos:
  - Veateade (täistekst)
  - `foundry service status` väljund
  - `foundry --version` väljund
  - GPU/NPU info (nvidia-smi jne)
  - Sammud probleemi taastamiseks

### 3. Dokumentatsioon
- **Peamine repo:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI viide:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Tõrkeotsing:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Kiirparanduste kontrollnimekiri

Kui midagi läheb valesti, proovi neid järjekorras:

- [ ] Kontrolli, kas teenus töötab: `foundry service status`
- [ ] Taaskäivita teenus: `foundry service stop && foundry service start`
- [ ] Kontrolli, kas mudel eksisteerib: `foundry model ls | grep phi-4-mini`
- [ ] Laadi vajalikud mudelid: `foundry model run phi-4-mini`
- [ ] Kontrolli GPU mälu: `nvidia-smi` (kui NVIDIA)
- [ ] Proovi CPU varianti: Kasuta `phi-4-mini-cpu` asemel `phi-4-mini`
- [ ] Taaskäivita märkmiku kernel
- [ ] Tühjenda märkmiku väljundid ja käivita kõik lahtrid uuesti
- [ ] Paigalda SDK uuesti: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Taaskäivita süsteem (viimane võimalus)

---

## Ennetamise näpunäited

### Parimad praktikad

1. **Kontrolli alati esmalt teenust:**
   ```bash
   foundry service status
   ```

2. **Kasuta vaikimisi CPU variante:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Laadi mudelid enne märkmike käivitamist:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Hoia teenus töös:**
   - Ära peata/käivita teenust tarbetult
   - Lase sel töötada taustal sessioonide vahel

5. **Jälgi ressursse:**
   - Kontrolli GPU mälu enne käivitamist
   - Sulge mittevajalikud GPU rakendused
   - Kasuta Task Manageri / nvidia-smi

6. **Uuenda regulaarselt:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Viimati uuendatud:** 8. oktoober 2025

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.