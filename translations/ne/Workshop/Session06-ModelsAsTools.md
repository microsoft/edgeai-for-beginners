<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T21:20:30+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ne"
}
-->
# सत्र ६: फाउन्ड्री लोकल – उपकरणको रूपमा मोडेलहरू

## सारांश

मोडेलहरूलाई स्थानीय AI अपरेटिङ लेयरभित्र संयोजनीय उपकरणको रूपमा व्यवहार गर्नुहोस्। यो सत्रले कसरी धेरै विशेष SLM/LLM कलहरू श्रृंखलाबद्ध गर्ने, कार्यहरू चयनात्मक रूपमा रुट गर्ने, र एप्लिकेसनहरूमा एकीकृत SDK सतहलाई उजागर गर्ने देखाउँछ। तपाईंले हल्का मोडेल राउटर + कार्य योजनाकार निर्माण गर्नुहुनेछ, यसलाई एप स्क्रिप्टमा एकीकृत गर्नुहुनेछ, र उत्पादन कार्यभारहरूको लागि Azure AI Foundry मा स्केलिङ मार्गको रूपरेखा बनाउनुहुनेछ।

## सिकाइ उद्देश्यहरू

- **परिकल्पना गर्नुहोस्** मोडेलहरूलाई घोषित क्षमताहरू भएका परमाणु उपकरणको रूपमा
- **रुट गर्नुहोस्** अनुरोधहरू उद्देश्य / ह्युरिस्टिक स्कोरिङको आधारमा
- **श्रृंखला बनाउनुहोस्** बहु-चरण कार्यहरूमा आउटपुटहरू (विभाजन → समाधान गर्नुहोस् → परिष्कृत गर्नुहोस्)
- **एकीकृत गर्नुहोस्** डाउनस्ट्रीम एप्लिकेसनहरूको लागि एकीकृत क्लाइन्ट API
- **स्केल गर्नुहोस्** क्लाउडमा डिजाइन (OpenAI-संगत सम्झौता समान)

## पूर्वापेक्षाहरू

