# „Windows Edge AI“ kūrimo vadovas

## Įvadas

Sveiki atvykę į „Windows Edge AI“ kūrimą – jūsų visapusišką vadovą kuriant intelektualias programas, kurios naudoja įrenginyje vykdomą AI galias naudodamos „Microsoft“ „Windows AI Foundry“ platformą. Šis vadovas skirtas būtent „Windows“ kūrėjams, kurie nori integruoti pažangias Edge AI galimybes į savo programas, panaudodami visą „Windows“ aparatinės įrangos spartinimo spektrą.

### „Windows AI“ pranašumas

„Windows AI Foundry“ yra vieninga, patikima ir saugi platforma, palaikanti visą AI kūrėjo gyvenimo ciklą – nuo modelio pasirinkimo ir tikslinimo iki optimizavimo ir diegimo per CPU, GPU, NPU bei hibridinės debesijos architektūras. Ši platforma demokratizuoja AI kūrimą, siūlydama:

- **Aparatinės įrangos abstrakcija**: sklandi diegimo galimybė per AMD, Intel, NVIDIA ir Qualcomm lustus
- **Įrenginyje vykdoma intelektualumas**: privatumą saugantis AI, kuris veikia visiškai lokaliai
- **Optimizuotas našumas**: modeliai iš anksto optimizuoti „Windows“ aparatūros konfigūracijoms
- **Paruošta įmonėms**: gamybinio lygio saugumo ir atitikties funkcijos

### Windows ML
„Windows Machine Learning“ (ML) leidžia C#, C++ ir Python kūrėjams vietoje „Windows“ PC paleisti ONNX AI modelius per ONNX Runtime, automatiškai valdant vykdymo teikėjus skirtingai aparatinei įrangai (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) galima naudoti su modeliais iš PyTorch, Tensorflow/Keras, TFLite, scikit-learn ir kitų sistemų.


