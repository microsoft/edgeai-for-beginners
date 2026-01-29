# AI Toolkit for Visual Studio Code - Edge AI Fejlesztési Útmutató

## Bevezetés

Üdvözlünk az AI Toolkit for Visual Studio Code átfogó útmutatójában, amely az Edge AI fejlesztéshez nyújt segítséget. Ahogy a mesterséges intelligencia a központosított felhőalapú számítástechnikáról a decentralizált edge eszközökre helyeződik át, a fejlesztőknek olyan erőteljes, integrált eszközökre van szükségük, amelyek képesek kezelni az edge telepítés egyedi kihívásait - a korlátozott erőforrásoktól az offline működési követelményekig.

Az AI Toolkit for Visual Studio Code áthidalja ezt a szakadékot azáltal, hogy egy teljes fejlesztési környezetet biztosít, amelyet kifejezetten az edge eszközökön hatékonyan futó AI alkalmazások építésére, tesztelésére és optimalizálására terveztek. Legyen szó IoT szenzorokról, mobil eszközökről, beágyazott rendszerekről vagy edge szerverekről, ez az eszköztár leegyszerűsíti a teljes fejlesztési munkafolyamatot a megszokott VS Code környezetben.

Ez az útmutató végigvezeti az alapvető fogalmakon, eszközökön és legjobb gyakorlatokon, amelyek segítségével az AI Toolkit-et hatékonyan használhatod Edge AI projektjeidben, a kezdeti modell kiválasztástól egészen a gyártási telepítésig.

## Áttekintés

Az AI Toolkit for Visual Studio Code egy erőteljes kiterjesztés, amely leegyszerűsíti az ügynökfejlesztést és az AI alkalmazások létrehozását. Az eszköztár átfogó képességeket kínál AI modellek felfedezésére, értékelésére és telepítésére számos szolgáltatótól - például Anthropic, OpenAI, GitHub, Google - miközben támogatja a helyi modell futtatást ONNX és Ollama segítségével.

Az AI Toolkit különlegessége az AI fejlesztési életciklus teljes körű megközelítése. A hagyományos AI fejlesztési eszközökkel ellentétben, amelyek egyetlen aspektusra összpontosítanak, az AI Toolkit egy integrált környezetet biztosít, amely lefedi a modell felfedezést, kísérletezést, ügynökfejlesztést, értékelést és telepítést - mindezt a megszokott VS Code környezetben.

A platformot kifejezetten gyors prototípus készítésre és gyártási telepítésre tervezték, olyan funkciókkal, mint a prompt generálás, gyors kezdés, zökkenőmentes MCP (Model Context Protocol) eszköz integrációk és kiterjedt értékelési képességek. Az Edge AI fejlesztés szempontjából ez azt jelenti, hogy hatékonyan fejleszthetsz, tesztelhetsz és optimalizálhatsz AI alkalmazásokat edge telepítési forgatókönyvekhez, miközben a teljes fejlesztési munkafolyamatot a VS Code-ban tartod.

## Tanulási célok

Az útmutató végére képes leszel:

### Alapvető kompetenciák
- **Telepíteni és konfigurálni** az AI Toolkit-et a Visual Studio Code-ban az Edge AI fejlesztési munkafolyamatokhoz
- **Navigálni és használni** az AI Toolkit felületét, beleértve a Model Catalog, Playground és Agent Builder funkciókat
- **Kiválasztani és értékelni** az edge telepítésre alkalmas AI modelleket teljesítmény és erőforrás korlátok alapján
- **Konvertálni és optimalizálni** modelleket ONNX formátumra és kvantálási technikákkal az edge eszközökhöz

### Edge AI fejlesztési készségek
- **Edge AI alkalmazásokat tervezni és megvalósítani** az integrált fejlesztési környezet segítségével
- **Modelleket tesztelni** edge-szerű körülmények között helyi következtetés és erőforrás-figyelés révén
- **AI ügynököket létrehozni és testreszabni**, amelyek optimalizáltak az edge telepítési forgatókönyvekhez
- **Értékelni a modellek teljesítményét** az edge számítástechnika szempontjából releváns mutatók alapján (késleltetés, memóriahasználat, pontosság)

