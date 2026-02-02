# EdgeAI kezdőknek 


![Course cover image](../../translated_images/hu/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kövesse ezeket a lépéseket, hogy elkezdje használni ezeket az erőforrásokat:

1. **Repository forkolása**: Kattintson a [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork) gombra
2. **Repository klónozása**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Csatlakozás az Azure AI Foundry Discordhoz, hogy találkozzon szakértőkkel és fejlesztőtársaival**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Többnyelvű támogatás

#### GitHub Action által támogatott (Automatikus és Mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](./README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Inkább helyileg szeretnéd klónozni?**

> Ez a repository több mint 50 nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. Ha fordítások nélkül szeretnéd klónozni, használd a sparse checkout-ot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ez mindent megad, amire a kurzus elvégzéséhez szükséged van, sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ha további nyelvi támogatást szeretnél, a támogatott nyelvek listája megtalálható [itt](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Bevezetés

Üdvözlünk a **EdgeAI kezdőknek** kurzuson – az átfogó utadon az Edge Mesterséges Intelligencia átalakító világába. Ez a tanfolyam áthidalja az erőteljes MI képességek és a gyakorlati, valós világban történő élőhelyi eszközökre történő telepítés közötti szakadékot, lehetővé téve számodra, hogy közvetlenül ott használd az MI lehetőségeit, ahol az adat keletkezik és a döntéseket meg kell hozni.

### Mit sajátíthatsz el

Ez a tanfolyam az alapfogalmaktól vezet el a gyártásra kész megvalósításokig, beleértve:
- **Kis Nyelvi Modellek (SLM-ek)**, amelyek az edge telepítéshez vannak optimalizálva
- **Hardver-tudatos optimalizáció** különböző platformokon
- **Valós idejű következtetés** adatvédelmi képességekkel
- **Gyártási telepítési** stratégiák vállalati alkalmazásokhoz

### Miért fontos az EdgeAI

Az Edge AI paradigmaváltást jelent, amely a modern kritikus kihívásokat kezeli:
- **Adatvédelem és biztonság**: Érzékeny adatokat kezel helyileg, cloud kitettség nélkül
- **Valós idejű teljesítmény**: Hálózati késleltetés kiküszöbölése időkritikus alkalmazásokhoz
- **Költséghatékonyság**: Csökkenti a sávszélesség és felhőszámítás költségeit
- **Ellenálló működés**: Funkcionalitás fenntartása hálózati kiesések esetén is
- **Szabályozási megfelelés**: Adat-szuverenitási előírások betartása

### Edge AI

Az Edge AI azt jelenti, hogy MI algoritmusokat és nyelvi modelleket helyben, a hardveren futtatunk, közel az adatok keletkezési helyéhez, felhőforrások használata nélkül az inferencia során. Csökkenti a késleltetést, növeli az adatvédelmet és lehetővé teszi a valós idejű döntéshozatalt.

### Alapelvek:
- **Helyi inferencia**: MI modellek futtatása edge eszközökön (telefonok, routerek, mikrokontrollerek, ipari számítógépek)
- **Offline képesség**: Internetkapcsolat nélkül is működik
- **Alacsony késleltetés**: Azonnali válaszok valós idejű rendszerekhez
- **Adatszuverenitás**: Érzékeny adatok helyben tartása, ezáltal növelve a biztonságot és megfelelést

### Kis Nyelvi Modellek (SLM-ek)

Az olyan SLM-ek, mint Phi-4, Mistral-7B és Gemma, optimalizált nagyobb LLM-ek változatai—kiképzettek vagy letisztítottak a következőkre:
- **Csökkentett memóriaigény**: Hatékony használat a korlátozott edge eszköz memóriából
- **Alacsonyabb számítási igény**: CPU és edge GPU teljesítményre optimalizálva
- **Gyorsabb indítási idő**: Gyors inicializáció a reszponzív alkalmazásokhoz

Lehetővé teszik az erőteljes NLP képességeket miközben megfelelnek az alábbi korlátoknak:
- **Beágyazott rendszerek**: IoT eszközök és ipari vezérlők
- **Mobil eszközök**: Okostelefonok és tabletek offline képességekkel
- **IoT eszközök**: Érzékelők és okoseszközök korlátozott erőforrásokkal
- **Edge szerverek**: Helyi feldolgozó egységek korlátozott GPU erőforrásokkal
- **Személyi számítógépek**: Asztali és laptop telepítési forgatókönyvek

## Tanfolyam modulok és navigáció

| Modul | Téma | Fókuszterület | Kulcstartalom | Szint | Időtartam |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Bevezetés az EdgeAI-be](./introduction.md) | Alapok és kontextus | EdgeAI áttekintés • Ipari alkalmazások • SLM bemutatása • Tanulási célok | Kezdő | 1-2 óra |
| [📚 01](../../Module01) | [EdgeAI alapjai](./Module01/README.md) | Felhő- és Edge AI összehasonlítás | EdgeAI alapok • Valós esettanulmányok • Megvalósítási útmutató • Edge telepítés | Kezdő | 3-4 óra |
| [🧠 02](../../Module02) | [SLM modellalapok](./Module02/README.md) | Modellcsaládok és architektúra | Phi család • Qwen család • Gemma család • BitNET • μModel • Phi-Silica | Kezdő | 4-5 óra |
| [🚀 03](../../Module03) | [SLM telepítési gyakorlat](./Module03/README.md) | Helyi és felhő alapú telepítés | Haladó tanulás • Helyi környezet • Felhő telepítés | Középhaladó | 4-5 óra |
| [⚙️ 04](../../Module04) | [Model optimalizációs eszköztár](./Module04/README.md) | Többplatformos optimalizáció | Bevezetés • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Munkafolyamat szintézis | Középhaladó | 5-6 óra |
| [🔧 05](../../Module05) | [SLMOps gyártási működés](./Module05/README.md) | Gyártási operációk | SLMOps bevezetés • Modell desztilláció • Finomhangolás • Gyártási telepítés | Haladó | 5-6 óra |
| [🤖 06](../../Module06) | [MI ügynökök és függvényhívás](./Module06/README.md) | Ügynök keretrendszerek és MCP | Ügynök bevezetés • Függvényhívás • Modell kontextus protokoll | Haladó | 4-5 óra |
| [💻 07](../../Module07) | [Platform megvalósítás](./Module07/README.md) | Többplatformos minták | MI eszközkészlet • Foundry Local • Windows fejlesztés | Haladó | 3-4 óra |
| [🏭 08](../../Module08) | [Foundry Local eszköztár](./Module08/README.md) | Gyártásra kész minták | Mintaalkalmazások (lásd lejjebb részletezve) | Szakértő | 8-10 óra |

### 🏭 **8. modul: Mintaalkalmazások**

- [01: REST Chat gyors kezdés](./Module08/samples/01/README.md)
- [02: OpenAI SDK integráció](./Module08/samples/02/README.md)
- [03: Modell felfedezés és teljesítményteszt](./Module08/samples/03/README.md)
- [04: Chainlit RAG alkalmazás](./Module08/samples/04/README.md)
- [05: Több-ügynökös összehangolás](./Module08/samples/05/README.md)
- [06: Modellek eszközként router](./Module08/samples/06/README.md)
- [07: Közvetlen API kliens](./Module08/samples/07/README.md)
- [08: Windows 11 Chat alkalmazás](./Module08/samples/08/README.md)
- [09: Fejlett több-ügynökös rendszer](./Module08/samples/09/README.md)
- [10: Foundry eszköz keretrendszer](./Module08/samples/10/README.md)

### 🎓 **Workshop: Gyakorlati tanulási út**

Átfogó, gyakorlati workshop anyagok gyártásra kész megvalósításokkal:

- **[Workshop útmutató](./Workshop/Readme.md)** - Teljes tanulási célok, eredmények és erőforrás navigáció
- **Python minták** (6 alkalom) - Frissítve a legjobb gyakorlatokkal, hibakezeléssel és átfogó dokumentációval
- **Jupyter füzetek** (8 interaktív) - Lépésről lépésre bemutatók benchmarkokkal és teljesítményfigyeléssel
- **Ülési útmutatók** - Részletes markdown útmutatók az egyes workshop alkalmakhoz
- **Validációs eszközök** - Szkriptek a kódminőség ellenőrzésére és smoke tesztek futtatására

**Amit építeni fogsz:**
- Helyi MI chat alkalmazások streaming támogatással
- RAG pipeline-ok minőség-értékeléssel (RAGAS)
- Többmodell teljesítménytesztelő és összehasonlító eszközök
- Több-ügynökös összehangoló rendszerek
- Intelligens modell irányítás feladatalapú kiválasztással

### 🎙️ **Workshop Agentic-nek: Gyakorlati – Az MI Podcast Stúdió**

Építs egy MI-alapú podcast gyártási folyamatot a nulláról! Ez az elmélyítő workshop megtanít arra, hogyan készíts egy komplett több-ügynökös rendszert, amely ötleteket alakít profi podcast epizódokká.
**[🎬 Indítsd el az AI Podcast Studio műhelyt](./WorkshopForAgentic/README.md)**

**A küldetésed**: Indítsd el a "Future Bytes" nevű tech podcastot, amelyet teljes egészében az általad épített AI ügynökök működtetnek. Nincs felhőalapú függőség, nincs API-költség — minden helyben, a gépeden fut.

**Mi teszi egyedivé:**
- **🤖 Valódi többügynökös összehangolás** – Építs speciális AI ügynököket, akik kutatnak, írnak és hanganyagot készítenek
- **🎯 Teljes gyártási folyamat** – A témaválasztástól a végleges podcast hanganyagig
- **💻 100%-ban helyi telepítés** – Ollama és helyi modellek (Qwen-3-8B) felhasználásával teljes adatvédelem és kontroll
- **🎤 Szöveg-beszéddé integráció** – Alakítsd a szkripteket természetes hangzású, többbeszélős beszélgetésekké
- **✋ Emberi felügyelettel működő munkafolyamatok** – Jóváhagyási pontok biztosítják a minőséget az automatizálás mellett

**Háromfelvonásos tanulási út:**

| Felvonás | Fókusz | Kulcsképességek | Időtartam |
|-----|-------|------------|----------|
| **[1. felvonás: Ismerkedj meg az AI asszisztenseiddel](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Építsd meg első AI ügynöködet | Eszközintegráció • Webes keresés • Problémamegoldás • Ügynöki gondolkodás | 2-3 óra |
| **[2. felvonás: Állítsd össze a gyártási csapatodat](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Hangold össze több ügynök munkáját | Csapatkoordináció • Jóváhagyási munkafolyamatok • DevUI felület • Emberi felügyelet | 3-4 óra |
| **[3. felvonás: Keltsd életre a podcastod](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generálj podcast hanganyagot | Szöveg-beszéd • Többbeszélős szintézis • Hosszú formátumú hanganyag • Teljes automatizálás | 2-3 óra |

**Használt technológiák:**
- **Microsoft Agent Framework** – Többügynökös összehangolás és koordináció
- **Ollama** – Helyi AI modell futtató környezet (felhő nélkül)
- **Qwen-3-8B** – Nyílt forráskódú nyelvi modell ügynöki feladatokra optimalizálva
- **Szöveg-beszéd API-k** – Természetes hangszintézis podcast generáláshoz

**Hardvertámogatás:**
- ✅ **CPU mód** – Tetszőleges modern számítógépen működik (ajánlott 8GB+ RAM)
- 🚀 **GPU gyorsítás** – Jelentősen gyorsabb következtetés NVIDIA/AMD GPU-kkal
- ⚡ **NPU támogatás** – Következő generációs neurális feldolgozó egység gyorsítás

**Kinek ideális:**
- Többügynökös AI rendszereket tanuló fejlesztőknek
- AI automatizáció és munkafolyamatok iránt érdeklődőknek
- AI által segített tartalomkészítőknek
- Praktikus AI összehangolási mintákat tanuló hallgatóknak

**Kezdd el építeni**: [🎙️ AI Podcast Studio műhely →](./WorkshopForAgentic/README.md)

### 📊 **Tanulási út összefoglaló**
- **Teljes időtartam**: 36-45 óra
- **Kezdő út**: 01-02 modulok (7-9 óra)  
- **Középhaladó út**: 03-04 modulok (9-11 óra)
- **Haladó út**: 05-07 modulok (12-15 óra)
- **Szakértői út**: 08 modul (8-10 óra)

## Mit építesz meg

### 🎯 Alapképességek
- **Edge AI architektúra**: Helyi-először AI rendszerek tervezése felhőintegrációval
- **Modelloptimalizálás**: Modellek kvantálása és tömörítése edge telepítéshez (85% sebességnövekedés, 75% méretcsökkentés)
- **Többplatformos telepítés**: Windows, mobileszköz, beágyazott és felhő-edge hibrid rendszerek
- **Gyártási műveletek**: Edge AI monitorozása, méretezése és karbantartása élesben

### 🏗️ Gyakorlati projektek
- **Foundry helyi chat alkalmazások**: Windows 11 natív app modellváltással
- **Többügynökös rendszerek**: Koordinátor speciális ügynökökkel komplex munkafolyamatokhoz  
- **RAG alkalmazások**: Helyi dokumentumfeldolgozás vektorkereséssel
- **Modell útválasztók**: Intelligens modellválasztás feladat elemzés alapján
- **API keretrendszerek**: Éles környezetre kész kliensek streaminggel és egészségügyi monitorozással
- **Többplatformos eszközök**: LangChain/Semantic Kernel integrációs minták

### 🏢 Ipari alkalmazások
**Gyártás** • **Egészségügy** • **Autonóm járművek** • **Okos városok** • **Mobilalkalmazások**

## Gyors kezdés

**Ajánlott tanulási út** (összesen 20-30 óra):

0. **📖 Bevezetés** ([Introduction.md](./introduction.md)): EdgeAI alapok + ipari kontextus + tanulási keretrendszer
1. **📚 Alapozás** (01-02 modulok): EdgeAI fogalmak + SLM modellcsaládok
2. **⚙️ Optimalizálás** (03-04 modulok): Telepítés + kvantálás keretrendszerek  
3. **🚀 Gyártás** (05-06 modulok): SLMOps + AI ügynökök + függvényhívások
4. **💻 Megvalósítás** (07-08 modulok): Platform minták + Foundry Local eszköztár

Minden modul elméletet, gyakorlati feladatokat és éles kódmintákat tartalmaz.

## Karrier hatás

**Technikai szerepek**: EdgeAI megoldás architekt • ML mérnök (Edge) • IoT AI fejlesztő • Mobil AI fejlesztő

**Ipari szektorok**: Gyártás 4.0 • Egészségügyi technológia • Autonóm rendszerek • FinTech • Fogyasztói elektronika

**Portfólió projektek**: Többügynökös rendszerek • Éles RAG alkalmazások • Többplatformos telepítés • Teljesítmény optimalizálás

## Könyvtárszerkezet

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Tanfolyam kiemelések

✅ **Fokozatos tanulás**: Elmélet → Gyakorlat → Éles telepítés  
✅ **Valódi esettanulmányok**: Microsoft, Japan Airlines, vállalati megvalósítások  
✅ **Gyakorlati példák**: 50+ példa, 10 átfogó Foundry Local demó  
✅ **Teljesítmény fókusz**: 85%-os sebességnövekedés, 75%-os méretcsökkenés  
✅ **Többplatformos megoldás**: Windows, mobil, beágyazott, felhő-edge hibrid  
✅ **Éles környezetre készen**: Monitorozás, méretezés, biztonság, megfelelőségi keretrendszerek

📖 **[Tanulási útmutató elérhető](STUDY_GUIDE.md)**: Strukturált 20 órás tanulási út időbeosztási útmutatóval és önértékelő eszközökkel.

---

**Az EdgeAI az AI telepítés jövőjét jelenti**: helyi-először, adatvédelmet megőrző és hatékony megoldások. Sajátítsd el ezeket a készségeket a következő generáció intelligens alkalmazásainak építéséhez.

## Más tanfolyamok

Csapatunk más tanfolyamokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain kezdőknek](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tanfolyamok
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Segítség kérése

Ha elakadsz vagy kérdéseid vannak az AI alkalmazások fejlesztésével kapcsolatban, csatlakozz:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzésed vagy hibákba ütközöl fejlesztés közben, látogass el ide:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változata tekinthető hiteles forrásnak. Fontos információk esetén javasoljuk szakmai, emberi fordítás igénybevételét. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->