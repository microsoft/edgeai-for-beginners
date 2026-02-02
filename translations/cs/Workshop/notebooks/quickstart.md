# Workshop Notebooks - Rychlý průvodce

## Obsah

- [Předpoklady](../../../../Workshop/notebooks)
- [Počáteční nastavení](../../../../Workshop/notebooks)
- [Sezení 04: Porovnání modelů](../../../../Workshop/notebooks)
- [Sezení 05: Orchestrátor pro více agentů](../../../../Workshop/notebooks)
- [Sezení 06: Směrování modelů na základě záměru](../../../../Workshop/notebooks)
- [Proměnné prostředí](../../../../Workshop/notebooks)
- [Běžné příkazy](../../../../Workshop/notebooks)

---

## Předpoklady

### 1. Instalace Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Ověření instalace:**
```bash
foundry --version
```

### 2. Instalace Python závislostí

```bash
cd Workshop
pip install -r requirements.txt
```

Nebo instalace jednotlivě:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Počáteční nastavení

### Spuštění služby Foundry Local

**Nutné před spuštěním jakéhokoliv notebooku:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Očekávaný výstup:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Stažení a načtení modelů

Notebooky používají tyto modely jako výchozí:

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

### Ověření nastavení

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sezení 04: Porovnání modelů

### Účel
Porovnat výkon mezi malými jazykovými modely (SLM) a velkými jazykovými modely (LLM).

### Rychlé nastavení

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Spuštění notebooku

1. **Otevřete** `session04_model_compare.ipynb` ve VS Code nebo Jupyteru
2. **Restartujte kernel** (Kernel → Restart Kernel)
3. **Spusťte všechny buňky** v pořadí

### Klíčová konfigurace

**Výchozí modely:**
- **SLM:** `phi-4-mini` (~4GB RAM, rychlejší)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimalizováno pro paměť)

**Proměnné prostředí (volitelné):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Očekávaný výstup

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

### Přizpůsobení

**Použití jiných modelů:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Vlastní prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Kontrolní seznam validace

- [ ] Buňka 12 ukazuje správné modely (phi-4-mini, qwen2.5-3b)
- [ ] Buňka 12 ukazuje správný endpoint (port 59959)
- [ ] Diagnostika buňky 16 úspěšná (✅ Služba běží)
- [ ] Kontrola před spuštěním v buňce 20 úspěšná (oba modely v pořádku)
- [ ] Porovnání v buňce 22 dokončeno s hodnotami latence
- [ ] Validace v buňce 24 ukazuje 🎉 VŠECHNY KONTROLY ÚSPĚŠNÉ!

### Odhad času
- **První spuštění:** 5-10 minut (včetně stahování modelů)
- **Další spuštění:** 1-2 minuty

---

## Sezení 05: Orchestrátor pro více agentů

### Účel
Ukázat spolupráci více agentů pomocí Foundry Local SDK - agenti spolupracují na vytvoření vylepšených výstupů.

### Rychlé nastavení

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Spuštění notebooku

1. **Otevřete** `session05_agents_orchestrator.ipynb`
2. **Restartujte kernel**
3. **Spusťte všechny buňky** v pořadí

### Klíčová konfigurace

**Výchozí nastavení (stejný model pro oba agenty):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Pokročilé nastavení (různé modely):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektura

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

### Očekávaný výstup

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

### Rozšíření

**Přidání dalších agentů:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch testování:**
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
- **První spuštění:** 3-5 minut
- **Další spuštění:** 1-2 minuty na otázku

---

## Sezení 06: Směrování modelů na základě záměru

### Účel
Inteligentně směrovat prompty na specializované modely na základě detekovaného záměru.

### Rychlé nastavení

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Poznámka:** Sezení 06 používá výchozí modely na CPU pro maximální kompatibilitu.

### Spuštění notebooku

1. **Otevřete** `session06_models_router.ipynb`
2. **Restartujte kernel**
3. **Spusťte všechny buňky** v pořadí

### Klíčová konfigurace

