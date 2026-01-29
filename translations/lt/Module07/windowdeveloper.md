# Windows Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į Windows Edge AI kūrimą – išsamų vadovą, padėsiantį kurti išmaniąsias programas, kurios naudoja įrenginio AI galimybes per Microsoft Windows AI Foundry platformą. Šis vadovas skirtas Windows kūrėjams, norintiems integruoti pažangias Edge AI funkcijas į savo programas, pasinaudojant visais Windows aparatūros pagreičio privalumais.

### Windows AI privalumai

Windows AI Foundry yra vieninga, patikima ir saugi platforma, palaikanti visą AI kūrimo ciklą – nuo modelio pasirinkimo ir pritaikymo iki optimizavimo ir diegimo per CPU, GPU, NPU ir hibridines debesų architektūras. Ši platforma demokratizuoja AI kūrimą, siūlydama:

- **Aparatūros abstrakciją**: Sklandus diegimas per AMD, Intel, NVIDIA ir Qualcomm lustus
- **Vietinė intelektinė sistema**: Privatumo užtikrinimas, kai AI veikia tik vietinėje aparatūroje
- **Optimizuotas našumas**: Modeliai, iš anksto optimizuoti Windows aparatūros konfigūracijoms
- **Paruošta verslui**: Gamybinio lygio saugumo ir atitikties funkcijos

### Windows ML
Windows Machine Learning (ML) leidžia C#, C++ ir Python kūrėjams vykdyti ONNX AI modelius vietoje Windows kompiuteriuose per ONNX Runtime, automatiškai valdant vykdymo teikėjus skirtingai aparatūrai (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) galima naudoti su modeliais iš PyTorch, Tensorflow/Keras, TFLite, scikit-learn ir kitų sistemų.

