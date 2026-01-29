# Eksempel 04: Produktionsklare Chat-applikationer med Chainlit

Et omfattende eksempel, der demonstrerer flere tilgange til at bygge produktionsklare chat-applikationer ved hjælp af Microsoft Foundry Local, med moderne webgrænseflader, streaming-svar og avancerede browserteknologier.

## Hvad er inkluderet

- **🚀 Chainlit Chat App** (`app.py`): Produktionsklar chat-applikation med streaming
- **🌐 WebGPU Demo** (`webgpu-demo/`): Browserbaseret AI-inferens med hardwareacceleration
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): Professionel ChatGPT-lignende grænseflade
- **📚 Uddannelsesnotebook** (`chainlit_app.ipynb`): Interaktive læringsmaterialer

## Hurtig Start

### 1. Chainlit Chat-applikation

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Åbnes på: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Åbnes på: `http://localhost:5173`

### 3. Open WebUI Opsætning

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Åbnes på: `http://localhost:3000`

## Arkitektur Mønstre

### Lokal vs Cloud Beslutningsmatrix

| Scenarie | Anbefaling | Årsag |
|----------|------------|-------|
| **Privatfølsomme data** | 🏠 Lokal (Foundry) | Data forlader aldrig enheden |
| **Kompleks ræsonnement** | ☁️ Cloud (Azure OpenAI) | Adgang til større modeller |
| **Realtidschat** | 🏠 Lokal (Foundry) | Lavere latenstid, hurtigere svar |
| **Dokumentanalyse** | 🔄 Hybrid | Lokal til udtrækning, cloud til analyse |
| **Kodegenerering** | 🏠 Lokal (Foundry) | Privatliv + specialiserede modeller |
| **Forskningsopgaver** | ☁️ Cloud (Azure OpenAI) | Bredt vidensgrundlag nødvendigt |

### Teknologisammenligning

| Teknologi | Anvendelse | Fordele | Ulemper |
|-----------|------------|---------|---------|
| **Chainlit** | Python-udviklere, hurtig prototyping | Nem opsætning, streaming-understøttelse | Kun Python |
| **WebGPU** | Maksimal privatliv, offline scenarier | Browser-native, ingen server nødvendig | Begrænset modelstørrelse |
| **Open WebUI** | Produktionsudrulning, teams | Professionel UI, brugeradministration | Kræver Docker |

## Forudsætninger

