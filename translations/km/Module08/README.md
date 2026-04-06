# Module 08: ខ្លឹមសារអនុវត្តជាមួយ Microsoft Foundry Local - ប្រអប់ឧបករណ៍សម្រាប់អ្នកអភិវឌ្ឍពេញលេញ

## ទិដ្ឋភាពទូទៅ

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) ជាបច្ចេកវិទ្យា​ជំនាន់ក្រោយសម្រាប់ការអភិវឌ្ឍ AI នៅឆាកផ្ទាល់ឧបករណ៍ ដែលផ្តល់ឧបករណ៍ដ៏ដំណើរការច្រើនសម្រាប់អ្នកអភិវឌ្ឍ ដើម្បីបង្កើត បញ្ចូន និងវិសាលភាពកម្មវិធី AI ក្នុងកន្លែងក្រៅខ្សែភ្លើង ខណៈពេលនៃការរួមបញ្ចូលដោយឥតខ្សែជាមួយ Azure AI Foundry។ ម៉ូឌុលនេះគ្របដណ្តប់យ៉ាងទូលំទូលាយពីការដំឡើងរហូតដល់ការអភិវឌ្ឍភ្នែកម៉ាស៊ីនក аген្ (advanced agent development) ។

**បច្ចេកវិទ្យាសំខាន់៖**
- Microsoft Foundry Local CLI និង SDK
- ការរួមបញ្ចូល Azure AI Foundry
- ការសន្សំពិន្ទុម៉ូដែល និងប្រើប្រាស់ម៉ូដែលនៅលើឧបករណ៍
- ការផ្ទុកបណ្តុះម៉ូដែលក្នុងឡុកាល់ និងការបញ្ច.optimize
- វិទ្យាស្ថានបញ្ជាស្ថិតិដោយឧត្តមភាពជាអេជន

## គោលបំណងការសិក្សា

ដោយបញ្ចប់ម៉ូឌុលនេះ អ្នកនឹង:

- **ជំនាញនៅលើ Foundry Local**៖ ដំឡើង កំណត់ និងបង្កើនប្រសិទ្ធភាពសម្រាប់ការអភិវឌ្ឍលើ Windows 11
- **ចេញផ្សាយម៉ូដែលជាច្រើន**៖ រត់ម៉ូដែល phi, qwen, deepseek, និង GPT នៅលើកុំព្យូទ័រផ្ទាល់ជាមួយពាក្យបញ្ជារ CLI
- **សាងសង់ដំណោះស្រាយផលិតកម្ម**៖ បង្កើតកម្មវិធី AI ជាមួយ prompt engineering លើកម្លាំង និងការរួមបញ្ចូលទិន្នន័យ
- **អាស្រ័យលើអេកូស៊ីស្ទឹមបើកចំហ**៖ រួមបញ្ចូលម៉ូដែល Hugging Face និងការគ្រប់គ្រងពីសហគមន៍
- **អភិវឌ្ឍអេជន AI**៖ សង់អេជនឆ្លាតវៃដោយមាន grounding និងសមត្ថភាពអធិប្បាយ
- **អនុវត្តគំរូសម្រាប់សហគ្រាស**៖ បង្កើតដំណោះស្រាយម៉ូឌ្យុល ដែលអាចវិសាល និងតម្រូវសម្រាប់ការផ្ដល់ចេញក្នុងផលិតកម្ម

## រចនាសម្ព័ន្ធសម័យ

### [1: Getting Started with Foundry Local](./01.FoundryLocalSetup.md)
**ផ្តោត**: ការដំឡើង ការកំណត់ CLI ការចេញផ្សាយម៉ូដែល និងការបង្កើនប្រសិទ្ធភាពឧបករណ៍

**ប្រធានបទសំខាន់**: ការដំឡើងពេញលេញ • ពាក្យបញ្ជារ CLI • ការសន្សំបោះម៉ូដែល • ការបង្កើនល្បឿនឧបករណ៍ • ការចេញផ្សាយម៉ូដែលច្រើន

**ឧទាហរណ៍**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**រយៈពេល**: 2-3 ម៉ោង | **កម្រិត**: ដំបូង

---

