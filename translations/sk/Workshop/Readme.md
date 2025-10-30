<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T23:06:17+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "sk"
}
-->
# EdgeAI pre začiatočníkov - Workshop

> **Praktická cesta učenia na vytváranie produkčne pripravených Edge AI aplikácií**
>
> Ovládnite lokálne nasadenie AI s Microsoft Foundry Local, od prvého dokončenia chatu po orchestráciu viacerých agentov v 6 progresívnych lekciách.

---

## 🎯 Úvod

Vitajte na **EdgeAI pre začiatočníkov Workshop** - vašom praktickom sprievodcovi na vytváranie inteligentných aplikácií, ktoré fungujú výlučne na lokálnom hardvéri. Tento workshop premieňa teoretické koncepty Edge AI na reálne zručnosti prostredníctvom postupne náročnejších cvičení s využitím Microsoft Foundry Local a Small Language Models (SLMs).

### Prečo tento workshop?

**Revolúcia Edge AI je tu**

Organizácie po celom svete prechádzajú od AI závislej na cloude k edge computingu z troch kľúčových dôvodov:

1. **Ochrana súkromia a súlad s predpismi** - Spracovanie citlivých údajov lokálne bez prenosu do cloudu (HIPAA, GDPR, finančné regulácie)
2. **Výkon** - Eliminácia latencie siete (50-500ms lokálne vs 500-2000ms cloudový prenos)
3. **Kontrola nákladov** - Odstránenie nákladov na API za token a škálovanie bez výdavkov na cloud

**Ale Edge AI je iné**

Prevádzka AI na lokálnych zariadeniach vyžaduje nové zručnosti:
- Výber a optimalizácia modelov pre obmedzené zdroje
- Správa lokálnych služieb a hardvérová akcelerácia
- Tvorba promptov pre menšie modely
- Produkčné nasadenie vzorov pre edge zariadenia

**Tento workshop vám tieto zručnosti poskytne**

V 6 zameraných lekciách (~3 hodiny celkovo) prejdete od "Hello World" k nasadeniu produkčne pripravených systémov s viacerými agentmi - všetko lokálne na vašom zariadení.

---

## 📚 Ciele učenia

Po absolvovaní tohto workshopu budete schopní:

### Základné kompetencie
1. **Nasadiť a spravovať lokálne AI služby**
   - Nainštalovať a nakonfigurovať Microsoft Foundry Local
   - Vybrať vhodné modely pre nasadenie na edge
   - Spravovať životný cyklus modelov (stiahnuť, načítať, cacheovať)
   - Monitorovať využitie zdrojov a optimalizovať výkon

2. **Vytvárať aplikácie poháňané AI**
   - Implementovať OpenAI-kompatibilné chatové dokončenia lokálne
   - Navrhovať efektívne prompty pre Small Language Models
   - Spracovávať streamované odpovede pre lepší UX
   - Integrovať lokálne modely do existujúcich aplikácií

3. **Vytvárať systémy RAG (Retrieval Augmented Generation)**
   - Vytvárať semantické vyhľadávanie s embeddingami
   - Zakotviť odpovede LLM v doménovo špecifických znalostiach
   - Hodnotiť kvalitu RAG pomocou priemyselných štandardných metrík
   - Škálovať od prototypu k produkcii

4. **Optimalizovať výkon modelov**
   - Testovať viaceré modely pre váš prípad použitia
   - Merať latenciu, priepustnosť a čas prvého tokenu
   - Vybrať optimálne modely na základe kompromisov medzi rýchlosťou a kvalitou
   - Porovnať kompromisy medzi SLM a LLM v reálnych scenároch

5. **Orchestrácia systémov s viacerými agentmi**
   - Navrhovať špecializovaných agentov pre rôzne úlohy
   - Implementovať pamäť agentov a správu kontextu
   - Koordinovať agentov v komplexných pracovných postupoch
   - Inteligentne smerovať požiadavky medzi viacerými modelmi

6. **Nasadiť produkčne pripravené riešenia**
   - Implementovať spracovanie chýb a logiku opakovania
   - Monitorovať využitie tokenov a systémových zdrojov
   - Vytvárať škálovateľné architektúry s modelmi ako nástrojmi
   - Plánovať migračné cesty z edge na hybridné (edge + cloud)

---

## 🎓 Výsledky učenia

### Čo vytvoríte

Na konci tohto workshopu budete mať vytvorené:

