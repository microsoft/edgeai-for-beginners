# Workshop Samples - ប័ណ្ណតំណាងយោងរហ័ស

**បន្ទាន់សម័យចុងក្រោយ**: តុលា 8, 2025

---

## 🚀 ចាប់ផ្តើមឆាប់

```bash
# 1. ប្រាកដថា Foundry Local កំពុងដំណើរការ
foundry service status
foundry model run phi-4-mini

# 2. តំឡើងការរាប់បញ្ចូល
pip install -r Workshop/requirements.txt

# 3. រត់គំរូមួយ
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 ទិដ្ឋភាពទូទៅនៃសំណុំឧទាហរណ៍

| វគ្គ | ឧទាហរណ៍ | គោលបំណង | ពេលវេលា |
|---------|--------|---------|------|
| 01 | `chat_bootstrap.py` | ការជជែកមូលដ្ឋាន + ចាក់បញ្ចាំង | ~30វិនាទី |
| 02 | `rag_pipeline.py` | RAG ជាមួយ embeddings | ~45វិនាទី |
| 02 | `rag_eval_ragas.py` | វាយតម្លៃ RAG | ~60វិនាទី |
| 03 | `benchmark_oss_models.py` | វាយតម្លៃម៉ូដែល | ~2 នាទី |
| 04 | `model_compare.py` | ប្រៀបធៀប SLM ជាមួយ LLM | ~45វិនាទី |
| 05 | `agents_orchestrator.py` | ប្រព័ន្ធភ្នាក់ងារច្រើន | ~60វិនាទី |
| 06 | `models_router.py` | បញ្ជូនបំណង | ~45វិនាទី |
| 06 | `models_pipeline.py` | បណ្តាញកាលបរិច្ឆេទច្រើនជំហាន | ~60វិនាទី |

---

## 🛠️ អថេរស្ថានីយ

### ជាទីបំផុត
```bash
# ជ្រើសម៉ូដែល
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# លុបផ្ទៃបង្ហាញរួច (ជាជម្រើស)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# បង្ហាញការប្រើប្រាស់សញ្ញាតវ៉ាន់
set SHOW_USAGE=1
```

### ជាពិសេសសម្រាប់វគ្គ
```bash
# អង្គភាព 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# អង្គភាព 03: ការប្រមូលផ្តុំ
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# អង្គភាព 04: ការប្រៀបធៀប
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# អង្គភាព 05: អ្នកតំណាង
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# អង្គភាព 06: បណ្ដាញបង្ហូរ
set PIPELINE_TASK="Your task here"
```

---

## ✅ ការផ្ទៀងផ្ទាត់ និង ការធ្វើតេស្ត

```bash
# ផ្ទៀងផ្ទាត់វេយ្យាករណ៍ និងការនាំចូល
python scripts/validate_samples.py

# ផ្ទៀងផ្ទាត់សម័យនិយមជាក់លាក់
python scripts/validate_samples.py --session 01

# រត់តេស្តម៉ូខ
python scripts/test_samples.py --quick

# ការធ្វើតេស្តលម្អិត
python scripts/test_samples.py --verbose
```

---

## 🐛 ការ​ដោះស្រាយ​បញ្ហា

### កំហុសភ្ជាប់
```bash
# ពិនិត្យ Foundry ទីលាន
foundry service status

# ចាប់ផ្តើម ប្រសិនបើចាំបាច់
foundry service start
foundry model run phi-4-mini
```

### កំហុសនាំចូល
```bash
# ដំឡើងការពឹងផ្អែកដែលខ្វះ
pip install sentence-transformers ragas datasets

# ឬដំឡើងទាំងអស់
pip install -r Workshop/requirements.txt
```

### មិនឃើញម៉ូដែល
```bash
# បញ្ជីម៉ូដែលដែលមាន
foundry model ls

# ទាញយកម៉ូដែល
foundry model download phi-4-mini
```

### ប្រតិបត្តិការយឺត
```bash
# ប្រើម៉ូដែលតូចជាងនេះ
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# កាត់បន្ថយវដ្តបញ្ជាក់សមត្ថភាព
set BENCH_ROUNDS=1
```

---

## 📖 លំនាំទូទៅ

### ជជែកមូលដ្ឋាន
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### ទទួលបានភ្ញៀវ
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # ស្វ័យប្រវត្តិ​រកឃើញ
)
```

### ការដោះស្រាយកំហុស
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ចាក់បញ្ចាំង
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 ជ្រើសរើសម៉ូដែល

| ម៉ូដែល | ទំហំ | ល្អសម្រាប់ | ល្បឿន |
|-------|------|----------|-------|
| `qwen2.5-0.5b` | 0.5B | ការរៀបចំប្រភេទលឿន | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | បង្កើតកូដឆាប់រហ័ស | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | សរសេរច្នៃប្រឌិត | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | កូដ, ការប្រែប្រួល | ⚡⚡ |
| `phi-4-mini` | 4B | ទូទៅ, សង្ខេប | ⚡⚡ |
| `qwen2.5-7b` | 7B | គំនិតស្មុគស្មាញ | ⚡ |

---

## 🔗 ធនធាន

- **អត្ថបទ SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **ការយោងរហ័ស**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 យោបល់

1. **ផ្ទុកភ្ញៀវចាំ**: `workshop_utils` ផ្ទុកសម្រាប់អ្នក
2. **ប្រើម៉ូដែលតូចជាង**: ចាប់ផ្តើមជាមួយ `qwen2.5-0.5b` សម្រាប់ការធ្វើតេស្ត
3. **បើកបង្ហាញស្ថិតិការប្រើប្រាស់**: កំណត់ `SHOW_USAGE=1` ដើម្បីតាមដាន token
4. **ដំណើរការជាក្រុម**: ដំណើរការប្រដាប់ផ្សេងៗតាមលំដាប់
5. **បន្ថយ max_tokens**: កាត់បន្ថយភាពយឺតសម្រាប់ការឆ្លើយតបលឿន

---

## 🎯 សំណុំដំណើរការ

### ពិនិត្យគ្រប់យ៉ាង
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### វាយតម្លៃម៉ូដែល
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### បណ្តាញ RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### ប្រព័ន្ធភ្នាក់ងារច្រើន
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**ជំនួយរហ័ស**: ប្រតិបត្តិឧទាហរណ៍ណាមួយជាមួយ `--help` ពីថត `samples` ឬពិនិត្យ docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**សំណុំឧទាហរណ៍ទាំងអស់បានបន្ទាន់សម័យខែតុលា 2025 ជាមួយនឹងអនុសាសន៍ល្អបំផុតនៃ Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពួកយើងខំប្រឹងប្រែងដើម្បីមានត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬមិនត្រឹមត្រូវ។ ឯកសារដើមដែលមានភាសាដើមគួរត្រូវបានគេយកជា ប្រភពយោងចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរតែប្រើការបកប្រែដោយអ្នកជំនាញ។ ពួកយើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->