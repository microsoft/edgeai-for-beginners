# Workshop Jegyzetek - Hibaelhárítási Útmutató

## Tartalomjegyzék

- [Gyakori problémák és megoldások](../../../../Workshop/notebooks)
- [04. szekció specifikus problémák](../../../../Workshop/notebooks)
- [05. szekció specifikus problémák](../../../../Workshop/notebooks)
- [06. szekció specifikus problémák](../../../../Workshop/notebooks)
- [Hardver-specifikus problémák](../../../../Workshop/notebooks)
- [Diagnosztikai parancsok](../../../../Workshop/notebooks)
- [Segítség kérése](../../../../Workshop/notebooks)

---

## Gyakori problémák és megoldások

### 🔴 CUDA Out of Memory

**Hibaüzenet:**
```
CUDA failure 2: out of memory
```
  
**Ok:** A GPU nem rendelkezik elegendő VRAM-mal a modell betöltéséhez.

**Megoldások:**

#### Opció 1: Használj CPU változatokat (Ajánlott)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Opció 2: Használj kisebb modelleket GPU-n
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Opció 3: Tisztítsd meg a GPU memóriát
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Opció 4: Növeld a GPU memóriát (ha lehetséges)
- Zárd be a böngészőlapokat, videószerkesztőket vagy más GPU-t használó alkalmazásokat
- Csökkentsd a Windows vizuális effektusait
- Használj dedikált GPU-t, ha van integrált + dedikált GPU-d

---

### 🔴 APIConnectionError: Kapcsolódási hiba

**Hibaüzenet:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Ok:** A Foundry Local szolgáltatás nem fut vagy nem elérhető.

**Megoldások:**

#### 1. lépés: Ellenőrizd a szolgáltatás állapotát
```bash
foundry service status
```
  
#### 2. lépés: Indítsd el a szolgáltatást, ha leállt
```bash
foundry service start
```
  
#### 3. lépés: Ellenőrizd az endpointot
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### 4. lépés: Töltsd be a szükséges modelleket
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### 5. lépés: Indítsd újra a notebook kernelét  
A szolgáltatás elindítása és a modellek betöltése után indítsd újra a notebook kernelét, és futtasd újra az összes cellát.

---

### 🔴 Modell nem található a katalógusban

**Hibaüzenet:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Ok:** A modell nincs letöltve vagy betöltve a Foundry Local-ba.

**Megoldások:**

#### Opció 1: Töltsd le és töltsd be a modelleket
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
  
#### Opció 2: Használj automatikus kiválasztási módot  
Frissítsd a CATALOG-ot, hogy az alapmodell neveket használja (a `-cpu` utótag nélkül):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
A Foundry Local SDK automatikusan kiválasztja a legjobb változatot (CPU, GPU vagy NPU) a hardveredhez.

---

### 🔴 HttpResponseError: 500 - Modell betöltése sikertelen

**Hibaüzenet:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Ok:** A modell fájl sérült vagy nem kompatibilis a hardverrel.

**Megoldások:**

#### Töltsd le újra a modellt
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Használj másik változatot
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: Modul nem található

**Hibaüzenet:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Ok:** A foundry-local-sdk csomag nincs telepítve.

**Megoldások:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Lassú első kérés

**Tünet:** Az első válasz több mint 30 másodpercet vesz igénybe, a következő kérések gyorsak.

**Ok:** Ez normális viselkedés - a szolgáltatás az első kéréskor tölti be a modellt a memóriába.

**Megoldások:**

#### Töltsd be előre a modelleket
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Hagyd futni a szolgáltatást
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## 04. szekció specifikus problémák

### Rossz port konfiguráció

**Probléma:** A notebook rossz porthoz csatlakozik (55769 vs 59959 vs 57127)

**Megoldás:**

1. Ellenőrizd, hogy melyik portot használja a Foundry Local:
```bash
foundry service status
# Note the port number displayed
```
  
2. Frissítsd a 10. cellát a notebookban:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Indítsd újra a kernelt, és futtasd újra a 6., 8., 10., 12., 16., 20., 22. cellákat

---

### Rossz modell kiválasztás

**Probléma:** A notebook a gpt-oss-20b vagy qwen2.5-7b modellt mutatja a qwen2.5-3b helyett

**Megoldás:**

1. Indítsd újra a notebook kernelét (törli a régi változó állapotot)
2. Futtasd újra a 10. cellát (Állítsd be a modell aliasokat)
3. Futtasd újra a 12. cellát (Konfiguráció megjelenítése)
4. **Ellenőrizd:** A 12. cellának ezt kell mutatnia: `LLM Model: qwen2.5-3b`

---

### Diagnosztikai cella hibás

**Probléma:** A 16. cella "❌ Foundry Local service not found!" üzenetet mutat

**Megoldás:**

1. Ellenőrizd, hogy a szolgáltatás fut-e:
```bash
foundry service status
```
  
2. Teszteld az endpointot manuálisan:
```bash
curl http://localhost:59959/v1/models
```
  
3. Ha a curl működik, de a notebook nem:
   - Indítsd újra a notebook kernelét
   - Futtasd újra a cellákat sorrendben: 6, 8, 10, 12, 14, 16

4. Ha a curl nem működik:
   - Indítsd el a szolgáltatást: `foundry service start`
   - Töltsd be a modelleket: `foundry model run phi-4-mini` és `foundry model run qwen2.5-3b`

---

### Előzetes ellenőrzés sikertelen

