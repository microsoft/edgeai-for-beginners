# Voorbeeld 04: Productie Chattoepassingen met Chainlit

Een uitgebreide demonstratie van verschillende benaderingen om productieklare chattoepassingen te bouwen met Microsoft Foundry Local, inclusief moderne webinterfaces, streamingreacties en geavanceerde browsertechnologieën.

## Wat is inbegrepen

- **🚀 Chainlit Chat App** (`app.py`): Productieklare chattoepassing met streaming
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI-inferentie in de browser met hardwareversnelling
- **🎨 Open WebUI Integratie** (`open-webui-guide.md`): Professionele ChatGPT-achtige interface
- **📚 Educatief Notebook** (`chainlit_app.ipynb`): Interactieve leermaterialen

## Snelle Start

### 1. Chainlit Chattoepassing

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Open op: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Open op: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Open op: `http://localhost:3000`

## Architectuurpatronen

### Matrix voor lokale vs. cloudbeslissingen

| Scenario | Aanbeveling | Reden |
|----------|-------------|-------|
| **Privacygevoelige gegevens** | 🏠 Lokaal (Foundry) | Gegevens blijven op het apparaat |
| **Complexe redenering** | ☁️ Cloud (Azure OpenAI) | Toegang tot grotere modellen |
| **Realtime chat** | 🏠 Lokaal (Foundry) | Lagere latentie, snellere reacties |
| **Documentanalyse** | 🔄 Hybride | Lokaal voor extractie, cloud voor analyse |
| **Codegeneratie** | 🏠 Lokaal (Foundry) | Privacy + gespecialiseerde modellen |
| **Onderzoekstaken** | ☁️ Cloud (Azure OpenAI) | Brede kennisbasis nodig |

### Technologievergelijking

| Technologie | Gebruiksscenario | Voordelen | Nadelen |
|-------------|------------------|-----------|---------|
| **Chainlit** | Python-ontwikkelaars, snelle prototyping | Eenvoudige installatie, streamingondersteuning | Alleen Python |
| **WebGPU** | Maximale privacy, offline scenario's | Browser-native, geen server nodig | Beperkte modelgrootte |
| **Open WebUI** | Productie-implementatie, teams | Professionele UI, gebruikersbeheer | Vereist Docker |

## Vereisten

