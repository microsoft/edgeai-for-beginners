<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:56:43+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "hu"
}
-->
# EdgeAI kezdőknek - Workshop

> **Gyakorlati tanulási útmutató termelésre kész Edge AI alkalmazások fejlesztéséhez**
>
> Sajátítsd el a helyi AI telepítést a Microsoft Foundry Local segítségével, az első chat válaszadástól a többügynökös koordinációig, 6 egymást követő szakaszban.

---

## 🎯 Bevezetés

Üdvözlünk az **EdgeAI kezdőknek Workshopon** - gyakorlati útmutató az intelligens alkalmazások fejlesztéséhez, amelyek teljes mértékben helyi hardveren futnak. Ez a workshop az elméleti Edge AI koncepciókat valós készségekké alakítja át, fokozatosan nehezedő gyakorlatokon keresztül, a Microsoft Foundry Local és Kis Nyelvi Modellek (SLM-ek) használatával.

### Miért érdemes részt venni ezen a workshopon?

**Az Edge AI forradalma megérkezett**

Világszerte egyre több szervezet tér át a felhőfüggő AI-ról az edge computingra három kulcsfontosságú ok miatt:

1. **Adatvédelem és megfelelőség** - Érzékeny adatok helyi feldolgozása felhőbe történő továbbítás nélkül (HIPAA, GDPR, pénzügyi szabályozások)
2. **Teljesítmény** - Hálózati késleltetés kiküszöbölése (50-500ms helyi vs 500-2000ms felhő körút)
3. **Költségkontroll** - Tokenenkénti API költségek eltávolítása és skálázás felhő költségek nélkül

**De az Edge AI más**

Az AI helyi futtatása új készségeket igényel:
- Modell kiválasztása és optimalizálása erőforrás-korlátokhoz
- Helyi szolgáltatáskezelés és hardvergyorsítás
- Prompt tervezés kisebb modellekhez
- Termelési telepítési minták edge eszközökhöz

**Ez a workshop ezeket a készségeket nyújtja**

6 fókuszált szakaszban (~3 óra összesen) haladsz a "Hello World"-től a termelésre kész többügynökös rendszerek telepítéséig - mindezt helyben, a saját gépeden.

---

## 📚 Tanulási célok

A workshop elvégzésével képes leszel:

### Alapvető kompetenciák
1. **Helyi AI szolgáltatások telepítése és kezelése**
   - Microsoft Foundry Local telepítése és konfigurálása
   - Megfelelő modellek kiválasztása edge telepítéshez
   - Modell életciklusának kezelése (letöltés, betöltés, gyorsítótárazás)
   - Erőforrás-használat monitorozása és teljesítmény optimalizálása

2. **AI-alapú alkalmazások építése**
   - OpenAI-kompatibilis chat válaszok helyi megvalósítása
   - Hatékony promptok tervezése Kis Nyelvi Modellekhez
   - Streaming válaszok kezelése a jobb felhasználói élmény érdekében
   - Helyi modellek integrálása meglévő alkalmazásokba

3. **RAG (Retrieval Augmented Generation) rendszerek létrehozása**
   - Szemantikus keresés építése beágyazásokkal
   - LLM válaszok alapozása domain-specifikus tudásra
   - RAG minőségének értékelése iparági szabványokkal
   - Prototípustól termelésig történő skálázás

4. **Modell teljesítményének optimalizálása**
   - Több modell benchmarkolása az adott felhasználási esethez
   - Késleltetés, áteresztőképesség és első token idő mérése
   - Optimális modellek kiválasztása sebesség/minőség kompromisszumok alapján
   - SLM vs LLM kompromisszumok összehasonlítása valós forgatókönyvekben

5. **Többügynökös rendszerek koordinálása**
   - Speciális ügynökök tervezése különböző feladatokhoz
   - Ügynök memória és kontextus kezelés megvalósítása
   - Ügynökök koordinálása összetett munkafolyamatokban
   - Kérések intelligens irányítása több modell között

6. **Termelésre kész megoldások telepítése**
   - Hibakezelés és újrapróbálkozási logika megvalósítása
   - Token használat és rendszer erőforrások monitorozása
   - Skálázható architektúrák építése modell-eszköz mintákkal
   - Migrációs utak tervezése edge-ről hibridre (edge + felhő)

---

## 🎓 Tanulási eredmények

### Amit építeni fogsz

A workshop végére elkészíted:

