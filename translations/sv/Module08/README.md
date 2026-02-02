# Modul 08: Praktisk erfarenhet med Microsoft Foundry Local - Komplett utvecklarverktyg

## Översikt

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) representerar nästa generation av edge AI-utveckling och ger utvecklare kraftfulla verktyg för att bygga, distribuera och skala AI-applikationer lokalt samtidigt som en smidig integration med Azure AI Foundry bibehålls. Denna modul täcker Foundry Local från installation till avancerad agentutveckling.

**Nyckelteknologier:**
- Microsoft Foundry Local CLI och SDK
- Azure AI Foundry-integration
- Modellinferens på enheten
- Lokal modellcaching och optimering
- Agentbaserade arkitekturer

## Lärandemål

Genom att slutföra denna modul kommer du att:

- **Bemästra Foundry Local**: Installera, konfigurera och optimera för utveckling på Windows 11
- **Distribuera olika modeller**: Kör phi, qwen, deepseek och GPT-modeller lokalt med CLI-kommandon
- **Bygga produktionslösningar**: Skapa AI-applikationer med avancerad promptteknik och dataintegration
- **Utnyttja öppen källkod**: Integrera Hugging Face-modeller och bidrag från communityn
- **Utveckla AI-agenter**: Bygga intelligenta agenter med grounding och orkestreringsfunktioner
- **Implementera företagsmönster**: Skapa modulära, skalbara AI-lösningar för produktionsdistribution

## Sessionsstruktur

### [1: Kom igång med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installation, CLI-setup, modelldistribution och hårdvaruoptimering

**Nyckelämnen**: Komplett installation • CLI-kommandon • Modellcaching • Hårdvaruacceleration • Multimodell-distribution

**Exempel**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**Varaktighet**: 2-3 timmar | **Nivå**: Nybörjare

---

### [2: Bygg AI-lösningar med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avancerad promptteknik, dataintegration och molnanslutning

**Nyckelämnen**: Promptteknik • Dataintegration • Azure-arbetsflöden • Prestandaoptimering • Övervakning

**Exempel**: [Chainlit RAG Application](./samples/04/README.md)

**Varaktighet**: 2-3 timmar | **Nivå**: Mellanliggande

---

### [3: Öppen källkod med Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integration, BYOM-strategier och community-modeller

**Nyckelämnen**: Hugging Face-integration • Bring-your-own-model • Model Mondays-insikter • Community-bidrag • Modellval

**Exempel**: [Multi-Agent Orchestration](./samples/05/README.md)

**Varaktighet**: 2-3 timmar | **Nivå**: Mellanliggande

---

### [4: Utforska banbrytande modeller](./04.CuttingEdgeModels.md)
**Fokus**: LLMs vs SLMs, EdgeAI-implementering och avancerade demos

**Nyckelämnen**: Modelljämförelse • Edge vs molninferens • Phi + ONNX Runtime • Chainlit RAG-app • WebGPU-optimering

**Exempel**: [Models-as-Tools Router](./samples/06/README.md)

**Varaktighet**: 3-4 timmar | **Nivå**: Avancerad

---

### [5: Bygg AI-drivna agenter snabbt](./05.AIPoweredAgents.md)
**Fokus**: Agentarkitekturer, systemprompter, grounding och orkestrering

**Nyckelämnen**: Agentdesignmönster • Systempromptteknik • Groundingtekniker • Multi-agent-system • Produktionsdistribution

**Exempel**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**Varaktighet**: 3-4 timmar | **Nivå**: Avancerad

---

### [6: Foundry Local - Modeller som verktyg](./06.ModelsAsTools.md)
**Fokus**: Modulära AI-lösningar, företagsmässig skalning och produktionsmönster

**Nyckelämnen**: Modeller som verktyg • Distribution på enheten • SDK/API-integration • Företagsarkitekturer • Skalningsstrategier

**Exempel**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Varaktighet**: 3-4 timmar | **Nivå**: Expert

---

### [7: Direkt API-integrationsmönster](./samples/07/README.md)
**Fokus**: Ren REST API-integration utan SDK-beroenden för maximal kontroll

**Nyckelämnen**: HTTP-klientimplementering • Anpassad autentisering • Modellhälsokontroll • Strömmande svar • Produktionsfelhantering

**Exempel**: [Direct API Client](./samples/07/README.md)

**Varaktighet**: 2-3 timmar | **Nivå**: Mellanliggande

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**Fokus**: Bygga moderna, inhemska chattapplikationer med Foundry Local-integration

