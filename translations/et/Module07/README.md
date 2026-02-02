# Peatükk 07: EdgeAI näited

Edge AI ühendab tehisintellekti ja serva-arvutuse, võimaldades intelligentset töötlemist otse seadmetes ilma pilveühenduse vajaduseta. Selles peatükis uuritakse viit erinevat EdgeAI rakendust erinevatel platvormidel ja raamistikus, näidates AI mudelite servas käitamise mitmekülgsust ja võimsust.

## 1. EdgeAI NVIDIA Jetson Orin Nano platvormil

NVIDIA Jetson Orin Nano on läbimurre taskukohases serva AI arvutuses, pakkudes kuni 67 TOPS-i AI jõudlust kompaktses, krediitkaardi suuruses vormis. See võimas serva AI platvorm demokratiseerib generatiivse AI arenduse nii hobiarendajatele, tudengitele kui ka professionaalsetele arendajatele.

### Põhifunktsioonid
- Pakub kuni 67 TOPS-i AI jõudlust—1,7-kordne paranemine võrreldes eelkäijaga
- 1024 CUDA tuuma ja kuni 32 Tensor Core'i AI töötlemiseks
- 6-tuumaline Arm Cortex-A78AE v8.2 64-bitine protsessor maksimaalse sagedusega 1,5 GHz
- Hind vaid $249, pakkudes arendajatele, tudengitele ja loojatele kõige taskukohasemat ja kättesaadavamat platvormi

### Rakendused
Jetson Orin Nano paistab silma kaasaegsete generatiivsete AI mudelite, sealhulgas visioonitransformaatorite, suurte keelemudelite ja visioon-keele mudelite käitamisel. See on spetsiaalselt loodud GenAI kasutusjuhtumite jaoks ning nüüd saab mitmeid LLM-e käitada peopesasuurusel seadmel. Populaarsed kasutusjuhtumid hõlmavad AI-toega robootikat, nutikaid droone, intelligentseid kaameraid ja autonoomseid servaseadmeid.

