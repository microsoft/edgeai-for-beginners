# Műhely Jegyzetfüzetek

> **Interaktív Jupyter Jegyzetfüzetek Gyakorlati Edge MI Tanuláshoz**
>
> Fokozatos, önállóan haladható oktatóanyagok, amelyek az alapvető chat kitöltésektől az előrehaladott többügynökös rendszerekig terjednek a Microsoft Foundry Local és Kis Nyelvi Modellek használatával.

---

## 📖 Bevezetés

Üdvözlünk a **EdgeAI Kezdőknek Műhely Jegyzetfüzetek** gyűjteményben. Ezek az interaktív Jupyter jegyzetfüzetek kézzelfogható tanulási élményt nyújtanak, ahol valós időben írhatsz, futtathatsz és kísérletezhetsz Edge MI kóddal.

### Miért Jupyter Jegyzetfüzetek?

A hagyományos oktatóanyagoktól eltérően ezek a jegyzetfüzetek a következőket kínálják:

- **Interaktív Tanulás**: Kód cellák futtatása és azonnali eredmények megtekintése
- **Kísérletezés**: Paraméterek módosítása és változások valós idejű megfigyelése
- **Dokumentáció**: Beépített magyarázatok és markdown cellák, amelyek végigvezetnek a fogalmakon
- **Reprodukálhatóság**: Teljes működő példák, amelyeket hivatkozhatsz és újra felhasználhatsz
- **Vizualizáció**: Teljesítménymutatók, beágyazások és eredmények megtekintése inline

### Mi Teszi Különlegessé Ezeket a Jegyzetfüzeteket?

Minden jegyzetfüzetet a **termelésre kész legjobb gyakorlatok** alapján terveztek:

✅ **Átfogó Hibakezelés** - Fokozatos leépülés és tájékoztató hibaüzenetek  
✅ **Típus Segédletek & Dokumentáció** - Egyértelmű függvényaláírások és docstringek  
✅ **Teljesítmény Monitorozás** - Token használat és késleltetés mérése  
✅ **Moduláris Dizájn** - Újrafelhasználható minták, amelyeket alkalmazhatsz projektjeidben  
✅ **Fokozatos Komplexitás** - Rendszeresen épít az előző szekciókra

---

## 🎯 Tanulási Célok

### Fő Készségek, Amiket Fejleszteni Fogsz

Ezeket a jegyzetfüzeteket végigcsinálva elsajátítod:

1. **Helyi MI Szolgáltatás Menedzsment**
   - Microsoft Foundry Local szolgáltatások konfigurálása és kezelése
   - Az adott hardverhez megfelelő modellek kiválasztása és betöltése
   - Erőforrások használatának monitorozása és teljesítményoptimalizálás
   - Szolgáltatás felfedezés és állapotellenőrzés kezelése

2. **MI Alkalmazásfejlesztés**
   - OpenAI-kompatibilis chat kitöltések helyi megvalósítása
   - Streaming interfészek építése jobb felhasználói élményért
   - Hatékony promptok tervezése Kis Nyelvi Modellekhez
   - Helyi modellek integrálása alkalmazásokba

3. **Retrieval Augmented Generation (RAG)**
   - Szemantikus keresés létrehozása vektor beágyazásokkal
   - LLM válaszok alapozása domain-specifikus dokumentumokra
   - RAG minőség értékelése RAGAS metrikákkal
   - Prototípustól a termelésig skálázás

4. **Teljesítmény Optimalizálás**
   - Több modell összehasonlító mérésének megvalósítása rendszerezetten
   - Késleltetés, áteresztőképesség és első token idő mérése
   - Kis Nyelvi Modellek vs Nagy Nyelvi Modellek összehasonlítása
   - Optimális modellek kiválasztása teljesítmény/minőség kompromisszum alapján

5. **Többügynökös Orkesztráció**
   - Különleges ügynökök tervezése különféle feladatokra
   - Ügynök memória és kontextuskezelés megvalósítása
   - Több ügynök koordinálása komplex munkafolyamatokban
   - Koordinátor minták építése ügynök együttműködéshez

6. **Intelligens Modellirányítás**
   - Szándék felismerés és mintázat illesztés megvalósítása
   - Lekérdezések automatikus irányítása megfelelő modellekhez
   - Többlépéses pipeline-ok építése (tervezés → végrehajtás → finomítás)
   - Skálázható modell mint eszköz architektúrák tervezése

