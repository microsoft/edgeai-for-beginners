# AI Eszközkészlet a Visual Studio Code-hoz - Edge AI fejlesztési útmutató

## Bevezetés

Üdvözöljük az AI Eszközkészlet a Visual Studio Code-hoz való használatának átfogó útmutatójában az Edge AI fejlesztés területén. Ahogy a mesterséges intelligencia a központosított felhőalapú számítástechnikáról az elosztott edge eszközökre helyeződik át, a fejlesztőknek erőteljes, integrált eszközökre van szükségük, amelyek képesek megbirkózni az edge telepítés egyedi kihívásaival – az erőforrás-korlátozásoktól az offline működési követelményekig.

Az AI Eszközkészlet a Visual Studio Code-hoz áthidalja ezt a szakadékot azáltal, hogy egy teljes fejlesztési környezetet biztosít, amely kifejezetten az edge eszközökön hatékonyan futó AI alkalmazások építésére, tesztelésére és optimalizálására lett tervezve. Akár IoT érzékelőkhöz, mobil eszközökhöz, beágyazott rendszerekhez vagy edge szerverekhez fejleszt, ez az eszközkészlet egyszerűsíti az egész fejlesztési munkafolyamatát a megszokott VS Code környezetben.

Ez az útmutató végigvezeti Önt az AI Eszközkészlet Edge AI projektjeiben való kihasználásához szükséges alapvető fogalmakon, eszközökön és bevált gyakorlatokon, az első modell kiválasztásától egészen a termelési telepítésig.

## Áttekintés

Az AI Eszközkészlet a Visual Studio Code-hoz egy erőteljes bővítmény, amely egyszerűsíti az ügynökfejlesztést és az AI alkalmazások létrehozását. Az eszközkészlet átfogó képességeket nyújt AI modellek feltérképezésére, értékelésére és üzembe helyezésére számos szolgáltatótól – beleértve az Anthropict, OpenAI-t, GitHub-ot, Google-t –, miközben támogatja a helyi modell futtatást ONNX és Ollama segítségével.

Ami megkülönbözteti az AI Eszközkészletet, az a teljes AI fejlesztési életciklusra kiterjedő átfogó megközelítés. A hagyományos AI fejlesztőeszközökkel ellentétben, amelyek egy-egy aspektusra összpontosítanak, az AI Eszközkészlet egy integrált környezetet biztosít, amely lefedi a modell felfedezését, kísérletezést, ügynökfejlesztést, értékelést és üzembe helyezést – mindezt a megszokott VS Code környezetben.

A platform kifejezetten gyors prototípus-készítésre és termelési telepítésre lett tervezve, olyan funkciókkal, mint például a prompt generálás, gyorsindítók, zökkenőmentes MCP (Model Context Protocol) eszköz integrációk és átfogó értékelési képességek. Az Edge AI fejlesztéshez ez azt jelenti, hogy hatékonyan fejleszthet, tesztelhet és optimalizálhat AI alkalmazásokat edge telepítési forgatókönyvekre, miközben a teljes fejlesztési munkafolyamatot megtartja a VS Code-ban.

## Tanulási célok

Az útmutató végére képes lesz:

### Alapkészségek
- **Telepíteni és konfigurálni** az AI Eszközkészletet a Visual Studio Code-hoz az Edge AI fejlesztési munkafolyamatokhoz
- **Navigálni és használni** az AI Eszközkészlet felületét, beleértve a Modell Katalógust, Játékteret és Ügynöképítőt
- **Kiválasztani és értékelni** az edge telepítésre alkalmas AI modelleket teljesítmény és erőforrás-korlátozások alapján
- **Konvertálni és optimalizálni** modelleket ONNX formátummal és kvantálási technikákkal edge eszközök számára

