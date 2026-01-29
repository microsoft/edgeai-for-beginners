# Workshop Notebooks

> **Interaktívne Jupyter Notebooks pre praktické učenie Edge AI**
>
> Postupné, samostatné tutoriály, ktoré sa rozvíjajú od základných chatovacích dokončení až po pokročilé systémy s viacerými agentmi pomocou Microsoft Foundry Local a Small Language Models.

---

## 📖 Úvod

Vitajte v kolekcii **EdgeAI for Beginners Workshop Notebooks**. Tieto interaktívne Jupyter Notebooks poskytujú praktickú skúsenosť, kde budete písať, vykonávať a experimentovať s kódom Edge AI v reálnom čase.

### Prečo Jupyter Notebooks?

Na rozdiel od tradičných tutoriálov tieto notebooks ponúkajú:

- **Interaktívne učenie**: Spúšťajte bunky s kódom a okamžite vidíte výsledky
- **Experimentovanie**: Upravujte parametre a sledujte zmeny v reálnom čase
- **Dokumentácia**: Vysvetlenia priamo v notebooku vás prevedú konceptmi
- **Reprodukovateľnosť**: Kompletné funkčné príklady, ktoré môžete použiť znova
- **Vizualizácia**: Zobrazte metriky výkonu, vkladania a výsledky priamo v notebooku

### Čo robí tieto notebooks výnimočnými?

Každý notebook je navrhnutý podľa **najlepších praktík pripravených na produkciu**:

✅ **Komplexné spracovanie chýb** - Elegantné degradovanie a informatívne chybové správy  
✅ **Typové náznaky a dokumentácia** - Jasné podpisy funkcií a docstringy  
✅ **Monitorovanie výkonu** - Sledovanie používania tokenov a meranie latencie  
✅ **Modulárny dizajn** - Opakovane použiteľné vzory, ktoré môžete prispôsobiť svojim projektom  
✅ **Postupná zložitosť** - Systematicky stavia na predchádzajúcich lekciách  

---

## 🎯 Ciele učenia

### Základné zručnosti, ktoré si osvojíte

Prácou s týmito notebooks zvládnete:

1. **Správa lokálnych AI služieb**
   - Konfigurácia a správa služieb Microsoft Foundry Local
   - Výber a načítanie vhodných modelov pre váš hardvér
   - Monitorovanie využitia zdrojov a optimalizácia výkonu
   - Správa objavovania služieb a kontroly ich stavu

2. **Vývoj AI aplikácií**
   - Implementácia chatovacích dokončení kompatibilných s OpenAI lokálne
   - Vytváranie streamovacích rozhraní pre lepší používateľský zážitok
   - Návrh efektívnych promptov pre Small Language Models
   - Integrácia lokálnych modelov do aplikácií

3. **Generácia s podporou vyhľadávania (RAG)**
   - Vytváranie semantického vyhľadávania pomocou vektorových vkladov
   - Ukotvenie odpovedí LLM v dokumentoch špecifických pre danú oblasť
   - Hodnotenie kvality RAG pomocou metrík RAGAS
   - Škálovanie od prototypu po produkciu

4. **Optimalizácia výkonu**
   - Systematické porovnávanie viacerých modelov
   - Meranie latencie, priepustnosti a času prvého tokenu
   - Porovnávanie Small Language Models vs Large Language Models
   - Výber optimálnych modelov na základe kompromisov výkonu/kvality

5. **Orchestrácia viacerých agentov**
   - Návrh špecializovaných agentov pre rôzne úlohy
   - Implementácia pamäte agentov a správy kontextu
   - Koordinácia viacerých agentov v komplexných pracovných postupoch
   - Vytváranie vzorov koordinátorov pre spoluprácu agentov

6. **Inteligentné smerovanie modelov**
   - Implementácia detekcie zámerov a porovnávania vzorov
   - Automatické smerovanie dotazov na vhodné modely
   - Vytváranie viacstupňových pipeline (plán → vykonanie → zdokonalenie)
   - Návrh škálovateľných architektúr modelov ako nástrojov

