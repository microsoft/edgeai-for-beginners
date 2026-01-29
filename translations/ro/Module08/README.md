# Modulul 08: Practică cu Microsoft Foundry Local - Kit complet pentru dezvoltatori

## Prezentare generală

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) reprezintă generația următoare în dezvoltarea AI la margine, oferind dezvoltatorilor instrumente puternice pentru a construi, implementa și scala aplicații AI local, menținând în același timp integrarea fluidă cu Azure AI Foundry. Acest modul acoperă în detaliu Foundry Local, de la instalare până la dezvoltarea avansată a agenților.

**Tehnologii cheie:**
- Microsoft Foundry Local CLI și SDK
- Integrare cu Azure AI Foundry
- Inferență de modele pe dispozitiv
- Cache local de modele și optimizare
- Arhitecturi bazate pe agenți

## Obiective de învățare

Prin completarea acestui modul, vei:

- **Stăpâni Foundry Local**: Instala, configura și optimiza pentru dezvoltarea pe Windows 11
- **Implementa modele diverse**: Rula modele phi, qwen, deepseek și GPT local folosind comenzi CLI
- **Construi soluții de producție**: Crea aplicații AI cu inginerie avansată a prompturilor și integrare de date
- **Valorifica ecosistemul open-source**: Integra modele Hugging Face și contribuții comunitare
- **Dezvolta agenți AI**: Construi agenți inteligenți cu capacități de ancorare și orchestrare
- **Implementa modele de întreprindere**: Crea soluții AI modulare și scalabile pentru implementare în producție

## Structura sesiunii

### [1: Introducere în Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Instalare, configurare CLI, implementare de modele și optimizare hardware

**Subiecte cheie**: Instalare completă • Comenzi CLI • Cache de modele • Accelerare hardware • Implementare multi-model

**Exemplu**: [REST Chat Quickstart](./samples/01/README.md) • [Integrare OpenAI SDK](./samples/02/README.md) • [Descoperire și benchmarking modele](./samples/03/README.md)

**Durată**: 2-3 ore | **Nivel**: Începător

---

### [2: Construirea soluțiilor AI cu Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Inginerie avansată a prompturilor, integrare de date și conectivitate cloud

**Subiecte cheie**: Inginerie a prompturilor • Integrare de date • Fluxuri de lucru Azure • Optimizare performanță • Monitorizare

**Exemplu**: [Aplicație Chainlit RAG](./samples/04/README.md)

**Durată**: 2-3 ore | **Nivel**: Intermediar

---

### [3: Modele open-source în Foundry Local](./03.OpenSourceModels.md)
**Focus**: Integrare Hugging Face, strategii BYOM și modele comunitare

**Subiecte cheie**: Integrare Hugging Face • Bring-your-own-model • Perspective Model Mondays • Contribuții comunitare • Selecție de modele

**Exemplu**: [Orchestrare multi-agent](./samples/05/README.md)

**Durată**: 2-3 ore | **Nivel**: Intermediar

---

### [4: Explorarea modelelor de ultimă generație](./04.CuttingEdgeModels.md)
**Focus**: LLM-uri vs SLM-uri, implementare EdgeAI și demonstrații avansate

**Subiecte cheie**: Comparare modele • Inferență la margine vs cloud • Phi + ONNX Runtime • Aplicație Chainlit RAG • Optimizare WebGPU

**Exemplu**: [Router pentru modele ca instrumente](./samples/06/README.md)

**Durată**: 3-4 ore | **Nivel**: Avansat

---

### [5: Construirea rapidă a agenților AI](./05.AIPoweredAgents.md)
**Focus**: Arhitecturi de agenți, prompturi de sistem, ancorare și orchestrare

**Subiecte cheie**: Modele de design pentru agenți • Inginerie a prompturilor de sistem • Tehnici de ancorare • Sisteme multi-agent • Implementare în producție

**Exemplu**: [Orchestrare multi-agent](./samples/05/README.md) • [Sistem multi-agent avansat](./samples/09/README.md)

**Durată**: 3-4 ore | **Nivel**: Avansat

---

### [6: Foundry Local - Modele ca instrumente](./06.ModelsAsTools.md)
**Focus**: Soluții AI modulare, scalare la nivel de întreprindere și modele de producție

**Subiecte cheie**: Modele ca instrumente • Implementare pe dispozitiv • Integrare SDK/API • Arhitecturi de întreprindere • Strategii de scalare

**Exemplu**: [Router pentru modele ca instrumente](./samples/06/README.md) • [Framework Foundry Tools](./samples/10/README.md)

**Durată**: 3-4 ore | **Nivel**: Expert

---

### [7: Modele de integrare directă API](./samples/07/README.md)
**Focus**: Integrare pură REST API fără dependențe SDK pentru control maxim

**Subiecte cheie**: Implementare client HTTP • Autentificare personalizată • Monitorizare sănătate modele • Răspunsuri în streaming • Gestionare erori în producție

