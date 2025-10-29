<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T21:01:29+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "hi"
}
-->
# सत्र 5: Foundry Local के साथ AI-संचालित एजेंट्स को तेजी से बनाएं

## सारांश

Foundry Local के लो-लेटेंसी, प्राइवेसी-संरक्षण रनटाइम का उपयोग करके मल्टी-रोल AI एजेंट्स को डिज़ाइन और ऑर्केस्ट्रेट करें। आप एजेंट्स की भूमिकाएं, मेमोरी रणनीतियां, टूल इनवोकेशन पैटर्न और निष्पादन ग्राफ्स को परिभाषित करेंगे। सत्र में स्कैफोल्डिंग पैटर्न का परिचय दिया गया है जिसे आप Chainlit या LangGraph के साथ विस्तारित कर सकते हैं। स्टार्टर प्रोजेक्ट मौजूदा एजेंट आर्किटेक्चर नमूने को मेमोरी पर्सिस्टेंस + मूल्यांकन हुक्स जोड़ने के लिए विस्तारित करता है।

## सीखने के उद्देश्य

- **भूमिकाएं परिभाषित करें**: सिस्टम प्रॉम्प्ट्स और क्षमता सीमाएं
- **मेमोरी लागू करें**: शॉर्ट-टर्म (संवाद), लॉन्ग-टर्म (वेक्टर / फाइल), अस्थायी स्क्रैचपैड्स
- **वर्कफ़्लो स्कैफोल्ड करें**: क्रमिक, शाखित, और समानांतर एजेंट चरण
- **टूल्स को एकीकृत करें**: हल्के फंक्शन टूल कॉलिंग पैटर्न
- **मूल्यांकन करें**: बेसिक ट्रेस + रूब्रिक-चालित परिणाम स्कोरिंग

## आवश्यकताएं

- सत्र 1–4 पूरे किए गए हों
- Python के साथ `foundry-local-sdk`, `openai`, वैकल्पिक `chainlit`
- लोकल मॉडल्स चल रहे हों (कम से कम `phi-4-mini`)

### क्रॉस-प्लेटफ़ॉर्म एनवायरनमेंट स्निपेट

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

यदि macOS से रिमोट Windows होस्ट सेवा के खिलाफ एजेंट्स चला रहे हैं:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (30 मिनट)

### 1. एजेंट भूमिकाएं और मेमोरी परिभाषित करें (7 मिनट)

`samples/05-agents/agents_core.py` बनाएं:

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


### 2. CLI स्कैफोल्डिंग पैटर्न (3 मिनट)

```powershell
python samples/05-agents/agents_core.py
```


### 3. टूल इनवोकेशन जोड़ें (7 मिनट)

`samples/05-agents/tools.py` के साथ विस्तारित करें:

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

`agents_core.py` को संशोधित करें ताकि सरल टूल सिंटैक्स की अनुमति दी जा सके: उपयोगकर्ता लिखता है `#tool:get_time` और एजेंट जनरेशन से पहले संदर्भ में टूल आउटपुट को विस्तारित करता है।

### 4. ऑर्केस्ट्रेटेड वर्कफ़्लो (6 मिनट)

`samples/05-agents/orchestrator.py` बनाएं:

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


### 5. स्टार्टर प्रोजेक्ट: `05-agent-architecture` को विस्तारित करें (7 मिनट)

जोड़ें:
1. स्थायी मेमोरी लेयर (जैसे, JSON लाइन्स में संवादों को जोड़ना)
2. सरल मूल्यांकन रूब्रिक: तथ्यात्मकता / स्पष्टता / शैली प्लेसहोल्डर्स
3. वैकल्पिक Chainlit फ्रंट-एंड (दो टैब्स: संवाद और ट्रेसेस)
4. वैकल्पिक LangGraph शैली स्टेट मशीन (यदि निर्भरता जोड़ रहे हैं) शाखित निर्णयों के लिए

## सत्यापन चेकलिस्ट

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

टूल इंजेक्शन नोट के साथ संरचित पाइपलाइन आउटपुट की अपेक्षा करें।

## मेमोरी रणनीतियों का अवलोकन

| लेयर | उद्देश्य | उदाहरण |
|------|----------|---------|
| शॉर्ट-टर्म | संवाद निरंतरता | अंतिम N संदेश |
| एपिसोडिक | सत्र पुनः स्मरण | प्रत्येक सत्र के लिए JSON |
| सेमांटिक | लॉन्ग-टर्म पुनर्प्राप्ति | सारांशों का वेक्टर स्टोर |
| स्क्रैचपैड | तर्क चरण | इनलाइन चेन-ऑफ-थॉट (निजी) |

## मूल्यांकन हुक्स (सैद्धांतिक)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## समस्या निवारण

