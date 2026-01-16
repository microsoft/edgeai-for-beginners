<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:54:32+00:00",
  "source_file": "README.md",
  "language_code": "cs"
}
-->
# EdgeAI pro začátečníky


![Obrázek obálky kurzu](../../translated_images/cs/cover.eb18d1b9605d754b.png)

[![Přispěvatelé GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR jsou vítány](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Sledovatelé GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forky GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hvězdy GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Postupujte podle těchto kroků, abyste začali používat tyto zdroje:

1. **Zforkujte repozitář**: Klikněte na [![Forky GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Naklonujte repozitář**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Připojte se k Azure AI Foundry Discord a potkejte experty a další vývojáře**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Vícejazyčná podpora

#### Podporováno přes GitHub Action (automatizováno a vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](./README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raději klonovat lokálně?**

> Tento repozitář obsahuje více než 50 jazykových překladů, což výrazně zvětšuje velikost stažení. Pro klonování bez překladů použijte sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tím získáte vše potřebné ke zvládnutí kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Pokud chcete mít podporovány další jazyky, jsou uvedeny [zde](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Úvod

Vítejte u **EdgeAI pro začátečníky** – vašeho komplexního průvodce transformativním světem edge umělé inteligence. Tento kurz překlene propast mezi výkonnými schopnostmi AI a praktickým nasazením v reálném světě na edge zařízeních, díky čemuž můžete využívat potenciál AI přímo tam, kde jsou data generována a kde je třeba činit rozhodnutí.

### Co se naučíte

Kurz vás provede od základních konceptů po produkčně připravená řešení a zahrnuje:
- **Malé jazykové modely (SLM)** optimalizované pro nasazení na edge zařízení
- **Optimalizaci citlivou na hardware** pro různé platformy
- **Real-time inferenci** s ochranou soukromí
- **Strategie produkčního nasazení** pro podnikové aplikace

### Proč je EdgeAI důležité

Edge AI představuje posun paradigmat, který řeší klíčové moderní výzvy:
- **Soukromí a bezpečnost**: Zpracování citlivých dat lokálně bez vystavení v cloudu
- **Výkon v reálném čase**: Eliminace latence sítě u aplikací kritických na čas
- **Nákladová efektivita**: Snížení nákladů na šířku pásma a cloudové výpočty
- **Odolný provoz**: Zachování funkčnosti během výpadků sítě
- **Soulad s regulacemi**: Splnění požadavků na suverenitu dat

### Edge AI

Edge AI znamená provozování AI algoritmů a jazykových modelů lokálně na hardwaru, blízko místa generování dat, bez závislosti na cloudových zdrojích pro inferenci. Snižuje latenci, zvyšuje soukromí a umožňuje rozhodování v reálném čase.

### Základní principy:
- **Inferencování na zařízení**: AI modely běží na edge zařízeních (telefony, routery, mikrokontroléry, průmyslové PC)
- **Offline schopnost**: Fungování bez trvalého internetového připojení
- **Nízká latence**: Okamžité reakce vhodné pro systémy v reálném čase
- **Suverenita dat**: Citlivá data zůstávají lokálně, čímž se zlepšuje bezpečnost a soulad

### Malé jazykové modely (SLM)

SLM jako Phi-4, Mistral-7B a Gemma jsou optimalizované verze větších LLM – trénované nebo distilované pro:
- **Sníženou paměťovou náročnost**: Efektivní využití omezené paměti edge zařízení
- **Nižší požadavky na výpočetní výkon**: Optimalizované pro CPU a edge GPU výkon
- **Rychlejší starty**: Rychlá inicializace pro aplikace vyžadující okamžitou odezvu

Umožňují silné NLP schopnosti a přitom splňují omezení:
- **Vestavěné systémy**: IoT zařízení a průmyslové kontroléry
- **Mobilní zařízení**: Chytré telefony a tablety s offline schopnostmi
- **IoT zařízení**: Senzory a chytrá zařízení s omezenými zdroji
- **Edge servery**: Lokální jednotky s omezenými GPU zdroji
- **Osobní počítače**: Scénáře nasazení na desktop a laptop

## Moduly kurzu a navigace

| Modul | Téma | Oblast zaměření | Klíčový obsah | Úroveň | Doba trvání |
|--------|-------|----------------|--------------|--------|-------------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy a kontext | Přehled EdgeAI • Průmyslové aplikace • Úvod do SLM • Cíle učení | Začátečník | 1-2 hodiny |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Srovnání cloud vs edge AI | Základy EdgeAI • Případové studie z praxe • Průvodce implementací • Nasazení na edge | Začátečník | 3-4 hodiny |
| [🧠 02](../../Module02) | [Základy SLM modelů](./Module02/README.md) | Rodiny modelů a architektura | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začátečník | 4-5 hodin |
| [🚀 03](../../Module03) | [Praxe nasazení SLM](./Module03/README.md) | Lokální a cloudové nasazení | Pokročilé učení • Lokální prostředí • Cloudové nasazení | Středně pokročilý | 4-5 hodin |
| [⚙️ 04](../../Module04) | [Nástroje pro optimalizaci modelů](./Module04/README.md) | Optimalizace napříč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza workflow | Středně pokročilý | 5-6 hodin |
| [🔧 05](../../Module05) | [SLMOps v produkci](./Module05/README.md) | Produkční provoz | Úvod do SLMOps • Distilace modelů • Doladění • Produkční nasazení | Pokročilý | 5-6 hodin |
| [🤖 06](../../Module06) | [AI agenti & volání funkcí](./Module06/README.md) | Rámce agentů a MCP | Úvod do agentů • Volání funkcí • Protokol modelového kontextu | Pokročilý | 4-5 hodin |
| [💻 07](../../Module07) | [Implementace platformy](./Module07/README.md) | Vzorky napříč platformami | AI Toolkit • Foundry Local • Vývoj pro Windows | Pokročilý | 3-4 hodiny |
| [🏭 08](../../Module08) | [Nástroje Foundry Local](./Module08/README.md) | Produkčně připravené vzorky | Ukázkové aplikace (viz podrobnosti níže) | Expert | 8-10 hodin |

### 🏭 **Modul 08: Ukázkové aplikace**

- [01: Rychlý start REST chatu](./Module08/samples/01/README.md)
- [02: Integrace OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objevování modelů & benchmarky](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikace](./Module08/samples/04/README.md)
- [05: Orchestrace multi-agentů](./Module08/samples/05/README.md)
- [06: Router modelů jako nástrojů](./Module08/samples/06/README.md)
- [07: Přímý API klient](./Module08/samples/07/README.md)
- [08: Chat aplikace pro Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý multi-agentní systém](./Module08/samples/09/README.md)
- [10: Framework Foundry nástrojů](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická výuka**

Komplexní praktické materiály s produkčně připravenými implementacemi:

- **[Průvodce workshopem](./Workshop/Readme.md)** - Kompletní cíle učení, výstupy a navigace zdrojů
- **Python ukázky** (6 sezení) - Aktualizované o nejlepší postupy, zpracování chyb a komplexní dokumentaci
- **Jupyter notebooky** (8 interaktivních) - Podrobné návody krok za krokem s benchmarky a sledováním výkonu
- **Průvodce sezeními** - Detailní markdown průvodci pro každé sezení workshopu
- **Nástroje pro validaci** - Skripty pro ověřování kvality kódu a spuštění prvotních testů

**Co vytvoříte:**
- Lokální AI chat aplikace s podporou streamování
- RAG pipeline s hodnocením kvality (RAGAS)
- Nástroje pro benchmark a porovnání více modelů
- Systémy orchestrace multi-agentů
- Inteligentní směrování modelů s výběrem podle úkolu

### 🎙️ **Workshop Agentic: Prakticky - AI podcastové studio**

Postavte si pipeline produkce podcastů řízenou AI od začátku! Tento pohlcující workshop vás naučí vytvořit kompletní multi-agentní systém, který promění nápady do profesionálních epizod podcastu.
**[🎬 Začněte workshop AI podcastového studia](./WorkshopForAgentic/README.md)**

**Vaše mise**: Spusťte "Future Bytes" — technologický podcast zcela poháněný AI agenty, které si sami vytvoříte. Žádné závislosti na cloudu, žádné náklady na API — vše běží lokálně na vašem počítači.

**Co dělá toto unikátním:**
- **🤖 Skutečná multi-agentní orchestraci** - Vytvořte specializované AI agenty, kteří zkoumají, píší a produkují audio
- **🎯 Kompletní produkční proces** - Od výběru tématu až po finální audio podcastu
- **💻 100% lokální nasazení** - Používá Ollama a lokální modely (Qwen-3-8B) pro plné soukromí a kontrolu
- **🎤 Integrace text-hlas** - Přeměna skriptů na přirozeně znějící konverzace s více mluvčími
- **✋ Workflow s lidským schvalováním** - Kontrolní brány zajišťují kvalitu při zachování automatizace

**Tříaktová vzdělávací cesta:**

| Akt | Zaměření | Klíčové dovednosti | Doba trvání |
|-----|----------|--------------------|-------------|
| **[Akt 1: Poznejte své AI asistenty](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Vytvoření prvního AI agenta | Integrace nástrojů • Vyhledávání na webu • Řešení problémů • Agentní uvažování | 2-3 hodiny |
| **[Akt 2: Sestavte svůj produkční tým](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestrace více agentů | Koordinace týmu • Workflows schvalování • Rozhraní DevUI • Lidský dohled | 3-4 hodiny |
| **[Akt 3: Oživte svůj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generování podcastového audia | Text-hlas • Syntéza vícemluvčích • Dlouhý formát • Plná automatizace | 2-3 hodiny |

**Použité technologie:**
- **Microsoft Agent Framework** - Orchestrace a koordinace multi-agentních systémů
- **Ollama** - Lokální runtime AI modelů (bez potřeby cloudu)
- **Qwen-3-8B** - Open source jazykový model optimalizovaný pro agentní úlohy
- **API pro text-hlas** - Přirozená syntéza hlasu pro generování podcastů

**Podpora hardwaru:**
- ✅ **Režim CPU** - Funguje na jakémkoli moderním počítači (doporučeno 8GB+ RAM)
- 🚀 **GPU akcelerace** - Výrazně rychlejší inferenční výkon s NVIDIA/AMD GPU
- ⚡ **Podpora NPU** - Akcelerace pomocí nové generace neuronových procesorů

**Ideální pro:**
- Vývojáře učící se multi-agentním AI systémům
- Každého se zájmem o AI automatizaci a workflow
- Tvůrce obsahu zkoumající AI asistovanou produkci
- Studenty studující praktické vzory orchestrací AI

**Začněte budovat**: [🎙️ Workshop AI podcastového studia →](./WorkshopForAgentic/README.md)

### 📊 **Shrnutí vzdělávací cesty**
- **Celková délka:** 36-45 hodin
- **Začátečnická cesta:** Moduly 01-02 (7-9 hodin)  
- **Středně pokročilá cesta:** Moduly 03-04 (9-11 hodin)
- **Pokročilá cesta:** Moduly 05-07 (12-15 hodin)
- **Expertní cesta:** Modul 08 (8-10 hodin)

## Co vybudujete

### 🎯 Základní kompetence
- **Edge AI architektura**: Navrhujte AI systémy výhradně lokálně s cloudovou integrací
- **Optimalizace modelů**: Kvantizace a komprese modelů pro nasazení na okraji (rychlost +85 %, velikost -75 %)
- **Víceplatformní nasazení**: Windows, mobilní zařízení, embedded a cloud-edge hybridní systémy
- **Produkční operace**: Monitorování, škálování a udržování edge AI v produkci

### 🏗️ Praktické projekty
- **Foundry Lokální chat aplikace**: Nativní aplikace pro Windows 11 s přepínáním modelů
- **Multi-agentní systémy**: Koordinátor s specialisty pro složité workflow  
- **RAG aplikace**: Lokální zpracování dokumentů s vektorovým vyhledáváním
- **Model Routery**: Inteligentní výběr modelu na základě analýzy úlohy
- **API frameworky**: Produkčně připravení klienti s podporou streamingu a monitoringu zdraví
- **Nástroje pro víceplatforemní použití**: Integrace LangChain/Semantic Kernel

### 🏢 Průmyslové aplikace
**Výroba** • **Zdravotnictví** • **Autonomní vozidla** • **Chytrá města** • **Mobilní aplikace**

## Rychlý start

**Doporučená vzdělávací cesta** (20-30 hodin celkem):

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + průmyslový kontext + vzdělávací rámec
1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelů SLM
2. **⚙️ Optimalizace** (Moduly 03-04): Nasazení + kvantizační frameworky  
3. **🚀 Produkce** (Moduly 05-06): SLMOps + AI agenti + volání funkcí
4. **💻 Realizace** (Moduly 07-08): Ukázky platforem + Foundry Local toolkit

Každý modul obsahuje teorii, praktická cvičení a produkčně připravené ukázky kódu.

## Kariérní dopad

**Technické role**: EdgeAI Solutions Architect • ML inženýr (Edge) • IoT AI vývojář • Mobilní AI vývojář

**Průmyslové sektory**: Výroba 4.0 • Zdravotnické technologie • Autonomní systémy • FinTech • Spotřební elektronika

**Portfoliové projekty**: Multi-agentní systémy • Produkční RAG aplikace • Víceplatformní nasazení • Optimalizace výkonu

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

## Klíčové body kurzu

✅ **Progresivní učení**: Teorie → Praxe → Produkční nasazení  
✅ **Skutečné případové studie**: Microsoft, Japan Airlines, podniková nasazení  
✅ **Praktické ukázky**: 50+ příkladů, 10 komplexních demonstrací Foundry Local  
✅ **Zaměření na výkon**: Zrychlení o 85 %, snížení velikosti o 75 %  
✅ **Víceplatformní**: Windows, mobilní zařízení, embedded, cloud-edge hybrid  
✅ **Produkčně připravené**: Monitorování, škálování, zabezpečení, dodržování pravidel

📖 **[Dostupný studijní průvodce](STUDY_GUIDE.md)**: Strukturovaná 20hodinová vzdělávací cesta s doporučením časového rozvrhu a nástroji pro sebehodnocení.

---

**EdgeAI představuje budoucnost nasazení AI**: lokálně prioritní, zachovávající soukromí a efektivní. Ovládněte tyto dovednosti a vytvořte generaci inteligentních aplikací.

## Další kurzy

Náš tým produkuje i další kurzy! Podívejte se na:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pro začátečníky](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pro začátečníky](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD pro začátečníky](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pro začátečníky](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pro začátečníky](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti pro začátečníky](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série generativní AI
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní vzdělávání
[![ML pro začátečníky](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberbezpečnost pro začátečníky](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Vývoj XR pro začátečníky](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot pro AI párové programování](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získání pomoci

Pokud uvíznete nebo máte jakékoli otázky ohledně vytváření AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte připomínky k produktu nebo narazíte na chyby při vývoji, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->