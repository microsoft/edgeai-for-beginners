# Workshop Jegyzetek

> **Interaktív Jupyter Jegyzetek a Gyakorlati Edge AI Tanuláshoz**
>
> Fokozatos, önállóan végezhető oktatóanyagok, amelyek az alapvető chat-kompletálástól a fejlett többügynökös rendszerekig építkeznek a Microsoft Foundry Local és Kis Nyelvi Modellek használatával.

---

## 📖 Bevezetés

Üdvözlünk az **EdgeAI Kezdőknek Workshop Jegyzetek** gyűjteményében. Ezek az interaktív Jupyter jegyzetek gyakorlati tanulási élményt nyújtanak, ahol valós időben írhatsz, futtathatsz és kísérletezhetsz Edge AI kóddal.

### Miért Jupyter Jegyzetek?

A hagyományos oktatóanyagokkal szemben ezek a jegyzetek az alábbiakat kínálják:

- **Interaktív Tanulás**: Futtasd a kódcellákat és azonnal láthatod az eredményeket
- **Kísérletezés**: Módosítsd a paramétereket és figyeld meg a változásokat valós időben
- **Dokumentáció**: Beágyazott magyarázatok és markdown cellák segítenek megérteni a fogalmakat
- **Reprodukálhatóság**: Teljesen működő példák, amelyeket referenciaként használhatsz és újrahasznosíthatsz
- **Vizualizáció**: Teljesítménymutatók, beágyazások és eredmények megtekintése közvetlenül a jegyzetekben

### Miért Különlegesek Ezek a Jegyzetek?

Minden jegyzetet **gyártásra kész legjobb gyakorlatok** alapján terveztünk:

✅ **Átfogó Hibakezelés** - Zökkenőmentes működés és informatív hibaüzenetek  
✅ **Típusjelzések és Dokumentáció** - Egyértelmű függvényaláírások és docstringek  
✅ **Teljesítményfigyelés** - Tokenhasználat követése és késleltetés mérése  
✅ **Moduláris Tervezés** - Újrahasznosítható minták, amelyeket saját projektjeidhez igazíthatsz  
✅ **Fokozatos Komplexitás** - Rendszeresen építkezik az előző szekciókra

---

## 🎯 Tanulási Célok

### Fejlesztendő Alapkészségek

A jegyzetek feldolgozása során elsajátítod:

1. **Helyi AI Szolgáltatáskezelés**
   - Microsoft Foundry Local szolgáltatások konfigurálása és kezelése
   - Megfelelő modellek kiválasztása és betöltése a hardveredhez
   - Erőforrás-használat figyelése és teljesítmény optimalizálása
   - Szolgáltatáskeresés és állapotellenőrzés kezelése

2. **AI Alkalmazásfejlesztés**
   - OpenAI-kompatibilis chat-kompletálások megvalósítása helyben
   - Streaming interfészek építése a jobb felhasználói élmény érdekében
   - Hatékony promptok tervezése Kis Nyelvi Modellekhez
   - Helyi modellek integrálása alkalmazásokba

3. **Visszakeresésen Alapuló Generálás (RAG)**
   - Szemantikus keresés létrehozása vektorbeágyazásokkal
   - LLM válaszok megalapozása specifikus dokumentumokban
   - RAG minőségének értékelése RAGAS mutatókkal
   - Prototípustól a gyártásig történő skálázás

4. **Teljesítményoptimalizálás**
   - Több modell szisztematikus összehasonlítása
   - Késleltetés, áteresztőképesség és első token idő mérése
   - Kis Nyelvi Modellek és Nagy Nyelvi Modellek összehasonlítása
   - Optimális modellek kiválasztása teljesítmény/minőség kompromisszumok alapján

5. **Többügynökös Orkesztráció**
   - Speciális ügynökök tervezése különböző feladatokra
   - Ügynök memória és kontextuskezelés megvalósítása
   - Több ügynök koordinálása összetett munkafolyamatokban
   - Koordinátor minták építése ügynökök együttműködéséhez

6. **Intelligens Modellirányítás**
   - Szándékfelismerés és mintázatillesztés megvalósítása
   - Lekérdezések automatikus irányítása megfelelő modellekhez
   - Többlépcsős csővezetékek építése (tervezés → végrehajtás → finomítás)
   - Skálázható modell-eszköz architektúrák tervezése

---

## 🎓 Tanulási Eredmények

### Amit Felépítesz

