# Töötuba Märkmikud - Kiire Alustamise Juhend

## Sisukord

- [Eeltingimused](../../../../Workshop/notebooks)
- [Esialgne Seadistus](../../../../Workshop/notebooks)
- [Sessioon 04: Mudelite Võrdlus](../../../../Workshop/notebooks)
- [Sessioon 05: Multi-Agent Orkestreerija](../../../../Workshop/notebooks)
- [Sessioon 06: Kavatsuspõhine Mudelite Suunamine](../../../../Workshop/notebooks)
- [Keskkonnamuutujad](../../../../Workshop/notebooks)
- [Üldised Käsud](../../../../Workshop/notebooks)

---

## Eeltingimused

### 1. Paigalda Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Paigalduse Kontrollimine:**
```bash
foundry --version
```

### 2. Paigalda Python'i Sõltuvused

```bash
cd Workshop
pip install -r requirements.txt
```

Või paigalda eraldi:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Esialgne Seadistus

### Käivita Foundry Local Teenus

**Nõutav enne märkmike käivitamist:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Oodatav väljund:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Laadi ja Lae Mudelid

Märkmikud kasutavad vaikimisi järgmisi mudeleid:

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

### Seadistuse Kontrollimine

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sessioon 04: Mudelite Võrdlus

### Eesmärk
Võrdle Väikeste Keelte Mudelite (SLM) ja Suurte Keelte Mudelite (LLM) jõudlust.

### Kiire Seadistus

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Märkmiku Käivitamine

1. **Ava** `session04_model_compare.ipynb` VS Code'is või Jupyteris
2. **Taaskäivita kernel** (Kernel → Restart Kernel)
3. **Käivita kõik lahtrid** järjest

### Oluline Konfiguratsioon

**Vaikimisi Mudelid:**
- **SLM:** `phi-4-mini` (~4GB RAM, kiirem)
- **LLM:** `qwen2.5-3b` (~3GB RAM, mälusäästlik)

**Keskkonnamuutujad (valikuline):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Oodatav Väljund

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

### Kohandamine

**Kasuta erinevaid mudeleid:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Kohandatud küsimus:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Kontrollnimekiri

- [ ] Lahter 12 kuvab õiged mudelid (phi-4-mini, qwen2.5-3b)
- [ ] Lahter 12 kuvab õige lõpp-punkti (port 59959)
- [ ] Lahter 16 diagnostika õnnestub (✅ Teenus töötab)
- [ ] Lahter 20 eelkontroll õnnestub (mõlemad mudelid korras)
- [ ] Lahter 22 võrdlus lõpeb latentsusväärtustega
- [ ] Lahter 24 valideerimine kuvab 🎉 KÕIK KONTROLLID LÄBITUD!

### Ajakulu
- **Esimene käivitus:** 5-10 minutit (sh mudelite allalaadimine)
- **Järgnevad käivitused:** 1-2 minutit

---

## Sessioon 05: Multi-Agent Orkestreerija

### Eesmärk
Näidata mitme agendi koostööd Foundry Local SDK abil - agendid töötavad koos, et luua täpsemaid tulemusi.

### Kiire Seadistus

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Märkmiku Käivitamine

1. **Ava** `session05_agents_orchestrator.ipynb`
2. **Taaskäivita kernel**
3. **Käivita kõik lahtrid** järjest

### Oluline Konfiguratsioon

**Vaikimisi Seadistus (Sama Mudel Mõlemale Agendile):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Täiustatud Seadistus (Erinevad Mudelid):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arhitektuur

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

### Oodatav Väljund

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

### Laiendused

**Lisa rohkem agente:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Partii testimine:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Ajakulu
- **Esimene käivitus:** 3-5 minutit
- **Järgnevad käivitused:** 1-2 minutit küsimuse kohta

---

## Sessioon 06: Kavatsuspõhine Mudelite Suunamine

### Eesmärk
Suunata küsimused intelligentselt spetsialiseeritud mudelitele tuvastatud kavatsuse alusel.

### Kiire Seadistus

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Märkus:** Sessioon 06 kasutab vaikimisi CPU mudeleid maksimaalse ühilduvuse tagamiseks.

### Märkmiku Käivitamine

1. **Ava** `session06_models_router.ipynb`
2. **Taaskäivita kernel**
3. **Käivita kõik lahtrid** järjest

### Oluline Konfiguratsioon