### Optimalizálás és telepítés
- **Kvantálási és metszési technikákat alkalmazni**, hogy csökkentsd a modell méretét, miközben elfogadható teljesítményt tartasz fenn
- **Modelleket optimalizálni** specifikus edge hardver platformokhoz, beleértve a CPU, GPU és NPU gyorsítást
- **Legjobb gyakorlatokat megvalósítani** az edge AI fejlesztéshez, beleértve az erőforrás-kezelést és a tartalék stratégiákat
- **Modelleket és alkalmazásokat előkészíteni** az edge eszközökön történő gyártási telepítéshez

### Haladó Edge AI fogalmak
- **Integrálni edge AI keretrendszerekkel**, például ONNX Runtime, Windows ML és TensorFlow Lite
- **Többmodellű architektúrákat és szövetségi tanulási forgatókönyveket megvalósítani** edge környezetekhez
- **Gyakori edge AI problémákat elhárítani**, beleértve a memória korlátokat, következtetési sebességet és hardver kompatibilitást
- **Monitoring és naplózási stratégiákat tervezni** edge AI alkalmazásokhoz gyártási környezetben

### Gyakorlati alkalmazás
- **Teljes Edge AI megoldásokat építeni** a modell kiválasztástól a telepítésig
- **Bemutatni a jártasságot** edge-specifikus fejlesztési munkafolyamatokban és optimalizálási technikákban
- **Alkalmazni a tanult fogalmakat** valós edge AI felhasználási esetekben, beleértve az IoT-t, mobil és beágyazott alkalmazásokat
- **Értékelni és összehasonlítani** különböző edge AI telepítési stratégiákat és azok kompromisszumait

## Kulcsfunkciók az Edge AI fejlesztéshez

### 1. Modellkatalógus és felfedezés
- **Több szolgáltató támogatása**: AI modellek böngészése és elérése Anthropic, OpenAI, GitHub, Google és más szolgáltatóktól
- **Helyi modell integráció**: ONNX és Ollama modellek egyszerű felfedezése edge telepítéshez
- **GitHub modellek**: Közvetlen integráció a GitHub modell hosting szolgáltatásával a zökkenőmentes hozzáférés érdekében
- **Modell összehasonlítás**: Modellek összehasonlítása egymás mellett az edge eszközök korlátainak optimális egyensúlyának megtalálásához

### 2. Interaktív játszótér
- **Interaktív tesztkörnyezet**: Gyors kísérletezés a modellek képességeivel ellenőrzött környezetben
- **Multimodális támogatás**: Tesztelés képekkel, szövegekkel és más, edge forgatókönyvekben tipikus bemenetekkel
- **Valós idejű kísérletezés**: Azonnali visszajelzés a modellek válaszairól és teljesítményéről
- **Paraméter optimalizálás**: Modellparaméterek finomhangolása edge telepítési követelményekhez

### 3. Prompt (Agent) Builder
- **Természetes nyelvi generálás**: Kezdő promptok generálása természetes nyelvi leírások alapján
- **Iteratív finomítás**: Promptok javítása a modellek válaszai és teljesítménye alapján
- **Feladat lebontás**: Összetett feladatok lebontása prompt láncolással és strukturált kimenetekkel
- **Változók támogatása**: Változók használata a promptokban a dinamikus ügynök viselkedéshez
- **Gyártásra kész kód generálása**: Gyártásra kész kód generálása a gyors alkalmazásfejlesztéshez

### 4. Tömeges futtatás és értékelés
- **Több modell tesztelése**: Több prompt futtatása egyszerre a kiválasztott modelleken
- **Hatékony tesztelés nagy léptékben**: Különböző bemenetek és konfigurációk hatékony tesztelése
- **Egyedi tesztesetek**: Ügynökök futtatása tesztesetekkel a funkcionalitás validálásához
- **Teljesítmény összehasonlítás**: Eredmények összehasonlítása különböző modellek és konfigurációk között