| Jegyzet | Eredmény | Bemutatott Készségek | Nehézség |
|---------|----------|-----------------------|----------|
| **1. Szekció** | Chat alkalmazás streaminggel | Szolgáltatás beállítása, alapvető kompletálások, streaming UX | ⭐ Kezdő |
| **2. Szekció (RAG)** | RAG csővezeték értékeléssel | Beágyazások, szemantikus keresés, minőségi mutatók | ⭐⭐ Középhaladó |
| **2. Szekció (Értékelés)** | RAG minőségértékelő | RAGAS mutatók, szisztematikus értékelés | ⭐⭐ Középhaladó |
| **3. Szekció** | Többmodell benchmark | Teljesítménymérés, modell összehasonlítás | ⭐⭐ Középhaladó |
| **4. Szekció** | SLM vs LLM összehasonlító | Kompromisszum elemzés, optimalizálási stratégiák | ⭐⭐⭐ Haladó |
| **5. Szekció** | Többügynökös orkesztrátor | Ügynök tervezés, memória, koordináció | ⭐⭐⭐ Haladó |
| **6. Szekció (Router)** | Intelligens irányítórendszer | Szándékfelismerés, modell kiválasztás | ⭐⭐⭐ Haladó |
| **6. Szekció (Pipeline)** | Többlépcsős csővezeték | Tervezés/végrehajtás/finomítás munkafolyamatok | ⭐⭐⭐ Haladó |

### Kompetencia Fejlődés

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshop Ütemezés

### 🚀 Fél Napos Workshop (3,5 óra)

**Ideális: Csapatképzések, hackathonok, konferencia workshopok**

| Idő | Időtartam | Szekció | Témák | Tevékenységek |
|-----|-----------|---------|-------|---------------|
| **0:00** | 30 perc | Beállítás és Bevezetés | Környezet beállítása, Foundry Local telepítése | Függőségek telepítése, beállítás ellenőrzése |
| **0:30** | 30 perc | 1. Szekció | Alapvető chat-kompletálások, streaming | Jegyzet futtatása, promptok módosítása |
| **1:00** | 45 perc | 2. Szekció | RAG csővezeték, beágyazások, értékelés | RAG rendszer építése, lekérdezések tesztelése |
| **1:45** | 15 perc | Szünet | ☕ Kávé és kérdések | — |
| **2:00** | 30 perc | 3. Szekció | Többmodell benchmark | 3+ modell összehasonlítása |
| **2:30** | 30 perc | 4. Szekció | SLM vs LLM kompromisszumok | Teljesítmény/minőség elemzése |
| **3:00** | 30 perc | 5-6. Szekció | Többügynökös rendszerek és irányítás | Fejlett minták felfedezése |

**Eredmény**: A résztvevők 6 működő Edge AI alkalmazással és gyártásra kész kódmintákkal távoznak.

---

### 🎓 Egész Napos Workshop (6 óra)

**Ideális: Mélyreható képzések, bootcamp-ek, egyetemi kurzusok**

| Idő | Időtartam | Szekció | Témák | Tevékenységek |
|-----|-----------|---------|-------|---------------|
| **0:00** | 45 perc | Beállítás és Elmélet | Környezet beállítása, Edge AI alapok | Telepítés, ellenőrzés, esettanulmányok megvitatása |
| **0:45** | 45 perc | 1. Szekció | Chat-kompletálások mélyrehatóan | Alapvető és streaming chat megvalósítása |
| **1:30** | 30 perc | Szünet | ☕ Kávé és kapcsolatépítés | — |
| **2:00** | 60 perc | 2. Szekció (Mindkettő) | RAG csővezeték + RAGAS értékelés | Teljes RAG rendszer építése |
| **3:00** | 30 perc | Gyakorlati Labor 1 | Egyedi RAG a saját területeden | Saját dokumentumok alkalmazása |
| **3:30** | 30 perc | Ebéd | 🍽️ | — |
| **4:00** | 45 perc | 3. Szekció | Benchmarking módszertan | Szisztematikus modell összehasonlítás |
| **4:45** | 45 perc | 4. Szekció | Optimalizálási stratégiák | SLM vs LLM elemzés |
| **5:30** | 60 perc | 5-6. Szekció | Fejlett orkesztráció | Többügynökös rendszerek, irányítás |
| **6:30** | 30 perc | Gyakorlati Labor 2 | Egyedi ügynökrendszer építése | Saját orkesztrátor tervezése |

