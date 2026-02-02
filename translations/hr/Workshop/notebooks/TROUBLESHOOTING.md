# Priručnik za rješavanje problema - Radionica Notebooks

## Sadržaj

- [Uobičajeni problemi i rješenja](../../../../Workshop/notebooks)
- [Problemi specifični za sesiju 04](../../../../Workshop/notebooks)
- [Problemi specifični za sesiju 05](../../../../Workshop/notebooks)
- [Problemi specifični za sesiju 06](../../../../Workshop/notebooks)
- [Problemi vezani uz hardver](../../../../Workshop/notebooks)
- [Dijagnostičke naredbe](../../../../Workshop/notebooks)
- [Kako dobiti pomoć](../../../../Workshop/notebooks)

---

## Uobičajeni problemi i rješenja

### 🔴 CUDA Out of Memory

**Poruka o grešci:**
```
CUDA failure 2: out of memory
```

**Uzrok:** GPU nema dovoljno VRAM-a za učitavanje modela.

**Rješenja:**

#### Opcija 1: Koristite CPU varijante (preporučeno)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opcija 2: Koristite manje modele na GPU-u
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opcija 3: Očistite memoriju GPU-a
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opcija 4: Povećajte memoriju GPU-a (ako je moguće)
- Zatvorite kartice preglednika, video editore ili druge aplikacije koje koriste GPU
- Smanjite vizualne efekte u Windowsu
- Koristite namjenski GPU ako imate integrirani + namjenski

---

### 🔴 APIConnectionError: Connection Error

**Poruka o grešci:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Uzrok:** Foundry Local usluga nije pokrenuta ili nije dostupna.

**Rješenja:**

#### Korak 1: Provjerite status usluge
```bash
foundry service status
```

#### Korak 2: Pokrenite uslugu ako je zaustavljena
```bash
foundry service start
```

#### Korak 3: Provjerite endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Korak 4: Učitajte potrebne modele
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Korak 5: Ponovno pokrenite kernel notesa
Nakon pokretanja usluge i učitavanja modela, ponovno pokrenite kernel notesa i ponovno pokrenite sve ćelije.

---

### 🔴 Model nije pronađen u katalogu

**Poruka o grešci:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Uzrok:** Model nije preuzet ili učitan u Foundry Local.

**Rješenja:**

#### Opcija 1: Preuzmite i učitajte modele
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

