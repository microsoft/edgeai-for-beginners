<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T23:01:50+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "cs"
}
-->
# EdgeAI pro začátečníky - Workshop

> **Praktická cesta k vytvoření produkčně připravených Edge AI aplikací**
>
> Ovládněte lokální nasazení AI s Microsoft Foundry Local, od prvního chatovacího dokončení až po orchestraci více agentů v 6 postupných lekcích.

---

## 🎯 Úvod

Vítejte na **EdgeAI pro začátečníky Workshopu** - praktickém průvodci pro vytváření inteligentních aplikací, které běží výhradně na lokálním hardwaru. Tento workshop přeměňuje teoretické koncepty Edge AI na reálné dovednosti prostřednictvím postupně náročnějších cvičení s využitím Microsoft Foundry Local a malých jazykových modelů (SLMs).

### Proč tento workshop?

**Revoluce Edge AI je tady**

Organizace po celém světě přecházejí od AI závislé na cloudu k edge computingu ze tří klíčových důvodů:

1. **Soukromí a dodržování předpisů** - Zpracování citlivých dat lokálně bez přenosu do cloudu (HIPAA, GDPR, finanční regulace)
2. **Výkon** - Eliminace síťové latence (50-500ms lokálně vs 500-2000ms cloudový přenos)
3. **Kontrola nákladů** - Odstranění nákladů na API za token a škálování bez výdajů na cloud

**Ale Edge AI je jiný**

Provozování AI na místě vyžaduje nové dovednosti:
- Výběr a optimalizace modelů pro omezené zdroje
- Správa lokálních služeb a hardwarová akcelerace
- Návrh promptů pro menší modely
- Vzory nasazení pro produkci na edge zařízeních

**Tento workshop vám tyto dovednosti poskytne**

Během 6 zaměřených lekcí (~3 hodiny celkem) se posunete od "Hello World" k nasazení produkčně připravených systémů s více agenty - vše běžící lokálně na vašem zařízení.

---

## 📚 Cíle učení

Po absolvování tohoto workshopu budete schopni:

### Klíčové kompetence
1. **Nasadit a spravovat lokální AI služby**
   - Instalovat a konfigurovat Microsoft Foundry Local
   - Vybrat vhodné modely pro nasazení na edge
   - Spravovat životní cyklus modelů (stahování, načítání, ukládání do cache)
   - Monitorovat využití zdrojů a optimalizovat výkon

2. **Vytvářet aplikace poháněné AI**
   - Implementovat OpenAI-kompatibilní chatovací dokončení lokálně
   - Navrhovat efektivní prompty pro malé jazykové modely
   - Zpracovávat streamované odpovědi pro lepší uživatelskou zkušenost
   - Integrovat lokální modely do existujících aplikací

3. **Vytvářet systémy RAG (Retrieval Augmented Generation)**
   - Vytvářet sémantické vyhledávání pomocí embeddingů
   - Zakládat odpovědi LLM na znalostech specifických pro danou doménu
   - Hodnotit kvalitu RAG pomocí průmyslových standardních metrik
   - Škálovat od prototypu k produkci

4. **Optimalizovat výkon modelů**
   - Provádět benchmarky více modelů pro váš případ použití
   - Měřit latenci, propustnost a čas prvního tokenu
   - Vybrat optimální modely na základě kompromisů mezi rychlostí a kvalitou
   - Porovnávat kompromisy mezi SLM a LLM v reálných scénářích

5. **Orchestraci systémů s více agenty**
   - Navrhovat specializované agenty pro různé úkoly
   - Implementovat paměť agentů a správu kontextu
   - Koordinovat agenty v komplexních pracovních postupech
   - Inteligentně směrovat požadavky mezi více modely

6. **Nasadit produkčně připravená řešení**
   - Implementovat zpracování chyb a logiku opakování
   - Monitorovat využití tokenů a systémových zdrojů
   - Vytvářet škálovatelné architektury s modely jako nástroji
   - Plánovat migrační cesty z edge na hybridní (edge + cloud)

---

## 🎓 Výsledky učení

### Co vytvoříte

Na konci tohoto workshopu budete mít:

