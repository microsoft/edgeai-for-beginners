# Caiet de lucru - Ghid de depanare

## Cuprins

- [Probleme comune și soluții](../../../../Workshop/notebooks)
- [Probleme specifice sesiunii 04](../../../../Workshop/notebooks)
- [Probleme specifice sesiunii 05](../../../../Workshop/notebooks)
- [Probleme specifice sesiunii 06](../../../../Workshop/notebooks)
- [Probleme specifice hardware-ului](../../../../Workshop/notebooks)
- [Comenzi de diagnosticare](../../../../Workshop/notebooks)
- [Obținerea ajutorului](../../../../Workshop/notebooks)

---

## Probleme comune și soluții

### 🔴 CUDA Out of Memory

**Mesaj de eroare:**
```
CUDA failure 2: out of memory
```

**Cauza principală:** GPU-ul nu are suficientă memorie VRAM pentru a încărca modelul.

**Soluții:**

#### Opțiunea 1: Utilizați variantele CPU (Recomandat)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opțiunea 2: Utilizați modele mai mici pe GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opțiunea 3: Goliți memoria GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opțiunea 4: Creșteți memoria GPU (dacă este posibil)
- Închideți filele de browser, editorii video sau alte aplicații care folosesc GPU
- Reduceți efectele vizuale din Windows
- Utilizați GPU-ul dedicat dacă aveți atât GPU integrat, cât și dedicat

---

### 🔴 APIConnectionError: Connection Error

**Mesaj de eroare:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Cauza principală:** Serviciul Foundry Local nu rulează sau nu este accesibil.

**Soluții:**

#### Pasul 1: Verificați starea serviciului
```bash
foundry service status
```

#### Pasul 2: Porniți serviciul dacă este oprit
```bash
foundry service start
```

#### Pasul 3: Verificați endpoint-ul
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Pasul 4: Încărcați modelele necesare
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Pasul 5: Reporniți kernel-ul caietului
După ce ați pornit serviciul și ați încărcat modelele, reporniți kernel-ul caietului și rulați din nou toate celulele.

---

### 🔴 Model Not Found in Catalog

**Mesaj de eroare:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Cauza principală:** Modelul nu este descărcat sau încărcat în Foundry Local.

**Soluții:**

#### Opțiunea 1: Descărcați și încărcați modelele
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

