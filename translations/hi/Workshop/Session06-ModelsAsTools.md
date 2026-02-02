# सत्र 6: फाउंड्री लोकल – उपकरण के रूप में मॉडल

## सारांश

मॉडलों को स्थानीय AI ऑपरेटिंग लेयर के अंदर संयोजनीय उपकरण के रूप में मानें। यह सत्र दिखाता है कि कैसे कई विशेष SLM/LLM कॉल्स को चेन किया जाए, कार्यों को चयनात्मक रूप से रूट किया जाए, और एप्लिकेशन के लिए एकीकृत SDK सतह को उजागर किया जाए। आप एक हल्का मॉडल राउटर + टास्क प्लानर बनाएंगे, इसे एक ऐप स्क्रिप्ट में एकीकृत करेंगे, और उत्पादन कार्यभार के लिए Azure AI Foundry तक स्केलिंग पथ को रेखांकित करेंगे।

## सीखने के उद्देश्य

- **कल्पना करें** कि मॉडल को घोषित क्षमताओं वाले परमाणु उपकरण के रूप में कैसे देखा जा सकता है  
- **रूट करें** अनुरोधों को इरादे / हीयुरिस्टिक स्कोरिंग के आधार पर  
- **चेन करें** आउटपुट को बहु-चरणीय कार्यों में (विभाजित करें → हल करें → परिष्कृत करें)  
- **एकीकृत करें** डाउनस्ट्रीम एप्लिकेशन के लिए एकीकृत क्लाइंट API  
- **स्केल करें** डिज़ाइन को क्लाउड तक (OpenAI-संगत अनुबंध के साथ)

## आवश्यकताएँ

