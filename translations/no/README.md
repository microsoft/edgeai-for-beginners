# EdgeAI for nybegynnere 


![Kursforsidebilde](../../translated_images/no/cover.eb18d1b9605d754b.webp)

[![GitHub bidragsytere](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Følg disse trinnene for å komme i gang med å bruke disse ressursene:

1. **Fork repositoriet**: Klikk [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klone repositoriet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bli med i Azure AI Foundry Discord og møt eksperter og andre utviklere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Flerspråklig støtte

#### Støttet via GitHub Action (Automatisk og alltid oppdatert)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](./README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Foretrekker du å klone lokalt?**

> Dette repositoriet inkluderer 50+ språkoversettelser som øker nedlastingsstørrelsen betydelig. For å klone uten oversettelser, bruk sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dette gir deg alt du trenger for å fullføre kurset med mye raskere nedlasting.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Hvis du ønsker at flere oversettelses språk skal støttes, er de listet opp [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduksjon

Velkommen til **EdgeAI for nybegynnere** – din omfattende reise inn i den transformative verden av Edge kunstig intelligens. Dette kurset bygger bro mellom kraftfulle AI-muligheter og praktisk, virkelighetsnær distribusjon på edge-enheter, og gir deg mulighet til å utnytte AI sitt potensial direkte der data genereres og beslutninger må tas.

### Hva du vil mestre

Dette kurset tar deg fra grunnleggende konsepter til produksjonsklare implementeringer, med fokus på:
- **Små språkmodeller (SLM)** optimalisert for edge-distribusjon
- **Maskinvarebevisst optimalisering** på tvers av ulike plattformer
- **Sanntids inferens** med personvernbevarende muligheter
- **Produksjonsdistribusjonsstrategier** for bedriftsapplikasjoner

### Hvorfor EdgeAI er viktig

Edge AI representerer et paradigmeskifte som adresserer kritiske moderne utfordringer:
- **Personvern og sikkerhet**: Behandle sensitiv data lokalt uten eksponering for skyen
- **Sanntidsprestasjon**: Eliminere nettverksforsinkelse for tidskritiske applikasjoner
- **Kostnadseffektivitet**: Reduserer båndbredde- og skyberegningskostnader
- **Robuste operasjoner**: Oppretthold funksjonalitet under nettverksavbrudd
- **Regulatorisk samsvar**: Møt krav til datasuverenitet

### Edge AI

Edge AI refererer til kjøring av AI-algoritmer og språkmodeller lokalt på maskinvare, nær der data genereres uten å være avhengig av skyressurser for inferens. Det reduserer forsinkelse, forbedrer personvern og muliggjør sanntidsbeslutninger.

### Kjerneprinsipper:
- **Inferens på enheten**: AI-modeller kjører på edge-enheter (telefoner, rutere, mikrokontrollere, industrielle PC-er)
- **Offline evne**: Fungerer uten kontinuerlig internettforbindelse
- **Lav forsinkelse**: Umiddelbare svar egnet for sanntidssystemer
- **Datasuverenitet**: Beholder sensitiv data lokalt, forbedrer sikkerhet og samsvar

### Små språkmodeller (SLM)

SLMer som Phi-4, Mistral-7B og Gemma er optimaliserte versjoner av større LLMer — trent eller destillert for:
- **Redusert minneavtrykk**: Effektiv bruk av begrenset minne på edge-enheter
- **Lavere beregningsbehov**: Optimalisert for CPU- og edge GPU-ytelse
- **Raskere oppstartstider**: Kjapp initialisering for responsivrike applikasjoner

De frigjør kraftige NLP-muligheter samtidig som de møter begrensningene til:
- **Innbyggede systemer**: IoT-enheter og industrielle kontrollere
- **Mobile enheter**: Smarttelefoner og nettbrett med offline funksjonalitet
- **IoT-enheter**: Sensorer og smarte enheter med begrensede ressurser
- **Edge-servere**: Lokale prosesseringsenheter med begrensede GPU-ressurser
- **Personlige datamaskiner**: Desktop- og laptopdistribusjonsscenarier

## Kursmoduler og navigasjon

| Modul | Emne | Fokusområde | Nøkkelinnhold | Nivå | Varighet |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduksjon til EdgeAI](./introduction.md) | Grunnlag & kontekst | EdgeAI Oversikt • Industriapplikasjoner • SLM Introduksjon • Læringsmål | Nybegynner | 1-2 t |
| [📚 01](../../Module01) | [EdgeAI Grunnleggende](./Module01/README.md) | Sky vs Edge AI sammenligning | EdgeAI Grunnleggende • Virkelige eksempler • Implementeringsguide • Edge Distribusjon | Nybegynner | 3-4 t |
| [🧠 02](../../Module02) | [SLM Modellgrunnlag](./Module02/README.md) | Modellfamilier & arkitektur | Phi-familien • Qwen-familien • Gemma-familien • BitNET • μModel • Phi-Silica | Nybegynner | 4-5 t |
| [🚀 03](../../Module03) | [SLM Distribusjonspraksis](./Module03/README.md) | Lokal & sky-distribusjon | Avansert læring • Lokalt miljø • Sky-distribusjon | Middels | 4-5 t |
| [⚙️ 04](../../Module04) | [Verktøykasse for modelloptimalisering](./Module04/README.md) | Optimalisering på tvers av plattformer | Introduksjon • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbeidsflytsyntese | Middels | 5-6 t |
| [🔧 05](../../Module05) | [SLMOps Produksjon](./Module05/README.md) | Produksjonsdrift | SLMOps Introduksjon • Modell-destillering • Finjustering • Produksjonsdistribusjon | Avansert | 5-6 t |
| [🤖 06](../../Module06) | [AI Agenter & Funksjonsanrop](./Module06/README.md) | Agent-rammeverk & MCP | Agentintroduksjon • Funksjonsanrop • Modellkontekstprotokoll | Avansert | 4-5 t |
| [💻 07](../../Module07) | [Plattformimplementering](./Module07/README.md) | Tverrplattformeksempler | AI-verktøykasse • Foundry Local • Windows-utvikling | Avansert | 3-4 t |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Produksjonsklare eksempler | Eksempelsapplikasjoner (se detaljer nedenfor) | Ekspert | 8-10 t |

### 🏭 **Modul 08: Eksempelsapplikasjoner**

- [01: REST Chat Hurtigstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK-integrasjon](./Module08/samples/02/README.md)
- [03: Modelloppdagelse & benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG-applikasjon](./Module08/samples/04/README.md)
- [05: Multi-agent orkestrering](./Module08/samples/05/README.md)
- [06: Models-as-Tools Ruting](./Module08/samples/06/README.md)
- [07: Direkte API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat-app](./Module08/samples/08/README.md)
- [09: Avansert multi-agent system](./Module08/samples/09/README.md)
- [10: Foundry verktøy-rammeverk](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk læringssti**

Omfattende praktiske workshop-materialer med produksjonsklare implementeringer:

- **[Workshop Guide](./Workshop/Readme.md)** - Fullstendige læringsmål, resultater og ressursnavigasjon
- **Python-eksempler** (6 økter) - Oppdatert med beste praksis, feilhåndtering og omfattende dokumentasjon
- **Jupyter-notatbøker** (8 interaktive) - Trinnvise veiledninger med benchmarker og ytelsesovervåking
- **Sesiionsguider** - Detaljerte markdown-veiledninger for hver workshop-økt
- **Valideringsverktøy** - Skript for å verifisere kodekvalitet og kjøre røyktester

**Hva du vil bygge:**
- Lokale AI-chat-applikasjoner med strømmestøtte
- RAG-pipelines med kvalitetsvurdering (RAGAS)
- Benchmarking og sammenligning av multimodeller
- Multi-agent orkestreringssystemer
- Intelligente modellrutingssystemer med oppgavebasert valg

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Bygg en AI-drevet podcast-produksjonspipeline fra bunnen av! Denne immersive workshopen lærer deg å lage et komplett multi-agent system som forvandler ideer til profesjonelle podkastepisoder.
**[🎬 Start AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Din oppgave**: Lanser "Future Bytes" — en teknologipodcast drevet helt av AI-agenter du bygger selv. Ingen skytjenester, ingen API-kostnader — alt kjører lokalt på din maskin.

**Hva gjør dette unikt:**
- **🤖 Ekte multi-agent orkestrering** - Bygg spesialiserte AI-agenter som forsker, skriver og produserer lyd
- **🎯 Komplett produksjonspipeline** - Fra temautvelgelse til endelig podcast-lyd
- **💻 100 % lokal distribusjon** - Bruker Ollama og lokale modeller (Qwen-3-8B) for full personvern og kontroll
- **🎤 Tekst-til-tale-integrasjon** - Gjør skript om til naturlig lydende samtaler med flere talere
- **✋ Human-in-the-loop arbeidsflyter** - Godkjenningsporter sikrer kvalitet samtidig som automatisering opprettholdes

**Tre-akt læringsreise:**

| Akt | Fokus | Viktige ferdigheter | Varighet |
|-----|-------|---------------------|----------|
| **[Akt 1: Møt AI-assistentene dine](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Bygg din første AI-agent | Verktøyintegrasjon • Nettsøk • Problemløsning • Agentisk resonnering | 2-3 t |
| **[Akt 2: Sett sammen produksjonsteamet ditt](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrer flere agenter | Teamkoordinering • Godkjenningsflyter • DevUI-grensesnitt • Menneskelig tilsyn | 3-4 t |
| **[Akt 3: Gi podcasten liv](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generer podkast-lyd | Tekst-til-tale • Flere talere-syntese • Langformet lyd • Full automatikk | 2-3 t |

**Brukte teknologier:**
- **Microsoft Agent Framework** - Multi-agent orkestrering og koordinering
- **Ollama** - Lokal AI-modell-runtime (ingen sky nødvendig)
- **Qwen-3-8B** - Åpen kildekode språkmodell optimalisert for agentiske oppgaver
- **Tekst-til-tale-APIer** - Naturlig stemmesyntese for podkastgenerering

**Maskinvarestøtte:**
- ✅ **CPU-modus** - Fungerer på enhver moderne datamaskin (8 GB+ RAM anbefalt)
- 🚀 **GPU-akselerasjon** - Betydelig raskere inferens med NVIDIA/AMD GPUer
- ⚡ **NPU-støtte** - Neste generasjon nevral prosesseringsenhetsakselerasjon

**Perfekt for:**
- Utviklere som lærer multi-agent AI-systemer
- Alle interesserte i AI-automatisering og arbeidsflyter
- Innholdsprodusenter som utforsker AI-assistert produksjon
- Studenter som studerer praktiske AI-orkestreringsmønstre

**Start byggingen**: [🎙️ AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Læringsvei oppsummering**
- **Total varighet**: 36-45 timer
- **Nybegynnervei**: Moduler 01-02 (7-9 timer)  
- **Mellomliggende vei**: Moduler 03-04 (9-11 timer)
- **Avansert vei**: Moduler 05-07 (12-15 timer)
- **Ekspertvei**: Modul 08 (8-10 timer)

## Hva du vil bygge

### 🎯 Kjernekompetanser
- **Edge AI-arkitektur**: Design lokal-først AI-systemer med skyintegrasjon
- **Modelloptimalisering**: Kvantiser og komprimer modeller for edge-distribusjon (85 % hastighetsøkning, 75 % størrelsesreduksjon)
- **Multi-plattform distribusjon**: Windows, mobil, innebygde og sky-kant hybride systemer
- **Produksjonsoperasjoner**: Overvåkning, skalering og vedlikehold av edge AI i produksjon

### 🏗️ Praktiske prosjekter
- **Foundry Local chat-apper**: Windows 11 native-applikasjon med modellveksling
- **Multi-agent systemer**: Koordinator med spesialistagenter for komplekse arbeidsflyter  
- **RAG-applikasjoner**: Lokal dokumentprosessering med vektorsøk
- **Modellrutere**: Intelligent valg mellom modeller basert på oppgaveanalyse
- **API-rammeverk**: Produksjonsklare klienter med strømming og helsesjekk
- **Tverrplattformverktøy**: LangChain/Semantic Kernel integrasjonsmønstre

### 🏢 Bransjeapplikasjoner
**Produksjon** • **Helsevesen** • **Autonome kjøretøy** • **Smartere byer** • **Mobilapper**

## Rask start

**Anbefalt læringsvei** (20-30 timer totalt):

0. **📖 Introduksjon** ([Introduction.md](./introduction.md)): EdgeAI-grunnlag + bransjekontekst + læringsrammeverk
1. **📚 Grunnlag** (Moduler 01-02): EdgeAI-konsepter + SLM-modellfamilier
2. **⚙️ Optimalisering** (Moduler 03-04): Distribusjon + kvantiseringsrammeverk  
3. **🚀 Produksjon** (Moduler 05-06): SLMOps + AI-agenter + funksjonskall
4. **💻 Implementering** (Moduler 07-08): Plattformeksempler + Foundry Local verktøykasse

Hver modul inkluderer teori, praktiske øvelser og produksjonsklare kodeeksempler.

## Karrierepåvirkning

**Tekniske roller**: EdgeAI løsningsarkitekt • ML-ingeniør (Edge) • IoT AI-utvikler • Mobil AI-utvikler

**Bransjesektorer**: Produksjon 4.0 • Helse-teknologi • Autonome systemer • FinTech • Forbrukerelektronikk

**Porteføljeprosjekter**: Multi-agent systemer • Produksjons-RAG-apper • Tverrplattform distribusjon • Ytelsesoptimalisering

## Repositorium-struktur

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

## Kurs høydepunkter

✅ **Progressiv læring**: Teori → Praksis → Produksjonsdistribusjon  
✅ **Reelle casestudier**: Microsoft, Japan Airlines, bedriftsimplementeringer  
✅ **Praktiske eksempler**: 50+ eksempler, 10 omfattende Foundry Local demoer  
✅ **Ytelsesfokus**: 85 % hastighetsforbedringer, 75 % størrelsesreduksjoner  
✅ **Multi-plattform**: Windows, mobil, innebygd, sky-kant hybrid  
✅ **Produksjonsklar**: Overvåkning, skalering, sikkerhet, samsvarsrammeverk

📖 **[Studieveiledning tilgjengelig](STUDY_GUIDE.md)**: Strukturert 20-timers læringsvei med tidsallokeringsveiledning og egenvurderingsverktøy.

---

**EdgeAI representerer fremtiden for AI-distribusjon**: lokal-først, personvernbevarende og effektiv. Mestre disse ferdighetene for å bygge neste generasjon intelligente applikasjoner.

## Andre kurs

Vårt team produserer flere kurs! Sjekk ut:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for nybegynnere](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for nybegynnere](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for nybegynnere](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenter
[![AZD for nybegynnere](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for nybegynnere](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for nybegynnere](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenter for nybegynnere](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI-serie
[![Generativ AI for nybegynnere](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kjerne-læring
[![ML for nybegynnere](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for nybegynnere](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for nybegynnere](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersikkerhet for nybegynnere](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webutvikling for nybegynnere](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for nybegynnere](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-utvikling for nybegynnere](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serie
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få hjelp

Hvis du støter på problemer eller har spørsmål om å lage AI-apper, bli med i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktinnspill eller feil mens du bygger, besøk:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->