| Lekce | Výstup | Demonstrované dovednosti |
|-------|--------|--------------------------|
| **1** | Chatovací aplikace se streamováním | Nastavení služby, základní dokončení, UX streamování |
| **2** | RAG systém s hodnocením | Embeddingy, sémantické vyhledávání, kvalitativní metriky |
| **3** | Sada benchmarků pro více modelů | Měření výkonu, porovnání modelů |
| **4** | Porovnání SLM vs LLM | Analýza kompromisů, optimalizační strategie |
| **5** | Orchestrátor s více agenty | Návrh agentů, správa paměti, koordinace |
| **6** | Inteligentní směrovací systém | Detekce záměru, výběr modelu, škálovatelnost |

### Matice kompetencí

| Úroveň dovedností | Lekce 1-2 | Lekce 3-4 | Lekce 5-6 |
|-------------------|-----------|-----------|-----------|
| **Začátečník** | ✅ Nastavení & základy | ⚠️ Náročné | ❌ Příliš pokročilé |
| **Středně pokročilý** | ✅ Rychlý přehled | ✅ Klíčové učení | ⚠️ Cíle pro rozvoj |
| **Pokročilý** | ✅ Snadno zvládnutelné | ✅ Zjemnění | ✅ Produkční vzory |

### Dovednosti připravené pro kariéru

**Po tomto workshopu budete připraveni:**

✅ **Vytvářet aplikace zaměřené na soukromí**
- Zdravotnické aplikace zpracovávající PHI/PII lokálně
- Finanční služby s požadavky na dodržování předpisů
- Vládní systémy s potřebou datové suverenity

✅ **Optimalizovat pro edge prostředí**
- IoT zařízení s omezenými zdroji
- Mobilní aplikace s prioritou offline režimu
- Systémy s nízkou latencí v reálném čase

✅ **Navrhovat inteligentní architektury**
- Systémy s více agenty pro komplexní pracovní postupy
- Hybridní nasazení edge-cloud
- Nákladově optimalizovaná AI infrastruktura

✅ **Vést iniciativy Edge AI**
- Hodnotit proveditelnost Edge AI pro projekty
- Vybrat vhodné modely a frameworky
- Navrhovat škálovatelné lokální AI řešení

---

## 🗺️ Struktura workshopu

### Přehled lekcí (6 lekcí × 30 minut = 3 hodiny)

| Lekce | Téma | Zaměření | Délka |
|-------|------|----------|-------|
| **1** | Začínáme s Foundry Local | Instalace, validace, první dokončení | 30 min |
| **2** | Vytváření AI řešení s RAG | Návrh promptů, embeddingy, hodnocení | 30 min |
| **3** | Open Source modely | Objevování modelů, benchmarky, výběr | 30 min |
| **4** | Pokročilé modely | SLM vs LLM, optimalizace, frameworky | 30 min |
| **5** | Agenti pohánění AI | Návrh agentů, orchestrace, paměť | 30 min |
| **6** | Modely jako nástroje | Směrování, řetězení, strategie škálování | 30 min |

---

## 🚀 Rychlý start

### Předpoklady

**Požadavky na systém:**
- **OS**: Windows 10/11, macOS 11+ nebo Linux (Ubuntu 20.04+)
- **RAM**: Minimálně 8GB, doporučeno 16GB+
- **Úložiště**: 10GB+ volného místa pro modely
- **CPU**: Moderní procesor s podporou AVX2
- **GPU** (volitelné): CUDA-kompatibilní nebo Qualcomm NPU pro akceleraci

