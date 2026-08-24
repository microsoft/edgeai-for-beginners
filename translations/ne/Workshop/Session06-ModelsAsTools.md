# सत्र 6: फाउन्ड्री लोकल – मोडेलहरू उपकरणको रूपमा

## सारांश

मोडेलहरूलाई स्थानीय AI सञ्चालन तह भित्र संयोज्य उपकरणहरूको रूपमा उपचार गर्नुहोस्। यस सत्रले धेरै विशेष SLM/LLM कलहरूलाई कसरी श्रृंखलाबद्ध गर्ने, कार्यहरूलाई चयनात्मक रूपमा मार्गदर्शन गर्ने, र एप्लिकेशनहरूलाई एकीकृत SDK सतह कसरी प्रस्तुति गर्ने देखाउँदछ। तपाईंले एक हल्का मोडेल राउटर + कार्य योजनाकार निर्माण गर्नुहुनेछ, यसलाई एप स्क्रिप्टमा एकीकृत गर्नुहुनेछ, र उत्पादन कार्यभारको लागि Azure AI Foundry तर्फ स्केलिंग मार्गरेखा तयार गर्नुहुनेछ।

## सिकाइ लक्ष्यहरू

- **धारणा गर्नुहोस्** मोडेलहरूलाई घोषणा गरिएको क्षमतासहित परमाणु उपकरणहरूका रूपमा
- **मार्गदर्शन गर्नुहोस्** अनुरोधहरू इरादा / ह्युरिस्टिक स्कोरिंगको आधारमा
- **श्रृंखला बनाउनुहोस्** बहु-चरण कार्यहरूमा आउटपुटहरू (बिउँत्र्याउनु → समाधान गर्नु → सुधार गर्नु)
- **एकीकृत गर्नुहोस्** रूपमा एक संयुक्त क्लाइन्ट API डाउनस्ट्रीम एप्लिकेशनहरूका लागि
- **स्केल गर्नुहोस्** डिजाइनलाई क्लाउडमा (उही OpenAI-संगत सम्झौता)

## पूर्व आवश्यकताहरू

