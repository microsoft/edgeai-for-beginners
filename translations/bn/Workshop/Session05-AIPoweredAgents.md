# সেশন ৫: Foundry Local ব্যবহার করে দ্রুত AI-চালিত এজেন্ট তৈরি করুন

## সারসংক্ষেপ

Foundry Local-এর কম লেটেন্সি এবং গোপনীয়তা-সংরক্ষণকারী রানটাইম ব্যবহার করে মাল্টি-রোল AI এজেন্ট ডিজাইন এবং পরিচালনা করুন। আপনি এজেন্টের ভূমিকা, মেমোরি কৌশল, টুল ব্যবহারের প্যাটার্ন এবং এক্সিকিউশন গ্রাফ সংজ্ঞায়িত করবেন। সেশনে স্ক্যাফোল্ডিং প্যাটার্নের পরিচয় করানো হবে যা আপনি Chainlit বা LangGraph দিয়ে প্রসারিত করতে পারেন। স্টার্টার প্রজেক্ট বিদ্যমান এজেন্ট আর্কিটেকচার নমুনাকে প্রসারিত করে মেমোরি সংরক্ষণ + মূল্যায়ন হুক যোগ করবে।

## শেখার লক্ষ্যসমূহ

- **ভূমিকা সংজ্ঞায়িত করুন**: সিস্টেম প্রম্পট এবং সক্ষমতার সীমা
- **মেমোরি বাস্তবায়ন করুন**: স্বল্পমেয়াদী (কথোপকথন), দীর্ঘমেয়াদী (ভেক্টর / ফাইল), অস্থায়ী স্ক্র্যাচপ্যাড
- **ওয়ার্কফ্লো স্ক্যাফোল্ড করুন**: ধারাবাহিক, শাখাবদ্ধ এবং সমান্তরাল এজেন্ট ধাপ
- **টুল ইন্টিগ্রেট করুন**: হালকা ফাংশন টুল কলিং প্যাটার্ন
- **মূল্যায়ন করুন**: বেসিক ট্রেস + রুব্রিক-চালিত ফলাফল স্কোরিং

## পূর্বশর্ত

- সেশন ১–৪ সম্পন্ন
- Python সহ `foundry-local-sdk`, `openai`, ঐচ্ছিক `chainlit`
- লোকাল মডেল চালু (কমপক্ষে `phi-4-mini`)

### ক্রস-প্ল্যাটফর্ম পরিবেশ স্নিপেট

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

যদি macOS থেকে দূরবর্তী Windows হোস্ট সার্ভিসে এজেন্ট চালানো হয়:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ডেমো ফ্লো (৩০ মিনিট)

### ১. এজেন্ট ভূমিকা এবং মেমোরি সংজ্ঞায়িত করুন (৭ মিনিট)

`samples/05-agents/agents_core.py` তৈরি করুন:

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


### ২. CLI স্ক্যাফোল্ডিং প্যাটার্ন (৩ মিনিট)

```powershell
python samples/05-agents/agents_core.py
```


### ৩. টুল ব্যবহারের যোগ (৭ মিনিট)

`samples/05-agents/tools.py` দিয়ে প্রসারিত করুন:

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

`agents_core.py` পরিবর্তন করুন যাতে সহজ টুল সিনট্যাক্স অনুমোদিত হয়: ব্যবহারকারী লেখেন `#tool:get_time` এবং এজেন্ট প্রজন্মের আগে প্রসঙ্গের মধ্যে টুল আউটপুট প্রসারিত করে।

### ৪. সমন্বিত ওয়ার্কফ্লো (৬ মিনিট)

`samples/05-agents/orchestrator.py` তৈরি করুন:

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


### ৫. স্টার্টার প্রজেক্ট: `05-agent-architecture` প্রসারিত করুন (৭ মিনিট)

যোগ করুন:
1. স্থায়ী মেমোরি স্তর (যেমন, কথোপকথনের JSON লাইন সংযোজন)
2. সহজ মূল্যায়ন রুব্রিক: বাস্তবতা / স্পষ্টতা / স্টাইল প্লেসহোল্ডার
3. ঐচ্ছিক Chainlit ফ্রন্ট-এন্ড (দুই ট্যাব: কথোপকথন এবং ট্রেস)
4. ঐচ্ছিক LangGraph স্টাইল স্টেট মেশিন (যদি নির্ভরতা যোগ করা হয়) শাখাবদ্ধ সিদ্ধান্তের জন্য

## যাচাই চেকলিস্ট

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

টুল ইনজেকশন নোট সহ কাঠামোগত পাইপলাইন আউটপুট প্রত্যাশা করুন।

## মেমোরি কৌশলসমূহের ওভারভিউ

| স্তর | উদ্দেশ্য | উদাহরণ |
|------|----------|--------|
| স্বল্পমেয়াদী | কথোপকথনের ধারাবাহিকতা | শেষ N বার্তা |
| এপিসোডিক | সেশন পুনরায় স্মরণ | প্রতি সেশনের JSON |
| সেমান্টিক | দীর্ঘমেয়াদী পুনরুদ্ধার | সারাংশের ভেক্টর স্টোর |
| স্ক্র্যাচপ্যাড | যুক্তি ধাপ | ইনলাইন চিন্তার শৃঙ্খল (ব্যক্তিগত) |

## মূল্যায়ন হুক (ধারণাগত)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## সমস্যা সমাধান

| সমস্যা | কারণ | সমাধান |
|-------|------|--------|
| পুনরাবৃত্তি উত্তর | প্রসঙ্গ উইন্ডো খুব বড়/ছোট | মেমোরি উইন্ডো প্যারামিটার টিউন করুন |
| টুল ব্যবহার হয়নি | ভুল সিনট্যাক্স | `#tool:tool_name` ফরম্যাট ব্যবহার করুন |
| ধীর সমন্বয় | একাধিক ঠান্ডা মডেল | প্রি-রান ওয়ার্মআপ প্রম্পট ব্যবহার করুন |