#### Opțiunea 2: Utilizați modul de selecție automată
Actualizați CATALOG pentru a utiliza numele de bază ale modelelor (fără sufixul `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK va selecta automat cea mai bună variantă (CPU, GPU sau NPU) pentru hardware-ul dvs.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Mesaj de eroare:**
```
HttpResponseError: 500 - Failed loading model
```

**Cauza principală:** Fișierul modelului este corupt sau incompatibil cu hardware-ul.

**Soluții:**

#### Descărcați din nou modelul
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Utilizați o altă variantă
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Mesaj de eroare:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Cauza principală:** Pachetul foundry-local-sdk nu este instalat.

**Soluții:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Prima solicitare este lentă

**Simptom:** Prima completare durează peste 30 de secunde, solicitările ulterioare sunt rapide.

**Cauza principală:** Acest comportament este normal - serviciul încarcă modelul în memorie la prima solicitare.

**Soluții:**

#### Pre-încărcați modelele
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Mențineți serviciul activ
```bash
# Start service manually and leave it running
foundry service start
```

---

## Probleme specifice sesiunii 04

### Configurare greșită a portului

**Problemă:** Caietul se conectează la un port greșit (55769 vs 59959 vs 57127)

**Soluție:**

1. Verificați ce port utilizează Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Actualizați celula 10 din caiet:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Reporniți kernel-ul și rulați din nou celulele 6, 8, 10, 12, 16, 20, 22

---

### Selecție greșită a modelului

**Problemă:** Caietul afișează gpt-oss-20b sau qwen2.5-7b în loc de qwen2.5-3b

**Soluție:**

1. Reporniți kernel-ul caietului (șterge starea veche a variabilelor)
2. Rulați din nou celula 10 (Setați Aliasurile Modelului)
3. Rulați din nou celula 12 (Afișați Configurația)
4. **Verificați:** Celula 12 ar trebui să afișeze `LLM Model: qwen2.5-3b`

---

### Celula de diagnosticare eșuează

**Problemă:** Celula 16 afișează "❌ Foundry Local service not found!"

**Soluție:**

1. Verificați dacă serviciul rulează:
```bash
foundry service status
```

2. Testați endpoint-ul manual:
```bash
curl http://localhost:59959/v1/models
```

3. Dacă curl funcționează, dar caietul nu:
   - Reporniți kernel-ul caietului
   - Rulați celulele în ordine: 6, 8, 10, 12, 14, 16

4. Dacă curl eșuează:
   - Porniți serviciul: `foundry service start`
   - Încărcați modelele: `foundry model run phi-4-mini` și `foundry model run qwen2.5-3b`

---

### Verificarea preliminară eșuează

**Problemă:** Celula 20 afișează erori de conexiune, deși diagnosticul a trecut

**Soluție:**

1. Verificați dacă modelele sunt încărcate:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Dacă modelele lipsesc:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Rulați din nou celula 20 după ce modelele sunt încărcate

---

### Compararea eșuează cu valori None

**Problemă:** Celula 22 se finalizează, dar afișează latența ca None

**Soluție:**

1. Verificați dacă verificarea preliminară a trecut mai întâi (Celula 20)
2. Rulați din nou celula 22 - modelele pot necesita încălzire la prima solicitare
3. Verificați dacă ambele modele sunt încărcate: `foundry model ls`

---

## Probleme specifice sesiunii 05

### Agentul folosește modelul greșit

**Problemă:** Agentul nu folosește modelul așteptat

**Soluție:**

Verificați configurația:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Reporniți kernel-ul dacă modelele sunt incorecte.

---

### Depășirea memoriei contextuale

**Problemă:** Răspunsurile agentului se degradează în timp

**Soluție:** Deja gestionat automat - agenții păstrează doar ultimele 6 mesaje în memorie.

---

## Probleme specifice sesiunii 06

### Confuzie între modelele CPU și GPU

**Problemă:** Apar erori CUDA când se folosește configurația implicită

**Soluție:** Configurația implicită folosește acum modele CPU. Dacă apar erori CUDA:

1. Verificați dacă utilizați catalogul implicit CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Reporniți kernel-ul și rulați din nou toate celulele

---

### Detectarea intenției nu funcționează

**Problemă:** Solicitările sunt direcționate către modele greșite

**Soluție:**

Testați detectarea intenției:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Actualizați RULES dacă modelele necesită ajustări.

---

## Probleme specifice hardware-ului

### GPU NVIDIA

**Verificați starea GPU-ului:**
```bash
nvidia-smi
```

**Probleme comune:**
- **Driver învechit**: Actualizați driverele NVIDIA
- **Nepotrivire versiune CUDA**: Reinstalați Foundry Local
- **Memorie GPU fragmentată**: Reporniți sistemul

### NPU Qualcomm

**Verificați starea NPU-ului:**
```bash
foundry device info
```

**Probleme comune:**
- **Drivere NPU neinstalate**: Instalați driverele Qualcomm NPU
- **Varianta NPU indisponibilă**: Utilizați varianta CPU
- **Versiune Windows prea veche**: Actualizați la cea mai recentă versiune de Windows 11

### Sisteme doar cu CPU

**Modele recomandate:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Sfaturi pentru performanță:**
- Utilizați cele mai mici modele
- Reduceți max_tokens
- Aveți răbdare pentru prima solicitare

---

## Comenzi de diagnosticare

### Verificați totul
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

### În Python
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

## Obținerea ajutorului

### 1. Verificați jurnalele
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Probleme pe GitHub
- Căutați probleme existente: https://github.com/microsoft/Foundry-Local/issues
- Creați o problemă nouă cu:
  - Mesajul de eroare (text complet)
  - Rezultatul comenzii `foundry service status`
  - Rezultatul comenzii `foundry --version`
  - Informații despre GPU/NPU (nvidia-smi, etc.)
  - Pașii pentru a reproduce problema

### 3. Documentație
- **Repository principal**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referință CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Depanare**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Lista de verificare pentru soluții rapide

Când ceva nu funcționează, încercați următoarele, în ordine:

- [ ] Verificați dacă serviciul rulează: `foundry service status`
- [ ] Reporniți serviciul: `foundry service stop && foundry service start`
- [ ] Verificați dacă modelul există: `foundry model ls | grep phi-4-mini`
- [ ] Încărcați modelele necesare: `foundry model run phi-4-mini`
- [ ] Verificați memoria GPU: `nvidia-smi` (dacă aveți NVIDIA)
- [ ] Încercați varianta CPU: Utilizați `phi-4-mini-cpu` în loc de `phi-4-mini`
- [ ] Reporniți kernel-ul caietului
- [ ] Goliți ieșirile caietului și rulați din nou toate celulele
- [ ] Reinstalați SDK-ul: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Reporniți sistemul (ultima soluție)

---

## Sfaturi pentru prevenire

### Cele mai bune practici

1. **Verificați întotdeauna serviciul mai întâi:**
   ```bash
   foundry service status
   ```

2. **Utilizați variantele CPU în mod implicit:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pre-încărcați modelele înainte de a rula caietele:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Mențineți serviciul activ:**
   - Nu opriți/porniți serviciul inutil
   - Lăsați-l să ruleze în fundal între sesiuni

5. **Monitorizați resursele:**
   - Verificați memoria GPU înainte de rulare
   - Închideți aplicațiile GPU inutile
   - Utilizați Task Manager / nvidia-smi

6. **Actualizați regulat:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Ultima actualizare:** 8 octombrie 2025

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.