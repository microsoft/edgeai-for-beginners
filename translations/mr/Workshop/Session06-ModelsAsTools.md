# सत्र 6: Foundry लोकल – मॉडेल्स टूल्स म्हणून

## सारांश

स्थानिक AI ऑपरेटिंग लेयरमध्ये मॉडेल्सना संयोज्य टूल्स म्हणून वागवा. हे सत्र कसे अनेक विशेषीकृत SLM/LLM कॉल्सचे साखळीस वाढवायचे, निवडकपणे कामे रूट करायची, आणि अनुप्रयोगांसाठी एकसंध SDK पृष्ठभाग उघडायचे हे दाखवते. तुम्ही एक हलका मॉडेल राऊटर + टास्क प्लॅनर तयार कराल, त्याला अॅप स्क्रिप्टमध्ये एकत्र कराल, आणि उत्पादन कार्यांसाठी Azure AI Foundry कडे स्केलिंगचा मार्ग आखाल.

## शिकण्याची उद्दिष्टे

- मॉडेल्सना घोषित क्षमतांसह अणु उपकरणे म्हणून **संकल्पना** करा
- हेतू / युक्तिवादात्मक स्कोरिंगवर आधारित विनंत्या **रूट** करा
- बहु-टप्पीय कामांमध्ये आउटपुट्स **साखळी** करा (विभाजित करा → सोडवा → सुधारा)
- खालच्या स्तरातील अनुप्रयोगांसाठी एकसंध क्लायंट API **एकत्रित** करा
- डिझाइनला क्लाउडमध्ये **स्केल** करा (समान OpenAI-सुसंगत करार)

## पूर्वअटी

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

macOS मधून Remote/VM सेवा प्रवेश:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## डेमो फ्लो (30 मिनिटे)

### 1. टूल क्षमता घोषणा (5 मिनिटे)

तयार करा `samples/06-tools/models_catalog.py`:

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

### 2. हेतू ओळख आणि रूटिंग (8 मिनिटे)

तयार करा `samples/06-tools/router.py`:

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
    # गुणांकन सूची: प्रथम क्षमता जुळणी, नंतर प्राधान्यक्रम
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # क्रमवारी लावा: प्रथम जुळणी खरे, नंतर कमी प्राधान्य मूल्य
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

### 3. बहु-टप्पा काम साखळी (7 मिनिटे)

तयार करा `samples/06-tools/pipeline.py`:

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

### 4. स्टार्ट करण्यासाठी प्रोजेक्ट: `06-models-as-tools` मध्ये रूपांतरण (5 मिनिटे)

सुधारणा:
- स्ट्रीमिंग टोकन समर्थन जोडा (प्रगतीशील UI अपडेट)
- आत्मविश्वास स्कोरिंग जोडा: लेक्सिकल ओव्हरलॅप किंवा प्रॉम्प्ट रूब्रिक
- ट्रेस JSON निर्यात करा (हेतू → मॉडेल → विलंब → टोकन वापर)
- पुनरावृत्तीच्या उपटप्प्यांसाठी कॅश पुनर्वापर अंमलबजावणी करा

### 5. Azure कडे स्केलिंगचा मार्ग (5 मिनिटे)

| स्तर | स्थानिक (Foundry) | क्लाउड (Azure AI Foundry) | संक्रमण धोरण |
|-------|-----------------|--------------------------|---------------------|
| रूटिंग | युक्तिवादात्मक पाइथन | टिकाऊ मायक्रोसर्व्हिस | कंटेनराइज करा आणि API तैनात करा |
| मॉडेल्स | SLMs कॅश केलेले | व्यवस्थापित तैनात्या | स्थानिक नावे तैनात आयडींशी नकाशित करा |
| निरीक्षणक्षमता | CLI आकडे/मॅन्युअल | केंद्रीकृत लॉगिंग & मेट्रिक्स | संरचित ट्रेस इव्हेंट जोडा |
| सुरक्षा | स्थानिक होस्ट फक्त | Azure प्रमाणीकरण / नेटवर्किंग | रहस्यांसाठी की वॉल्ट सुरू करा |
| खर्च | उपकरण संसाधन | वापर बिलिंग | बजेट गार्डरेल्स जोडा |

## पडताळणी यादी

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

अपेक्षा करा हेतू-आधारित मॉडेल निवड आणि अंतिम सुधारीत आउटपुट.

## समस्या निवारण

| समस्या | कारण | उपाय |
|---------|-------|-----|
| सर्व कामे एकाच मॉडेलकडे रूट होतात | कमजोर नियम | INTENT_RULES regex संच समृद्ध करा |
| पाइपलाइन मधल्या टप्प्यात अयशस्वी | आवश्यक मॉडेल लोड नाही झाले | `foundry model run <model>` चालवा |
| कमी आउटपुट एकरसता | सुधारण टप्पा नाही | सारांश/पडताळणी टप्पा जोडा |

## संदर्भ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- प्रॉम्प्ट गुणवत्ता नमुने: सत्र 2 पहा

---

**सत्र कालावधी**: 30 मिनिटे  
**कठिणाई**: तज्ञ

