# Minta 04: Chatalkalmazások gyártási környezetben Chainlit segítségével

Egy átfogó példa, amely bemutatja a gyártásra kész chatalkalmazások különböző megközelítéseit a Microsoft Foundry Local használatával, modern webes felületekkel, streaming válaszokkal és legújabb böngészőtechnológiákkal.

## Mi található benne?

- **🚀 Chainlit Chatalkalmazás** (`app.py`): Gyártásra kész chatalkalmazás streaming funkcióval
- **🌐 WebGPU Demó** (`webgpu-demo/`): Böngészőalapú AI következtetés hardvergyorsítással
- **🎨 Open WebUI Integráció** (`open-webui-guide.md`): Professzionális ChatGPT-szerű felület
- **📚 Oktatási Jegyzetfüzet** (`chainlit_app.ipynb`): Interaktív tananyagok

## Gyors kezdés

### 1. Chainlit Chatalkalmazás

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Megnyílik: `http://localhost:8080`

### 2. WebGPU Böngésző Demó

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Megnyílik: `http://localhost:5173`

### 3. Open WebUI Beállítás

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Megnyílik: `http://localhost:3000`

## Architektúra minták

### Lokális vs Felhő döntési mátrix

| Forgatókönyv | Ajánlás | Indok |
|--------------|---------|-------|
| **Adatvédelem érzékeny adatok** | 🏠 Lokális (Foundry) | Az adatok nem hagyják el az eszközt |
| **Komplex következtetés** | ☁️ Felhő (Azure OpenAI) | Nagyobb modellek elérése |
| **Valós idejű chat** | 🏠 Lokális (Foundry) | Alacsonyabb késleltetés, gyorsabb válaszok |
| **Dokumentumelemzés** | 🔄 Hibrid | Lokális az adatkinyeréshez, felhő az elemzéshez |
| **Kódgenerálás** | 🏠 Lokális (Foundry) | Adatvédelem + speciális modellek |
| **Kutatási feladatok** | ☁️ Felhő (Azure OpenAI) | Széleskörű tudásbázis szükséges |

### Technológiai összehasonlítás

| Technológia | Felhasználási terület | Előnyök | Hátrányok |
|-------------|-----------------------|---------|-----------|
| **Chainlit** | Python fejlesztők, gyors prototípus készítés | Könnyű beállítás, streaming támogatás | Csak Python |
| **WebGPU** | Maximális adatvédelem, offline forgatókönyvek | Böngésző-alapú, nincs szükség szerverre | Korlátozott modellméret |
| **Open WebUI** | Gyártási környezet, csapatok | Professzionális UI, felhasználókezelés | Docker szükséges |

## Előfeltételek

