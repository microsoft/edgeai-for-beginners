# Seminarų Užrašai - Trikčių Šalinimo Vadovas

## Turinys

- [Dažnos problemos ir sprendimai](../../../../Workshop/notebooks)
- [4-os sesijos specifinės problemos](../../../../Workshop/notebooks)
- [5-os sesijos specifinės problemos](../../../../Workshop/notebooks)
- [6-os sesijos specifinės problemos](../../../../Workshop/notebooks)
- [Problemos, susijusios su aparatine įranga](../../../../Workshop/notebooks)
- [Diagnostikos komandos](../../../../Workshop/notebooks)
- [Pagalbos gavimas](../../../../Workshop/notebooks)

---

## Dažnos problemos ir sprendimai

### 🔴 CUDA atminties trūkumas

**Klaidos pranešimas:**
```
CUDA failure 2: out of memory
```
  
**Priežastis:** GPU neturi pakankamai VRAM, kad įkeltų modelį.

**Sprendimai:**

#### 1 variantas: Naudokite CPU modelius (rekomenduojama)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### 2 variantas: Naudokite mažesnius modelius GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### 3 variantas: Išvalykite GPU atmintį
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### 4 variantas: Padidinkite GPU atmintį (jei įmanoma)
- Uždarykite naršyklės skirtukus, vaizdo redaktorius ar kitas GPU programas
- Sumažinkite „Windows“ vizualinius efektus
- Naudokite dedikuotą GPU, jei turite integruotą + dedikuotą

---

### 🔴 APIConnectionError: Ryšio klaida

**Klaidos pranešimas:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Priežastis:** Foundry Local paslauga neveikia arba nėra pasiekiama.

**Sprendimai:**

#### 1 žingsnis: Patikrinkite paslaugos būseną
```bash
foundry service status
```
  
#### 2 žingsnis: Paleiskite paslaugą, jei ji sustabdyta
```bash
foundry service start
```
  
#### 3 žingsnis: Patikrinkite galinį tašką
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### 4 žingsnis: Įkelkite reikiamus modelius
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### 5 žingsnis: Paleiskite iš naujo užrašų knygelės branduolį  
Po paslaugos paleidimo ir modelių įkėlimo, paleiskite iš naujo užrašų knygelės branduolį ir vykdykite visas ląsteles.

---

### 🔴 Modelis nerastas kataloge

**Klaidos pranešimas:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Priežastis:** Modelis nėra atsisiųstas arba įkeltas į Foundry Local.

**Sprendimai:**

#### 1 variantas: Atsisiųskite ir įkelkite modelius
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
  
#### 2 variantas: Naudokite automatinio pasirinkimo režimą  
Atnaujinkite savo CATALOG, kad naudotumėte bazinius modelių pavadinimus (be `-cpu` priesagos):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK automatiškai parinks geriausią variantą (CPU, GPU ar NPU) pagal jūsų aparatinę įrangą.

---

### 🔴 HttpResponseError: 500 - Nepavyko įkelti modelio

**Klaidos pranešimas:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Priežastis:** Modelio failas sugadintas arba nesuderinamas su aparatine įranga.

**Sprendimai:**

#### Perkraukite modelį
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Naudokite kitą variantą
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: Modulis nerastas

**Klaidos pranešimas:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Priežastis:** foundry-local-sdk paketas nėra įdiegtas.

**Sprendimai:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Lėtas pirmasis užklausos vykdymas

**Simptomas:** Pirmasis užklausos vykdymas trunka 30+ sekundžių, vėlesnės užklausos vykdomos greitai.

**Priežastis:** Tai normalu - paslauga pirmą kartą įkelia modelį į atmintį.

**Sprendimai:**

#### Iš anksto įkelkite modelius
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Palikite paslaugą veikti
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## 4-os sesijos specifinės problemos

### Neteisinga prievado konfigūracija

**Problema:** Užrašų knygelė jungiasi prie neteisingo prievado (55769 vs 59959 vs 57127)

**Sprendimas:**

1. Patikrinkite, kurį prievadą naudoja Foundry Local:
```bash
foundry service status
# Note the port number displayed
```
  
2. Atnaujinkite 10-ąją ląstelę užrašų knygelėje:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Paleiskite branduolį iš naujo ir vykdykite ląsteles: 6, 8, 10, 12, 16, 20, 22

---

### Neteisingas modelio pasirinkimas

**Problema:** Užrašų knygelė rodo gpt-oss-20b arba qwen2.5-7b vietoj qwen2.5-3b

**Sprendimas:**

1. Paleiskite užrašų knygelės branduolį iš naujo (išvalo seną kintamųjų būseną)
2. Vykdykite 10-ąją ląstelę (Nustatyti modelio aliasus)
3. Vykdykite 12-ąją ląstelę (Rodyti konfigūraciją)
4. **Patikrinkite:** 12-oji ląstelė turėtų rodyti `LLM Model: qwen2.5-3b`

---

### Diagnostikos ląstelė neveikia

**Problema:** 16-oji ląstelė rodo "❌ Foundry Local paslauga nerasta!"

**Sprendimas:**

1. Patikrinkite, ar paslauga veikia:
```bash
foundry service status
```
  
2. Išbandykite galinį tašką rankiniu būdu:
```bash
curl http://localhost:59959/v1/models
```
  
3. Jei curl veikia, bet užrašų knygelė neveikia:
   - Paleiskite užrašų knygelės branduolį iš naujo
   - Vykdykite ląsteles iš eilės: 6, 8, 10, 12, 14, 16

4. Jei curl neveikia:
   - Paleiskite paslaugą: `foundry service start`
   - Įkelkite modelius: `foundry model run phi-4-mini` ir `foundry model run qwen2.5-3b`

