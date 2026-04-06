# EdgeAI for nybegynnere


![Kurs omslagsbilde](../../translated_images/no/cover.eb18d1b9605d754b.webp)

[![GitHub-bidragsytere](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Følg disse trinnene for å komme i gang med å bruke disse ressursene:

1. **Gaffel repoet**: Klikk [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klon repoet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bli med i Azure AI Foundry Discord og møt eksperter og andre utviklere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Støtte for flere språk

#### Støttet via GitHub Action (Automatisk og alltid oppdatert)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesisk (Forenklet)](../zh-CN/README.md) | [Kinesisk (Tradisjonell, Hong Kong)](../zh-HK/README.md) | [Kinesisk (Tradisjonell, Macau)](../zh-MO/README.md) | [Kinesisk (Tradisjonell, Taiwan)](../zh-TW/README.md) | [Kroatisk](../hr/README.md) | [Tsjekkisk](../cs/README.md) | [Dansk](../da/README.md) | [Nederlandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Gresk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeriansk pidgin](../pcm/README.md) | [Norsk](./README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasil)](../pt-BR/README.md) | [Portugisisk (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumensk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)

> **Foretrekker å klone lokalt?**
>
> Dette repoet inkluderer 50+ språkoversettelser som øker nedlastingsstørrelsen betydelig. For å klone uten oversettelser, bruk sparsjekontroll:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Dette gir deg alt du trenger for å fullføre kurset med mye raskere nedlasting.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Hvis du ønsker flere støttede oversettelsesspråk, finnes de listet [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduksjon

Velkommen til **EdgeAI for nybegynnere** – din omfattende reise inn i den transformative verdenen av Edge kunstig intelligens. Dette kurset bygger bro mellom kraftige AI-muligheter og praktisk, virkelig distribusjon på kant-enheter, og gir deg evnen til å utnytte AI sitt potensiale direkte der hvor data genereres og beslutninger må tas.

### Hva du vil mestre

Dette kurset tar deg fra grunnleggende konsepter til produksjonsklare implementeringer, og dekker:
- **Små språkmodeller (SLMs)** optimalisert for kant-distribusjon
- **Maskinvarebevisst optimalisering** på tvers av ulike plattformer
- **Sanntidsinferenser** med personvernbevarende muligheter
- **Strategier for produksjonsdistribusjon** for bedriftsapplikasjoner

### Hvorfor EdgeAI er viktig

Edge AI representerer et paradigmeskifte som adresserer kritiske moderne utfordringer:
- **Personvern og sikkerhet**: Behandle sensitiv data lokalt uten eksponering mot skyen
- **Sanntidsprestasjon**: Eliminere nettverksforsinkelse for tidskritiske applikasjoner
- **Kostnadseffektivitet**: Redusere båndbredde- og skykostnader
- **Robuste operasjoner**: Opprettholde funksjonalitet under nettverksavbrudd
- **Regulatorisk samsvar**: Oppfylle krav om datasuverenitet

### Edge AI

Edge AI betyr å kjøre AI-algoritmer og språkmodeller lokalt på maskinvare, nær der data genereres, uten å stole på skyressurser for inferens. Det reduserer forsinkelse, forbedrer personvern, og muliggjør sanntidsbeslutninger.

### Kjerneprinsipper:
- **Inferens på enheten**: AI-modeller kjører på kant-enheter (telefoner, rutere, mikrokontrollere, industrielle PC-er)
- **Offline-funksjonalitet**: Fungerer uten konstant internettforbindelse
- **Lav forsinkelse**: Umiddelbare responser egnet for sanntidssystemer
- **Datasuverenitet**: Holder sensitiv data lokalt, forbedrer sikkerhet og samsvar

### Små språkmodeller (SLMs)

SLMer som Phi-4, Mistral-7B og Gemma er optimaliserte versjoner av større LLM-er—trent eller destillert for:
- **Redusert minnebruk**: Effektiv bruk av begrenset minne på kant-enheter
- **Lavere beregningsbehov**: Optimalisert for CPU og kant-GPU-ytelse
- **Raskere oppstartstid**: Kjapp initialisering for responsive applikasjoner

De låser opp kraftige NLP-funksjoner samtidig som de tilfredsstiller begrensningene til:
- **Innebygde systemer**: IoT-enheter og industrielle kontrollere
- **Mobile enheter**: Smarttelefoner og nettbrett med offline-muligheter
- **IoT-enheter**: Sensorer og smarte enheter med begrensede ressurser
- **Edge-servere**: Lokale prosesseringsenheter med begrensede GPU-ressurser
- **Personlige datamaskiner**: Stasjonær og bærbar distribusjon

## Kursmoduler og navigasjon

| Modul | Emne | Fokusområde | Nøkkelinnhold | Nivå | Varighet |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduksjon til EdgeAI](./introduction.md) | Grunnlag og kontekst | EdgeAI Oversikt • Bransjeapplikasjoner • SLM-introduksjon • Læringsmål | Nybegynner | 1-2 timer |
| [📚 01](../../Module01) | [EdgeAI Grunnprinsipper](./Module01/README.md) | Sky vs Edge AI sammenligning | EdgeAI Grunnprinsipper • Virkelige caser • Implementeringsveiledning • Edge-distribusjon | Nybegynner | 3-4 timer |
| [🧠 02](../../Module02) | [SLM Modellgrunnlag](./Module02/README.md) | Modellfamilier og arkitektur | Phi-familien • Qwen-familien • Gemma-familien • BitNET • μModel • Phi-Silica | Nybegynner | 4-5 timer |
| [🚀 03](../../Module03) | [SLM Distribusjonspraksis](./Module03/README.md) | Lokal og skybasert distribusjon | Avansert læring • Lokalt miljø • Sky-distribusjon | Mellomnivå | 4-5 timer |
| [⚙️ 04](../../Module04) | [Verktøykasse for modelloptimalisering](./Module04/README.md) | Tverrplattformoptimalisering | Innføring • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbeidsflytsyntese | Mellomnivå | 5-6 timer |
| [🔧 05](../../Module05) | [SLMOps Produksjon](./Module05/README.md) | Produksjonsoperasjoner | SLMOps introduksjon • Modelldestillasjon • Finjustering • Produksjonsdistribusjon | Avansert | 5-6 timer |
| [🤖 06](../../Module06) | [AI-agenter & Funksjonskall](./Module06/README.md) | Agentrammeverk og MCP | Agentintroduksjon • Funksjonskall • Modellkontekstprotokoll | Avansert | 4-5 timer |
| [💻 07](../../Module07) | [Plattformimplementering](./Module07/README.md) | Tverrplattformeksempler | AI-verktøykasse • Foundry Local • Windows utvikling | Avansert | 3-4 timer |
| [🏭 08](../../Module08) | [Foundry Local Verktøykasse](./Module08/README.md) | Produksjonsklare eksempler | Eksempelsøknader (se detaljer nedenfor) | Ekspert | 8-10 timer |

### 🏭 **Modul 08: Eksempelsøknader**

- [01: REST Chat Raskstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK-integrasjon](./Module08/samples/02/README.md)
- [03: Modelloppdagelse & benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG-applikasjon](./Module08/samples/04/README.md)
- [05: Multi-agent orkestrering](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direkte API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat-app](./Module08/samples/08/README.md)
- [09: Avansert multi-agent system](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk læringsvei**

Omfattende praktisk workshop-materiale med produksjonsklare implementeringer:

- **[Workshop Guide](./Workshop/Readme.md)** - Komplette læringsmål, resultater og ressursnavigasjon
- **Python-eksempler** (6 økter) - Oppdatert med beste praksis, feilhåndtering og omfattende dokumentasjon
- **Jupyter Notebooks** (8 interaktive) - Steg-for-steg veiledninger med benchmarks og ytelsesovervåkning
- **Øktveiledninger** - Detaljerte markdown-veiledninger for hver workshop-økt
- **Valideringsverktøy** - Skript for å verifisere kodekvalitet og kjøre røyktester

**Hva du vil bygge:**
- Lokale AI-chat-applikasjoner med streamingstøtte
- RAG-pipelines med kvalitetsevaluering (RAGAS)
- Multi-modell benchmarking og sammenligning
- Multi-agent orkestreringssystemer
- Intelligente modellrutere basert på oppgavevalg

### 🎙️ **Workshop For Agentic: Praktisk - AI Podcast Studio**
Bygg en AI-drevet podcastproduksjonspipeline fra bunnen av! Denne engasjerende workshoppen lærer deg å lage et komplett multi-agent system som forvandler ideer til profesjonelle podcastepisoder.

**[🎬 Start The AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Din oppgave**: Lanser "Future Bytes" — en teknologipodcast drevet helt av AI-agenter du bygger selv. Ingen skyavhengigheter, ingen API-kostnader — alt kjører lokalt på din maskin.

**Hva som gjør dette unikt:**
- **🤖 Ekte multi-agent orkestrering** - Bygg spesialiserte AI-agenter som forsker, skriver og produserer lyd
- **🎯 Komplett produksjonspipeline** - Fra valg av tema til ferdig podcastlyd
- **💻 100% Lokal distribusjon** - Bruker Ollama og lokale modeller (Qwen-3-8B) for full personvern og kontroll
- **🎤 Tekst-til-tale integrasjon** - Forvandle manus til naturlig klingende samtaler med flere stemmer
- **✋ Menneskelig kontrollpunkt i arbeidsflyter** - Godkjenningsporter sikrer kvalitet samtidig som automatiseringen bevares

**Læringsreise i tre akter:**

| Akt | Fokus | Nøkkelferdigheter | Varighet |
|-----|-------|-------------------|----------|
| **[Akt 1: Møt dine AI-assistenter](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Bygg din første AI-agent | Verktøyintegrasjon • Websøk • Problemløsning • Agentisk resonnering | 2-3 timer |
| **[Akt 2: Sett sammen ditt produksjonsteam](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrere flere agenter | Teamkoordinering • Godkjenningsflyter • DevUI-grensesnitt • Menneskelig tilsyn | 3-4 timer |
| **[Akt 3: Gi liv til podcasten din](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generer podcastlyd | Tekst-til-tale • Flerstemmesyntese • Langformat lyd • Full automatisering | 2-3 timer |

**Brukte teknologier:**
- **Microsoft Agent Framework** - Multi-agent orkestrering og koordinering
- **Ollama** - Lokalt AI-modell-runtime (ingen sky nødvendig)
- **Qwen-3-8B** - Åpen kildekode språkmodell optimalisert for agentiske oppgaver
- **Tekst-til-tale API-er** - Naturlig stemmesyntese for podcastgenerering

**Maskinvarestøtte:**
- ✅ **CPU-modus** - Fungerer på hvilken som helst moderne datamaskin (anbefalt 8GB+ RAM)
- 🚀 **GPU-akselerasjon** - Betydelig raskere inferens med NVIDIA/AMD GPUer
- ⚡ **NPU-støtte** - Neste generasjons nevral behandling akselerasjon

**Perfekt for:**
- Utviklere som lærer multi-agent AI-systemer
- Alle med interesse for AI-automatisering og arbeidsflyter
- Innholdsprodusenter som utforsker AI-assistert produksjon
- Studenter som studerer praktiske AI-orkestreringsmønstre

**Start byggingen**: [🎙️ The AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Sammendrag av læringsløype**
- **Total varighet**: 36-45 timer
- **Nybegynnerløype**: Moduler 01-02 (7-9 timer)  
- **Mellomnivåløype**: Moduler 03-04 (9-11 timer)
- **Avansert løype**: Moduler 05-07 (12-15 timer)
- **Ekspertløype**: Modul 08 (8-10 timer)

## Hva du vil bygge

### 🎯 Kjernekompetanser
- **Edge AI-arkitektur**: Design lokale AI-systemer med skyløs integrasjon
- **Modelloptimalisering**: Kvantisere og komprimere modeller for edge-distribusjon (85 % fartsgain, 75 % størrelsesreduksjon)
- **Multi-plattform distribusjon**: Windows, mobil, innebygde og sky-edge hybride systemer
- **Produksjonsoperasjoner**: Overvåking, skalering og vedlikehold av Edge AI i produksjon

### 🏗️ Praktiske prosjekter
- **Foundry Local Chat-apper**: Windows 11 native applikasjon med modellbryting
- **Multi-agent systemer**: Koordinator med spesialistagenter for komplekse arbeidsflyter  
- **RAG-applikasjoner**: Lokal dokumentbehandling med vektorsøk
- **Modellrutere**: Intelligent valg mellom modeller basert på oppgaveanalyse
- **API-rammeverk**: Produksjonsklare klienter med streaming og helsesjekk
- **Tverrplattformverktøy**: LangChain/Semantic Kernel integrasjonsmønstre

### 🏢 Industrielle anvendelser
**Produksjon** • **Helsevesen** • **Autonome kjøretøy** • **Smartere byer** • **Mobilapper**

## Rask start

**Anbefalt læringsløype** (totalt 20-30 timer):

0. **📖 Introduksjon** ([Introduction.md](./introduction.md)): EdgeAI-grunnlag + industrieffekt + læringsrammeverk  
1. **📚 Grunnlag** (Moduler 01-02): EdgeAI-konsepter + SLM-modellfamilier  
2. **⚙️ Optimalisering** (Moduler 03-04): Distribusjon + kvantiseringsrammeverk  
3. **🚀 Produksjon** (Moduler 05-06): SLMOps + AI-agenter + funksjonskalling  
4. **💻 Implementering** (Moduler 07-08): Plattformeksempler + Foundry Local verktøykasse

Hver modul inkluderer teori, praktiske øvelser og produksjonsklare kodesnutter.

## Karriereeffekt

**Tekniske roller**: EdgeAI-løsningsarkitekt • ML-ingeniør (Edge) • IoT AI-utvikler • Mobil AI-utvikler

**Bransjesektorer**: Produksjon 4.0 • Helsevesensteknologi • Autonome systemer • FinTech • Forbrukerelektronikk

**Porteføljeprosjekter**: Multi-agent systemer • Produksjons-RAG-apper • Tverrplattform distribusjon • Ytelsesoptimalisering

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

## Kurs høydepunkter

✅ **Progressiv læring**: Teori → Praksis → Produksjonsdistribusjon  
✅ **Virkelige case-studier**: Microsoft, Japan Airlines, bedriftsimplementeringer  
✅ **Praktiske eksempler**: 50+ eksempler, 10 omfattende Foundry Local demoer  
✅ **Ytelsesfokus**: 85 % raskere, 75 % mindre størrelse  
✅ **Multi-plattform**: Windows, mobil, innebygde, sky-edge hybrid  
✅ **Produksjonsklart**: Overvåking, skalering, sikkerhet, compliance rammeverk

📖 **[Studieveiledning tilgjengelig](STUDY_GUIDE.md)**: Strukturert 20-timers læringsløype med tidsallokeringsveiledning og selvvurderingsverktøy.

---

**EdgeAI representerer fremtiden for AI-distribusjon**: lokal-først, personvernbeskyttende og effektiv. Mestre disse ferdighetene for å bygge neste generasjon intelligente applikasjoner.

## Andre kurs

Vårt team produserer flere kurs! Sjekk ut:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få hjelp

Hvis du sitter fast eller har spørsmål om å bygge AI-apper, bli med:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har tilbakemeldinger på produktet eller feil under bygging, besøk:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->