---

## 🎓 Výsledky učenia

### Čo vytvoríte

| Notebook | Výstup | Demonštrované zručnosti | Obtiažnosť |
|----------|--------|-------------------------|------------|
| **Session 01** | Chatovacia aplikácia so streamovaním | Nastavenie služby, základné dokončenia, UX streamovania | ⭐ Začiatočník |
| **Session 02 (RAG)** | RAG pipeline s hodnotením | Vklady, semantické vyhľadávanie, metriky kvality | ⭐⭐ Stredne pokročilý |
| **Session 02 (Eval)** | Hodnotiteľ kvality RAG | Metriky RAGAS, systematické hodnotenie | ⭐⭐ Stredne pokročilý |
| **Session 03** | Benchmark viacerých modelov | Meranie výkonu, porovnávanie modelov | ⭐⭐ Stredne pokročilý |
| **Session 04** | Porovnávač SLM vs LLM | Analýza kompromisov, stratégie optimalizácie | ⭐⭐⭐ Pokročilý |
| **Session 05** | Orchestrátor viacerých agentov | Návrh agentov, pamäť, koordinácia | ⭐⭐⭐ Pokročilý |
| **Session 06 (Router)** | Inteligentný smerovací systém | Detekcia zámerov, výber modelov | ⭐⭐⭐ Pokročilý |
| **Session 06 (Pipeline)** | Viacstupňová pipeline | Pracovné postupy plán/vykonanie/zdokonalenie | ⭐⭐⭐ Pokročilý |

### Postup kompetencií

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Harmonogram workshopu

### 🚀 Pol-dňový workshop (3,5 hodiny)

**Ideálne pre: Tímové školenia, hackathony, konferenčné workshopy**

| Čas | Trvanie | Session | Témy | Aktivity |
|-----|---------|---------|------|----------|
| **0:00** | 30 min | Nastavenie & Úvod | Nastavenie prostredia, inštalácia Foundry Local | Inštalácia závislostí, overenie nastavenia |
| **0:30** | 30 min | Session 01 | Základné chatovacie dokončenia, streamovanie | Spustenie notebooku, úprava promptov |
| **1:00** | 45 min | Session 02 | RAG pipeline, vklady, hodnotenie | Vytvorenie systému RAG, testovanie dotazov |
| **1:45** | 15 min | Prestávka | ☕ Káva & otázky | — |
| **2:00** | 30 min | Session 03 | Benchmark viacerých modelov | Porovnanie 3+ modelov |
| **2:30** | 30 min | Session 04 | Kompromisy SLM vs LLM | Analýza výkonu/kvality |
| **3:00** | 30 min | Session 05-06 | Systémy viacerých agentov & smerovanie | Preskúmanie pokročilých vzorov |

**Výstup**: Účastníci odchádzajú so 6 funkčnými Edge AI aplikáciami a vzormi kódu pripravenými na produkciu.

---

### 🎓 Celodenný workshop (6 hodín)

**Ideálne pre: Hĺbkové školenia, bootcampy, univerzitné kurzy**

| Čas | Trvanie | Session | Témy | Aktivity |
|-----|---------|---------|------|----------|
| **0:00** | 45 min | Nastavenie & Teória | Nastavenie prostredia, základy Edge AI | Inštalácia, overenie, diskusia o prípadoch použitia |
| **0:45** | 45 min | Session 01 | Hĺbkový ponor do chatovacích dokončení | Implementácia základného & streamovacieho chatu |
| **1:30** | 30 min | Prestávka | ☕ Káva & networking | — |
| **2:00** | 60 min | Session 02 (Obe) | RAG pipeline + hodnotenie RAGAS | Vytvorenie kompletného systému RAG |
| **3:00** | 30 min | Praktické cvičenie 1 | Vlastný RAG pre vašu oblasť | Aplikácia na vlastné dokumenty |
| **3:30** | 30 min | Obed | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Metodológia benchmarkingu | Systematické porovnávanie modelov |
| **4:45** | 45 min | Session 04 | Stratégie optimalizácie | Analýza SLM vs LLM |
| **5:30** | 60 min | Session 05-06 | Pokročilá orchestrácia | Systémy viacerých agentov, smerovanie |
| **6:30** | 30 min | Praktické cvičenie 2 | Vytvorenie vlastného systému agentov | Návrh vlastného orchestrátora |

