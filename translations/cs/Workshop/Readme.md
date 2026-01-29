# EdgeAI pro začátečníky - Workshop

> **Praktická cesta k vytvoření produkčně připravených Edge AI aplikací**
>
> Ovládněte lokální nasazení AI pomocí Microsoft Foundry Local, od prvního chatovacího dokončení až po orchestraci více agentů v 6 postupných lekcích.

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

**Tento workshop tyto dovednosti poskytuje**

Během 6 zaměřených lekcí (~3 hodiny celkem) se posunete od "Hello World" k nasazení produkčně připravených systémů s více agenty - vše běžící lokálně na vašem zařízení.

---

## 📚 Cíle učení

Po absolvování tohoto workshopu budete schopni:

### Klíčové kompetence
1. **Nasadit a spravovat lokální AI služby**
   - Instalovat a konfigurovat Microsoft Foundry Local
   - Vybrat vhodné modely pro nasazení na edge
   - Spravovat životní cyklus modelů (stahování, načítání, ukládání do mezipaměti)
   - Monitorovat využití zdrojů a optimalizovat výkon

2. **Vytvářet aplikace poháněné AI**
   - Implementovat chatovací dokončení kompatibilní s OpenAI lokálně
   - Navrhovat efektivní prompty pro malé jazykové modely
   - Zpracovávat streamované odpovědi pro lepší uživatelský zážitek
   - Integrovat lokální modely do stávajících aplikací

3. **Vytvářet systémy RAG (Retrieval Augmented Generation)**
   - Vytvářet sémantické vyhledávání pomocí embeddingů
   - Zakládat odpovědi LLM na znalostech specifických pro danou oblast
   - Hodnotit kvalitu RAG pomocí průmyslových standardních metrik
   - Škálovat od prototypu k produkci

4. **Optimalizovat výkon modelů**
   - Provádět benchmarky různých modelů pro vaše použití
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

Na konci tohoto workshopu budete mít vytvořeno:

| Lekce | Výstup | Demonstrované dovednosti |
|-------|--------|--------------------------|
| **1** | Chatovací aplikace se streamováním | Nastavení služby, základní dokončení, streamovací UX |
| **2** | Systém RAG s hodnocením | Embeddingy, sémantické vyhledávání, kvalitativní metriky |
| **3** | Sada benchmarků pro více modelů | Měření výkonu, porovnání modelů |
| **4** | Porovnání SLM vs LLM | Analýza kompromisů, optimalizační strategie |
| **5** | Orchestrátor s více agenty | Návrh agentů, správa paměti, koordinace |
| **6** | Inteligentní směrovací systém | Detekce záměru, výběr modelu, škálovatelnost |

### Matice kompetencí

| Úroveň dovedností | Lekce 1-2 | Lekce 3-4 | Lekce 5-6 |
|-------------------|-----------|-----------|-----------|
| **Začátečník** | ✅ Nastavení & základy | ⚠️ Náročné | ❌ Příliš pokročilé |
| **Středně pokročilý** | ✅ Rychlý přehled | ✅ Klíčové učení | ⚠️ Výzvy |
| **Pokročilý** | ✅ Snadné | ✅ Zlepšení | ✅ Produkční vzory |

### Dovednosti připravené pro kariéru

**Po tomto workshopu budete připraveni:**

✅ **Vytvářet aplikace s prioritou soukromí**
- Zdravotnické aplikace zpracovávající PHI/PII lokálně
- Finanční služby s požadavky na dodržování předpisů
- Vládní systémy s požadavky na suverenitu dat

✅ **Optimalizovat pro prostředí Edge**
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
| **1** | Začínáme s Foundry Local | Instalace, ověření, první dokončení | 30 min |
| **2** | Vytváření AI řešení s RAG | Návrh promptů, embeddingy, hodnocení | 30 min |
| **3** | Open Source modely | Objevování modelů, benchmarky, výběr | 30 min |
| **4** | Nejmodernější modely | SLM vs LLM, optimalizace, frameworky | 30 min |
| **5** | AI-pohánění agenti | Návrh agentů, orchestrace, paměť | 30 min |
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
- **Microsoft Foundry Local** ([Průvodce instalací](../../../Workshop))
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
Chcete-li zjistit, které modely jsou dostupné ve vaší instanci Foundry Local, můžete dotazovat endpoint modelů:

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

Postupné praktické ukázky demonstrující každý koncept:

| Lekce | Příklad | Popis | Doba běhu |
|-------|---------|-------|----------|
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
|-------|----------|-------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Základy chatu & streamování | ⭐ Začátečník |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Vytvoření systému RAG | ⭐⭐ Středně pokročilý |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Hodnocení kvality RAG | ⭐⭐ Středně pokročilý |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modelů | ⭐⭐ Středně pokročilý |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porovnání modelů | ⭐⭐ Středně pokročilý |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrace agentů | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Směrování na základě záměru | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrace pipeline | ⭐⭐⭐ Pokročilý |

