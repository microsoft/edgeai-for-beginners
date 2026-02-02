# Mwongozo wa Maendeleo ya Windows Edge AI

## Utangulizi

Karibu kwenye Maendeleo ya Windows Edge AI - mwongozo wako wa kina wa kujenga programu za akili zinazotumia nguvu ya AI kwenye kifaa kupitia jukwaa la Microsoft Windows AI Foundry. Mwongozo huu umeundwa mahsusi kwa watengenezaji wa Windows wanaotaka kuingiza uwezo wa kisasa wa Edge AI kwenye programu zao huku wakitumia kikamilifu kasi ya vifaa vya Windows.

### Faida ya Windows AI

Windows AI Foundry ni jukwaa lililounganishwa, la kuaminika, na salama linalosaidia mzunguko mzima wa maendeleo ya AI - kutoka kuchagua na kurekebisha modeli hadi kuboresha na kupeleka kwenye CPU, GPU, NPU, na miundombinu ya wingu mseto. Jukwaa hili linapanua maendeleo ya AI kwa kutoa:

- **Uondoaji wa Vifaa**: Uwezo wa kupeleka bila shida kwenye vifaa vya AMD, Intel, NVIDIA, na Qualcomm
- **Akili ya Kifaa**: AI inayohifadhi faragha inayofanya kazi kikamilifu kwenye vifaa vya ndani
- **Utendaji Ulioboreshwa**: Modeli zilizoboreshwa kwa usanidi wa vifaa vya Windows
- **Tayari kwa Biashara**: Vipengele vya usalama wa daraja la uzalishaji na kufuata kanuni

### Windows ML
Windows Machine Learning (ML) inawawezesha watengenezaji wa C#, C++, na Python kuendesha modeli za AI za ONNX moja kwa moja kwenye kompyuta za Windows kupitia ONNX Runtime, na usimamizi wa kiotomatiki wa watoa huduma wa utekelezaji kwa vifaa tofauti (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) inaweza kutumika na modeli kutoka PyTorch, Tensorflow/Keras, TFLite, scikit-learn, na mifumo mingine.

