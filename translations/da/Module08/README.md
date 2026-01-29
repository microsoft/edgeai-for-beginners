# Modul 08: Hands-on med Microsoft Foundry Local - Komplet udviklerværktøjssæt

## Oversigt

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) repræsenterer næste generation af edge AI-udvikling og giver udviklere kraftfulde værktøjer til at bygge, implementere og skalere AI-applikationer lokalt, samtidig med at der opretholdes problemfri integration med Azure AI Foundry. Dette modul dækker Foundry Local fra installation til avanceret agentudvikling.

**Nøgleteknologier:**
- Microsoft Foundry Local CLI og SDK
- Azure AI Foundry integration
- Modelinference på enheden
- Lokal modelcaching og optimering
- Agentbaserede arkitekturer

## Læringsmål

Ved at gennemføre dette modul vil du:

- **Beherske Foundry Local**: Installere, konfigurere og optimere til udvikling på Windows 11
- **Implementere forskellige modeller**: Køre phi-, qwen-, deepseek- og GPT-modeller lokalt med CLI-kommandoer
- **Bygge produktionsløsninger**: Skabe AI-applikationer med avanceret prompt engineering og dataintegration
- **Udnytte open source-økosystemet**: Integrere Hugging Face-modeller og bidrag fra fællesskabet
- **Udvikle AI-agenter**: Bygge intelligente agenter med grounding og orkestreringsfunktioner
- **Implementere virksomhedsmønstre**: Skabe modulære, skalerbare AI-løsninger til produktionsimplementering

## Sessionstruktur

### [1: Kom godt i gang med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installation, CLI-opsætning, modelimplementering og hardwareoptimering

**Nøgleemner**: Komplet installation • CLI-kommandoer • Modelcaching • Hardwareacceleration • Multi-model implementering

**Eksempel**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**Varighed**: 2-3 timer | **Niveau**: Begynder

---

### [2: Byg AI-løsninger med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avanceret prompt engineering, dataintegration og cloud-forbindelse

**Nøgleemner**: Prompt engineering • Dataintegration • Azure workflows • Performanceoptimering • Overvågning

**Eksempel**: [Chainlit RAG Application](./samples/04/README.md)

**Varighed**: 2-3 timer | **Niveau**: Mellem

---

### [3: Open Source-modeller i Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integration, BYOM-strategier og fællesskabsmodeller

**Nøgleemner**: Hugging Face-integration • Bring-your-own-model • Model Mondays indsigt • Fællesskabsbidrag • Modelvalg

**Eksempel**: [Multi-Agent Orchestration](./samples/05/README.md)

**Varighed**: 2-3 timer | **Niveau**: Mellem

---

### [4: Udforsk banebrydende modeller](./04.CuttingEdgeModels.md)
**Fokus**: LLMs vs SLMs, EdgeAI-implementering og avancerede demoer

**Nøgleemner**: Model sammenligning • Edge vs cloud inference • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimering

**Eksempel**: [Models-as-Tools Router](./samples/06/README.md)

**Varighed**: 3-4 timer | **Niveau**: Avanceret

---

### [5: Byg AI-drevne agenter hurtigt](./05.AIPoweredAgents.md)
**Fokus**: Agentarkitekturer, systemprompter, grounding og orkestrering

**Nøgleemner**: Agent designmønstre • System prompt engineering • Grounding teknikker • Multi-agent systemer • Produktionsimplementering

**Eksempel**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**Varighed**: 3-4 timer | **Niveau**: Avanceret

---

### [6: Foundry Local - Modeller som værktøjer](./06.ModelsAsTools.md)
**Fokus**: Modulære AI-løsninger, virksomhedsskalerbarhed og produktionsmønstre

**Nøgleemner**: Modeller som værktøjer • Implementering på enheden • SDK/API integration • Virksomhedsarkitekturer • Skaleringsstrategier

**Eksempel**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Varighed**: 3-4 timer | **Niveau**: Ekspert

---

### [7: Direkte API-integrationsmønstre](./samples/07/README.md)
**Fokus**: Ren REST API-integration uden SDK-afhængigheder for maksimal kontrol

**Nøgleemner**: HTTP-klientimplementering • Brugerdefineret autentificering • Modelovervågning • Streaming-responser • Produktionsfejlhåndtering

**Eksempel**: [Direct API Client](./samples/07/README.md)

**Varighed**: 2-3 timer | **Niveau**: Mellem

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**Fokus**: Bygge moderne native chat-applikationer med Foundry Local integration

