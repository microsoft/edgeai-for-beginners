# EdgeAI pro začátečníky 


![Obrázek obálky kurzu](../../translated_images/cs/cover.eb18d1b9605d754b.webp)

[![Přispěvatelé na GitHubu](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHubu](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty na GitHubu](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![Vítáme PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Sledující na GitHubu](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hvězdy na GitHubu](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Postupujte podle těchto kroků, abyste mohli začít používat tyto zdroje:

1. **Vytvořte fork repozitáře**: Klikněte na [![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Naklonujte repozitář**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Připojte se k Azure AI Foundry Discord a setkejte se s odborníky a kolegy vývojáři**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Podpora více jazyků

#### Podporováno přes GitHub Action (automatizované & vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmština (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradiční, Hong Kong)](../zh-HK/README.md) | [Čínština (tradiční, Macao)](../zh-MO/README.md) | [Čínština (tradiční, Taiwan)](../zh-TW/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malajalámština](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijská pidžinština](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Farsi)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../pt-BR/README.md) | [Portugalština (Portugalsko)](../pt-PT/README.md) | [Paňdžábština (Gurmukhí)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Telugština](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)

> **Dáváte přednost klonování lokálně?**

> Tento repozitář obsahuje více než 50 jazykových překladů, což výrazně zvětšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> To vám poskytne vše potřebné k dokončení kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Pokud si přejete podpořit další překladatelské jazyky, jsou uvedeny [zde](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Úvod

Vítejte v kurzu **EdgeAI pro začátečníky** – vaší komplexní cestě do transformujícího světa Edge umělé inteligence. Tento kurz překlene propast mezi výkonnými AI možnostmi a praktickým nasazením v reálném světě na okrajových zařízeních, což vám umožní využít potenciál AI přímo tam, kde jsou data generována a je potřeba přijímat rozhodnutí.

### Co se naučíte

Kurz vás provede od základních pojmů až po implementace připravené pro produkci, zahrnující:
- **Malé jazykové modely (SLM)** optimalizované pro nasazení na okraji
- **Optimalizace s ohledem na hardware** napříč různými platformami
- **Inference v reálném čase** s možnostmi ochrany soukromí
- **Strategie nasazení do produkce** pro podnikové aplikace

### Proč je EdgeAI důležitý

Edge AI představuje zásadní posun, který řeší kritické moderní výzvy:
- **Soukromí a bezpečnost**: Zpracování citlivých dat lokálně bez exponování do cloudu
- **Výkon v reálném čase**: Eliminace latence sítě pro časově kritické aplikace
- **Efektivita nákladů**: Snížení nákladů na přenos dat a cloudové výpočty
- **Odolný provoz**: Zachování funkčnosti během výpadků sítě
- **Soulad s regulacemi**: Splnění požadavků na suverenitu dat

### Edge AI

Edge AI znamená spuštění AI algoritmů a jazykových modelů lokálně na hardwaru blízko místa generování dat bez závislosti na cloudových zdrojích pro inference. Snižuje latenci, zvyšuje soukromí a umožňuje rozhodování v reálném čase.

### Základní principy:
- **Inference na zařízení**: AI modely běží na okrajových zařízeních (telefony, routery, mikrokontroléry, průmyslové PC)
- **Offline schopnost**: Funguje bez trvalého připojení k internetu
- **Nízká latence**: Okamžité reakce vhodné pro systémy v reálném čase
- **Suverenita dat**: Udržuje citlivá data lokálně, což zvyšuje bezpečnost a soulad s předpisy

### Malé jazykové modely (SLM)

SLM jako Phi-4, Mistral-7B a Gemma jsou optimalizované verze větších LLM—trénované nebo destilované pro:
- **Sníženou paměťovou náročnost**: Efektivní využití omezené paměti okrajových zařízení
- **Nižší výpočetní požadavky**: Optimalizované pro výkon CPU a okrajových GPU
- **Rychlejší spuštění**: Rychlá inicializace pro responzivní aplikace

Umožňují výkonné NLP schopnosti a zároveň splňují omezení:
- **Vestavěné systémy**: IoT zařízení a průmyslové regulátory
- **Mobilní zařízení**: Smartphony a tablety s offline možnostmi
- **IoT zařízení**: Senzory a chytrá zařízení s omezenými zdroji
- **Okrajové servery**: Lokální zpracování s omezenými GPU zdroji
- **Osobní počítače**: Scénáře nasazení na desktop a notebook

## Moduly kurzu & navigace

| Modul | Téma | Oblast zaměření | Klíčový obsah | Úroveň | Délka |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy a kontext | Přehled EdgeAI • Průmyslové aplikace • Úvod do SLM • Výukové cíle | Začátečník | 1-2 hod |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnání Cloud vs Edge AI | Základy EdgeAI • Reálné případové studie • Průvodce implementací • Nasazení na okraji | Začátečník | 3-4 hod |
| [🧠 02](../../Module02) | [Základy modelů SLM](./Module02/README.md) | Rodiny modelů & architektura | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začátečník | 4-5 hod |
| [🚀 03](../../Module03) | [Praktické nasazení SLM](./Module03/README.md) | Lokální & cloudové nasazení | Pokročilé učení • Lokální prostředí • Cloudové nasazení | Středně pokročilý | 4-5 hod |
| [⚙️ 04](../../Module04) | [Nástroje pro optimalizaci modelů](./Module04/README.md) | Optimalizace napříč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza pracovního toku | Středně pokročilý | 5-6 hod |
| [🔧 05](../../Module05) | [SLMOps pro produkci](./Module05/README.md) | Provoz v produkci | Úvod do SLMOps • Destilace modelů • Doladění • Nasazení do produkce | Pokročilý | 5-6 hod |
| [🤖 06](../../Module06) | [AI agenti & volání funkcí](./Module06/README.md) | Rámce agentů & MCP | Úvod do agentů • Volání funkcí • Protokol kontextu modelu | Pokročilý | 4-5 hod |
| [💻 07](../../Module07) | [Implementace na platformě](./Module07/README.md) | Vzory napříč platformami | AI toolkit • Foundry Local • Vývoj na Windows | Pokročilý | 3-4 hod |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Vzory připravené pro produkci | Ukázkové aplikace (viz detaily níže) | Expert | 8-10 hod |

### 🏭 **Modul 08: Ukázkové aplikace**

- [01: REST Chat rychlý start](./Module08/samples/01/README.md)
- [02: Integrace s OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objevování modelů & benchmarky](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikace](./Module08/samples/04/README.md)
- [05: Orchestrace multi-agentů](./Module08/samples/05/README.md)
- [06: Směrovač Models-as-Tools](./Module08/samples/06/README.md)
- [07: Přímý API klient](./Module08/samples/07/README.md)
- [08: Chat aplikace pro Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý multi-agentní systém](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická výuka**

Komplexní materiály workshopu s implementacemi připravenými pro produkci:

- **[Workshop průvodce](./Workshop/Readme.md)** - Komplexní výukové cíle, výsledky a navigace zdrojů
- **Python ukázky** (6 sezení) - Aktualizované podle nejlepších postupů, zpracování chyb a důkladná dokumentace
- **Jupyter notebooky** (8 interaktivních) - Krok za krokem tutoriály s benchmarky a monitorováním výkonu
- **Průvodci sezeními** - Detailní markdown průvodci ke každé části workshopu
- **Nástroje pro validaci** - Skripty pro ověření kvality kódu a provedení smoke testů

**Co postavíte:**
- Lokální AI chat aplikace s podporou streamování
- RAG pipeline s hodnocením kvality (RAGAS)
- Nástroje pro měření výkonu a srovnání více modelů
- Orchestrace systémů s více agenty
- Inteligentní směrování modelů s výběrem dle úloh

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Postavte si pipeline pro produkci podcastů poháněnou AI od základů! Tento intenzivní workshop vás naučí vytvořit kompletní multi-agentní systém, který promění nápady v profesionální podcastové epizody.
**[🎬 Začněte workshop AI Podcast Studia](./WorkshopForAgentic/README.md)**

**Vaše mise**: Spusťte "Future Bytes" — technologický podcast zcela poháněný AI agenty, které si sami vytvoříte. Bez závislosti na cloudu, bez nákladů na API — vše běží lokálně na vašem počítači.

**Co je na tom jedinečné:**
- **🤖 Skutečná multiagentová orchestrácia** - Vytvořte specializované AI agenty, kteří vyhledávají, píší a produkují zvuk
- **🎯 Kompletní produkční pipeline** - Od výběru tématu až po finální audio podcast
- **💻 100% lokální nasazení** - Používá Ollama a lokální modely (Qwen-3-8B) pro plné soukromí a kontrolu
- **🎤 Integrace převodu textu na řeč** - Přeměňte scénáře na přirozeně znějící konverzace více mluvčích
- **✋ Workflow s člověkem v procesu** - Schvalovací brány zajišťují kvalitu při zachování automatizace

**Tříaktová učební cesta:**

| Akt | Zaměření | Klíčové dovednosti | Délka trvání |
|-----|-------|------------|----------|
| **[Akt 1: Seznamte se se svými AI asistenty](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Vytvořte svého prvního AI agenta | Integrace nástrojů • Webové vyhledávání • Řešení problémů • Agentní uvažování | 2-3 hodiny |
| **[Akt 2: Sestavte svůj produkční tým](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestrujte více agentů | Koordinace týmu • Schvalovací workflow • Rozhraní DevUI • Dozor člověka | 3-4 hodiny |
| **[Akt 3: Oživte svůj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generujte audio podcastu | Převod textu na řeč • Syntéza více hlasů • Dlouhé audio • Plná automatizace | 2-3 hodiny |

**Použité technologie:**
- **Microsoft Agent Framework** - Multiagentní orchestrácia a koordinace
- **Ollama** - Lokální runtime AI modelu (bez cloudu)
- **Qwen-3-8B** - Open-source jazykový model optimalizovaný pro agentní úlohy
- **API převodu textu na řeč** - Přirozená syntéza hlasu pro generování podcastu

**Podpora hardwaru:**
- ✅ **Režim CPU** - Funguje na jakémkoli moderním počítači (doporučeno 8GB+ RAM)
- 🚀 **GPU akcelerace** - Výrazně rychlejší inferenční výpočty na NVIDIA/AMD GPU
- ⚡ **Podpora NPU** - Akcelerace nové generace neuronových procesorů

**Ideální pro:**
- Vývojáře, kteří se učí multiagentní AI systémy
- Každého se zájmem o AI automatizaci a workflow
- Tvůrce obsahu zkoumající AI asistovanou produkci
- Studentky a studenty studující praktické vzory orchestraci AI

**Začněte stavět**: [🎙️ Workshop AI Podcast Studia →](./WorkshopForAgentic/README.md)

### 📊 **Shrnutí učební cesty**
- **Celková délka**: 36-45 hodin
- **Cesta pro začátečníky**: Moduly 01-02 (7-9 hodin)  
- **Středně pokročilá cesta**: Moduly 03-04 (9-11 hodin)
- **Pokročilá cesta**: Moduly 05-07 (12-15 hodin)
- **Expertní cesta**: Modul 08 (8-10 hodin)

## Co vytvoříte

### 🎯 Základní kompetence
- **Edge AI architektura**: Navrhněte AI systémy primárně lokální s integrací cloudu
- **Optimalizace modelů**: Kvantizace a komprese modelů pro nasazení na okraji sítě (85% zvýšení rychlosti, 75% zmenšení velikosti)
- **Nasazení na více platformách**: Windows, mobil, embedded a hybrid cloud-edge systémy
- **Provozní produkce**: Monitorování, škálování a údržba Edge AI v produkci

### 🏗️ Praktické projekty
- **Foundry lokální chat aplikace**: Nativní aplikace Windows 11 s přepínáním modelů
- **Multiagentní systémy**: Koordinátor s odbornými agenty pro složité workflow  
- **RAG aplikace**: Lokální zpracování dokumentů s vektorovým vyhledáváním
- **Model routry**: Inteligentní výběr mezi modely na základě analýzy úkolů
- **API frameworky**: Produkčně připravení klienti s podporou streamování a sledování zdraví
- **Křížové platformní nástroje**: Vzory integrace LangChain/Semantic Kernel

### 🏢 Průmyslová využití
**Výroba** • **Zdravotnictví** • **Autonomní vozidla** • **Chytrá města** • **Mobilní aplikace**

## Rychlý start

**Doporučená učební cesta** (20-30 hodin celkem):

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + průmyslový kontext + učební rámec
1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelů SLM
2. **⚙️ Optimalizace** (Moduly 03-04): Nasazení + kvantizační frameworky  
3. **🚀 Produkce** (Moduly 05-06): SLMOps + AI agenti + volání funkcí
4. **💻 Implementace** (Moduly 07-08): Ukázky platformy + nástroje Foundry Local

Každý modul obsahuje teorii, praktické cvičení a produkčně připravené ukázky kódu.

## Kariérní dopad

**Technické role**: Architekt řešení EdgeAI • ML inženýr (Edge) • IoT AI vývojář • Mobilní AI vývojář

**Průmyslová odvětví**: Výroba 4.0 • Zdravotnické technologie • Autonomní systémy • FinTech • Spotřební elektronika

**Portfolio projektů**: Multiagentní systémy • Produkční RAG aplikace • Křížové platformní nasazení • Optimalizace výkonu

## Struktura repozitáře

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

## Hlavní body kurzu

✅ **Progresivní učení**: Teorie → Praxe → Produkční nasazení  
✅ **Reálné případy**: Microsoft, Japan Airlines, implementace ve firmách  
✅ **Praktické ukázky**: 50+ příkladů, 10 komplexních ukázek Foundry Local  
✅ **Zaměření na výkon**: 85% zrychlení, 75% zmenšení velikosti  
✅ **Multi-platformní**: Windows, mobil, embedded, cloud-edge hybrid  
✅ **Připraveno pro produkci**: Monitoring, škálování, bezpečnost, soulad s předpisy

📖 **[Dostupný studijní průvodce](STUDY_GUIDE.md)**: Strukturovaná 20hodinová učební cesta s rozdělením času a nástroji pro sebehodnocení.

---

**EdgeAI představuje budoucnost AI nasazení**: lokálně orientované, chránící soukromí a efektivní. Ovládněte tyto dovednosti a postavte další generaci inteligentních aplikací.

## Ostatní kurzy

Náš tým vytváří i další kurzy! Podívejte se:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Generativní AI
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní učení
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získání pomoci

Pokud narazíte na problém nebo máte jakékoli dotazy ohledně tvorby AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby při vývoji, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoli nejasnosti či nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->