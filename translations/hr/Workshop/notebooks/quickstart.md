# Radionice - Brzi vodič za početak

## Sadržaj

- [Preduvjeti](../../../../Workshop/notebooks)
- [Početna postavka](../../../../Workshop/notebooks)
- [Sesija 04: Usporedba modela](../../../../Workshop/notebooks)
- [Sesija 05: Orkestrator s više agenata](../../../../Workshop/notebooks)
- [Sesija 06: Usmjeravanje modela prema namjeri](../../../../Workshop/notebooks)
- [Varijable okruženja](../../../../Workshop/notebooks)
- [Uobičajene naredbe](../../../../Workshop/notebooks)

---

## Preduvjeti

### 1. Instalirajte Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Provjera instalacije:**
```bash
foundry --version
```

### 2. Instalirajte Python ovisnosti

```bash
cd Workshop
pip install -r requirements.txt
```

Ili instalirajte pojedinačno:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Početna postavka

### Pokrenite Foundry Local servis

**Potrebno prije pokretanja bilo koje bilježnice:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Očekivani izlaz:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Preuzmite i učitajte modele

Bilježnice koriste sljedeće modele prema zadanim postavkama:

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

### Provjera postavki

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesija 04: Usporedba modela

### Svrha
Usporedite performanse između malih jezičnih modela (SLM) i velikih jezičnih modela (LLM).

### Brza postavka

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Pokretanje bilježnice

1. **Otvorite** `session04_model_compare.ipynb` u VS Code ili Jupyteru
2. **Ponovno pokrenite kernel** (Kernel → Restart Kernel)
3. **Pokrenite sve ćelije** redoslijedom

### Ključne postavke

**Zadani modeli:**
- **SLM:** `phi-4-mini` (~4GB RAM-a, brži)
- **LLM:** `qwen2.5-3b` (~3GB RAM-a, optimiziran za memoriju)

**Varijable okruženja (opcionalno):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Očekivani izlaz

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

### Prilagodba

**Koristite različite modele:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prilagođeni upit:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Lista za provjeru valjanosti

- [ ] Ćelija 12 prikazuje ispravne modele (phi-4-mini, qwen2.5-3b)
- [ ] Ćelija 12 prikazuje ispravan endpoint (port 59959)
- [ ] Dijagnostika ćelije 16 prolazi (✅ Servis radi)
- [ ] Provjera prije pokretanja ćelije 20 prolazi (oba modela u redu)
- [ ] Usporedba ćelije 22 završava s vrijednostima kašnjenja
- [ ] Validacija ćelije 24 prikazuje 🎉 SVI TESTOVI PROŠLI!

### Procjena vremena
- **Prvo pokretanje:** 5-10 minuta (uključujući preuzimanje modela)
- **Sljedeća pokretanja:** 1-2 minute

---

## Sesija 05: Orkestrator s više agenata

### Svrha
Demonstrirajte suradnju više agenata koristeći Foundry Local SDK - agenti rade zajedno kako bi proizveli poboljšane rezultate.

### Brza postavka

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Pokretanje bilježnice

1. **Otvorite** `session05_agents_orchestrator.ipynb`
2. **Ponovno pokrenite kernel**
3. **Pokrenite sve ćelije** redoslijedom

### Ključne postavke

**Zadana postavka (isti model za oba agenta):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Napredna postavka (različiti modeli):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arhitektura

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

### Očekivani izlaz

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

### Proširenja

**Dodajte više agenata:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Testiranje u serijama:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Procjena vremena
- **Prvo pokretanje:** 3-5 minuta
- **Sljedeća pokretanja:** 1-2 minute po pitanju

---

## Sesija 06: Usmjeravanje modela prema namjeri

### Svrha
Pametno usmjeravanje upita prema specijaliziranim modelima na temelju otkrivene namjere.

### Brza postavka

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Napomena:** Sesija 06 koristi CPU modele za maksimalnu kompatibilnost.

### Pokretanje bilježnice

1. **Otvorite** `session06_models_router.ipynb`
2. **Ponovno pokrenite kernel**
3. **Pokrenite sve ćelije** redoslijedom

### Ključne postavke

**Zadani katalog (CPU modeli):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (GPU modeli):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Otkrivanje namjere

