# AGENTS.md

> **មគ_GRAPH ដំណើរការអ្នកអភិវឌ្ឍសម្រាប់ការរួមរបស់ EdgeAI សម្រាប់អ្នកចាប់ផ្តើម**
> 
> ឯកសារនេះផ្តល់ព័ត៌មានលម្អិតសម្រាប់អ្នកអភិវឌ្ឍន៍, បំណងAI, និងអ្នករួមចំណែកដែលបានធ្វើការជាមួយrepository នេះ។ វាផ្តោតលើការតំឡើង វីធានការអភិវឌ្ឍ, ការតេស្ត, និងការអនុវត្តល្អបំផុត។
> 
> **បានធ្វើបច្ចុប្បន្នភាពចុងក្រោយ**៖ តុលា 30, 2025 | **កំណែឯកសារ**៖ 3.0

## តារាងមាតិកា

- [ទិដ្ឋភាពជុំវិញគម្រោង](#ទិដ្ឋភាពជុំវិញគម្រោង)
- [រចនាសម្ព័ន្ធRepository](#រចនាសម្ព័ន្ធrepository)
- [លក្ខខណ្ឌជាមុន](#លក្ខខណ្ឌជាមុន)
- [ពាក្យបញ្ជាតំឡើង](#ពាក្យបញ្ជាតំឡើង)
- [ដំណើរការអភិវឌ្ឍ](#ដំណើរការអភិវឌ្ឍ)
- [ការណែនាំស្តីពីការតេស្ត](#ការណែនាំស្តីពីការតេស្ត)
- [ការណែនាំនៃរចនាសម្ព័ន្ធកូដ](#ការណែនាំនៃរចនាសម្ព័ន្ធកូដ)
- [ការណែនាំស្តីពីការផ្ញើ Pull Request](#ការណែនាំស្តីពីការផ្ញើ-pull-request)
- [ប្រព័ន្ធបកប្រែ](#ប្រព័ន្ធបកប្រែ)
- [ការតភ្ជាប់ Foundry Local](#ការតភ្ជាប់-foundry-local)
- [ការសាងសង់ និងការបញ្ជូន](#ការសាងសង់-និងការបញ្ជូន)
- [បញ្ហាធម្មតា និងវិធីដោះស្រាយ](#បញ្ហាធម្មតា-និងវិធីដោះស្រាយ)
- [ធនធានបន្ថែម](#ធនធានបន្ថែម)
- [កំណត់សម្គាល់ជាក់លាក់កម្មវិធី](#កំណត់សម្គាល់ជាក់លាក់កម្មវិធី)
- [ការជួយទទួលបានជំនួយ](#លទ្ធភាពទទួលជំនួយ)

## ទិដ្ឋភាពជុំវិញគម្រោង

EdgeAI សម្រាប់អ្នកចាប់ផ្តើមគឺជាគ្រប់គ្រងព័ត៌មានសិក្សាធម្មតាដែលបង្រៀនអភិវឌ្ឍន៍ Edge AI ជាមួយម៉ូដែលភាសាតិច (SLMs)។ វគ្គបណ្តុះបណ្តាលគឺប្រហែលដល់មូលដ្ឋានEdgeAI, ការបំពេញម៉ូដែល, បច្ចេកវិទ្យាថែមទ្រីក, និងការអនុវត្តផលិតកម្មប្រើ Microsoft Foundry Local និងវេទិកា AI ផ្សេងៗ។

**បច្ចេកវិទ្យាផ្លូវការ៖**
- Python 3.8+ (ភាសាផ្នែកសំខាន់សម្រាប់គំរូ AI/ML)
- .NET C# (គំរូ AI/ML)
- JavaScript/Node.js ជាមួយ Electron (សម្រាប់កម្មវិធីតុ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- វេទិកា AI: LangChain, Semantic Kernel, Chainlit
- ការបញ្ជូលម៉ូដែល៖ Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ប្រភេទ Repository:** ការសិក្សា ដែលមានមេរៀនទាំង 8 និងកម្មវិធីគំរូទាំង 10។

**វីធីសាស្ត្រអាគារណ៍**៖ ផ្លូវការសម្រាប់ការសិក្សាច្រើនជំហានជាមួយគំរូដែលបង្ហាញពីរចនាប័ទ្មការបញ្ចូលEdge AI

## រចនាសម្ព័ន្ធRepository

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## លក្ខខណ្ឌជាមុន

### ឧបករណ៍ចាំបាច់

- **Python 3.8+** - សម្រាប់គំរូ AI/ML និងសៀវភៅកំណត់ត្រា
- **Node.js 16+** - សម្រាប់កម្មវិធីគំរូ Electron
- **Git** - សម្រាប់គ្រប់គ្រងកំណែ
- **Microsoft Foundry Local** - សម្រាប់រត់ម៉ូដែល AI ដោយផ្ទាល់

### ឧបករណ៍ដែលបានណែនាំ

- **Visual Studio Code** - ជាមួយបន្ថែម Python, Jupyter, និង Pylance
- **Windows Terminal** - សម្រាប់បទពិសោធន៍បន្ទាត់ពាក្យប្រសើរ (សម្រាប់អ្នកប្រើWindows)
- **Docker** - សម្រាប់ការអភិវឌ្ឍតាម container (ចំណង់ចំណូលចិត្ត)

### តម្រូវការប្រព័ន្ធ

- **RAM**: អប្បបរមា 8GB, 16GB+ រៀបចំសម្រាប់សេណារីយ៉ូម៉ូដែលច្រើន
- **ផ្ទុកទិន្នន័យ**: ចោលទទេ 10GB+ សម្រាប់ម៉ូដែល និងការគាំទ្រ
- **ប្រព័ន្ធប្រតិបត្តិការ**: Windows 10/11, macOS 11+, ឬ Linux (Ubuntu 20.04+)
- **មជ្ឈមណ្ឌលឧបករណ៍**: CPU ដែលគាំទ្រ AVX2; GPU (CUDA, Qualcomm NPU) ជាជម្រើសប៉ុន្តែណែនាំ

### ចំណេះដឹងជាមុន

- យល់ដឹងមូលដ្ឋានពីកម្មវិធី Python
- ជំនាញប្រើប្រាស់បន្ទាត់ពាក្យ
- យល់ដឹងពីមូលដ្ឋាន AI/ML (សម្រាប់ការអភិវឌ្ឍគំរូ)
- ការងារជាមួយ Git និងដំណើរការបញ្ចូន pull request

## ពាក្យបញ្ជាតំឡើង

### ការតំឡើង Repository

```bash
# ប្នក់ប្តូរផ្ទាំងផ្ទុក
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# មិនចាំបាច់មានដំណាក់កាលសាងសង់ទេ - នេះគឺជាផ្ទាំងផ្ទុកខ្លឹមសារអប់រំមូលដ្ឋាន
```

### ការតំឡើងគំរូ Python (Module08 និងគំរូ Workshop)

```bash
# បង្កើត និងសកម្មបរិយាកាសវីរុស្ស
python -m venv .venv
# នៅលើ Windows
.venv\Scripts\activate
# នៅលើ macOS/Linux
source .venv/bin/activate

# ដំឡើង Foundry Local SDK និងកាលបរិច្ឆេទពឹងផ្អែក
pip install foundry-local-sdk openai

# ដំឡើងកាលបរិច្ឆេទពឹងផ្អែកបន្ថែមសម្រាប់ម៉ូឌុល08 ឧទាហរណ៍
cd Module08
pip install -r requirements.txt

# ដំឡើងកាលបរិច្ឆេទពឹងផ្អែកសិក្ខាសាលា
cd ../Workshop
pip install -r requirements.txt
```

### ការតំឡើងគំរូ Node.js (គំរូ 08 - កម្មវិធីជជែក Windows)

```bash
cd Module08/samples/08
npm install

# ចាប់ផ្តើមក្នុងរបៀបអភិវឌ្ឍន៍
npm run dev

# សាងសង់សម្រាប់ការផលិត
npm run build

# បង្កើតកម្មវិធីដំឡើង
npm run dist
```

### ការតំឡើង Foundry Local

Foundry Local ត្រូវការសម្រាប់រត់គំរូ។ ទាញយកនិងដំឡើងពី repository ផ្លូវការ៖

**ការដំឡើង:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ដំឡើងដោយដៃ**: ទាញយកពី [releases page](https://github.com/microsoft/Foundry-Local/releases)

**ចាប់ផ្តើមរហ័ស:**
```bash
# បើកដំណើរការម៉ូដែលដំបូងរបស់អ្នក (ទាញយកដោយស្វ័យប្រវត្តិយើលតាមការត្រូវការ)
foundry model run phi-4-mini

# បញ្ជីម៉ូដែលដែលមាន
foundry model ls

# ពិនិត្យស្ថានភាពសេវា
foundry service status
```

**ចំណាំ**: Foundry Local ជ្រើសរើសម៉ូដែលល្អបំផុតសម្រាប់ឧបករណ៍របស់អ្នកស្វ័យប្រវត្តិ (GPU CUDA, Qualcomm NPU, ឬ CPU)។

## ដំណើរការអភិវឌ្ឍ

### ការអភិវឌ្ឍមាតិកា

Repository នេះមានមេរៀននៅក្នុង **មាតិកា Markdown** ជាគ្រប់គ្រាន់។ នៅពេលធ្វើបំលាស់បំរួល៖

1. កែសម្រួលឯកសារ `.md` នៅក្នុងថតមេរៀនសមរម្យ
2. តាមដានគំរូទ្រង់ទ្រាយដែលមានស្រាប់
3. ធ្វើឲ្យប្រាកដថាគំរូកូដត្រឹមត្រូវ និងបានតេស្ត
4. ផ្សំយកមាតិកាបកប្រែដែលអាចត្រូវបានអាប់ដេត (ឬអនុញ្ញាតឲ្យប្រព័ន្ធស្វ័យប្រវត្តិរៀបចំ)

### ការអភិវឌ្ឍកម្មវិធីគំរូ

សម្រាប់គំរូ Python Module08 (គំរូ 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

សម្រាប់គំរូ Python Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

សម្រាប់គំរូ Electron (គំរូ 08):
```bash
cd Module08/samples/08
npm run dev  # ការអភិវឌ្ឍន៍ជាមួយការផ្ទុកឡើងវិញរហ័ស
```

### ការតេស្តកម្មវិធីគំរូ

គំរូ Python មិនមានតេស្តស្វ័យប្រវត្តិទេ ប៉ុន្តែអាចតេស្តបានដោយរត់វា៖
```bash
# សាកល្បងមុខងារជជែកមូលដ្ឋាន
python samples/01/chat_quickstart.py "Hello"

# សាកល្បងជាមួយគំរូជាក់លាក់
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

គំរូ Electron មានវេដិកាតេស្ត៖
```bash
cd Module08/samples/08
npm test           # បញ្ជា​តេស្ត​ឯកតា
npm run test:e2e   # បញ្ជា​តេស្ត​ពី​ផុត​ផ្សេង​ទៅ​ផុត
npm run lint       # ពិនិត្យ​រចនា​កូដ
```

## ការណែនាំស្តីពីការតេស្ត

### ធ្វើតេស្តមាតិកា

Repository ប្រើការជំនួយបកប្រែស្វ័យប្រវត្តិ។ មិនត្រូវធ្វើតេស្តដោយដៃសម្រាប់ការបកប្រែទេ។

**ការធ្វើតេស្តដោយដៃសម្រាប់បំលាស់បំរួលមាតិកា:**
1. ពិនិត្យមើលការបង្ហាញ Markdown ដោយមើលបង្ហាញ`preview` ឯកសារ .md
2. ពិនិត្យតំណភ្ជាប់ទាំងអស់ តាមកន្លែងគោលដៅត្រឹមត្រូវ
3. តេស្តឯកសារកូដណាមួយដែលបានបញ្ចូលក្នុងឯកសារ
4. ពិនិត្យថារូបភាពផ្ទុកបានត្រឹមត្រូវ

### ការតេស្តកម្មវិធីគំរូ

**គំរូ Module08/samples/08 (កម្មវិធី Electron) មានការតេស្តគ្រប់គ្រាន់:**
```bash
cd Module08/samples/08

# ប្រតិបត្តិការប្រលងទាំងអស់
npm test

# ប្រតិបត្តិការប្រលងឯកតាតែប៉ុណ្ណោះ
npm test -- --testPathPattern=unit

# ប្រតិបត្តិការប្រលងបញ្ចូលគ្នា
npm run test:integration

# ប្រតិបត្តិការប្រលងចាប់ពីចំបងដល់ចុង
npm run test:e2e

# ពិនិត្យការគ្របដណ្តប់នៃការប្រលង
npm test -- --coverage
```

**គំរូ Python ត្រូវតែតេស្តដោយដៃ:**
```bash
# ឧទាហរណ៍ Module08
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# ឧទាហរណ៍សិក្ខាសាលា
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# ប្រើឧបករណ៍ផ្ទៀងផ្ទាត់សិក្ខាសាលា
cd Workshop/scripts
python validate_samples.py  # ផ្ទៀងផ្ទាត់វេយ្យាករណ៍ និងការនាំចូល
python test_samples.py      # រត់តេស្តផ្សែង
```

## ការណែនាំនៃរចនាសម្ព័ន្ធកូដ

### មាតិកា Markdown

- ប្រើជំពូកមានដំណាក់កាលនៅល្អ (# សម្រាប់ចំណងជើង, ## សម្រាប់ផ្នែកសំខាន់, ### សម្រាប់ផ្នែករង)
- បញ្ចូលគម្លាត កូដជាមួយភាសាកំណត់ `python`, `bash`, `javascript`
- តាមដានដំណើរការបច្ចុប្បន្នសម្រាប់តារាង, បញ្ជី, និងការតម្រង់
- រក្សាទុកបន្ទាត់អានបានងាយ (ប្រមាណ 80-100 តួអក្សរ ក្នុងមួយបន្ទាត់ ប៉ុន្តែមិនតឹងរឹង)
- ប្រើតំណភ្ជាប់ទាក់ទងសម្រាប់ឯកសារផ្ទៃក្នុង

### រចនាសម្ព័ន្ធកូដ Python

- តាម PEP 8
- ប្រើភាពចំរូងប្រភេទ (type hints) នៅកន្លែងត្រូវការ
- បញ្ចូល docstrings សម្រាប់មុខងារ និងថ្នាក់
- ប្រើឈ្មោះអថេរមានន័យច្បាស់
- រក្សាមុខងារឲ្យផ្តោត និងខ្លី

### រចនាសម្ព័ន្ធកូដ JavaScript/Node.js

```bash
# គំរូ Electron អនុវត្តតាមការកំណត់ ESLint
cd Module08/samples/08
npm run lint        # ពិនិត្យរកបញ្ហា​រចនាប័ទ្ម
npm run lint:fix    # ជួសជុលបញ្ហារចនាប័ទ្មដោយស្វ័យប្រវត្តិ
npm run format      # បំលែងទ្រង់ទ្រាយជាមួយ Prettier
```

**ប្រព័ន្ធសំខាន់:**
- ការកំណត់ ESLint មាននៅគំរូ 08
- Prettier សម្រាប់រៀបចំកូដ
- ប្រើវចនានុក្រម ES6+
- តាមដានគំរូដែលមានស្រាប់នៅក្នុងកូដ

## ការណែនាំស្តីពីការផ្ញើ Pull Request

### ដំណើរការរួមចំណែក

1. **Fork repository** និងបង្កើតសាខាថ្មីពី `main`
2. **ធ្វើការកែប្រែ** យកតាមរចនាបថកូដ
3. **តេស្តយ៉ាងល្អ** ប្រើការណែនាំក្នុងផ្នែកតេស្តខាងលើ
4. **Commit ជាមួយសារ​​ច្បាស់លាស់** តាមបែបបទ Conventional Commits
5. **Push ទៅ fork របស់អ្នក** ហើយបង្កើត pull request
6. **ឆ្លើយតបនឹងមតិយោបល់** ពីអ្នកគ្រប់គ្រងពេលពិនិត្យ

### ការផ្តល់ឈ្មោះសាខា

- `feature/<module>-<description>` - សម្រាប់មុខងារថ្មី ឬមាតិកា
- `fix/<module>-<description>` - សម្រាប់កែតម្រូវកំហុស
- `docs/<description>` - សម្រាប់កែលម្អឯកសារ
- `refactor/<description>` - សម្រាប់ផ្លាស់ប្តូរកូដ

### រូបមន្តសារ Commit

តាម [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ឧទាហរណ៍:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### ទ្រង់ទ្រាយចំណងជើង
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### ច្បាប់ក្រមសីលធម៌

អ្នករួមចំណែកទាំងអស់ត្រូវតែអនុវត្តតាម [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). សូមពិនិត្យមើល [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) មុនពេលរួមចំណែក។

### មុនដាក់ស្នើ

**សម្រាប់ការបំលាស់បំរួលមាតិកា:**
- មើលមុនឯកសារ Markdown ដែលបានកែប្រែ
- ពិនិត្យតំណភ្ជាប់ និងរូបភាព
- ជួសជុលកំហុសអក្ខរកម្ម និងវេយ្យាករណ៍

**សម្រាប់ការកែប្រែកូដគំរូ (Module08/samples/08):**
```bash
npm run lint
npm test
```

**សម្រាប់ការកែប្រែកូដ Python:**
- តេស្តថាគំរូរត់បានជោគជ័យ
- ពិនិត្យឲ្យប្រាកដថាការគ្រប់គ្រងកំហុសបានត្រឹមត្រូវ
- ត្រួតពិនិត្យឲ្យប្រាកដថាគួរត្រូវជាមួយ Foundry Local

### ដំណើរការពិនិត្យ

- ការផ្លាស់ប្ដូរមាតិកាសិក្សាត្រូវបានពិនិត្យសម្រាប់ភាពត្រឹមត្រូវ និងច្បាស់លាស់
- គំរូកូដត្រូវបានតេស្តសម្រាប់មុខងារ
- ការអាប់ដេតបកប្រែដោយស្វ័យប្រវត្តិកម្មវិធី GitHub Actions

## ប្រព័ន្ធបកប្រែ

**សំខាន់**៖ Repository នេះប្រើប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិកម្មវិធី GitHub Actions។

- បកប្រែរក្សាទុកក្នុងថត `/translations/` (ជាង ៥០ភាសា)
- ប្រើការងារ `co-op-translator.yml` ដើម្បីបកប្រែស្វ័យប្រវត្តិ
- **កុំកែប្រែផ្ទាល់គ្រប់ឯកសារបកប្រែ** ពួកវានឹងត្រូវបានលុបចោល
- ត្រូវកែតែឯកសារប្រែភាសាអង់គ្លេសនៅថតគេហដ្ឋាន និងថតម៉ូឌុល
- ការបកប្រែរកើតឡើងដោយស្វ័យប្រវត្តិពេល push ទៅសាខា `main`

## ការតភ្ជាប់ Foundry Local

គំរូ Module08 ភាគច្រើនត្រូវការកម្មវិធី Microsoft Foundry Local ដើម្បីជួយជំរុញ។

### ការដំឡើង និងតំឡើង

**តំឡើង Foundry Local:**
```bash
# វីនដូរ
winget install Microsoft.FoundryLocal

# ម៉ាេកអូស៍
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**តំឡើង Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### ចាប់ផ្តើម Foundry Local
```bash
# ចាប់ផ្តើមសេវា និងរត់ម៉ូដែល (ទាញយកដោយស្វ័យប្រវត្តិប្រសិនបើត្រូវការ)
foundry model run phi-3.5-mini

# ឬប្រើឈ្មោះដូចគ្នារបស់ម៉ូដែលសម្រាប់ការបង្កើតប្រសិទ្ធភាពរបស់ឧបករណ៍ដោយស្វ័យប្រវត្តិ
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# ពិនិត្យสถานភាពសេវា
foundry service status

# បញ្ជីម៉ូដែលដែលមានស្រាប់
foundry model ls
```

### ការប្រើប្រាស់ SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# ប្រើនាមតំណាងម៉ូដែលសម្រាប់ការរចនាផ្គាប់រឹងស្វ័យប្រវត្តិ
alias = "phi-4-mini"

# បង្កើតអ្នកគ្រប់គ្រង (ចាប់ផ្តើមសេវាកម្មស្វ័យប្រវត្តិ និងផ្ទុកម៉ូដែល)
manager = FoundryLocalManager(alias)

# កំណត់រចនាសម្ព័ន្ធអតិថិជន OpenAI សម្រាប់សេវាកម្ម Foundry ក្នុងតំបន់
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# ប្រើម៉ូដែល
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### បញ្ជាក់ការដំណើរការ Foundry Local
```bash
# ស្ថានភាពសេវាកម្ម និងចំណុចបញ្ចប់
foundry service status

# បញ្ជីម៉ូដែលដែលបានផ្ទុក (REST API)
curl http://localhost:<port>/v1/models

# កំណត់ចំណាំ: ព័រត្រូវបានបង្ហាញនៅពេលបើកដំណើរការ 'foundry service status'
```

### អថេរបរិស្ថិតសម្រាប់គំរូ

សំភារៈភាគច្រើនប្រើអថេរបរិស្ថិតខាងក្រោម:
```bash
# ការកំណត់ Foundry ទីន់់
# សម្គាល់៖ SDK (FoundryLocalManager) ស្វ័យប្រវត្តិរកឃើញចំណុចផុតកំណត់
set MODEL=phi-4-mini  # ឬ phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # មិនទាមទារសម្រាប់ការប្រើប្រាស់ក្នុងតំបន់

# ចំណុចផុតកំណត់ដោយដៃ (បើមិនប្រើ SDK)
# លេខផតផ្តល់តាមរយៈ 'foundry service status'
set BASE_URL=http://localhost:<port>

# សម្រាប់ Azure OpenAI fallback (ជាជម្រើស)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**ចំណាំ**: នៅពេលប្រើ `FoundryLocalManager`, SDK នឹងរៀបចំស្វ័យប្រវត្តិត្រូវការណ៍សេវាកម្ម និងបង្ហោះម៉ូដែល។ ឈ្មោះកាត់ម៉ូដែល (ដូចជា `phi-3.5-mini`) ជួយធានាថាម៉ូដែលល្អបំផុតត្រូវបានជ្រើសរើសសម្រាប់ឧបករណ៍របស់អ្នក។

## ការសាងសង់ និងការបញ្ជូន

### ការបញ្ជូនមាតិកា

Repository នេះគឺមានតែឯកសារព័ត៌មាន ហើយមិនចាំបាច់មានដំណើរការសាងសង់សម្រាប់មាតិកា៕

### ការសាងសង់កម្មវិធីគំរូ

**កម្មវិធី Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# រចនាសម្ព័ន្ធអភិវឌ្ឍន៍
npm run dev

# រចនាសម្ព័ន្ធផលិតកម្ម
npm run build

# បង្កើតកម្មវិធីដំឡើង Windows
npm run dist

# បង្កើតកម្មវិធីអាចចល័តបាន
npm run pack
```

**គំរូ Python:**
គ្មានដំណើរការសាងសង់ - គំរូរត្រូវបានរត់ដោយផ្ទាល់ជាមួយ Python interpreter។

## បញ្ហាធម្មតា និងវិធីដោះស្រាយ

> **គន្លឹះ**: ពិនិត្យ [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) សម្រាប់បញ្ហាទូទៅ និងដំណោះស្រាយ។

### បញ្ហាសំខាន់ (បិទខ្សែ)

#### Foundry Local មិនដំណើរការ
**បញ្ហា:** គំរូបរាជ័យដោយកំហុសភ្ជាប់

**ដំណោះស្រាយ:**
```bash
# ពិនិត្យមើលថា សេវាកម្មកំពុងដំណើរការឬទេ
foundry service status

# ចាប់ផ្ដើមសេវាកម្មជាមួយម៉ូដែលមួយ
foundry model run phi-4-mini

# ឬចាប់ផ្ដើមសេវាកម្មដោយច្បាស់លាស់
foundry service start

# រាយបញ្ជីម៉ូដែលដែលបានបញ្ចូល
foundry model ls

# ធ្វើការផ្ទៀងផ្ទាត់តាមរយៈ REST API (ព្រិលត្រូវបានបង្ហាញនៅក្នុង 'foundry service status')
curl http://localhost:<port>/v1/models
```

### បញ្ហាទូទៅ (មធ្យម)

#### បញ្ហាពី Python Virtual Environment
**បញ្ហា:** កំហុសនាំចូលម៉ូឌុល

**ដំណោះស្រាយ:**
```bash
# ប្រាកដថាបរិយាកាសវីរុជួបបានបើកដំណើរការ
# វីនដូស
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# ធ្វើបច្ចុប្បន្នភាពការពឹងផ្អែកឡើងវិញ
pip install -r requirements.txt
```

#### បញ្ហាសាងសង់ Electron
**បញ្ហា:** npm install ឬ build បរាជ័យ

**ដំណោះស្រាយ:**
```bash
cd Module08/samples/08
# ដំឡើងស្អាត
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### បញ្ហាដំណើរការអភិវឌ្ឍ (តិចតួច)

#### បញ្ហាសង្គ្រាមការបកប្រែ
**បញ្ហា:** Pull request បកប្រែជួបបញ្ហាជំហរប់ពាក់ព័ន្ធ

**ដំណោះស្រាយ:**
- កែទាំងអស់នៅក្នុងមាតិកាភាសាអង់គ្លេស
- អនុញ្ញាតឲ្យប្រព័ន្ធបកប្រែស្វ័យប្រវត្តិត្រូវតែដោះស្រាយ
- ប្រសិនបើមានបញ្ហា សូម merges `main` តាមសាខារបស់អ្នកបន្ទាប់ពីបញ្ចូលការបកប្រែ

#### បញ្ហាទាញយកម៉ូដែល
**បញ្ហា:** Foundry Local បរាជ័យក្នុងការទាញយកម៉ូដែល

**ដំណោះស្រាយ:**
```bash
# សូមពិនិត្យការតភ្ជាប់អ៊ីនធឺណិត
# ដកចេញផ្ទុកម៉ូឌែល ហើយព្យាយាមម្តងទៀត
foundry model remove <model-alias>
foundry model run <model-alias>

# ពិនិត្យកន្លែងទំនេរក្នុងឌីស្ក์ (ម៉ូឌែល​អាចមានទំហំនៅចន្លោះ 2-16GB)
# ដាក់ពិនិត្យការកំណត់Firewall ដើម្បីអនុញ្ញាតឲ្យទាញយក.Documents_Userok now translate to vietnamese (vi)
```

## ធនធានបន្ថែម

### ផ្លូវការសិក្សា
- **ផ្លូវអ្នកចាប់ផ្តើម:** Module01-02 (៧-៩ ម៉ោង)
- **ផ្លូវកម្រិតមធ្យម:** Module03-04 (៩-១១ ម៉ោង)
- **ផ្លូវកម្រិតខ្ពស់:** Module05-07 (១២-១៥ ម៉ោង)
- **ផ្លូវអ្នកជំនាញ:** Module08 (៨-១០ ម៉ោង)
- **សិក្ខាសាលាដោយដៃ:** សម្ភារៈវគ្គសិក្សា (៦-៨ ម៉ោង)

### មាតិកាមេរៀនសំខាន់
- **Module01:** មូលដ្ឋាន EdgeAI និងករណីរៀនជាក់ស្តែង
- **Module02:** គ្រួសារម៉ូដែលភាសាទឹកចិត្ត (SLM) និងរចនា
- **Module03:** យុទ្ធសាស្ត្របំពេញនៅលើដីឡូក និងមេឃ
- **Module04:** ការបញ្ជូលម៉ូដែលជាមួយវេទិកាច្រើន (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - ប្រតិបត្តិការផលិតកម្ម
- **Module06:** បំណង AI និងហៅមុខងារ
- **Module07:** ការអនុវត្តលើវេទិកាពិសេស
- **Module08:** សំណុំឧបករណ៍ Foundry Local ជាមួយគំរូទាំង 10

### ភាពផ្អែកខាងក្រៅ
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - ម៉ូដែល AI ដំណើរការផ្ទាល់ជាមួយ OpenAI-compatible API
  - [ឯកសារព័ត៌មាន](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - វេទិកាបញ្ជូលម៉ូដែល
- [Microsoft Olive](https://microsoft.github.io/Olive/) - សំណុំឧបករណ៍បញ្ជូលម៉ូដែល
- [OpenVINO](https://docs.openvino.ai/) - វេទិកាបញ្ជូលដែល Intel ផ្តល់ជូន

## កំណត់សម្គាល់ជាក់លាក់កម្មវិធី

### កម្មវិធីគំរូ Module08

Repository មានកម្មវិធីគំរូ 10 ផ្តល់ជូនដោយពេញលេញ៖

1. **01-REST Chat Quickstart** - ការបញ្ចូល OpenAI SDK មូលដ្ឋាន
2. **02-OpenAI SDK Integration** - លក្ខណៈប្រើប្រាស់ SDK ជាដំណាក់កាលខ្ពស់
3. **03-Model Discovery & Benchmarking** - ឧបករណ៍ប្រៀបធៀបម៉ូដែល
4. **04-Chainlit RAG Application** - ការបង្កើតតាមការទាញយកបន្ថែម
5. **05-Multi-Agent Orchestration** - ការត្រួតត្រាបុគ្គលអាជ្ញា
6. **06-Models-as-Tools Router** - ការបញ្ជូនម៉ូដែលឆ្លាតវៃ
7. **07-Direct API Client** - ការបញ្ចូល API ផ្ទាល់
8. **08-Windows 11 Chat App** - កម្មវិធីតុ Electron ដំណើរការលើ Windows
9. **09-Advanced Multi-Agent System** - ប្រព័ន្ធបុគ្គលជាច្រើនដំណើរការ
10. **10-Foundry Tools Framework** - ការបញ្ចូល LangChain/Semantic Kernel

### កម្មវិធីគំរូ Workshop


កម្មវិធីហ្វឹកហ្វឺនរួមមានវគ្គសិក្សាចំនួន៦ ដែលមានការអនុវត្តជាក់ស្តែង៖

1. **វគ្គសិក្សា ០១** - ការចាប់ផ្តើមជជែកជាមួយការរួមបញ្ចូល Foundry Local
2. **វគ្គសិក្សា ០២** - ខ្សែបណ្តាញ RAG និងការវាយតម្លៃជាមួយ RAGAS
3. **វគ្គសិក្សា ០៣** - ការប្រៀបធៀបទ្រព្យសម្បត្តិ open-source
4. **វគ្គសិក្សា ០៤** - ការប្រៀបធៀបទ្រព្យសម្បត្តិ និងការជ្រើសរើស
5. **វគ្គសិក្សា ០៥** - ប្រព័ន្ធច្រកចេញអ្នកតំណាងច្រើន
6. **វគ្គសិក្សា ០៦** - ការបញ្ជូនម៉ូដែល និងការគ្រប់គ្រងខ្សែបណ្តាញ

គំរូនីមួយៗបង្ហាញពីផ្នែកផ្សេងៗនៃការអភិវឌ្ឍ Edge AI ជាមួយ Foundry Local។

### ការពិចារណាពីការអនុវត្តន៍

- SLMs មានការបង្កើតសម្រាប់ការដំឡើងនៅតំបន់ edge (RAM ២-១៦GB)
- ការទាយថ្នាក់ជាលokal ផ្តល់ម៉ោងឆ្លើយតប ៥០-៥០០ms
- វិធីសាស្ត្របំលែងទំហំទទួលបានការចុះតម្លៃ ៧៥% ដោយរក្សាទុកកម្រិតប្រសិទ្ធភាព ៨៥%
- មានសមត្ថភាពជជែកពេលវេលាពិតជាមួយម៉ូដែលក្នុងស្រុក

### សុវត្ថិភាព និងភាពឯកជន

- ការបញ្ចូលទិន្នន័យទាំងអស់កើតមានក្នុងស្រុក - គ្មានទិន្នន័យផ្ញើទៅពពក
- សមស្របសម្រាប់កម្មវិធីដែលមានសុវត្ថិភាពខ្ពស់ (សុខាភិបាល, ហិរញ្ញវត្ថុ)
- បំពេញតម្រូវការកម្មសិទ្ធិទិន្នន័យ
- Foundry Local ដំណើរការជាស្ថានអង្គភាពក្នុងផ្នែកក្នុងស្រុក

## លទ្ធភាពទទួលជំនួយ

### ឯកសារ

- **README សំខាន់**: [README.md](README.md) - សង្ខេបរ៉ែប៉ូស៊ីទូរី និងផ្លូវកំណត់ការសិក្សា
- **មេរៀនសិក្សា**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - ធនធានសិក្សា និងពេលវេលា
- **ការគាំទ្រ**: [SUPPORT.md](SUPPORT.md) - របៀបទទួលបានជំនួយ
- **សុវត្ថិភាព**: [SECURITY.md](SECURITY.md) - របាយការណ៍បញ្ហាសុវត្ថិភាព

### គាំទ្រសហគមន៍

- **បញ្ហា GitHub**: [រាយការណ៍កំហុស ឬសំណូមពរពិសេស](https://github.com/microsoft/edgeai-for-beginners/issues)
- **ការពិភាក្សា GitHub**: [សួរបញ្ហា និងចែករំលែកគំនិត](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **បញ្ហា Foundry Local**: [បញ្ហាបច្ចេកទេសជាមួយ Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### ព័ត៌មានទំនាក់ទំនង

- **អ្នកថែទាំ**: មើល [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **បញ្ហាសុវត្ថិភាព**: តាមដានការបញ្ចេញព័ត៌មានដោយទំនួលខុសត្រូវក្នុង [SECURITY.md](SECURITY.md)
- **ការគាំទ្រពី Microsoft**: សម្រាប់ការគាំទ្រអាជីវកម្ម សូមទំនាក់ទំនងសេវាអតិថិជន Microsoft

### ធនធានបន្ថែម

- **Microsoft Learn**: [ផ្លូវកំណត់សិក្សា AI និងការសិក្សា ម៉ាស៊ីនរៀន](https://learn.microsoft.com/training/browse/?products=ai-services)
- **ឯកសារ Foundry Local**: [ឯកសារផ្លូវការជាផ្លូវការ](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **គំរូសហគមន៍**: ពិនិត្យមើល [ការពិភាក្សា GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) សម្រាប់ការបរិច្ចាកពីសហគមន៍

---

**នេះគឺជារូបិយភាពសិក្សាដើម្បីបង្រៀនអំពីការអភិវឌ្ឍ Edge AI។ ទឹកប្រាក់ចម្បង​គឺធ្វើឲ្យខ្លួនអប់រំកាន់តែល្អ និងបន្ថែម/បំលែងកម្មវិធីគំរូដែលបង្ហាញគំនិត Edge AI។**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំផ្តល់ភាពត្រឹមត្រូវ ក៏សូមយល់ឱ្យបានថាការបកប្រែដោយស្វ័យប្រវត្តិ​អាចមានកំហុស ឬ ខុសប្រក្រតីខ្លះៗ។ ឯកសារដើមក្នុងភាសាដើមត្រូវបានគេចាត់ទុកថាជាមួយប្រភពដែលមានសិទ្ធិ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬ ការបកអក្សរខុសៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->