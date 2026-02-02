# Workshop Notebooks

> **Interaktivní Jupyter Notebooky pro praktické učení Edge AI**
>
> Postupné, samostatně řízené tutoriály, které přecházejí od základních chatovacích dokončení k pokročilým systémům s více agenty pomocí Microsoft Foundry Local a Small Language Models.

---

## 📖 Úvod

Vítejte v kolekci **EdgeAI for Beginners Workshop Notebooks**. Tyto interaktivní Jupyter notebooky poskytují praktické vzdělávací prostředí, kde budete psát, spouštět a experimentovat s kódem Edge AI v reálném čase.

### Proč Jupyter Notebooky?

Na rozdíl od tradičních tutoriálů tyto notebooky nabízejí:

- **Interaktivní učení**: Spouštějte buňky s kódem a okamžitě vidíte výsledky
- **Experimentování**: Měňte parametry a pozorujte změny v reálném čase
- **Dokumentace**: Vysvětlení přímo v textu a buňkách s markdownem vás provedou koncepty
- **Reprodukovatelnost**: Kompletní funkční příklady, které můžete použít znovu
- **Vizualizace**: Zobrazte metriky výkonu, vnoření a výsledky přímo v notebooku

### Co dělá tyto notebooky výjimečnými?

Každý notebook je navržen podle **osvědčených postupů pro produkční prostředí**:

✅ **Komplexní zpracování chyb** - Plynulé degradace a informativní chybové zprávy  
✅ **Typové nápovědy a dokumentace** - Jasné podpisy funkcí a docstringy  
✅ **Monitorování výkonu** - Sledování využití tokenů a měření latence  
✅ **Modulární design** - Znovupoužitelné vzory, které můžete přizpůsobit svým projektům  
✅ **Postupná složitost** - Systematicky navazuje na předchozí lekce  

---

## 🎯 Cíle učení

### Klíčové dovednosti, které si osvojíte

Prací s těmito notebooky zvládnete:

1. **Správa lokálních AI služeb**
   - Konfigurace a správa služeb Microsoft Foundry Local
   - Výběr a načítání vhodných modelů pro váš hardware
   - Monitorování využití zdrojů a optimalizace výkonu
   - Zajištění objevování služeb a kontrola jejich stavu

2. **Vývoj AI aplikací**
   - Implementace chatovacích dokončení kompatibilních s OpenAI lokálně
   - Vytváření streamovacích rozhraní pro lepší uživatelský zážitek
   - Návrh efektivních promptů pro Small Language Models
   - Integrace lokálních modelů do aplikací

3. **Generování s podporou vyhledávání (RAG)**
   - Vytváření sémantického vyhledávání pomocí vektorových vnoření
   - Ukotvení odpovědí LLM v dokumentech specifických pro danou oblast
   - Hodnocení kvality RAG pomocí metrik RAGAS
   - Škálování od prototypu k produkci

4. **Optimalizace výkonu**
   - Systematické porovnávání více modelů
   - Měření latence, propustnosti a času prvního tokenu
   - Porovnání Small Language Models vs Large Language Models
   - Výběr optimálních modelů na základě kompromisů mezi výkonem a kvalitou

5. **Orchestrace více agentů**
   - Návrh specializovaných agentů pro různé úkoly
   - Implementace paměti agentů a správy kontextu
   - Koordinace více agentů v komplexních pracovních postupech
   - Vytváření vzorů koordinátorů pro spolupráci agentů

6. **Inteligentní směrování modelů**
   - Implementace detekce záměrů a rozpoznávání vzorů
   - Automatické směrování dotazů na vhodné modely
   - Vytváření vícekrokových pipeline (plán → provedení → zdokonalení)
   - Návrh škálovatelných architektur modelů jako nástrojů

---

## 🎓 Výsledky učení

### Co vytvoříte

| Notebook | Výstup | Demonstrované dovednosti | Obtížnost |
|----------|--------|--------------------------|-----------|
| **Session 01** | Chatovací aplikace se streamováním | Nastavení služby, základní dokončení, UX streamování | ⭐ Začátečník |
| **Session 02 (RAG)** | RAG pipeline s hodnocením | Vnoření, sémantické vyhledávání, metriky kvality | ⭐⭐ Středně pokročilý |
| **Session 02 (Eval)** | Hodnotitel kvality RAG | Metriky RAGAS, systematické hodnocení | ⭐⭐ Středně pokročilý |
| **Session 03** | Benchmark více modelů | Měření výkonu, porovnání modelů | ⭐⭐ Středně pokročilý |
| **Session 04** | Porovnání SLM vs LLM | Analýza kompromisů, optimalizační strategie | ⭐⭐⭐ Pokročilý |
| **Session 05** | Orchestrátor více agentů | Návrh agentů, paměť, koordinace | ⭐⭐⭐ Pokročilý |
| **Session 06 (Router)** | Inteligentní směrovací systém | Detekce záměrů, výběr modelů | ⭐⭐⭐ Pokročilý |
| **Session 06 (Pipeline)** | Vícekroková pipeline | Pracovní postupy plán/provedení/zdokonalení | ⭐⭐⭐ Pokročilý |

