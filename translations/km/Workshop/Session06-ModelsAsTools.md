# សម័យទី ៦៖ Foundry ស្រុកខ្លួន – ម៉ូដែលជាឧបករណ៍

## សង្ខេប

ចាត់ទុកម៉ូដែលជាឧបករណ៍ដែលអាចប្រើរួមគ្នា ក្នុងសត្រង់សកម្មភាព AI ស្រុកខ្លួនមួយ។ សម័យនេះបង្ហាញពីរបៀបភ្ជាប់ការហៅ SLM/LLM ជាច្រើនដែលមានជំនាញជាក់លាក់, ការបញ្ជូនភារកិច្ចជ្រើសរើស, និងការបង្ហាញផ្ទៃ SDK រួមមួយទៅកាន់កម្មវិធី។ អ្នកនឹងបង្កើតមួយម៉ូដែលដែលមានភាពស្រាលស្រួលជាមួយអ្នកចំណាត់ថ្នាក់ភារកិច្ច, រួមបញ្ចូលវាទៅក្នុងស្គ្រីបកម្មវិធីមួយ, ហើយរៀបរាប់ផ្លូវតម្រុយបន្ដទៅកាន់ Azure AI Foundry សម្រាប់ភារកិច្ចផលិតកម្ម។

## គោលបំណងការសិក្សា

- **គំនិត** មើលម៉ូដែលជាឧបករណ៍អាតូមប៉ុន្មាន ដែលមានសមត្ថភាពប្រកាស
- **បញ្ជូន** សំណើដោយផ្អែកលើបំណង / ស្កូរហេយ៊ូរីស្ទិច
- **ភ្ជាប់** លទ្ធផលជាច្រើនជំហាន (ដកចេញ → ដោះស្រាយ → កែលម្អ)
- **រួមបញ្ចូល** API ក្រុមហ៊ុនរួមសម្រាប់កម្មវិធីផ្នែកខាងក្រោម
- **ពង្រីក** ការរចនាទៅពពក (កិច្ចសន្យាស្រដៀង OpenAI)

## លទ្ធផលដាន

