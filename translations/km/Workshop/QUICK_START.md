# មេរៀនជំហានលឿនសម្រាប់សិក្ខាសាលា

## លក្ខខណ្ឌមុនបំពេញតម្រូវការ

### 1. តម្លើង Foundry Local

ធ្វើតាមមគ្គុទេសក៍តម្លើងផ្លូវការនេះ៖
https://github.com/microsoft/Foundry-Local

```bash
# ចាប់ផ្តើមសេវាកម្ម Foundry Local
foundry service start

# បន្ទាប់ម៉ូដែលមួយ (phi-4-mini គឺផ្តល់អនុសាសន៍សម្រាប់ការសិក្ខាសាលា)
foundry model run phi-4-mini

# ផ្ទៀងផ្ទាត់ថាសេវាកម្មកំពុងដំណើរការ
foundry service status
```

### 2. តម្លើងឧបករណ៍ Python ដែលតម្រូវការ

ពីថតសិក្ខាសាលា៖

```bash
# បង្កើតបរិយាកាសវីជ្ស៊ល (ផ្ដាច់មុខแนะนำ)
python -m venv .venv

# បញ្ចូលបរិយាកាសវីជ្ស៊ល
# វីនដូ:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# ដំឡើងតម្រូវការ
pip install -r requirements.txt
```

## រត់គំរូក្នុងសិក្ខាសាលា

### ព្រឹត្តិការណ៍ 01៖ ការសន្ទនាមូលដ្ឋាន

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**អថេរក្នុងបរិយាកាសៈ**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### ព្រឹត្តិការណ៍ 02៖ ផ្លូវដើម RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**អថេរក្នុងបរិយាកាសៈ**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### ព្រឹត្តិការណ៍ 02៖ ការវាយតម្លៃ RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**ចំណាំ**៖ តម្រូវឧបករណ៍បន្ថែមដែលត្រូវបានដំឡើងតាម `requirements.txt`

### ព្រឹត្តិការណ៍ 03៖ ការវាស់ប្រសិទ្ធភាព

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**អថេរក្នុងបរិយាកាសៈ**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**លទ្ធផល**៖ JSON ជាមួយគុណភាពយឺត និងល្បឿន និងខ្សែដើម Token

### ព្រឹត្តិការណ៍ 04៖ ការប្រៀបធៀបម៉ូដែល

```bash
cd Workshop/samples
python -m session04.model_compare
```

**អថេរក្នុងបរិយាកាសៈ**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### ព្រឹត្តិការណ៍ 05៖ ការគ្រប់គ្រង Multi-Agent

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**អថេរក្នុងបរិយាកាសៈ**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### ព្រឹត្តិការណ៍ 06៖ ភ្នាក់ងារម៉ូដែល

```bash
cd Workshop/samples
python -m session06.models_router
```

**សាកល្បងตรรกะការបញ្ជូន** ជាមួយចេតនាច្រើន (កូដ, សង្ខេប, ចំណាត់ថ្នាក់)

### ព្រឹត្តិការណ៍ 06៖ ផ្លូវដើម Pipeline

```bash
python -m session06.models_pipeline
```

**ផ្លូវដើមច្រើនជំហានស្មុគស្មាញ** ជាមួយផែនការ, ចាត់ការ និងកែតម្រូវ

## ស្គ្រីប

### នាំចេញរបាយការណ៍វាស់ប្រសិទ្ធភាព

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**លទ្ធផល**៖ តារាង Markdown + វិមាត្រ JSON

### ตรวจสอบម៉ូដែល Markdown CLI Patterns

```bash
python lint_markdown_cli.py --verbose
```

**គោលបំណង**៖ រកឃើញគំរូ CLI ដែលត្រូវបោះបង់ក្នុងឯកសារយោង

## ការធ្វើតេស្ត

### តេស្ត Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**តេស្ត**៖ មុខងារជាថ្មីនៃគំរូសំខាន់ៗ

## ដោះស្រាយបញ្ហា

### សេវាកម្មមិនដំណើរការ

```bash
# ពិនិត្យស្ថានភាព
foundry service status

# ចាប់ផ្តើមបើមិនដំណើរការ
foundry service start

# ផ្ទុកម៉ូដែលមួយ
foundry model run phi-4-mini
```

### បញ្ហាក្នុងការនាំចូលម៉ូឌុល

```bash
# ប្រាកដថាបរិយាកាសវីរុអែលត្រូវបានបើកដំណើរការ
.venv\Scripts\activate  # វីនដូស
source .venv/bin/activate  # ម៉ាក់អូអេស/លីនុច

# ដំឡើងម្ដងទៀតឯកសារជំនួយ
pip install -r requirements.txt
```

### បញ្ហាការតភ្ជាប់

```bash
# ពិនិត្យមើលចំណុចបញ្ចប់
foundry service status

# កំណត់ចំណុចបញ្ចប់បញ្ជាក់ប្រសិនបើត្រូវការ
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### ម៉ូដែលមិនមាន

```bash
# បញ្ជីម៉ូដែលដែលមាន
foundry model list

