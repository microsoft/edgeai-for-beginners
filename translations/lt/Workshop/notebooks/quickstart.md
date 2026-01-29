# Dirbtuvių užrašai - Greito starto vadovas

## Turinys

- [Būtinos sąlygos](../../../../Workshop/notebooks)
- [Pradinis nustatymas](../../../../Workshop/notebooks)
- [Sesija 04: Modelių palyginimas](../../../../Workshop/notebooks)
- [Sesija 05: Daugiaveiksmis orkestratorius](../../../../Workshop/notebooks)
- [Sesija 06: Ketinimų pagrindu pagrįstas modelių maršrutizavimas](../../../../Workshop/notebooks)
- [Aplinkos kintamieji](../../../../Workshop/notebooks)
- [Bendros komandos](../../../../Workshop/notebooks)

---

## Būtinos sąlygos

### 1. Įdiekite Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Patikrinkite diegimą:**
```bash
foundry --version
```

### 2. Įdiekite Python priklausomybes

```bash
cd Workshop
pip install -r requirements.txt
```

Arba įdiekite atskirai:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Pradinis nustatymas

### Paleiskite Foundry Local paslaugą

**Būtina prieš paleidžiant bet kurį užrašą:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Tikėtinas rezultatas:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Atsisiųskite ir įkelkite modelius

Užrašai pagal numatymą naudoja šiuos modelius:

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

### Patikrinkite nustatymus

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesija 04: Modelių palyginimas

### Tikslas
Palyginti mažų kalbos modelių (SLM) ir didelių kalbos modelių (LLM) našumą.

### Greitas nustatymas

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Užrašo paleidimas

1. **Atidarykite** `session04_model_compare.ipynb` VS Code arba Jupyter
2. **Paleiskite branduolį iš naujo** (Kernel → Restart Kernel)
3. **Paleiskite visas ląsteles** iš eilės

### Pagrindiniai nustatymai

**Numatytieji modeliai:**
- **SLM:** `phi-4-mini` (~4GB RAM, greitesnis)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimizuotas atminčiai)

**Aplinkos kintamieji (neprivaloma):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Tikėtinas rezultatas

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

### Pritaikymas

**Naudokite kitus modelius:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Individualus užklausos tekstas:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Patikrinimo sąrašas

- [ ] 12 ląstelėje rodomi teisingi modeliai (phi-4-mini, qwen2.5-3b)
- [ ] 12 ląstelėje rodomas teisingas galinis taškas (portas 59959)
- [ ] 16 ląstelės diagnostika sėkminga (✅ Paslauga veikia)
- [ ] 20 ląstelės išankstinis patikrinimas sėkmingas (abu modeliai gerai)
- [ ] 22 ląstelėje palyginimas baigtas su vėlavimo reikšmėmis
- [ ] 24 ląstelės patikrinimas rodo 🎉 VISI PATIKRINIMAI SĖKMINGI!

### Laiko sąnaudos
- **Pirmas paleidimas:** 5-10 minučių (įskaitant modelių atsisiuntimą)
- **Kiti paleidimai:** 1-2 minutės

---

## Sesija 05: Daugiaveiksmis orkestratorius

### Tikslas
Pademonstruoti daugiaveiksmį bendradarbiavimą naudojant Foundry Local SDK - agentai dirba kartu, kad sukurtų patobulintus rezultatus.

### Greitas nustatymas

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Užrašo paleidimas

1. **Atidarykite** `session05_agents_orchestrator.ipynb`
2. **Paleiskite branduolį iš naujo**
3. **Paleiskite visas ląsteles** iš eilės

### Pagrindiniai nustatymai

**Numatytasis nustatymas (tas pats modelis abiem agentams):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Išplėstinis nustatymas (skirtingi modeliai):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektūra

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

### Tikėtinas rezultatas

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

### Plėtiniai

**Pridėkite daugiau agentų:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Partijų testavimas:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Laiko sąnaudos
- **Pirmas paleidimas:** 3-5 minutės
- **Kiti paleidimai:** 1-2 minutės vienam klausimui

---

## Sesija 06: Ketinimų pagrindu pagrįstas modelių maršrutizavimas

### Tikslas
Protingai nukreipti užklausas į specializuotus modelius pagal nustatytą ketinimą.

### Greitas nustatymas

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Pastaba:** Sesija 06 pagal numatymą naudoja CPU modelius, kad užtikrintų maksimalų suderinamumą.

### Užrašo paleidimas

1. **Atidarykite** `session06_models_router.ipynb`
2. **Paleiskite branduolį iš naujo**
3. **Paleiskite visas ląsteles** iš eilės

### Pagrindiniai nustatymai

**Numatytasis katalogas (CPU modeliai):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatyva (GPU modeliai):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Ketinimų nustatymas

