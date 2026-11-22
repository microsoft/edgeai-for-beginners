# Windows Edge AI Fejlesztési Útmutató

## Bevezetés

Üdvözöljük a Windows Edge AI Fejlesztésben - az átfogó útmutatójában az intelligens alkalmazások építéséhez, amelyek kiaknázák az eszközön futó MI erejét a Microsoft Windows AI Foundry platform segítségével. Ez az útmutató kifejezetten Windows fejlesztőknek készült, akik a legmodernebb Edge AI képességeket kívánják integrálni alkalmazásaikba, miközben kihasználják a Windows teljes körű hardveres gyorsítását.

### A Windows AI Előnyei

A Windows AI Foundry egy egységes, megbízható és biztonságos platform, amely támogatja a teljes MI fejlesztői életciklust - a modell kiválasztásától és finomhangolásától az optimalizáláson és telepítésen át a CPU, GPU, NPU és hibrid felhő architektúráknak megfelelő működésig. Ez a platform demokratizálja az MI fejlesztést azáltal, hogy biztosítja:

- **Hardver Absztrakció**: Zökkenőmentes telepítés AMD, Intel, NVIDIA és Qualcomm szilikonon
- **Eszközön Futó Intelligencia**: Adatvédelmet megőrző MI, amely teljes egészében helyi hardveren fut
- **Optimalizált Teljesítmény**: Előre optimalizált modellek Windows hardver konfigurációkhoz
- **Vállalati Szintű**: Gyártásra alkalmas biztonsági és megfelelőségi funkciók

### Windows ML
A Windows Machine Learning (ML) lehetővé teszi C#, C++ és Python fejlesztők számára, hogy helyben futtassanak ONNX MI modelleket Windows PC-ken az ONNX Runtime segítségével, automatikus végrehajtási közvetítő kezeléssel különböző hardverekhez (CPU-k, GPU-k, NPU-k). Az [ONNX Runtime](https://onnxruntime.ai/docs/) használható PyTorch, Tensorflow/Keras, TFLite, scikit-learn és más keretrendszerekből származó modellekkel.


