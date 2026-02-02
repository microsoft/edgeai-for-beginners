# 7. fejezet: EdgeAI minták

Az Edge AI az intelligens feldolgozás lehetőségét hozza el közvetlenül az eszközökre, a felhőkapcsolattól függetlenül, az edge computing és a mesterséges intelligencia konvergenciáját képviselve. Ez a fejezet öt különböző EdgeAI megvalósítást mutat be különböző platformokon és keretrendszereken, bemutatva az AI modellek edge környezetben történő futtatásának sokoldalúságát és erejét.

## 1. EdgeAI az NVIDIA Jetson Orin Nano platformon

Az NVIDIA Jetson Orin Nano áttörést jelent az elérhető edge AI számítástechnikában, akár 67 TOPS AI teljesítményt nyújtva egy kompakt, hitelkártya méretű eszközben. Ez az erőteljes edge AI platform demokratizálja a generatív AI fejlesztést hobbisták, diákok és profi fejlesztők számára.

### Főbb jellemzők
- Akár 67 TOPS AI teljesítmény – 1,7-szeres javulás az elődjéhez képest
- 1024 CUDA mag és akár 32 Tensor Core az AI feldolgozáshoz
- 6-magos Arm Cortex-A78AE v8.2 64 bites CPU, maximum 1,5 GHz frekvenciával
- Mindössze 249 dolláros áron, a legmegfizethetőbb és legelérhetőbb platformot kínálva fejlesztőknek, diákoknak és alkotóknak

### Alkalmazások
A Jetson Orin Nano kiválóan futtatja a modern generatív AI modelleket, például a látás transzformátorokat, nagy nyelvi modelleket és látás-nyelv modelleket. Kifejezetten GenAI felhasználási esetekre tervezték, és most már több LLM-et is futtathat egy tenyérnyi eszközön. Népszerű felhasználási területek: AI-alapú robotika, okos drónok, intelligens kamerák és autonóm edge eszközök.