- **Foundry Local**: Telepítve és futtatva ([Letöltés](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ virtuális környezettel
- **Modell**: Legalább egy betöltve (`foundry model run phi-4-mini`)
- **Böngésző**: Chrome/Edge WebGPU támogatással a demókhoz
- **Docker**: Open WebUI-hoz (opcionális)

## Telepítés és beállítás

### 1. Python környezet beállítása

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local beállítása

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Mintaalkalmazások

### Chainlit Chatalkalmazás

**Funkciók:**
- 🚀 **Valós idejű streaming**: A tokenek generálás közben jelennek meg
- 🛡️ **Erős hibaelhárítás**: Zökkenőmentes degradáció és helyreállítás
- 🎨 **Modern UI**: Professzionális chatfelület alapból
- 🔧 **Rugalmas konfiguráció**: Környezeti változók és automatikus felismerés
- 📱 **Reszponzív dizájn**: Működik asztali és mobil eszközökön

**Gyors kezdés:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU Böngésző Demó

**Funkciók:**
- 🌐 **Böngésző-alapú AI**: Nincs szükség szerverre, teljesen böngészőben fut
- ⚡ **WebGPU gyorsítás**: Hardvergyorsítás, ha elérhető
- 🔒 **Maximális adatvédelem**: Az adatok soha nem hagyják el az eszközt
- 🎯 **Nulla telepítés**: Működik bármely kompatibilis böngészőben
- 🔄 **Zökkenőmentes visszaállás**: CPU-ra vált, ha WebGPU nem elérhető

**Futtatás:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integráció

**Funkciók:**
- 🎨 **ChatGPT-szerű felület**: Professzionális, ismerős UI
- 👥 **Többfelhasználós támogatás**: Felhasználói fiókok és beszélgetési előzmények
- 📁 **Fájlkezelés**: Dokumentumok feltöltése és elemzése
- 🔄 **Modellváltás**: Könnyű váltás különböző modellek között
- 🐳 **Docker telepítés**: Gyártásra kész konténeres beállítás

**Gyors beállítás:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurációs referencia

### Környezeti változók

| Változó | Leírás | Alapértelmezett | Példa |
|---------|--------|-----------------|-------|
| `MODEL` | Használandó modell alias | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local végpont | Automatikusan felismerve | `http://localhost:51211` |
| `API_KEY` | API kulcs (opcionális lokális használathoz) | `""` | `your-api-key` |

## Hibakeresés

### Gyakori problémák

**Chainlit alkalmazás:**

1. **Szolgáltatás nem elérhető:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Portütközések:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python környezeti problémák:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demó:**

1. **WebGPU nem támogatott:**
   - Frissíts Chrome/Edge 113+ verzióra
   - Engedélyezd a WebGPU-t: `chrome://flags/#enable-unsafe-webgpu`
   - Ellenőrizd a GPU állapotát: `chrome://gpu`
   - A demó automatikusan CPU-ra vált

2. **Modell betöltési hibák:**
   - Biztosíts internetkapcsolatot a modell letöltéséhez
   - Ellenőrizd a böngésző konzolt CORS hibákért
   - Győződj meg róla, hogy HTTP-n keresztül szolgáltatsz (nem file://)

**Open WebUI:**

1. **Kapcsolat megtagadva:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modellek nem jelennek meg:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Érvényesítési ellenőrzőlista

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Haladó használat

### Teljesítményoptimalizálás

**Chainlit:**
- Használj streaminget a jobb érzékelt teljesítmény érdekében
- Implementálj kapcsolat poolingot magas párhuzamossághoz
- Cache-eld a modell válaszait ismételt lekérdezésekhez
- Figyeld a memóriahasználatot nagy beszélgetési előzmények esetén

**WebGPU:**
- Használj WebGPU-t a maximális adatvédelem és sebesség érdekében
- Implementálj modell kvantálást kisebb modellekhez
- Használj Web Worker-eket háttérfeldolgozáshoz
- Cache-eld a lefordított modelleket a böngésző tárolójában

**Open WebUI:**
- Használj tartós köteteket a beszélgetési előzményekhez
- Konfiguráld az erőforráskorlátokat a Docker konténerhez
- Implementálj biztonsági mentési stratégiákat a felhasználói adatokhoz
- Állíts be fordított proxy-t SSL termináláshoz

### Integrációs minták

**Hibrid Lokális/Felhő:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Multi-Modális Pipeline:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Gyártási telepítés

### Biztonsági szempontok

- **API kulcsok**: Használj környezeti változókat, soha ne kódold be
- **Hálózat**: Használj HTTPS-t gyártásban, fontold meg VPN-t csapat hozzáféréshez
- **Hozzáférés-vezérlés**: Implementálj hitelesítést az Open WebUI-hoz
- **Adatvédelem**: Ellenőrizd, hogy mely adatok maradnak lokálisan és melyek kerülnek a felhőbe
- **Frissítések**: Tartsd naprakészen a Foundry Local-t és a konténereket

### Felügyelet és karbantartás

- **Egészségellenőrzések**: Implementálj végpont monitorozást
- **Naplózás**: Centralizáld az összes komponens naplóit
- **Metrikák**: Kövesd a válaszidőket, hibaarányokat, erőforrás-használatot
- **Biztonsági mentés**: Rendszeres mentés a beszélgetési adatok és konfigurációk számára

## Referenciák és források

### Dokumentáció
- [Chainlit Dokumentáció](https://docs.chainlit.io/) - Teljes keretrendszer útmutató
- [Foundry Local Dokumentáció](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Hivatalos Microsoft dokumentáció
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integráció
- [Open WebUI Dokumentáció](https://docs.openwebui.com/) - Haladó konfiguráció

### Mintafájlok
- [`app.py`](../../../../../Module08/samples/04/app.py) - Gyártásra kész Chainlit alkalmazás
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Oktatási jegyzetfüzet
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Böngészőalapú AI következtetés
- [`open-webui-guide.md`](./open-webui-guide.md) - Teljes Open WebUI beállítás

### Kapcsolódó minták
- [4. szekció dokumentációja](../../04.CuttingEdgeModels.md) - Teljes szekció útmutató
- [Foundry Local minták](https://github.com/microsoft/foundry-local/tree/main/samples) - Hivatalos minták

---

**Felelősségi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.