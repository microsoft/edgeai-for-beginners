# Foundry Local ជា ឧទាហរណ៍ API

ឧទាហរណ៍នេះបង្ហាញពីរបៀបប្រើ Microsoft Foundry Local ជាសេវា REST API ដោយមិនផ្អែកលើយាន OpenAI SDK។ វាបង្ហាញគំរូសម្រាប់ការតភ្ជាប់ HTTP ដោយផ្ទាល់សម្រាប់ការគ្រប់គ្រង និងការកែតម្រូវឲ្យបានអតិបរមា។

## ទិដ្ឋភាពទូទៅ

យោងទៅតាមគំរូផ្លូវការរបស់ Microsoft សម្រាប់ Foundry Local, ឧទាហរណ៍នេះផ្តល់នូវ:
- ការតភ្ជាប់ REST API ដោយផ្ទាល់ ជាមួយ FoundryLocalManager
- ការអនុវត្ត​អតិថិជន HTTP ផ្ទាល់ខ្លួន
- ការគ្រប់គ្រងម៉ូឌែល និងការតាមដានសុខភាព
- ការដោះស្រាយចម្លើយទាំងទ្រង់ទ្រាយស្ទ្រីម និងអត់ស្ទ្រីម
- ការគ្រប់គ្រងកំហុស និងយុទ្ធសាស្រ្តព្យាយាមឡើងវិញដែលរួចរាល់សម្រាប់ផលិតកម្ម

## តម.requirementsមុន

1. **ការដំឡើង Foundry Local**
   ```powershell
   # ដំឡើងពីការចេញផ្សាយលើ GitHub
   winget install Microsoft.FoundryLocal
   ```

2. **ការ​ពឹងផ្អែក Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## ស្ថាបត្យកម្ម

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## លក្ខណៈពិសេសសំខាន់

### 1. **ការតភ្ជាប់ HTTP ដោយផ្ទាល់**
- ការហៅ REST API ដោយសុទ្ធ ដោយមិនពឹងផ្អែកលើយាន SDK
- ការផ្ទៀងផ្ទាត់ និង headers ផ្ទាល់ខ្លួន
- ការគ្រប់គ្រងពេញលេញលើការដោះស្រាយសំណើ/ចម្លើយ

### 2. **ការគ្រប់គ្រងម៉ូឌែល**
- ការផ្ទុក និងដោះបញ្ចេញម៉ូឌែលយ៉ាងឌីណាមិច
- ការតាមដានសុខភាព និងពិនិត្យស្ថានភាព
- ការប្រមូលមាត្រដ្ឋានសមត្ថភាព

### 3. **គំរូសម្រាប់ផលិតកម្ម**
- មេកានីស៊ីមព្យាយាមឡើងវិញជាមួយការពន្យារពេល exponential backoff
- Circuit breaker សម្រាប់ធន់ទ្រាំកំហុស
- ការចុះបញ្ជី និងតាមដានដ៏ទូលំទូលាយ

### 4. **ការដោះស្រាយចម្លើយដែលអាចបត់បែនបាន**
- ចម្លើយស្ទ្រីមសម្រាប់កម្មវិធីពេលពិត
- ដំណើរការប្លុកសម្រាប់លក្ខខណ្ឌដែលមាន throughput ខ្ពស់
- ការបំបែកចម្លើយ និងបញ្ជាក់ភាពត្រឹមត្រូវផ្ទាល់ខ្លួន

## ឧទាហរណ៍ការប្រើប្រាស់

