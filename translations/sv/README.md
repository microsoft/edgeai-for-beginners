# EdgeAI för nybörjare


![Kursomslag](../../translated_images/sv/cover.eb18d1b9605d754b.webp)

[![GitHub-bidragsgivare](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub-ärenden](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pullförfrågningar](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Välkomna](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub-följare](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub-förgreningar](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub-stjärnor](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Följ dessa steg för att komma igång med att använda dessa resurser:

1. **Fork:a Repositoriet**: Klicka på [![GitHub-förgreningar](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klona Repositoriet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Gå med i Azure AI Foundry Discord och träffa experter och andra utvecklare**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Fler språkstöd

#### Stöds via GitHub Action (Automatiserat & Alltid uppdaterat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarska](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesiska (Förenklad)](../zh-CN/README.md) | [Kinesiska (Traditionell, Hong Kong)](../zh-HK/README.md) | [Kinesiska (Traditionell, Macau)](../zh-MO/README.md) | [Kinesiska (Traditionell, Taiwan)](../zh-TW/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Holländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Kannada](../kn/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesiska](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../pt-BR/README.md) | [Portugisiska (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (Kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (Filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)

> **Föredrar du att klona lokalt?**

> Detta repository inkluderar över 50 språköversättningar som avsevärt ökar nedladdningsstorleken. För att klona utan översättningar, använd sparsamt urval:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Detta ger dig allt du behöver för att slutföra kursen med en mycket snabbare nedladdning.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Om du önskar stöd för fler översättningsspråk finns de listade [här](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduktion

Välkommen till **EdgeAI för nybörjare** – din omfattande resa in i den transformerande världen av Edge Artificiell Intelligens. Denna kurs överbryggar gapet mellan kraftfull AI och praktisk, verklig implementering på edge-enheter, vilket ger dig möjlighet att utnyttja AI:s potential direkt där data genereras och beslut behöver fattas.

### Vad du kommer att behärska

Den här kursen tar dig från grundläggande koncept till produktionsfärdiga implementationer och täcker:
- **Små språkmodeller (SLMs)** optimerade för edge-implementering
- **Hårdvaru-medveten optimering** över olika plattformar
- **Real-tids inferens** med integritetsskyddande funktioner
- **Produktionsimplementeringsstrategier** för företagsapplikationer

### Varför EdgeAI är viktigt

Edge AI representerar ett paradigmskifte som tar itu med kritiska moderna utmaningar:
- **Privacy & Säkerhet**: Bearbeta känslig data lokalt utan exponering i molnet
- **Real-tids Prestanda**: Eliminera nätverksfördröjning för tidkritiska applikationer
- **Kostnadseffektivitet**: Minska bandbredd och molndatorutgifter
- **Robust Drift**: Behåll funktionalitet vid nätverksavbrott
- **Regulatorisk efterlevnad**: Uppfyll krav på datasuveränitet

### Edge AI

Edge AI syftar till att köra AI-algoritmer och språkmodeller lokalt på hårdvara, nära den plats där data genereras, utan att förlita sig på molnresurser för inferens. Det minskar latens, förbättrar integritet och möjliggör realtidsbeslutsfattande.

### Kärnprinciper:
- **Inferens på enheten**: AI-modeller körs på edge-enheter (telefoner, routrar, mikrokontroller, industriella datorer)
- **Offline-funktionalitet**: Fungerar utan ständig internetanslutning
- **Låg latens**: Omedelbara svar anpassade för realtidsystem
- **Datasuveränitet**: Håller känslig data lokal för bättre säkerhet och efterlevnad

### Små språkmodeller (SLMs)

SLMs som Phi-4, Mistral-7B och Gemma är optimerade versioner av större LLMs – tränade eller destillerade för:
- **Minskad minnesanvändning**: Effektiv användning av begränsat minne på edge-enheter
- **Lägre beräkningsbehov**: Optimerade för CPU och edge GPU-prestanda
- **Snabbare uppstartstider**: Snabb initiering för responsiva applikationer

De låser upp kraftfulla NLP-funktioner samtidigt som de uppfyller krav från:
- **Inbyggda system**: IoT-enheter och industriella styrsystem
- **Mobila enheter**: Smartphones och surfplattor med offlinefunktioner
- **IoT-enheter**: Sensorer och smarta enheter med begränsade resurser
- **Edge-servrar**: Lokala processorenheter med begränsade GPU-resurser
- **Persondatorer**: Scenarier för skrivbords- och laptop-implementering

## Kursmoduler & Navigering

| Modul | Ämne | Fokusområde | Nyckelinnehåll | Nivå | Varaktighet |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduktion till EdgeAI](./introduction.md) | Grundläggande & Kontext | EdgeAI Översikt • Branschapplikationer • SLM Introduktion • Lärandemål | Nybörjare | 1-2 tim |
| [📚 01](../../Module01) | [Grundläggande EdgeAI](./Module01/README.md) | Jämförelse Moln vs Edge AI | EdgeAI Grundläggande • Fallstudier från verkligheten • Implementeringsguide • Edge Deployment | Nybörjare | 3-4 tim |
| [🧠 02](../../Module02) | [SLM Modellgrunder](./Module02/README.md) | Modellfamiljer & arkitektur | Phi-familjen • Qwen-familjen • Gemma-familjen • BitNET • μModel • Phi-Silica | Nybörjare | 4-5 tim |
| [🚀 03](../../Module03) | [SLM Implementeringspraktik](./Module03/README.md) | Lokal & molnimplementation | Avancerad inlärning • Lokal miljö • Molnimplementering | Mellannivå | 4-5 tim |
| [⚙️ 04](../../Module04) | [Verktyg för optimering av modeller](./Module04/README.md) | Plattformsgemensam optimering | Introduktion • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbetsflödessyntes | Mellannivå | 5-6 tim |
| [🔧 05](../../Module05) | [SLMOps Produktion](./Module05/README.md) | Produktionsdrift | SLMOps Introduktion • Modell Destillering • Finjustering • Produktionsdistribuering | Avancerad | 5-6 tim |
| [🤖 06](../../Module06) | [AI Agenter & Funktionsanrop](./Module06/README.md) | Agentramverk & MCP | Agentintroduktion • Funktionsanrop • Modellkontextprotokoll | Avancerad | 4-5 tim |
| [💻 07](../../Module07) | [Plattformsimplementation](./Module07/README.md) | Plattformsgemensamma exempel | AI Toolkit • Foundry Lokal • Windows-utveckling | Avancerad | 3-4 tim |
| [🏭 08](../../Module08) | [Foundry Lokalt Toolkit](./Module08/README.md) | Produktionsklara exempel | Exempelapplikationer (se detaljer nedan) | Expert | 8-10 tim |

### 🏭 **Modul 08: Exempelapplikationer**

- [01: REST Chat Snabbstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Modellupptäckt & Prestandamätning](./Module08/samples/03/README.md)
- [04: Chainlit RAG Applikation](./Module08/samples/04/README.md)
- [05: Multi-Agent Orkestrering](./Module08/samples/05/README.md)
- [06: Modeller-som-Verktyg Router](./Module08/samples/06/README.md)
- [07: Direkt API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Avancerat Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Verktygsramverk](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk inlärningsväg**

Omfattande praktiskt workshopmaterial med produktionsklara implementationer:

- **[Workshop Guide](./Workshop/Readme.md)** - Kompletta lärandemål, resultat och resursnavigering
- **Pythonexempel** (6 sessioner) - Uppdaterade med bästa praxis, felhantering och omfattande dokumentation
- **Jupyter-anteckningsböcker** (8 interaktiva) - Steg-för-steg handledningar med prestandamätningar och övervakning
- **Sessionsguider** - Detaljerade markdown-guider för varje workshop-session
- **Valideringsverktyg** - Skript för att verifiera kodkvalitet och köra röktester

**Vad du kommer att bygga:**
- Lokala AI-chattapplikationer med stöd för streaming
- RAG pipelines med kvalitetsevaluering (RAGAS)
- Benchmarking och jämförelseverktyg för flera modeller
- Orkestreringssystem för multi-agent
- Intelligenta modellrouter för uppgiftsbaserad val

### 🎙️ **Workshop för Agentic: Hands-On - AI Podcast Studio**

Bygg en AI-driven podcastproduktionspipeline från grunden! Denna intensiva workshop lär dig skapa ett komplett multi-agent system som förvandlar idéer till professionella poddavsnitt.
**[🎬 Starta AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Ditt uppdrag**: Lansera "Future Bytes" — en teknikpodcast som drivs helt av AI-agenter som du bygger själv. Inga molntjänster, inga API-kostnader — allt körs lokalt på din dator.

**Vad som gör detta unikt:**
- **🤖 Äkta Multi-Agent Orkestrering** - Bygg specialiserade AI-agenter som forskar, skriver och producerar ljud
- **🎯 Komplett produktionspipeline** - Från ämnesval till slutlig podcastljudproduktion
- **💻 100 % lokal distribution** - Använder Ollama och lokala modeller (Qwen-3-8B) för fullständig integritet och kontroll
- **🎤 Text-till-tal-integration** - Förvandla manus till naturligt klingande, flerstämmiga samtal
- **✋ Människa-i-loopen-arbetsflöden** - Godkännandemekanismer säkerställer kvalitet samtidigt som automation upprätthålls

**Läranderesa i tre akter:**

| Akt | Fokus | Nyckelfärdigheter | Längd |
|-----|-------|-------------------|-------|
| **[Akt 1: Träffa dina AI-assistenter](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Skapa din första AI-agent | Verktygsintegration • Webbsökning • Problemlösning • Agent-resonemang | 2-3 tim |
| **[Akt 2: Sätt ihop ditt produktionsteam](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrera flera agenter | Teamkoordinering • Godkännandearbetsflöden • DevUI-gränssnitt • Mänsklig övervakning | 3-4 tim |
| **[Akt 3: Ge liv åt din podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generera podcastljud | Text-till-tal • Flerstämmig syntes • Långformat ljud • Fullständig automation | 2-3 tim |

**Använda teknologier:**
- **Microsoft Agent Framework** - Multi-agent orkestrering och koordinering
- **Ollama** - Lokal AI-modell-runtime (ingen molnanslutning krävs)
- **Qwen-3-8B** - Öppen källkods språkmodell optimerad för agentuppgifter
- **Text-till-tal-API:er** - Naturlig röstsyntes för podcastgenerering

**Hårdvarustöd:**
- ✅ **CPU-läge** - Fungerar på alla moderna datorer (8GB+ RAM rekommenderas)
- 🚀 **GPU-acceleration** - Betydligt snabbare inferens med NVIDIA/AMD GPU:er
- ⚡ **NPU-stöd** - Nästa generations neural processorenhets-acceleration

**Perfekt för:**
- Utvecklare som lär sig multi-agent AI-system
- Alla intresserade av AI-automation och arbetsflöden
- Innehållsskapare som utforskar AI-assisterad produktion
- Studenter som studerar praktiska AI-orkestreringsmönster

**Börja bygga**: [🎙️ AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Sammanfattning av lärväg**
- **Total längd**: 36-45 timmar
- **Nybörjarväg**: Moduler 01-02 (7-9 timmar)
- **Mellanväg**: Moduler 03-04 (9-11 timmar)
- **Avancerad väg**: Moduler 05-07 (12-15 timmar)
- **Expertväg**: Modul 08 (8-10 timmar)

## Vad du kommer att bygga

### 🎯 Kärnkompetenser
- **Edge AI-arkitektur**: Designa lokalt första AI-system med molnintegration
- **Modelloptimering**: Kvantisera och komprimera modeller för edge-distribution (85 % snabbare, 75 % mindre storlek)
- **Multi-plattformsdistribution**: Windows, mobilt, inbäddat och moln-edge hybrida system
- **Produktionsdrift**: Övervakning, skalning och underhåll av edge AI i produktion

### 🏗️ Praktiska projekt
- **Foundry Local chattappar**: Windows 11 native-app med modellväxling
- **Multi-agent-system**: Koordinator med specialistagenter för komplexa arbetsflöden
- **RAG-applikationer**: Lokal dokumentbehandling med vektorsökning
- **Modell-routning**: Intelligenta val mellan modeller baserat på uppgiftsanalys
- **API-ramverk**: Produktionsklara klienter med streaming och hälsokontroll
- **Korsplattformverktyg**: LangChain/Semantic Kernel integrationsmönster

### 🏢 Branschapplikationer
**Tillverkning** • **Sjukvård** • **Autonoma fordon** • **Smarta städer** • **Mobila appar**

## Snabbstart

**Rekommenderad lärväg** (20-30 timmar totalt):

0. **📖 Introduktion** ([Introduction.md](./introduction.md)): EdgeAI-grunder + branschkontext + lärandekoncept
1. **📚 Grundläggande** (Moduler 01-02): EdgeAI-koncept + SLM-modellfamiljer
2. **⚙️ Optimering** (Moduler 03-04): Distribution + kvantiseringsramverk
3. **🚀 Produktion** (Moduler 05-06): SLMOps + AI-agenter + funktionsanrop
4. **💻 Implementering** (Moduler 07-08): Plattformsexempel + Foundry Local-verktyg

Varje modul innehåller teori, praktiska övningar och produktionsfärdiga kodexempel.

## Karriäreffekt

**Tekniska roller**: EdgeAI Solutions Architect • ML Engineer (Edge) • IoT AI-utvecklare • Mobil AI-utvecklare

**Branscher**: Tillverkning 4.0 • Sjukvårdsteknik • Autonoma system • FinTech • Konsumentelektronik

**Portfolio-projekt**: Multi-agent-system • Produktions-RAG-appar • Korsplattformdistribuering • Prestandaoptimering

## Repositoriumstruktur

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

## Kursens höjdpunkter

✅ **Progressivt lärande**: Teori → Praktik → Produktionssättning  
✅ **Verkliga fallstudier**: Microsoft, Japan Airlines, företagsimplementeringar  
✅ **Praktiska exempel**: 50+ exempel, 10 omfattande Foundry Local-demonstrationer  
✅ **Prestandafokus**: 85 % snabbare, 75 % mindre storlek  
✅ **Multi-plattform**: Windows, mobilt, inbäddat, moln-edge hybrid  
✅ **Produktionsklart**: Övervakning, skalning, säkerhet, efterlevnadsramverk

📖 **[Studiehandledning tillgänglig](STUDY_GUIDE.md)**: Strukturerad 20-timmars lärväg med tidsfördelning och självbedömningsverktyg.

---

**EdgeAI representerar framtiden för AI-distribution**: lokalt först, integritetsskyddat och effektivt. Bemästra dessa färdigheter för att bygga nästa generations intelligenta applikationer.

## Andra kurser

Vårt team producerar fler kurser! Kolla in:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j för nybörjare](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js för nybörjare](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain för nybörjare](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenter
[![AZD för nybörjare](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI för nybörjare](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP för nybörjare](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI-agenter för nybörjare](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI-serie
[![Generativ AI för nybörjare](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kärnkunskap
[![ML för nybörjare](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science för nybörjare](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI för nybörjare](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersäkerhet för nybörjare](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webbutveckling för nybörjare](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT för nybörjare](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-utveckling för nybörjare](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serie
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få hjälp

Om du fastnar eller har några frågor om att bygga AI-appar, gå med i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Om du har produktfeedback eller fel under skapandet besök:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör anses vara den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->