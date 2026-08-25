# Windows Edge AI arendusjuhend

## Sissejuhatus

Tere tulemast Windows Edge AI arendusse – teie põhjalik juhend intelligentsete rakenduste loomiseks, mis kasutavad seadmesisese AI jõudu Microsofti Windows AI Foundry platvormi abil. See juhend on spetsiaalselt loodud Windowsi arendajatele, kes soovivad oma rakendustesse integreerida tipptasemel Edge AI võimekused, samal ajal kasutades Windowsi riistvara kiirenduse kogu spektrit.

### Windows AI eelis

Windows AI Foundry esindab ühtset, usaldusväärset ja turvalist platvormi, mis toetab AI arendaja kogu elutsüklit – mudeli valimisest ja täpsustamisest optimeerimise ja juurutamiseni CPU, GPU, NPU ja hübriidpilve arhitektuurides. See platvorm demokraatiseerib AI arenduse, pakkudes:

- **Riistvara abstraktsioon**: sujuv juurutamine AMD, Inteli, NVIDIA ja Qualcommi kiibistikel
- **Seadmesisene intelligentsus**: privaatsust tagav AI, mis töötab täielikult lokaalsel riistvaral
- **Optimeeritud jõudlus**: mudelid on Windowsi riistvarakokkuvõtetele eeloptimeeritud
- **Ettevõttevalmidus**: tootmisklassi turvafunktsioonid ja nõuetekohasus

### Windows ML 
Windows Machine Learning (ML) võimaldab C#, C++ ja Python arendajatel käivitada ONNX AI mudeleid lokaalselt Windowsi arvutites ONNX Runtime'i kaudu, automaatse käituse pakkujate haldusega erinevate riistvarade (CPU, GPU, NPU) jaoks. [ONNX Runtime](https://onnxruntime.ai/docs/) saab kasutada PyTorchi, Tensorflow/Keras, TFLite, scikit-learn ja teiste raamistike mudelitega.


