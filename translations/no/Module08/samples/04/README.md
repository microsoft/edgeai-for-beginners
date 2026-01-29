# Eksempel 04: Produksjonsklare chat-applikasjoner med Chainlit

Et omfattende eksempel som viser flere tilnærminger til å bygge produksjonsklare chat-applikasjoner ved bruk av Microsoft Foundry Local, med moderne webgrensesnitt, strømming av svar og avanserte nettleserteknologier.

## Hva er inkludert

- **🚀 Chainlit Chat App** (`app.py`): Produksjonsklar chat-applikasjon med strømming
- **🌐 WebGPU Demo** (`webgpu-demo/`): Nettleserbasert AI-inferens med maskinvareakselerasjon
- **🎨 Open WebUI-integrasjon** (`open-webui-guide.md`): Profesjonelt ChatGPT-lignende grensesnitt
- **📚 Pedagogisk notatbok** (`chainlit_app.ipynb`): Interaktive læringsmaterialer

## Kom i gang

### 1. Chainlit Chat-applikasjon

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Åpnes på: `http://localhost:8080`

### 2. WebGPU Nettleser-demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Åpnes på: `http://localhost:5173`

### 3. Open WebUI-oppsett

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Åpnes på: `http://localhost:3000`

## Arkitekturmønstre

### Lokal vs sky beslutningsmatrise

| Scenario | Anbefaling | Begrunnelse |
|----------|------------|-------------|
| **Personvernfølsomme data** | 🏠 Lokal (Foundry) | Data forlater aldri enheten |
| **Kompleks resonnement** | ☁️ Sky (Azure OpenAI) | Tilgang til større modeller |
| **Sanntidschat** | 🏠 Lokal (Foundry) | Lavere ventetid, raskere svar |
| **Dokumentanalyse** | 🔄 Hybrid | Lokal for utvinning, sky for analyse |
| **Kodegenerering** | 🏠 Lokal (Foundry) | Personvern + spesialiserte modeller |
| **Forskningsoppgaver** | ☁️ Sky (Azure OpenAI) | Bred kunnskapsbase nødvendig |

### Teknologisammenligning

| Teknologi | Bruksområde | Fordeler | Ulemper |
|-----------|-------------|----------|---------|
| **Chainlit** | Python-utviklere, rask prototyping | Enkel oppsett, støtte for strømming | Kun Python |
| **WebGPU** | Maksimalt personvern, offline-scenarier | Nettleserbasert, ingen server nødvendig | Begrenset modellstørrelse |
| **Open WebUI** | Produksjonsdistribusjon, team | Profesjonelt grensesnitt, brukerstyring | Krever Docker |

## Forutsetninger