### 5. Modellértékelés adathalmazokkal
- **Standard metrikák**: AI modellek tesztelése beépített értékelőkkel (F1 pontszám, relevancia, hasonlóság, koherencia)
- **Egyedi értékelők**: Saját értékelési metrikák létrehozása specifikus felhasználási esetekhez
- **Adathalmaz integráció**: Modellek tesztelése átfogó adathalmazokkal
- **Teljesítmény mérés**: Modell teljesítményének számszerűsítése edge telepítési döntésekhez

### 6. Finomhangolási képességek
- **Modell testreszabás**: Modellek testreszabása specifikus felhasználási esetekhez és területekhez
- **Speciális adaptáció**: Modellek adaptálása speciális területekhez és követelményekhez
- **Edge optimalizálás**: Modellek finomhangolása kifejezetten edge telepítési korlátokhoz
- **Területspecifikus képzés**: Modellek létrehozása, amelyek kifejezetten edge felhasználási esetekhez illeszkednek

### 7. MCP eszköz integráció
- **Külső eszközök csatlakoztatása**: Ügynökök csatlakoztatása külső eszközökhöz Model Context Protocol szervereken keresztül
- **Valós cselekvések**: Ügynökök engedélyezése adatbázisok lekérdezésére, API-k elérésére vagy egyedi logika végrehajtására
- **Meglévő MCP szerverek**: Eszközök használata parancs (stdio) vagy HTTP (server-sent event) protokollokon keresztül
- **Egyedi MCP fejlesztés**: Új MCP szerverek építése és tesztelése az Agent Builder segítségével

### 8. Ügynökfejlesztés és tesztelés
- **Funkcióhívás támogatása**: Ügynökök engedélyezése külső funkciók dinamikus meghívására
- **Valós idejű integrációs tesztelés**: Integrációk tesztelése valós idejű futtatásokkal és eszközhasználattal
- **Ügynök verziózás**: Verziókezelés ügynökökhöz összehasonlítási képességekkel az értékelési eredményekhez
- **Hibakeresés és nyomkövetés**: Helyi nyomkövetési és hibakeresési képességek az ügynökfejlesztéshez

## Edge AI fejlesztési munkafolyamat

### Fázis 1: Modell felfedezés és kiválasztás
1. **Modellkatalógus böngészése**: Használd a modellkatalógust az edge telepítésre alkalmas modellek megtalálásához
2. **Teljesítmény összehasonlítása**: Modellek értékelése méret, pontosság és következtetési sebesség alapján
3. **Helyi tesztelés**: Ollama vagy ONNX modellek használata helyi teszteléshez edge telepítés előtt
4. **Erőforrás követelmények felmérése**: Memória- és számítási igények meghatározása a cél edge eszközökhöz

### Fázis 2: Modell optimalizálás
1. **Konvertálás ONNX formátumba**: A kiválasztott modellek konvertálása ONNX formátumba az edge kompatibilitás érdekében
2. **Kvantálás alkalmazása**: Modellméret csökkentése INT8 vagy INT4 kvantálással
3. **Hardver optimalizálás**: Optimalizálás a cél edge hardverhez (ARM, x86, speciális gyorsítók)
4. **Teljesítmény validálás**: Az optimalizált modellek elfogadható pontosságának ellenőrzése

### Fázis 3: Alkalmazásfejlesztés
1. **Ügynök tervezés**: Az Agent Builder használata edge-optimalizált AI ügynökök létrehozásához
2. **Prompt tervezés**: Olyan promptok fejlesztése, amelyek hatékonyan működnek kisebb edge modellekkel
3. **Integrációs tesztelés**: Ügynökök tesztelése szimulált edge körülmények között
4. **Kód generálás**: Gyártásra optimalizált kód generálása edge telepítéshez