![WindowsML Diagrama, iliustruojanti ONNX modelio perėjimą per Windows ML į NPU, GPU ir CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML siūlo bendrą Windows-wide ONNX Runtime kopiją, taip pat galimybę dinamiškai atsisiųsti vykdymo teikėjus (EPs).

### Kodėl Windows Edge AI?

**Universalus aparatūros palaikymas**  
Windows ML automatiškai optimizuoja aparatūrą visoje Windows ekosistemoje, užtikrindama, kad jūsų AI programos veiktų optimaliai, nepriklausomai nuo pagrindinės lustų architektūros.

**Integruotas AI vykdymo variklis**  
Įmontuotas Windows ML inferencijos variklis pašalina sudėtingus nustatymo reikalavimus, leidžiant kūrėjams susitelkti į programos logiką, o ne infrastruktūros problemas.

**Copilot+ PC optimizacija**  
Specialiai sukurti API, skirti naujos kartos Windows įrenginiams su dedikuotais neuroniniais procesoriais (NPU), užtikrinantys išskirtinį našumą per vatą.

**Kūrėjų ekosistema**  
Turtingi įrankiai, įskaitant Visual Studio integraciją, išsamią dokumentaciją ir pavyzdines programas, kurios pagreitina kūrimo ciklus.

## Mokymosi tikslai

Baigę šį Windows Edge AI kūrimo vadovą, įgysite esminių įgūdžių, reikalingų kurti gamybai paruoštas AI programas Windows platformoje.

### Pagrindinės techninės kompetencijos

**Windows AI Foundry įvaldymas**  
- Suprasti Windows AI Foundry platformos architektūrą ir komponentus  
- Naršyti visą AI kūrimo ciklą Windows ekosistemoje  
- Įgyvendinti saugumo geriausią praktiką vietinėms AI programoms  
- Optimizuoti programas skirtingoms Windows aparatūros konfigūracijoms  

**API integracijos ekspertizė**  
- Įvaldyti Windows AI API tekstui, vaizdams ir multimodalinėms programoms  
- Įgyvendinti Phi Silica kalbos modelio integraciją tekstų generavimui ir samprotavimui  
- Diegti kompiuterinio matymo galimybes naudojant įmontuotus vaizdų apdorojimo API  
- Pritaikyti iš anksto apmokytus modelius naudojant LoRA (Low-Rank Adaptation) technikas  

**Foundry Local įgyvendinimas**  
- Naršyti, vertinti ir diegti atvirojo kodo kalbos modelius naudojant Foundry Local CLI  
- Suprasti modelio optimizavimą ir kvantizaciją vietiniam diegimui  
- Įgyvendinti neprisijungus veikiančias AI galimybes, kurios veikia be interneto ryšio  
- Valdyti modelių gyvavimo ciklus ir atnaujinimus gamybos aplinkoje  

**Windows ML diegimas**  
- Integruoti pasirinktinius ONNX modelius į Windows programas naudojant Windows ML  
- Pasinaudoti automatiniu aparatūros pagreičiu per CPU, GPU ir NPU architektūras  
- Įgyvendinti realaus laiko inferenciją su optimaliu resursų panaudojimu  
- Kurti mastelio AI programas įvairioms Windows įrenginių kategorijoms  

### Programų kūrimo įgūdžiai

**Kryžminės platformos Windows kūrimas**  
- Kurti AI galimybes turinčias programas naudojant .NET MAUI universaliam Windows diegimui  
- Integruoti AI funkcijas į Win32, UWP ir progresyvias interneto programas  
- Įgyvendinti prisitaikančius UI dizainus, kurie reaguoja į AI apdorojimo būsenas  
- Tvarkyti asinchronines AI operacijas laikantis tinkamų vartotojo patirties modelių  

**Našumo optimizavimas**  
- Profiluoti ir optimizuoti AI inferencijos našumą skirtingose aparatūros konfigūracijose  
- Įgyvendinti efektyvų atminties valdymą dideliems kalbos modeliams  
- Kurti programas, kurios grakščiai prisitaiko prie turimos aparatūros galimybių  
- Taikyti talpyklos strategijas dažnai naudojamoms AI operacijoms  

**Paruošimas gamybai**  
- Įgyvendinti išsamų klaidų tvarkymą ir atsargines mechanizmus  
- Kurti telemetriją ir stebėjimą AI programų našumui  
- Taikyti saugumo geriausią praktiką vietiniam AI modelių saugojimui ir vykdymui  
- Planuoti diegimo strategijas verslo ir vartotojų programoms  

### Verslo ir strateginis supratimas

**AI programų architektūra**  
- Kurti hibridines architektūras, optimizuojančias vietinį ir debesų AI apdorojimą  
- Įvertinti kompromisus tarp modelio dydžio, tikslumo ir inferencijos greičio  
- Planuoti duomenų srautų architektūras, kurios užtikrina privatumą ir intelektą  
- Įgyvendinti ekonomiškus AI sprendimus, kurie plečiasi pagal vartotojų poreikius  

**Rinkos pozicionavimas**  
- Suprasti konkurencinius pranašumus Windows gimtųjų AI programų  
- Identifikuoti naudojimo atvejus, kur vietinis AI suteikia geresnę vartotojo patirtį  
- Kurti rinkos strategijas AI praturtintoms Windows programoms  
- Pozicionuoti programas, kad pasinaudotų Windows ekosistemos privalumais  

## Windows App SDK AI pavyzdžiai

Windows App SDK siūlo išsamius pavyzdžius, demonstruojančius AI integraciją per įvairias sistemas ir diegimo scenarijus. Šie pavyzdžiai yra esminiai šaltiniai, padedantys suprasti Windows AI kūrimo modelius.

### Windows AI Foundry pavyzdžiai

| Pavyzdys | Sistema | Fokusavimo sritis | Pagrindinės funkcijos |
|----------|---------|-------------------|-----------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API integracija | Pilna WinUI programa, demonstruojanti Windows AI API, ARM64 optimizaciją, supakuotą diegimą |

**Pagrindinės technologijos:**  
- Windows AI API  
- WinUI 3 sistema  
- ARM64 platformos optimizacija  
- Copilot+ PC suderinamumas  
- Supakuotas programos diegimas  

**Reikalavimai:**  
- Windows 11 su Copilot+ PC rekomenduojama  
- Visual Studio 2022  
- ARM64 kūrimo konfigūracija  
- Windows App SDK 1.8.1+  

### Windows ML pavyzdžiai

#### C++ pavyzdžiai

| Pavyzdys | Tipas | Fokusavimo sritis | Pagrindinės funkcijos |
|----------|-------|-------------------|-----------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolės programa | Pagrindinis Windows ML | EP atradimas, komandų eilutės parinktys, modelio kompiliacija |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolės programa | Framework diegimas | Bendras vykdymo laikas, mažesnis diegimo pėdsakas |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolės programa | Savarankiškas diegimas | Savarankiškas diegimas, be vykdymo laiko priklausomybių |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Bibliotekos naudojimas | WindowsML bendroje bibliotekoje, atminties valdymas |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demonstracija | ResNet pamoka | Modelio konversija, EP kompiliacija, Build 2025 pamoka |

#### C# pavyzdžiai

**Konsolės programos**

| Pavyzdys | Tipas | Fokusavimo sritis | Pagrindinės funkcijos |
|----------|-------|-------------------|-----------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolės programa | Pagrindinė C# integracija | Bendras pagalbininkų naudojimas, komandų eilutės sąsaja |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demonstracija | ResNet pamoka | Modelio konversija, EP kompiliacija, Build 2025 pamoka |

**GUI programos**

| Pavyzdys | Sistema | Fokusavimo sritis | Pagrindinės funkcijos |
|----------|---------|-------------------|-----------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Darbalaukio GUI | Vaizdų klasifikacija su WPF sąsaja |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicinis GUI | Vaizdų klasifikacija su Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modernus GUI | Vaizdų klasifikacija su WinUI 3 sąsaja |

#### Python pavyzdžiai

| Pavyzdys | Kalba | Fokusavimo sritis | Pagrindinės funkcijos |
|----------|-------|-------------------|-----------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Vaizdų klasifikacija | WinML Python jungtys, vaizdų apdorojimas partijomis |

### Pavyzdžių reikalavimai

**Sistemos reikalavimai:**  
- Windows 11 kompiuteris, veikiantis versija 24H2 (build 26100) ar naujesnė  
- Visual Studio 2022 su C++ ir .NET darbo krūviais  
- Windows App SDK 1.8.1 ar naujesnė  
- Python 3.10-3.13 Python pavyzdžiams x64 ir ARM64 įrenginiuose  

**Windows AI Foundry specifiniai:**  
- Copilot+ PC rekomenduojama optimaliam našumui  
- ARM64 kūrimo konfigūracija Windows AI pavyzdžiams  
- Reikalinga paketo tapatybė (nepakuotos programos nebepalaikomos)  

### Bendras pavyzdžių darbo procesas

Dauguma Windows ML pavyzdžių laikosi šio standartinio modelio:

1. **Aplinkos inicializavimas** – Sukurti ONNX Runtime aplinką  
2. **Vykdymo teikėjų registracija** – Aptikti ir registruoti galimus aparatūros pagreičius (CPU, GPU, NPU)  
3. **Modelio įkėlimas** – Įkelti ONNX modelį, pasirinktinai kompiliuoti tikslinei aparatūrai  
4. **Įvesties paruošimas** – Konvertuoti vaizdus/duomenis į modelio įvesties formatą  
5. **Inferencijos vykdymas** – Vykdyti modelį ir gauti prognozes  
6. **Rezultatų apdorojimas** – Taikyti softmax ir rodyti geriausias prognozes  

### Naudoti modelio failai

| Modelis | Paskirtis | Įtrauktas | Pastabos |
|---------|----------|----------|---------|
| SqueezeNet | Lengva vaizdų klasifikacija | ✅ Įtrauktas | Iš anksto apmokytas, paruoštas naudoti |
| ResNet-50 | Aukšto tikslumo vaizdų klasifikacija | ❌ Reikia konversijos | Naudokite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) konversijai |