### Edge AI Fejlesztési Készségek
- **Tervezni és megvalósítani** Edge AI alkalmazásokat az integrált fejlesztési környezet használatával
- **Modelltesztelést végezni** edge-szerű feltételek között helyi inferencia és erőforrás-figyelő használatával
- **Létrehozni és testreszabni** AI ügynököket, amelyek optimalizáltak edge telepítési forgatókönyvekhez
- **Értékelni a modell teljesítményét** az edge számítástechnika szempontjából releváns metrikák alapján (késleltetés, memória használat, pontosság)

### Optimalizálás és telepítés
- **Alkalmazni kvantálási és nyesési** technikákat a modellméret csökkentésére miközben elfogadható teljesítményt tart fenn
- **Optimalizálni modelleket** specifikus edge hardver platformokhoz, többek között CPU-, GPU- és NPU gyorsításhoz
- **Megvalósítani bevált gyakorlatokat** edge AI fejlesztéshez, beleértve az erőforrás-kezelést és tartalék stratégiákat
- **Előkészíteni modelleket és alkalmazásokat** termelési telepítésre edge eszközökön

### Fejlett Edge AI Fogalmak
- **Integrálódni edge AI keretrendszerekkel**, beleértve az ONNX Runtime-ot, Windows ML-t és TensorFlow Lite-ot
- **Megvalósítani többmodell-architektúrákat** és federált tanulási forgatókönyveket edge környezetekhez
- **Hibaelhárítani gyakori edge AI problémákat**, beleértve a memória korlátokat, az inferencia sebességet és a hardver kompatibilitást
- **Tervezni figyelő és naplózó stratégiákat** edge AI alkalmazások termelésben történő futtatásához

### Gyakorlati Alkalmazás
- **Építeni end-to-end Edge AI megoldásokat** a modell kiválasztásától kezdve a telepítésig
- **Bemutatni jártasságot** az edge specifikus fejlesztési munkafolyamatokban és optimalizálási technikákban
- **Alkalmazni az elsajátított fogalmakat** valós edge AI használati eseteken, beleértve IoT-t, mobil és beágyazott alkalmazásokat
- **Értékelni és összehasonlítani** különböző edge AI telepítési stratégiákat és azok kompromisszumait

## Főbb jellemzők az Edge AI Fejlesztéshez

### 1. Modell Katalógus és Felfedezés
- **Többszolgáltatói támogatás**: Böngésszen és férjen hozzá AI modellekhez az Anthropic, OpenAI, GitHub, Google és más szolgáltatóktól
- **Helyi modell integráció**: Egyszerűsített felfedezés ONNX és Ollama modellekhez edge telepítésre
- **GitHub modellek**: Közvetlen integráció a GitHub modell-tárolókkal a zökkenőmentes hozzáférésért
- **Model összehasonlítás**: Oldal-az-oldal melletti összehasonlítás, hogy megtalálja az optimális egyensúlyt az edge eszköz-korlátokhoz

### 2. Interaktív Játékterem
- **Interaktív tesztelési környezet**: Gyors kísérletezés modell-képességekkel szabályozott környezetben
- **Multimodális támogatás**: Tesztelés képekkel, szöveggel és más, edge forgatókönyvekben tipikus bemenetekkel
- **Valós idejű kísérletezés**: Azonnali visszajelzés a modell válaszairól és teljesítményéről
- **Paraméter optimalizálás**: Finomhangolja a modell paramétereit az edge telepítési követelményekhez

### 3. Prompt (Ügynök) Építő
- **Természetes nyelvű generálás**: Indító promptok generálása természetes nyelvi leírások alapján
- **Iteratív finomítás**: Javítsa a promptokat a modell válaszai és teljesítménye alapján
- **Feladat bontás**: Összetett feladatok lebontása prompt láncolással és strukturált kimenetekkel
- **Változó támogatás**: Használjon változókat promptokban dinamikus ügynök viselkedéshez
- **Termelési kód generálás**: Termelésre kész kód generálása gyors alkalmazásfejlesztéshez