---

## 🎓 Tanulási Eredmények

### Amit Meg Fogsz Építeni

| Jegyzetfüzet | Kézbesíthető | Bemutatott készségek | Nehézség |
|----------|-------------|---------------------|------------|
| **1. Foglalkozás** | Streaming chat alkalmazás | Szolgáltatás beállítás, alap chat kitöltések, streaming UX | ⭐ Kezdő |
| **2. Foglalkozás (RAG)** | RAG pipeline értékeléssel | Beágyazások, szemantikus keresés, minőségi mutatók | ⭐⭐ Középhaladó |
| **2. Foglalkozás (Értékelés)** | RAG minőség értékelő | RAGAS metrikák, rendszerszerű értékelés | ⭐⭐ Középhaladó |
| **3. Foglalkozás** | Több-modelles benchmark | Teljesítmény mérés, modell összehasonlítás | ⭐⭐ Középhaladó |
| **4. Foglalkozás** | SLM vs LLM összehasonlító | Kompromisszum elemzés, optimalizálási stratégiák | ⭐⭐⭐ Haladó |
| **5. Foglalkozás** | Több-ügynökös orkesztrátor | Ügynök tervezés, memória, koordináció | ⭐⭐⭐ Haladó |
| **6. Foglalkozás (Router)** | Intelligens irányító rendszer | Szándék felismerés, modell kiválasztás | ⭐⭐⭐ Haladó |
| **6. Foglalkozás (Pipeline)** | Többlépéses pipeline | Tervezés/végrehajtás/finomítás munkafolyamatok | ⭐⭐⭐ Haladó |

### Kompetencia Fejlődés

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Műhely Ütemterv

### 🚀 Fél Napos Műhely (3,5 óra)

**Tökéletes: Csapatképzésekhez, hackathonokhoz, konferencia műhelyekhez**

| Időpont | Időtartam | Foglalkozás | Témakörök | Tevékenységek |
|------|----------|---------|--------|------------|
| **0:00** | 30 perc | Beállítás & Bevezetés | Környezet beállítása, Foundry Local telepítése | Függőségek telepítése, beállítás ellenőrzése |
| **0:30** | 30 perc | 1. Foglalkozás | Alap chat kitöltések, streaming | Jegyzetfüzet futtatása, promptok módosítása |
| **1:00** | 45 perc | 2. Foglalkozás | RAG pipeline, beágyazások, értékelés | RAG rendszer építése, lekérdezések tesztelése |
| **1:45** | 15 perc | Szünet | ☕ Kávé & kérdések | — |
| **2:00** | 30 perc | 3. Foglalkozás | Több-modeles benchmarking | 3+ modell összehasonlítása |
| **2:30** | 30 perc | 4. Foglalkozás | SLM vs LLM kompromisszumok | Teljesítmény/minőség elemzés |
| **3:00** | 30 perc | 5-6. Foglalkozás | Több-ügynökös rendszerek & irányítás | Haladó minták felfedezése |

**Eredmény**: A résztvevők 6 működő Edge MI alkalmazással és termelésre kész kódmintákkal távoznak.

---

### 🎓 Egész Napos Műhely (6 óra)

**Tökéletes: Mélyreható képzésekhez, bootcamp-ekhez, egyetemi kurzusokhoz**

| Időpont | Időtartam | Foglalkozás | Témakörök | Tevékenységek |
|------|----------|---------|--------|------------|
| **0:00** | 45 perc | Beállítás & Elmélet | Környezet beállítása, Edge MI alapok | Telepítés, ellenőrzés, használati esetek megvitatása |
| **0:45** | 45 perc | 1. Foglalkozás | Chat kitöltések mélyrehatóan | Alap és streaming chat implementálása |
| **1:30** | 30 perc | Szünet | ☕ Kávé & hálózatépítés | — |
| **2:00** | 60 perc | 2. Foglalkozás (Mindkettő) | RAG pipeline + RAGAS értékelés | Teljes RAG rendszer építése |
| **3:00** | 30 perc | Gyakorlati Lab 1 | Egyedi RAG a saját domainodra | Saját dokumentumokra alkalmazás |
| **3:30** | 30 perc | Ebéd | 🍽️ | — |
| **4:00** | 45 perc | 3. Foglalkozás | Benchmarking módszertan | Rendszerszerű modell összehasonlítás |
| **4:45** | 45 perc | 4. Foglalkozás | Optimalizálási stratégiák | SLM vs LLM elemzés |
| **5:30** | 60 perc | 5-6. Foglalkozás | Haladó orkesztráció | Több-ügynökös rendszerek, irányítás |
| **6:30** | 30 perc | Gyakorlati Lab 2 | Egyedi ügynök rendszer építése | Saját orkesztrátor tervezése |

