# Windows Edge AI Arenduse Juhend

## Sissejuhatus

Tere tulemast Windows Edge AI arenduse juhendisse – teie põhjalik juhend intelligentsete rakenduste loomiseks, mis kasutavad Microsofti Windows AI Foundry platvormi seadmesisest tehisintellekti. See juhend on mõeldud spetsiaalselt Windowsi arendajatele, kes soovivad integreerida oma rakendustesse tipptasemel Edge AI võimalusi, kasutades ära Windowsi riistvara kiirenduse täielikku potentsiaali.

### Windows AI eelised

Windows AI Foundry on ühtne, usaldusväärne ja turvaline platvorm, mis toetab kogu tehisintellekti arenduse elutsüklit – alates mudeli valikust ja peenhäälestusest kuni optimeerimise ja juurutamiseni CPU, GPU, NPU ja hübriidpilve arhitektuurides. See platvorm demokratiseerib tehisintellekti arendust, pakkudes:

- **Riistvara abstraktsioon**: sujuv juurutamine AMD, Inteli, NVIDIA ja Qualcomi kiipidel
- **Seadmesisene intelligentsus**: privaatsust säilitav tehisintellekt, mis töötab täielikult kohalikul riistvaral
- **Optimeeritud jõudlus**: mudelid, mis on eeloptimeeritud Windowsi riistvara konfiguratsioonide jaoks
- **Ettevõttevalmidus**: tootmisklassi turvalisus ja vastavusnõuded

### Windows ML
Windows Machine Learning (ML) võimaldab C#, C++ ja Python arendajatel käivitada ONNX tehisintellekti mudeleid kohapeal Windowsi arvutites, kasutades ONNX Runtime'i, mis haldab automaatselt erinevate riistvarade (CPU, GPU, NPU) täitmise pakkujaid. [ONNX Runtime](https://onnxruntime.ai/docs/) ühildub mudelitega, mis on loodud PyTorch, Tensorflow/Keras, TFLite, scikit-learn ja teiste raamistikudega.