### 4. Tömeges futtatás és értékelés
- **Többmodell tesztelés**: Több prompt egyidejű végrehajtása kiválasztott modelleken
- **Hatékony tesztelés nagyban**: Különböző bemenetek és konfigurációk hatékony tesztelése
- **Egyéni tesztesetek**: Ügynökök futtatása tesztesetekkel a funkciók érvényesítésére
- **Teljesítmény összehasonlítás**: Eredmények összevetése különböző modelleken és konfigurációkban

### 5. Modell értékelés adathalmazokkal
- **Standard metrikák**: AI modellek tesztelése beépített értékelőkkel (F1 pontszám, relevancia, hasonlóság, koherencia)
- **Egyedi értékelők**: Saját értékelési metrikák létrehozása specifikus használati esetekhez
- **Adathalmaz integráció**: Modellek tesztelése átfogó adathalmazokkal
- **Teljesítménymérés**: A modell teljesítményének számszerűsítése edge telepítési döntésekhez

### 6. Finomhangolási képességek
- **Modell testreszabás**: Modellek testreszabása specifikus használati esetek és területek számára
- **Speciális adaptáció**: Modellek specializált területekhez és követelményekhez igazítása
- **Edge optimalizáció**: Modellek finomhangolása kifejezetten edge telepítési korlátokhoz
- **Területspecifikus tréning**: Modellek létrehozása külön specifikus edge használati esetekhez

### 7. MCP eszköz integráció
- **Külső eszköz kapcsolódás**: Ügynökök csatlakoztatása külső eszközökhöz Model Context Protocol szervereken keresztül
- **Valós világi műveletek**: Ügynökök adatbázis lekérdezésre, API hozzáférésre vagy egyéni logika végrehajtására képesek
- **Meglévő MCP szerverek**: Használjon eszközöket parancssori (stdio) vagy HTTP (server-sent event) protokollokon
- **Egyedi MCP fejlesztés**: Új MCP szerverek építése és előkészítése teszteléssel az Ügynöképítőben

### 8. Ügynök fejlesztés és tesztelés
- **Funkcióhívás támogatás**: Ügynökök dinamikus külső függvényhívásra képesek
- **Valós idejű integrációs tesztelés**: Integrációk tesztelése valós idejű futtatással és eszközhasználattal
- **Ügynök verziókezelés**: Verziókövetés ügynökök számára értékelési eredmények összehasonlításával
- **Hibakeresés és nyomkövetés**: Helyi nyomkövetési és hibakeresési lehetőségek ügynökfejlesztéshez

## Edge AI fejlesztési munkafolyamat

### 1. fázis: Modell felfedezés és kiválasztás
1. **Modell katalógus böngészése**: Használja a modell katalógust az edge telepítésre alkalmas modellek megtalálásához
2. **Teljesítmény összehasonlítása**: Értékelje a modelleket méret, pontosság és inferencia sebesség alapján
3. **Helyi tesztelés**: Helyi tesztelés Ollama vagy ONNX modelleken az edge telepítés előtt
4. **Erőforrás igények felmérése**: Határozza meg a memória- és számítási szükségleteket a cél edge eszközökhöz

### 2. fázis: Modell optimalizálás
1. **Konvertálás ONNX-re**: Az kiválasztott modellek átalakítása ONNX formátumba az edge kompatibilitás érdekében
2. **Kvantálás alkalmazása**: A modellméret csökkentése INT8 vagy INT4 kvantálással
3. **Hardver optimalizálás**: Optimalizálás a cél edge hardverhez (ARM, x86, speciális gyorsítók)
4. **Teljesítmény érvényesítés**: Ellenőrizze, hogy az optimalizált modellek megtartják az elfogadható pontosságot

### 3. fázis: Alkalmazás fejlesztés
1. **Ügynök tervezés**: Ügynöképítő használata edge-optimalizált AI ügynökök készítéséhez
2. **Prompt mérnökség**: Olyan promptok fejlesztése, amelyek hatékonyan működnek kisebb edge modellekkel
3. **Integrációs tesztelés**: Ügynökök tesztelése szimulált edge körülmények között
4. **Kódgenerálás**: Termelésre optimalizált kód generálása edge telepítéshez

