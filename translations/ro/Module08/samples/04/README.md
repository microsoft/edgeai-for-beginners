# Exemplu 04: Aplicații de Chat pentru Producție cu Chainlit

Un exemplu cuprinzător care demonstrează mai multe abordări pentru construirea aplicațiilor de chat pregătite pentru producție folosind Microsoft Foundry Local, incluzând interfețe web moderne, răspunsuri în flux și tehnologii avansate pentru browser.

## Ce este inclus

- **🚀 Aplicație de Chat Chainlit** (`app.py`): Aplicație de chat pregătită pentru producție cu streaming
- **🌐 Demo WebGPU** (`webgpu-demo/`): Inferență AI bazată pe browser cu accelerare hardware
- **🎨 Integrare Open WebUI** (`open-webui-guide.md`): Interfață profesională asemănătoare ChatGPT
- **📚 Notebook Educațional** (`chainlit_app.ipynb`): Materiale interactive de învățare

## Start Rapid

### 1. Aplicația de Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Se deschide la: `http://localhost:8080`

### 2. Demo WebGPU în Browser

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Se deschide la: `http://localhost:5173`

### 3. Configurare Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Se deschide la: `http://localhost:3000`

## Modele de Arhitectură

### Matrice de Decizie Local vs Cloud

| Scenariu | Recomandare | Motiv |
|----------|-------------|-------|
| **Date Sensibile** | 🏠 Local (Foundry) | Datele nu părăsesc dispozitivul |
| **Raționament Complex** | ☁️ Cloud (Azure OpenAI) | Acces la modele mai mari |
| **Chat în Timp Real** | 🏠 Local (Foundry) | Latență redusă, răspunsuri mai rapide |
| **Analiza Documentelor** | 🔄 Hibrid | Local pentru extragere, cloud pentru analiză |
| **Generare de Cod** | 🏠 Local (Foundry) | Confidențialitate + modele specializate |
| **Sarcini de Cercetare** | ☁️ Cloud (Azure OpenAI) | Bază de cunoștințe extinsă necesară |

### Comparație Tehnologică

| Tehnologie | Caz de Utilizare | Avantaje | Dezavantaje |
|------------|------------------|----------|-------------|
| **Chainlit** | Dezvoltatori Python, prototipare rapidă | Configurare ușoară, suport pentru streaming | Doar Python |
| **WebGPU** | Confidențialitate maximă, scenarii offline | Nativ pentru browser, fără server necesar | Dimensiune limitată a modelului |
| **Open WebUI** | Implementare pentru producție, echipe | Interfață profesională, gestionare utilizatori | Necesită Docker |

## Cerințe Prealabile

