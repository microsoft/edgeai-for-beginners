# Workshop Notebooks - Felsökningsguide

## Innehållsförteckning

- [Vanliga problem och lösningar](../../../../Workshop/notebooks)
- [Specifika problem för session 04](../../../../Workshop/notebooks)
- [Specifika problem för session 05](../../../../Workshop/notebooks)
- [Specifika problem för session 06](../../../../Workshop/notebooks)
- [Hårdvaruspecifika problem](../../../../Workshop/notebooks)
- [Diagnostiska kommandon](../../../../Workshop/notebooks)
- [Få hjälp](../../../../Workshop/notebooks)

---

## Vanliga problem och lösningar

### 🔴 CUDA Out of Memory

**Felmeddelande:**
```
CUDA failure 2: out of memory
```
  
**Orsak:** GPU:n har inte tillräckligt med VRAM för att ladda modellen.

**Lösningar:**

#### Alternativ 1: Använd CPU-varianter (Rekommenderas)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Alternativ 2: Använd mindre modeller på GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Alternativ 3: Rensa GPU-minne
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Alternativ 4: Öka GPU-minne (om möjligt)
- Stäng webbläsarflikar, videoredigeringsprogram eller andra GPU-appar
- Minska Windows visuella effekter
- Använd dedikerad GPU om du har både integrerad och dedikerad

---

### 🔴 APIConnectionError: Connection Error

**Felmeddelande:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Orsak:** Foundry Local-tjänsten körs inte eller är inte tillgänglig.

**Lösningar:**

#### Steg 1: Kontrollera tjänstens status
```bash
foundry service status
```
  
#### Steg 2: Starta tjänsten om den är stoppad
```bash
foundry service start
```
  
#### Steg 3: Verifiera endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Steg 4: Ladda nödvändiga modeller
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Steg 5: Starta om notebook-kärnan
Efter att ha startat tjänsten och laddat modeller, starta om notebook-kärnan och kör alla celler igen.

---

### 🔴 Modell hittas inte i katalogen

**Felmeddelande:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Orsak:** Modellen är inte nedladdad eller laddad i Foundry Local.

**Lösningar:**

#### Alternativ 1: Ladda ner och ladda modeller
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
  
#### Alternativ 2: Använd Auto-Selection Mode
Uppdatera din CATALOG för att använda basmodellnamn (utan `-cpu` suffix):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK väljer automatiskt den bästa varianten (CPU, GPU eller NPU) för din hårdvara.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Felmeddelande:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Orsak:** Modelfilen är korrupt eller inkompatibel med hårdvaran.

**Lösningar:**

#### Ladda ner modellen igen
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Använd en annan variant
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: No Module Found

**Felmeddelande:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Orsak:** foundry-local-sdk-paketet är inte installerat.

**Lösningar:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Långsam första begäran

**Symptom:** Första completion tar 30+ sekunder, efterföljande begäranden är snabba.

**Orsak:** Detta är normalt beteende - tjänsten laddar modellen i minnet vid första begäran.

**Lösningar:**

#### Förladda modeller
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Håll tjänsten igång
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## Specifika problem för session 04

### Fel portkonfiguration

**Problem:** Notebook ansluter till fel port (55769 vs 59959 vs 57127)

**Lösning:**

1. Kontrollera vilken port Foundry Local använder:
```bash
foundry service status
# Note the port number displayed
```
  
2. Uppdatera Cell 10 i notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Starta om kärnan och kör cellerna 6, 8, 10, 12, 16, 20, 22 igen

---

### Fel modellval

**Problem:** Notebook visar gpt-oss-20b eller qwen2.5-7b istället för qwen2.5-3b

**Lösning:**

1. Starta om notebook-kärnan (rensa gamla variabler)
2. Kör Cell 10 igen (Set Model Aliases)
3. Kör Cell 12 igen (Visa konfiguration)
4. **Verifiera:** Cell 12 ska visa `LLM Model: qwen2.5-3b`

---

### Diagnostisk cell misslyckas

**Problem:** Cell 16 visar "❌ Foundry Local service not found!"

**Lösning:**

1. Verifiera att tjänsten körs:
```bash
foundry service status
```
  
2. Testa endpoint manuellt:
```bash
curl http://localhost:59959/v1/models
```
  
3. Om curl fungerar men notebook inte gör det:
   - Starta om notebook-kärnan
   - Kör cellerna i ordning: 6, 8, 10, 12, 14, 16

4. Om curl misslyckas:
   - Starta tjänsten: `foundry service start`
   - Ladda modeller: `foundry model run phi-4-mini` och `foundry model run qwen2.5-3b`