- **Foundry Local**: Geïnstalleerd en actief ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ met virtuele omgeving
- **Model**: Minimaal één geladen (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge met WebGPU-ondersteuning voor demo's
- **Docker**: Voor Open WebUI (optioneel)

## Installatie & Setup

### 1. Python-omgeving instellen

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local instellen

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

## Voorbeeldtoepassingen

### Chainlit Chattoepassing

**Kenmerken:**
- 🚀 **Realtime Streaming**: Tokens verschijnen terwijl ze worden gegenereerd
- 🛡️ **Robuuste Foutafhandeling**: Soepele degradatie en herstel
- 🎨 **Moderne UI**: Professionele chatinterface direct beschikbaar
- 🔧 **Flexibele Configuratie**: Omgevingsvariabelen en automatische detectie
- 📱 **Responsief Ontwerp**: Werkt op desktop en mobiele apparaten

**Snelle Start:**
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

**Kenmerken:**
- 🌐 **Browser-native AI**: Geen server nodig, draait volledig in de browser
- ⚡ **WebGPU Versnelling**: Hardwareversnelling indien beschikbaar
- 🔒 **Maximale Privacy**: Gegevens verlaten nooit je apparaat
- 🎯 **Geen Installatie**: Werkt in elke compatibele browser
- 🔄 **Soepele Terugvaloptie**: Valt terug op CPU als WebGPU niet beschikbaar is

**Uitvoeren:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integratie

**Kenmerken:**
- 🎨 **ChatGPT-achtige Interface**: Professionele, vertrouwde UI
- 👥 **Multi-gebruikersondersteuning**: Gebruikersaccounts en gespreksgeschiedenis
- 📁 **Bestandsverwerking**: Uploaden en analyseren van documenten
- 🔄 **Modelwisseling**: Eenvoudig schakelen tussen verschillende modellen
- 🐳 **Docker Implementatie**: Productieklaar containerized setup

**Snelle Setup:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Configuratiereferentie

### Omgevingsvariabelen

| Variabele | Beschrijving | Standaard | Voorbeeld |
|-----------|--------------|-----------|-----------|
| `MODEL` | Modelalias om te gebruiken | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local eindpunt | Automatisch gedetecteerd | `http://localhost:51211` |
| `API_KEY` | API-sleutel (optioneel voor lokaal) | `""` | `your-api-key` |

## Probleemoplossing

### Veelvoorkomende problemen

**Chainlit Toepassing:**

1. **Service niet beschikbaar:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Poortconflicten:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python-omgeving problemen:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU niet ondersteund:**
   - Update naar Chrome/Edge 113+
   - Schakel WebGPU in: `chrome://flags/#enable-unsafe-webgpu`
   - Controleer GPU-status: `chrome://gpu`
   - Demo valt automatisch terug op CPU

2. **Model laadfouten:**
   - Zorg voor internetverbinding voor modeldownload
   - Controleer browserconsole op CORS-fouten
   - Verifieer dat je via HTTP serveert (niet file://)

**Open WebUI:**

1. **Verbinding geweigerd:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modellen verschijnen niet:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Validatiechecklist

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

## Geavanceerd Gebruik

### Prestatieoptimalisatie

**Chainlit:**
- Gebruik streaming voor betere waargenomen prestaties
- Implementeer verbindingpooling voor hoge gelijktijdigheid
- Cache modelreacties voor herhaalde vragen
- Monitor geheugengebruik bij grote gespreksgeschiedenissen

**WebGPU:**
- Gebruik WebGPU voor maximale privacy en snelheid
- Implementeer modelkwantisering voor kleinere modellen
- Gebruik Web Workers voor achtergrondverwerking
- Cache gecompileerde modellen in browseropslag

**Open WebUI:**
- Gebruik persistente volumes voor gespreksgeschiedenis
- Configureer resourcebeperkingen voor Docker-container
- Implementeer back-upstrategieën voor gebruikersgegevens
- Stel een reverse proxy in voor SSL-terminatie

### Integratiepatronen

**Hybride Lokaal/Cloud:**
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

**Multi-Modale Pijplijn:**
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

## Productie-implementatie

### Veiligheidsoverwegingen

- **API-sleutels**: Gebruik omgevingsvariabelen, nooit hardcoderen
- **Netwerk**: Gebruik HTTPS in productie, overweeg VPN voor teamtoegang
- **Toegangscontrole**: Implementeer authenticatie voor Open WebUI
- **Gegevensprivacy**: Controleer welke gegevens lokaal blijven vs. naar de cloud gaan
- **Updates**: Houd Foundry Local en containers up-to-date

### Monitoring en Onderhoud

- **Gezondheidscontroles**: Implementeer eindpuntmonitoring
- **Logging**: Centraliseer logs van alle componenten
- **Statistieken**: Volg responstijden, foutpercentages, resourcegebruik
- **Back-up**: Regelmatige back-up van gespreksgegevens en configuraties

## Referenties en Bronnen

### Documentatie
- [Chainlit Documentatie](https://docs.chainlit.io/) - Complete frameworkgids
- [Foundry Local Documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Officiële Microsoft-documentatie
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-integratie
- [Open WebUI Documentatie](https://docs.openwebui.com/) - Geavanceerde configuratie

### Voorbeeldbestanden
- [`app.py`](../../../../../Module08/samples/04/app.py) - Productie Chainlit toepassing
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Educatief notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI-inferentie in de browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Complete Open WebUI setup

### Gerelateerde Voorbeelden
- [Sessie 4 Documentatie](../../04.CuttingEdgeModels.md) - Complete sessiegids
- [Foundry Local Voorbeelden](https://github.com/microsoft/foundry-local/tree/main/samples) - Officiële voorbeelden

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.