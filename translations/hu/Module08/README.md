# Modul 08: Gyakorlati munka a Microsoft Foundry Local-lal - Teljes fejlesztői eszköztár

## Áttekintés

A [Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) az él AI fejlesztés következő generációját képviseli, amely erőteljes eszközöket biztosít a fejlesztőknek AI alkalmazások helyi fejlesztésére, telepítésére és skálázására, miközben zökkenőmentes integrációt tesz lehetővé az Azure AI Foundry-val. Ez a modul átfogó lefedést nyújt a Foundry Localról a telepítéstől az előrehaladott ügynökfejlesztésig.

**Fő technológiák:**
- Microsoft Foundry Local CLI és SDK
- Azure AI Foundry integráció
- Eszközön történő modell következtetés
- Helyi modell gyorsítótárazás és optimalizáció
- Ügynökalapú architektúrák

## Tanulási célok

Ennek a modulnak a teljesítésével:

- **Elsajátítod a Foundry Localt**: Telepítés, konfigurálás és optimalizálás Windows 11 fejlesztéshez
- **Különböző modellek telepítése**: Phi, qwen, deepseek és GPT modellek helyi futtatása CLI parancsokkal
- **Termelési megoldások építése**: AI alkalmazások létrehozása fejlett prompt tervezéssel és adat integrációval
- **Nyílt forráskódú ökoszisztéma kihasználása**: Hugging Face modellek és közösségi hozzájárulások integrálása
- **AI ügynökök fejlesztése**: Intelligens ügynökök építése groundinggel és összehangolási képességekkel
- **Vállalati minták megvalósítása**: Moduláris, skálázható AI megoldások létrehozása termelési telepítésre

## Ülés felépítése

### [1: Foundry Local kezdő lépések](./01.FoundryLocalSetup.md)
**Fókusz**: Telepítés, CLI beállítás, modell telepítés, hardver optimalizáció

**Fő témák**: Teljes telepítés • CLI parancsok • Modell gyorsítótárazás • Hardver gyorsítás • Több modell egyidejű telepítése

**Minta**: [REST Chat Gyorsindítás](./samples/01/README.md) • [OpenAI SDK integráció](./samples/02/README.md) • [Modell felfedezés és benchmark](./samples/03/README.md)

**Időtartam**: 2-3 óra | **Szint**: Kezdő

---

### [2: AI megoldások építése az Azure AI Foundry-val](./02.AzureAIFoundryIntegration.md)
**Fókusz**: Fejlett prompt tervezés, adat integráció, és felhőkapcsolat

**Fő témák**: Prompt tervezés • Adat integráció • Azure munkafolyamatok • Teljesítmény optimalizálás • Figyelés