**Výstup**: Hĺbkové pochopenie vzorov Edge AI plus 2 vlastné projekty.

---

### 📚 Samostatné učenie (2 týždne)

**Ideálne pre: Individuálnych študentov, online kurzy, samostatné štúdium**

#### Týždeň 1: Základy (6 hodín)

| Deň | Zameranie | Trvanie | Notebooks | Domáca úloha |
|-----|----------|---------|-----------|-------------|
| **Po** | Nastavenie & Základy | 1,5 hod | Session 01 | Úprava promptov, testovanie streamovania |
| **St** | Základy RAG | 2 hod | Session 02 (obe) | Pridanie vlastných dokumentov |
| **Pi** | Benchmarking | 1,5 hod | Session 03 | Porovnanie ďalších modelov |
| **So** | Prehľad & Prax | 1 hod | Všetky Týždeň 1 | Dokončenie cvičení, ladenie |

#### Týždeň 2: Pokročilé (5 hodín)

| Deň | Zameranie | Trvanie | Notebooks | Domáca úloha |
|-----|----------|---------|-----------|-------------|
| **Po** | Optimalizácia | 1,5 hod | Session 04 | Dokumentácia kompromisov |
| **St** | Systémy viacerých agentov | 2 hod | Session 05 | Návrh vlastných agentov |
| **Pi** | Inteligentné smerovanie | 1,5 hod | Session 06 (obe) | Vytvorenie logiky smerovania |
| **So** | Záverečný projekt | 2 hod | Integrácia | Kombinácia viacerých vzorov |

**Výstup**: Ovládnutie vzorov Edge AI plus projekt do portfólia.

---

## 📔 Popisy notebookov

### 📘 Session 01: Chat Bootstrap
**Súbor**: `session01_chat_bootstrap.ipynb`  
**Trvanie**: 20-30 minút  
**Predpoklady**: Žiadne  
**Obtiažnosť**: ⭐ Začiatočník

**Čo sa naučíte**:
- Inštalácia a konfigurácia Foundry Local Python SDK
- Použitie `FoundryLocalManager` na automatické objavovanie služieb
- Implementácia základných chatovacích dokončení s OpenAI-kompatibilným API
- Vytvorenie streamovacích odpovedí pre lepší používateľský zážitok
- Elegantné spracovanie chýb a nedostupnosti služieb

**Kľúčové koncepty**: Správa služieb, chatovacie dokončenia, streamovanie, spracovanie chýb

**Čo vytvoríte**: Interaktívna chatovacia aplikácia s podporou streamovania

---

### 📗 Session 02: RAG Pipeline
**Súbor**: `session02_rag_pipeline.ipynb`  
**Trvanie**: 30-45 minút  
**Predpoklady**: Session 01  
**Obtiažnosť**: ⭐⭐ Stredne pokročilý

**Čo sa naučíte**:
- Implementácia vzoru Retrieval Augmented Generation (RAG)
- Vytváranie vektorových vkladov pomocou sentence-transformers
- Vytvorenie semantického vyhľadávania pomocou kosínovej podobnosti
- Ukotvenie odpovedí LLM v dokumentoch špecifických pre danú oblasť
- Elegantné spracovanie voliteľných závislostí pomocou import guards

**Kľúčové koncepty**: Architektúra RAG, vklady, semantické vyhľadávanie, vektorová podobnosť

**Čo vytvoríte**: Systém otázok a odpovedí ukotvený v dokumentoch

---

### 📗 Session 02: Hodnotenie RAG pomocou RAGAS
**Súbor**: `session02_rag_eval_ragas.ipynb`  
**Trvanie**: 30-45 minút  
**Predpoklady**: Session 02 RAG Pipeline  
**Obtiažnosť**: ⭐⭐ Stredne pokročilý