**Eredmény**: Mélyreható Edge AI minták megértése és 2 egyedi projekt.

---

### 📚 Önálló Tanulás (2 hét)

**Ideális: Egyéni tanulók, online kurzusok, önálló tanulás**

#### 1. Hét: Alapok (6 óra)

| Nap | Fókusz | Időtartam | Jegyzetek | Házi feladat |
|-----|--------|-----------|-----------|-------------|
| **Hétfő** | Beállítás és Alapok | 1,5 óra | 1. Szekció | Promptok módosítása, streaming tesztelése |
| **Szerda** | RAG Alapok | 2 óra | 2. Szekció (mindkettő) | Saját dokumentumok hozzáadása |
| **Péntek** | Benchmarking | 1,5 óra | 3. Szekció | További modellek összehasonlítása |
| **Szombat** | Áttekintés és Gyakorlás | 1 óra | 1. hét összes | Feladatok befejezése, hibakeresés |

#### 2. Hét: Haladó (5 óra)

| Nap | Fókusz | Időtartam | Jegyzetek | Házi feladat |
|-----|--------|-----------|-----------|-------------|
| **Hétfő** | Optimalizálás | 1,5 óra | 4. Szekció | Kompromisszumok dokumentálása |
| **Szerda** | Többügynökös Rendszerek | 2 óra | 5. Szekció | Egyedi ügynökök tervezése |
| **Péntek** | Intelligens Irányítás | 1,5 óra | 6. Szekció (mindkettő) | Irányítási logika építése |
| **Szombat** | Záró Projekt | 2 óra | Integráció | Több minta kombinálása |

**Eredmény**: Edge AI minták elsajátítása és portfólió projekt.

---

## 📔 Jegyzet Leírások

### 📘 1. Szekció: Chat Bootstrap
**Fájl**: `session01_chat_bootstrap.ipynb`  
**Időtartam**: 20-30 perc  
**Előfeltételek**: Nincs  
**Nehézség**: ⭐ Kezdő

**Amit Megtanulsz**:
- Foundry Local Python SDK telepítése és konfigurálása
- `FoundryLocalManager` használata automatikus szolgáltatáskereséshez
- Alapvető chat-kompletálások megvalósítása OpenAI-kompatibilis API-val
- Streaming válaszok építése a jobb felhasználói élmény érdekében
- Hibák és szolgáltatáselérhetetlenség kezelése zökkenőmentesen

**Kulcsfogalmak**: Szolgáltatáskezelés, chat-kompletálások, streaming, hibakezelés

**Amit Felépítesz**: Interaktív chat alkalmazás streaming támogatással

---

### 📗 2. Szekció: RAG Csővezeték
**Fájl**: `session02_rag_pipeline.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. Szekció  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Megtanulsz**:
- Visszakeresésen Alapuló Generálás (RAG) minta megvalósítása
- Vektorbeágyazások létrehozása mondat-transzformátorokkal
- Szemantikus keresés építése koszinusz hasonlósággal
- LLM válaszok megalapozása specifikus dokumentumokban
- Opcionális függőségek kezelése importőrök segítségével

**Kulcsfogalmak**: RAG architektúra, beágyazások, szemantikus keresés, vektorhasonlóság

**Amit Felépítesz**: Dokumentum-alapú kérdés-válasz rendszer

---

### 📗 2. Szekció: RAG Értékelés RAGAS-szal
**Fájl**: `session02_rag_eval_ragas.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 2. Szekció RAG Csővezeték  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Megtanulsz**:
- RAG minőség értékelése iparági szabvány mutatókkal
- Kontextus relevancia, válasz relevancia, hitelesség mérése
- RAGAS keretrendszer használata szisztematikus értékeléshez
- RAG minőségi problémák azonosítása és javítása
- Értékelési adathalmazok építése saját területedhez

**Kulcsfogalmak**: RAG értékelés, RAGAS mutatók, minőségmérés, szisztematikus tesztelés

**Amit Felépítesz**: RAG minőségértékelési keretrendszer

---