#### Opcija 2: Koristite način automatskog odabira
Ažurirajte svoj CATALOG da koristi osnovna imena modela (bez sufiksa `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK automatski će odabrati najbolju varijantu (CPU, GPU ili NPU) za vaš hardver.

---

### 🔴 HttpResponseError: 500 - Neuspješno učitavanje modela

**Poruka o grešci:**
```
HttpResponseError: 500 - Failed loading model
```

**Uzrok:** Datoteka modela je oštećena ili nije kompatibilna s hardverom.

**Rješenja:**

#### Ponovno preuzmite model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Koristite drugu varijantu
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Modul nije pronađen

**Poruka o grešci:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Uzrok:** Paket foundry-local-sdk nije instaliran.

**Rješenja:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Sporo prvo pokretanje

**Simptom:** Prvo dovršavanje traje više od 30 sekundi, dok su naknadni zahtjevi brzi.

**Uzrok:** Ovo je normalno ponašanje - usluga učitava model u memoriju pri prvom zahtjevu.

**Rješenja:**

#### Pred-učitajte modele
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Ostavite uslugu da radi
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problemi specifični za sesiju 04

### Pogrešna konfiguracija porta

**Problem:** Notes se povezuje na pogrešan port (55769 vs 59959 vs 57127)

**Rješenje:**

1. Provjerite koji port koristi Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Ažurirajte ćeliju 10 u notesu:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Ponovno pokrenite kernel i ponovno pokrenite ćelije 6, 8, 10, 12, 16, 20, 22

---

### Pogrešan odabir modela

**Problem:** Notes prikazuje gpt-oss-20b ili qwen2.5-7b umjesto qwen2.5-3b

**Rješenje:**

1. Ponovno pokrenite kernel notesa (čisti stare varijable)
2. Ponovno pokrenite ćeliju 10 (Postavite alias modela)
3. Ponovno pokrenite ćeliju 12 (Prikaži konfiguraciju)
4. **Provjerite:** Ćelija 12 treba prikazati `LLM Model: qwen2.5-3b`

---

### Dijagnostička ćelija ne uspijeva

**Problem:** Ćelija 16 prikazuje "❌ Foundry Local usluga nije pronađena!"

**Rješenje:**

1. Provjerite radi li usluga:
```bash
foundry service status
```

2. Ručno testirajte endpoint:
```bash
curl http://localhost:59959/v1/models
```

3. Ako curl radi, ali notes ne:
   - Ponovno pokrenite kernel notesa
   - Ponovno pokrenite ćelije redoslijedom: 6, 8, 10, 12, 14, 16

4. Ako curl ne radi:
   - Pokrenite uslugu: `foundry service start`
   - Učitajte modele: `foundry model run phi-4-mini` i `foundry model run qwen2.5-3b`

---

### Pre-flight provjera ne uspijeva

**Problem:** Ćelija 20 prikazuje greške povezivanja iako je dijagnostika prošla

**Rješenje:**

1. Provjerite jesu li modeli učitani:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Ako modeli nedostaju:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Ponovno pokrenite ćeliju 20 nakon što su modeli učitani

---

### Usporedba ne uspijeva s vrijednostima None

**Problem:** Ćelija 22 završava, ali prikazuje latenciju kao None

**Rješenje:**

1. Provjerite je li pre-flight prošao (Ćelija 20)
2. Ponovno pokrenite ćeliju 22 - modeli se možda trebaju zagrijati pri prvom zahtjevu
3. Provjerite jesu li oba modela učitana: `foundry model ls`

---

## Problemi specifični za sesiju 05

### Agent koristi pogrešan model

**Problem:** Agent ne koristi očekivani model

**Rješenje:**

Provjerite konfiguraciju:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Ponovno pokrenite kernel ako su modeli pogrešni.

---

### Prekoračenje memorijskog konteksta

**Problem:** Odgovori agenta se pogoršavaju s vremenom

**Rješenje:** Već automatski riješeno - agenti zadržavaju samo posljednjih 6 poruka u memoriji.

---

## Problemi specifični za sesiju 06

### Zbunjenost između CPU i GPU modela

**Problem:** Pojavljuju se CUDA greške pri korištenju zadane konfiguracije

**Rješenje:** Zadana konfiguracija sada koristi CPU modele. Ako vidite CUDA greške:

1. Provjerite koristite li zadani CPU katalog:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Ponovno pokrenite kernel i ponovno pokrenite sve ćelije

---

### Detekcija namjere ne radi

**Problem:** Upiti se usmjeravaju na pogrešne modele

**Rješenje:**

Testirajte detekciju namjere:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Ažurirajte RULES ako obrasci trebaju prilagodbu.

---

## Problemi vezani uz hardver

### NVIDIA GPU

**Provjerite status GPU-a:**
```bash
nvidia-smi
```

**Uobičajeni problemi:**
- **Zastarjeli driveri:** Ažurirajte NVIDIA drivere
- **Neusklađenost verzije CUDA:** Ponovno instalirajte Foundry Local
- **Fragmentirana memorija GPU-a:** Ponovno pokrenite sustav

### Qualcomm NPU

**Provjerite status NPU-a:**
```bash
foundry device info
```

**Uobičajeni problemi:**
- **Driveri za NPU nisu instalirani:** Instalirajte Qualcomm NPU drivere
- **Varijanta NPU-a nije dostupna:** Koristite CPU varijantu
- **Windows verzija je zastarjela:** Ažurirajte na najnoviji Windows 11

### Sustavi samo s CPU-om

**Preporučeni modeli:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Savjeti za performanse:**
- Koristite najmanje modele
- Smanjite max_tokens
- Budite strpljivi pri prvom zahtjevu

---

## Dijagnostičke naredbe

### Provjerite sve
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

### U Pythonu
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

## Kako dobiti pomoć

### 1. Provjerite logove
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Pretražite postojeće probleme: https://github.com/microsoft/Foundry-Local/issues
- Kreirajte novi problem s:
  - Porukom o grešci (cijeli tekst)
  - Izlazom naredbe `foundry service status`
  - Izlazom naredbe `foundry --version`
  - Informacijama o GPU/NPU (nvidia-smi, itd.)
  - Koracima za reprodukciju

### 3. Dokumentacija
- **Glavni repozitorij:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI referenca:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Rješavanje problema:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Popis za brza rješenja

Kad nešto pođe po zlu, pokušajte sljedeće redom:

- [ ] Provjerite radi li usluga: `foundry service status`
- [ ] Ponovno pokrenite uslugu: `foundry service stop && foundry service start`
- [ ] Provjerite postoji li model: `foundry model ls | grep phi-4-mini`
- [ ] Učitajte potrebne modele: `foundry model run phi-4-mini`
- [ ] Provjerite memoriju GPU-a: `nvidia-smi` (ako koristite NVIDIA)
- [ ] Pokušajte CPU varijantu: Koristite `phi-4-mini-cpu` umjesto `phi-4-mini`
- [ ] Ponovno pokrenite kernel notesa
- [ ] Očistite izlaze notesa i ponovno pokrenite sve ćelije
- [ ] Ponovno instalirajte SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Ponovno pokrenite sustav (kao posljednje rješenje)

---

## Savjeti za prevenciju

### Najbolje prakse

1. **Uvijek prvo provjerite uslugu:**
   ```bash
   foundry service status
   ```

2. **Koristite CPU varijante kao zadane:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pred-učitajte modele prije pokretanja notesa:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Ostavite uslugu da radi:**
   - Nemojte nepotrebno zaustavljati/pokretati uslugu
   - Neka radi u pozadini između sesija

5. **Pratite resurse:**
   - Provjerite memoriju GPU-a prije pokretanja
   - Zatvorite nepotrebne aplikacije koje koriste GPU
   - Koristite Task Manager / nvidia-smi

6. **Redovito ažurirajte:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Zadnje ažuriranje:** 8. listopada 2025.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.