- **Foundry Local**: Instalată și rulată ([Descărcare](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ cu mediu virtual
- **Model**: Cel puțin unul încărcat (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge cu suport WebGPU pentru demo-uri
- **Docker**: Pentru Open WebUI (opțional)

## Instalare și Configurare

### 1. Configurare Mediu Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configurare Foundry Local

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

## Aplicații Exemplu

### Aplicația de Chat Chainlit

**Caracteristici:**
- 🚀 **Streaming în Timp Real**: Token-urile apar pe măsură ce sunt generate
- 🛡️ **Gestionare Robustă a Erorilor**: Degradare și recuperare grațioasă
- 🎨 **Interfață Modernă**: Interfață profesională de chat gata de utilizare
- 🔧 **Configurare Flexibilă**: Variabile de mediu și detectare automată
- 📱 **Design Responsiv**: Funcționează pe dispozitive desktop și mobile

**Start Rapid:**
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

### Demo WebGPU în Browser

**Caracteristici:**
- 🌐 **AI Nativ pentru Browser**: Fără server necesar, rulează complet în browser
- ⚡ **Accelerare WebGPU**: Accelerare hardware când este disponibilă
- 🔒 **Confidențialitate Maximă**: Datele nu părăsesc niciodată dispozitivul
- 🎯 **Zero Instalare**: Funcționează în orice browser compatibil
- 🔄 **Fallback Grațios**: Revine la CPU dacă WebGPU nu este disponibil

**Rulare:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrare Open WebUI

**Caracteristici:**
- 🎨 **Interfață Asemănătoare ChatGPT**: UI profesional, familiar
- 👥 **Suport Multi-utilizator**: Conturi de utilizator și istoric conversații
- 📁 **Procesare Fișiere**: Încărcare și analiză documente
- 🔄 **Schimbare Modele**: Schimbare ușoară între diferite modele
- 🐳 **Implementare Docker**: Configurare containerizată pregătită pentru producție

**Configurare Rapidă:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referință Configurare

### Variabile de Mediu

| Variabilă | Descriere | Implicit | Exemplu |
|-----------|-----------|----------|---------|
| `MODEL` | Alias-ul modelului utilizat | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint Foundry Local | Detectat automat | `http://localhost:51211` |
| `API_KEY` | Cheie API (opțional pentru local) | `""` | `your-api-key` |

## Depanare

### Probleme Comune

**Aplicația Chainlit:**

1. **Serviciu indisponibil:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflicte de port:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Probleme cu mediul Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU nu este suportat:**
   - Actualizați la Chrome/Edge 113+
   - Activați WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Verificați statusul GPU: `chrome://gpu`
   - Demo-ul va reveni automat la CPU

2. **Erori la încărcarea modelului:**
   - Asigurați-vă că aveți conexiune la internet pentru descărcarea modelului
   - Verificați consola browserului pentru erori CORS
   - Verificați că serviți prin HTTP (nu file://)

**Open WebUI:**

1. **Conexiune refuzată:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modelele nu apar:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Listă de Verificare Validare

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

## Utilizare Avansată

### Optimizare Performanță

**Chainlit:**
- Utilizați streaming pentru o performanță percepută mai bună
- Implementați pooling de conexiuni pentru concurență ridicată
- Cache răspunsurile modelului pentru interogări repetate
- Monitorizați utilizarea memoriei cu istorii mari de conversații

**WebGPU:**
- Utilizați WebGPU pentru confidențialitate și viteză maximă
- Implementați cuantificarea modelului pentru modele mai mici
- Utilizați Web Workers pentru procesare în fundal
- Cache modele compilate în stocarea browserului

**Open WebUI:**
- Utilizați volume persistente pentru istoricul conversațiilor
- Configurați limite de resurse pentru containerul Docker
- Implementați strategii de backup pentru datele utilizatorilor
- Configurați un proxy invers pentru terminarea SSL

### Modele de Integrare

**Hibrid Local/Cloud:**
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

**Pipeline Multi-Modal:**
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

## Implementare pentru Producție

### Considerații de Securitate

- **Chei API**: Utilizați variabile de mediu, nu le hardcodați
- **Rețea**: Utilizați HTTPS în producție, luați în considerare VPN pentru accesul echipei
- **Control Acces**: Implementați autentificare pentru Open WebUI
- **Confidențialitate Date**: Auditați ce date rămân locale vs. ce ajung în cloud
- **Actualizări**: Mențineți Foundry Local și containerele actualizate

### Monitorizare și Mentenanță

- **Verificări de Sănătate**: Implementați monitorizarea endpoint-urilor
- **Logare**: Centralizați logurile din toate componentele
- **Metrice**: Monitorizați timpii de răspuns, ratele de eroare, utilizarea resurselor
- **Backup**: Realizați backup regulat pentru datele conversațiilor și configurații

## Referințe și Resurse

### Documentație
- [Documentație Chainlit](https://docs.chainlit.io/) - Ghid complet al framework-ului
- [Documentație Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentație oficială Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrare WebGPU
- [Documentație Open WebUI](https://docs.openwebui.com/) - Configurare avansată

### Fișiere Exemplu
- [`app.py`](../../../../../Module08/samples/04/app.py) - Aplicație Chainlit pentru producție
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook educațional
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferență AI bazată pe browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Configurare completă Open WebUI

### Exemple Asociate
- [Documentație Sesiunea 4](../../04.CuttingEdgeModels.md) - Ghid complet al sesiunii
- [Exemple Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Exemple oficiale

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.