# ទាញយក និងបើកដំណើរការ​ម៉ូដែល​មួយ
foundry model run phi-4-mini
```

## ឯកសារអថេរក្នុងបរិយាកាស

### កំណត់រចនាសម្ព័ន្ធចំបង
| អថេរ | តម្លៃដើម | សេចក្ដីបរិច្ឆេទ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | ផ្លាស់ប្ដូរ | ឈ្មោះបម្រាមម៉ូដែលដែលត្រូវប្រើ |
| `FOUNDRY_LOCAL_ENDPOINT` | ស្វ័យប្រវត្តិ | ជំនួសចំណុចបញ្ជូនសេវា |
| `SHOW_USAGE` | `0` | បង្ហាញស្ថិតិការប្រើប្រាស់ Token |
| `RETRY_ON_FAIL` | `1` | បើកបញ្ញា retry នៅពេលខ្វះខាត |
| `RETRY_BACKOFF` | `1.0` | ពេលយឺតចាប់ផ្តើម retry (វិនាទី) |

### សម្រាប់ព្រឹត្តិការណ៍ជាក់លាក់
| អថេរ | តម្លៃដើម | សេចក្ដីបរិច្ឆេទ |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ម៉ូដែលបង្កើត embedding |
| `RAG_QUESTION` | វាដូចគំរូ | សំនួរប្រភេទ RAG |
| `BENCH_MODELS` | ផ្លាស់ប្ដូរ | ម៉ូដែលបំបែកជាសញ្ញាក្បៀស |
| `BENCH_ROUNDS` | `3` | ចំនួនសាកល្បងវាស់ប្រសិទ្ធភាព |
| `BENCH_PROMPT` | វាដូចគំរូ | សំណើវាស់ប្រសិទ្ធភាព |
| `BENCH_STREAM` | `0` | វាស់ស្ទាត់ភាពយឺតនៃ token ដើម |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ម៉ូដែលភ្នាក់ងារចម្បង |
| `AGENT_MODEL_EDITOR` | ភ្នាក់ងារចម្បង | ម៉ូដែលភ្នាក់ងារកែសម្រួល |
| `SLM_ALIAS` | `phi-4-mini` | ម៉ូដែលភាសាខ្នាតតូច |
| `LLM_ALIAS` | `qwen2.5-7b` | ម៉ូដែលភាសាខ្នាតធំ |
| `COMPARE_PROMPT` | វាដូចគំរូ | សំណើប្រៀបធៀប |

## ម៉ូដែលដែលផ្ដល់អនុសាសន៍

### ការអភិវឌ្ឍន៍ និងធ្វើតេស្ត
- **phi-4-mini** - សមភាពគុណភាពនិងល្បឿនជាប្រក្រតី
- **qwen2.5-0.5b** - ល្បឿនលឿនសម្រាប់ចំណាត់ថ្នាក់
- **gemma-2-2b** - គុណភាពល្អ និងល្បឿនចម moderation

### ព្រឹត្តិការណ៍ផលិតកម្ម
- **phi-4-mini** - គោលបំណងទូទៅ
- **deepseek-coder-1.3b** - ការបង្កើតកូដ
- **qwen2.5-7b** - ចម្លើយមានគុណភាពខ្ពស់

## ឯកសារ SDK

- **Foundry Local**៖ https://github.com/microsoft/Foundry-Local
- **Python SDK**៖ https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## រកជំនួយ

1. ពិនិត្យស្ថានភាពសេវា៖ `foundry service status`
2. ចូលមើលកំណត់ហេតុ៖ ពិនិត្យកំណត់ហេតុសេវា Foundry Local
3. ពិនិត្យឯកសារ SDK៖ https://github.com/microsoft/Foundry-Local
4. អានគំរូកូដ៖ គំរូទាំងអស់មានពិពណ៌នាពីអត្ថន័យ

## ជំហានបន្ទាប់

1. បញ្ចប់វគ្គសិក្ខាសាលាទាំងអស់ដោយលំដាប់
2. សាកល្បងម៉ូដែលផ្សេងៗគ្នា
3. កែប្រែគំរូសម្រាប់ករណីប្រើប្រាស់របស់អ្នក

---

**បច្ចុប្បន្នភាពចុងក្រោយ**៖ 2025-01-08  
**កំណែសិក្ខាសាលា**៖ ថ្មីបំផុត  
**SDK**៖ Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator) ។ បើទោះបីជាយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ ប៉ុន្តែសូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិក៏អាចមានកំហុស ឬការមិនត្រឹមត្រូវខ្លះៗ។ ឯកសារដើមជាភាសាតម្កល់បណ្តឹងគួរត្រូវបានគេយកជារូបមន្តសំខាន់។ សម្រាប់ព័ត៌មានសំខាន់ៗ មនុស្សជំនាញបកប្រែដោយព្រមព្រៀងគឺត្រូវបានផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកស្រាយខុសខាតណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->