# सत्र ५: फाउंड्री लोकलसह एआय-सक्षम एजंट्स जलद तयार करा

## सारांश

फाउंड्री लोकलच्या कमी विलंबता आणि गोपनीयता जपणाऱ्या रनटाइमचा उपयोग करून बहु-भूमिका एआय एजंट्स डिझाइन करा आणि त्यांचे समन्वयन करा. तुम्ही एजंट्सच्या भूमिका, मेमरी रणनीती, टूल कॉलिंग पॅटर्न्स आणि अंमलबजावणी ग्राफ्स परिभाषित कराल. सत्रात तुम्ही चेनलिट किंवा लँगग्राफसह विस्तार करू शकणाऱ्या स्कॅफोल्डिंग पॅटर्न्सची ओळख करून दिली जाते. स्टार्टर प्रोजेक्ट विद्यमान एजंट आर्किटेक्चर नमुन्याचा विस्तार करून मेमरी टिकवून ठेवणे + मूल्यांकन हुक्स जोडतो.

## शिकण्याची उद्दिष्टे

- **भूमिका परिभाषित करा**: सिस्टम प्रॉम्प्ट्स आणि क्षमता मर्यादा
- **मेमरी अंमलात आणा**: अल्पकालीन (संवाद), दीर्घकालीन (व्हेक्टर / फाइल), तात्पुरते स्क्रॅचपॅड्स
- **वर्कफ्लो तयार करा**: अनुक्रमिक, शाखीय आणि समांतर एजंट स्टेप्स
- **टूल्स समाकलित करा**: हलके फंक्शन टूल कॉलिंग पॅटर्न
- **मूल्यांकन करा**: मूलभूत ट्रेस + रुब्रिक-आधारित परिणाम स्कोअरिंग

## पूर्वतयारी

- सत्र १–४ पूर्ण केलेले असणे आवश्यक
- Python सह `foundry-local-sdk`, `openai`, पर्यायी `chainlit`
- स्थानिक मॉडेल्स चालू (किमान `phi-4-mini`)

### क्रॉस-प्लॅटफॉर्म एन्व्हायर्नमेंट स्निपेट

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

जर macOS वरून एजंट्स रिमोट Windows होस्ट सर्व्हिसवर चालवत असाल:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (३० मिनिटे)

### १. एजंट्सच्या भूमिका आणि मेमरी परिभाषित करा (७ मिनिटे)

`samples/05-agents/agents_core.py` तयार करा:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### २. CLI स्कॅफोल्डिंग पॅटर्न (३ मिनिटे)

```powershell
python samples/05-agents/agents_core.py
```


### ३. टूल कॉलिंग जोडा (७ मिनिटे)

`samples/05-agents/tools.py` सह विस्तार करा:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


`agents_core.py` मध्ये बदल करा जेणेकरून साध्या टूल सिंटॅक्सला परवानगी मिळेल: वापरकर्ता लिहितो `#tool:get_time` आणि एजंट जनरेशनपूर्वी संदर्भात टूल आउटपुट जोडतो.

### ४. समन्वित वर्कफ्लो (६ मिनिटे)

`samples/05-agents/orchestrator.py` तयार करा:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### ५. स्टार्टर प्रोजेक्ट: `05-agent-architecture` विस्तारित करा (७ मिनिटे)

जोडा:
1. टिकाऊ मेमरी स्तर (उदा., संभाषणांचे JSON लाइन्स अॅपेंड)
2. साधी मूल्यांकन रुब्रिक: तथ्यात्मकता / स्पष्टता / शैली प्लेसहोल्डर्स
3. पर्यायी चेनलिट फ्रंट-एंड (दोन टॅब्स: संभाषण आणि ट्रेसेस)
4. पर्यायी लँगग्राफ शैली स्टेट मशीन (जर अवलंबित्व जोडले असेल) शाखीय निर्णयांसाठी

## व्हॅलिडेशन चेकलिस्ट

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

टूल इंजेक्शन नोटसह संरचित पाइपलाइन आउटपुट अपेक्षित.

## मेमरी रणनीतींचा आढावा

| स्तर | उद्देश | उदाहरण |
|-------|---------|---------|
| अल्पकालीन | संवाद सातत्य | शेवटचे N संदेश |
| एपिसोडिक | सत्र आठवण | प्रत्येक सत्रासाठी JSON |
| सेमॅंटिक | दीर्घकालीन पुनर्प्राप्ती | सारांशांचा व्हेक्टर स्टोअर |
| स्क्रॅचपॅड | विचार प्रक्रिया | इनलाइन चेन-ऑफ-थॉट (खाजगी) |

## मूल्यांकन हुक्स (संकल्पना)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## समस्या सोडवणे

| समस्या | कारण | उपाय |
|-------|------|------------|
| पुनरावृत्ती उत्तर | संदर्भ विंडो खूप मोठी/लहान | मेमरी विंडो पॅरामीटर ट्यून करा |
| टूल कॉल झाले नाही | चुकीचा सिंटॅक्स | `#tool:tool_name` स्वरूप वापरा |
| संथ समन्वयन | अनेक थंड मॉडेल्स | प्री-रन वॉर्मअप प्रॉम्प्ट्स वापरा |

