# Workshop Jegyzetek - Gyorsindítási Útmutató

## Tartalomjegyzék

- [Előfeltételek](../../../../Workshop/notebooks)
- [Kezdeti Beállítás](../../../../Workshop/notebooks)
- [4. Szekció: Modellösszehasonlítás](../../../../Workshop/notebooks)
- [5. Szekció: Többügynökös Orkesztrátor](../../../../Workshop/notebooks)
- [6. Szekció: Szándék-alapú Modellirányítás](../../../../Workshop/notebooks)
- [Környezeti Változók](../../../../Workshop/notebooks)
- [Gyakori Parancsok](../../../../Workshop/notebooks)

---

## Előfeltételek

### 1. Foundry Local telepítése

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Telepítés ellenőrzése:**
```bash
foundry --version
```

### 2. Python függőségek telepítése

```bash
cd Workshop
pip install -r requirements.txt
```

Vagy telepítse egyenként:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Kezdeti Beállítás

### Foundry Local Szolgáltatás indítása

**Szükséges minden jegyzet futtatása előtt:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Várható kimenet:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Modellek letöltése és betöltése

A jegyzetek alapértelmezés szerint ezeket a modelleket használják:

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

### Beállítás ellenőrzése

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## 4. Szekció: Modellösszehasonlítás

### Cél
Kis Nyelvi Modellek (SLM) és Nagy Nyelvi Modellek (LLM) teljesítményének összehasonlítása.

### Gyors Beállítás

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Jegyzet futtatása

1. **Nyissa meg** a `session04_model_compare.ipynb` fájlt VS Code-ban vagy Jupyterben
2. **Indítsa újra a kernelt** (Kernel → Restart Kernel)
3. **Futtassa az összes cellát** sorrendben

### Fő Konfiguráció

**Alapértelmezett modellek:**
- **SLM:** `phi-4-mini` (~4GB RAM, gyorsabb)
- **LLM:** `qwen2.5-3b` (~3GB RAM, memória-optimalizált)

**Környezeti változók (opcionális):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Várható kimenet

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

### Testreszabás

**Más modellek használata:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Egyedi prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Ellenőrzőlista

- [ ] A 12. cella a megfelelő modelleket mutatja (phi-4-mini, qwen2.5-3b)
- [ ] A 12. cella a megfelelő végpontot mutatja (port 59959)
- [ ] A 16. cella diagnosztikája sikeres (✅ Szolgáltatás fut)
- [ ] A 20. cella előzetes ellenőrzése sikeres (mindkét modell rendben)
- [ ] A 22. cella összehasonlítása befejeződik késleltetési értékekkel
- [ ] A 24. cella validációja mutatja 🎉 MINDEN ELLENŐRZÉS SIKERES!

### Időbecslés
- **Első futtatás:** 5-10 perc (beleértve a modellek letöltését)
- **Következő futtatások:** 1-2 perc

---

## 5. Szekció: Többügynökös Orkesztrátor

### Cél
Többügynökös együttműködés bemutatása a Foundry Local SDK segítségével - az ügynökök együtt dolgoznak a kifinomultabb eredmények érdekében.

### Gyors Beállítás

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Jegyzet futtatása

1. **Nyissa meg** a `session05_agents_orchestrator.ipynb` fájlt
2. **Indítsa újra a kernelt**
3. **Futtassa az összes cellát** sorrendben

### Fő Konfiguráció

**Alapértelmezett beállítás (ugyanaz a modell mindkét ügynöknél):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Haladó beállítás (különböző modellek):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektúra

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

### Várható kimenet

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

### Kiterjesztések

**További ügynökök hozzáadása:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch tesztelés:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Időbecslés
- **Első futtatás:** 3-5 perc
- **Következő futtatások:** 1-2 perc kérdésenként

---

## 6. Szekció: Szándék-alapú Modellirányítás

### Cél
Promptok intelligens irányítása specializált modellekhez a szándék felismerése alapján.

### Gyors Beállítás

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Megjegyzés:** A 6. szekció alapértelmezés szerint CPU modelleket használ a maximális kompatibilitás érdekében.

### Jegyzet futtatása

1. **Nyissa meg** a `session06_models_router.ipynb` fájlt
2. **Indítsa újra a kernelt**
3. **Futtassa az összes cellát** sorrendben

### Fő Konfiguráció

**Alapértelmezett katalógus (CPU modellek):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatíva (GPU modellek):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Szándék Felismerés