**Čo sa naučíte**:
- Hodnotenie kvality RAG pomocou štandardných metrík v odvetví
- Meranie relevantnosti kontextu, relevantnosti odpovede, dôveryhodnosti
- Použitie rámca RAGAS na systematické hodnotenie
- Identifikácia a oprava problémov kvality RAG
- Vytváranie hodnotiacich datasetov pre vašu oblasť

**Kľúčové koncepty**: Hodnotenie RAG, metriky RAGAS, meranie kvality, systematické testovanie

**Čo vytvoríte**: Rámec na hodnotenie kvality RAG

---

### 📙 Session 03: Benchmark OSS Models
**Súbor**: `session03_benchmark_oss_models.ipynb`  
**Trvanie**: 30-45 minút  
**Predpoklady**: Session 01  
**Obtiažnosť**: ⭐⭐ Stredne pokročilý

**Čo sa naučíte**:
- Systematické porovnávanie viacerých modelov
- Meranie latencie, priepustnosti, času prvého tokenu
- Elegantné degradovanie pri zlyhaní modelov
- Porovnávanie výkonu medzi rodinami modelov
- Vizualizácia a analýza výsledkov benchmarku

**Kľúčové koncepty**: Benchmarking výkonu, meranie latencie, porovnávanie modelov, štatistická analýza

**Čo vytvoríte**: Sada na benchmark viacerých modelov

---

### 📙 Session 04: Porovnanie modelov (SLM vs LLM)
**Súbor**: `session04_model_compare.ipynb`  
**Trvanie**: 30-45 minút  
**Predpoklady**: Sessions 01, 03  
**Obtiažnosť**: ⭐⭐⭐ Pokročilý

**Čo sa naučíte**:
- Porovnávanie Small Language Models vs Large Language Models
- Analýza kompromisov výkonu vs kvality
- Meranie metrík vhodnosti pre edge
- Výber optimálnych modelov pre obmedzenia nasadenia
- Dokumentácia kritérií rozhodovania pri výbere modelov

**Kľúčové koncepty**: Výber modelov, analýza kompromisov, stratégie optimalizácie, plánovanie nasadenia

**Čo vytvoríte**: Rámec na porovnanie SLM vs LLM

---

### 📕 Session 05: Orchestrátor viacerých agentov
**Súbor**: `session05_agents_orchestrator.ipynb`  
**Trvanie**: 45-60 minút  
**Predpoklady**: Sessions 01-02  
**Obtiažnosť**: ⭐⭐⭐ Pokročilý

**Čo sa naučíte**:
- Návrh špecializovaných agentov pre rôzne úlohy
- Implementácia pamäte agentov a správy kontextu
- Vytváranie vzorov koordinátorov pre spoluprácu agentov
- Správa komunikácie agentov a odovzdávania úloh
- Monitorovanie výkonu systému viacerých agentov

**Kľúčové koncepty**: Architektúra agentov, vzory koordinátorov, správa pamäte, orchestrácia agentov

**Čo vytvoríte**: Systém viacerých agentov s koordinátorom a špecialistami

---

### 📕 Session 06: Smerovač modelov
**Súbor**: `session06_models_router.ipynb`  
**Trvanie**: 30-45 minút  
**Predpoklady**: Sessions 01, 03  
**Obtiažnosť**: ⭐⭐⭐ Pokročilý

**Čo sa naučíte**:
- Implementácia detekcie zámerov a porovnávania vzorov
- Vytváranie smerovania modelov na základe kľúčových slov
- Automatické smerovanie dotazov na vhodné modely
- Konfigurácia registrácií viacerých modelov
- Monitorovanie rozhodnutí o smerovaní a výkonu

**Kľúčové koncepty**: Detekcia zámerov, smerovanie modelov, porovnávanie vzorov, inteligentný výber

**Čo
- Navrhnite škálovateľné architektúry modelov ako nástrojov

**Kľúčové koncepty**: Architektúra pipeline, viacstupňové spracovanie, obnova chýb, vzory škálovateľnosti