- **Foundry Local**: Installert og kjører ([Last ned](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ med virtuelt miljø
- **Modell**: Minst én lastet (`foundry model run phi-4-mini`)
- **Nettleser**: Chrome/Edge med WebGPU-støtte for demoer
- **Docker**: For Open WebUI (valgfritt)

## Installasjon og oppsett

### 1. Oppsett av Python-miljø

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Oppsett av Foundry Local

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

## Eksempelapplikasjoner

### Chainlit Chat-applikasjon

**Funksjoner:**
- 🚀 **Sanntidsstrømming**: Tokens vises mens de genereres
- 🛡️ **Robust feilhåndtering**: Grasiøs nedgradering og gjenoppretting
- 🎨 **Moderne grensesnitt**: Profesjonelt chat-grensesnitt rett ut av boksen
- 🔧 **Fleksibel konfigurasjon**: Miljøvariabler og automatisk deteksjon
- 📱 **Responsivt design**: Fungerer på både desktop og mobile enheter

**Kom i gang:**
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

### WebGPU Nettleser-demo

**Funksjoner:**
- 🌐 **Nettleserbasert AI**: Ingen server nødvendig, kjører helt i nettleseren
- ⚡ **WebGPU-akselerasjon**: Maskinvareakselerasjon når tilgjengelig
- 🔒 **Maksimalt personvern**: Ingen data forlater enheten din
- 🎯 **Ingen installasjon**: Fungerer i enhver kompatibel nettleser
- 🔄 **Grasiøs fallback**: Faller tilbake til CPU hvis WebGPU ikke er tilgjengelig

**Kjøring:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI-integrasjon

**Funksjoner:**
- 🎨 **ChatGPT-lignende grensesnitt**: Profesjonelt, kjent UI
- 👥 **Støtte for flere brukere**: Brukerkontoer og samtalehistorikk
- 📁 **Filbehandling**: Last opp og analyser dokumenter
- 🔄 **Modellbytte**: Enkel bytting mellom ulike modeller
- 🐳 **Docker-distribusjon**: Produksjonsklar containerbasert oppsett

**Raskt oppsett:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurasjonsreferanse

### Miljøvariabler

| Variabel | Beskrivelse | Standard | Eksempel |
|----------|-------------|----------|----------|
| `MODEL` | Modellalias som skal brukes | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local-endepunkt | Automatisk oppdaget | `http://localhost:51211` |
| `API_KEY` | API-nøkkel (valgfritt for lokal) | `""` | `your-api-key` |

## Feilsøking

### Vanlige problemer

**Chainlit-applikasjon:**

1. **Tjenesten er ikke tilgjengelig:**
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

**WebGPU-demo:**

1. **WebGPU ikke støttet:**
   - Oppdater til Chrome/Edge 113+
   - Aktiver WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Sjekk GPU-status: `chrome://gpu`
   - Demoen faller automatisk tilbake til CPU

2. **Feil ved modelllasting:**
   - Sørg for internettforbindelse for modellnedlasting
   - Sjekk nettleserkonsollen for CORS-feil
   - Verifiser at du serverer via HTTP (ikke file://)

**Open WebUI:**

1. **Tilkobling nektet:**
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

### Valideringssjekkliste

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

## Avansert bruk

### Ytelsesoptimalisering

**Chainlit:**
- Bruk strømming for bedre opplevd ytelse
- Implementer tilkoblingspooling for høy samtidighet
- Cache modellresponser for gjentatte forespørsler
- Overvåk minnebruk med store samtalehistorikker

**WebGPU:**
- Bruk WebGPU for maksimal personvern og hastighet
- Implementer modellkvantisering for mindre modeller
- Bruk Web Workers for bakgrunnsprosessering
- Cache kompilerte modeller i nettleserlagring

**Open WebUI:**
- Bruk persistente volumer for samtalehistorikk
- Konfigurer ressursgrenser for Docker-container
- Implementer backup-strategier for brukerdata
- Sett opp reverse proxy for SSL-terminering

### Integrasjonsmønstre

**Hybrid Lokal/Sky:**
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

**Multi-modal pipeline:**
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

## Produksjonsdistribusjon

### Sikkerhetsvurderinger

- **API-nøkler**: Bruk miljøvariabler, aldri hardkod
- **Nettverk**: Bruk HTTPS i produksjon, vurder VPN for teamtilgang
- **Tilgangskontroll**: Implementer autentisering for Open WebUI
- **Datapersonvern**: Gjennomgå hva som forblir lokalt vs. går til skyen
- **Oppdateringer**: Hold Foundry Local og containere oppdatert

### Overvåking og vedlikehold

- **Helsetester**: Implementer endepunktovervåking
- **Logging**: Sentraliser logger fra alle komponenter
- **Metrikker**: Spor responstider, feilrater, ressursbruk
- **Backup**: Regelmessig backup av samtaledata og konfigurasjoner

## Referanser og ressurser

### Dokumentasjon
- [Chainlit Dokumentasjon](https://docs.chainlit.io/) - Komplett rammeverksguide
- [Foundry Local Dokumentasjon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Offisiell Microsoft-dokumentasjon
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-integrasjon
- [Open WebUI Dokumentasjon](https://docs.openwebui.com/) - Avansert konfigurasjon

### Eksempelfiler
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produksjonsklar Chainlit-applikasjon
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Pedagogisk notatbok
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Nettleserbasert AI-inferens
- [`open-webui-guide.md`](./open-webui-guide.md) - Komplett Open WebUI-oppsett

### Relaterte eksempler
- [Sesjon 4 Dokumentasjon](../../04.CuttingEdgeModels.md) - Komplett sesjonsguide
- [Foundry Local Eksempler](https://github.com/microsoft/foundry-local/tree/main/samples) - Offisielle eksempler

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.