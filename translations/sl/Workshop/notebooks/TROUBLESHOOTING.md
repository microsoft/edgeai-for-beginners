# Delovni zvezki - Vodnik za odpravljanje težav

## Kazalo

- [Pogoste težave in rešitve](../../../../Workshop/notebooks)
- [Težave specifične za sejo 04](../../../../Workshop/notebooks)
- [Težave specifične za sejo 05](../../../../Workshop/notebooks)
- [Težave specifične za sejo 06](../../../../Workshop/notebooks)
- [Težave specifične za strojno opremo](../../../../Workshop/notebooks)
- [Diagnostični ukazi](../../../../Workshop/notebooks)
- [Pomoč](../../../../Workshop/notebooks)

---

## Pogoste težave in rešitve

### 🔴 CUDA Out of Memory

**Sporočilo o napaki:**
```
CUDA failure 2: out of memory
```

**Vzrok:** GPU nima dovolj VRAM-a za nalaganje modela.

**Rešitve:**

#### Možnost 1: Uporabite CPU različice (priporočeno)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Možnost 2: Uporabite manjše modele na GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Možnost 3: Počistite pomnilnik GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Možnost 4: Povečajte pomnilnik GPU (če je mogoče)
- Zaprite zavihke brskalnika, video urejevalnike ali druge aplikacije, ki uporabljajo GPU
- Zmanjšajte vizualne učinke v Windows
- Uporabite namenski GPU, če imate integriran + namenski GPU

---

### 🔴 APIConnectionError: Connection Error

**Sporočilo o napaki:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Vzrok:** Storitev Foundry Local ne deluje ali ni dostopna.

**Rešitve:**

#### Korak 1: Preverite stanje storitve
```bash
foundry service status
```

#### Korak 2: Zaženite storitev, če je ustavljena
```bash
foundry service start
```

#### Korak 3: Preverite končno točko
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Korak 4: Naložite potrebne modele
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Korak 5: Znova zaženite jedro zvezka
Po zagonu storitve in nalaganju modelov znova zaženite jedro zvezka in ponovno zaženite vse celice.

---

### 🔴 Model ni najden v katalogu

**Sporočilo o napaki:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Vzrok:** Model ni prenesen ali naložen v Foundry Local.

**Rešitve:**

#### Možnost 1: Prenesite in naložite modele
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

