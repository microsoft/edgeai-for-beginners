# Workshop Notebooks - Fejlfindingsguide

## Indholdsfortegnelse

- [Almindelige problemer og løsninger](../../../../Workshop/notebooks)
- [Specifikke problemer i session 04](../../../../Workshop/notebooks)
- [Specifikke problemer i session 05](../../../../Workshop/notebooks)
- [Specifikke problemer i session 06](../../../../Workshop/notebooks)
- [Hardware-specifikke problemer](../../../../Workshop/notebooks)
- [Diagnostiske kommandoer](../../../../Workshop/notebooks)
- [Få hjælp](../../../../Workshop/notebooks)

---

## Almindelige problemer og løsninger

### 🔴 CUDA Out of Memory

**Fejlmeddelelse:**
```
CUDA failure 2: out of memory
```
  
**Årsag:** GPU'en har ikke nok VRAM til at indlæse modellen.

**Løsninger:**

#### Mulighed 1: Brug CPU-varianter (anbefalet)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Mulighed 2: Brug mindre modeller på GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Mulighed 3: Ryd GPU-hukommelse
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Mulighed 4: Forøg GPU-hukommelse (hvis muligt)
- Luk browserfaner, videoredigeringsprogrammer eller andre GPU-apps
- Reducer Windows' visuelle effekter
- Brug dedikeret GPU, hvis du har både integreret og dedikeret GPU

---

### 🔴 APIConnectionError: Connection Error

**Fejlmeddelelse:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Årsag:** Foundry Local-tjenesten kører ikke eller er ikke tilgængelig.

**Løsninger:**

#### Trin 1: Tjek tjenestens status
```bash
foundry service status
```
  
#### Trin 2: Start tjenesten, hvis den er stoppet
```bash
foundry service start
```
  
#### Trin 3: Bekræft endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Trin 4: Indlæs nødvendige modeller
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Trin 5: Genstart notebook-kernen  
Efter at have startet tjenesten og indlæst modellerne, genstart notebook-kernen og kør alle celler igen.

---

### 🔴 Model ikke fundet i kataloget

**Fejlmeddelelse:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Årsag:** Modellen er ikke downloadet eller indlæst i Foundry Local.

**Løsninger:**

#### Mulighed 1: Download og indlæs modeller
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
  
#### Mulighed 2: Brug auto-selektionsmode  
Opdater dit CATALOG til at bruge basismodellernes navne (uden `-cpu` suffix):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK vælger automatisk den bedste variant (CPU, GPU eller NPU) til din hardware.

---

### 🔴 HttpResponseError: 500 - Fejl ved indlæsning af model

**Fejlmeddelelse:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Årsag:** Modelfilen er beskadiget eller inkompatibel med hardwaren.

**Løsninger:**

#### Download modellen igen
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Brug en anden variant
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: No Module Found

**Fejlmeddelelse:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Årsag:** foundry-local-sdk-pakken er ikke installeret.

**Løsninger:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Langsom første forespørgsel

**Symptom:** Første completion tager 30+ sekunder, efterfølgende forespørgsler er hurtige.

**Årsag:** Dette er normal opførsel - tjenesten indlæser modellen i hukommelsen ved første forespørgsel.

**Løsninger:**

#### Forudindlæs modeller
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Hold tjenesten kørende
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## Specifikke problemer i session 04

### Forkert portkonfiguration

**Problem:** Notebook forbinder til forkert port (55769 vs 59959 vs 57127)

**Løsning:**

1. Tjek hvilken port Foundry Local bruger:
```bash
foundry service status
# Note the port number displayed
```
  
2. Opdater celle 10 i notebooken:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Genstart kernen og kør cellerne 6, 8, 10, 12, 16, 20, 22 igen.

---

### Forkert modelvalg

**Problem:** Notebook viser gpt-oss-20b eller qwen2.5-7b i stedet for qwen2.5-3b

**Løsning:**

1. Genstart notebook-kernen (rydder gamle variabler)
2. Kør celle 10 igen (sæt modelaliaser)
3. Kør celle 12 igen (vis konfiguration)
4. **Bekræft:** Celle 12 skal vise `LLM Model: qwen2.5-3b`

---

### Diagnostisk celle fejler

**Problem:** Celle 16 viser "❌ Foundry Local service not found!"

**Løsning:**

1. Bekræft at tjenesten kører:
```bash
foundry service status
```
  
2. Test endpoint manuelt:
```bash
curl http://localhost:59959/v1/models
```
  
3. Hvis curl virker, men notebook ikke gør:
   - Genstart notebook-kernen
   - Kør cellerne i rækkefølge: 6, 8, 10, 12, 14, 16

4. Hvis curl fejler:
   - Start tjenesten: `foundry service start`
   - Indlæs modeller: `foundry model run phi-4-mini` og `foundry model run qwen2.5-3b`