Az irányító regex mintákat használ a szándék felismerésére:

| Szándék | Példa minták | Irányított modell |
|---------|--------------|-------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Minden más | phi-4-mini-cpu |

### Várható kimenet

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

### Testreszabás

**Egyedi szándék hozzáadása:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Token követés engedélyezése:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPU modellekre váltás

Ha van 8GB+ VRAM:

1. A **6. cellában** kommentelje ki a CPU katalógust
2. Hagyja jóvá a GPU katalógust
3. Töltse be a GPU modelleket:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Indítsa újra a kernelt és futtassa újra a jegyzetet

### Időbecslés
- **Első futtatás:** 5-10 perc (modellek betöltése)
- **Következő futtatások:** 30-60 másodperc tesztenként

---

## Környezeti Változók

### Globális Konfiguráció

Állítsa be Jupyter/VS Code indítása előtt:

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

### Jegyzeten belüli konfiguráció

Állítsa be bármely jegyzet elején:

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

## Gyakori Parancsok

### Szolgáltatáskezelés

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

### Modellkezelés

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

### Végpontok tesztelése

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

### Diagnosztikai parancsok

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

## Legjobb Gyakorlatok

### Mielőtt bármely jegyzetet elindítana

1. **Ellenőrizze, hogy a szolgáltatás fut-e:**
   ```bash
   foundry service status
   ```

2. **Győződjön meg róla, hogy a modellek betöltve vannak:**
   ```bash
   foundry model ls
   ```

3. **Indítsa újra a jegyzet kernelt**, ha újra futtatja

4. **Törölje az összes kimenetet** a tiszta futtatás érdekében

### Erőforrás-kezelés

1. **Használjon CPU modelleket alapértelmezés szerint** a kompatibilitás érdekében
2. **Váltson GPU modellekre**, ha van 8GB+ VRAM
3. **Zárja be más GPU alkalmazásokat** futtatás előtt
4. **Tartsa a szolgáltatást futva** a jegyzetek között
5. **Figyelje az erőforrás-használatot** a Feladatkezelővel / nvidia-smi-vel

### Hibakeresés

1. **Mindig ellenőrizze először a szolgáltatást**, mielőtt a kódot hibakeresné
2. **Indítsa újra a kernelt**, ha elavult konfigurációt lát
3. **Futtassa újra a diagnosztikai cellákat** bármilyen változtatás után
4. **Ellenőrizze, hogy a modellnevek** megegyeznek a betöltött modellekkel
5. **Győződjön meg róla, hogy a végpont portja** megegyezik a szolgáltatás állapotával

---

## Gyors Referencia: Modell Aliasok

### Gyakori Modellek

| Alias | Méret | Legjobb Felhasználás | RAM/VRAM | Variánsok |
|-------|-------|-----------------------|----------|----------|
| `phi-4-mini` | ~4B | Általános chat, összegzés | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kódgenerálás, refaktorálás | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Általános feladatok, hatékony | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Gyors, alacsony erőforrás | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Osztályozás, minimális erőforrás | 1-2GB | `-cpu`, `-cuda-gpu` |

### Variáns Elnevezés

- **Alapnév** (pl. `phi-4-mini`): Automatikusan kiválasztja a legjobb variánst a hardveréhez
- **`-cpu`**: CPU-optimalizált, mindenhol működik
- **`-cuda-gpu`**: NVIDIA GPU optimalizált, 8GB+ VRAM szükséges
- **`-npu`**: Qualcomm NPU optimalizált, NPU driverek szükségesek

**Ajánlás:** Használja az alapneveket (suffix nélkül), és hagyja, hogy a Foundry Local automatikusan kiválassza a legjobb variánst.

---

## Siker Mutatók

Készen áll, ha:

✅ `foundry service status` "running"-ot mutat  
✅ `foundry model ls` megjeleníti a szükséges modelleket  
✅ Szolgáltatás elérhető a megfelelő végponton  
✅ Egészségügyi ellenőrzés 200 OK-t ad vissza  
✅ Jegyzet diagnosztikai cellái sikeresek  
✅ Nincs kapcsolat hiba a kimenetben  

---

## Segítség Kérése

### Dokumentáció
- **Fő Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referencia**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Hibakeresés**: Lásd `troubleshooting.md` ebben a könyvtárban

### GitHub Hibák
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Utolsó frissítés:** 2025. október 8.  
**Verzió:** Workshop Jegyzetek 2.0

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.