#### Možnost 2: Uporabite način samodejne izbire
Posodobite svoj CATALOG, da uporabite osnovna imena modelov (brez pripone `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK bo samodejno izbral najboljšo različico (CPU, GPU ali NPU) za vašo strojno opremo.

---

### 🔴 HttpResponseError: 500 - Napaka pri nalaganju modela

**Sporočilo o napaki:**
```
HttpResponseError: 500 - Failed loading model
```

**Vzrok:** Datoteka modela je poškodovana ali ni združljiva s strojno opremo.

**Rešitve:**

#### Ponovno prenesite model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Uporabite drugo različico
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Modul ni najden

**Sporočilo o napaki:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Vzrok:** Paket foundry-local-sdk ni nameščen.

**Rešitve:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Počasna prva zahteva

**Simptom:** Prva zahteva za dokončanje traja več kot 30 sekund, nadaljnje zahteve so hitre.

**Vzrok:** To je normalno vedenje - storitev ob prvi zahtevi nalaga model v pomnilnik.

**Rešitve:**

#### Predhodno naložite modele
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Naj storitev ostane zagnana
```bash
# Start service manually and leave it running
foundry service start
```

---

## Težave specifične za sejo 04

### Napačna konfiguracija vrat

**Težava:** Zvezek se povezuje na napačna vrata (55769 namesto 59959 ali 57127)

**Rešitev:**

1. Preverite, katera vrata uporablja Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Posodobite celico 10 v zvezku:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Znova zaženite jedro in ponovno zaženite celice 6, 8, 10, 12, 16, 20, 22

---

### Napačna izbira modela

**Težava:** Zvezek prikazuje gpt-oss-20b ali qwen2.5-7b namesto qwen2.5-3b

**Rešitev:**

1. Znova zaženite jedro zvezka (počisti staro stanje spremenljivk)
2. Ponovno zaženite celico 10 (nastavite vzdevke modelov)
3. Ponovno zaženite celico 12 (prikaz konfiguracije)
4. **Preverite:** Celica 12 mora prikazati `LLM Model: qwen2.5-3b`

---

### Diagnostična celica ne uspe

**Težava:** Celica 16 prikazuje "❌ Foundry Local storitev ni najdena!"

**Rešitev:**

1. Preverite, ali storitev deluje:
```bash
foundry service status
```

2. Ročno preizkusite končno točko:
```bash
curl http://localhost:59959/v1/models
```

3. Če curl deluje, zvezek pa ne:
   - Znova zaženite jedro zvezka
   - Ponovno zaženite celice v vrstnem redu: 6, 8, 10, 12, 14, 16

4. Če curl ne deluje:
   - Zaženite storitev: `foundry service start`
   - Naložite modele: `foundry model run phi-4-mini` in `foundry model run qwen2.5-3b`

---

### Pre-flight preverjanje ne uspe

**Težava:** Celica 20 prikazuje napake povezave, čeprav je diagnostika uspela

**Rešitev:**

1. Preverite, ali so modeli naloženi:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Če modeli manjkajo:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Ponovno zaženite celico 20, ko so modeli naloženi

---

### Primerjava ne uspe z vrednostmi None

**Težava:** Celica 22 se zaključi, vendar prikazuje latenco kot None

**Rešitev:**

1. Preverite, ali je pre-flight preverjanje uspelo (celica 20)
2. Ponovno zaženite celico 22 - modeli se morda morajo ogreti ob prvi zahtevi
3. Preverite, ali sta oba modela naložena: `foundry model ls`

---

## Težave specifične za sejo 05

### Agent uporablja napačen model

**Težava:** Agent ne uporablja pričakovanega modela

**Rešitev:**

Preverite konfiguracijo:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Znova zaženite jedro, če so modeli napačni.

---

### Presežek konteksta pomnilnika

**Težava:** Odzivi agenta se sčasoma slabšajo

**Rešitev:** To je že samodejno urejeno - agenti hranijo le zadnjih 6 sporočil v pomnilniku.

---

## Težave specifične za sejo 06

### Zmeda med CPU in GPU modeli

**Težava:** Pojavljajo se CUDA napake pri uporabi privzete konfiguracije

**Rešitev:** Privzeta konfiguracija zdaj uporablja CPU modele. Če vidite CUDA napake:

1. Preverite, ali uporabljate privzeti CPU katalog:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Znova zaženite jedro in ponovno zaženite vse celice

---

### Zaznavanje namena ne deluje

**Težava:** Pozivi se usmerjajo na napačne modele

**Rešitev:**

Preizkusite zaznavanje namena:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Posodobite RULES, če je treba prilagoditi vzorce.

---

## Težave specifične za strojno opremo

### NVIDIA GPU

**Preverite stanje GPU:**
```bash
nvidia-smi
```

**Pogoste težave:**
- **Zastarel gonilnik:** Posodobite NVIDIA gonilnike
- **Neskladje različic CUDA:** Znova namestite Foundry Local
- **Fragmentiran pomnilnik GPU:** Znova zaženite sistem

### Qualcomm NPU

**Preverite stanje NPU:**
```bash
foundry device info
```

**Pogoste težave:**
- **Gonilniki NPU niso nameščeni:** Namestite Qualcomm NPU gonilnike
- **Različica NPU ni na voljo:** Uporabite CPU različico
- **Windows različica je preveč zastarela:** Posodobite na najnovejši Windows 11

### Sistemi samo s CPU

**Priporočeni modeli:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Nasveti za zmogljivost:**
- Uporabite najmanjše modele
- Zmanjšajte max_tokens
- Bodite potrpežljivi pri prvi zahtevi

---

## Diagnostični ukazi

### Preverite vse
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

### V Pythonu
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

## Pomoč

### 1. Preverite dnevnike
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub težave
- Poiščite obstoječe težave: https://github.com/microsoft/Foundry-Local/issues
- Ustvarite novo težavo z:
  - Sporočilo o napaki (celotno besedilo)
  - Izhod `foundry service status`
  - Izhod `foundry --version`
  - Informacije o GPU/NPU (nvidia-smi itd.)
  - Koraki za reprodukcijo

### 3. Dokumentacija
- **Glavno skladišče:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI referenca:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Odpravljanje težav:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Kontrolni seznam hitrih rešitev

Ko gre kaj narobe, poskusite naslednje po vrsti:

- [ ] Preverite, ali storitev deluje: `foundry service status`
- [ ] Znova zaženite storitev: `foundry service stop && foundry service start`
- [ ] Preverite, ali model obstaja: `foundry model ls | grep phi-4-mini`
- [ ] Naložite potrebne modele: `foundry model run phi-4-mini`
- [ ] Preverite pomnilnik GPU: `nvidia-smi` (če uporabljate NVIDIA)
- [ ] Poskusite CPU različico: Uporabite `phi-4-mini-cpu` namesto `phi-4-mini`
- [ ] Znova zaženite jedro zvezka
- [ ] Počistite izhode zvezka in ponovno zaženite vse celice
- [ ] Znova namestite SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Znova zaženite sistem (zadnja možnost)

---

## Nasveti za preprečevanje

### Najboljše prakse

1. **Vedno najprej preverite storitev:**
   ```bash
   foundry service status
   ```

2. **Privzeto uporabljajte CPU različice:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Predhodno naložite modele pred zagonom zvezkov:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Naj storitev ostane zagnana:**
   - Ne ustavljajte/zaženite storitve po nepotrebnem
   - Naj deluje v ozadju med sejami

5. **Spremljajte vire:**
   - Preverite pomnilnik GPU pred zagonom
   - Zaprite nepotrebne aplikacije, ki uporabljajo GPU
   - Uporabite Upravitelja opravil / nvidia-smi

6. **Redno posodabljajte:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Zadnja posodobitev:** 8. oktober 2025

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.