### Postup kompetencí

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Harmonogram workshopu

### 🚀 Workshop na půl dne (3,5 hodiny)

**Ideální pro: Týmová školení, hackathony, workshopy na konferencích**

| Čas | Délka | Lekce | Témata | Aktivity |
|-----|-------|-------|--------|----------|
| **0:00** | 30 min | Nastavení a úvod | Nastavení prostředí, instalace Foundry Local | Instalace závislostí, ověření nastavení |
| **0:30** | 30 min | Session 01 | Základní chatovací dokončení, streamování | Spuštění notebooku, úprava promptů |
| **1:00** | 45 min | Session 02 | RAG pipeline, vnoření, hodnocení | Vytvoření systému RAG, testování dotazů |
| **1:45** | 15 min | Přestávka | ☕ Káva a otázky | — |
| **2:00** | 30 min | Session 03 | Benchmark více modelů | Porovnání 3+ modelů |
| **2:30** | 30 min | Session 04 | Kompromisy SLM vs LLM | Analýza výkonu/kvality |
| **3:00** | 30 min | Session 05-06 | Systémy více agentů a směrování | Prozkoumání pokročilých vzorů |

**Výstup**: Účastníci odcházejí s 6 funkčními Edge AI aplikacemi a vzory kódu připravenými pro produkci.

---

### 🎓 Workshop na celý den (6 hodin)

**Ideální pro: Hloubkové školení, bootcampy, univerzitní kurzy**

| Čas | Délka | Lekce | Témata | Aktivity |
|-----|-------|-------|--------|----------|
| **0:00** | 45 min | Nastavení a teorie | Nastavení prostředí, základy Edge AI | Instalace, ověření, diskuse o případech použití |
| **0:45** | 45 min | Session 01 | Hloubkový pohled na chatovací dokončení | Implementace základního a streamovacího chatu |
| **1:30** | 30 min | Přestávka | ☕ Káva a networking | — |
| **2:00** | 60 min | Session 02 (obě části) | RAG pipeline + hodnocení RAGAS | Vytvoření kompletního systému RAG |
| **3:00** | 30 min | Praktická laboratoř 1 | Vlastní RAG pro vaši oblast | Aplikace na vlastní dokumenty |
| **3:30** | 30 min | Oběd | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Metodologie benchmarkingu | Systematické porovnání modelů |
| **4:45** | 45 min | Session 04 | Optimalizační strategie | Analýza SLM vs LLM |
| **5:30** | 60 min | Session 05-06 | Pokročilá orchestrace | Systémy více agentů, směrování |
| **6:30** | 30 min | Praktická laboratoř 2 | Vytvoření vlastního systému agentů | Návrh vlastního orchestrátoru |

**Výstup**: Hloubkové pochopení vzorů Edge AI plus 2 vlastní projekty.

---

### 📚 Samostatné učení (2 týdny)

**Ideální pro: Individuální studenty, online kurzy, samostudium**

#### Týden 1: Základy (6 hodin)

| Den | Zaměření | Délka | Notebooky | Domácí úkol |
|-----|----------|-------|-----------|-------------|
| **Po** | Nastavení a základy | 1,5 hod | Session 01 | Úprava promptů, testování streamování |
| **St** | Základy RAG | 2 hod | Session 02 (obě části) | Přidání vlastních dokumentů |
| **Pá** | Benchmarking | 1,5 hod | Session 03 | Porovnání dalších modelů |
| **So** | Revize a praxe | 1 hod | Vše z týdne 1 | Dokončení cvičení, ladění |

#### Týden 2: Pokročilé (5 hodin)

| Den | Zaměření | Délka | Notebooky | Domácí úkol |
|-----|----------|-------|-----------|-------------|
| **Po** | Optimalizace | 1,5 hod | Session 04 | Dokumentace kompromisů |
| **St** | Systémy více agentů | 2 hod | Session 05 | Návrh vlastních agentů |
| **Pá** | Inteligentní směrování | 1,5 hod | Session 06 (obě části) | Vytvoření logiky směrování |
| **So** | Závěrečný projekt | 2 hod | Integrace | Kombinace více vzorů |

