# Workshop Notebooks - Hurtigstartguide

## Innholdsfortegnelse

- [Forutsetninger](../../../../Workshop/notebooks)
- [Initial Oppsett](../../../../Workshop/notebooks)
- [Sesjon 04: Modell Sammenligning](../../../../Workshop/notebooks)
- [Sesjon 05: Multi-Agent Orkestrator](../../../../Workshop/notebooks)
- [Sesjon 06: Intent-Basert Modellruting](../../../../Workshop/notebooks)
- [Miljøvariabler](../../../../Workshop/notebooks)
- [Vanlige Kommandoer](../../../../Workshop/notebooks)

---

## Forutsetninger

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

**Verifiser installasjon:**
```bash
foundry --version
```

### 2. Installer Python-avhengigheter

```bash
cd Workshop
pip install -r requirements.txt
```

Eller installer individuelt:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Initial Oppsett

### Start Foundry Local-tjenesten

**Påkrevd før du kjører noen notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Forventet utdata:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Last ned og last inn modeller

Notebookene bruker disse modellene som standard:

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

### Verifiser oppsett

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesjon 04: Modell Sammenligning

### Formål
Sammenligne ytelsen mellom Small Language Models (SLM) og Large Language Models (LLM).

### Hurtigoppsett

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Kjøre notebooken

1. **Åpne** `session04_model_compare.ipynb` i VS Code eller Jupyter
2. **Start kernel på nytt** (Kernel → Restart Kernel)
3. **Kjør alle celler** i rekkefølge

### Viktig konfigurasjon

**Standardmodeller:**
- **SLM:** `phi-4-mini` (~4GB RAM, raskere)
- **LLM:** `qwen2.5-3b` (~3GB RAM, minneoptimalisert)

**Miljøvariabler (valgfritt):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Forventet utdata

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

**Bruk andre modeller:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Egendefinert prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Valideringskontrolliste

- [ ] Celle 12 viser riktige modeller (phi-4-mini, qwen2.5-3b)
- [ ] Celle 12 viser riktig endepunkt (port 59959)
- [ ] Celle 16 diagnostikk passerer (✅ Tjenesten kjører)
- [ ] Celle 20 forhåndssjekk passerer (begge modeller ok)
- [ ] Celle 22 sammenligning fullføres med latensverdier
- [ ] Celle 24 validering viser 🎉 ALL CHECKS PASSED!

### Tidsestimat
- **Første kjøring:** 5-10 minutter (inkludert modellnedlastinger)
- **Senere kjøringer:** 1-2 minutter

---

## Sesjon 05: Multi-Agent Orkestrator

### Formål
Demonstrere samarbeid mellom flere agenter ved bruk av Foundry Local SDK - agenter jobber sammen for å produsere forbedrede resultater.

### Hurtigoppsett

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Kjøre notebooken

1. **Åpne** `session05_agents_orchestrator.ipynb`
2. **Start kernel på nytt**
3. **Kjør alle celler** i rekkefølge

### Viktig konfigurasjon

**Standardoppsett (samme modell for begge agenter):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Avansert oppsett (forskjellige modeller):**
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

### Forventet utdata

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

### Utvidelser

**Legg til flere agenter:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch-testing:**
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
- **Første kjøring:** 3-5 minutter
- **Senere kjøringer:** 1-2 minutter per spørsmål

---

## Sesjon 06: Intent-Basert Modellruting

### Formål
Rute forespørsler til spesialiserte modeller basert på oppdaget intensjon.

### Hurtigoppsett

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Merk:** Sesjon 06 bruker som standard CPU-modeller for maksimal kompatibilitet.

### Kjøre notebooken

1. **Åpne** `session06_models_router.ipynb`
2. **Start kernel på nytt**
3. **Kjør alle celler** i rekkefølge

### Viktig konfigurasjon

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

### Intentdeteksjon

Routeren bruker regex-mønstre for å oppdage intensjon:

| Intensjon | Eksempler på mønstre | Rutes til |
|-----------|----------------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Alt annet | phi-4-mini-cpu |

### Forventet utdata

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

**Legg til egendefinert intensjon:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Aktiver token-sporing:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Bytte til GPU-modeller

Hvis du har 8GB+ VRAM:

1. I **Celle #6**, kommenter ut CPU-katalogen
2. Fjern kommentar på GPU-katalogen
3. Last inn GPU-modeller:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Start kernel på nytt og kjør notebooken på nytt

### Tidsestimat
- **Første kjøring:** 5-10 minutter (modellinnlasting)
- **Senere kjøringer:** 30-60 sekunder per test

---

## Miljøvariabler

### Global konfigurasjon

Sett før du starter Jupyter/VS Code:

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

### Konfigurasjon i notebook

Sett i starten av hvilken som helst notebook:

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

## Vanlige Kommandoer

### Tjenestestyring

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

### Modellstyring

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

### Testing av endepunkter

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

### Diagnostiske kommandoer

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

## Beste Praksis

### Før du starter noen notebook

1. **Sjekk at tjenesten kjører:**
   ```bash
   foundry service status
   ```

2. **Verifiser at modeller er lastet inn:**
   ```bash
   foundry model ls
   ```

3. **Start notebook-kernel på nytt** hvis du kjører på nytt

4. **Tøm alle utdata** for en ren kjøring

### Ressursstyring

1. **Bruk CPU-modeller som standard** for kompatibilitet
2. **Bytt til GPU-modeller** kun hvis du har 8GB+ VRAM
3. **Lukk andre GPU-applikasjoner** før kjøring
4. **Hold tjenesten i gang** mellom notebook-sesjoner
5. **Overvåk ressursbruk** med Oppgavebehandling / nvidia-smi

### Feilsøking

1. **Sjekk alltid tjenesten først** før du feilsøker kode
2. **Start kernel på nytt** hvis du ser gammel konfigurasjon
3. **Kjør diagnostiske celler på nytt** etter endringer
4. **Sjekk at modellnavn** samsvarer med det som er lastet inn
5. **Verifiser endepunktport** samsvarer med tjenestestatus

---

## Hurtigreferanse: Modellaliaser

### Vanlige modeller

| Alias | Størrelse | Best til | RAM/VRAM | Varianter |
|-------|-----------|----------|----------|-----------|
| `phi-4-mini` | ~4B | Generell chat, oppsummering | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kodegenerering, refaktorering | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Generelle oppgaver, effektiv | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rask, lav ressursbruk | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klassifisering, minimal ressursbruk | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variantnavngivning

- **Grunnnavn** (f.eks., `phi-4-mini`): Velger automatisk beste variant for maskinvaren din
- **`-cpu`**: CPU-optimalisert, fungerer overalt
- **`-cuda-gpu`**: NVIDIA GPU-optimalisert, krever 8GB+ VRAM
- **`-npu`**: Qualcomm NPU-optimalisert, krever NPU-drivere

**Anbefaling:** Bruk grunnnavn (uten suffiks) og la Foundry Local velge beste variant automatisk.

---

## Suksessindikatorer

Du er klar når du ser:

✅ `foundry service status` viser "running"
✅ `foundry model ls` viser de nødvendige modellene
✅ Tjenesten er tilgjengelig på riktig endepunkt
✅ Helsesjekk returnerer 200 OK
✅ Notebook-diagnostiske celler passerer
✅ Ingen tilkoblingsfeil i utdata

---

## Få Hjelp

### Dokumentasjon
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-referanse**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Feilsøking**: Se `troubleshooting.md` i denne katalogen

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Sist oppdatert:** 8. oktober 2025  
**Versjon:** Workshop Notebooks 2.0

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.