- **Foundry Local**: Installeret og kører ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ med virtuel miljø
- **Model**: Mindst én indlæst (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge med WebGPU-understøttelse til demoer
- **Docker**: Til Open WebUI (valgfrit)

## Installation & Opsætning

### 1. Opsætning af Python-miljø

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Opsætning af Foundry Local

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

## Eksempelapplikationer

### Chainlit Chat-applikation

**Funktioner:**
- 🚀 **Realtidsstreaming**: Tokens vises, mens de genereres
- 🛡️ **Robust fejlhåndtering**: Elegant nedgradering og genopretning
- 🎨 **Moderne UI**: Professionel chat-grænseflade klar til brug
- 🔧 **Fleksibel konfiguration**: Miljøvariabler og automatisk detektion
- 📱 **Responsivt design**: Fungerer på både desktop og mobile enheder

**Hurtig Start:**
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

### WebGPU Browser Demo

**Funktioner:**
- 🌐 **Browser-native AI**: Ingen server nødvendig, kører helt i browseren
- ⚡ **WebGPU Acceleration**: Hardwareacceleration, når tilgængelig
- 🔒 **Maksimal privatliv**: Ingen data forlader din enhed
- 🎯 **Ingen installation**: Fungerer i enhver kompatibel browser
- 🔄 **Elegant fallback**: Fald tilbage til CPU, hvis WebGPU ikke er tilgængelig

**Kørsel:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**Funktioner:**
- 🎨 **ChatGPT-lignende grænseflade**: Professionel, velkendt UI
- 👥 **Multi-bruger understøttelse**: Brugerkonti og samtalehistorik
- 📁 **Filbehandling**: Upload og analyser dokumenter
- 🔄 **Modelskift**: Nem skift mellem forskellige modeller
- 🐳 **Docker-udrulning**: Produktionsklar containeropsætning

**Hurtig Opsætning:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurationsreference

### Miljøvariabler

| Variabel | Beskrivelse | Standard | Eksempel |
|----------|-------------|----------|----------|
| `MODEL` | Modelalias, der skal bruges | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local endpoint | Automatisk detekteret | `http://localhost:51211` |
| `API_KEY` | API-nøgle (valgfri for lokal) | `""` | `your-api-key` |

## Fejlfinding

### Almindelige Problemer

**Chainlit-applikation:**

1. **Tjeneste ikke tilgængelig:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Portkonflikter:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problemer med Python-miljø:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU ikke understøttet:**
   - Opdater til Chrome/Edge 113+
   - Aktiver WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Tjek GPU-status: `chrome://gpu`
   - Demo falder automatisk tilbage til CPU

2. **Fejl ved modellæsning:**
   - Sørg for internetforbindelse til modeldownload
   - Tjek browserkonsollen for CORS-fejl
   - Bekræft, at du serverer via HTTP (ikke file://)

**Open WebUI:**

1. **Forbindelse nægtet:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeller vises ikke:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Valideringscheckliste

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

## Avanceret Brug

### Performanceoptimering

**Chainlit:**
- Brug streaming for bedre opfattet performance
- Implementer forbindelsespooling for høj samtidighed
- Cache modelrespons for gentagne forespørgsler
- Overvåg hukommelsesforbrug med store samtalehistorikker

**WebGPU:**
- Brug WebGPU for maksimal privatliv og hastighed
- Implementer modelkvantisering for mindre modeller
- Brug Web Workers til baggrundsbehandling
- Cache kompilerede modeller i browserlagring

**Open WebUI:**
- Brug vedvarende volumener til samtalehistorik
- Konfigurer ressourcegrænser for Docker-container
- Implementer backupstrategier for brugerdata
- Opsæt reverse proxy til SSL-terminering

### Integrationsmønstre

**Hybrid Lokal/Cloud:**
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

**Multi-modal Pipeline:**
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

## Produktionsudrulning

### Sikkerhedsovervejelser

- **API-nøgler**: Brug miljøvariabler, aldrig hardcode
- **Netværk**: Brug HTTPS i produktion, overvej VPN til teamadgang
- **Adgangskontrol**: Implementer autentifikation for Open WebUI
- **Dataprivacy**: Auditér hvilke data der forbliver lokale vs. sendes til cloud
- **Opdateringer**: Hold Foundry Local og containere opdateret

### Overvågning og Vedligeholdelse

- **Sundhedstjek**: Implementer endpoint-overvågning
- **Logning**: Centraliser logs fra alle komponenter
- **Metrikker**: Spor svartider, fejlrater, ressourceforbrug
- **Backup**: Regelmæssig backup af samtaledata og konfigurationer

## Referencer og Ressourcer

### Dokumentation
- [Chainlit Dokumentation](https://docs.chainlit.io/) - Komplet framework-guide
- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Officielle Microsoft-dokumenter
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-integration
- [Open WebUI Dokumentation](https://docs.openwebui.com/) - Avanceret konfiguration

### Eksempelfiler
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produktionsklar Chainlit-applikation
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Uddannelsesnotebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Browserbaseret AI-inferens
- [`open-webui-guide.md`](./open-webui-guide.md) - Komplet Open WebUI opsætning

### Relaterede Eksempler
- [Session 4 Dokumentation](../../04.CuttingEdgeModels.md) - Komplet sessionsguide
- [Foundry Local Eksempler](https://github.com/microsoft/foundry-local/tree/main/samples) - Officielle eksempler

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.