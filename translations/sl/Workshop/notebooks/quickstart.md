# Delovni zvezki - Hitri vodnik

## Kazalo

- [Predpogoji](../../../../Workshop/notebooks)
- [Začetna nastavitev](../../../../Workshop/notebooks)
- [Seja 04: Primerjava modelov](../../../../Workshop/notebooks)
- [Seja 05: Orkestrator več agentov](../../../../Workshop/notebooks)
- [Seja 06: Usmerjanje modelov na podlagi namena](../../../../Workshop/notebooks)
- [Okoljske spremenljivke](../../../../Workshop/notebooks)
- [Pogosti ukazi](../../../../Workshop/notebooks)

---

## Predpogoji

### 1. Namestite Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Preverite namestitev:**
```bash
foundry --version
```

### 2. Namestite Python odvisnosti

```bash
cd Workshop
pip install -r requirements.txt
```

Ali namestite posamezno:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Začetna nastavitev

### Zaženite storitev Foundry Local

**Potrebno pred zagonom katerega koli zvezka:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Pričakovani izhod:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Prenesite in naložite modele

Zvezki privzeto uporabljajo te modele:

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

### Preverite nastavitev

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Seja 04: Primerjava modelov

### Namen
Primerjajte zmogljivost med majhnimi jezikovnimi modeli (SLM) in velikimi jezikovnimi modeli (LLM).

### Hitra nastavitev

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Zagon zvezka

1. **Odprite** `session04_model_compare.ipynb` v VS Code ali Jupyter
2. **Ponovno zaženite jedro** (Kernel → Restart Kernel)
3. **Zaženite vse celice** po vrsti

### Ključna konfiguracija

**Privzeti modeli:**
- **SLM:** `phi-4-mini` (~4GB RAM, hitrejši)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimiziran za pomnilnik)

**Okoljske spremenljivke (neobvezno):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Pričakovani izhod

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

### Prilagoditev

**Uporabite različne modele:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prilagojen poziv:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Preveritveni seznam

- [ ] Celica 12 prikazuje pravilne modele (phi-4-mini, qwen2.5-3b)
- [ ] Celica 12 prikazuje pravilno končno točko (port 59959)
- [ ] Diagnostika celice 16 uspešna (✅ Storitev deluje)
- [ ] Predhodni pregled celice 20 uspešen (oba modela v redu)
- [ ] Primerjava celice 22 se zaključi z vrednostmi zakasnitve
- [ ] Validacija celice 24 prikazuje 🎉 VSE PREVERITVE USPEŠNE!

### Časovna ocena
- **Prvi zagon:** 5-10 minut (vključno s prenosom modelov)
- **Naslednji zagoni:** 1-2 minuti

---

## Seja 05: Orkestrator več agentov

### Namen
Prikaz sodelovanja več agentov z uporabo Foundry Local SDK - agenti sodelujejo za izdelavo izpopolnjenih rezultatov.

### Hitra nastavitev

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Zagon zvezka

1. **Odprite** `session05_agents_orchestrator.ipynb`
2. **Ponovno zaženite jedro**
3. **Zaženite vse celice** po vrsti

### Ključna konfiguracija

**Privzeta nastavitev (isti model za oba agenta):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Napredna nastavitev (različni modeli):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arhitektura

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

### Pričakovani izhod

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

### Razširitve

**Dodajte več agentov:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Testiranje v serijah:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Časovna ocena
- **Prvi zagon:** 3-5 minut
- **Naslednji zagoni:** 1-2 minuti na vprašanje

---

## Seja 06: Usmerjanje modelov na podlagi namena

### Namen
Pametno usmerjanje pozivov k specializiranim modelom glede na zaznani namen.

### Hitra nastavitev

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Opomba:** Seja 06 privzeto uporablja modele na CPU za največjo združljivost.

### Zagon zvezka

1. **Odprite** `session06_models_router.ipynb`
2. **Ponovno zaženite jedro**
3. **Zaženite vse celice** po vrsti

### Ključna konfiguracija

**Privzeti katalog (CPU modeli):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (GPU modeli):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Zaznavanje namena