- បានបញ្ចប់សម័យ ១–៥
- មានម៉ូដែលស្រុកខ្លួនជាច្រើនបានរក្សាទុក (ឧ. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ក្បាលបរិយាកាសឆ្លងវេទិកា

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
សេវាកម្មឆក់/VM ពី macOS:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## សំណុំដំណើរការ​បង្ហាញ (៣០ នាទី)

### ១. ប្រកាសសមត្ថភាពឧបករណ៍ (៥ នាទី)

បង្កើត `samples/06-tools/models_catalog.py`៖

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```
  
### ២. ការចាប់បំណងនិងការបញ្ជូន (៨ នាទី)

បង្កើត `samples/06-tools/router.py`៖

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # កាតាឡុកពិន្ទុ៖ ការផ្គូផ្គងសមត្ថភាពជាមុន បន្ទាប់មកលំដាប់អាទិភាព
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # តម្រៀប៖ ផ្គូផ្គង True ជាមុន បន្ទាប់មកតម្លៃអាទិភាពដ៏ទាបបំផុត
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```
  
### ៣. ភ្ជាប់ភារកិច្ចជាច្រើនជំហាន (៧ នាទី)

បង្កើត `samples/06-tools/pipeline.py`៖

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```
  
### ៤. គម្រោងចាប់ផ្តើម៖ បង្រួមបង្រួម `06-models-as-tools` (៥ នាទី)

ការកែលម្អ៖  
- បន្ថែមការគាំទ្រតូចតាចនៃការចេញសញ្ញា ( UI អាប់ដេតជាដំណាក់កាល)  
- បន្ថែមពិន្ទុទំនុកចិត្ត៖ ការជួបប្រយោលអក្សរសមាស ឬគម្រោងបញ្ជា  
- នាំចេញ JSON តាមដំណើរ (បំណង → ម៉ូដែល → យឺត → ការប្រើសញ្ញា)  
- ដំណើរការចំហCached សម្រាប់ជំហានរងដែលមានការញឹកញាប់  

### ៥. ផ្លូវពង្រីកទៅ Azure (៥ នាទី)

| ស្រទាប់ | ស្រុកខ្លួន (Foundry) | ពពក (Azure AI Foundry) | និតិវិធីផ្លាស់ប្តូរ |
|-------|-----------------|--------------------------|---------------------|
| ការបញ្ជូន | Python Heuristic | សេវាប្រតិបត្តិការស្រាប់ | បន្ទប់បេឡាកូរ និងដាក់អោយ API ផ្គត់ផ្គង់ |
| ម៉ូដែល | SLMs រក្សាទុក | ការដាក់ចេញគ្រប់គ្រង | ផ្សំឈ្មោះស្រុកខ្លួនទៅ ID ដាក់ចេញ |
| ការត្រួតពិនិត្យ | ស្ថិតិ CLI / ដៃ | ការចុះកំណត់កណ្ដាល និងគុណភាព | បន្ថែមព្រឹត្តិការណ៍តាមដើរ |
| សន្តិសុខ | ម៉ាស៊ីនស្រុកខ្លួនតែប៉ុណ្ណោះ | ភាពយន្ត Azure / បណ្ដាញ | បញ្ចូលគោលការណ៍កូនសោសម្រាប់សម្ងាត់ |
| ថ្លៃដើម | ប្រើធនធានឧបករណ៍ | ការទូទាត់តាមការប្រើប្រាស់ | បន្ថែមគន្លងគាំទ្រចំណាយ |

## បញ្ជីត្រួតពិនិត្យការផ្ទៀងផ្ទាត់

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
រំពឹងថា ការជ្រើសរើសម៉ូដែលដោយផ្អែកលើបំណង និងលទ្ធផលចុងក្រោយបានកែលម្អ។

## ដោះស្រាយបញ្ហា

| បញ្ហា | មូលហេតុ | ដោះស្រាយ |
|---------|-------|-----|
| ភារកិច្ចទាំងអស់បញ្ជូនទៅម៉ូដែលដូចគ្នា | ច្បាប់ខ្សោយ | ពង្រឹងប្រភេទ INTENT_RULES regex |
| ជំហានមួយក្នុង pipeline បរាជ័យ | ម៉ូដែលដែលខ្វះមិនបានផ្ទុក | ដំណើរការ `foundry model run <model>` |
| លទ្ធផលខ្វះសម្របសម្រួល | គ្មានដំណាក់កាលកែលម្អ | បន្ថែមជំហានសង្ខេប/ផ្ទៀងផ្ទាត់ |

## ឯកសារយោង

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry  
- គំរូគុណភាពប្រើ Prompt: មើលសម័យទី ២  

---

**រយៈពេលសម័យ**៖ ៣០ នាទី  
**កម្រិត**៖ ជំនាញជាស្រេច

## ទ្រឹស្តីទិន្នន័យ & ការចងក្រងវគ្គបង្រៀន

| ស្គ្រីបវគ្គបង្រៀន / សៀវភៅកំណត់ហេតុនាំចូល | ទេវកម្ម | គោលបំណង | ទិន្នន័យ / ប្រភពតារាង |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ជំនួយការអភិវឌ្ឍន៍ដោះស្រាយបំណងផ្សំ (កែលម្អ, សង្ខេប, ចាត់ថ្នាក់) | បំណងហេយ៊ូរីស្ទិច → បញ្ជូនម៉ូដែលជាឈ្មោះកាត់ជាមួយការប្រើសញ្ញា | `CATALOG` នៅក្នុង + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | ការធ្វើផែនការ និងកែលម្អជាច្រើនជំហានសម្រាប់ភារកិច្ចជំនួយកូដស្មុគស្មាញ | ដកចេញ → អនុវត្តជំនាញ → ជំហានកែលម្អសង្ខេប | `CATALOG` ដដែល; ជំហានទទួលបានពីលទ្ធផលផែនការ |

### រឿងរ៉ាវទ្រឹស្តី  
ឧបករណ៍ផលិតភាពវិស្វកម្មទទួលភារកិច្ចផ្សេងគ្នា៖ កែលម្អកូដ, សង្ខេបកំណត់ត្រាស្ថាបត្យកម្ម, ចាត់ថ្នាក់មតិយោបល់។ ដើម្បីតិចថយការយឺត និងការប្រើធនធាន, ម៉ូដែលទូទៅតូចមួយធ្វើផែនការ និងសង្ខេប, ម៉ូដែលជំនាញកូដដោះស្រាយការកែលម្អ, ហើយម៉ូដែលស្រាលមានសមត្ថភាពចាត់ថ្នាក់ដាក់ស្លាកមតិយោបល់។ ឯកសារ pipeline បង្ហាញពីការភ្ជាប់និងកែលម្អ; ស្គ្រីប router ឯកតាធ្វើឲ្យមានការបញ្ជូនរចនាសម្ព័ន្ធតែមួយ។  

### រូបថតសង្ខេបតារាង  
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  
### គំរូសំណួរប្រឡង  
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  
### ផ្នែកបន្ថែមតាមដើរ (ជាជម្រើស)  
បន្ថែមបន្ទាត់ JSON តាមជំហានសម្រាប់ `models_pipeline.py`:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  
### គំនិតការកើនឡើងពេញចិត្ត (Idea)  
បើផែនការមានពាក្យគន្លឹះដូចជា "បង្កើតប្រសើរឡើង", "សន្តិសុខ", ឬបន្ទាត់ជំហាន> ២៨០ តួអក្សរ → ធ្វើឲ្យមានម៉ូដែលធំជាង (ឧ. `gpt-oss-20b`) ប្រើសម្រាប់ជំហាននោះតែប៉ុណ្ណោះ។  

### ការកែលម្អជាជម្រើស

| ផ្នែក | កែលម្អ | តម្លៃ | ការណែនាំ |
|------|-------------|-------|------|
| ការកែប្រែ Cached | គ្រប់គ្រងការប្រើឡើងវិញ + អតិថិជន | ការសន្សំពេលវេលា, បន្ថយយ៉ាក | ប្រើ `workshop_utils.get_client` |
| គុណភាពប្រើប្រាស់ | យកចំនួនសញ្ញា និងពេលយឺតជាអង្គភាព | ពិនិត្យនិងបង្កើតប្រសិទ្ធភាព | ថ្ងៃណាមួយការហៅប្រើ​បញ្ជូនដំណើរការ និងរក្សាទុកក្នុងបញ្ជីតាមដើរ |
| ការបញ្ជូនបត់បែន | ទំនុកចិត្ត / ដឹងថ្លៃ | ជាមួយគុណភាព-ថ្លៃល្អប្រសើរ | បន្ថែមពិន្ទុ៖ បើ prompt > N តួអក្សរ ឬ regex ត្រូវពេលដែលតំបន់ទំនាក់ទំនង → ធ្វើឲ្យមានម៉ូដែលធំជាង |
| រាជធានីសមត្ថភាពឌីណាមិច | បញ្ចូលកាតាឡុកដោយកម្តៅ | មិនចាំបាច់ចាប់ផ្តើមឡើងវិញ | ផ្ទុក `catalog.json` ពេលដំណើរការ; មើលម៉ោង ផ្ទុកឯកសារ |
| និតិវិធីសង ការផ្ទាល់ខ្លួន | រឹងមាំក្រោមការបរាជ័យ | មានភាពចូលដំណើរការខ្ពស់ | ព្យាយាមជាលើកដំបូង → លើកលែងករណីកើតកំហុស alias ពាក់កណ្តាល |
| សន្ទស្សន៍ផ្លាស់ប្តូរផែនការ | មតិយោបល់ដើម | កែលំអរប្រើប្រាស់ | បញ្ជូនជាជំហាននីមួយៗ ហើយបន្សំព័ត៌មានចុងក្រោយចូល |
| ចំណាត់ថ្នាក់ភាសាវ៉ិចទ័រ | ការបញ្ជូនច្រើនវិធី | មានភាពត្រឹមត្រូវបំណងខ្ពស់ | បញ្ចូល prompt, ជំពូក និងផ្គុំចន្លោះបណ្ដោយ → សមត្ថភាព |
| នាំចេញតាមដើរ | ស្របច្បាប់ / របាយការណ៍ | ធ្វើរបាយការណ៍តាមច្រក | ផ្សាយ JSON បន្ទាត់៖ ជំហាន, បំណង, ម៉ូដែល, ពេលវេលា_ms, សញ្ញា |
| ពិពណ៌នាតម្លៃ | ការប៉ាន់ស្មានមុនពពក | គ្រប់គ្រងថវិកា | កំណត់តម្លៃគំរូ/សញ្ញា និងប្រមាណតាមភារកិច្ច |
| របៀបធម្មតា | ការបង្កើតចំរូងជាឡើងវិញ | ស្ថិតិសម្តែងថ្មោង | Env: `temperature=0`, ចំនួនជំហានកំណត់ |

#### គំរូរចនាសម្ព័ន្ធតាមដើរ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  
#### គំនូរតាងការកើនឡើងបត់បែន

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # បន្តទៅកាន់គំរូហិរញ្ញវត្ថុដ៏ធំនៅពេលមាន
    alias = 'gpt-oss-20b'
```
  
#### ការផ្ទុកឡើងវិញកាតាឡុកម៉ូដែលដោយកម្តៅ

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើទោះបីយើងខិតខំរកភាពត្រឹមត្រូវក៏ដោយ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគិតថាជា ប្រភពដែលមានសុពលភាពបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរតែប្រើការបកប្រែដោយមនុស្សដែលមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសចេញពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->