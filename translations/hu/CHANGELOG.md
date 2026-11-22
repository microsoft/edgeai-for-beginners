# Változásnapló

Az EdgeAI for Beginners összes jelentős változását itt dokumentáljuk. Ez a projekt dátumalapú bejegyzéseket és a Keep a Changelog stílust használja (Hozzáadva, Módosítva, Javítva, Eltávolítva, Dokumentáció, Áthelyezve).

## 2025-10-30

### Hozzáadva - Module06 AI Ügynökök Átfogó Fejlesztése
- **Microsoft Agent Framework Integráció** (`Module06/01.IntroduceAgent.md`):
  - Teljes szakasz a Microsoft Agent Frameworkről termelésre kész ügynökfejlesztéshez
  - Részletes integrációs minták a Foundry Local-al élszéli telepítéshez
  - Többügynökös összehangolási példák speciális SLM modellekkel
  - Vállalati telepítési minták erőforrás-menedzsmenttel és monitorozással
  - Biztonsági és megfelelőségi funkciók élszéli ügynökrendszerekhez
  - Valódi megvalósítási példák (kiskereskedelem, egészségügy, ügyfélszolgálat)

- **Termelési SLM Ügynök Telepítési Stratégiák**:
  - **Foundry Local**: Teljes vállalati szintű élszéli AI futtatókörnyezet dokumentáció telepítéssel, konfigurálással és termelési mintákkal
  - **Ollama**: Fejlesztett közösségközpontú telepítés átfogó monitorozással és modell menedzsmenttel
  - **VLLM**: Nagyteljesítményű következtető motor fejlett optimalizációs technikákkal és vállalati funkciókkal
  - Termelési telepítési ellenőrzőlisták és összehasonlító táblázatok mindhárom platformra

- **Élszéli-optimalizált SLM Keretrendszerek Fejlesztése**:
  - **ONNX Runtime**: Új átfogó szakasz többplatformos SLM ügynök telepítéshez
  - Univerzális telepítési minták Windows, Linux, macOS, iOS és Android rendszerekhez
  - Hardveres gyorsítási lehetőségek (CPU, GPU, NPU) automatikus felismeréssel
  - Termelésre kész funkciók és ügynökspecifikus optimalizálások
  - Teljes megvalósítási példák Microsoft Agent Framework integrációval

- **Hivatkozások és További Olvasmányok**:
  - Átfogó forráskönyvtár 100+ hiteles forrással
  - Alapkutatási cikkek AI ügynökökről és Kis Nyelvi Modellekről
  - Hivatalos dokumentáció minden fontosabb keretrendszerről és eszközről
  - Iparági jelentések, piaci elemzések és technikai teljesítménymutatók
  - Oktatási anyagok, konferenciák és közösségi fórumok
  - Szabványok, specifikációk és megfelelőségi keretrendszerek

### Módosítva - Module06 Tartalom Modernizálása
- **Fejlesztett Tanulási Célok**: Hozzáadva Microsoft Agent Framework elsajátítása és élszéli telepítési képességek
- **Termelési fókusz**: Elmozdulás a koncepcionálistól megvalósítás-kész útmutató felé termelési példákkal
- **Kódpéldák**: Minden példa frissítve modern SDK minták és legjobb gyakorlatok szerint
- **Architektúra minták**: Hozzáadva hierarchikus ügynök architektúrák és élszéli-felhő koordináció
- **Teljesítményoptimalizálás**: Fejlesztve erőforrás menedzsmenttel és automatikus skálázási ajánlásokkal

### Dokumentáció - Module06 Szerkezet Fejlesztése
- **Átfogó Ügynök Keretrendszer Lefedettség**: Az alapfogalmaktól a vállalati telepítésig
- **Termelési Telepítési Stratégiák**: Teljes útmutatók Foundry Local, Ollama és VLLM számára
- **Többplatformos Optimalizálás**: Hozzáadva ONNX Runtime az univerzális telepítéshez
- **Forráskönyvtár**: Kiterjedt hivatkozások a további tanuláshoz és megvalósításhoz

