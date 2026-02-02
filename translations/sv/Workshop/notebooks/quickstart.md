# Workshop Notebooks - Snabbstartsguide

## Innehållsförteckning

- [Förutsättningar](../../../../Workshop/notebooks)
- [Initial inställning](../../../../Workshop/notebooks)
- [Session 04: Modelljämförelse](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent Orchestrator](../../../../Workshop/notebooks)
- [Session 06: Intentbaserad modellroutning](../../../../Workshop/notebooks)
- [Miljövariabler](../../../../Workshop/notebooks)
- [Vanliga kommandon](../../../../Workshop/notebooks)

---

## Förutsättningar

### 1. Installera Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifiera installation:**
```bash
foundry --version
```

### 2. Installera Python-beroenden

```bash
cd Workshop
pip install -r requirements.txt
```

Eller installera individuellt:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Initial inställning

### Starta Foundry Local-tjänsten

**Krävs innan du kör någon notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Förväntad output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Ladda ner och ladda modeller

Notebooks använder dessa modeller som standard:

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

### Verifiera inställning

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Modelljämförelse

### Syfte
Jämför prestanda mellan Small Language Models (SLM) och Large Language Models (LLM).

### Snabb inställning

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Köra notebooken

1. **Öppna** `session04_model_compare.ipynb` i VS Code eller Jupyter
2. **Starta om kärnan** (Kernel → Restart Kernel)
3. **Kör alla celler** i ordning

### Viktig konfiguration

**Standardmodeller:**
- **SLM:** `phi-4-mini` (~4GB RAM, snabbare)
- **LLM:** `qwen2.5-3b` (~3GB RAM, minnesoptimerad)

**Miljövariabler (valfritt):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Förväntad output

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

### Anpassning

**Använd olika modeller:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Anpassad prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Valideringschecklista

- [ ] Cell 12 visar korrekta modeller (phi-4-mini, qwen2.5-3b)
- [ ] Cell 12 visar korrekt endpoint (port 59959)
- [ ] Cell 16 diagnostik godkänd (✅ Tjänsten körs)
- [ ] Cell 20 förkontroll godkänd (båda modellerna ok)
- [ ] Cell 22 jämförelse slutförd med latensvärden
- [ ] Cell 24 validering visar 🎉 ALLA KONTROLLER GODKÄNDA!

### Tidsuppskattning
- **Första körning:** 5-10 minuter (inklusive modellnedladdningar)
- **Efterföljande körningar:** 1-2 minuter

---

## Session 05: Multi-Agent Orchestrator

### Syfte
Demonstrera samarbete mellan flera agenter med Foundry Local SDK - agenter arbetar tillsammans för att producera förfinade resultat.

### Snabb inställning

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Köra notebooken

1. **Öppna** `session05_agents_orchestrator.ipynb`
2. **Starta om kärnan**
3. **Kör alla celler** i ordning

### Viktig konfiguration

**Standardinställning (samma modell för båda agenterna):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Avancerad inställning (olika modeller):**
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

### Förväntad output

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

### Utvidgningar

**Lägg till fler agenter:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batchtestning:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Tidsuppskattning
- **Första körning:** 3-5 minuter
- **Efterföljande körningar:** 1-2 minuter per fråga

---

## Session 06: Intentbaserad modellroutning

### Syfte
Intelligent routning av prompts till specialiserade modeller baserat på upptäckt intent.

### Snabb inställning

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Obs:** Session 06 använder standardmässigt CPU-modeller för maximal kompatibilitet.

### Köra notebooken

1. **Öppna** `session06_models_router.ipynb`
2. **Starta om kärnan**
3. **Kör alla celler** i ordning

### Viktig konfiguration

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

### Intentdetektion

Routern använder regex-mönster för att upptäcka intent:

| Intent | Exempel på mönster | Routas till |
|--------|--------------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Allt annat | phi-4-mini-cpu |

### Förväntad output

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

### Anpassning

**Lägg till anpassad intent:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Aktivera token-spårning:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Växla till GPU-modeller

Om du har 8GB+ VRAM:

1. I **Cell #6**, kommentera bort CPU-katalogen
2. Avkommentera GPU-katalogen
3. Ladda GPU-modeller:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Starta om kärnan och kör notebooken igen

### Tidsuppskattning
- **Första körning:** 5-10 minuter (modellinladdning)
- **Efterföljande körningar:** 30-60 sekunder per test

---

## Miljövariabler

### Global konfiguration

Ställ in innan du startar Jupyter/VS Code:

**Windows (Kommandotolken):**
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

### Konfiguration i notebook

Ställ in i början av valfri notebook:

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

## Vanliga kommandon

### Tjänstehantering

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

### Modellhantering

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

### Testa endpoints

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

### Diagnostiska kommandon

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

## Bästa praxis

### Innan du startar någon notebook

1. **Kontrollera att tjänsten körs:**
   ```bash
   foundry service status
   ```

2. **Verifiera att modeller är laddade:**
   ```bash
   foundry model ls
   ```

3. **Starta om notebook-kärnan** om du kör om

4. **Rensa alla outputs** för en ren körning

### Resurshantering

1. **Använd CPU-modeller som standard** för kompatibilitet
2. **Växla till GPU-modeller** endast om du har 8GB+ VRAM
3. **Stäng andra GPU-applikationer** innan du kör
4. **Håll tjänsten igång** mellan notebook-sessioner
5. **Övervaka resursanvändning** med Aktivitetshanteraren / nvidia-smi

### Felsökning

1. **Kontrollera alltid tjänsten först** innan du felsöker kod
2. **Starta om kärnan** om du ser föråldrad konfiguration
3. **Kör diagnostiska celler igen** efter ändringar
4. **Kontrollera modellnamn** matchar det som är laddat
5. **Verifiera endpoint-port** matchar tjänstens status

---

## Snabbreferens: Modellalias

### Vanliga modeller

| Alias | Storlek | Bäst för | RAM/VRAM | Varianter |
|-------|---------|----------|----------|-----------|
| `phi-4-mini` | ~4B | Allmän chatt, sammanfattning | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kodgenerering, refaktorering | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Allmänna uppgifter, effektiv | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Snabb, låg resursanvändning | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klassificering, minimal resursanvändning | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variantnamngivning

- **Basnamn** (t.ex. `phi-4-mini`): Väljer automatiskt bästa variant för din hårdvara
- **`-cpu`**: CPU-optimerad, fungerar överallt
- **`-cuda-gpu`**: NVIDIA GPU-optimerad, kräver 8GB+ VRAM
- **`-npu`**: Qualcomm NPU-optimerad, kräver NPU-drivrutiner

**Rekommendation:** Använd basnamn (utan suffix) och låt Foundry Local automatiskt välja bästa variant.

---

## Framgångsindikatorer

Du är redo när du ser:

✅ `foundry service status` visar "running"
✅ `foundry model ls` visar dina nödvändiga modeller
✅ Tjänsten är tillgänglig på rätt endpoint
✅ Hälsokontroll returnerar 200 OK
✅ Notebook-diagnostiska celler godkända
✅ Inga anslutningsfel i output

---

## Få hjälp

### Dokumentation
- **Huvudrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-referens**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Felsökning**: Se `troubleshooting.md` i denna katalog

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Senast uppdaterad:** 8 oktober 2025  
**Version:** Workshop Notebooks 2.0

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.