### [2: Build AI Solutions with Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**ផ្តោត**: prompt engineering ជាន់ខ្ពស់ ការរួមបញ្ចូលទិន្នន័យ និងការតភ្ជាប់ទៅ cloud

**ប្រធានបទសំខាន់**: Prompt engineering • ការរួមបញ្ចូលទិន្នន័យ • វិធីសាស្ត្រ Azure • ការបង្កើនសមត្ថភាព • ការត្រួតពិនិត្យ

**ឧទាហរណ៍**: [Chainlit RAG Application](./samples/04/README.md)

**រយៈពេល**: 2-3 ម៉ោង | **កម្រិត**: មធ្យម

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**ផ្តោត**: ការរួមបញ្ចូល Hugging Face អុីការយន BYOM និងម៉ូដែលសហគមន៍

**ប្រធានបទសំខាន់**: ការរួមបញ្ចូល HuggingFace • ដាក់ម៉ូដែលរបស់អ្នក (Bring-your-own-model) • គំនិត Model Mondays • ការ​ចូលរួមសហគមន៍ • ការជ្រើសរើសម៉ូដែល

**ឧទាហរណ៍**: [Multi-Agent Orchestration](./samples/05/README.md)

**រយៈពេល**: 2-3 ម៉ោង | **កម្រិត**: មធ្យម

---

### [4: Explore Cutting-Edge Models](./04.CuttingEdgeModels.md)
**ផ្តោត**: LLMs ទល់នឹង SLMs ការអនុវត្ត EdgeAI និងដេម៉ូជាន់ខ្ពស់

**ប្រធានបទសំខាន់**: ការប្រៀបធៀបម៉ូដែល • ការប៉ាន់ប្រមាណ Edge ទល់នឹង cloud • Phi + ONNX Runtime • Chainlit RAG app • ការបង្កើនល្បឿន WebGPU

**ឧទាហរណ៍**: [Models-as-Tools Router](./samples/06/README.md)

**រយៈពេល**: 3-4 ម៉ោង | **កម្រិត**: ជំនាញខ្ពស់

---

### [5: Build AI-Powered Agents Fast](./05.AIPoweredAgents.md)
**ផ្តោត**: ស្ថាបត្យកម្មអេជន prompt ប្រព័ន្ធ grounding និង orchestration

**ប្រធានបទសំខាន់**: លំនាំរចនាអេជន • Prompt engineering ប្រព័ន្ធ • បច្ចេកទេស grounding • ប្រព័ន្ធអេជនច្រើន • ការផ្ទៀងផ្ទាត់ផលិតកម្ម

**ឧទាហរណ៍**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**រយៈពេល**: 3-4 ម៉ោង | **កម្រិត**: ជំនាញខ្ពស់

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**ផ្តោត**: ដំណោះស្រាយ AI ម៉ូឌុល ការវាស់វិសាលសហគ្រាស និងលំនាំផលិតកម្ម

**ប្រធានបទសំខាន់**: ម៉ូដែលជាឧបករណ៍ • ការចេញផ្សាយលើឧបករណ៍ • ការរួមបញ្ចូល SDK/API • ស្ថាបត្យកម្មសហគ្រាស •យុទ្ធសាស្ត្រវិសាលកាម

**ឧទាហរណ៍**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**រយៈពេល**: 3-4 ម៉ោង | **កម្រិត**: ជំនាញឯកទេស

---

### [7: Direct API Integration Patterns](./samples/07/README.md)
**ផ្តោត**: ការរួមបញ្ចូល REST API ដោយគ្មានអាស្រ័យភាពលើ SDK សម្រាប់ការគ្រប់គ្រងខ្ពស់បំផុត

**ប្រធានបទសំខាន់**: ការអនុវត្ត HTTP client • អAUTH​ផ្ទាល់ខ្លួន • ការត្រួតពិនិត្យសុខភាពម៉ូដែល • ចម្លើយបង្ហាញជាស្ទ្រីម • ការគ្រប់គ្រងកំហុសក្នុងផលិតកម្ម

**ឧទាហរណ៍**: [Direct API Client](./samples/07/README.md)