![WindowsML Joonis, mis illustreerib ONNX mudeli liikumist läbi Windows ML, et jõuda NPUsse, GPUdesse ja CPDesse.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML pakub jagatud kogu Windowsi ulatuses ONNX Runtime'i koopiat ning võimalust dünaamiliselt alla laadida käituse pakkujaid (EP-sid).

### Miks Windows Edge AI jaoks?

**Ülemaailmne riistvaratugi**
Windows ML pakub automaatset riistvara optimeerimist kogu Windowsi ökosüsteemis, tagades, et teie AI rakendused töötavad optimaalselt sõltumata põhialusest kiibistiku arhitektuurist.

**Integreeritud AI käituskeskkond**
Windows ML sisseehitatud järeldusmootor kõrvaldab keerukad seadistamisnõuded, võimaldades arendajatel keskenduda rakenduse loogikale, mitte infrastruktuurile.

**Copilot+ PC optimeerimine**
Eesmärgipärased API-d, mis on spetsiaalselt loodud järgmise põlvkonna Windowsi seadmete jaoks, kus on pühendatud närvivõrgu töötlemise üksused (NPUd), pakkudes erakordset jõudlust vatt.

**Arendajate ökosüsteem**
Rikkalikud tööriistad, sh Visual Studio integratsioon, põhjalik dokumentatsioon ja näidisarendused, mis kiirendavad arendusprotsesse.

## Õpieesmärgid

Selle Windows Edge AI arendusjuhendi lõpetamisel omandate põhioskused tootmisvalmis AI rakenduste loomiseks Windowsi platvormil.

### Põhilised tehnilised pädevused

**Windows AI Foundry valdamine**
- Mõista Windows AI Foundry platvormi arhitektuuri ja komponente
- Navigeerida kogu AI arenduse elutsüklis Windowsi ökosüsteemis
- Rakendada turvalisuse parimaid praktikaid seadmesiseste AI rakenduste jaoks
- Optimeerida rakendusi erinevate Windowsi riistvara konfiguratsioonide jaoks

**API integratsiooni ekspertteadmised**
- Valdada Windows AI API-sid teksti, nägemise ja multimodaalsete rakenduste jaoks
- Integreerida Phi Silica keelemudeli kasutus teksti genereerimiseks ja järeldamiseks
- Juurutada arvutinägemise võimekusi sisseehitatud pilditöötluse API-dega
- Kohandada eelõpetatud mudeleid LoRA (madala järjestusega adapteerimine) tehnikate abil

**Foundry Local rakendamine**
- Sirvida, hinnata ja juurutada avatud lähtekoodiga keelemudeleid Foundry Local CLI kaudu
- Mõista mudelite optimeerimist ja kvantiseerimist lokaalseks juurutamiseks
- Rakendada võrguühenduseta AI võimekusi, mis toimivad ilma internetiühenduseta
- Hallata mudelite elutsükleid ja uuendusi tootmiskeskkonnas

**Windows ML juurutus**
- Too kohandatud ONNX mudelid Windowsi rakendustesse Windows ML abil
- Kasuta automaatset riistvarakiirendust CPU, GPU ja NPU arhitektuuridel
- Rakenda reaalajas järeldust optimaalse ressursside kasutusega
- Kujunda skaleeritavaid AI rakendusi erinevatesse Windowsi seadmete kategooriatesse

### Rakenduste arendusoskused

**Platvormideülene Windowsi arendus**
- Ehita AI toetatud rakendusi .NET MAUI abil universaalseks Windowsi juurutuseks
- Integreeri AI võimekused Win32, UWP ja Progressiivsetesse Veebirakendustesse
- Rakenda reageerivaid kasutajaliidese kujundusi, mis kohanduvad AI töötlemise olekuga
- Halda asünkroonseid AI operatsioone, järgides korrapärast kasutajakogemuse mustrit

**Jõudluse optimeerimine**
- Profiili ja optimeeri AI järelduste jõudlust erinevates riistvarakonfiguratsioonides
- Rakenda tõhusat mäluhaldust suurte keelemudelite jaoks
- Kujunda rakendusi nii, et need degradeeruksid sujuvalt vastavalt riistvara võimekusele
- Kasuta vahemällu salvestamise strateegiaid sagedasti kasutatavate AI toimingute jaoks

**Tootmisvalmidus**
- Rakenda põhjalikku veakäsitlust ja varuplaanimehhanisme
- Kujunda telemeetriat ja jälgimist AI rakenduse jõudluse jaoks
- Kasuta turvalisi praktikaid lokaalse AI mudeli salvestamisel ja täitmisel
- Plaanita juurutusstrateegiaid ettevõtte- ja tarbijarakendustele

### Äri- ja strateegiline arusaam

**AI rakenduse arhitektuur**
- Kujunda hübriidseid arhitektuure, mis optimeerivad lokaalse ja pilve AI töötlemise vahel
- Hinda kompromisse mudeli suuruse, täpsuse ja järelduse kiiruse vahel
- Planeeri andmevoo arhitektuure, mis säilitavad privaatsuse, võimaldades intelligentsust
- Rakenda kuluefektiivseid AI lahendusi, mis skaleeruvad kasutajate nõudlusega

**Turupositsioneerimine**
- Mõista Windowsi natiivsete AI rakenduste konkurentsieeliseid
- Tuvasta kasutusjuhtumid, kus seadmesisene AI pakub paremat kasutajakogemust
- Arenda turuletoomise strateegiaid AI-võimendatud Windowsi rakendustele
- Positsioneeri rakendused nii, et nad kasutaksid Windowsi ökosüsteemi eeliseid

## Windows App SDK AI näidised

Windows App SDK pakub kõikehõlmavaid näidiseid, mis demonstreerivad AI integreerimist mitme raamistiku ja juurutusstsenaariumi vahel. Need näidised on olulised viited Windows AI arendusmustrite mõistmiseks.

### Windows AI Foundry näidised

| Näidis | Raamistik | Keskendunud valdkond | Põhifunktsioonid |
|--------|-----------|---------------------|-------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API-de integratsioon | Täielik WinUI rakendus, mis demonstreerib Windows AI API-sid, ARM64 optimeerimist, pakendatud juurutust |

**Põhitehnoloogiad:**
- Windows AI API-d
- WinUI 3 raamistik
- ARM64 platvormi optimeerimine
- Copilot+ PC ühilduvus
- Pakendatud rakenduse juurutus

**Eeltingimused:**
- Windows 11 koos Copilot+ PC soovituslik
- Visual Studio 2022
- ARM64 build konfiguratsioon
- Windows App SDK 1.8.1 või uuem

### Windows ML näidised

#### C++ näidised

| Näidis | Tüüp | Keskendunud valdkond | Põhifunktsioonid |
|--------|------|---------------------|-------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Põhiline Windows ML | EP avastamine, käsurea valikud, mudeli kompileerimine |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Raamistiku juurutus | Jagatud runtime, väiksem juurutuse maht |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsoolirakendus | Isoleeritud juurutus | Isoleeritud juurutus, ilma runtime sõltuvusteta |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Raamatukogu kasutus | WindowsML jagatud raamatukogus, mäluhaldus |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet õpetus | Mudelite teisendamine, EP kompileerimine, Build 2025 õpetus |

#### C# näidised

**Konsoolirakendused**

| Näidis | Tüüp | Keskendunud valdkond | Põhifunktsioonid |
|--------|------|---------------------|-------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsoolirakendus | Põhiline C# integratsioon | Jagatud abistaja kasutus, käsurea liides |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet õpetus | Mudelite teisendamine, EP kompileerimine, Build 2025 õpetus |

**GUI rakendused**

| Näidis | Raamistik | Keskendunud valdkond | Põhifunktsioonid |
|--------|-----------|---------------------|-------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Töölaua GUI | Pildi klassifitseerimine WPF liidesega |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditsiooniline GUI | Pildi klassifitseerimine Windows Formsiga |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moodne GUI | Pildi klassifitseerimine WinUI 3 liidesega |

#### Python näidised

| Näidis | Keelel | Keskendunud valdkond | Põhifunktsioonid |
|--------|----------|---------------------|-------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Pildi klassifitseerimine | WinML Python sidemed, partii pilditöötlus |

### Näidiste eeltingimused

**Süsteeminõuded:**
- Windows 11 arvuti, mis töötab versiooniga 24H2 (build 26100) või hilisem
- Visual Studio 2022 koos C++ ja .NET töökoormustega
- Windows App SDK 1.8.1 või uuem
- Python 3.10-3.13 Python näidiste jaoks x64 ja ARM64 seadmetel

**Windows AI Foundry spetsiifilised:**
- Copilot+ PC optimaalset jõudlust soovitatakse
- ARM64 build konfiguratsioon Windows AI näidiste jaoks
- Vajalik pakendi identiteet (pakendamata rakendusi enam ei toetata)

### Üldine näidise töövoog

Enamik Windows ML näidiseid järgib seda standardmustrit:

1. **Keskkonna algatamine** - Loo ONNX Runtime keskkond
2. **Käituse pakkujate registreerimine** - Otsi ja registreeri saadaval olevad riistvarakiirendid (CPU, GPU, NPU)
3. **Mudeli laadimine** - Laadi ONNX mudel, vajadusel kompileeri sihtseadmele
4. **Sisendi eeltöötlus** - Muuda pildid/andmed mudeli sisendvormingusse
5. **Järelduse käivitamine** - Käivita mudel ja saa prognoosid
6. **Tulemuste töötlemine** - Rakenda softmax ja kuva tipptulemused

### Kasutatavad mudelifailid

| Mudel | Eesmärk | Kaasas | Märkused |
|-------|---------|---------|----------|
| SqueezeNet | Kerge pildi klassifitseerimine | ✅ Kaasas | Eelõpetatud, kasutamiseks valmis |
| ResNet-50 | Kõrgtäpsusega pildi klassifitseerimine | ❌ Vajab teisendamist | Kasuta teisendamiseks [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) tööriista |

### Riistvaratoetus

Kõik näidised avastavad ja kasutavad automaatselt saadaval olevat riistvara:
- **CPU** - Universaalne tugi kõigis Windowsi seadmetes
- **GPU** - Automaatne avastamine ja optimeerimine saadaval olevale graafikakiirendusele
- **NPU** - Kasutab närvivõrgu töötlemise üksusi toetatud seadmetes (Copilot+ PC-d)

## Windows AI Foundry platvormi komponendid

### 1. Windows AI API-d

Windows AI API-d pakuvad kasutusvalmis AI võimekusi seadmesiseste mudelite abil, mis on optimeeritud efektiivsuseks ja jõudluseks Copilot+ PC seadmetel, nõudes minimaalset seadistust.

#### Põhiseeria API kategooriad

**Phi Silica keelemudel**
- Väike, kuid võimas keelemudel teksti genereerimiseks ja mõtlemiseks
- Optimeeritud reaalajas järelduseks minimaalse energiatarbega
- Toetus kohandatud täpsustamiseks LoRA tehnikate abil
- Integratsioon Windowsi semantilise otsingu ja teadmiste taaskasutusega

**Arvutinägemise API-d**
- **Teksti tuvastus (OCR)**: Ekstrakti tekst pilteelt suure täpsusega
- **Pildi kõrgresolutsiooni suurendamine**: Suurenda pilte lokaalsete AI mudelite abil
- **Pildi segmentimine**: Tuvasta ja eralda kindlad objektid piltidelt
- **Pildi kirjeldus**: Genereeri detailsed tekstikirjeldused visuaalse sisu jaoks
- **Objekti eemaldamine**: Eemalda soovimatud objektid AI-põhise maalimise abil piltidelt

**Multimodaalsed võimekused**
- **Nägemise ja keele integratsioon**: Ühenda teksti ja pildi mõistmine
- **Semantiline otsing**: Võimalda loomuliku keele päringud multimeediumisisus
- **Teadmiste taaskasutus**: Loo intelligentseid otsingukogemusi kohalike andmetega

### 2. Foundry Local

Foundry Local annab arendajatele kiire juurdepääsu kasutusvalmis avatud lähtekoodiga keelemudelitele Windowsi kiibil, pakkudes võimalust sirvida, testida, suhelda ja juurutada mudeleid kohalikes rakendustes.

#### Foundry Local näidiserakendused

[Foundry Local hoidla](https://github.com/microsoft/Foundry-Local/tree/main/samples) pakub põhjalikke näidiseid mitmes programmeerimiskeeles ja -raamistikus, demonstreerides erinevaid integratsioonimustreid ja kasutusjuhtumeid.

| Näidis | Keel/raamistik | Keskendunud valdkond | Põhifunktsioonid |
|--------|-----------------|---------------------|-------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG rakendus | Semantic Kernel integratsioon, Qdrant vektoripood, JINA kirjeldused, dokumentide import, reaalajas vestlus |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Töölaua vestlusapp | Platvormideülene vestlus, lokaalse/pilve mudeli vahetamine, OpenAI SDK integratsioon, reaalajas voogesitus |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Põhiline integratsioon | Lihtne SDK kasutus, mudeli algatamine, põhiline vestlusfunktsioon |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Põhiline integratsioon | Python SDK kasutus, voogesituse vastused, OpenAI-ga ühilduv API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Süsteemide integratsioon | Madala taseme SDK kasutamine, asünkroonsed operatsioonid, reqwest HTTP klient |

#### Näidiste kategooriad kasutusjuhtumite järgi

**RAG (Andmete täiendatud genereerimine)**
- **dotNET/rag**: Täielik RAG-i rakendus Semantic Kerneliga, Qdrant vektorandmebaasiga ja JINA manustega
- **Arhitektuur**: Dokumentide sisestamine → Tekstijuppide moodustamine → Vektormanused → Sarnasuse otsing → Kontekstitundlikud vastused
- **Tehnoloogiad**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX manused, voogedastuse vestluse täitmine

**Lauaarvuti rakendused**
- **electron/foundry-chat**: Tootmiseks valmis vestlusrakendus kohaliku/pilve mudelivahetusega
- **Funktsioonid**: Mudeli valija, voogesituse vastused, veahaldus, platvormideülene juurutus
- **Arhitektuur**: Electrone põhiprotsess, IPC suhtlus, turvalised eellaadimisskriptid

**SDK integratsiooni näited**
- **JavaScript (Node.js)**: Põhiline mudeliga suhtlemine ja voogesituse vastused
- **Python**: OpenAI-ühildumisega API kasutamine asünkroonse voogesitusega
- **Rust**: Madala taseme integratsioon reqwesti ja tokio abil asünkroonsete operatsioonide jaoks

#### Eeltingimused Foundry Local näidiste jaoks

**Süsteeminõuded:**
- Windows 11 koos Foundry Local paigaldusega
- Node.js v16+ JavaScript/Electron näidiste jaoks
- .NET 8.0+ C# näidiste jaoks
- Python 3.10+ Python näidiste jaoks
- Rust 1.70+ Rust näidiste jaoks

**Paigaldamine:**
```powershell
# Paigalda Foundry kohalikult
winget install Microsoft.FoundryLocal

# Kontrolli paigaldust
foundry --version
foundry model list
```

#### Näidispõhine seadistamine

**dotNET RAG näide:**
```powershell
# Paigalda vajalikud paketid NuGeti kaudu
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Käivita Qdrant vektorandmebaas
docker run -p 6333:6333 qdrant/qdrant

# Käivita Jupyteri märkmik
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electroni vestluse näide:**
```powershell
# Määra pilve varufunktsiooni jaoks keskkonnamuutujad
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Paigalda sõltuvused ja käivita
npm install
npm start
```

**JavaScript/Python/Rust näited:**
```powershell
# Lae alla mudel (näide phi-3.5-mini)
foundry model run phi-3.5-mini

# Käivita vastav näidis
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Põhifunktsioonid

**Mudelite kataloog**
- Ulatuslik kogumik eeloptimeeritud avatud lähtekoodiga mudeleid
- Mudelid optimeeritud CPU-de, GPU-de ja NPU-de jaoks kohe kasutuseks
- Tugi populaarsetele mudeliperele nagu Llama, Mistral, Phi ja spetsialiseeritud domeenimudelid

**CLI integratsioon**
- Käsklussuhtluse liides mudelite haldamiseks ja juurutamiseks
- Automaatne optimeerimise ja kvantiseerimise töövoog
- Integratsioon populaarsete arendusvahendite ja CI/CD torujuhtmetega

**Kohalik juurutus**
- Täielik võrguühenduseta töö ilma pilve sõltuvuseta
- Tugi kohandatud mudelifailidele ja konfiguratsioonidele
- Tõhus mudelite teenindamine automaatse riistvara optimeerimisega

### 3. Windows ML

Windows ML on Windowsi põhiline tehisintellekti platvorm ja integreeritud järeldamise käitusaja süsteem, mis võimaldab arendajatel efektiivselt juurutada kohandatud mudeleid kogu laia Windowsi riistvaramaastiku ulatuses.

#### Arhitektuuri eelised

**Üldine riistvara tugi**
- Automaatne optimeerimine AMD, Inteli, NVIDIA ja Qualcommi kiipide jaoks
- Tugi CPU, GPU ja NPU täitmiseks läbipaistva vaheldumisega
- Riistvara abstraktsioon, mis kõrvaldab platvormispetsiifilise optimeerimise töö

**Mudelide paindlikkus**
- Tugi ONNX mudelivormingule automaatse konverteerimisega populaarsetest raamistikest
- Kohandatud mudelite juurutus tootmistaseme jõudlusega
- Integratsioon olemasolevate Windowsi rakendusarhitektuuridega

**Ettevõtte integratsioon**
- Ühilduvus Windowsi turbe- ja vastavusraamistikuga
- Tugi ettevõtte juurutuse ja haldustööriistadele
- Integratsioon Windowsi seadmete halduse ja jälgimissüsteemidega

## Arendusprotsess

### Faas 1: Keskkonna seadistamine ja tööriistade konfiguratsioon

**Arenduskeskkonna ettevalmistus**
1. Paigalda Visual Studio 2022 koos C++ ja .NET töökoormustega
2. Paigalda Windows App SDK 1.8.1 või uuem versioon
3. Konfigureeri Windows AI Foundry CLI tööriistad
4. Seadista AI toolkit laiendus Visual Studio Code’ile
5. Loo jõudluse profiilimise ja jälgimise tööriistad
6. Tagada ARM64 ehituskonfiguratsioon Copilot+ PC optimeerimiseks

**Näidiste hoidla seadistamine**
1. Kloneeri [Windows App SDK näidiste hoidla](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Liigu kataloogi `Samples/WindowsAIFoundry/cs-winui` Windows AI API näidiste jaoks
3. Liigu kataloogi `Samples/WindowsML` Windows ML põhjalike näidiste jaoks
4. Vaata üle [ehitusnõuded](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) sihtplatvormidele

**AI arenduse galeriis tutvumine**
- Uuri näidiserakendusi ja viitamisrakendusi
- Testi Windows AI API-sid interaktiivsete demonstratsioonidega
- Vaata lähtekoodi parimate tavade ja mustrite jaoks
- Määra oma konkreetse kasutusjuhtumi jaoks asjakohased näited

### Faas 2: Mudeli valimine ja integratsioon

**Nõuete analüüs**
- Määra AI võimekuste funktsionaalsed nõuded
- Sea jõudluspiirangud ja optimeerimise eesmärgid
- Hinda privaatsuse ja turbenõudeid
- Plaani juurutusarhitektuur ja skaleerimisstrateegiad

**Mudeli hindamine**
- Kasuta Foundry Local’i avatud lähtekoodiga mudelite testimiseks oma kasutusjuhtumi jaoks
- Võrdle Windows AI API-de jõudlust kohandatud mudelinõuetega
- Hinda kompromisse mudeli suuruse, täpsuse ja järelduskiiruse vahel
- Prototüübi integratsioonimeetodeid valitud mudelitega

### Faas 3: Rakenduse arendus

**Tuumikintegratsioon**
- Rakenda Windows AI API integratsioon koos korrapärase veahaldusega
- Kujunda kasutajaliidesed, mis mahutavad AI töövoogudega
- Rakenda vahemällu salvestamise ja optimeerimise strateegiad mudeli järeldamiseks
- Lisa telemeetria ja jõudluse jälgimine AI operatsioonide jaoks

**Testimine ja valideerimine**
- Testi rakendusi erinevate Windowsi riistvarakonfiguratsioonide puhul
- Kontrolli jõudlusmõõdikuid erinevate koormustingimuste all
- Rakenda automatiseeritud testimine AI funktsionaalsuse usaldusväärsuse tagamiseks
- Viige läbi kasutajakogemuse testimine AI-lisanditega funktsioonidega

### Faas 4: Optimeerimine ja juurutus

**Jõudluse optimeerimine**
- Profiili rakenduse jõudlust sihtriistvara konfiguratsioonide ulatuses
- Optimeeri mälu kasutust ja mudeli laadimise strateegiaid
- Rakenda adaptiivset käitumist olemasolevate riistvaravõimaluste põhjal
- Täiusta kasutajakogemust erinevate jõudlusstsenaariumite jaoks

**Tootmisjuurutus**
- Paki rakendused koos korras AI mudelite sõltuvustega
- Rakenda mudelite ja rakendusloogika uuendusmehhanismid
- Konfigureeri tootmiskeskkonna jälgimine ja analüütika
- Planeeri järkjärgulise levitamise strateegiad ettevõtetele ja tarbijatele

## Praktilised rakenduse näited

### Näide 1: Intelligentsed dokumenditöötluse rakendus

Arenda Windowsi rakendus, mis töötleb dokumente mitme AI võimekusega:

**Kasutatavad tehnoloogiad:**
- Phi Silica dokumentide kokkuvõtmiseks ja küsimuste vastamiseks
- OCR API-d skaneeritud dokumentide tekstieksktraktsiooniks
- Pildikirjelduse API-d diagrammide ja graafikute analüüsiks
- Kohandatud ONNX mudelid dokumentide klassifitseerimiseks

**Rakenduse lähenemine:**
- Kujunda moodulaarne arhitektuur liigendatavate AI komponentidega
- Rakenda asünkroonset töötlemist suurtes dokumendipakettides
- Lisa edenemisindikaatorid ja tühistamise tugi pikaajalistele operatsioonidele
- Kaasa võrguühenduseta töövõime tundlike dokumentide töötlemiseks

### Näide 2: Jaemüügivarude haldussüsteem

Loo AI-põhine varude haldussüsteem jaemüügi rakendustele:

**Kasutatavad tehnoloogiad:**
- Pildilõikamise tehnoloogia toote identifitseerimiseks
- Kohandatud nägemismudelid kaubamärgi ja kategooria klassifitseerimiseks
- Foundry Local juurutus spetsialiseeritud jaemüügikeele mudelite jaoks
- Integratsioon olemasolevate kassasüsteemide ja varude haldusega

**Rakenduse lähenemine:**
- Loo kaamera integratsioon reaalajas toodete skannimiseks
- Rakenda vöötkoodi ja visuaalse toote tuvastamine
- Lisa loodusliku keele varude päringud kohalike keelemudelitega
- Kujunda skaleeritav arhitektuur mitme kaupluse juurutuseks

### Näide 3: Tervishoiu dokumentatsiooni assistent

Arenda privaatsust kaitsev tervishoiu dokumentatsiooni tööriist:

**Kasutatavad tehnoloogiad:**
- Phi Silica meditsiiniliste märkmete genereerimiseks ja kliinilise otsuse toetuseks
- OCR käsitsi kirjutatud meditsiiniliste dokumentide digitaliseerimiseks
- Kohandatud meditsiinilised keelemudelid Windows ML kaudu juurutatult
- Kohalik vektorisalvestus meditsiinilise teadmise kuvamiseks

**Rakenduse lähenemine:**
- Tagada täielik võrguühenduseta töö patsiendi privaatsuse kaitseks
- Rakenda meditsiinilise terminoloogia valideerimist ja soovitusi
- Lisa auditeerimise logimine regulatiivse vastavuse tagamiseks
- Kujunda integratsioon olemasolevate elektrooniliste tervisekannete süsteemidega

## Jõudluse optimeerimise strateegiad

### Riistvarateadlik arendus

**NPU optimeerimine**
- Kujunda rakendusi, mis kasutavad ära NPU võimalusi Copilot+ PC-del
- Rakenda sujuv langemine GPU/CPU peale seadmetel, kus NPU puudub
- Optimeeri mudelivormingud NPU-spetsiifilise kiirenduse jaoks
- Jälgi NPU kasutust ja soojusomadusi

**Mälu haldus**
- Rakenda tõhusaid mudelite laadimise ja vahemällu salvestamise strateegiaid
- Kasuta mälumappingut suurte mudelite puhul käivitamisaja vähendamiseks
- Kujunda mälu säästvaid rakendusi piiratud ressurssidega seadmete jaoks
- Rakenda mudelite kvantiseerimist mälu optimeerimiseks

**Aku efektiivsus**
- Optimeeri AI operatsioone minimaalsete energiakuludega
- Rakenda adaptiivne töötlemine vastavalt aku olekule
- Kujunda tõhus taustatöötlus jätkuvateks AI operatsioonideks
- Kasuta võimu profiili tööriistu energiakasutuse optimeerimiseks

### Skalale mõeldes

**Mitme lõime kasutamine**
- Kujunda lõimesõbralikke AI operatsioone paralleelseks töötlemiseks
- Rakenda tõhus tööjaotus saadaval olevate tuumade vahel
- Kasuta asünkroonne/oota mustreid mittetalitavate AI operatsioonide jaoks
- Plaani lõimepuni optimeerimine erinevate riistvarakonfiguratsioonide jaoks

**Vahemälu strateegiad**
- Rakenda intelligentset vahemälu sagedasti kasutatavate AI operatsioonide jaoks
- Kujunda vahemälu kehtetuks muutmise strateegiad mudelite uuenduste jaoks
- Kasuta püsivat vahemälu kallite eeltöötluste jaoks
- Rakenda hajutatud vahemälu mitme kasutajaga stsenaariumide jaoks

## Turvalisus ja privaatsus parimad tavad

### Andmekaitse

**Kohalik töötlemine**
- Tagada, et tundlikud andmed ei lahkuks kunagi lokaalsest seadmest
- Rakenda turvalist hoiustamist AI mudelitele ja ajutistele andmetele
- Kasuta Windowsi turvaeesmärke rakenduste liivakastimiseks
- Kasuta krüptimist salvestatud mudelite ja vaheprotsesside tulemuste jaoks

**Mudeli turvalisus**
- Kontrolli mudeli terviklikkust enne laadimist ja täitmist
- Rakenda turvalised mudeli uuendusmehhanismid
- Kasuta allkirjastatud mudeleid, et takistada manipuleerimist
- Rakenda juurdepääsu kontrolli mudelifailidele ja konfiguratsioonile

### Vastavusnõuded

**Regulatiivne vastavus**
- Kujunda rakendusi GDPR-i, HIPAA ja teiste regulatiivsete nõuete täitmiseks
- Rakenda auditeerimise logimine AI otsuste protsesside jaoks
- Paku läbipaistvuse funktsioone AI genereeritud tulemuste jaoks
- Võimalda kasutajal juhtida AI andmetöötlust

**Ettevõtte turvalisus**
- Integreeru Windowsi ettevõtte turvapoliitikatega
- Tugi hallatud juurutust ettevõtte haldustööriistade kaudu
- Rakenda rollipõhised juurdepääsu kontrollid AI funktsioonidele
- Paku administraatori kontrolli AI funktsionaalsuse üle

## Tõrkeotsing ja silumine

### Tavalised arenduse väljakutsed

**Ehituse konfiguratsiooniprobleemid**
- Tagada ARM64 platvormikonfiguratsioon Windows AI API näidiste jaoks
- Kontrolli Windows App SDK versiooni ühilduvust (vaja vähemalt 1.8.1)
- Veendu, et paketi identiteet oleks õigesti seadistatud (nõutud Windows AI API-de jaoks)
- Kontrolli, et ehitustööriistad toetaksid sihtsüsteemi raamistiku versiooni

**Mudelite laadimise probleemid**
- Kontrolli ONNX mudelite ühilduvust Windows ML-iga
- Kontrolli mudelifailide terviklikkust ja vormingu nõudeid
- Kontrolli riistvaravõime nõudeid konkreetsete mudelite jaoks
- Silu mäluhaldusprobleeme mudeli laadimise ajal
- Tagada täitmismeetodi pakkuja registreerimine riistvara kiirenduseks

**Juurutusrežiimi kaalutlused**
- **Iseseisev režiim**: Täielikult toetatud suurema juurutamise mahuga
- **Raamistiku sõltuv režiim**: Väiksem jalajälg, kuid nõuab jagatud käitusaega
- **Pakendamata rakendused**: Windows AI API-de jaoks enam toetatud ei ole
- Kasuta `dotnet run -p:Platform=ARM64 -p:SelfContained=true` iseseisva ARM64 juurutuse jaoks

**Jõudlusprobleemid**
- Profiili rakenduse jõudlust erinevate riistvarakonfiguratsioonide järgi
- Tuvasta kitsaskohad AI töötlemistorudes
- Optimeeri andmete eeltöötlust ja järgtöötlust
- Rakenda jõudluse jälgimine ja hoiatused

**Integratsiooniraskused**
- Silu API integratsiooniprobleeme korrapärase veahaldusega
- Kontrolli sisendandmete formaate ja eeltöötluse nõudeid
- Testi põhjalikult ääritingimusi ja veatujusid
- Rakenda ulatuslik logimine tootmisvea silumiseks

### Silumisseadmed ja tehnikad

**Visual Studio integratsioon**
- Kasuta AI toolkit silurit mudelite täitmise analüüsiks
- Rakenda jõudluse profiilimine AI operatsioonide jaoks
- Silu asünkroonsed AI operatsioonid korrektses erindite käsitlemises
- Kasuta mälu profiilimise tööriistu optimeerimiseks

**Windows AI Foundry tööriistad**
- Kasuta Foundry Local CLI mudelite testimiseks ja valideerimiseks
- Kasuta Windows AI API testimistööriistu integratsiooni kinnitamiseks
- Rakenda kohandatud logimine AI operatsioonide jälgimiseks
- Loo automatiseeritud testimine AI funktsionaalsuse usaldusväärsuse tagamiseks

## Teie rakenduste tulevikukindlus

### Tuleviku tehnoloogiad

**Järgmise põlvkonna riistvara**
- Kujunda rakendusi, mis kasutavad tulevasi NPU võimeid
- Planeeri suurenevaid mudeli suurusi ja keerukust
- Rakenda adaptiivseid arhitektuure areneva riistvara jaoks
- Mõtle kvantvalmis algoritmidele tulevase ühilduvuse tagamiseks

**Arenenud AI võimed**
- Valmista multimodaalse AI integratsiooniks rohkemate andmetüüpidega
- Planeeri reaalajas koostööl põhinevat AI-d mitme seadme vahel
- Kujunda föderaalse õppimise võimed
- Mõtle serva-pilve hübriidintelligentsuse arhitektuuridele

### Jätkuv õppimine ja kohanemine

**Mudeliuuendused**
- Rakenda sujuvaid mudeli uuendusmehhanisme
- Kujunda rakendusi, mis kohanevad täiustatud mudelivõimekustega
- Planeeri tagurpidi ühilduvust olemasolevate mudelitega
- Rakenda A/B testimist mudeli jõudluse hindamiseks

**Funktsioonide areng**
- Kujunda moodulaarseid arhitektuure, mis mahutavad uusi AI võimeid
- Planeeri uuenevate Windows AI API-de integratsiooni
- Rakenda funktsioonilipu süsteemi järkjärgulise võimekuse lansseerimiseks
- Kujunda kasutajaliideseid, mis kohanevad täiustatud AI omadustega

## Kokkuvõte

Windows Edge AI arendus tähistab võimsate AI võimekuste ühendamist tugeva, turvalise ja skaleeritava Windowsi platvormiga. Windows AI Foundry ökosüsteemi valdamisega suudavad arendajad luua intelligentseid rakendusi, mis pakuvad erakordset kasutajakogemust, säilitades samas kõrgeimad privaatsuse, turvalisuse ja jõudluse standardid.

Windows AI API-de, Foundry Local ja Windows ML kombinatsioon pakub ületamatut alust järgmise põlvkonna intelligentsete Windowsi rakenduste ehitamiseks. Nagu AI jätkab arenemist, tagab Windows platvorm, et teie rakendused skaleeruvad koos tekkivate tehnoloogiate ja säilitavad ühilduvuse ning jõudluse mitmekesises Windowsi riistvaramaastikus.

Olenemata sellest, kas loote tarbijarakendusi, ettevõtterakendusi või spetsialiseeritud tööstusvahendeid, võimaldab Windows Edge AI arendus teil luua intelligentseid, reageerivaid ja sügavalt integreeritud kogemusi, mis kasutavad täielikult kaasaegsete Windowsi seadmete potentsiaali.

## Täiendavad ressursid

### Dokumentatsioon ja õppematerjalid
- [Windows AI Foundry dokumentatsioon](https://learn.microsoft.com/windows/ai/)
- [Windows AI API-de viited](https://learn.microsoft.com/windows/ai/apis/)
- [Alustamine rakenduse loomisel Windows AI API-dega](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local alustamine](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML ülevaade](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK süsteeminõuded](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windowsi rakenduste SDK arenduskeskkonna häälestus](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Näidisvaramu ja kood
- [Windowsi rakenduste SDK näidised - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windowsi rakenduste SDK näidised - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime järelduse näited](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windowsi rakenduste SDK näidiste varamu](https://github.com/microsoft/WindowsAppSDK-Samples)

### Arendustööriistad
- [AI tööriistakomplekt Visual Studio Code jaoks](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI arenduse galerii](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI näidised](https://learn.microsoft.com/windows/ai/samples/)
- [Mudelite teisendamise tööriistad](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehniline tugi
- [Windows ML dokumentatsioon](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime dokumentatsioon](https://onnxruntime.ai/docs/)
- [Windowsi rakenduste SDK dokumentatsioon](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Vigade teatamine - Windowsi rakenduste SDK näidised](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Kogukond ja tugi
- [Windowsi arendajakogukond](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry blogi](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI koolitus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*See juhend on loodud arenema koos kiiresti areneva Windows AI ökosüsteemiga. Regulaarsete uuenduste kaudu tagatakse ühilduvus uusimate platvormi võimekuste ja arendusparimate tavadega.*

[08. Microsoft Foundry Local praktiline kasutus - Täielik arendustööriistade komplekt](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->