**Eredmény**: Mély Edge MI minták megértése és 2 egyedi projekt.

---

### 📚 Önálló Tanulás (2 hét)

**Tökéletes: Egyéni tanulóknak, online kurzusokhoz, önképzéshez**

#### 1. hét: Alapok (6 óra)

| Nap | Fókusz | Időtartam | Jegyzetfüzetek | Házi Feladat |
|-----|-------|----------|-----------|----------|
| **Hétfő** | Beállítás & Alapok | 1,5 óra | 1. Foglalkozás | Promptok módosítása, streaming teszt |
| **Szerda** | RAG Alapok | 2 óra | 2. Foglalkozás (mindkettő) | Saját dokumentumok hozzáadása |
| **Péntek** | Benchmarking | 1,5 óra | 3. Foglalkozás | További modellek összehasonlítása |
| **Szombat** | Áttekintés & Gyakorlás | 1 óra | Az egész 1. hét | Gyakorlatok befejezése, hibakeresés |

#### 2. hét: Haladó (5 óra)

| Nap | Fókusz | Időtartam | Jegyzetfüzetek | Házi Feladat |
|-----|-------|----------|-----------|----------|
| **Hétfő** | Optimalizálás | 1,5 óra | 4. Foglalkozás | Kompromisszumok dokumentálása |
| **Szerda** | Több-ügynökös rendszerek | 2 óra | 5. Foglalkozás | Egyedi ügynökök tervezése |
| **Péntek** | Intelligens Iránymutatás | 1,5 óra | 6. Foglalkozás (mindkettő) | Iránymutatási logika megépítése |
| **Szombat** | Záró Projekt | 2 óra | Integráció | Több minta kombinálása |

**Eredmény**: Edge MI minták elsajátítása és portfólió projekt.

---

## 📔 Jegyzetfüzet Leírások

### 📘 1. Foglalkozás: Chat Indító
**Fájl**: `session01_chat_bootstrap.ipynb`  
**Időtartam**: 20-30 perc  
**Előfeltételek**: Nincs  
**Nehézség**: ⭐ Kezdő

**Amit Meg Fogsz Tanulni**:
- Foundry Local Python SDK telepítése és konfigurálása
- `FoundryLocalManager` használata automatikus szolgáltatás felfedezéshez
- Alap chat kitöltések megvalósítása OpenAI-kompatibilis API-val
- Streaming válaszok építése jobb felhasználói élményért
- Hibák és szolgáltatás elérhetetlenség kezelésének finomhangolása

**Kulcsfogalmak**: Szolgáltatás kezelés, chat kitöltések, streaming, hibakezelés

**Amit Meg Fogsz Építeni**: Interaktív chat alkalmazás streaming támogatással

---

### 📗 2. Foglalkozás: RAG Pipeline
**Fájl**: `session02_rag_pipeline.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. Foglalkozás  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Meg Fogsz Tanulni**:
- Retrieval Augmented Generation (RAG) minta megvalósítása
- Vektor beágyazások létrehozása sentence-transformers segítségével
- Szemantikus keresés építése koszinusz hasonlósággal
- LLM válaszok alapozása domain-specifikus dokumentumokra
- Opcionális függőségek kezelése import őrökön keresztül

**Kulcsfogalmak**: RAG architektúra, beágyazások, szemantikus keresés, vektorszerűség

**Amit Meg Fogsz Építeni**: Dokumentum-alapú kérdés-válasz rendszert

---

### 📗 2. Foglalkozás: RAG Értékelés RAGAS-szal
**Fájl**: `session02_rag_eval_ragas.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 2. Foglalkozás RAG Pipeline  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Meg Fogsz Tanulni**:
- Iparági szabvány szerinti mérésekkel RAG minőség értékelése
- Kontextus relevancia, válasz relevancia, hűség mérés
- RAGAS keretrendszer használata rendszerszintű értékeléshez
- RAG minőség problémák azonosítása és javítása
- Értékelési adatkészletek építése a saját domainodhoz

