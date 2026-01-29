# Modul 08: Gyakorlati munka a Microsoft Foundry Local eszközkészlettel

## Áttekintés

A [Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) az edge AI fejlesztés következő generációját képviseli, amely erőteljes eszközöket biztosít a fejlesztők számára AI alkalmazások helyi építéséhez, telepítéséhez és skálázásához, miközben zökkenőmentesen integrálódik az Azure AI Foundry-val. Ez a modul átfogó bemutatást nyújt a Foundry Local-ról, az installációtól kezdve a fejlett ügynökfejlesztésig.

**Kulcstechnológiák:**
- Microsoft Foundry Local CLI és SDK
- Azure AI Foundry integráció
- Eszközön történő modellkövetkeztetés
- Helyi modellgyorsítótár és optimalizálás
- Ügynök-alapú architektúrák

## Tanulási célok

A modul elvégzésével:

- **Elsajátítod a Foundry Local használatát**: Telepítés, konfigurálás és optimalizálás Windows 11 fejlesztéshez
- **Különféle modelleket telepítesz**: Phi, Qwen, Deepseek és GPT modellek futtatása helyben CLI parancsokkal
- **Termelési megoldásokat építesz**: AI alkalmazások létrehozása fejlett prompttervezéssel és adatintegrációval
- **Nyílt forráskódú ökoszisztéma használata**: Hugging Face modellek és közösségi hozzájárulások integrálása
- **AI ügynököket fejlesztesz**: Intelligens ügynökök építése alapozási és orkestrációs képességekkel
- **Vállalati minták megvalósítása**: Moduláris, skálázható AI megoldások létrehozása termelési telepítéshez

## Foglalkozások felépítése

### [1: Bevezetés a Foundry Local használatába](./01.FoundryLocalSetup.md)
**Fókusz**: Telepítés, CLI beállítás, modelltelepítés és hardveroptimalizálás

**Kulcstémák**: Teljes telepítés • CLI parancsok • Modellgyorsítótár • Hardvergyorsítás • Többmodell telepítés

**Minta**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK integráció](./samples/02/README.md) • [Modellfelfedezés és benchmarking](./samples/03/README.md)

**Időtartam**: 2-3 óra | **Szint**: Kezdő

---

### [2: AI megoldások építése az Azure AI Foundry-val](./02.AzureAIFoundryIntegration.md)
**Fókusz**: Fejlett prompttervezés, adatintegráció és felhőkapcsolat

**Kulcstémák**: Prompttervezés • Adatintegráció • Azure munkafolyamatok • Teljesítményoptimalizálás • Monitorozás