Router koristi regex uzorke za otkrivanje namjere:

| Namjera | Primjeri uzoraka | Usmjereno na |
|---------|------------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Sve ostalo | phi-4-mini-cpu |

### Očekivani izlaz

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

### Prilagodba

**Dodajte prilagođenu namjeru:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Omogućite praćenje tokena:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Prebacivanje na GPU modele

Ako imate 8GB+ VRAM-a:

1. U **Ćeliji #6**, komentirajte CPU katalog
2. Otkomentirajte GPU katalog
3. Učitajte GPU modele:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Ponovno pokrenite kernel i ponovno pokrenite bilježnicu

### Procjena vremena
- **Prvo pokretanje:** 5-10 minuta (učitavanje modela)
- **Sljedeća pokretanja:** 30-60 sekundi po testu

---

## Varijable okruženja

### Globalna konfiguracija

Postavite prije pokretanja Jupyter/VS Code:

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

### Konfiguracija unutar bilježnice

Postavite na početku bilo koje bilježnice:

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

## Uobičajene naredbe

### Upravljanje servisom

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

### Upravljanje modelima

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

### Testiranje endpointa

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

### Dijagnostičke naredbe

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

## Najbolje prakse

### Prije pokretanja bilo koje bilježnice

1. **Provjerite je li servis pokrenut:**
   ```bash
   foundry service status
   ```

2. **Provjerite jesu li modeli učitani:**
   ```bash
   foundry model ls
   ```

3. **Ponovno pokrenite kernel bilježnice** ako ponovno pokrećete

4. **Očistite sve izlaze** za čisto pokretanje

### Upravljanje resursima

1. **Koristite CPU modele prema zadanim postavkama** za kompatibilnost
2. **Prebacite se na GPU modele** samo ako imate 8GB+ VRAM-a
3. **Zatvorite druge GPU aplikacije** prije pokretanja
4. **Održavajte servis pokrenutim** između sesija bilježnica
5. **Pratite korištenje resursa** pomoću Task Managera / nvidia-smi

### Rješavanje problema

1. **Uvijek prvo provjerite servis** prije otklanjanja grešaka u kodu
2. **Ponovno pokrenite kernel** ako vidite zastarjele postavke
3. **Ponovno pokrenite dijagnostičke ćelije** nakon bilo kakvih promjena
4. **Provjerite nazive modela** odgovaraju učitanima
5. **Provjerite port endpointa** odgovara statusu servisa

---

## Brzi pregled: Alias modela

### Uobičajeni modeli

| Alias | Veličina | Najbolje za | RAM/VRAM | Varijante |
|-------|----------|-------------|----------|-----------|
| `phi-4-mini` | ~4B | Opći chat, sažimanje | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generiranje koda, refaktoriranje | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Opći zadaci, učinkovito | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Brzo, malo resursa | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasifikacija, minimalni resursi | 1-2GB | `-cpu`, `-cuda-gpu` |

### Nazivanje varijanti

- **Osnovni naziv** (npr. `phi-4-mini`): Automatski odabire najbolju varijantu za vaš hardver
- **`-cpu`**: Optimizirano za CPU, radi svugdje
- **`-cuda-gpu`**: Optimizirano za NVIDIA GPU, zahtijeva 8GB+ VRAM-a
- **`-npu`**: Optimizirano za Qualcomm NPU, zahtijeva NPU upravljačke programe

**Preporuka:** Koristite osnovne nazive (bez sufiksa) i dopustite Foundry Localu da automatski odabere najbolju varijantu.

---

## Indikatori uspjeha

Spremni ste kada vidite:

✅ `foundry service status` prikazuje "running"
✅ `foundry model ls` prikazuje potrebne modele
✅ Servis dostupan na ispravnom endpointu
✅ Provjera zdravlja vraća 200 OK
✅ Dijagnostičke ćelije bilježnice prolaze
✅ Nema grešaka u povezivanju u izlazu

---

## Dobivanje pomoći

### Dokumentacija
- **Glavni repozitorij**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI referenca**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Rješavanje problema**: Pogledajte `troubleshooting.md` u ovom direktoriju

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Zadnje ažuriranje:** 8. listopada 2025.
**Verzija:** Workshop Notebooks 2.0

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.