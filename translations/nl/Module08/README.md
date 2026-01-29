# Module 08: Praktisch aan de slag met Microsoft Foundry Local - Complete ontwikkeltoolkit

## Overzicht

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) vertegenwoordigt de volgende generatie van edge AI-ontwikkeling en biedt ontwikkelaars krachtige tools om AI-toepassingen lokaal te bouwen, implementeren en schalen, terwijl naadloze integratie met Azure AI Foundry behouden blijft. Deze module biedt een uitgebreide dekking van Foundry Local, van installatie tot geavanceerde agentontwikkeling.

**Belangrijke technologieën:**
- Microsoft Foundry Local CLI en SDK
- Integratie met Azure AI Foundry
- Modelinferentie op apparaat
- Lokale modelcaching en optimalisatie
- Agent-gebaseerde architecturen

## Leerdoelen

Door deze module te voltooien, leer je:

- **Beheers Foundry Local**: Installeer, configureer en optimaliseer voor Windows 11-ontwikkeling
- **Implementeer diverse modellen**: Voer phi-, qwen-, deepseek- en GPT-modellen lokaal uit met CLI-commando's
- **Bouw productietoepassingen**: Creëer AI-toepassingen met geavanceerde prompt-engineering en gegevensintegratie
- **Maak gebruik van open-source ecosystemen**: Integreer Hugging Face-modellen en bijdragen van de gemeenschap
- **Ontwikkel AI-agents**: Bouw intelligente agents met grounding- en orkestratiecapaciteiten
- **Implementeer bedrijfsmodellen**: Creëer modulaire, schaalbare AI-oplossingen voor productie-implementatie

## Sessiestructuur

### [1: Aan de slag met Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Installatie, CLI-configuratie, modelimplementatie en hardware-optimalisatie

**Belangrijke onderwerpen**: Volledige installatie • CLI-commando's • Modelcaching • Hardwareversnelling • Multi-model implementatie

**Voorbeeld**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integratie](./samples/02/README.md) • [Modelontdekking & Benchmarking](./samples/03/README.md)

**Duur**: 2-3 uur | **Niveau**: Beginner

---

### [2: Bouw AI-oplossingen met Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Geavanceerde prompt-engineering, gegevensintegratie en cloudconnectiviteit

**Belangrijke onderwerpen**: Prompt-engineering • Gegevensintegratie • Azure-workflows • Prestatieoptimalisatie • Monitoring

**Voorbeeld**: [Chainlit RAG-toepassing](./samples/04/README.md)

**Duur**: 2-3 uur | **Niveau**: Gemiddeld

---

### [3: Open-source modellen Foundry Local](./03.OpenSourceModels.md)
**Focus**: Hugging Face-integratie, BYOM-strategieën en gemeenschapsmodellen

**Belangrijke onderwerpen**: Hugging Face-integratie • Bring-your-own-model • Model Mondays inzichten • Bijdragen van de gemeenschap • Modelselectie

**Voorbeeld**: [Multi-Agent Orchestratie](./samples/05/README.md)

**Duur**: 2-3 uur | **Niveau**: Gemiddeld

---

### [4: Verken geavanceerde modellen](./04.CuttingEdgeModels.md)
**Focus**: LLM's versus SLM's, EdgeAI-implementatie en geavanceerde demo's

**Belangrijke onderwerpen**: Modelvergelijking • Edge versus cloud-inferentie • Phi + ONNX Runtime • Chainlit RAG-app • WebGPU-optimalisatie

**Voorbeeld**: [Models-as-Tools Router](./samples/06/README.md)

**Duur**: 3-4 uur | **Niveau**: Geavanceerd

---

### [5: Bouw snel AI-aangedreven agents](./05.AIPoweredAgents.md)
**Focus**: Agentarchitecturen, systeemprompts, grounding en orkestratie

**Belangrijke onderwerpen**: Agentontwerpmodellen • Systeemprompt-engineering • Groundingtechnieken • Multi-agent systemen • Productie-implementatie

**Voorbeeld**: [Multi-Agent Orchestratie](./samples/05/README.md) • [Geavanceerd Multi-Agent Systeem](./samples/09/README.md)

**Duur**: 3-4 uur | **Niveau**: Geavanceerd

---

### [6: Foundry Local - Modellen als tools](./06.ModelsAsTools.md)
**Focus**: Modulaire AI-oplossingen, bedrijfsopschaling en productiepatronen

**Belangrijke onderwerpen**: Modellen als tools • Implementatie op apparaat • SDK/API-integratie • Bedrijfsarchitecturen • Opschalingsstrategieën

**Voorbeeld**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Duur**: 3-4 uur | **Niveau**: Expert

---

### [7: Directe API-integratiepatronen](./samples/07/README.md)
**Focus**: Pure REST API-integratie zonder SDK-afhankelijkheden voor maximale controle

**Belangrijke onderwerpen**: HTTP-clientimplementatie • Aangepaste authenticatie • Modelgezondheidsmonitoring • Streamingreacties • Productiefoutafhandeling

**Voorbeeld**: [Direct API Client](./samples/07/README.md)

