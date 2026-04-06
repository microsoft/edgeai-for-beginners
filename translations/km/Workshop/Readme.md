# EdgeAI សម្រាប់អ្នកចាប់ផ្តើម - សិក្ខាសាលា

> **ផ្លូវហ្វឹកហាត់ដៃសម្រាប់បង្កើតកម្មវិធី Edge AI ដែលរួចរាល់សម្រាប់ផលិតកម្ម**
>
> ជំនាញរៀបចំ AI មូលដ្ឋានជាលក្ខណៈធ្វើ​បានជាកម្មវិធីតាមទីតាំងជាមួយ Microsoft Foundry Local ចាប់ពីការបញ្ចប់ជជែកដំបូង ដល់ការគ្រប់គ្រងម៉ាស៊ីនច្រើនក្នុងសម័យ ៦ ផ្នែកលំដាប់កើនជានិច្ច។

---

## 🎯 បញ្ចូលមុខ

សូមស្វាគមន៍មកកាន់ **សិក្ខាសាលា EdgeAI សម្រាប់អ្នកចាប់ផ្តើម** - មនុស្សណាមួយដែលចង់បានមគ្គុទេសក៍អនុវត្តបទដ្ឋានដៃ ហើយកសាងកម្មវិធីប្រសើរដែលដំណើរការមួយគត់នៅលើថាសហ្គោល។ សិក្ខាសាលានេះបម្លែងគំនិត Edge AI ទៅជាជំនាញពិតប្រាកដតាមរយៈលំហាត់ដែលមានកម្រិតតំបន់កើនមកវិញ ដោយប្រើ Microsoft Foundry Local និង ម៉ូដែលភាសាខ្នាតតូច (SLMs)។

### ហេតុអ្វីបានជាសិក្ខាសាលានេះ?

**បដិវត្តន៍ Edge AI បានមកដល់ហើយ**

អង្គការផ្សេងៗទូទាំងពិភពលោកកំពុងផ្លាស់ប្តូរពី AI ដែលពឹងផ្អែកលើពពកទៅកាន់កំណត់ជំហាន edge computing ដើម្បីមូលហេតុ ៣ សំខាន់ៈ

1. **ឯកជនភាព និងការអនុលោមតាមច្បាប់** - ដំណើរការទិន្នន័យសំខាន់នៅទីតាំងមូលដោយគ្មានការផ្ញើពពក (HIPAA, GDPR, វិធានហិរញ្ញវត្ថុ)
2. **ប្រសិទ្ធភាព** - កាត់បន្ថយភាពយឺតបណ្តាញ (50-500ms នៅជាប់កន្លែង ប្រៀបធៀបទៅនឹង 500-2000ms ក្នុងពពក)
3. **ការគ្រប់គ្រងចំណាយ** - លុបចោលថ្លៃប្រើប្រាស់ API ក្នុងរាល់ហត្ថលេខា និងកំណត់មាត្រដ្ឋានដោយគ្មានចំណាយពពក

**ប៉ុន្តែ Edge AI ខុសពីមុន**

ការរត់ AI នៅជាប់កន្លែងទាមទារជំនាញថ្មីៗ៖
- ជ្រើសម៉ូដែល និងធ្វើឱ្យប្រសើរឡើងសម្រាប់កំណត់ដែនធនធាន
- គ្រប់គ្រងសេវាកម្មក្នុងជំហានមូល និងល្បឿនបង្គាត់សៀគ្វី
- ស្ថាបនាវីធីទប់ចិត្តសម្រាប់ម៉ូដែលតូច
- គំរូប្រើប្រាស់ផលិតកម្មសម្រាប់ឧបករណ៍មូលដ្ឋាន

**សិក្ខាសាលានេះផ្តល់ជំនាញទាំងនោះ**

ក្នុង ៦ សម័យផ្តោតលើ (~3 ម៉ោងសរុប) អ្នកនឹងរីកចម្រើនពី "Hello World" ទៅដល់ការដាក់បញ្ចូលប្រព័ន្ធម៉ាស៊ីនច្រើនរួចរាល់សម្រាប់ផលិតកម្ម — ទាំងអស់នេះដំណើរការនៅលើកុំព្យូទ័ររបស់អ្នក។

---

## 📚 គោលបំណងរៀន

ដោយបញ្ចប់សិក្ខាសាលានេះ អ្នកនឹងអាច:

### ជំនាញស្នូល
1. **ដាក់បញ្ចូល និងគ្រប់គ្រងសេវាកម្ម AI មូលដ្ឋាន**
   - ដំឡើង និងកំណត់ Microsoft Foundry Local
   - ជ្រើសម៉ូដែលសមរម្យសម្រាប់ការដាក់បញ្ចូលមូល
   - គ្រប់គ្រងជីវិតម៉ូដែល (ទាញយក ផ្ទុក ហើយ​អង្គចងចាំ)
   - ត្រួតពិនិត្យការប្រើធនធាន និងធ្វើឱ្យមានប្រសិទ្ធភាព