**Nøgleemner**: Electron-udvikling • Fluent Design System • Native Windows integration • Real-time streaming • Chat interface design

**Eksempel**: [Windows 11 Chat Application](./samples/08/README.md)

**Varighed**: 3-4 timer | **Niveau**: Avanceret

---

### [9: Avanceret multi-agent orkestrering](./samples/09/README.md)
**Fokus**: Sofistikeret agentkoordinering, specialiseret opgavefordeling og samarbejdende AI-workflows

**Nøgleemner**: Intelligent agentkoordinering • Funktionskaldsmønstre • Kommunikation mellem agenter • Workflow-orkestrering • Kvalitetssikringsmekanismer

**Eksempel**: [Advanced Multi-Agent System](./samples/09/README.md)

**Varighed**: 4-5 timer | **Niveau**: Ekspert

---

### [10: Foundry Local som værktøjsramme](./samples/10/README.md)
**Fokus**: Værktøjsbaseret arkitektur til integration af Foundry Local i eksisterende applikationer og rammer

**Nøgleemner**: LangChain integration • Semantic Kernel funktioner • REST API rammer • CLI værktøjer • Jupyter integration • Produktionsimplementeringsmønstre

**Eksempel**: [Foundry Tools Framework](./samples/10/README.md)

**Varighed**: 4-5 timer | **Niveau**: Ekspert

## Forudsætninger

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller nyere)
- **Hukommelse**: 16GB RAM (32GB anbefales til større modeller)
- **Lagring**: 50GB ledig plads til modelcaching
- **Hardware**: NPU-aktiveret enhed anbefales (Copilot+ PC), GPU valgfri
- **Netværk**: Højhastighedsinternet til første modeldownload

### Udviklingsmiljø
- Visual Studio Code med AI Toolkit-udvidelse
- Python 3.10+ og pip
- Git til versionskontrol
- PowerShell eller Kommandoprompt
- Azure CLI (valgfrit til cloud-integration)

### Videnforudsætninger
- Grundlæggende forståelse af AI/ML-koncepter
- Kendskab til kommandolinjen
- Grundlæggende Python-programmering
- REST API-koncepter
- Grundlæggende viden om prompting og modelinference

## Modul tidslinje

**Samlet estimeret tid**: 30-38 timer

| Session | Fokusområde | Eksempler | Tid | Kompleksitet |
|---------|-------------|-----------|-----|--------------|
|  1 | Opsætning & Grundlæggende | 01, 02, 03 | 2-3 timer | Begynder |
|  2 | AI-løsninger | 04 | 2-3 timer | Mellem |
|  3 | Open Source | 05 | 2-3 timer | Mellem |
|  4 | Avancerede modeller | 06 | 3-4 timer | Avanceret |
|  5 | AI-agenter | 05, 09 | 3-4 timer | Avanceret |
|  6 | Virksomhedsværktøjer | 06, 10 | 3-4 timer | Ekspert |
|  7 | Direkte API-integration | 07 | 2-3 timer | Mellem |
|  8 | Windows 11 Chat App | 08 | 3-4 timer | Avanceret |
|  9 | Avanceret multi-agent | 09 | 4-5 timer | Ekspert |
| 10 | Værktøjsramme | 10 | 4-5 timer | Ekspert |

## Nøgle ressourcer