- सत्र १–५ पूरा गरिएका
- धेरै स्थानीय मोडेलहरू क्यास गरिएका (जस्तै, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### क्रस-प्ल्याटफर्म वातावरण स्निपेट

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

macOS बाट रिमोट/VM सेवा पहुँच:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (३० मिनेट)

### १. उपकरण क्षमता घोषणा (५ मिनेट)

`samples/06-tools/models_catalog.py` सिर्जना गर्नुहोस्:

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


### २. उद्देश्य पत्ता लगाउने र रुटिङ (८ मिनेट)

`samples/06-tools/router.py` सिर्जना गर्नुहोस्:

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
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
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


### ३. बहु-चरण कार्य श्रृंखला बनाउने (७ मिनेट)

`samples/06-tools/pipeline.py` सिर्जना गर्नुहोस्:

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


### ४. स्टार्टर प्रोजेक्ट: `06-models-as-tools` अनुकूलन गर्नुहोस् (५ मिनेट)

सुधारहरू:
- स्ट्रिमिङ टोकन समर्थन थप्नुहोस् (प्रगतिशील UI अपडेट)
- आत्मविश्वास स्कोरिङ थप्नुहोस्: लेक्सिकल ओभरलैप वा प्रम्प्ट रुब्रिक
- ट्रेस JSON निर्यात गर्नुहोस् (उद्देश्य → मोडेल → विलम्बता → टोकन प्रयोग)
- दोहोरिएका उपचरणहरूको लागि क्यास पुन: प्रयोग कार्यान्वयन गर्नुहोस्

### ५. Azure मा स्केलिङ मार्ग (५ मिनेट)

| तह | स्थानीय (फाउन्ड्री) | क्लाउड (Azure AI Foundry) | संक्रमण रणनीति |
|-----|---------------------|--------------------------|----------------|
| रुटिङ | ह्युरिस्टिक पायथन | टिकाउ माइक्रोसर्भिस | API कन्फिगर गरेर डिप्लोय गर्नुहोस् |
| मोडेलहरू | SLMs क्यास गरिएका | व्यवस्थापित डिप्लोयमेन्टहरू | स्थानीय नामहरूलाई डिप्लोयमेन्ट IDs मा म्याप गर्नुहोस् |
| अवलोकनयोग्यता | CLI तथ्यांक/म्यानुअल | केन्द्रीय लगिङ र मेट्रिक्स | संरचित ट्रेस घटनाहरू थप्नुहोस् |
| सुरक्षा | स्थानीय होस्ट मात्र | Azure प्रमाणीकरण / नेटवर्किङ | गोप्य कुराहरूको लागि की भल्ट परिचय गराउनुहोस् |
| लागत | उपकरण स्रोत | उपभोग बिलिङ | बजेट गार्डरेलहरू थप्नुहोस् |

## मान्यकरण चेकलिस्ट

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

उद्देश्य-आधारित मोडेल चयन र अन्तिम परिष्कृत आउटपुट अपेक्षा गर्नुहोस्।

## समस्या समाधान

| समस्या | कारण | समाधान |
|--------|-------|--------|
| सबै कार्यहरू एउटै मोडेलमा रुट गरिन्छ | कमजोर नियमहरू | INTENT_RULES regex सेटलाई समृद्ध गर्नुहोस् |
| पाइपलाइन बीचमा असफल हुन्छ | लोड गरिएको मोडेल हराइरहेको छ | `foundry model run <model>` चलाउनुहोस् |
| कम आउटपुट सामंजस्यता | परिष्कृत चरण छैन | सारांश/मान्यकरण पास थप्नुहोस् |

## सन्दर्भहरू

- फाउन्ड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry डकुमेन्ट्स: https://learn.microsoft.com/azure/ai-foundry
- प्रम्प्ट गुणस्तर ढाँचा: सत्र २ हेर्नुहोस्

---

**सत्र अवधि**: ३० मिनेट  
**कठिनाई स्तर**: विशेषज्ञ

## नमूना परिदृश्य र कार्यशाला म्यापिङ

| कार्यशाला स्क्रिप्टहरू / नोटबुकहरू | परिदृश्य | उद्देश्य | डेटासेट / क्याटलग स्रोत |
|------------------------------------|----------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | मिश्रित उद्देश्य प्रम्प्टहरू (पुन: संरचना, सारांश, वर्गीकरण) ह्यान्डल गर्ने विकासकर्ता सहायक | ह्युरिस्टिक उद्देश्य → मोडेल उपनाम रुटिङ टोकन प्रयोगको साथ | इनलाइन `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | जटिल कोडिङ सहायता कार्यको लागि बहु-चरण योजना र परिष्कृत | विभाजन गर्नुहोस् → विशेष कार्यान्वयन → सारांश परिष्कृत चरण | समान `CATALOG`; चरणहरू योजना आउटपुटबाट व्युत्पन्न |

### परिदृश्य कथा

एक इन्जिनियरिङ उत्पादकता उपकरणले विभिन्न कार्यहरू प्राप्त गर्दछ: कोड पुन: संरचना गर्नुहोस्, वास्तुकला नोटहरूको सारांश बनाउनुहोस्, प्रतिक्रिया वर्गीकरण गर्नुहोस्। विलम्बता र स्रोत प्रयोगलाई न्यूनतम गर्न, एउटा सानो सामान्य मोडेलले योजना बनाउँछ र सारांश बनाउँछ, कोड-विशेष मोडेलले पुन: संरचना गर्छ, र हल्का वर्गीकरण-सक्षम मोडेलले प्रतिक्रिया लेबल गर्छ। पाइपलाइन स्क्रिप्टले श्रृंखला + परिष्कृत प्रदर्शन गर्दछ; राउटर स्क्रिप्टले अनुकूलन एकल-प्रम्प्ट रुटिङलाई अलग गर्दछ।

### क्याटलग स्न्यापशट

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### उदाहरण परीक्षण प्रम्प्टहरू

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### ट्रेस विस्तार (वैकल्पिक)

`models_pipeline.py` को लागि प्रति-चरण ट्रेस JSON लाइनहरू थप्नुहोस्:

```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### वृद्धि ह्युरिस्टिक (आइडिया)

यदि योजनामा "अप्टिमाइज", "सुरक्षा", वा चरण लम्बाइ > २८० अक्षरहरू जस्ता कुञ्जी शब्दहरू समावेश छन् भने → त्यो चरणको लागि मात्र ठूलो मोडेल (जस्तै, `gpt-oss-20b`) मा वृद्धि गर्नुहोस्।

### वैकल्पिक सुधारहरू

| क्षेत्र | सुधार | मूल्य | संकेत |
|--------|-------|-------|-------|
| क्यासिङ | प्रबन्धक + क्लाइन्ट वस्तुहरू पुन: प्रयोग गर्नुहोस् | कम विलम्बता, कम ओभरहेड | `workshop_utils.get_client` प्रयोग गर्नुहोस् |
| प्रयोग मेट्रिक्स | टोकनहरू र प्रति-चरण विलम्बता कब्जा गर्नुहोस् | प्रोफाइलिङ र अनुकूलन | प्रत्येक रुट गरिएको कलको समय लिनुहोस्; ट्रेस सूचीमा भण्डारण गर्नुहोस् |
| अनुकूलन रुटिङ | आत्मविश्वास / लागत सचेत | गुणस्तर-लागत व्यापार-अफ सुधार | स्कोरिङ थप्नुहोस्: यदि प्रम्प्ट > N अक्षरहरू वा regex डोमेन मिल्छ भने → ठूलो मोडेलमा वृद्धि गर्नुहोस् |
| गतिशील क्षमता रजिस्ट्री | क्याटलग हट रीलोड गर्नुहोस् | पुन: सुरु पुन: डिप्लोय आवश्यक छैन | रनटाइममा `catalog.json` लोड गर्नुहोस्; फाइल टाइमस्ट्याम्प हेर्नुहोस् |
| फलब्याक रणनीति | असफलताहरू अन्तर्गत मजबूती | उच्च उपलब्धता | प्राथमिक प्रयास गर्नुहोस् → अपवादमा फलब्याक उपनाम |
| स्ट्रिमिङ पाइपलाइन | प्रारम्भिक प्रतिक्रिया | UX सुधार | प्रत्येक चरण स्ट्रिम गर्नुहोस् र अन्तिम परिष्कृत इनपुट बफर गर्नुहोस् |
| भेक्टर उद्देश्य एम्बेडिङ | अधिक सूक्ष्म रुटिङ | उच्च उद्देश्य सटीकता | प्रम्प्ट एम्बेड गर्नुहोस्, क्लस्टर गर्नुहोस् र केन्द्रबिन्दु → क्षमता म्याप गर्नुहोस् |
| ट्रेस निर्यात | अडिटेबल श्रृंखला | अनुपालन/रिपोर्टिङ | JSON लाइनहरू निकाल्नुहोस्: चरण, उद्देश्य, मोडेल, विलम्बता_ms, टोकनहरू |
| लागत सिमुलेशन | प्रि-क्लाउड अनुमान | बजेट योजना | प्रति मोडेल टोकनको लागि अनुमानित लागत असाइन गर्नुहोस् र प्रति कार्य समग्र |
| निर्धारण मोड | पुन: उत्पादन पुनरुत्पादनयोग्यता | स्थिर बेंचमार्किङ | Env: `temperature=0`, निश्चित चरणहरूको संख्या |

#### ट्रेस संरचना उदाहरण

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### अनुकूलन वृद्धि स्केच

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### मोडेल क्याटलग हट रीलोड

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

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।