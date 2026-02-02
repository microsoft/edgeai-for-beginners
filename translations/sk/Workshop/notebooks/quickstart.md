# Workshop Notebooks - Rýchly sprievodca

## Obsah

- [Predpoklady](../../../../Workshop/notebooks)
- [Počiatočné nastavenie](../../../../Workshop/notebooks)
- [Session 04: Porovnanie modelov](../../../../Workshop/notebooks)
- [Session 05: Orchestrátor viacerých agentov](../../../../Workshop/notebooks)
- [Session 06: Smerovanie modelov na základe zámeru](../../../../Workshop/notebooks)
- [Environmentálne premenné](../../../../Workshop/notebooks)
- [Bežné príkazy](../../../../Workshop/notebooks)

---

## Predpoklady

### 1. Nainštalujte Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Overenie inštalácie:**
```bash
foundry --version
```

### 2. Nainštalujte Python závislosti

```bash
cd Workshop
pip install -r requirements.txt
```

Alebo nainštalujte jednotlivo:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Počiatočné nastavenie

### Spustite službu Foundry Local

**Vyžaduje sa pred spustením akéhokoľvek notebooku:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Očakávaný výstup:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Stiahnite a načítajte modely

Notebooky predvolene používajú tieto modely:

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

### Overenie nastavenia

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Porovnanie modelov

### Účel
Porovnanie výkonu medzi malými jazykovými modelmi (SLM) a veľkými jazykovými modelmi (LLM).

### Rýchle nastavenie

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Spustenie notebooku

1. **Otvorte** `session04_model_compare.ipynb` vo VS Code alebo Jupyter
2. **Reštartujte kernel** (Kernel → Restart Kernel)
3. **Spustite všetky bunky** v poradí

### Kľúčová konfigurácia

**Predvolené modely:**
- **SLM:** `phi-4-mini` (~4GB RAM, rýchlejší)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimalizovaný pre pamäť)

**Environmentálne premenné (voliteľné):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Očakávaný výstup

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

### Prispôsobenie

**Použite iné modely:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Vlastný prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Kontrolný zoznam validácie

- [ ] Bunky 12 zobrazujú správne modely (phi-4-mini, qwen2.5-3b)
- [ ] Bunky 12 zobrazujú správny endpoint (port 59959)
- [ ] Diagnostika bunky 16 prebehla úspešne (✅ Služba beží)
- [ ] Predletová kontrola bunky 20 prebehla úspešne (oba modely sú v poriadku)
- [ ] Porovnanie bunky 22 je dokončené s hodnotami latencie
- [ ] Validácia bunky 24 ukazuje 🎉 VŠETKY KONTROLY PREŠLI!

### Odhad času
- **Prvé spustenie:** 5-10 minút (vrátane sťahovania modelov)
- **Nasledujúce spustenia:** 1-2 minúty

---

## Session 05: Orchestrátor viacerých agentov

### Účel
Ukážka spolupráce viacerých agentov pomocou Foundry Local SDK - agenti spolupracujú na vytváraní vylepšených výstupov.

### Rýchle nastavenie

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Spustenie notebooku

1. **Otvorte** `session05_agents_orchestrator.ipynb`
2. **Reštartujte kernel**
3. **Spustite všetky bunky** v poradí

### Kľúčová konfigurácia

**Predvolené nastavenie (rovnaký model pre oboch agentov):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Pokročilé nastavenie (rôzne modely):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektúra

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

### Očakávaný výstup

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

### Rozšírenia

**Pridajte viac agentov:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch testovanie:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Odhad času
- **Prvé spustenie:** 3-5 minút
- **Nasledujúce spustenia:** 1-2 minúty na otázku

---

## Session 06: Smerovanie modelov na základe zámeru

### Účel
Inteligentné smerovanie promptov na špecializované modely na základe detekovaného zámeru.

### Rýchle nastavenie

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Poznámka:** Session 06 predvolene používa CPU modely pre maximálnu kompatibilitu.

### Spustenie notebooku

1. **Otvorte** `session06_models_router.ipynb`
2. **Reštartujte kernel**
3. **Spustite všetky bunky** v poradí

### Kľúčová konfigurácia

