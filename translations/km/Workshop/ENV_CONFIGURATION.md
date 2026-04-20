# មគ្គុទេសក៍កំណត់បរិយាកាស

## ទិដ្ឋភាពទូទៅ

គំរូ Workshop ប្រើអថេរបរិយាកាសសម្រាប់ការកំណត់តម្លៃ ដែលបានមធ្យមមកជាកំណត់ក្នុងឯកសារ `.env` នៅដើមឃ្លាំង។ វាអាចធ្វើឲ្យការប្ដូរតម្លៃកាន់តែងាយស្រួល ដោយគ្មានការកែប្រែកូដ។

## ចាប់ផ្តើមយ៉ាងរហ័ស

### 1. ពិនិត្យតម្រូវការ

```bash
# ពិនិត្យមើលថា Foundry Local ត្រូវបានដំឡើងហើយ
foundry --version

# ពិនិត្យមើលថាសេវាកម្មកំពុងរត់
foundry service status

# ផ្ទុកម៉ូដែលមួយ
foundry model run phi-4-mini
```

### 2. កំណត់បរិយាកាស

ឯកសារ `.env` មានការកំណត់រួចជាមួយតម្លៃលំនាំដើមដែលមានន័យល្អ។ អ្នកប្រើភាគច្រើនមិនចាំបាច់ផ្លាស់ប្ដូរអ្វីឡើយ។

**ជំណាប់ជំនួស**: ពិនិត្យ និងប្តូរសមាសភាពការកំណត់:
```bash
# កែសម្រួលឯកសារ .env
notepad .env  # វីនដូ​ធျ
nano .env     # ម៉ាកអូអេស/លីនុច
```

### 3. អនុវត្តការកំណត់

**សម្រាប់ Script Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# អថេរសេវាកម្មបរិយាកាសបានផ្ទុកដោយស្វ័យប្រវត្តិ
```

**សម្រាប់ Notebook:**
```python
# ចាប់ផ្ដើម kernel ម្ដងទៀតបន្ទាប់ពីការផ្លាស់ប្តូរ .env
# អថេរត្រូវបានផ្ទុកពេលកូដក្នុង cells ដំណើរការ
```

## ឯកសារអថេរបរិយាកាសយោង

### ការកំណត់ស្នូល

| អថេរ | លំនាំដើម | សេចក្ដីពិពណ៌នា |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | ម៉ូឌែលលំនាំដើមសម្រាប់គំរូ |
| `FOUNDRY_LOCAL_ENDPOINT` | (ទទេ) | ប្តូរទីតាំងសេវាកម្ម |
| `PYTHONPATH` | ផ្លូវ Workshop | ផ្លូវស្វែងរកម៉ូឌុល Python |

**ពេលណាត្រូវកំណត់ FOUNDRY_LOCAL_ENDPOINT:**
- វិធីសាស្ត្រក្នុង Foundry Local ពីចម្ងាយ
- ការកំណត់កំពង់ផែនីយ៍ផ្ទាល់ខ្លួន
- ការបំបែកការអភិវឌ្ឍន៍/ផលិតកម្ម

**ឧទាហរណ៍:**
```bash
# កំពង់ផ្លូវផ្ទាល់ខ្លួន
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# ឧបករណ៍ចម្ងាយ
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### អថេរមុខងារក្នុងសម័យ

#### សម័យ 02: បណ្ដាញ RAG
| អថេរ | លំនាំដើម | គោលបំណង |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ម៉ូឌែលចាក់តំណរ |
| `RAG_QUESTION` | កំណត់រួច | សំណួរតេស្ត |

#### សម័យ 03: វាស់វែងប្រសិទ្ធភាព
| អថេរ | លំនាំដើម | គោលបំណង |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | ម៉ូឌែលសម្រាប់ប្រតិបត្តិតេស្ត |
| `BENCH_ROUNDS` | `3` | ចំនួនដំណើរការតាមម៉ូឌែល |
| `BENCH_PROMPT` | កំណត់រួច | ការបញ្ជាទាត់តេស្ត |
| `BENCH_STREAM` | `0` | វាស់ពេលយឺតនៃ token ដំបូង |

#### សម័យ 04: ប្រៀបធៀបទ្រង់ទ្រាយម៉ូឌែល
| អថេរ | លំនាំដើម | គោលបំណង |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | ម៉ូឌែលភាសាខ្នាតតូច |
| `LLM_ALIAS` | `qwen2.5-7b` | ម៉ូឌែលភាសាធំ |
| `COMPARE_PROMPT` | កំណត់រួច | បញ្ជាទាត់ប្រៀបធៀប |
| `COMPARE_RETRIES` | `2` | ចំនួនព្យាយាមជាពីរដង |