**Minta**: [Chainlit RAG alkalmazás](./samples/04/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [3: Nyílt forráskódú modellek Foundry Local-ban](./03.OpenSourceModels.md)
**Fókusz**: Hugging Face integráció, BYOM stratégiák és közösségi modellek

**Kulcstémák**: Hugging Face integráció • Saját modellek használata • Model Mondays betekintések • Közösségi hozzájárulások • Modellválasztás

**Minta**: [Többügynökös orkestráció](./samples/05/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [4: Legmodernebb modellek felfedezése](./04.CuttingEdgeModels.md)
**Fókusz**: LLM-ek vs SLM-ek, EdgeAI megvalósítás és fejlett demók

**Kulcstémák**: Modellösszehasonlítás • Edge vs felhő következtetés • Phi + ONNX Runtime • Chainlit RAG alkalmazás • WebGPU optimalizálás

**Minta**: [Models-as-Tools Router](./samples/06/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [5: AI-alapú ügynökök gyors építése](./05.AIPoweredAgents.md)
**Fókusz**: Ügynökarchitektúrák, rendszerpromptok, alapozás és orkestráció

**Kulcstémák**: Ügynöktervezési minták • Rendszerprompttervezés • Alapozási technikák • Többügynökös rendszerek • Termelési telepítés

**Minta**: [Többügynökös orkestráció](./samples/05/README.md) • [Fejlett többügynökös rendszer](./samples/09/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [6: Foundry Local - Modellek mint eszközök](./06.ModelsAsTools.md)
**Fókusz**: Moduláris AI megoldások, vállalati skálázás és termelési minták

**Kulcstémák**: Modellek mint eszközök • Eszközön történő telepítés • SDK/API integráció • Vállalati architektúrák • Skálázási stratégiák

**Minta**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Időtartam**: 3-4 óra | **Szint**: Szakértő

---

### [7: Közvetlen API integrációs minták](./samples/07/README.md)
**Fókusz**: Tiszta REST API integráció SDK függőségek nélkül a maximális kontroll érdekében

**Kulcstémák**: HTTP kliens megvalósítás • Egyedi hitelesítés • Modell egészségmonitorozás • Streaming válaszok • Termelési hibakezelés

**Minta**: [Közvetlen API kliens](./samples/07/README.md)

**Időtartam**: 2-3 óra | **Szint**: Középhaladó

---

### [8: Windows 11 natív chat alkalmazás](./samples/08/README.md)
**Fókusz**: Modern natív chat alkalmazások építése Foundry Local integrációval

**Kulcstémák**: Electron fejlesztés • Fluent Design System • Natív Windows integráció • Valós idejű streaming • Chat interfész tervezés

**Minta**: [Windows 11 Chat alkalmazás](./samples/08/README.md)

**Időtartam**: 3-4 óra | **Szint**: Haladó

---

### [9: Fejlett többügynökös orkestráció](./samples/09/README.md)
**Fókusz**: Összetett ügynökkoordináció, specializált feladatdelegálás és együttműködő AI munkafolyamatok

**Kulcstémák**: Intelligens ügynökkoordináció • Funkcióhívási minták • Ügynökök közötti kommunikáció • Munkafolyamat-orkestráció • Minőségbiztosítási mechanizmusok

**Minta**: [Fejlett többügynökös rendszer](./samples/09/README.md)

**Időtartam**: 4-5 óra | **Szint**: Szakértő

---

### [10: Foundry Local mint eszközkeretrendszer](./samples/10/README.md)
**Fókusz**: Eszköz-alapú architektúra a Foundry Local meglévő alkalmazásokba és keretrendszerekbe való integrálásához

**Kulcstémák**: LangChain integráció • Semantic Kernel funkciók • REST API keretrendszerek • CLI eszközök • Jupyter integráció • Termelési telepítési minták

**Minta**: [Foundry Tools Framework](./samples/10/README.md)

**Időtartam**: 4-5 óra | **Szint**: Szakértő

## Előfeltételek

### Rendszerkövetelmények
- **Operációs rendszer**: Windows 11 (22H2 vagy újabb)
- **Memória**: 16GB RAM (32GB ajánlott nagyobb modellekhez)
- **Tárhely**: 50GB szabad hely modellgyorsítótárhoz
- **Hardver**: NPU-val ellátott eszköz ajánlott (Copilot+ PC), GPU opcionális
- **Hálózat**: Nagy sebességű internet az első modellletöltésekhez

### Fejlesztési környezet
- Visual Studio Code AI Toolkit bővítménnyel
- Python 3.10+ és pip
- Git verziókezeléshez
- PowerShell vagy Command Prompt
- Azure CLI (opcionális felhőintegrációhoz)

### Tudás előfeltételek
- AI/ML alapfogalmak alapvető ismerete
- Parancssoros ismeretek
- Python programozási alapok
- REST API fogalmak
- Prompttervezés és modellkövetkeztetés alapvető ismerete

## Modul idővonala

**Teljes becsült idő**: 30-38 óra

| Foglalkozás | Fókuszterület | Minták | Idő | Bonyolultság |
|-------------|---------------|--------|-----|--------------|
|  1 | Telepítés és alapok | 01, 02, 03 | 2-3 óra | Kezdő |
|  2 | AI megoldások | 04 | 2-3 óra | Középhaladó |
|  3 | Nyílt forráskód | 05 | 2-3 óra | Középhaladó |
|  4 | Fejlett modellek | 06 | 3-4 óra | Haladó |
|  5 | AI ügynökök | 05, 09 | 3-4 óra | Haladó |
|  6 | Vállalati eszközök | 06, 10 | 3-4 óra | Szakértő |
|  7 | Közvetlen API integráció | 07 | 2-3 óra | Középhaladó |
|  8 | Windows 11 chat alkalmazás | 08 | 3-4 óra | Haladó |
|  9 | Fejlett többügynökös | 09 | 4-5 óra | Szakértő |
| 10 | Eszközkeretrendszer | 10 | 4-5 óra | Szakértő |

## Kulcsfontosságú források

**Hivatalos dokumentáció:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Forráskód és hivatalos minták
- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Teljes telepítési és használati útmutató
- [Model Mondays sorozat](https://aka.ms/model-mondays) - Heti modellbemutatók és oktatóanyagok

**Közösség és támogatás:**
- [Foundry Local viták](https://github.com/microsoft/Foundry-Local/discussions) - Közösségi kérdések és funkciókérések
- [Microsoft AI fejlesztői közösség](https://techcommunity.microsoft.com/category/artificialintelligence) - Legfrissebb hírek és legjobb gyakorlatok

## Tanulási eredmények

A modul elvégzésével képes leszel:

### Technikai jártasság
- **Telepítés és kezelés**: Foundry Local telepítése és kezelése fejlesztési és termelési környezetekben
- **Modellek integrálása**: Különféle modellcsaládok zökkenőmentes használata Microsofttól, Hugging Face-től és közösségi forrásokból
- **Alkalmazások építése**: Termelésre kész AI alkalmazások létrehozása fejlett funkciókkal és optimalizálásokkal
- **Ügynökök fejlesztése**: Összetett AI ügynökök megvalósítása alapozással, érveléssel és eszközintegrációval

### Stratégiai megértés
- **Architektúra döntések**: Tájékozott választás helyi és felhő telepítés között
- **Teljesítményoptimalizálás**: Következtetési teljesítmény optimalizálása különböző hardverkonfigurációkban
- **Vállalati skálázás**: Alkalmazások tervezése, amelyek helyi prototípusoktól vállalati telepítésekig skálázhatók
- **Adatvédelem és biztonság**: Adatvédelmet biztosító AI megoldások megvalósítása helyi következtetéssel

### Innovációs képességek
- **Gyors prototípusépítés**: AI alkalmazás koncepciók gyors építése és tesztelése mind a 10 mintázat alapján
- **Közösségi integráció**: Nyílt forráskódú modellek használata és hozzájárulás az ökoszisztémához
- **Fejlett minták**: Legmodernebb AI minták megvalósítása, beleértve a RAG-et, ügynököket és eszközintegrációt
- **Keretrendszer jártasság**: Szakértő szintű integráció LangChain, Semantic Kernel, Chainlit és Electron eszközökkel
- **Termelési telepítés**: Skálázható AI megoldások telepítése helyi prototípusoktól vállalati rendszerekig
- **Jövőálló fejlesztés**: Alkalmazások építése, amelyek készen állnak a feltörekvő AI technológiákra és mintákra

## Kezdés

1. **Környezet beállítása**: Biztosítsd a Windows 11-et az ajánlott hardverrel (lásd: Előfeltételek)
2. **Foundry Local telepítése**: Kövesd az 1. foglalkozást a teljes telepítéshez és konfigurációhoz
3. **Futtasd az 01-es mintát**: Kezdd az alapvető REST API integrációval a beállítás ellenőrzéséhez
4. **Haladj végig a mintákon**: Teljesítsd az 01-10 mintákat az átfogó jártasság érdekében

## Sikerességi mutatók

Kövesd nyomon a haladásodat mind a 10 átfogó mintán keresztül:

### Alapozási szint (Minták 01-03)
- [ ] Sikeresen telepítetted és konfiguráltad a Foundry Local-t
- [ ] REST API integráció befejezése (01-es minta)
- [ ] OpenAI SDK kompatibilitás megvalósítása (02-es minta)
- [ ] Modellfelfedezés és benchmarking végrehajtása (03-as minta)

### Alkalmazási szint (Minták 04-06)
- [ ] Legalább 4 különböző modellcsalád telepítése és futtatása
- [ ] Funkcionális RAG chat alkalmazás építése (04-es minta)
- [ ] Többügynökös orkestrációs rendszer létrehozása (05-ös minta)
- [ ] Intelligens modellirányító megvalósítása (06-os minta)

### Fejlett integrációs szint (Minták 07-10)
- [ ] Termelésre kész API kliens építése (07-es minta)
- [ ] Windows 11 natív chat alkalmazás fejlesztése (08-as minta)
- [ ] Fejlett többügynökös rendszer megvalósítása (09-es minta)
- [ ] Átfogó eszközkeretrendszer létrehozása (10-es minta)

### Jártassági mutatók
- [ ] Mind a 10 minta hibamentes futtatása
- [ ] Legalább 3 minta testreszabása specifikus felhasználási esetekhez
- [ ] 2+ minta telepítése termelési környezetben
- [ ] Javítások vagy bővítések hozzájárulása a mintakódhoz
- [ ] Foundry Local minták integrálása személyes/professzionális projektekbe

## Gyors kezdési útmutató - Mind a 10 minta

### Környezet beállítása (Minden mintához szükséges)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Alapozási minták (01-06)

**01-es minta: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**02-es minta: OpenAI SDK integráció**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**03-as minta: Modellfelfedezés és benchmarking
Ez a modul az élvonalbeli edge AI fejlesztést képviseli, ötvözve a Microsoft vállalati szintű eszközeit az open-source ökoszisztéma rugalmasságával és innovációjával. Ha elsajátítod a Foundry Local használatát mind a 10 átfogó mintán keresztül, az AI alkalmazásfejlesztés élvonalába kerülsz.

**Teljes tanulási útvonal:**
- **Alapok** (Minták 01-03): API integráció és modellkezelés
- **Alkalmazások** (Minták 04-06): RAG, ügynökök és intelligens útvonaltervezés
- **Haladó** (Minták 07-10): Gyártási keretrendszerek és vállalati integráció

Az Azure OpenAI integrációhoz (2. szekció) tekintsd meg az egyes minták README fájljait a szükséges környezeti változók és API verzió beállítások érdekében.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.