**Officiel dokumentation:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kildekode og officielle eksempler
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Komplet opsætnings- og brugsvejledning
- [Model Mondays Series](https://aka.ms/model-mondays) - Ugentlige modelhøjdepunkter og tutorials

**Fællesskab & Support:**
- [Foundry Local Diskussioner](https://github.com/microsoft/Foundry-Local/discussions) - Fællesskabets Q&A og funktionsanmodninger
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Seneste nyheder og bedste praksis

## Læringsresultater

Når du har gennemført dette modul, vil du være i stand til:

### Teknisk ekspertise
- **Implementere og administrere**: Foundry Local installationer på tværs af udviklings- og produktionsmiljøer
- **Integrere modeller**: Arbejde problemfrit med forskellige modelfamilier fra Microsoft, Hugging Face og fællesskabet
- **Bygge applikationer**: Skabe produktionsklare AI-applikationer med avancerede funktioner og optimeringer
- **Udvikle agenter**: Implementere sofistikerede AI-agenter med grounding, ræsonnement og værktøjsintegration

### Strategisk forståelse
- **Arkitekturvalg**: Træffe informerede beslutninger mellem lokal vs cloud-implementering
- **Performanceoptimering**: Optimere inference-performance på tværs af forskellige hardwarekonfigurationer
- **Virksomhedsskalerbarhed**: Designe applikationer, der skalerer fra lokale prototyper til virksomhedsimplementeringer
- **Privatliv og sikkerhed**: Implementere privatlivsbevarende AI-løsninger med lokal inference

### Innovationskapaciteter
- **Hurtig prototyping**: Hurtigt bygge og teste AI-applikationskoncepter på tværs af alle 10 eksempelmønstre
- **Fællesskabsintegration**: Udnytte open source-modeller og bidrage til økosystemet
- **Avancerede mønstre**: Implementere banebrydende AI-mønstre, herunder RAG, agenter og værktøjsintegration
- **Rammemesterskab**: Ekspertintegration med LangChain, Semantic Kernel, Chainlit og Electron
- **Produktionsimplementering**: Implementere skalerbare AI-løsninger fra lokale prototyper til virksomhedssystemer
- **Fremtidsklar udvikling**: Bygge applikationer klar til fremtidens AI-teknologier og mønstre

## Kom godt i gang

1. **Miljøopsætning**: Sørg for Windows 11 med anbefalet hardware (se Forudsætninger)
2. **Installer Foundry Local**: Følg Session 1 for komplet installation og konfiguration
3. **Kør Eksempel 01**: Start med grundlæggende REST API-integration for at verificere opsætningen
4. **Fortsæt gennem eksempler**: Gennemfør eksempler 01-10 for omfattende ekspertise

## Succeskriterier

Følg din fremgang gennem alle 10 omfattende eksempler:

### Grundlæggende niveau (Eksempler 01-03)
- [ ] Installér og konfigurer Foundry Local med succes
- [ ] Fuldfør REST API-integration (Eksempel 01)
- [ ] Implementér OpenAI SDK-kompatibilitet (Eksempel 02)
- [ ] Udfør modelopdagelse og benchmarking (Eksempel 03)

### Applikationsniveau (Eksempler 04-06)
- [ ] Implementér og kør mindst 4 forskellige modelfamilier
- [ ] Byg en funktionel RAG chat-applikation (Eksempel 04)
- [ ] Skab et multi-agent orkestreringssystem (Eksempel 05)
- [ ] Implementér intelligent model-routing (Eksempel 06)

### Avanceret integrationsniveau (Eksempler 07-10)
- [ ] Byg produktionsklar API-klient (Eksempel 07)
- [ ] Udvikl Windows 11 native chat-applikation (Eksempel 08)
- [ ] Implementér avanceret multi-agent system (Eksempel 09)
- [ ] Skab omfattende værktøjsramme (Eksempel 10)

### Mesterskabsindikatorer
- [ ] Kør alle 10 eksempler uden fejl
- [ ] Tilpas mindst 3 eksempler til specifikke brugsscenarier
- [ ] Implementér 2+ eksempler i produktionslignende miljøer
- [ ] Bidrag med forbedringer eller udvidelser til eksempelkode
- [ ] Integrér Foundry Local mønstre i personlige/professionelle projekter

## Hurtig start guide - Alle 10 eksempler

### Miljøopsætning (Påkrævet for alle eksempler)

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

### Grundlæggende eksempler (01-06)

**Eksempel 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Eksempel 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Eksempel 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Eksempel 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Eksempel 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Eksempel 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Avancerede integrations-eksempler (07-10)

**Eksempel 07: Direct API Client**
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

**Eksempel 08: Windows 11 Chat Application**
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

**Eksempel 09: Advanced Multi-Agent System**
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

**Eksempel 10: Foundry Tools Framework**
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

### Fejlfinding af almindelige problemer

**Foundry Local forbindelsesfejl**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemer med modelloading**
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

**Afhængighedsproblemer**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Resumé
Dette modul repræsenterer den nyeste udvikling inden for edge AI, hvor Microsofts værktøjer i virksomhedsklasse kombineres med fleksibiliteten og innovationen fra open source-økosystemet. Ved at mestre Foundry Local gennem alle 10 omfattende eksempler vil du være i spidsen for udviklingen af AI-applikationer.

**Komplet læringssti:**
- **Grundlag** (Eksempler 01-03): API-integration og modelstyring
- **Applikationer** (Eksempler 04-06): RAG, agenter og intelligent routing
- **Avanceret** (Eksempler 07-10): Produktionsrammer og virksomhedsintegration

For Azure OpenAI-integration (Session 2), se de individuelle README-filer for de nødvendige miljøvariabler og API-versionsindstillinger.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.