**Čo budete vytvárať**: Inteligentnú pipeline s viacerými krokmi a smerovaním

---

## 🚀 Začíname

### Predpoklady

**Systémové požiadavky**:
- **OS**: Windows 10/11, macOS 11+ alebo Linux (Ubuntu 20.04+)
- **RAM**: Minimálne 8GB, odporúča sa 16GB+
- **Úložisko**: Voľné miesto 10GB+ pre modely
- **Hardvér**: CPU s AVX2; GPU (CUDA, Qualcomm NPU) voliteľné

**Softvérové požiadavky**:
- **Python 3.8+** s pip
- **Jupyter Notebook** alebo **VS Code** s rozšírením Jupyter
- **Microsoft Foundry Local** nainštalovaný a nakonfigurovaný
- **Git** (na klonovanie repozitára)

### Kroky inštalácie

#### 1. Nainštalujte Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Overenie inštalácie**:
```bash
foundry --version
```

#### 2. Nastavte Python prostredie

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

#### 3. Spustite Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Spustite Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Rýchle overenie

Spustite tento kód v Python bunke na overenie nastavenia:

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

**Očakávaný výstup**: Odpoveď s pozdravom od lokálneho modelu.

---

## 📝 Najlepšie praktiky pre workshop

### Pre inštruktorov

**Pred workshopom**:
- ✅ Pošlite inštalačné pokyny týždeň vopred
- ✅ Otestujte všetky notebooky na cieľovom hardvéri
- ✅ Pripravte príručku na riešenie bežných problémov
- ✅ Majte pripravené záložné modely (phi-3.5-mini, ak phi-4-mini zlyhá)
- ✅ Nastavte zdieľaný chatovací kanál na otázky

**Počas workshopu**:
- ✅ Začnite rýchlou kontrolou prostredia (5 minút)
- ✅ Okamžite zdieľajte zdroje na riešenie problémov
- ✅ Povzbudzujte experimentovanie a úpravy
- ✅ Strategicky využívajte prestávky (po každých 2 sekciách)
- ✅ Majte k dispozícii TAs na individuálnu pomoc

**Po workshope**:
- ✅ Zdieľajte kompletné funkčné notebooky a riešenia
- ✅ Poskytnite odkazy na ďalšie zdroje
- ✅ Vytvorte dotazník na spätnú väzbu pre zlepšenie
- ✅ Ponúknite konzultačné hodiny na následné otázky

### Pre účastníkov

**Maximalizujte svoje učenie**:
- ✅ Dokončite nastavenie pred začiatkom workshopu
- ✅ Spustite každý kódový blok sami (nečítajte len)
- ✅ Experimentujte s parametrami a promptami
- ✅ Robte si poznámky o postrehoch a úskaliach
- ✅ Pýtajte sa otázky, keď ste zmätení (pravdepodobne majú rovnakú otázku aj ostatní)

**Bežné chyby, ktorým sa treba vyhnúť**:
- ❌ Preskakovanie poradia vykonávania buniek (spúšťajte postupne)
- ❌ Nečítanie chybových hlásení pozorne
- ❌ Príliš rýchle prechádzanie bez pochopenia
- ❌ Ignorovanie vysvetlení v markdown
- ❌ Neuloženie upravených notebookov

**Tipy na ladenie**:
1. **Služba nebeží**: Skontrolujte `foundry service status`
2. **Import chyby**: Overte, či je aktivované virtuálne prostredie
3. **Model sa nenašiel**: Spustite `foundry model ls` na zobrazenie načítaných modelov
4. **Pomalý výkon**: Skontrolujte využitie RAM, zatvorte ostatné aplikácie
5. **Neočakávané výsledky**: Reštartujte kernel a spustite všetky bunky od začiatku

---

## 🔗 Ďalšie zdroje

### Materiály workshopu