**Exemplu**: [Client API direct](./samples/07/README.md)

**Durată**: 2-3 ore | **Nivel**: Intermediar

---

### [8: Aplicație de chat nativă Windows 11](./samples/08/README.md)
**Focus**: Construirea aplicațiilor moderne de chat native cu integrare Foundry Local

**Subiecte cheie**: Dezvoltare Electron • Fluent Design System • Integrare nativă Windows • Streaming în timp real • Design interfață chat

**Exemplu**: [Aplicație de chat Windows 11](./samples/08/README.md)

**Durată**: 3-4 ore | **Nivel**: Avansat

---

### [9: Orchestrare avansată multi-agent](./samples/09/README.md)
**Focus**: Coordonarea sofisticată a agenților, delegarea sarcinilor specializate și fluxuri de lucru AI colaborative

**Subiecte cheie**: Coordonare inteligentă a agenților • Modele de apelare funcții • Comunicare între agenți • Orchestrare fluxuri de lucru • Mecanisme de asigurare a calității

**Exemplu**: [Sistem multi-agent avansat](./samples/09/README.md)

**Durată**: 4-5 ore | **Nivel**: Expert

---

### [10: Foundry Local ca framework de instrumente](./samples/10/README.md)
**Focus**: Arhitectură orientată pe instrumente pentru integrarea Foundry Local în aplicații și framework-uri existente

**Subiecte cheie**: Integrare LangChain • Funcții Semantic Kernel • Framework-uri REST API • Instrumente CLI • Integrare Jupyter • Modele de implementare în producție

**Exemplu**: [Framework Foundry Tools](./samples/10/README.md)

**Durată**: 4-5 ore | **Nivel**: Expert

## Cerințe preliminare

### Cerințe de sistem
- **Sistem de operare**: Windows 11 (22H2 sau mai recent)
- **Memorie**: 16GB RAM (32GB recomandat pentru modele mai mari)
- **Stocare**: 50GB spațiu liber pentru cache de modele
- **Hardware**: Dispozitiv cu NPU recomandat (PC Copilot+), GPU opțional
- **Rețea**: Internet de mare viteză pentru descărcarea inițială a modelelor

### Mediu de dezvoltare
- Visual Studio Code cu extensia AI Toolkit
- Python 3.10+ și pip
- Git pentru controlul versiunilor
- PowerShell sau Command Prompt
- Azure CLI (opțional pentru integrare cloud)

### Cunoștințe necesare
- Înțelegere de bază a conceptelor AI/ML
- Familiaritate cu linia de comandă
- Noțiuni de bază de programare în Python
- Concepte REST API
- Cunoștințe de bază despre prompturi și inferență de modele

## Cronologia modulului

**Timp estimat total**: 30-38 ore

| Sesiune | Domeniu de focus | Exemple | Timp | Complexitate |
|---------|------------------|---------|------|-------------|
|  1 | Configurare & Baze | 01, 02, 03 | 2-3 ore | Începător |
|  2 | Soluții AI | 04 | 2-3 ore | Intermediar |
|  3 | Open Source | 05 | 2-3 ore | Intermediar |
|  4 | Modele avansate | 06 | 3-4 ore | Avansat |
|  5 | Agenți AI | 05, 09 | 3-4 ore | Avansat |
|  6 | Instrumente de întreprindere | 06, 10 | 3-4 ore | Expert |
|  7 | Integrare directă API | 07 | 2-3 ore | Intermediar |
|  8 | Aplicație chat Windows 11 | 08 | 3-4 ore | Avansat |
|  9 | Multi-agent avansat | 09 | 4-5 ore | Expert |
| 10 | Framework de instrumente | 10 | 4-5 ore | Expert |

## Resurse cheie