#### សម័យ 05: ការប្រតិបត្តិឯកអង្គច្រើន
| អថេរ | លំនាំដើម | គោលបំណង |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ម៉ូឌែលតំណាងអ្នកស្រាវជ្រាវ |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ម៉ូឌែលតំណាង អ្នកកែសម្រួល |
| `AGENT_QUESTION` | កំណត់រួច | សំណួរតេស្ត |

### ការកំណត់ប្រសិទ្ធិភាព

| អថេរ | លំនាំដើម | គោលបំណង |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | បង្ហាញការប្រើប្រាស់ token |
| `RETRY_ON_FAIL` | `1` | បើកល្បឿន retry |
| `RETRY_BACKOFF` | `1.0` | ពេលពន្យារពេល retry (វិនាទី) |

## ការកំណត់ទូទៅ

### ការតំឡើងអភិវឌ្ឍន៍ (ជំហានរហ័ស)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### ការតំឡើងផលិតកម្ម (ផ្តោតលើគុណភាព)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### ការតំឡើងវាស់វែងប្រសិទ្ធភាព
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### ភាពឯកជនឯកអង្គច្រើន
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # លឿនសម្រាប់ការស្រាវជ្រាវ
AGENT_MODEL_EDITOR=qwen2.5-7b         # គុណភាពសម្រាប់ការកែសម្រួល
```

### អភិវឌ្ឍន៍ពីចម្ងាយ
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## ម៉ូឌែលដែលបានណែនាំ

### តាមករណីប្រើប្រាស់

**គោលបំណងទូទៅ:**
- `phi-4-mini` - គុណភាពនិងល្បឿនត្រឹមត្រូវ

**ចម្លើយលឿន:**
- `qwen2.5-0.5b` - លឿនខ្លាំង សម្រាប់ចាត់ថ្នាក់
- `phi-4-mini` - លឿនជាមួយគុណភាពល្អ

**គុណភាពខ្ពស់:**
- `qwen2.5-7b` - គុណភាពល្អបំផុត ប្រើធនធានច្រើន
- `phi-4-mini` - គុណភាពល្អ ប្រើធនធានតិចជាង

**បង្កើតកូដ:**
- `deepseek-coder-1.3b` - ផ្តោតលើកូដ
- `phi-4-mini` - កូដគោលបំណងទូទៅ

### តាមការចូលប្រើធនធាន

**ធនធានទាប (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**ធនធានមធ្យម (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**ធនធានខ្ពស់ (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## ការកំណត់ដែលមានកម្រិតខ្ពស់

### ទីតាំងបញ្ជាក់ផ្ទាល់ខ្លួន

```bash
# បរិយាកាស​អភិវឌ្ឍន៍
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# បរិយាកាស​អាកាស​ថត
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# បរិយាកាស​ផលិត
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### សីតុណភាព & ការយកគំរូ (ប្តូរនៅក្នុងកូដ)

```python
# នៅក្នុងស្គ្រីប/សៀវភៅកំណត់ត្រារបស់អ្នក
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### ការតំឡើង Azure OpenAI លាយបញ្ចូល

```bash
# ប្រើ local សម្រាប់ការអភិវឌ្ឍន៍
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# កំណត់តម្លៃ Azure សម្រាប់ការត្រឡប់មកផលិតកម្ម
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## ការដោះស្រាយបញ្ហា

### អថេរបរិយាកាសមិនបានបញ្ចូល

**រោគសញ្ញា:**
- Script ប្រើម៉ូឌែលខុស
- កំហុសកាស្រូវភ្ជាប់
- អថេរមិនត្រូវបានស្គាល់

**ដំណោះស្រាយ:**
```bash
# 1. ធ្វើការត្រួតពិនិត្យថា .env មាននៅនៅឫសឃ្លាំងទិន្នន័យ
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. ពិនិត្យឯកសារមិនមែនជា .env.txt (Windows)
# ប្រាកដថាគ្មាននិទាឃរូបនិមិត្តនៅសងខាង

# 3. សម្រាប់សៀវភៅកំណត់ត្រា៖ ចាប់ផ្ដើម kernel ឡើងវិញ
# Kernel > ចាប់ផ្ដើមឡើងវិញ

# 4. សម្រាប់ស្គ្រីប៖ ពិនិត្យថាតំបន់ការងារ
pwd  # គួរតែមាននៅក្នុងសិក្ខាសាលា ឬឫសឃ្លាំងទិន្នន័យ
```