**Vaikimisi Kataloog (CPU Mudelid):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatiiv (GPU Mudelid):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Kavatsuse Tuvastamine

Router kasutab regex mustreid kavatsuse tuvastamiseks:

| Kavatsus | Mustri Näited | Suunatud Mudel |
|----------|---------------|----------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Kõik muu | phi-4-mini-cpu |

### Oodatav Väljund

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

### Kohandamine

**Lisa kohandatud kavatsus:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Luba tokenite jälgimine:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Üleminek GPU Mudelitele

Kui sul on 8GB+ VRAM:

1. **Lahtris #6**, kommenteeri välja CPU kataloog
2. Tühista GPU kataloogi kommentaar
3. Laadi GPU mudelid:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Taaskäivita kernel ja käivita märkmik uuesti

### Ajakulu
- **Esimene käivitus:** 5-10 minutit (mudelite laadimine)
- **Järgnevad käivitused:** 30-60 sekundit testi kohta

---

## Keskkonnamuutujad

### Üldine Konfiguratsioon

Seadista enne Jupyter/VS Code käivitamist:

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

### Märkmikus Seadistamine

Seadista märkmiku alguses:

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

## Üldised Käsud

### Teenuse Haldamine

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

### Mudelite Haldamine

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

### Lõpp-punktide Testimine

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

### Diagnostika Käsud

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

## Parimad Tavad

### Enne Märkmiku Käivitamist

1. **Kontrolli, et teenus töötab:**
   ```bash
   foundry service status
   ```

2. **Veendu, et mudelid on laaditud:**
   ```bash
   foundry model ls
   ```

3. **Taaskäivita märkmiku kernel** kui käivitatakse uuesti

4. **Kustuta kõik väljundid** puhta käivituse jaoks

### Ressursside Haldamine

1. **Kasuta vaikimisi CPU mudeleid** ühilduvuse tagamiseks
2. **Lülitu GPU mudelitele** ainult kui sul on 8GB+ VRAM
3. **Sulge muud GPU rakendused** enne käivitamist
4. **Hoia teenus käimas** märkmiku sessioonide vahel
5. **Jälgi ressursikasutust** Task Manageri / nvidia-smi abil

### Tõrkeotsing

1. **Kontrolli alati teenust esmalt** enne koodi silumist
2. **Taaskäivita kernel** kui näed vananenud konfiguratsiooni
3. **Käivita diagnostika lahtrid uuesti** pärast muudatusi
4. **Kontrolli mudelinimesid** vastavuses laaditud mudelitega
5. **Veendu, et lõpp-punkti port** vastab teenuse olekule

---

## Kiire Viide: Mudelite Aliased

### Levinud Mudelid

| Alias | Suurus | Parim Kasutus | RAM/VRAM | Variandid |
|-------|--------|---------------|----------|-----------|
| `phi-4-mini` | ~4B | Üldine vestlus, kokkuvõtted | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Koodi genereerimine, refaktorimine | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Üldised ülesanded, tõhus | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Kiire, madal ressursikasutus | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klassifikatsioon, minimaalne ressursikasutus | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variandi Nimekonventsioon

- **Põhinimi** (nt `phi-4-mini`): Valib automaatselt parima variandi vastavalt riistvarale
- **`-cpu`**: CPU optimeeritud, töötab kõikjal
- **`-cuda-gpu`**: NVIDIA GPU optimeeritud, nõuab 8GB+ VRAM
- **`-npu`**: Qualcomm NPU optimeeritud, nõuab NPU draivereid

**Soovitus:** Kasuta põhinimesid (ilma järelliiteta) ja lase Foundry Local'il automaatselt valida parim variant.

---

## Edu Näitajad

Oled valmis, kui näed:

✅ `foundry service status` kuvab "running"
✅ `foundry model ls` kuvab vajalikud mudelid
✅ Teenus on ligipääsetav õiges lõpp-punktis
✅ Tervisekontroll tagastab 200 OK
✅ Märkmiku diagnostika lahtrid õnnestuvad
✅ Väljundis pole ühenduse vigu

---

## Abi Saamine

### Dokumentatsioon
- **Peamine Repositoorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Viide**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Tõrkeotsing**: Vaata `troubleshooting.md` selles kataloogis

### GitHub Probleemid
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Viimati Uuendatud:** 8. oktoober 2025
**Versioon:** Töötuba Märkmikud 2.0

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.