# सत्र 6: फाउंड्री लोकल – मॉडेल्स साधन म्हणून

## सारांश

मॉडेल्सना स्थानिक AI ऑपरेटिंग लेयरमध्ये संयोजनीय साधन म्हणून वापरा. या सत्रात अनेक विशेष SLM/LLM कॉल्स कसे साखळीने जोडायचे, कार्ये निवडकपणे कशी रूट करायची आणि अनुप्रयोगांसाठी एकसंध SDK पृष्ठभाग कसा उघडायचा हे दाखवले आहे. तुम्ही एक हलके मॉडेल राउटर + टास्क प्लॅनर तयार कराल, ते अॅप स्क्रिप्टमध्ये समाकलित कराल आणि उत्पादन कार्यभारासाठी Azure AI Foundry पर्यंत स्केलिंग मार्ग रेखाटाल.

## शिकण्याची उद्दिष्टे

- मॉडेल्सना घोषित क्षमतांसह अणु साधन म्हणून **कल्पना करा**
- हेतू / ह्युरिस्टिक स्कोअरिंगवर आधारित विनंत्या **रूट करा**
- बहु-चरण कार्यांमध्ये आउटपुट **साखळीने जोडा** (विभाजित करा → सोडवा → सुधारणा करा)
- डाउनस्ट्रीम अनुप्रयोगांसाठी एकसंध क्लायंट API **समाकलित करा**
- क्लाउडसाठी डिझाइन **स्केल करा** (सारखाच OpenAI-सुसंगत करार)

## पूर्वतयारी