2. **បង្កើតកម្មវិធីដែលមាន AI ជាជំនួយ**
   - អនុវត្តការបញ្ចប់ជជែកសមស្របនឹង OpenAI នៅក្នុងមូលដ្ឋាន
   - ធ្វើរចនាសេចក្តីទប់ចិត្តល្អសម្រាប់ម៉ូដែលភាសាខ្នាតតូច
   - គ្រប់គ្រងចម្លើយបន្តសម្រាប់ UX ល្អប្រសើរ
   - សម្របម៉ូដែលក្នុងមូលទៅកម្មវិធីដែលមានរួចហើយ

3. **បង្កើតប្រព័ន្ធ RAG (Generation ជំនួយការទាញយក)**
   - បង្កើតស្វែងរកអត្ថន័យជាមួយគំនូសនិមិត្ត
   - ពង្រឹងចម្លើយ LLM ជាស្គាល់ច្បាស់ក្នុងវិស័យជាក់លាក់
   - វាយតម្លៃគុណភាព RAG ជាមួយគន្លងឧស្សាហកម្ម
   - កំណត់តាមទំហំចាប់ផ្តើមរហូតដល់ផលិតកម្ម

4. **ធ្វើឱ្យមានប្រសិទ្ធភាពការ​ដំណើរការ​ម៉ូឌែល**
   - បរិច្ឆេទម៉ូដែលច្រើនសម្រាប់ករណីប្រើប្រាស់
   - វាស់ពេលយឺត ស្ថានភាពឆ្លើយ និងពេលបានតួហត្ថលេខាលើកដំបូង
   - ជ្រើសម៉ូដែលល្អបំផុតដោយផ្អែកលើជំពូកល្បឿន/គុណភាព
   - ប្រៀបធៀបចំណុចប្រយោជន៍ SLM ទល់នឹង LLM ក្នុងស្ថានការណ៍ពិតប្រាកដ

5. **រៀបចំប្រព័ន្ធម៉ាស៊ីនច្រើន**
   - រចនាម៉ាស៊ីនជាពិសេសសម្រាប់ភារកិច្ចផ្សេងៗ
   - អនុវត្តចងចាំម៉ាស៊ីន និងគ្រប់គ្រងបរិបទ
   - សម្របមាស៊ីនក្នុងសកម្មភាពស្មុគស្មាញ
   - ស្នើសុំការចូលបំរើយ៉ាងមានវិជ្ជាជីវៈឡើងទៅម៉ូដែលច្រើន

6. **ដាក់បញ្ចូលដំណោះស្រាយដាក់ប្រាក់ដំណើរការ**
   - ដាក់អនុវត្តការដោះស្រាយកំហុស និងស្រង់ឡើងវិញ
   - ត្រួតពិនិត្យការប្រើហត្ថលេខា និងធនធានប្រព័ន្ធ
   - កសាងរចនាសម្ព័ន្ធដែលអាចពង្រីកបានជាមួយគំនិតម៉ូដែលជាឧបករណ៍
   - គ្រោងផ្លូវផ្លាស់ប្តូរពី edge ទៅ hybrid (edge + cloud)

---

## 🎓 លទ្ធផលរៀន

### អ្វីដែលអ្នកនឹងបង្កើត

នៅចុងបញ្ចប់សិក្ខាសាលានេះ អ្នកបានបង្កើត:

| សម័យ | ផលិតផល | ជំនាញបង្ហាញ |
|---------|-------------|---------------------|
| **1** | កម្មវិធីជជែកជាមួយចម្លើយបន្ត | ការតំឡើងសេវា, ការបញ្ចប់មូលដ្ឋាន, ការបន្ត UX |
| **2** | ប្រព័ន្ធ RAG ជាមួយវាយតម្លៃ | គំនូសនិមិត្ត, ស្វែងរកអត្ថន័យ, គន្លងគុណភាព |
| **3** | សំណុំបែបបទវាស់ម៉ូដែលច្រើន | វាស់សមត្ថភាព, ប្រៀបធៀបម៉ូដែល |
| **4** | ប្រៀបធៀប SLM ទល់នឹង LLM | វិភាគការប្រែប្រួល, គោលការណ៍ប្រសើរឡើង |
| **5** | អ្នករៀបចំម៉ាស៊ីនច្រើន | រចនាម៉ាស៊ីន, គ្រប់គ្រងចងចាំ, សម្រួល |
| **6** | ប្រព័ន្ធបញ្ជូនយ៉ាងវៃឆ្លាត | ការរកឃើញបំណង, ជ្រើសម៉ូដែល, កំណត់មាត្រដ្ឋាន |

### តារាងជំនាញ