**រយៈពេល**: 2-3 ម៉ោង | **កម្រិត**: មធ្យម

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**ផ្តោត**: ការសាងសង់កម្មវិធី chat ជាកម្មវិធីដើមនៅលើ Windows 11 ដោយរួមបញ្ចូល Foundry Local

**ប្រធានបទសំខាន់**: ការអភិវឌ្ឍ Electron • Fluent Design System • ការរួមបញ្ចូលដើម Windows • ស្ទ្រីមពេលពិត • រចនាចំណុចចូលជជែក

**ឧទាហរណ៍**: [Windows 11 Chat Application](./samples/08/README.md)

**រយៈពេល**: 3-4 ម៉ោង | **កម្រិត**: ជំនាញខ្ពស់

---

### [9: Advanced Multi-Agent Orchestration](./samples/09/README.md)
**ផ្តោត**: ការសម្របសម្រួលអេជនជាន់ខ្ពស់ ការចាត់ចែងភារកិច្ចជាពិសេស និងដំណើរការសហការណ៍ AI

**ប្រធានបទសំខាន់**: ការសម្របសម្រួលអេជនឆ្លាតវៃ • លំនាំ function calling • ការទំនាក់ទំនងគ្នារវាងអេជន • orchestration នៃ workflow • គ្រប់គ្រងគុណភាព

**ឧទាហរណ៍**: [Advanced Multi-Agent System](./samples/09/README.md)

**រយៈពេល**: 4-5 ម៉ោង | **កម្រិត**: ជំនាញឯកទេស

---

### [10: Foundry Local as Tools Framework](./samples/10/README.md)
**ផ្តោត**: វិធីសាស្ត្រយកឧបករណ៍ជាមុនសម្រាប់រួមបញ្ចូល Foundry Local ទៅក្នុងកម្មវិធី និងផ្នែកទឹកជ្រៅដែលមានស្រាប់

**ប្រធានបទសំខាន់**: ការរួមបញ្ចូល LangChain • Semantic Kernel functions • ស៊ុម REST API • ឧបករណ៍ CLI • ការរួមបញ្ចូល Jupyter • លំនាំចេញក្នុងផលិតកម្ម

**ឧទាហរណ៍**: [Foundry Tools Framework](./samples/10/README.md)

**រយៈពេល**: 4-5 ម៉ោង | **កម្រិត**: ជំនាញឯកទេស

## លក្ខខណ្ឌមុន

### ការទាមទាររបស់ប្រព័ន្ធ
- **ប្រព័ន្ធប្រតិបត្តិការ**: Windows 11 (22H2 or later)
- **ម៉ាញម៉ខ្ញល់**: 16GB RAM (32GB ត្រូវបានផ្ដល់អនុសាសន៍​សម្រាប់ម៉ូដែលធំនៅ)
- **ចង្ក្រានដាក់ទិន្នន័យ**: ទំហំទទេ 50GB សម្រាប់ការសន្សុំនៅលើម៉ូដែល
- **ឧបករណ៍ហា HARDWARE**: ឧបករណ៍ដែលគាំទារ NPU ត្រូវបានផ្ដល់អនុសាសន៍ (Copilot+ PC), GPU ជាជម្រើស
- **បណ្ដាញ**: អ៊ីនធឺណែតល្បឿនលឿនសម្រាប់ការទាញយកម៉ូដែលដំបូង

### បរិយាកាសអភិវឌ្ឍន៍
- Visual Studio Code មានផ្នែកបន្ថែម AI Toolkit
- Python 3.10+ និង pip
- Git សម្រាប់ការគ្រប់គ្រងកំណែ
- PowerShell ឬ Command Prompt
- Azure CLI (ជាជម្រើសសម្រាប់ការរួមបញ្ចូលទៅ cloud)

### ចំណេះដឹងត្រូវមាន
- ការយល់ដឹងបឋមពីទ្រឹស្ដី AI/ML
- របៀបប្រើបន្ទាត់ពាក្យបញ្ជារ (command line) មូលដ្ឋាន
- មូលដ្ឋានកម្មវិធីភាសា Python
- គំនិត REST API
- ចំណេះដឹងមូលដ្ឋានពី prompting និងការបញ្ជាក់ម៉ូដែល