## नमुना परिस्थिती आणि कार्यशाळा नकाशा

| कार्यशाळा स्क्रिप्ट्स / नोटबुक्स | परिस्थिती | उद्दिष्ट | डेटासेट / कॅटलॉग स्रोत |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | डेव्हलपर सहाय्यक विणलेल्या हेतूच्या प्रॉम्प्ट हाताळणी (रिफॅक्टर, सारांश, वर्गीकरण) | युक्तिवादात्मक हेतू → मॉडेल आणि टोकन वापर रूटिंग | इनलाइन `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | गुंतागुंतीच्या कोडिंग सहाय्याच्या कामासाठी बहु-टप्पा नियोजन व सुधारणा | विभाजित करा → विशेष कार्यान्वयन → सारांश सुधारीत टप्पा | समान `CATALOG`; टप्पे योजनेच्या आउटपुटवर आधारित |

### परिस्थिती कथन
एक अभियांत्रिकी उत्पादकता साधन विविध कामे प्राप्त करते: कोड रिफॅक्टर करा, आर्किटेक्चरल नोट्स सारांशित करा, अभिप्राय वर्गीकृत करा. विलंब आणि संसाधन वापर कमी करण्यासाठी, एक लहान सामान्य मॉडेल योजना बनवते आणि सारांश करतो, एक कोड-विशेष मॉडेल रिफॅक्टरिंग हाताळतो, आणि एक हलका वर्गीकरणक्षम मॉडेल अभिप्राय लेबल करतो. पाइपलाइन स्क्रिप्ट साखळी + सुधारणा दाखवते; राऊटर स्क्रिप्ट अनुकूली सिंगल-प्रॉम्प्ट रूटिंग वेगळे करते.

### कॅटलॉग झलक
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

### ट्रेस विस्तार (ऐच्छिक)
`models_pipeline.py` साठी प्रति-टप्पा ट्रेस JSON ओळी जोडा:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### वाढीव युक्तिवादात्मक (कल्पना)
जर योजनेत "optimize", "security", किंवा टप्प्याची लांबी > 280 अक्षरे असे कीवर्ड्स असतील → त्या टप्प्यासाठी फक्त मोठ्या मॉडेलकडे (उदा., `gpt-oss-20b`) वाढविणे.

### ऐच्छिक सुधारणा

| क्षेत्र | सुधारणा | मूल्य | सूचना |
|------|-------------|-------|------|
| कॅशिंग | पुनर्वापर व्यवस्थापक + क्लायंट वस्तू | कमी विलंब, कमी ओव्हरहेड | `workshop_utils.get_client` वापरा |
| वापर मेट्रिक्स | टोकन आणि प्रति-टप्पा विलंब कैद करा | प्रॉफाइलिंग आणि ऑप्टिमायझेशन | प्रत्येक रूटेड कॉलचा वेळ घ्या; ट्रेस यादीत साठवा |
| अनुकूली रूटिंग | विश्वास / खर्च जागरूक | चांगले गुणवत्ता-खर्च संतोलन | स्कोरिंग जोडा: जर प्रॉम्प्ट > N अक्षरे किंवा regex डोमेनशी जुळले → मोठ्या मॉडेलकडे वाढवा |
| डायनामिक क्षमता नोंदणी | हॉट रीलोड कॅटलॉग | पुन्हा सुरू न करता पुनर्प्रस्थापित करा | रनटाइममध्ये `catalog.json` लोड करा; फाइल टाइमस्टॅम्प पाहा |
| फallback धोरण | अपयशांवर दृढता | उच्च उपलब्धता | प्राथमिक प्रयत्न करा → अपवादावर फallback उपनाम |
| स्ट्रीमिंग पाइपलाइन | लवकर अभिप्राय | UX सुधारणा | प्रत्येक टप्पा स्ट्रीम करा आणि अंतिम सुधारणेचा इनपुट बफर करा |
| व्हेक्टर हेतू एम्बेडिंग्ज | अधिक सूक्ष्म रूटिंग | उच्च हेतू अचूकता | प्रॉम्प्ट एम्बेड करा, क्लस्टर करा आणि सेंट्रोइड क्षमता म्हणून नकाशित करा |
| ट्रेस निर्यात | ऑडिट करण्यायोग्य साखळी | अनुपालन/अहवाल | JSON ओळी जारी करा: टप्पा, हेतू, मॉडेल, विलंब_ms, टोकन्स |
| खर्च अनुकरण | पूर्व-क्लाउड अंदाज | बजेट नियोजन | प्रति मॉडेल प्रती टोकन काल्पनिक किंमत द्या व कामानुसार एकत्र करा |
| निश्चित मोड | पुनरुत्पादनीयता | स्थिर बेंचमार्किंग | पर्यावरण: `temperature=0`, निश्चित टप्पा संख्या |

#### ट्रेस रचना उदाहरण

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### अनुकूली वाढीचा आराखडा

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # उपलब्ध असल्यास मोठ्या विचारसरणीच्या मॉडेलकडे वाढवा
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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->