| កម្រិតជំនាញ | សម័យ ១-២ | សម័យ ៣-៤ | សម័យ ៥-៦ |
|-------------|-------------|-------------|-------------|
| **អ្នកចាប់ផ្តើម** | ✅ តំឡើង និងមូលដ្ឋាន | ⚠️ ថោកស្មាន | ❌ មិនសមរាប់ |
| **មធ្យម** | ✅ ពិនិត្យរហ័ស | ✅ រៀនស្នូល | ⚠️ គោលដៅកំណាត់ចិត្ត |
| **ជំនាញខ្ពស់** | ✅ ងាយស្រួល | ✅ ការកែលម្អ | ✅ គំរូផលិតកម្ម |

### ជំនាញមុខរបរ

**បន្ទាប់ពីសិក្ខាសាលានេះ អ្នកនឹងមានសមត្ថភាពក្នុងការបំពេញ៖**

✅ **បង្កើតកម្មវិធីឯកជនភាពជាទីមួយ**
- កម្មវិធីសុខាភិបាលដែលគ្រប់គ្រង PHI/PII នៅកន្លែង
- សេវាពហុហិរញ្ញវត្ថុដែលតម្រូវស្របច្បាប់
- ប្រព័ន្ធរដ្ឋាភិបាលដែលតម្រូវសិទ្ធិទិន្នន័យ

✅ **ធ្វើឱ្យប្រសើរលើបរិយាកាស Edge**
- ឧបករណ៍ IoT ដែលមានធនធានកំណត់
- កម្មវិធីទូរសព្ទចល័តក្រៅបណ្ដាញជាមុន
- ប្រព័ន្ធពេលវេលាពិតមានយឺតតិច

✅ **រចនាស្ថាបត្យកម្មវៃឆ្លាត**
- ប្រព័ន្ធម៉ាស៊ីនច្រើនសម្រាប់សកម្មភាពស្មុគស្មាញ
- ការដាក់ប្រាក់លើផ្លូវ edge-cloud លើសគ្នា
- បច្ចេកវិទ្យា AI ដែលបង្កើតចំណាយបានល្អ

✅ **ដឹកនាំយុទ្ធនាការ Edge AI**
- វាយតម្លៃសមត្ថភាព Edge AI សម្រាប់គម្រោង
- ជ្រើសម៉ូដែល និងវេទិកាសមរម្យ
- រចនាផែនការទាំងមូលសម្រាប់ AI មូល

---

## 🗺️ រចនាសម្ព័ន្ធសិក្ខាសាលា

### សម័យសិក្សា (6 សម័យ × 30 នាទី = 3 ម៉ោង)

| សម័យ | ប្រធានបទ | ផ្តោត | រយៈពេល |
|---------|-------|-------|----------|
| **1** | ចាប់ផ្តើមជាមួយ Foundry Local | ដំឡើង, ត្រួតពិនិត្យ, បញ្ចប់ដំបូង | 30 នាទី |
| **2** | បង្កើតដំណោះស្រាយ AI ជាមួយ RAG | វិច្ឆេរ prompt, embeddings, វាយតម្លៃ | 30 នាទី |
| **3** | ម៉ូដែល Open Source | រកឃើញម៉ូដែល, វាស់សមត្ថភាព, ជ្រើសរើស | 30 នាទី |
| **4** | ម៉ូដែល Cutting Edge | SLM ទល់នឹង LLM, ប្រសើរឡើង, វេទិកា | 30 នាទី |
| **5** | អ្នកភ្នាក់ងារដោយ AI | រចនាម៉ាស៊ីន, រឿងកំណត់ចងចាំ, សម្របសម្រួល | 30 នាទី |
| **6** | ម៉ូដែលជាឧបករណ៍ | បញ្ជូន, បង្រួបបង្រួម, គន្លងពង្រីក | 30 នាទី |

---

## 🚀 ចាប់ផ្តើមយ៉ាងរហ័ស

### ជំនួយលក្ខខណ្ឌ

**តម្រូវការប្រព័ន្ធ៖**
- **ប្រព័ន្ធប្រតិបត្តិការ**: Windows 10/11, macOS 11+, ឬ Linux (Ubuntu 20.04+)
- **រ៉ាំ**: 8GB ជាទំនេរ, ត្រូវបានផ្តល់អនុសាសន៍ 16GB+
- **ការផ្ទុកទិន្នន័យ**: ទំហំទំនេរ 10GB+ សម្រាប់ម៉ូដែល
- **CPU**: ប្រព័ន្ធកំចាត់ស្លឹកទំនើបដែលគាំទ្រ AVX2
- **GPU** (ចង់បាន): មានខ្នាត CUDA សមរម្យ ឬ Qualcomm NPU សម្រាប់ល្បឿនបង្កើត