**Documentație oficială:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Cod sursă și exemple oficiale
- [Documentație Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Ghid complet de configurare și utilizare
- [Seria Model Mondays](https://aka.ms/model-mondays) - Evidențieri și tutoriale săptămânale despre modele

**Comunitate & Suport:**
- [Discuții Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Întrebări și cereri de funcționalități din comunitate
- [Comunitatea Microsoft AI Developer](https://techcommunity.microsoft.com/category/artificialintelligence) - Noutăți și bune practici

## Rezultate de învățare

După finalizarea acestui modul, vei fi pregătit să:

### Stăpânire tehnică
- **Implementa și gestiona**: Instalări Foundry Local în medii de dezvoltare și producție
- **Integra modele**: Lucrează fără probleme cu diverse familii de modele de la Microsoft, Hugging Face și surse comunitare
- **Construi aplicații**: Creează aplicații AI pregătite pentru producție cu funcționalități avansate și optimizări
- **Dezvolta agenți**: Implementează agenți AI sofisticați cu ancorare, raționament și integrare de instrumente

### Înțelegere strategică
- **Decizii arhitecturale**: Ia decizii informate între implementarea locală vs cloud
- **Optimizare performanță**: Optimizează performanța inferenței pe diferite configurații hardware
- **Scalare la nivel de întreprindere**: Proiectează aplicații care se extind de la prototipuri locale la implementări de întreprindere
- **Confidențialitate și securitate**: Implementează soluții AI care protejează confidențialitatea prin inferență locală

### Capacități de inovare
- **Prototipare rapidă**: Construiește și testează rapid concepte de aplicații AI pe toate cele 10 modele de exemplu
- **Integrare comunitară**: Valorifică modele open-source și contribuie la ecosistem
- **Modele avansate**: Implementează modele AI de ultimă generație, inclusiv RAG, agenți și integrare de instrumente
- **Stăpânirea framework-urilor**: Integrare la nivel expert cu LangChain, Semantic Kernel, Chainlit și Electron
- **Implementare în producție**: Implementare soluții AI scalabile de la prototipuri locale la sisteme de întreprindere
- **Dezvoltare pregătită pentru viitor**: Construiește aplicații pregătite pentru tehnologii și modele AI emergente

## Începe acum

1. **Configurare mediu**: Asigură-te că ai Windows 11 cu hardware recomandat (vezi Cerințe preliminare)
2. **Instalează Foundry Local**: Urmează Sesiunea 1 pentru instalare și configurare completă
3. **Rulează Exemplul 01**: Începe cu integrarea de bază REST API pentru a verifica configurarea
4. **Progresează prin exemple**: Completează exemplele 01-10 pentru stăpânire completă

## Metrice de succes

Monitorizează progresul tău prin toate cele 10 exemple cuprinzătoare:

### Nivel de bază (Exemple 01-03)
- [ ] Instalează și configurează cu succes Foundry Local
- [ ] Completează integrarea REST API (Exemplul 01)
- [ ] Implementează compatibilitatea OpenAI SDK (Exemplul 02)
- [ ] Realizează descoperirea și benchmarking-ul modelelor (Exemplul 03)

### Nivel de aplicație (Exemple 04-06)
- [ ] Implementează și rulează cel puțin 4 familii de modele diferite
- [ ] Construiește o aplicație funcțională RAG chat (Exemplul 04)
- [ ] Creează un sistem de orchestrare multi-agent (Exemplul 05)
- [ ] Implementează rutarea inteligentă a modelelor (Exemplul 06)

### Nivel de integrare avansată (Exemple 07-10)
- [ ] Construiește un client API pregătit pentru producție (Exemplul 07)
- [ ] Dezvoltă o aplicație de chat nativă Windows 11 (Exemplul 08)
- [ ] Implementează un sistem multi-agent avansat (Exemplul 09)
- [ ] Creează un framework de instrumente cuprinzător (Exemplul 10)

### Indicatori de stăpânire
- [ ] Rulează cu succes toate cele 10 exemple fără erori
- [ ] Personalizează cel puțin 3 exemple pentru cazuri de utilizare specifice
- [ ] Implementează 2+ exemple în medii similare producției
- [ ] Contribuie cu îmbunătățiri sau extensii la codul exemplu
- [ ] Integrează modelele Foundry Local în proiecte personale/profesionale

## Ghid de start rapid - Toate cele 10 exemple

### Configurare mediu (Necesar pentru toate exemplele)

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

### Exemple de bază (01-06)

**Exemplul 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Exemplul 02: Integrare OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Exemplul 03: Descoperire și benchmarking modele**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Exemplul 04: Aplicație Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Exemplul 05: Orchestrare multi-agent**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Exemplul 06: Router pentru modele ca instrumente**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Exemple de integrare avansată (07-10)

**Exemplul 07: Client API direct**
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

**Exemplul 08: Aplicație de chat Windows 11**
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

**Exemplul 09: Sistem multi-agent avansat**
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

**Exemplul 10: Framework Foundry Tools**
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

### Rezolvarea problemelor comune

**Erori de conexiune Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Probleme de încărcare modele**
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

**Probleme de dependențe**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Rezumat
Acest modul reprezintă vârful dezvoltării AI la margine, combinând instrumentele de nivel enterprise de la Microsoft cu flexibilitatea și inovația ecosistemului open-source. Stăpânind Foundry Local prin toate cele 10 exemple cuprinzătoare, veți fi poziționat în avangarda dezvoltării aplicațiilor AI.

**Calea completă de învățare:**
- **Fundament** (Exemplele 01-03): Integrarea API-urilor și gestionarea modelelor
- **Aplicații** (Exemplele 04-06): RAG, agenți și rutare inteligentă
- **Avansat** (Exemplele 07-10): Cadre de producție și integrare enterprise

Pentru integrarea Azure OpenAI (Sesiunea 2), consultați fișierele README individuale ale exemplelor pentru variabilele de mediu necesare și setările versiunii API.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.