| Szakasz | Eredmény | Demonstrált készségek |
|---------|----------|-----------------------|
| **1** | Chat alkalmazás streaminggel | Szolgáltatás beállítása, alapvető válaszok, streaming UX |
| **2** | RAG rendszer értékeléssel | Beágyazások, szemantikus keresés, minőségi metrikák |
| **3** | Többmodell benchmark készlet | Teljesítmény mérés, modell összehasonlítás |
| **4** | SLM vs LLM összehasonlító | Kompromisszum elemzés, optimalizálási stratégiák |
| **5** | Többügynökös koordinátor | Ügynök tervezés, memória kezelés, koordináció |
| **6** | Intelligens irányítási rendszer | Szándék felismerés, modell kiválasztás, skálázhatóság |

### Kompetencia mátrix

| Készség szint | Szakasz 1-2 | Szakasz 3-4 | Szakasz 5-6 |
|---------------|-------------|-------------|-------------|
| **Kezdő** | ✅ Beállítás és alapok | ⚠️ Kihívás | ❌ Túl nehéz |
| **Középhaladó** | ✅ Gyors áttekintés | ✅ Alapvető tanulás | ⚠️ Nyújtott célok |
| **Haladó** | ✅ Könnyedén | ✅ Finomítás | ✅ Termelési minták |

### Karrierre kész készségek

**A workshop után képes leszel:**

✅ **Adatvédelem-központú alkalmazások építése**
- Egészségügyi alkalmazások, amelyek helyben kezelik a PHI/PII-t
- Pénzügyi szolgáltatások megfelelőségi követelményekkel
- Kormányzati rendszerek adat szuverenitási igényekkel

✅ **Optimalizálás edge környezetekhez**
- IoT eszközök korlátozott erőforrásokkal
- Offline-első mobilalkalmazások
- Alacsony késleltetésű valós idejű rendszerek

✅ **Intelligens architektúrák tervezése**
- Többügynökös rendszerek összetett munkafolyamatokhoz
- Hibrid edge-felhő telepítések
- Költséghatékony AI infrastruktúra

✅ **Edge AI kezdeményezések vezetése**
- Edge AI megvalósíthatóságának értékelése projektekhez
- Megfelelő modellek és keretrendszerek kiválasztása
- Skálázható helyi AI megoldások tervezése

---

## 🗺️ Workshop felépítése

### Szakasz áttekintés (6 szakasz × 30 perc = 3 óra)

| Szakasz | Téma | Fókusz | Időtartam |
|---------|------|--------|-----------|
| **1** | Kezdés a Foundry Local-lal | Telepítés, validálás, első válaszok | 30 perc |
| **2** | AI megoldások építése RAG-gal | Prompt tervezés, beágyazások, értékelés | 30 perc |
| **3** | Nyílt forráskódú modellek | Modell felfedezés, benchmarkolás, kiválasztás | 30 perc |
| **4** | Legújabb modellek | SLM vs LLM, optimalizálás, keretrendszerek | 30 perc |
| **5** | AI-alapú ügynökök | Ügynök tervezés, koordináció, memória | 30 perc |
| **6** | Modellek mint eszközök | Irányítás, láncolás, skálázási stratégiák | 30 perc |

---

## 🚀 Gyors kezdés

### Előfeltételek

**Rendszerkövetelmények:**
- **OS**: Windows 10/11, macOS 11+, vagy Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, ajánlott 16GB+
- **Tárhely**: Minimum 10GB szabad hely modellekhez
- **CPU**: Modern processzor AVX2 támogatással
- **GPU** (opcionális): CUDA-kompatibilis vagy Qualcomm NPU gyorsításhoz