**Duur**: 2-3 uur | **Niveau**: Gemiddeld

---

### [8: Windows 11 Native Chat-toepassing](./samples/08/README.md)
**Focus**: Moderne native chattoepassingen bouwen met Foundry Local-integratie

**Belangrijke onderwerpen**: Electron-ontwikkeling • Fluent Design System • Native Windows-integratie • Real-time streaming • Chatinterfaceontwerp

**Voorbeeld**: [Windows 11 Chat-toepassing](./samples/08/README.md)

**Duur**: 3-4 uur | **Niveau**: Geavanceerd

---

### [9: Geavanceerde Multi-Agent Orchestratie](./samples/09/README.md)
**Focus**: Geavanceerde agentcoördinatie, gespecialiseerde taakdelegatie en collaboratieve AI-workflows

**Belangrijke onderwerpen**: Intelligente agentcoördinatie • Functieaanroepmodellen • Cross-agent communicatie • Workfloworkestratie • Mechanismen voor kwaliteitsborging

**Voorbeeld**: [Geavanceerd Multi-Agent Systeem](./samples/09/README.md)

**Duur**: 4-5 uur | **Niveau**: Expert

---

### [10: Foundry Local als Tools Framework](./samples/10/README.md)
**Focus**: Tool-first architectuur voor integratie van Foundry Local in bestaande toepassingen en frameworks

**Belangrijke onderwerpen**: LangChain-integratie • Semantic Kernel-functies • REST API-frameworks • CLI-tools • Jupyter-integratie • Productie-implementatiepatronen

**Voorbeeld**: [Foundry Tools Framework](./samples/10/README.md)

**Duur**: 4-5 uur | **Niveau**: Expert

## Vereisten

### Systeemeisen
- **Besturingssysteem**: Windows 11 (22H2 of later)
- **Geheugen**: 16GB RAM (32GB aanbevolen voor grotere modellen)
- **Opslag**: 50GB vrije ruimte voor modelcaching
- **Hardware**: NPU-apparaat aanbevolen (Copilot+ PC), GPU optioneel
- **Netwerk**: Snelle internetverbinding voor initiële modeldownloads

### Ontwikkelomgeving
- Visual Studio Code met AI Toolkit-extensie
- Python 3.10+ en pip
- Git voor versiebeheer
- PowerShell of Command Prompt
- Azure CLI (optioneel voor cloudintegratie)

### Kennisvereisten
- Basiskennis van AI/ML-concepten
- Bekendheid met de command line
- Basiskennis van Python-programmering
- REST API-concepten
- Basiskennis van prompting en modelinferentie

## Module Tijdlijn

**Totale geschatte tijd**: 30-38 uur

| Sessie | Focusgebied | Voorbeelden | Tijd | Complexiteit |
|--------|-------------|-------------|------|-------------|
|  1 | Setup & Basis | 01, 02, 03 | 2-3 uur | Beginner |
|  2 | AI-oplossingen | 04 | 2-3 uur | Gemiddeld |
|  3 | Open Source | 05 | 2-3 uur | Gemiddeld |
|  4 | Geavanceerde Modellen | 06 | 3-4 uur | Geavanceerd |
|  5 | AI-agents | 05, 09 | 3-4 uur | Geavanceerd |
|  6 | Bedrijfstools | 06, 10 | 3-4 uur | Expert |
|  7 | Directe API-integratie | 07 | 2-3 uur | Gemiddeld |
|  8 | Windows 11 Chat App | 08 | 3-4 uur | Geavanceerd |
|  9 | Geavanceerde Multi-Agent | 09 | 4-5 uur | Expert |
| 10 | Tools Framework | 10 | 4-5 uur | Expert |

## Belangrijke bronnen