**Probléma:** A 20. cella kapcsolódási hibákat mutat, annak ellenére, hogy a diagnosztika sikeres volt

**Megoldás:**

1. Ellenőrizd, hogy a modellek betöltve vannak-e:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Ha hiányoznak a modellek:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Futtasd újra a 20. cellát, miután a modellek betöltve vannak

---

### Összehasonlítás sikertelen None értékekkel

**Probléma:** A 22. cella lefut, de a késleltetést None értékként mutatja

**Megoldás:**

1. Ellenőrizd, hogy az előzetes ellenőrzés sikeres volt-e (20. cella)
2. Futtasd újra a 22. cellát - a modelleknek fel kell melegedniük az első kérésnél
3. Ellenőrizd, hogy mindkét modell betöltve van-e: `foundry model ls`

---

## 05. szekció specifikus problémák

### Ügynök rossz modellt használ

**Probléma:** Az ügynök nem a várt modellt használja

**Megoldás:**

Ellenőrizd a konfigurációt:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Indítsd újra a kernelt, ha a modellek helytelenek.

---

### Memória kontextus túlcsordulás

**Probléma:** Az ügynök válaszai idővel romlanak

**Megoldás:** Már automatikusan kezelve - az ügynökök csak az utolsó 6 üzenetet tartják meg a memóriában.

---

## 06. szekció specifikus problémák

### CPU vs GPU modell zavar

**Probléma:** CUDA hibák a default konfiguráció használatakor

**Megoldás:** Az alapértelmezett konfiguráció most CPU modelleket használ. Ha CUDA hibákat látsz:

1. Ellenőrizd, hogy az alapértelmezett CPU katalógust használod-e:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Indítsd újra a kernelt, és futtasd újra az összes cellát

---

### Szándékfelismerés nem működik

**Probléma:** A promptok rossz modellekhez kerülnek

**Megoldás:**

Teszteld a szándékfelismerést:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Frissítsd a RULES-t, ha a minták módosításra szorulnak.

---

## Hardver-specifikus problémák

### NVIDIA GPU

**Ellenőrizd a GPU állapotát:**
```bash
nvidia-smi
```
  
**Gyakori problémák:**
- **Elavult driver:** Frissítsd az NVIDIA drivereket
- **CUDA verzió eltérés:** Telepítsd újra a Foundry Local-t
- **GPU memória töredezett:** Indítsd újra a rendszert

### Qualcomm NPU

**Ellenőrizd az NPU állapotát:**
```bash
foundry device info
```
  
**Gyakori problémák:**
- **NPU driverek nincsenek telepítve:** Telepítsd a Qualcomm NPU drivereket
- **NPU változat nem elérhető:** Használj CPU változatot
- **Windows verzió túl régi:** Frissítsd a legújabb Windows 11-re

### Csak CPU-t használó rendszerek

**Ajánlott modellek:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Teljesítmény tippek:**
- Használj kisebb modelleket
- Csökkentsd a max_tokens értéket
- Légy türelmes az első kérésnél

---

## Diagnosztikai parancsok

### Ellenőrizd mindent
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
  
### Pythonban
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

## Segítség kérése

### 1. Ellenőrizd a naplókat
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub problémák
- Keresd meg a meglévő problémákat: https://github.com/microsoft/Foundry-Local/issues
- Hozz létre új problémát az alábbiakkal:
  - Hibaüzenet (teljes szöveg)
  - `foundry service status` kimenete
  - `foundry --version` kimenete
  - GPU/NPU információ (nvidia-smi, stb.)
  - Lépések a reprodukáláshoz

### 3. Dokumentáció
- **Fő repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI referencia**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Hibaelhárítás**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Gyors javítások ellenőrzőlistája

Ha problémák merülnek fel, próbáld ki ezeket sorrendben:

- [ ] Ellenőrizd, hogy a szolgáltatás fut-e: `foundry service status`
- [ ] Indítsd újra a szolgáltatást: `foundry service stop && foundry service start`
- [ ] Ellenőrizd, hogy a modell létezik-e: `foundry model ls | grep phi-4-mini`
- [ ] Töltsd be a szükséges modelleket: `foundry model run phi-4-mini`
- [ ] Ellenőrizd a GPU memóriát: `nvidia-smi` (ha NVIDIA)
- [ ] Próbáld ki a CPU változatot: Használj `phi-4-mini-cpu`-t a `phi-4-mini` helyett
- [ ] Indítsd újra a notebook kernelét
- [ ] Tisztítsd meg a notebook kimeneteit, és futtasd újra az összes cellát
- [ ] Telepítsd újra az SDK-t: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Indítsd újra a rendszert (végső megoldásként)

---

## Megelőzési tippek

### Legjobb gyakorlatok

1. **Mindig ellenőrizd először a szolgáltatást:**
   ```bash
   foundry service status
   ```
  
2. **Használj alapértelmezés szerint CPU változatokat:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Töltsd be a modelleket a notebookok futtatása előtt:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Hagyd futni a szolgáltatást:**
   - Ne állítsd le/indítsd újra a szolgáltatást feleslegesen
   - Hagyd, hogy a háttérben fusson a szekciók között

5. **Figyeld az erőforrásokat:**
   - Ellenőrizd a GPU memóriát futtatás előtt
   - Zárd be a felesleges GPU alkalmazásokat
   - Használj Feladatkezelőt / nvidia-smi-t

6. **Frissíts rendszeresen:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Utolsó frissítés:** 2025. október 8.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.