**Kulcsfogalmak**: RAG értékelés, RAGAS metrikák, minőség mérés, rendszerszintű tesztelés

**Amit Meg Fogsz Építeni**: RAG minőség értékelő keretrendszert

---

### 📙 3. Foglalkozás: OSS Modellek Benchmarkolása
**Fájl**: `session03_benchmark_oss_models.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. Foglalkozás  
**Nehézség**: ⭐⭐ Középhaladó

**Amit Meg Fogsz Tanulni**:
- Több modell rendszerszerű összehasonlító mérésének megvalósítása
- Késleltetés, áteresztőképesség, első token idő mérése
- Finom hibaleépülési viselkedés implementálása modelleknél
- Teljesítmény összehasonlító elemzés model családok között
- Benchmark eredmények vizualizálása és elemzése

**Kulcsfogalmak**: Teljesítmény mérés, késleltetés mérése, modell összehasonlítás, statisztikai elemzés

**Amit Meg Fogsz Építeni**: Több-modelles benchmark csomagot

---

### 📙 4. Foglalkozás: Modell Összehasonlítás (SLM vs LLM)
**Fájl**: `session04_model_compare.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. és 3. Foglalkozás  
**Nehézség**: ⭐⭐⭐ Haladó

**Amit Meg Fogsz Tanulni**:
- Kis Nyelvi Modellek és Nagy Nyelvi Modellek összehasonlítása
- Teljesítmény és minőség kompromisszum elemzése
- Edge-kompatibilitási mutatók mérése
- Optimális modellek kiválasztása üzembe helyezési korlátok alapján
- Modell kiválasztási döntési kritériumok dokumentálása

**Kulcsfogalmak**: Modell választás, kompromisszum elemzés, optimalizálási stratégiák, üzembe helyezési tervezés

**Amit Meg Fogsz Építeni**: SLM vs LLM összehasonlító keretrendszer

---

### 📕 5. Foglalkozás: Több-Ügynökös Orkesztrátor
**Fájl**: `session05_agents_orchestrator.ipynb`  
**Időtartam**: 45-60 perc  
**Előfeltételek**: 1-2. Foglalkozás  
**Nehézség**: ⭐⭐⭐ Haladó

**Amit Meg Fogsz Tanulni**:
- Különböző feladatokra specializált ügynökök tervezése
- Ügynök memória és kontextus kezelés megvalósítása
- Koordinátor minták építése az ügynök együttműködéshez
- Ügynök kommunikáció és átadások kezelése
- Több-ügynökös rendszer teljesítményének monitorozása

**Kulcsfogalmak**: Ügynök architektúra, koordinátor minták, memória kezelés, ügynök orkesztráció

**Amit Meg Fogsz Építeni**: Több-ügynökös rendszer koordinátorral és szakértőkkel

---

### 📕 6. Foglalkozás: Modell Irányító
**Fájl**: `session06_models_router.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. és 3. Foglalkozás  
**Nehézség**: ⭐⭐⭐ Haladó

**Amit Meg Fogsz Tanulni**:
- Szándék felismerés és mintázat illesztés megvalósítása
- Kulcsszavas alapú modellirányítás építése
- Lekérdezések automatikus irányítása megfelelő modellekhez
- Több-modelles regisztrációk konfigurálása
- Irányítási döntések és teljesítmény monitorozása

**Kulcsfogalmak**: Szándék felismerés, modellirányítás, mintázat illesztés, intelligens kiválasztás

**Amit Meg Fogsz Építeni**: Intelligens modellirányító rendszert

---

### 📕 6. Foglalkozás: Többlépéses Pipeline
**Fájl**: `session06_models_pipeline.ipynb`  
**Időtartam**: 30-45 perc  
**Előfeltételek**: 1. és 6. Router Foglalkozás  
**Nehézség**: ⭐⭐⭐ Haladó

**Amit Meg Fogsz Tanulni**:
- Többlépéses MI pipeline-ok építése (tervezés → végrehajtás → finomítás)
- Router integrálása intelligens modell kiválasztáshoz
- Pipeline hibakezelés és helyreállítás megvalósítása
- Pipeline teljesítményének és szakaszainak monitorozása
- Skálázható modell-mint eszköz architektúrák tervezése


**Kulcsfogalmak**: Csővezeték-architektúra, többlépcsős feldolgozás, hibajavítás, skálázhatósági minták

**Amit építesz**: Többlépéses intelligens csővezeték irányítással

---

## 🚀 Első lépések

### Előfeltételek

**Rendszerkövetelmények**:
- **Operációs rendszer**: Windows 10/11, macOS 11+, vagy Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, javasolt 16GB+
- **Tárhely**: 10GB+ szabad hely modelleknek
- **Hardver**: AVX2 támogatású CPU; GPU (CUDA, Qualcomm NPU) opcionális

**Szoftverkövetelmények**:
- **Python 3.8+** pip-pel
- **Jupyter Notebook** vagy **VS Code** Jupyter kiterjesztéssel
- Telepített és konfigurált **Microsoft Foundry Local**
- **Git** (a tároló klónozásához)

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
# Navigáljon a Workshop könyvtárba
cd Workshop

# Hozzon létre virtuális környezetet
python -m venv .venv

# Aktiválja a virtuális környezetet
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Telepítse a függőségeket
pip install -r requirements.txt
```