### Dokumentace

Komplexní průvodce a reference:

| Dokument | Popis | Použít kdy |
|----------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | Rychlý průvodce nastavením | Začínáte od nuly |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Přehled příkazů & API | Potřebujete rychlé odpovědi |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Vzory & příklady SDK | Píšete kód |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Průvodce proměnnými prostředí | Konfigurujete příklady |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Běžné problémy & opravy | Řešíte problémy |

---

## 🎓 Doporučení pro cestu učení

### Pro začátečníky (3-4 hodiny)
1. ✅ Lekce 1: Začínáme (zaměřte se na nastavení a základní chat)
2. ✅ Lekce 2: Základy RAG (zpočátku přeskočte hodnocení)
3. ✅ Lekce 3: Jednoduché benchmarky (pouze 2 modely)
4. ⏭️ Zatím přeskočte lekce 4-6
5. 🔄 Vraťte se k lekcím 4-6 po vytvoření první aplikace

### Pro středně pokročilé vývojáře (3 hodiny)
1. ⚡ Lekce 1: Rychlé ověření nastavení
2. ✅ Lekce 2: Kompletní pipeline RAG s hodnocením
3. ✅ Lekce 3: Kompletní sada benchmarků
4. ✅ Lekce 4: Optimalizace modelů
5. ✅ Lekce 5-6: Zaměřte se na vzory architektury

### Pro pokročilé odborníky (2-3 hodiny)
1. ⚡ Lekce 1-3: Rychlý přehled a ověření
2. ✅ Lekce 4: Hlubší ponor do optimalizace
3. ✅ Lekce 5: Architektura s více agenty
4. ✅ Lekce 6: Produkční vzory a škálování
5. 🚀 Rozšíření: Vytvořte vlastní logiku směrování a hybridní nasazení

---

## Balíček workshopových lekcí (zaměřené 30minutové laboratoře)

Pokud následujete zkrácený formát workshopu o 6 lekcích, použijte tyto dedikované průvodce (každý odpovídá a doplňuje širší dokumentaci modulů výše):

| Workshopová lekce | Průvodce | Hlavní zaměření |
|-------------------|----------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalace, ověření, spuštění phi & GPT-OSS-20B, akcelerace |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Návrh promptů, vzory RAG, CSV & dokumentové zakotvení, migrace |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrace Hugging Face, benchmarky, výběr modelů |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, akcelerace ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Role agentů, paměť, nástroje, orchestrace |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Směrování, řetězení, škálování cesty do Azure |

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
| 1 | `samples/session01/chat_bootstrap.py` | Spuštění služby & streamovací chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimální RAG (embeddings v paměti) |
|   | `samples/session02/rag_eval_ragas.py` | Hodnocení RAG pomocí metrik ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latence a propustnosti více modelů |
| 4 | `samples/session04/model_compare.py` | Porovnání SLM vs LLM (latence & ukázkový výstup) |
| 5 | `samples/session05/agents_orchestrator.py` | Výzkum dvou agentů → redakční pipeline |
| 6 | `samples/session06/models_router.py` | Demo směrování na základě záměru |
|   | `samples/session06/models_pipeline.py` | Vícekrokový plán/realizace/zlepšení řetězu |

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
| `SHOW_USAGE` | Pokud `1`, tiskne využití tokenů na dokončení | `1` |
| `RETRY_ON_FAIL` | Pokud `1`, jednou se pokusí znovu při přechodných chybách chatu | `1` |
| `RETRY_BACKOFF` | Sekundy čekání před opakováním | `1.0` |

Pokud není proměnná nastavena, skripty se vrací k rozumným výchozím hodnotám. Pro ukázky s jedním modelem obvykle potřebujete pouze `FOUNDRY_LOCAL_ALIAS`.

### Pomocný modul

Všechny ukázky nyní sdílejí pomocný `samples/workshop_utils.py`, který poskytuje:

* Vytvoření cache `FoundryLocalManager` + klienta OpenAI
* Pomocník `chat_once()` s volitelným opakováním + tiskem využití
* Jednoduché hlášení využití tokenů (aktivace přes `SHOW_USAGE=1`)

To snižuje duplicitu a zdůrazňuje osvědčené postupy pro efektivní orchestraci lokálních modelů.

## Volitelná vylepšení (napříč relacemi)

| Téma | Vylepšení | Relace | Env / Přepínač |
|------|-----------|--------|---------------|
| Determinismus | Pevná teplota + stabilní sady promptů | 1–6 | Nastavte `temperature=0`, `top_p=1` |
| Viditelnost využití tokenů | Konzistentní výuka nákladů/efektivity | 1–6 | `SHOW_USAGE=1` |
| Streamování prvního tokenu | Metrika vnímané latence | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odolnost vůči opakování | Řeší přechodné problémy při studeném startu | Vše | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modeloví agenti | Specializace rolí v heterogenním prostředí | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivní směrování | Záměr + heuristiky nákladů | 6 | Rozšíření routeru o logiku eskalace |
| Vektorová paměť | Dlouhodobé sémantické vybavení | 2,5,6 | Integrace FAISS/Chroma embedding indexu |
| Export trasování | Auditování & hodnocení | 2,5,6 | Přidání JSON řádků na krok |
| Kvalitativní rubriky | Sledování kvality | 3–6 | Sekundární scoring promptů |
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

