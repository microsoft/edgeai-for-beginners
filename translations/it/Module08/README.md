# Modulo 08: Pratica con Microsoft Foundry Local - Toolkit Completo per Sviluppatori

## Panoramica

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) rappresenta la nuova generazione dello sviluppo AI edge, fornendo agli sviluppatori strumenti potenti per creare, distribuire e scalare applicazioni AI localmente, mantenendo un'integrazione fluida con Azure AI Foundry. Questo modulo offre una copertura completa di Foundry Local, dall'installazione allo sviluppo avanzato di agenti.

**Tecnologie Chiave:**
- Microsoft Foundry Local CLI e SDK
- Integrazione con Azure AI Foundry
- Inferenza di modelli su dispositivo
- Caching e ottimizzazione locale dei modelli
- Architetture basate su agenti

## Obiettivi di Apprendimento

Completando questo modulo, sarai in grado di:

- **Dominare Foundry Local**: Installare, configurare e ottimizzare per lo sviluppo su Windows 11
- **Distribuire Modelli Diversi**: Eseguire modelli phi, qwen, deepseek e GPT localmente con comandi CLI
- **Creare Soluzioni di Produzione**: Sviluppare applicazioni AI con tecniche avanzate di prompt engineering e integrazione dei dati
- **Sfruttare l'Ecosistema Open-Source**: Integrare modelli Hugging Face e contributi della comunità
- **Sviluppare Agenti AI**: Costruire agenti intelligenti con capacità di grounding e orchestrazione
- **Implementare Pattern Aziendali**: Creare soluzioni AI modulari e scalabili per la distribuzione in produzione

## Struttura della Sessione

### [1: Introduzione a Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Installazione, configurazione CLI, distribuzione di modelli e ottimizzazione hardware

**Argomenti Chiave**: Installazione completa • Comandi CLI • Caching dei modelli • Accelerazione hardware • Distribuzione multi-modello

**Esempi**: [REST Chat Quickstart](./samples/01/README.md) • [Integrazione SDK OpenAI](./samples/02/README.md) • [Scoperta e Benchmarking dei Modelli](./samples/03/README.md)

**Durata**: 2-3 ore | **Livello**: Principiante

---

### [2: Creare Soluzioni AI con Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Prompt engineering avanzato, integrazione dei dati e connettività cloud

**Argomenti Chiave**: Prompt engineering • Integrazione dei dati • Workflow Azure • Ottimizzazione delle prestazioni • Monitoraggio

**Esempio**: [Applicazione Chainlit RAG](./samples/04/README.md)

**Durata**: 2-3 ore | **Livello**: Intermedio

---

### [3: Modelli Open-Source con Foundry Local](./03.OpenSourceModels.md)
**Focus**: Integrazione Hugging Face, strategie BYOM e modelli della comunità

**Argomenti Chiave**: Integrazione Hugging Face • Bring-your-own-model • Approfondimenti Model Mondays • Contributi della comunità • Selezione dei modelli

**Esempio**: [Orchestrazione Multi-Agente](./samples/05/README.md)

**Durata**: 2-3 ore | **Livello**: Intermedio

---

### [4: Esplorare Modelli All'Avanguardia](./04.CuttingEdgeModels.md)
**Focus**: Confronto tra LLM e SLM, implementazione EdgeAI e demo avanzate

**Argomenti Chiave**: Confronto tra modelli • Inferenza edge vs cloud • Phi + ONNX Runtime • Applicazione Chainlit RAG • Ottimizzazione WebGPU

**Esempio**: [Router Modelli-come-Strumenti](./samples/06/README.md)

**Durata**: 3-4 ore | **Livello**: Avanzato

---

### [5: Creare Agenti AI Rapidamente](./05.AIPoweredAgents.md)
**Focus**: Architetture di agenti, prompt di sistema, grounding e orchestrazione

**Argomenti Chiave**: Pattern di progettazione degli agenti • Prompt di sistema • Tecniche di grounding • Sistemi multi-agente • Distribuzione in produzione

**Esempi**: [Orchestrazione Multi-Agente](./samples/05/README.md) • [Sistema Multi-Agente Avanzato](./samples/09/README.md)

**Durata**: 3-4 ore | **Livello**: Avanzato

---

### [6: Foundry Local - Modelli come Strumenti](./06.ModelsAsTools.md)
**Focus**: Soluzioni AI modulari, scalabilità aziendale e pattern di produzione

**Argomenti Chiave**: Modelli come strumenti • Distribuzione su dispositivo • Integrazione SDK/API • Architetture aziendali • Strategie di scalabilità

**Esempi**: [Router Modelli-come-Strumenti](./samples/06/README.md) • [Framework Strumenti Foundry](./samples/10/README.md)

**Durata**: 3-4 ore | **Livello**: Esperto

---

### [7: Pattern di Integrazione API Diretta](./samples/07/README.md)
**Focus**: Integrazione API REST pura senza dipendenze SDK per il massimo controllo