**Požadavky na software:**
- **Python 3.8+** ([Stáhnout](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Instalační příručka](../../../Workshop))
- **Git** ([Stáhnout](https://git-scm.com/downloads))
- **Visual Studio Code** (doporučeno) ([Stáhnout](https://code.visualstudio.com/))

### Nastavení ve 3 krocích

#### 1. Instalace Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Ověření instalace:**
```bash
foundry --version
foundry service status
```

**Ujistěte se, že Azure AI Foundry Local běží s pevně nastaveným portem**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Ověření funkčnosti:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Zjištění dostupných modelů**
Pro zobrazení dostupných modelů ve vaší instanci Foundry Local můžete dotazovat endpoint modelů:

```bash
# cmd/bash/powershell
foundry model list
```

Použití webového endpointu 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klonování repozitáře a instalace závislostí

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

#### 3. Spuštění prvního příkladu

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Úspěch!** Měli byste vidět streamovanou odpověď o Edge AI.

---

## 📦 Zdroje workshopu

### Python příklady

Postupné praktické příklady demonstrující každý koncept:

| Lekce | Příklad | Popis | Doba běhu |
|-------|---------|-------|-----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Základní & streamovací chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG s embeddingy | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Hodnocení kvality RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking více modelů | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Porovnání SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Systém s více agenty | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Směrování na základě záměru | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Vícekroková pipeline | ~60s |

### Jupyter Notebooks

Interaktivní průzkum s vysvětleními a vizualizacemi:

| Lekce | Notebook | Popis | Obtížnost |
|-------|----------|-------|-----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Základy chatu & streamování | ⭐ Začátečník |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Vytvoření RAG systému | ⭐⭐ Středně pokročilý |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Hodnocení kvality RAG | ⭐⭐ Středně pokročilý |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modelů | ⭐⭐ Středně pokročilý |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porovnání modelů | ⭐⭐ Středně pokročilý |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrace agentů | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Směrování záměrů | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrace pipeline | ⭐⭐⭐ Pokročilý |

### Dokumentace

Komplexní příručky a referenční materiály:

| Dokument | Popis | Použít kdy |
|----------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | Rychlý průvodce nastavením | Začínáte od nuly |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Přehled příkazů & API | Potřebujete rychlé odpovědi |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Vzory & příklady SDK | Píšete kód |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Příručka k proměnným prostředí | Konfigurace příkladů |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Nejnovější vylepšení příkladů | Porozumění změnám |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Příručka migrace | Aktualizace kódu |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Běžné problémy & řešení | Řešení potíží |

---

## 🎓 Doporučení pro vzdělávací cestu

### Pro začátečníky (3-4 hodiny)
1. ✅ Lekce 1: Začínáme (zaměřte se na nastavení a základní chat)
2. ✅ Lekce 2: Základy RAG (zpočátku přeskočte hodnocení)
3. ✅ Lekce 3: Jednoduché benchmarky (pouze 2 modely)
4. ⏭️ Zatím přeskočte lekce 4-6
5. 🔄 Vraťte se k lekcím 4-6 po vytvoření první aplikace

### Pro středně pokročilé vývojáře (3 hodiny)
1. ⚡ Lekce 1: Rychlé ověření nastavení
2. ✅ Lekce 2: Kompletní RAG pipeline s hodnocením
3. ✅ Lekce 3: Plná sada benchmarků
4. ✅ Lekce 4: Optimalizace modelů
5. ✅ Lekce 5-6: Zaměření na architektonické vzory

### Pro pokročilé odborníky (2-3 hodiny)
1. ⚡ Lekce 1-3: Rychlý přehled a ověření
2. ✅ Lekce 4: Hlubší ponor do optimalizace
3. ✅ Lekce 5: Architektura s více agenty
4. ✅ Lekce 6: Produkční vzory a škálování
5. 🚀 Rozšíření: Vytvořte vlastní logiku směrování a hybridní nasazení

---

## Balíček workshopových lekcí (zaměřené 30minutové laboratoře)

Pokud sledujete zhuštěný formát workshopu s 6 lekcemi, použijte tyto dedikované příručky (každá odpovídá a doplňuje širší modulovou dokumentaci výše):

| Workshopová lekce | Příručka | Hlavní zaměření |
|-------------------|----------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalace, validace, spuštění phi & GPT-OSS-20B, akcelerace |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Návrh promptů, RAG vzory, ukotvení v CSV & dokumentech, migrace |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrace Hugging Face, benchmarky, výběr modelů |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX akcelerace |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Role agentů, paměť, nástroje, orchestrace |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Směrování, řetězení, škálování na Azure |

Každý soubor relace obsahuje: abstrakt, vzdělávací cíle, 30minutový demo průběh, startovací projekt, kontrolní seznam validace, řešení problémů a odkazy na oficiální Foundry Local Python SDK.

### Ukázkové skripty

Instalace závislostí workshopu (Windows):

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

Pokud spouštíte službu Foundry Local na jiném (Windows) počítači nebo virtuálním stroji z macOS, exportujte endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Relace | Skript(y) | Popis |
|--------|-----------|-------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap služby & streamovací chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimální RAG (embeddings v paměti) |
|   | `samples/session02/rag_eval_ragas.py` | Hodnocení RAG pomocí metrik ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latence & propustnosti více modelů |
| 4 | `samples/session04/model_compare.py` | Porovnání SLM vs LLM (latence & ukázkový výstup) |
| 5 | `samples/session05/agents_orchestrator.py` | Výzkum dvou agentů → redakční pipeline |
| 6 | `samples/session06/models_router.py` | Demo směrování na základě záměru |
|   | `samples/session06/models_pipeline.py` | Vícekrokový řetězec plánování/vykonávání/zdokonalování |

### Proměnné prostředí (společné pro všechny ukázky)

| Proměnná | Účel | Příklad |
|----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Výchozí alias jednoho modelu pro základní ukázky | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicitní SLM vs větší model pro porovnání | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Seznam aliasů modelů pro benchmarking | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Opakování benchmarku na model | `3` |
| `BENCH_PROMPT` | Prompt použitý při benchmarkingu | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Přepsání testovacího dotazu pro RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Přepsání dotazu pro pipeline agentů | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modelu pro výzkumného agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modelu pro redakčního agenta (může se lišit) | `gpt-oss-20b` |
| `SHOW_USAGE` | Pokud `1`, vypíše využití tokenů na dokončení | `1` |
| `RETRY_ON_FAIL` | Pokud `1`, jednou se pokusí znovu při přechodných chybách chatu | `1` |
| `RETRY_BACKOFF` | Sekundy čekání před opakováním | `1.0` |

Pokud proměnná není nastavena, skripty se vrátí k rozumným výchozím hodnotám. Pro ukázky s jedním modelem obvykle potřebujete pouze `FOUNDRY_LOCAL_ALIAS`.

### Pomocný modul

Všechny ukázky nyní sdílejí pomocný `samples/workshop_utils.py`, který poskytuje:

* Vytvoření cache `FoundryLocalManager` + klienta OpenAI
* Pomocník `chat_once()` s volitelným opakováním + tiskem využití
* Jednoduché hlášení využití tokenů (aktivace přes `SHOW_USAGE=1`)

To snižuje duplicitu a zdůrazňuje osvědčené postupy pro efektivní orchestraci lokálních modelů.

## Volitelná vylepšení (napříč relacemi)

| Téma | Vylepšení | Relace | Env / Přepínač |
|------|-----------|--------|---------------|
| Determinismus | Pevná teplota + stabilní sady promptů | 1–6 | Nastavit `temperature=0`, `top_p=1` |
| Viditelnost využití tokenů | Konzistentní výuka nákladů/efektivity | 1–6 | `SHOW_USAGE=1` |
| Streamování prvního tokenu | Metrika vnímané latence | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odolnost při opakování | Řeší přechodné problémy při studeném startu | Vše | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modeloví agenti | Specializace rolí heterogenních modelů | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivní směrování | Záměr + heuristika nákladů | 6 | Rozšíření směrovače o logiku eskalace |
| Vektorová paměť | Dlouhodobé sémantické vybavení | 2,5,6 | Integrace FAISS/Chroma embedding indexu |
| Export trasování | Auditování & hodnocení | 2,5,6 | Přidání JSON řádků na krok |
| Kvalitativní metriky | Sledování kvality | 3–6 | Sekundární scoring prompty |
| Rychlé testy | Rychlá validace před workshopem | Vše | `python Workshop/tests/smoke.py` |

### Deterministický rychlý start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očekávejte stabilní počty tokenů při opakovaných identických vstupech.

### Hodnocení RAG (Relace 2)

Použijte `rag_eval_ragas.py` k výpočtu relevance odpovědí, věrnosti a přesnosti kontextu na malém syntetickém datasetu:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Rozšiřte dodáním většího JSONL souboru s otázkami, kontexty a pravdivými odpověďmi, poté je převeďte na dataset Hugging Face.

## Příloha přesnosti příkazů CLI

Workshop záměrně používá pouze aktuálně dokumentované / stabilní příkazy Foundry Local CLI.

### Odkazované stabilní příkazy

| Kategorie | Příkaz | Účel |
|-----------|--------|------|
| Jádro | `foundry --version` | Zobrazí nainstalovanou verzi |
| Jádro | `foundry init` | Inicializace konfigurace |
| Služba | `foundry service start` | Spustí lokální službu (pokud není automaticky) |
| Služba | `foundry status` | Zobrazí stav služby |
| Modely | `foundry model list` | Seznam katalogu / dostupných modelů |
| Modely | `foundry model download <alias>` | Stáhne váhy modelu do cache |
| Modely | `foundry model run <alias>` | Spustí (načte) model lokálně; kombinace s `--prompt` pro jednorázové spuštění |
| Modely | `foundry model unload <alias>` / `foundry model stop <alias>` | Uvolní model z paměti (pokud je podporováno) |
| Cache | `foundry cache list` | Seznam modelů v cache (stažených) |
| Systém | `foundry system info` | Snímek hardwarových & akceleračních schopností |
| Systém | `foundry system gpu-info` | Diagnostické informace o GPU |
| Konfigurace | `foundry config list` | Zobrazí aktuální hodnoty konfigurace |
| Konfigurace | `foundry config set <key> <value>` | Aktualizuje konfiguraci |

### Vzorový jednorázový prompt

Namísto zastaralého podpříkazu `model chat` použijte:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Tím se provede jeden cyklus prompt/odpověď a poté se ukončí.

### Odstraněné / vyhýbané vzory

| Zastaralé / Nedokumentované | Náhrada / Doporučení |
|-----------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Použijte jednoduchý `foundry model list` + nedávnou aktivitu / logy |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Použijte benchmarkovací Python skript + nástroje OS (Správce úloh / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latence, p95, tokeny/sekunda: `samples/session03/benchmark_oss_models.py`
- Latence prvního tokenu (streamování): nastavit `BENCH_STREAM=1`
- Využití zdrojů: monitorování OS (Správce úloh, Monitor aktivity, `nvidia-smi`) + `foundry system info`.

Jakmile nové příkazy telemetrie CLI stabilizují, mohou být snadno začleněny do markdown souborů relací.

### Automatická kontrola syntaxe

Automatický linter zabraňuje opětovnému zavedení zastaralých vzorů CLI příkazů uvnitř bloků kódu v markdown souborech:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Zastaralé vzory jsou blokovány uvnitř bloků kódu.

Doporučené náhrady:
| Zastaralé | Náhrada |
|-----------|---------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmarkovací skript + systémové nástroje |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Spustit lokálně:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` se spustí při každém push & PR.

Volitelný pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Rychlá tabulka migrace CLI → SDK

| Úkol | Jednorázový příkaz CLI | Ekvivalent SDK (Python) | Poznámky |
|------|------------------------|-------------------------|----------|
| Spustit model jednou (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automaticky inicializuje službu & cache |
| Stáhnout (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager vybírá nejlepší variantu, pokud alias odpovídá více buildům |
| Seznam katalogu | `foundry model list` | `# use manager for each alias or maintain known list` | CLI agreguje; SDK aktuálně instancuje každou alias |
| Seznam modelů v cache | `foundry cache list` | `manager.list_cached_models()` | Po inicializaci manageru (jakýkoli alias) |
| Aktivovat akceleraci GPU | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Konfigurace je externí vedlejší efekt |
| Získat URL endpointu | (implicitní) | `manager.endpoint` | Používá se k vytvoření klienta kompatibilního s OpenAI |
| Zahřát model | `foundry model run <alias>` a poté první prompt | `chat_once(alias, messages=[...])` (pomocník) | Pomocníci řeší počáteční latenci při studeném startu |
| Měřit latenci | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (nebo nový exportní skript) | Preferujte skript pro konzistentní metriky |
| Zastavit / uvolnit model | `foundry model unload <alias>` | (Není vystaveno – restartovat službu / proces) | Typicky není nutné pro průběh workshopu |
| Získat využití tokenů | (zobrazit výstup) | `resp.usage.total_tokens` | Poskytováno, pokud backend vrací objekt využití |

## Export benchmarků do Markdownu

Použijte skript `Workshop/scripts/export_benchmark_markdown.py` k provedení nového benchmarku (stejná logika jako `samples/session03/benchmark_oss_models.py`) a k vytvoření tabulky Markdown přátelské k GitHubu plus surového JSON.

### Příklad

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generované soubory:
| Soubor | Obsah |
|--------|-------|
| `benchmark_report.md` | Tabulka Markdown + interpretace |
| `benchmark_report.json` | Surové pole metrik (pro porovnání / sledování trendů) |

Nastavte `BENCH_STREAM=1` v prostředí pro zahrnutí latence prvního tokenu, pokud je podporována.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.