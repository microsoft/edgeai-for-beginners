<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:53:09+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# EdgeAI kezdőknek


![Tanfolyam borítókép](../../translated_images/hu/cover.eb18d1b9605d754b.png)

[![GitHub közreműködők](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub hibák](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub lehúzási kérelmek](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR-eket várunk](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub megfigyelők](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forkok](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub csillagok](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kövesse ezeket a lépéseket a források használatának megkezdéséhez:

1. **Forkolja a Tárolót**: Kattintson [![GitHub forkok](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klónozza a Tárolót**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Csatlakozzon az Azure AI Foundry Discordhoz, és ismerkedjen szakértőkkel és fejlesztőtársakkal**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Többnyelvű támogatás

#### GitHub Action segítségével támogatott (Automatizált és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](./README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Inkább helyileg klónoznád?**

> Ez a tároló 50+ nyelvű fordítást tartalmaz, ami jelentősen megnöveli a letöltés méretét. Fordítások nélküli klónozáshoz használd a sparse checkoutot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ez mindent megad, amire szükséged van a kurzus elvégzéséhez, jóval gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ha további fordítási nyelveket szeretnél támogatni, azok listája itt található: [itt](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Bevezetés

Üdvözlünk az **EdgeAI kezdőknek** kurzuson – ez a teljes körű útmutató az Edge Mesterséges Intelligencia átalakító világába. Ez a tanfolyam hidat képez az erős AI képességek és a gyakorlati, valós eszközön történő bevezetés között, lehetővé téve, hogy kihasználd az AI potenciálját közvetlenül ott, ahol az adatok keletkeznek és a döntéseket meg kell hozni.

### Amit elsajátítasz

Ez a tanfolyam az alapfogalmaktól a termelésre kész megoldásokig vezet, beleértve:
- **Kisméretű nyelvi modelleket (SLM-ek)**, amelyek az edge telepítésre vannak optimalizálva
- **Hardver-központú optimalizálást** különböző platformokon
- **Valós idejű következtetést** adatvédelmi képességekkel
- **Termelési telepítési stratégiákat** vállalati alkalmazásokhoz

### Miért fontos az EdgeAI

Az Edge AI paradigmaváltást jelent, amely a modern kihívásokra ad megoldást:
- **Adatvédelem és Biztonság**: érzékeny adatokat helyben dolgoz fel, felhő nélküli hozzáférés nélkül
- **Valós idejű teljesítmény**: megszünteti a hálózati késleltetést időkritikus alkalmazásoknál
- **Költséghatékonyság**: csökkenti a sávszélességet és a felhőszolgáltatási költségeket
- **Funkcionális ellenállás**: működőképesség hálózati kimaradás esetén is
- **Szabályozási megfelelőség**: megfelel az adat-szuverenitás követelményeinek

### Edge AI

Az Edge AI a helyi hardveren futtatott AI algoritmusokat és nyelvi modelleket jelenti, közvetlenül ott, ahol az adat keletkezik, felhőszolgáltatások nélkül a következtetéshez. Csökkenti a késleltetést, növeli az adatvédelmet, és lehetővé teszi a valós idejű döntéshozatalt.

### Alapelvek:
- **Helyszíni következtetés**: AI modellek futtatása edge eszközökön (telefonok, routerek, mikrokontrollerek, ipari PC-k)
- **Offline képesség**: internetkapcsolat nélkül is működik
- **Alacsony késleltetés**: azonnali válaszok valós idejű rendszerek számára
- **Adatszuverenitás**: az érzékeny adatokat helyben tartja, javítva a biztonságot és a megfelelést

### Kisméretű Nyelvi Modellek (SLM-ek)

Az olyan SLM-ek, mint a Phi-4, Mistral-7B és Gemma, optimalizált változatai a nagyobb LLM-eknek—képzettek vagy desztilláltak a következőkre:
- **Csökkentett memóriaigény**: hatékony használat a limitált edge eszközök memóriájával
- **Alacsonyabb számítási igény**: optimalizált CPU- és edge GPU-teljesítményhez
- **Gyorsabb indítási idő**: gyors inicializálás a reszponzív alkalmazásokhoz

Erőteljes NLP képességeket nyitnak meg, miközben megfelelnek a következő korlátoknak:
- **Beágyazott rendszerek**: IoT eszközök és ipari vezérlők
- **Mobil eszközök**: okostelefonok és táblagépek offline képességekkel
- **IoT eszközök**: érzékelők és okoseszközök korlátozott erőforrásokkal
- **Edge szerverek**: helyi feldolgozó egységek korlátozott GPU erőforrásokkal
- **Személyi számítógépek**: asztali és laptopos telepítési forgatókönyvek

## Tanfolyam modulok és navigáció

| Modul | Téma | Fókuszterület | Fő tartalom | Szint | Időtartam |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Bevezetés az EdgeAI-be](./introduction.md) | Alapok és kontextus | EdgeAI áttekintés • Ipari alkalmazások • SLM bevezetés • Tanulási célok | Kezdő | 1-2 óra |
| [📚 01](../../Module01) | [EdgeAI Alapok](./Module01/README.md) | Felhő vs Edge AI összehasonlítás | EdgeAI alapok • Valós esettanulmányok • Megvalósítási útmutató • Edge telepítés | Kezdő | 3-4 óra |
| [🧠 02](../../Module02) | [SLM Modell Alapok](./Module02/README.md) | Modellcsaládok és architektúra | Phi család • Qwen család • Gemma család • BitNET • μModel • Phi-Silica | Kezdő | 4-5 óra |
| [🚀 03](../../Module03) | [SLM Telepítési Gyakorlat](./Module03/README.md) | Helyi és felhő alapú telepítés | Haladó tanulás • Helyi környezet • Felhő alapú telepítés | Középhaladó | 4-5 óra |
| [⚙️ 04](../../Module04) | [Model Optimalizációs Eszköztár](./Module04/README.md) | Platformok közötti optimalizálás | Bevezetés • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Munkafolyamat szintézis | Középhaladó | 5-6 óra |
| [🔧 05](../../Module05) | [SLMOps Termelés](./Module05/README.md) | Termelési működés | SLMOps bevezetés • Modell desztilláció • Finomhangolás • Termelési telepítés | Haladó | 5-6 óra |
| [🤖 06](../../Module06) | [AI Ügynökök és Függvényhívás](./Module06/README.md) | Ügynök keretrendszerek és MCP | Ügynök bevezetés • Függvényhívás • Modell Kontextus Protokoll | Haladó | 4-5 óra |
| [💻 07](../../Module07) | [Platform megvalósítás](./Module07/README.md) | Keresztplatform minták | AI Eszközkészlet • Foundry Local • Windows fejlesztés | Haladó | 3-4 óra |
| [🏭 08](../../Module08) | [Foundry Local eszköztár](./Module08/README.md) | Termelésre kész minták | Mintaalkalmazások (lásd részleteket lent) | Szakértő | 8-10 óra |

### 🏭 **08. modul: Mintaalkalmazások**

- [01: REST Chat gyorsindítás](./Module08/samples/01/README.md)
- [02: OpenAI SDK integráció](./Module08/samples/02/README.md)
- [03: Modell felfedezés és benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG alkalmazás](./Module08/samples/04/README.md)
- [05: Több-ügynökös koordináció](./Module08/samples/05/README.md)
- [06: Modellek mint eszközök router](./Module08/samples/06/README.md)
- [07: Közvetlen API kliens](./Module08/samples/07/README.md)
- [08: Windows 11 csevegőalkalmazás](./Module08/samples/08/README.md)
- [09: Haladó többugynökös rendszer](./Module08/samples/09/README.md)
- [10: Foundry eszköz keretrendszer](./Module08/samples/10/README.md)

### 🎓 **Workshop: Gyakorlati tanulási út**

Átfogó gyakorlati workshop anyagok termelésre kész megvalósításokkal:

- **[Workshop útmutató](./Workshop/Readme.md)** - Teljes tanulási célkitűzések, eredmények és forrásnavigáció
- **Python minták** (6 alkalom) - Frissített legjobb gyakorlatokkal, hibakezeléssel és átfogó dokumentációval
- **Jupyter jegyzetfüzetek** (8 interaktív) - Lépésről lépésre oktatóanyagok benchmarkokkal és teljesítményfigyeléssel
- **Ülés útmutatók** - Részletes markdown útmutatók minden workshop üléshez
- **Érvényesítő eszközök** - Szkriptek a kódminőség ellenőrzésére és alapvető tesztek futtatására

**Mit fogsz építeni:**
- Helyi AI csevegőalkalmazások streaming támogatással
- RAG folyamatok minőségi értékeléssel (RAGAS)
- Többmodell benchmarking és összehasonlító eszközök
- Többugynökös koordinációs rendszerek
- Intelligens modellirányítás feladat alapú kiválasztással

### 🎙️ **Workshop az Agentic számára: Gyakorlati - Az AI Podcast Stúdió**

Építs egy AI által működtetett podcast gyártási folyamatot a semmiből! Ez az átfogó workshop megtanítja, hogyan készíts teljes többugynökös rendszert, amely az ötleteket professzionális podcast epizódokká alakítja.
**[🎬 Indítsd el az AI Podcast Stúdió Workshopot](./WorkshopForAgentic/README.md)**

**A te küldetésed:** Indítsd el a "Future Bytes" – egy olyan technológiai podcastot, amely teljes egészében az általad épített AI ügynökök által működik. Nincs felhőfüggőség, nincs API költség – minden helyben, a gépeden fut.

**Mi teszi egyedivé ezt:**
- **🤖 Valódi Több-ügynökös Orkesztráció** – Építs specializált AI ügynököket, akik kutatnak, írnak és hanganyagokat készítenek
- **🎯 Teljes gyártási folyamat** – A téma kiválasztásától a végső podcast hangkimenetig
- **💻 100% helyi futtatás** – Ollama és helyi modellek (Qwen-3-8B) használata a teljes adatvédelem és kontroll érdekében
- **🎤 Szöveg-beszéddé integráció** – Alakítsd át a forgatókönyveket természetes hangzású, többszólamú beszélgetésekké
- **✋ Emberi felügyelet a folyamatban** – Jóváhagyási pontok a minőség biztosítására az automatizálás mellett

**Három felvonásos tanulási út:**

| Felvonás | Fókusz | Kulcskészségek | Időtartam |
|-----|-------|------------|----------|
| **[1. felvonás: Ismerkedj meg AI asszisztenseiddel](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Építsd meg első AI ügynöködet | Eszközintegráció • Webkeresés • Problémamegoldás • Ügynöki érvelés | 2-3 óra |
| **[2. felvonás: Állítsd össze a produkciós csapatod](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Több ügynök összehangolása | Csapatkoordináció • Jóváhagyási munkafolyamatok • DevUI felület • Emberi felügyelet | 3-4 óra |
| **[3. felvonás: Élesítsd a podcastod](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Podcast hanganyag előállítása | Szöveg-beszéd • Többszólamú szintézis • Hosszú hanganyag • Teljes automatizálás | 2-3 óra |

**Felhasznált technológiák:**
- **Microsoft Agent Framework** – Több-ügynökös összehangolás és koordináció
- **Ollama** – Helyi AI modell futtatókörnyezet (nem igényel felhőt)
- **Qwen-3-8B** – Nyílt forráskódú nyelvi modell ügynöki feladatokra optimalizálva
- **Szöveg-beszéd API-k** – Természetes hangzású hangszintézis podcastgeneráláshoz

**Hardvertámogatás:**
- ✅ **CPU mód** – Minden modern számítógépen működik (ajánlott: 8GB+ RAM)
- 🚀 **GPU gyorsítás** – Jelentősen gyorsabb következtetés NVIDIA/AMD GPU-kon
- ⚡ **NPU támogatás** – Következő generációs neurális feldolgozóegység gyorsítás

**Tökéletes választás:**
- Több-ügynökös AI rendszereket tanuló fejlesztőknek
- AI automatizálás és munkafolyamatok iránt érdeklődőknek
- AI által segített tartalomkészítőknek
- Praktikus AI orkesztrációs mintákat tanuló diákoknak

**Kezdd el az építést**: [🎙️ Az AI Podcast Stúdió Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Tanulási út összefoglaló**
- **Teljes időtartam:** 36-45 óra
- **Kezdő út:** Modulok 01-02 (7-9 óra)  
- **Középhaladó út:** Modulok 03-04 (9-11 óra)
- **Haladó út:** Modulok 05-07 (12-15 óra)
- **Szakértői út:** Modul 08 (8-10 óra)

## Amit építeni fogsz

### 🎯 Alapkészségek
- **Edge AI architektúra**: Helyi elsődleges AI rendszerek tervezése felhőintegrációval
- **Modelloptimalizálás**: Modellek kvantálása és tömörítése edge telepítéshez (85% sebességnövelés, 75% méretcsökkentés)
- **Többplatformos telepítés**: Windows, mobil, beágyazott és felhő-edge hibrid rendszerek
- **Gyártási üzemeltetés**: Edge AI monitorozása, skálázása és karbantartása

### 🏗️ Gyakorlati projektek
- **Foundry helyi chat alkalmazások**: Windows 11 natív alkalmazás modellváltással
- **Több-ügynökös rendszerek**: Koordinátor szakértő ügynökökkel bonyolult munkafolyamatokhoz  
- **RAG alkalmazások**: Helyi dokumentumfeldolgozás vektorkereséssel
- **Modellrouterek**: Intelligens modellek közti választás feladatelemzés alapján
- **API keretrendszerek**: Gyártásra kész kliens streaminggel és egészségfigyeléssel
- **Többplatformos eszközök**: LangChain/Semantic Kernel integrációs minták

### 🏢 Iparági alkalmazások
**Gyártás** • **Egészségügy** • **Önvezető járművek** • **Okos városok** • **Mobilalkalmazások**

## Gyors indulás

**Ajánlott tanulási út** (összesen 20-30 óra):

0. **📖 Bevezetés** ([Introduction.md](./introduction.md)): EdgeAI alapok + iparági kontextus + tanulási keretrendszer  
1. **📚 Alapok** (01-02 modulok): EdgeAI fogalmak + SLM modellcsaládok  
2. **⚙️ Optimalizálás** (03-04 modulok): Telepítés + kvantázó keretrendszerek  
3. **🚀 Gyártás** (05-06 modulok): SLMOps + AI ügynökök + függvényhívások  
4. **💻 Megvalósítás** (07-08 modulok): Platformpéldák + Foundry Local eszköztár

Minden modul elméletet, gyakorlati feladatokat és gyártásra kész kódmintákat tartalmaz.

## Karrier hatás

**Technikai szerepek:** EdgeAI megoldástervező • ML mérnök (Edge) • IoT AI fejlesztő • Mobil AI fejlesztő

**Iparági szektorok:** Gyártás 4.0 • Egészségügyi technológia • Autonóm rendszerek • FinTech • Fogyasztói elektronika

**Portfólió projektek:** Több-ügynökös rendszerek • Gyártásra kész RAG alkalmazások • Többplatformos telepítés • Teljesítményoptimalizálás

## Tároló felépítése

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

## Tanfolyam főbb pontjai

✅ **Fokozatos tanulás**: Elmélet → Gyakorlat → Gyártási telepítés  
✅ **Valódi esettanulmányok**: Microsoft, Japan Airlines, vállalati megvalósítások  
✅ **Gyakorlati példák**: 50+ példa, 10 átfogó Foundry Local demo  
✅ **Teljesítmény fókusz**: 85%-os gyorsulás, 75%-os méretcsökkenés  
✅ **Többplatformos**: Windows, mobil, beágyazott, felhő-edge hibrid  
✅ **Gyártásra kész**: Monitorozás, skálázás, biztonság, megfelelőség keretrendszerek

📖 **[Tanulmányi útmutató elérhető](STUDY_GUIDE.md)**: Strukturált 20 órás tanulási út időbeosztási javaslatokkal és önértékelő eszközökkel.

---

**Az EdgeAI az AI jövőjét képviseli:** helyi elsődlegesség, adatvédelem és hatékonyság. Sajátítsd el ezeket a készségeket, hogy a következő generációs intelligens alkalmazásokat építhesd meg.

## Egyéb tanfolyamok

Csapatunk más kurzusokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tanulás
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat
[![Copilot AI társprogramozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Segítség kérése

Ha elakad, vagy kérdése van az AI alkalmazások fejlesztésével kapcsolatban, csatlakozzon:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzése vagy hibája van a fejlesztés során, látogassa meg:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy helytelen értelmezésért, amely ebből a fordításból származik.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->