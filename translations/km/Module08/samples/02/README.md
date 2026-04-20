# ឧទាហរណ៍ 02: ការរួមបញ្ចូល OpenAI SDK

បង្ហាញពីការរួមបញ្ចូលជាច្រើនជាមួយ OpenAI Python SDK ដោយគាំទ្រទាំង Microsoft Foundry Local និង Azure OpenAI ជាមួយការផ្តល់ចម្លើយជាមុខងារស្ទ្រីម និងការដោះស្រាយកំហុសដែលត្រឹមត្រូវ។

## ទិដ្ឋភាពទូទៅ

ឧទាហរណ៍នេះបង្ហាញ៖
- ការផ្លាស់ប្ដូរយ៉ាងរលូនរវាង Foundry Local និង Azure OpenAI
- ការ​ផ្តល់​ចម្លើយ​សន្ទនា​ជា​ស្ទ្រីម​សម្រាប់បទពិសោធន៍អ្នកប្រើល្អប្រសើរ
- ការ​ប្រើប្រាស់ FoundryLocalManager SDK ដោយត្រឹមត្រូវ
- ការគ្រប់គ្រងកំហុសរឹងមាំ និងយន្តការវិលត្រឡប់
- គំរូកូដដែលមានស្រាប់សម្រាប់ផលិតកម្ម

## លក្ខខណ្ឌជាមុន

- **Foundry Local**: បានដំឡើង និងដំណើរការ (សម្រាប់ inference ដោយក្នុងស្រុក)
- **Python**: 3.8 ឬច្រើនជាងនេះ ជាមួយ OpenAI SDK
- **Azure OpenAI**: endpoint និង API key ត្រឹមត្រូវ (សម្រាប់ inference ពពក)

## Installation

1. **Set up Python environment:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local (for local mode):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Usage Scenarios

### Foundry Local (លំនាំដើម)

**ជម្រើស 1: ការប្រើ FoundryLocalManager (បានណែនាំ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ជម្រើស 2: ការកំណត់ដោយដៃ**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```

## រៀបចំកូដ

### គំរូរបស់ Client Factory

ឧទាហរណ៍នេះប្រើគំរូ factory ដើម្បីបង្កើត client ដែលសមរម្យ៖

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```

### ការ​ផ្តល់​ចម្លើយ​ជា​ស្ទ្រីម

ឧទាហរណ៍នេះបង្ហាញការស្ទ្រីមសម្រាប់ការបង្កើតចម្លើយពេលពិត៖

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## អថេរបរិស្ថាន

### ការកំណត់ Foundry Local

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MODEL` | អត្តនាមម៉ូដែលដែលត្រូវប្រើ | `phi-4-mini` | ទេ |
| `BASE_URL` | endpoint របស់ Foundry Local | `http://localhost:8000` | ទេ |
| `API_KEY` | កូនសោ API (ជាជម្រើសសម្រាប់ក្នុងស្រុក) | `""` | ទេ |

### ការកំណត់ Azure OpenAI

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | ចំណុចផ្តើមធនធាន Azure OpenAI | - | ចាំបាច់ |
| `AZURE_OPENAI_API_KEY` | កូនសោ API របស់ Azure OpenAI | - | ចាំបាច់ |
| `AZURE_OPENAI_API_VERSION` | កំណែ API | `2024-08-01-preview` | ទេ |
| `MODEL` | ឈ្មោះការដាក់ឱ្យដំណើរការរបស់ Azure | `your-deployment-name` | ចាំបាច់ |

## មុខងារខ្ពស់

### ការរកឃើញសេវាដោយស្វ័យប្រវត្តិ

ឧទាហរណ៍នេះគឺ​ស្វ័យគុណរកសេវាដែលសមរម្យ ដោយផ្អែកលើអថេរបរិស្ថាន៖

1. **ម៉ូដ Azure**: បើ `AZURE_OPENAI_ENDPOINT` និង `AZURE_OPENAI_API_KEY` ត្រូវបានកំណត់
2. **ម៉ូដ Foundry SDK**: បើ Foundry Local SDK មាន
3. **ម៉ូដដាក់ដៃ**: វិលត្រឡប់ទៅកាន់ការកំណត់ដោយដៃ

### ការដោះស្រាយកំហុស

- វិលត្រឡប់យ៉ាងស្រួលពី SDK ទៅការកំណត់ដោយដៃ
- សារ​កំហុស​ច្បាស់​សម្រាប់ការដោះស្រាយបញ្ហា
- ការកាន់កាប់ exception ដែលត្រឹមត្រូវសម្រាប់បញ្ហាបណ្តាញ
- ភាពត្រឹមត្រូវនៃអថេរបរិស្ថានដែលចាំបាច់

## ចំណុចពិចារណាផ្នែកប្រសិទិ្ធភាព

### ការប្រៀបធៀបទៅលើក្នុងស្រុក និងពពក

**អត្ថប្រយោជន៍ Foundry Local:**
- ✅ គ្មានការចំណាយ API
- ✅ សម្ងាត់ទិន្នន័យ (ទិន្នន័យមិនចាកចេញពីឧបករណ៍)
- ✅ ចម្លើយយឺតតិចសម្រាប់ម៉ូដែលដែលគាំទ្រ
- ✅ អាចធ្វើការ​ឡើងវិញដោយអនឡាញ

**អត្ថប្រយោជន៍ Azure OpenAI:**
- ✅ ចូលដំណើរការទៅម៉ូដែលធំចុងក្រោយ
- ✅ ថាមពល throughput ខ្ពស់
- ✅ មិនត្រូវការគណនា​ទីតាំងក្នុងស្រុក
- ✅ SLA ស្តង់ដារសម្រាប់សហគ្រាស

## ការដោះស្រាយបញ្ហា

### បញ្ហាទូទៅ

1. **"Could not use Foundry SDK" warning:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **កំហុសសៀងការផ្ទៀងផ្ទាត់ Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **ម៉ូដែលមិនមាន:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### ការត្រួតពិនិត្យសុខភាព

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## ជំហានបន្ទាប់

- **Sample 03**: ការស្វែងរកម៉ូដែល និងការវាស់ស្ទង់ប្រសិទ្ធភាព
- **Sample 04**: បង្កើតកម្មវិធី Chainlit RAG
- **Sample 05**: ការសម្របសម្រួលភ្នាក់ងារច្រើន
- **Sample 06**: ការបញ្ជូនដោយប្រើម៉ូឌែលជា​ឧបករណ៍

## ឯកសារ​យោង

- [ឯកសារណែនាំ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [ឯកសារណែនាំ OpenAI Python SDK](https://github.com/openai/openai-python)
- [មគ្គុទេសក៍ Streaming Completions](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**សេចក្តីប្រកាសបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានការខិតខំដើម្បីរក្សាការត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនត្រឹមត្រូវបានខ្លះ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកថា ជាប្រភពផ្លូវការទាំងស្រុង។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ យើងណែនាំឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->