- सत्र 1–5 पूर्ण केलेले
- अनेक स्थानिक मॉडेल्स कॅश केलेले (उदा., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### क्रॉस-प्लॅटफॉर्म वातावरण स्निपेट

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

macOS वरून Remote/VM सेवा प्रवेश:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (30 मिनिटे)

### 1. साधन क्षमता घोषणा (5 मिनिटे)

`samples/06-tools/models_catalog.py` तयार करा:

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


### 2. हेतू शोध आणि रूटिंग (8 मिनिटे)

`samples/06-tools/router.py` तयार करा:

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


### 3. बहु-चरण कार्य साखळी (7 मिनिटे)

`samples/06-tools/pipeline.py` तयार करा:

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


### 4. स्टार्टर प्रोजेक्ट: `06-models-as-tools` अनुकूल करा (5 मिनिटे)

सुधारणा:
- स्ट्रीमिंग टोकन समर्थन जोडा (प्रगत UI अपडेट)
- आत्मविश्वास स्कोअरिंग जोडा: लॅक्सिकल ओव्हरलॅप किंवा प्रॉम्प्ट रुब्रिक
- ट्रेस JSON निर्यात करा (हेतू → मॉडेल → विलंब → टोकन वापर)
- पुनरावृत्ती उपचरणांसाठी कॅशे पुनर्वापर अंमलात आणा

### 5. Azure पर्यंत स्केलिंग मार्ग (5 मिनिटे)

| स्तर | स्थानिक (फाउंड्री) | क्लाउड (Azure AI Foundry) | संक्रमण धोरण |
|------|--------------------|---------------------------|--------------|
| रूटिंग | ह्युरिस्टिक Python | टिकाऊ मायक्रोसर्व्हिस | API कंटेनराइझ करा आणि तैनात करा |
| मॉडेल्स | SLMs कॅश केलेले | व्यवस्थापित तैनाती | स्थानिक नावे तैनाती IDs शी नकाशा करा |
| निरीक्षणक्षमता | CLI आकडेवारी/मॅन्युअल | केंद्रीय लॉगिंग आणि मेट्रिक्स | संरचित ट्रेस इव्हेंट्स जोडा |
| सुरक्षा | फक्त स्थानिक होस्ट | Azure प्रमाणीकरण / नेटवर्किंग | गुपितांसाठी की व्हॉल्ट सादर करा |
| खर्च | डिव्हाइस संसाधन | वापर बिलिंग | बजेट गार्डरेल्स जोडा |

## सत्यापन चेकलिस्ट

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

हेतू-आधारित मॉडेल निवड आणि अंतिम सुधारित आउटपुट अपेक्षित.

## समस्या निवारण

| समस्या | कारण | उपाय |
|--------|-------|------|
| सर्व कार्ये समान मॉडेलकडे रूट केली जातात | कमजोर नियम | INTENT_RULES regex सेट समृद्ध करा |
| पाइपलाइन मधल्या चरणात अयशस्वी होते | लोड केलेले मॉडेल गहाळ | `foundry model run <model>` चालवा |
| आउटपुट सुसंगती कमी | सुधारणा टप्पा नाही | सारांश/सत्यापन पास जोडा |

## संदर्भ

- फाउंड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry दस्तऐवज: https://learn.microsoft.com/azure/ai-foundry
- प्रॉम्प्ट गुणवत्ता नमुने: सत्र 2 पहा

---

**सत्र कालावधी**: 30 मिनिटे  
**अडचण पातळी**: तज्ज्ञ

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा स्क्रिप्ट्स / नोटबुक्स | परिस्थिती | उद्दिष्ट | डेटासेट / कॅटलॉग स्रोत |
|----------------------------------|------------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | मिश्र हेतू प्रॉम्प्ट्स हाताळणारा विकसक सहाय्यक (पुनर्रचना, सारांश, वर्गीकरण) | ह्युरिस्टिक हेतू → मॉडेल उपनाम रूटिंग टोकन वापरासह | इनलाइन `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | जटिल कोडिंग सहाय्य कार्यासाठी बहु-चरण नियोजन आणि सुधारणा | विभाजित करा → विशेष कार्यान्वयन → सारांश सुधारणा चरण | समान `CATALOG`; चरण योजना आउटपुटमधून व्युत्पन्न |

### परिस्थिती कथन

एक अभियांत्रिकी उत्पादकता साधन विविध कार्ये प्राप्त करते: कोड पुनर्रचना करा, स्थापत्य नोट्स सारांशित करा, अभिप्राय वर्गीकृत करा. विलंब आणि संसाधन वापर कमी करण्यासाठी, एक लहान सामान्य मॉडेल नियोजन आणि सारांशित करते, कोड-विशेष मॉडेल पुनर्रचना हाताळते, आणि एक हलके वर्गीकरण-सक्षम मॉडेल अभिप्राय लेबल करते. पाइपलाइन स्क्रिप्ट साखळी + सुधारणा दाखवते; राउटर स्क्रिप्ट अनुकुल सिंगल-प्रॉम्प्ट रूटिंग वेगळे करते.

### कॅटलॉग स्नॅपशॉट

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### उदाहरण चाचणी प्रॉम्प्ट्स

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### ट्रेस विस्तार (पर्यायी)

`models_pipeline.py` साठी प्रति-चरण ट्रेस JSON ओळी जोडा:

```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### एस्कलेशन ह्युरिस्टिक (कल्पना)

जर योजना "ऑप्टिमाइझ", "सुरक्षा" यासारख्या कीवर्ड्स समाविष्ट करते किंवा चरण लांबी > 280 वर्ण असेल → त्या चरणासाठी मोठ्या मॉडेलकडे (उदा., `gpt-oss-20b`) एस्कलेट करा.

### पर्यायी सुधारणा

| क्षेत्र | सुधारणा | मूल्य | सूचना |
|--------|---------|-------|-------|
| कॅशिंग | व्यवस्थापक + क्लायंट ऑब्जेक्ट्स पुनर्वापर करा | कमी विलंब, कमी ओव्हरहेड | `workshop_utils.get_client` वापरा |
| वापर मेट्रिक्स | टोकन्स आणि प्रति-चरण विलंब कॅप्चर करा | प्रोफाइलिंग आणि ऑप्टिमायझेशन | प्रत्येक रूट केलेल्या कॉलचे वेळ मोजा; ट्रेस यादीत संग्रहित करा |
| अनुकुल रूटिंग | आत्मविश्वास / खर्च जागरूक | चांगले गुणवत्ता-खर्च व्यापार | स्कोअरिंग जोडा: जर प्रॉम्प्ट > N वर्ण किंवा regex डोमेन जुळते → मोठ्या मॉडेलकडे एस्कलेट करा |
| डायनॅमिक क्षमता रजिस्ट्र्री | कॅटलॉग हॉट रीलोड करा | पुन्हा सुरू न करता पुनर्नियोजन | रनटाइमवर `catalog.json` लोड करा; फाइल टाइमस्टॅम्प पहा |
| फॉलबॅक धोरण | अपयशांखाली मजबुती | उच्च उपलब्धता | प्राथमिक प्रयत्न करा → अपवादावर फॉलबॅक उपनाम |
| स्ट्रीमिंग पाइपलाइन | लवकर अभिप्राय | UX सुधारणा | प्रत्येक चरण प्रवाहित करा आणि अंतिम सुधारणा इनपुट बफर करा |
| वेक्टर हेतू एम्बेडिंग | अधिक सूक्ष्म रूटिंग | उच्च हेतू अचूकता | प्रॉम्प्ट एम्बेड करा, क्लस्टर करा आणि सेंट्रॉइड → क्षमता नकाशा करा |
| ट्रेस निर्यात | ऑडिट करण्यायोग्य साखळी | अनुपालन/अहवाल | JSON ओळी उत्सर्जित करा: चरण, हेतू, मॉडेल, विलंब_ms, टोकन्स |
| खर्च अनुकरण | प्री-क्लाउड अंदाज | बजेट नियोजन | प्रति मॉडेल टोकनसाठी काल्पनिक खर्च नियुक्त करा आणि प्रति कार्य एकत्रित करा |
| निर्धारक मोड | पुनरुत्पादनक्षम पुनरुत्पादकता | स्थिर बेंचमार्किंग | Env: `temperature=0`, निश्चित चरण संख्या |

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


#### अनुकुल एस्कलेशन स्केच

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### मॉडेल कॅटलॉग हॉट रीलोड

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
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.