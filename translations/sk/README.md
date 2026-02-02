# EdgeAI pre Začiatočníkov


![Obalový obrázok kurzu](../../translated_images/sk/cover.eb18d1b9605d754b.webp)

[![Prispievatelia na GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Žiadosti o stiahnutie na GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs vítané](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Sledujúci na GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Rozdvojenia na GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hviezdy na GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Nasledujte tieto kroky, aby ste mohli začať používať tieto zdroje:

1. **Forknite Repository**: Kliknite na [![Rozdvojenia na GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonujte Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridajte sa na Azure AI Foundry Discord a stretnite sa s expertmi a ostatnými vývojármi**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (automatizované a vždy aktuálne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmský (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradičná, Hong Kong)](../zh-HK/README.md) | [Čínština (tradičná, Macau)](../zh-MO/README.md) | [Čínština (tradičná, Taiwan)](../zh-TW/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Malajálamčina](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigérijská pidginčina](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../pt-BR/README.md) | [Portugalčina (Portugalsko)](../pt-PT/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swasilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

> **Radšej klonovať lokálne?**

> Tento repozitár obsahuje viac ako 50 jazykových prekladov, čo významne zväčšuje veľkosť sťahovania. Ak chcete klonovať bez prekladov, použite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Toto vám poskytne všetko potrebné pre dokončenie kurzu s oveľa rýchlejším sťahovaním.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ak si prajete podporu ďalších jazykov, podporované jazyky sú uvedené [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Úvod

Vitajte v **EdgeAI pre Začiatočníkov** – vašej komplexnej ceste do transformujúceho sveta Edge umelej inteligencie. Tento kurz premostuje priepasť medzi výkonnými AI možnosťami a praktickým, reálnym nasadením na okrajových zariadeniach, pričom vám umožňuje využiť potenciál AI priamo tam, kde sa generujú dáta a kde sa musia prijímať rozhodnutia.

### Čo sa naučíte

Tento kurz vás prevedie od základných konceptov po implementácie pripravené na produkciu, zahŕňajúc:
- **Malé jazykové modely (SLM)** optimalizované pre nasadenie na edge zariadeniach
- **Optimalizáciu s ohľadom na hardvér** naprieč rozmanitými platformami
- **Inferenciu v reálnom čase** s možnosťami zabezpečenia súkromia
- **Stratégie produkčného nasadenia** pre podnikové aplikácie

### Prečo je EdgeAI dôležitý

Edge AI predstavuje paradigmatický posun, ktorý rieši kľúčové moderné výzvy:
- **Súkromie a bezpečnosť**: Spracúvajte citlivé údaje lokálne bez vystavenia cloudu
- **Výkon v reálnom čase**: Eliminujte oneskorenia siete pre časovo kritické aplikácie
- **Efektívnosť nákladov**: Znížte výdavky na šírku pásma a cloudové výpočty
- **Odolné operácie**: Udržiavajte funkčnosť počas výpadkov siete
- **Dodržiavanie regulácií**: Splňte požiadavky na suverenitu dát

### Edge AI

Edge AI znamená spustenie AI algoritmov a jazykových modelov lokálne na hardvéri, blízko k tomu, kde sa generujú dáta, bez spoliehania sa na cloudové zdroje pre inferenciu. Znižuje latenciu, zvyšuje súkromie a umožňuje rozhodovanie v reálnom čase.

### Základné princípy:
- **Inferencia na zariadení**: AI modely bežia na edge zariadeniach (telefóny, routery, mikrokontroléry, priemyselné PC)
- **Offline schopnosť**: Funguje bez trvalého internetového pripojenia
- **Nízka latencia**: Okamžité reakcie vhodné pre systémy v reálnom čase
- **Sovereignita dát**: Citlivé dáta zostávajú lokálne, čo zlepšuje bezpečnosť a súlad s reguláciami

### Malé jazykové modely (SLM)

SLM ako Phi-4, Mistral-7B a Gemma sú optimalizované verzie väčších LLM—trénované alebo destilované pre:
- **Zníženú pamäťovú náročnosť**: Efektívne využitie obmedzenej pamäte edge zariadení
- **Nižšiu výpočtovú náročnosť**: Optimalizované pre CPU a edge GPU výkon
- **Rýchlejšie spustenie**: Rýchla inicializácia pre responzívne aplikácie

Umožňujú výkonné NLP schopnosti pri dodržaní obmedzení:
- **Vložené systémy**: IoT zariadenia a priemyselné ovládače
- **Mobilné zariadenia**: Smartfóny a tablety s offline funkciami
- **IoT zariadenia**: Senzory a inteligentné zariadenia s limitovanými zdrojmi
- **Edge servery**: Lokálne spracovateľské jednotky s obmedzenými GPU zdrojmi
- **Osobné počítače**: Scenáre nasadenia na desktopoch a laptopoch

## Moduly kurzu & Navigácia

| Modul | Téma | Zameranie | Kľúčový obsah | Úroveň | Trvanie |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy & Kontext | Prehľad EdgeAI • Príklady z praxe • Úvod do SLM • Ciele učenia | Začiatočník | 1-2 hodiny |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnanie cloud vs edge AI | Základy EdgeAI • Prípadové štúdie z praxe • Sprievodca implementáciou • Nasadenie na edge | Začiatočník | 3-4 hodiny |
| [🧠 02](../../Module02) | [Základy modelov SLM](./Module02/README.md) | Rodiny modelov & architektúra | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začiatočník | 4-5 hodín |
| [🚀 03](../../Module03) | [Praktické nasadenie SLM](./Module03/README.md) | Lokálne & cloudové nasadenie | Pokročilé učenie • Lokálne prostredie • Cloudové nasadenie | Stredne pokročilý | 4-5 hodín |
| [⚙️ 04](../../Module04) | [Nástroje na optimalizáciu modelov](./Module04/README.md) | Optimalizácia naprieč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza workflow | Stredne pokročilý | 5-6 hodín |
| [🔧 05](../../Module05) | [SLMOps produkcia](./Module05/README.md) | Produkčné operácie | Úvod do SLMOps • Destilácia modelov • Finálne dolaďovanie • Produkčné nasadenie | Pokročilý | 5-6 hodín |
| [🤖 06](../../Module06) | [AI agenti & volanie funkcií](./Module06/README.md) | Frameworky agentov & MCP | Úvod do agentov • Volanie funkcií • Protokol kontextu modelu | Pokročilý | 4-5 hodín |
| [💻 07](../../Module07) | [Implementácia platformy](./Module07/README.md) | Ukážky naprieč platformami | AI Toolkit • Foundry Lokálne • Vývoj na Windows | Pokročilý | 3-4 hodiny |
| [🏭 08](../../Module08) | [Foundry Lokálny Toolkit](./Module08/README.md) | Produkčne pripravené príklady | Ukážkové aplikácie (viď detaily nižšie) | Expert | 8-10 hodín |

### 🏭 **Modul 08: Ukážkové aplikácie**

- [01: Rýchly štart REST chatu](./Module08/samples/01/README.md)
- [02: Integrácia OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objavovanie modelov & benchmarkovanie](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikácia](./Module08/samples/04/README.md)
- [05: Orchestrace viacerých agentov](./Module08/samples/05/README.md)
- [06: Router Models-as-Tools](./Module08/samples/06/README.md)
- [07: Priamy API klient](./Module08/samples/07/README.md)
- [08: Chat aplikácia pre Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý systém viacerých agentov](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická učebná cesta**

Komplexné workshopové materiály s implementáciami pripravenými na produkciu:

- **[Návod k workshopu](./Workshop/Readme.md)** - Kompletné vzdelávacie ciele, výsledky a navigácia zdrojov
- **Python príklady** (6 relácií) - Aktualizované o najlepšie postupy, spracovanie chýb a komplexnú dokumentáciu
- **Jupyter zošity** (8 interaktívnych) - Krok za krokom tutoriály s benchmarkami a monitorovaním výkonu
- **Návody k reláciám** - Detailné markdown návody pre každú workshopovú reláciu
- **Nástroje na validáciu** - Skripty na overenie kvality kódu a spustenie základných testov

**Čo vytvoríte:**
- Lokálne AI chatové aplikácie s podporou streamovania
- RAG pipelines s hodnotením kvality (RAGAS)
- Nástroje na benchmarkovanie a porovnávanie viacerých modelov
- Systémy pre orchestráciu viacerých agentov
- Inteligentné smerovanie modelov s výberom úloh založeným na úlohách

### 🎙️ **Workshop For Agentic: Hands-On - AI Podcast Studio**

Vytvorte AI poháňaný produkčný pipeline pre podcast od základov! Tento pohlcujúci workshop vás naučí vytvoriť kompletný systém viacerých agentov, ktorý transformuje nápady na profesionálne podcastové epizódy.
**[🎬 Začni workshop AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Tvoja misia**: Spusti "Future Bytes" — technologický podcast poháňaný výhradne AI agentmi, ktorých si sám/a vybuduješ. Žiadne závislosti na cloude, žiadne náklady na API — všetko beží lokálne na tvojom počítači.

**Čo robí toto unikátnym:**
- **🤖 Skutočná orchestrácia viacerých agentov** - Vybuduj špecializovaných AI agentov, ktorí robia výskum, píšu a produkujú audio
- **🎯 Kompletný produkčný proces** - Od výberu témy až po finálny audio výstup podcastu
- **💻 100% lokálne nasadenie** - Používa Ollama a lokálne modely (Qwen-3-8B) pre plné súkromie a kontrolu
- **🎤 Integrácia text-na-reč** - Premeň skripty na prirodzene znejúce viacosobné rozhovory
- **✋ Pracovné postupy s ľudským schvaľovaním** - Schvaľovacie brány zaručujú kvalitu pri zachovaní automatizácie

**Trojdielna vzdelávacia cesta:**

| Dejstvo | Zameranie | Kľúčové zručnosti | Trvanie |
|---------|-----------|-------------------|---------|
| **[Dejstvo 1: Spoznaj svojich AI asistentov](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Vybuduj svoj prvý AI agent | Integrácia nástrojov • Webový vyhľadávač • Riešenie problémov • Agentické uvažovanie | 2-3 hodiny |
| **[Dejstvo 2: Zostav svoj produkčný tím](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestruj viacerých agentov | Koordinácia tímu • Schvaľovacie pracovné postupy • Rozhranie DevUI • Ľudský dohľad | 3-4 hodiny |
| **[Dejstvo 3: Oživ svoj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generuj audio podcastu | Text-na-reč • Viacosobná syntéza • Dlhé audio • Plná automatizácia | 2-3 hodiny |

**Použité technológie:**
- **Microsoft Agent Framework** - Orchestrácia a koordinácia viacerých agentov
- **Ollama** - Lokálne prostredie pre AI modely (žiadny cloud nie je potrebný)
- **Qwen-3-8B** - Open-source jazykový model optimalizovaný pre agentické úlohy
- **Text-to-Speech API** - Syntéza prírodzeného hlasu pre generovanie podcastu

**Podpora hardvéru:**
- ✅ **CPU režim** - Funguje na akomkoľvek modernom počítači (odporúča sa 8GB+ RAM)
- 🚀 **GPU akcelerácia** - Výrazne rýchlejšie inferovanie s NVIDIA/AMD GPU
- ⚡ **Podpora NPU** - Akcelerácia s jednotkou neurónového spracovania novej generácie

**Perfektné pre:**
- Vývojárov, ktorí sa učia systémy AI viacerých agentov
- Každého zaujímajúceho sa o AI automatizáciu a pracovné postupy
- Tvorcov obsahu, ktorí skúmajú AI podporenú produkciu
- Študentov študujúcich praktické vzory AI orchestrácie

**Začni stavať**: [🎙️ Workshop AI Podcast Studio →](./WorkshopForAgentic/README.md)

### 📊 **Zhrnutie učebnej cesty**
- **Celkové trvanie**: 36-45 hodín
- **Začiatočnícka cesta**: Moduly 01-02 (7-9 hodín)  
- **Stredne pokročilá cesta**: Moduly 03-04 (9-11 hodín)
- **Pokročilá cesta**: Moduly 05-07 (12-15 hodín)
- **Expertná cesta**: Modul 08 (8-10 hodín)

## Čo vybuduješ

### 🎯 Kľúčové kompetencie
- **Edge AI architektúra**: Navrhuj AI systémy s dôrazom na lokálne používanie s cloudovou integráciou
- **Optimalizácia modelov**: Kvantizuj a komprimuj modely pre edge nasadenie (85% zrýchlenie, 75% zmenšenie veľkosti)
- **Nasadenie na viacerých platformách**: Windows, mobil, embedded a cloud-edge hybridné systémy
- **Prevádzkové operácie**: Monitorovanie, škálovanie a údržba edge AI v produkcii

### 🏗️ Praktické projekty
- **Foundry Local Chat Apps**: Nativná aplikácia Windows 11 s prepínaním modelov
- **Systémy viacerých agentov**: Koordinátor so špecializovanými agentmi pre komplexné pracovné postupy  
- **RAG aplikácie**: Lokálne spracovanie dokumentov s vektorovým vyhľadávaním
- **Model Routers**: Inteligentný výber medzi modelmi na základe analýzy úloh
- **API frameworky**: Produkčne pripravení klienti s streamovaním a monitorovaním stavu
- **Nástroje pre viaceré platformy**: Vzory integrácie LangChain/Semantic Kernel

### 🏢 Priemyselné aplikácie
**Výroba** • **Zdravotníctvo** • **Autonómne vozidlá** • **Smart Cities** • **Mobilné aplikácie**

## Rýchly začiatok

**Odporúčaná učebná cesta** (20-30 hodín celkom):

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + priemyselný kontext + učebný rámec  
1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelov SLM  
2. **⚙️ Optimalizácia** (Moduly 03-04): Nasadenie + kvantizačné frameworky  
3. **🚀 Produkcia** (Moduly 05-06): SLMOps + AI agenti + volanie funkcií  
4. **💻 Implementácia** (Moduly 07-08): Ukážky platforiem + Foundry Local toolkit

Každý modul obsahuje teóriu, praktické cvičenia a produkčne pripravené ukážky kódu.

## Vplyv na kariéru

**Technické pozície**: Architekt EdgeAI riešení • ML inžinier (Edge) • IoT AI vývojár • Mobilný AI vývojár

**Priemyselné odvetvia**: Výroba 4.0 • Zdravotnícke technológie • Autonómne systémy • FinTech • Spotrebná elektronika

**Portfólio projektov**: Systémy viacerých agentov • Produkčné RAG aplikácie • Viacplatformové nasadenie • Optimalizácia výkonu

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

## Najdôležitejšie body kurzu

✅ **Postupné učenie**: Teória → prax → produkčné nasadenie  
✅ **Reálne prípadové štúdie**: Microsoft, Japan Airlines, podnikové implementácie  
✅ **Praktické príklady**: 50+ príkladov, 10 komplexných demoverzií Foundry Local  
✅ **Zameranie na výkon**: 85% zrýchlenie, 75% zmenšenie veľkosti  
✅ **Viacplatformové**: Windows, mobil, embedded, cloud-edge hybrid  
✅ **Produkčne pripravené**: Monitorovanie, škálovanie, bezpečnosť, súlad s nariadeniami

📖 **[Dostupný študijný sprievodca](STUDY_GUIDE.md)**: Štruktúrovaná 20-hodinová učebná cesta s odporúčaným časovým rozvrhom a nástrojmi na seba-hodnotenie.

---

**EdgeAI predstavuje budúcnosť AI nasadzovania**: lokálne preferované, s dôrazom na súkromie a efektívnosť. Osvoj si tieto zručnosti, aby si mohol/mohla budovať ďalšiu generáciu inteligentných aplikácií.

## Iné kurzy

Náš tím pripravuje aj iné kurzy! Pozri si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pre začiatočníkov](https://img.shields.io/badge/LangChain4j%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pre začiatočníkov](https://img.shields.io/badge/LangChain.js%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pre začiatočníkov](https://img.shields.io/badge/LangChain%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD pre začiatočníkov](https://img.shields.io/badge/AZD%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pre začiatočníkov](https://img.shields.io/badge/Edge%20AI%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pre začiatočníkov](https://img.shields.io/badge/MCP%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti pre začiatočníkov](https://img.shields.io/badge/AI%20Agenti%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatívne AI série
[![Generatívne AI pre začiatočníkov](https://img.shields.io/badge/Generat%C3%ADvne%20AI%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (.NET)](https://img.shields.io/badge/Generat%C3%ADvne%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (Java)](https://img.shields.io/badge/Generat%C3%ADvne%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (JavaScript)](https://img.shields.io/badge/Generat%C3%ADvne%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základné učenie
[![ML pre začiatočníkov](https://img.shields.io/badge/ML%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Dátová veda pre začiatočníkov](https://img.shields.io/badge/Data%20Science%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pre začiatočníkov](https://img.shields.io/badge/AI%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberbezpečnosť pre začiatočníkov](https://img.shields.io/badge/Cybersecurity%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pre začiatočníkov](https://img.shields.io/badge/Web%20Dev%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pre začiatočníkov](https://img.shields.io/badge/IoT%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pre začiatočníkov](https://img.shields.io/badge/XR%20Development%20pre%20za%C4%8Diato%C4%8Dn%C3%ADkov-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot séria
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získanie pomoci

Ak máte problémy alebo otázky o tvorbe aplikácií s AI, pripojte sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu na produkt alebo narazíte na chyby počas vývoja, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou automatizovanej prekladateľskej služby AI [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->