**Argomenti Chiave**: Implementazione client HTTP • Autenticazione personalizzata • Monitoraggio della salute dei modelli • Risposte in streaming • Gestione degli errori in produzione

**Esempio**: [Client API Diretta](./samples/07/README.md)

**Durata**: 2-3 ore | **Livello**: Intermedio

---

### [8: Applicazione Chat Nativa per Windows 11](./samples/08/README.md)
**Focus**: Creare applicazioni chat moderne native con integrazione Foundry Local

**Argomenti Chiave**: Sviluppo Electron • Fluent Design System • Integrazione nativa Windows • Streaming in tempo reale • Progettazione interfaccia chat

**Esempio**: [Applicazione Chat per Windows 11](./samples/08/README.md)

**Durata**: 3-4 ore | **Livello**: Avanzato

---

### [9: Orchestrazione Multi-Agente Avanzata](./samples/09/README.md)
**Focus**: Coordinamento sofisticato degli agenti, delega di compiti specializzati e workflow collaborativi AI

**Argomenti Chiave**: Coordinamento intelligente degli agenti • Pattern di chiamata delle funzioni • Comunicazione tra agenti • Orchestrazione dei workflow • Meccanismi di garanzia della qualità

**Esempio**: [Sistema Multi-Agente Avanzato](./samples/09/README.md)

**Durata**: 4-5 ore | **Livello**: Esperto

---

### [10: Foundry Local come Framework di Strumenti](./samples/10/README.md)
**Focus**: Architettura orientata agli strumenti per integrare Foundry Local in applicazioni e framework esistenti

**Argomenti Chiave**: Integrazione LangChain • Funzioni Semantic Kernel • Framework API REST • Strumenti CLI • Integrazione Jupyter • Pattern di distribuzione in produzione

**Esempio**: [Framework Strumenti Foundry](./samples/10/README.md)

**Durata**: 4-5 ore | **Livello**: Esperto

## Prerequisiti

### Requisiti di Sistema
- **Sistema Operativo**: Windows 11 (22H2 o successivo)
- **Memoria**: 16GB RAM (32GB consigliati per modelli più grandi)
- **Spazio di Archiviazione**: 50GB di spazio libero per il caching dei modelli
- **Hardware**: Dispositivo con NPU consigliato (PC Copilot+), GPU opzionale
- **Rete**: Connessione internet ad alta velocità per il download iniziale dei modelli

### Ambiente di Sviluppo
- Visual Studio Code con estensione AI Toolkit
- Python 3.10+ e pip
- Git per il controllo di versione
- PowerShell o Prompt dei Comandi
- Azure CLI (opzionale per integrazione cloud)

### Conoscenze Prerequisite
- Comprensione di base dei concetti AI/ML
- Familiarità con la linea di comando
- Nozioni di base di programmazione Python
- Concetti di API REST
- Conoscenza di base del prompting e dell'inferenza dei modelli

## Cronologia del Modulo

**Tempo Totale Stimato**: 30-38 ore

| Sessione | Area di Focus | Esempi | Tempo | Complessità |
|----------|---------------|--------|-------|-------------|
|  1 | Setup & Basi | 01, 02, 03 | 2-3 ore | Principiante |
|  2 | Soluzioni AI | 04 | 2-3 ore | Intermedio |
|  3 | Open Source | 05 | 2-3 ore | Intermedio |
|  4 | Modelli Avanzati | 06 | 3-4 ore | Avanzato |
|  5 | Agenti AI | 05, 09 | 3-4 ore | Avanzato |
|  6 | Strumenti Aziendali | 06, 10 | 3-4 ore | Esperto |
|  7 | Integrazione API Diretta | 07 | 2-3 ore | Intermedio |
|  8 | App Chat Windows 11 | 08 | 3-4 ore | Avanzato |
|  9 | Multi-Agente Avanzato | 09 | 4-5 ore | Esperto |
| 10 | Framework Strumenti | 10 | 4-5 ore | Esperto |

## Risorse Chiave

