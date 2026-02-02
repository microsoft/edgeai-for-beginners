# Workshop Notebooks - Hurtig Start Guide

## Indholdsfortegnelse

- [Forudsætninger](../../../../Workshop/notebooks)
- [Initial Opsætning](../../../../Workshop/notebooks)
- [Session 04: Model Sammenligning](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent Orkestrator](../../../../Workshop/notebooks)
- [Session 06: Intent-Baseret Model Routing](../../../../Workshop/notebooks)
- [Miljøvariabler](../../../../Workshop/notebooks)
- [Almindelige Kommandoer](../../../../Workshop/notebooks)

---

## Forudsætninger

### 1. Installer Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Bekræft Installation:**
```bash
foundry --version
```

### 2. Installer Python-afhængigheder

```bash
cd Workshop
pip install -r requirements.txt
```

Eller installer individuelt:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Initial Opsætning

### Start Foundry Local Service

**Påkrævet før du kører nogen notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Forventet output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Download og Indlæs Modeller

Notebooks bruger disse modeller som standard:

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

### Bekræft Opsætning

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Model Sammenligning

### Formål
Sammenlign ydeevne mellem Small Language Models (SLM) og Large Language Models (LLM).

### Hurtig Opsætning

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Kør Notebook

1. **Åbn** `session04_model_compare.ipynb` i VS Code eller Jupyter
2. **Genstart kernel** (Kernel → Restart Kernel)
3. **Kør alle celler** i rækkefølge

### Nøglekonfiguration

**Standardmodeller:**
- **SLM:** `phi-4-mini` (~4GB RAM, hurtigere)
- **LLM:** `qwen2.5-3b` (~3GB RAM, hukommelsesoptimeret)

**Miljøvariabler (valgfrit):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Forventet Output

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

### Tilpasning

**Brug andre modeller:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Tilpasset prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Valideringscheckliste

- [ ] Celle 12 viser korrekte modeller (phi-4-mini, qwen2.5-3b)
- [ ] Celle 12 viser korrekt endpoint (port 59959)
- [ ] Celle 16 diagnosticering passerer (✅ Service kører)
- [ ] Celle 20 pre-flight check passerer (begge modeller ok)
- [ ] Celle 22 sammenligning fuldføres med latenstider
- [ ] Celle 24 validering viser 🎉 ALLE CHECKS PASSED!

### Tidsestimat
- **Første kørsel:** 5-10 minutter (inklusive modeldownloads)
- **Efterfølgende kørsler:** 1-2 minutter

---

## Session 05: Multi-Agent Orkestrator

### Formål
Demonstrer multi-agent samarbejde ved hjælp af Foundry Local SDK - agenter arbejder sammen for at producere forbedrede outputs.

### Hurtig Opsætning

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Kør Notebook

1. **Åbn** `session05_agents_orchestrator.ipynb`
2. **Genstart kernel**
3. **Kør alle celler** i rækkefølge

### Nøglekonfiguration

**Standardopsætning (Samme Model for Begge Agenter):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Avanceret Opsætning (Forskellige Modeller):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arkitektur

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

### Forventet Output

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

### Udvidelser

**Tilføj flere agenter:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch-testning:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Tidsestimat
- **Første kørsel:** 3-5 minutter
- **Efterfølgende kørsler:** 1-2 minutter pr. spørgsmål

---

## Session 06: Intent-Baseret Model Routing

### Formål
Intelligent routing af prompts til specialiserede modeller baseret på detekteret intent.

### Hurtig Opsætning

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Bemærk:** Session 06 bruger som standard CPU-modeller for maksimal kompatibilitet.

### Kør Notebook

1. **Åbn** `session06_models_router.ipynb`
2. **Genstart kernel**
3. **Kør alle celler** i rækkefølge

### Nøglekonfiguration

**Standardkatalog (CPU-modeller):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativ (GPU-modeller):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Intent-detektering

Routeren bruger regex-mønstre til at detektere intent:

| Intent | Eksempler på Mønstre | Routed Til |
|--------|----------------------|------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Alt andet | phi-4-mini-cpu |

### Forventet Output

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

### Tilpasning

**Tilføj tilpasset intent:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Aktiver token-tracking:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Skift til GPU-modeller

Hvis du har 8GB+ VRAM:

1. I **Celle #6**, kommenter CPU-kataloget ud
2. Fjern kommentar fra GPU-kataloget
3. Indlæs GPU-modeller:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Genstart kernel og kør notebook igen

### Tidsestimat
- **Første kørsel:** 5-10 minutter (modelloading)
- **Efterfølgende kørsler:** 30-60 sekunder pr. test

---

## Miljøvariabler

### Global Konfiguration

Sæt før start af Jupyter/VS Code:

**Windows (Kommandoprompt):**
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

### I-Notebook Konfiguration

Sæt i starten af enhver notebook:

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

## Almindelige Kommandoer

### Servicehåndtering

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

### Modelhåndtering

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

### Test af Endpoints

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

### Diagnostiske Kommandoer

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

## Bedste Fremgangsmåder

### Før Start af Enhver Notebook

1. **Tjek at service kører:**
   ```bash
   foundry service status
   ```

2. **Bekræft at modeller er indlæst:**
   ```bash
   foundry model ls
   ```

3. **Genstart notebook kernel** hvis du kører igen

4. **Ryd alle outputs** for en ren kørsel

### Ressourcestyring

1. **Brug CPU-modeller som standard** for kompatibilitet
2. **Skift til GPU-modeller** kun hvis du har 8GB+ VRAM
3. **Luk andre GPU-applikationer** før kørsel
4. **Hold service kørende** mellem notebook-sessioner
5. **Overvåg ressourceforbrug** med Task Manager / nvidia-smi

### Fejlfinding

1. **Tjek altid service først** før du fejlsøger kode
2. **Genstart kernel** hvis du ser forældet konfiguration
3. **Kør diagnostiske celler igen** efter ændringer
4. **Tjek modelnavne** matcher det, der er indlæst
5. **Bekræft endpoint-port** matcher servicestatus

---

## Hurtig Reference: Model Aliaser

### Almindelige Modeller

| Alias | Størrelse | Bedst Til | RAM/VRAM | Varianter |
|-------|-----------|-----------|----------|-----------|
| `phi-4-mini` | ~4B | Generel chat, opsummering | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kodegenerering, refaktorering | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Generelle opgaver, effektiv | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Hurtig, lavt ressourceforbrug | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klassifikation, minimalt ressourceforbrug | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variantnavngivning

- **Basenavn** (f.eks. `phi-4-mini`): Auto-vælger den bedste variant til din hardware
- **`-cpu`**: CPU-optimeret, fungerer overalt
- **`-cuda-gpu`**: NVIDIA GPU-optimeret, kræver 8GB+ VRAM
- **`-npu`**: Qualcomm NPU-optimeret, kræver NPU-drivere

**Anbefaling:** Brug basenavne (uden suffix) og lad Foundry Local auto-vælge den bedste variant.

---

## Succeskriterier

Du er klar, når du ser:

✅ `foundry service status` viser "running"  
✅ `foundry model ls` viser dine nødvendige modeller  
✅ Service tilgængelig på det korrekte endpoint  
✅ Health check returnerer 200 OK  
✅ Notebook-diagnostiske celler passerer  
✅ Ingen forbindelsesfejl i output  

---

## Få Hjælp

### Dokumentation
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Fejlfinding**: Se `troubleshooting.md` i denne mappe

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Sidst Opdateret:** 8. oktober 2025  
**Version:** Workshop Notebooks 2.0

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.