**Výstup**: Mistrovství vzorů Edge AI plus projekt do portfolia.

---

## 📔 Popisy notebooků

### 📘 Session 01: Chat Bootstrap
**Soubor**: `session01_chat_bootstrap.ipynb`  
**Délka**: 20-30 minut  
**Předpoklady**: Žádné  
**Obtížnost**: ⭐ Začátečník

**Co se naučíte**:
- Instalace a konfigurace Foundry Local Python SDK
- Použití `FoundryLocalManager` pro automatické objevování služeb
- Implementace základních chatovacích dokončení s API kompatibilním s OpenAI
- Vytvoření streamovacích odpovědí pro lepší uživatelský zážitek
- Plynulé zpracování chyb a nedostupnosti služeb

**Klíčové koncepty**: Správa služeb, chatovací dokončení, streamování, zpracování chyb

**Co vytvoříte**: Interaktivní chatovací aplikaci s podporou streamování

---

### 📗 Session 02: RAG Pipeline
**Soubor**: `session02_rag_pipeline.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Session 01  
**Obtížnost**: ⭐⭐ Středně pokročilý

**Co se naučíte**:
- Implementace vzoru Retrieval Augmented Generation (RAG)
- Vytváření vektorových vnoření pomocí sentence-transformers
- Vytvoření sémantického vyhledávání pomocí kosinové podobnosti
- Ukotvení odpovědí LLM v dokumentech specifických pro danou oblast
- Zpracování volitelných závislostí pomocí import guardů

**Klíčové koncepty**: Architektura RAG, vnoření, sémantické vyhledávání, vektorová podobnost

**Co vytvoříte**: Systém odpovídání na otázky ukotvený v dokumentech

---

### 📗 Session 02: Hodnocení RAG pomocí RAGAS
**Soubor**: `session02_rag_eval_ragas.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Session 02 RAG Pipeline  
**Obtížnost**: ⭐⭐ Středně pokročilý

**Co se naučíte**:
- Hodnocení kvality RAG pomocí průmyslových standardních metrik
- Měření relevance kontextu, relevance odpovědí, věrnosti
- Použití rámce RAGAS pro systematické hodnocení
- Identifikace a oprava problémů s kvalitou RAG
- Vytváření hodnotících datových sad pro vaši oblast

**Klíčové koncepty**: Hodnocení RAG, metriky RAGAS, měření kvality, systematické testování

**Co vytvoříte**: Rámec pro hodnocení kvality RAG

---

### 📙 Session 03: Benchmark OSS Modelů
**Soubor**: `session03_benchmark_oss_models.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Session 01  
**Obtížnost**: ⭐⭐ Středně pokročilý

**Co se naučíte**:
- Systematické porovnávání více modelů
- Měření latence, propustnosti, času prvního tokenu
- Implementace plynulé degradace při selhání modelů
- Porovnání výkonu napříč rodinami modelů
- Vizualizace a analýza výsledků benchmarku

**Klíčové koncepty**: Benchmarking výkonu, měření latence, porovnání modelů, statistická analýza

**Co vytvoříte**: Sada pro benchmark více modelů

---

### 📙 Session 04: Porovnání modelů (SLM vs LLM)
**Soubor**: `session04_model_compare.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Sessions 01, 03  
**Obtížnost**: ⭐⭐⭐ Pokročilý

**Co se naučíte**:
- Porovnání Small Language Models vs Large Language Models
- Analýza kompromisů mezi výkonem a kvalitou
- Měření metrik vhodnosti pro edge
- Výběr optimálních modelů pro omezení nasazení
- Dokumentace kritérií rozhodování pro výběr modelů

**Klíčové koncepty**: Výběr modelů, analýza kompromisů, optimalizační strategie, plánování nasazení

**Co vytvoříte**: Rámec pro porovnání SLM vs LLM

---

### 📕 Session 05: Orchestrátor více agentů
**Soubor**: `session05_agents_orchestrator.ipynb`  
**Délka**: 45-60 minut  
**Předpoklady**: Sessions 01-02  
**Obtížnost**: ⭐⭐⭐ Pokročilý

**Co se naučíte**:
- Návrh specializovaných agentů pro různé úkoly
- Implementace paměti agentů a správy kontextu
- Vytvoření vzorů koordinátorů pro spolupráci agentů
- Zpracování komunikace mezi agenty a předávání úkolů
- Monitorování výkonu systému více agentů