### Aparatūros palaikymas

Visi pavyzdžiai automatiškai aptinka ir naudoja turimą aparatūrą:  
- **CPU** – Universalus palaikymas visiems Windows įrenginiams  
- **GPU** – Automatinis aptikimas ir optimizavimas turimai grafikos aparatūrai  
- **NPU** – Naudoja neuroninius procesorius palaikomuose įrenginiuose (Copilot+ PC)  

## Windows AI Foundry platformos komponentai

### 1. Windows AI API

Windows AI API siūlo paruoštas naudoti AI galimybes, paremtas vietiniais modeliais, optimizuotais efektyvumui ir našumui Copilot+ PC įrenginiuose, su minimaliu nustatymu.

#### Pagrindinės API kategorijos

**Phi Silica kalbos modelis**  
- Mažas, bet galingas kalbos modelis tekstų generavimui ir samprotavimui  
- Optimizuotas realaus laiko inferencijai su minimaliu energijos suvartojimu  
- Palaikymas pritaikymui naudojant LoRA technikas  
- Integracija su Windows semantine paieška ir žinių gavimu  

**Kompiuterinio matymo API**  
- **Teksto atpažinimas (OCR)**: Išgauti tekstą iš vaizdų su aukštu tikslumu  
- **Vaizdų superrezoliucija**: Padidinti vaizdų raišką naudojant vietinius AI modelius  
- **Vaizdų segmentacija**: Identifikuoti ir izoliuoti specifinius objektus vaizduose  
- **Vaizdų aprašymas**: Generuoti detalius tekstinius aprašymus vizualiniam turiniui  
- **Objektų šalinimas**: Pašalinti nereikalingus objektus iš vaizdų naudojant AI pagrįstą inpainting  