---

### Pre-flight check fejler

**Problem:** Celle 20 viser forbindelsesfejl, selvom diagnostikken bestod

**Løsning:**

1. Tjek at modellerne er indlæst:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Hvis modeller mangler:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Kør celle 20 igen, efter modellerne er indlæst.

---

### Sammenligning fejler med None-værdier

**Problem:** Celle 22 fuldføres, men viser latenstid som None

**Løsning:**

1. Tjek at pre-flight bestod først (celle 20)
2. Kør celle 22 igen - modellerne skal muligvis "varmes op" ved første forespørgsel
3. Bekræft at begge modeller er indlæst: `foundry model ls`

---

## Specifikke problemer i session 05

### Agent bruger forkert model

**Problem:** Agenten bruger ikke den forventede model

**Løsning:**

Bekræft konfiguration:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Genstart kernen, hvis modellerne er forkerte.

---

### Hukommelseskontekst overflow

**Problem:** Agentens svar forringes over tid

**Løsning:** Allerede håndteret automatisk - agenter gemmer kun de sidste 6 beskeder i hukommelsen.

---

## Specifikke problemer i session 06

### Forvirring mellem CPU- og GPU-modeller

**Problem:** CUDA-fejl opstår, når standardkonfigurationen bruges

**Løsning:** Standardkonfigurationen bruger nu CPU-modeller. Hvis du ser CUDA-fejl:

1. Bekræft at du bruger standard CPU-kataloget:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Genstart kernen og kør alle celler igen.

---

### Intent-detektion virker ikke

**Problem:** Prompter bliver sendt til forkerte modeller

**Løsning:**

Test intent-detektion:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Opdater RULES, hvis mønstrene skal justeres.

---

## Hardware-specifikke problemer

### NVIDIA GPU

**Tjek GPU-status:**
```bash
nvidia-smi
```
  
**Almindelige problemer:**
- **Forældet driver:** Opdater NVIDIA-drivere
- **CUDA-version mismatch:** Geninstaller Foundry Local
- **Fragmenteret GPU-hukommelse:** Genstart systemet

### Qualcomm NPU

**Tjek NPU-status:**
```bash
foundry device info
```
  
**Almindelige problemer:**
- **NPU-drivere ikke installeret:** Installer Qualcomm NPU-drivere
- **NPU-variant ikke tilgængelig:** Brug CPU-variant
- **Windows-version for gammel:** Opdater til nyeste Windows 11

### Kun CPU-systemer

**Anbefalede modeller:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Ydelsestips:**
- Brug de mindste modeller
- Reducer max_tokens
- Hav tålmodighed med første forespørgsel

---

## Diagnostiske kommandoer

### Tjek alt
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
  
### I Python
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

## Få hjælp

### 1. Tjek logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub Issues
- Søg efter eksisterende problemer: https://github.com/microsoft/Foundry-Local/issues
- Opret et nyt problem med:
  - Fejlmeddelelse (fuld tekst)
  - Output fra `foundry service status`
  - Output fra `foundry --version`
  - GPU/NPU-info (nvidia-smi osv.)
  - Trin til at genskabe fejlen

### 3. Dokumentation
- **Hovedrepository:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Fejlfindingsguide:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Tjekliste til hurtige løsninger

Når noget går galt, prøv følgende i rækkefølge:

- [ ] Tjek at tjenesten kører: `foundry service status`
- [ ] Genstart tjenesten: `foundry service stop && foundry service start`
- [ ] Bekræft at modellen findes: `foundry model ls | grep phi-4-mini`
- [ ] Indlæs nødvendige modeller: `foundry model run phi-4-mini`
- [ ] Tjek GPU-hukommelse: `nvidia-smi` (hvis NVIDIA)
- [ ] Prøv CPU-variant: Brug `phi-4-mini-cpu` i stedet for `phi-4-mini`
- [ ] Genstart notebook-kernen
- [ ] Ryd notebook-outputs og kør alle celler igen
- [ ] Geninstaller SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Genstart systemet (sidste udvej)

---

## Forebyggelsestips

### Bedste praksis

1. **Tjek altid tjenesten først:**
   ```bash
   foundry service status
   ```
  
2. **Brug CPU-varianter som standard:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Forudindlæs modeller før du kører notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Hold tjenesten kørende:**
   - Stop/start ikke tjenesten unødvendigt
   - Lad den køre i baggrunden mellem sessioner

5. **Overvåg ressourcer:**
   - Tjek GPU-hukommelse før kørsel
   - Luk unødvendige GPU-applikationer
   - Brug Task Manager / nvidia-smi

6. **Opdater regelmæssigt:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Sidst opdateret:** 8. oktober 2025

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.