### Fázis 4: Értékelés és tesztelés
1. **Tömeges értékelés**: Több konfiguráció tesztelése az optimális edge beállítások megtalálásához
2. **Teljesítmény profilozás**: Következtetési sebesség, memóriahasználat és pontosság elemzése
3. **Edge szimuláció**: Tesztelés a cél edge telepítési környezethez hasonló körülmények között
4. **Stressz tesztelés**: Teljesítmény értékelése különböző terhelési körülmények között

### Fázis 5: Telepítési előkészítés
1. **Végső optimalizálás**: Végső optimalizálások alkalmazása a tesztelési eredmények alapján
2. **Telepítési csomagolás**: Modellek és kód csomagolása edge telepítéshez
3. **Dokumentáció**: Telepítési követelmények és konfiguráció dokumentálása
4. **Monitoring beállítása**: Monitoring és naplózás előkészítése edge telepítéshez

## Célközönség az Edge AI fejlesztéshez

### Edge AI fejlesztők
- Alkalmazásfejlesztők, akik AI-alapú edge eszközöket és IoT megoldásokat készítenek
- Beágyazott rendszerek fejlesztői, akik AI képességeket integrálnak erőforrás-korlátozott eszközökbe
- Mobilfejlesztők, akik on-device AI alkalmazásokat készítenek okostelefonokra és táblagépekre

### Edge AI mérnökök
- AI mérnökök, akik modelleket optimalizálnak edge telepítéshez és kezelik a következtetési folyamatokat
- DevOps mérnökök, akik AI modelleket telepítenek és kezelnek elosztott edge infrastruktúrában
- Teljesítmény mérnökök, akik AI munkaterheléseket optimalizálnak edge hardver korlátokhoz

### Kutatók és oktatók
- AI kutatók, akik hatékony modelleket és algoritmusokat fejlesztenek edge számítástechnikához
- Oktatók, akik edge AI fogalmakat tanítanak és optimalizálási technikákat demonstrálnak
- Diákok, akik az edge AI telepítés kihívásait és megoldásait tanulják

## Edge AI felhasználási esetek

### Okos IoT eszközök
- **Valós idejű képfelismerés**: Számítógépes látás modellek telepítése IoT kamerákon és szenzorokon
- **Hangfeldolgozás**: Beszédfelismerés és természetes nyelvi feldolgozás megvalósítása okos hangszórókon
- **Prediktív karbantartás**: Anomália detektáló modellek futtatása ipari edge eszközökön
- **Környezeti monitorozás**: Szenzoradat-elemző modellek telepítése környezeti alkalmazásokhoz

### Mobil és beá
2. Induló promptok létrehozása természetes nyelvi leírások alapján  
3. Promptok iterálása és finomítása a modell válaszai alapján  
4. MCP eszközök integrálása az ügynökök képességeinek növelésére  

#### 3. lépés: Tesztelés és értékelés  
1. Használja a **Bulk Run** funkciót több prompt tesztelésére kiválasztott modellek között  
2. Futtassa az ügynököket tesztesetekkel a funkcionalitás validálásához  
3. Értékelje a pontosságot és teljesítményt beépített vagy egyedi metrikák segítségével  
4. Hasonlítsa össze különböző modelleket és konfigurációkat  

#### 4. lépés: Finomhangolás és optimalizálás  
1. Testreszabja a modelleket specifikus edge használati esetekhez  
2. Alkalmazzon domain-specifikus finomhangolást  
3. Optimalizálja az edge telepítési korlátokhoz  
4. Verziózza és hasonlítsa össze az ügynökök különböző konfigurációit  

#### 5. lépés: Telepítés előkészítése  
1. Generáljon gyártásra kész kódot az Agent Builder segítségével  
2. Állítsa be az MCP szerverkapcsolatokat gyártási használatra  
3. Készítse elő a telepítési csomagokat edge eszközökhöz  
4. Konfigurálja a monitorozási és értékelési metrikákat  