### 4. fázis: Értékelés és tesztelés
1. **Csoportos értékelés**: Több konfiguráció tesztelése az optimális edge beállítások megtalálásához
2. **Teljesítmény profilozás**: Inferencia sebesség, memóriahasználat és pontosság elemzése
3. **Edge szimuláció**: Tesztelés a cél edge telepítési környezethez hasonló feltételek között
4. **Terheléses tesztelés**: Teljesítmény értékelése különböző terhelési körülmények között

### 5. fázis: Telepítés előkészítése
1. **Végső optimalizálás**: Végső finomhangolások alkalmazása a tesztelési eredmények alapján
2. **Telepítési csomagolás**: Modellek és kód csomagolása edge telepítéshez
3. **Dokumentáció**: A telepítési követelmények és konfiguráció dokumentálása
4. **Figyelés beállítása**: Monitorozás és naplózás előkészítése edge telepítéshez

## Célközönség az Edge AI Fejlesztéshez

### Edge AI Fejlesztők
- AI által hajtott edge eszközöket és IoT megoldásokat fejlesztő alkalmazásfejlesztők
- Beágyazott rendszerek fejlesztői, akik AI képességeket integrálnak erőforrás-korlátozott eszközökbe
- Mobil fejlesztők, akik okostelefonokra és tabletekre készítenek helyi AI alkalmazásokat

### Edge AI Mérnökök
- AI mérnökök, akik optimalizálják a modelleket edge telepítésre és kezelik az inferencia pipeline-okat
- DevOps mérnökök, akik edge infrastruktúrán keresztül telepítenek és menedzselnek AI modelleket
- Teljesítmény mérnökök, akik az edge hardver korlátokhoz optimalizálják az AI munkaterheléseket

### Kutatók és Oktatók
- AI kutatók, akik hatékony modelleket és algoritmusokat fejlesztenek edge számítástechnika számára
- Oktatók, akik tanítják az edge AI fogalmait és demonstrálják az optimalizálási technikákat
- Hallgatók, akik tanulják az edge AI telepítés kihívásait és megoldásait

## Edge AI Használati esetek

### Intelligens IoT eszközök
- **Valós idejű képfelismerés**: Számítógépes látás modellek telepítése IoT kamerákra és érzékelőkre
- **Hangfeldolgozás**: Beszédfelismerés és természetes nyelvfeldolgozás megvalósítása okoshangszórókon
- **Előrejelző karbantartás**: Anomália észlelési modellek futtatása ipari edge eszközökön
- **Környezetfigyelés**: Szenzoradat elemző modellek telepítése környezeti alkalmazásokhoz

### Mobil és beágyazott alkalmazások
- **Helyi fordítás**: Offline működő nyelvi fordító modellek megvalósítása
- **Kiterjesztett valóság**: Valós idejű objektum felismerés és követés AR alkalmazásokhoz
- **Egészségügyi monitorozás**: Egészségügyi elemző modellek futtatása hordható eszközökön és orvosi berendezéseken
- **Autonóm rendszerek**: Döntéshozó modellek megvalósítása drónok, robotok és járművek számára

### Edge számítástechnikai infrastruktúra
- **Edge adatközpontok**: AI modellek telepítése edge adatközpontokban alacsony késleltetésű alkalmazásokhoz
- **CDN integráció**: AI feldolgozási képességek beépítése tartalomszállító hálózatokba
- **5G Edge**: 5G edge számítástechnika kihasználása AI-meghajtású alkalmazásokhoz
- **Köd számítástechnika**: AI feldolgozás megvalósítása köd számítástechnikai környezetekben

## Telepítés és beállítás

### Bővítmény telepítés
Telepítse az AI Eszközkészlet bővítményt közvetlenül a Visual Studio Code Marketplace-ből:

**Bővítmény azonosító**: `ms-windows-ai-studio.windows-ai-studio`

**Telepítési módok**:
1. **VS Code Marketplace**: Keresse meg az "AI Toolkit" kifejezést a Bővítmények nézetben
2. **Parancssor**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Közvetlen telepítés**: Letöltés a [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) oldalról