Maršrutizatorius naudoja regex šablonus ketinimams nustatyti:

| Ketinimas | Šablonų pavyzdžiai | Nukreipiama į |
|-----------|--------------------|---------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Viskas kita | phi-4-mini-cpu |

### Tikėtinas rezultatas

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

### Pritaikymas

**Pridėkite individualų ketinimą:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Įjunkite žetonų sekimą:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Perjungimas į GPU modelius

Jei turite 8GB+ VRAM:

1. **6 ląstelėje** užkomentuokite CPU katalogą
2. Atkomentuokite GPU katalogą
3. Įkelkite GPU modelius:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Paleiskite branduolį iš naujo ir vėl paleiskite užrašą

### Laiko sąnaudos
- **Pirmas paleidimas:** 5-10 minučių (modelių įkėlimas)
- **Kiti paleidimai:** 30-60 sekundžių vienam testui

---

## Aplinkos kintamieji

### Bendrasis nustatymas

Nustatykite prieš paleisdami Jupyter/VS Code:

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

### Užrašo nustatymas

Nustatykite užrašo pradžioje:

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

## Bendros komandos

### Paslaugų valdymas

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

### Modelių valdymas

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

### Galinių taškų testavimas

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

### Diagnostikos komandos

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

## Geriausia praktika

### Prieš pradedant bet kurį užrašą

1. **Patikrinkite, ar paslauga veikia:**
   ```bash
   foundry service status
   ```

2. **Patikrinkite, ar modeliai įkelti:**
   ```bash
   foundry model ls
   ```

3. **Paleiskite užrašo branduolį iš naujo**, jei paleidžiate iš naujo

4. **Išvalykite visus rezultatus**, kad pradėtumėte nuo švaraus lapo

### Išteklių valdymas

1. **Naudokite CPU modelius pagal numatymą**, kad užtikrintumėte suderinamumą
2. **Perjunkite į GPU modelius**, tik jei turite 8GB+ VRAM
3. **Uždarykite kitas GPU programas** prieš paleidžiant
4. **Laikykite paslaugą veikiančią** tarp užrašų sesijų
5. **Stebėkite išteklių naudojimą** naudodami Task Manager / nvidia-smi

### Trikčių šalinimas

1. **Visada pirmiausia patikrinkite paslaugą**, prieš taisydami kodą
2. **Paleiskite branduolį iš naujo**, jei matote pasenusį nustatymą
3. **Iš naujo paleiskite diagnostikos ląsteles** po bet kokių pakeitimų
4. **Patikrinkite modelių pavadinimus**, kad jie atitiktų įkeltus
5. **Patikrinkite galinio taško portą**, kad jis atitiktų paslaugos būseną

---

## Greita nuoroda: Modelių pavadinimai

### Dažniausiai naudojami modeliai

| Pavadinimas | Dydis | Geriausiai tinka | RAM/VRAM | Variantai |
|-------------|-------|------------------|----------|-----------|
| `phi-4-mini` | ~4B | Bendras pokalbis, santrauka | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kodo generavimas, perrašymas | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Bendros užduotys, efektyvumas | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Greitas, mažai išteklių reikalaujantis | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasifikacija, minimalūs ištekliai | 1-2GB | `-cpu`, `-cuda-gpu` |

### Varianto pavadinimai

- **Pagrindinis pavadinimas** (pvz., `phi-4-mini`): Automatiškai parenka geriausią variantą jūsų aparatūrai
- **`-cpu`**: Optimizuotas CPU, veikia visur
- **`-cuda-gpu`**: Optimizuotas NVIDIA GPU, reikalauja 8GB+ VRAM
- **`-npu`**: Optimizuotas Qualcomm NPU, reikalauja NPU tvarkyklių

**Rekomendacija:** Naudokite pagrindinius pavadinimus (be priesagos) ir leiskite Foundry Local automatiškai parinkti geriausią variantą.

---

## Sėkmės rodikliai

Jūs pasiruošę, kai matote:

✅ `foundry service status` rodo "veikia"  
✅ `foundry model ls` rodo reikiamus modelius  
✅ Paslauga pasiekiama teisingu galiniu tašku  
✅ Sveikatos patikrinimas grąžina 200 OK  
✅ Užrašo diagnostikos ląstelės sėkmingos  
✅ Nėra ryšio klaidų išvestyje  

---

## Pagalba

### Dokumentacija
- **Pagrindinis saugykla**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **CLI nuoroda**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Trikčių šalinimas**: Žr. `troubleshooting.md` šiame kataloge  

### GitHub klausimai
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**Paskutinį kartą atnaujinta:** 2025 m. spalio 8 d.  
**Versija:** Dirbtuvių užrašai 2.0

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.