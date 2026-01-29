# EdgeAI pre začiatočníkov 


![Obálka kurzu](../../translated_images/sk/cover.eb18d1b9605d754b.webp)

[![Prispievatelia na GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Žiadosti o pull na GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![Príspevky vítané](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Pozorovatelia na GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forky na GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hviezdy na GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Postupujte podľa týchto krokov, aby ste začali používať tieto zdroje:

1. **Forknite Repozitár**: Kliknite na [![Forky na GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonujte Repozitár**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridajte sa na Discord Azure AI Foundry a stretávajte sa s odborníkmi a kolegami vývojármi**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Viacjazyčná podpora

#### Podporované cez GitHub Action (Automatizované a vždy aktuálne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradičná, Hongkong)](../zh-HK/README.md) | [Čínština (tradičná, Macao)](../zh-MO/README.md) | [Čínština (tradičná, Taiwan)](../zh-TW/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Malayalam](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigerijská pidžinčina](../pcm/README.md) | [Norwegian](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../pt-BR/README.md) | [Portugalčina (Portugalsko)](../pt-PT/README.md) | [Pandžábčina (Gurmukhí)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Suahelčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipíny)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

> **Radšej klonovať lokálne?**

> Tento repozitár obsahuje viac ako 50 jazykových prekladov, čo výrazne zvyšuje veľkosť na stiahnutie. Pre klonovanie bez prekladov použite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Toto vám poskytne všetko potrebné na dokončenie kurzu s oveľa rýchlejším sťahovaním.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ak chcete, aby boli pridané ďalšie podporované jazyky, nájdete ich [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Úvod

Vitajte v **EdgeAI pre začiatočníkov** – vašej komplexnej ceste do prelomového sveta Edge umelej inteligencie. Tento kurz premostí medzeru medzi výkonnými AI schopnosťami a praktickým nasadením v reálnom svete na edge zariadeniach a umožní vám využiť potenciál AI priamo tam, kde sa generujú dáta a kde je potrebné prijímať rozhodnutia.

### Čo sa naučíte

Tento kurz vás prevedie od základných konceptov až po implementácie pripravené do výroby, pokrývajúc:
- **Malé jazykové modely (SLMs)** optimalizované pre nasadenie na edge
- **Optimalizácia so zreteľom na hardvér** naprieč rôznymi platformami
- **Inference v reálnom čase** s možnosťami zachovania súkromia
- **Stratégie nasadenia do výroby** pre podnikové aplikácie

### Prečo je EdgeAI dôležitá

Edge AI predstavuje paradigmatickú zmenu, ktorá rieši kritické moderné výzvy:
- **Súkromie a bezpečnosť**: Spracovanie citlivých údajov lokálne bez vystavenia v cloude
- **Výkon v reálnom čase**: Odstránenie sieťových latencií pre časovo kritické aplikácie
- **Nákladová efektívnosť**: Zníženie nákladov na šírku pásma a cloudové výpočty
- **Odolné operácie**: Zachovanie funkčnosti počas výpadkov siete
- **Dodržiavanie regulácií**: Splnenie požiadaviek na suverenitu dát

### Edge AI

Edge AI označuje prevádzku AI algoritmov a jazykových modelov lokálne na hardvéri blízko miesta generovania dát bez závislosti na cloudových zdrojoch pre inference. Znižuje latenciu, zvyšuje súkromie a umožňuje rozhodovanie v reálnom čase.

### Základné princípy:
- **Inference na zariadení**: AI modely bežia na edge zariadeniach (telefóny, routre, mikrokontroléry, priemyselné PC)
- **Funkčnosť offline**: Pracuje bez trvalého pripojenia na internet
- **Nízka latencia**: Okamžité reakcie vhodné pre systémy v reálnom čase
- **Suverenita dát**: Zachovanie citlivých dát lokálne, zlepšuje bezpečnosť a súlad s reguláciami

### Malé jazykové modely (SLMs)

SLM ako Phi-4, Mistral-7B a Gemma sú optimalizované verzie väčších LLM—trénované alebo destilované pre:
- **Zníženú pamäťovú stopu**: Efektívne využitie obmedzenej pamäte edge zariadení
- **Nižšie výpočtové nároky**: Optimalizované pre výkon CPU a edge GPU
- **Rýchlejšie spustenie**: Rýchla inicializácia pre responzívne aplikácie

Umožňujú výkonné NLP schopnosti pri dodržaní obmedzení:
- **Embedované systémy**: IoT zariadenia a priemyselné kontroléry
- **Mobilné zariadenia**: Smartfóny a tablety s offline funkciami
- **IoT zariadenia**: Senzory a inteligentné zariadenia s obmedzenými zdrojmi
- **Edge servery**: Lokálne spracovateľské jednotky s limitovanými GPU zdrojmi
- **Osobné počítače**: Nasadenie na desktopoch a notebookoch

## Moduly kurzu a navigácia

| Modul | Téma | Zameranie | Kľúčový obsah | Úroveň | Trvanie |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy a kontext | Prehľad EdgeAI • Priemyselné aplikácie • Úvod do SLM • Ciele učenia | Začiatočník | 1-2 hod |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnanie cloud vs edge AI | Základy EdgeAI • Prípadové štúdie z praxe • Sprievodca implementáciou • Nasadenie na edge | Začiatočník | 3-4 hod |
| [🧠 02](../../Module02) | [Základy modelov SLM](./Module02/README.md) | Rodiny modelov a architektúra | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začiatočník | 4-5 hod |
| [🚀 03](../../Module03) | [Praktické nasadenie SLM](./Module03/README.md) | Lokálne a cloudové nasadenie | Pokročilé učenie • Lokálne prostredie • Cloudové nasadenie | Stredne pokročilý | 4-5 hod |
| [⚙️ 04](../../Module04) | [Nástroje na optimalizáciu modelov](./Module04/README.md) | Optimalizácia cez platformy | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza pracovných postupov | Stredne pokročilý | 5-6 hod |
| [🔧 05](../../Module05) | [SLMOps vo výrobe](./Module05/README.md) | Prevádzkové postupy | Úvod do SLMOps • Destilácia modelov • Doladenie • Nasadenie do výroby | Pokročilý | 5-6 hod |
| [🤖 06](../../Module06) | [AI agenti a volanie funkcií](./Module06/README.md) | Agentné frameworky a MCP | Úvod do agentov • Volanie funkcií • Protokol kontextu modelu | Pokročilý | 4-5 hod |
| [💻 07](../../Module07) | [Implementácia platformy](./Module07/README.md) | Krosplatformové príklady | AI Toolkit • Foundry Local • Windows vývoj | Pokročilý | 3-4 hod |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Ukážkové aplikácie pripravené na výrobu | Ukážkové aplikácie (viď nižšie) | Expert | 8-10 hod |

### 🏭 **Modul 08: Ukážkové aplikácie**

- [01: Rýchly štart REST chatu](./Module08/samples/01/README.md)
- [02: Integrácia OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objavovanie modelov a benchmarky](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikácia](./Module08/samples/04/README.md)
- [05: Orchestrace multi-agentov](./Module08/samples/05/README.md)
- [06: Router modelov ako nástrojov](./Module08/samples/06/README.md)
- [07: Priamy API klient](./Module08/samples/07/README.md)
- [08: Chat aplikácia pre Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý multi-agentný systém](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická cesta učenia**

Komplexné praktické materiály workshopu s implementáciami pripravenými do výroby:

- **[Sprievodca workshopom](./Workshop/Readme.md)** - Kompletné ciele učenia, výsledky a navigácia zdrojov
- **Python ukážky** (6 relácií) - Aktualizované o najlepšie praktiky, spracovanie chýb a podrobnú dokumentáciu
- **Jupyter notebooky** (8 interaktívnych) - Návody krok za krokom s benchmarkmi a monitorovaním výkonu
- **Príručky k reláciám** - Podrobné markdown sprievodcovia ku každej relácii workshopu
- **Nástroje na validáciu** - Skripty na overenie kvality kódu a testovanie stability

**Čo vytvoríte:**
- Lokálne AI chat aplikácie s podporou streamovania
- RAG pipeline s hodnotením kvality (RAGAS)
- Nástroje na benchmarking a porovnávanie viacerých modelov
- Systémy orchestrácie multi-agentov
- Inteligentné smerovanie modelov s výberom úloh

### 🎙️ **Workshop pre Agentic: Praktické v štúdiu AI podcastov**

Vybudujte produkčnú pipeline na vytváranie podcastov poháňanú AI od základu! Tento pohlcujúci workshop vás naučí vytvoriť kompletný multi-agentný systém, ktorý transformuje nápady na profesionálne podcastové epizódy.
**[🎬 Začni workshop AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Tvoja misia**: Spusti "Future Bytes" — technologický podcast, ktorý beží úplne na AI agentoch, ktorých si sám vytvoríš. Žiadne závislosti na cloude, žiadne náklady na API — všetko beží lokálne na tvojom počítači.

**Čo robí toto unikátnym:**
- **🤖 Skutočná multi-agentná orchestrácia** - Vytváraj špecializovaných AI agentov, ktorí skúmajú, píšu a produkujú audio
- **🎯 Kompletný produkčný proces** - Od výberu témy až po finálny podcastový audio výstup
- **💻 100 % lokálne nasadenie** - Používa Ollama a lokálne modely (Qwen-3-8B) pre plné súkromie a kontrolu
- **🎤 Integrácia prevodu textu na reč** - Premeň skripty na prirodzene znejúce viachlasové konverzácie
- **✋ Pracovné postupy s ľudským zásahom** - Schvaľovacie brány zabezpečujú kvalitu a zároveň udržiavajú automatizáciu

**Trojakčné vzdelávacie putovanie:**

| Akt | Zameranie | Kľúčové schopnosti | Trvanie |
|-----|-----------|--------------------|---------|
| **[Akt 1: Spoznaj svojich AI asistentov](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Vytvor si svojho prvého AI agenta | Integrácia nástrojov • Webové vyhľadávanie • Riešenie problémov • Agentické uvažovanie | 2-3 hodiny |
| **[Akt 2: Zostav svoj produkčný tím](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestruj viacerých agentov | Koordinácia tímu • Schvaľovacie pracovné postupy • Rozhranie DevUI • Ľudský dohľad | 3-4 hodiny |
| **[Akt 3: Oživ svoj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generuj podcastové audio | Text na reč • Multi-speaker syntéza • Dlhé audio • Plná automatizácia | 2-3 hodiny |

**Použité technológie:**
- **Microsoft Agent Framework** - Orchestrácia a koordinácia multi-agentov
- **Ollama** - Lokálny runtime AI modelu (žiadny cloud nie je potrebný)
- **Qwen-3-8B** - Open-source jazykový model optimalizovaný pre agentické úlohy
- **API na prevod textu na reč** - Prírodná syntéza hlasu pre generovanie podcastov

**Hardvérová podpora:**
- ✅ **Režim CPU** - Funguje na akomkoľvek modernom počítači (odporúča sa 8GB+ RAM)
- 🚀 **GPU akcelerácia** - Výrazne rýchlejšia inferencia s NVIDIA/AMD GPU
- ⚡ **Podpora NPU** - Akcelerácia nasledujúcej generácie neurónových procesorov

**Ideálne pre:**
- Vývojárov učúcich sa multi-agentné AI systémy
- Každého, koho zaujíma AI automatizácia a pracovné postupy
- Tvorcov obsahu preskúmajúcich AI-podporovanú produkciu
- Študentov študujúcich praktické vzory AI orchestrácie

**Začni stavať**: [🎙️ Workshop AI Podcast Studio →](./WorkshopForAgentic/README.md)

### 📊 **Zhrnutie vzdelávacej cesty**
- **Celkové trvanie**: 36-45 hodín
- **Začiatočnícka cesta**: Moduly 01-02 (7-9 hodín)  
- **Stredne pokročilá cesta**: Moduly 03-04 (9-11 hodín)
- **Pokročilá cesta**: Moduly 05-07 (12-15 hodín)
- **Expertná cesta**: Modul 08 (8-10 hodín)

## Čo vybuduješ

### 🎯 Kľúčové kompetencie
- **Edge AI architektúra**: Navrhovanie AI systémov s prioritou lokálneho spracovania s integráciou cloudu
- **Optimalizácia modelov**: Kvantizácia a kompresia modelov pre edge nasadenie (85 % zrýchlenie, 75 % zmenšenie veľkosti)
- **Multi-platformové nasadenie**: Windows, mobilné zariadenia, embedded a cloud-edge hybridné systémy
- **Produkčné operácie**: Monitorovanie, škálovanie a údržba edge AI v produkcii

### 🏗️ Praktické projekty
- **Foundry Local Chat Apps**: Nativná aplikácia pre Windows 11 s prepínaním modelov
- **Multi-agentné systémy**: Koordinátor so špecializovanými agentmi pre komplexné pracovné postupy  
- **RAG aplikácie**: Lokálne spracovanie dokumentov s vektorovým vyhľadávaním
- **Routery modelov**: Inteligentný výber medzi modelmi na základe analýzy úloh
- **API frameworky**: Produkčne pripravení klienti s streamovaním a monitorovaním stavu
- **Nástroje pre viacero platforiem**: Vzory integrácie LangChain/Semantic Kernel

### 🏢 Priemyselné aplikácie
**Výroba** • **Zdravotníctvo** • **Autonómne vozidlá** • **Smart Cities** • **Mobilné aplikácie**

## Rýchly štart

**Odporúčaná vzdelávacia cesta** (20-30 hodín celkom):

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + priemyselný kontext + vzdelávací rámec  
1. **📚 Základy** (Moduly 01-02): EdgeAI koncepty + rodiny SLM modelov  
2. **⚙️ Optimalizácia** (Moduly 03-04): Nasadenie + frameworky pre kvantizáciu  
3. **🚀 Produkcia** (Moduly 05-06): SLMOps + AI agenti + volanie funkcií  
4. **💻 Implementácia** (Moduly 07-08): Vzory platforiem + Foundry Local toolkit

Každý modul obsahuje teóriu, praktické cvičenia a ukážky kódu pripravené do produkcie.

## Kariérny dopad

**Technické role**: Architekt riešení EdgeAI • ML inžinier (Edge) • IoT AI vývojár • Mobilný AI vývojár

**Priemyselné sektory**: Výroba 4.0 • Zdravotnícke technológie • Autonómne systémy • FinTech • Spotrebná elektronika

**Portfólio projektov**: Multi-agentné systémy • Produkčné RAG aplikácie • Multi-platformové nasadenie • Optimalizácia výkonu

## Štruktúra repozitára

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

## Hlavné body kurzu

✅ **Postupné učenie**: Teória → prax → produkčné nasadenie  
✅ **Reálne prípadové štúdie**: Microsoft, Japan Airlines, implementácie podnikov  
✅ **Praktické ukážky**: 50+ príkladov, 10 komplexných ukážok Foundry Local  
✅ **Zameranie na výkon**: 85% zrýchlenie, 75% zmenšenie veľkosti  
✅ **Viacplatformové**: Windows, mobilné zariadenia, embedded, cloud-edge hybrid  
✅ **Produkčne pripravené**: Monitorovanie, škálovanie, bezpečnosť, rámce na dodržiavanie noriem  

📖 **[Študijný sprievodca k dispozícii](STUDY_GUIDE.md)**: Štruktúrovaná vzdelávacia cesta na 20 hodín s rozdelením času a nástrojmi na sebahodnotenie.

---

**EdgeAI predstavuje budúcnosť nasadenia AI**: prioritne lokálne, s ochranou súkromia a efektívnosťou. Osvoj si tieto schopnosti a vytvor ďalšiu generáciu inteligentných aplikácií.

## Iné kurzy

Náš tím produkuje aj iné kurzy! Pozri si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Generatívnej AI
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základné učenie
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získanie pomoci

Ak sa zaseknete alebo máte akékoľvek otázky týkajúce sa tvorby AI aplikácií, pripojte sa na:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu k produktu alebo chyby počas tvorby, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča využiť profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->