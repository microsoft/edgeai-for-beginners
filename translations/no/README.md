# EdgeAI for nybegynnere 


![Course cover image](../../translated_images/no/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Følg disse trinnene for å komme i gang med disse ressursene:

1. **Fork Repositoryet**: Klikk [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klon Repositoryet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bli med i Azure AI Foundry Discord og møt eksperter og medutviklere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Flerspråklig støtte

#### Støttet via GitHub Action (Automatisert og alltid oppdatert)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](./README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Foretrekker du å klone lokalt?**

> Dette repositoryet inkluderer 50+ språkoversettelser som betydelig øker nedlastingsstørrelsen. For å klone uten oversettelser, bruk sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dette gir deg alt du trenger for å fullføre kurset med mye raskere nedlasting.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Hvis du ønsker flere støttede oversettelsesspråk, er disse listet [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduksjon

Velkommen til **EdgeAI for nybegynnere** – din omfattende reise inn i den transformerende verden av Edge Kunstig intelligens. Dette kurset bygger bro mellom kraftfulle AI-muligheter og praktisk, reell distribusjon på edge-enheter, og gir deg muligheten til å utnytte AI sitt potensial direkte der data genereres og avgjørelser må tas.

### Hva du vil mestre

Dette kurset tar deg fra grunnleggende konsepter til produksjonsklare implementeringer, og dekker:
- **Små språkmodeller (SLMs)** optimalisert for edge-distribusjon
- **Maskinvarebevisst optimalisering** på tvers av ulike plattformer
- **Sanntidsinferenz** med personvernbeskyttelse
- **Strategier for produksjonsdistribusjon** for bedriftsapplikasjoner

### Hvorfor EdgeAI er viktig

Edge AI representerer et paradigmeskift som adresserer kritiske moderne utfordringer:
- **Personvern og sikkerhet**: Behandle sensitiv data lokalt uten sky-eksponering
- **Sanntidsytelse**: Eliminere nettverksforsinkelse for tidskritiske applikasjoner
- **Kostnadseffektivitet**: Redusere båndbredde og skylagringsutgifter
- **Robust drift**: Opprettholde funksjonalitet under nettverksbrudd
- **Regulatorisk etterlevelse**: Oppfylle krav til datasuverenitet

### Edge AI

Edge AI refererer til å kjøre AI-algoritmer og språkmodeller lokalt på maskinvare, nær der data genereres uten å stole på skyressurser for inferens. Det reduserer ventetid, forbedrer personvern og muliggjør sanntidsbeslutninger.

### Kjerneprinsipper:
- **Inferens på enheten**: AI-modeller kjører på edge-enheter (telefoner, rutere, mikrokontrollere, industrielle PCer)
- **Offline kapasitet**: Fungerer uten vedvarende internett-tilkobling
- **Lav ventetid**: Umiddelbare responser egnet for sanntidssystemer
- **Datasuverenitet**: Holder sensitiv informasjon lokalt, noe som forbedrer sikkerhet og etterlevelse

### Små språkmodeller (SLMs)

SLMer som Phi-4, Mistral-7B og Gemma er optimaliserte versjoner av større LLM-er—trent eller destillert for:
- **Redusert minnebruk**: Effektiv utnyttelse av begrenset minne på edge-enheter
- **Lavere beregningsbehov**: Optimalisert for CPU- og edge-GPU-ytelse
- **Raskere oppstartstider**: Rask initialisering for responsive applikasjoner

De åpner for kraftige NLP-muligheter samtidig som de oppfyller krav til:
- **Innbygde systemer**: IoT-enheter og industrielle kontrollere
- **Mobilt utstyr**: Smarttelefoner og nettbrett med offline funksjonalitet
- **IoT-enheter**: Sensorer og smarte enheter med begrensede ressurser
- **Edge-servere**: Lokale prosesseringsenheter med begrensede GPU-ressurser
- **Personlige datamaskiner**: Desktop- og laptop-distribusjonsscenarier

## Kursmoduler og navigasjon

| Modul | Emne | Fokusområde | Viktig innhold | Nivå | Varighet |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduksjon til EdgeAI](./introduction.md) | Grunnlag og kontekst | Oversikt over EdgeAI • Bransjeapplikasjoner • SLM-introduksjon • Læringsmål | Nybegynner | 1-2 t |
| [📚 01](../../Module01) | [EdgeAI Grunnleggende](./Module01/README.md) | Sky vs Edge AI sammenligning | Grunnleggende EdgeAI • Virkelige casestudier • Implementeringsguide • Edge-distribusjon | Nybegynner | 3-4 t |
| [🧠 02](../../Module02) | [SLM modellgrunnlag](./Module02/README.md) | Modellfamilier og arkitektur | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | Nybegynner | 4-5 t |
| [🚀 03](../../Module03) | [SLM distribusjonspraksis](./Module03/README.md) | Lokal og sky-distribusjon | Avansert læring • Lokalt miljø • Sky-distribusjon | Mellomnivå | 4-5 t |
| [⚙️ 04](../../Module04) | [Modelloptimaliseringsverktøy](./Module04/README.md) | Tverrplattform optimalisering | Introduksjon • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbeidsflytssyntese | Mellomnivå | 5-6 t |
| [🔧 05](../../Module05) | [SLMOps Produksjon](./Module05/README.md) | Driftsoperasjoner | SLMOps introduksjon • Modell destillering • Finjustering • Produksjonsdistribusjon | Avansert | 5-6 t |
| [🤖 06](../../Module06) | [AI-agenter & Funksjonskalling](./Module06/README.md) | Agent-rammeverk og MCP | Agent introduksjon • Funksjonskalling • Modellkontekstprotokoll | Avansert | 4-5 t |
| [💻 07](../../Module07) | [Plattformimplementering](./Module07/README.md) | Tverrplattformeksempler | AI-verktøykasse • Foundry Local • Windows-utvikling | Avansert | 3-4 t |
| [🏭 08](../../Module08) | [Foundry Local verktøykasse](./Module08/README.md) | Produksjonsklare eksempler | Eksempelsapplikasjoner (se detaljer nedenfor) | Ekspert | 8-10 t |

### 🏭 **Modul 08: Eksempelsapplikasjoner**

- [01: REST Chat Hurtigstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK-integrasjon](./Module08/samples/02/README.md)
- [03: Modelloppdagelse og benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG-applikasjon](./Module08/samples/04/README.md)
- [05: Multi-agent orkestrering](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direkte API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat-app](./Module08/samples/08/README.md)
- [09: Avansert multi-agent system](./Module08/samples/09/README.md)
- [10: Foundry verktøy-rammeverk](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk læringssti**

Omfattende praktisk workshop-materiale med produksjonsklare implementeringer:

- **[Workshop Guide](./Workshop/Readme.md)** - Fullstendige læringsmål, resultater og ressursnavigasjon
- **Python-eksempler** (6 økter) - Oppdatert med beste praksis, feilhåndtering og omfattende dokumentasjon
- **Jupyter Notebooks** (8 interaktive) - Trinnvise veiledninger med benchmarking og ytelsesovervåking
- **Øktguider** - Detaljerte markdown-guider for hver workshop-økt
- **Valideringsverktøy** - Skript for å verifisere kodekvalitet og kjøre røyktester

**Hva du vil bygge:**
- Lokale AI-chat-applikasjoner med streamingstøtte
- RAG-rørledninger med kvalitetsvurdering (RAGAS)
- Multi-modell benchmark- og sammenligningsverktøy
- Multi-agent orkestreringssystemer
- Intelligent modellruting med oppgavebasert valg

### 🎙️ **Workshop For Agentic: Praktisk - The AI Podcast Studio**

Bygg en AI-drevet produksjonsrørledning for podcaster fra bunnen av! Denne engasjerende workshoppen lærer deg å lage et komplett multi-agent system som forvandler ideer til profesjonelle podcastepisoder.
**[🎬 Start AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Din Oppgave**: Lanser "Future Bytes" — en teknologipodcast drevet helt av AI-agenter du bygger selv. Ingen skyløsninger, ingen API-kostnader — alt kjører lokalt på din maskin.

**Hva Gjør Dette Unikt:**
- **🤖 Ekte Multi-Agent Orkestrering** - Bygg spesialiserte AI-agenter som forsker, skriver og produserer lyd
- **🎯 Fullstendig Produksjonspipeline** - Fra valg av tema til endelig podkastlyd
- **💻 100 % Lokal Distribusjon** - Bruker Ollama og lokale modeller (Qwen-3-8B) for full personvern og kontroll
- **🎤 Tekst-til-Tale Integrasjon** - Omform manus til naturlig lydende flerforeleser-samtaler
- **✋ Menneske-i-Loop Arbeidsflyter** - Godkjenningsporter sikrer kvalitet samtidig som automatisering opprettholdes

**Tre-Akts Læringsreise:**

| Akt | Fokus | Nøkkelferdigheter | Varighet |
|-----|-------|-------------------|----------|
| **[Akt 1: Møt Dine AI-assistenter](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Bygg din første AI-agent | Verktøyintegrasjon • Nett-søk • Problemløsing • Agentisk resonnering | 2-3 t |
| **[Akt 2: Sett Sammen Produksjonsteamet](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrer flere agenter | Teamkoordinasjon • Godkjenningsflyter • DevUI-grensesnitt • Menneskelig overvåkning | 3-4 t |
| **[Akt 3: Gi Liv Til Podkasten Din](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generer podkastlyd | Tekst-til-tale • Flerspiller-syntese • Langformet lyd • Full automatisering | 2-3 t |

**Teknologier Som Brukes:**
- **Microsoft Agent Framework** - Orkestrering og koordinering av multi-agenter
- **Ollama** - Lokal AI-modell runtime (ingen sky nødvendig)
- **Qwen-3-8B** - Åpen kildekode språkmodell optimalisert for agentiske oppgaver
- **Tekst-til-Tale APIer** - Naturlig stemmesyntese for podkastgenerering

**Maskinvarestøtte:**
- ✅ **CPU-modus** - Fungerer på hvilken som helst moderne datamaskin (8GB+ RAM anbefalt)
- 🚀 **GPU-akselerasjon** - Betydelig raskere inferens med NVIDIA/AMD GPUer
- ⚡ **NPU-støtte** - Neste generasjons akselerasjon med nevral prosesseringsenhet

**Perfekt For:**
- Utviklere som lærer seg multi-agent AI-systemer
- Alle som er interessert i AI-automatisering og arbeidsflyter
- Innholdsprodusenter som utforsker AI-assistert produksjon
- Studenter som studerer praktiske AI-orkestreringsmønstre

**Begynn Å Bygge**: [🎙️ The AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Læringsveiens Sammendrag**
- **Total Varighet**: 36-45 timer
- **Nybegynnerveien**: Moduler 01-02 (7-9 timer)  
- **Mellomnivåvei**: Moduler 03-04 (9-11 timer)
- **Avansert Vei**: Moduler 05-07 (12-15 timer)
- **Ekspertvei**: Modul 08 (8-10 timer)

## Hva Du Vil Bygge

### 🎯 Kjernekompetanser
- **Edge AI-arkitektur**: Design lokale-første AI-systemer med skykobling
- **Modelloptimalisering**: Kvantiser og komprimer modeller for edge-distribusjon (85 % hastighetsøkning, 75 % størrelse-reduksjon)
- **Multi-Plattform Distribusjon**: Windows, mobil, innebygd og sky-edge-hybride systemer
- **Produksjonsoperasjoner**: Overvåking, skalering og vedlikehold av edge AI i produksjon

### 🏗️ Praktiske Prosjekter
- **Foundry Local Chat Apps**: Windows 11 innfødt applikasjon med modellbytte
- **Multi-Agent Systemer**: Koordinator med spesialistagenter for komplekse arbeidsflyter  
- **RAG-applikasjoner**: Lokal dokumentbehandling med vektorsøk
- **Modellruter**: Intelligent valg mellom modeller basert på oppgaveanalyse
- **API-rammeverk**: Produksjonsklare klienter med streaming og helsesjekk
- **Tverrplattform-verktøy**: LangChain/Semantic Kernel integrasjonsmønstre

### 🏢 Industribruk
**Produksjon** • **Helsevesen** • **Autonome Kjøretøy** • **Smarte Byer** • **Mobilapper**

## Rask Start

**Anbefalt Læringsvei** (20-30 timer totalt):

0. **📖 Introduksjon** ([Introduction.md](./introduction.md)): EdgeAI-grunnlag + industrikontekst + læringsrammeverk  
1. **📚 Grunnlag** (Moduler 01-02): EdgeAI-konsepter + SLM modellfamilier  
2. **⚙️ Optimalisering** (Moduler 03-04): Distribusjon + kvantiseringsrammeverk  
3. **🚀 Produksjon** (Moduler 05-06): SLMOps + AI-agenter + funksjonskall  
4. **💻 Implementering** (Moduler 07-08): Plattformeksempler + Foundry Local verktøykasse

Hver modul inkluderer teori, praktiske øvelser og produksjonsklare kodeeksempler.

## Karriereeffekt

**Tekniske Roller**: EdgeAI-løsningsarkitekt • ML-ingeniør (Edge) • IoT AI-utvikler • Mobil AI-utvikler

**Bransjesektorer**: Produksjon 4.0 • Helse teknologi • Autonome systemer • FinTech • Forbrukerelektronikk

**Porteføljeprosjekter**: Multi-agent systemer • Produksjon RAG apper • Tverrplattform distribusjon • Ytelsesoptimalisering

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

## Kurs Høydepunkter

✅ **Progressiv Læring**: Teori → Praksis → Produksjonsdistribusjon  
✅ **Reelle Case Studier**: Microsoft, Japan Airlines, bedriftsimplementeringer  
✅ **Hands-on Eksempler**: 50+ eksempler, 10 omfattende Foundry Local demonstrasjoner  
✅ **Ytelsesfokus**: 85 % hastighetsforbedringer, 75 % størrelsesreduksjoner  
✅ **Multi-Plattform**: Windows, mobil, innebygd, sky-edge-hybrid  
✅ **Produksjonsklart**: Overvåking, skalering, sikkerhet, samsvarsrammeverk

📖 **[Studieveiledning Tilgjengelig](STUDY_GUIDE.md)**: Strukturert 20-timers læringsvei med tidallokeringsguidance og selvvurderingsverktøy.

---

**EdgeAI representerer fremtiden for AI-distribusjon**: lokal-først, personvernbevarende og effektiv. Mestre disse ferdighetene for å bygge neste generasjon intelligente applikasjoner.

## Andre Kurs

Vårt team produserer andre kurs! Sjekk ut:

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
 
### Generativ AI-serie
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kjerneopplæring
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serie
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få hjelp

Hvis du står fast eller har spørsmål om å bygge AI-apper, bli med på:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktfeedback eller opplever feil under utvikling, besøk:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi tar ikke ansvar for eventuelle misforståelser eller feiltolkninger som følge av bruken av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->