**តម្រូវការផ្នែកទន់ៈ**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installation Guide](#install-foundry-local))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (ផ្តល់អនុសាសន៍) ([Download](https://code.visualstudio.com/))

### ដំឡើងក្នុង 3 ជំហាន

#### 1. ដំឡើង Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**ផ្ទៀងផ្ទាត់ការដំឡើង:**
```bash
foundry --version
foundry service status
```

**ប្រាកដថា Azure AI Foundry Local កំពុងដំណើរការជាមួយផតខ្សែថេរ**

```bash
# កំណត់ FoundryLocal ដើម្បីប្រើព័រត 58123 (លំនាំដើម)
foundry service set --port 58123 --show

# ឬប្រើព័រតផ្សេងទៀត
foundry service set --port 58000 --show
```

**ផ្ទៀងផ្ទាត់ថាដំណើរការ​ស្ថិតល្អ:**
```bash
# ពិនិត្យស្ថានភាពសេវា
foundry service status

# សាកល្បងចុងបញ្ចប់
curl http://127.0.0.1:58123/v1/models
```
**រកម៉ូដែលដែលមាននៅ Foundry Local**
ដើម្បីមើលម៉ូដែលដែលមាននៅក្នុង Foundry Local របស់អ្នក អ្នកអាចស្នើសុំទៅកាន់ endpoints ម៉ូដែល៖

```bash
# ពាក្យបញ្ជា/bash/powershell
foundry model list
```

ប្រើ Web Endpoint

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# ឬប្រើ curl (បើមាន)
curl http://127.0.0.1:58123/v1/models
```

#### 2. ស្វែងបានរ៉េប៉ូស៊ីតូរី និងដំឡើងការពឹងផ្អែក

```bash
# បង្កើតចម្លងឃ្លាំងទិន្នន័យ
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# បង្កើតបរិដ្ឋានវើឌួល
python -m venv .venv

# បើកបរិដ្ឋានវើឌួល
# វីនដូច:
.\.venv\Scripts\activate
# ម៉ាក់អូអិល/លីនុច:
source .venv/bin/activate

# ដំឡើងការពឹងផ្អែក
pip install -r requirements.txt
```

#### 3. រត់គំរូដំបូងរបស់អ្នក

```bash
# ចាប់ផ្ដើម Foundry Local ហើយបញ្ចូលម៉ូដែលមួយ
foundry model run phi-4-mini

# ប្រតិបត្តិការណ៍សំណុំបង្ហាញការចាប់ផ្ដើម chat
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ ជោគជ័យ!** អ្នកគួរតែបានមើលឃើញចម្លើយបន្តអំពី edge AI។

---

## 📦 ឯកសារសិក្ខាសាលា

### គំរូ Python

ឧទាហរណ៍ហ្វឹកហាត់ដៃដែលកើនឡើងបង្ហាញគំនិតមួយៗ៖

| សម័យ | គំរូ | សង្ខេប | ពេលរត់ |
|---------|--------|-------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | ជជែកមូលដ្ឋាន និងបន្ត | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG ជាមួយគំនូសនិមិត្ត | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | វាយតម្លៃគុណភាព RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | វាស់ម៉ូដែលច្រើន | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | ប្រៀបធៀប SLM ទល់នឹង LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | ប្រព័ន្ធម៉ាស៊ីនច្រើន | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | បញ្ជូនដោយបំណង | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | លំហូរបញ្ចូលច្រើនជំហាន | ~60s |

### សៀវភៅកំណត់ហេតុ Jupyter

ស្វែងយល់ចម្រុះដោយមានការពន្យល់និងផ្គូផ្គងរូបភាព៖

| សម័យ | សៀវភៅកំណត់ហេតុ | សង្ខេប | កម្រិត |
|---------|----------|-------------|------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | ជជែកជារដ្ឋមូលដ្ឋាន និងបន្ត | ⭐ អ្នកចាប់ផ្តើម |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | បង្កើតប្រព័ន្ធ RAG | ⭐⭐ មធ្យម |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | វាយតម្លៃគុណភាព RAG | ⭐⭐ មធ្យម |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | វាស់ម៉ូដែល | ⭐⭐ មធ្យម |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | ប្រៀបធៀបម៉ូដែល | ⭐⭐ មធ្យម |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | រៀបចំម៉ាស៊ីន | ⭐⭐⭐ ខ្ពស់ |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | បញ្ជូនដោយបំណង | ⭐⭐⭐ ខ្ពស់ |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | លំហូរបញ្ចូល | ⭐⭐⭐ ខ្ពស់ |

### ឯកសារ

មគ្គុទេសក៍ពេញលេញ និងឯកសារយោង៖

| ឯកសារ | សង្ខេប | ប្រើពេលណា |
|----------|-------------|----------|
| [QUICK_START.md](./QUICK_START.md) | មគ្គុទេសការដំឡើងលឿន | ចាប់ផ្តើមពីគ្នា |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | ជំនួយមួយសន្លឹក សម្រាប់ពាក្យបញ្ជា និង API | ត្រូវការឆ្លើយតបរហ័ស |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | គំរូ និងម៉ូដែល SDK | ការសរសេរកូដ |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | មគ្គុទេសក៍អំពីអថេរសៀវភៅបរិយាកាស | កំណត់កំណត់ឧទាហរណ៍ |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | បញ្ហាទូទៅ និងដោះស្រាយ | ផ្ទៀងផ្ទាត់កំហុស |

---

## 🎓 ការផ្តល់អនុសាសន៍ផ្លូវរៀន

### សម្រាប់អ្នកចាប់ផ្តើម (3-4 ម៉ោង)
1. ✅ សម័យ ១៖ ចាប់ផ្តើម (ផ្តោតលើការតំឡើង និងជជែកមូលដ្ឋាន)
2. ✅ សម័យ ២៖ មូលដ្ឋាន RAG (បោះបង់ការវាយតម្លៃនៅដំបូង)
3. ✅ សម័យ ៣៖ វាស់សេវាមូលដ្ឋាន (ម៉ូដែល 2 តែប៉ុណ្ណោះ)
4. ⏭️ ជ្រើសរើសមិនចូលរួមសម័យ ៤-៦ ពេលនេះ
5. 🔄 ត្រឡប់ទៅសម័យ ៤-៦ បន្ទាប់ពីបង្កើតកម្មវិធីដំបូងរួច

### សម្រាប់អ្នកអភិវឌ្ឍន៍មធ្យម (3 ម៉ោង)
1. ⚡ សម័យ ១៖ ត្រួតពិនិត្យការតំឡើងរហ័ស
2. ✅ សម័យ ២៖ បញ្ចប់លំហាត់ RAG ជាមួយវាយតម្លៃ
3. ✅ សម័យ ៣៖ សំណុំពេញវាស់ម៉ូឌែល
4. ✅ សម័យ ៤៖ ធ្វើឱ្យប្រសើរម៉ូដែល
5. ✅ សម័យ ៥-៦៖ ផ្តោតលើគំរូស្ថាបត្យកម្ម

### សម្រាប់អ្នកជំនាញខ្ពស់ (2-3 ម៉ោង)
1. ⚡ សម័យ ១-៣៖ ធ្វើការពិនិត្យបន្ទាន់ និងផ្ទៀងផ្ទាត់
2. ✅ សម័យ ៤៖ ជ្រាបជ្រាលក្នុងការសម្រេចប្រសើរ
3. ✅ សម័យ ៥៖ រចនាស្ថាបត្យកម្មម៉ាស៊ីនច្រើន
4. ✅ សម័យ ៦៖ គំរូផលិតកម្ម និងការពង្រីក
5. 🚀 ពង្រីក៖ បង្កើតគន្លងបញ្ជូនផ្ទាល់ខ្លួន និងការដាក់ប្រាក់លើផ្លូវ hybrid

---

## ជំពូកសម័យសិក្ខាសាលា (មន្ទីរពិសោធន៍ផ្តោត ៣០ នាទី)

បើអ្នកតាមម៉ូឌុលសិក្ខាសាលា ៦ សម័យដែលខ្លីនេះ ប្រើមគ្គុទេសក៍ដូចខាងក្រោម (មួយៗផ្គូផ្គង និងបំពេញឯកសារខាងលើ):

| សម័យសិក្ខាសាលា | មគ្គុទេស | ផ្តោតស្នូល |
|------------------|-------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | ដំឡើង, ត្រួតពិនិត្យ, រត់ phi & GPT-OSS-20B, ល្បឿនបង្កើត |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | វិច្ឆេរ prompt, គំរូ RAG, CSV & ការទទួលដាក់ឯកសារ, ផ្លាស់ប្តូរ |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | លាយបញ្ចូល Hugging Face, វាស់វែង, ជ្រើសម៉ូដែល |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM ទល់នឹង LLM, WebGPU, Chainlit RAG, ល្បឿន ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | តួនាទីម៉ាស៊ីន, ចងចាំ, ឧបករណ៍, សម្របសម្រួល |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | បញ្ជូន, បង្រួបបង្រួម, ផ្លូវពង្រីកទៅ Azure |
ឯកសារពិធីការរៀននីមួយៗរួមមាន៖ សង្ខេប គោលបំណងការរៀន ស្ទង់ពេល ៣០ នាទី សេចក្ដីអញ្ជើញគំរូ គ្រប់គ្រងការត្រួតពិនិត្យ ការដោះស្រាយបញ្ហា និងយោងទៅកាន់ Foundry Local Python SDK ផ្លូវការណ៍។

### ស្គ្រីបគំរូ

តំឡើងផ្នែកបំណងសិក្សា (Windows)៖

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
  
macOS / Linux៖

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
  
បើបើកសេវាកម្ម Foundry Local នៅលើកុំព្យូទ័រផ្សេង (Windows) ឬ VM ពី macOS សូមបញ្ជូនចេញ endpoint៖

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
| ពិធីការ | ស្គ្រីប(ៗ) | សេចក្ដីពិពណ៌នា |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | សេវាកម្ម Bootstrap និងការចាក់ផ្សាយជជែក |
| 2 | `samples/session02/rag_pipeline.py` | RAG អប្បបរមា (embedding នៅក្នុងម៉ាស៊ីន) |
|   | `samples/session02/rag_eval_ragas.py` | ការវាយតម្លៃ RAG ជាមួយគោលនីយម ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | ការវាយតម្លៃស្ទង់ពេលលឿន និង throughput ទៅលើម៉ូដែលច្រើន |
| 4 | `samples/session04/model_compare.py` | ប្រៀបធៀប SLM និង LLM (ស្ទង់ពេល និងលទ្ធផលគំរូ) |
| 5 | `samples/session05/agents_orchestrator.py` | ការស្រាវជ្រាវដោយភ្នាក់ងារពីរជា pipeline កែសម្រួល |
| 6 | `samples/session06/models_router.py` | ធ្វើដំបូន្មានដោយផ្អែកលើគំរោង |
|   | `samples/session06/models_pipeline.py` | ខ្សែសង្វាក់គំនិតលម្អិត ធ្វើ និង បន្តពិនិត្យ |

### អថេរបរិបទ (ធ្វើដំណើរជាសាធារណៈគ្នានៃគំរូ)

| អថេរ | គោលបំណង | ឧទាហរណ៍ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | ឈ្មោះម៉ូដែលតែមួយដើមសម្រាប់គំរូមូលដ្ឋាន | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | ឈ្មោះម៉ូដែល SLM ឬ LLM សម្រាប់ប្រៀបធៀប | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | បញ្ជីឈ្មោះម៉ូដែលផ្សេងៗសម្រាប់វាយតម្លៃ | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | ចំនួនសិប្បនិម្មិតសម្រាប់វាយតម្លៃ | `3` |
| `BENCH_PROMPT` | ប្រើសម្រាប់ប្រើក្នុងការវាយតម្លៃ | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | ម៉ូដែល embedding sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | ទិន្នន័យសំណួរតេស្តសម្រាប់ pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | សំណួរសម្រាប់ pipeline អ្នកប្រតិភូ | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | ឈ្មោះម៉ូដែលសម្រាប់ភ្នាក់ងារស្រាវជ្រាវ | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | ឈ្មោះម៉ូដែលសម្រាប់ភ្នាក់ងារ​កែលម្អ (អាចខុសគ្នា) | `gpt-oss-20b` |
| `SHOW_USAGE` | បើជាសំណុំពាក្យ `1` បង្ហាញការប្រើ token ក្នុងកំឡុងបញ្ចប់ | `1` |
| `RETRY_ON_FAIL` | បើជា `1` ជំនួសម្តងនៅពេលមានកំហុសជជែកចោល | `1` |
| `RETRY_BACKOFF` | វេលាទុករង់ចាំមុនធ្វើជំនួស | `1.0` |

បើអថេរមួយមិនបានកំណត់ ស្គ្រីបនឹងប្រើលំនាំដើមដែលសមរម្យ។ សម្រាប់ការបង្ហាញម៉ូដែលតែមួយជាធម្មតា អ្នកត្រូវតែប្រើតែ `FOUNDRY_LOCAL_ALIAS` ប៉ុណ្ណោះ។

### ម៉ូឌុលជំនួយ

គំរូទាំងអស់ឥឡូវនេះប្រើគំនួយ `samples/workshop_utils.py` ដែលផ្ដល់៖

* ការបង្កើត FoundryLocalManager និង OpenAI client បានយ៉ាងមានប្រសិទ្ធភាព  
* ជំនួយ `chat_once()` ជាជម្រើស retry + បង្ហាញការប្រើ  
* រាយការណ៍អំពីការប្រើ token យ៉ាងសាមញ្ញ (បើបើកដោយ `SHOW_USAGE=1`)

នេះបន្ថយការចម្លងស្គ្រីបហើយបង្ហាញពីការអនុវត្តល្អសម្រាប់ច្រកបណ្ដាញម៉ូដែលក្នុងម៉ាស៊ីនមូលដ្ឋានបានយ៉ាងមានប្រសិទ្ធភាព។

## ការកែលម្អជាជម្រើស (ជាកាត់តម្កល់ជាផ្លូវការ)

| ប្រធានបទ | ការកែប្រែ | ពិធីការ | បរិយាកាស / បិទបើក |
|-------|-------------|----------|--------------|
| Determinism | កំណត់សីតុណ្ហភាព + ប្រព័ន្ធបញ្ចូលឯកសារត្រួតបន្តិច | 1–6 | កំណត់ `temperature=0`, `top_p=1` |
| Token Usage Visibility | បង្ហាញថ្លៃ/ប្រសិទ្ធភាពយ៉ាងមិនប្រែប្រួល | 1–6 | `SHOW_USAGE=1` |
| Streaming First Token | វិមាត្រស្ទង់ពេល latency | 1,3,4,6 | `BENCH_STREAM=1` (វាយតម្លៃ) |
| Retry Resilience | ទប់ស្កាត់ភាពខ្សោយចាប់ផ្តើមក្រោម | ទាំងអស់ | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | ការបែងចែកតួនាទីនៃភ្នាក់ងារច្រើនម៉ូដែល | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptive Routing | ចំណង់ចំណូល + គន្លងថ្លៃ | 6 | ផ្ដល់ជំនួយការជួរមុខជាមួយហេតុផលចម្រូងចម្រាស់ |
| Vector Memory | ការចងចាំយូរអង្វែងផ្អែកលើអត្ថន័យ | 2,5,6 | ដាក់បញ្ចូល FAISS/Chroma សម្រាប់ index embedding |
| Trace Export | ការត្រួតពិនិត្យ និងវាយតម្លៃ | 2,5,6 | បន្ថែម JSON ក្នុងមួយជំហាន |
| Quality Rubrics | ការត្រួតពិនិត្យគុណភាព | 3–6 | ការវាយតម្លៃជាជំនួយផ្សេងទៀត |
| Smoke Tests | ការពិនិត្យមើលមុនវាគ្មិន | ទាំងអស់ | `python Workshop/tests/smoke.py` |

### ត្រួតបន្ថែមដោយរហ័សដោយកំណត់

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```
  
រំពឹងថា token នឹងដូចគ្នានៅលើការបញ្ចូលដូចគ្នាក្នុងសំណុំម្តងម្កាល។

### ការវាយតម្លៃ RAG (ពិធីការ 2)

ប្រើ `rag_eval_ragas.py` ដើម្បីគណនា ភាពសុពលភាព សេចក្ដីជឿ និងភាពត្រឹមត្រូវបរិបទលើសំណុំទិន្នន័យសង្ខេបមួយ៖

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```
  
បន្ថែមទិន្នន័យដោយផ្ដល់ JSONL ធំជាងនេះ រួចបម្លែងទៅជា Hugging Face `Dataset`។

## ភាគបន្ថែមអំពី CLI Command Accuracy

វគ្គសិក្សានេះប្រើតែសេចក្ដីបញ្ជាផ្លូវការដែលមានឯកសារនិងមានស្ថេរភាពបច្ចុប្បន្ន។

### បញ្ជាផ្លូវការដែលបានយោង

| ប្រភេទ | បញ្ជា | គោលបំណង |
|----------|---------|---------|
| មូលដ្ឋាន | `foundry --version` | បង្ហាញប័ណ្ណកំណែ |
| សេវាកម្ម | `foundry service start` | ចាប់ផ្តើមសេវាកម្មលើម៉ាស៊ីន (បើមិនមានជំហឹ) |
| សេវាកម្ម | `foundry service status` | បង្ហាញស្ថានភាពសេវាកម្ម |
| ម៉ូដែល | `foundry model list` | បញ្ជីម៉ូដែលក្នុងសៀវភៅ/មានស្រាប់ |
| ម៉ូដែល | `foundry model download <alias>` | ទាញយកទំងន់ម៉ូដែលទៅកាន់ cache |
| ម៉ូដែល | `foundry model run <alias>` | បើក (ផ្ទុក) ម៉ូដែលក្នុងម៉ាស៊ីន; ប្រើជាមួយ `--prompt` សម្រាប់ផ្ញើពាក្យលើកដំបូង |
| ម៉ូដែល | `foundry model unload <alias>` / `foundry model stop <alias>` | បញ្ឈប់ផ្ទុកម៉ូដែលចេញពីចងចាំ (បើបានគាំទ្រ) |
| cache | `foundry cache list` | បង្ហាញម៉ូដែលបាន cache (ទាញយក) |

### លំនាំ Prompt ពីលើ One-Shot

ជំនួសសម្រាប់ `model chat` ដែលមិនប្រើបានទៀតៈ

```powershell
foundry model run <alias> --prompt "Your question here"
```
  
នេះបំពេញមួយហៅសំណុំ/ប្រតិកម្មបន្ទាប់មកចេញ។

### លំនាំដែលបានលុប/ជៀសវាង

| មិនមានតម្លាភាព/គ្មានឯកសារ | ជំនួស/ណែនាំ |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | ប្រើសម្រាប់ `foundry model list` ធម្មតា + សកម្មភាពថ្មីៗ / កំណត់ហេតុ |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | ប្រើស្គ្រីប Python ពិនិត្យ + ឧបករណ៍ OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### ការវាយតម្លៃ និង Telemetry

- ភាពយឺត p95, tokens/វិនាទី៖ `samples/session03/benchmark_oss_models.py`  
- ភាពយឺត token ដំបូង (ការផ្គត់ផ្គង់): កំណត់ `BENCH_STREAM=1`  
- ការ​ប្រើធនធាន: មុខងារ OS (Task Manager, Activity Monitor, `nvidia-smi`)។

ពេលបញ្ជាទិញ telemetry CLI ថ្មីមានស្ថេរភាព upstream អាចបញ្ចូលក្នុង markdown session ដោយកាត់ចេញតិចតួច។

### Automated Lint Guard

កម្មវិធីលីនធ្វើការពារការរួមបញ្ចូលលំនាំ CLI ខុសក្នុង code blocks របស់ markdown៖

ស្គ្រីប៖ `Workshop/scripts/lint_markdown_cli.py`

លំនាំដែលបានហាមឃាត់នៅក្នុង fences។

ការជំនួសដែលបានណែនាំ៖  
| មិនគោរព | ជំនួស |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | ស្គ្រីបវាយតម្លៃ + ឧបករណ៍ប្រព័ន្ធ |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

រត់នៅលើម៉ាស៊ីន៖  
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```
  
GitHub Action៖ `.github/workflows/markdown-cli-lint.yml` រត់រាល់ការបញ្ចូល និង PR។

ព្រឹត្តិការណ៍ pre-commit ជាជម្រើស៖  
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
  
## តារាងផ្លាស់ប្តូរ CLI ទៅ SDK

| ការងារ | បញ្ជា CLI តែមួយជួរ | សមាជិក SDK (Python) ផ្ទាល់ | ការបញ្ចាក់ |
|------|---------------|-------------------------|-------|
| រត់ម៉ូដែលម្តង (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK បិទធ្វើសេវាកម្ម និង caching ដោយស្វ័យប្រវត្តិ |
| ទាញយក (cache) ម៉ូដែល | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | អ្នកគ្រប់គ្រងជ្រើសបំរែបំរួលល្អបើ alias មានច្រើនម៉ូដែល |
| បញ្ជីសៀវភៅ | `foundry model list` | `# use manager for each alias or maintain known list` | CLI សរុប; SDK បច្ចុប្បន្នបង្កើតមួយ alias ម្តង |
| បញ្ជីម៉ូដែលបានcache | `foundry cache list` | `manager.list_cached_models()` | បន្ទាប់ពីចាប់ផ្តើម manager (alias មួយណាមួយ) |
| ទទួល URL endpoint | (Implicit) | `manager.endpoint` | ប្រើបង្កើត OpenAI-compatible client |
| ពន្លត់ម៉ូដែល | `foundry model run <alias>` បន្ទាប់ prompt ដំបូង | `chat_once(alias, messages=[...])` (ជំនួយ) | ជំនួយដោះស្រាយដំណើរការសូត្រដំបូង latency |
| វាស់ស្ទង់ពេល latency | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (ឬស្គ្រីបនាំចេញថ្មី) | ផ្ដល់ផ្នែកស្គ្រីបសម្រាប់វាស់តម្លៃមិនប្រែប្រួល |
| បញ្ឈប់/ដកម៉ូដែលចេញ | `foundry model unload <alias>` | (មិនបង្ហាញ - ត្រូវចាប់ផ្តើមសេវាកម្មម្តងទៀត) | មិនតម្រូវណាស់សម្រាប់វិធីសាស្រ្តផលិតកម្ម |
| ស្នើរពាក្យតokens | (មើលលទ្ធផលប័ណ្ណ) | `resp.usage.total_tokens` | ផ្ដល់បើ backend ផ្តល់ usage object |

## ការនាំចេញ Markdown របាយការណ៍វាយតម្លៃ

ប្រើស្គ្រីប `Workshop/scripts/export_benchmark_markdown.py` ដើម្បីរត់វាយតម្លៃថ្មី (ដូចជាតំណលើ `samples/session03/benchmark_oss_models.py`) ហើយបញ្ចេញតារាង Markdown សមរម្យសម្រាប់ GitHub និង JSON ទ_raw_។

### ឧទាហរណ៏

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```
  
ឯកសារបង្កើត៖  
| ឯកសារ | ខ្លឹមសារ |
|------|----------|
| `benchmark_report.md` | តារាង Markdown + ការបកស្រាយផ្នែកសំខាន់ៗ |
| `benchmark_report.json` | អារេ metrics ទ_raw_ (សម្រាប់ប្រៀបធៀប / តាមដាន) |

កំណត់ `BENCH_STREAM=1` នៅក្នុងបរិយាកាសដើម្បីរួមបញ្ចូល latency token ដំបូងបើគាំទ្រ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងរកសុពលភាព ជាក់លាក់ សូមជំរុញឱ្យដឹងថាការបកប្រែដោយម៉ាស៊ីនអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមក្នុងភាសាទូទៅរបស់វាគួរត្រូវបានគិតថាជាប្រភពសម្គាល់ផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ សូមផ្តល់អនុសាសន៍ឱ្យជ្រើសរើសការបកប្រែដោយអ្នកជំនាញមនុស្ស។ ពួកយើងមិនធ្វើការទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែអ្វីដែលមិនត្រឹមត្រូវណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->