## Minták az AI Toolkithez  

Próbálja ki mintáinkat  
Az [AI Toolkit minták](https://github.com/Azure-Samples/AI_Toolkit_Samples) célja, hogy segítsék a fejlesztőket és kutatókat az AI megoldások hatékony felfedezésében és megvalósításában.  

Mintáink tartalmazzák:  

Mintakód: Előre elkészített példák az AI funkciók bemutatására, mint például modellek tanítása, telepítése vagy alkalmazásokba való integrálása.  
Dokumentáció: Útmutatók és oktatóanyagok, amelyek segítenek megérteni az AI Toolkit funkcióit és használatát.  
Előfeltételek  

- Visual Studio Code  
- AI Toolkit a Visual Studio Code-hoz  
- GitHub finomhangolt személyes hozzáférési token (PAT)  
- Foundry Local  

## Legjobb gyakorlatok az Edge AI fejlesztéshez  

### Modellválasztás  
- **Méretkorlátok**: Válasszon olyan modelleket, amelyek megfelelnek a célzott eszközök memória korlátainak  
- **Következtetési sebesség**: Részesítse előnyben a gyors következtetési idővel rendelkező modelleket valós idejű alkalmazásokhoz  
- **Pontossági kompromisszumok**: Egyensúlyozza a modell pontosságát az erőforrás-korlátokkal  
- **Formátumkompatibilitás**: Részesítse előnyben az ONNX vagy hardver-optimalizált formátumokat edge telepítéshez  

### Optimalizálási technikák  
- **Kvantálás**: Használjon INT8 vagy INT4 kvantálást a modell méretének csökkentésére és sebesség növelésére  
- **Metszés**: Távolítsa el a felesleges modellparamétereket a számítási igény csökkentésére  
- **Tudásdesztilláció**: Hozzon létre kisebb modelleket, amelyek megtartják a nagyobb modellek teljesítményét  
- **Hardvergyorsítás**: Használjon NPU-kat, GPU-kat vagy speciális gyorsítókat, ha elérhetők  

### Fejlesztési munkafolyamat  
- **Iteratív tesztelés**: Teszteljen gyakran edge-szerű körülmények között a fejlesztés során  
- **Teljesítményfigyelés**: Folyamatosan figyelje az erőforrás-használatot és a következtetési sebességet  
- **Verziókezelés**: Kövesse nyomon a modellverziókat és optimalizálási beállításokat  
- **Dokumentáció**: Dokumentálja az összes optimalizálási döntést és teljesítmény-kompromisszumot  

### Telepítési szempontok  
- **Erőforrás-figyelés**: Figyelje a memória-, CPU- és energiahasználatot gyártásban  
- **Visszaesési stratégiák**: Valósítson meg visszaesési mechanizmusokat modellhibák esetére  
- **Frissítési mechanizmusok**: Tervezze meg a modellfrissítéseket és verziókezelést  
- **Biztonság**: Valósítson meg megfelelő biztonsági intézkedéseket edge AI alkalmazásokhoz  

## Integráció Edge AI keretrendszerekkel  

### ONNX Runtime  
- **Platformközi telepítés**: Telepítse az ONNX modelleket különböző edge platformokon  
- **Hardver-optimalizáció**: Használja az ONNX Runtime hardver-specifikus optimalizációit  
- **Mobil támogatás**: Használja az ONNX Runtime Mobile-t okostelefonokhoz és táblagépekhez  
- **IoT integráció**: Telepítse IoT eszközökre az ONNX Runtime könnyű disztribúcióival  

### Windows ML  
- **Windows eszközök**: Optimalizálja Windows-alapú edge eszközökhöz és PC-khez  
- **NPU gyorsítás**: Használja a Windows eszközök Neural Processing Unit-jait  
- **DirectML**: Használja a DirectML-t GPU gyorsításhoz Windows platformokon  
- **UWP integráció**: Integrálja Universal Windows Platform alkalmazásokkal  

### TensorFlow Lite  
- **Mobil optimalizáció**: Telepítse a TensorFlow Lite modelleket mobil és beágyazott eszközökre  
- **Hardver delegáltak**: Használjon speciális hardver delegáltakat gyorsításhoz  
- **Mikrokontrollerek**: Telepítse mikrokontrollerekre a TensorFlow Lite Micro segítségével  
- **Platformközi támogatás**: Telepítse Android, iOS és beágyazott Linux rendszerekre  

### Azure IoT Edge  
- **Felhő-edge hibrid**: Kombinálja a felhőben történő tanítást az edge következtetéssel  
- **Modul telepítés**: Telepítse az AI modelleket IoT Edge modulokként  
- **Eszközkezelés**: Kezelje edge eszközöket és modellfrissítéseket távolról  
- **Telemetria**: Gyűjtsön teljesítményadatokat és modellmetrikákat edge telepítésekből  

## Fejlett Edge AI forgatókönyvek  

### Többmodellű telepítés  
- **Modellcsoportok**: Telepítsen több modellt a pontosság vagy redundancia javítására  
- **A/B tesztelés**: Teszteljen különböző modelleket egyidejűleg edge eszközökön  
- **Dinamikus kiválasztás**: Válasszon modelleket az aktuális eszközállapot alapján  
- **Erőforrás-megosztás**: Optimalizálja az erőforrás-használatot több telepített modell között  

### Federált tanulás  
- **Elosztott tanítás**: Tanítsa a modelleket több edge eszközön  
- **Adatvédelem megőrzése**: Tartsa helyben a tanítási adatokat, miközben megosztja a modellfejlesztéseket  
- **Kollaboratív tanulás**: Tegye lehetővé az eszközök számára, hogy kollektív tapasztalatokból tanuljanak  
- **Edge-felhő koordináció**: Koordinálja a tanulást edge eszközök és felhő infrastruktúra között  

### Valós idejű feldolgozás  
- **Stream feldolgozás**: Folyamatos adatfolyamok feldolgozása edge eszközökön  
- **Alacsony késleltetésű következtetés**: Optimalizálja a minimális következtetési késleltetés érdekében  
- **Batch feldolgozás**: Hatékonyan dolgozza fel az adatcsomagokat edge eszközökön  
- **Adaptív feldolgozás**: Igazítsa a feldolgozást az aktuális eszközkapacitásokhoz  

## Edge AI fejlesztés hibaelhárítása  

### Gyakori problémák  
- **Memóriakorlátok**: A modell túl nagy a célzott eszköz memóriájához  
- **Következtetési sebesség**: A modell következtetése túl lassú valós idejű követelményekhez  
- **Pontosságromlás**: Az optimalizálás elfogadhatatlanul csökkenti a modell pontosságát  
- **Hardverkompatibilitás**: A modell nem kompatibilis a célzott hardverrel  

### Hibakeresési stratégiák  
- **Teljesítményprofilozás**: Használja az AI Toolkit nyomkövetési funkcióit a szűk keresztmetszetek azonosításához  
- **Erőforrás-figyelés**: Figyelje a memória- és CPU-használatot a fejlesztés során  
- **Inkrementális tesztelés**: Tesztelje az optimalizálásokat fokozatosan a problémák elkülönítéséhez  
- **Hardverszimuláció**: Használjon fejlesztői eszközöket a célzott hardver szimulálásához  

### Optimalizálási megoldások  
- **További kvantálás**: Alkalmazzon agresszívebb kvantálási technikákat  
- **Modellarchitektúra**: Fontolja meg különböző modellarchitektúrákat, amelyek edge-re optimalizáltak  
- **Előfeldolgozási optimalizálás**: Optimalizálja az adat előfeldolgozást edge korlátokhoz  
- **Következtetési optimalizálás**: Használjon hardver-specifikus következtetési optimalizációkat  

## Erőforrások és következő lépések  

### Hivatalos dokumentáció  
- [AI Toolkit fejlesztői dokumentáció](https://aka.ms/AIToolkit/doc)  
- [Telepítési és beállítási útmutató](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentáció](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentáció](https://modelcontextprotocol.io/)  

### Közösség és támogatás  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub hibák és funkciókérések](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord közösség](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technikai erőforrások  
- [ONNX Runtime dokumentáció](https://onnxruntime.ai/)  
- [Ollama dokumentáció](https://ollama.ai/)  
- [Windows ML dokumentáció](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Tanulási útvonalak  
- [Edge AI alapok kurzus](../Module01/README.md)  
- [Kis nyelvi modellek útmutató](../Module02/README.md)  
- [Edge telepítési stratégiák](../Module03/README.md)  
- [Windows Edge AI fejlesztés](./windowdeveloper.md)  

### További erőforrások  
- **Repository statisztikák**: 1.8k+ csillag, 150+ fork, 18+ közreműködő  
- **Licenc**: MIT Licenc  
- **Biztonság**: Microsoft biztonsági irányelvek érvényesek  
- **Telemetria**: Tiszteletben tartja a VS Code telemetria beállításait  

## Összegzés  

Az AI Toolkit for Visual Studio Code egy átfogó platformot képvisel a modern AI fejlesztéshez, amely különösen értékes az Edge AI alkalmazások számára. Kiterjedt modellkatalógusával, amely támogatja az olyan szolgáltatókat, mint Anthropic, OpenAI, GitHub és Google, valamint helyi végrehajtási lehetőségeivel az ONNX és Ollama segítségével, a toolkit biztosítja a különböző edge telepítési forgatókönyvekhez szükséges rugalmasságot.  

A toolkit ereje az integrált megközelítésében rejlik—modellfelfedezéstől és kísérletezéstől a Playgroundban, a Prompt Builderrel történő kifinomult ügynökfejlesztésen, átfogó értékelési képességeken és zökkenőmentes MCP eszközintegráción keresztül. Az Edge AI fejlesztők számára ez gyors prototípus-készítést és AI ügynökök tesztelését jelenti edge telepítés előtt, azzal a képességgel, hogy gyorsan iteráljanak és optimalizáljanak erőforrás-korlátozott környezetekhez.  

Az Edge AI fejlesztés kulcsfontosságú előnyei közé tartozik:  
- **Gyors kísérletezés**: Modellek és ügynökök gyors tesztelése edge telepítés előtt  
- **Több szolgáltató rugalmassága**: Modellek elérése különböző forrásokból az optimális edge megoldások megtalálásához  
- **Helyi fejlesztés**: Tesztelés ONNX és Ollama segítségével offline és adatvédelmi szempontból biztonságos fejlesztéshez  
- **Gyártási készség**: Gyártásra kész kód generálása és külső eszközök integrálása MCP-n keresztül  
- **Átfogó értékelés**: Beépített és egyedi metrikák használata az edge AI teljesítmény validálásához  

Ahogy az AI egyre inkább az edge telepítési forgatókönyvek felé mozdul, az AI Toolkit for VS Code biztosítja azt a fejlesztési környezetet és munkafolyamatot, amely szükséges az intelligens alkalmazások építéséhez, teszteléséhez és optimalizálásához erőforrás-korlátozott környezetekben. Akár IoT megoldásokat, mobil AI alkalmazásokat vagy beágyazott intelligens rendszereket fejleszt, a toolkit átfogó funkciókészlete és integrált munkafolyamata támogatja az egész Edge AI fejlesztési életciklust.  

A folyamatos fejlesztéssel és aktív közösséggel (1.8k+ GitHub csillag), az AI Toolkit továbbra is az AI fejlesztési eszközök élvonalában marad, folyamatosan fejlődve, hogy megfeleljen a modern AI fejlesztők igényeinek, akik edge telepítési forgatókönyvekre építenek.  

[Next Foundry Local](./foundrylocal.md)  

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.