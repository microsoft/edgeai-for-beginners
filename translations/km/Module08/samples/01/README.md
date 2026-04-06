# ឧទាហរណ៍ 01: ការជជែករហ័សតាមរយៈ OpenAI SDK

ឧទាហរណ៍សាមញ្ញមួយបង្ហាញពីរបៀបប្រើ OpenAI SDK ជាមួយ Microsoft Foundry Local សម្រាប់ការសន្មត់ AI ក្នុងស្រុក។

## ទិដ្ឋភាពទូទៅ

ឧទាហរណ៍នេះបង្ហាញពីរបៀប:
- ប្រើ OpenAI Python SDK ជាមួយ Foundry Local
- ដោះស្រាយការកំណត់ទាំង Azure OpenAI និង ការកំណត់ Foundry ក្នុងស្រុក
- អនុវត្តការគ្រប់គ្រងកំហុស និងយុទ្ធសាស្ត្រការធ្លាក់ចុះ
- ប្រើ FoundryLocalManager សម្រាប់ការគ្រប់គ្រងសេវា

## តម្រូវការមុន

- **Foundry Local**: ត្រូវបានតំឡើង និងអាចប្រើបានលើ PATH
- **Python**: 3.8 ឬក្រោយពីនេះ
- **Model**: ម៉ូឌែលមួយដែលបានដុញក្នុង Foundry Local (ឧ. `phi-4-mini`)

## ការតំឡើង

1. **តំឡើងបរិយាកាស Python:**  
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **តំឡើងឧបករណ៍អាស្រ័យភាព:**  
   ```cmd
   pip install -r requirements.txt
   ```

3. **ចាប់ផ្តើមសេវាកម្ម Foundry Local និងដាក់ម៉ូឌែលមួយ:**  
   ```cmd
   foundry model run phi-4-mini
   ```

## ការប្រើប្រាស់

### Foundry Local (លំនាំដើម)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## លក្ខណៈពិសេសកូដ

### ការរួមបញ្ចូល FoundryLocalManager

ឧទាហរណ៍នេះប្រើ Foundry Local SDK ផ្លូវការសម្រាប់ការគ្រប់គ្រងសេវាកម្មយ៉ាងត្រឹមត្រូវ៖

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ចាប់ផ្ដើម Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# កំណត់រចនាសម្ព័ន្ធកម្មវិធីអតិថិជន OpenAI
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### ការគ្រប់គ្រងកំហុស

ការគ្រប់គ្រងកំហុសរឹងមាំជាមួយការធ្លាក់ចុះទៅកាន់ការកំណត់ដោយដៃ:
- ការស្វែងរកសេវាកម្មដោយស្វ័យប្រវត្តិ
- ការធ្លាក់ចុះយ៉ាងស្ងប់ស្ងាត់ ប្រសិនបើ SDK មិនអាចប្រើបាន
- សារកំហុសដែលច្បាស់លាស់សម្រាប់ដោះស្រាយបញ្ហា

## អថេរ​បរិយាកាស

| អថេរ | ពណ៌នា | លំនាំដើម | ចាំបាច់ |
|----------|-------------|---------|----------|
| `MODEL` | ឈ្មោះឬឈ្មោះរងរបស់ម៉ូឌែល | `phi-4-mini` | ទេ |
| `BASE_URL` | Foundry Local base URL | `http://localhost:8000` | ទេ |
| `API_KEY` | កូនសោ API (ធម្មតាមិនចាំបាច់សម្រាប់ក្នុងស្រុក) | `""` | ទេ |
| `AZURE_OPENAI_ENDPOINT` | ចំណុចចប់ Azure OpenAI | - | សម្រាប់ Azure |
| `AZURE_OPENAI_API_KEY` | កូនសោ API របស់ Azure OpenAI | - | សម្រាប់ Azure |
| `AZURE_OPENAI_API_VERSION` | កំណែ API របស់ Azure | `2024-08-01-preview` | ទេ |

## ការដោះស្រាយបញ្ហា

### បញ្ហាទូទៅ

1. **"មិនអាចប្រើ Foundry SDK" ការព្រមាន:**
   - តំឡើង foundry-local-sdk: `pip install foundry-local-sdk`
   - ឬកំណត់អថេរបរិយាកាសសម្រាប់ការកំណត់ដោយដៃ

2. **ការ​តភ្ជាប់​ត្រូវបាន​បដិសេធ:**
   - ធានាថា Foundry Local កំពុងដំណើរការ: `foundry service status`
   - ពិនិត្យមើលថាតើមានម៉ូឌែលត្រូវបានដឹកឡើងឬទេ: `foundry service ps`

3. **រកមិនឃើញម៉ូឌែល:**
   - បញ្ជីម៉ូឌែលដែលមាន: `foundry model list`
   - ដង្កើត/ដាក់ម៉ូឌែល: `foundry model run phi-4-mini`

### ការផ្ទៀងផ្ទាត់

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## ឯកសារ​យោង

- [ឯកសារ Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [យោងអំពី API ស្របនឹង OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខំប្រឹងសម្រាប់ភាពត្រឹមត្រូវក៏ដោយ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកថាជាប្រភពដែលអាចយោងបាន។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ ពិចារណាការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយមិនត្រឹមត្រូវណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->