## संदर्भ

- फाउंड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- लँगग्राफ (पर्यायी संकल्पना): https://github.com/langchain-ai/langgraph
- चेनलिट: https://docs.chainlit.io

---

**सत्र कालावधी**: ३० मिनिटे  
**अडचणीचे स्तर**: प्रगत

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा स्क्रिप्ट | परिस्थिती | उद्दिष्ट | उदाहरण प्रॉम्प्ट |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | कार्यकारी-अनुकूल सारांश तयार करणारा ज्ञान संशोधन बॉट | दोन-एजंट पाइपलाइन (संशोधन → संपादकीय सुधारणा) पर्यायी वेगळ्या मॉडेल्ससह | स्पष्ट करा की अनुपालनासाठी एज इन्फरन्स का महत्त्वाचे आहे. |
| (विस्तारित) `tools.py` संकल्पना | वेळ आणि टोकन अंदाज टूल्स जोडा | हलक्या टूल कॉलिंग पॅटर्नचे प्रदर्शन करा | #tool:get_time |

### परिस्थिती कथा
अनुपालन दस्तऐवज टीमला स्थानिक ज्ञान स्रोतांमधून जलद अंतर्गत माहिती आवश्यक आहे, ज्यामुळे ड्राफ्ट्स क्लाउड सेवांना पाठवले जात नाहीत. संशोधक एजंट संक्षिप्त तथ्यात्मक बुलेट्स गोळा करतो; संपादक एजंट कार्यकारी स्पष्टतेसाठी पुन्हा लिहितो. विलंबता अनुकूल करण्यासाठी वेगळ्या मॉडेल्ससाठी उपनाम नियुक्त केले जाऊ शकतात (जलद SLM) व शैली सुधारण्यासाठी (फक्त आवश्यक असल्यास मोठे मॉडेल).

### उदाहरण मल्टी-मॉडेल एन्व्हायर्नमेंट
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### ट्रेस संरचना (पर्यायी)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

प्रत्येक चरण JSONL फाइलमध्ये टिकवून ठेवा जेणेकरून नंतर रुब्रिक स्कोअरिंग करता येईल.

### पर्यायी सुधारणा

| थीम | सुधारणा | फायदा | अंमलबजावणी स्केच |
|-------|------------|---------|-----------------------|
| मल्टी-मॉडेल भूमिका | प्रत्येक एजंटसाठी वेगळे मॉडेल (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | विशेषीकरण आणि गती | उपनाम एन्व्हायर्नमेंट व्हेरिएबल्स निवडा, प्रत्येक भूमिकेसाठी उपनामासह `chat_once` कॉल करा |
| संरचित ट्रेसेस | प्रत्येक कृतीचे JSON ट्रेस (टूल, इनपुट, विलंबता, टोकन्स) | डीबग आणि मूल्यांकन | यादीमध्ये डिक्ट अॅपेंड करा; शेवटी `.jsonl` लिहा |
| मेमरी टिकवून ठेवणे | पुन्हा लोड करण्यायोग्य संवाद संदर्भ | सत्र सातत्य | `Agent.memory` ला `sessions/<ts>.json` मध्ये डंप करा |
| टूल रजिस्ट्ररी | डायनॅमिक टूल शोध | विस्तारक्षमता | `TOOLS` डिक्ट ठेवा आणि नाव/वर्णन तपासा |
| रीट्राय आणि बॅकऑफ | मजबूत लांब चेन | तात्पुरत्या अयशस्वीतेत घट | `act` ला try/except + एक्स्पोनेंशियल बॅकऑफसह रॅप करा |
| रुब्रिक स्कोअरिंग | स्वयंचलित गुणात्मक लेबल्स | सुधारणा ट्रॅक करा | मॉडेलला द्वितीय पास प्रॉम्प्टिंग: "स्पष्टता १-५ दराने रेट करा" |
| व्हेक्टर मेमरी | सेमॅंटिक पुनर्प्राप्ती | समृद्ध दीर्घकालीन संदर्भ | सारांश एम्बेड करा, सिस्टम संदेशात टॉप-k पुनर्प्राप्त करा |
| स्ट्रीमिंग रिप्लाइज | जलद प्रतिसाद अनुभव | UX सुधारणा | स्ट्रीमिंग उपलब्ध झाल्यावर वापरा आणि अंशतः टोकन्स फ्लश करा |
| निर्धारक चाचण्या | पुनरावृत्ती नियंत्रण | स्थिर CI | `temperature=0`, निश्चित प्रॉम्प्ट सीड्ससह चालवा |
| समांतर शाखा | जलद अन्वेषण | थ्रूपुट | स्वतंत्र एजंट स्टेप्ससाठी `concurrent.futures` वापरा |

#### ट्रेस रेकॉर्ड उदाहरण

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### साधा मूल्यांकन प्रॉम्प्ट

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) जोड्या टिकवून ठेवा जेणेकरून ऐतिहासिक गुणवत्ता ग्राफ तयार करता येईल.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.