![WindowsML Egy diagram, amely bemutatja, hogy egy ONNX modell hogyan jut át a Windows ML-en, hogy elérje az NPU-kat, GPU-kat és CPU-kat.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

A Windows ML biztosít egy megosztott Windows-szintű példányt az ONNX Runtime-ból, valamint a végrehajtási közvetítők (EP-k) dinamikus letöltésének lehetőségét.

### Miért Windows az Edge AI-hoz?

**Univerzális Hardvertámogatás**
A Windows ML automatikus hardveroptimalizálást nyújt a teljes Windows ökoszisztémában, biztosítva, hogy MI alkalmazásai optimálisan működjenek a mögöttes szilikon architektúrától függetlenül.

**Integrált MI Futásidő**
A beépített Windows ML következtető motor kiküszöböli a bonyolult beállítási igényeket, lehetővé téve a fejlesztők számára, hogy az alkalmazáslogikára koncentráljanak az infrastruktúra aggályai helyett.

**Copilot+ PC Optimalizáció**
Kifejezetten a következő generációs Windows eszközökhöz tervezett API-k, amelyek dedikált Neurális Feldolgozó Egységekkel (NPU-k) kivételes teljesítményt nyújtanak watt-onként.

**Fejlesztői Ökoszisztéma**
Gazdag eszközkészlet, beleértve a Visual Studio integrációt, átfogó dokumentációt és mintaalkalmazásokat, amelyek felgyorsítják a fejlesztési ciklusokat.

## Tanulási Célok

Ezzel a Windows Edge AI fejlesztési útmutatóval elsajátítja a kulcsfontosságú készségeket a termelésre kész MI alkalmazások építéséhez a Windows platformon.

### Alapvető Technikai Kompetenciák

**Windows AI Foundry Mesterfok**
- Ismerje meg a Windows AI Foundry platform felépítését és komponenseit
- Navigáljon az MI fejlesztői életciklus teljes spektrumán a Windows környezetben
- Alkalmazzon biztonsági legjobb gyakorlatokat az eszközön futó MI alkalmazások esetében
- Optimalizálja alkalmazásait különböző Windows hardver konfigurációkhoz

**API Integrációs Szakértelem**
- Sajátítsa el a Windows AI API-k használatát szöveg-, látás- és multimodális alkalmazásokhoz
- Valósítson meg Phi Silica nyelvi modell integrációt szöveggeneráláshoz és érveléshez
- Telepítsen számítógépes látás képességeket beépített képfeldolgozó API-kon keresztül
- Testreszabja az előre betanított modelleket LoRA (alacsony rangú adaptáció) technikákkal

**Foundry Local Implementáció**
- Böngésszen, értékeljen és telepítsen nyílt forráskódú nyelvi modelleket a Foundry Local CLI segítségével
- Értse meg a modellek optimalizálását és kvantálását helyi telepítéshez
- Valósítson meg offline MI képességeket internetkapcsolat nélkül
- Kezelje a modellek életciklusait és frissítéseit gyártási környezetekben

**Windows ML Telepítés**
- Vigye egyedi ONNX modelleket Windows alkalmazásokba a Windows ML használatával
- Használja ki az automatikus hardveres gyorsítást CPU, GPU és NPU architektúrákon
- Valósítson meg valós idejű következtetést optimális erőforrás használattal
- Tervezzen skálázható MI alkalmazásokat különféle Windows eszközkategóriákhoz

### Alkalmazásfejlesztési Készségek

**Platformközi Windows Fejlesztés**
- Építsen MI által vezérelt alkalmazásokat .NET MAUI segítségével univerzális Windows telepítéshez
- Integrálja az MI képességeket Win32, UWP és Progresszív Webalkalmazásokba
- Implementáljon válaszkész felhasználói felületeket, amelyek igazodnak az MI feldolgozási állapotokhoz
- Kezelje az aszinkron MI műveleteket megfelelő felhasználói élmény mintákkal

**Teljesítmény Optimalizálás**
- Profilozza és optimalizálja az MI következtetés teljesítményét különböző hardver konfigrációkon
- Valósítson meg hatékony memória kezelést nagy nyelvi modellekhez
- Tervezzen olyan alkalmazásokat, amelyek elegánsan csökkennek elérhető hardver képességek szerint
- Alkalmazzon gyorsítótárazási stratégiákat gyakran használt MI műveletekhez

**Termelésre Készen**
- Implementáljon átfogó hibakezelést és tartalék mechanizmusokat
- Tervezzen telemetriai és monitorozó rendszereket az MI alkalmazás teljesítményének követéséhez
- Alkalmazzon biztonsági legjobb gyakorlatokat helyi MI modell tárolás és végrehajtás esetén
- Tervezze meg a telepítési stratégiákat vállalati és fogyasztói alkalmazásokhoz

### Üzleti és Stratégiai Megértés

**MI Alkalmazás Architektúra**
- Tervezzen hibrid architektúrákat, amelyek optimalizálják a helyi és felhőalapú MI feldolgozást
- Értékelje a modell méret, pontosság és következtetési sebesség közötti kompromisszumokat
- Tervezzen adatfolyam architektúrákat, amelyek megőrzik a magánéletet, miközben lehetővé teszik az intelligenciát
- Valósítson meg költséghatékony MI megoldásokat, amelyek skálázhatóak a felhasználói igények szerint

**Piaci Pozícionálás**
- Értse meg a Windows-natív MI alkalmazások versenyelőnyeit
- Azonosítsa azokat az eseteket, amikor az eszközön futó MI jobb felhasználói élményt nyújt
- Fejlesszen piacra lépési stratégiákat MI-vel feljavított Windows alkalmazásokhoz
- Pozícionálja alkalmazásait a Windows ökoszisztéma előnyeinek kihasználására

## Windows App SDK MI Minták

A Windows App SDK átfogó mintákat nyújt, amelyek bemutatják az MI integrációt több keretrendszerben és telepítési forgatókönyvben. Ezek a minták alapvető hivatkozások a Windows MI fejlesztési mintáinak megértéséhez.

### Windows AI Foundry Minták

| Minta | Keretrendszer | Fókusz Terület | Kulcsjellemzők |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API-k Integrációja | Teljes WinUI alkalmazás, amely bemutatja a Windows AI API-kat, ARM64 optimalizációt, csomagolt telepítést |

**Kulcs Technológiák:**
- Windows AI API-k
- WinUI 3 keretrendszer
- ARM64 platform optimalizáció
- Copilot+ PC kompatibilitás
- Csomagolt alkalmazás telepítés

**Előfeltételek:**
- Windows 11 Copilot+ PC ajánlott
- Visual Studio 2022
- ARM64 build konfiguráció
- Windows App SDK 1.8.1+

### Windows ML Minták

#### C++ Minták

| Minta | Típus | Fókusz Terület | Kulcsjellemzők |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolalkalmazás | Alapvető Windows ML | EP felfedezés, parancssori opciók, modell fordítás |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolalkalmazás | Keretrendszer Telepítés | Megosztott futásidő, kisebb telepítési lábnyom |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolalkalmazás | Önálló Telepítés | Önálló telepítés, futásidő függőségek nélkül |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Könyvtár Használat | WindowsML megosztott könyvtárban, memória kezelés |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Oktatóanyag | Modell konverzió, EP fordítás, Build 2025 oktatóanyag |

#### C# Minták

**Konzolalkalmazások**

| Minta | Típus | Fókusz Terület | Kulcsjellemzők |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolalkalmazás | Alapvető C# Integráció | Megosztott segédhasználat, parancssori felület |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Oktatóanyag | Modell konverzió, EP fordítás, Build 2025 oktatóanyag |

**GUI Alkalmazások**

| Minta | Keretrendszer | Fókusz Terület | Kulcsjellemzők |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Asztali GUI | Kép osztályozás WPF felülettel |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Hagyományos GUI | Kép osztályozás Windows Forms felülettel |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | Kép osztályozás WinUI 3 felülettel |

#### Python Minták

| Minta | Nyelv | Fókusz Terület | Kulcsjellemzők |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Kép Osztályozás | WinML Python kötődések, kötegelt képfeldolgozás |

### Minta Előfeltételek

**Rendszerkövetelmények:**
- Windows 11 PC, 24H2 (26100-as build) vagy újabb verzióval
- Visual Studio 2022 C++ és .NET munka terhelésekkel
- Windows App SDK 1.8.1 vagy későbbi
- Python 3.10-3.13 Python mintákhoz x64 és ARM64 eszközökön

**Windows AI Foundry Specifikus:**
- Copilot+ PC ajánlott optimális teljesítményhez
- ARM64 build konfiguráció Windows AI mintákhoz
- Csomagazonosság szükséges (nem csomagolt alkalmazások már nem támogatottak)

### Általános Minta Munkamenet

A legtöbb Windows ML minta követi ezt a szabványos mintát:

1. **Környezet Inicializálása** - ONNX Runtime környezet létrehozása
2. **Végrehajtási Közvetítők Regisztrálása** - Elérhető hardver gyorsítók (CPU, GPU, NPU) felfedezése és regisztrálása
3. **Modell Betöltése** - ONNX modell betöltése, opcionálisan célozott hardverre fordítás
4. **Bemenet Előkészítése** - Képek/adatok konvertálása modell bemeneti formátumba
5. **Következtetés Futtatása** - Modell futtatása és előrejelzések lekérése
6. **Eredmények Feldolgozása** - Softmax alkalmazása és top előrejelzések megjelenítése

### Használt Modellfájlok

| Modell | Cél | Tartalmazza | Megjegyzések |
|-------|---------|----------|-------|
| SqueezeNet | Könnyű súlyú kép osztályozás | ✅ Tartalmazza | Előre betanított, használatra kész |
| ResNet-50 | Nagy pontosságú kép osztályozás | ❌ Átalakítást igényel | Használja az [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) átalakításhoz |

### Hardvertámogatás

Minden minta automatikusan észleli és kihasználja az elérhető hardvert:
- **CPU** - Univerzális támogatás minden Windows eszközön
- **GPU** - Automatikus detektálás és optimalizálás az elérhető grafikus hardverhez
- **NPU** - Kihasználja a Neurális Feldolgozó Egységeket a támogatott eszközökön (Copilot+ PC-k)

## Windows AI Foundry Platform Komponensek

### 1. Windows AI API-k

A Windows AI API-k készen álló MI képességeket biztosítanak eszközön futó modellekkel, optimalizálva a hatékonyságot és teljesítményt Copilot+ PC eszközökön, minimális beállítást igényelve.

#### Alapvető API Kategóriák

**Phi Silica Nyelvi Modell**
- Kicsi, de erős nyelvi modell szöveggeneráláshoz és érveléshez
- Optimalizált valós idejű következtetéshez minimális energiafogyasztással
- Támogatja az egyedi finomhangolást LoRA technikákkal
- Integráció a Windows szemantikus kereséssel és tudás lekérdezéssel

**Számítógépes Látás API-k**
- **Szövegfelismerés (OCR)**: Magas pontosságú szövegek kinyerése képekből
- **Kép felbontás növelése**: Képek felskálázása helyi MI modellekkel
- **Kép szegmentálás**: Különálló objektumok azonosítása és elkülönítése képekben
- **Kép leírás**: Részletes szöveges leírások generálása vizuális tartalomhoz
- **Objektum eltávolítás**: Nem kívánt objektumok eltávolítása képekből MI által vezérelt kitöltéssel

**Multimodális Képességek**
- **Látás-Nyelv Integráció**: Szöveg és kép értelmezés egybekapcsolása
- **Szemantikus Keresés**: Természetes nyelvű keresések multimédiás tartalmak között
- **Tudás Lekérdezés**: Intelligens keresési élmények építése helyi adatokkal

### 2. Foundry Local

A Foundry Local fejlesztőknek gyors hozzáférést biztosít készen álló nyílt forráskódú nyelvi modellekhez Windows Szilikonon, lehetővé téve modellek böngészését, tesztelését, interakcióját és helyi alkalmazásokban való telepítését.

#### Foundry Local Mintaalkalmazások

A [Foundry Local tárház](https://github.com/microsoft/Foundry-Local/tree/main/samples) átfogó mintákat biztosít több programozási nyelven és keretrendszerben, bemutatva különböző integrációs mintákat és használati eseteket.

| Minta | Nyelv/Keretrendszer | Fókusz Terület | Kulcsjellemzők |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Implementáció | szemantikus Kernel integráció, Qdrant vektortár, JINA beágyazások, dokumentum feldolgozás, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Asztali Chat Alkalmazás | Platformfüggetlen chat, helyi/felhő modell váltás, OpenAI SDK integráció, valós idejű streaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Alap Integráció | Egyszerű SDK használat, modell inicializálás, alap chat funkciók |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Alap Integráció | Python SDK használat, streaming válaszok, OpenAI-kompatibilis API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Rendszerintegráció | Alacsony szintű SDK használat, aszinkron műveletek, reqwest HTTP kliens |

#### Minta kategóriák használati eset szerint

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Teljes RAG megvalósítás a Semantic Kernel, Qdrant vektor adatbázis és JINA beágyazások használatával
- **Architektúra**: Dokumentumbetáplálás → Szövegtördelés → Vektor beágyazások → Hasonlósági keresés → Kontextusérzékeny válaszok
- **Technológiák**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX beágyazások, folyamatos csevegés-kiegészítés

**Asztali alkalmazások**
- **electron/foundry-chat**: Gyártásra kész csevegőalkalmazás helyi/felhő modellek közötti váltással
- **Funkciók**: Modellválasztó, folyamatos válaszok, hibakezelés, többplatformos telepítés
- **Architektúra**: Electron fő folyamat, IPC kommunikáció, biztonságos előtöltési szkriptek

**SDK integrációs példák**
- **JavaScript (Node.js)**: Alapvető modellinterakció és folyamatos válaszok
- **Python**: OpenAI-kompatibilis API használata aszinkron folyamatos adatfolyammal
- **Rust**: Alacsony szintű integráció reqwesttel és tokióval aszinkron műveletekhez

#### Feltételek a Foundry Local mintákhoz

**Rendszerkövetelmények:**
- Windows 11 a Foundry Local telepítésével
- Node.js v16+ a JavaScript/Electron mintákhoz
- .NET 8.0+ a C# mintákhoz
- Python 3.10+ a Python mintákhoz
- Rust 1.70+ a Rust mintákhoz

**Telepítés:**
```powershell
# Telepítse a Foundry Local-t
winget install Microsoft.FoundryLocal

# Ellenőrizze a telepítést
foundry --version
foundry model list
```

#### Minta specifikus beállítás

**dotNET RAG minta:**
```powershell
# Szükséges csomagok telepítése NuGet segítségével
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Qdrant vektor adatbázis indítása
docker run -p 6333:6333 qdrant/qdrant

# Jupyter jegyzetfüzet futtatása
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron csevegő minta:**
```powershell
# Környezeti változók beállítása felhő tartalékhoz
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Függőségek telepítése és futtatás
npm install
npm start
```

**JavaScript/Python/Rust minták:**
```powershell
# Modell letöltése (példa a phi-3.5-mini-vel)
foundry model run phi-3.5-mini

# Futtassa a megfelelő mintát
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Főbb jellemzők

**Modell katalógus**
- Átfogó gyűjtemény előre optimalizált nyílt forráskódú modellekből
- CPU-kon, GPU-kon és NPU-kon optimalizált modellek azonnali telepítésre
- Népszerű modellcsaládok támogatása, köztük Llama, Mistral, Phi, és speciális domain modellek

**CLI integráció**
- Parancssori felület a modellkezeléshez és telepítéshez
- Automatikus optimalizálás és kvantálási munkafolyamatok
- Integráció népszerű fejlesztői környezettel és CI/CD folyamatokkal

**Helyi telepítés**
- Teljes offline működés felhőfüggőség nélkül
- Egyedi modellformátumok és konfigurációk támogatása
- Hatékony modellkiszolgálás automatikus hardveroptimalizálással

### 3. Windows ML

A Windows ML szolgál alap AI platformként és integrált levezetési futtatókörnyezetként Windows alatt, lehetővé téve a fejlesztők számára, hogy hatékonyan telepítsenek egyedi modelleket a széles Windows hardverökoszisztémán belül.

#### Architektúra előnyei

**Univerzális hardvertámogatás**
- Automatikus optimalizálás az AMD, Intel, NVIDIA és Qualcomm processzorokra
- CPU, GPU és NPU végrehajtás támogatása átlátszó váltással
- Hardver absztrakció, amely megszünteti a platform-specifikus optimalizációs munkát

**Modell rugalmasság**
- ONNX modellformátum támogatása automatikus konverzióval népszerű keretrendszerekből
- Egyedi modell telepítés gyártásravaló teljesítménnyel
- Integráció meglévő Windows alkalmazás architektúrákkal

**Vállalati integráció**
- Kompatibilis a Windows biztonsági és megfelelőségi keretrendszerekkel
- Támogatás vállalati telepítési és menedzsment eszközökhöz
- Integráció a Windows eszközmenedzsment és megfigyelő rendszerekkel

## Fejlesztési munkafolyamat

### 1. Fázis: Környezet előkészítés és eszköz konfiguráció

**Fejlesztői környezet előkészítése**
1. Telepítse a Visual Studio 2022-t C++ és .NET munkaterhelésekkel
2. Telepítse a Windows App SDK 1.8.1 vagy újabb verziót
3. Állítsa be a Windows AI Foundry CLI eszközöket
4. Állítsa be az AI Toolkit kiegészítőt a Visual Studio Code-hoz
5. Hozzon létre teljesítmény profilozási és megfigyelési eszközöket
6. Biztosítsa az ARM64 build konfigurációt a Copilot+ PC optimalizációhoz

**Minta tároló beállítása**
1. Klónozza a [Windows App SDK mintatárat](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigáljon a `Samples/WindowsAIFoundry/cs-winui` mappába Windows AI API példákhoz
3. Navigáljon a `Samples/WindowsML` mappába teljes Windows ML példákhoz
4. Tekintse át a [build követelményeket](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) a kívánt platformokhoz

**AI Dev Gallery felfedezése**
- Fedezze fel a mintaalkalmazásokat és referenciamegvalósításokat
- Tesztelje a Windows AI API-kat interaktív bemutatókkal
- Vizsgálja meg a forráskódot a legjobb gyakorlatok és minták érdekében
- Azonosítson releváns mintákat az adott használati esethez

### 2. Fázis: Modell kiválasztása és integrációja

**Követelmények elemzése**
- Határozza meg az AI képességek funkcionális követelményeit
- Állapítsa meg a teljesítménybeli korlátokat és optimalizációs célokat
- Értékelje az adatvédelmi és biztonsági követelményeket
- Tervezze meg a telepítési architektúrát és skálázási stratégiákat

**Modell értékelése**
- Használja a Foundry Local-t nyílt forráskódú modellek tesztelésére az adott esethez
- Mérje össze a Windows AI API-kat az egyedi modellkövetelményekkel
- Értékelje a modellméret, pontosság és inferencia sebesség közti kompromisszumokat
- Prototípus integrációs megközelítések kiválasztott modellekkel

### 3. Fázis: Alkalmazásfejlesztés

**Alapvető integráció**
- Valósítsa meg a Windows AI API integrációt megfelelő hibakezeléssel
- Tervezzen felhasználói felületeket, amelyek támogatják az AI feldolgozási munkafolyamatokat
- Alkalmazzon gyorsítótárazási és optimalizálási stratégiákat modell inferenciához
- Tegyen hozzá telemetriát és megfigyelést az AI működés teljesítményéhez

**Tesztelés és érvényesítés**
- Tesztelje az alkalmazásokat különböző Windows hardverkonfigurációkon
- Hitelesítse a teljesítménymutatókat különféle terhelési feltételek mellett
- Valósítson meg automatizált tesztelést az AI funkciók megbízhatóságára
- Végezzen felhasználói élmény tesztelést AI-alapú funkciókkal

### 4. Fázis: Optimalizálás és Telepítés

**Teljesítmény optimalizálás**
- Profilozza az alkalmazás teljesítményét a céltarget hardverkonfigurációkon
- Optimalizálja a memóriahasználatot és a modell betöltési stratégiákat
- Valósítson meg alkalmazkodó viselkedést a rendelkezésre álló hardverfunkciók szerint
- Finomhangolja a felhasználói élményt különböző teljesítményesetekhez

**Gyártási telepítés**
- Csomagolja az alkalmazásokat a megfelelő AI modell függőségekkel
- Valósítson meg frissítési mechanizmusokat modellekhez és alkalmazáslogikához
- Állítsa be a megfigyelést és elemzést gyártási környezetekhez
- Tervezze meg a kibocsátási stratégiákat vállalati és fogyasztói telepítésekhez

## Gyakorlati megvalósítási példák

### Példa 1: Intelligens dokumentumfeldolgozó alkalmazás

Készítsen Windows alkalmazást, amely több AI képességet használ dokumentumfeldolgozáshoz:

**Használt technológiák:**
- Phi Silica dokumentumösszefoglaláshoz és kérdés-válasz támogatáshoz
- OCR API-k szkennelt dokumentumok szövegkinyeréséhez
- Kép Leíró API-k diagramok és ábrák elemzéséhez
- Egyedi ONNX modellek dokumentumosztályozáshoz

**Megvalósítási megközelítés:**
- Tervezzen moduláris architektúrát csatlakoztatható AI komponensekkel
- Valósítson meg aszinkron feldolgozást nagy dokumentumtömegekhez
- Tegyen hozzá előrehaladási jelzőket és törlés támogatást hosszú műveletekhez
- Tartalmazzon offline képességet érzékeny dokumentumfeldolgozáshoz

### Példa 2: Kiskereskedelmi készletkezelő rendszer

Hozzon létre AI által vezérelt készletrendszert kiskereskedelmi alkalmazásokhoz:

**Használt technológiák:**
- Kép szegmentálás termékazonosításhoz
- Egyedi látásmodellek márka- és kategória osztályozáshoz
- Foundry Local telepítése speciális kiskereskedelmi nyelvi modellekkel
- Integráció meglévő POS és készletrendszerekkel

**Megvalósítási megközelítés:**
- Kamera integráció valós idejű termékszkenneléshez
- Vonalkód és vizuális termék felismerés megvalósítása
- Természetes nyelvű készlet lekérdezések helyi nyelvi modellekkel
- Skálázható architektúra tervezése több üzlet telepítéséhez

### Példa 3: Egészségügyi dokumentációs asszisztens

Fejlesszen adatvédelmet biztosító egészségügyi dokumentációs eszközt:

**Használt technológiák:**
- Phi Silica orvosi jegyzet generáláshoz és klinikai döntéstámogatáshoz
- OCR kézzel írt orvosi feljegyzések digitalizálásához
- Egyedi orvosi nyelvi modellek Windows ML-en keresztüli telepítése
- Helyi vektortár az orvosi tudás lekéréséhez

**Megvalósítási megközelítés:**
- Biztosítsa a teljes offline működést a betegadatok védelméhez
- Valósítson meg orvosi terminológia ellenőrzést és javaslatokat
- Adjon hozzá audit naplózást a szabályozási megfeleléshez
- Tervezze meg az integrációt meglévő Elektronikus Egészségügyi Nyilvántartó rendszerekkel

## Teljesítményoptimalizálási stratégiák

### Hardver-specifikus fejlesztés

**NPU optimalizálás**
- Tervezze meg az alkalmazásokat a Copilot+ PC-k NPU képességeinek kihasználására
- Valósítson meg szépen használható visszazuhanást GPU/CPU-ra NPU nélküli eszközökön
- Optimalizálja a modell formátumokat NPU-specifikus gyorsításhoz
- Figyelje az NPU kihasználtságot és termikus jellemzőket

**Memóriakezelés**
- Hatékony modell betöltési és gyorsítótárazási stratégiák megvalósítása
- Használjon memóriatérképezést nagy modellek indítási idejének csökkentésére
- Tervezzen memória-tudatos alkalmazásokat erőforráskorlátos eszközökre
- Alkalmazzon modell kvantálást a memóriaoptimalizálás érdekében

**Akkumulátorhatékonyság**
- Optimalizálja az AI műveleteket minimális fogyasztásra
- Valósítson meg adaptív feldolgozást az akkumulátor állapota alapján
- Tervezzen hatékony háttérfeldolgozást folyamatos AI műveletekhez
- Használjon energiafogyasztás profilozó eszközöket az optimalizáláshoz

### Skálázhatósági megfontolások

**Többszálúsítás**
- Tervezzen szál-biztos AI műveleteket párhuzamos feldolgozáshoz
- Valósítson meg hatékony munkamegosztást az elérhető magok között
- Használjon async/await mintákat nem blokkoló AI műveletekhez
- Tervezze meg a szálmedence optimalizációját különböző hardverkonfigurációkon

**Gyorsítótárazási stratégiák**
- Alkalmazzon intelligens gyorsítótárazást gyakran használt AI műveletekhez
- Tervezze meg a gyorsítótár érvénytelenítési stratégiákat modellfrissítésekhez
- Használjon tartós gyorsítótárazást költséges előfeldolgozási műveletekhez
- Valósítson meg elosztott gyorsítótárat több-felhasználós helyzetekben

## Biztonsági és adatvédelmi legjobb gyakorlatok

### Adatvédelem

**Helyi feldolgozás**
- Biztosítsa, hogy az érzékeny adatok soha ne hagyják el a helyi eszközt
- Alkalmazzon biztonságos tárolást AI modelleknek és ideiglenes adatoknak
- Használja a Windows biztonsági funkciókat az alkalmazásszabályozáshoz
- Alkalmazzon titkosítást a tárolt modellekhez és köztes feldolgozási eredményekhez

**Modellbiztonság**
- Érvényesítse a modell integritását betöltés előtt és végrehajtáskor
- Valósítson meg biztonságos modellfrissítési mechanizmusokat
- Használjon aláírt modelleket a manipuláció megelőzésére
- Alkalmazzon hozzáférés-kezelést a modell fájlokra és konfigurációra

### Megfelelőség megfontolások

**Szabályozási megfelelés**
- Tervezze meg az alkalmazásokat GDPR, HIPAA és más szabályozási követelmények szerint
- Valósítson meg audit naplózást az AI döntési folyamatokhoz
- Biztosítson átláthatósági funkciókat az AI által generált eredményekhez
- Tegye lehetővé a felhasználói irányítást az AI adatfeldolgozás felett

**Vállalati biztonság**
- Integráljon a Windows vállalati biztonsági szabályzataival
- Támogassa a menedzselt telepítést vállalati menedzsment eszközökkel
- Valósítson meg szerepalapú hozzáférés-vezérlést az AI funkciókhoz
- Biztosítson adminisztratív vezérlést az AI képességekhez

## Hibakeresés és hibaelhárítás

### Gyakori fejlesztési kihívások

**Build konfigurációs problémák**
- Biztosítsa az ARM64 platform konfigurációt a Windows AI API mintákhoz
- Ellenőrizze a Windows App SDK verzió kompatibilitást (1.8.1+ szükséges)
- Ellenőrizze a csomagazonosság helyes konfigurálását (szükséges a Windows AI API-hoz)
- Érvényesítse, hogy a build eszközök támogatják a célzott keretrendszer verziót

**Modell betöltési problémák**
- Érvényesítse az ONNX modell kompatibilitást a Windows ML-el
- Ellenőrizze a modell fájl integritását és formátumkövetelményeket
- Ellenőrizze a hardver képesség követelményeket specifikus modellekhez
- Hibakeresés a memória allokációs problémákra modell betöltéskor
- Biztosítsa a végrehajtási szolgáltató regisztrációját hardver gyorsításhoz

**Telepítési mód megfontolások**
- **Önálló mód**: Teljes támogatás, nagyobb telepítési mérettel
- **Keretrendszer függő mód**: Kisebb lábnyom, de megosztott futtatókörnyezet szükséges
- **Nem csomagolt alkalmazások**: Már nem támogatottak a Windows AI API számára
- Használja a `dotnet run -p:Platform=ARM64 -p:SelfContained=true` parancsot önálló ARM64 telepítéshez

**Teljesítmény problémák**
- Profilozza az alkalmazás teljesítményét különböző hardverkonfigurációkon
- Azonosítsa az AI feldolgozási lánc szűk keresztmetszeteit
- Optimalizálja az adat előfeldolgozási és utófeldolgozási lépéseket
- Valósítson meg teljesítményfigyelést és riasztást

**Integrációs nehézségek**
- Hibakeresés API integrációs problémák esetén megfelelő hibakezeléssel
- Érvényesítse a bemeneti adat formátumokat és előfeldolgozási követelményeket
- Alapos tesztelés szélsőséges esetekre és hibafeltételekre
- Valósítson meg átfogó naplózást a gyártási hibák hibakereséséhez

### Hibakeresési eszközök és technikák

**Visual Studio integráció**
- Használja az AI Toolkit hibakeresőt a modell végrehajtás elemzéséhez
- Valósítson meg teljesítmény profilozást AI műveletekhez
- Hibakeresés aszinkron AI műveletekhez megfelelő kivételkezeléssel
- Használjon memória profilozó eszközöket optimalizáláshoz

**Windows AI Foundry eszközök**
- Használja a Foundry Local CLI-t modell teszteléshez és érvényesítéshez
- Használja a Windows AI API tesztelő eszközöket integrációs ellenőrzésre
- Valósítson meg egyedi naplózást az AI működés megfigyeléséhez
- Készítsen automatizált tesztelést az AI funkciók megbízhatóságához

## Alkalmazását jövőbiztossá téve

### Felbukkanó technológiák

**Következő generációs hardverek**
- Tervezze az alkalmazásokat a jövőbeli NPU képességek kihasználására
- Készüljön fel növekvő modellméretekre és komplexitásra
- Valósítson meg adaptív architektúrákat a fejlődő hardverekhez
- Vegye figyelembe a kvantum-kompatibilis algoritmusokat a jövőbeni kompatibilitás érdekében

**Fejlett AI képességek**
- Készüljön multimodális AI integrációra több adattípus között
- Tervezze valós idejű együttműködésre több eszköz AI-ját
- Tervezze a federált tanulási képességeket
- Vegye figyelembe élszegmens-felhő hibrid intelligencia architektúrákat

### Folyamatos tanulás és alkalmazkodás

**Modell frissítések**
- Valósítson meg zökkenőmentes modellfrissítési mechanizmusokat
- Tervezzen olyan alkalmazásokat, melyek alkalmazkodnak a javított modellképességekhez
- Készüljön fel visszafelé kompatibilitásra meglévő modellekkel
- Valósítson meg A/B tesztelést a modell teljesítményének értékelésére

**Funkciófejlődés**
- Tervezzen moduláris architektúrákat, amelyek befogadják az új AI képességeket
- Készüljön fel az új Windows AI API-k integrációjára
- Valósítson meg funkció-kapcsolókat a képességek fokozatos bevezetéséhez
- Tervezzen felhasználói felületeket, amelyek alkalmazkodnak a fejlett AI funkciókhoz

## Összefoglalás

A Windows Edge AI fejlesztés a hatékony AI képességek és a robosztus, biztonságos, skálázható Windows platform találkozása. A Windows AI Foundry ökoszisztéma elsajátításával a fejlesztők intelligens alkalmazásokat hozhatnak létre, amelyek kivételes felhasználói élményt kínálnak, miközben a legmagasabb adatvédelmi, biztonsági és teljesítményi szabványokat tartják.

A Windows AI API-k, Foundry Local és Windows ML kombinációja páratlan alapot biztosít a következő generációs intelligens Windows alkalmazások építéséhez. Az AI fejlődésével a Windows platform biztosítja, hogy az alkalmazások alkalmazkodjanak a felbukkanó technológiákhoz, miközben kompatibilitást és teljesítményt tartanak fenn a sokszínű Windows hardverökoszisztémában.

Legyen szó fogyasztói alkalmazásokról, vállalati megoldásokról vagy speciális ipari eszközökről, a Windows Edge AI fejlesztés lehetővé teszi intelligens, reagáló és mélyen integrált élmények létrehozását, amelyek kiaknázják a modern Windows eszközök teljes potenciálját.

## További források

### Dokumentáció és tanulás
- [Windows AI Foundry dokumentáció](https://learn.microsoft.com/windows/ai/)
- [Windows AI API-k referencia](https://learn.microsoft.com/windows/ai/apis/)
- [Kezdje el az alkalmazásépítést Windows AI API-kkal](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local kezdőlépések](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML áttekintés](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK rendszerkövetelmények](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows App SDK Fejlesztői Környezet Beállítása](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Példa Tárolók és Kódok
- [Windows App SDK Példák - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Példák - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Következtetési Példák](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Példatár](https://github.com/microsoft/WindowsAppSDK-Samples)

### Fejlesztői Eszközök
- [AI Eszköztár a Visual Studio Code-hoz](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Fejlesztői Galéria](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Példák](https://learn.microsoft.com/windows/ai/samples/)
- [Modellkonvertáló Eszközök](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Műszaki Támogatás
- [Windows ML Dokumentáció](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentáció](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentáció](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Hibabejelentés - Windows App SDK Példák](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Közösség és Támogatás
- [Windows Fejlesztői Közösség](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Képzések](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ez az útmutató a gyorsan fejlődő Windows AI ökoszisztémával együtt fejlődik. A rendszeres frissítések biztosítják az összhangot a legújabb platform-képességekkel és fejlesztési legjobb gyakorlatokkal.*

[08. Gyakorlati Munka a Microsoft Foundry Local-lal - Teljes Fejlesztői Eszközkészlet](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->