- सत्रहरू 1–5 सम्पन्न
- धेरै स्थानीय मोडेलहरू क्यास गरिएको (जस्तै, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### क्रस-प्लेटफर्म वातावरण स्निपेट

विन्डोज पावरशेल:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

म्याकओएस / लिनक्स:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

म्याकओएसबाट रिमोट/VM सेवा पहुँच:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## डेमो फ्लो (३० मिनेट)

### १. उपकरण क्षमता घोषणा (५ मिनेट)

`samples/06-tools/models_catalog.py` बनाउनुस्:

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

### २. इरादा पत्ता लगाउने र मार्गदर्शन (८ मिनेट)

`samples/06-tools/router.py` बनाउनुस्:

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
    # स्कोर क्याटलग: क्षमता मिलान पहिले, त्यसपछि प्राथमिकता
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # क्रमबद्ध गर्नुहोस्: पहिले मिलान साँचो, त्यसपछि सबैभन्दा कम प्राथमिकता मान
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

### ३. बहु-चरण कार्य श्रृंखला (७ मिनेट)

`samples/06-tools/pipeline.py` बनाउनुस्:

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

### ४. सुरु परियोजना: `06-models-as-tools` अनुकूलन (५ मिनेट)

सुधारहरू:
- स्ट्रिमिङ टोकन समर्थन थप्नुहोस् (प्रगतिको UI अपडेट)
- विश्वास स्कोरिङ थप्नुहोस्: लेक्सिकल ओभरलैप वा प्रॉम्प्ट रूब्रिक
- ट्रेस JSON निर्यात गर्नुहोस् (इरादा → मोडेल → लेटेंसी → टोकन प्रयोग)
- पुन: प्रयोगका लागि क्यास कार्यान्वयन गर्नुहोस् दोहोरिएका उपचरणहरूमा

### ५. Azure तर्फ स्केलिंग मार्ग (५ मिनेट)

| तह | स्थानीय (फाउन्ड्री) | क्लाउड (Azure AI Foundry) | संक्रमण रणनीति |
|-------|-----------------|--------------------------|---------------------|
| मार्गदर्शन | ह्युरिस्टिक पायथन | दिर्घकालीन माइक्रोसर्भिस | कंटेनरमा परिणत गर्ने र API तैनाथ गर्ने |
| मोडेलहरू | SLMs क्यास गरिएको | प्रबन्धित तैनाथीहरू | स्थानीय नामहरूलाई तैनाथी IDसँग म्याप गर्ने |
| अवलोकनशीलता | CLI तथ्याङ्क/म्यानुअल | केन्द्रिय लगिङ र मेट्रिक्स | संरचित ट्रेस घटनाहरू थप्नुहोस् |
| सुरक्षा | स्थानीय होस्ट मात्र | Azure प्रमाणीकरण / नेटवर्किङ | गोप्यका लागि की भॉल्ट परिचय गर्नुहोस् |
| लागत | उपकरण स्रोत | उपभोक्ता बिलिङ | बजेट गार्डरेलहरू थप्नुहोस् |

## प्रमाणीकरण जाँच सूची

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

इरादा आधारित मोडेल चयन र अन्तिम सुधारिएको आउटपुटको अपेक्षा गर्नुहोस्।

## समस्या समाधान

| समस्या | कारण | समाधान |
|---------|-------|-----|
| सबै कार्यहरू एउटै मोडेलमा मार्गदर्शित | कमजोर नियमहरू | INTENT_RULES regex सेट समृद्ध पार्नुहोस् |
| पाइपलाइन मध्य चरणमा असफल | आवश्यक मोडेल लोड नभएको | `foundry model run <model>` चलाउनुहोस् |
| कम आउटपुट साङ्गठन | सुधार चरण छैन | सारांश/प्रमाणीकरण पास थप्नुहोस् |

## सन्दर्भहरू

- फाउन्ड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry दस्तावेजहरू: https://learn.microsoft.com/azure/ai-foundry
- प्रॉम्प्ट गुणस्तर ढाँचाहरू: सेसन 2 हेर्नुहोस्

---

**सत्र अवधि**: ३० मिनेट  
**कठिनाइ**: विशेषज्ञ

## नमूना परिस्थिति र कार्यशाला म्यापिङ

| कार्यशाला स्क्रिप्टहरू / नोटबुकहरू | परिस्थिति | उद्देश्य | डाटासेट / क्याचलग स्रोत |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | विकासकर्ता सहायक विभिन्न इरादाका प्रॉम्प्टहरू (रिफ्याक्टर, सारांश, वर्गीकरण) व्यवस्थापन गर्दै | ह्युरिस्टिक इरादा → मोडेल एलियस मार्गदर्शन टोकन प्रयोगसहित | इनलाइन `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | जटिल कोडिङ सहायता कार्यको लागि बहु-चरण योजना र सुधार | बिउँत्र्याउनु → विशेष कार्यान्वयन → सारांश सुधार चरण | उही `CATALOG`; चरणहरू योजना आउटपुटबाट व्युत्पन्न |

### परिस्थिति वर्णन
एक इन्जिनियरिङ उत्पादकता उपकरणले विभिन्न प्रकारका कार्यहरू प्राप्त गर्दछ: कोड रिफ्याक्टर, वास्तुकला नोटहरूको सारांश, प्रतिक्रिया वर्गीकरण। विलम्ब र स्रोत प्रयोग कम गर्न, एउटा सानो सामान्य मोडेल योजना बनाउँछ र सारांश गर्छ, एक कोड विशेष मोडेल रिफ्याक्टर ह्यान्डल गर्छ, र एक हल्का वर्गीकरण-सक्षम मोडेल प्रतिक्रिया लेबल गर्दछ। पाइपलाइन स्क्रिप्टले श्रृंखला + सुधार देखाउँछ; राउटर स्क्रिप्टले अनुकूली एकल-प्रॉम्प्ट मार्गदर्शन पृथक गर्दछ।

### क्याचलग स्न्यापशट
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### उदाहरण परीक्षण प्रॉम्प्टहरू
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### ट्रेस विस्तार (वैकल्पिक)
`models_pipeline.py` लागि प्रति-चरण ट्रेस JSON लाइनहरू थप्नुहोस्:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### वृद्धि ह्युरिस्टिक (विचार)
योजना शब्दहरू जस्तै "optimize", "security" वा चरण लम्बाइ > 280 अक्षर भएमा → ठूलो मोडेल (जस्तै, `gpt-oss-20b`) तर्फ केवल त्यस चरणका लागि बढाउनुहोस्।

### वैकल्पिक सुधारहरू

| क्षेत्र | सुधार | मान | संकेत |
|------|-------------|-------|------|
| क्यासिङ | पुन: प्रयोग प्रबन्धक + क्लाइन्ट वस्तुहरू | कम विलम्ब, कम ओभरहेड | `workshop_utils.get_client` प्रयोग गर्नुहोस् |
| प्रयोग मेट्रिक्स | टोकन र प्रति-चरण लेटेंसी कैद गर्नुहोस् | प्रोफाइलिङ र अनुकूलन | प्रत्येक मार्गनिर्देशित कलको समय लिनुहोस्; ट्रेस सूचीमा भण्डारण गर्नुहोस् |
| अनुकूली मार्गदर्शन | विश्वास / लागत जान्ने | राम्रो गुणस्तर-लागत व्यापार-off | स्कोरिङ थप्नुहोस्: प्रॉम्प्ट > N अक्षर वा regex डोमेनसँग मेल खाए → ठूलो मोडेल तर्फ बढाउनुहोस् |
| गतिशील क्षमता रजिष्ट्री | हट रीलोड क्याचलग | पुनः सुरु वा पुनः तैनाथ गर्नु हुँदैन | रuntime मा `catalog.json` लोड गर्नुहोस्; फाइल टाइमस्ट्याम्प हेर्नुहोस् |
| फालब्याक रणनीति | असफलतामा मजबुती | उच्च उपलब्धता | प्राथमिक प्रयास गर्नुहोस् → अपवादमा फालब्याक एलियस |
| स्ट्रिमिङ पाइपलाइन | प्रारम्भिक प्रतिक्रिया | प्रयोगकर्ता अनुभव सुधार | प्रत्येक चरण स्ट्रिम गर्नुहोस् र अन्तिम सुधार इनपुट बफर गर्नुहोस् |
| भेक्टर इरादा एम्बेडिङ्स | थप सूक्ष्म मार्गदर्शन | उच्च इरादा सटीकता | प्रॉम्प्ट एम्बेड गर्नुहोस्, क्लस्टर गर्नुहोस् र केन्द्र भ्रूणलाई क्षमतामा म्याप गर्नुहोस् |
| ट्रेस निर्यात | अडिट गर्न मिल्ने श्रृंखला | अनुपालन/प्रतिवेदन | JSON लाइनहरू निकासा गर्नुहोस्: चरण, इरादा, मोडेल, लेटेंसी_ms, टोकनहरू |
| लागत सिमुलेशन | पूर्व क्लाउड अनुमान | बजेट योजना | मोडेल अनुसार प्रती टोकन काल्पनिक लागत तोक्नुहोस् र प्रति कार्य समेकन गर्नुहोस् |
| डिटरमिनिस्टिक मोड | पुनरुत्पादनयोग्यता | स्थिर बेन्चमार्किङ | वातावरण: `temperature=0`, निर्दिष्ट चरण गणना |

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

#### अनुकूली वृद्धि स्केच

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # यदि उपलब्ध छ भने ठूलो सोधबुझ मोडेलमा उहि चढाउनुहोस्
    alias = 'gpt-oss-20b'
```

#### मोडेल क्याचलग हट रीलोड

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
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->