**Nyckelämnen**: Electron-utveckling • Fluent Design System • Inhemsk Windows-integration • Realtidsströmning • Chattgränssnittsdesign

**Exempel**: [Windows 11 Chat Application](./samples/08/README.md)

**Varaktighet**: 3-4 timmar | **Nivå**: Avancerad

---

### [9: Avancerad multi-agent orkestrering](./samples/09/README.md)
**Fokus**: Sofistikerad agentkoordinering, specialiserad uppgiftsdelegering och samarbetsbaserade AI-arbetsflöden

**Nyckelämnen**: Intelligent agentkoordinering • Funktionsanropsmönster • Kommunikation mellan agenter • Arbetsflödesorkestrering • Kvalitetssäkringsmekanismer

**Exempel**: [Advanced Multi-Agent System](./samples/09/README.md)

**Varaktighet**: 4-5 timmar | **Nivå**: Expert

---

### [10: Foundry Local som verktygsramverk](./samples/10/README.md)
**Fokus**: Verktygsfokuserad arkitektur för att integrera Foundry Local i befintliga applikationer och ramverk

**Nyckelämnen**: LangChain-integration • Semantiska kärnfunktioner • REST API-ramverk • CLI-verktyg • Jupyter-integration • Produktionsdistributionsmönster

**Exempel**: [Foundry Tools Framework](./samples/10/README.md)

**Varaktighet**: 4-5 timmar | **Nivå**: Expert

## Förkunskapskrav

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller senare)
- **Minne**: 16GB RAM (32GB rekommenderas för större modeller)
- **Lagring**: 50GB ledigt utrymme för modellcaching
- **Hårdvara**: NPU-aktiverad enhet rekommenderas (Copilot+ PC), GPU valfritt
- **Nätverk**: Snabbt internet för initiala modellnedladdningar

### Utvecklingsmiljö
- Visual Studio Code med AI Toolkit-tillägg
- Python 3.10+ och pip
- Git för versionskontroll
- PowerShell eller Kommandotolken
- Azure CLI (valfritt för molnintegration)

### Kunskapsförutsättningar
- Grundläggande förståelse för AI/ML-koncept
- Bekantskap med kommandoraden
- Grundläggande Python-programmering
- REST API-koncept
- Grundläggande kunskap om promptteknik och modellinferens

## Modulens tidslinje

**Total uppskattad tid**: 30-38 timmar

| Session | Fokusområde | Exempel | Tid | Komplexitet |
|---------|-------------|---------|-----|-------------|
|  1 | Setup & Grunder | 01, 02, 03 | 2-3 timmar | Nybörjare |
|  2 | AI-lösningar | 04 | 2-3 timmar | Mellanliggande |
|  3 | Öppen källkod | 05 | 2-3 timmar | Mellanliggande |
|  4 | Avancerade modeller | 06 | 3-4 timmar | Avancerad |
|  5 | AI-agenter | 05, 09 | 3-4 timmar | Avancerad |
|  6 | Företagsverktyg | 06, 10 | 3-4 timmar | Expert |
|  7 | Direkt API-integration | 07 | 2-3 timmar | Mellanliggande |
|  8 | Windows 11 Chattapp | 08 | 3-4 timmar | Avancerad |
|  9 | Avancerad multi-agent | 09 | 4-5 timmar | Expert |
| 10 | Verktygsramverk | 10 | 4-5 timmar | Expert |

## Viktiga resurser