Usmerjevalnik uporablja regex vzorce za zaznavanje namena:

| Namen | Primeri vzorcev | Usmerjeno k |
|-------|-----------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Vse ostalo | phi-4-mini-cpu |

### Pričakovani izhod

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

### Prilagoditev

**Dodajte prilagojen namen:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Omogočite sledenje žetonom:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Preklop na GPU modele

Če imate 8GB+ VRAM:

1. V **Celici #6**, zakomentirajte CPU katalog
2. Odkomentirajte GPU katalog
3. Naložite GPU modele:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Ponovno zaženite jedro in ponovno zaženite zvezek

### Časovna ocena
- **Prvi zagon:** 5-10 minut (nalaganje modelov)
- **Naslednji zagoni:** 30-60 sekund na test

---

## Okoljske spremenljivke

### Globalna konfiguracija

Nastavite pred zagonom Jupyter/VS Code:

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

### Konfiguracija v zvezku

Nastavite na začetku katerega koli zvezka:

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

## Pogosti ukazi

### Upravljanje storitev

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

### Upravljanje modelov

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

### Testiranje končnih točk

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

### Diagnostični ukazi

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

## Najboljše prakse

### Pred začetkom katerega koli zvezka

1. **Preverite, ali storitev deluje:**
   ```bash
   foundry service status
   ```

2. **Preverite, ali so modeli naloženi:**
   ```bash
   foundry model ls
   ```

3. **Ponovno zaženite jedro zvezka**, če ga ponovno zaženete

4. **Počistite vse izhode** za čist zagon

### Upravljanje virov

1. **Privzeto uporabljajte CPU modele** za združljivost
2. **Preklopite na GPU modele** le, če imate 8GB+ VRAM
3. **Zaprite druge GPU aplikacije** pred zagonom
4. **Naj storitev deluje** med sejami zvezkov
5. **Spremljajte uporabo virov** z Upraviteljem opravil / nvidia-smi

### Odpravljanje težav

1. **Vedno najprej preverite storitev**, preden odpravljate napake v kodi
2. **Ponovno zaženite jedro**, če opazite zastarelo konfiguracijo
3. **Ponovno zaženite diagnostične celice** po kakršnih koli spremembah
4. **Preverite imena modelov**, da se ujemajo z naloženimi
5. **Preverite vrata končne točke**, da se ujemajo s statusom storitve

---

## Hitri referenčni vodič: Imena modelov

### Pogosti modeli

| Ime | Velikost | Najboljše za | RAM/VRAM | Različice |
|-----|----------|--------------|----------|-----------|
| `phi-4-mini` | ~4B | Splošni klepet, povzemanje | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generiranje kode, preoblikovanje | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Splošne naloge, učinkovito | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Hitro, nizki viri | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Razvrščanje, minimalni viri | 1-2GB | `-cpu`, `-cuda-gpu` |

### Imenovanje različic

- **Osnovno ime** (npr. `phi-4-mini`): Samodejno izbere najboljšo različico za vašo strojno opremo
- **`-cpu`**: Optimizirano za CPU, deluje povsod
- **`-cuda-gpu`**: Optimizirano za NVIDIA GPU, zahteva 8GB+ VRAM
- **`-npu`**: Optimizirano za Qualcomm NPU, zahteva NPU gonilnike

**Priporočilo:** Uporabljajte osnovna imena (brez pripon) in pustite, da Foundry Local samodejno izbere najboljšo različico.

---

## Kazalniki uspeha

Pripravljeni ste, ko vidite:

✅ `foundry service status` prikazuje "running"
✅ `foundry model ls` prikazuje zahtevane modele
✅ Storitev dostopna na pravilni končni točki
✅ Preverjanje zdravja vrne 200 OK
✅ Diagnostične celice zvezka uspešne
✅ Brez napak povezave v izhodu

---

## Pomoč

### Dokumentacija
- **Glavno skladišče:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI referenca:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Odpravljanje težav:** Glejte `troubleshooting.md` v tej mapi

### GitHub težave
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Zadnja posodobitev:** 8. oktober 2025
**Različica:** Workshop Notebooks 2.0

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.