| समस्या | कारण | समाधान |
|--------|-------|---------|
| दोहराव वाले उत्तर | संदर्भ विंडो बहुत बड़ी/छोटी | मेमोरी विंडो पैरामीटर को ट्यून करें |
| टूल इनवोक नहीं हुआ | गलत सिंटैक्स | `#tool:tool_name` प्रारूप का उपयोग करें |
| धीमा ऑर्केस्ट्रेशन | कई ठंडे मॉडल्स | प्री-रन वार्मअप प्रॉम्प्ट्स का उपयोग करें |

## संदर्भ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (वैकल्पिक अवधारणा): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**सत्र अवधि**: 30 मिनट  
**कठिनाई स्तर**: उन्नत

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला स्क्रिप्ट | परिदृश्य | उद्देश्य | उदाहरण प्रॉम्प्ट |
|---------------------|----------|----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ज्ञान अनुसंधान बॉट जो कार्यकारी-अनुकूल सारांश तैयार करता है | दो-एजेंट पाइपलाइन (अनुसंधान → संपादकीय पॉलिश) वैकल्पिक अलग-अलग मॉडल्स के साथ | समझाएं कि अनुपालन के लिए एज इनफेरेंस क्यों महत्वपूर्ण है। |
| (विस्तारित) `tools.py` अवधारणा | समय और टोकन अनुमान टूल्स जोड़ें | हल्के टूल इनवोकेशन पैटर्न का प्रदर्शन करें | #tool:get_time |

### परिदृश्य कथा
अनुपालन दस्तावेज़ीकरण टीम को लोकल ज्ञान से तेज़ आंतरिक ब्रीफ्स की आवश्यकता है, बिना ड्राफ्ट्स को क्लाउड सेवाओं में भेजे। एक शोधकर्ता एजेंट संक्षिप्त तथ्यात्मक बुलेट्स एकत्र करता है; एक संपादक एजेंट कार्यकारी स्पष्टता के लिए उन्हें फिर से लिखता है। विलंबता को अनुकूलित करने के लिए अलग-अलग मॉडल उपनाम सौंपे जा सकते हैं (तेज़ SLM) बनाम शैलीगत परिष्करण (केवल आवश्यकता होने पर बड़ा मॉडल)।

### उदाहरण मल्टी-मॉडल एनवायरनमेंट
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### ट्रेस संरचना (वैकल्पिक)
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

प्रत्येक चरण को JSONL फ़ाइल में बाद में रूब्रिक स्कोरिंग के लिए संरक्षित करें।

### वैकल्पिक सुधार

| थीम | सुधार | लाभ | कार्यान्वयन स्केच |
|-----|-------|------|-------------------|
| मल्टी-मॉडल भूमिकाएं | प्रत्येक एजेंट के लिए अलग-अलग मॉडल्स (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | विशेषज्ञता और गति | उपनाम एनव वेरिएबल्स का चयन करें, प्रति-भूमिका उपनाम के साथ `chat_once` कॉल करें |
| संरचित ट्रेसेस | प्रत्येक एक्ट(tool,input,latency,tokens) का JSON ट्रेस | डिबग और मूल्यांकन | सूची में डिक्ट जोड़ें; अंत में `.jsonl` लिखें |
| मेमोरी पर्सिस्टेंस | पुनः लोड करने योग्य संवाद संदर्भ | सत्र निरंतरता | `Agent.memory` को `sessions/<ts>.json` में डंप करें |
| टूल रजिस्ट्री | डायनामिक टूल डिस्कवरी | विस्तारशीलता | `TOOLS` डिक्ट बनाए रखें और नाम/विवरण का निरीक्षण करें |
| रिट्री और बैकऑफ | मजबूत लंबे चेन | अस्थायी विफलताओं को कम करें | `act` को try/except + एक्सपोनेंशियल बैकऑफ के साथ लपेटें |
| रूब्रिक स्कोरिंग | स्वचालित गुणात्मक लेबल्स | सुधारों को ट्रैक करें | मॉडल को सेकेंडरी पास प्रॉम्प्ट करें: "स्पष्टता को 1-5 रेट करें" |
| वेक्टर मेमोरी | सेमांटिक पुनर्प्राप्ति | समृद्ध लॉन्ग-टर्म संदर्भ | सारांशों को एम्बेड करें, सिस्टम संदेश में टॉप-k पुनर्प्राप्त करें |
| स्ट्रीमिंग उत्तर | तेज़ अनुभवात्मक प्रतिक्रिया | UX सुधार | उपलब्ध होने पर स्ट्रीमिंग का उपयोग करें और आंशिक टोकन फ्लश करें |
| निर्धारक परीक्षण | रिग्रेशन नियंत्रण | स्थिर CI | `temperature=0`, फिक्स्ड प्रॉम्प्ट सीड्स के साथ चलाएं |
| समानांतर शाखित | तेज़ अन्वेषण | थ्रूपुट | स्वतंत्र एजेंट चरणों के लिए `concurrent.futures` का उपयोग करें |

#### ट्रेस रिकॉर्ड उदाहरण

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### सरल मूल्यांकन प्रॉम्प्ट

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) जोड़े को संरक्षित करें ताकि ऐतिहासिक गुणवत्ता ग्राफ बनाया जा सके।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।