### Előfeltételek Edge AI fejlesztéshez
- **Visual Studio Code**: Legfrissebb verzió ajánlott
- **Python környezet**: Python 3.8+ a szükséges AI könyvtárakkal
- **ONNX Runtime** (opcionális): ONNX modell inferenciához
- **Ollama** (opcionális): Helyi modell szolgáltatáshoz
- **Hardver gyorsító eszközök**: CUDA, OpenVINO vagy platform-specifikus gyorsítók

### Kezdeti konfiguráció
1. **Bővítmény aktiválás**: Nyissa meg a VS Code-ot és ellenőrizze, hogy az AI Eszközkészlet megjelenik az aktivitás sávban
2. **Modell szolgáltató beállítása**: Konfigurálja a hozzáférést GitHub-hoz, OpenAI-hoz, Anthropic-hoz vagy más modell szolgáltatókhoz
3. **Helyi környezet**: Állítsa be a Python környezetet és telepítse a szükséges csomagokat
4. **Hardver gyorsítás**: Konfigurálja a GPU/NPU gyorsítást, ha elérhető
5. **MCP integráció**: Állítsa be a Model Context Protocol szervereket, ha szükséges

### Első beállítás ellenőrző lista
- [ ] AI Eszközkészlet bővítmény telepítve és aktiválva
- [ ] Modell katalógus elérhető és modellek felfedezhetők
- [ ] Játékterem működőképes a modell teszteléséhez
- [ ] Ügynöképítő elérhető a prompt fejlesztéshez
- [ ] Helyi fejlesztési környezet konfigurálva
- [ ] Hardver gyorsítás (ha elérhető) megfelelően konfigurálva

## Kezdés az AI Eszközkészlettel

### Gyors indítási útmutató

Ajánljuk, hogy kezdje a GitHub által tárolt modellekkel a legzökkenőmentesebb élmény érdekében:

1. **Telepítés**: Kövesse a [telepítési útmutatót](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) az AI Eszközkészlet eszközére való beállításához
2. **Modell felfedezés**: A bővítmény fa nézetében válassza a **CATALOG > Models** lehetőséget az elérhető modellek böngészéséhez
3. **GitHub modellek**: Kezdje a GitHub által tárolt modellekkel az optimális integrációért
4. **Játékterem tesztelés**: Bármely modell kártyáról válassza a **Try in Playground** lehetőséget, hogy elkezdje a modell képességek kipróbálását

### Lépésről lépésre Edge AI fejlesztés

#### 1. lépés: Modell felfedezés és kiválasztás
1. Nyissa meg az AI Eszközkészlet nézetet a VS Code aktivitás sávjában
2. Böngésszen a Modell Katalógusban edge telepítésre alkalmas modellek után
3. Szűrje szolgáltatók szerint (GitHub, ONNX, Ollama) az edge követelményeinek megfelelően
4. Használja a **Try in Playground** funkciót a modell képességek azonnali teszteléséhez

#### 2. lépés: Ügynök fejlesztés
1. Használja a **Prompt (Agent) Builder**-t edge-optimalizált AI ügynökök létrehozásához
2. Generáljon indító promptokat természetes nyelvű leírások alapján
3. Ismételje és finomítsa a promptokat a modell válaszai alapján
4. Integrálja az MCP eszközöket a továbbfejlesztett ügynöki képességekhez


#### 3. lépés: Tesztelés és értékelés
1. Használja a **Bulk Run** funkciót több prompt tesztelésére a kiválasztott modellek között
2. Futtassa az ügynököket tesztesetekkel a funkcionalitás megerősítéséhez
3. Értékelje a pontosságot és teljesítményt beépített vagy egyedi metrikák segítségével
4. Hasonlítsa össze a különböző modelleket és konfigurációkat

#### 4. lépés: Finomhangolás és optimalizálás
1. Testreszabja a modelleket speciális él eseteihez
2. Alkalmazzon domain-specifikus finomhangolást
3. Optimalizálja az élről történő telepítés korlátaihoz
4. Verziózza és hasonlítsa össze a különböző ügynök konfigurációkat

