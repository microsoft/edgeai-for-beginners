# Ghid Rapid pentru Workshop Notebooks

## Cuprins

- [Prerechizite](../../../../Workshop/notebooks)
- [Configurare Inițială](../../../../Workshop/notebooks)
- [Sesiunea 04: Compararea Modelelor](../../../../Workshop/notebooks)
- [Sesiunea 05: Orchestrator Multi-Agent](../../../../Workshop/notebooks)
- [Sesiunea 06: Rutare pe Bază de Intenție](../../../../Workshop/notebooks)
- [Variabile de Mediu](../../../../Workshop/notebooks)
- [Comenzi Comune](../../../../Workshop/notebooks)

---

## Prerechizite

### 1. Instalează Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifică Instalarea:**
```bash
foundry --version
```

### 2. Instalează Dependențele Python

```bash
cd Workshop
pip install -r requirements.txt
```

Sau instalează individual:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Configurare Inițială

### Pornește Serviciul Foundry Local

**Necesar înainte de a rula orice notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Rezultatul așteptat:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Descarcă și Încarcă Modelele

Notebook-urile folosesc aceste modele implicit:

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

### Verifică Configurarea

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesiunea 04: Compararea Modelelor

### Scop
Compară performanța între Modele de Limbaj Mici (SLM) și Modele de Limbaj Mari (LLM).

### Configurare Rapidă

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Rularea Notebook-ului

1. **Deschide** `session04_model_compare.ipynb` în VS Code sau Jupyter
2. **Repornește kernel-ul** (Kernel → Restart Kernel)
3. **Rulează toate celulele** în ordine

### Configurare Cheie

**Modele Implicite:**
- **SLM:** `phi-4-mini` (~4GB RAM, mai rapid)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimizat pentru memorie)

