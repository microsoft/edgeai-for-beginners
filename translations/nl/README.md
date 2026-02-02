# EdgeAI voor Beginners 


![Course cover image](../../translated_images/nl/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Volg deze stappen om te beginnen met het gebruik van deze bronnen:

1. **Fork de Repository**: Klik [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone de Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Word lid van The Azure AI Foundry Discord en ontmoet experts en mede-ontwikkelaars**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Meertalige Ondersteuning

#### Ondersteund via GitHub Action (Geautomatiseerd & Altijd Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](./README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Liever lokaal clonen?**

> Deze repository bevat 50+ taalvertalingen wat de downloadgrootte significant vergroot. Om zonder vertalingen te clonen, gebruik sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dit geeft je alles wat je nodig hebt om de cursus te voltooien met een veel snellere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Als je extra vertalingen wenst, de ondersteunde talen staan [hier](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introductie

Welkom bij **EdgeAI voor Beginners** – jouw uitgebreide reis in de transformerende wereld van Edge Kunstmatige Intelligentie. Deze cursus slaat de brug tussen krachtige AI-capaciteiten en praktische, real-world implementaties op edge-apparaten, waardoor je in staat wordt gesteld om AI's potentieel direct te benutten waar data wordt gegenereerd en beslissingen genomen moeten worden.

### Wat je zult beheersen

Deze cursus neemt je mee van fundamentele concepten tot productie-klare implementaties, met onder andere:
- **Kleine taalmodellen (SLM's)** geoptimaliseerd voor edge-implementatie
- **Hardwarebewuste optimalisatie** over diverse platformen
- **Realtime inferentie** met privacybeschermende mogelijkheden
- **Strategieën voor productie-implementatie** van zakelijke applicaties

### Waarom EdgeAI belangrijk is

Edge AI vertegenwoordigt een paradigmaverschuiving die cruciale moderne uitdagingen aanpakt:
- **Privacy & Beveiliging**: Verwerk gevoelige data lokaal zonder blootstelling aan de cloud
- **Realtime Prestaties**: Elimineren van netwerkvertraging voor tijdkritische applicaties
- **Kostenefficiëntie**: Verminder bandbreedte- en cloudcomputingkosten
- **Veerkrachtige Operaties**: Behoud functionaliteit tijdens netwerkstoringen
- **Naleving van regelgeving**: Voldoe aan eisen rondom datasouvereiniteit

### Edge AI

Edge AI verwijst naar het draaien van AI-algoritmen en taalmodellen lokaal op hardware, dicht bij waar data wordt gegenereerd, zonder afhankelijk te zijn van cloudbronnen voor inferentie. Dit vermindert latentie, verhoogt privacy en maakt realtime besluitvorming mogelijk.

### Kernprincipes:
- **On-device inferentie**: AI-modellen draaien op edge-apparaten (telefoons, routers, microcontrollers, industriële pc's)
- **Offline functionaliteit**: Functioneert zonder continue internetverbinding
- **Lage latentie**: Onmiddellijke reacties geschikt voor realtime systemen
- **Datasouvereiniteit**: Houdt gevoelige data lokaal, verbetert beveiliging en naleving

### Kleine taalmodellen (SLM's)

SLM's zoals Phi-4, Mistral-7B en Gemma zijn geoptimaliseerde versies van grotere LLM's—getraind of gedistilleerd voor:
- **Verminderde geheugencapaciteit**: Efficiënt gebruik van beperkte edge-apparaatgeheugen
- **Lagere rekenbelasting**: Geoptimaliseerd voor CPU- en edge-GPU-prestaties
- **Snellere opstarttijden**: Snelle initialisatie voor responsieve applicaties

Ze ontsluiten krachtige NLP-mogelijkheden terwijl ze voldoen aan de beperkingen van:
- **Embedded systemen**: IoT-apparaten en industriële controllers
- **Mobiele apparaten**: Smartphones en tablets met offline-functionaliteit
- **IoT-apparaten**: Sensoren en slimme apparaten met beperkte bronnen
- **Edge-servers**: Lokale verwerkingsunits met beperkte GPU-bronnen
- **Persoonlijke computers**: Desktop- en laptop-implementatiescenario's

## Cursusmodules & Navigatie

| Module | Onderwerp | Focusgebied | Belangrijkste Inhoud | Niveau | Duur |
|--------|-----------|-------------|---------------------|--------|-------|
| [📖 00 ](./introduction.md) | [Introductie tot EdgeAI](./introduction.md) | Basis & Context | Overzicht EdgeAI • Industriële Toepassingen • Introductie SLM • Leerdoelen | Beginner | 1-2 uur |
| [📚 01](../../Module01) | [EdgeAI Basisprincipes](./Module01/README.md) | Cloud vs Edge AI vergelijking | EdgeAI Basisprincipes • Praktijkvoorbeelden • Implementatiehandleiding • Edge Deployment | Beginner | 3-4 uur |
| [🧠 02](../../Module02) | [SLM Model Fundamenten](./Module02/README.md) | Modelfamilies & architectuur | Phi Familie • Qwen Familie • Gemma Familie • BitNET • μModel • Phi-Silica | Beginner | 4-5 uur |
| [🚀 03](../../Module03) | [SLM Deployment Praktijk](./Module03/README.md) | Lokale & cloud implementatie | Geavanceerd Leren • Lokale Omgeving • Cloud Deployment | Gemiddeld | 4-5 uur |
| [⚙️ 04](../../Module04) | [Model Optimalisatie Toolkit](./Module04/README.md) | Cross-platform optimalisatie | Introductie • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Workflow Synthese | Gemiddeld | 5-6 uur |
| [🔧 05](../../Module05) | [SLMOps Productie](./Module05/README.md) | Productieoperaties | Introductie SLMOps • Model Distillatie • Fijnafstelling • Productie-implementatie | Gevorderd | 5-6 uur |
| [🤖 06](../../Module06) | [AI Agents & Functieoproepen](./Module06/README.md) | Agent frameworks & MCP | Introductie Agent • Functieoproepen • Model Context Protocol | Gevorderd | 4-5 uur |
| [💻 07](../../Module07) | [Platform Implementatie](./Module07/README.md) | Cross-platform voorbeelden | AI Toolkit • Foundry Local • Windows Development | Gevorderd | 3-4 uur |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Productieklare voorbeelden | Voorbeeldapplicaties (zie details hieronder) | Expert | 8-10 uur |

### 🏭 **Module 08: Voorbeeldapplicaties**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integratie](./Module08/samples/02/README.md)
- [03: Model Ontdekking & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Applicatie](./Module08/samples/04/README.md)
- [05: Multi-Agent Orkestratie](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Directe API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Geavanceerd Multi-Agent Systeem](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Hands-On Leerpad**

Uitgebreid hands-on workshopmateriaal met productieklare implementaties:

- **[Workshop Gids](./Workshop/Readme.md)** - Volledige leerdoelen, uitkomsten en bronnennavigatie
- **Python Voorbeelden** (6 sessies) - Geüpdatet met best practices, foutafhandeling en uitgebreide documentatie
- **Jupyter Notebooks** (8 interactieve) - Stap-voor-stap tutorials met benchmarks en prestatiemonitoring
- **Sessiegidsen** - Gedetailleerde markdown gidsen voor elke workshopsessie
- **Validatietools** - Scripts om codekwaliteit te verifiëren en smoke tests uit te voeren

**Wat je zult bouwen:**
- Lokale AI-chatapplicaties met streamingondersteuning
- RAG-pijplijnen met kwaliteitsbeoordeling (RAGAS)
- Multi-model benchmarking- en vergelijkingstools
- Multi-agent orkestratiesystemen
- Intelligente modelroutering met taakgebaseerde selectie

### 🎙️ **Workshop voor Agentic: Hands-On - The AI Podcast Studio**

Bouw een AI-gestuurde podcastproductiepijplijn vanaf nul! Deze intensieve workshop leert je een volledig multi-agent systeem te creëren dat ideeën transformeert in professionele podcastafleveringen.
**[🎬 Start de AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Jouw Missie**: Lanceer "Future Bytes" — een tech podcast volledig aangedreven door AI-agenten die jij zelf bouwt. Geen cloudafhankelijkheden, geen API-kosten — alles draait lokaal op jouw machine.

**Wat Dit Uniek Maakt:**
- **🤖 Echte Multi-Agent Orkestratie** - Bouw gespecialiseerde AI-agenten die onderzoeken, schrijven en audio produceren
- **🎯 Complete Productielijn** - Van onderwerpkeuze tot uiteindelijke podcast audio-uitvoer
- **💻 100% Lokale Implementatie** - Gebruikt Ollama en lokale modellen (Qwen-3-8B) voor volledige privacy en controle
- **🎤 Tekst-naar-Spraak Integratie** - Verander scripts in natuurlijk klinkende gesprekken met meerdere sprekers
- **✋ Mens-in-de-Lus Workflows** - Goedkeuringsmomenten garanderen kwaliteit terwijl automatisering behouden blijft

**Drie-Acten Leertraject:**

| Act | Focus | Kernvaardigheden | Duur |
|-----|-------|------------------|-------|
| **[Act 1: Ontmoet Je AI Assistenten](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Bouw je eerste AI-agent | Toolintegratie • Websearch • Probleemoplossing • Agent-gestuurd redeneren | 2-3 uur |
| **[Act 2: Stel Je Productieteam Samen](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestreer meerdere agenten | Teamcoördinatie • Goedkeuringsworkflows • DevUI-interface • Menselijke controle | 3-4 uur |
| **[Act 3: Breng Je Podcast tot Leven](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Genereer podcast audio | Tekst-naar-spraak • Synthese met meerdere sprekers • Lange audio • Volledige automatisering | 2-3 uur |

**Gebruikte Technologieën:**
- **Microsoft Agent Framework** - Multi-agent orkestratie en coördinatie
- **Ollama** - Lokale AI-model runtime (geen cloud nodig)
- **Qwen-3-8B** - Open-source taalmodel geoptimaliseerd voor agentgerelateerde taken
- **Tekst-naar-Spraak API's** - Natuurlijke stemsynthetisatie voor podcastproductie

**Hardware Ondersteuning:**
- ✅ **CPU Modus** - Werkt op elke moderne computer (8GB+ RAM aanbevolen)
- 🚀 **GPU Versnelling** - Veel sneller inferentie met NVIDIA/AMD GPU's
- ⚡ **NPU Ondersteuning** - Versnelling met next-generation neurale verwerkingsunits

**Perfect Voor:**
- Ontwikkelaars die multi-agent AI-systemen leren
- Iedereen geïnteresseerd in AI-automatisering en workflows
- Contentmakers die AI-geassisteerde productie verkennen
- Studenten die praktische AI-orkestratiepatronen bestuderen

**Begin met Bouwen**: [🎙️ De AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Samenvatting Leerpad**
- **Totale Duur**: 36-45 uur
- **Beginnerstraject**: Modules 01-02 (7-9 uur)  
- **Middenniveau Traject**: Modules 03-04 (9-11 uur)
- **Gevorderd Traject**: Modules 05-07 (12-15 uur)
- **Expert Traject**: Module 08 (8-10 uur)

## Wat Je Gaat Bouwen

### 🎯 Kerncompetenties
- **Edge AI Architectuur**: Ontwerp lokaal-eerst AI-systemen met cloudintegratie
- **Modeloptimalisatie**: Kwantiseren en comprimeren van modellen voor edge-implementatie (85% snelheidsverbetering, 75% volumeking)
- **Multi-Platform Implementatie**: Windows, mobiel, embedded en cloud-edge hybride systemen
- **Productieoperaties**: Monitoring, opschalen en onderhouden van edge AI in productie

### 🏗️ Praktische Projecten
- **Foundry Local Chat Apps**: Windows 11 native applicatie met model-switching
- **Multi-Agent Systemen**: Coördinator met specialistische agenten voor complexe workflows  
- **RAG Applicaties**: Lokale documentverwerking met vectorzoekfunctie
- **Model Routers**: Intelligente selectie tussen modellen op basis van taak-analyse
- **API Frameworks**: Productieklaar met streaming en health monitoring
- **Cross-Platform Tools**: Integratiepatronen met LangChain/Semantic Kernel

### 🏢 Industriële Toepassingen
**Productie** • **Gezondheidszorg** • **Autonome Voertuigen** • **Slimme Steden** • **Mobiele Apps**

## Snelle Start

**Aanbevolen Leerpad** (20-30 uur totaal):

0. **📖 Introductie** ([Introduction.md](./introduction.md)): EdgeAI basis + industrieel kader + leerframework
1. **📚 Fundament** (Modules 01-02): EdgeAI concepten + SLM modelfamilies
2. **⚙️ Optimalisatie** (Modules 03-04): Implementatie + kwantisatie frameworks  
3. **🚀 Productie** (Modules 05-06): SLMOps + AI-agenten + functie-aanroepen
4. **💻 Implementatie** (Modules 07-08): Platformvoorbeelden + Foundry Local toolkit

Elke module bevat theorie, praktische oefeningen en productieklare voorbeeldcode.

## Carrière-impact

**Technische Rollen**: EdgeAI Solution Architect • ML Engineer (Edge) • IoT AI Developer • Mobile AI Developer

**Industriesectoren**: Manufacturing 4.0 • Healthcare Tech • Autonome systemen • FinTech • Consumentenelektronica

**Portfolio Projecten**: Multi-agent systemen • Productie RAG-apps • Cross-platform implementatie • Prestatieoptimalisatie

## Repositoriumstructuur

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

## Hoogtepunten van de Cursus

✅ **Geleidelijke Leerprogressie**: Theorie → Praktijk → Productie-implementatie  
✅ **Echte Casestudies**: Microsoft, Japan Airlines, enterprise-implementaties  
✅ **Hands-on Voorbeelden**: 50+ voorbeelden, 10 uitgebreide Foundry Local demo’s  
✅ **Prestatiegericht**: 85% snelheidsverbeteringen, 75% volumevermindering  
✅ **Multi-Platform**: Windows, mobiel, embedded, cloud-edge hybride  
✅ **Productieklaar**: Monitoring, opschalen, beveiliging, compliance frameworks

📖 **[Studiegids Beschikbaar](STUDY_GUIDE.md)**: Gestructureerd 20-uur leerpad met tijdsindeling en zelfevaluatiehulpmiddelen.

---

**EdgeAI vertegenwoordigt de toekomst van AI-implementatie**: lokaal-eerst, privacybewust en efficiënt. Beheers deze vaardigheden om de volgende generatie intelligente applicaties te bouwen.

## Andere Cursussen

Ons team produceert ook andere cursussen! Bekijk:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j voor Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js voor Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain voor Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD voor Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI voor Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP voor Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents voor Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatieve AI Series
[![Generative AI voor Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Kernleren
[![ML voor Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science voor Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI voor Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity voor Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev voor Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT voor Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Ontwikkeling voor Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Hulp krijgen

Als je vastloopt of vragen hebt over het bouwen van AI-apps, sluit je aan bij:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Als je productfeedback hebt of fouten tegenkomt tijdens het bouwen, bezoek dan:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onjuistheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professioneel menselijk vertalen aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->