### 📙 3. Szekció: OSS Modellek Benchmarkja
**Fájl**: `session03_benchmark_oss_models.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. Szekció  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Megtanulsz**:
- Több modell szisztematikus benchmarkolása
- Késleltetés, áteresztőképesség, első token idő mérése
- Modellhibák zökkenőmentes kezelése
- Teljesítmény összehasonlítása modellcsaládok között
- Benchmark eredmények vizualizálása és elemzése

**Kulcsfogalmak**: Teljesítmény benchmarkolás, késleltetés mérése, modell összehasonlítás, statisztikai elemzés

**Amit Felépítesz**: Többmodell benchmark eszköz

---

### 📙 4. Szekció: Modell Összehasonlítás (SLM vs LLM)
**Fájl**: `session04_model_compare.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1., 3. Szekció  
**Nehézség**: ⭐⭐⭐ Haladó

**Amit Megtanulsz**:
- Kis Nyelvi Modellek és Nagy Nyelvi Modellek összehasonlítása
- Teljesítmény és minőség kompromisszumok elemzése
- Edge-alkalmassági mutatók mérése
- Optimális modellek kiválasztása telepítési korlátok alapján
- Modellválasztási döntési kritérium
- Tervezzen skálázható modellek-eszközök architektúrákat

**Kulcsfogalmak**: Pipeline architektúra, többlépcsős feldolgozás, hibakezelés, skálázhatósági minták

**Amit építeni fog**: Többlépcsős intelligens pipeline útvonalvezérléssel

---

## 🚀 Első lépések

### Előfeltételek

**Rendszerkövetelmények**:
- **Operációs rendszer**: Windows 10/11, macOS 11+, vagy Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, ajánlott 16GB+
- **Tárhely**: Legalább 10GB szabad hely a modellek számára
- **Hardver**: CPU AVX2 támogatással; GPU (CUDA, Qualcomm NPU) opcionális

**Szoftverkövetelmények**:
- **Python 3.8+** pip csomagkezelővel
- **Jupyter Notebook** vagy **VS Code** Jupyter kiegészítővel
- **Microsoft Foundry Local** telepítve és konfigurálva
- **Git** (a repository klónozásához)

### Telepítési lépések

#### 1. Foundry Local telepítése

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Telepítés ellenőrzése**:
```bash
foundry --version
```

#### 2. Python környezet beállítása

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

#### 3. Foundry Local indítása

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Jupyter elindítása

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Gyors ellenőrzés

Futtassa ezt egy Python cellában a beállítás ellenőrzéséhez:

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

**Várható kimenet**: Üdvözlő válasz a helyi modellből.

---

## 📝 Workshop legjobb gyakorlatok

### Oktatóknak

**A workshop előtt**:
- ✅ Küldje el a telepítési útmutatót 1 héttel korábban
- ✅ Tesztelje az összes notebookot a célhardveren
- ✅ Készítsen hibaelhárítási útmutatót gyakori problémákhoz
- ✅ Tartson készenlétben tartalék modelleket (phi-3.5-mini, ha a phi-4-mini nem működik)
- ✅ Hozzon létre közös chat csatornát a kérdésekhez

**A workshop alatt**:
- ✅ Kezdje gyors környezetellenőrzéssel (5 perc)
- ✅ Ossza meg azonnal a hibaelhárítási forrásokat
- ✅ Bátorítsa a kísérletezést és módosításokat
- ✅ Stratégiailag használja a szüneteket (minden 2 session után)
- ✅ Legyenek TAs elérhetők személyes segítségnyújtásra

**A workshop után**:
- ✅ Ossza meg a teljes működő notebookokat és megoldásokat
- ✅ Adjon linkeket további forrásokhoz
- ✅ Készítsen visszajelzési kérdőívet a fejlesztéshez
- ✅ Ajánljon konzultációs órákat utólagos kérdésekhez

### Résztvevőknek

**Hozza ki a legtöbbet a tanulásból**:
- ✅ Végezze el a beállítást a workshop kezdete előtt
- ✅ Futtassa az összes kódcellát saját maga (ne csak olvassa)
- ✅ Kísérletezzen paraméterekkel és promptokkal
- ✅ Jegyzeteljen az észrevételekről és buktatókról
- ✅ Tegyen fel kérdéseket, ha elakad (valószínűleg másoknak is ugyanaz a kérdésük)

**Gyakori hibák, amelyeket el kell kerülni**:
- ❌ A cellák végrehajtási sorrendjének kihagyása (futtassa sorban)
- ❌ Hibaüzenetek figyelmen kívül hagyása
- ❌ Túl gyors haladás anélkül, hogy megértené
- ❌ Markdown magyarázatok figyelmen kívül hagyása
- ❌ Saját módosított notebookok el nem mentése