![WindowsML Diagramm, mis illustreerib ONNX mudeli liikumist Windows ML kaudu NPU-de, GPU-de ja CPU-de juurde.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML pakub jagatud Windowsi ulatuses ONNX Runtime'i koopiat ning võimalust dünaamiliselt alla laadida täitmise pakkujaid (EP-sid).

### Miks valida Windows Edge AI jaoks?

**Universaalne riistvaratugi**  
Windows ML pakub automaatset riistvara optimeerimist kogu Windowsi ökosüsteemis, tagades, et teie tehisintellekti rakendused töötavad optimaalselt sõltumata aluseks olevast kiipide arhitektuurist.

**Integreeritud tehisintellekti käitusaeg**  
Sisseehitatud Windows ML järeldusmootor kõrvaldab keerulised seadistamisnõuded, võimaldades arendajatel keskenduda rakenduse loogikale, mitte infrastruktuuri probleemidele.

**Copilot+ PC optimeerimine**  
Spetsiaalselt loodud API-d järgmise põlvkonna Windowsi seadmete jaoks, millel on pühendatud närvitöötlusüksused (NPU-d), pakkudes erakordset jõudlust vati kohta.

**Arendajate ökosüsteem**  
Rikkalik tööriistakomplekt, sealhulgas Visual Studio integratsioon, põhjalik dokumentatsioon ja näidisrakendused, mis kiirendavad arendustsükleid.

## Õpieesmärgid

Selle Windows Edge AI arenduse juhendi läbimisega omandate olulised oskused tootmisvalmis tehisintellekti rakenduste loomiseks Windowsi platvormil.

### Põhitehnilised pädevused

**Windows AI Foundry valdamine**  
- Mõista Windows AI Foundry platvormi arhitektuuri ja komponente  
- Navigeerida kogu tehisintellekti arenduse elutsüklis Windowsi ökosüsteemis  
- Rakendada turvalisuse parimaid tavasid seadmesiseste tehisintellekti rakenduste jaoks  
- Optimeerida rakendusi erinevate Windowsi riistvara konfiguratsioonide jaoks  

**API integratsiooni ekspertiis**  
- Valda Windows AI API-sid teksti, visiooni ja multimodaalsete rakenduste jaoks  
- Rakenda Phi Silica keelemudeli integreerimist teksti genereerimiseks ja põhjendamiseks  
- Juuruta arvutinägemise võimalusi, kasutades sisseehitatud pilditöötluse API-sid  
- Kohanda eelnevalt treenitud mudeleid, kasutades LoRA (Low-Rank Adaptation) tehnikaid  

**Foundry Local rakendamine**  
- Sirvi, hinda ja juuruta avatud lähtekoodiga keelemudeleid, kasutades Foundry Local CLI-d  
- Mõista mudelite optimeerimist ja kvantifitseerimist kohalikuks juurutamiseks  
- Rakenda võrguühenduseta tehisintellekti võimalusi, mis töötavad ilma internetiühenduseta  
- Halda mudelite elutsükleid ja värskendusi tootmiskeskkondades  

**Windows ML juurutamine**  
- Too kohandatud ONNX mudelid Windowsi rakendustesse, kasutades Windows ML-i  
- Kasuta automaatset riistvara kiirendust CPU, GPU ja NPU arhitektuurides  
- Rakenda reaalajas järeldusi optimaalse ressursikasutusega  
- Kujunda skaleeritavaid tehisintellekti rakendusi erinevatele Windowsi seadmekategooriatele  

### Rakenduste arendamise oskused

**Platvormidevaheline Windowsi arendus**  
- Loo tehisintellektiga varustatud rakendusi, kasutades .NET MAUI-d universaalseks Windowsi juurutamiseks  
- Integreeri tehisintellekti võimalusi Win32, UWP ja progressiivsetesse veebirakendustesse  
- Rakenda reageerivaid kasutajaliidese kujundusi, mis kohanduvad tehisintellekti töötlemise olekutega  
- Käsitle asünkroonseid tehisintellekti toiminguid, järgides õigeid kasutajakogemuse mustreid  

**Jõudluse optimeerimine**  
- Profiili ja optimeeri tehisintellekti järelduste jõudlust erinevate riistvara konfiguratsioonide vahel  
- Rakenda tõhusat mäluhaldust suurte keelemudelite jaoks  
- Kujunda rakendusi, mis degradeeruvad sujuvalt vastavalt saadaolevatele riistvaravõimalustele  
- Kasuta vahemälu strateegiaid sageli kasutatavate tehisintellekti toimingute jaoks  

**Tootmisvalmidus**  
- Rakenda põhjalikku vigade käsitlemist ja varumehhanisme  
- Kujunda telemeetria ja jälgimine tehisintellekti rakenduste jõudluse jaoks  
- Rakenda turvalisuse parimaid tavasid kohalike tehisintellekti mudelite salvestamiseks ja käitamiseks  
- Planeeri juurutusstrateegiaid ettevõtete ja tarbijarakenduste jaoks  

### Äri- ja strateegiline arusaam

**Tehisintellekti rakenduste arhitektuur**  
- Kujunda hübriidarhitektuure, mis optimeerivad kohaliku ja pilve tehisintellekti töötlemise vahel  
- Hinda kompromisse mudeli suuruse, täpsuse ja järelduskiiruse vahel  
- Planeeri andmevoo arhitektuure, mis säilitavad privaatsuse, võimaldades samal ajal intelligentsust  
- Rakenda kulutõhusaid tehisintellekti lahendusi, mis skaleeruvad vastavalt kasutajate nõudmistele  

**Turupositsioneerimine**  
- Mõista Windowsi-põhiste tehisintellekti rakenduste konkurentsieeliseid  
- Tuvasta kasutusjuhtumid, kus seadmesisene tehisintellekt pakub paremat kasutajakogemust  
- Arenda turule sisenemise strateegiaid tehisintellektiga täiustatud Windowsi rakenduste jaoks  
- Positsioneeri rakendusi, et kasutada ära Windowsi ökosüsteemi eeliseid  

## Windows App SDK AI näidised

Windows App SDK pakub põhjalikke näidiseid, mis demonstreerivad tehisintellekti integreerimist mitmesugustes raamistikus ja juurutusstsenaariumides. Need näidised on olulised viited Windowsi tehisintellekti arenduse mustrite mõistmiseks.

### Windows AI Foundry näidised

| Näidis | Raamistik | Fookusala | Põhifunktsioonid |
|--------|-----------|-----------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API-de integreerimine | Täielik WinUI rakendus, mis demonstreerib Windows AI API-sid, ARM64 optimeerimist, pakendatud juurutust |

**Põhitehnoloogiad:**  
- Windows AI API-d  
- WinUI 3 raamistik  
- ARM64 platvormi optimeerimine  
- Copilot+ PC ühilduvus  
- Pakendatud rakenduse juurutus  

**Eeltingimused:**  
- Windows 11 koos Copilot+ PC soovitatav  
- Visual Studio 2022  
- ARM64 ehituse konfiguratsioon  
- Windows App SDK 1.8.1+  

### Windows ML näidised

#### C++ näidised

| Näidis | Tüüp | Fookusala | Põhifunktsioonid |
|--------|------|-----------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Põhiline Windows ML | EP avastamine, käsurea valikud, mudeli kompileerimine |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Raamistiku juurutus | Jagatud käitusaeg, väiksem juurutusmaht |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Iseseisev juurutus | Iseseisev juurutus, ilma käitusaja sõltuvusteta |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Raamatukogu kasutamine | WindowsML jagatud raamatukogus, mäluhaldus |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet õpetus | Mudeli teisendamine, EP kompileerimine, Build 2025 õpetus |

#### C# näidised

**Konsoolirakendused**

| Näidis | Tüüp | Fookusala | Põhifunktsioonid |
|--------|------|-----------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsoolirakendus | Põhiline C# integreerimine | Jagatud abivahendite kasutamine, käsurealiides |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet õpetus | Mudeli teisendamine, EP kompileerimine, Build 2025 õpetus |

**GUI rakendused**

| Näidis | Raamistik | Fookusala | Põhifunktsioonid |
|--------|-----------|-----------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Lauaarvuti GUI | Pildiklassifikatsioon WPF liidesega |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditsiooniline GUI | Pildiklassifikatsioon Windows Formsiga |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Kaasaegne GUI | Pildiklassifikatsioon WinUI 3 liidesega |

#### Python näidised

| Näidis | Keel | Fookusala | Põhifunktsioonid |
|--------|------|-----------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Pildiklassifikatsioon | WinML Python sidumised, partii pilditöötlus |

### Näidiste eeltingimused

**Süsteeminõuded:**  
- Windows 11 arvuti, mis töötab versioonil 24H2 (ehitus 26100) või uuemal  
- Visual Studio 2022 koos C++ ja .NET töökoormustega  
- Windows App SDK 1.8.1 või uuem  
- Python 3.10-3.13 Python näidiste jaoks x64 ja ARM64 seadmetel  

**Windows AI Foundry spetsiifiline:**  
- Copilot+ PC soovitatav optimaalse jõudluse jaoks  
- ARM64 ehituse konfiguratsioon Windows AI näidiste jaoks  
- Paketi identiteet vajalik (pakendamata rakendusi enam ei toetata)  

### Tavaline näidiste töövoog

Enamik Windows ML näidiseid järgib seda standardset mustrit:

1. **Keskkonna algatamine** – Loo ONNX Runtime keskkond  
2. **Täitmise pakkujate registreerimine** – Avasta ja registreeri saadaolevad riistvara kiirendid (CPU, GPU, NPU)  
3. **Mudeli laadimine** – Laadi ONNX mudel, vajadusel kompileeri sihtriistvara jaoks  
4. **Sisendi eeltöötlus** – Konverteeri pildid/andmed mudeli sisendi formaati  
5. **Järelduse käivitamine** – Käivita mudel ja saa prognoosid  
6. **Tulemuste töötlemine** – Rakenda softmax ja kuva parimad prognoosid  

### Kasutatavad mudelid

| Mudel | Eesmärk | Kaasas | Märkused |
|-------|---------|--------|----------|
| SqueezeNet | Kerge pildiklassifikatsioon | ✅ Kaasas | Eeltreenitud, kasutusvalmis |
| ResNet-50 | Kõrge täpsusega pildiklassifikatsioon | ❌ Vajab teisendamist | Kasuta [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) teisendamiseks |

### Riistvara tugi

Kõik näidised avastavad ja kasutavad automaatselt saadaolevat riistvara:  
- **CPU** – Universaalne tugi kõigil Windowsi seadmetel  
- **GPU** – Automaatne avastamine ja optimeerimine saadaoleva graafikariistvara jaoks  
- **NPU** – Kasutab närvitöötlusüksusi toetatud seadmetel (Copilot+ PC-d)  

## Windows AI Foundry platvormi komponendid

### 1. Windows AI API-d

Windows AI API-d pakuvad kasutusvalmis tehisintellekti võimalusi, mida toetavad seadmesisesed mudelid, optimeeritud tõhususe ja jõudluse jaoks Copilot+ PC seadmetel, vajades minimaalset seadistust.

#### Põhilised API kategooriad

**Phi Silica keelemudel**  
- Väike, kuid võimas keelemudel teksti genereerimiseks ja põhjendamiseks  
- Optimeeritud reaalajas järelduste jaoks minimaalse energiatarbega  
- Toetus kohandatud peenhäälestusele, kasutades LoRA tehnikaid  
- Integreerimine Windowsi semantilise otsingu ja teadmiste hankimisega  

**Arvutinägemise API-d**  
- **Tekstituvastus (OCR)**: Ekstraktige teksti piltidelt suure täpsusega  
- **Pildi superresolutsioon**: Suurendage pilte, kasutades kohalikke tehisintellekti mudeleid  
- **Pildi segmenteerimine**: Tuvastage ja eraldage piltidel kindlaid objekte  
- **Pildi kirjeldus**: Genereerige visuaalse sisu jaoks üksikasjalikke tekstikirjeldusi  
- **Objekti kustutamine**: Eemaldage soovimatud objektid piltidelt, kasutades tehisintellekti-põhist täitmist  

**Multimodaalsed võimalused**  
- **Visiooni ja keele integreerimine**: Kombineerige teksti ja pildi mõistmine  
- **Semantiline otsing**: Võimaldage loomuliku keele päringuid multimeediumisisu kaudu  
- **Teadmiste hankimine**: Looge intelligentsed otsingukogemused kohalike andmetega  

### 2. Foundry Local

Foundry Local pakub arendajatele kiiret juurdepääsu kasutusvalmis avatud lähtekoodiga keelemudelitele Windowsi kiipidel, võimaldades mudeleid sirvida, testida, kasutada ja juurutada kohalikes rakendustes.

#### Foundry Local näidisrakendused

[Foundry Local repository](https://github.com/microsoft/Foundry
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Süsteemide integreerimine | Madala taseme SDK kasutamine, asünkroonsed operatsioonid, reqwest HTTP klient |

#### Näidiskategooriad kasutusjuhtude järgi

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Täielik RAG-i rakendus, mis kasutab Semantic Kernelit, Qdrant vektoriandmebaasi ja JINA embeddings'eid
- **Arhitektuur**: Dokumentide sisestamine → Teksti tükeldamine → Vektori embeddings → Sarnasuse otsing → Kontekstitundlikud vastused
- **Tehnoloogiad**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, voogedastusega vestluse lõpetamine

**Töölauarakendused**
- **electron/foundry-chat**: Tootmisvalmis vestlusrakendus, mis võimaldab mudelite vahetamist lokaalse ja pilve vahel
- **Funktsioonid**: Mudeli valik, voogedastusega vastused, veakäsitlus, platvormidevaheline juurutamine
- **Arhitektuur**: Electroni põhiprotsess, IPC suhtlus, turvalised eelkoormusskriptid

**SDK integreerimise näited**
- **JavaScript (Node.js)**: Põhiline mudeli interaktsioon ja voogedastusega vastused
- **Python**: OpenAI-ga ühilduva API kasutamine asünkroonse voogedastusega
- **Rust**: Madala taseme integreerimine reqwest'i ja tokio abil asünkroonsete operatsioonide jaoks

#### Foundry Local näidiste eeldused

**Süsteeminõuded:**
- Windows 11 koos paigaldatud Foundry Localiga
- Node.js v16+ JavaScripti/Electroni näidiste jaoks
- .NET 8.0+ C# näidiste jaoks
- Python 3.10+ Pythoni näidiste jaoks
- Rust 1.70+ Rusti näidiste jaoks

**Paigaldamine:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Näidispõhine seadistus

**dotNET RAG näidis:**
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

**Electroni vestlusrakenduse näidis:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScripti/Pythoni/Rusti näidised:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Põhifunktsioonid

**Mudelikataloog**
- Ulatuslik kollektsioon eeloptimeeritud avatud lähtekoodiga mudeleid
- Mudelid optimeeritud CPU-de, GPU-de ja NPU-de jaoks koheseks juurutamiseks
- Tugi populaarsetele mudeliperekondadele, sealhulgas Llama, Mistral, Phi ja spetsialiseeritud valdkonnamudelid

**CLI integreerimine**
- Käsurealiides mudelite haldamiseks ja juurutamiseks
- Automaatne optimeerimise ja kvantimise töövoog
- Integreerimine populaarsete arenduskeskkondade ja CI/CD torujuhtmetega

**Lokaalne juurutamine**
- Täielik võrguühenduseta töö ilma pilve sõltuvusteta
- Tugi kohandatud mudeliformaatidele ja konfiguratsioonidele
- Tõhus mudelite teenindamine automaatse riistvara optimeerimisega

### 3. Windows ML

Windows ML toimib Windowsi põhitehisintellekti platvormina ja integreeritud järeldusmootorina, võimaldades arendajatel tõhusalt juurutada kohandatud mudeleid laias Windowsi riistvarakeskkonnas.

#### Arhitektuuri eelised

**Universaalne riistvaratugi**
- Automaatne optimeerimine AMD, Inteli, NVIDIA ja Qualcomi kiipide jaoks
- Tugi CPU, GPU ja NPU täitmisele koos läbipaistva vahetamisega
- Riistvara abstraktsioon, mis kõrvaldab platvormispetsiifilise optimeerimistöö

**Mudelite paindlikkus**
- Tugi ONNX mudeliformaadile koos automaatse konversiooniga populaarsetest raamistikest
- Kohandatud mudelite juurutamine tootmiskvaliteediga jõudlusega
- Integreerimine olemasolevate Windowsi rakenduste arhitektuuridega

**Ettevõtte integreerimine**
- Ühilduvus Windowsi turvalisuse ja vastavusraamistikega
- Tugi ettevõtte juurutamise ja haldustööriistadele
- Integreerimine Windowsi seadmehalduse ja jälgimissüsteemidega

## Arendustöövoog

### Faas 1: Keskkonna seadistamine ja tööriistade konfigureerimine

**Arenduskeskkonna ettevalmistamine**
1. Paigalda Visual Studio 2022 koos C++ ja .NET töökoormustega
2. Paigalda Windows App SDK 1.8.1 või uuem
3. Konfigureeri Windows AI Foundry CLI tööriistad
4. Seadista AI Toolkit laiendus Visual Studio Code'i jaoks
5. Loo jõudluse profileerimise ja jälgimise tööriistad
6. Veendu ARM64 ehituse konfiguratsioonis Copilot+ PC optimeerimiseks

**Näidiste repo seadistamine**
1. Klooni [Windows App SDK näidiste repo](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Liigu `Samples/WindowsAIFoundry/cs-winui` kataloogi Windows AI API näidiste jaoks
3. Liigu `Samples/WindowsML` kataloogi põhjalike Windows ML näidiste jaoks
4. Vaata üle [ehitusnõuded](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) sihtplatvormide jaoks

**AI arenduse galerii uurimine**
- Uuri näidisrakendusi ja viiteimplementatsioone
- Testi Windows AI API-sid interaktiivsete demonstratsioonidega
- Vaata lähtekoodi parimate praktikate ja mustrite jaoks
- Tuvasta asjakohased näidised oma konkreetse kasutusjuhtumi jaoks

### Faas 2: Mudeli valik ja integreerimine

**Nõuete analüüs**
- Määra tehisintellekti funktsionaalsed nõuded
- Sea jõudluspiirangud ja optimeerimise eesmärgid
- Hinda privaatsuse ja turvalisuse nõudeid
- Planeeri juurutamise arhitektuur ja skaleerimisstrateegiad

**Mudeli hindamine**
- Kasuta Foundry Locali avatud lähtekoodiga mudelite testimiseks oma kasutusjuhtumi jaoks
- Võrdle Windows AI API-sid kohandatud mudelinõuete vastu
- Hinda kompromisse mudeli suuruse, täpsuse ja järelduskiiruse vahel
- Prototüübi integreerimisviise valitud mudelitega

### Faas 3: Rakenduse arendamine

**Põhiintegreerimine**
- Rakenda Windows AI API integreerimine koos korrektse veakäsitlusega
- Kujunda kasutajaliidesed, mis arvestavad tehisintellekti töövoogudega
- Rakenda vahemälu ja optimeerimisstrateegiad mudeli järeldamiseks
- Lisa telemeetria ja jälgimine tehisintellekti tööjõudluse jaoks

**Testimine ja valideerimine**
- Testi rakendusi erinevates Windowsi riistvarakonfiguratsioonides
- Kinnita jõudlusmõõdikud erinevate koormustingimuste all
- Rakenda automatiseeritud testimine tehisintellekti funktsionaalsuse usaldusväärsuse jaoks
- Teosta kasutajakogemuse testimine tehisintellekti täiustatud funktsioonidega

### Faas 4: Optimeerimine ja juurutamine

**Jõudluse optimeerimine**
- Profileeri rakenduse jõudlust sihtriistvara konfiguratsioonides
- Optimeeri mälu kasutust ja mudeli laadimisstrateegiaid
- Rakenda adaptiivne käitumine vastavalt saadavalolevale riistvarale
- Peenhäälesta kasutajakogemus erinevate jõudlusstsenaariumide jaoks

**Tootmise juurutamine**
- Paki rakendused koos korrektsete tehisintellekti mudelite sõltuvustega
- Rakenda mudelite ja rakendusloogika uuendusmehhanismid
- Konfigureeri jälgimine ja analüütika tootmiskeskkondade jaoks
- Planeeri juurutusstrateegiad ettevõtte ja tarbijate jaoks

## Praktilised rakendusnäited

### Näide 1: Nutikas dokumenditöötlusrakendus

Loo Windowsi rakendus, mis töötleb dokumente mitme tehisintellekti funktsiooni abil:

**Kasutatud tehnoloogiad:**
- Phi Silica dokumentide kokkuvõtete ja küsimustele vastamise jaoks
- OCR API-d skaneeritud dokumentidest teksti eraldamiseks
- Pildikirjelduse API-d diagrammide ja graafikute analüüsiks
- Kohandatud ONNX mudelid dokumentide klassifitseerimiseks

**Rakendamise lähenemine:**
- Kujunda modulaarne arhitektuur koos pistikprogrammidega tehisintellekti komponentide jaoks
- Rakenda asünkroonne töötlemine suurte dokumentide partiide jaoks
- Lisa edenemise indikaatorid ja tühistamise tugi pikaajaliste operatsioonide jaoks
- Kaasa võrguühenduseta võimekus tundlike dokumentide töötlemiseks

### Näide 2: Jaemüügi inventari haldussüsteem

Loo tehisintellekti juhitud inventari haldussüsteem jaemüügirakenduste jaoks:

**Kasutatud tehnoloogiad:**
- Pildisegmentatsioon toodete tuvastamiseks
- Kohandatud visioonimudelid brändi ja kategooria klassifitseerimiseks
- Foundry Locali juurutatud spetsialiseeritud jaemüügi keelemudelid
- Integreerimine olemasolevate POS- ja inventarisüsteemidega

**Rakendamise lähenemine:**
- Loo kaameraintegratsioon reaalajas toodete skaneerimiseks
- Rakenda triipkoodide ja visuaalsete toodete tuvastamine
- Lisa loomuliku keele inventari päringud kohalike keelemudelite abil
- Kujunda skaleeritav arhitektuur mitme poe juurutamiseks

### Näide 3: Tervishoiu dokumentatsiooni assistent

Arenda privaatsust säilitav tervishoiu dokumentatsiooni tööriist:

**Kasutatud tehnoloogiad:**
- Phi Silica meditsiiniliste märkmete genereerimiseks ja kliiniliste otsuste toetamiseks
- OCR käsitsi kirjutatud meditsiiniliste dokumentide digiteerimiseks
- Kohandatud meditsiinilised keelemudelid, mis on juurutatud Windows ML-i kaudu
- Kohalik vektorite salvestus meditsiiniliste teadmiste otsimiseks

**Rakendamise lähenemine:**
- Tagada täielik võrguühenduseta töö patsiendi privaatsuse jaoks
- Rakenda meditsiinilise terminoloogia valideerimine ja soovitused
- Lisa auditi logimine regulatiivse vastavuse jaoks
- Kujunda integratsioon olemasolevate elektrooniliste tervisekaardisüsteemidega

## Jõudluse optimeerimise strateegiad

### Riistvarateadlik arendus

**NPU optimeerimine**
- Kujunda rakendused, et kasutada NPU võimekust Copilot+ PC-del
- Rakenda sujuv üleminek GPU/CPU-le seadmetel, kus NPU puudub
- Optimeeri mudeliformaadid NPU-spetsiifiliseks kiirenduseks
- Jälgi NPU kasutust ja termilisi omadusi

**Mälu haldamine**
- Rakenda tõhusad mudeli laadimis- ja vahemälu strateegiad
- Kasuta mälukaardistust suurte mudelite jaoks, et vähendada käivitusaega
- Kujunda mälusäästlikud rakendused ressursipiiratud seadmete jaoks
- Rakenda mudeli kvantimine mälu optimeerimiseks

**Aku efektiivsus**
- Optimeeri tehisintellekti operatsioonid minimaalse energiatarbimise jaoks
- Rakenda adaptiivne töötlemine vastavalt aku olekule
- Kujunda tõhus tausttöötlus pidevate tehisintellekti operatsioonide jaoks
- Kasuta energiakasutuse profileerimise tööriistu energiatarbimise optimeerimiseks

### Skaleeritavuse kaalutlused

**Mitme lõime kasutamine**
- Kujunda lõimeohutud tehisintellekti operatsioonid samaaegseks töötlemiseks
- Rakenda tõhus tööjaotus olemasolevate tuumade vahel
- Kasuta asünkroonseid mustreid mitteblokeerivate tehisintellekti operatsioonide jaoks
- Planeeri lõimebasseini optimeerimine erinevate riistvarakonfiguratsioonide jaoks

**Vahemälu strateegiad**
- Rakenda intelligentne vahemälu sageli kasutatavate tehisintellekti operatsioonide jaoks
- Kujunda vahemälu tühistamise strateegiad mudeli uuenduste jaoks
- Kasuta püsivat vahemälu kulukate eeltöötlusoperatsioonide jaoks
- Rakenda hajutatud vahemälu mitme kasutaja stsenaariumide jaoks

## Turvalisuse ja privaatsuse parimad praktikad

### Andmekaitse

**Kohalik töötlemine**
- Tagada, et tundlikud andmed ei lahku kunagi kohalikust seadmest
- Rakenda turvaline salvestus tehisintellekti mudelite ja ajutiste andmete jaoks
- Kasuta Windowsi turvafunktsioone rakenduse liivakastiks
- Rakenda krüpteerimine salvestatud mudelite ja vahepealsete töötlemistulemuste jaoks

**Mudeli turvalisus**
- Kinnita mudeli terviklikkus enne laadimist ja täitmist
- Rakenda turvalised mudeli uuendusmehhanismid
- Kasuta allkirjastatud mudeleid, et vältida manipuleerimist
- Rakenda juurdepääsukontrollid mudelifailidele ja konfiguratsioonile

### Vastavuse kaalutlused

**Regulatiivne vastavus**
- Kujunda rakendused vastavusse GDPR-i, HIPAA ja teiste regulatiivsete nõuetega
- Rakenda auditi logimine tehisintellekti otsustusprotsesside jaoks
- Paku läbipaistvuse funktsioone tehisintellekti genereeritud tulemuste jaoks
- Võimalda kasutajatel kontrollida tehisintellekti andmetöötlust

**Ettevõtte turvalisus**
- Integreeri Windowsi ettevõtte turvapoliitikatega
- Tugi hallatud juurutamisele ettevõtte haldustööriistade kaudu
- Rakenda rollipõhine juurdepääsukontroll tehisintellekti funktsioonidele
- Paku administratiivseid kontrolli tehisintellekti funktsionaalsuse jaoks

## Tõrkeotsing ja silumine

### Tavalised arendusprobleemid

**Ehituse konfiguratsiooni probleemid**
- Veendu ARM64 platvormi konfiguratsioonis Windows AI API näidiste jaoks
- Kontrolli Windows App SDK versiooni ühilduvust (vajalik 1.8.1+)
- Kontrolli, et paketi identiteet oleks korrektselt konfigureeritud (vajalik Windows AI API-de jaoks)
- Kinnita, et ehitustööriistad toetavad sihtraamistiku versiooni

**Mudeli laadimise probleemid**
- Kinnita ONNX mudeli ühilduvus Windows ML-iga
- Kontrolli mudelifaili terviklikkust ja formaadinõudeid
- Kinnita riistvara võimekuse nõuded konkreetsete mudelite jaoks
- Silu mälukasutuse probleeme mudeli laadimise ajal
- Veendu täitmispakkuja registreerimises riistvarakiirenduse jaoks

**Juurutamise režiimi kaalutlused**
- **Isemajandav režiim**: Täielikult toetatud suurema juurutuse suurusega
- **Raamistiku sõltuv režiim**: Väiksem jalajälg, kuid vajab jagatud tööaega
- **Pakendamata rakendused**: Windows AI API-de jaoks enam ei toetata
- Kasuta `dotnet run -p:Platform=ARM64 -p:SelfContained=true` isemajandava ARM64 juurutuse jaoks

**Jõudlusprobleemid**
- Profileeri rakenduse jõudlust erinevates riistvarakonfiguratsioonides
- Tuvasta kitsaskohad tehisintellekti töötlemistorudes
- Optimeeri andmete eeltöötlus ja järelprotsessimine
- Rakenda jõudluse jälgimine ja hoiatused

**Integreerimisraskused**
- Silu API integreerimisprobleeme korrektse veakäsitlusega
- Kinnita sisendandmete formaadid ja eeltöötlusnõuded
- Testi äärejuhtumeid ja veatingimusi põhjalikult
- Rakenda ulatuslik logimine tootmisprobleemide silumiseks

### Silumistööriistad ja -tehnikad

**Visual Studio integreerimine**
- Kasuta AI Toolkit silurit mudelite täitmise analüüsiks
- Rakenda jõud
- [Windows ML Ülevaade](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK Süsteeminõuded](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK Arenduskeskkonna Seadistamine](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Näidiskood ja Repositooriumid
- [Windows App SDK Näidised - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Näidised - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Järelduste Näited](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Näidiste Repositoorium](https://github.com/microsoft/WindowsAppSDK-Samples)

### Arendustööriistad
- [AI Tööriistakomplekt Visual Studio Code'i jaoks](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Arendajate Galerii](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Näidised](https://learn.microsoft.com/windows/ai/samples/)
- [Mudelikonversiooni Tööriistad](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehniline Tugi
- [Windows ML Dokumentatsioon](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentatsioon](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentatsioon](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Teata Probleemidest - Windows App SDK Näidised](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Kogukond ja Tugi
- [Windows Arendajate Kogukond](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogi](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Koolitus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*See juhend on loodud arenema koos kiiresti areneva Windows AI ökosüsteemiga. Regulaarsete uuendustega tagatakse vastavus uusimate platvormivõimaluste ja arenduse parimate tavadega.*

[08. Praktiline Töö Microsoft Foundry Localiga - Täielik Arendajate Tööriistakomplekt](../Module08/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.