**Predvolený katalóg (CPU modely):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatíva (GPU modely):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Detekcia zámeru

Router používa regex vzory na detekciu zámeru:

| Zámer | Príklady vzorov | Smerované na |
|-------|-----------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Všetko ostatné | phi-4-mini-cpu |

### Očakávaný výstup

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

### Prispôsobenie

**Pridajte vlastný zámer:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Povolenie sledovania tokenov:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Prechod na GPU modely

Ak máte 8GB+ VRAM:

1. V **bunka #6**, zakomentujte CPU katalóg
2. Odkomentujte GPU katalóg
3. Načítajte GPU modely:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Reštartujte kernel a znovu spustite notebook

### Odhad času
- **Prvé spustenie:** 5-10 minút (načítanie modelov)
- **Nasledujúce spustenia:** 30-60 sekúnd na test

---

## Environmentálne premenné

### Globálna konfigurácia

Nastavte pred spustením Jupyter/VS Code:

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

### Konfigurácia v notebooku

Nastavte na začiatku akéhokoľvek notebooku:

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

## Bežné príkazy

### Správa služby

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

### Správa modelov

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

### Testovanie endpointov

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

### Diagnostické príkazy

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

## Najlepšie postupy

### Pred spustením akéhokoľvek notebooku

1. **Skontrolujte, či služba beží:**
   ```bash
   foundry service status
   ```

2. **Overte, či sú modely načítané:**
   ```bash
   foundry model ls
   ```

3. **Reštartujte kernel notebooku** pri opätovnom spustení

4. **Vymažte všetky výstupy** pre čisté spustenie

### Správa zdrojov

1. **Používajte CPU modely predvolene** pre kompatibilitu
2. **Prepnite na GPU modely** iba ak máte 8GB+ VRAM
3. **Zatvorte ostatné GPU aplikácie** pred spustením
4. **Udržujte službu bežiacu** medzi notebookovými reláciami
5. **Monitorujte využitie zdrojov** pomocou Task Manager / nvidia-smi

### Riešenie problémov

1. **Vždy najskôr skontrolujte službu** pred ladením kódu
2. **Reštartujte kernel** ak vidíte zastaranú konfiguráciu
3. **Znovu spustite diagnostické bunky** po akýchkoľvek zmenách
4. **Skontrolujte názvy modelov** či zodpovedajú načítaným
5. **Overte port endpointu** či zodpovedá stavu služby

---

## Rýchla referencia: Alias modelov

### Bežné modely

| Alias | Veľkosť | Najlepšie pre | RAM/VRAM | Varianty |
|-------|---------|---------------|----------|----------|
| `phi-4-mini` | ~4B | Všeobecný chat, sumarizácia | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generovanie kódu, refaktoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Všeobecné úlohy, efektívne | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rýchle, nízke nároky na zdroje | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasifikácia, minimálne nároky | 1-2GB | `-cpu`, `-cuda-gpu` |

### Názvoslovie variantov

- **Základný názov** (napr. `phi-4-mini`): Automaticky vyberie najlepší variant pre váš hardvér
- **`-cpu`**: Optimalizované pre CPU, funguje všade
- **`-cuda-gpu`**: Optimalizované pre NVIDIA GPU, vyžaduje 8GB+ VRAM
- **`-npu`**: Optimalizované pre Qualcomm NPU, vyžaduje NPU ovládače

**Odporúčanie:** Používajte základné názvy (bez prípony) a nechajte Foundry Local automaticky vybrať najlepší variant.

---

## Indikátory úspechu

Ste pripravení, keď vidíte:

✅ `foundry service status` ukazuje "running"
✅ `foundry model ls` ukazuje požadované modely
✅ Služba je dostupná na správnom endpointe
✅ Kontrola stavu vracia 200 OK
✅ Diagnostické bunky notebooku prešli
✅ Žiadne chyby pripojenia vo výstupe

---

## Získanie pomoci

### Dokumentácia
- **Hlavné úložisko**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referencia**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Riešenie problémov**: Pozrite si `troubleshooting.md` v tomto adresári

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Posledná aktualizácia:** 8. október 2025  
**Verzia:** Workshop Notebooks 2.0

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.