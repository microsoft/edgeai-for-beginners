# Esempio 04: Applicazioni Chat di Produzione con Chainlit

Un esempio completo che dimostra diversi approcci per costruire applicazioni chat pronte per la produzione utilizzando Microsoft Foundry Local, con interfacce web moderne, risposte in streaming e tecnologie avanzate per browser.

## Cosa è incluso

- **🚀 Applicazione Chat Chainlit** (`app.py`): Applicazione chat pronta per la produzione con streaming
- **🌐 Demo WebGPU** (`webgpu-demo/`): Inferenza AI basata su browser con accelerazione hardware
- **🎨 Integrazione Open WebUI** (`open-webui-guide.md`): Interfaccia professionale simile a ChatGPT
- **📚 Notebook Educativo** (`chainlit_app.ipynb`): Materiali interattivi per l'apprendimento

## Avvio Rapido

### 1. Applicazione Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Apre su: `http://localhost:8080`

### 2. Demo Browser WebGPU

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Apre su: `http://localhost:5173`

### 3. Configurazione Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Apre su: `http://localhost:3000`

## Modelli di Architettura

### Matrice Decisionale Locale vs Cloud

| Scenario | Raccomandazione | Motivo |
|----------|----------------|--------|
| **Dati Sensibili alla Privacy** | 🏠 Locale (Foundry) | I dati non lasciano mai il dispositivo |
| **Ragionamento Complesso** | ☁️ Cloud (Azure OpenAI) | Accesso a modelli più grandi |
| **Chat in Tempo Reale** | 🏠 Locale (Foundry) | Minore latenza, risposte più rapide |
| **Analisi Documenti** | 🔄 Ibrido | Locale per estrazione, cloud per analisi |
| **Generazione di Codice** | 🏠 Locale (Foundry) | Privacy + modelli specializzati |
| **Compiti di Ricerca** | ☁️ Cloud (Azure OpenAI) | Necessità di una base di conoscenza ampia |

### Confronto Tecnologico

| Tecnologia | Caso d'Uso | Vantaggi | Svantaggi |
|------------|------------|----------|-----------|
| **Chainlit** | Sviluppatori Python, prototipazione rapida | Configurazione semplice, supporto streaming | Solo Python |
| **WebGPU** | Massima privacy, scenari offline | Nativo per browser, nessun server necessario | Dimensione modello limitata |
| **Open WebUI** | Distribuzione in produzione, team | Interfaccia professionale, gestione utenti | Richiede Docker |

## Prerequisiti