**Klíčové koncepty**: Architektura agentů, vzory koordinátorů, správa paměti, orchestrace agentů

**Co vytvoříte**: Systém více agentů s koordinátorem a specialisty

---

### 📕 Session 06: Směrovač modelů
**Soubor**: `session06_models_router.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Sessions 01, 03  
**Obtížnost**: ⭐⭐⭐ Pokročilý

**Co se naučíte**:
- Implementace detekce záměrů a rozpoznávání vzorů
- Vytvoření směrování modelů na základě klíčových slov
- Automatické směrování dotazů na vhodné modely
- Konfigurace registrů více modelů
- Monitorování rozhodnutí o směrování a výkonu

**Klíčové koncepty**: Detekce záměrů, směrování modelů, rozpoznávání vzorů, inteligentní výběr

**Co vytvoříte**: Inteligentní systém směrování modelů

---

### 📕 Session 06: Vícekroková pipeline
**Soubor**: `session06_models_pipeline.ipynb`  
**Délka**: 30-45 minut  
**Předpoklady**: Sessions 01, 06 Router  
**Obtížnost**: ⭐⭐⭐ Pokročilý

**Co se naučíte**:
- Vytvoření ví
- Navrhování škálovatelných architektur modelů jako nástrojů

**Klíčové koncepty**: Architektura pipeline, vícestupňové zpracování, obnova chyb, vzory škálovatelnosti

**Co vytvoříte**: Inteligentní vícestupňovou pipeline s routováním

---

## 🚀 Začínáme

### Předpoklady

**Požadavky na systém**:
- **OS**: Windows 10/11, macOS 11+ nebo Linux (Ubuntu 20.04+)
- **RAM**: Minimálně 8 GB, doporučeno 16 GB+
- **Úložiště**: Minimálně 10 GB volného místa pro modely
- **Hardware**: CPU s AVX2; GPU (CUDA, Qualcomm NPU) volitelné

**Požadavky na software**:
- **Python 3.8+** s pip
- **Jupyter Notebook** nebo **VS Code** s rozšířením Jupyter
- **Microsoft Foundry Local** nainstalovaný a nakonfigurovaný
- **Git** (pro klonování repozitáře)

### Kroky instalace

#### 1. Instalace Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Ověření instalace**:
```bash
foundry --version
```

#### 2. Nastavení Python prostředí

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Spuštění Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Spuštění Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Rychlé ověření

Spusťte tento kód v Python buňce pro ověření nastavení:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Očekávaný výstup**: Odpověď s pozdravem od lokálního modelu.

---

## 📝 Nejlepší postupy pro workshop

### Pro instruktory

**Před workshopem**:
- ✅ Zašlete instalační pokyny týden předem
- ✅ Otestujte všechny notebooky na cílovém hardwaru
- ✅ Připravte průvodce řešením běžných problémů
- ✅ Mějte připravené záložní modely (phi-3.5-mini, pokud phi-4-mini selže)
- ✅ Nastavte sdílený chatovací kanál pro dotazy

**Během workshopu**:
- ✅ Začněte rychlou kontrolou prostředí (5 minut)
- ✅ Ihned sdílejte zdroje pro řešení problémů
- ✅ Podporujte experimentování a úpravy
- ✅ Strategicky využívejte přestávky (po každých 2 sezeních)
- ✅ Mějte asistenty (TAs) k dispozici pro individuální pomoc

**Po workshopu**:
- ✅ Sdílejte kompletní funkční notebooky a řešení
- ✅ Poskytněte odkazy na další zdroje
- ✅ Vytvořte dotazník pro zpětnou vazbu
- ✅ Nabídněte konzultační hodiny pro následné dotazy

### Pro účastníky

**Maximalizujte své učení**:
- ✅ Dokončete nastavení před začátkem workshopu
- ✅ Spusťte každý kódový blok sami (nejen čtěte)
- ✅ Experimentujte s parametry a výzvami
- ✅ Pište si poznámky o postřezích a úskalích
- ✅ Ptejte se, když narazíte na problém (pravděpodobně má stejný problém i někdo jiný)

**Běžné chyby, kterým se vyhnout**:
- ❌ Přeskakování pořadí spuštění buněk (spouštějte postupně)
- ❌ Nečtení chybových zpráv pozorně
- ❌ Spěchání bez pochopení
- ❌ Ignorování vysvětlení v markdownu
- ❌ Neuložení upravených notebooků

**Tipy pro ladění**:
1. **Služba neběží**: Zkontrolujte `foundry service status`
2. **Chyby při importu**: Ověřte, že je aktivováno virtuální prostředí
3. **Model nenalezen**: Spusťte `foundry model ls` pro zobrazení načtených modelů
4. **Pomalejší výkon**: Zkontrolujte využití RAM, zavřete jiné aplikace
5. **Neočekávané výsledky**: Restartujte kernel a spusťte všechny buňky od začátku

---

## 🔗 Další zdroje

### Materiály workshopu

- **[Hlavní průvodce workshopem](../Readme.md)** - Přehled, cíle učení, kariérní přínosy
- **[Python ukázky](../../../../Workshop/samples)** - Odpovídající Python skripty pro každé sezení
- **[Průvodce sezeními](../../../../Workshop)** - Podrobné průvodce v markdownu (Session01-06)
- **[Skripty](../../../../Workshop/scripts)** - Nástroje pro validaci a testování
- **[Řešení problémů](./TROUBLESHOOTING.md)** - Běžné problémy a jejich řešení
- **[Rychlý start](./quickstart.md)** - Průvodce rychlým začátkem

### Dokumentace

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Oficiální dokumentace Microsoftu
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referenční dokumentace SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentace embedding modelů
- **[RAGAS Framework](https://docs.ragas.io/)** - Metodika hodnocení RAG

### Komunita

- **[GitHub Diskuze](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Pokládejte dotazy, sdílejte projekty
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Podpora komunity v reálném čase
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technické otázky a odpovědi

---

## 🎯 Doporučení pro vzdělávací cestu

### Začátečnická úroveň (Začněte zde)

1. **Sezení 01** - Chat Bootstrap
2. **Sezení 02** - RAG Pipeline
3. **Sezení 03** - Benchmarking modelů

**Čas**: ~2 hodiny | **Zaměření**: Základní vzory

---

### Středně pokročilá úroveň

1. Dokončete začátečnickou úroveň
2. **Sezení 02** - Hodnocení RAG
3. **Sezení 04** - Porovnání modelů

**Čas**: ~4 hodiny | **Zaměření**: Kvalita a optimalizace

---

### Pokročilá úroveň (Kompletní workshop)

1. Dokončete středně pokročilou úroveň
2. **Sezení 05** - Orchestrátor více agentů
3. **Sezení 06** - Router modelů
4. **Sezení 06** - Vícestupňová pipeline

**Čas**: ~6 hodin | **Zaměření**: Produkční vzory

---

### Vlastní projektová úroveň

1. Dokončete začátečnickou úroveň (Sezení 01-03)
2. Vyberte JEDNO pokročilé sezení podle svého cíle:
   - **Budování RAG aplikace?** → Sezení 02 Hodnocení
   - **Optimalizace výkonu?** → Sezení 04 Porovnání
   - **Komplexní pracovní postupy?** → Sezení 05 Orchestrátor
   - **Škálovatelná architektura?** → Sezení 06 Router + Pipeline

**Čas**: ~3 hodiny | **Zaměření**: Dovednosti specifické pro projekt

---

## 📊 Metriky úspěchu

Sledujte svůj pokrok pomocí těchto milníků:

- [ ] **Dokončené nastavení** - Foundry Local běží, všechny závislosti nainstalovány
- [ ] **První chat** - Dokončeno Sezení 01, funkční streamovací chat
- [ ] **Postavený RAG** - Dokončeno Sezení 02, funkční systém dotazování na dokumenty
- [ ] **Benchmarking modelů** - Dokončeno Sezení 03, shromážděná data o výkonu
- [ ] **Analyzované kompromisy** - Dokončeno Sezení 04, dokumentovaná kritéria výběru modelů
- [ ] **Orchestrace agentů** - Dokončeno Sezení 05, funkční systém více agentů
- [ ] **Implementované routování** - Dokončeno Sezení 06, funkční inteligentní výběr modelů
- [ ] **Vlastní projekt** - Aplikované vzory workshopu na vlastní případ použití

---

## 🤝 Přispívání

Našli jste problém nebo máte návrh? Uvítáme vaše příspěvky!

- **Nahlásit problémy**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Navrhnout vylepšení**: [GitHub Diskuze](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Odeslat PRs**: Postupujte podle [Pokynů pro přispívání](../../AGENTS.md)

---

## 📄 Licence

Tento workshop je součástí repozitáře [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) a je licencován pod [MIT Licencí](../../../../LICENSE).

---

**Připraveni vytvářet produkčně připravené aplikace Edge AI?**  
**Začněte s [Sezením 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Poslední aktualizace: 8. října 2025 | Verze workshopu: 2.0*

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.