## রেফারেন্স

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (ঐচ্ছিক ধারণা): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**সেশনের সময়কাল**: ৩০ মিনিট  
**কঠিনতা**: উন্নত

## নমুনা পরিস্থিতি এবং ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট | পরিস্থিতি | উদ্দেশ্য | উদাহরণ প্রম্পট |
|--------------------|-----------|----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | নির্বাহী-বান্ধব সারাংশ তৈরি করা জ্ঞান গবেষণা বট | দুই-এজেন্ট পাইপলাইন (গবেষণা → সম্পাদনা) ঐচ্ছিক পৃথক মডেল সহ | ব্যাখ্যা করুন কেন কমপ্লায়েন্সের জন্য এজ ইনফারেন্স গুরুত্বপূর্ণ। |
| (প্রসারিত) `tools.py` ধারণা | সময় এবং টোকেন অনুমান টুল যোগ করুন | হালকা টুল ব্যবহারের প্যাটার্ন প্রদর্শন করুন | #tool:get_time |

### পরিস্থিতি বিবরণ
কমপ্লায়েন্স ডকুমেন্টেশন টিম দ্রুত অভ্যন্তরীণ ব্রিফিং চায় যা লোকাল জ্ঞান থেকে উৎসাহিত হয়, ক্লাউড সার্ভিসে ড্রাফট পাঠানো ছাড়াই। একজন গবেষক এজেন্ট সংক্ষিপ্ত বাস্তব বুলেট সংগ্রহ করে; একজন সম্পাদক এজেন্ট নির্বাহী স্পষ্টতার জন্য পুনর্লিখন করে। লেটেন্সি অপ্টিমাইজ করতে পৃথক মডেল এলিয়াস বরাদ্দ করা যেতে পারে (দ্রুত SLM) বনাম স্টাইলিস্টিক পরিমার্জন (প্রয়োজন হলে শুধুমাত্র বড় মডেল)।

### উদাহরণ মাল্টি-মডেল পরিবেশ
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### ট্রেস কাঠামো (ঐচ্ছিক)
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

প্রতিটি ধাপ JSONL ফাইলে সংরক্ষণ করুন পরবর্তী রুব্রিক স্কোরিংয়ের জন্য।

### ঐচ্ছিক উন্নতি

| থিম | উন্নতি | সুবিধা | বাস্তবায়ন স্কেচ |
|-----|--------|--------|-----------------|
| মাল্টি-মডেল ভূমিকা | প্রতি এজেন্টে পৃথক মডেল (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | বিশেষায়ন এবং গতি | এলিয়াস পরিবেশ ভেরিয়েবল নির্বাচন করুন, প্রতি-ভূমিকা এলিয়াস সহ `chat_once` কল করুন |
| কাঠামোগত ট্রেস | প্রতিটি কাজের JSON ট্রেস (টুল, ইনপুট, লেটেন্সি, টোকেন) | ডিবাগ এবং মূল্যায়ন | একটি তালিকায় ডিক্ট যোগ করুন; শেষে `.jsonl` লিখুন |
| মেমোরি সংরক্ষণ | পুনরায় লোডযোগ্য কথোপকথন প্রসঙ্গ | সেশন ধারাবাহিকতা | `Agent.memory` ডাম্প করুন `sessions/<ts>.json` এ |
| টুল রেজিস্ট্রি | গতিশীল টুল আবিষ্কার | প্রসারণযোগ্যতা | `TOOLS` ডিক্ট বজায় রাখুন এবং নাম/বর্ণনা পরীক্ষা করুন |
| পুনরায় চেষ্টা এবং ব্যাকঅফ | শক্তিশালী দীর্ঘ শৃঙ্খল | অস্থায়ী ব্যর্থতা কমান | `act` কে try/except + এক্সপোনেনশিয়াল ব্যাকঅফ দিয়ে মোড়ান |
| রুব্রিক স্কোরিং | স্বয়ংক্রিয় গুণগত লেবেল | উন্নতির ট্র্যাকিং | সেকেন্ডারি পাস প্রম্পটিং মডেল: "স্পষ্টতা ১-৫ রেট করুন" |
| ভেক্টর মেমোরি | সেমান্টিক পুনরুদ্ধার | সমৃদ্ধ দীর্ঘমেয়াদী প্রসঙ্গ | সারাংশ এম্বেড করুন, সিস্টেম বার্তায় শীর্ষ-k পুনরুদ্ধার করুন |
| স্ট্রিমিং রিপ্লাই | দ্রুত অনুভূত প্রতিক্রিয়া | UX উন্নতি | স্ট্রিমিং উপলব্ধ হলে ব্যবহার করুন এবং আংশিক টোকেন ফ্লাশ করুন |
| নির্ধারিত পরীক্ষা | রিগ্রেশন নিয়ন্ত্রণ | স্থিতিশীল CI | `temperature=0`, নির্দিষ্ট প্রম্পট বীজ দিয়ে চালান |
| সমান্তরাল শাখাবদ্ধ | দ্রুত অনুসন্ধান | থ্রুপুট | স্বাধীন এজেন্ট ধাপের জন্য `concurrent.futures` ব্যবহার করুন |

#### ট্রেস রেকর্ড উদাহরণ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### সহজ মূল্যায়ন প্রম্পট

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) জোড়া সংরক্ষণ করুন একটি ঐতিহাসিক গুণমান গ্রাফ তৈরি করতে।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।