**Variabile de Mediu (opțional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Rezultatul Așteptat

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

### Personalizare

**Folosește modele diferite:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt personalizat:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Listă de Verificare pentru Validare

- [ ] Celula 12 afișează modelele corecte (phi-4-mini, qwen2.5-3b)
- [ ] Celula 12 afișează endpoint-ul corect (port 59959)
- [ ] Diagnosticul din celula 16 trece (✅ Serviciul este activ)
- [ ] Verificarea prealabilă din celula 20 trece (ambele modele sunt ok)
- [ ] Compararea din celula 22 se finalizează cu valori de latență
- [ ] Validarea din celula 24 afișează 🎉 TOATE VERIFICĂRILE AU TRECUT!

### Estimare Timp
- **Prima rulare:** 5-10 minute (inclusiv descărcarea modelelor)
- **Rulări ulterioare:** 1-2 minute

---

## Sesiunea 05: Orchestrator Multi-Agent

### Scop
Demonstrează colaborarea multi-agent folosind Foundry Local SDK - agenții lucrează împreună pentru a produce rezultate rafinate.

### Configurare Rapidă

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Rularea Notebook-ului

1. **Deschide** `session05_agents_orchestrator.ipynb`
2. **Repornește kernel-ul**
3. **Rulează toate celulele** în ordine

### Configurare Cheie

**Configurație Implicită (Același Model pentru Ambii Agenți):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Configurație Avansată (Modele Diferite):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arhitectură

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

### Rezultatul Așteptat

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

### Extensii

**Adaugă mai mulți agenți:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Testare în loturi:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Estimare Timp
- **Prima rulare:** 3-5 minute
- **Rulări ulterioare:** 1-2 minute per întrebare

---

## Sesiunea 06: Rutare pe Bază de Intenție

### Scop
Rutează inteligent prompturile către modele specializate pe baza intenției detectate.

### Configurare Rapidă

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Notă:** Sesiunea 06 folosește modele CPU implicit pentru compatibilitate maximă.

### Rularea Notebook-ului

1. **Deschide** `session06_models_router.ipynb`
2. **Repornește kernel-ul**
3. **Rulează toate celulele** în ordine

### Configurare Cheie

**Catalog Implicit (Modele CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativă (Modele GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Detectarea Intenției

Router-ul folosește expresii regex pentru a detecta intenția:

| Intenție | Exemple de Pattern | Rutat Către |
|----------|--------------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Orice altceva | phi-4-mini-cpu |

### Rezultatul Așteptat

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

### Personalizare

**Adaugă intenții personalizate:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Activează urmărirea token-urilor:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Trecerea la Modele GPU

Dacă ai 8GB+ VRAM:

1. În **Celula #6**, comentează catalogul CPU
2. Decomentează catalogul GPU
3. Încarcă modelele GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Repornește kernel-ul și rulează din nou notebook-ul

### Estimare Timp
- **Prima rulare:** 5-10 minute (încărcarea modelelor)
- **Rulări ulterioare:** 30-60 secunde per test

---

## Variabile de Mediu

### Configurare Globală

Setează înainte de a porni Jupyter/VS Code:

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

### Configurare în Notebook

Setează la începutul oricărui notebook:

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

## Comenzi Comune

### Managementul Serviciului

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

### Managementul Modelelor

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

### Testarea Endpoint-urilor

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

### Comenzi de Diagnostic

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

## Cele Mai Bune Practici

### Înainte de a Porni Orice Notebook

1. **Verifică dacă serviciul este activ:**
   ```bash
   foundry service status
   ```

2. **Asigură-te că modelele sunt încărcate:**
   ```bash
   foundry model ls
   ```

3. **Repornește kernel-ul notebook-ului** dacă rulezi din nou

4. **Șterge toate rezultatele** pentru o rulare curată

### Managementul Resurselor

1. **Folosește modele CPU implicit** pentru compatibilitate
2. **Treci la modele GPU** doar dacă ai 8GB+ VRAM
3. **Închide alte aplicații GPU** înainte de rulare
4. **Menține serviciul activ** între sesiunile notebook
5. **Monitorizează utilizarea resurselor** cu Task Manager / nvidia-smi

### Depanare

1. **Verifică întotdeauna serviciul mai întâi** înainte de a depana codul
2. **Repornește kernel-ul** dacă vezi configurații vechi
3. **Rulează din nou celulele de diagnostic** după orice modificare
4. **Verifică numele modelelor** să corespundă cu cele încărcate
5. **Asigură-te că portul endpoint** corespunde cu starea serviciului

---

## Referință Rapidă: Aliasuri Modele

### Modele Comune

| Alias | Dimensiune | Cel Mai Bun Pentru | RAM/VRAM | Variante |
|-------|------------|--------------------|----------|----------|
| `phi-4-mini` | ~4B | Chat general, sumarizare | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generare cod, refactorizare | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Sarcini generale, eficient | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rapid, resurse reduse | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Clasificare, resurse minime | 1-2GB | `-cpu`, `-cuda-gpu` |

### Denumirea Variantelor

- **Nume de bază** (ex.: `phi-4-mini`): Selectează automat cea mai bună variantă pentru hardware-ul tău
- **`-cpu`**: Optimizat pentru CPU, funcționează peste tot
- **`-cuda-gpu`**: Optimizat pentru GPU NVIDIA, necesită 8GB+ VRAM
- **`-npu`**: Optimizat pentru NPU Qualcomm, necesită drivere NPU

**Recomandare:** Folosește numele de bază (fără sufix) și lasă Foundry Local să selecteze automat cea mai bună variantă.

---

## Indicatori de Succes

Ești pregătit când vezi:

✅ `foundry service status` afișează "running"  
✅ `foundry model ls` afișează modelele necesare  
✅ Serviciul este accesibil la endpoint-ul corect  
✅ Verificarea de sănătate returnează 200 OK  
✅ Celulele de diagnostic din notebook trec  
✅ Nu există erori de conexiune în rezultate  

---

## Obținerea Ajutorului

### Documentație
- **Repository Principal:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referință CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Depanare:** Vezi `troubleshooting.md` în acest director

### Probleme pe GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Ultima Actualizare:** 8 Octombrie 2025  
**Versiune:** Workshop Notebooks 2.0

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.