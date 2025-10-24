<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f958250b0b94976c721e6cbdc541581",
  "translation_date": "2025-10-24T09:38:14+00:00",
  "source_file": "README.md",
  "language_code": "sv"
}
-->
# EdgeAI för Nybörjare

![Kursomslagsbild](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sv.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Följ dessa steg för att komma igång med dessa resurser:

1. **Forka Repositoriet**: Klicka [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klona Repositoriet**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Gå med i Azure AI Foundry Discord och träffa experter och andra utvecklare**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Stöd för flera språk

#### Stöds via GitHub Action (Automatiserat & Alltid Uppdaterat)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](./README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Om du vill ha ytterligare översättningar finns stödda språk listade [här](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduktion

Välkommen till **EdgeAI för Nybörjare** – din omfattande resa in i den transformativa världen av Edge Artificial Intelligence. Denna kurs bygger en bro mellan kraftfulla AI-funktioner och praktisk, verklig implementering på edge-enheter, vilket ger dig möjlighet att utnyttja AI:s potential direkt där data genereras och beslut behöver fattas.

### Vad du kommer att bemästra

Denna kurs tar dig från grundläggande koncept till produktionsklara implementationer och täcker:
- **Små Språkmodeller (SLMs)** optimerade för edge-implementering
- **Hårdvaruoptimering** över olika plattformar
- **Realtidsinferens** med integritetsskyddande funktioner
- **Produktionsimplementeringsstrategier** för företagsapplikationer

### Varför EdgeAI är viktigt

Edge AI representerar ett paradigmskifte som adresserar moderna utmaningar:
- **Integritet & Säkerhet**: Bearbeta känslig data lokalt utan exponering för molnet
- **Realtidsprestanda**: Eliminera nätverksfördröjning för tidskritiska applikationer
- **Kostnadseffektivitet**: Minska bandbredd och molnberäkningskostnader
- **Robusta operationer**: Upprätthåll funktionalitet under nätverksavbrott
- **Regulatorisk efterlevnad**: Uppfyll krav på datasuveränitet

### Edge AI

Edge AI innebär att köra AI-algoritmer och språkmodeller lokalt på hårdvara, nära där data genereras, utan att förlita sig på molnresurser för inferens. Det minskar fördröjning, förbättrar integritet och möjliggör beslutsfattande i realtid.

### Grundprinciper:
- **Inferens på enheten**: AI-modeller körs på edge-enheter (telefoner, routrar, mikrokontroller, industriella PC)
- **Offline-funktionalitet**: Fungerar utan konstant internetanslutning
- **Låg fördröjning**: Omedelbara svar som passar för realtidssystem
- **Datasuveränitet**: Håller känslig data lokal, förbättrar säkerhet och efterlevnad

### Små Språkmodeller (SLMs)

SLMs som Phi-4, Mistral-7B och Gemma är optimerade versioner av större LLMs—tränade eller destillerade för:
- **Minskad minnesanvändning**: Effektiv användning av begränsat minne på edge-enheter
- **Lägre beräkningskrav**: Optimerade för CPU och edge GPU-prestanda
- **Snabbare starttider**: Snabb initialisering för responsiva applikationer

De låser upp kraftfulla NLP-funktioner samtidigt som de möter begränsningarna för:
- **Inbyggda system**: IoT-enheter och industriella kontroller
- **Mobila enheter**: Smartphones och surfplattor med offline-funktioner
- **IoT-enheter**: Sensorer och smarta enheter med begränsade resurser
- **Edge-servrar**: Lokala bearbetningsenheter med begränsade GPU-resurser
- **Persondatorer**: Stationära och bärbara implementeringsscenarier

## Kursmoduler & Navigering

| Modul | Ämne | Fokusområde | Nyckelinnehåll | Nivå | Varaktighet |
|-------|------|-------------|----------------|------|-------------|
| [📖 00 ](./introduction.md) | [Introduktion till EdgeAI](./introduction.md) | Grund & Kontext | Översikt över EdgeAI • Industriella applikationer • Introduktion till SLM • Lärandemål | Nybörjare | 1-2 timmar |
| [📚 01](../../Module01) | [EdgeAI Grunder](./Module01/README.md) | Jämförelse mellan moln och Edge AI | Grunder i EdgeAI • Fallstudier från verkligheten • Implementeringsguide • Edge-implementering | Nybörjare | 3-4 timmar |
| [🧠 02](../../Module02) | [SLM Modellgrunder](./Module02/README.md) | Modelfamiljer & arkitektur | Phi-familjen • Qwen-familjen • Gemma-familjen • BitNET • μModel • Phi-Silica | Nybörjare | 4-5 timmar |
| [🚀 03](../../Module03) | [SLM Implementeringspraktik](./Module03/README.md) | Lokal & molnimplementering | Avancerat lärande • Lokal miljö • Molnimplementering | Mellanliggande | 4-5 timmar |
| [⚙️ 04](../../Module04) | [Verktyg för Modelloptimering](./Module04/README.md) | Plattformskorsande optimering | Introduktion • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbetsflödessyntes | Mellanliggande | 5-6 timmar |
| [🔧 05](../../Module05) | [SLMOps Produktion](./Module05/README.md) | Produktionsoperationer | Introduktion till SLMOps • Modelldestillation • Finjustering • Produktionsimplementering | Avancerad | 5-6 timmar |
| [🤖 06](../../Module06) | [AI-agenter & Funktionsanrop](./Module06/README.md) | Agentramverk & MCP | Introduktion till agenter • Funktionsanrop • Modellkontextprotokoll | Avancerad | 4-5 timmar |
| [💻 07](../../Module07) | [Plattformsimplementering](./Module07/README.md) | Plattformskorsande exempel | AI-verktyg • Foundry Local • Windows-utveckling | Avancerad | 3-4 timmar |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Produktionsklara exempel | Exempelapplikationer (se detaljer nedan) | Expert | 8-10 timmar |

### 🏭 **Modul 08: Exempelapplikationer**

- [01: REST Chat Snabbstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Modellupptäckt & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Applikation](./Module08/samples/04/README.md)
- [05: Multi-Agent Orkestrering](./Module08/samples/05/README.md)
- [06: Modeller-som-Verktyg Router](./Module08/samples/06/README.md)
- [07: Direkt API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Avancerat Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk Lärandebana**

Omfattande praktiska workshopmaterial med produktionsklara implementationer:

- **[Workshop Guide](./Workshop/Readme.md)** - Kompletta lärandemål, resultat och resursnavigering
- **Python Exempel** (6 sessioner) - Uppdaterade med bästa praxis, felhantering och omfattande dokumentation
- **Jupyter Notebooks** (8 interaktiva) - Steg-för-steg handledningar med benchmarking och prestandaövervakning
- **Sessionsguider** - Detaljerade markdown-guider för varje workshop-session
- **Valideringsverktyg** - Skript för att verifiera kodkvalitet och köra snabbtester

**Vad du kommer att bygga:**
- Lokala AI-chattapplikationer med streamingstöd
- RAG-pipelines med kvalitetsutvärdering (RAGAS)
- Multi-modell benchmarking och jämförelseverktyg
- Multi-agent orkestreringssystem
- Intelligenta modellroutrar med uppgiftsbaserad val

### 📊 **Sammanfattning av Lärandebanan**
- **Total Varaktighet**: 36-45 timmar
- **Nybörjarbana**: Moduler 01-02 (7-9 timmar)  
- **Mellanliggande bana**: Moduler 03-04 (9-11 timmar)
- **Avancerad bana**: Moduler 05-07 (12-15 timmar)
- **Expertbana**: Modul 08 (8-10 timmar)

## Vad du kommer att bygga

### 🎯 Kärnkompetenser
- **Edge AI Arkitektur**: Designa lokala AI-system med molnintegration
- **Modelloptimering**: Kvantisera och komprimera modeller för edge-implementering (85% snabbare, 75% mindre storlek)
- **Multi-Plattform Implementering**: Windows, mobila enheter, inbyggda system och moln-edge hybrida system
- **Produktionsdrift**: Övervakning, skalning och underhåll av edge AI i produktion

### 🏗️ Praktiska Projekt
- **Foundry Local Chat Apps**: Windows 11-native applikation med modellväxling
- **Multi-Agent Systems**: Koordinator med specialistagenter för komplexa arbetsflöden  
- **RAG-applikationer**: Lokal dokumentbearbetning med vektorsökning
- **Model Routers**: Intelligent val mellan modeller baserat på uppgiftsanalys
- **API-ramverk**: Produktionsklara klienter med streaming och hälsokontroll
- **Plattformsoberoende verktyg**: LangChain/Semantic Kernel integrationsmönster

### 🏢 Industriella Tillämpningar
**Tillverkning** • **Hälsovård** • **Autonoma fordon** • **Smarta städer** • **Mobilappar**

## Snabbstart

**Rekommenderad inlärningsväg** (totalt 20-30 timmar):

0. **📖 Introduktion** ([Introduction.md](./introduction.md)): EdgeAI-grunder + industrikontext + inlärningsramverk
1. **📚 Grundläggande** (Moduler 01-02): EdgeAI-koncept + SLM-modellfamiljer
2. **⚙️ Optimering** (Moduler 03-04): Implementering + kvantiseringsramverk  
3. **🚀 Produktion** (Moduler 05-06): SLMOps + AI-agenter + funktionsanrop
4. **💻 Implementering** (Moduler 07-08): Plattformsexempel + Foundry Local-verktyg

Varje modul innehåller teori, praktiska övningar och produktionsklara kodexempel.

## Karriärpåverkan

**Tekniska roller**: EdgeAI Lösningsarkitekt • ML-ingenjör (Edge) • IoT AI-utvecklare • Mobil AI-utvecklare

**Industrier**: Tillverkning 4.0 • Hälsoteknik • Autonoma system • FinTech • Konsumentelektronik

**Portföljprojekt**: Multi-agent system • Produktionsklara RAG-appar • Plattformsoberoende implementering • Prestandaoptimering

## Repositoriets Struktur

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

## Kursens Höjdpunkter

✅ **Progressiv inlärning**: Teori → Praktik → Produktionsimplementering  
✅ **Verkliga fallstudier**: Microsoft, Japan Airlines, företagsimplementeringar  
✅ **Praktiska exempel**: 50+ exempel, 10 omfattande Foundry Local-demonstrationer  
✅ **Prestandafokus**: 85% snabbare, 75% mindre storlek  
✅ **Plattformsoberoende**: Windows, mobil, inbyggda system, hybrid moln-edge  
✅ **Produktionsklar**: Övervakning, skalning, säkerhet, efterlevnadsramverk

📖 **[Studieguide tillgänglig](STUDY_GUIDE.md)**: Strukturerad 20-timmars inlärningsväg med tidsfördelningsråd och självbedömningsverktyg.

---

**EdgeAI representerar framtiden för AI-implementering**: lokal först, integritetsbevarande och effektiv. Bemästra dessa färdigheter för att bygga nästa generation av intelligenta applikationer.

## Andra Kurser

Vårt team producerar andra kurser! Kolla in:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### Azure / Edge / MCP / Agenter
[![AZD för Nybörjare](https://img.shields.io/badge/AZD%20för%20Nybörjare-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI för Nybörjare](https://img.shields.io/badge/Edge%20AI%20för%20Nybörjare-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP för Nybörjare](https://img.shields.io/badge/MCP%20för%20Nybörjare-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenter för Nybörjare](https://img.shields.io/badge/AI%20Agenter%20för%20Nybörjare-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI-serie
[![Generativ AI för Nybörjare](https://img.shields.io/badge/Generativ%20AI%20för%20Nybörjare-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generativ%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generativ%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generativ%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Grundläggande Inlärning
[![ML för Nybörjare](https://img.shields.io/badge/ML%20för%20Nybörjare-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science för Nybörjare](https://img.shields.io/badge/Data%20Science%20för%20Nybörjare-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI för Nybörjare](https://img.shields.io/badge/AI%20för%20Nybörjare-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersäkerhet för Nybörjare](https://img.shields.io/badge/Cybersäkerhet%20för%20Nybörjare-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webbutveckling för Nybörjare](https://img.shields.io/badge/Webbutveckling%20för%20Nybörjare-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT för Nybörjare](https://img.shields.io/badge/IoT%20för%20Nybörjare-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-utveckling för Nybörjare](https://img.shields.io/badge/XR%20utveckling%20för%20Nybörjare-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serie
[![Copilot för AI-parprogrammering](https://img.shields.io/badge/Copilot%20för%20AI%20parprogrammering-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot för C#/.NET](https://img.shields.io/badge/Copilot%20för%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Få Hjälp

Om du fastnar eller har frågor om att bygga AI-appar, gå med i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Om du har produktfeedback eller stöter på fel under byggandet, besök:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.