**Szoftverkövetelmények:**
- **Python 3.8+** ([Letöltés](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Telepítési útmutató](../../../Workshop))
- **Git** ([Letöltés](https://git-scm.com/downloads))
- **Visual Studio Code** (ajánlott) ([Letöltés](https://code.visualstudio.com/))

### Beállítás 3 lépésben

#### 1. Foundry Local telepítése

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Telepítés ellenőrzése:**
```bash
foundry --version
foundry service status
```

**Győződj meg róla, hogy az Azure AI Foundry Local fix porttal fut**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Ellenőrizd a működést:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Elérhető modellek keresése**
Az elérhető modellek megtekintéséhez a Foundry Local példányban lekérdezheted a modellek végpontját:

```bash
# cmd/bash/powershell
foundry model list
```

Webes végpont használata 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Tároló klónozása és függőségek telepítése

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

#### 3. Futtasd az első mintát

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Siker!** Egy streaming válasz jelenik meg az edge AI-ról.

---

## 📦 Workshop források

### Python minták

Fokozatos, gyakorlati példák, amelyek bemutatják az egyes koncepciókat:

| Szakasz | Minta | Leírás | Futtatási idő |
|---------|-------|--------|--------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Alapvető és streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG beágyazásokkal | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG minőség értékelése | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Többmodell benchmarkolás | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM összehasonlítás | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Többügynökös rendszer | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Szándék-alapú irányítás | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Többlépcsős folyamat | ~60s |

### Jupyter jegyzetfüzetek

Interaktív felfedezés magyarázatokkal és vizualizációkkal:

| Szakasz | Jegyzetfüzet | Leírás | Nehézség |
|---------|--------------|--------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat alapok és streaming | ⭐ Kezdő |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG rendszer építése | ⭐⭐ Középhaladó |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG minőség értékelése | ⭐⭐ Középhaladó |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modell benchmarkolás | ⭐⭐ Középhaladó |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modell összehasonlítás | ⭐⭐ Középhaladó |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Ügynök koordináció | ⭐⭐⭐ Haladó |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Szándék irányítás | ⭐⭐⭐ Haladó |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Folyamat koordináció | ⭐⭐⭐ Haladó |

### Dokumentáció

Átfogó útmutatók és referenciák:

| Dokumentum | Leírás | Használat ideje |
|------------|--------|-----------------|
| [QUICK_START.md](./QUICK_START.md) | Gyors beállítási útmutató | Kezdéskor |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Parancs és API segédlet | Gyors válaszokhoz |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK minták és példák | Kód írásakor |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Környezeti változók útmutatója | Minták konfigurálása |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Legújabb minta fejlesztések | Változások megértése |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migrációs útmutató | Kód frissítése |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Gyakori problémák és megoldások | Hibák elhárítása |

---

## 🎓 Tanulási útmutató ajánlások

### Kezdőknek (3-4 óra)
1. ✅ 1. szakasz: Kezdés (fókusz a beállításon és az alapvető chaten)
2. ✅ 2. szakasz: RAG alapok (értékelés kihagyása kezdetben)
3. ✅ 3. szakasz: Egyszerű benchmarkolás (csak 2 modell)
4. ⏭️ 4-6. szakaszok kihagyása egyelőre
5. 🔄 Térj vissza a 4-6. szakaszokra az első alkalmazás elkészítése után

### Középhaladó fejlesztőknek (3 óra)
1. ⚡ 1. szakasz: Gyors beállítás ellenőrzése
2. ✅ 2. szakasz: Teljes RAG folyamat értékeléssel
3. ✅ 3. szakasz: Teljes benchmark készlet
4. ✅ 4. szakasz: Modell optimalizálás
5. ✅ 5-6. szakaszok: Fókusz az architektúra mintákra

### Haladó szakembereknek (2-3 óra)
1. ⚡ 1-3. szakaszok: Gyors áttekintés és ellenőrzés
2. ✅ 4. szakasz: Mélyreható optimalizálás
3. ✅ 5. szakasz: Többügynökös architektúra
4. ✅ 6. szakasz: Termelési minták és skálázás
5. 🚀 Kiterjesztés: Egyedi irányítási logika és hibrid telepítések építése

---

## Workshop szakasz csomag (Fókuszált 30 perces laborok)

Ha a tömörített 6 szakaszos workshop formát követed, használd ezeket a dedikált útmutatókat (mindegyik megfelel és kiegészíti a fentebb bemutatott átfogó modul dokumentációkat):

| Workshop szakasz | Útmutató | Fő fókusz |
|------------------|----------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Telepítés, validálás, phi & GPT-OSS-20B futtat
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX gyorsítás |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Ügynök szerepek, memória, eszközök, összehangolás |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Útvonalválasztás, láncolás, skálázási útvonal Azure-ra |

Minden szekciófájl tartalmazza: összefoglaló, tanulási célok, 30 perces bemutató folyamat, kezdő projekt, ellenőrző lista, hibakeresés és hivatkozások az hivatalos Foundry Local Python SDK-hoz.

### Példa szkriptek

Workshop függőségek telepítése (Windows):

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

Ha a Foundry Local szolgáltatást másik (Windows) gépen vagy VM-en futtatja macOS-ről, exportálja az endpointot:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Szekció | Szkript(ek) | Leírás |
|---------|-------------|--------|
| 1 | `samples/session01/chat_bootstrap.py` | Szolgáltatás indítása és streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimális RAG (memóriában tárolt beágyazások) |
|   | `samples/session02/rag_eval_ragas.py` | RAG értékelés ragas metrikákkal |
| 3 | `samples/session03/benchmark_oss_models.py` | Több modell késleltetés és áteresztőképesség benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM összehasonlítás (késleltetés és mintakimenet) |
| 5 | `samples/session05/agents_orchestrator.py` | Két ügynök kutatás → szerkesztői folyamat |
| 6 | `samples/session06/models_router.py` | Szándék-alapú útválasztás bemutató |
|   | `samples/session06/models_pipeline.py` | Többlépéses tervezés/végrehajtás/finomítás lánc |

### Környezeti változók (minden mintához közös)

| Változó | Cél | Példa |
|---------|-----|-------|
| `FOUNDRY_LOCAL_ALIAS` | Alapértelmezett egyetlen modell alias alapmintákhoz | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Kifejezett SLM vs nagyobb modell összehasonlításhoz | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Aliasok vesszővel elválasztott listája benchmarkinghoz | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark ismétlések modellenként | `3` |
| `BENCH_PROMPT` | Benchmarking során használt prompt | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers beágyazási modell | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Tesztkérdés felülírása RAG pipeline-hoz | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Ügynök pipeline kérdés felülírása | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Modell alias kutatási ügynökhöz | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Modell alias szerkesztő ügynökhöz (eltérhet) | `gpt-oss-20b` |
| `SHOW_USAGE` | Ha `1`, megjeleníti a token használatot befejezésenként | `1` |
| `RETRY_ON_FAIL` | Ha `1`, egyszer újrapróbálkozik átmeneti chat hibák esetén | `1` |
| `RETRY_BACKOFF` | Másodpercek várakozása újrapróbálkozás előtt | `1.0` |

Ha egy változó nincs beállítva, a szkriptek ésszerű alapértelmezésekre esnek vissza. Egyetlen modell bemutatókhoz általában csak a `FOUNDRY_LOCAL_ALIAS` szükséges.

### Segédmodul

Minden minta megoszt egy segédprogramot, `samples/workshop_utils.py`, amely biztosítja:

* Cache-elt `FoundryLocalManager` + OpenAI kliens létrehozása
* `chat_once()` segédprogram opcionális újrapróbálkozással + használati statisztikák megjelenítésével
* Egyszerű token használati jelentés (engedélyezés: `SHOW_USAGE=1`)

Ez csökkenti a duplikációt és kiemeli a legjobb gyakorlatokat a hatékony helyi modell összehangoláshoz.

## Opcionális fejlesztések (szekciók között)

| Téma | Fejlesztés | Szekciók | Környezet / Kapcsoló |
|------|------------|----------|----------------------|
| Determinizmus | Fixált hőmérséklet + stabil prompt készletek | 1–6 | Állítsa be: `temperature=0`, `top_p=1` |
| Token használat láthatósága | Következetes költség/hatékonyság tanítás | 1–6 | `SHOW_USAGE=1` |
| Első token streaming | Érzékelt késleltetési metrika | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Újrapróbálkozási ellenállás | Átmeneti hidegindítás kezelése | Minden | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Többmodellű ügynökök | Heterogén szerepspecializáció | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptív útválasztás | Szándék + költség heurisztikák | 6 | Router kiterjesztése eszkalációs logikával |
| Vektormemória | Hosszú távú szemantikai visszaemlékezés | 2,5,6 | FAISS/Chroma beágyazási index integrálása |
| Nyomkövetés exportálása | Auditálás és értékelés | 2,5,6 | JSON sorok hozzáadása lépésenként |
| Minőségi rubrikák | Minőségi nyomon követés | 3–6 | Másodlagos pontozási promptok |
| Gyors tesztek | Gyors workshop előtti validáció | Minden | `python Workshop/tests/smoke.py` |

### Determinisztikus gyors kezdés

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Várható stabil token szám ismételt azonos bemenetek esetén.

### RAG értékelés (2. szekció)

Használja a `rag_eval_ragas.py` szkriptet válasz relevancia, hitelesség és kontextus pontosság kiszámításához egy apró szintetikus adathalmazon:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Bővítse egy nagyobb JSONL kérdések, kontextusok és valós adatok megadásával, majd konvertálja Hugging Face `Dataset`-re.

## CLI parancs pontossági melléklet

A workshop szándékosan csak jelenleg dokumentált / stabil Foundry Local CLI parancsokat használ.

### Hivatkozott stabil parancsok

| Kategória | Parancs | Cél |
|-----------|---------|-----|
| Alap | `foundry --version` | Telepített verzió megjelenítése |
| Alap | `foundry init` | Konfiguráció inicializálása |
| Szolgáltatás | `foundry service start` | Helyi szolgáltatás indítása (ha nem automatikus) |
| Szolgáltatás | `foundry status` | Szolgáltatás állapotának megjelenítése |
| Modellek | `foundry model list` | Katalógus / elérhető modellek listázása |
| Modellek | `foundry model download <alias>` | Modell súlyok letöltése a cache-be |
| Modellek | `foundry model run <alias>` | Modell indítása (betöltése) helyben; kombinálható `--prompt`-tal egyetlen futtatáshoz |
| Modellek | `foundry model unload <alias>` / `foundry model stop <alias>` | Modell kiürítése a memóriából (ha támogatott) |
| Cache | `foundry cache list` | Cache-elt (letöltött) modellek listázása |
| Rendszer | `foundry system info` | Hardver és gyorsítási képességek pillanatképe |
| Rendszer | `foundry system gpu-info` | GPU diagnosztikai információk |
| Konfiguráció | `foundry config list` | Jelenlegi konfigurációs értékek megjelenítése |
| Konfiguráció | `foundry config set <key> <value>` | Konfiguráció frissítése |

### Egyetlen prompt minta

A `model chat` alparancs helyett használja:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ez egyetlen prompt/válasz ciklust hajt végre, majd kilép.

### Eltávolított / kerülendő minták

| Elavult / Nem dokumentált | Helyettesítés / Útmutatás |
|---------------------------|--------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Használja a sima `foundry model list`-et + legutóbbi aktivitás / naplók |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Használja a benchmark Python szkriptet + OS eszközöket (Feladatkezelő / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking és telemetria

- Késleltetés, p95, tokenek/másodperc: `samples/session03/benchmark_oss_models.py`
- Első token késleltetés (streaming): állítsa be `BENCH_STREAM=1`
- Erőforrás használat: OS monitorok (Feladatkezelő, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Amint új CLI telemetria parancsok stabilizálódnak, minimális szerkesztéssel beépíthetők a szekció markdownokba.

### Automatikus lint őr

Egy automatikus linter megakadályozza az elavult CLI minták újbóli bevezetését a markdown fájlok kódkerítéseiben:

Szkript: `Workshop/scripts/lint_markdown_cli.py`

Elavult minták blokkolva vannak a kódkerítésekben.

Ajánlott helyettesítések:
| Elavult | Helyettesítés |
|---------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark szkript + rendszer eszközök |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Futtatás helyben:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` minden push és PR esetén fut.

Opcionális pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Gyors CLI → SDK migrációs táblázat

| Feladat | CLI egy soros | SDK (Python) megfelelője | Megjegyzések |
|---------|---------------|--------------------------|--------------|
| Modell futtatása egyszer (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Az SDK automatikusan inicializálja a szolgáltatást és a cache-t |
| Modell letöltése (cache) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | A Manager a legjobb változatot választja, ha az alias több buildhez is tartozik |
| Katalógus listázása | `foundry model list` | `# use manager for each alias or maintain known list` | A CLI aggregál; az SDK jelenleg aliasonkénti inicializálást igényel |
| Cache-elt modellek listázása | `foundry cache list` | `manager.list_cached_models()` | Manager inicializálása után (bármely alias) |
| GPU gyorsítás engedélyezése | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | A konfiguráció külső hatás |
| Endpoint URL lekérése | (implicit) | `manager.endpoint` | OpenAI-kompatibilis kliens létrehozásához használható |
| Modell melegítése | `foundry model run <alias>` majd első prompt | `chat_once(alias, messages=[...])` (utility) | A segédprogramok kezelik a kezdeti hideg késleltetési melegítést |
| Késleltetés mérése | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (vagy új exportáló szkript) | A szkriptet preferálja a következetes metrikákhoz |
| Modell leállítása / kiürítése | `foundry model unload <alias>` | (Nem elérhető – szolgáltatás / folyamat újraindítása) | Általában nem szükséges a workshop folyamatban |
| Token használat lekérése | (nézze meg a kimenetet) | `resp.usage.total_tokens` | Ha a backend visszaadja a használati objektumot |

## Benchmark Markdown exportálás

Használja a `Workshop/scripts/export_benchmark_markdown.py` szkriptet friss benchmark futtatásához (ugyanaz a logika, mint a `samples/session03/benchmark_oss_models.py`-ban), és generáljon egy GitHub-barát Markdown táblázatot plusz nyers JSON-t.

### Példa

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generált fájlok:
| Fájl | Tartalom |
|------|---------|
| `benchmark_report.md` | Markdown táblázat + értelmezési tippek |
| `benchmark_report.json` | Nyers metrikák tömbje (összehasonlításhoz / trendkövetéshez) |

Állítsa be a `BENCH_STREAM=1` környezetet, hogy az első token késleltetést is tartalmazza, ha támogatott.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.