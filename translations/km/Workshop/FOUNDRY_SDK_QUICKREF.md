# Foundry Local SDK - ឯកសារយោងរហ័ស

## ការដំឡើង

```bash
# ដំឡើង SDK
pip install foundry-local-sdk openai

# ដំឡើងសេវាកម្ម Foundry Local
# ប្រព័ន្ធប្រតិបត្តិការ Windows
winget install Microsoft.FoundryLocal

# ប្រព័ន្ធប្រតិបត្តិការ macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## ការគ្រប់គ្រងសេវាកម្ម

```bash
# ចាប់ផ្តើមសេវាកម្ម
foundry service start

# ពិនិត្យស្ថានភាព
foundry service status

# បញ្ឈប់សេវាកម្ម
foundry service stop

# បញ្ជីម៉ូដែល
foundry model ls

# ទាញយកម៉ូដែល
foundry model download phi-4-mini

# ទទួលព័ត៌មានម៉ូដែល
foundry model info phi-4-mini
```

## លំនាំការប្រើប្រាស់មូលដ្ឋាន

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# ចាប់ផ្តើមគ្រប់គ្រង (ចាប់ផ្តើមសេវាកម្មប្រសិនបើចាំបាច់)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# បង្កើតអតិថិជនដែលសមរម្យនឹង OpenAI
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# ទទួលបានលេខសម្គាល់ម៉ូដែល
model_id = manager.get_model_info(alias).id

# បញ្ចប់ការជជែកឆាត
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## ការឆ្លើយតបស្ទ្រីម

```python
stream = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## ឧបករណ៍កម្មវិធីរោងចក្រ (បានសម្រួល)

```python
from workshop_utils import chat_once

# ហៅតែមួយជាមួយការផ្ទុកក្នុងមេម៉ូរី និងការព្យាយាមម្ដងទៀត
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## អថេរសហគ្រាស

```python
import os

# បង្ហាញការប្រើប្រាស់សញ្ញាសម្គាល់
os.environ['SHOW_USAGE'] = '1'

# អនុញ្ញាតការព្យាយាមម្ដងទៀត
os.environ['RETRY_ON_FAIL'] = '1'

# កំណត់ពេលយឺតសម្រាប់ព្យាយាមម្ដងទៀត
os.environ['RETRY_BACKOFF'] = '2.0'

# ចំណុចចេញបញ្ជាក់បុគ្គលិក
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## ឈ្មោះរួមគំរូទូទៅ

| Alias | Size | Best For |
|-------|------|----------|
| `phi-4-mini` | ~4B | ទូទៅ, សង្ខេប |
| `phi-3.5-mini` | ~3.5B | កូដ, ដំណែលវិញ |
| `qwen2.5-0.5b` | ~0.5B | ចំណាត់ថ្នាក់រហ័ស |
| `qwen2.5-coder-0.5b` | ~0.5B | បង្កើតកូដ |
| `gemma-2b` | ~2B | សរសេរច្នៃប្រឌិត |

## ការដោះស្រាយកំហុស

```python
from openai import OpenAIError

try:
    text, usage = chat_once('phi-4-mini', messages=[...])
except RuntimeError as e:
    print(f"Manager initialization failed: {e}")
    print("Check: foundry service status")
except OpenAIError as e:
    print(f"API call failed: {e}")
    print("Check: foundry model ls")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## ការដោះស្រាយបញ្ហា

### កំហុសការតភ្ជាប់
```bash
# ពិនិត្យសេវាកម្ម
foundry service status

# ចាប់ផ្តើមឡើងវិញ
foundry service stop
foundry service start

# សាកល្បងចំណុចបញ្ចបាជើង
curl http://localhost:55769/health
```

### មិនរកឃើញគំរូ
```bash
# បញ្ជីដែលមានស្រាប់
foundry model ls

# ទាញយកបើចាំបាច់
foundry model download phi-4-mini
```

### កំហុសនាំចូល
```bash
# ដំឡើង SDKឡើងវិញ
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## ជំហានខ្ពស់៖ គំរូច្រើន

```python
from workshop_utils import get_client

# កំណត់ម៉ូដែលច្រើនមុខ
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# ប្រើម៉ូដែលផ្សេងៗ
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## គន្លឹះបង្កើតប្រសិទ្ធិភាព

1. **ផ្ទុកទុកអតិថិជន**: ប្រើម៉ូឌែល `FoundryLocalManager` ម្តងហើយប្រើឡើងវិញ
2. **បញ្ចូលការស្នើសុំជាច្រើនជាក្រុម**: ឆ្លើយតបសំណូមពរជាច្រើនជាដំណាក់កាល
3. **កំណត់ max_tokens**: តម្លៃទាប=ឆ្លើយតបរហ័ស
4. **ផ្ទុកគំរូរួចមុន**: ទាញយកមុនប្រើប្រាស់ក្នុងផលិតកម្ម
5. **តាមដានការប្រើប្រាស់**: តាមដានតុកិនជាមួយ `SHOW_USAGE=1`

## ធនធាន

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **បញ្ហា**: https://github.com/microsoft/Foundry-Local/issues

---

**ចាប់ផ្ដើមរហ័ស៖**
```bash
# ដំឡើងទាំងអស់
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# ចាប់ផ្តើមសេវាកម្ម
foundry service start

# សាកល្បងក្នុង Python
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ប៉ុន្តែមិនថា​យើង​ព្យាយាម​ធ្វើ​ឲ្យ​មានភាព​ត្រឹមត្រូវ​ច្រើន​ប៉ុណ្ណា ទុក​ចិត្ត​ថា​ការបកប្រែ​ដោយ​ស្វ័យប្រវត្តិ​អាច​មាន​កំហុស ឬ​អភាព​ត្រឹមត្រូវ​មួយចំនួន។ ឯកសារដើមក្នុងភាសាតំបន់របស់ខ្លួនគួរត្រូវបានពិចារណាថាជា​អ្នក​ផ្តល់​ព័ត៌មាន​ដែលមានសុពលភាព។ សម្រាប់ព័ត៌មាន​សំខាន់ៗ ការបកប្រែ​ដោយអ្នកជំនាញ​មនុស្ស​ត្រូវ​បានផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំពីតម្លើងផ្សេងៗ ឬការបញ្ជេញចេញពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->