**Multimodalinės galimybės**  
- **Vaizdo-teksto integracija**: Sujungti teksto ir vaizdo supratimą  
- **Semantinė paieška**: Įgalinti natūralios kalbos užklausas per multimedijos turinį  
- **Žinių gavimas**: Kurti išmanias paieškos patirtis su vietiniais duomenimis  

### 2. Foundry Local

Foundry Local suteikia kūrėjams greitą prieigą prie paruoštų naudoti atvirojo kodo kalbos modelių Windows Silicon, siūlant galimybę naršyti, testuoti, sąveikauti ir diegti modelius vietinėse programose.

#### Foundry Local pavyzdinės programos

[Foundry Local saugykla](https://github.com/microsoft/Foundry-Local/tree/main/samples) siūlo išsamius pavyzdžius per įvairias programavimo kalbas ir sistemas, demonstruojančius įvairius integracijos modelius
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistemų integracija | Žemo lygio SDK naudojimas, asinchroninės operacijos, reqwest HTTP klientas |

#### Pavyzdžių kategorijos pagal naudojimo atvejį

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Pilna RAG įgyvendinimo schema naudojant Semantic Kernel, Qdrant vektorinę duomenų bazę ir JINA įterpinius
- **Architektūra**: Dokumentų įkėlimas → Teksto skaidymas → Vektoriniai įterpiniai → Panašumo paieška → Kontekstiniai atsakymai
- **Technologijos**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX įterpiniai, srautinio pokalbio užbaigimas

**Darbalaukio programos**
- **electron/foundry-chat**: Gamybai paruošta pokalbių programa su vietinio/debesų modelio perjungimu
- **Funkcijos**: Modelio pasirinkimas, srautiniai atsakymai, klaidų tvarkymas, daugiaplatformis diegimas
- **Architektūra**: Electron pagrindinis procesas, IPC komunikacija, saugūs išankstiniai scenarijai

**SDK integracijos pavyzdžiai**
- **JavaScript (Node.js)**: Pagrindinė modelio sąveika ir srautiniai atsakymai
- **Python**: OpenAI suderinamos API naudojimas su asinchroniniu srautiniu apdorojimu
- **Rust**: Žemo lygio integracija su reqwest ir tokio asinchroninėms operacijoms

#### Foundry Local pavyzdžių reikalavimai

**Sistemos reikalavimai:**
- Windows 11 su įdiegtu Foundry Local
- Node.js v16+ JavaScript/Electron pavyzdžiams
- .NET 8.0+ C# pavyzdžiams
- Python 3.10+ Python pavyzdžiams
- Rust 1.70+ Rust pavyzdžiams

**Įdiegimas:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Pavyzdžių specifinis nustatymas

**dotNET RAG pavyzdys:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron pokalbių pavyzdys:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust pavyzdžiai:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Pagrindinės funkcijos

**Modelių katalogas**
- Išsamus iš anksto optimizuotų atvirojo kodo modelių rinkinys
- Modeliai optimizuoti CPU, GPU ir NPU, kad būtų galima nedelsiant naudoti
- Palaikomi populiarūs modelių šeimos, įskaitant Llama, Mistral, Phi, ir specializuoti domenų modeliai

**CLI integracija**
- Komandinės eilutės sąsaja modelių valdymui ir diegimui
- Automatiniai optimizavimo ir kvantavimo procesai
- Integracija su populiariomis kūrimo aplinkomis ir CI/CD procesais

**Vietinis diegimas**
- Visiškai nepriklausomas nuo debesų veikimas
- Palaikomi individualūs modelių formatai ir konfigūracijos
- Efektyvus modelių aptarnavimas su automatine aparatūros optimizacija

### 3. Windows ML

Windows ML yra pagrindinė AI platforma ir integruota inferencijos aplinka Windows sistemoje, leidžianti kūrėjams efektyviai diegti individualius modelius visoje Windows aparatūros ekosistemoje.

#### Architektūros privalumai

**Universalus aparatūros palaikymas**
- Automatinis optimizavimas AMD, Intel, NVIDIA ir Qualcomm lustams
- CPU, GPU ir NPU vykdymo palaikymas su skaidriu perjungimu
- Aparatūros abstrakcija, pašalinanti platformos specifinio optimizavimo poreikį

**Modelių lankstumas**
- ONNX modelio formato palaikymas su automatiniu konvertavimu iš populiarių sistemų
- Individualių modelių diegimas su gamybos lygio našumu
- Integracija su esamomis Windows programų architektūromis

**Įmonių integracija**
- Suderinamumas su Windows saugumo ir atitikties sistemomis
- Palaikymas įmonių diegimo ir valdymo įrankiams
- Integracija su Windows įrenginių valdymo ir stebėjimo sistemomis

## Kūrimo procesas

### 1 etapas: Aplinkos paruošimas ir įrankių konfigūracija

**Kūrimo aplinkos paruošimas**
1. Įdiekite Visual Studio 2022 su C++ ir .NET darbo krūviais
2. Įdiekite Windows App SDK 1.8.1 ar naujesnę versiją
3. Konfigūruokite Windows AI Foundry CLI įrankius
4. Nustatykite AI Toolkit plėtinį Visual Studio Code
5. Įdiekite našumo profiliavimo ir stebėjimo įrankius
6. Užtikrinkite ARM64 kūrimo konfigūraciją Copilot+ PC optimizavimui

**Pavyzdžių saugyklos nustatymas**
1. Nukopijuokite [Windows App SDK Samples saugyklą](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Eikite į `Samples/WindowsAIFoundry/cs-winui`, kad rastumėte Windows AI API pavyzdžius
3. Eikite į `Samples/WindowsML`, kad rastumėte išsamius Windows ML pavyzdžius
4. Peržiūrėkite [kūrimo reikalavimus](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) savo tikslinėms platformoms

**AI kūrimo galerijos tyrinėjimas**
- Tyrinėkite pavyzdines programas ir nuorodines įgyvendinimo schemas
- Testuokite Windows AI API su interaktyviais demonstraciniais pavyzdžiais
- Peržiūrėkite šaltinio kodą, kad rastumėte geriausias praktikas ir šablonus
- Nustatykite tinkamus pavyzdžius savo specifiniam naudojimo atvejui

### 2 etapas: Modelio pasirinkimas ir integracija

**Reikalavimų analizė**
- Apibrėžkite AI funkcionalumo reikalavimus
- Nustatykite našumo apribojimus ir optimizavimo tikslus
- Įvertinkite privatumo ir saugumo reikalavimus
- Planuokite diegimo architektūrą ir mastelio strategijas

**Modelio vertinimas**
- Naudokite Foundry Local, kad išbandytumėte atvirojo kodo modelius savo naudojimo atvejui
- Atlikite Windows AI API našumo testus pagal individualių modelių reikalavimus
- Įvertinkite kompromisus tarp modelio dydžio, tikslumo ir inferencijos greičio
- Sukurkite prototipus su pasirinktais modeliais

### 3 etapas: Programos kūrimas

**Pagrindinė integracija**
- Įgyvendinkite Windows AI API integraciją su tinkamu klaidų tvarkymu
- Sukurkite vartotojo sąsajas, kurios atitiktų AI apdorojimo darbo eigas
- Įgyvendinkite talpyklos ir optimizavimo strategijas modelio inferencijai
- Pridėkite telemetriją ir stebėjimą AI veikimo našumui

**Testavimas ir validacija**
- Testuokite programas įvairiose Windows aparatūros konfigūracijose
- Patikrinkite našumo rodiklius esant skirtingoms apkrovos sąlygoms
- Įgyvendinkite automatizuotą testavimą AI funkcionalumo patikimumui
- Atlikite vartotojo patirties testavimą su AI patobulintomis funkcijomis

### 4 etapas: Optimizavimas ir diegimas

**Našumo optimizavimas**
- Profilinkite programos našumą įvairiose tikslinėse aparatūros konfigūracijose
- Optimizuokite atminties naudojimą ir modelio įkėlimo strategijas
- Įgyvendinkite adaptyvų elgesį pagal turimus aparatūros pajėgumus
- Patobulinkite vartotojo patirtį skirtingiems našumo scenarijams

**Gamybinis diegimas**
- Supakuokite programas su tinkamomis AI modelio priklausomybėmis
- Įgyvendinkite atnaujinimo mechanizmus modeliams ir programos logikai
- Konfigūruokite stebėjimą ir analizę gamybinėms aplinkoms
- Planuokite diegimo strategijas įmonėms ir vartotojams

## Praktiniai įgyvendinimo pavyzdžiai

### Pavyzdys 1: Išmanioji dokumentų apdorojimo programa

Sukurkite Windows programą, kuri apdoroja dokumentus naudodama kelias AI galimybes:

**Naudotos technologijos:**
- Phi Silica dokumentų santraukų ir klausimų-atsakymų funkcijoms
- OCR API tekstui iš nuskaitytų dokumentų išgauti
- Vaizdo aprašymo API diagramų ir grafikų analizei
- Individualūs ONNX modeliai dokumentų klasifikavimui

**Įgyvendinimo metodas:**
- Sukurkite modulinę architektūrą su prijungiamais AI komponentais
- Įgyvendinkite asinchroninį apdorojimą didelėms dokumentų partijoms
- Pridėkite progreso indikatorius ir atšaukimo palaikymą ilgai trunkančioms operacijoms
- Įtraukite neprisijungimo galimybę jautrių dokumentų apdorojimui

### Pavyzdys 2: Mažmeninės prekybos inventoriaus valdymo sistema

Sukurkite AI pagrįstą inventoriaus sistemą mažmeninės prekybos programoms:

**Naudotos technologijos:**
- Vaizdo segmentacija produktų identifikavimui
- Individualūs vizijos modeliai prekės ženklo ir kategorijos klasifikavimui
- Foundry Local specializuotų mažmeninės prekybos kalbos modelių diegimas
- Integracija su esamomis POS ir inventoriaus sistemomis

**Įgyvendinimo metodas:**
- Sukurkite kamerų integraciją realaus laiko produktų skenavimui
- Įgyvendinkite brūkšninių kodų ir vizualinį produktų atpažinimą
- Pridėkite natūralios kalbos inventoriaus užklausas naudodami vietinius kalbos modelius
- Sukurkite mastelio architektūrą daugelio parduotuvių diegimui

### Pavyzdys 3: Sveikatos priežiūros dokumentacijos asistentas

Sukurkite privatumo užtikrinančią sveikatos priežiūros dokumentacijos priemonę:

**Naudotos technologijos:**
- Phi Silica medicininių užrašų generavimui ir klinikinių sprendimų palaikymui
- OCR ranka rašytų medicininių įrašų skaitmeninimui
- Individualūs medicininiai kalbos modeliai, diegiami per Windows ML
- Vietinė vektorinė saugykla medicininių žinių paieškai

**Įgyvendinimo metodas:**
- Užtikrinkite visiškai neprisijungusį veikimą pacientų privatumui
- Įgyvendinkite medicininės terminologijos validaciją ir pasiūlymus
- Pridėkite audito žurnalus reguliavimo atitikties užtikrinimui
- Sukurkite integraciją su esamomis elektroninėmis sveikatos įrašų sistemomis

## Našumo optimizavimo strategijos

### Aparatūros sąmoningas kūrimas

**NPU optimizavimas**
- Sukurkite programas, kurios išnaudoja NPU galimybes Copilot+ PC
- Įgyvendinkite sklandų perėjimą prie GPU/CPU įrenginiuose be NPU
- Optimizuokite modelių formatus NPU specifiniam pagreitinimui
- Stebėkite NPU naudojimą ir šilumines charakteristikas

**Atminties valdymas**
- Įgyvendinkite efektyvias modelių įkėlimo ir talpyklos strategijas
- Naudokite atminties žemėlapį dideliems modeliams, kad sumažintumėte paleidimo laiką
- Sukurkite atminties sąmoningas programas ribotų išteklių įrenginiams
- Įgyvendinkite modelių kvantavimą atminties optimizavimui

**Baterijos efektyvumas**
- Optimizuokite AI operacijas minimaliam energijos suvartojimui
- Įgyvendinkite adaptyvų apdorojimą pagal baterijos būklę
- Sukurkite efektyvų foninį apdorojimą nuolatinėms AI operacijoms
- Naudokite energijos profiliavimo įrankius energijos naudojimui optimizuoti

### Mastelio didinimo svarstymai

**Daugiasriegis apdorojimas**
- Sukurkite sriegio saugias AI operacijas lygiagrečiam apdorojimui
- Įgyvendinkite efektyvų darbo paskirstymą tarp turimų branduolių
- Naudokite asinchroninius modelius neblokuojančioms AI operacijoms
- Planuokite sriegio baseino optimizavimą skirtingoms aparatūros konfigūracijoms

**Talpyklos strategijos**
- Įgyvendinkite intelektualią talpyklą dažnai naudojamoms AI operacijoms
- Sukurkite talpyklos atnaujinimo strategijas modelių atnaujinimams
- Naudokite nuolatinę talpyklą brangiems išankstinio apdorojimo veiksmams
- Įgyvendinkite paskirstytą talpyklą kelių vartotojų scenarijams

## Saugumo ir privatumo geriausios praktikos

### Duomenų apsauga

**Vietinis apdorojimas**
- Užtikrinkite, kad jautrūs duomenys niekada nepaliktų vietinio įrenginio
- Įgyvendinkite saugų saugojimą AI modeliams ir laikiniesiems duomenims
- Naudokite Windows saugumo funkcijas programų smėlio dėžėms
- Taikykite šifravimą saugomiems modeliams ir tarpiniams apdorojimo rezultatams

**Modelio saugumas**
- Patikrinkite modelio vientisumą prieš įkėlimą ir vykdymą
- Įgyvendinkite saugius modelių atnaujinimo mechanizmus
- Naudokite pasirašytus modelius, kad išvengtumėte klastojimo
- Taikykite prieigos kontrolę modelių failams ir konfigūracijoms

### Atitikties svarstymai

**Reguliavimo suderinamumas**
- Sukurkite programas, atitinkančias GDPR, HIPAA ir kitus reguliavimo reikalavimus
- Įgyvendinkite audito žurnalus AI sprendimų priėmimo procesams
- Suteikite skaidrumo funkcijas AI generuotiems rezultatams
- Leiskite vartotojams kontroliuoti AI duomenų apdorojimą

**Įmonių saugumas**
- Integruokite su Windows įmonių saugumo politikomis
- Palaikykite valdomą diegimą per įmonių valdymo įrankius
- Įgyvendinkite vaidmenimis pagrįstą prieigos kontrolę AI funkcijoms
- Suteikite administracines AI funkcionalumo valdymo galimybes

## Trikčių šalinimas ir derinimas

### Dažniausios kūrimo problemos

**Kūrimo konfigūracijos problemos**
- Užtikrinkite ARM64 platformos konfigūraciją Windows AI API pavyzdžiams
- Patikrinkite Windows App SDK versijos suderinamumą (reikalinga 1.8.1+)
- Patikrinkite, ar paketo tapatybė tinkamai sukonfigūruota (reikalinga Windows AI API)
- Patikrinkite, ar kūrimo įrankiai palaiko tikslinės sistemos versiją

**Modelio įkėlimo problemos**
- Patikrinkite ONNX modelio suderinamumą su Windows ML
- Patikrinkite modelio failo vientisumą ir formato reikalavimus
- Patikrinkite aparatūros pajėgumų reikalavimus specifiniams modeliams
- Derinkite atminties paskirstymo problemas modelio įkėlimo metu
- Užtikrinkite vykdymo teikėjo registraciją aparatūros pagreitinimui

**Diegimo režimo svarstymai**
- **Savarankiškas režimas**: Visiškai palaikomas, bet su didesniu diegimo dydžiu
- **Priklausomas nuo sistemos režimas**: Mažesnis dydis, bet reikalauja bendro vykdymo
- [Windows ML apžvalga](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK sistemos reikalavimai](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK kūrimo aplinkos nustatymas](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Pavyzdžių saugyklos ir kodas
- [Windows App SDK pavyzdžiai - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK pavyzdžiai - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime įžvalgų pavyzdžiai](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK pavyzdžių saugykla](https://github.com/microsoft/WindowsAppSDK-Samples)

### Kūrimo įrankiai
- [AI įrankių rinkinys Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI kūrėjų galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI pavyzdžiai](https://learn.microsoft.com/windows/ai/samples/)
- [Modelių konvertavimo įrankiai](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Techninė pagalba
- [Windows ML dokumentacija](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime dokumentacija](https://onnxruntime.ai/docs/)
- [Windows App SDK dokumentacija](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Pranešti apie problemas - Windows App SDK pavyzdžiai](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Bendruomenė ir palaikymas
- [Windows kūrėjų bendruomenė](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry tinklaraštis](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI mokymai](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Šis vadovas sukurtas taip, kad prisitaikytų prie sparčiai besivystančios Windows AI ekosistemos. Reguliarūs atnaujinimai užtikrina suderinamumą su naujausiomis platformos galimybėmis ir geriausiomis kūrimo praktikomis.*

[08. Praktinis darbas su Microsoft Foundry Local - pilnas kūrėjo įrankių rinkinys](../Module08/README.md)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.