---

### Priešskrydžio patikra nepavyksta

**Problema:** 20-oji ląstelė rodo ryšio klaidas, nors diagnostika praėjo

**Sprendimas:**

1. Patikrinkite, ar modeliai įkelti:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Jei modelių trūksta:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Vykdykite 20-ąją ląstelę po modelių įkėlimo

---

### Palyginimas nepavyksta su None reikšmėmis

**Problema:** 22-oji ląstelė baigia vykdymą, bet rodo vėlinimą kaip None

**Sprendimas:**

1. Patikrinkite, ar priešskrydžio patikra praėjo (20-oji ląstelė)
2. Vykdykite 22-ąją ląstelę - modeliams gali reikėti sušilti pirmosios užklausos metu
3. Patikrinkite, ar abu modeliai įkelti: `foundry model ls`

---

## 5-os sesijos specifinės problemos

### Agentas naudoja neteisingą modelį

**Problema:** Agentas nenaudoja tikėtino modelio

**Sprendimas:**

Patikrinkite konfigūraciją:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Paleiskite branduolį iš naujo, jei modeliai neteisingi.

---

### Atminties konteksto perpildymas

**Problema:** Agentų atsakymai blogėja laikui bėgant

**Sprendimas:** Jau automatiškai tvarkoma - agentai saugo tik paskutinius 6 pranešimus atmintyje.

---

## 6-os sesijos specifinės problemos

### CPU vs GPU modelių painiava

**Problema:** Gaunate CUDA klaidas, kai naudojate numatytąją konfigūraciją

**Sprendimas:** Numatytoji konfigūracija dabar naudoja CPU modelius. Jei matote CUDA klaidas:

1. Patikrinkite, ar naudojate numatytąjį CPU katalogą:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Paleiskite branduolį iš naujo ir vykdykite visas ląsteles

---

### Ketinimų aptikimas neveikia

**Problema:** Užklausos nukreipiamos į neteisingus modelius

**Sprendimas:**

Išbandykite ketinimų aptikimą:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Atnaujinkite RULES, jei reikia koreguoti šablonus.

---

## Problemos, susijusios su aparatine įranga

### NVIDIA GPU

**Patikrinkite GPU būseną:**
```bash
nvidia-smi
```
  
**Dažnos problemos:**
- **Pasenę tvarkyklės:** Atnaujinkite NVIDIA tvarkykles
- **CUDA versijos neatitikimas:** Iš naujo įdiekite Foundry Local
- **GPU atmintis suskaidyta:** Paleiskite sistemą iš naujo

### Qualcomm NPU

**Patikrinkite NPU būseną:**
```bash
foundry device info
```
  
**Dažnos problemos:**
- **NPU tvarkyklės neįdiegtos:** Įdiekite Qualcomm NPU tvarkykles
- **NPU variantas nepasiekiamas:** Naudokite CPU variantą
- **Windows versija per sena:** Atnaujinkite į naujausią Windows 11

### Tik CPU sistemos

**Rekomenduojami modeliai:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Našumo patarimai:**
- Naudokite mažiausius modelius
- Sumažinkite max_tokens
- Būkite kantrūs pirmosios užklausos metu

---

## Diagnostikos komandos

### Patikrinkite viską
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
  
### Python'e
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

## Pagalbos gavimas

### 1. Patikrinkite žurnalus
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub problemos
- Ieškokite esamų problemų: https://github.com/microsoft/Foundry-Local/issues
- Sukurkite naują problemą su:
  - Klaidos pranešimu (pilnas tekstas)
  - `foundry service status` išvestimi
  - `foundry --version` išvestimi
  - GPU/NPU informacija (nvidia-smi ir kt.)
  - Žingsniais, kaip atkurti problemą

### 3. Dokumentacija
- **Pagrindinis saugykla:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI nuoroda:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Trikčių šalinimas:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Greitų sprendimų kontrolinis sąrašas

Kai kyla problemų, išbandykite šiuos veiksmus iš eilės:

- [ ] Patikrinkite, ar paslauga veikia: `foundry service status`
- [ ] Paleiskite paslaugą iš naujo: `foundry service stop && foundry service start`
- [ ] Patikrinkite, ar modelis egzistuoja: `foundry model ls | grep phi-4-mini`
- [ ] Įkelkite reikiamus modelius: `foundry model run phi-4-mini`
- [ ] Patikrinkite GPU atmintį: `nvidia-smi` (jei NVIDIA)
- [ ] Išbandykite CPU variantą: Naudokite `phi-4-mini-cpu` vietoj `phi-4-mini`
- [ ] Paleiskite užrašų knygelės branduolį iš naujo
- [ ] Išvalykite užrašų knygelės išvestis ir vykdykite visas ląsteles iš naujo
- [ ] Iš naujo įdiekite SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Paleiskite sistemą iš naujo (paskutinė priemonė)

---

## Prevencijos patarimai

### Geriausia praktika

1. **Visada pirmiausia patikrinkite paslaugą:**
   ```bash
   foundry service status
   ```
  
2. **Naudokite CPU variantus pagal numatymą:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Iš anksto įkelkite modelius prieš vykdant užrašų knygeles:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Palikite paslaugą veikti:**
   - Nenaudokite paslaugos sustabdymo/paleidimo be reikalo
   - Leiskite jai veikti fone tarp sesijų

5. **Stebėkite išteklius:**
   - Patikrinkite GPU atmintį prieš vykdymą
   - Uždarykite nereikalingas GPU programas
   - Naudokite „Task Manager“ / nvidia-smi

6. **Reguliariai atnaujinkite:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Paskutinį kartą atnaujinta:** 2025 m. spalio 8 d.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.