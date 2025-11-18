<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e49c901b8a8e953904d655ae4630bfe",
  "translation_date": "2025-11-18T18:05:31+00:00",
  "source_file": "README.md",
  "language_code": "cs"
}
-->
# EdgeAI pro začátečníky

![Obrázek kurzu](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.cs.png)

[![Přispěvatelé na GitHubu](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHubu](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty na GitHubu](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Sledující na GitHubu](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hvězdičky na GitHubu](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Postupujte podle těchto kroků, abyste mohli začít používat tyto zdroje:

1. **Forkněte repozitář**: Klikněte [![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Naklonujte repozitář**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Připojte se na Discord Azure AI Foundry a setkejte se s odborníky a dalšími vývojáři**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podpora více jazyků

#### Podporováno prostřednictvím GitHub Action (automatizované a vždy aktuální)

[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmština (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradiční, Hongkong)](../hk/README.md) | [Čínština (tradiční, Macao)](../mo/README.md) | [Čínština (tradiční, Tchaj-wan)](../tw/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijský pidgin](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Farsi)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../br/README.md) | [Portugalština (Portugalsko)](../pt/README.md) | [Panjábština (Gurmukhi)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (Filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)

**Pokud si přejete přidat další překlady, seznam podporovaných jazyků najdete [zde](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Úvod

Vítejte v **EdgeAI pro začátečníky** – komplexní cestě do světa Edge umělé inteligence. Tento kurz propojuje výkonné schopnosti AI s praktickým nasazením na edge zařízeních, což vám umožní využít potenciál AI přímo tam, kde se data generují a kde je třeba činit rozhodnutí.

### Co se naučíte

Tento kurz vás provede od základních konceptů až po implementace připravené pro produkci, včetně:
- **Malých jazykových modelů (SLMs)** optimalizovaných pro nasazení na edge
- **Optimalizace s ohledem na hardware** na různých platformách
- **Inferencí v reálném čase** s ochranou soukromí
- **Strategií nasazení** pro podnikové aplikace

### Proč je EdgeAI důležité

Edge AI představuje změnu paradigmatu, která řeší klíčové moderní výzvy:
- **Soukromí a bezpečnost**: Zpracování citlivých dat lokálně bez vystavení cloudu
- **Výkon v reálném čase**: Eliminace latence sítě pro aplikace kritické na čas
- **Efektivita nákladů**: Snížení nákladů na šířku pásma a cloudové výpočty
- **Odolnost**: Funkčnost i při výpadcích sítě
- **Regulační shoda**: Splnění požadavků na suverenitu dat

### Edge AI

Edge AI znamená provozování AI algoritmů a jazykových modelů lokálně na hardwaru, blízko místa, kde se data generují, bez závislosti na cloudových zdrojích pro inferenci. Snižuje latenci, zvyšuje soukromí a umožňuje rozhodování v reálném čase.

### Základní principy:
- **Inferencí na zařízení**: AI modely běží na edge zařízeních (telefony, routery, mikrokontroléry, průmyslové PC)
- **Offline schopnosti**: Funguje bez trvalého připojení k internetu
- **Nízká latence**: Okamžité reakce vhodné pro systémy v reálném čase
- **Suverenita dat**: Udržuje citlivá data lokálně, zlepšuje bezpečnost a shodu

### Malé jazykové modely (SLMs)

SLMs jako Phi-4, Mistral-7B a Gemma jsou optimalizované verze větších LLMs – trénované nebo destilované pro:
- **Snížené nároky na paměť**: Efektivní využití omezené paměti edge zařízení
- **Nižší výpočetní nároky**: Optimalizace pro výkon CPU a edge GPU
- **Rychlejší start**: Rychlá inicializace pro pohotové aplikace

Umožňují výkonné NLP schopnosti při splnění omezení:
- **Vestavěné systémy**: IoT zařízení a průmyslové kontroléry
- **Mobilní zařízení**: Smartphony a tablety s offline schopnostmi
- **IoT zařízení**: Senzory a chytrá zařízení s omezenými zdroji
- **Edge servery**: Lokální zpracovatelské jednotky s omezenými GPU zdroji
- **Osobní počítače**: Scénáře nasazení na desktopu a notebooku

## Moduly kurzu a navigace

| Modul | Téma | Oblast zaměření | Klíčový obsah | Úroveň | Délka |
|-------|------|-----------------|---------------|--------|-------|
| [📖 00 ](./introduction.md) | [Úvod do EdgeAI](./introduction.md) | Základy a kontext | Přehled EdgeAI • Průmyslové aplikace • Úvod do SLM • Cíle učení | Začátečník | 1-2 hod |
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnání cloud vs Edge AI | Základy EdgeAI • Případové studie • Průvodce implementací • Nasazení na edge | Začátečník | 3-4 hod |
| [🧠 02](../../Module02) | [Základy modelů SLM](./Module02/README.md) | Rodiny modelů a architektura | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začátečník | 4-5 hod |
| [🚀 03](../../Module03) | [Praxe nasazení SLM](./Module03/README.md) | Lokální a cloudové nasazení | Pokročilé učení • Lokální prostředí • Cloudové nasazení | Středně pokročilý | 4-5 hod |
| [⚙️ 04](../../Module04) | [Toolkit pro optimalizaci modelů](./Module04/README.md) | Optimalizace napříč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Syntéza workflow | Středně pokročilý | 5-6 hod |
| [🔧 05](../../Module05) | [SLMOps v produkci](./Module05/README.md) | Produkční operace | Úvod do SLMOps • Destilace modelů • Doladění • Produkční nasazení | Pokročilý | 5-6 hod |
| [🤖 06](../../Module06) | [AI agenti a volání funkcí](./Module06/README.md) | Rámce agentů a MCP | Úvod do agentů • Volání funkcí • Protokol kontextu modelu | Pokročilý | 4-5 hod |
| [💻 07](../../Module07) | [Implementace na platformě](./Module07/README.md) | Ukázky napříč platformami | AI Toolkit • Foundry Local • Vývoj na Windows | Pokročilý | 3-4 hod |
| [🏭 08](../../Module08) | [Toolkit Foundry Local](./Module08/README.md) | Ukázky připravené pro produkci | Ukázkové aplikace (viz podrobnosti níže) | Expert | 8-10 hod |

### 🏭 **Modul 08: Ukázkové aplikace**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integrace OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objevování modelů a benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikace](./Module08/samples/04/README.md)
- [05: Orchestrace více agentů](./Module08/samples/05/README.md)
- [06: Router modelů jako nástrojů](./Module08/samples/06/README.md)
- [07: Přímý API klient](./Module08/samples/07/README.md)
- [08: Chatovací aplikace pro Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý systém více agentů](./Module08/samples/09/README.md)
- [10: Rámec nástrojů Foundry](./Module08/samples/10/README.md)

### 🎓 **Workshop: Praktická cesta učení**

Komplexní materiály pro praktický workshop s implementacemi připravenými pro produkci:

- **[Průvodce workshopem](./Workshop/Readme.md)** - Kompletní cíle učení, výsledky a navigace zdrojů
- **Python ukázky** (6 sezení) - Aktualizováno s osvědčenými postupy, zpracováním chyb a komplexní dokumentací
- **Jupyter Notebooks** (8 interaktivních) - Krok za krokem tutoriály s benchmarky a monitorováním výkonu
- **Průvodce sezeními** - Podrobné markdown průvodce pro každé sezení workshopu
- **Nástroje pro validaci** - Skripty pro ověření kvality kódu a provedení rychlých testů

**Co vytvoříte:**
- Lokální AI chatovací aplikace s podporou streamování
- RAG pipeline s hodnocením kvality (RAGAS)
- Nástroje pro benchmarking a porovnání více modelů
- Systémy orchestrace více agentů
- Inteligentní směrování modelů s výběrem na základě úkolů

### 📊 **Shrnutí cesty učení**
- **Celková délka**: 36-45 hodin
- **Cesta pro začátečníky**: Moduly 01-02 (7-9 hodin)  
- **Cesta pro středně pokročilé**: Moduly 03-04 (9-11 hodin)
- **Cesta pro pokročilé**: Moduly 05-07 (12-15 hodin)
- **Cesta pro experty**: Modul 08 (8-10 hodin)

## Co vytvoříte

### 🎯 Klíčové dovednosti
- **Architektura Edge AI**: Navrhování AI systémů s lokálním zaměřením a integrací cloudu
- **Optimalizace modelů**: Kvantizace a komprese modelů pro nasazení na edge (85% zrychlení, 75% snížení velikosti)
- **Nasazení na více platformách**: Windows, mobilní zařízení, vestavěné systémy a hybridní systémy cloud-edge
- **Provoz v produkci**: Monitorování, škálování a údržba edge AI v produkčním prostředí

### 🏗️ Praktické projekty
- **Foundry Local Chat Apps**: Nativní aplikace pro Windows 11 s přepínáním modelů
- **Multi-Agent Systems**: Koordinátor se specializovanými agenty pro komplexní pracovní postupy  
- **RAG Applications**: Lokální zpracování dokumentů s vektorovým vyhledáváním
- **Model Routers**: Inteligentní výběr mezi modely na základě analýzy úkolů
- **API Frameworks**: Klienti připravení pro produkci se streamováním a monitorováním stavu
- **Cross-Platform Tools**: Vzory integrace LangChain/Semantic Kernel

### 🏢 Průmyslové aplikace
**Výroba** • **Zdravotnictví** • **Autonomní vozidla** • **Chytrá města** • **Mobilní aplikace**

## Rychlý start

**Doporučená učební cesta** (celkem 20-30 hodin):

0. **📖 Úvod** ([Introduction.md](./introduction.md)): Základy EdgeAI + průmyslový kontext + učební rámec
1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelů SLM
2. **⚙️ Optimalizace** (Moduly 03-04): Nasazení + kvantizační rámce  
3. **🚀 Produkce** (Moduly 05-06): SLMOps + AI agenti + volání funkcí
4. **💻 Implementace** (Moduly 07-08): Ukázky platforem + nástroje Foundry Local

Každý modul obsahuje teorii, praktická cvičení a ukázky kódu připravené pro produkci.

## Dopad na kariéru

**Technické role**: Architekt řešení EdgeAI • ML inženýr (Edge) • Vývojář IoT AI • Vývojář mobilní AI

**Průmyslové sektory**: Výroba 4.0 • Zdravotnické technologie • Autonomní systémy • FinTech • Spotřební elektronika

**Portfolio projektů**: Multi-agentní systémy • Produkční RAG aplikace • Nasazení napříč platformami • Optimalizace výkonu

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

✅ **Progresivní učení**: Teorie → Praxe → Nasazení v produkci  
✅ **Skutečné případové studie**: Microsoft, Japan Airlines, podnikové implementace  
✅ **Praktické ukázky**: 50+ příkladů, 10 komplexních ukázek Foundry Local  
✅ **Zaměření na výkon**: Zlepšení rychlosti o 85 %, snížení velikosti o 75 %  
✅ **Multi-platformní**: Windows, mobilní zařízení, embedded systémy, hybridní cloud-edge  
✅ **Připraveno pro produkci**: Monitorování, škálování, bezpečnost, rámce pro dodržování předpisů

📖 **[Studijní průvodce k dispozici](STUDY_GUIDE.md)**: Strukturovaná učební cesta na 20 hodin s doporučením časového rozvrhu a nástroji pro sebehodnocení.

---

**EdgeAI představuje budoucnost nasazení AI**: lokální přístup, ochrana soukromí a efektivita. Ovládněte tyto dovednosti a vytvořte další generaci inteligentních aplikací.

## Další kurzy

Náš tým vytváří i další kurzy! Podívejte se:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### Azure / Edge / MCP / Agenti
[![AZD pro začátečníky](https://img.shields.io/badge/AZD%20pro%20začátečníky-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pro začátečníky](https://img.shields.io/badge/Edge%20AI%20pro%20začátečníky-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pro začátečníky](https://img.shields.io/badge/MCP%20pro%20začátečníky-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti pro začátečníky](https://img.shields.io/badge/AI%20agenti%20pro%20začátečníky-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativní AI série
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generativní%20AI%20pro%20začátečníky-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generativní%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generativní%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generativní%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní učení
[![ML pro začátečníky](https://img.shields.io/badge/ML%20pro%20začátečníky-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20pro%20začátečníky-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20pro%20začátečníky-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kybernetická bezpečnost pro začátečníky](https://img.shields.io/badge/Kybernetická%20bezpečnost%20pro%20začátečníky-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Webový%20vývoj%20pro%20začátečníky-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20pro%20začátečníky-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pro začátečníky](https://img.shields.io/badge/XR%20vývoj%20pro%20začátečníky-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot série
[![Copilot pro AI párové programování](https://img.shields.io/badge/Copilot%20pro%20AI%20párové%20programování-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pro C#/.NET](https://img.shields.io/badge/Copilot%20pro%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získání pomoci

Pokud narazíte na problém nebo máte otázky ohledně vytváření AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby při vytváření, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->