**Výchozí katalog (CPU modely):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (GPU modely):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Detekce záměru

Router používá regex vzory k detekci záměru:

| Záměr | Příklady vzorů | Směrováno na |
|-------|----------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Vše ostatní | phi-4-mini-cpu |

### Očekávaný výstup

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

### Přizpůsobení

**Přidání vlastního záměru:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Povolení sledování tokenů:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Přepnutí na GPU modely

Pokud máte 8GB+ VRAM:

1. V **buňce #6** zakomentujte CPU katalog
2. Odkomentujte GPU katalog
3. Načtěte GPU modely:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Restartujte kernel a znovu spusťte notebook

### Odhad času
- **První spuštění:** 5-10 minut (načítání modelů)
- **Další spuštění:** 30-60 sekund na test

---

## Proměnné prostředí

### Globální konfigurace

Nastavte před spuštěním Jupyter/VS Code:

**Windows (Příkazový řádek):**
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

### Konfigurace v notebooku

Nastavte na začátku jakéhokoliv notebooku:

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

## Běžné příkazy

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

### Správa modelů

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

### Testování endpointů

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

### Diagnostické příkazy

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

## Nejlepší postupy

### Před spuštěním jakéhokoliv notebooku

1. **Zkontrolujte, zda služba běží:**
   ```bash
   foundry service status
   ```

2. **Ověřte, zda jsou modely načteny:**
   ```bash
   foundry model ls
   ```

3. **Restartujte kernel notebooku** při opakovaném spuštění

4. **Vymažte všechny výstupy** pro čisté spuštění

### Správa zdrojů

1. **Používejte CPU modely jako výchozí** pro kompatibilitu
2. **Přepněte na GPU modely** pouze pokud máte 8GB+ VRAM
3. **Zavřete ostatní GPU aplikace** před spuštěním
4. **Udržujte službu běžící** mezi sezeními notebooku
5. **Sledujte využití zdrojů** pomocí Správce úloh / nvidia-smi

### Řešení problémů

1. **Vždy nejprve zkontrolujte službu** před laděním kódu
2. **Restartujte kernel** pokud vidíte zastaralou konfiguraci
3. **Znovu spusťte diagnostické buňky** po jakýchkoliv změnách
4. **Ověřte názvy modelů** odpovídají načteným modelům
5. **Ověřte port endpointu** odpovídá stavu služby

---

## Rychlá reference: Alias modelů

### Běžné modely

| Alias | Velikost | Nejlepší pro | RAM/VRAM | Varianty |
|-------|----------|--------------|----------|----------|
| `phi-4-mini` | ~4B | Obecný chat, sumarizace | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generování kódu, refaktoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Obecné úkoly, efektivní | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rychlé, nízké nároky | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasifikace, minimální nároky | 1-2GB | `-cpu`, `-cuda-gpu` |

### Názvy variant

- **Základní název** (např. `phi-4-mini`): Automaticky vybere nejlepší variantu pro vaše hardware
- **`-cpu`**: Optimalizováno pro CPU, funguje všude
- **`-cuda-gpu`**: Optimalizováno pro NVIDIA GPU, vyžaduje 8GB+ VRAM
- **`-npu`**: Optimalizováno pro Qualcomm NPU, vyžaduje NPU ovladače

**Doporučení:** Používejte základní názvy (bez přípony) a nechte Foundry Local automaticky vybrat nejlepší variantu.

---

## Indikátory úspěchu

Jste připraveni, když vidíte:

✅ `foundry service status` ukazuje "running"
✅ `foundry model ls` ukazuje požadované modely
✅ Služba je dostupná na správném endpointu
✅ Kontrola stavu vrací 200 OK
✅ Diagnostické buňky notebooku úspěšné
✅ Žádné chyby připojení ve výstupu

---

## Získání pomoci

### Dokumentace
- **Hlavní repozitář**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Řešení problémů**: Viz `troubleshooting.md` v tomto adresáři

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Poslední aktualizace:** 8. října 2025  
**Verze:** Workshop Notebooks 2.0

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.