Rozšiřte dodáním většího JSONL souboru otázek, kontextů a pravdivých odpovědí, poté konvertujte na Hugging Face `Dataset`.

## Příloha přesnosti CLI příkazů

Workshop záměrně používá pouze aktuálně dokumentované / stabilní příkazy Foundry Local CLI.

### Odkazované stabilní příkazy

| Kategorie | Příkaz | Účel |
|-----------|--------|------|
| Jádro | `foundry --version` | Zobrazení nainstalované verze |
| Služba | `foundry service start` | Spuštění lokální služby (pokud není automatické) |
| Služba | `foundry service status` | Zobrazení stavu služby |
| Modely | `foundry model list` | Seznam katalogu / dostupných modelů |
| Modely | `foundry model download <alias>` | Stažení váhy modelu do cache |
| Modely | `foundry model run <alias>` | Spuštění (načtení) modelu lokálně; kombinace s `--prompt` pro jednorázové spuštění |
| Modely | `foundry model unload <alias>` / `foundry model stop <alias>` | Vyložení modelu z paměti (pokud je podporováno) |
| Cache | `foundry cache list` | Seznam modelů v cache (stažených) |

### Jednorázový prompt vzor

Namísto zastaralého podpříkazu `model chat` použijte:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Tím se provede jeden cyklus prompt/odpověď a poté se ukončí.

### Odstraněné / vyhýbané vzory

| Zastaralé / Nedokumentované | Náhrada / Doporučení |
|-----------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Použijte jednoduchý `foundry model list` + nedávná aktivita / logy |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Použijte benchmarkovací Python skript + nástroje OS (Správce úloh / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latence, p95, tokeny/sekunda: `samples/session03/benchmark_oss_models.py`
- Latence prvního tokenu (streamování): nastavte `BENCH_STREAM=1`
- Využití zdrojů: Monitory OS (Správce úloh, Activity Monitor, `nvidia-smi`).

Jakmile nové telemetrické příkazy CLI stabilizují upstream, mohou být začleněny s minimálními úpravami do markdown souborů relací.

### Automatická kontrola syntaxe

Automatický linter zabraňuje opětovnému zavedení zastaralých CLI vzorů uvnitř bloků kódu v markdown souborech:

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

Spusťte lokálně:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` se spouští při každém push & PR.

Volitelný pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Rychlá tabulka migrace CLI → SDK

| Úkol | CLI Jednorázový příkaz | SDK (Python) Ekvivalent | Poznámky |
|------|------------------------|-------------------------|----------|
| Spuštění modelu jednou (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automaticky inicializuje službu & cache |
| Stažení (cache) modelu | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # spustí stažení/načtení` | Manager vybírá nejlepší variantu, pokud alias mapuje na více buildů |
| Seznam katalogu | `foundry model list` | `# použijte manager pro každý alias nebo udržujte známý seznam` | CLI agreguje; SDK aktuálně instancuje per-alias |
| Seznam modelů v cache | `foundry cache list` | `manager.list_cached_models()` | Po inicializaci manageru (jakýkoli alias) |
| Získání URL endpointu | (implicitní) | `manager.endpoint` | Používá se k vytvoření klienta kompatibilního s OpenAI |
| Zahřátí modelu | `foundry model run <alias>` poté první prompt | `chat_once(alias, messages=[...])` (utility) | Utility řeší počáteční studenou latenci zahřátí |
| Měření latence | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (nebo nový exportní skript) | Preferujte skript pro konzistentní metriky |
| Zastavení / vyložení modelu | `foundry model unload <alias>` | (Není vystaveno – restartujte službu / proces) | Typicky není vyžadováno pro průběh workshopu |
| Získání využití tokenů | (zobrazení výstupu) | `resp.usage.total_tokens` | Poskytováno, pokud backend vrací objekt využití |

## Export benchmarku do Markdownu

Použijte skript `Workshop/scripts/export_benchmark_markdown.py` k provedení čerstvého benchmarku (stejná logika jako `samples/session03/benchmark_oss_models.py`) a emitujte GitHub-friendly Markdown tabulku plus surový JSON.

### Příklad

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generované soubory:
| Soubor | Obsah |
|--------|-------|
| `benchmark_report.md` | Markdown tabulka + interpretační tipy |
| `benchmark_report.json` | Surové pole metrik (pro porovnání / sledování trendů) |

Nastavte `BENCH_STREAM=1` v prostředí pro zahrnutí latence prvního tokenu, pokud je podporováno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->