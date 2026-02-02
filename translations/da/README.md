# EdgeAI for Begyndere 


![Course cover image](../../translated_images/da/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Følg disse trin for at komme i gang med at bruge disse ressourcer:

1. **Fork Repositoryet**: Klik [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klon Repositoryet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Deltag i Azure AI Foundry Discord og mød eksperter og andre udviklere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Multisprogsunderstøttelse

#### Understøttet via GitHub Action (Automatiseret & Altid Opdateret)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](./README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Foretrækker du at klone lokalt?**

> Dette repository inkluderer over 50 sprogoversættelser, som væsentligt øger downloadstørrelsen. For at klone uden oversættelser, brug sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dette giver dig alt, hvad du behøver for at gennemføre kurset med en meget hurtigere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Hvis du ønsker at få understøttelse for yderligere oversættelsessprog, er de listede [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduktion

Velkommen til **EdgeAI for Beginners** – din omfattende rejse ind i den transformerende verden af Edge Kunstig Intelligens. Dette kursus bygger bro mellem kraftfulde AI-muligheder og praktisk, real-world implementering på edge-enheder, som giver dig mulighed for at udnytte AI's potentiale direkte, hvor data genereres, og beslutninger skal træffes.

### Hvad du vil mestre

Dette kursus tager dig fra grundlæggende koncepter til produktionsklare implementeringer og dækker:
- **Små sprogmodeller (SLMs)** optimeret til edge-implementering
- **Hardware-bevidst optimering** på tværs af forskellige platforme
- **Real-time inferens** med privatlivsbevarende funktioner
- **Produktionsimplementering** strategier for virksomhedsapplikationer

### Hvorfor EdgeAI er vigtigt

Edge AI repræsenterer et paradigmeskift, der adresserer kritiske moderne udfordringer:
- **Privatliv & Sikkerhed**: Behandl følsomme data lokalt uden eksponering til skyen
- **Real-time Ydeevne**: Eliminér netværksforsinkelse for tidskritiske applikationer
- **Omkostningseffektivitet**: Reducer båndbredde og cloud computing-udgifter
- **Robuste Drift**: Oprethold funktionalitet under netværksnedbrud
- **Regulatorisk Overholdelse**: Opfyld krav til datasuverænitet

### Edge AI

Edge AI betyder at køre AI-algoritmer og sprogmodeller lokalt på hardware, tæt på hvor data genereres uden at afhænge af cloud-ressourcer til inferens. Det reducerer latenstid, forbedrer privatliv og muliggør realtidsbeslutninger.

### Kerneprincipper:
- **Inferens på enheden**: AI-modeller kører på edge-enheder (telefoner, routere, mikrokontrollere, industrielle PC'er)
- **Offline kapabilitet**: Fungerer uden vedvarende internetforbindelse
- **Lav latenstid**: Øjeblikkelige svar egnet til realtidsystemer
- **Datasuverænitet**: Holder følsomme data lokalt, forbedrer sikkerhed og overholdelse

### Små sprogmodeller (SLMs)

SLMs som Phi-4, Mistral-7B, og Gemma er optimerede versioner af større LLM'er — trænet eller destilleret for:
- **Reduceret hukommelsesforbrug**: Effektiv brug af begrænset hukommelse på edge-enheder
- **Lavere beregningsbehov**: Optimeret til CPU og edge GPU-ydeevne
- **Hurtigere opstartstider**: Hurtig initialisering til responsive applikationer

De åbner for kraftfulde NLP-funktioner, samtidig med at de opfylder begrænsningerne af:
- **Indlejrede systemer**: IoT-enheder og industrielle controllere
- **Mobile enheder**: Smartphones og tablets med offline-muligheder
- **IoT-enheder**: Sensorer og smarte enheder med begrænsede ressourcer
- **Edge-servere**: Lokale behandlingsenheder med begrænsede GPU-ressourcer
- **Personlige computere**: Desktop og laptop implementeringsscenarier

## Kursusmoduler & Navigation

| Modul | Emne | Fokusområde | Central Indhold | Niveau | Varighed |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduktion til EdgeAI](./introduction.md) | Fundament & Kontekst | EdgeAI Oversigt • Brancheapplikationer • SLM Introduktion • Læringsmål | Begynder | 1-2 timer |
| [📚 01](../../Module01) | [EdgeAI Grundlæggende](./Module01/README.md) | Cloud vs Edge AI sammenligning | EdgeAI Grundlæggende • Virkelige Case Studier • Implementeringsguide • Edge Implementering | Begynder | 3-4 timer |
| [🧠 02](../../Module02) | [SLM Modelfundament](./Module02/README.md) | Modelfamilier & arkitektur | Phi Familie • Qwen Familie • Gemma Familie • BitNET • μModel • Phi-Silica | Begynder | 4-5 timer |
| [🚀 03](../../Module03) | [SLM Implementeringspraksis](./Module03/README.md) | Lokal & cloud implementering | Avanceret læring • Lokalt miljø • Cloud implementering | Mellem | 4-5 timer |
| [⚙️ 04](../../Module04) | [Modeloptimeringsværktøj](./Module04/README.md) | Tværplatform-optimering | Introduktion • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Workflow-syntese | Mellem | 5-6 timer |
| [🔧 05](../../Module05) | [SLMOps Produktion](./Module05/README.md) | Produktionsdrift | SLMOps Introduktion • Modeldestillation • Finjustering • Produktionsimplementering | Avanceret | 5-6 timer |
| [🤖 06](../../Module06) | [AI Agenter & Funktionsopkald](./Module06/README.md) | Agentrammer & MCP | Agent Introduktion • Funktionsopkald • Model Context Protocol | Avanceret | 4-5 timer |
| [💻 07](../../Module07) | [Platformimplementering](./Module07/README.md) | Tværplatform-eksempler | AI Toolkit • Foundry Local • Windows Udvikling | Avanceret | 3-4 timer |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Produktionsklare eksempler | Eksempelapplikationer (se detaljer nedenfor) | Ekspert | 8-10 timer |

### 🏭 **Modul 08: Eksempelapplikationer**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Model Discovery & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Applikation](./Module08/samples/04/README.md)
- [05: Multi-Agent Orchestration](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direct API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Avanceret Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Hands-On Læringssti**

Omfattende hands-on workshopmaterialer med produktionsklare implementeringer:

- **[Workshop Guide](./Workshop/Readme.md)** - Færdige læringsmål, resultater og ressourcenavigation
- **Python Eksempler** (6 sessioner) - Opdateret med bedste praksis, fejlhåndtering og omfattende dokumentation
- **Jupyter Notebooks** (8 interaktive) - Trin-for-trin tutorials med benchmarks og ydelsesovervågning
- **Sessionsguider** - Detaljerede markdown guider for hver workshop-session
- **Valideringsværktøjer** - Scripts til at verificere kodekvalitet og køre smoke tests

**Hvad du vil bygge:**
- Lokale AI chat-applikationer med streaming-support
- RAG pipelines med kvalitetsevaluering (RAGAS)
- Multi-model benchmarking og sammenligning værktøjer
- Multi-agent orkestrering systemer
- Intelligent modelrouting med opgavebaseret udvælgelse

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Byg en AI-drevet podcastproduktionspipeline fra bunden! Denne immersive workshop lærer dig at skabe et komplet multi-agent system, der omdanner idéer til professionelle podcast-episoder.
**[🎬 Start AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Din Mission**: Lancér "Future Bytes" — en tech-podcast udelukkende drevet af AI-agenter, som du selv bygger. Ingen cloud-afhængigheder, ingen API-omkostninger — alt kører lokalt på din maskine.

**Hvad Gør Dette Unikt:**
- **🤖 Ægte Multi-Agent Orkestrering** - Byg specialiserede AI-agenter, der forsker, skriver og producerer lyd
- **🎯 Kompletn Produktionspipeline** - Fra valg af emne til endeligt podcastlydoutput
- **💻 100% Lokal Udrulning** - Bruger Ollama og lokale modeller (Qwen-3-8B) for fuldt privatliv og kontrol
- **🎤 Tekst-til-Tale Integration** - Transformer manuskripter til naturligt klingende samtaler med flere talere
- **✋ Human-in-the-Loop Workflows** - Godkendelsesporte sikrer kvalitet samtidig med automation

**Tre-Akt Læringsrejse:**

| Akt | Fokus | Nøglefærdigheder | Varighed |
|-----|-------|------------|----------|
| **[Akt 1: Mød Dine AI Assistenter](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Byg din første AI-agent | Værktøjsintegration • Websøgning • Problemløsning • Agentisk ræsonnering | 2-3 timer |
| **[Akt 2: Saml Dit Produktionsteam](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrer flere agenter | Teamkoordinering • Godkendelsesworkflows • DevUI-interface • Menneskelig overvågning | 3-4 timer |
| **[Akt 3: Giv Din Podcast Liv](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generer podcastlyd | Tekst-til-tale • Multi-taler syntese • Langformet lyd • Fuld automation | 2-3 timer |

**Brugte Teknologier:**
- **Microsoft Agent Framework** - Multi-agent orkestrering og koordinering
- **Ollama** - Lokal AI-model runtime (ingen cloud nødvendig)
- **Qwen-3-8B** - Open-source sprogmodel optimeret til agentiske opgaver
- **Tekst-til-Tale APIs** - Naturlig stemmesyntese til podcastproduktion

**Hardwareunderstøttelse:**
- ✅ **CPU-tilstand** - Virker på enhver moderne computer (8GB+ RAM anbefalet)
- 🚀 **GPU-Acceleration** - Markant hurtigere inferens med NVIDIA/AMD GPU'er
- ⚡ **NPU Support** - Næste-generation neural processeringsenhedsacceleration

**Perfekt Til:**
- Udviklere, der lærer multi-agent AI-systemer
- Alle interesserede i AI-automatisering og workflows
- Indholdsskabere, der udforsker AI-assisteret produktion
- Studerende, der studerer praktiske AI-orkestreringsmønstre

**Begynd at Bygge**: [🎙️ The AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Læringssti Oversigt**
- **Total Varighed**: 36-45 timer
- **Begyndersti**: Moduler 01-02 (7-9 timer)  
- **Mellemsti**: Moduler 03-04 (9-11 timer)
- **Avanceret sti**: Moduler 05-07 (12-15 timer)
- **Ekspertsti**: Modul 08 (8-10 timer)

## Hvad Du Vil Bygge

### 🎯 Kernekompetencer
- **Edge AI Arkitektur**: Design lokal-først AI-systemer med cloud-integration
- **Modeloptimering**: Kvantisere og komprimere modeller til edge-udrulning (85 % hastighedsforøgelse, 75 % størrelsesreduktion)
- **Multi-Platform Udrulning**: Windows, mobil, embedded og cloud-edge hybrid systemer
- **Produktionsdrift**: Overvågning, skalering og vedligeholdelse af edge AI i produktion

### 🏗️ Praktiske Projekter
- **Foundry Local Chat Apps**: Windows 11 native applikation med modelskift
- **Multi-Agent Systemer**: Koordinator med specialistagenter til komplekse workflows  
- **RAG Applikationer**: Lokal dokumentbehandling med vektorsøgning
- **Model Routers**: Intelligent udvælgelse mellem modeller baseret på opgaveanalyse
- **API Rammer**: Produktionsklare klienter med streaming og sundhedsovervågning
- **Cross-Platform Værktøjer**: LangChain/Semantic Kernel integrationsmønstre

### 🏢 Brancheanvendelser
**Fremstilling** • **Sundhedsvæsen** • **Autonome Køretøjer** • **Smarte Byer** • **Mobile Apps**

## Hurtig Start

**Anbefalet Læringssti** (20-30 timer i alt):

0. **📖 Introduktion** ([Introduction.md](./introduction.md)): EdgeAI grundlag + branchekontekst + læringsramme
1. **📚 Grundlag** (Moduler 01-02): EdgeAI begreber + SLM modelfamilier
2. **⚙️ Optimering** (Moduler 03-04): Udrulning + kvantiseringsrammer  
3. **🚀 Produktion** (Moduler 05-06): SLMOps + AI-agenter + funktionskald
4. **💻 Implementering** (Moduler 07-08): Platformseksempler + Foundry Local værktøjskasse

Hvert modul indeholder teori, praktiske øvelser og produktionsklare kodeeksempler.

## Karrierepåvirkning

**Tekniske Roller**: EdgeAI Solutions Architect • ML Engineer (Edge) • IoT AI Developer • Mobile AI Developer

**Branchesektorer**: Manufacturing 4.0 • Healthcare Tech • Autonomous Systems • FinTech • Consumer Electronics

**Porteføljeprojekter**: Multi-agent systemer • Produktions-RAG apps • Cross-platform udrulning • Ydeevneoptimering

## Repository Struktur

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Kursus Højdepunkter

✅ **Progressiv Læring**: Teori → Praksis → Produktionsudrulning  
✅ **Ægte Case Studier**: Microsoft, Japan Airlines, virksomheders implementeringer  
✅ **Hands-on Eksempler**: 50+ eksempler, 10 omfattende Foundry Local demos  
✅ **Ydeevne Fokus**: 85 % hastighedsforbedringer, 75 % størrelsesreduktioner  
✅ **Multi-Platform**: Windows, mobil, embedded, cloud-edge hybrid  
✅ **Produktionsklar**: Overvågning, skalering, sikkerhed, compliance-rammer

📖 **[Studievejledning Tilgængelig](STUDY_GUIDE.md)**: Struktureret 20-timers læringssti med tidsallokeringsvejledning og selvvurderingsværktøjer.

---

**EdgeAI repræsenterer fremtiden for AI-udrulning**: lokal-først, privatlivsbevarende og effektiv. Mestér disse færdigheder for at bygge næste generation af intelligente applikationer.

## Andre Kurser

Vores team producerer andre kurser! Se:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenter
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI Serie
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kerne Læring
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serie
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få hjælp

Hvis du går i stå eller har spørgsmål om at bygge AI-apps, så deltag i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktfeedback eller fejl under udvikling, besøg:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på sit oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->