---

### Pre-flight Check misslyckas

**Problem:** Cell 20 visar anslutningsfel trots att diagnostiken passerade

**Lösning:**

1. Kontrollera att modeller är laddade:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Om modeller saknas:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Kör Cell 20 igen efter att modellerna är laddade

---

### Jämförelse misslyckas med None-värden

**Problem:** Cell 22 slutförs men visar latens som None

**Lösning:**

1. Kontrollera att pre-flight passerade först (Cell 20)
2. Kör Cell 22 igen - modeller kan behöva värmas upp vid första begäran
3. Verifiera att båda modellerna är laddade: `foundry model ls`

---

## Specifika problem för session 05

### Agent använder fel modell

**Problem:** Agenten använder inte förväntad modell

**Lösning:**

Verifiera konfiguration:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Starta om kärnan om modellerna är felaktiga.

---

### Minneskontext överflöde

**Problem:** Agentens svar försämras över tid

**Lösning:** Redan hanterat automatiskt - agenter behåller endast de senaste 6 meddelandena i minnet.

---

## Specifika problem för session 06

### Förvirring mellan CPU och GPU-modeller

**Problem:** Får CUDA-fel när standardkonfiguration används

**Lösning:** Standardkonfigurationen använder nu CPU-modeller. Om du får CUDA-fel:

1. Verifiera att du använder standard CPU-katalogen:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Starta om kärnan och kör alla celler igen

---

### Intent-detektering fungerar inte

**Problem:** Prompter skickas till fel modeller

**Lösning:**

Testa intent-detektering:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Uppdatera RULES om mönster behöver justeras.

---

## Hårdvaruspecifika problem

### NVIDIA GPU

**Kontrollera GPU-status:**
```bash
nvidia-smi
```
  
**Vanliga problem:**
- **Drivrutin föråldrad**: Uppdatera NVIDIA-drivrutiner
- **CUDA-version mismatch**: Installera om Foundry Local
- **GPU-minne fragmenterat**: Starta om systemet

### Qualcomm NPU

**Kontrollera NPU-status:**
```bash
foundry device info
```
  
**Vanliga problem:**
- **NPU-drivrutiner inte installerade**: Installera Qualcomm NPU-drivrutiner
- **NPU-variant inte tillgänglig**: Använd CPU-variant
- **Windows-version för gammal**: Uppdatera till senaste Windows 11

### Endast CPU-system

**Rekommenderade modeller:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Prestandatips:**
- Använd de minsta modellerna
- Minska max_tokens
- Ha tålamod för första begäran

---

## Diagnostiska kommandon

### Kontrollera allt
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

## Få hjälp

### 1. Kontrollera loggar
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub Issues
- Sök befintliga problem: https://github.com/microsoft/Foundry-Local/issues
- Skapa nytt problem med:
  - Felmeddelande (fullständig text)
  - Output från `foundry service status`
  - Output från `foundry --version`
  - GPU/NPU-info (nvidia-smi, etc.)
  - Steg för att återskapa

### 3. Dokumentation
- **Huvudrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-referens**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Felsökning**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Snabbfix-checklista

När något går fel, prova dessa i ordning:

- [ ] Kontrollera att tjänsten körs: `foundry service status`
- [ ] Starta om tjänsten: `foundry service stop && foundry service start`
- [ ] Verifiera att modellen finns: `foundry model ls | grep phi-4-mini`
- [ ] Ladda nödvändiga modeller: `foundry model run phi-4-mini`
- [ ] Kontrollera GPU-minne: `nvidia-smi` (om NVIDIA)
- [ ] Prova CPU-variant: Använd `phi-4-mini-cpu` istället för `phi-4-mini`
- [ ] Starta om notebook-kärnan
- [ ] Rensa notebook-utdata och kör alla celler igen
- [ ] Installera om SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Starta om systemet (sista utväg)

---

## Förebyggande tips

### Bästa praxis

1. **Kontrollera alltid tjänsten först:**
   ```bash
   foundry service status
   ```
  
2. **Använd CPU-varianter som standard:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Förladda modeller innan du kör notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Håll tjänsten igång:**
   - Stoppa/starta inte tjänsten i onödan
   - Låt den köra i bakgrunden mellan sessioner

5. **Övervaka resurser:**
   - Kontrollera GPU-minne innan du kör
   - Stäng onödiga GPU-applikationer
   - Använd Task Manager / nvidia-smi

6. **Uppdatera regelbundet:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Senast uppdaterad:** 8 oktober 2025

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.