**Documentazione Ufficiale:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Codice sorgente e esempi ufficiali
- [Documentazione Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Guida completa all'installazione e utilizzo
- [Serie Model Mondays](https://aka.ms/model-mondays) - Approfondimenti settimanali sui modelli e tutorial

**Comunità & Supporto:**
- [Discussioni su Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Q&A della comunità e richieste di funzionalità
- [Comunità Sviluppatori AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Ultime novità e best practice

## Risultati di Apprendimento

Completando questo modulo, sarai in grado di:

### Padronanza Tecnica
- **Distribuire e Gestire**: Installazioni di Foundry Local in ambienti di sviluppo e produzione
- **Integrare Modelli**: Lavorare senza problemi con famiglie di modelli diverse da Microsoft, Hugging Face e fonti della comunità
- **Creare Applicazioni**: Sviluppare applicazioni AI pronte per la produzione con funzionalità avanzate e ottimizzazioni
- **Sviluppare Agenti**: Implementare agenti AI sofisticati con grounding, ragionamento e integrazione di strumenti

### Comprensione Strategica
- **Decisioni Architetturali**: Fare scelte informate tra distribuzione locale e cloud
- **Ottimizzazione delle Prestazioni**: Ottimizzare le prestazioni di inferenza su diverse configurazioni hardware
- **Scalabilità Aziendale**: Progettare applicazioni che scalano dai prototipi locali alle distribuzioni aziendali
- **Privacy e Sicurezza**: Implementare soluzioni AI che preservano la privacy con inferenza locale

### Capacità di Innovazione
- **Prototipazione Rapida**: Creare e testare rapidamente concetti di applicazioni AI utilizzando tutti i 10 pattern di esempio
- **Integrazione Comunitaria**: Sfruttare modelli open-source e contribuire all'ecosistema
- **Pattern Avanzati**: Implementare pattern AI all'avanguardia, inclusi RAG, agenti e integrazione di strumenti
- **Padronanza dei Framework**: Integrazione esperta con LangChain, Semantic Kernel, Chainlit ed Electron
- **Distribuzione in Produzione**: Distribuire soluzioni AI scalabili dai prototipi locali ai sistemi aziendali
- **Sviluppo Pronto per il Futuro**: Creare applicazioni pronte per tecnologie e pattern AI emergenti

## Come Iniziare

1. **Setup dell'Ambiente**: Assicurati di avere Windows 11 con hardware consigliato (vedi Prerequisiti)
2. **Installa Foundry Local**: Segui la Sessione 1 per l'installazione e configurazione completa
3. **Esegui l'Esempio 01**: Inizia con l'integrazione API REST di base per verificare il setup
4. **Progredisci Attraverso gli Esempi**: Completa gli esempi 01-10 per una padronanza completa

## Metriche di Successo

Monitora i tuoi progressi attraverso tutti i 10 esempi completi:

### Livello Fondamentale (Esempi 01-03)
- [ ] Installare e configurare con successo Foundry Local
- [ ] Completare l'integrazione API REST (Esempio 01)
- [ ] Implementare la compatibilità con SDK OpenAI (Esempio 02)
- [ ] Eseguire scoperta e benchmarking dei modelli (Esempio 03)

### Livello Applicativo (Esempi 04-06)
- [ ] Distribuire ed eseguire almeno 4 famiglie di modelli diverse
- [ ] Creare un'applicazione chat RAG funzionale (Esempio 04)
- [ ] Creare un sistema di orchestrazione multi-agente (Esempio 05)
- [ ] Implementare un router intelligente per i modelli (Esempio 06)

### Livello di Integrazione Avanzata (Esempi 07-10)
- [ ] Creare un client API pronto per la produzione (Esempio 07)
- [ ] Sviluppare un'applicazione chat nativa per Windows 11 (Esempio 08)
- [ ] Implementare un sistema multi-agente avanzato (Esempio 09)
- [ ] Creare un framework di strumenti completo (Esempio 10)

### Indicatori di Padronanza
- [ ] Eseguire con successo tutti i 10 esempi senza errori
- [ ] Personalizzare almeno 3 esempi per casi d'uso specifici
- [ ] Distribuire 2+ esempi in ambienti simili alla produzione
- [ ] Contribuire con miglioramenti o estensioni al codice degli esempi
- [ ] Integrare i pattern di Foundry Local in progetti personali/professionali

## Guida Rapida - Tutti i 10 Esempi

### Setup dell'Ambiente (Richiesto per Tutti gli Esempi)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Esempi Fondamentali (01-06)

**Esempio 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Esempio 02: Integrazione SDK OpenAI**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Esempio 03: Scoperta e Benchmarking dei Modelli**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Esempio 04: Applicazione Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Esempio 05: Orchestrazione Multi-Agente**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Esempio 06: Router Modelli-come-Strumenti**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Esempi di Integrazione Avanzata (07-10)

**Esempio 07: Client API Diretta**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Esempio 08: Applicazione Chat per Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Esempio 09: Sistema Multi-Agente Avanzato**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Esempio 10: Framework Strumenti Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Risoluzione dei Problemi Comuni

**Errori di Connessione Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemi di Caricamento dei Modelli**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Problemi di Dipendenze**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Sommario
Questo modulo rappresenta l'avanguardia dello sviluppo AI edge, combinando gli strumenti di livello enterprise di Microsoft con la flessibilità e l'innovazione dell'ecosistema open-source. Padroneggiando Foundry Local attraverso tutti i 10 esempi completi, sarai posizionato all'avanguardia nello sviluppo di applicazioni AI.

**Percorso di apprendimento completo:**
- **Fondamenti** (Esempi 01-03): Integrazione API e gestione dei modelli
- **Applicazioni** (Esempi 04-06): RAG, agenti e instradamento intelligente
- **Avanzato** (Esempi 07-10): Framework di produzione e integrazione aziendale

Per l'integrazione con Azure OpenAI (Sessione 2), consulta i file README dei singoli esempi per le variabili d'ambiente richieste e le impostazioni della versione API.

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.