**Loe lähemalt**: [NVIDIA Jetson Orin Nano Superarvuti: Järgmine suur asi EdgeAI-s](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobiilirakendustes .NET MAUI ja ONNX Runtime GenAI abil

See lahendus näitab, kuidas integreerida generatiivset AI-d ja suuri keelemudeleid (LLM-e) platvormidevahelistesse mobiilirakendustesse, kasutades .NET MAUI-d (Multi-platform App UI) ja ONNX Runtime GenAI-d. See lähenemine võimaldab .NET arendajatel luua keerukaid AI-toega mobiilirakendusi, mis töötavad natiivsetena Androidi ja iOS-i seadmetes.

### Põhifunktsioonid
- Ehitatud .NET MAUI raamistikule, pakkudes ühtset koodibaasi nii Androidi kui iOS-i rakendustele
- ONNX Runtime GenAI integratsioon võimaldab generatiivsete AI mudelite käitamist otse mobiilseadmetes
- Toetab erinevaid riistvarakiirendeid, mis on kohandatud mobiilseadmetele, sealhulgas CPU, GPU ja spetsiaalsed mobiilsed AI protsessorid
- Platvormispetsiifilised optimeerimised nagu CoreML iOS-i jaoks ja NNAPI Androidi jaoks ONNX Runtime kaudu
- Rakendab täielikku generatiivse AI tsüklit, sealhulgas eel- ja järelprotsessimist, järeldamist, logitite töötlemist, otsingut ja valimist ning KV vahemälu haldamist

### Arenduse eelised
.NET MAUI lähenemine võimaldab arendajatel kasutada oma olemasolevaid C# ja .NET oskusi, luues samal ajal platvormidevahelisi AI rakendusi. ONNX Runtime GenAI raamistik toetab mitmeid mudeliarhitektuure, sealhulgas Llama, Mistral, Phi, Gemma ja paljusid teisi. Optimeeritud ARM64 tuumad kiirendavad INT4 kvantiseeritud maatriksikorrutust, tagades tõhusa jõudluse mobiilse riistvara peal, säilitades samas tuttava .NET arenduskogemuse.

### Kasutusjuhtumid
See lahendus sobib ideaalselt arendajatele, kes soovivad luua AI-toega mobiilirakendusi, kasutades .NET tehnoloogiaid, sealhulgas intelligentseid vestlusroboteid, pildituvastusrakendusi, keele tõlketööriistu ja isikupärastatud soovitussüsteeme, mis töötavad täielikult seadmes, pakkudes paremat privaatsust ja võrguühenduseta võimekust.

**Loe lähemalt**: [.NET MAUI ONNX Runtime GenAI näide](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI Azure'is väikeste keelemudelite mootoriga

Microsofti Azure-põhine EdgeAI lahendus keskendub väikeste keelemudelite (SLM-ide) tõhusale juurutamisele pilv-serva hübriidkeskkondades. See lähenemine ühendab pilvemastaabis AI teenused ja serva juurutamise nõuded.

### Arhitektuuri eelised
- Sujuv integratsioon Azure AI teenustega
- Käita SLM-e/LLM-e ja multimodaalseid mudeleid seadmes ja pilves ONNX Runtime abil
- Optimeeritud ettevõttemastaabis juurutamiseks
- Toetus pidevatele mudeli uuendustele ja haldamisele

### Kasutusjuhtumid
Azure EdgeAI rakendus paistab silma ettevõttemastaabis AI juurutamise stsenaariumides, kus on vaja pilvehaldusvõimekust. See hõlmab intelligentset dokumenditöötlust, reaalajas analüütikat ja hübriidseid AI töövooge, mis kasutavad nii pilve kui serva arvutusressursse.

**Loe lähemalt**: [Azure EdgeAI SLM mootor](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI Windows ML-iga](./windowdeveloper.md)

Windows ML on Microsofti tipptasemel tööaeg, mis on optimeeritud mudelite tõhusaks seadmes järeldamiseks ja lihtsustatud juurutamiseks, olles Windows AI Foundry aluseks. See platvorm võimaldab arendajatel luua AI-toega Windowsi rakendusi, mis kasutavad täielikult PC riistvara potentsiaali.

### Platvormi võimalused
- Töötab kõigil Windows 11 arvutitel, mille versioon on 24H2 (ehitis 26100) või uuem
- Töötab kõigil x64 ja ARM64 PC riistvaradel, isegi arvutitel, millel pole NPUsid või GPUsid
- Võimaldab arendajatel tuua oma mudelid ja juurutada neid tõhusalt üle silikoonipartnerite ökosüsteemi, sealhulgas AMD, Intel, NVIDIA ja Qualcomm, hõlmates CPU, GPU, NPU
- Kasutades infrastruktuuri API-sid, ei pea arendajad enam looma mitut rakenduse versiooni, et sihtida erinevat silikooni

### Arendaja eelised
Windows ML abstraheerib riistvara ja täitmisprotsessorid, võimaldades teil keskenduda koodi kirjutamisele. Lisaks uuendab Windows ML automaatselt, et toetada uusimaid NPUsid, GPUsid ja CPUsid nende väljalaskmisel. Platvorm pakub ühtset raamistikku AI arenduseks mitmekesise Windowsi riistvara ökosüsteemi jaoks.

**Loe lähemalt**: 
- [Windows ML ülevaade](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI arendusjuhend](./windowdeveloper.md) - Põhjalik juhend Windows Edge AI arenduseks

## [5. EdgeAI Foundry Local rakendustega](./foundrylocal.md)

Foundry Local võimaldab Windowsi ja Maci arendajatel luua Retrieval Augmented Generation (RAG) rakendusi, kasutades kohalikke ressursse .NET-is, kombineerides kohalikke keelemudeleid semantilise otsinguvõimekusega. See lähenemine pakub privaatsusele keskenduvaid AI lahendusi, mis töötavad täielikult kohaliku infrastruktuuri peal.

### Tehniline arhitektuur
- Kombineerib Phi keelemudeli, kohalikud sisukirjeldused ja semantilise tuuma, et luua RAG stsenaarium
- Kasutab sisukirjeldusi vektorite (ujukomaarvude massiivide) kujul, mis esindavad sisu ja selle semantilist tähendust
- Semantiline tuum toimib peamise orkestreerijana, integreerides Phi ja nutikad komponendid, et luua sujuv RAG torustik
- Toetus kohalikele vektorandmebaasidele, sealhulgas SQLite ja Qdrant

### Rakenduse eelised
RAG ehk Retrieval Augmented Generation on lihtsalt viis öelda "otsige midagi üles ja lisage see sisendisse". See kohalik rakendus tagab andmete privaatsuse, pakkudes samal ajal intelligentseid vastuseid, mis põhinevad kohandatud teadmistebaasidel. Lähenemine on eriti väärtuslik ettevõtte stsenaariumides, kus on vaja andmesuveräänsust ja võrguühenduseta töövõimekust.

**Loe lähemalt**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG näited](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local pakub OpenAI-ühilduvat REST-serverit, mida toetab ONNX Runtime, mudelite käitamiseks kohapeal Windowsis. Allpool on kiire, valideeritud kokkuvõte; vaadake ametlikke dokumente täielike detailide jaoks.

- Alustamine: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektuur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI viide: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Täielik Windowsi juhend selles repos: [foundrylocal.md](./foundrylocal.md)

Installimine või uuendamine Windowsis (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI kategooriate uurimine:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Mudeli käitamine ja dünaamilise lõpp-punkti avastamine:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Kiire REST-kontroll mudelite loetlemiseks (asendage PORT staatusega):
```cmd
curl -s http://localhost:PORT/v1/models
```

Näpunäited:
- SDK integratsioon: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Oma mudeli lisamine (kompileerimine): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI arendusressursid

Windowsi platvormi sihtivatele arendajatele oleme loonud põhjaliku juhendi, mis hõlmab kogu Windows EdgeAI ökosüsteemi. See ressurss pakub üksikasjalikku teavet Windows AI Foundry kohta, sealhulgas API-d, tööriistad ja parimad tavad EdgeAI arenduseks Windowsis.

### Windows AI Foundry platvorm
Windows AI Foundry platvorm pakub terviklikku tööriistade ja API-de komplekti, mis on spetsiaalselt loodud Edge AI arenduseks Windowsi seadmetel. See hõlmab spetsiaalset tuge NPU-kiirendatud riistvarale, Windows ML integratsiooni ja platvormispetsiifilisi optimeerimistehnikaid.

**Põhjalik juhend**: [Windows EdgeAI arendusjuhend](../windowdeveloper.md)

See juhend hõlmab:
- Windows AI Foundry platvormi ülevaadet ja komponente
- Phi Silica API tõhusaks järeldamiseks NPU riistvaral
- Arvutinägemise API-d pilditöötluseks ja OCR-iks
- Windows ML tööaja integratsiooni ja optimeerimist
- Foundry Local CLI kohalikuks arenduseks ja testimiseks
- Riistvara optimeerimise strateegiaid Windowsi seadmetele
- Praktilisi rakenduse näiteid ja parimaid tavasid

### [AI tööriistakomplekt Edge AI arenduseks](./aitoolkit.md)
Visual Studio Code'i kasutavatele arendajatele pakub AI tööriistakomplekti laiendus terviklikku arenduskeskkonda, mis on spetsiaalselt loodud Edge AI rakenduste loomiseks, testimiseks ja juurutamiseks. See tööriistakomplekt lihtsustab kogu Edge AI arenduse töövoogu VS Code'is.

**Arendusjuhend**: [AI tööriistakomplekt Edge AI arenduseks](./aitoolkit.md)

AI tööriistakomplekti juhend hõlmab:
- Mudelite avastamist ja valimist serva juurutamiseks
- Kohalikke testimis- ja optimeerimisvooge
- ONNX ja Ollama integratsiooni serva mudelite jaoks
- Mudelite konverteerimise ja kvantiseerimise tehnikaid
- Agentide arendust serva stsenaariumide jaoks
- Jõudluse hindamist ja jälgimist
- Juurutamise ettevalmistust ja parimaid tavasid

## Kokkuvõte

Need viis EdgeAI rakendust näitavad serva AI lahenduste küpsust ja mitmekesisust, mis on tänapäeval saadaval. Alates riistvarakiirendusega servaseadmetest nagu Jetson Orin Nano kuni tarkvara raamistikeni nagu ONNX Runtime GenAI ja Windows ML, on arendajatel enneolematud võimalused intelligentsete rakenduste juurutamiseks servas.

Kõigi nende platvormide ühine joon on AI võimekuse demokratiseerimine, muutes keeruka masinõppe kättesaadavaks arendajatele erinevatel oskustasemetel ja kasutusjuhtumites. Olgu tegemist mobiilirakenduste, töölauatarkvara või manussüsteemide loomisega, need EdgeAI lahendused pakuvad alust järgmise põlvkonna intelligentsetele rakendustele, mis töötavad tõhusalt ja privaatselt servas.

Iga platvorm pakub unikaalseid eeliseid: Jetson Orin Nano riistvarakiirendusega servaarvutuseks, ONNX Runtime GenAI platvormidevaheliseks mobiiliarenduseks, Azure EdgeAI ettevõtte pilv-serva integratsiooniks, Windows ML Windowsi natiivrakenduste jaoks ja Foundry Local privaatsusele keskenduvate RAG rakenduste jaoks. Koos moodustavad need tervikliku ökosüsteemi EdgeAI arenduseks.

[Next AI Toolkit](aitoolkit.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.