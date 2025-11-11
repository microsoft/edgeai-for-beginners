<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e61ee5b6cb0bff11495c72afb37a9e8",
  "translation_date": "2025-11-11T16:59:52+00:00",
  "source_file": "README.md",
  "language_code": "no"
}
-->
# EdgeAI for Nybegynnere

![Kurs forsidebilde](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.no.png)

Følg disse trinnene for å komme i gang med ressursene:

1. **Fork Repository**: Klikk [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klon Repository**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bli med i Azure AI Foundry Discord og møt eksperter og andre utviklere**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Støtte for flere språk

#### Støttet via GitHub Action (Automatisk og alltid oppdatert)

**Hvis du ønsker å få støtte for flere oversettelsesspråk, er de listet opp [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduksjon

Velkommen til **EdgeAI for Nybegynnere** – din omfattende reise inn i den transformative verdenen av Edge Artificial Intelligence. Dette kurset bygger bro mellom kraftige AI-funksjoner og praktisk, virkelighetsnær implementering på edge-enheter, og gir deg muligheten til å utnytte AI direkte der data genereres og beslutninger må tas.

### Hva du vil mestre

Dette kurset tar deg fra grunnleggende konsepter til produksjonsklare implementeringer, og dekker:
- **Små språkmodeller (SLMs)** optimalisert for edge-implementering
- **Maskinvarebevisst optimalisering** på tvers av ulike plattformer
- **Sanntidsinferens** med personvernbevarende funksjoner
- **Produksjonsimplementeringsstrategier** for bedriftsapplikasjoner

### Hvorfor EdgeAI er viktig

Edge AI representerer et paradigmeskifte som adresserer kritiske moderne utfordringer:
- **Personvern og sikkerhet**: Behandle sensitiv data lokalt uten eksponering til skyen
- **Sanntidsytelse**: Fjern nettverksforsinkelser for tidskritiske applikasjoner
- **Kostnadseffektivitet**: Reduser båndbredde og skyberegningskostnader
- **Robuste operasjoner**: Oppretthold funksjonalitet under nettverksavbrudd
- **Regulatorisk samsvar**: Oppfyll krav til datasuverenitet

### Edge AI

Edge AI refererer til å kjøre AI-algoritmer og språkmodeller lokalt på maskinvare, nær der data genereres, uten å være avhengig av skyressurser for inferens. Det reduserer forsinkelser, forbedrer personvern og muliggjør sanntidsbeslutninger.

### Kjerneprinsipper:
- **På-enhet inferens**: AI-modeller kjører på edge-enheter (telefoner, rutere, mikrokontrollere, industrielle PC-er)
- **Offline-funksjonalitet**: Fungerer uten vedvarende internettforbindelse
- **Lav forsinkelse**: Umiddelbare responser egnet for sanntidssystemer
- **Datasuverenitet**: Holder sensitiv data lokalt, forbedrer sikkerhet og samsvar

### Små språkmodeller (SLMs)

SLMs som Phi-4, Mistral-7B og Gemma er optimaliserte versjoner av større LLMs—trent eller destillert for:
- **Redusert minnebruk**: Effektiv bruk av begrenset edge-enhetsminne
- **Lavere beregningskrav**: Optimalisert for CPU og edge GPU-ytelse
- **Raskere oppstartstider**: Rask initialisering for responsive applikasjoner

De låser opp kraftige NLP-funksjoner samtidig som de oppfyller begrensningene til:
- **Innebygde systemer**: IoT-enheter og industrielle kontrollere
- **Mobile enheter**: Smarttelefoner og nettbrett med offline-funksjonalitet
- **IoT-enheter**: Sensorer og smarte enheter med begrensede ressurser
- **Edge-servere**: Lokale behandlingsenheter med begrensede GPU-ressurser
- **Personlige datamaskiner**: Stasjonære og bærbare implementeringsscenarier

## Kursmoduler og navigasjon

| Modul | Emne | Fokusområde | Nøkkelinnhold | Nivå | Varighet |
|-------|------|-------------|---------------|------|----------|
| [📖 00 ](./introduction.md) | [Introduksjon til EdgeAI](./introduction.md) | Grunnlag og kontekst | Oversikt over EdgeAI • Industriapplikasjoner • Introduksjon til SLM • Læringsmål | Nybegynner | 1-2 timer |
| [📚 01](../../Module01) | [Grunnleggende om EdgeAI](./Module01/README.md) | Sammenligning av sky og Edge AI | Grunnleggende om EdgeAI • Virkelige casestudier • Implementeringsveiledning • Edge-implementering | Nybegynner | 3-4 timer |
| [🧠 02](../../Module02) | [SLM Modellgrunnlag](./Module02/README.md) | Modeller og arkitektur | Phi-familien • Qwen-familien • Gemma-familien • BitNET • μModel • Phi-Silica | Nybegynner | 4-5 timer |
| [🚀 03](../../Module03) | [SLM Implementeringspraksis](./Module03/README.md) | Lokal og skyimplementering | Avansert læring • Lokalt miljø • Skyimplementering | Middels | 4-5 timer |
| [⚙️ 04](../../Module04) | [Verktøy for modelloptimalisering](./Module04/README.md) | Tverrplattformoptimalisering | Introduksjon • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Arbeidsflytsyntese | Middels | 5-6 timer |
| [🔧 05](../../Module05) | [SLMOps Produksjon](./Module05/README.md) | Produksjonsoperasjoner | Introduksjon til SLMOps • Modelldestillasjon • Finjustering • Produksjonsimplementering | Avansert | 5-6 timer |
| [🤖 06](../../Module06) | [AI-agenter og funksjonskall](./Module06/README.md) | Agentrammeverk og MCP | Introduksjon til agenter • Funksjonskall • Modellkontekstprotokoll | Avansert | 4-5 timer |
| [💻 07](../../Module07) | [Plattformimplementering](./Module07/README.md) | Tverrplattformeksempler | AI-verktøysett • Foundry Local • Windows-utvikling | Avansert | 3-4 timer |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Produksjonsklare eksempler | Eksempelapplikasjoner (se detaljer nedenfor) | Ekspert | 8-10 timer |

### 🏭 **Modul 08: Eksempelapplikasjoner**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK-integrasjon](./Module08/samples/02/README.md)
- [03: Modelloppdagelse og benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG-applikasjon](./Module08/samples/04/README.md)
- [05: Multi-agent orkestrering](./Module08/samples/05/README.md)
- [06: Modeller-som-verktøy router](./Module08/samples/06/README.md)
- [07: Direkte API-klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Avansert multi-agent system](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktisk læringssti**

Omfattende praktiske workshop-materialer med produksjonsklare implementeringer:

- **[Workshop Guide](./Workshop/Readme.md)** - Fullstendige læringsmål, resultater og ressursnavigasjon
- **Python-eksempler** (6 økter) - Oppdatert med beste praksis, feilhåndtering og omfattende dokumentasjon
- **Jupyter Notebooks** (8 interaktive) - Trinnvise opplæringer med benchmarking og ytelsesovervåking
- **Øktguider** - Detaljerte markdown-guider for hver workshop-økt
- **Valideringsverktøy** - Skript for å verifisere kodekvalitet og kjøre røyktester

**Hva du vil bygge:**
- Lokale AI-chatapplikasjoner med streamingstøtte
- RAG-pipelines med kvalitetsevaluering (RAGAS)
- Multi-modell benchmarking og sammenligningsverktøy
- Multi-agent orkestreringssystemer
- Intelligent modellruting med oppgavebasert utvalg

### 📊 **Oppsummering av læringssti**
- **Total varighet**: 36-45 timer
- **Nybegynnersti**: Moduler 01-02 (7-9 timer)  
- **Middels sti**: Moduler 03-04 (9-11 timer)
- **Avansert sti**: Moduler 05-07 (12-15 timer)
- **Ekspertsti**: Modul 08 (8-10 timer)

## Hva du vil bygge

### 🎯 Kjernekompetanser
- **Edge AI-arkitektur**: Design AI-systemer med lokal-først tilnærming og skyintegrasjon
- **Modelloptimalisering**: Kvantisere og komprimere modeller for edge-implementering (85% hastighetsøkning, 75% størrelsesreduksjon)
- **Multi-plattform distribusjon**: Windows, mobil, innebygde systemer og sky-edge hybridløsninger  
- **Produksjonsdrift**: Overvåking, skalering og vedlikehold av edge AI i produksjon  

### 🏗️ Praktiske prosjekter  
- **Foundry lokale chat-apper**: Windows 11 native-applikasjon med modellbytte  
- **Multi-agent systemer**: Koordinator med spesialistagenter for komplekse arbeidsflyter  
- **RAG-applikasjoner**: Lokal dokumentbehandling med vektorsøk  
- **Modellrutere**: Intelligent valg mellom modeller basert på oppgaveanalyse  
- **API-rammeverk**: Produksjonsklare klienter med streaming og helsesjekk  
- **Tverrplattformverktøy**: LangChain/Semantic Kernel integrasjonsmønstre  

### 🏢 Bruksområder i industrien  
**Produksjon** • **Helsevesen** • **Autonome kjøretøy** • **Smarte byer** • **Mobilapper**  

## Kom i gang  

**Anbefalt læringssti** (20-30 timer totalt):  

0. **📖 Introduksjon** ([Introduction.md](./introduction.md)): EdgeAI-grunnlag + industrikontekst + læringsrammeverk  
1. **📚 Grunnlag** (Moduler 01-02): EdgeAI-konsepter + SLM-modellfamilier  
2. **⚙️ Optimalisering** (Moduler 03-04): Distribusjon + kvantiseringsrammeverk  
3. **🚀 Produksjon** (Moduler 05-06): SLMOps + AI-agenter + funksjonskall  
4. **💻 Implementering** (Moduler 07-08): Plattformeksempler + Foundry Local-verktøysett  

Hver modul inkluderer teori, praktiske øvelser og produksjonsklare kodeeksempler.  

## Karrierepåvirkning  

**Tekniske roller**: EdgeAI-løsningsarkitekt • ML-ingeniør (Edge) • IoT AI-utvikler • Mobil AI-utvikler  

**Industrielle sektorer**: Produksjon 4.0 • Helse-teknologi • Autonome systemer • FinTech • Forbrukerelektronikk  

**Porteføljeprosjekter**: Multi-agent systemer • Produksjonsklare RAG-apper • Tverrplattform distribusjon • Ytelsesoptimalisering  

## Repository-struktur  

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

✅ **Progressiv læring**: Teori → Praktisk → Produksjonsdistribusjon  
✅ **Reelle casestudier**: Microsoft, Japan Airlines, bedriftsimplementeringer  
✅ **Praktiske eksempler**: 50+ eksempler, 10 omfattende Foundry Local-demoer  
✅ **Fokus på ytelse**: 85 % hastighetsforbedringer, 75 % størrelsesreduksjoner  
✅ **Multi-plattform**: Windows, mobil, innebygde systemer, sky-edge hybrid  
✅ **Produksjonsklar**: Overvåking, skalering, sikkerhet, samsvarsrammeverk  

📖 **[Studieguide tilgjengelig](STUDY_GUIDE.md)**: Strukturert 20-timers læringssti med tidsallokering og selvvurderingsverktøy.  

---

**EdgeAI representerer fremtiden for AI-distribusjon**: lokal-først, personvernvennlig og effektiv. Mestre disse ferdighetene for å bygge neste generasjons intelligente applikasjoner.  

## Andre kurs  

Vårt team produserer andre kurs! Sjekk ut:  

<!-- CO-OP TRANSLATOR OTHER COURSES START -->  
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

### Copilot-serien  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->  

## Få hjelp  

Hvis du står fast eller har spørsmål om å bygge AI-apper, bli med:  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

Hvis du har produktfeedback eller feil under bygging, besøk:  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->