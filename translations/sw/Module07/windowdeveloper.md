# Mwongozo wa Maendeleo ya AI ya Edge ya Windows

## Utangulizi

Karibu kwenye Maendeleo ya AI ya Edge ya Windows - mwongozo wako kamili wa kujenga programu za akili zinazotumia nguvu ya AI ya kifaa kwa kutumia jukwaa la Windows AI Foundry la Microsoft. Mwongozo huu umeundwa mahsusi kwa watengenezaji wa Windows ambao wanataka kuunganisha uwezo wa hali ya juu wa Edge AI katika programu zao huku wakitumia nguvu kamili ya kasi za vifaa vya Windows.

### Faida ya Windows AI

Windows AI Foundry ni jukwaa linalounganisha, la kuaminika, na salama linalounga mkono mzunguko mzima wa maendeleo ya AI - kutoka uchaguzi wa modeli na usahihishaji hadi uboreshaji na uenezaji kote CPU, GPU, NPU, na usanifu wa wingu mseto. Jukwaa hili linawaruhusu wote maendeleo ya AI kwa kutoa:

- **Ufafanuzi wa Vifaa**: Uenezaji usio na mshono kwenye siliconi za AMD, Intel, NVIDIA, na Qualcomm
- **Akili Kifaa Ndani**: AI inayohifadhi faragha inayotekelezwa kabisa kwenye vifaa vya ndani
- **Utendaji Ulioboreshwa**: Modeli zilizoandaliwa awali kwa usanifu wa vifaa vya Windows
- **Tayari kwa Sekta**: Usalama wa hali ya juu wa uzalishaji na vipengele vya kufuata sheria

### Windows ML 
Windows Machine Learning (ML) inawawezesha watengenezaji wa C#, C++, na Python kuendesha modeli za AI za ONNX moja kwa moja kwenye PC za Windows kupitia ONNX Runtime, na usimamizi wa kiotomatiki wa watoa huduma za utekelezaji kwa vifaa tofauti (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) inaweza kutumika na modeli kutoka PyTorch, Tensorflow/Keras, TFLite, scikit-learn, na mifumo mingine.