#### 3. Foundry Local indítása

```bash
# Modell betöltése (szükség esetén automatikus letöltés)
foundry model run phi-4-mini

# Ellenőrizze, hogy a szolgáltatás fut-e
foundry service status
```

#### 4. Jupyter indítása

```bash
# Indítsa el a Jupyter Notebookot
jupyter notebook notebooks/

# Vagy használja a VS Code-ot a Jupyter kiterjesztéssel
code notebooks/
```

### Gyors ellenőrzés

Futtasd ezt egy Python cellában a beállítás ellenőrzéséhez:

```python
from foundry_local import FoundryLocalManager
import openai

# Inicializálja a kezelőt (automatikusan felfedezi a szolgáltatást)
manager = FoundryLocalManager("phi-4-mini")

# Konfigurálja az OpenAI klienset
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Tesztelje a csevegés kiegészítést
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Várt eredmény**: Üdvözlő válasz a helyi modelltől.

---

## 📝 Workshop legjobb gyakorlatok

### Oktatóknak

**Workshop előtt**:
- ✅ Küldj telepítési utasításokat 1 héttel előre
- ✅ Teszteld az összes jegyzetfüzetet céleszközön
- ✅ Készíts hibakeresési útmutatót gyakori problémákra
- ✅ Legyenek tartalék modellek kéznél (phi-3.5-mini, ha phi-4-mini nem működik)
- ✅ Állíts be közös chat csatornát kérdésekhez

**A workshop alatt**:
- ✅ Kezdj gyors környezeti ellenőrzéssel (5 perc)
- ✅ Oszd meg azonnal a hibakeresési forrásokat
- ✅ Bátorítsd a kísérletezést és módosításokat
- ✅ Használj szüneteket stratégiával (minden 2 szekció után)
- ✅ Legyenek TÁ-k elérhetők egyéni segítségre

**A workshop után**:
- ✅ Oszd meg a teljes működő jegyzetfüzeteket és megoldásokat
- ✅ Adj linkeket további forrásokhoz
- ✅ Készíts visszajelzési felmérést a fejlődéshez
- ✅ Ajánlj konzultációs időpontokat további kérdésekhez

### Tanulóknak

**Maximalizáld a tanulásod**:
- ✅ Készítsd el a beállítást a workshop kezdete előtt
- ✅ Futtasd le minden kódcellát magad (ne csak olvasd)
- ✅ Kísérletezz paraméterekkel és promptokkal
- ✅ Jegyzetelj az észrevételekről és buktatókról
- ✅ Tegyél fel kérdéseket, ha elakadsz (másoknak is lehet ugyanez a kérdésük)

**Gyakori hibák, amelyeket kerülj**:
- ❌ Nem sorrendben futtatni a cellákat
- ❌ Nem figyelni figyelmesen a hibaüzeneteket
- ❌ Türelmetlenül haladni megértés nélkül
- ❌ Figyelmen kívül hagyni a markdown magyarázatokat
- ❌ Nem menteni a módosított jegyzetfüzeteket

**Hibakeresési tippek**:
1. **Szolgáltatás nem fut**: Ellenőrizd a `foundry service status` parancsot
2. **Import hibák**: Győződj meg, hogy a virtuális környezet aktív
3. **Modell nem található**: Futtasd a `foundry model ls` -t a betöltött modellek listázásához
4. **Lassú teljesítmény**: Ellenőrizd a RAM használatot, zárd be a többi alkalmazást
5. **Váratlan eredmények**: Indítsd újra a kernelt és futtasd le az összes cellát felülről

---

## 🔗 További források

### Workshop anyagok

- **[Workshop fő útmutató](../Readme.md)** - Áttekintés, tanulási célok, karrier eredmények
- **[Python minták](../../../../Workshop/samples)** - Minden szekcióhoz kapcsolódó Python szkriptek
- **[Szekció útmutatók](../../../../Workshop)** - Részletes markdown útmutatók (Session01-06)
- **[Szkriptek](../../../../Workshop/scripts)** - Ellenőrző és tesztelő eszközök
- **[Hibajavítás](./TROUBLESHOOTING.md)** - Gyakori problémák és megoldások
- **[Gyors kezdés](./quickstart.md)** - Gyorsított kezdő útmutató

### Dokumentáció

- **[Foundry Local dokumentáció](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Hivatalos Microsoft dokumentáció
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK referencia
- **[Sentence Transformers](https://www.sbert.net/)** - Beágyazó modellek dokumentációja
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG értékelési metrikák

### Közösség

- **[GitHub Beszélgetések](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Kérdések, projektmegosztás
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Valós idejű közösségi támogatás
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technikai kérdések-válaszok

---

## 🎯 Tanulási út javaslatok

### Kezdő tanfolyam (innen indulj)

1. **Szekció 01** - Chat Bootstrap
2. **Szekció 02** - RAG Pipeline
3. **Szekció 03** - Modell mérési alapok

**Időtartam**: ~2 óra | **Fókusz**: Alapvető minták

---

### Haladó közép szint

1. Befejezni a kezdő tanfolyamot
2. **Szekció 02** - RAG értékelés
3. **Szekció 04** - Modell összehasonlítás

**Időtartam**: ~4 óra | **Fókusz**: Minőség és optimalizáció

---

### Haladó tanfolyam (teljes workshop)

1. Befejezni a haladó közép szintet
2. **Szekció 05** - Többügynökös kezelő
3. **Szekció 06** - Modell irányító
4. **Szekció 06** - Többlépéses csővezeték

**Időtartam**: ~6 óra | **Fókusz**: Termelési minták

---

### Egyedi projekt sáv

1. Befejezni a kezdő tanfolyamot (Szekciók 01-03)
2. Válassz EGY fejlett szekciót a célod alapján:
   - **RAG alkalmazást építesz?** → Szekció 02 Értékelés
   - **Teljesítmény optimalizálás?** → Szekció 04 Összehasonlítás
   - **Összetett munkafolyamatok?** → Szekció 05 Kezelő
   - **Skálázható architektúrát?** → Szekció 06 Irányító + Csővezeték

**Időtartam**: ~3 óra | **Fókusz**: Projekt-specifikus készségek

---

## 📊 Sikermutatók

Kövesd nyomon előrehaladásodat ezekkel a mérföldkövekkel:

- [ ] **Beállítás kész** - Foundry Local fut, minden függőség telepítve
- [ ] **Első chat** - Szekció 01 teljesítve, folyamatos chat működik
- [ ] **RAG elkészült** - Szekció 02 kész, dokumentum QA rendszer működik
- [ ] **Modellek mérve** - Szekció 03 kész, teljesítményadatok gyűjtve
- [ ] **Kompromisszumok elemzve** - Szekció 04 kész, modellválasztási kritériumok dokumentálva
- [ ] **Ügynökök kezelve** - Szekció 05 kész, többügynökös rendszer működik
- [ ] **Irányítás megvalósítva** - Szekció 06 kész, intelligens modellválasztás működik
- [ ] **Egyedi projekt** - Workshop minták alkalmazva saját esethez

---

## 🤝 Közreműködés

Találtál hibát vagy van javaslatod? Szívesen fogadjuk a hozzájárulásokat!

- **Hibák jelentése**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Javítási javaslatok**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **PR beküldése**: Kövesd a [Hozzájárulási irányelveket](../../AGENTS.md)

---

## 📄 Licenc

Ez a workshop a [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) tároló része, és az [MIT License](../../../../LICENSE) licenc alatt áll.

---

**Készen állsz gyártásra kész Edge AI alkalmazások építésére?**  
**Kezdd a [Szekció 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb)-pal →**

---

*Utolsó frissítés: 2025. október 8. | Workshop verzió: 2.0*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->