### Hozzáadva - Module06 Model Context Protocol (MCP) Dokumentáció Frissítés
- **MCP Bemutató Modernizálása** (`Module06/03.IntroduceMCP.md`):
  - Frissítve a legújabb MCP specifikációkkal a modelcontextprotocol.io oldalról (2025-06-18 verzió)
  - Hozzáadva hivatalos USB-C analógia a szabványosított AI alkalmazáskapcsolatokhoz
  - Frissített architektúra szakasz hivatalos kétszintű dizájnnal (Adatréteg + Szállítóréteg)
  - Fejlesztett alapvető primitívek dokumentáció szerver primitívekkel (Eszközök, Erőforrások, Kérések) és kliens primitívekkel (Mintavétel, Kiváltás, Naplózás)

- **Átfogó MCP Hivatkozások és Források**:
  - Hozzáadva **MCP kezdőknek** link (https://aka.ms/mcp-for-beginners)
  - Hivatalos MCP dokumentáció és specifikációk (modelcontextprotocol.io)
  - Fejlesztési források beleértve MCP Inspector és referenciamegvalósításokat
  - Technikai szabványok (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Hozzáadva - Module04 Qualcomm QNN Integráció
- **Új 7. szakasz: Qualcomm QNN Optimalizációs Csomag** (`Module04/05.QualcommQNN.md`):
  - Átfogó, 400+ soros útmutató Qualcomm egységes AI következtető keretrendszeréről
  - Részletes fedezet a heterogén számításról (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardver-tudatos optimalizáció Snapdragon platformokra intelligens munkaterhelés elosztással
  - Fejlett kvantálási technikák (INT8, INT16, vegyes pontosság) mobil telepítéshez
  - Energihatékony következtetés optimalizálás akkumulátoros eszközökre és valós idejű alkalmazásokra
  - Teljes telepítési útmutató QNN SDK beállításával és környezetkonfigurációval
  - Gyakorlati példák: PyTorch-ból QNN konverzió, több hátsó vég optimalizáció, kontextus bináris generálás
  - Fejlett használati minták: egyedi hátsó vég konfiguráció, dinamikus kvantálás, teljesítmény profilozás
  - Átfogó hibakeresési szakasz és közösségi források

- **Module04 szerkezet fejlesztése**:
  - README.md frissítve 7 progresszív szakaszra (korábban 6)
  - Hozzáadva Qualcomm QNN a teljesítmény összehasonlító táblázathoz (5-15x sebességnövelés, 50-80% memória csökkenés)
  - Átfogó tanulási eredmények mobil AI telepítésről és energiaoptimalizálásról

### Módosítva - Module04 Dokumentáció Frissítések
- **Microsoft Olive dokumentáció fejlesztése** (`Module04/03.MicrosoftOlive.md`):
  - Hozzáadva átfogó "Olive Receptek Gyűjteménye" szakasz 100+ előre elkészített optimalizációs recepten keresztül
  - Részletes áttekintés a támogatott modell családokról (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Gyakorlati használati példák recepttestreszabáshoz és közösségi hozzájárulásokhoz
  - Fejlesztve teljesítmény mérésekkel és integrációs útmutatással

- **Szakasz átrendezések a Module04-ben**:
  - Apple MLX áthelyezve az 5. szakaszba (korábban 6.)
  - Munkafolyamat szintézis áthelyezve a 6. szakaszba (korábban 7.)
  - Qualcomm QNN elhelyezve a 7. szakaszként (specializált mobil/élszéli fókusz)
  - Minden fájlreferenciát és navigációs linket ennek megfelelően frissítve

### Javítva - Workshop Minták Érvényesítése
- **chat_bootstrap.py érvényesítés és javítás**:
  - Hibás import utasítás javítva (`util.util.workshop_utils` → `util.workshop_utils`)
  - Hiányzó `__init__.py` létrehozása a util csomagban a megfelelő Python modul feloldáshoz
  - Szükséges függőségek telepítve (openai, foundry-local-sdk) conda környezetben
  - Minták futtatása sikeresen érvényesítve alapértelmezett és egyedi promptokkal
  - Integráció megerősítve a Foundry Local szolgáltatással és modell betöltéssel (phi-4-mini CUDA optimalizációval)

### Dokumentáció - Átfogó Útmutató Frissítések
- **Module04 README.md teljes átalakítása**:
  - Hozzáadva Qualcomm QNN mint jelentős optimalizációs keretrendszer OpenVINO, Olive, MLX mellett
  - Frissített fejezet tanulási eredmények mobil AI telepítés és energiaoptimalizálás témában
  - Fejlesztett teljesítmény összehasonlító táblázat QNN mutatókkal és mobil/élszéli használati esetekkel
  - Megőrizve a logikus előrehaladás a vállalati megoldásoktól a platform-specifikus optimalizációkig

- **Kereszt-hivatkozások és navigáció**:
  - Minden belső link és fájlreferencia frissítve az új szakaszszámozás szerint
  - Munkafolyamat szintézis kifejtése bővítve mobil, asztali és felhő környezetekre
  - Átfogó erőforrás linkek Qualcomm fejlesztői ökoszisztémához hozzáadva

## 2025-10-08

### Hozzáadva - Workshop Átfogó Frissítés
- **Workshop README.md teljes átírása**:
  - Átfogó bevezető hozzáadva az Edge AI értékajánlatáról (adatvédelem, teljesítmény, költség)
  - 6 fő tanulási cél létrehozva részletes kompetenciákkal
  - Tanulási eredmények táblázat a szállítmányokkal és kompetenciamátrixszal
  - Karrierkészség szekció az ipari relevancia érdekében
  - Gyors kezdési útmutató előfeltételekkel és 3 lépéses beállítással
  - Forrás táblázatok Python mintákhoz (8 fájl futási időkkel)
  - Jupyter notebookok táblázata (8 notebook nehézségi szintekkel)
  - Dokumentációs táblázat (7 kulcs dokumentum "Használat mikor" útmutatóval)
  - Tanulási út ajánlások különböző szintű készségekhez

- **Workshop validáció és tesztelési infrastruktúra**:
  - `scripts/validate_samples.py` létrehozva – Átfogó validációs eszköz szintaxisra, importokra és legjobb gyakorlatokra
  - `scripts/test_samples.py` létrehozva – Füstteszt futtató minden Python mintához
  - Validációs dokumentáció hozzáadva a `scripts/README.md`-hez

- **Átfogó dokumentáció**:
  - `SAMPLES_UPDATE_SUMMARY.md` létrehozva – 400+ soros részletes útmutató minden fejlesztéshez
  - `UPDATE_COMPLETE.md` létrehozva – Vezetői összefoglaló a frissítés befejezéséről
  - `QUICK_REFERENCE.md` létrehozva – Gyorsreferencia kártya a Workshophoz

### Módosítva - Workshop Python Minta Modernizáció
- **Mind a 8 Python minta frissítve legjobb gyakorlatokkal**:
  - Hibakezelés fejlesztve try-except blokkokkal minden I/O művelet körül
  - Típusmegjegyzések és átfogó docstringek hozzáadva
  - Egységes [INFO]/[ERROR]/[RESULT] naplózási minta megvalósítva
  - Opcionális importok védelme telepítési tippekkel
  - Felhasználói visszajelzés javítva minden mintában

- **session01/chat_bootstrap.py**:
  - Vevő inicializáció fejlesztve átfogó hibaüzenetekkel
  - Streaming hibakezelés javítva szelet validációval
  - Jobb kivételkezelés hozzáadva szolgáltatás elérhetetlenség esetére

- **session02/rag_pipeline.py**:
  - Importvédők hozzáadva sentence-transformers-hez telepítési tippekkel
  - Hibakezelés fejlesztve beágyazási és generálási műveleteknél
  - Kimenet formázás javítva strukturált eredményekkel

- **session02/rag_eval_ragas.py**:
  - Opcionális importok védve (ragas, datasets) felhasználóbarát hibaüzenetekkel
  - Hibakezelés hozzáadva értékelési mutatókhoz
  - Kimenet formázás fejlesztve az értékelési eredményekhez

- **session03/benchmark_oss_models.py**:
  - Kecses hibakezelés megvalósítva (modell hibák esetén folytatódik)
  - Részletes előrehaladás-jelentés és modellenkénti hibakezelés hozzáadva
  - Statisztika számítás fejlesztve átfogó hibajavítással

- **session04/model_compare.py**:
  - Típusmegjegyzések hozzáadva (Tuple visszatérési típusok)
  - Kimenet formázás javítva strukturált JSON eredményekkel
  - Modellenkénti hibakezelés megvalósítva javítással

- **session05/agents_orchestrator.py**:
  - Agent.act() fejlesztve átfogó docstringekkel
  - Pipeline hibakezelés hozzáadva szakaszonkénti naplózással
  - Memóriakezelés és állapotkövetés javítva

- **session06/models_router.py**:
  - Függvény dokumentáció fejlesztve minden útválasztó komponenshez
  - Részletes naplózás hozzáadva a route() függvényben
  - Teszt kimenet javítva strukturált eredményekkel

- **session06/models_pipeline.py**:
  - Hibakezelés hozzáadva a chat() segédfüggvényhez
  - Pipeline() fejlesztve szakaszos naplózással és előrehaladás-jelentéssel
  - Main() fejlesztve átfogó hibakezeléssel

### Dokumentáció - Workshop Dokumentáció Fejlesztése
- Fő README.md frissítve Workshop szekcióval, amely kiemeli a gyakorlati tanulási útvonalat
- STUDY_GUIDE.md fejlesztve átfogó Workshop szakasz hozzáadásával, amely tartalmazza:
  - Tanulási célokat és tanulmányi fókuszterületeket
  - Önértékelő kérdéseket
  - Gyakorlati feladatokat időbecsléssel
  - Időallokáció koncentrált és részmunkaidős tanulásra
  - Workshop hozzáadva előrehaladás követés sablonhoz
- Időallokációs útmutató frissítve 20 óráról 30 órára (beleértve a Workshopot)
- Workshop minták leírásai és tanulási eredmények hozzáadva a README-hez

### Javítva
- Egyenetlen hibakezelési minták megszüntetése a Workshop mintákban
- Opcionális függőség import hibák javítása megfelelő védőhálókkal
- Hiányzó típusmegjegyzések javítása kritikus függvényekben
- Nem elegendő felhasználói visszajelzés kezelése hibás esetekben
- Érvényesítési problémák javítása átfogó tesztelési infrastruktúrával

---

## 2025-09-23

### Módosítva - Jelentős Module 08 Modernizáció
- **Teljes összehangolás a Microsoft Foundry-Local adattár mintáival**
  - Minden kódpélda frissítve a modern `FoundryLocalManager` és OpenAI SDK integráció használatára
  - Megszűntetve az elavult manuális `requests` hívások, helyettük SDK használat
  - Megfelelőség az implementációs mintákkal a hivatalos Microsoft dokumentáció és minták szerint

- **05.AIPoweredAgents.md modernizáció**:
  - Többügynökös összehangolás frissítve modern SDK mintákkal
  - Fejlesztett koordinátor implementáció haladó funkciókkal (visszacsatolási hurkok, teljesítmény monitorozás)
  - Átfogó hibakezelés és szolgáltatás egészségellenőrzés hozzáadva
  - Helyi mintákra való megfelelő hivatkozás (`samples/05/multi_agent_orchestration.ipynb`)
  - Függvényhívási példák frissítve modern `tools` paraméter használatára az elavult `functions` helyett
  - Termelésre kész minták monitorozással és statisztika követéssel

- **06.ModelsAsTools.md teljes átírása**:
  - Alap eszköztár helyett intelligens modell útválasztó megvalósítás
  - Kulcsszó-alapú modellválasztás különféle feladat típusokhoz (általános, érvelés, kód, kreatív)
  - Környezetalapú konfiguráció integrálva rugalmas modell hozzárendeléssel
  - Átfogó szolgáltatás egészség monitorozás és hibakezelés hozzáadva
  - Termelési telepítési minták hozzáadva kérések monitorozásával és teljesítmény követéssel
  - Összhangban a helyi megvalósítással `samples/06/router.py` és `samples/06/model_router.ipynb`

- **Dokumentációs szerkezet fejlesztések**:
  - Áttekintő szakaszok hozzáadva, kiemelve modernizálás és SDK összehangolás
  - Kidolgozott emoji-k és jobb formázás a jobb olvashatóság érdekében
  - Helyi minta fájlokra való megfelelő hivatkozások a teljes dokumentációban
  - Termelésre kész megvalósítási útmutatás és legjobb gyakorlatok beillesztése

### Hozzáadva
- Átfogó áttekintő szakaszok a Module 08 fájlokban, kiemelve a modern SDK integrációt
- Architektúra kiemelések haladó funkciókról (többügynökös rendszerek, intelligens útválasztás)
- Közvetlen hivatkozások a helyi minta megvalósításokra gyakorlati tapasztalatokhoz
- Termelési telepítési útmutatás monitorozással és hibakezelési mintákkal
- Interaktív Jupyter notebook példák haladó funkciókkal és teljesítménytesztekkel

### Javítva
- Dokumentáció és tényleges minta megvalósítások közötti eltérések összehangolása
- Elavult SDK használati minták javítása Module 08 egészén
- Hiányzó hivatkozások a teljes helyi minta könyvtárra
- Inkonzisztens implementációs megközelítések eltávolítása különböző szakaszok között

---

## 2025-09-18

### Hozzáadva
- Module 08: Microsoft Foundry Local – Teljes Fejlesztői Eszköztár
  - Hat szekció: beállítás, Azure AI Foundry integráció, nyílt forráskódú modellek, élvonalbeli demók, ügynökök, és modellek mint eszközök
  - Futtatható minták `Module08/samples/01`–`06` könyvtárban Windows parancssori utasításokkal
    - `01` REST gyors chat (`chat_quickstart.py`)

    - `02` SDK gyors kezdés OpenAI/Foundry Local és Azure OpenAI támogatással (`sdk_quickstart.py`)
    - `03` CLI lista és teljesítményteszt (`list_and_bench.cmd`)
    - `04` Chainlit bemutató (`app.py`)
    - `05` Többügynökös koordináció (`python -m samples.05.agents.coordinator`)
    - `06` Modellek eszközként router (`router.py`)
- Azure OpenAI támogatás a Session 2 SDK mintában környezeti változó konfigurációval
- `.vscode/settings.json` a `Module08/.venv` irányításával és a Python elemzés feloldásának javításával
- `.env` `PYTHONPATH` jelzéssel a VS Code/Pylance értesüléshez

### Változtatva
- Az alapértelmezett modell frissítve `phi-4-mini`-re a Module 08 dokumentációban és mintákban; a maradék `phi-3.5` hivatkozások eltávolítva a Module 08-ban
- Router (`Module08/samples/06/router.py`) fejlesztések:
  - Végpont felfedezés `foundry service status` segítségével regex elemzéssel
  - `/v1/models` állapotellenőrzés induláskor
  - Környezeti konfigurálható modellregiszter (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Frissített követelmények: `Module08/requirements.txt` immár tartalmazza az `openai` csomagot (a `requests` és `chainlit` mellett)
- Chainlit minta útmutató tisztázva és hibakeresés hozzáadva; importok feloldása munkaterület beállításai által

### Javítva
- Import problémák megoldva:
  - A router már nem támaszkodik nem létező `utils` modulra; a funkciók be vannak ágyazva
  - A koordinátor relatív importot használ (`from .specialists import ...`) és modul útvonalon keresztül indítható
  - VS Code/Pylance konfigurációk a `chainlit` és csomag importok feloldásához
- Hibás írásjel javítása az `STUDY_GUIDE.md`-ben és Module 08 lefedettség hozzáadva

### Eltávolítva
- Nem használt `Module08/infra/obs.py` törölve és az üres `infra/` könyvtár eltávolítva; megfigyelési minták opcionálisan megőrizve a dokumentációban

### Áthelyezve
- Module 08 demók összevonva a `Module08/samples` könyvtárba szekciószámozott mappákkal
  - Chainlit app áthelyezve a `samples/04`-be
  - Ügynökök áthelyezve a `samples/05`-be és `__init__.py` fájlok hozzáadva a csomagfeloldáshoz

### Dokumentáció
- Module 08 szekció dokumentáció és összes minta README-je bővítve Microsoft Learn és megbízható szállítói hivatkozásokkal
- `Module08/README.md` frissítve a Minták áttekintésével, router konfigurációval és validálási tippekkel
- `Module07/README.md` Windows Foundry Local szekció validálva a Learn dokumentumok alapján
- `STUDY_GUIDE.md` frissítve:
  - Hozzáadva a Module 08 áttekintéshez, ütemezésekhez, előrehaladási nyomonkövetőhöz
  - Hozzáadva átfogó Referencia szekció (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Történeti áttekintés (összefoglaló)
- A tanfolyam architektúrája és moduljai kialakítva (01–07 modulok)
- Iteratív tartalom korszerűsítés, formázási szabványosítás és esettanulmányok hozzáadása
- Kiterjesztett optimalizációs keretrendszer lefedettség (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nem kiadott / Hátralék (javaslatok)
- Opcionális mintánkénti gyors tesztek a Foundry Local elérhetőség validálásához
- Fordítások felülvizsgálata a modell hivatkozások (pl. `phi-4-mini`) összehangolásához, ahol megfelelő
- Minimális pyright konfiguráció hozzáadása, ha a csapatok munkaterület szintű szigorúságot preferálnak

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->