**Officiell dokumentation:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Källkod och officiella exempel
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Komplett installations- och användningsguide
- [Model Mondays Series](https://aka.ms/model-mondays) - Veckovisa modellhöjdpunkter och handledningar

**Community & Support:**
- [Foundry Local Diskussioner](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A och funktionsförfrågningar
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Senaste nyheterna och bästa praxis

## Läranderesultat

Efter att ha slutfört denna modul kommer du att vara utrustad för att:

### Teknisk kompetens
- **Distribuera och hantera**: Foundry Local-installationer i utvecklings- och produktionsmiljöer
- **Integrera modeller**: Arbeta smidigt med olika modelfamiljer från Microsoft, Hugging Face och communityn
- **Bygga applikationer**: Skapa produktionsklara AI-applikationer med avancerade funktioner och optimeringar
- **Utveckla agenter**: Implementera sofistikerade AI-agenter med grounding, resonemang och verktygsintegration

### Strategisk förståelse
- **Arkitekturval**: Göra informerade val mellan lokal och molndistribution
- **Prestandaoptimering**: Optimera inferensprestanda över olika hårdvarukonfigurationer
- **Företagsskalning**: Designa applikationer som skalar från lokala prototyper till företagsdistributioner
- **Integritet och säkerhet**: Implementera integritetsbevarande AI-lösningar med lokal inferens

### Innovationsförmåga
- **Snabb prototypframställning**: Snabbt bygga och testa AI-applikationskoncept över alla 10 exempel
- **Community-integration**: Utnyttja öppen källkod och bidra till ekosystemet
- **Avancerade mönster**: Implementera banbrytande AI-mönster inklusive RAG, agenter och verktygsintegration
- **Ramverkskompetens**: Expertintegration med LangChain, Semantic Kernel, Chainlit och Electron
- **Produktionsdistribution**: Distribuera skalbara AI-lösningar från lokala prototyper till företagsmiljöer
- **Framtidsredo utveckling**: Bygga applikationer redo för framväxande AI-teknologier och mönster

## Kom igång

1. **Miljöinställning**: Säkerställ Windows 11 med rekommenderad hårdvara (se Förkunskapskrav)
2. **Installera Foundry Local**: Följ Session 1 för komplett installation och konfiguration
3. **Kör Exempel 01**: Börja med grundläggande REST API-integration för att verifiera installationen
4. **Fortsätt genom exemplen**: Slutför exempel 01-10 för omfattande kompetens

## Framgångsmått

Följ din framgång genom alla 10 omfattande exempel:

### Grundläggande nivå (Exempel 01-03)
- [ ] Installera och konfigurera Foundry Local framgångsrikt
- [ ] Slutföra REST API-integration (Exempel 01)
- [ ] Implementera OpenAI SDK-kompatibilitet (Exempel 02)
- [ ] Utföra modellupptäckt och benchmarking (Exempel 03)

### Applikationsnivå (Exempel 04-06)
- [ ] Distribuera och köra minst 4 olika modelfamiljer
- [ ] Bygga en funktionell RAG-chattapplikation (Exempel 04)
- [ ] Skapa ett multi-agent orkestreringssystem (Exempel 05)
- [ ] Implementera intelligent modellrouting (Exempel 06)

### Avancerad integrationsnivå (Exempel 07-10)
- [ ] Bygga produktionsklar API-klient (Exempel 07)
- [ ] Utveckla Windows 11 inhemsk chattapplikation (Exempel 08)
- [ ] Implementera avancerat multi-agent-system (Exempel 09)
- [ ] Skapa omfattande verktygsramverk (Exempel 10)

### Mästerskapsindikatorer
- [ ] Köra alla 10 exempel utan fel
- [ ] Anpassa minst 3 exempel för specifika användningsfall
- [ ] Distribuera 2+ exempel i produktionsliknande miljöer
- [ ] Bidra med förbättringar eller utökningar till exempelkod
- [ ] Integrera Foundry Local-mönster i personliga/professionella projekt

## Snabbstartsguide - Alla 10 exempel

### Miljöinställning (Krävs för alla exempel)

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

### Grundläggande exempel (01-06)

**Exempel 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Exempel 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Exempel 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Exempel 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Exempel 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Exempel 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Avancerade integrations-exempel (07-10)

**Exempel 07: Direct API Client**
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

**Exempel 08: Windows 11 Chat Application**
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

**Exempel 09: Advanced Multi-Agent System**
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

**Exempel 10: Foundry Tools Framework**
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

### Felsökning av vanliga problem

**Foundry Local-anslutningsfel**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problem med modellinläsning**
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

**Beroendeproblem**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Sammanfattning
Den här modulen representerar det senaste inom edge AI-utveckling och kombinerar Microsofts verktyg i företagsklass med flexibiliteten och innovationen från open source-ekosystemet. Genom att bemästra Foundry Local via alla 10 omfattande exempel kommer du att vara i framkant av AI-applikationsutveckling.

**Komplett lärandebana:**
- **Grundläggande** (Exempel 01-03): API-integrering och modellhantering
- **Applikationer** (Exempel 04-06): RAG, agenter och intelligent routing
- **Avancerat** (Exempel 07-10): Produktionsramverk och företagsintegration

För Azure OpenAI-integrering (Session 2), se README-filerna för de enskilda exemplen för nödvändiga miljövariabler och inställningar för API-version.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.