**Minta**: [Chainlit RAG alkalmazás](./samples/04/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [3: Nyílt forráskódú modellek Foundry Localon](./03.OpenSourceModels.md)
**Fókusz**: Hugging Face integráció, BYOM stratégiák, és közösségi modellek

**Fő témák**: HuggingFace integráció • Saját modell behozatala • Model Mondays betekintők • Közösségi hozzájárulások • Modell kiválasztás

**Minta**: [Többügynökös összehangolás](./samples/05/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [4: Vágóél Modellek felfedezése](./04.CuttingEdgeModels.md)
**Fókusz**: LLM-ek vs SLM-ek, EdgeAI megvalósítás, és fejlett demók

**Fő témák**: Modell összehasonlítás • Edge vs felhő következtetés • Phi + ONNX Runtime • Chainlit RAG alkalmazás • WebGPU optimalizáció

**Minta**: [Modellek eszközként router](./samples/06/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [5: Gyors AI-vezérelt ügynökök építése](./05.AIPoweredAgents.md)
**Fókusz**: Ügynök architektúrák, rendszer promptok, grounding és összehangolás

**Fő témák**: Ügynök tervezési minták • Rendszer prompt tervezés • Grounding technikák • Többügynökös rendszerek • Termelési telepítés

**Minta**: [Többügynökös összehangolás](./samples/05/README.md) • [Fejlett többügynökös rendszer](./samples/09/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [6: Foundry Local - Modellek eszközként](./06.ModelsAsTools.md)
**Fókusz**: Moduláris AI megoldások, vállalati skálázás, és termelési minták

**Fő témák**: Modellek eszközként • Eszközön telepítés • SDK/API integráció • Vállalati architektúrák • Skálázási stratégiák

**Minta**: [Modellek eszközként router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Időtartam**: 3-4 óra | **Szint**: Szakértő

---

### [7: Közvetlen API Integrációs Minták](./samples/07/README.md)
**Fókusz**: Tiszta REST API integráció SDK függőségek nélkül a maximális kontroll érdekében

**Fő témák**: HTTP kliens megvalósítás • Egyedi hitelesítés • Modell egészség ellenőrzés • Streaming válaszok • Hibakezelés termelésben

**Minta**: [Közvetlen API kliens](./samples/07/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [8: Windows 11 natív csevegőalkalmazás](./samples/08/README.md)
**Fókusz**: Modern natív csevegőalkalmazások építése Foundry Local integrációval

**Fő témák**: Electron fejlesztés • Fluent Design Rendszer • Natív Windows integráció • Valós idejű streaming • Csevegő felület tervezés

**Minta**: [Windows 11 csevegőalkalmazás](./samples/08/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [9: Fejlett többügynökös összehangolás](./samples/09/README.md)
**Fókusz**: Összetett ügynök koordináció, speciális feladatdelegálás, és együttműködő AI munkafolyamatok

**Fő témák**: Intelligens ügynök koordináció • Funkcióhívási minták • Ügynökök közötti kommunikáció • Munkafolyamat irányítás • Minőségbiztosítási mechanizmusok

**Minta**: [Fejlett többügynökös rendszer](./samples/09/README.md)

**Időtartam**: 4-5 óra | **Szint**: Szakértő

---

### [10: Foundry Local eszköz keretrendszerként](./samples/10/README.md)
**Fókusz**: Eszköz-előnyös architektúra a Foundry Local meglévő alkalmazásokba és keretrendszerekbe való integrálásához

**Fő témák**: LangChain integráció • Semantic Kernel funkciók • REST API keretrendszerek • CLI eszközök • Jupyter integráció • Termelési telepítési minták

**Minta**: [Foundry Tools Framework](./samples/10/README.md)

**Időtartam**: 4-5 óra | **Szint**: Szakértő

## Előfeltételek

### Rendszerkövetelmények
- **Operációs rendszer**: Windows 11 (22H2 vagy újabb)
- **Memória**: 16GB RAM (nagyobb modellekhez 32GB ajánlott)
- **Tároló**: 50GB szabad hely modell gyorsítótárazáshoz
- **Hardver**: NPU-támogatott eszköz ajánlott (Copilot+ PC), GPU opcionális
- **Hálózat**: Nagysebességű internet az első modell letöltéséhez

### Fejlesztői környezet
- Visual Studio Code AI Toolkit kiterjesztéssel
- Python 3.10+ és pip
- Git verziókezeléshez
- PowerShell vagy Parancssor
- Azure CLI (opcionális a felhő integrációhoz)

### Tudáselőfeltételek
- AI/ML alapfogalmak ismerete
- Parancssoros ismeretek
- Python programozási alapok
- REST API fogalmak
- Promptolás és modell következtetés alapjai

## Modul idővonal

**Összes becsült idő**: 30-38 óra

| Ülés | Fókuszterület | Minták | Idő | Nehézség |
|---------|------------|---------|------|------------|
|  1 | Beállítások és alapok | 01, 02, 03 | 2-3 óra | Kezdő |
|  2 | AI megoldások | 04 | 2-3 óra | Középhaladó |
|  3 | Nyílt forrás | 05 | 2-3 óra | Középhaladó |
|  4 | Fejlett modellek | 06 | 3-4 óra | Haladó |
|  5 | AI ügynökök | 05, 09 | 3-4 óra | Haladó |
|  6 | Vállalati eszközök | 06, 10 | 3-4 óra | Szakértő |
|  7 | Közvetlen API integráció | 07 | 2-3 óra | Középhaladó |
|  8 | Windows 11 csevegőalkalmazás | 08 | 3-4 óra | Haladó |
|  9 | Fejlett többügynökös rendszer | 09 | 4-5 óra | Szakértő |
| 10 | Eszköz keretrendszer | 10 | 4-5 óra | Szakértő |

## Fő források

**Hivatalos dokumentáció:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Forráskód és hivatalos minták
- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Teljes telepítési és használati útmutató
- [Model Mondays sorozat](https://aka.ms/model-mondays) - Heti modell kiemelések és oktatóanyagok

**Közösség és támogatás:**
- [Foundry Local viták](https://github.com/microsoft/Foundry-Local/discussions) - Közösségi kérdések és funkció kérések
- [Microsoft AI fejlesztői közösség](https://techcommunity.microsoft.com/category/artificialintelligence) - Legfrissebb hírek és legjobb gyakorlatok

## Tanulási eredmények

A modul teljesítése után képes leszel:

### Műszaki jártasság
- **Telepíteni és kezelni**: Foundry Local telepítéseket fejlesztési és termelési környezetekben
- **Modelleket integrálni**: Zökkenőmentesen dolgozni különféle model családokkal, beleértve Microsoft, Hugging Face és közösségi forrásokat
- **Alkalmazásokat építeni**: Termelésre kész AI alkalmazások létrehozása fejlett funkciókkal és optimalizációkkal
- **Ügynököket fejleszteni**: Kifinomult AI ügynököket megvalósítani grounding, érvelés és eszköz integrációval

### Stratégiai megértés
- **Architektúra döntések**: Megfontolt választások helyi vs felhőben történő telepítés között
- **Teljesítmény optimalizálás**: Következtetési teljesítmény optimalizálása különböző hardver konfigurációkon
- **Vállalati skálázás**: Alkalmazásokat tervezni, amelyek helyi prototípusoktól vállalati telepítésekig skálázhatók
- **Adatvédelem és biztonság**: Adatvédelmet biztosító AI megoldásokat megvalósítani helyi következtetéssel

### Innovációs képességek
- **Gyors prototípus készítés**: Gyorsan építeni és tesztelni AI alkalmazás koncepciókat mind a 10 mintaminta alapján
- **Közösségi integráció**: Nyílt forrású modelleket használni és hozzájárulni az ökoszisztémához
- **Fejlett minták**: Élvonalbeli AI mintákat megvalósítani, beleértve RAG, ügynökök és eszköz integrációt
- **Keretrendszer szakértelem**: Szakértői szintű integráció LangChain, Semantic Kernel, Chainlit és Electron eszközökkel
- **Termelési telepítés**: Skálázható AI megoldásokat telepíteni helyi prototípusoktól vállalati rendszerekig
- **Jövőálló fejlesztés**: Alkalmazásokat építeni, amelyek készen állnak az új AI technológiákra és mintákra

## Kezdés

1. **Környezet beállítása**: Biztosítani Windows 11 rendszert ajánlott hardverrel (lásd Előfeltételek)
2. **Foundry Local telepítése**: Kövesd az 1. ülés lépéseit a teljes telepítéshez és konfigurációhoz
3. **Mintapélda 01 futtatása**: Kezdj az alap REST API integrációval a beállítás ellenőrzéséhez
4. **Minták végigvezetése**: Teljesítsd a 01-10 mintákat, hogy átfogó jártasságot szerezz

## Siker mutatók

Kövesd a haladásodat a 10 átfogó mintán keresztül:

### Alapfokú szint (Minták 01-03)
- [ ] Sikeresen telepíteni és konfigurálni a Foundry Localt
- [ ] REST API integráció befejezése (Minta 01)
- [ ] OpenAI SDK kompatibilitás megvalósítása (Minta 02)
- [ ] Modell felfedezés és benchmarking elvégzése (Minta 03)

### Alkalmazási szint (Minták 04-06)
- [ ] Legalább 4 különböző modell család telepítése és futtatása
- [ ] Funkcionális RAG csevegőalkalmazás építése (Minta 04)
- [ ] Többügynökös összehangolási rendszer létrehozása (Minta 05)
- [ ] Intelligens modell irányítás megvalósítása (Minta 06)

### Fejlett integrációs szint (Minták 07-10)
- [ ] Termelésre kész API kliens építése (Minta 07)
- [ ] Windows 11 natív csevegőalkalmazás fejlesztése (Minta 08)
- [ ] Fejlett többügynökös rendszer implementálása (Minta 09)
- [ ] Átfogó eszköz keretrendszer létrehozása (Minta 10)

### Jártassági mutatók
- [ ] Sikeres futtatás minden 10 mintán hibák nélkül
- [ ] Legalább 3 minta testreszabása specifikus felhasználási esetekhez
- [ ] 2+ minta telepítése termelés-szerű környezetekben
- [ ] Fejlesztések vagy bővítések hozzájárulása a mintakódhoz
- [ ] Foundry Local minták integrálása személyes/professzionális projektekbe

## Gyors kezdési útmutató - Mind a 10 minta

### Környezet beállítása (kötelező minden mintához)

```powershell
# 1. Klónozd és navigálj a Module08 mappába
cd Module08

# 2. Hozz létre Python virtuális környezetet
py -m venv .venv
.\.venv\Scripts\activate

# 3. Telepítsd az alapvető függőségeket
pip install -r requirements.txt

# 4. Telepítsd a Foundry Local-t (ha még nincs telepítve)
winget install Microsoft.FoundryLocal

# 5. Ellenőrizd a Foundry Local telepítését
foundry --version
foundry model list
```

### Alap Foundation minták (01-06)

**Minta 01: REST Chat Gyorsindítás**
```powershell
# Foundry helyi szolgáltatás indítása
foundry model run phi-4-mini

# REST chat demó futtatása
python samples/01/chat_quickstart.py
```

**Minta 02: OpenAI SDK integráció**
```powershell
# Győződjön meg róla, hogy a modell fut
foundry status

# Futtassa az SDK demót
python samples/02/sdk_quickstart.py
```

**Minta 03: Modell felfedezés és benchmarking**
```powershell
# Futtass átfogó modellesztést
samples/03/list_and_bench.cmd

# Vagy futtass egyéni komponenseket
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Minta 04: Chainlit RAG alkalmazás**
```powershell
# Chainlit függőségek telepítése
pip install chainlit langchain chromadb

# RAG chat alkalmazás indítása
chainlit run samples/04/app.py -w
# Böngésző megnyitása a http://localhost:8000 címen
```

**Minta 05: Többügynökös összehangolás**
```powershell
# Ügynök koordinátor demó futtatása
python -m samples.05.agents.coordinator

# Specifikus ügynök példák futtatása
python samples/05/examples/specialists_demo.py
```

**Minta 06: Modellek eszközként router**
```powershell
# Környezet beállítása
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Intelligens útválasztó futtatása
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Fejlett integrációs minták (07-10)

**Minta 07: Közvetlen API kliens**
```powershell
# Navigáljon a minta könyvtárba
cd samples/07

# Telepítse a további függőségeket
pip install -r requirements.txt

# Futtassa az alap API példákat
python examples/basic_usage.py

# Próbálja ki az adatfolyam-válaszokat
python examples/streaming.py

# Tesztelje a gyártási mintákat
python examples/production.py
```

**Minta 08: Windows 11 csevegőalkalmazás**
```powershell
# Navigálás a minta könyvtárba
cd samples/08

# Node.js függőségek telepítése
npm install

# Electron alkalmazás indítása
npm start

# Vagy építés éles környezethez
npm run build
```

**Minta 09: Fejlett többügynökös rendszer**
```powershell
# Navigálás a mintakönyvtárba
cd samples/09

# Ügynök rendszerfüggőségeinek telepítése
pip install -r requirements.txt

# Alapvető koordinációs példa futtatása
python examples/basic_coordination.py

# Összetett munkafolyamat kipróbálása
python examples/complex_workflow.py

# Interaktív ügynök demó
python examples/interactive_demo.py
```

**Minta 10: Foundry eszköz keretrendszer**
```powershell
# Navigáljon a minta könyvtárba
cd samples/10

# Telepítse a keretrendszer függőségeit
pip install -r requirements.txt

# Futtassa az alapvető eszközök bemutatóját
python examples/basic_tools.py

# Indítsa el a REST API szervert
python examples/rest_api_server.py
# Az API elérhető a http://localhost:8080 címen

# Próbálja ki a CLI alkalmazást
python examples/cli_application.py --help

# Indítsa el a Jupyter jegyzetfüzetet
jupyter notebook examples/jupyter_notebook.ipynb

# Tesztelje a LangChain integrációt
python examples/langchain_demo.py
```

### Gyakori problémák elhárítása

**Foundry Local kapcsolódási hibák**
```powershell
# Szolgáltatás állapotának ellenőrzése
foundry status

# Újraindítás szükség esetén
foundry restart

# Végpont elérhetőségének ellenőrzése
curl http://localhost:5273/v1/models
```

**Modell betöltési problémák**
```powershell
# Ellenőrizze az elérhető modelleket
foundry model list --cached

# Töltse le a hiányzó modelleket
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Szükség esetén kényszerített újratöltés
foundry model unload --all
foundry model run phi-4-mini
```

**Függőségi problémák**
```powershell
# Pip frissítése és újratelepítése
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Node.js példákhoz
npm cache clean --force
npm install
```

## Összefoglaló


Ez a modul az élvonalbeli edge AI fejlesztést képviseli, ötvözve a Microsoft vállalati szintű eszközeit az open-source ökoszisztéma rugalmasságával és innovációjával. A Foundry Local mind a 10 átfogó mintájának elsajátításával az AI alkalmazásfejlesztés élvonalában helyezkedhetsz el.

**Teljes tanulási út:**
- **Alapok** (01-03 minta): API integráció és modellkezelés
- **Alkalmazások** (04-06 minta): RAG, ügynökök és intelligens útválasztás
- **Fejlett** (07-10 minta): Termelési keretrendszerek és vállalati integráció

Az Azure OpenAI integrációhoz (2. alkalom) lásd az egyes minták README fájljait a szükséges környezeti változók és API verzió beállítások miatt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->