| Lekcia | Výstup | Demonštrované zručnosti |
|--------|--------|--------------------------|
| **1** | Chatová aplikácia so streamovaním | Nastavenie služby, základné dokončenia, UX streamovania |
| **2** | Systém RAG s hodnotením | Embeddingy, semantické vyhľadávanie, metriky kvality |
| **3** | Sada benchmarkov pre viaceré modely | Meranie výkonu, porovnanie modelov |
| **4** | Porovnávač SLM vs LLM | Analýza kompromisov, optimalizačné stratégie |
| **5** | Orchestrátor viacerých agentov | Návrh agentov, správa pamäte, koordinácia |
| **6** | Inteligentný smerovací systém | Detekcia zámeru, výber modelu, škálovateľnosť |

### Matrica kompetencií

| Úroveň zručností | Lekcia 1-2 | Lekcia 3-4 | Lekcia 5-6 |
|------------------|------------|------------|------------|
| **Začiatočník** | ✅ Nastavenie & základy | ⚠️ Náročné | ❌ Príliš pokročilé |
| **Stredne pokročilý** | ✅ Rýchly prehľad | ✅ Základné učenie | ⚠️ Ciele na rozšírenie |
| **Pokročilý** | ✅ Jednoduché | ✅ Zdokonaľovanie | ✅ Produkčné vzory |

### Zručnosti pripravené na kariéru

**Po tomto workshope budete pripravení:**

✅ **Vytvárať aplikácie s ochranou súkromia**
- Zdravotnícke aplikácie spracovávajúce PHI/PII lokálne
- Finančné služby s požiadavkami na súlad
- Vládne systémy s potrebou suverenity údajov

✅ **Optimalizovať pre prostredie Edge**
- IoT zariadenia s obmedzenými zdrojmi
- Mobilné aplikácie fungujúce offline
- Systémy s nízkou latenciou v reálnom čase

✅ **Navrhovať inteligentné architektúry**
- Systémy s viacerými agentmi pre komplexné pracovné postupy
- Hybridné nasadenia edge-cloud
- Nákladovo optimalizovaná AI infraštruktúra

✅ **Viesť iniciatívy Edge AI**
- Hodnotiť realizovateľnosť Edge AI pre projekty
- Vybrať vhodné modely a rámce
- Navrhnúť škálovateľné lokálne AI riešenia

---

## 🗺️ Štruktúra workshopu

### Prehľad lekcií (6 lekcií × 30 minút = 3 hodiny)

| Lekcia | Téma | Zameranie | Trvanie |
|--------|------|-----------|---------|
| **1** | Začíname s Foundry Local | Inštalácia, validácia, prvé dokončenia | 30 min |
| **2** | Vytváranie AI riešení s RAG | Tvorba promptov, embeddingy, hodnotenie | 30 min |
| **3** | Open Source modely | Objavovanie modelov, benchmarking, výber | 30 min |
| **4** | Najnovšie modely | SLM vs LLM, optimalizácia, rámce | 30 min |
| **5** | Agentmi poháňané AI | Návrh agentov, orchestrácia, pamäť | 30 min |
| **6** | Modely ako nástroje | Smerovanie, reťazenie, škálovacie stratégie | 30 min |

---

## 🚀 Rýchly štart

### Predpoklady

**Požiadavky na systém:**
- **OS**: Windows 10/11, macOS 11+ alebo Linux (Ubuntu 20.04+)
- **RAM**: Minimálne 8GB, odporúčané 16GB+
- **Úložisko**: 10GB+ voľného miesta pre modely
- **CPU**: Moderný procesor s podporou AVX2
- **GPU** (voliteľné): CUDA-kompatibilné alebo Qualcomm NPU pre akceleráciu

