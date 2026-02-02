# Workshop Notebooks - Snelstartgids

## Inhoudsopgave

- [Vereisten](../../../../Workshop/notebooks)
- [Initiële Setup](../../../../Workshop/notebooks)
- [Sessie 04: Modelvergelijking](../../../../Workshop/notebooks)
- [Sessie 05: Multi-Agent Orchestrator](../../../../Workshop/notebooks)
- [Sessie 06: Intent-gebaseerde Modelroutering](../../../../Workshop/notebooks)
- [Omgevingsvariabelen](../../../../Workshop/notebooks)
- [Algemene Commando's](../../../../Workshop/notebooks)

---

## Vereisten

### 1. Installeer Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installatie verifiëren:**
```bash
foundry --version
```

### 2. Installeer Python-afhankelijkheden

```bash
cd Workshop
pip install -r requirements.txt
```

Of installeer afzonderlijk:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Initiële Setup

### Start Foundry Local Service

**Vereist voordat je een notebook uitvoert:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Verwachte output:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Modellen downloaden en laden

De notebooks gebruiken standaard deze modellen:

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

### Setup verifiëren

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sessie 04: Modelvergelijking

### Doel
Vergelijk de prestaties tussen Small Language Models (SLM) en Large Language Models (LLM).

### Snelle Setup

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Notebook uitvoeren

1. **Open** `session04_model_compare.ipynb` in VS Code of Jupyter
2. **Herstart kernel** (Kernel → Herstart Kernel)
3. **Voer alle cellen uit** in volgorde

### Belangrijke Configuratie

**Standaardmodellen:**
- **SLM:** `phi-4-mini` (~4GB RAM, sneller)
- **LLM:** `qwen2.5-3b` (~3GB RAM, geheugen-geoptimaliseerd)

**Omgevingsvariabelen (optioneel):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Verwachte Output

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

### Aanpassing

**Gebruik andere modellen:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Aangepaste prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Validatiechecklist

- [ ] Cel 12 toont correcte modellen (phi-4-mini, qwen2.5-3b)
- [ ] Cel 12 toont correcte endpoint (poort 59959)
- [ ] Cel 16 diagnostiek slaagt (✅ Service draait)
- [ ] Cel 20 pre-flight check slaagt (beide modellen oké)
- [ ] Cel 22 vergelijking voltooid met latentie-waarden
- [ ] Cel 24 validatie toont 🎉 ALLE CHECKS GESLAAGD!

### Tijdsschatting
- **Eerste keer uitvoeren:** 5-10 minuten (inclusief modeldownloads)
- **Volgende keren:** 1-2 minuten

---

## Sessie 05: Multi-Agent Orchestrator

### Doel
Toon samenwerking tussen meerdere agents met Foundry Local SDK - agents werken samen om verfijnde outputs te produceren.

### Snelle Setup

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Notebook uitvoeren

1. **Open** `session05_agents_orchestrator.ipynb`
2. **Herstart kernel**
3. **Voer alle cellen uit** in volgorde

### Belangrijke Configuratie

**Standaard Setup (Zelfde Model voor Beide Agents):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Geavanceerde Setup (Verschillende Modellen):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architectuur

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

### Verwachte Output

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

### Uitbreidingen

**Voeg meer agents toe:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch testen:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Tijdsschatting
- **Eerste keer uitvoeren:** 3-5 minuten
- **Volgende keren:** 1-2 minuten per vraag

---

## Sessie 06: Intent-gebaseerde Modelroutering

### Doel
Routeer prompts intelligent naar gespecialiseerde modellen op basis van gedetecteerde intentie.

### Snelle Setup

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Opmerking:** Sessie 06 gebruikt standaard CPU-modellen voor maximale compatibiliteit.

### Notebook uitvoeren

1. **Open** `session06_models_router.ipynb`
2. **Herstart kernel**
3. **Voer alle cellen uit** in volgorde

### Belangrijke Configuratie

**Standaardcatalogus (CPU-modellen):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatief (GPU-modellen):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Intentdetectie

De router gebruikt regex-patronen om intenties te detecteren:

| Intentie | Voorbeeldpatronen | Gerouteerd naar |
|----------|-------------------|-----------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Alles anders | phi-4-mini-cpu |

### Verwachte Output

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

### Aanpassing

**Voeg aangepaste intentie toe:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Schakel token-tracking in:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Overschakelen naar GPU-modellen

Als je 8GB+ VRAM hebt:

1. In **Cel #6**, commentaar CPU-catalogus uit
2. Haal commentaar weg bij GPU-catalogus
3. Laad GPU-modellen:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Herstart kernel en voer notebook opnieuw uit

### Tijdsschatting
- **Eerste keer uitvoeren:** 5-10 minuten (modellen laden)
- **Volgende keren:** 30-60 seconden per test

---

## Omgevingsvariabelen

### Globale Configuratie

Instellen voordat je Jupyter/VS Code start:

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

### Configuratie in Notebook

Instellen aan het begin van een notebook:

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

## Algemene Commando's

### Servicemanagement

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

### Modelmanagement

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

### Endpoints testen

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

### Diagnostische Commando's

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

## Beste Praktijken

### Voordat je een Notebook start

1. **Controleer of de service draait:**
   ```bash
   foundry service status
   ```

2. **Verifieer of modellen geladen zijn:**
   ```bash
   foundry model ls
   ```

3. **Herstart de notebook kernel** als je opnieuw uitvoert

4. **Wis alle outputs** voor een schone run

### Resourcebeheer

1. **Gebruik standaard CPU-modellen** voor compatibiliteit
2. **Schakel over naar GPU-modellen** alleen als je 8GB+ VRAM hebt
3. **Sluit andere GPU-applicaties** voordat je uitvoert
4. **Houd de service draaiend** tussen notebooksessies
5. **Monitor resourcegebruik** met Taakbeheer / nvidia-smi

### Probleemoplossing

1. **Controleer altijd eerst de service** voordat je code debugt
2. **Herstart kernel** als je verouderde configuratie ziet
3. **Voer diagnostische cellen opnieuw uit** na wijzigingen
4. **Controleer of modelnamen** overeenkomen met wat geladen is
5. **Verifieer endpointpoort** komt overeen met servicestatus

---

## Snelle Referentie: Modelaliassen

### Veelgebruikte Modellen

| Alias | Grootte | Beste Voor | RAM/VRAM | Varianten |
|-------|---------|------------|----------|-----------|
| `phi-4-mini` | ~4B | Algemene chat, samenvatting | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Codegeneratie, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Algemene taken, efficiënt | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Snel, weinig resources | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classificatie, minimale resources | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variantbenaming

- **Basisnaam** (bijv. `phi-4-mini`): Selecteert automatisch de beste variant voor je hardware
- **`-cpu`**: CPU-geoptimaliseerd, werkt overal
- **`-cuda-gpu`**: NVIDIA GPU-geoptimaliseerd, vereist 8GB+ VRAM
- **`-npu`**: Qualcomm NPU-geoptimaliseerd, vereist NPU-drivers

**Aanbeveling:** Gebruik basisnamen (zonder achtervoegsel) en laat Foundry Local automatisch de beste variant selecteren.

---

## Succesindicatoren

Je bent klaar als je ziet:

✅ `foundry service status` toont "running"  
✅ `foundry model ls` toont je vereiste modellen  
✅ Service toegankelijk op het juiste endpoint  
✅ Health check retourneert 200 OK  
✅ Notebook diagnostische cellen slagen  
✅ Geen verbindingsfouten in de output  

---

## Hulp krijgen

### Documentatie
- **Hoofdrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referentie**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Probleemoplossing**: Zie `troubleshooting.md` in deze map

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Laatst bijgewerkt:** 8 oktober 2025  
**Versie:** Workshop Notebooks 2.0  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.