![WindowsML Mchoro unaoonyesha modeli ya ONNX ikipitia Windows ML kisha kufikia NPUs, GPUs, na CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML hutoa nakala ya pamoja ya ONNX Runtime kwa Windows yote, pamoja na uwezo wa kupakua watoa huduma za utekelezaji (EPs) kwa mabadiliko ya haraka.

### Kwa Nini Windows kwa Edge AI?

**Msaada wa Vifaa wa Ulimwengu Wote**
Windows ML hutoa uboreshaji wa kiotomatiki wa vifaa kote kwenye mfumo wa Windows, kuhakikisha programu zako za AI zinafanya kazi kwa ufanisi bila kujali usanifu wa silicioni.

**Muda wa Utekelezaji wa AI uliounganishwa**
Injini ya utafiti ya Windows ML iliyojengwa ndani huondoa mahitaji magumu ya usanidi, ikiruhusu watengenezaji kuzingatia mantiki ya programu badala ya masuala ya miundombinu.

**Uboreshaji wa Kompyuta ya Copilot+**
API zilizojengwa mahsusi kwa vifaa vya kizazi kijacho vya Windows vyenye Vitengo vya Usindikaji wa Neva (NPUs) vinavyotoa utendaji wa kipekee kwa kila watt.

**Ecosystem ya Watengenezaji**
Zana tajiri ikijumuisha ujumuishaji wa Visual Studio, nyaraka kamili, na mifano ya programu inayoharakisha mizunguko ya maendeleo.

## Malengo ya Kujifunza

Kwa kumaliza mwongozo huu wa maendeleo ya AI ya Edge ya Windows, utakuwa mtaalamu wa ujuzi muhimu wa kujenga programu za AI zinazotayarika kwa uzalishaji kwenye jukwaa la Windows.

### Uwezo wa Kiufundi wa Msingi

**Utaalamu wa Windows AI Foundry**
- Elewa usanifu na vipengele vya jukwaa la Windows AI Foundry
- Pitia mzunguko mzima wa maendeleo ya AI ndani ya mfumo wa Windows
- Tekeleza mbinu bora za usalama kwa programu za AI za kifaa
- Boreshaji programu kwa usanifu tofauti wa vifaa vya Windows

**Utaalamu wa Muungano wa API**
- Jifunze API za Windows AI kwa matumizi ya maandishi, picha, na programu zilizo na njia nyingi
- Tekeleza muungano wa mfano wa lugha wa Phi Silica kwa uzalishaji wa maandishi na hoja
- Tumia uwezo wa kuona kwa kompyuta kwa kutumia API za usindikaji wa picha zilizo ndani
- Badilisha modeli zilizopangwa awali kwa kutumia mbinu za LoRA (Low-Rank Adaptation)

**Utekelezaji wa Foundry Local**
- Vinjari, tathmini, na tuma modeli za lugha za chanzo wazi kwa kutumia Foundry Local CLI
- Elewa uboreshaji wa modeli na upunguzaji kwa ajili ya uenezaji wa eneo
- Tekeleza uwezo wa AI wa bila mtandao unaofanya kazi bila muunganisho wa intaneti
- Simamia mizunguko ya maisha na masasisho ya modeli katika mazingira ya uzalishaji

**Usambazaji wa Windows ML**
- Leta modeli za ONNX zilizobinafsishwa kwa programu za Windows kwa kutumia Windows ML
- Tumia kiotomatiki kasi za vifaa kwenye usanifu wa CPU, GPU, na NPU
- Tekeleza tafsiri ya wakati halisi kwa matumizi bora ya rasilimali
- Buni programu za AI zinazoweza kupanuka kwa makundi tofauti ya vifaa vya Windows

### Ujuzi wa Maendeleo ya Programu

**Maendeleo ya Windows kwa Majukwaa Mbalimbali**
- Tengeneza programu zinazoendeshwa na AI kwa kutumia .NET MAUI kwa uenezaji wa ulimwengu wa Windows
- Unganisha uwezo wa AI katika Win32, UWP, na Programu za Wavuti za Kijumuishi
- Tekeleza muundo wa UI unaojibadilisha unaolingana na hali za usindikaji wa AI
- Simamia shughuli za AI zisizo sambamba kwa mifano sahihi ya uzoefu wa mtumiaji

**Uboreshaji wa Utendaji**
- Pima na boresha utendaji wa tafsiri ya AI kwa usanifu tofauti za vifaa
- Tekeleza usimamizi wa kumbukumbu uliofanika kwa modeli kubwa za lugha
- Buni programu zinazopungua utendaji polepole kulingana na uwezo wa vifaa vilivyopo
- Tumia mikakati ya kuhifadhi data kwa shughuli za AI zinazotumika mara kwa mara

**Utayari kwa Uzalishaji**
- Tekeleza usimamizi kamili wa makosa na mbinu za kuepuka matatizo
- Buni telemetry na ufuatiliaji wa utendaji wa programu za AI
- Tumia mbinu bora za usalama kwa hifadhi na utekelezaji wa modeli za AI za eneo
- Panga mikakati ya uenezaji kwa programu za sekta na watumiaji

### Uelewa wa Biashara na Mikakati

**Usanifu wa Programu za AI**
- Buni usanifu mseto unaoboreshwa kati ya usindikaji wa AI wa eneo na wingu
- Tathmini masuala ya gharama kati ya ukubwa wa modeli, usahihi, na kasi ya tafsiri
- Panga usanifu wa mtiririko wa data unaoendeleza faragha huku ukiruhusu utambuzi
- Tekeleza suluhisho za gharama nafuu za AI zinazopanuka kulingana na mahitaji ya watumiaji

**Upangaji Soko**
- Elewa faida za ushindani za programu za AI za asili za Windows
- Tambua matumizi ambapo AI ya kifaa inatoa uzoefu bora kwa watumiaji
- Tengeneza mikakati ya kuingia sokoni kwa programu za Windows zilizo na AI
- Panga programu kutumia manufaa ya mfumo wa Windows

## Mifano ya AI ya Windows App SDK

Windows App SDK hutoa mifano kamili inaonyesha muunganiko wa AI kupitia mifumo mingi na mazingira ya uenezaji. Mifano hii ni marejeleo muhimu kwa kuelewa mifano ya maendeleo ya Windows AI.

### Mifano ya Windows AI Foundry

| Mfano | Mfumo | Eneo la Kuzingatia | Sifa Muhimu |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Muunganiko wa API za Windows AI | Programu ya WinUI kamili inayoonyesha API za Windows AI, uboreshaji wa ARM64, uenezaji wa kifurushi |

**Teknolojia Muhimu:**
- API za Windows AI
- Mfumo wa WinUI 3
- Uboreshaji wa jukwaa la ARM64
- Ulinganifu wa Kompyuta ya Copilot+
- Uenezaji wa programu zilizofurushwa

**Mahitaji Kabla ya Kuanzia:**
- Windows 11 na Kompyuta ya Copilot+ inapendekezwa
- Visual Studio 2022
- Mipangilio ya kujenga ARM64
- Windows App SDK 1.8.1+

### Mifano ya Windows ML

#### Mifano ya C++

| Mfano | Aina | Eneo la Kuzingatia | Sifa Muhimu |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Windows ML ya Msingi | Ugunduzi wa EP, chaguzi za mstari wa amri, uundaji modeli |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Uenezaji wa Mfumo | Runtime ya pamoja, mwelekeo mdogo wa uenezaji |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Uenezaji wa Kujitegemea | Uenezaji huru, haina utegemezi wa runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Matumizi ya Maktaba | WindowsML katika maktaba iliyo sambazwa, usimamizi wa kumbukumbu |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, uundaji wa EP, mafunzo ya Build 2025 |

#### Mifano ya C#

**Programu za Console**

| Mfano | Aina | Eneo la Kuzingatia | Sifa Muhimu |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Programu ya Console | Muunganiko wa Msingi wa C# | Matumizi ya mshirika wa pamoja, kiolesura cha mstari wa amri |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, uundaji wa EP, mafunzo ya Build 2025 |

**Programu za GUI**

| Mfano | Mfumo | Eneo la Kuzingatia | Sifa Muhimu |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI ya Desktop | Uainishaji wa picha na kiolesura cha WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI ya Kawaida | Uainishaji wa picha na Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI ya Kisasa | Uainishaji wa picha na kiolesura cha WinUI 3 |

#### Mifano ya Python

| Mfano | Lugha | Eneo la Kuzingatia | Sifa Muhimu |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Uainishaji wa Picha | Uunganisho wa WinML Python, usindikaji wa picha kwa kundi |

### Mahitaji ya Mfano

**Mahitaji ya Mfumo:**
- PC ya Windows 11 inaendesha toleo la 24H2 (ujenzi 26100) au juu zaidi
- Visual Studio 2022 na mizigo ya kazi ya C++ na .NET
- Windows App SDK 1.8.1 au baadaye
- Python 3.10-3.13 kwa mifano ya Python kwenye vifaa vya x64 na ARM64

**Mahususi kwa Windows AI Foundry:**
- Kompyuta ya Copilot+ inapendekezwa kwa utendaji bora
- Mipangilio ya kujenga ARM64 kwa mifano ya Windows AI
- Kitambulisho cha kifurushi kinahitajika (programu zisizo na kifurushi hazitatii tena)

### Mtiririko wa Kazi wa Mfano wa Kawaida

Mifano mingi ya Windows ML hufuata mfano huu wa kawaida:

1. **Anzisha Mazingira** - Tengeneza mazingira ya ONNX Runtime
2. **Sajili Watoa Huduma za Utekelezaji** - Gundua na sajili viwekaji kasi vya vifaa vinavyopatikana (CPU, GPU, NPU)
3. **Pakia Modeli** - Pakia modeli ya ONNX, kwa hiari unda kwa vifaa lengwa
4. **Tayarisha Ingizo** - Badilisha picha/data kuwa muundo wa ingizo wa modeli
5. **Endesha Tafsiri** - Tekeleza modeli na pata utabiri
6. **Chakata Matokeo** - Tumia softmax naonyesha utabiri bora

### Faili za Modeli Zilizotumika

| Modeli | Kusudi | Imekuwemo | Maelezo |
|-------|---------|----------|-------|
| SqueezeNet | Uainishaji wa picha nyepesi | ✅ Imekuwemo | Iliyotayarishwa awali, tayari kutumika |
| ResNet-50 | Uainishaji wa picha wenye usahihi wa juu | ❌ Inahitaji ubadilishaji | Tumia [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kwa ubadilishaji |

### Msaada wa Vifaa

Mifano yote hugundua moja kwa moja na kutumia vifaa vinavyopatikana:
- **CPU** - Msaada wa ulimwengu wote kwenye vifaa vyote vya Windows
- **GPU** - Ugunduzi na uboreshaji wa kiotomatiki wa vifaa vya picha vinavyopatikana
- **NPU** - Inatumia Vitengo vya Usindikaji Neva kwenye vifaa vinavyounga mkono (Kompyuta za Copilot+)

## Vipengele vya Jukwaa la Windows AI Foundry

### 1. API za Windows AI

API za Windows AI hutoa uwezo wa AI tayari kutumia unaotumia modeli za kifaa, zilizoboreshwa kwa ufanisi na utendaji kwenye vifaa vya Kompyuta ya Copilot+ na usanidi mdogo.

#### Makundi Makuu ya API

**Mfano wa Lugha wa Phi Silica**
- Mfano mdogo lakini wenye nguvu wa lugha kwa uzalishaji wa maandishi na hoja
- Uboreshaji wa tafsiri ya wakati halisi kwa matumizi madogo ya nguvu
- Msaada wa usahihishaji maalum kwa kutumia mbinu za LoRA
- Muunganiko na utaftaji wa maana za Windows na upatikanaji wa maarifa

**API za Kuona kwa Kompyuta**
- **Utambuzi wa Maandishi (OCR)**: Tenga maandishi kutoka picha kwa usahihi mkubwa
- **Ukuaji wa Picha kwa Ufanisi**: Ongeza kiwango cha picha kwa kutumia modeli za AI za ndani
- **Ugawaji wa Picha**: Tambua na tengeneza vitu maalum katika picha
- **Maelezo ya Picha**: Tengeneza maelezo ya maandishi ya kina kwa maudhui ya kuona
- **Ufutaji wa Vitu**: Ondoa vitu visivyohitajika kutoka picha kwa uchoraji unaozingatia AI

**Uwezo wa Njia Nyingi**
- **Muunganiko wa Maono-Na-Lugha**: Changanya kuelewa maandishi na picha
- **Utafutaji wa Maana**: Ruhusu maswali kwa lugha ya asili kwenye maudhui ya media tofauti
- **Upatikanaji wa Maarifa**: Jenga uzoefu wa utaftaji wa akili kwa data za ndani

### 2. Foundry Local

Foundry Local huwapa watengenezaji upatikanaji wa haraka kwa modeli za lugha za chanzo huru zenye matumizi tayari kwenye Silikoni ya Windows, ikitoa uwezo wa kuvinjari, kujaribu, kuingiliana, na kueneza modeli katika programu za eneo.

#### Programu za Mfano za Foundry Local

Hifadhi ya [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) hutoa mifano kamili kwa lugha mbalimbali za programu na mifumo, ikionyesha mifano tofauti ya muunganiko na matumizi.

| Mfano | Lugha/Mfumo | Eneo la Kuzingatia | Sifa Muhimu |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Utekelezaji wa RAG | Muunganiko wa Semantic Kernel, hifadhi ya vekta ya Qdrant, uundaji wa JINA, ingizo la hati, mazungumzo ya mtiririko |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Programu ya Mazungumzo ya Desktop | Mazungumzo ya majukwaa mengi, kubadili modeli ya ndani/wingu, muunganiko wa OpenAI SDK, mtiririko wa wakati halisi |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Muunganiko wa Msingi | Matumizi rahisi ya SDK, utangulizi wa modeli, uwezo wa mazungumzo wa msingi |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Muunganiko wa Msingi | Matumizi ya SDK ya Python, majibu ya mtiririko, API inayolingana na OpenAI |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Muungano wa Mifumo | Matumizi ya kiwango cha chini cha SDK, operesheni za async, mteja wa HTTP reqwest |

#### Aina za Mfano kwa Matumizi

**RAG (Uundaji ulioongezwa kwa Kupata)**
- **dotNET/rag**: Utekelezaji kamili wa RAG ukitumia Semantic Kernel, hifadhidata ya vekta ya Qdrant, na uingizaji wa JINA
- **Mimdingilio**: Kuingiza nyaraka → Kugawanya maandishi → Uingizaji vekta → Utafutaji wa ufananisho → Majibu yanayojali muktadha
- **Teknolojia**: Microsoft.SemanticKernel, Qdrant.Client, uingizaji wa BERT ONNX, ukamilisho wa mazungumzo yanayotiririka

**Programu za Desktop**
- **electron/foundry-chat**: Programu ya mazungumzo tayari kwa matumizi ya uzalishaji na kubadilisha mifano ya ndani/wingu
- **Sifa**: Mchaguzi wa modeli, majibu yanayotiririka, usimamizi wa makosa, utekelezaji wa majukwaa mbalimbali
- **Mimdingilio**: Mchakato mkuu wa Electron, mawasiliano ya IPC, skiripti salama za preload

**Mifano ya Muungano wa SDK**
- **JavaScript (Node.js)**: Mwingiliano wa msingi wa modeli na majibu yanayotiririka
- **Python**: Matumizi ya API inayolingana na OpenAI na utiririko wa async
- **Rust**: Muungano wa kiwango cha chini na reqwest na tokio kwa operesheni za async

#### Mahitaji ya Awali kwa Mifano ya Foundry Local

**Mahitaji ya Mfumo:**
- Windows 11 yenye Foundry Local imewekwa
- Node.js v16+ kwa mifano ya JavaScript/Electron
- .NET 8.0+ kwa mifano ya C#
- Python 3.10+ kwa mifano ya Python
- Rust 1.70+ kwa mifano ya Rust

**Usakinishaji:**
```powershell
# Sakinisha Foundry Local
winget install Microsoft.FoundryLocal

# Thibitisha usakinishaji
foundry --version
foundry model list
```

#### Maandalizi Maalum ya Mfano

**Mfano wa dotNET RAG:**
```powershell
# Sakinisha vifurushi vinavyohitajika kupitia NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Anzisha hifadhidata ya vekta ya Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Endesha daftari la Jupyter
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Mfano wa Mazungumzo wa Electron:**
```powershell
# Weka vigezo vya mazingira kwa ajili ya kurejea kwa mawingu
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Sakinisha utegemezi na endesha
npm install
npm start
```

**Mifano ya JavaScript/Python/Rust:**
```powershell
# Pakua mfano (mfano na phi-3.5-mini)
foundry model run phi-3.5-mini

# Endesha sampuli husika
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Sifa Muhimu

**Katalogi ya Modeli**
- Mkusanyiko kamili wa modeli wazi zilizoboreshwa tayari
- Modeli zilizoboreshwa kwa CPU, GPU, na NPU kwa utekelezaji wa papo hapo
- Msaada kwa familia maarufu za modeli ikiwemo Llama, Mistral, Phi, na modeli maalum za nyanja

**Muungano wa CLI**
- Kiolesura cha amri kwa usimamizi wa modeli na utekelezaji
- Mchakato wa kiotomatiki wa uboreshaji na kuhesabu
- Muungano na mazingira maarufu ya ukuzaji na mistari ya CI/CD

**Utekelezaji wa Kwenye Eneo**
- Operesheni kamili ya nje ya mtandao bila utegemezi wa wingu
- Msaada kwa aina na usanidi za spesho za modeli
- Huduma bora za modeli kwa uboreshaji wa vifaa kiotomatiki

### 3. Windows ML

Windows ML hutumikia kama jukwaa kuu la AI na wakati uliounganishwa wa utekelezaji wa inferencia kwenye Windows, kuruhusu watengenezaji kueneza modeli maalum kwa ufanisi kote katika ekosistimu pana ya vifaa vya Windows.

#### Faida za Mimdingilio

**Msaada wa Vifaa vya Ulimwenguni**
- Uboreshaji wa kiotomatiki kwa silicon za AMD, Intel, NVIDIA, na Qualcomm
- Msaada kwa utekelezaji wa CPU, GPU, na NPU pamoja na kubadilisha kioo wazi
- Utoaji wa vifaa utakaondoa kazi za uboreshaji wa mazingira maalum

**Uwezo wa Modeli**
- Msaada kwa fomati ya modeli ya ONNX na uongofu wa kiotomatiki kutoka kwa mifumo maarufu
- Utekelezaji wa modeli maalum wenye utendaji wa daraja la uzalishaji
- Muungano na usanifu uliopo wa programu za Windows

**Muungano wa Biashara**
- Inalingana na usalama wa Windows na mifumo ya kufuata sheria
- Msaada kwa zana za usimamizi na utekelezaji wa biashara
- Muungano na mifumo ya usimamizi na ufuatiliaji wa vifaa vya Windows

## Mtiririko wa Maendeleo

### Awamu ya 1: Usanidi wa Mazingira na Usanidi wa Zana

**Maandalizi ya Mazingira ya Maendeleo**
1. Weka Visual Studio 2022 na kazi za C++ na .NET
2. Weka Windows App SDK 1.8.1 au zaidi
3. Sanidi zana za CLI za Windows AI Foundry
4. Weka ugani wa AI Toolkit kwa Visual Studio Code
5. Anzisha zana za kupima utendaji na ufuatiliaji
6. Hakikisha usanidi wa kujenga ARM64 kwa uboreshaji wa PC ya Copilot+

**Usanidi wa Hifadhidata ya Mifano**
1. Nakili hifadhidata ya [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Nenda `Samples/WindowsAIFoundry/cs-winui` kwa mifano ya API za Windows AI
3. Nenda `Samples/WindowsML` kwa mifano kamili ya Windows ML
4. Kagua [mahitaji ya ujenzi](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) kwa majukwaa unayolenga

**Uchunguzi wa Kwenye Maktaba ya AI Dev**
- Chunguza programu za mfano na utekelezaji wa rejea
- Jaribu API za Windows AI kwa maonyesho ya mwingiliano
- Kagua msimbo wa chanzo kwa mbinu bora na mifumo
- Tambua mifano inayofaa kwa matumizi yako maalum

### Awamu ya 2: Uchaguzi wa Modeli na Muungano

**Uchambuzi wa Mahitaji**
- Eleza mahitaji ya kazi kwa uwezo wa AI
- Weka vizingiti vya utendaji na malengo ya uboreshaji
- Tathmini mahitaji ya faragha na usalama
- Panga usanifu wa utekelezaji na mikakati ya kupanua

**Tathmini ya Modeli**
- Tumia Foundry Local kujaribu modeli wazi kwa matumizi yako
- Linganisha API za Windows AI na mahitaji maalum ya modeli
- Tathmini marejesho kati ya ukubwa wa modeli, usahihi, na kasi ya inferencia
- Tumia mbinu za mfano wa muungano na modeli zilizochaguliwa

### Awamu ya 3: Maendeleo ya Programu

**Muungano wa Msingi**
- Tekeleza muungano wa API za Windows AI na usimamizi mzuri wa makosa
- Tengeneza interfaces za mtumiaji zinazowezesha mitiririko ya usindikaji wa AI
- Tekeleza mbinu za kuhifadhi na kuboresha kwasababu ya inferencia ya modeli
- Ongeza telemetry na ufuatiliaji wa utendakazi wa AI

**Upimaji na Uhakikisho**
- Jaribu programu kwa usanidi tofauti wa vifaa vya Windows
- Hakikisha vipimo vya utendaji chini ya hali tofauti za mzigo
- Tekeleza upimaji wa kiotomatiki kwa uaminifu wa utendaji wa AI
- Fanya majaribio ya uzoefu wa mtumiaji kwa vipengele vilivyoimarishwa na AI

### Awamu ya 4: Uboreshaji na Utekelezaji

**Uboreshaji wa Utendaji**
- Pima utendaji wa programu kwa usanidi wa vifaa unayolenga
- Boresha matumizi ya kumbukumbu na mbinu za kupakia modeli
- Tekeleza tabia inayojibadilisha kwa msingi wa uwezo wa vifaa vilivyopo
- Fanya marekebisho ya uzoefu wa mtumiaji kwa hali tofauti za utendaji

**Utekelezaji wa Uzalishaji**
- Pakia programu pamoja na utegemezi sahihi wa modeli za AI
- Tekeleza taratibu za sasisho za modeli na mantiki ya programu
- Sanidi ufuatiliaji na uchambuzi kwa mazingira ya uzalishaji
- Panga mikakati ya usambazaji kwa biashara na watumiaji

## Mifano ya Utekelezaji wa Kivitendo

### Mfano 1: Programu ya Kusindika Nyaraka kwa Akili

Tengeneza programu ya Windows inayosindika nyaraka kwa kutumia uwezo mbalimbali wa AI:

**Teknolojia Zinazotumika:**
- Phi Silica kwa muhtasari wa nyaraka na majibu ya maswali
- API za OCR kwa kutoa maandishi kutoka kwa nyaraka zilizochanganuliwa
- API za Maelezo ya Picha kwa uchambuzi wa chati na michoro
- Modeli maalum za ONNX kwa uainishaji wa nyaraka

**Mbinu ya Utekelezaji:**
- Tengeneza usanifu wa moduli zilizo na vipengele vya AI vinavyoweza kuunganishwa
- Tekeleza usindikaji wa async kwa kundi kubwa la nyaraka
- Ongeza viashiria vya maendeleo na msaada wa kughairi operesheni ndefu
- Jumuisha uwezo wa nje ya mtandao kwa usindikaji wa nyaraka nyeti

### Mfano 2: Mfumo wa Usimamizi wa Hali ya Bidhaa za Rejareja

Unda mfumo wa hesabu unaotumia AI kwa programu za rejareja:

**Teknolojia Zinazotumika:**
- Ukataji wa Picha kwa utambuzi wa bidhaa
- Modeli za kuona maalum kwa uainishaji wa chapa na kategoria
- Utekelezaji wa Foundry Local wa modeli maalum za lugha za rejareja
- Muungano na mifumo ya POS na hesabu iliyopo

**Mbinu ya Utekelezaji:**
- Tengeneza muungano wa kamera kwa ajili ya kuwachambua bidhaa kwa wakati halisi
- Tekeleza utambuzi wa misimbo ya mstari na utambuzi wa bidhaa kwa macho
- Ongeza maswali ya hesabu kwa lugha asilia kwa kutumia modeli za lugha za mahali
- Tengeneza usanifu unaoweza kupanuliwa kwa utekelezaji wa maduka mengi

### Mfano 3: Msaidizi wa Nyaraka za Huduma za Afya

Tengeneza chombo cha nyaraka za huduma za afya kinachohifadhi faragha:

**Teknolojia Zinazotumika:**
- Phi Silica kwa uzalishaji wa vidokezo vya matibabu na msaada wa maamuzi ya kliniki
- OCR kwa kudadabisha rekodi za matibabu zilizoandikwa kwa mkono
- Modeli maalum za lugha za matibabu zilizoanzishwa kupitia Windows ML
- Hifadhi ya vekta ya ndani kwa kupata maarifa ya matibabu

**Mbinu ya Utekelezaji:**
- Hakikisha operesheni kamili nje ya mtandao kwa faragha ya mgonjwa
- Tekeleza uthibitishaji wa istilahi za matibabu na mapendekezo
- Ongeza uandikishaji wa ukaguzi wa kufuata kanuni
- Tengeneza muungano na mifumo iliyopo ya Rekodi za Afya za Kielektroniki

## Mikakati ya Uboreshaji wa Utendaji

### Maendeleo Yanayojali Vifaa

**Uboreshaji wa NPU**
- Tengeneza programu zinazotumia uwezo wa NPU kwenye PC za Copilot+
- Tekeleza kurudi salama kwa GPU/CPU kwenye vifaa visivyo na NPU
- Boresha aina za modeli kwa uhamasishaji maalum wa NPU
- Simamia matumizi ya NPU na sifa za joto

**Usimamizi wa Kumbukumbu**
- Tekeleza mbinu bora za kupakia modeli na kuhifadhi cache
- Tumia ramani ya kumbukumbu kwa modeli kubwa kupunguza muda wa kuanza
- Tengeneza programu zenye uangalifu wa kumbukumbu kwa vifaa vyenye rasilimali chache
- Tekeleza kuhesabu modeli kwa uboreshaji wa kumbukumbu

**Ufanisi wa Betri**
- Boresha operesheni za AI kwa matumizi madogo ya nguvu
- Tekeleza usindikaji unaojibadilisha kulingana na hali ya betri
- Tengeneza usindikaji wa nyuma wenye ufanisi kwa operesheni za AI endelevu
- Tumia zana za kupima nguvu kuboresha matumizi ya nishati

### Mambo ya Kuangalia Uwezo wa Kupanua

**Multi-Threading**
- Tengeneza operesheni za AI salama kwa nyuzi kwa usindikaji sambamba
- Tekeleza usambazaji mzuri wa kazi kote viini vinavyopatikana
- Tumia mitindo ya async/await kwa operesheni za AI zisizozuia
- Panga uboreshaji wa hifadhidata ya nyuzi kwa usanidi tofauti wa vifaa

**Mikakati ya Kuhifadhi Cache**
- Tekeleza kuhifadhi cache kwa akili kwa operesheni za mara kwa mara za AI
- Tengeneza mbinu za kufuta cache kwa sasisho za modeli
- Tumia kuhifadhi cache thabiti kwa operesheni gharama kubwa za awali
- Tekeleza kuhifadhi cache kwa usambazaji kwa hali za watumiaji wengi

## Mazoezi Bora ya Usalama na Faragha

### Ulinzi wa Data

**Usindikaji wa Kwenye Eneo**
- Hakikisha data nyeti haiondoki kifaa cha eneo la mtumiaji kamwe
- Tekeleza uhifadhi salama kwa modeli za AI na data za muda mfupi
- Tumia sifa za usalama za Windows kwa sandboxing ya programu
- Tumia usimbaji fiche kwa modeli zilizohifadhiwa na matokeo ya usindikaji wa kati

**Usalama wa Modeli**
- Thibitisha uadilifu wa modeli kabla ya kupakia na kutekeleza
- Tekeleza taratibu za usalama za sasisho za modeli
- Tumia modeli zilizosainiwa kuzuia mabadiliko yasiyotakikana
- Tumia udhibiti wa upatikanaji kwa faili za modeli na usanidi

### Mahitaji ya Ufuatiliaji wa Sheria

**Ulinganifu wa Sheria**
- Tengeneza programu kukidhi GDPR, HIPAA, na mahitaji mengine ya sheria
- Tekeleza uandikishaji wa ukaguzi kwa michakato ya maamuzi ya AI
- Toa sifa za uwazi kwa matokeo yaliyotokana na AI
- Ruhusu mtumiaji kudhibiti usindikaji wa data za AI

**Usalama wa Biashara**
- Jumuisha na sera za usalama za biashara za Windows
- Msaada kwa utekelezaji ulioendeshwa na zana za usimamizi wa biashara
- Tekeleza udhibiti wa upatikanaji wa kazi za AI kulingana na majukumu
- Toa udhibiti wa usimamizi kwa utendaji wa AI

## Utatuzi wa Matatizo na Uvujaji wa Makosa

### Changamoto za Kawaida za Maendeleo

**Masuala ya Usanidi wa Ujenzi**
- Hakikisha usanidi wa jukwaa wa ARM64 kwa mifano ya API za Windows AI
- Thibitisha utangamano wa toleo la Windows App SDK (1.8.1+ inahitajika)
- Angalia kuwa kitambulisho cha kifurushi kimewekwa vizuri (kinahitajika kwa API za Windows AI)
- Thibitisha kwamba zana za ujenzi zinaunga mkono toleo la mfumo unaolengwa

**Masuala ya Kupakia Modeli**
- Thibitisha utangamano wa modeli za ONNX na Windows ML
- Angalia uadilifu wa faili ya modeli na mahitaji ya fomati
- Hakiki mahitaji ya uwezo wa vifaa vya modeli maalum
- Tatua matatizo ya ugawaji wa kumbukumbu wakati wa kupakia modeli
- Hakikisha usajili wa mtoa utekelezaji kwa kuhamasisha vifaa

**Mahitaji ya Hali ya Utekelezaji**
- **Hali ya Kujitegemea**: Inasaidiwa kikamilifu na ukubwa mkubwa wa utekelezaji
- **Hali ya Kutegemea Muktadha**: Kiasi kidogo lakini inahitaji runtime ya pamoja
- **Programu zisizojumuishwa**: Haiziungi mkono tena kwa API za Windows AI
- Tumia `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kwa utekelezaji wa ARM64 usiojitegemea

**Matatizo ya Utendaji**
- Pima utendaji wa programu kwa usanidi tofauti wa vifaa
- Tambua vizuizi katika mitiririko ya usindikaji wa AI
- Boresha utayarishaji wa data kabla na baada ya usindikaji
- Tekeleza ufuatiliaji wa utendaji na tahadhari

**Madhara ya Muungano**
- Tatuza matatizo ya muungano wa API kwa usimamizi mzuri wa makosa
- Thibitisha fomati za data za ingizo na mahitaji ya awali ya usindikaji
- Jaribu hali za mwisho na hali za makosa kwa kina
- Tekeleza uandikishaji wa kina kwa uvujaji wa matatizo ya utendaji

### Zana na Mbinu za Uvujaji wa Makosa

**Muungano wa Visual Studio**
- Tumia debugger ya AI Toolkit kwa uchambuzi wa utekelezaji wa modeli
- Tekeleza upimaji wa utendaji kwa operesheni za AI
- Tatuza operesheni za async za AI na utunzaji sahihi wa makosa
- Tumia zana za kupima kumbukumbu kwa uboreshaji

**Zana za Windows AI Foundry**
- Tumia Foundry Local CLI kwa majaribio na uhakikisho wa modeli
- Tumia zana za upimaji wa API za Windows AI kwa uhakikisho wa muungano
- Tekeleza uandikishaji maalum kwa ufuatiliaji wa operesheni za AI
- Tengeneza upimaji wa kiotomatiki kwa uaminifu wa utendaji wa AI

## Kuimarisha Programu Zako kwa Ajili ya Baadaye

### Teknolojia Zinazojitokeza

**Vifaa vya Kizazi Kipya**
- Tengeneza programu zinazotumia uwezo wa NPU wa baadaye
- Panga ukuaji wa ukubwa na ugumu wa modeli
- Tekeleza usanifu unaojibadilisha kwa vifaa vinavyoendelea
- Angalia algoriti za kuandaa kwa akili za quantum kwa utegemezi wa baadaye

**Uwezo wa AI wa Juu**
- Jiandae kwa muungano wa AI wa njia nyingi kwa aina zaidi za data
- Panga kwa ushirikiano wa AI kwa wakati halisi kati ya vifaa vingi
- Tengeneza kwa uwezo wa kujifunza kwa pamoja (federated learning)
- Angalia usanifu mchanganyiko wa kivuli-wingu cha akili (edge-cloud)

### Kujifunza Endelevu na Ujibadilishaji

**Sasisho za Modeli**
- Tekeleza taratibu zisizo na mshono za kusasisha modeli
- Tengeneza programu zenye uwezo wa kubadilika kwa uwezo wa modeli ulioimarishwa
- Panga kwa utangamano wa nyuma na modeli zilizopo
- Tekeleza upimaji wa A/B kwa tathmini ya utendaji wa modeli

**Mabadiliko ya Sifa**
- Tengeneza usanifu wa moduli unaorejesha uwezo mpya wa AI
- Panga muungano wa API za Windows AI zinazojitokeza
- Tekeleza bendera za sifa kwa utekelezaji wa uwezo hatua kwa hatua
- Tengeneza interfaces za mtumiaji zinazojibadilisha kwa sifa zilizoimarishwa za AI

## Hitimisho

Maendeleo ya Windows Edge AI yanawakilisha muunganiko wa uwezo mkubwa wa AI na jukwaa thabiti, salama, na linaloweza kupanuka la Windows. Kwa kumiliki ekosistimu ya Windows AI Foundry, watengenezaji wanaweza kuunda programu za akili zinazotoa uzoefu bora wa mtumiaji huku zikiweka viwango vya juu vya faragha, usalama, na utendaji.

Mchanganyiko wa API za Windows AI, Foundry Local, na Windows ML hutoa msingi usio na kifani kwa kujenga kizazi kijacho cha programu za akili za Windows. Kadri AI inavyoendelea, jukwaa la Windows linahakikisha programu zako zitapanuka kwa teknolojia zinazoibuka huku zikiendelea kulingana na muingiliano na utendaji katika ekosistimu zinazotofautiana za vifaa vya Windows.

Iwapo unajenga programu za watumiaji, suluhisho za biashara, au zana maalum za sekta, maendeleo ya Windows Edge AI yanakuwezesha kuunda uzoefu wa akili, wa haraka, na ulioingizwa kwa kina unaotumia uwezo kamili wa vifaa vya kisasa vya Windows.

## Rasilimali Zaidi

### Nyaraka na Kujifunza
- [Nyaraka za Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Marejeleo ya API za Windows AI](https://learn.microsoft.com/windows/ai/apis/)
- [Anza kujenga programu kwa API za Windows AI](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Kuanzia na Foundry Local](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Muhtasari wa Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Mahitaji ya Mfumo wa Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Mazoea ya Maendeleo ya Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Hifadhidata za Mifano na Msimbo
- [Mifano ya Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Mifano ya Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Mifano ya ONNX Runtime Inference](https://github.com/microsoft/onnxruntime-inference-examples)
- [Hifadhidata ya Mifano ya Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vifaa vya Maendeleo
- [Kifaa cha AI kwa Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Nyumba ya Maendeleo ya AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Mifano ya Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Vifaa vya Kubadilisha Mfano](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Msaada wa Kiufundi
- [Nyaraka za Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Nyaraka za ONNX Runtime](https://onnxruntime.ai/docs/)
- [Nyaraka za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Ripoti Masuala - Mifano ya Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Jamii na Msaada
- [Jumuiya ya Waendelezaji wa Windows](https://developer.microsoft.com/en-us/windows/)
- [Bolg ya Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Mafunzo ya AI ya Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Mwongozo huu umebuniwa kuendana na mabadiliko ya haraka katika mfumo wa Windows AI. Sasisho la mara kwa mara lina hakikisha ulinganifu na uwezo wa kisasa wa jukwaa pamoja na mbinu bora za maendeleo.*

[08. Vitendo na Microsoft Foundry Local - Kikokotoo Kamili cha Msaada kwa Waendelezaji](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->