**Požiadavky na softvér:**
- **Python 3.8+** ([Stiahnuť](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Inštalačný návod](../../../Workshop))
- **Git** ([Stiahnuť](https://git-scm.com/downloads))
- **Visual Studio Code** (odporúčané) ([Stiahnuť](https://code.visualstudio.com/))

### Nastavenie v 3 krokoch

#### 1. Inštalácia Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Overenie inštalácie:**
```bash
foundry --version
foundry service status
```

**Uistite sa, že Azure AI Foundry Local beží s pevne nastaveným portom**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Overenie funkčnosti:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Zistenie dostupných modelov**
Ak chcete zistiť, ktoré modely sú dostupné vo vašej inštancii Foundry Local, môžete dotazovať endpoint modelov:

```bash
# cmd/bash/powershell
foundry model list
```

Použitie webového endpointu 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klonovanie repozitára a inštalácia závislostí

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Spustenie prvého vzorku

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Úspech!** Mali by ste vidieť streamovanú odpoveď o edge AI.

---

## 📦 Zdroje workshopu

### Python vzorky

Postupné praktické príklady demonštrujúce každý koncept:

| Lekcia | Vzorka | Popis | Čas spustenia |
|--------|--------|-------|---------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Základný & streamovaný chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG s embeddingami | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Hodnotenie kvality RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking viacerých modelov | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Porovnanie SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Systém s viacerými agentmi | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Smerovanie na základe zámeru | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Viacstupňová pipeline | ~60s |

### Jupyter Notebooks

Interaktívne skúmanie s vysvetleniami a vizualizáciami:

| Lekcia | Notebook | Popis | Obtiažnosť |
|--------|----------|-------|-----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Základy chatu & streamovanie | ⭐ Začiatočník |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Vytvorenie systému RAG | ⭐⭐ Stredne pokročilý |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Hodnotenie kvality RAG | ⭐⭐ Stredne pokročilý |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modelov | ⭐⭐ Stredne pokročilý |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porovnanie modelov | ⭐⭐ Stredne pokročilý |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrácia agentov | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Smerovanie zámerov | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrácia pipeline | ⭐⭐⭐ Pokročilý |

### Dokumentácia

Komplexné príručky a referencie:

| Dokument | Popis | Použiť kedy |
|----------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | Rýchly návod na nastavenie | Začínate od nuly |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Cheat sheet príkazov & API | Potrebujete rýchle odpovede |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Vzory & príklady SDK | Píšete kód |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Príručka premenných prostredia | Konfigurujete vzorky |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Najnovšie vylepšenia vzoriek | Pochopenie zmien |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Príručka migrácie | Aktualizujete kód |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Bežné problémy & opravy | Riešenie problémov |

---

## 🎓 Odporúčania pre cestu učenia

### Pre začiatočníkov (3-4 hodiny)
1. ✅ Lekcia 1: Začíname (zamerajte sa na nastavenie a základný chat)
2. ✅ Lekcia 2: Základy RAG (hodnotenie preskočte na začiatku)
3. ✅ Lekcia 3: Jednoduché benchmarkovanie (iba 2 modely)
4. ⏭️ Preskočte lekcie 4-6 zatiaľ
5. 🔄 Vráťte sa k lekciám 4-6 po vytvorení prvej aplikácie

### Pre stredne pokročilých vývojárov (3 hodiny)
1. ⚡ Lekcia 1: Rýchla validácia nastavenia
2. ✅ Lekcia 2: Kompletný RAG pipeline s hodnotením
3. ✅ Lekcia 3: Kompletná sada benchmarkov
4. ✅ Lekcia 4: Optimalizácia modelov
5. ✅ Lekcie 5-6: Zameranie na vzory architektúry

### Pre pokročilých odborníkov (2-3 hodiny)
1. ⚡ Lekcie 1-3: Rýchly prehľad a validácia
2. ✅ Lekcia 4: Hĺbková optimalizácia
3. ✅ Lekcia 5: Architektúra s viacerými agentmi
4. ✅ Lekcia 6: Produkčné vzory a škálovanie
5. 🚀 Rozšírenie: Vytvorte vlastnú logiku smerovania a hybridné nasadenia

---

## Balík workshopových lekcií (Zamerané 30-minútové laboratóriá)

Ak sledujete skrátený formát workshopu s 6 lekciami, použite tieto špeciálne príručky (každá zodpovedá a dopĺňa širšiu dokumentáciu modulov vyššie):

| Workshopová lekcia | Príručka | Hlavné zameranie |
|--------------------|----------|------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Inštalácia, validácia, spustenie phi & GPT-OSS-20B, akcelerácia |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Tvorba promptov, vzory RAG, zakotvenie CSV & dokumentov, migrácia |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrácia Hugging Face, benchmarking, výber modelov |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX akcelerácia |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Úlohy agentov, pamäť, nástroje, orchestrácia |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Smerovanie, reťazenie, škálovanie na Azure |

Každý súbor relácie obsahuje: abstrakt, vzdelávacie ciele, 30-minútový demo postup, štartovací projekt, kontrolný zoznam validácie, riešenie problémov a odkazy na oficiálny Foundry Local Python SDK.

### Ukážkové skripty

Inštalácia závislostí workshopu (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ak spúšťate službu Foundry Local na inom (Windows) počítači alebo VM z macOS, exportujte endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Relácia | Skript(y) | Popis |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap služby & streamovanie chatu |
| 2 | `samples/session02/rag_pipeline.py` | Minimálny RAG (v pamäti) |
|   | `samples/session02/rag_eval_ragas.py` | Hodnotenie RAG pomocou metrik ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latencie & priepustnosti viacerých modelov |
| 4 | `samples/session04/model_compare.py` | Porovnanie SLM vs LLM (latencia & ukážkový výstup) |
| 5 | `samples/session05/agents_orchestrator.py` | Výskum dvoch agentov → redakčný proces |
| 6 | `samples/session06/models_router.py` | Demo smerovania na základe zámeru |
|   | `samples/session06/models_pipeline.py` | Reťazec plánovania/vykonávania/zdokonaľovania v niekoľkých krokoch |

### Premenné prostredia (spoločné pre všetky ukážky)

| Premenná | Účel | Príklad |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Predvolený alias jedného modelu pre základné ukážky | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicitný SLM vs väčší model na porovnanie | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Zoznam aliasov na benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Opakovania benchmarku na model | `3` |
| `BENCH_PROMPT` | Prompt použitý v benchmarku | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Prekrytie testovacej otázky pre RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Prekrytie otázky pre pipeline agentov | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modelu pre výskumného agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modelu pre redakčného agenta (môže byť odlišný) | `gpt-oss-20b` |
| `SHOW_USAGE` | Ak je `1`, vypíše použitie tokenov na dokončenie | `1` |
| `RETRY_ON_FAIL` | Ak je `1`, pri dočasných chybách chatu sa pokus zopakuje | `1` |
| `RETRY_BACKOFF` | Sekundy čakania pred opakovaním | `1.0` |

Ak premenná nie je nastavená, skripty sa vrátia k rozumným predvoleným hodnotám. Pre ukážky s jedným modelom zvyčajne stačí iba `FOUNDRY_LOCAL_ALIAS`.

### Pomocný modul

Všetky ukážky teraz zdieľajú pomocný `samples/workshop_utils.py`, ktorý poskytuje:

* Vytvorenie cache pre `FoundryLocalManager` + OpenAI klienta
* Pomocník `chat_once()` s voliteľným opakovaním + výpisom použitia
* Jednoduché hlásenie použitia tokenov (aktivácia cez `SHOW_USAGE=1`)

Toto znižuje duplicitu a zdôrazňuje najlepšie postupy pre efektívnu orchestráciu lokálnych modelov.

## Voliteľné vylepšenia (naprieč reláciami)

| Téma | Vylepšenie | Relácie | Env / Prepínač |
|-------|-------------|----------|--------------|
| Determinizmus | Fixná teplota + stabilné sady promptov | 1–6 | Nastaviť `temperature=0`, `top_p=1` |
| Viditeľnosť použitia tokenov | Konzistentná výučba nákladov/efektivity | 1–6 | `SHOW_USAGE=1` |
| Streamovanie prvého tokenu | Metrika vnímaného oneskorenia | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odolnosť voči opakovaniu | Rieši dočasné studené štarty | Všetky | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modeloví agenti | Špecializácia heterogénnych úloh | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptívne smerovanie | Zámer + heuristiky nákladov | 6 | Rozšíriť router o logiku eskalácie |
| Vektorová pamäť | Dlhodobé sémantické spomienky | 2,5,6 | Integrovať FAISS/Chroma embedding index |
| Export stopy | Auditovanie & hodnotenie | 2,5,6 | Pridať JSON riadky na krok |
| Kvalitatívne rubriky | Kvalitatívne sledovanie | 3–6 | Sekundárne prompty na skórovanie |
| Rýchle testy | Rýchla validácia pred workshopom | Všetky | `python Workshop/tests/smoke.py` |

### Deterministický rýchly štart

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očakávajte stabilné počty tokenov pri opakovaných identických vstupoch.

### Hodnotenie RAG (Relácia 2)

Použite `rag_eval_ragas.py` na výpočet relevantnosti odpovede, vernosti a presnosti kontextu na malom syntetickom datasete:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Rozšírte dodaním väčšieho JSONL otázok, kontextov a pravdivých údajov, potom konvertujte na Hugging Face `Dataset`.

## Príloha presnosti príkazov CLI

Workshop zámerne používa iba aktuálne dokumentované / stabilné príkazy Foundry Local CLI.

### Referencované stabilné príkazy

| Kategória | Príkaz | Účel |
|----------|---------|---------|
| Core | `foundry --version` | Zobraziť nainštalovanú verziu |
| Core | `foundry init` | Inicializovať konfiguráciu |
| Služba | `foundry service start` | Spustiť lokálnu službu (ak nie je automatická) |
| Služba | `foundry status` | Zobraziť stav služby |
| Modely | `foundry model list` | Zoznam katalógu / dostupných modelov |
| Modely | `foundry model download <alias>` | Stiahnuť váhy modelu do cache |
| Modely | `foundry model run <alias>` | Spustiť (načítať) model lokálne; kombinovať s `--prompt` na jednorazové použitie |
| Modely | `foundry model unload <alias>` / `foundry model stop <alias>` | Vyložiť model z pamäte (ak je podporované) |
| Cache | `foundry cache list` | Zoznam uložených (stiahnutých) modelov |
| Systém | `foundry system info` | Snímka hardvéru & schopností akcelerácie |
| Systém | `foundry system gpu-info` | Diagnostické informácie GPU |
| Konfigurácia | `foundry config list` | Zobraziť aktuálne hodnoty konfigurácie |
| Konfigurácia | `foundry config set <key> <value>` | Aktualizovať konfiguráciu |

### Jednorazový prompt vzor

Namiesto zastaraného podpríkazu `model chat` použite:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Toto vykoná jeden cyklus prompt/odpoveď a potom ukončí.

### Odstránené / vyhýbané vzory

| Zastarané / Nedokumentované | Náhrada / Odporúčanie |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Použiť jednoduché `foundry model list` + nedávna aktivita / logy |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Použiť benchmarkovací Python skript + nástroje OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetria

- Latencia, p95, tokeny/sekunda: `samples/session03/benchmark_oss_models.py`
- Latencia prvého tokenu (streamovanie): nastaviť `BENCH_STREAM=1`
- Použitie zdrojov: Monitory OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Ako sa nové príkazy CLI telemetrie stabilizujú, môžu byť začlenené s minimálnymi úpravami do markdown súborov relácií.

### Automatická kontrola syntaxe

Automatický kontrolór syntaxe zabraňuje opätovnému zavádzaniu zastaraných CLI vzorov vo vnútri ohradených blokov kódu v markdown súboroch:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Zastarané vzory sú blokované vo vnútri ohradených blokov kódu.

Odporúčané náhrady:
| Zastarané | Náhrada |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmarkovací skript + systémové nástroje |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Spustiť lokálne:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` sa spúšťa pri každom push & PR.

Voliteľný pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Rýchla tabuľka migrácie CLI → SDK

| Úloha | CLI jednorazový príkaz | Ekvivalent SDK (Python) | Poznámky |
|------|---------------|-------------------------|-------|
| Spustiť model raz (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automaticky inicializuje službu & cache |
| Stiahnuť (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # spustí stiahnutie/načítanie` | Manager vyberie najlepšiu variantu, ak alias mapuje na viacero verzií |
| Zoznam katalógu | `foundry model list` | `# použiť manager pre každý alias alebo udržiavať známy zoznam` | CLI agreguje; SDK aktuálne na inštanciu per-alias |
| Zoznam uložených modelov | `foundry cache list` | `manager.list_cached_models()` | Po inicializácii managera (akýkoľvek alias) |
| Aktivovať GPU akceleráciu | `foundry config set compute.onnx.enable_gpu true` | `# CLI akcia; SDK predpokladá už aplikovanú konfiguráciu` | Konfigurácia je externý vedľajší efekt |
| Získať URL endpointu | (implicitné) | `manager.endpoint` | Používa sa na vytvorenie OpenAI-kompatibilného klienta |
| Zahriatie modelu | `foundry model run <alias>` potom prvý prompt | `chat_once(alias, messages=[...])` (pomocník) | Pomocníci riešia počiatočné studené oneskorenie |
| Meranie latencie | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (alebo nový exportovací skript) | Preferovať skript pre konzistentné metriky |
| Zastaviť / vyložiť model | `foundry model unload <alias>` | (Nie je vystavené – reštartovať službu / proces) | Typicky nie je potrebné pre workshopový tok |
| Získať použitie tokenov | (zobraziť výstup) | `resp.usage.total_tokens` | Poskytované, ak backend vráti objekt použitia |

## Export benchmarku do Markdown

Použite skript `Workshop/scripts/export_benchmark_markdown.py` na spustenie čerstvého benchmarku (rovnaká logika ako `samples/session03/benchmark_oss_models.py`) a emitovanie GitHub-priateľskej tabuľky Markdown plus surového JSON.

### Príklad

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generované súbory:
| Súbor | Obsah |
|------|----------|
| `benchmark_report.md` | Tabuľka Markdown + interpretácia |
| `benchmark_report.json` | Surové metriky (na porovnanie / sledovanie trendov) |

Nastaviť `BENCH_STREAM=1` v prostredí na zahrnutie latencie prvého tokenu, ak je podporované.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.