#### 5. lépés: Telepítés előkészítése
1. Generáljon élesítésre kész kódot az Agent Builder segítségével
2. Állítson be MCP szerverkapcsolatokat éles használat céljából
3. Készítse elő a telepítési csomagokat az él eszközökhöz
4. Konfigurálja a monitorozást és az értékelési metrikákat

## Minták az AI Toolkithez 

Próbálja ki mintáinkat
Az [AI Toolkit minták](https://github.com/Azure-Samples/AI_Toolkit_Samples) célja, hogy segítsék a fejlesztőket és kutatókat az AI megoldások hatékony felfedezésében és megvalósításában. 

Mintáink tartalmazzák:

Minta kódok: Előre elkészített példák az AI funkciók bemutatására, mint például modellek betanítása, telepítése vagy alkalmazásokba integrálása.
Dokumentáció: Útmutatók és oktatóanyagok az AI Toolkit funkciók megértéséhez és használatához.
Előfeltételek

- Visual Studio Code
- AI Toolkit for Visual Studio Code
- GitHub finomhangolt személyes hozzáférési token (PAT)
- Foundry Local

## Legjobb gyakorlatok az Edge AI fejlesztéshez

### Modell kiválasztás
- **Méretkorlátok**: Válasszon olyan modelleket, amelyek illeszkednek a céleszközök memóriakorlátaihoz
- **Absztrakciós sebesség**: Előnyben részesítse a gyors absztrakciós idejű modelleket valós idejű alkalmazásokhoz
- **Pontosság kompromisszumok**: Egyensúlyozza a modell pontosságát az erőforrás korlátozásokkal
- **Formátum kompatibilitás**: Előnyben részesítse az ONNX vagy hardver-optimalizált formátumokat élre történő telepítéshez

### Optimalizációs technikák
- **Quantizálás**: Használjon INT8 vagy INT4 kvantizálást a modell méretének csökkentésére és a sebesség javítására
- **Pruning**: Távolítsa el a szükségtelen modellparamétereket a számítási igények csökkentése érdekében
- **Tudásdesztilláció**: Készítsen kisebb modelleket, amelyek megtartják a nagyobb modellek teljesítményét
- **Hardvergyorsítás**: Használja NPUs, GPU-k vagy speciális gyorsítókat, ha elérhető

### Fejlesztési munkafolyamat
- **Ismételt tesztelés**: Teszteljen gyakran élhez hasonló körülmények között fejlesztés közben
- **Teljesítményfigyelés**: Folyamatosan figyelje az erőforrás-felhasználást és az absztrakciós sebességet
- **Verziókezelés**: Kövesse nyomon a modellverziókat és az optimalizációs beállításokat
- **Dokumentáció**: Dokumentálja az összes optimalizációs döntést és teljesítmény kompromisszumot

### Telepítési megfontolások
- **Erőforrás megfigyelés**: Figyelje a memória, CPU és energiafelhasználást éles környezetben
- **Visszaesési stratégiák**: Valósítson meg tartalék mechanizmusokat modellhibák esetére
- **Frissítési mechanizmusok**: Tervezze meg a modellfrissítéseket és verziókezelést
- **Biztonság**: Alkalmazzon megfelelő biztonsági intézkedéseket él AI alkalmazásokhoz

## Integráció az Edge AI keretrendszerekkel

### ONNX Runtime
- **Platformfüggetlen telepítés**: Telepítse az ONNX modelleket különböző él platformokra
- **Hardver optimalizáció**: Használja ki az ONNX Runtime hardver specifikus optimalizációit
- **Mobil támogatás**: Használja az ONNX Runtime Mobile-t okostelefonokra és táblagépekre
- **IoT integráció**: Telepítse IoT eszközökre az ONNX Runtime könnyű disztribúcióival

### Windows ML
- **Windows eszközök**: Optimalizálja Windows-alapú él eszközökre és PC-kre
- **NPU gyorsítás**: Használja a Neurális Feldolgozó Egységeket Windows eszközökön
- **DirectML**: Alkalmazza a DirectML-t GPU gyorsításhoz Windows platformokon
- **UWP integráció**: Integrálja Univerzális Windows Platform alkalmazásokkal

### TensorFlow Lite
- **Mobil optimalizáció**: Telepítsen TensorFlow Lite modelleket mobil és beágyazott eszközökre
- **Hardver delegáltak**: Használjon speciális hardver delegáltakat gyorsításhoz
- **Mikrokontrollerek**: Telepítsen mikrokontrollerekre a TensorFlow Lite Micro segítségével
- **Platformfüggetlen támogatás**: Telepítse Android, iOS és beágyazott Linux rendszerekre

### Azure IoT Edge
- **Felhő-él hibrid**: Kombinálja a felhőben történő tanítást az él absztrakcióval
- **Modul telepítés**: Telepítse az AI modelleket IoT Edge modulokként
- **Eszközmenedzsment**: Távolról kezelje az él eszközöket és modellfrissítéseket
- **Telemetria**: Gyűjtsön teljesítményadatokat és modell metrikákat él telepítésekből

## Fejlett él AI forgatókönyvek

### Többmodell telepítés
- **Model együttesek**: Több modellt telepítve jobb pontosság vagy redundancia érdekében
- **A/B tesztelés**: Különböző modelleket tesztel egyszerre él eszközökön
- **Dinamikus kiválasztás**: Válasszon modelleket az aktuális eszközfeltételek alapján
- **Erőforrás megosztás**: Optimalizálja az erőforrás-felhasználást több telepített modell között

### Federált tanulás
- **Elosztott tanítás**: Modell tanítás több él eszközön
- **Adatvédelem fenntartása**: Tartsa a tanítási adatokat helyben, miközben a modell fejlesztéseket megosztja
- **Együttműködő tanulás**: Tegye lehetővé, hogy az eszközök közösen tanuljanak a tapasztalatokból
- **Él-felhő koordináció**: Koordinálja a tanulást az él eszközök és a felhő infrastruktúra között

### Valós idejű feldolgozás
- **Folyamatos adatfeldolgozás**: Folyamatos adatfolyamokat dolgozzon fel él eszközökön
- **Alacsony késleltetésű absztrakció**: Optimalizálja a minimális absztrakciós késleltetést
- **Kötetes feldolgozás**: Hatékonyan dolgozzon fel adatcsomagokat él eszközökön
- **Adaptív feldolgozás**: Igazítsa a feldolgozást az aktuális eszköz képességeihez

## Él AI fejlesztési hibakeresés

### Gyakori problémák
- **Memória korlátok**: A modell túl nagy a céleszköz memóriájához képest
- **Absztrakciós sebesség**: A modell absztrakciója túl lassú valós idejű követelményekhez
- **Pontosság romlás**: Az optimalizáció elfogadhatatlanul csökkenti a modell pontosságát
- **Hardver kompatibilitás**: A modell nem kompatibilis a céleszköz hardverével

### Hibakeresési stratégiák
- **Teljesítmény profilozás**: Használja az AI Toolkit nyomkövetési funkcióit a szűk keresztmetszetek azonosításához
- **Erőforrás megfigyelés**: Figyelje a memória- és CPU használatot fejlesztés közben
- **Fokozatos tesztelés**: Tesztelje az optimalizációkat lépésenként a problémák elkülönítéséhez
- **Hardver szimuláció**: Használja fejlesztői eszközöket a célhardver szimulálására

### Optimalizációs megoldások
- **További kvantizálás**: Alkalmazzon agresszívebb kvantizálási technikákat
- **Modell architektúra**: Vegye fontolóra az élre optimalizált különböző modellarchitektúrákat
- **Előfeldolgozás optimalizáció**: Optimalizálja az adat előfeldolgozást az él korlátozásokhoz
- **Absztrakció optimalizáció**: Alkalmazzon hardver specifikus absztrakciós optimalizációkat

## Erőforrások és további lépések

### Hivatalos dokumentáció
- [AI Toolkit fejlesztői dokumentáció](https://aka.ms/AIToolkit/doc)
- [Telepítési és beállítási útmutató](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps dokumentáció](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) dokumentáció](https://modelcontextprotocol.io/)

### Közösség és támogatás
- [AI Toolkit GitHub tárház](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub hibák és funkciókérések](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord közösség](https://aka.ms/azureaifoundry/discord)
- [VS Code bővítmény piactér](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Technikai erőforrások
- [ONNX Runtime dokumentáció](https://onnxruntime.ai/)
- [Ollama dokumentáció](https://ollama.ai/)
- [Windows ML dokumentáció](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Tanulási útvonalak
- [Edge AI alapok tanfolyam](../Module01/README.md)
- [Kis nyelvi modellek útmutató](../Module02/README.md)
- [Edge telepítési stratégiák](../Module03/README.md)
- [Windows Edge AI fejlesztés](./windowdeveloper.md)

### További erőforrások
- **Tárház statisztikák**: 1.8k+ csillag, 150+ fork, 18+ közreműködő
- **Licenc**: MIT licenc
- **Biztonság**: Alkalmazza a Microsoft biztonsági irányelveket
- **Telemetria**: Tiszteletben tartja a VS Code telemetria beállításait

## Összefoglalás

Az AI Toolkit a Visual Studio Code-hoz egy átfogó platformot képvisel a modern AI fejlesztéshez, egyszerűsített ügynökfejlesztési képességekkel, amelyek különösen értékesek az Edge AI alkalmazások számára. Széles modellkatalógusával, amely támogatja az olyan szolgáltatókat, mint az Anthropic, OpenAI, GitHub és Google, valamint helyi végrehajtással ONNX és Ollama segítségével, a toolkit rugalmasságot kínál a változatos él telepítési forgatókönyvekhez.

A toolkit ereje az integrált megközelítésben rejlik – a modell felfedezéstől és kísérletezéstől a Playground-ban a kifinomult ügynökfejlesztésig a Prompt Builder-rel, átfogó értékelési képességeken át az akadálytalan MCP eszköz integrációig. Az Edge AI fejlesztők számára ez gyors prototipizálást és tesztelést jelent az élre történő telepítés előtt, a gyors iteráció és optimalizálás lehetőségével az erőforrás-korlátozott környezetekben.

Az Edge AI fejlesztés fő előnyei:
- **Gyors kísérletezés**: Gyors tesztelés modelleken és ügynökökön az élre történő véglegesítés előtt
- **Több szolgáltató rugalmassága**: Hozzáférés különböző forrásokból származó modellekhez az optimális él megoldások megtalálásához
- **Helyi fejlesztés**: Tesztelés ONNX és Ollama segítségével offline és adatvédelmi megfontolásokkal
- **Éles készenlét**: Élesítésre kész kód generálása és integráció külső eszközökkel MCP-n keresztül
- **Átfogó értékelés**: Beépített és egyedi metrikák használata az él AI teljesítmény validálásához

Ahogy az AI egyre inkább az élre történő telepítési forgatókönyvek felé halad, az AI Toolkit a VS Code-hoz megadja a fejlesztési környezetet és munkafolyamatot az intelligens alkalmazások építéséhez, teszteléséhez és optimalizálásához az erőforrás-korlátozott környezetek számára. Akár IoT megoldásokat, mobil AI alkalmazásokat vagy beágyazott intelligens rendszereket fejleszt, a toolkit átfogó funkciókészlete és integrált munkafolyamata támogatja az egész él AI fejlesztési életciklust.

Folyamatos fejlesztéssel és aktív közösséggel (1.8k+ GitHub csillag) az AI Toolkit az AI fejlesztési eszközök élvonalában marad, folyamatosan fejlődve, hogy megfeleljen a modern AI fejlesztők igényeinek az élre történő telepítési forgatókönyvekhez.

[Következő Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->