**Hibaelhárítási tippek**:
1. **Szolgáltatás nem fut**: Ellenőrizze `foundry service status`
2. **Importálási hibák**: Győződjön meg róla, hogy a virtuális környezet aktiválva van
3. **Modell nem található**: Futtassa `foundry model ls` a betöltött modellek listázásához
4. **Lassú teljesítmény**: Ellenőrizze a RAM használatot, zárja be a többi alkalmazást
5. **Váratlan eredmények**: Indítsa újra a kernelt, és futtassa az összes cellát felülről

---

## 🔗 További források

### Workshop anyagok

- **[Workshop fő útmutató](../Readme.md)** - Áttekintés, tanulási célok, karrierlehetőségek
- **[Python példák](../../../../Workshop/samples)** - Python szkriptek minden session-hez
- **[Session útmutatók](../../../../Workshop)** - Részletes markdown útmutatók (Session01-06)
- **[Szkriptek](../../../../Workshop/scripts)** - Validációs és tesztelési eszközök
- **[Hibaelhárítás](./TROUBLESHOOTING.md)** - Gyakori problémák és megoldások
- **[Gyors kezdés](./quickstart.md)** - Gyors bevezető útmutató

### Dokumentáció

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Hivatalos Microsoft dokumentáció
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK referencia
- **[Sentence Transformers](https://www.sbert.net/)** - Beágyazási modellek dokumentációja
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG értékelési metrikák

### Közösség

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Kérdések, projektek megosztása
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Valós idejű közösségi támogatás
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technikai kérdések és válaszok

---

## 🎯 Tanulási útvonal ajánlások

### Kezdő szint (Induljon innen)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Modellek benchmarkolása

**Idő**: ~2 óra | **Fókusz**: Alapvető minták

---

### Középhaladó szint

1. Fejezze be a kezdő szintet
2. **Session 02** - RAG értékelés
3. **Session 04** - Modell összehasonlítás

**Idő**: ~4 óra | **Fókusz**: Minőség és optimalizálás

---

### Haladó szint (Teljes workshop)

1. Fejezze be a középhaladó szintet
2. **Session 05** - Multi-Agent Orchestrator
3. **Session 06** - Modell útválasztó
4. **Session 06** - Többlépcsős pipeline

**Idő**: ~6 óra | **Fókusz**: Produkciós minták

---

### Egyedi projekt szint

1. Fejezze be a kezdő szintet (Session 01-03)
2. Válasszon EGY haladó session-t a célja alapján:
   - **RAG alkalmazás építése?** → Session 02 értékelés
   - **Teljesítmény optimalizálása?** → Session 04 összehasonlítás
   - **Komplex munkafolyamatok?** → Session 05 Orchestrator
   - **Skálázható architektúra?** → Session 06 Router + Pipeline

**Idő**: ~3 óra | **Fókusz**: Projekt-specifikus készségek

---

## 📊 Sikerességi mutatók

Kövesse nyomon a haladását ezekkel a mérföldkövekkel:

- [ ] **Beállítás kész** - Foundry Local fut, minden függőség telepítve
- [ ] **Első chat** - Session 01 befejezve, streaming chat működik
- [ ] **RAG elkészült** - Session 02 befejezve, dokumentum QA rendszer működik
- [ ] **Modellek benchmarkolva** - Session 03 befejezve, teljesítményadatok gyűjtve
- [ ] **Kompromisszumok elemzése** - Session 04 befejezve, modellválasztási kritériumok dokumentálva
- [ ] **Ügynökök összehangolva** - Session 05 befejezve, multi-agent rendszer működik
- [ ] **Útválasztás megvalósítva** - Session 06 befejezve, intelligens modellválasztás működik
- [ ] **Egyedi projekt** - Workshop minták alkalmazva saját felhasználási esetére

---

## 🤝 Hozzájárulás

Talált egy problémát vagy van javaslata? Örömmel fogadjuk a hozzájárulásokat!

- **Hibák jelentése**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Javaslatok**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **PR beküldése**: Kövesse a [Hozzájárulási irányelveket](../../AGENTS.md)

---

## 📄 Licenc

Ez a workshop az [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) repository része, és az [MIT Licenc](../../../../LICENSE) alatt van licencelve.

---

**Készen áll produkcióra kész Edge AI alkalmazások építésére?**  
**Kezdje a [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Utolsó frissítés: 2025. október 8. | Workshop verzió: 2.0*

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.