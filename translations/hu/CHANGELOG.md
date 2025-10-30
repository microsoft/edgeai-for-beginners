<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T14:03:09+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hu"
}
-->
# Változásnapló

Az EdgeAI for Beginners minden jelentős változása itt van dokumentálva. Ez a projekt dátum-alapú bejegyzéseket és a Keep a Changelog stílust használja (Hozzáadva, Módosítva, Javítva, Eltávolítva, Dokumentáció, Áthelyezve).

## 2025-10-30

### Hozzáadva - Modul06 AI Ügynökök Átfogó Fejlesztése
- **Microsoft Agent Framework Integráció** (`Module06/01.IntroduceAgent.md`):
  - Teljes szekció a Microsoft Agent Frameworkről, amely gyártásra kész ügynökök fejlesztésére szolgál
  - Részletes integrációs minták a Foundry Local használatával élő telepítéshez
  - Több ügynök együttes működésének példái speciális SLM modellekkel
  - Vállalati telepítési minták erőforrás-kezeléssel és monitorozással
  - Biztonsági és megfelelőségi funkciók élő ügynökrendszerekhez
  - Valós példák (kiskereskedelem, egészségügy, ügyfélszolgálat)

- **SLM Ügynökök Gyártási Telepítési Stratégiái**:
  - **Foundry Local**: Teljes vállalati szintű élő AI futtatási dokumentáció telepítéssel, konfigurációval és gyártási mintákkal
  - **Ollama**: Közösségközpontú telepítés fejlett monitorozással és modellkezeléssel
  - **VLLM**: Nagy teljesítményű következtetési motor fejlett optimalizációs technikákkal és vállalati funkciókkal
  - Gyártási telepítési ellenőrzőlisták és összehasonlító táblázatok mindhárom platformhoz

- **Élőre Optimalizált SLM Keretrendszerek Fejlesztése**:
  - **ONNX Runtime**: Új átfogó szekció a többplatformos SLM ügynökök telepítéséhez
  - Univerzális telepítési minták Windows, Linux, macOS, iOS és Android rendszerekhez
  - Hardvergyorsítási opciók (CPU, GPU, NPU) automatikus felismeréssel
  - Gyártásra kész funkciók és ügynök-specifikus optimalizációk
  - Teljes implementációs példák Microsoft Agent Framework integrációval

- **Hivatkozások és További Olvasmányok**:
  - Átfogó forráskönyvtár több mint 100 hiteles forrással
  - Alapvető kutatási anyagok AI ügynökökről és Kis Nyelvi Modellekről
  - Hivatalos dokumentáció minden jelentős keretrendszerhez és eszközhöz
  - Iparági jelentések, piaci elemzések és technikai összehasonlítások
  - Oktatási források, konferenciák és közösségi fórumok
  - Szabványok, specifikációk és megfelelőségi keretrendszerek

### Módosítva - Modul06 Tartalom Modernizálása
- **Fejlesztett Tanulási Célok**: Hozzáadva a Microsoft Agent Framework elsajátítását és élő telepítési képességeket
- **Gyártási Fókusz**: Konceptuális útmutatás helyett implementációra kész példák
- **Kódpéldák**: Minden példa frissítve modern SDK mintákra és legjobb gyakorlatokra
- **Architektúra Minták**: Hozzáadva hierarchikus ügynök architektúrák és élő-felhő koordináció
- **Teljesítmény Optimalizáció**: Fejlesztve erőforrás-kezelési és automatikus skálázási ajánlásokkal

### Dokumentáció - Modul06 Struktúra Fejlesztése
- **Átfogó Ügynök Keretrendszer Lefedettség**: Alapfogalmaktól a vállalati telepítésig
- **Gyártási Telepítési Stratégiák**: Teljes útmutatók Foundry Local, Ollama és VLLM számára
- **Többplatformos Optimalizáció**: Hozzáadva ONNX Runtime univerzális telepítéshez
- **Forráskönyvtár**: Kiterjedt hivatkozások folyamatos tanuláshoz és implementációhoz

### Hozzáadva - Modul06 Modell Kontextus Protokoll (MCP) Dokumentáció Frissítése
- **MCP Bevezetés Modernizálása** (`Module06/03.IntroduceMCP.md`):
  - Frissítve a legújabb MCP specifikációkkal a modelcontextprotocol.io-ról (2025-06-18 verzió)
  - Hozzáadva hivatalos USB-C analógia szabványos AI alkalmazáskapcsolatokhoz
  - Frissítve az architektúra szekció hivatalos két rétegű dizájnnal (Adatréteg + Szállítási réteg)
  - Fejlesztett alapvető primitívek dokumentáció szerver primitívekkel (Eszközök, Erőforrások, Utasítások) és kliens primitívekkel (Mintavétel, Kiváltás, Naplózás)