![WindowsML Mchoro unaonyesha modeli ya ONNX ikipitia Windows ML na kufikia NPU, GPU, na CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML hutoa nakala ya Windows-wide ya ONNX Runtime, pamoja na uwezo wa kupakua watoa huduma wa utekelezaji (EPs) kwa njia ya nguvu.

### Kwa Nini Windows kwa Edge AI?

**Msaada wa Vifaa Vyote**
Windows ML inatoa uboreshaji wa kiotomatiki wa vifaa kote kwenye mfumo wa Windows, kuhakikisha programu zako za AI zinafanya kazi kwa ufanisi bila kujali usanifu wa vifaa vya msingi.

**Mazingira ya AI Yaliyounganishwa**
Injini ya inferensi ya Windows ML iliyojengwa ndani huondoa mahitaji ya usanidi mgumu, ikiruhusu watengenezaji kuzingatia mantiki ya programu badala ya masuala ya miundombinu.

**Uboreshaji wa PC ya Copilot+**
API zilizoundwa mahsusi kwa vifaa vya Windows vya kizazi kijacho vilivyo na Vitengo vya Usindikaji wa Neural (NPUs) vinavyotoa utendaji bora kwa kila watt.

**Mfumo wa Watengenezaji**
Zana tajiri ikiwa ni pamoja na ujumuishaji wa Visual Studio, nyaraka za kina, na programu za mfano zinazoharakisha mizunguko ya maendeleo.

## Malengo ya Kujifunza

Kwa kukamilisha mwongozo huu wa maendeleo ya Windows Edge AI, utakuwa na ujuzi muhimu wa kujenga programu za AI tayari kwa uzalishaji kwenye jukwaa la Windows.

### Ujuzi wa Kiufundi wa Msingi

**Ustadi wa Windows AI Foundry**
- Elewa usanifu na vipengele vya jukwaa la Windows AI Foundry
- Elekeza mzunguko mzima wa maendeleo ya AI ndani ya mfumo wa Windows
- Tekeleza mbinu bora za usalama kwa programu za AI kwenye kifaa
- Boreshaji programu kwa usanidi tofauti wa vifaa vya Windows

**Utaalamu wa Ujumuishaji wa API**
- Elewa API za Windows AI kwa programu za maandishi, maono, na multimodal
- Tekeleza ujumuishaji wa modeli ya lugha ya Phi Silica kwa kizazi cha maandishi na uamuzi
- Peleka uwezo wa maono ya kompyuta kwa kutumia API za usindikaji wa picha zilizojengwa ndani
- Rekebisha modeli zilizofunzwa awali kwa kutumia mbinu za LoRA (Low-Rank Adaptation)

**Utekelezaji wa Foundry Local**
- Vinjari, tathmini, na peleka modeli za lugha za chanzo wazi kwa kutumia Foundry Local CLI
- Elewa uboreshaji wa modeli na upunguzaji kwa utekelezaji wa ndani
- Tekeleza uwezo wa AI wa nje ya mtandao unaofanya kazi bila muunganisho wa intaneti
- Simamia mizunguko ya maisha ya modeli na masasisho katika mazingira ya uzalishaji

**Upelekaji wa Windows ML**
- Leta modeli za ONNX zilizobinafsishwa kwenye programu za Windows kwa kutumia Windows ML
- Tumia kasi ya vifaa kiotomatiki kwenye usanifu wa CPU, GPU, na NPU
- Tekeleza inferensi ya wakati halisi kwa matumizi bora ya rasilimali
- Buni programu za AI zinazoweza kupanuka kwa kategoria mbalimbali za vifaa vya Windows

### Ujuzi wa Maendeleo ya Programu

**Maendeleo ya Windows ya Msalaba-Jukwaa**
- Jenga programu zinazotumia AI kwa kutumia .NET MAUI kwa upelekaji wa Windows wa ulimwengu
- Jumuisha uwezo wa AI kwenye Win32, UWP, na Programu za Wavuti Zinazoendelea
- Tekeleza miundo ya UI inayojibika inayobadilika kulingana na hali za usindikaji wa AI
- Shughulikia operesheni za AI zisizo za wakati mmoja kwa mifumo sahihi ya uzoefu wa mtumiaji

**Uboreshaji wa Utendaji**
- Profaili na boresha utendaji wa inferensi ya AI kwenye usanidi tofauti wa vifaa
- Tekeleza usimamizi mzuri wa kumbukumbu kwa modeli kubwa za lugha
- Buni programu zinazopungua kwa neema kulingana na uwezo wa vifaa vilivyopo
- Tumia mikakati ya kuhifadhi kwa operesheni za AI zinazotumika mara kwa mara

**Uwezo wa Uzalishaji**
- Tekeleza utunzaji wa makosa wa kina na mifumo ya kurudi nyuma
- Buni telemetry na ufuatiliaji wa utendaji wa programu za AI
- Tumia mbinu bora za usalama kwa uhifadhi wa modeli za AI za ndani na utekelezaji
- Panga mikakati ya upelekaji kwa programu za biashara na watumiaji

### Uelewa wa Kibiashara na Mkakati

**Usanifu wa Programu za AI**
- Buni usanifu mseto unaoboreshwa kati ya usindikaji wa AI wa ndani na wa wingu
- Tathmini faida na hasara kati ya ukubwa wa modeli, usahihi, na kasi ya inferensi
- Panga usanifu wa mtiririko wa data unaohifadhi faragha huku ukiruhusu akili
- Tekeleza suluhisho za AI za gharama nafuu zinazopanuka kulingana na mahitaji ya watumiaji

**Nafasi ya Soko**
- Elewa faida za ushindani za programu za AI za asili za Windows
- Tambua matumizi ambapo AI kwenye kifaa inatoa uzoefu bora wa mtumiaji
- Buni mikakati ya kuingia sokoni kwa programu za Windows zilizoimarishwa na AI
- Weka programu ili kutumia faida za mfumo wa Windows

## Sampuli za AI za Windows App SDK

Windows App SDK inatoa sampuli za kina zinazoonyesha ujumuishaji wa AI kwenye mifumo mbalimbali na hali za upelekaji. Sampuli hizi ni marejeleo muhimu kwa kuelewa mifumo ya maendeleo ya Windows AI.

### Sampuli za Windows AI Foundry

| Sampuli | Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Ujumuishaji wa API za Windows AI | Programu kamili ya WinUI inayoonyesha API za Windows AI, uboreshaji wa ARM64, upelekaji wa kifurushi |

**Teknolojia Muhimu:**
- API za Windows AI
- Mfumo wa WinUI 3
- Uboreshaji wa jukwaa la ARM64
- Utangamano wa PC ya Copilot+
- Upelekaji wa programu iliyofungashwa

**Mahitaji ya Awali:**
- Windows 11 na PC ya Copilot+ inapendekezwa
- Visual Studio 2022
- Usanidi wa ujenzi wa ARM64
- Windows App SDK 1.8.1+

### Sampuli za Windows ML

#### Sampuli za C++

| Sampuli | Aina | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Windows ML ya Msingi | Ugunduzi wa EP, chaguo za mstari wa amri, uundaji wa modeli |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Upelekaji wa Mfumo | Runtime ya pamoja, alama ndogo ya upelekaji |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Upelekaji wa Kujitegemea | Upelekaji wa pekee, hakuna utegemezi wa runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Matumizi ya Maktaba | WindowsML katika maktaba ya pamoja, usimamizi wa kumbukumbu |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, uundaji wa EP, Mafunzo ya Build 2025 |

#### Sampuli za C#

**Programu za Console**

| Sampuli | Aina | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Programu ya Console | Ujumuishaji wa Msingi wa C# | Matumizi ya msaada wa pamoja, interface ya mstari wa amri |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, uundaji wa EP, Mafunzo ya Build 2025 |

**Programu za GUI**

| Sampuli | Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI ya Desktop | Uainishaji wa picha na interface ya WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI ya Kawaida | Uainishaji wa picha na Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI ya Kisasa | Uainishaji wa picha na interface ya WinUI 3 |

#### Sampuli za Python

| Sampuli | Lugha | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Uainishaji wa Picha | Viunganishi vya WinML Python, usindikaji wa picha kwa kundi |

### Mahitaji ya Awali ya Sampuli

**Mahitaji ya Mfumo:**
- Kompyuta ya Windows 11 inayoendesha toleo la 24H2 (build 26100) au zaidi
- Visual Studio 2022 na mzigo wa kazi wa C++ na .NET
- Windows App SDK 1.8.1 au baadaye
- Python 3.10-3.13 kwa sampuli za Python kwenye vifaa vya x64 na ARM64

**Mahususi kwa Windows AI Foundry:**
- PC ya Copilot+ inapendekezwa kwa utendaji bora
- Usanidi wa ujenzi wa ARM64 kwa sampuli za Windows AI
- Utambulisho wa kifurushi unahitajika (programu zisizofungashwa hazina msaada tena)

### Mtiririko wa Kawaida wa Sampuli

Sampuli nyingi za Windows ML hufuata mtindo huu wa kawaida:

1. **Anzisha Mazingira** - Unda mazingira ya ONNX Runtime
2. **Sajili Watoa Huduma wa Utekelezaji** - Gundua na sajili kasi za vifaa zinazopatikana (CPU, GPU, NPU)
3. **Pakia Modeli** - Pakia modeli ya ONNX, kwa hiari unda kwa vifaa lengwa
4. **Tayarisha Ingizo** - Badilisha picha/data kuwa muundo wa ingizo wa modeli
5. **Endesha Inferensi** - Tekeleza modeli na pata utabiri
6. **Chakata Matokeo** - Tumia softmax na onyesha utabiri wa juu

### Faili za Modeli Zinazotumika

| Modeli | Kusudi | Imejumuishwa | Maelezo |
|-------|---------|----------|-------|
| SqueezeNet | Uainishaji wa picha nyepesi | ✅ Imejumuishwa | Imefunzwa awali, tayari kutumika |
| ResNet-50 | Uainishaji wa picha wa usahihi wa juu | ❌ Inahitaji ubadilishaji | Tumia [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kwa ubadilishaji |

### Msaada wa Vifaa

Sampuli zote hugundua na kutumia vifaa vinavyopatikana kiotomatiki:
- **CPU** - Msaada wa ulimwengu kote kwenye vifaa vyote vya Windows
- **GPU** - Ugunduzi wa kiotomatiki na uboreshaji kwa vifaa vya picha vinavyopatikana
- **NPU** - Inatumia Vitengo vya Usindikaji wa Neural kwenye vifaa vinavyoungwa mkono (PC za Copilot+)

## Vipengele vya Jukwaa la Windows AI Foundry

### 1. API za Windows AI

API za Windows AI hutoa uwezo wa AI ulio tayari kutumika unaotumia modeli za kifaa, zilizoboreshwa kwa ufanisi na utendaji kwenye vifaa vya PC vya Copilot+ na mahitaji madogo ya usanidi.

#### Makundi ya API Muhimu

**Modeli ya Lugha ya Phi Silica**
- Modeli ndogo lakini yenye nguvu ya lugha kwa kizazi cha maandishi na uamuzi
- Imeboreshwa kwa inferensi ya wakati halisi na matumizi madogo ya nguvu
- Msaada wa kurekebisha kwa kutumia mbinu za LoRA
- Ujumuishaji na utafutaji wa semantic wa Windows na upatikanaji wa maarifa

**API za Maono ya Kompyuta**
- **Utambuzi wa Maandishi (OCR)**: Toa maandishi kutoka kwa picha kwa usahihi wa juu
- **Azimio la Picha ya Juu**: Panua picha kwa kutumia modeli za AI za ndani
- **Ugawaji wa Picha**: Tambua na tenga vitu maalum kwenye picha
- **Maelezo ya Picha**: Tengeneza maelezo ya maandishi ya kina kwa maudhui ya kuona
- **Kuondoa Vitu**: Ondoa vitu visivyohitajika kutoka kwa picha kwa kutumia uchoraji wa AI

**Uwezo wa Multimodal**
- **Ujumuishaji wa Maono-Lugha**: Changanya uelewa wa maandishi na picha
- **Utafutaji wa Semantic**: Ruhusu maswali ya lugha asilia kwenye maudhui ya multimedia
- **Upatikanaji wa Maarifa**: Jenga uzoefu wa utafutaji wa akili kwa data ya ndani

### 2. Foundry Local

Foundry Local inawapa watengenezaji ufikiaji wa haraka wa modeli za lugha za chanzo wazi zinazotumika kwenye Silicon ya Windows, ikitoa uwezo wa kuvinjari, kujaribu, kuingiliana, na kupeleka modeli kwenye programu za ndani.

#### Programu za Sampuli za Foundry Local

Hifadhi ya [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) inatoa sampuli za kina kwenye lugha na mifumo mbalimbali ya programu, ikionyesha mifumo tofauti ya ujumuishaji na matumizi.

| Sampuli | Lugha/Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Utekelezaji wa RAG | Ujumuishaji wa Kernel ya Semantic, hifadhi ya vekta ya Qdrant, embeddings za JINA, uingizaji wa hati, mazungumzo ya mtiririko |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Programu ya Mazungumzo ya Desktop | Mazungumzo ya msalaba-jukwaa, kubadilisha modeli za ndani/wingu, ujumuishaji wa SDK ya OpenAI, mtiririko wa wakati halisi |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/s
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Muunganiko wa Mifumo | Matumizi ya SDK ya kiwango cha chini, operesheni za async, mteja wa HTTP reqwest |

#### Makundi ya Sampuli kulingana na Matumizi

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Utekelezaji kamili wa RAG ukitumia Semantic Kernel, hifadhidata ya vekta ya Qdrant, na embeddings za JINA
- **Muundo**: Kuingiza hati → Kugawanya maandishi → Embeddings za vekta → Utafutaji wa mfanano → Majibu yanayozingatia muktadha
- **Teknolojia**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, kukamilisha mazungumzo kwa njia ya mtiririko

**Programu za Kompyuta**
- **electron/foundry-chat**: Programu ya mazungumzo tayari kwa uzalishaji yenye kubadilisha modeli kati ya ndani/wingu
- **Vipengele**: Chaguo la modeli, majibu ya mtiririko, kushughulikia makosa, usambazaji wa majukwaa mbalimbali
- **Muundo**: Mchakato mkuu wa Electron, mawasiliano ya IPC, maandiko ya awali salama

**Mifano ya Muunganiko wa SDK**
- **JavaScript (Node.js)**: Mwingiliano wa msingi wa modeli na majibu ya mtiririko
- **Python**: Matumizi ya API inayolingana na OpenAI na mtiririko wa async
- **Rust**: Muunganiko wa kiwango cha chini ukitumia reqwest na tokio kwa operesheni za async

#### Mahitaji ya Awali kwa Sampuli za Foundry Local

**Mahitaji ya Mfumo:**
- Windows 11 yenye Foundry Local iliyosakinishwa
- Node.js v16+ kwa sampuli za JavaScript/Electron
- .NET 8.0+ kwa sampuli za C#
- Python 3.10+ kwa sampuli za Python
- Rust 1.70+ kwa sampuli za Rust

**Usakinishaji:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Usanidi Maalum wa Sampuli

**Sampuli ya dotNET RAG:**
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

**Sampuli ya Mazungumzo ya Electron:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Sampuli za JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Vipengele Muhimu

**Katalogi ya Modeli**
- Mkusanyiko kamili wa modeli za chanzo wazi zilizoboreshwa
- Modeli zilizoboreshwa kwa CPU, GPU, na NPU kwa usambazaji wa haraka
- Msaada kwa familia maarufu za modeli ikiwa ni pamoja na Llama, Mistral, Phi, na modeli za kikoa maalum

**Muunganiko wa CLI**
- Kiolesura cha mstari wa amri kwa usimamizi wa modeli na usambazaji
- Michakato ya kiotomatiki ya uboreshaji na upunguzaji
- Muunganiko na mazingira maarufu ya maendeleo na mabomba ya CI/CD

**Usambazaji wa Ndani**
- Uendeshaji kamili wa nje ya mtandao bila utegemezi wa wingu
- Msaada kwa miundo ya modeli maalum na usanidi
- Huduma ya modeli yenye ufanisi na uboreshaji wa kiotomatiki wa vifaa

### 3. Windows ML

Windows ML inahudumu kama jukwaa kuu la AI na mazingira ya utekelezaji wa inferensi kwenye Windows, ikiruhusu watengenezaji kusambaza modeli maalum kwa ufanisi kwenye mfumo mpana wa vifaa vya Windows.

#### Faida za Muundo

**Msaada wa Vifaa vya Ulimwenguni**
- Uboreshaji wa kiotomatiki kwa silikoni za AMD, Intel, NVIDIA, na Qualcomm
- Msaada kwa utekelezaji wa CPU, GPU, na NPU na ubadilishaji wa uwazi
- Abstrakta ya vifaa inayondoa kazi ya uboreshaji maalum wa jukwaa

**Uwezo wa Modeli**
- Msaada kwa muundo wa modeli wa ONNX na ubadilishaji wa kiotomatiki kutoka kwa mifumo maarufu
- Usambazaji wa modeli maalum na utendaji wa kiwango cha uzalishaji
- Muunganiko na miundo ya programu ya Windows iliyopo

**Muunganiko wa Biashara**
- Inalingana na mifumo ya usalama na ufuatiliaji ya Windows
- Msaada kwa zana za usambazaji na usimamizi wa biashara
- Muunganiko na mifumo ya usimamizi na ufuatiliaji wa vifaa vya Windows

## Mtiririko wa Maendeleo

### Awamu ya 1: Usanidi wa Mazingira na Zana

**Maandalizi ya Mazingira ya Maendeleo**
1. Sakinisha Visual Studio 2022 na mizigo ya C++ na .NET
2. Sakinisha Windows App SDK 1.8.1 au zaidi
3. Sanidi zana za CLI za Windows AI Foundry
4. Sanidi kiendelezi cha AI Toolkit kwa Visual Studio Code
5. Weka zana za ufuatiliaji wa utendaji
6. Hakikisha usanidi wa ARM64 kwa uboreshaji wa Copilot+ PC

**Usanidi wa Hifadhi ya Sampuli**
1. Clone [Hifadhi ya Sampuli za Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Nenda kwenye `Samples/WindowsAIFoundry/cs-winui` kwa mifano ya API ya Windows AI
3. Nenda kwenye `Samples/WindowsML` kwa mifano kamili ya Windows ML
4. Kagua [mahitaji ya ujenzi](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) kwa majukwaa yako lengwa

**Uchunguzi wa Jumba la Maendeleo ya AI**
- Chunguza programu za sampuli na utekelezaji wa marejeleo
- Jaribu API za Windows AI na maonyesho ya mwingiliano
- Kagua msimbo wa chanzo kwa mbinu bora na mifumo
- Tambua sampuli zinazofaa kwa matumizi yako maalum

### Awamu ya 2: Uchaguzi wa Modeli na Muunganiko

**Uchambuzi wa Mahitaji**
- Tambua mahitaji ya kiutendaji kwa uwezo wa AI
- Weka vikwazo vya utendaji na malengo ya uboreshaji
- Tathmini mahitaji ya faragha na usalama
- Panga muundo wa usambazaji na mikakati ya kupanua

**Tathmini ya Modeli**
- Tumia Foundry Local kujaribu modeli za chanzo wazi kwa matumizi yako
- Pima API za Windows AI dhidi ya mahitaji ya modeli maalum
- Tathmini faida na hasara kati ya ukubwa wa modeli, usahihi, na kasi ya inferensi
- Tengeneza mbinu za muunganiko kwa modeli zilizochaguliwa

### Awamu ya 3: Maendeleo ya Programu

**Muunganiko wa Msingi**
- Tekeleza muunganiko wa API za Windows AI na kushughulikia makosa ipasavyo
- Buni kiolesura cha mtumiaji kinachokidhi mtiririko wa usindikaji wa AI
- Tekeleza mikakati ya kuhifadhi na uboreshaji kwa inferensi ya modeli
- Ongeza telemetry na ufuatiliaji kwa utendaji wa operesheni za AI

**Upimaji na Uthibitishaji**
- Jaribu programu kwenye usanidi tofauti wa vifaa vya Windows
- Thibitisha vipimo vya utendaji chini ya hali mbalimbali za mzigo
- Tekeleza upimaji wa kiotomatiki kwa uaminifu wa utendaji wa AI
- Fanya upimaji wa uzoefu wa mtumiaji na vipengele vilivyoboreshwa na AI

### Awamu ya 4: Uboreshaji na Usambazaji

**Uboreshaji wa Utendaji**
- Pima utendaji wa programu kwenye usanidi lengwa wa vifaa
- Boresha matumizi ya kumbukumbu na mikakati ya kupakia modeli
- Tekeleza tabia ya kubadilika kulingana na uwezo wa vifaa vilivyopo
- Rekebisha uzoefu wa mtumiaji kwa hali tofauti za utendaji

**Usambazaji wa Uzalishaji**
- Funga programu na utegemezi sahihi wa modeli za AI
- Tekeleza mifumo ya masasisho kwa modeli na mantiki ya programu
- Sanidi ufuatiliaji na uchanganuzi kwa mazingira ya uzalishaji
- Panga mikakati ya usambazaji kwa biashara na watumiaji wa kawaida

## Mifano ya Utekelezaji wa Kivitendo

### Mfano 1: Programu ya Usindikaji wa Nyaraka za Kijasusi

Tengeneza programu ya Windows inayosindika nyaraka kwa kutumia uwezo mbalimbali wa AI:

**Teknolojia Zilizotumika:**
- Phi Silica kwa muhtasari wa nyaraka na kujibu maswali
- API za OCR kwa uchimbaji wa maandishi kutoka nyaraka zilizochanganuliwa
- API za Maelezo ya Picha kwa uchambuzi wa chati na michoro
- Modeli za ONNX maalum kwa uainishaji wa nyaraka

**Mbinu ya Utekelezaji:**
- Buni muundo wa moduli na vipengele vya AI vinavyoweza kuunganishwa
- Tekeleza usindikaji wa async kwa mafungu makubwa ya nyaraka
- Ongeza viashiria vya maendeleo na msaada wa kughairi kwa operesheni za muda mrefu
- Jumuisha uwezo wa nje ya mtandao kwa usindikaji wa nyaraka nyeti

### Mfano 2: Mfumo wa Usimamizi wa Hesabu ya Rejareja

Tengeneza mfumo wa hesabu unaotumia AI kwa matumizi ya rejareja:

**Teknolojia Zilizotumika:**
- Ugawaji wa Picha kwa utambuzi wa bidhaa
- Modeli za maono maalum kwa uainishaji wa chapa na kategoria
- Usambazaji wa Foundry Local wa modeli za lugha maalum za rejareja
- Muunganiko na mifumo ya POS na hesabu iliyopo

**Mbinu ya Utekelezaji:**
- Jenga muunganiko wa kamera kwa uchanganuzi wa bidhaa kwa wakati halisi
- Tekeleza utambuzi wa barcode na bidhaa kwa njia ya kuona
- Ongeza maswali ya hesabu kwa lugha asilia ukitumia modeli za lugha za ndani
- Buni muundo unaoweza kupanuka kwa usambazaji wa maduka mengi

### Mfano 3: Msaidizi wa Nyaraka za Huduma za Afya

Tengeneza zana ya nyaraka za huduma za afya inayohifadhi faragha:

**Teknolojia Zilizotumika:**
- Phi Silica kwa kizazi cha maelezo ya matibabu na msaada wa maamuzi ya kliniki
- OCR kwa kubadilisha rekodi za matibabu zilizoandikwa kwa mkono kuwa za kidijitali
- Modeli za lugha za matibabu maalum zilizotumwa kupitia Windows ML
- Hifadhi ya vekta ya ndani kwa urejeshaji wa maarifa ya matibabu

**Mbinu ya Utekelezaji:**
- Hakikisha uendeshaji kamili wa nje ya mtandao kwa faragha ya mgonjwa
- Tekeleza uthibitishaji wa istilahi za matibabu na mapendekezo
- Ongeza kumbukumbu za ukaguzi kwa kufuata kanuni
- Buni muunganiko na mifumo iliyopo ya Rekodi za Afya za Kielektroniki

## Mikakati ya Uboreshaji wa Utendaji

### Maendeleo Yanayozingatia Vifaa

**Uboreshaji wa NPU**
- Buni programu zinazotumia uwezo wa NPU kwenye PC za Copilot+
- Tekeleza kurudi kwa GPU/CPU kwa vifaa visivyo na NPU
- Boresha miundo ya modeli kwa kasi maalum ya NPU
- Fuatilia matumizi ya NPU na sifa za joto

**Usimamizi wa Kumbukumbu**
- Tekeleza mikakati bora ya kupakia na kuhifadhi modeli
- Tumia ramani ya kumbukumbu kwa modeli kubwa ili kupunguza muda wa kuanza
- Buni programu zinazojali kumbukumbu kwa vifaa vyenye rasilimali ndogo
- Tekeleza upunguzaji wa modeli kwa uboreshaji wa kumbukumbu

**Ufanisi wa Betri**
- Boresha operesheni za AI kwa matumizi ya nguvu ya chini
- Tekeleza usindikaji unaobadilika kulingana na hali ya betri
- Buni usindikaji wa nyuma wenye ufanisi kwa operesheni za AI zinazoendelea
- Tumia zana za ufuatiliaji wa nguvu ili kuboresha matumizi ya nishati

### Mawazo ya Kupanuka

**Uendeshaji wa Nyuzi Nyingi**
- Buni operesheni za AI salama kwa nyuzi kwa usindikaji wa pamoja
- Tekeleza usambazaji wa kazi kwa ufanisi kwenye cores zilizopo
- Tumia mifumo ya async/await kwa operesheni za AI zisizozuia
- Panga uboreshaji wa pool ya nyuzi kwa usanidi tofauti wa vifaa

**Mikakati ya Kuhifadhi**
- Tekeleza uhifadhi wa akili kwa operesheni za AI zinazotumika mara kwa mara
- Buni mikakati ya kubatilisha uhifadhi kwa masasisho ya modeli
- Tumia uhifadhi wa kudumu kwa operesheni za usindikaji wa gharama kubwa
- Tekeleza uhifadhi wa usambazaji kwa hali za watumiaji wengi

## Mbinu Bora za Usalama na Faragha

### Ulinzi wa Data

**Usindikaji wa Ndani**
- Hakikisha data nyeti haiondoki kwenye kifaa cha ndani
- Tekeleza uhifadhi salama kwa modeli za AI na data ya muda
- Tumia vipengele vya usalama vya Windows kwa sandboxing ya programu
- Tumia usimbaji kwa modeli zilizohifadhiwa na matokeo ya usindikaji wa kati

**Usalama wa Modeli**
- Thibitisha uadilifu wa modeli kabla ya kupakia na utekelezaji
- Tekeleza mifumo salama ya masasisho ya modeli
- Tumia modeli zilizotiwa saini ili kuzuia uharibifu
- Tekeleza udhibiti wa ufikiaji kwa faili za modeli na usanidi

### Mawazo ya Uzingatiaji

**Ulinganifu wa Kanuni**
- Buni programu zinazokidhi GDPR, HIPAA, na mahitaji mengine ya kanuni
- Tekeleza kumbukumbu za ukaguzi kwa michakato ya maamuzi ya AI
- Toa vipengele vya uwazi kwa matokeo yanayotokana na AI
- Ruhusu udhibiti wa mtumiaji juu ya usindikaji wa data ya AI

**Usalama wa Biashara**
- Jumuisha na sera za usalama za biashara za Windows
- Msaada wa usambazaji unaosimamiwa kupitia zana za usimamizi wa biashara
- Tekeleza udhibiti wa ufikiaji kulingana na majukumu kwa vipengele vya AI
- Toa udhibiti wa kiutawala kwa utendaji wa AI

## Utatuzi wa Matatizo na Ufuatiliaji

### Changamoto za Kawaida za Maendeleo

**Masuala ya Usanidi wa Ujenzi**
- Hakikisha usanidi wa jukwaa la ARM64 kwa sampuli za API za Windows AI
- Thibitisha utangamano wa toleo la Windows App SDK (1.8.1+ inahitajika)
- Angalia kwamba kitambulisho cha kifurushi kimewekwa ipasavyo (kinahitajika kwa API za Windows AI)
- Thibitisha kwamba zana za ujenzi zinaunga mkono toleo lengwa la mfumo

**Masuala ya Kupakia Modeli**
- Thibitisha utangamano wa modeli za ONNX na Windows ML
- Angalia uadilifu wa faili za modeli na mahitaji ya muundo
- Thibitisha mahitaji ya uwezo wa vifaa kwa modeli maalum
- Fuatilia masuala ya ugawaji wa kumbukumbu wakati wa kupakia modeli
- Hakikisha usajili wa mtoa huduma wa utekelezaji kwa kasi ya vifaa

**Mawazo ya Hali ya Usambazaji**
- **Hali ya Kujitegemea**: Inasaidiwa kikamilifu na ukubwa mkubwa wa usambazaji
- **Hali Inayotegemea Mfumo**: Alama ndogo lakini inahitaji runtime ya pamoja
- **Programu Zisizopakiwa**: Hazisaidiwi tena kwa API za Windows AI
- Tumia `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kwa usambazaji wa ARM64 wa kujitegemea

**Matatizo ya Utendaji**
- Pima utendaji wa programu kwenye usanidi tofauti wa vifaa
- Tambua vizuizi katika mifumo ya usindikaji wa AI
- Boresha operesheni za usindikaji wa data kabla na baada
- Tekeleza ufuatiliaji wa utendaji na tahadhari

**Ugumu wa Muunganiko**
- Fuatilia masuala ya muunganiko wa API kwa kushughulikia makosa ipasavyo
- Thibitisha miundo ya data ya pembejeo na mahitaji ya usindikaji wa awali
- Jaribu hali za ukingo na hali za makosa kwa kina
- Tekeleza kumbukumbu kamili kwa utatuzi wa masuala ya uzalishaji

### Zana na Mbinu za Ufuatiliaji

**Muunganiko wa Visual Studio**
- Tumia debugger ya AI Toolkit kwa uchambuzi wa utekelezaji wa modeli
- Tekeleza ufuatiliaji wa utendaji kwa operesheni za AI
- Fuatilia operesheni za AI za async kwa kushughulikia vizuizi ipasavyo
- Tumia zana za ufuatiliaji wa kumbukumbu kwa uboreshaji

**Zana za Windows AI Foundry**
- Tumia CLI ya Foundry Local kwa upimaji na uthibitishaji wa modeli
- Tumia
- [Muhtasari wa Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Mahitaji ya Mfumo wa Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Usanidi wa Mazingira ya Maendeleo ya Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Hifadhi za Sampuli na Msimbo
- [Sampuli za Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Sampuli za Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Mifano ya Utambuzi wa ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Hifadhi ya Sampuli za Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Zana za Maendeleo
- [AI Toolkit kwa Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Sampuli za Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Zana za Ubadilishaji wa Miundo](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Usaidizi wa Kiufundi
- [Nyaraka za Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Nyaraka za ONNX Runtime](https://onnxruntime.ai/docs/)
- [Nyaraka za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Ripoti Masuala - Sampuli za Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Jamii na Usaidizi
- [Jamii ya Watengenezaji wa Windows](https://developer.microsoft.com/en-us/windows/)
- [Blogu ya Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Mafunzo ya Microsoft Learn AI](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Mwongozo huu umeundwa kuendana na maendeleo ya haraka ya mfumo wa Windows AI. Sasisho za mara kwa mara huhakikisha ulinganifu na uwezo wa hivi karibuni wa jukwaa na mbinu bora za maendeleo.*

[08. Kufanya Kazi na Microsoft Foundry Local - Kifurushi Kamili cha Zana za Watengenezaji](../Module08/README.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.