- सत्र 1–5 पूरे किए गए  
- कई स्थानीय मॉडल कैश किए गए (जैसे, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### क्रॉस-प्लेटफ़ॉर्म पर्यावरण स्निपेट

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
  
macOS से रिमोट/VM सेवा एक्सेस:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## डेमो फ्लो (30 मिनट)

### 1. उपकरण क्षमता घोषणा (5 मिनट)

`samples/06-tools/models_catalog.py` बनाएं:  

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
  

### 2. इरादा पहचान और रूटिंग (8 मिनट)

`samples/06-tools/router.py` बनाएं:  

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
  

### 3. बहु-चरणीय कार्य चेनिंग (7 मिनट)

`samples/06-tools/pipeline.py` बनाएं:  

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
  

### 4. स्टार्टर प्रोजेक्ट: `06-models-as-tools` को अनुकूलित करें (5 मिनट)

सुधार:  
- स्ट्रीमिंग टोकन समर्थन जोड़ें (प्रगतिशील UI अपडेट)  
- आत्मविश्वास स्कोरिंग जोड़ें: लेक्सिकल ओवरलैप या प्रॉम्प्ट रूब्रिक  
- ट्रेस JSON निर्यात करें (इरादा → मॉडल → विलंबता → टोकन उपयोग)  
- पुनरावृत्त उपचरणों के लिए कैश पुन: उपयोग लागू करें  

### 5. Azure तक स्केलिंग पथ (5 मिनट)

| लेयर | लोकल (फाउंड्री) | क्लाउड (Azure AI Foundry) | संक्रमण रणनीति |
|-------|-----------------|--------------------------|---------------------|
| रूटिंग | हीयुरिस्टिक पायथन | टिकाऊ माइक्रोसर्विस | API को कंटेनराइज़ और तैनात करें |
| मॉडल | SLMs कैश किए गए | प्रबंधित तैनाती | स्थानीय नामों को तैनाती IDs से मैप करें |
| अवलोकन | CLI आँकड़े/मैनुअल | केंद्रीय लॉगिंग और मेट्रिक्स | संरचित ट्रेस इवेंट्स जोड़ें |
| सुरक्षा | केवल स्थानीय होस्ट | Azure प्रमाणीकरण / नेटवर्किंग | रहस्य के लिए की वॉल्ट पेश करें |
| लागत | डिवाइस संसाधन | खपत बिलिंग | बजट गार्डरेल्स जोड़ें |

## सत्यापन चेकलिस्ट

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
इरादा-आधारित मॉडल चयन और अंतिम परिष्कृत आउटपुट की अपेक्षा करें।

## समस्या निवारण

| समस्या | कारण | समाधान |
|---------|-------|-----|
| सभी कार्य एक ही मॉडल पर रूट हो रहे हैं | कमजोर नियम | INTENT_RULES regex सेट को समृद्ध करें |
| पाइपलाइन मध्य-चरण में विफल हो रही है | लोड किया गया मॉडल गायब है | `foundry model run <model>` चलाएं |
| आउटपुट में कम सामंजस्य | परिष्कृत चरण नहीं है | सारांश/मान्यकरण पास जोड़ें |

## संदर्भ

- फाउंड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry दस्तावेज़: https://learn.microsoft.com/azure/ai-foundry  
- प्रॉम्प्ट गुणवत्ता पैटर्न: सत्र 2 देखें  

---

**सत्र की अवधि**: 30 मिनट  
**कठिनाई स्तर**: विशेषज्ञ  

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला स्क्रिप्ट्स / नोटबुक्स | परिदृश्य | उद्देश्य | डेटा सेट / कैटलॉग स्रोत |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | डेवलपर सहायक जो मिश्रित इरादा प्रॉम्प्ट्स (पुनर्गठन, सारांश, वर्गीकरण) को संभालता है | हीयुरिस्टिक इरादा → मॉडल उपनाम रूटिंग टोकन उपयोग के साथ | इनलाइन `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | जटिल कोडिंग सहायता कार्य के लिए बहु-चरणीय योजना और परिष्करण | विभाजित करें → विशेष निष्पादन → सारांश परिष्करण चरण | वही `CATALOG`; चरण योजना आउटपुट से प्राप्त |

### परिदृश्य कथा
एक इंजीनियरिंग उत्पादकता उपकरण विभिन्न प्रकार के कार्य प्राप्त करता है: कोड को पुनर्गठित करना, वास्तु नोट्स का सारांश बनाना, प्रतिक्रिया को वर्गीकृत करना। विलंबता और संसाधन उपयोग को कम करने के लिए, एक छोटा सामान्य मॉडल योजना और सारांश बनाता है, एक कोड-विशेषीकृत मॉडल पुनर्गठन को संभालता है, और एक हल्का वर्गीकरण-सक्षम मॉडल प्रतिक्रिया को लेबल करता है। पाइपलाइन स्क्रिप्ट चेनिंग + परिष्करण का प्रदर्शन करती है; राउटर स्क्रिप्ट अनुकूली एकल-प्रॉम्प्ट रूटिंग को अलग करती है।

### कैटलॉग स्नैपशॉट
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  

### उदाहरण परीक्षण प्रॉम्प्ट्स
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  

### ट्रेस एक्सटेंशन (वैकल्पिक)
`models_pipeline.py` के लिए प्रति-चरण ट्रेस JSON लाइनों को जोड़ें:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  

### वृद्धि हीयुरिस्टिक (विचार)
यदि योजना में "ऑप्टिमाइज़", "सुरक्षा", या चरण की लंबाई > 280 वर्ण शामिल हैं → उस चरण के लिए केवल बड़े मॉडल (जैसे, `gpt-oss-20b`) पर बढ़ाएं।

### वैकल्पिक सुधार

| क्षेत्र | सुधार | मूल्य | संकेत |
|------|-------------|-------|------|
| कैशिंग | प्रबंधक + क्लाइंट ऑब्जेक्ट्स का पुन: उपयोग करें | कम विलंबता, कम ओवरहेड | `workshop_utils.get_client` का उपयोग करें |
| उपयोग मेट्रिक्स | टोकन और प्रति-चरण विलंबता कैप्चर करें | प्रोफाइलिंग और अनुकूलन | प्रत्येक रूटेड कॉल का समय लें; ट्रेस सूची में स्टोर करें |
| अनुकूली रूटिंग | आत्मविश्वास / लागत जागरूक | बेहतर गुणवत्ता-लागत संतुलन | स्कोरिंग जोड़ें: यदि प्रॉम्प्ट > N वर्ण या regex डोमेन से मेल खाता है → बड़े मॉडल पर बढ़ाएं |
| डायनामिक क्षमता रजिस्ट्री | कैटलॉग को हॉट रीलोड करें | कोई पुनः आरंभ पुनः तैनाती नहीं | रनटाइम पर `catalog.json` लोड करें; फ़ाइल टाइमस्टैम्प देखें |
| फॉलबैक रणनीति | विफलताओं के तहत मजबूती | उच्च उपलब्धता | प्राथमिक प्रयास करें → अपवाद पर फॉलबैक उपनाम |
| स्ट्रीमिंग पाइपलाइन | प्रारंभिक प्रतिक्रिया | UX सुधार | प्रत्येक चरण को स्ट्रीम करें और अंतिम परिष्कृत इनपुट को बफर करें |
| वेक्टर इरादा एम्बेडिंग्स | अधिक सूक्ष्म रूटिंग | उच्च इरादा सटीकता | प्रॉम्प्ट को एम्बेड करें, क्लस्टर करें और सेंट्रॉइड → क्षमता को मैप करें |
| ट्रेस निर्यात | ऑडिटेबल चेन | अनुपालन/रिपोर्टिंग | JSON लाइनों का उत्सर्जन करें: चरण, इरादा, मॉडल, विलंबता_ms, टोकन |
| लागत सिमुलेशन | प्री-क्लाउड अनुमान | बजट योजना | प्रत्येक मॉडल के लिए टोकन/लागत का अनुमानित मूल्य असाइन करें और प्रति कार्य कुल करें |
| निर्धारक मोड | पुनरुत्पादन क्षमता | स्थिर बेंचमार्किंग | Env: `temperature=0`, निश्चित चरणों की संख्या |

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
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```
  

#### मॉडल कैटलॉग हॉट रीलोड

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
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।