# Foundry Local នៅលើ Windows និង Mac

មាគ៌ានេះជួយអ្នកដំឡើង រត់ និងរួមបញ្ចូល Microsoft Foundry Local នៅលើ Windows និង Mac។ ជំហាន និងសេចក្ដីបញ្ជារទាំងអស់ត្រូវបានអះអាងដោយឯកសារ Microsoft Learn។

- ចាប់ផ្ដើម៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- សំណង់រចនាសម្ព័ន្ធ៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- ឯកសារយោង CLI៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- រួមបញ្ចូល SDK៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- សង្កត់ម៉ូដែល HF (BYOM)៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI៖ មូលដ្ឋាន​ទិន្នន័យ​តាមក្នុងម៉ាស៊ីន​បង្ហាញ​ប្រអប់​ចំហរ​ជាមួយពពក៖ https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) ដំឡើង / ធ្វើបច្ចុប្បន្នភាពលើ Windows

- ដំឡើង៖
```cmd
winget install Microsoft.FoundryLocal
```
- ធ្វើបច្ចុប្បន្នភាព៖
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ពិនិត្យកំណែ៖
```cmd
foundry --version
```
     
**ដំឡើង / Mac**

**MacOS**:  
បើក terminal ហើយរត់ពាក្យបញ្ជាខាងក្រោម៖
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) មូលដ្ឋាន CLI (ប្រាំបីប្រភេទ)

- ម៉ូដែល៖
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- សេវាកម្ម៖
```cmd
foundry service --help
foundry service status
foundry service ps
```
- ការផ្ទុក៖
```cmd
foundry cache --help
foundry cache list
```

កំណត់សម្គាល់៖
- សេវាកម្មបង្ហាញ API REST ដែលឆ្លុះបញ្ចាំងភាពផ្គូរផ្គង OpenAI។ ច្រកទ្វារស្វ័យប្រវត្តិកំណត់; ប្រើ `foundry service status` ដើម្បីស្វែងរកវា។
- ប្រើ SDKs ដើម្បីងាយស្រួល; ពួកវាអនុវត្តស្វែងរកច្រកទ្វារដោយស្វ័យប្រវត្តិពេលដែលគាំទ្រ។

## 3) ស្វែងរកច្រកទ្វារផ្ទាល់ម៉ាស៊ីន (ច្រកចល័ត)

Foundry Local ផ្ដល់ច្រកទ្វារចល័តរាល់ពេលសេវាកម្មចាប់ផ្ដើម៖
```cmd
foundry service status
```
ប្រើ `http://localhost:<PORT>` ដែលរាយការណ៍ជារូបមន្ត `base_url` របស់អ្នកជាមួយផ្លូវដែលផ្គូរផ្គង OpenAI (ឧទាហរណ៍, `/v1/chat/completions`)។

## 4) សាកល្បងរហ័សតាម SDK Python OpenAI

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
យោង៖
- រួមបញ្ចូល SDKៈ https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) នាំម៉ូដែលរបស់អ្នកមកផ្ទាល់ (បង្កCompilationជាមួយ Olive)

បើអ្នកត្រូវការម៉ូដែលដែលមិនមាននៅក្នុងកាតាឡុក បង្កCompilationវាទៅ ONNX សម្រាប់ Foundry Local ដោយប្រើ Olive។

ដំណើរការកម្រិតខ្ពស់ (មើលឯកសារសម្រាប់ជំហាន)៖
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ឯកសារ៖
- BYOM compilation៖ https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) ដោះស្រាយបញ្ហា

- ពិនិត្យស្ថានភាពសេវាកម្ម និងកំណត់ហេតុ៖
```cmd
foundry service status
foundry service diag
```
- សម្អាត ឬផ្លាស់ទីការផ្ទុក៖
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- ធ្វើបច្ចុប្បន្នភាពទៅមើលជាមុនបំផុត៖
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) បទពិសោធន៍អ្នកអភិវឌ្ឍន៍ Windows ទាក់ទង

- ជម្រើស AI ផ្ទាល់ក្នុងម៉ាស៊ីនត versus ពពកនៅ Windows រួមមាន Foundry Local និង Windows ML៖
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit ជាមួយ Foundry Local (ប្រើ `foundry service status` ដើម្បីទទួល URL ច្រកការជជែក)៖
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[អ្នកអភិវឌ្ឍន៍ Windows បន្ទាប់](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator) ។ ខណៈពេលដែលយើងខិតខំដើម្បីបានភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនច្បាស់លាស់។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានគេពិចារណាជាអ្នកផ្គត់ផ្គង់ព័ត៌មានផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងផ្តល់អនុសាសន៍ឲ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->