## កាលវិភាគម៉ូឌុល

**ពេលវេលាប៉ាន់ប្រមាណសរុប**: 30-38 ម៉ោង

| Session | Focus Area | Samples | Time | Complexity |
|---------|------------|---------|------|------------|
|  1 | Setup & Basics | 01, 02, 03 | 2-3 hours | Beginner |
|  2 | AI Solutions | 04 | 2-3 hours | Intermediate |
|  3 | Open Source | 05 | 2-3 hours | Intermediate |
|  4 | Advanced Models | 06 | 3-4 hours | Advanced |
|  5 | AI Agents | 05, 09 | 3-4 hours | Advanced |
|  6 | Enterprise Tools | 06, 10 | 3-4 hours | Expert |
|  7 | Direct API Integration | 07 | 2-3 hours | Intermediate |
|  8 | Windows 11 Chat App | 08 | 3-4 hours | Advanced |
|  9 | Advanced Multi-Agent | 09 | 4-5 hours | Expert |
| 10 | Tools Framework | 10 | 4-5 hours | Expert |

## ធនធានសំខាន់

**ឯកសារផ្លូវការ:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - រកូដដើម និងឧទាហរណ៍ផ្លូវការ
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - មគ្គុទេសក៍ដំឡើង និងការប្រើប្រាស់ពេញលេញ
- [Model Mondays Series](https://aka.ms/model-mondays) - ការបង្ហាញម៉ូដែលប្រចាំសប្តាហ៍ និងមេរៀន

**សហគមន៍ និង ការគាំទ្រ:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - សំណួរ Q&A របស់សហគមន៍ និងសំណើលក្ខណៈពិសេស
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - ព័ត៌មានថ្មីៗ និងល្អបំផុតក្នុងអនុវត្តន៍

## លទ្ធផលការសិក្សា

បន្ទាប់ពីបញ្ចប់ម៉ូឌុលនេះ អ្នកនឹងមានសមត្ថភាពក្នុង:

### ជំនាញបច្ចេកទេស
- **ចេញផ្សាយ និងគ្រប់គ្រង**: ដំឡើង Foundry Local ក្នុងបរិយាកាសអភិវឌ្ឍន៍ និងផលិតកម្ម
- **រួមបញ្ចូលម៉ូដែល**: ធ្វើការជាមួយគ្រួសារម៉ូដែលផ្សេងៗពី Microsoft, Hugging Face, និងប្រភពសហគមន៍ដោយរលូន
- **សាងសង់កម្មវិធី**: បង្កើតកម្មវិធី AI ស្រួលប្រើនៅក្នុងផលិតកម្ម ជាមួយមុខងារជាន់ខ្ពស់ និងការបង្កើនប្រសិទ្ធភាព
- **អភិវឌ្ឍអេជន**: អនុវត្តអេជន AI ក្មេងខ្ពស់ជាមួយ grounding, reasoning, និងការរួមបញ្ចូលឧបករណ៍

### ការយល់ដឹងយុទ្ធសាស្ត្រ
- **ជ្រើសរើសស្ថាបត្យកម្ម**: ធ្វើជម្រើសដោយមានព័ត៌មានច្រកចេញចូល រវាងការចេញផ្សាយក្នុងឡុកាល់ និង cloud
- **បង្កើនប្រសិទ្ធភាព**: បង្កើនសមត្ថភាពនៃការបញ្ចេញទិន្នន័យសម្រាប់ឧបករណ៍ខុសៗគ្នា
- **វិសាលភាពសហគ្រាស**: ស្ថាបនាកម្មវិធីអាចវិសាលពីគំរូក្នុងឡុកាល់ទៅការចេញផ្សាយក្នុងសហគ្រាស
- **ភាពឯកជន និងសុវត្ថិភាព**: អនុវត្តដំណោះស្រាយ AI រក្សាឯកជនភាពដោយប្រើការបញ្ចេញក្នុងឡុកាល់

### សមត្ថភាពច្នៃប្រឌិត
- **Rapid Prototyping**: សាងសង់ និងសាកល្បងគំនិតកម្មវិធី AI បានយ៉ាងលឿនទាំង 10 គំរូ
- **ការរួមបញ្ចូលសហគមន៍**: ប្រើម៉ូដែលបើកចំហរ និងចូលរួមចែកចាយទៅអេកូស៊ីស្ទឹម
- **លំនាំជាន់ខ្ពស់**: អនុវត្តលំនាំ AI ជាច្រើនដូចជា RAG, អេជន និងការរួមបញ្ចូលឧបករណ៍
- **ជំនាញនៅលើស៊ុម**: សមត្ថភាពជំនាញខ្ពស់ក្នុងការរួមបញ្ចូលជាមួយ LangChain, Semantic Kernel, Chainlit, និង Electron
- **ចេញផ្សាយក្នុងផលិតកម្ម**: ចេញផ្សាយដំណោះស្រាយ AI ដែលអាចវិសាលពីគំរូក្នុងឡុកាល់ទៅប្រព័ន្ធសហគ្រាស
- **អភិវឌ្ឍន៍សម្រាប់អនាគត**: សាងសង់កម្មវិធីដែលរួមបញ្ចូលនូវបច្ចេកវិទ្យា AI និងលំនាំដែលកំពុងមានការកើនឡើង

## ការចាប់ផ្តើម

1. **កំណត់បរិយាកាស**: ដាក់ទុក Windows 11 ជាមួយឧបករណ៍ណែនាំ (មើល លក្ខខណ្ឌមុន)
2. **ដំឡើង Foundry Local**: ធ្វើតាម សម័យ 1 សម្រាប់ការដំឡើង និងការកំណត់ពេញលេញ
3. **រត់គំរូ 01**: ចាប់ផ្ដើមជាមួយការរួមបញ្ចូល REST API ដើម្បីផ្ទៀងផ្ទាត់ការតំឡើង
4. **ចាប់ផ្តើមតាមគំរូ**: បញ្ចប់គំរូ 01-10 សម្រាប់ជំនាញពេញលេញ

## មាត្រដ្ឋានជោគជ័យ

តាមដានជំហានរបស់អ្នកតាមគំរូទាំង 10 ពេញលេញ៖

### កម្រិតមូលដ្ឋាន (គំរូ 01-03)
- [ ] ដំឡើង និងកំណត់ Foundry Local បានដោយជោគជ័យ
- [ ] បញ្ចប់ការរួមបញ្ចូល REST API (គំរូ 01)
- [ ] អនុវត្តភាពសមន្ធ OpenAI SDK (គំរូ 02)
- [ ] បំពេញការរកឃើញម៉ូដែល និងការវាស់សមត្ថភាព (គំរូ 03)

### កម្រិតកម្មវិធី (គំរូ 04-06)
- [ ] ចេញផ្សាយ និងរត់យ៉ាងហោចណាស់ 4 គ្រួសារម៉ូដែលផ្សេងគ្នា
- [ ] សាងសង់កម្មវិធីជជែក RAG ដែលអាចប្រើបាន (គំរូ 04)
- [ ] បង្កើតប្រព័ន្ធសម្របសម្រួលអេជនច្រើន (គំរូ 05)
- [ ] អនុវត្តការចែកចាយម៉ូដែលឆ្លាត (គំរូ 06)

### កម្រិតការរួមបញ្ចូលជាន់ខ្ពស់ (គំរូ 07-10)
- [ ] សង់ API client លក្ខណៈផលិតកម្ម (គំរូ 07)
- [ ] អភិវឌ្ឍកម្មវិធី chat ដើមនៅលើ Windows 11 (គំរូ 08)
- [ ] អនុវត្តប្រព័ន្ធអេជនច្រើនជាន់ខ្ពស់ (គំរូ 09)
- [ ] បង្កើតស៊ុមឧបករណ៍ពេញលេញ (គំរូ 10)

### សូចនាករជំនាញ
- [ ] រត់គំរូទាំង 10 ដោយគ្មានកំហុស
- [ ] តម្រូវយ៉ាងតិច 3 គំរូសម្រាប់ករណីប្រើប្រាស់ជាក់លាក់
- [ ] ចេញផ្សាយ 2+ គំរូក្នុងបរិយាកាសស្រដៀងផលិតកម្ម
- [ ] ធ្វើការរួមចំណែកក្នុងការកែលម្អ ឬផ្ដល់ការពង្រីកទៅកូដគំរូ
- [ ] រួមបញ្ចូលលំនាំ Foundry Local ទៅក្នុងគម្រោងផ្ទាល់ខ្លួន/វិជ្ជាជីវៈ

## មគ្គុទេសក៍ចាប់ផ្តើមរហ័ស - គំរូទាំង 10

### ការកំណត់បរិយាកាស (ត្រូវការ សម្រាប់គំរូទាំងអស់)

```powershell
# 1. ទាញ (clone) ហើយចូលទៅកាន់ Module08
cd Module08

# 2. បង្កើត virtual environment សម្រាប់ Python
py -m venv .venv
.\.venv\Scripts\activate

# 3. ដំឡើងអាស្រ័យភាពមូលដ្ឋាន
pip install -r requirements.txt

# 4. ដំឡើង Foundry Local (ប្រសិនបើមិនទាន់បានដំឡើង)
winget install Microsoft.FoundryLocal

# 5. ផ្ទៀងផ្ទាត់ការដំឡើង Foundry Local
foundry --version
foundry model list
```

### គំរូមូលដ្ឋាន (01-06)

**គំរូ 01: REST Chat Quickstart**
```powershell
# ចាប់ផ្តើមសេវា Foundry Local
foundry model run phi-4-mini

# រត់ឧទាហរណ៍ការឆាត REST
python samples/01/chat_quickstart.py
```

**គំរូ 02: OpenAI SDK Integration**
```powershell
# ធានាថា ម៉ូឌែលកំពុងដំណើរការ
foundry status

# រត់ ដេម៉ូ SDK
python samples/02/sdk_quickstart.py
```

**គំរូ 03: Model Discovery & Benchmarking**
```powershell
# រត់ការធ្វើតេស្តម៉ូដែលទាំងមូល
samples/03/list_and_bench.cmd

# ឬរត់ជា​សមាសធាតុដោយឡែក
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**គំរូ 04: Chainlit RAG Application**
```powershell
# ដំឡើងឧបករណ៍អាស្រ័យរបស់ Chainlit
pip install chainlit langchain chromadb

# ចាប់ផ្តើមកម្មវិធីជជែក RAG
chainlit run samples/04/app.py -w
# បើកកម្មវិធីរុករកនៅ http://localhost:8000
```

**គំរូ 05: Multi-Agent Orchestration**
```powershell
# រត់ការបង្ហាញអ្នកសម្របសម្រួលភ្នាក់ងារ
python -m samples.05.agents.coordinator

# រត់ឧទាហរណ៍នៃភ្នាក់ងារជាក់លាក់
python samples/05/examples/specialists_demo.py
```

**គំរូ 06: Models-as-Tools Router**
```powershell
# កំណត់រចនាសម្ព័ន្ធបរិយាកាស
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# រត់រ៉ូទ័រឆ្លាត
python samples/06/router.py "Analyze this Python code for performance issues"
```

### គំរូការរួមបញ្ចូលជាន់ខ្ពស់ (07-10)

**គំរូ 07: Direct API Client**
```powershell
# ទៅកាន់ថតឧទាហរណ៍
cd samples/07

# ដំឡើងការពឹងផ្អែកបន្ថែម
pip install -r requirements.txt

# រត់ឧទាហរណ៍ API មូលដ្ឋាន
python examples/basic_usage.py

# សាកល្បងការផ្សាយចម្លើយជាបន្ត
python examples/streaming.py

# សាកល្បងលំនាំក្នុងបរិយាកាសផលិតកម្ម
python examples/production.py
```

**គំរូ 08: Windows 11 Chat Application**
```powershell
# ចូលទៅកាន់ថតគំរូ
cd samples/08

# តំឡើងអាស្រ័យភាពរបស់ Node.js
npm install

# ចាប់ផ្តើមកម្មវិធី Electron
npm start

# ឬ បង្កើតសម្រាប់ការផលិត
npm run build
```

**គំរូ 09: Advanced Multi-Agent System**
```powershell
# ចូលទៅកាន់ថតឧទាហរណ៍
cd samples/09

# ដំឡើងអាស្រ័យភាពប្រព័ន្ធសម្រាប់ភ្នាក់ងារ
pip install -r requirements.txt

# រត់ឧទាហរណ៍សម្របសម្រួលមូលដ្ឋាន
python examples/basic_coordination.py

# សាកល្បងដំណើរការងារស្មុគស្មាញ
python examples/complex_workflow.py

# ការបង្ហាញភ្នាក់ងារអន្តរកម្ម
python examples/interactive_demo.py
```

**គំរូ 10: Foundry Tools Framework**
```powershell
# ទៅកាន់ថតឧទាហរណ៍
cd samples/10

# តំឡើងអាស្រ័យភាពរបស់ហ្វ្រេមវ័រ
pip install -r requirements.txt

# រត់ការបង្ហាញឧបករណ៍មូលដ្ឋាន
python examples/basic_tools.py

# ចាប់ផ្តើមម៉ាស៊ីនបម្រើ REST API
python examples/rest_api_server.py
# API អាចប្រើបាន​នៅ http://localhost:8080

# សាកល្បងកម្មវិធី CLI
python examples/cli_application.py --help

# បើក Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# សាកល្បងការរួមបញ្ចូល LangChain
python examples/langchain_demo.py
```

### ដោះស្រាយបញ្ហាទូទៅ

**កំហុសការតភ្ជាប់ Foundry Local**
```powershell
# ពិនិត្យស្ថានភាពសេវា
foundry status

# ចាប់ផ្តើមឡើងវិញ ប្រសិនបើចាំបាច់
foundry restart

# ផ្ទៀងផ្ទាត់ការចូលប្រើបានរបស់ចំណុចបញ្ចប់
curl http://localhost:5273/v1/models
```

**បញ្ហាក្នុងការបញ្ចូលម៉ូដែល**
```powershell
# ពិនិត្យម៉ូដែលដែលអាចប្រើបាន
foundry model list --cached

# ទាញយកម៉ូដែលដែលខ្វះ
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# បង្ខំផ្ទុកឡើងវិញ ប្រសិនបើចាំបាច់
foundry model unload --all
foundry model run phi-4-mini
```

**បញ្ហាអាស្រ័យភាព**
```powershell
# អាប់ដេត pip ហើយដំឡើងម្តងទៀត
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# សម្រាប់គំរូ Node.js
npm cache clean --force
npm install
```

## សេចក្ដីសង្ខេប
ម៉ូឌុលនេះតំណាងឱ្យកម្រិតកំពូលនៃការអភិវឌ្ឍ Edge AI ដោយបញ្ចូលឧបករណ៍ថ្នាក់អាជីវកម្មរបស់ Microsoft ជាមួយភាពបត់បែន និងនវានុវត្តន៍នៃប្រព័ន្ធប្រភពបើក។ ដោយពួកអ្នកស៊ាំ Foundry Local តាមរយៈគំរូទាំង 10 ដែលពេញលេញ អ្នកនឹងត្រូវបានដាក់នៅចំពោះមុខនៃការអភិវឌ្ឍកម្មវិធី AI។

**ផ្លូវសិក្សាពេញលេញ:**
- **Foundation** (Samples 01-03): ការរួមបញ្ចូល API និងការគ្រប់គ្រងម៉ូឌែល
- **Applications** (Samples 04-06): RAG, agents, និងការបញ្ជូនដំណើរការឆ្លាត
- **Advanced** (Samples 07-10): ស៊ុមរចនាសម្ព័ន្ធសម្រាប់ផលិតកម្ម និងការរួមបញ្ចូលជាមួយសហគ្រាស

សម្រាប់ការរួមបញ្ចូល Azure OpenAI (Session 2), សូមមើលឯកសារ README នៃគំរូនីមួយៗ សម្រាប់អថេរបរិយាកាសដែលត្រូវការ និងការកំណត់កំណែ API។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែបញ្ញាសិប្បនិម្មិត [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះយើងខិតខំរកភាពត្រឹមត្រូវក៏ដោយ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានពិចារណាថាជាប្រភពផ្លូវការដែលមានសិទ្ធិ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->