# Session 6 គំរូ: ម៉ូឌែលជាឧបករណ៍

គំរូនេះ អនុវត្ត router តិចតួច និងបញ្ជីឧបករណ៍ ដែលជ្រើសម៉ូឌែលដោយផ្អែកលើសំណើរអ្នកប្រើ ហើយហៅ endpoint របស់ Foundry Local ដែលឆបគ្នានឹង OpenAI។

## ឯកសារ
- `router.py`: បញ្ជីសាមញ្ញ និងការបង្វិលដោយ heuristic; ការរកឃើញ endpoint + ការត្រួតពិនិត្យសុខភាព។

## រត់ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## កំណត់ចំណាំ
- router ប្រើ heuristic ពាក្យគន្លឹះសាមញ្ញ ដើម្បីជ្រើសរើសរវាងឧបករណ៍ `general`, `reasoning`, និង `code` ហើយបោះពុម្ព `/v1/models` នៅពេលចាប់ផ្តើម។
- កំណត់តម្លៃតាមអថេរបរិយាកាស:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## យោង
- Foundry Local (រៀន): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- រួមបញ្ចូលជាមួយ inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកថាជាប្រភពយោងដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ យើងផ្ដល់អនុសាសន៍ឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->