**További információ**: [NVIDIA Jetson Orin Nano szuperkomputer: Az EdgeAI következő nagy dobása](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobilalkalmazásokban .NET MAUI és ONNX Runtime GenAI segítségével

Ez a megoldás bemutatja, hogyan integrálható a Generatív AI és a Nagy Nyelvi Modellek (LLM-ek) keresztplatformos mobilalkalmazásokba a .NET MAUI (Multi-platform App UI) és az ONNX Runtime GenAI segítségével. Ez a megközelítés lehetővé teszi a .NET fejlesztők számára, hogy kifinomult AI-alapú mobilalkalmazásokat építsenek, amelyek natívan futnak Android és iOS eszközökön.

### Főbb jellemzők
- A .NET MAUI keretrendszerre épül, amely egyetlen kódbázist biztosít Android és iOS alkalmazásokhoz
- Az ONNX Runtime GenAI integráció lehetővé teszi generatív AI modellek futtatását közvetlenül mobil eszközökön
- Támogatja a mobil eszközökre szabott különféle hardvergyorsítókat, beleértve a CPU-t, GPU-t és speciális mobil AI processzorokat
- Platformspecifikus optimalizációk, mint például CoreML iOS-hez és NNAPI Androidhoz az ONNX Runtime segítségével
- Megvalósítja a teljes generatív AI folyamatot, beleértve az elő- és utófeldolgozást, az inferenciát, a logitok feldolgozását, a keresést és mintavételezést, valamint a KV cache kezelését

### Fejlesztési előnyök
A .NET MAUI megközelítés lehetővé teszi a fejlesztők számára, hogy meglévő C# és .NET készségeiket kihasználva építsenek keresztplatformos AI alkalmazásokat. Az ONNX Runtime GenAI keretrendszer több modellarchitektúrát támogat, például Llama, Mistral, Phi, Gemma és sok más. Az optimalizált ARM64 kernel gyorsítja az INT4 kvantált mátrixszorzást, biztosítva a hatékony teljesítményt mobil hardveren, miközben megőrzi a megszokott .NET fejlesztési élményt.

### Felhasználási területek
Ez a megoldás ideális azoknak a fejlesztőknek, akik .NET technológiák segítségével szeretnének AI-alapú mobilalkalmazásokat építeni, például intelligens chatbotokat, képfelismerő alkalmazásokat, nyelvfordító eszközöket és személyre szabott ajánlórendszereket, amelyek teljesen eszközön futnak a fokozott adatvédelem és offline képességek érdekében.

**További információ**: [.NET MAUI ONNX Runtime GenAI példa](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI az Azure-ban Kis Nyelvi Modellek Motorjával

A Microsoft Azure-alapú EdgeAI megoldása a Kis Nyelvi Modellek (SLM-ek) hatékony telepítésére összpontosít felhő-edge hibrid környezetekben. Ez a megközelítés áthidalja a felhőméretű AI szolgáltatások és az edge telepítési követelmények közötti szakadékot.

### Architektúra előnyei
- Zökkenőmentes integráció az Azure AI szolgáltatásokkal
- SLM-ek/LLM-ek és multimodális modellek futtatása eszközön és felhőben az ONNX Runtime segítségével
- Optimalizált vállalati méretű telepítéshez
- Támogatja a folyamatos modellfrissítéseket és kezelést

### Felhasználási területek
Az Azure EdgeAI megvalósítás kiválóan alkalmas olyan helyzetekben, amelyek vállalati szintű AI telepítést igényelnek felhőkezelési képességekkel. Ide tartozik az intelligens dokumentumfeldolgozás, valós idejű elemzés és hibrid AI munkafolyamatok, amelyek kihasználják a felhő és az edge számítástechnikai erőforrásokat.

**További információ**: [Azure EdgeAI SLM Motor](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI a Windows ML segítségével](./windowdeveloper.md)

A Windows ML a Microsoft legmodernebb futtatókörnyezete, amely optimalizált eszközön történő modellinferenciát és egyszerűsített telepítést kínál, a Windows AI Foundry alapjaként szolgálva. Ez a platform lehetővé teszi a fejlesztők számára, hogy AI-alapú Windows alkalmazásokat hozzanak létre, amelyek kihasználják a PC hardver teljes spektrumát.

### Platform képességek
- Minden Windows 11 PC-n működik, amely a 24H2 (26100-as build) vagy újabb verziót futtatja
- Minden x64 és ARM64 PC hardveren működik, még olyan PC-ken is, amelyek nem rendelkeznek NPU-val vagy GPU-val
- Lehetővé teszi a fejlesztők számára, hogy saját modelleiket hozzák és hatékonyan telepítsék az AMD, Intel, NVIDIA és Qualcomm szilícium partnerökoszisztémájában, amely CPU-t, GPU-t és NPU-t foglal magában
- Az infrastruktúra API-k kihasználásával a fejlesztőknek már nem kell több buildet készíteniük alkalmazásukból különböző szilícium célpontokhoz

### Fejlesztői előnyök
A Windows ML absztrahálja a hardvert és a végrehajtási szolgáltatókat, így Ön a kódírásra koncentrálhat. Ráadásul a Windows ML automatikusan frissül, hogy támogassa a legújabb NPU-kat, GPU-kat és CPU-kat, amint azok megjelennek. A platform egységes keretrendszert biztosít az AI fejlesztéshez a Windows hardverökoszisztéma sokszínűségén belül.

**További információ**: 
- [Windows ML áttekintés](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI fejlesztési útmutató](./windowdeveloper.md) - Átfogó útmutató a Windows Edge AI fejlesztéséhez

## [5. EdgeAI Foundry Local alkalmazásokkal](./foundrylocal.md)

A Foundry Local lehetővé teszi a Windows és Mac fejlesztők számára, hogy Retrieval Augmented Generation (RAG) alkalmazásokat építsenek helyi erőforrások felhasználásával .NET-ben, kombinálva a helyi nyelvi modelleket szemantikus keresési képességekkel. Ez a megközelítés adatvédelmi szempontból fókuszált AI megoldásokat kínál, amelyek teljes mértékben helyi infrastruktúrán működnek.

### Technikai architektúra
- Kombinálja a Phi nyelvi modellt, helyi beágyazásokat és a Szemantikus Kernel-t egy RAG forgatókönyv létrehozásához
- A beágyazásokat vektorokként (lebegőpontos értékek tömbjeiként) használja, amelyek tartalmat és annak szemantikai jelentését képviselik
- A Szemantikus Kernel fő integrátorként működik, összekapcsolva a Phi-t és az intelligens komponenseket egy zökkenőmentes RAG csővezeték létrehozásához
- Támogatja a helyi vektoradatbázisokat, például SQLite és Qdrant

### Megvalósítási előnyök
A RAG, vagy Retrieval Augmented Generation, egyszerűen azt jelenti, hogy "keressünk meg néhány dolgot, és tegyük bele a promptba". Ez a helyi megvalósítás biztosítja az adatvédelmet, miközben intelligens válaszokat nyújt, amelyek egyedi tudásbázisokon alapulnak. Ez a megközelítés különösen értékes vállalati forgatókönyvekben, amelyek adatfüggetlenséget és offline működési képességeket igényelnek.

**További információ**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG minták](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

A Microsoft Foundry Local egy OpenAI-kompatibilis REST szervert biztosít, amelyet az ONNX Runtime hajt, és amely lehetővé teszi modellek helyi futtatását Windows rendszeren. Az alábbiakban egy gyors, validált összefoglaló található; a teljes részletekért lásd a hivatalos dokumentációt.

- Első lépések: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektúra: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI referencia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Teljes Windows útmutató ebben a repóban: [foundrylocal.md](./foundrylocal.md)

Telepítés vagy frissítés Windows rendszeren (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI kategóriák felfedezése:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Modell futtatása és dinamikus végpont felfedezése:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Gyors REST ellenőrzés a modellek listázásához (cserélje ki a PORT-ot az állapotból):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tippek:
- SDK integráció: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Saját modell hozatala (fordítás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI fejlesztési források

A kifejezetten Windows platformot célzó fejlesztők számára átfogó útmutatót készítettünk, amely a teljes Windows EdgeAI ökoszisztémát lefedi. Ez az erőforrás részletes információkat nyújt a Windows AI Foundry-ról, beleértve az API-kat, eszközöket és legjobb gyakorlatokat a Windows EdgeAI fejlesztéséhez.

### Windows AI Foundry platform
A Windows AI Foundry platform átfogó eszköz- és API-készletet kínál, amelyet kifejezetten Edge AI fejlesztésre terveztek Windows eszközökön. Ide tartozik a NPU-gyorsított hardverek speciális támogatása, a Windows ML integráció és a platformspecifikus optimalizációs technikák.

**Átfogó útmutató**: [Windows EdgeAI fejlesztési útmutató](../windowdeveloper.md)

Ez az útmutató lefedi:
- A Windows AI Foundry platform áttekintése és komponensei
- Phi Silica API hatékony inferenciához NPU hardveren
- Számítógépes látás API-k képfeldolgozáshoz és OCR-hez
- Windows ML futtatókörnyezet integrációja és optimalizációja
- Foundry Local CLI helyi fejlesztéshez és teszteléshez
- Hardveroptimalizációs stratégiák Windows eszközökhöz
- Gyakorlati megvalósítási példák és legjobb gyakorlatok

### [AI Toolkit Edge AI fejlesztéshez](./aitoolkit.md)
A Visual Studio Code-ot használó fejlesztők számára az AI Toolkit kiterjesztés átfogó fejlesztési környezetet biztosít, amelyet kifejezetten Edge AI alkalmazások építésére, tesztelésére és telepítésére terveztek. Ez az eszközkészlet leegyszerűsíti az Edge AI fejlesztési munkafolyamatot a VS Code-on belül.

**Fejlesztési útmutató**: [AI Toolkit Edge AI fejlesztéshez](./aitoolkit.md)

Az AI Toolkit útmutató lefedi:
- Modell felfedezése és kiválasztása edge telepítéshez
- Helyi tesztelési és optimalizációs munkafolyamatok
- ONNX és Ollama integráció edge modellekhez
- Modellkonverzió és kvantálási technikák
- Ügynökfejlesztés edge forgatókönyvekhez
- Teljesítményértékelés és monitorozás
- Telepítési előkészületek és legjobb gyakorlatok

## Összegzés

Ez az öt EdgeAI megvalósítás bemutatja az edge AI megoldások érettségét és sokszínűségét, amelyek ma elérhetők. A Jetson Orin Nano hardvergyorsított edge eszközeitől kezdve az ONNX Runtime GenAI keresztplatformos mobilfejlesztési keretrendszerén és a Windows ML Windows-natív alkalmazásain át egészen a Foundry Local adatvédelmi szempontból fókuszált RAG megvalósításáig, a fejlesztőknek példátlan lehetőségeik vannak intelligens alkalmazások telepítésére az edge környezetben.

A közös szál ezekben a platformokban az AI képességek demokratizálása, amely lehetővé teszi a fejlett gépi tanulás elérését különböző szintű készségekkel és felhasználási esetekkel rendelkező fejlesztők számára. Legyen szó mobilalkalmazások, asztali szoftverek vagy beágyazott rendszerek építéséről, ezek az EdgeAI megoldások alapot nyújtanak a következő generációs intelligens alkalmazásokhoz, amelyek hatékonyan és privát módon működnek az edge környezetben.

Minden platform egyedi előnyöket kínál: Jetson Orin Nano a hardvergyorsított edge számítástechnikához, ONNX Runtime GenAI a keresztplatformos mobilfejlesztéshez, Azure EdgeAI a vállalati felhő-edge integrációhoz, Windows ML a Windows-natív alkalmazásokhoz, és Foundry Local az adatvédelmi szempontból fókuszált RAG megvalósításokhoz. Együtt átfogó ökoszisztémát képviselnek az EdgeAI fejlesztéshez.

[Következő AI Toolkit](aitoolkit.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.