- **[Hlavná príručka workshopu](../Readme.md)** - Prehľad, vzdelávacie ciele, kariérne výsledky
- **[Python vzorky](../../../../Workshop/samples)** - Zodpovedajúce Python skripty pre každú sekciu
- **[Príručky sekcií](../../../../Workshop)** - Podrobné markdown príručky (Session01-06)
- **[Skripty](../../../../Workshop/scripts)** - Nástroje na validáciu a testovanie
- **[Riešenie problémov](./TROUBLESHOOTING.md)** - Bežné problémy a riešenia
- **[Rýchly štart](./quickstart.md)** - Príručka na rýchle začatie

### Dokumentácia

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Oficiálna dokumentácia Microsoftu
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referencia SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentácia embedding modelov
- **[RAGAS Framework](https://docs.ragas.io/)** - Metodika hodnotenia RAG

### Komunita

- **[GitHub Diskusie](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Pýtajte sa otázky, zdieľajte projekty
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Podpora komunity v reálnom čase
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technické otázky a odpovede

---

## 🎯 Odporúčania pre vzdelávaciu cestu

### Začiatočnícka úroveň (Začnite tu)

1. **Sekcia 01** - Chat Bootstrap
2. **Sekcia 02** - RAG Pipeline
3. **Sekcia 03** - Benchmark Modelov

**Čas**: ~2 hodiny | **Zameranie**: Základné vzory

---

### Stredne pokročilá úroveň

1. Dokončite začiatočnícku úroveň
2. **Sekcia 02** - Hodnotenie RAG
3. **Sekcia 04** - Porovnanie modelov

**Čas**: ~4 hodiny | **Zameranie**: Kvalita a optimalizácia

---

### Pokročilá úroveň (Kompletný workshop)

1. Dokončite stredne pokročilú úroveň
2. **Sekcia 05** - Multi-Agent Orchestrator
3. **Sekcia 06** - Model Router
4. **Sekcia 06** - Pipeline s viacerými krokmi

**Čas**: ~6 hodín | **Zameranie**: Produkčné vzory

---

### Vlastný projektový track

1. Dokončite začiatočnícku úroveň (Sekcie 01-03)
2. Vyberte JEDNU pokročilú sekciu podľa vášho cieľa:
   - **Budovanie RAG aplikácie?** → Sekcia 02 Hodnotenie
   - **Optimalizácia výkonu?** → Sekcia 04 Porovnanie
   - **Komplexné pracovné postupy?** → Sekcia 05 Orchestrator
   - **Škálovateľná architektúra?** → Sekcia 06 Router + Pipeline

**Čas**: ~3 hodiny | **Zameranie**: Zručnosti špecifické pre projekt

---

## 📊 Metriky úspechu

Sledujte svoj pokrok pomocou týchto míľnikov:

- [ ] **Dokončené nastavenie** - Foundry Local beží, všetky závislosti nainštalované
- [ ] **Prvý chat** - Dokončená sekcia 01, funkčný streaming chat
- [ ] **Postavený RAG** - Dokončená sekcia 02, funkčný systém QA dokumentov
- [ ] **Benchmark modelov** - Dokončená sekcia 03, zozbierané údaje o výkone
- [ ] **Analyzované kompromisy** - Dokončená sekcia 04, zdokumentované kritériá výberu modelov
- [ ] **Orchestrácia agentov** - Dokončená sekcia 05, funkčný systém multi-agentov
- [ ] **Implementované smerovanie** - Dokončená sekcia 06, funkčný inteligentný výber modelov
- [ ] **Vlastný projekt** - Aplikované vzory workshopu na váš vlastný prípad použitia

---

## 🤝 Prispievanie

Našli ste problém alebo máte návrh? Uvítame príspevky!

- **Nahláste problémy**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Navrhnite vylepšenia**: [GitHub Diskusie](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Odosielajte PRs**: Postupujte podľa [Príručky prispievania](../../AGENTS.md)

---

## 📄 Licencia

Tento workshop je súčasťou repozitára [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) a je licencovaný pod [MIT Licenciou](../../../../LICENSE).

---

**Pripravení vytvárať produkčne pripravené Edge AI aplikácie?**  
**Začnite s [Sekciou 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Posledná aktualizácia: 8. október 2025 | Verzia workshopu: 2.0*

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.