- **Átfogó MCP Hivatkozások és Források**:
  - Hozzáadva **MCP kezdőknek** link (https://aka.ms/mcp-for-beginners)
  - Hivatalos MCP dokumentáció és specifikációk (modelcontextprotocol.io)
  - Fejlesztési források, beleértve MCP Inspector és referencia implementációk
  - Technikai szabványok (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Hozzáadva - Modul04 Qualcomm QNN Integráció
- **Új 7. szekció: Qualcomm QNN Optimalizációs Csomag** (`Module04/05.QualcommQNN.md`):
  - Átfogó, több mint 400 soros útmutató Qualcomm egységes AI következtetési keretrendszeréhez
  - Részletes lefedettség a heterogén számításról (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardver-tudatos optimalizáció Snapdragon platformokhoz intelligens munkaterhelés elosztással
  - Fejlett kvantálási technikák (INT8, INT16, vegyes precizitás) mobil telepítéshez
  - Energiatakarékos következtetési optimalizáció akkumulátoros eszközökhöz és valós idejű alkalmazásokhoz
  - Teljes telepítési útmutató QNN SDK beállítással és környezeti konfigurációval
  - Gyakorlati példák: PyTorch QNN-re konvertálása, több háttér optimalizáció, kontextus bináris generálás
  - Fejlett használati minták: egyedi háttér konfiguráció, dinamikus kvantálás, teljesítmény profilozás
  - Átfogó hibaelhárítási szekció és közösségi források

- **Fejlesztett Modul04 Struktúra**:
  - README.md frissítve 7 progresszív szekcióval (korábban 6)
  - Qualcomm QNN hozzáadva a teljesítmény összehasonlító táblázathoz (5-15x sebességnövekedés, 50-80% memória csökkentés)
  - Átfogó tanulási eredmények mobil AI telepítéshez és energiaoptimalizációhoz

### Módosítva - Modul04 Dokumentáció Frissítések
- **Microsoft Olive dokumentáció fejlesztése** (`Module04/03.MicrosoftOlive.md`):
  - Hozzáadva átfogó "Olive Recipes Repository" szekció, amely több mint 100 előre elkészített optimalizációs receptet tartalmaz
  - Részletes lefedettség a támogatott modellcsaládokról (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Gyakorlati használati példák recept testreszabására és közösségi hozzájárulásokra
  - Fejlesztve teljesítmény összehasonlításokkal és integrációs útmutatóval

- **Szekció átrendezése a Modul04-ben**:
  - Apple MLX áthelyezve az 5. szekcióba (korábban 6. szekció)
  - Workflow Synthesis áthelyezve a 6. szekcióba (korábban 7. szekció)
  - Qualcomm QNN pozícionálva a 7. szekcióba (specializált mobil/élő fókusz)
  - Minden fájl hivatkozás és navigációs link frissítve ennek megfelelően

### Javítva - Workshop Minta Validáció
- **chat_bootstrap.py validáció és javítás**:
  - Javítva sérült import utasítás (`util.util.workshop_utils` → `util.workshop_utils`)
  - Hiányzó `__init__.py` létrehozva a util csomagban a megfelelő Python modul feloldáshoz
  - Szükséges függőségek telepítve (openai, foundry-local-sdk) conda környezetben
  - Minta futtatás sikeresen validálva alapértelmezett és egyedi utasításokkal
  - Integráció megerősítve a Foundry Local szolgáltatással és modell betöltéssel (phi-4-mini CUDA optimalizációval)

### Dokumentáció - Átfogó Útmutató Frissítések
- **Module04 README.md teljes átszervezése**:
  - Qualcomm QNN hozzáadva mint jelentős optimalizációs keretrendszer az OpenVINO, Olive, MLX mellett
  - Fejezet tanulási eredmények frissítve mobil AI telepítés és energiaoptimalizáció hozzáadásával
  - Fejlesztett teljesítmény összehasonlító táblázat QNN metrikákkal és mobil/élő használati esetekkel
  - Logikus előrehaladás fenntartva vállalati megoldásoktól platform-specifikus optimalizációkig

- **Kereszthivatkozások és navigáció**:
  - Minden belső link és fájl hivatkozás frissítve az új szekció számozás szerint
  - Fejlesztett workflow synthesis leírás mobil, asztali és felhő környezetekhez
  - Átfogó forráslinkek hozzáadva a Qualcomm fejlesztői ökoszisztémához

## 2025-10-08

### Hozzáadva - Workshop Átfogó Frissítés
- **Workshop README.md teljes újraírása**:
  - Átfogó bevezetés hozzáadva, amely magyarázza az Edge AI értékajánlatát (adatvédelem, teljesítmény, költség)
  - 6 alapvető tanulási cél létrehozva részletes kompetenciákkal
  - Tanulási eredmények táblázata létrehozva szállítmányokkal és kompetencia mátrixszal
  - Karrierre kész készségek szekció hozzáadva iparági relevanciával
  - Gyors kezdési útmutató létrehozva előfeltételekkel és 3 lépéses beállítással
  - Forrástáblák létrehozva Python mintákhoz (8 fájl futási idővel)
  - Jupyter notebookok táblázata (8 notebook nehézségi besorolással)
  - Dokumentációs táblázat létrehozva (7 kulcsfontosságú dokumentum "Használja, amikor" útmutatással)
  - Tanulási útvonal ajánlások különböző készségszintekhez

- **Workshop validációs és tesztelési infrastruktúra**:
  - `scripts/validate_samples.py` létrehozva - Átfogó validációs eszköz szintaxis, importok és legjobb gyakorlatok ellenőrzésére
  - `scripts/test_samples.py` létrehozva - Gyors teszt futtató minden Python mintához
  - Validációs dokumentáció hozzáadva a `scripts/README.md`-hez

- **Átfogó dokumentáció**:
  - `SAMPLES_UPDATE_SUMMARY.md` létrehozva - Több mint 400 soros részletes útmutató az összes fejlesztésről
  - `UPDATE_COMPLETE.md` létrehozva - Frissítés befejezésének vezetői összefoglalója
  - `QUICK_REFERENCE.md` létrehozva - Gyors referencia kártya a Workshophoz

### Módosítva - Workshop Python Minták Modernizálása
- **Mind a 8 Python minta frissítve legjobb gyakorlatokkal**:
  - Fejlesztett hiba kezelés try-except blokkokkal minden I/O művelet körül
  - Típusjelzések és átfogó docstringek hozzáadva
  - Egységes [INFO]/[ERROR]/[RESULT] naplózási minta implementálva
  - Opcionális importok védve telepítési utasításokkal
  - Felhasználói visszajelzés javítva minden mintában

- **session01/chat_bootstrap.py**:
  - Ügyfél inicializáció fejlesztve átfogó hibaüzenetekkel
  - Streaming hiba kezelés javítva szakasz validációval
  - Jobb kivételkezelés hozzáadva szolgáltatás elérhetetlenség esetén

- **session02/rag_pipeline.py**:
  - Import őrök hozzáadva sentence-transformershez telepítési utasításokkal
  - Hiba kezelés fejlesztve beágyazási és generálási műveletekhez
  - Kimeneti formázás javítva strukturált eredményekkel

- **session02/rag_eval_ragas.py**:
  - Opcionális importok védve (ragas, datasets) felhasználóbarát hibaüzenetekkel
  - Hiba kezelés hozzáadva értékelési metrikákhoz
  - Kimeneti formázás fejlesztve értékelési eredményekhez

- **session03/benchmark_oss_models.py**:
  - Kegyes degradáció implementálva (folytatja modellhibák esetén)
  - Részletes haladási jelentés és modell-specifikus hiba kezelés hozzáadva
  - Statisztikai számítás fejlesztve átfogó hiba helyreállítással

- **session04/model_compare.py**:
  - Típusjelzések hozzáadva (Tuple visszatérési típusok)
  - Kimeneti formázás fejlesztve strukturált JSON eredményekkel
  - Modell-specifikus hiba kezelés implementálva helyreállítással

- **session05/agents_orchestrator.py**:
  - Agent.act() fejlesztve átfogó docstringekkel
  - Pipeline hiba kezelés hozzáadva szakaszok szerinti naplózással
  - Memóriakezelés és állapotkövetés javítva

- **session06/models_router.py**:
  - Funkció dokumentáció fejlesztve minden útválasztó komponenshez
  - Részletes naplózás hozzáadva a route() funkcióban
  - Teszt kimenet javítva strukturált eredményekkel

- **session06/models_pipeline.py**:
  - Hiba kezelés hozzáadva a chat() segédfunkcióhoz
  - Pipeline() fejlesztve szakasz naplózással és haladási jelentéssel
  - Main() fejlesztve átfogó hiba helyreállítással

### Dokumentáció - Workshop Dokumentáció Fejlesztése
- Fő README.md frissítve Workshop szekcióval, amely kiemeli a gyakorlati tanulási utat
- STUDY_GUIDE.md fejlesztve átfogó Workshop szekcióval, beleértve:
  - Tanulási célok és tanulmányi fókuszterületek
  - Önértékelési kérdések
  - Gyakorlati feladatok időbecsléssel
  - Időbeosztás koncentrált és részmunkaidős tanulmányokhoz
  - Workshop hozzáadva haladáskövetési sablonhoz
- Időbeosztási útmutató frissítve 20 óráról 30 órára (beleértve a Workshopot)
- Workshop minta leírások és tanulási eredmények hozzáadva README-hez

### Javítva
- Workshop minták közötti hiba kezelés minták következetlenségei megoldva
- Opcionális függőség import hibák javítva megfelelő őrökkel
- Hiányzó típusjelzések javítva kritikus funkciókban
- Elégtelen felhasználói visszajelzés javítva hibahelyzetekben
- Validációs problémák megoldva átfogó tesztelési infrastruktúrával

---

## 2025-09-23

### Módosítva
  - Futtatható minták a `Module08/samples/01`–`06` alatt Windows cmd utasításokkal
    - `01` REST gyors chat (`chat_quickstart.py`)
    - `02` SDK gyorsindítás OpenAI/Foundry Local és Azure OpenAI támogatással (`sdk_quickstart.py`)
    - `03` CLI listázás és tesztelés (`list_and_bench.cmd`)
    - `04` Chainlit bemutató (`app.py`)
    - `05` Többügynökös koordináció (`python -m samples.05.agents.coordinator`)
    - `06` Modellek-eszközként router (`router.py`)
- Azure OpenAI támogatás a 2. szekció SDK mintájában környezeti változó konfigurációval
- `.vscode/settings.json` a `Module08/.venv`-re mutat, hogy javítsa a Python elemzési felbontást
- `.env` a `PYTHONPATH` utalással a VS Code/Pylance felismerés érdekében

### Változások
- Alapértelmezett modell frissítve `phi-4-mini`-re a Module 08 dokumentációban és mintákban; eltávolítva a fennmaradó `phi-3.5` említések a Module 08-ban
- Router (`Module08/samples/06/router.py`) fejlesztések:
  - Végpontok felfedezése a `foundry service status` regex elemzésével
  - `/v1/models` állapotellenőrzés indításkor
  - Környezeti változóval konfigurálható modellregisztráció (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Követelmények frissítve: `Module08/requirements.txt` most tartalmazza az `openai`-t (a `requests`, `chainlit` mellett)
- Chainlit minta útmutató pontosítva és hibaelhárítás hozzáadva; import feloldás munkaterületi beállításokkal

### Javítások
- Import problémák megoldva:
  - A router már nem függ egy nem létező `utils` modultól; a funkciók beépítve
  - A koordinátor relatív importot használ (`from .specialists import ...`) és modul útvonalon keresztül van meghívva
  - VS Code/Pylance konfiguráció a `chainlit` és csomagimportok feloldására
- Kisebb elírás javítva a `STUDY_GUIDE.md`-ben, és hozzáadva a Module 08 lefedettség

### Törölve
- Törölve a nem használt `Module08/infra/obs.py` és az üres `infra/` könyvtár; az opcionális megfigyelési minták megmaradtak a dokumentációban

### Áthelyezve
- A Module 08 bemutatók konszolidálva a `Module08/samples` alá szekciószámozott mappákkal
  - Chainlit alkalmazás áthelyezve a `samples/04`-be
  - Ügynökök áthelyezve a `samples/05`-be, és hozzáadva `__init__.py` fájlok a csomagfeloldáshoz

### Dokumentáció
- A Module 08 szekció dokumentációja és minden minta README-je gazdagítva Microsoft Learn és megbízható gyártói hivatkozásokkal
- `Module08/README.md` frissítve minták áttekintésével, router konfigurációval és validációs tippekkel
- `Module07/README.md` Windows Foundry Local szekciója validálva a Learn dokumentációval
- `STUDY_GUIDE.md` frissítve:
  - Module 08 hozzáadva az áttekintéshez, ütemtervekhez, haladási nyomkövetőhöz
  - Átfogó Hivatkozások szekció hozzáadva (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Történeti (összefoglaló)
- Tanfolyam architektúra és modulok létrehozva (Modules 01–07)
- Iteratív tartalom modernizálás, formázási szabványosítás és esettanulmányok hozzáadása
- Optimalizációs keretrendszerek lefedettségének bővítése (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Kiadatlan / Hátralévő (javaslatok)
- Opcionális mintánkénti gyors tesztek a Foundry Local elérhetőségének validálására
- Fordítások felülvizsgálata a modellhivatkozások összehangolására (pl. `phi-4-mini`)
- Minimális pyright konfiguráció hozzáadása, ha a csapatok munkaterület-szintű szigorúságot preferálnak

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.