- **Foundry Local**: Installato e in esecuzione ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ con ambiente virtuale
- **Modello**: Almeno uno caricato (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge con supporto WebGPU per demo
- **Docker**: Per Open WebUI (opzionale)

## Installazione e Configurazione

### 1. Configurazione Ambiente Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configurazione Foundry Local

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

## Applicazioni di Esempio

### Applicazione Chat Chainlit

**Caratteristiche:**
- 🚀 **Streaming in Tempo Reale**: I token appaiono man mano che vengono generati
- 🛡️ **Gestione Errori Robusta**: Degradazione e recupero graduali
- 🎨 **Interfaccia Moderna**: Interfaccia chat professionale pronta all'uso
- 🔧 **Configurazione Flessibile**: Variabili d'ambiente e rilevamento automatico
- 📱 **Design Responsivo**: Funziona su dispositivi desktop e mobili

**Avvio Rapido:**
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

### Demo Browser WebGPU

**Caratteristiche:**
- 🌐 **AI Nativa per Browser**: Nessun server richiesto, funziona interamente nel browser
- ⚡ **Accelerazione WebGPU**: Accelerazione hardware quando disponibile
- 🔒 **Massima Privacy**: Nessun dato lascia mai il tuo dispositivo
- 🎯 **Zero Installazione**: Funziona in qualsiasi browser compatibile
- 🔄 **Fallback Graduale**: Passa automaticamente alla CPU se WebGPU non disponibile

**Esecuzione:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrazione Open WebUI

**Caratteristiche:**
- 🎨 **Interfaccia Simile a ChatGPT**: UI professionale e familiare
- 👥 **Supporto Multi-utente**: Account utente e cronologia conversazioni
- 📁 **Elaborazione File**: Carica e analizza documenti
- 🔄 **Cambio Modello**: Passaggio facile tra modelli diversi
- 🐳 **Distribuzione Docker**: Configurazione pronta per la produzione in container

**Configurazione Rapida:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Riferimenti di Configurazione

### Variabili d'Ambiente

| Variabile | Descrizione | Predefinito | Esempio |
|-----------|-------------|-------------|---------|
| `MODEL` | Alias del modello da utilizzare | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint Foundry Local | Rilevato automaticamente | `http://localhost:51211` |
| `API_KEY` | Chiave API (opzionale per locale) | `""` | `your-api-key` |

## Risoluzione dei Problemi

### Problemi Comuni

**Applicazione Chainlit:**

1. **Servizio non disponibile:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflitti di porta:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problemi con l'ambiente Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU non supportato:**
   - Aggiorna a Chrome/Edge 113+
   - Abilita WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Controlla stato GPU: `chrome://gpu`
   - La demo passerà automaticamente alla CPU

2. **Errori di caricamento modello:**
   - Assicurati di avere una connessione internet per il download del modello
   - Controlla la console del browser per errori CORS
   - Verifica che stai servendo tramite HTTP (non file://)

**Open WebUI:**

1. **Connessione rifiutata:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modelli non visibili:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Checklist di Validazione

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

## Uso Avanzato

### Ottimizzazione delle Prestazioni

**Chainlit:**
- Usa lo streaming per migliorare la percezione delle prestazioni
- Implementa il pooling delle connessioni per alta concorrenza
- Memorizza nella cache le risposte del modello per query ripetute
- Monitora l'uso della memoria con cronologie di conversazioni estese

**WebGPU:**
- Usa WebGPU per massima privacy e velocità
- Implementa la quantizzazione del modello per modelli più piccoli
- Usa Web Workers per elaborazione in background
- Memorizza nella cache i modelli compilati nello storage del browser

**Open WebUI:**
- Usa volumi persistenti per la cronologia delle conversazioni
- Configura limiti di risorse per il container Docker
- Implementa strategie di backup per i dati utente
- Configura un reverse proxy per la terminazione SSL

### Modelli di Integrazione

**Ibrido Locale/Cloud:**
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

**Pipeline Multi-Modale:**
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

## Distribuzione in Produzione

### Considerazioni sulla Sicurezza

- **Chiavi API**: Usa variabili d'ambiente, non codificarle mai direttamente
- **Rete**: Usa HTTPS in produzione, considera VPN per accesso del team
- **Controllo Accessi**: Implementa autenticazione per Open WebUI
- **Privacy dei Dati**: Controlla quali dati rimangono locali e quali vanno nel cloud
- **Aggiornamenti**: Mantieni Foundry Local e i container aggiornati

### Monitoraggio e Manutenzione

- **Controlli di Salute**: Implementa il monitoraggio degli endpoint
- **Logging**: Centralizza i log di tutti i componenti
- **Metriche**: Monitora tempi di risposta, tassi di errore, uso delle risorse
- **Backup**: Esegui regolarmente il backup dei dati delle conversazioni e delle configurazioni

## Riferimenti e Risorse

### Documentazione
- [Documentazione Chainlit](https://docs.chainlit.io/) - Guida completa al framework
- [Documentazione Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentazione ufficiale Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrazione WebGPU
- [Documentazione Open WebUI](https://docs.openwebui.com/) - Configurazione avanzata

### File di Esempio
- [`app.py`](../../../../../Module08/samples/04/app.py) - Applicazione Chainlit di produzione
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook educativo
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferenza AI basata su browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Configurazione completa Open WebUI

### Esempi Correlati
- [Documentazione Sessione 4](../../04.CuttingEdgeModels.md) - Guida completa alla sessione
- [Esempi Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Esempi ufficiali

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.