<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e61ee5b6cb0bff11495c72afb37a9e8",
  "translation_date": "2025-11-11T17:07:51+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# EdgeAI pre začiatočníkov

![Obrázok obalu kurzu](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sk.png)

[![Prispievatelia na GitHube](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHube](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull-requests na GitHube](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Postupujte podľa týchto krokov, aby ste mohli začať používať tieto zdroje:

1. **Forknite repozitár**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonujte repozitár**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pripojte sa k Azure AI Foundry Discord a stretnite sa s odborníkmi a ďalšími vývojármi**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (Automatizované a vždy aktuálne)

[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Mjanmarsko)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézčina](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigérijský pidžin](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

**Ak chcete podporu ďalších jazykov, zoznam podporovaných jazykov nájdete [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Úvod

Vitajte v **EdgeAI pre začiatočníkov** – vašej komplexnej ceste do transformačného sveta Edge umelej inteligencie. Tento kurz spája silné schopnosti AI s praktickým nasadením v reálnom svete na edge zariadeniach, čo vám umožní využiť potenciál AI priamo tam, kde sa generujú dáta a kde je potrebné robiť rozhodnutia.

### Čo sa naučíte

Tento kurz vás prevedie od základných konceptov až po implementácie pripravené na produkciu, pokrývajúc:
- **Malé jazykové modely (SLMs)** optimalizované pre nasadenie na edge zariadeniach
- **Optimalizáciu zohľadňujúcu hardvér** na rôznych platformách
- **Inferenčné procesy v reálnom čase** s ochranou súkromia
- **Stratégie nasadenia do produkcie** pre podnikové aplikácie

### Prečo je EdgeAI dôležitá

Edge AI predstavuje zmenu paradigmy, ktorá rieši kritické moderné výzvy:
- **Súkromie a bezpečnosť**: Spracovanie citlivých údajov lokálne bez vystavenia cloudu
- **Výkon v reálnom čase**: Eliminácia oneskorenia siete pre aplikácie kritické na čas
- **Efektívnosť nákladov**: Zníženie nákladov na šírku pásma a cloudové výpočty
- **Odolnosť operácií**: Zachovanie funkčnosti počas výpadkov siete
- **Regulačné požiadavky**: Splnenie požiadaviek na suverenitu údajov

### Edge AI

Edge AI sa týka spúšťania algoritmov AI a jazykových modelov lokálne na hardvéri, blízko miesta, kde sa generujú dáta, bez závislosti na cloudových zdrojoch pre inferenciu. Znižuje latenciu, zvyšuje súkromie a umožňuje rozhodovanie v reálnom čase.

### Základné princípy:
- **Inferencia na zariadení**: AI modely bežia na edge zariadeniach (telefóny, routery, mikrokontroléry, priemyselné PC)
- **Offline schopnosti**: Funguje bez trvalého pripojenia na internet
- **Nízka latencia**: Okamžité reakcie vhodné pre systémy v reálnom čase
- **Suverenita údajov**: Uchováva citlivé údaje lokálne, čím zlepšuje bezpečnosť a súlad s predpismi

### Malé jazykové modely (SLMs)

SLMs ako Phi-4, Mistral-7B a Gemma sú optimalizované verzie väčších LLMs – trénované alebo destilované pre:
- **Zníženú pamäťovú náročnosť**: Efektívne využitie obmedzenej pamäte edge zariadení
- **Nižšie výpočtové požiadavky**: Optimalizované pre výkon CPU a edge GPU
- **Rýchlejšie spúšťanie**: Rýchla inicializácia pre responzívne aplikácie

Odomykajú silné schopnosti NLP pri splnení obmedzení:
- **Vstavané systémy**: IoT zariadenia a priemyselné kontroléry
- **Mobilné zariadenia**: Smartfóny a tablety s offline schopnosťami
- **IoT zariadenia**: Senzory a inteligentné zariadenia s obmedzenými zdrojmi
- **Edge servery**: Lokálne spracovacie jednotky s obmedzenými GPU zdrojmi
- **Osobné počítače**: Scenáre nasadenia na desktopoch a notebookoch

## Moduly kurzu a navigácia

| Modul | Téma | Oblasť zamerania | Kľúčový obsah | Úroveň | Trvanie |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy a kontext | Prehľad EdgeAI • Priemyselné aplikácie • Úvod do SLM • Ciele učenia | Začiatočník | 1-2 hod |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnanie Cloud vs Edge AI | Základy EdgeAI • Prípadové štúdie z reálneho sveta • Príručka implementácie • Nasadenie na edge | Začiatočník | 3-4 hod |
| [🧠 02](../../Module02) | [Základy modelov SLM](./Module02/README.md) | Rodiny modelov a architektúra | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začiatočník | 4-5 hod |
| [🚀 03](../../Module03) | [Praxe nasadenia SLM](./Module03/README.md) | Lokálne a cloudové nasadenie | Pokročilé učenie • Lokálne prostredie • Cloudové nasadenie | Stredne pokročilý | 4-5 hod |
| [⚙️ 04](../../Module04) | [Toolkit optimalizácie modelov](./Module04/README.md) | Optimalizácia naprieč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza pracovného toku | Stredne pokročilý | 5-6 hod |
| [🔧 05](../../Module05) | [SLMOps Produkcia](./Module05/README.md) | Produkčné operácie | Úvod do SLMOps • Destilácia modelov • Jemné doladenie • Nasadenie do produkcie | Pokročilý | 5-6 hod |
| [🤖 06](../../Module06) | [AI agenti a volanie funkcií](./Module06/README.md) | Rámce agentov & MCP | Úvod do agentov • Volanie funkcií • Protokol kontextu modelu | Pokročilý | 4-5 hod |
| [💻 07](../../Module07) | [Implementácia na platforme](./Module07/README.md) | Ukážky naprieč platformami | AI Toolkit • Foundry Local • Vývoj na Windows | Pokročilý | 3-4 hod |
| [🏭 08](../../Module08) | [Toolkit Foundry Local](./Module08/README.md) | Ukážky pripravené na produkciu | Ukážkové aplikácie (pozri detaily nižšie) | Expert | 8-10 hod |

### 🏭 **Modul 08: Ukážkové aplikácie**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integrácia OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objavovanie modelov a benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikácia](./Module08/samples/04/README.md)
- [05: Orchestrácia viacerých agentov](./Module08/samples/05/README.md)
- [06: Router modelov ako nástrojov](./Module08/samples/06/README.md)
- [07: Priamy API klient](./Module08/samples/07/README.md)
- [08: Chat aplikácia pre Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý systém viacerých agentov](./Module08/samples/09/README.md)
- [10: Rámec nástrojov Foundry](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická cesta učenia**

Komplexné materiály pre praktický workshop s implementáciami pripravenými na produkciu:

- **[Príručka workshopu](./Workshop/Readme.md)** - Kompletné ciele učenia, výsledky a navigácia zdrojov
- **Python ukážky** (6 relácií) - Aktualizované s najlepšími postupmi, spracovaním chýb a komplexnou dokumentáciou
- **Jupyter Notebooks** (8 interaktívnych) - Krok za krokom tutoriály s benchmarkmi a monitorovaním výkonu
- **Príručky relácií** - Podrobné markdown príručky pre každú reláciu workshopu
- **Nástroje validácie** - Skripty na overenie kvality kódu a spustenie testov

**Čo vytvoríte:**
- Lokálne AI chat aplikácie s podporou streamovania
- RAG pipeline s hodnotením kvality (RAGAS)
- Nástroje na benchmarking a porovnanie viacerých modelov
- Systémy orchestrácie viacerých agentov
- Inteligentné smerovanie modelov s výberom na základe úloh

### 📊 **Zhrnutie cesty učenia**
- **Celková dĺžka**: 36-45 hodín
- **Cesta pre začiatočníkov**: Moduly 01-02 (7-9 hodín)  
- **Cesta pre stredne pokročilých**: Moduly 03-04 (9-11 hodín)
- **Cesta pre pokročilých**: Moduly 05-07 (12-15 hodín)
- **Cesta pre expertov**: Modul 08 (8-10 hodín)

## Čo vytvoríte

### 🎯 Kľúčové kompetencie
- **Architektúra Edge AI**: Navrhnite systémy AI orientované na lokálne spracovanie s integráciou cloudu
- **Optimalizácia modelov**: Kvantizujte a komprimujte modely pre nasadenie na edge zariadeniach (85% zrýchlenie, 75% zníženie veľkosti)
- **Nasadenie na viacerých platformách**: Windows, mobilné zariadenia, zabudované systémy a hybridné cloud-edge systémy  
- **Prevádzka v produkcii**: Monitorovanie, škálovanie a údržba edge AI v produkčnom prostredí  

### 🏗️ Praktické projekty  
- **Foundry Local Chat Apps**: Natívna aplikácia pre Windows 11 s prepínaním modelov  
- **Systémy s viacerými agentmi**: Koordinátor so špecializovanými agentmi pre komplexné pracovné postupy  
- **RAG aplikácie**: Lokálne spracovanie dokumentov s vyhľadávaním pomocou vektorov  
- **Modelové smerovače**: Inteligentný výber medzi modelmi na základe analýzy úloh  
- **API rámce**: Klienti pripravení na produkciu so streamovaním a monitorovaním stavu  
- **Nástroje pre viaceré platformy**: Vzory integrácie LangChain/Semantic Kernel  

### 🏢 Priemyselné aplikácie  
**Výroba** • **Zdravotníctvo** • **Autonómne vozidlá** • **Inteligentné mestá** • **Mobilné aplikácie**  

## Rýchly štart  

**Odporúčaný študijný plán** (celkovo 20-30 hodín):  

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + kontext priemyslu + rámec učenia  
1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelov SLM  
2. **⚙️ Optimalizácia** (Moduly 03-04): Nasadenie + rámce kvantizácie  
3. **🚀 Produkcia** (Moduly 05-06): SLMOps + AI agenti + volanie funkcií  
4. **💻 Implementácia** (Moduly 07-08): Ukážky platforiem + Foundry Local toolkit  

Každý modul obsahuje teóriu, praktické cvičenia a ukážky kódu pripravené na produkciu.  

## Dopad na kariéru  

**Technické pozície**: Architekt riešení EdgeAI • ML inžinier (Edge) • IoT AI vývojár • Mobilný AI vývojár  

**Priemyselné sektory**: Výroba 4.0 • Zdravotnícka technológia • Autonómne systémy • FinTech • Spotrebná elektronika  

**Portfólio projektov**: Systémy s viacerými agentmi • Produkčné RAG aplikácie • Nasadenie na viacerých platformách • Optimalizácia výkonu  

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

✅ **Progresívne učenie**: Teória → Prax → Nasadenie v produkcii  
✅ **Skutočné prípadové štúdie**: Microsoft, Japan Airlines, implementácie v podnikoch  
✅ **Praktické ukážky**: Viac ako 50 príkladov, 10 komplexných Foundry Local demo projektov  
✅ **Zameranie na výkon**: Zlepšenie rýchlosti o 85 %, zníženie veľkosti o 75 %  
✅ **Viacero platforiem**: Windows, mobilné zariadenia, zabudované systémy, hybridné cloud-edge  
✅ **Pripravené na produkciu**: Monitorovanie, škálovanie, bezpečnosť, rámce súladu  

📖 **[Študijný sprievodca k dispozícii](STUDY_GUIDE.md)**: Štruktúrovaný 20-hodinový študijný plán s odporúčaním časového rozvrhu a nástrojmi na sebahodnotenie.  

---  

**EdgeAI predstavuje budúcnosť nasadenia AI**: lokálne orientované, zachovávajúce súkromie a efektívne. Ovládnite tieto zručnosti a vytvorte ďalšiu generáciu inteligentných aplikácií.  

## Ďalšie kurzy  

Náš tím vytvára aj ďalšie kurzy! Pozrite si:  

### Azure / Edge / MCP / Agent  
[![AZD pre začiatočníkov](https://img.shields.io/badge/AZD%20pre%20začiatočníkov-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI pre začiatočníkov](https://img.shields.io/badge/Edge%20AI%20pre%20začiatočníkov-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP pre začiatočníkov](https://img.shields.io/badge/MCP%20pre%20začiatočníkov-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI agenti pre začiatočníkov](https://img.shields.io/badge/AI%20agenti%20pre%20začiatočníkov-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---  

### Generatívna AI séria  
[![Generatívna AI pre začiatočníkov](https://img.shields.io/badge/Generatívna%20AI%20pre%20začiatočníkov-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generatívna AI (.NET)](https://img.shields.io/badge/Generatívna%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generatívna AI (Java)](https://img.shields.io/badge/Generatívna%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generatívna AI (JavaScript)](https://img.shields.io/badge/Generatívna%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---  

### Základné učenie  
[![ML pre začiatočníkov](https://img.shields.io/badge/ML%20pre%20začiatočníkov-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science pre začiatočníkov](https://img.shields.io/badge/Data%20Science%20pre%20začiatočníkov-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI pre začiatočníkov](https://img.shields.io/badge/AI%20pre%20začiatočníkov-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Kybernetická bezpečnosť pre začiatočníkov](https://img.shields.io/badge/Kybernetická%20bezpečnosť%20pre%20začiatočníkov-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Webový vývoj pre začiatočníkov](https://img.shields.io/badge/Webový%20vývoj%20pre%20začiatočníkov-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT pre začiatočníkov](https://img.shields.io/badge/IoT%20pre%20začiatočníkov-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR vývoj pre začiatočníkov](https://img.shields.io/badge/XR%20vývoj%20pre%20začiatočníkov-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---  

### Copilot séria  
[![Copilot pre AI párové programovanie](https://img.shields.io/badge/Copilot%20pre%20AI%20párové%20programovanie-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot pre C#/.NET](https://img.shields.io/badge/Copilot%20pre%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

## Získanie pomoci  

Ak narazíte na problém alebo máte otázky ohľadom budovania AI aplikácií, pridajte sa:  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

Ak máte spätnú väzbu k produktu alebo narazíte na chyby pri budovaní, navštívte:  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->