### បញ្ហាការភ្ជាប់សេវាកម្ម

**រោគសញ្ញា:**
- កំហុស "Connection refused"
- "Service not available"
- កំហុសពន្យារពេល

**ដំណោះស្រាយ:**
```bash
# 1. ពិនិត្យស្ថានភាពសេវា
foundry service status

# 2. ចាប់ផ្តើមបើមិនដំណើរការ
foundry service start

# 3. ផ្ទៀងផ្ទាត់ចំណុចចុងក្រោយ
# ពិនិត្យកំពស់(port) ក្នុងលទ្ធផលស្ថានភាព
foundry service status | grep "Port"

# 4. ធ្វើបច្ចុប្បន្នភាព .env ប្រសិនបើចាំបាច់
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### ម៉ូឌែលមិនឃើញ

**រោគសញ្ញា:**
- កំហុស "Model not found"
- "Alias not recognized"

**ដំណោះស្រាយ:**
```bash
# 1. បញ្ជីម៉ូដែលដែលមានស្រាប់
foundry model list

# 2. បញ្ចូលម៉ូដែលដែលត្រូវការ
foundry model run phi-4-mini

# 3. ធ្វើបច្ចុប្បន្នភាព .env ជាមួយម៉ូដែលដែលមានស្រាប់
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### កំហុសអំពីការនាំចូល

**រោគសញ្ញា:**
- កំហុស "Module not found"

**ដំណោះស្រាយ:**

```bash
# 1. បើកបរិស្ថានវីរុត្តិ
.venv\Scripts\activate  # វីនដូម
source .venv/bin/activate  # ម៉ាក់អូអេស/លីនុច

# 2. តំឡើងការពឹងផ្អែក
pip install -r requirements.txt
```

## ការពិនិត្យការកំណត់

### ពិនិត្យការបញ្ចូលបរិយាកាស

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### សាកល្បងការភ្ជាប់ Foundry Local

```python
# សាកល្បងការតភ្ជាប់.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## យុទ្ធសាស្ត្រសុវត្ថិភាពល្អបំផុត

### 1. មិនបញ្ចូលសម្ងាត់ចូលក្នុងចំណុច commit

```bash
# .gitignore គួរត្រូវមាន៖
.env
.env.local
*.key
```

### 2. ប្រើឯកសារ .env ផ្សេងគ្នា

```bash
.env              # ការកំណត់លំនាំដើម
.env.local        # ការផ្លាស់ប្តូរបណ្តោះអាសន្ននៃតំបន់ (មិនត្រូវចោលក្នុង git)
.env.production   # ការកំណត់ផលិតកម្ម (ការផ្ទុកដែលមានសុវត្ថិភាព)
```

### 3. បម្លែងកូនសោ API ជាប្រចាំ

```bash
# សម្រាប់ Azure OpenAI ឬសេវាកម្មពពកផ្សេងទៀត
# បង្ហូរលេខសំគាល់ជាប្រចាំ និងបញ្ជាក់ .env ឲ្យទាន់សម័យ
```

### 4. ប្រើការកំណត់បរិយាកាសផ្ទាល់ខ្លួន

```bash
# ការអភិវឌ្ឍន៍
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# ផលិតកម្ម (ប្រើការគ្រប់គ្រងអាថ៌កំបាំង)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## ឯកសារជំនួយ SDK

- **ឃ្លាំងសំខាន់**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **ឯកសាររបស់ API**: ពិនិត្យឃ្លាំង SDK សម្រាប់ផ្សេងៗថ្មីៗ

## ឯកសារជំនួយបន្ថែម

- `QUICK_START.md` - មគ្គុទេសក៍ចាប់ផ្តើម
- `Workshop/samples/*/README.md` - មគ្គុទេសក៍តាមគំរូពិសេស

---

**កំណែបំផុត**: 2025-01-08  
**កំណែ**: 2.0  
**SDK**: Foundry Local Python SDK (ថ្មីបំផុត)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើទោះបីយើងខិតខំធ្វើឱ្យបានត្រឹមត្រូវ ក៏ដោយ សូមកត់សម្គាល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការផ្លាស់ប្ដូរមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាបុរណ៍របស់វាគួរត្រូវបានចាត់ទុកជាឯកសារដើមដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរនាំមកនូវការបកប្រែដោយអ្នកជំនាញដែលជាសាច់ដុំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->