**Officiële documentatie:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Broncode en officiële voorbeelden
- [Azure AI Foundry Documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Complete installatie- en gebruiksgids
- [Model Mondays Series](https://aka.ms/model-mondays) - Wekelijkse modelhoogtepunten en tutorials

**Community & Ondersteuning:**
- [Foundry Local Discussies](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A en functieverzoeken
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Laatste nieuws en best practices

## Leerresultaten

Na het voltooien van deze module ben je in staat om:

### Technische beheersing
- **Implementeer en beheer**: Foundry Local-installaties in ontwikkel- en productieomgevingen
- **Integreer modellen**: Werk naadloos met diverse modelfamilies van Microsoft, Hugging Face en gemeenschapsbronnen
- **Bouw toepassingen**: Creëer productieklare AI-toepassingen met geavanceerde functies en optimalisaties
- **Ontwikkel agents**: Implementeer geavanceerde AI-agents met grounding, redenering en toolintegratie

### Strategisch inzicht
- **Architectuurkeuzes**: Maak weloverwogen beslissingen tussen lokale en cloudimplementatie
- **Prestatieoptimalisatie**: Optimaliseer inferentieprestaties voor verschillende hardwareconfiguraties
- **Bedrijfsopschaling**: Ontwerp toepassingen die schalen van lokale prototypes naar bedrijfsimplementaties
- **Privacy en beveiliging**: Implementeer privacybeschermende AI-oplossingen met lokale inferentie

### Innovatiecapaciteiten
- **Snelle prototyping**: Bouw en test AI-toepassingsconcepten snel met alle 10 voorbeeldpatronen
- **Community-integratie**: Maak gebruik van open-source modellen en draag bij aan het ecosysteem
- **Geavanceerde patronen**: Implementeer cutting-edge AI-patronen zoals RAG, agents en toolintegratie
- **Frameworkbeheersing**: Expertintegratie met LangChain, Semantic Kernel, Chainlit en Electron
- **Productie-implementatie**: Implementeer schaalbare AI-oplossingen van lokale prototypes naar bedrijfsomgevingen
- **Toekomstbestendige ontwikkeling**: Bouw toepassingen die klaar zijn voor opkomende AI-technologieën en -patronen

## Aan de slag

1. **Omgevingsinstelling**: Zorg voor Windows 11 met aanbevolen hardware (zie vereisten)
2. **Installeer Foundry Local**: Volg sessie 1 voor volledige installatie en configuratie
3. **Voer voorbeeld 01 uit**: Begin met basis REST API-integratie om de installatie te verifiëren
4. **Werk door de voorbeelden**: Voltooi voorbeelden 01-10 voor uitgebreide beheersing

## Successtatistieken

Volg je voortgang door alle 10 uitgebreide voorbeelden:

### Basisniveau (Voorbeelden 01-03)
- [ ] Foundry Local succesvol geïnstalleerd en geconfigureerd
- [ ] REST API-integratie voltooid (Voorbeeld 01)
- [ ] OpenAI SDK-compatibiliteit geïmplementeerd (Voorbeeld 02)
- [ ] Modelontdekking en benchmarking uitgevoerd (Voorbeeld 03)

### Toepassingsniveau (Voorbeelden 04-06)
- [ ] Minimaal 4 verschillende modelfamilies geïmplementeerd en uitgevoerd
- [ ] Functionele RAG-chattoepassing gebouwd (Voorbeeld 04)
- [ ] Multi-agent orkestratiesysteem gecreëerd (Voorbeeld 05)
- [ ] Intelligente modelroutering geïmplementeerd (Voorbeeld 06)

### Geavanceerd integratieniveau (Voorbeelden 07-10)
- [ ] Productieklaar API-client gebouwd (Voorbeeld 07)
- [ ] Windows 11 native chattoepassing ontwikkeld (Voorbeeld 08)
- [ ] Geavanceerd multi-agent systeem geïmplementeerd (Voorbeeld 09)
- [ ] Uitgebreid toolsframework gecreëerd (Voorbeeld 10)

### Beheersingsindicatoren
- [ ] Alle 10 voorbeelden succesvol uitgevoerd zonder fouten
- [ ] Minimaal 3 voorbeelden aangepast voor specifieke gebruiksscenario's
- [ ] Minimaal 2 voorbeelden geïmplementeerd in productieachtige omgevingen
- [ ] Verbeteringen of uitbreidingen bijgedragen aan voorbeeldcode
- [ ] Foundry Local-patronen geïntegreerd in persoonlijke/professionele projecten

## Snelle startgids - Alle 10 voorbeelden

### Omgevingsinstelling (Vereist voor alle voorbeelden)

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

### Kernbasisvoorbeelden (01-06)

**Voorbeeld 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Voorbeeld 02: OpenAI SDK Integratie**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Voorbeeld 03: Modelontdekking & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Voorbeeld 04: Chainlit RAG-toepassing**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Voorbeeld 05: Multi-Agent Orchestratie**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Voorbeeld 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Geavanceerde integratievoorbeelden (07-10)

**Voorbeeld 07: Direct API Client**
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

**Voorbeeld 08: Windows 11 Chat-toepassing**
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

**Voorbeeld 09: Geavanceerd Multi-Agent Systeem**
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

**Voorbeeld 10: Foundry Tools Framework**
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

### Veelvoorkomende problemen oplossen

**Foundry Local verbindingsfouten**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemen met modelladen**
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

**Afhankelijkheidsproblemen**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Samenvatting
Deze module vertegenwoordigt de nieuwste ontwikkelingen op het gebied van edge AI, waarbij de enterprise-grade tools van Microsoft worden gecombineerd met de flexibiliteit en innovatie van het open-source ecosysteem. Door Foundry Local volledig te beheersen via alle 10 uitgebreide voorbeelden, sta je aan de voorhoede van AI-toepassingsontwikkeling.

**Volledig leertraject:**
- **Basis** (Voorbeelden 01-03): API-integratie en modelbeheer
- **Toepassingen** (Voorbeelden 04-06): RAG, agents en intelligente routering
- **Geavanceerd** (Voorbeelden 07-10): Productiekaders en bedrijfsintegratie

Voor Azure OpenAI-integratie (Sessie 2), raadpleeg de README-bestanden van de afzonderlijke voorbeelden voor vereiste omgevingsvariabelen en API-versie-instellingen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.