### ការតភ្ជាប់ API មូលដ្ឋាន
```python
from api_client import FoundryAPIClient

# ចាប់ផ្តើមអតិថិជន API
client = FoundryAPIClient()

# ការបញ្ចប់សាមញ្ញ
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### ការតភ្ជាប់ស្ទ្រីម
```python
# ផ្តល់ចម្លើយជាស្ទ្រីមសម្រាប់កម្មវិធីពេលពិត
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### ការតាមដានសុខភាព
```python
# ពិនិត្យសុខភាពសេវាកម្ម
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## រចនាសម្ព័ន្ធ​ឯកសារ

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## ការរួមបញ្ចូល Microsoft Foundry Local

ឧទាហរណ៍នេះអនុវត្តតាមគំរូផ្លូវការរបស់ Microsoft៖

1. **ការរួមបញ្ចូល SDK**: ប្រើ `FoundryLocalManager` សម្រាប់ការគ្រប់គ្រងសេវា
2. **REST Endpoints**: ហៅដោយផ្ទាល់ទៅកាន់ `/v1/chat/completions` និង endpoints ផ្សេងទៀត
3. **Authentication**: ការដោះស្រាយកូនសោ API ដោយត្រឹមត្រូវសម្រាប់សេវាកម្មក្នុងប្រព័ន្ធ
4. **Model Management**: ការចាប់បញ្ជីកាតាឡុក, ការទាញយក និងគំរូការផ្ទុក
5. **Error Handling**: កូដកំហុស និងចម្លើយដែល Microsoft ណែនាំ

## ចាប់ផ្តើម

1. **ដំឡើងការ​ពឹងផ្អែក**
   ```bash
   pip install -r requirements.txt
   ```

2. **រត់ឧទាហរណ៍មូលដ្ឋាន**
   ```bash
   python examples/basic_usage.py
   ```

3. **សាកល្បងស្ទ្រីម**
   ```bash
   python examples/streaming.py
   ```

4. **ការកំណត់សម្រាប់ផលិតកម្ម**
   ```bash
   python examples/production.py
   ```

## ការកំណត់

អថេរស្ថានបរិយាកាសសម្រាប់ការប្តូរតាមចំណង់ចំណូលចិត្ត៖
- `FOUNDRY_MODEL`: ម៉ូឌែលលំនាំដើមសម្រាប់ប្រើ (default: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: ពេលកំណត់ស្នើសុំជា វិនាទី (default: 30)
- `FOUNDRY_RETRIES`: ចំនួនព្យាយាមឡើងវិញ (default: 3)
- `FOUNDRY_LOG_LEVEL`: កម្រិតកំណត់ហេតុ (default: "INFO")

## គន្លឹះអនុវត្តល្អបំផុត

1. **ការគ្រប់គ្រងការតភ្ជាប់**: ប្រើការតភ្ជាប់ HTTP ម្តងទៀតសម្រាប់ប្រសិទ្ធភាពកាន់តែប្រសើរ
2. **ការគ្រប់គ្រងកំហុស**: អនុវត្តយុទ្ធសាស្រ្តព្យាយាមឡើងវិញដោយត្រឹមត្រូវជាមួយ exponential backoff
3. **ការតាមដានធនធាន**: តាមដានការប្រើប្រាស់ចងចាំម៉ូឌែល និងសមត្ថភាព
4. **សុវត្ថិភាព**: ប្រើការផ្ទៀងផ្ទាត់យ៉ាងត្រឹមត្រូវ ទោះបីសម្រាប់សេវាកម្មក្នុងស្រុកក៏ដោយ
5. **ការ​តេស្ត**: រួមបញ្ចូលទាំងការធ្វើតេស្តឯកត្តា និងការធ្វើតេស្តការរួមបញ្ចូល

## ការដោះស្រាយបញ្ហា

### បញ្ហាសម្គាល់ទូទៅ

**សេវាកម្ម​មិនកំពុងដំណើរការ**
```bash
# ពិនិត្យស្ថានភាព Foundry Local
foundry status

# ចាប់ផ្តើម ប្រសិនបើចាំបាច់
foundry start
```

**បញ្ហាក្នុងការផ្ទុកម៉ូឌែល**
```bash
# បញ្ជីម៉ូឌែលដែលអាចប្រើបាន
foundry model list

# ទាញយកម៉ូឌែលជាក់លាក់
foundry model download phi-4-mini
```

**កំហុសការតភ្ជាប់**
- ត្រួតពិនិត្យថា Foundry Local កំពុងដំណើរការ​នៅលើច្រក (port) ដែលត្រឹមត្រូវ
- ពិនិត្យការកំណត់ firewall
- ធានាថាមាន headers ផ្ទៀងផ្ទាត់ដែលត្រឹមត្រូវ

## ការបង្កើនសមិទ្ធភាព

1. **Connection Pooling**: ប្រើ session objects សម្រាប់សំណើជាច្រើន
2. **Async Operations**: ប្រើ asyncio សម្រាប់សំណើដំណើរការជាបន្ត
3. **Caching**: ការកែចាំចម្លើយម៉ូឌែលនៅកន្លែងដែលសមស្រប
4. **Monitoring**: តាមដានពេលឆ្លើយតប ហើយកែប្រែពេលកំណត់ (timeouts)

## លទ្ធផលនៃការរៀន

បន្ទាប់ពីបញ្ចប់ឧទាហរណ៍នេះ អ្នកនឹងយល់ដឹងអំពី៖
- ការតភ្ជាប់ REST API ដោយផ្ទាល់ជាមួយ Foundry Local
- គំរូអនុវត្តអតិថិជន HTTP ផ្ទាល់ខ្លួន
- ការគ្រប់គ្រងកំហុស និងការតាមដានដែលរួចរាល់សម្រាប់ផលិតកម្ម
- ស្ថាបត្យកម្មសេវា Microsoft Foundry Local
- វិធីសាស្ត្របង្កើនសមិទ្ធភាពសម្រាប់សេវា AI ក្នុងស្រុក

## ជំហានបន្ទាប់

- ស្វែងយល់អំពី ឧទាហរណ៍ 08: Windows 11 Chat Application
- សាកល្បង ឧទាហរណ៍ 09: Multi-Agent Orchestration
- រៀន ឧទាហរណ៍ 10: Foundry Local ជាការរួមបញ្ចូលជាមួយ Tools

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារ​នេះ​ត្រូវបាន​បកប្រែ​ដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះបីយើងខិតខំរក្សាភាពត្រឹមត្រូវក៏ដោយ សូមយល់ព្រមថា ការបកប្រែដោយស្វ័យប្រវត្តิអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើម​ក្នុងភាសាដើមរបស់វា គួរត្រូវបានចាត់ទុកថាជាប្រភពផ្តាច់មុខ។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឲ្យប្រើការបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកអត្ថន័យខុសដែលអាចកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->