![WindowsML Schema, iliustruojanti ONNX modelį einantį per Windows ML pasiekti NPU, GPU ir CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

„Windows ML“ suteikia bendrą visos Windows ekosistemos ONNX Runtime kopiją ir galimybę dinamiškai atsisiųsti vykdymo teikėjus (EP).

### Kodėl Windows Edge AI?

**Universalus aparatūros palaikymas**
„Windows ML“ automatiškai optimizuoja aparatūrą visoje Windows ekosistemoje, užtikrindama, kad jūsų AI programos veiktų optimaliai, nepaisant naudojamo lustų architektūros.

**Integruota AI vykdymo sistema**
Integruotas „Windows ML“ infersijos variklis pašalina sudėtingą diegimo procesą, leidžiant kūrėjams daugiausia dėmesio skirti programų logikai, o ne infrastruktūros klausimams.

**Copilot+ PC optimizavimas**
Tiksliai sukurtos API specialiai naujos kartos „Windows“ įrenginiams su integruotais neuroninio apdorojimo vienetais (NPU), užtikrinantys išskirtinį našumą vienam vatui.

**Kūrėjų ekosistema**
Turtingi įrankiai įskaitant Visual Studio integraciją, išsamią dokumentaciją ir pavyzdines programas, kurios greitina kūrimo ciklus.

## Mokymosi tikslai

Baigę šį „Windows Edge AI“ kūrimo vadovą, įvaldysite svarbiausius įgūdžius kuriant gamybai paruoštas AI programas „Windows“ platformoje.

### Pagrindinės techninės kompetencijos

**„Windows AI Foundry“ išmanymas**
- Suprasti „Windows AI Foundry“ platformos architektūrą ir komponentus
- Naršyti visą AI kūrimo gyvenimo ciklą „Windows“ ekosistemoje
- Įgyvendinti saugumo geriausias praktikas įrenginyje vykdomoms AI programoms
- Optimizuoti programas skirtingoms „Windows“ aparatūros konfigūracijoms

**API integracijos ekspertizė**
- Įvaldyti „Windows AI“ API tekstui, vizijai ir multimodalinėms programoms
- Įgyvendinti Phi Silica kalbos modelio integraciją teksto generavimui ir samprotavimui
- Diegti kompiuterinės vizijos galimybes naudojant įmontuotas vaizdo apdorojimo API
- Koreguoti iš anksto apmokytus modelius naudojant LoRA (žemo laipsnio adaptaciją) metodus

**Foundry Local įgyvendinimas**
- Naršyti, vertinti ir diegti atvirojo kodo kalbos modelius naudojant Foundry Local CLI
- Suprasti modelių optimizavimą ir kvantizaciją vietiniam diegimui
- Įgyvendinti neprisijungus veikiančias AI funkcijas, veikiančias be interneto prieigos
- Valdyti modelių gyvavimo ciklus ir atnaujinimus gamybos aplinkose

**„Windows ML“ diegimas**
- Pristatyti pasirinktinius ONNX modelius „Windows“ programoms naudojant „Windows ML“
- Pasinaudoti automatine aparatūros akseleracija CPU, GPU ir NPU architektūrose
- Įgyvendinti realaus laiko infersiją su optimaliu resursų naudojimu
- Kurti mastelio keičiamas AI programas įvairioms „Windows“ įrenginių kategorijoms

### Programų kūrimo įgūdžiai

**Kryžminės platformos „Windows“ kūrimas**
- Kurti AI valdomas programas naudojant .NET MAUI universaliam „Windows“ diegimui
- Integruoti AI galimybes į Win32, UWP ir pažangias interneto programas
- Įgyvendinti reaguojančius vartotojo sąsajos dizainus, kurie prisitaiko prie AI apdorojimo būsenų
- Tvarkyti asinchroninius AI procesus naudojant tinkamus vartotojo patirties modelius

**Našumo optimizavimas**
- Profiluoti ir optimizuoti AI infersijos našumą skirtingoms aparatūros konfigūracijoms
- Įgyvendinti efektyvų didelių kalbos modelių atminties valdymą
- Kurti programas, kurios sklandžiai prastėja, atsižvelgiant į turimą aparatūros galimybes
- Taikyti talpyklavimo strategijas dažnai naudojamoms AI operacijoms

**Gamybos paruošimas**
- Įgyvendinti išsamų klaidų valdymą ir atsarginius mechanizmus
- Kurti telemetriją ir stebėseną AI programų našumui
- Taikyti saugumo geriausias praktikas vietinių AI modelių saugojimui ir vykdymui
- Planuoti diegimo strategijas įmonių ir vartotojų programoms

### Verslo ir strateginis suvokimas

**AI programų architektūra**
- Kurti hibridines architektūras, optimizuojančias vietinį ir debesijos AI apdorojimą
- Įvertinti kompromisus tarp modelio dydžio, tikslumo ir infersijos greičio
- Planuoti duomenų srauto architektūras, kurias išlaiko privatumą ir leidžiančias intelektualumą
- Įgyvendinti ekonomiškas AI sprendimų, kurie gali augti pagal vartotojų poreikius

**Rinkos pozicionavimas**
- Suprasti „Windows“ gimtųjų AI programų konkurencinius pranašumus
- Nustatyti atvejus, kai įrenginyje vykdoma AI suteikia geresnę vartotojo patirtį
- Kurti į rinką orientuotas strategijas AI patobulintoms „Windows“ programoms
- Pozicionuoti programas pasinaudojant „Windows“ ekosistemos privalumais

## „Windows App SDK“ AI pavyzdžiai

„Windows App SDK“ pateikia išsamius pavyzdžius, iliustruojančius AI integravimą per kelis karkasus ir diegimo scenarijus. Šie pavyzdžiai yra esminiai šablonai norint suprasti „Windows AI“ kūrimo modelius.

### „Windows AI Foundry“ pavyzdžiai

| Pavyzdys | Karkasas | Dėmesio sritis | Pagrindinės savybės |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | „Windows AI“ API integracija | Pilna WinUI programa demonstruojanti „Windows AI“ API, ARM64 optimizacija, supakuotas diegimas |

**Pagrindinės technologijos:**
- „Windows AI“ API
- WinUI 3 karkasas
- ARM64 platformos optimizavimas
- Suderinamumas su Copilot+ PC
- Supakuotos programos diegimas

**Reikalavimai:**
- Rekomenduojama „Windows 11“ su Copilot+ PC
- Visual Studio 2022
- ARM64 binarų konfigūracija
- „Windows App SDK“ 1.8.1 ar naujesnė versija

### „Windows ML“ pavyzdžiai

#### C++ pavyzdžiai

| Pavyzdys | Tipas | Dėmesio sritis | Pagrindinės savybės |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolinė programa | Pagrindinis Windows ML | EP aptikimas, komandų eilutės parinktys, modelių kompiliavimas |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolinė programa | Karkaso diegimas | Bendrinamas vykdymas, mažesnis diegimo dydis |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolinė programa | Savarankiškas diegimas | Nepriklausomas diegimas, be vykdymo laikotarpio priklausomybių |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Bibliotekos naudojimas | WindowsML bendroje bibliotekoje, atminties valdymas |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demonstracija | ResNet pamoka | Modelio konvertavimas, EP kompiliavimas, Build 2025 pamoka |

#### C# pavyzdžiai

**Konsolinės programos**

| Pavyzdys | Tipas | Dėmesio sritis | Pagrindinės savybės |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolinė programa | Pagrindinė C# integracija | Bendrinamų pagalbinių funkcijų naudojimas, komandų eilutės sąsaja |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demonstracija | ResNet pamoka | Modelio konvertavimas, EP kompiliavimas, Build 2025 pamoka |

**GUI programos**

| Pavyzdys | Karkasas | Dėmesio sritis | Pagrindinės savybės |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Darbalaukio GUI | Vaizdų klasifikavimas su WPF sąsaja |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicinė GUI | Vaizdų klasifikavimas su Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Vaizdų klasifikavimas su WinUI 3 sąsaja |

#### Python pavyzdžiai

| Pavyzdys | Kalba | Dėmesio sritis | Pagrindinės savybės |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Vaizdų klasifikacija | WinML Python saitai, partijinis vaizdų apdorojimas |

### Pavyzdžių reikalavimai

**Sistemos reikalavimai:**
- „Windows 11“ PC su versija 24H2 (build 26100) arba naujesnė
- Visual Studio 2022 su C++ ir .NET darbo krūviais
- „Windows App SDK“ 1.8.1 ar naujesnė versija
- Python 3.10-3.13 Python pavyzdžiams x64 ir ARM64 įrenginiuose

**Specifiniai „Windows AI Foundry“ reikalavimai:**
- Rekomenduojama Copilot+ PC optimaliam veikimui
- ARM64 binarų konfigūracija „Windows AI“ pavyzdžiams
- Reikalinga paketo tapatybė (nepaketuotos programos nebepalaikomos)

### Dažnas pavyzdžių darbo eiga

Dauguma „Windows ML“ pavyzdžių naudoja šį standartinį modelį:

1. **Aplinkos inicijavimas** – sukurti ONNX Runtime aplinką
2. **Vykdymo teikėjų registracija** – aptikti ir registruoti turimus aparatūros akseleratorius (CPU, GPU, NPU)
3. **Modelio įkėlimas** – įkelti ONNX modelį, opcionaliai kompiliuoti tikslinei aparatūrai
4. **Įvesties išankstinis apdorojimas** – konvertuoti vaizdus/duomenis į modelio įvesties formatą
5. **Inferences vykdymas** – paleisti modelį ir gauti prognozes
6. **Rezultatų apdorojimas** – pritaikyti softmax ir parodyti pagrindines prognozes

### Naudojami modelių failai

| Modelis | Paskirtis | Įtrauktas | Pastabos |
|-------|---------|----------|-------|
| SqueezeNet | Lengvas vaizdų klasifikavimas | ✅ Įtrauktas | Iš anksto apmokytas, paruoštas naudoti |
| ResNet-50 | Aukšto tikslumo vaizdų klasifikavimas | ❌ Reikalauja konvertavimo | Naudoti [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) konvertavimui |

### Aparatūros palaikymas

Visos pavyzdys automatiškai aptinka ir naudoja turimą aparatūrą:
- **CPU** – universali parama visiems „Windows“ įrenginiams
- **GPU** – automatinis aptikimas ir optimizavimas turimai grafinei aparatūrai
- **NPU** – naudojami neuroninio apdorojimo vienetai palaikomuose įrenginiuose (Copilot+ PC)

## „Windows AI Foundry“ platformos komponentai

### 1. „Windows AI“ API

„Windows AI“ API suteikia paruoštas naudoti AI galimybes, varomas įrenginyje veikiančių modelių, optimizuotų efektyvumui ir našumui „Copilot+ PC“ įrenginiuose, reikalaujant minimalaus nustatymo.

#### Pagrindinės API kategorijos

**Phi Silica kalbos modelis**
- Mažas, bet galingas kalbos modelis tekstų generavimui ir samprotavimui
- Optimizuotas realaus laiko infersijai su minimalia elektros energijos sąnauda
- Pagalba individualiam tikslinimui naudojant LoRA metodus
- Integracija su „Windows“ semantiniu paieškos ir žinių gavimu

**Kompiuterinės vizijos API**
- **Teksto atpažinimas (OCR)**: tekstų išgavimas iš vaizdų su dideliu tikslumu
- **Vaizdo super raiška**: vaizdų padidinimas naudojant vietinius AI modelius
- **Vaizdo segmentavimas**: specifinių objektų identifikavimas ir atskyrimas vaizduose
- **Vaizdo aprašymas**: generuoti detalius tekstinius aprašymus vizualiai informacijai
- **Objektų šalinimas**: pašalinti nepageidaujamus objektus iš vaizdų AI pagrįstu užpildymu

**Multimodalinės galimybės**
- **Vizijos ir kalbos integracija**: derinti teksto ir vaizdo supratimą
- **Semantinė paieška**: leisti natūralios kalbos užklausas per daugialypį turinį
- **Žinių gavimas**: kurti intelektualias paieškos patirtis su vietiniais duomenimis

### 2. Foundry Local

„Foundry Local“ suteikia kūrėjams greitą prieigą prie paruoštų naudoti atvirojo kodo kalbos modelių „Windows“ lustų platformoje, siūlydama galimybę naršyti, testuoti, sąveikauti ir diegti modelius vietinėse programose.

#### Foundry Local pavyzdinės programos

[Foundry Local saugykla](https://github.com/microsoft/Foundry-Local/tree/main/samples) pateikia išsamius pavyzdžius keliomis programavimo kalbomis ir karkasais, rodydama įvairius integracijos šablonus ir naudojimo atvejus.

| Pavyzdys | Kalba/Karkasas | Dėmesio sritis | Pagrindinės savybės |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG įgyvendinimas | Semantinis branduolys, Qdrant vektorių saugykla, JINA įterpimai, dokumentų įsisavinimas, srautinės pokalbių funkcijos |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Darbalaukio pokalbių programa | Kryžminės platformos pokalbiai, vietinių/debesijos modelių perjungimas, OpenAI SDK integracija, realaus laiko srautinimas |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Pagrindinė integracija | Paprastas SDK naudojimas, modelio inicijavimas, bazinės pokalbių funkcijos |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Pagrindinė integracija | Python SDK naudojimas, srautiniai atsakymai, OpenAI suderinamas API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistemų integracija | Žemo lygio SDK naudojimas, asinchroninės operacijos, reqwest HTTP klientas |

#### Pavyzdžių kategorijos pagal naudojimo atvejį

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Pilnas RAG įgyvendinimas naudojant Semantic Kernel, Qdrant vektorinę bazę ir JINA įterpimus
- **Architektūra**: Dokumentų įvedimas → Teksto skaidymas → Vektorinių įterpimų kūrimas → Panašumo paieška → Konteksto suprantantys atsakymai
- **Technologijos**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX įterpimai, srauto pokalbių užbaigimas

**Darbalaukio programos**
- **electron/foundry-chat**: Gamybai paruošta pokalbių programa su vietinių/debesų modelių perjungimu
- **Savybės**: Modelių pasirinkėjas, srautiniai atsakymai, klaidų tvarkymas, daugiaplatforminis diegimas
- **Architektūra**: Electron pagrindinis procesas, IPC komunikacija, saugūs įkėlimo scenarijai

**SDK integracijos pavyzdžiai**
- **JavaScript (Node.js)**: Pagrindinis modeliavimo sąveikos ir srautinių atsakymų pavyzdys
- **Python**: OpenAI suderinamo API naudojimas su asinchroniniu srautu
- **Rust**: Žemo lygio integracija su reqwest ir tokio asinchroninėms operacijoms

#### Reikalavimai Foundry Local pavyzdžiams

**Sistemos reikalavimai:**
- Windows 11 su įdiegta Foundry Local
- Node.js v16+ JavaScript/Electron pavyzdžiams
- .NET 8.0+ C# pavyzdžiams
- Python 3.10+ Python pavyzdžiams
- Rust 1.70+ Rust pavyzdžiams

**Įdiegimas:**
```powershell
# Įdiekite Foundry vietoje
winget install Microsoft.FoundryLocal

# Patikrinkite diegimą
foundry --version
foundry model list
```

#### Pavyzdžiams skirtas paruošimas

**dotNET RAG pavyzdys:**
```powershell
# Įdiekite reikalingas paketo per NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Paleiskite Qdrant vektorinę duomenų bazę
docker run -p 6333:6333 qdrant/qdrant

# Vykdyti Jupyter užrašų knygelę
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron pokalbių pavyzdys:**
```powershell
# Nustatyti aplinkos kintamuosius debesies atsarginėms kopijoms
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Įdiegti priklausomybes ir paleisti
npm install
npm start
```

**JavaScript/Python/Rust pavyzdžiai:**
```powershell
# Atsisiųsti modelį (pavyzdys su phi-3.5-mini)
foundry model run phi-3.5-mini

# Vykdyti atitinkamą pavyzdį
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Pagrindinės funkcijos

**Modelių katalogas**
- Išsamus atviro kodo optimizuotų modelių rinkinys
- Modeliai optimizuoti CPU, GPU ir NPU greitam diegimui
- Palaikymas populiarioms modeliavimo šeimoms, įskaitant Llama, Mistral, Phi ir specializuotus domenų modelius

**CLI integracija**
- Komandų eilutės sąsaja modelių valdymui ir diegimui
- Automatizuoti optimizavimo ir kiekinio sumažinimo procesai
- Integracija su populiariomis kūrimo aplinkomis ir CI/CD sistemomis

**Vietinis diegimas**
- Visiškai nepriklausomas darbas be debesijos priklausomybių
- Palaikymas individualiems modelių formatams ir konfigūracijoms
- Efektyvus modelių talpinimas su automatinėmis aparatūros optimizacijomis

### 3. Windows ML

Windows ML tarnauja kaip pagrindinė AI platforma ir integruota spėjimų vykdymo aplinka Windows sistemoje, leidžianti kūrėjams efektyviai diegti pasirinktinius modelius plačioje Windows aparatinės įrangos ekosistemoje.

#### Architektūros privalumai

**Universalus aparatūros palaikymas**
- Automatinė optimizacija AMD, Intel, NVIDIA ir Qualcomm lustams
- Palaikymas CPU, GPU ir NPU vykdymui su skaidriu perjungimu
- Aparatūros abstrakcija, pašalinanti platformai būdingus optimizavimo darbus

**Modelių lankstumas**
- Palaikymas ONNX modelių formatui su automatiniu konvertavimu iš populiarių karkasų
- Pasirinktinis modelių diegimas su gamybinės kokybės našumu
- Integracija į esamas Windows programų architektūras

**Įmonių integracija**
- Suderinamas su Windows saugos ir atitikties sistemomis
- Palaikymas įmonių diegimo ir valdymo įrankiams
- Integracija su Windows įrenginių valdymo ir stebėjimo sistemomis

## Kūrimo darbo eiga

### 1 etapas: Aplinkos paruošimas ir įrankių konfigūracija

**Kūrimo aplinkos paruošimas**
1. Įdiekite Visual Studio 2022 su C++ ir .NET darbo krūviais
2. Įdiekite Windows App SDK 1.8.1 arba naujesnę versiją
3. Suveskite Windows AI Foundry CLI įrankius
4. Įdiekite AI Toolkit priedą Visual Studio Code
5. Įdiekite našumo profiliavimo ir stebėjimo įrankius
6. Užtikrinkite ARM64 kompiliavimo konfigūraciją Copilot+ PC optimizavimui

**Pavyzdžių saugyklos paruošimas**
1. Nubraukite [Windows App SDK pavyzdžių saugyklą](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Naršykite į `Samples/WindowsAIFoundry/cs-winui` Windows AI API pavyzdžiams
3. Naršykite į `Samples/WindowsML` išsamiesiems Windows ML pavyzdžiams
4. Peržiūrėkite [sistemos reikalavimus](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) tikslinėms platformoms

**AI kūrimo galerijos tyrinėjimas**
- Tyrinėkite pavyzdžių programas ir referencinius įgyvendinimus
- Testuokite Windows AI API su interaktyviais demonstravimais
- Peržiūrėkite šaltinio kodą dėl geriausių praktikų ir modelių
- Identifikuokite tinkamus pavyzdžius pagal savo naudojimo atvejį

### 2 etapas: Modelių pasirinkimas ir integracija

**Reikalavimų analizė**
- Apibrėžkite funkcinius AI galimybių reikalavimus
- Nustatykite našumo apribojimus ir optimizavimo tikslus
- Įvertinkite privatumo ir saugumo reikalavimus
- Suplanuokite diegimo architektūrą ir mastelio taikymo strategijas

**Modelių vertinimas**
- Naudokite Foundry Local atviro kodo modelių testavimui savo naudojimo atvejui
- Įvertinkite Windows AI API našumą pagal pasirinktinius modelių reikalavimus
- Įvertinkite kompromisus tarp modelio dydžio, tikslumo ir spėjimų greičio
- Prototipuokite integracijos būdus su pasirinktais modeliais

### 3 etapas: Programų kūrimas

**Pagrindinė integracija**
- Įgyvendinkite Windows AI API integraciją su tinkamu klaidų tvarkymu
- Kurkite vartotojo sąsajas, pritaikytas AI apdorojimo srautams
- Implementuokite talpyklų ir optimizavimo strategijas modelių spėjimui
- Pridėkite telemetriją ir stebėseną AI operacijų našumui

**Testavimas ir patvirtinimas**
- Testuokite programas skirtingose Windows aparatinės įrangos konfiguracijose
- Patvirtinkite našumo rodiklius esant įvairioms apkrovos sąlygoms
- Įgyvendinkite automatizuotą testavimą AI funkcionalumo patikimumui
- Vykdykite naudotojo patirties testavimą su AI patobulintomis funkcijomis

### 4 etapas: Optimizavimas ir diegimas

**Našumo optimizacija**
- Profilizuokite programos našumą skirtingose aparatinės įrangos konfiguracijose
- Optimizuokite atminties naudojimą ir modeliavimo krovimo strategijas
- Įgyvendinkite adaptacines elgesio funkcijas pagal turimą aparatūrą
- Koreguokite naudotojo patirtį skirtingiems našumo scenarijams

**Gamybinis diegimas**
- Supakuokite programas su reikalingomis AI modelių priklausomybėmis
- Įgyvendinkite modelių ir programos logikos atnaujinimo mechanizmus
- Konfigūruokite stebėsenos ir analizės priemones gamybos aplinkoms
- Suplanuokite diegimo strategijas įmonėms ir vartotojams

## Praktiniai įgyvendinimo pavyzdžiai

### Pavyzdys 1: Intelektuali dokumentų apdorojimo programa

Sukurkite Windows programą, apdorojančią dokumentus naudodama kelias AI galimybes:

**Naudojamos technologijos:**
- Phi Silica dokumentų suvestinės ir klausimų atsakymo funkcijoms
- OCR API tekstui iš nuskaitytų dokumentų išgauti
- Vaizdo aprašymo API diagramų ir grafikų analizei
- Pasirinktini ONNX modeliai dokumentų klasifikavimui

**Įgyvendinimo metodika:**
- Sukurkite modulinę architektūrą su keičiamais AI komponentais
- Įgyvendinkite asinchroninį didelių dokumentų partijų apdorojimą
- Pridėkite pažangos indikatorius ir atšaukimo palaikymą ilgoms operacijoms
- Užtikrinkite veikimą neprisijungus jautrių dokumentų apdorojimui

### Pavyzdys 2: Mažmeninės prekybos inventoriaus valdymo sistema

Sukurkite AI paremta inventoriaus valdymo sistemą mažmeniniam verslui:

**Naudojamos technologijos:**
- Vaizdo segmentacija produktų atpažinimui
- Pasirinktini matymo modeliai prekės ženklų ir kategorijų klasifikacijai
- Foundry Local diegimas specializuotiems mažmeninės kalbos modeliams
- Integracija su esamomis POS ir inventoriaus sistemomis

**Įgyvendinimo metodika:**
- Sukurkite kameros integraciją realaus laiko produktų nuskaitymui
- Įgyvendinkite brūkšninių kodų ir vaizdų atpažinimą
- Pridėkite natūralios kalbos užklausas naudojant vietinius kalbos modelius
- Sukurkite keičiamą architektūrą daugia parduotuvių diegimui

### Pavyzdys 3: Sveikatos priežiūros dokumentacijos asistentas

Sukurkite privatumą saugantį sveikatos priežiūros dokumentacijos įrankį:

**Naudojamos technologijos:**
- Phi Silica medicininių pastabų kūrimui ir klinikinių sprendimų palaikymui
- OCR rašytinių medicininių įrašų skaitmeninimui
- Pasirinktini medicininiai kalbos modeliai diegiami per Windows ML
- Vietinis vektorinės saugyklos naudojimas medicinos žinių paieškai

**Įgyvendinimo metodika:**
- Užtikrinkite visišką neprisijungus veikimą pacientų privatumui
- Įgyvendinkite medicininių terminų patikrinimą ir siūlymus
- Pridėkite audito registraciją atitikties reikalavimams
- Sukurkite integraciją su esamomis Elektroninėmis sveikatos įrašų sistemomis

## Našumo optimizavimo strategijos

### Aparatūros suvokimas kūrime

**NPU optimizacija**
- Projektuokite programas, kad išnaudotų NPU galimybes Copilot+ PC
- Įgyvendinkite tvarkingą atsitraukimą į GPU/CPU įrenginiuose be NPU
- Optimizuokite modelių formatus NPU specifiniam pagreičiui
- Stebėkite NPU naudojimą ir šilumos parametrus

**Atminties valdymas**
- Įgyvendinkite efektyvų modelių krovimą ir talpyklų strategijas
- Naudokite atminties žemėlapiavimą dideliems modeliams sumažinti paleidimo laiką
- Kurkite atminties taupančias programas ribotos aparatinės įrangos įrenginiams
- Įgyvendinkite modelio kiekinį sumažinimą atminties optimizacijai

**Baterijos efektyvumas**
- Optimizuokite AI operacijas maksimaliai mažam energijos suvartojimui
- Įgyvendinkite adaptacinį apdorojimą pagal baterijos būseną
- Kurkite efektyvų foninį apdorojimą nuolatiniam AI veikimui
- Naudokite energijos profiliavimo įrankius optimizacijai

### Skalės svarstymai

**Daugiagyslumas**
- Kurkite siūlus apsaugančias AI operacijas lygiagreičiam apdorojimui
- Įgyvendinkite efektyvų darbo paskirstymą tarp turimų branduolių
- Naudokite asinchroninius/await modelius neblokuojančioms AI operacijoms
- Planuokite siūlų baseino optimizaciją skirtingoms aparatinės įrangos konfigūracijoms

**Talpyklų strategijos**
- Įgyvendinkite protingą talpyklų laikymą dažnai naudojamoms AI operacijoms
- Kurkite talpyklos nebegaliojimo strategijas modelių atnaujinimams
- Naudokite nuolatinę talpyklą brangiems išankstiniams apdorojimams
- Įgyvendinkite paskirstytą talpyklą daugnaudotojų scenarijams

## Saugumo ir privatumo gerosios praktikos

### Duomenų apsauga

**Vietinis apdorojimas**
- Užtikrinkite, kad jautrūs duomenys niekada nepaliktų vietinio įrenginio
- Įgyvendinkite saugią saugyklą AI modeliams ir laikiniems duomenims
- Naudokite Windows saugumo funkcijas programos izoliuotumui
- Taikykite šifravimą saugomiems modeliams ir tarpinėms apdorojimo rezultatams

**Modelių saugumas**
- Patikrinkite modelių vientisumą prieš kraunant ir vykdant
- Įgyvendinkite saugius modelių atnaujinimo mechanizmus
- Naudokite pasirašytus modelius, kad išvengtumėte klastojimo
- Taikykite prieigos valdymą modelių failams ir konfigūracijoms

### Atitikties svarstymai

**Reguliacinė atitiktis**
- Kurkite programas, atitinkančias GDPR, HIPAA ir kitus reglamentus
- Įgyvendinkite audito registraciją AI sprendimų procesams
- Užtikrinkite skaidrumo funkcijas AI generuotiems rezultatams
- Leidykite vartotojui valdyti AI duomenų apdorojimą

**Įmonių saugumas**
- Integruokite su Windows įmonių saugumo politikomis
- Palaikykite valdomą diegimą per įmonių valdymo įrankius
- Įgyvendinkite vaidmenų pagrindu veikiančius prieigos valdymus AI funkcijoms
- Suteikite administravimo valdymus AI funkcionalumui

## Gedimų šalinimas ir derinimas

### Dažniausios kūrimo problemos

**Kompiliavimo konfigūracijos problemos**
- Užtikrinkite ARM64 platformos konfigūraciją Windows AI API pavyzdžiams
- Patikrinkite Windows App SDK versijos suderinamumą (reikalinga 1.8.1+)
- Patikrinkite, kad paketo identitetas tinkamai sukonfigūruotas (reikalinga Windows AI API)
- Patvirtinkite, kad kūrimo įrankiai palaiko tikslinį karkasą

**Modelių krovimo problemos**
- Patikrinkite ONNX modelių suderinamumą su Windows ML
- Patikrinkite modelio failų vientisumą ir formato reikalavimus
- Patikrinkite aparatūros palaikymo reikalavimus konkretiems modeliams
- Derinkite atminties paskirstymo problemas modeliui kraunant
- Užtikrinkite vykdymo teikėjo registraciją aparatūros pagreičiui

**Diegimo režimo svarstymai**
- **Savęs turinčio režimas**: Visiškai palaikomas su didesniu diegimo dydžiu
- **Priklausomas nuo karkaso režimas**: Mažesnis pėdsakas, bet reikia bendro vykdymo laiko
- **Neapipakuotos programos**: Nebepalaikomos Windows AI API
- Naudokite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` savęs turinčio ARM64 diegimui

**Našumo problemos**
- Profilizuokite programos našumą skirtingose aparatinės įrangos konfigūracijose
- Identifikuokite AI apdorojimo siūlų užstrigimus
- Optimizuokite duomenų išankstinį ir galutinį apdorojimą
- Įgyvendinkite našumo stebėjimą ir įspėjimus

**Integracijos sunkumai**
- Derinkite API integracijos problemas su tinkamu klaidų tvarkymu
- Patikrinkite įvesties duomenų formatus ir išankstinio apdorojimo reikalavimus
- Kruopščiai testuokite ribines situacijas ir klaidų scenarijus
- Įgyvendinkite išsamią registraciją gamybos gedimų derinimui

### Derinimo įrankiai ir metodai

**Visual Studio integracija**
- Naudokite AI Toolkit derintuvą modeliavimo vykdymo analizei
- Įgyvendinkite AI našumo profiliavimą
- Derinkite asinchronines AI operacijas su tinkamu klaidų valdymu
- Naudokite atminties profiliavimo įrankius optimizavimui

**Windows AI Foundry įrankiai**
- Naudokite Foundry Local CLI modelių testavimui ir tikrinimui
- Naudokite Windows AI API testavimo įrankius integracijos patikrai
- Įgyvendinkite pasirinktinius įrašus AI veiklos stebėjimui
- Kurkite automatizuotus testus AI funkcionalumo patikimumui

## Ateities garantijos jūsų programoms

### Naujausios technologijos

**Naujos kartos aparatūra**
- Projektuokite programas, kad išnaudotų būsimą NPU galimybes
- Rinkitės didesnius modelius ir sudėtingumą
- Įgyvendinkite adaptacines architektūras besikeičiančiai aparatūrai
- Apsvarstykite kvantiniam skaičiavimui suderinamus algoritmus ateičiai

**Pažangios AI galimybės**
- Ruoškite multimodalinę AI integraciją platesniems duomenų tipams
- Planuokite realaus laiko bendradarbiavimą AI tarp kelių įrenginių
- Projektuokite federuoto mokymosi galimybes
- Apsvarstykite ribinės ir debesijos hibridinės intelekto architektūras

### Nuolatinis mokymasis ir adaptacija

**Modelių atnaujinimai**
- Įgyvendinkite sklandžius modelių atnaujinimo mechanizmus
- Kurkite programas, prisitaikančias prie patobulintų modelių galimybių
- Planuokite atgalinį suderinamumą su esamais modeliais
- Įgyvendinkite A/B testavimą modelių našumo vertinimui

**Funkcijų vystymas**
- Kurkite modulinę architektūrą, palaikančią naujas AI galimybes
- Planuokite naujų Windows AI API integraciją
- Įgyvendinkite funkcijų žymes palaipsniui diegimui
- Kurkite vartotojo sąsajas, prisitaikančias prie patobulintų AI funkcijų

## Išvados

Windows Edge AI kūrimas reiškia galingų AI galimybių sujungimą su patikima, saugia ir masteliuojama Windows platforma. Įvaldę Windows AI Foundry ekosistemą, kūrėjai gali kurti išmanias programas, kurios suteikia išskirtinę naudotojo patirtį, išlaikant aukščiausius privatumo, saugumo ir našumo standartus.

Windows AI API, Foundry Local ir Windows ML derinys suteikia neprilygstamą pagrindą kuriant naujos kartos išmanias Windows programas. AI tobulėjant, Windows platforma užtikrina, kad jūsų programos išliks suderinamos ir našios įvairioje Windows aparatūroje, palaikydamos naujausias technologijas.

Nesvarbu ar kuriate vartotojų programas, įmonių sprendimus ar specializuotus pramonės įrankius, Windows Edge AI kūrimas suteikia galimybę kurti išmanias, jautrias ir giliai integruotas patirtis, išnaudojančias šiuolaikinių Windows įrenginių pilną potencialą.

## Papildomi ištekliai

### Dokumentacija ir mokymasis
- [Windows AI Foundry dokumentacija](https://learn.microsoft.com/windows/ai/)
- [Windows AI API nuoroda](https://learn.microsoft.com/windows/ai/apis/)
- [Pradėkite kurti programą su Windows AI API](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local pradžia](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML apžvalga](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK sistemos reikalavimai](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows programų SDK kūrimo aplinkos nustatymas](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Pavyzdžių saugyklos ir kodas
- [Windows programų SDK pavyzdžiai - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows programų SDK pavyzdžiai - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime spėjimo pavyzdžiai](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows programų SDK pavyzdžių saugykla](https://github.com/microsoft/WindowsAppSDK-Samples)

### Kūrimo įrankiai
- [AI įrankių rinkinys Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI kūrėjų galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI pavyzdžiai](https://learn.microsoft.com/windows/ai/samples/)
- [Modelių konvertavimo įrankiai](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Techninė pagalba
- [Windows ML dokumentacija](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime dokumentacija](https://onnxruntime.ai/docs/)
- [Windows programų SDK dokumentacija](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Pranešti apie problemas - Windows programų SDK pavyzdžiai](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Bendruomenė ir palaikymas
- [Windows kūrėjų bendruomenė](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry tinklaraštis](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI mokymai](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ši gidas kuriamas kartu su sparčiai besivystančia Windows AI ekosistema. Reguliarūs atnaujinimai užtikrina suderinamumą su naujausiomis platformos galimybėmis ir geriausiomis kūrimo praktikomis.*

[08. Praktika su Microsoft Foundry Local - Pilnas kūrėjo įrankių rinkinys](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->