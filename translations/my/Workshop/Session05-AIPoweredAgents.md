<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T23:35:44+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "my"
}
-->
# အစည်းအဝေး ၅: Foundry Local ဖြင့် AI အင်ဂျင်များကို အလျင်အမြန် တည်ဆောက်ခြင်း

## အကျဉ်းချုပ်

Foundry Local ၏ အနိမ့်လက်ဆွဲနှုန်းနှင့် ကိုယ်ရေးအချက်အလက်များကို ကာကွယ်ထားသော runtime ကို အသုံးပြု၍ အခန်းကဏ္ဍများစွာရှိသော AI အင်ဂျင်များကို ဒီဇိုင်းဆွဲပြီး စီမံခန့်ခွဲပါ။ အင်ဂျင်၏ အခန်းကဏ္ဍများ၊ မှတ်ဉာဏ်နည်းလမ်းများ၊ ကိရိယာခေါ်ယူမှု ပုံစံများနှင့် အကောင်အထည်ဖော်မှု ဂရပ်များကို သတ်မှတ်ပါမည်။ အစည်းအဝေးတွင် Chainlit သို့မဟုတ် LangGraph ဖြင့် တိုးချဲ့နိုင်သော scaffolding ပုံစံများကို မိတ်ဆက်ပေးပါမည်။ Starter project သည် memory persistence + evaluation hooks ထည့်သွင်းရန် ရှိပြီးသား အင်ဂျင် architecture နမူနာကို တိုးချဲ့ပေးပါသည်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

- **အခန်းကဏ္ဍများကို သတ်မှတ်ခြင်း**: System prompts & capability boundaries
- **မှတ်ဉာဏ်ကို အကောင်အထည်ဖော်ခြင်း**: အတိုချုံး (စကားဝိုင်း), ရေရှည် (ဗက်တာ / ဖိုင်), အပျက်ခံ scratchpads
- **Workflow များကို Scaffold လုပ်ခြင်း**: အဆင့်လိုက်, ချိုးဖောက်ခြင်း, နှင့် အပြိုင်အဆိုင် အင်ဂျင်အဆင့်များ
- **ကိရိယာများကို ပေါင်းစည်းခြင်း**: အလွယ်တကူ function tool ခေါ်ယူမှု ပုံစံ
- **အကဲဖြတ်ခြင်း**: အခြေခံ trace + rubric အခြေခံသော ရလဒ်အဆင့်သတ်မှတ်ခြင်း

## ကြိုတင်လိုအပ်ချက်များ

- အစည်းအဝေး ၁–၄ ပြီးစီးထားရမည်
- Python နှင့် `foundry-local-sdk`, `openai`, optional `chainlit`
- `phi-4-mini` အနည်းဆုံးဖြင့် ဒေသခံမော်ဒယ်များ လည်ပတ်နေသည်

### Cross-Platform Environment Snippet

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

macOS မှ remote Windows host service ကို အသုံးပြု၍ အင်ဂျင်များကို လည်ပတ်နေပါက:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (၃၀ မိနစ်)

### ၁. အင်ဂျင်၏ အခန်းကဏ္ဍများနှင့် မှတ်ဉာဏ်ကို သတ်မှတ်ခြင်း (၇ မိနစ်)

`samples/05-agents/agents_core.py` ဖန်တီးပါ:

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


### ၂. CLI Scaffolding Pattern (၃ မိနစ်)

```powershell
python samples/05-agents/agents_core.py
```


### ၃. ကိရိယာခေါ်ယူမှု ထည့်သွင်းခြင်း (၇ မိနစ်)

`samples/05-agents/tools.py` ဖြင့် တိုးချဲ့ပါ:

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


`agents_core.py` ကို ပြင်ဆင်ပြီး ကိရိယာ syntax ကို အလွယ်တကူ အသုံးပြုနိုင်ရန် ပြင်ဆင်ပါ: အသုံးပြုသူသည် `#tool:get_time` ရေးပြီး အင်ဂျင်သည် generation မတိုင်မီ context ထဲသို့ ကိရိယာ output ကို ထည့်သွင်းပါမည်။

### ၄. Workflow ကို စီမံခန့်ခွဲခြင်း (၆ မိနစ်)

`samples/05-agents/orchestrator.py` ဖန်တီးပါ:

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


### ၅. Starter Project: `05-agent-architecture` ကို တိုးချဲ့ခြင်း (၇ မိနစ်)

ထည့်သွင်းရန်:
1. Persistent memory layer (ဥပမာ- စကားဝိုင်းများကို JSON lines append)
2. အကဲဖြတ်မှု rubric ရိုးရှင်းသော- factuality / clarity / style placeholders
3. Optional Chainlit front-end (tab နှစ်ခု: စကားဝိုင်း & traces)
4. Optional LangGraph style state machine (dependency ထည့်သွင်းပါက) ချိုးဖောက်မှု ဆုံးဖြတ်ချက်များအတွက်

## အတည်ပြုမှု စစ်ဆေးမှု စာရင်း

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


Tool injection မှတ်ချက်နှင့် structured pipeline output ကို မျှော်လင့်ပါ။

## မှတ်ဉာဏ်နည်းလမ်းများ အကျဉ်းချုပ်

| Layer | ရည်ရွယ်ချက် | ဥပမာ |
|-------|-------------|-------|
| အတိုချုံး | စကားဝိုင်း ဆက်လက်မှု | နောက်ဆုံး N မက်ဆေ့များ |
| Episodic | အစည်းအဝေးကို မှတ်မိမှု | JSON per session |
| Semantic | ရေရှည် ပြန်လည်ရယူမှု | အကျဉ်းချုပ်များ၏ ဗက်တာ store |
| Scratchpad | အကြောင်းပြချက် အဆင့်များ | Inline chain-of-thought (private) |

## အကဲဖြတ်မှု Hooks (အယူအဆ)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## ပြဿနာများ ဖြေရှင်းခြင်း

| ပြဿနာ | အကြောင်းရင်း | ဖြေရှင်းနည်း |
|-------|--------------|-------------|
| အကြောင်းပြန်များ ထပ်နေသည် | Context window အလွန်ကြီး/သေး | memory window parameter ကို tune လုပ်ပါ |
| Tool မခေါ်ယူနိုင် | Syntax မှားနေသည် | `#tool:tool_name` format ကို အသုံးပြုပါ |
| စီမံခန့်ခွဲမှု နှေးနေသည် | မော်ဒယ်များ အေးနေသည် | warmup prompts ကို ကြိုတင် run လုပ်ပါ |

## ကိုးကားချက်များ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optional concept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**အစည်းအဝေး ကြာမြင့်ချိန်**: ၃၀ မိနစ်  
**အခက်အခဲအဆင့်**: အဆင့်မြင့်

## နမူနာ အခြေအနေ & အလုပ်ရုံဆွေးနွေးမှု Mapping

| Workshop Script | အခြေအနေ | ရည်ရွယ်ချက် | Prompt နမူနာ |
|-----------------|----------|-------------|--------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | အမှုဆောင်များအတွက် အကျဉ်းချုပ်များ ထုတ်လုပ်သော အသိပညာ သုတေသန bot | အင်ဂျင်နှစ်ခု pipeline (သုတေသန → စာတည်းအဆင့်မြှင့်တင်မှု) distinct models optional | Edge inference compliance အရေးကြီးမှုကို ရှင်းပြပါ။ |
| (Extended) `tools.py` concept | အချိန် & token ခန့်မှန်းမှု tools ထည့်သွင်းခြင်း | Lightweight tool invocation pattern ကို ပြသပါ | #tool:get_time |

### အခြေအနေ အကြောင်းအရာ
Compliance documentation အဖွဲ့သည် cloud services သို့ မပို့ပဲ ဒေသခံအသိပညာမှ အတွင်းရေးအကျဉ်းချုပ်များကို အလျင်အမြန် ရယူရန် လိုအပ်သည်။ Researcher agent သည် အတိုချုံးသော အချက်အလက်များကို စုဆောင်းပြီး editor agent သည် အမှုဆောင်အဆင့်အတွက် ရှင်းလင်းမှုရှိသော စာများကို ပြန်ရေးပေးသည်။ Latency (အမြန်နှုန်းမြန်သော SLM) နှင့် stylistic refinement (လိုအပ်သောအခါတွင်သာ မော်ဒယ်ကြီးကို အသုံးပြုခြင်း) အတွက် distinct model aliases များကို သတ်မှတ်နိုင်သည်။

### Multi-Model Environment နမူနာ
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Trace Structure (Optional)
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

တစ်ခုချင်းစီကို JSONL ဖိုင်တွင် rubric scoring အတွက် နောက်ပိုင်းတွင် သိမ်းဆည်းပါ။

### Optional Enhancements

| Theme | Enhancement | အကျိုးကျေးဇူး | Implementation Sketch |
|-------|------------|---------------|-----------------------|
| Multi-Model Roles | အင်ဂျင်တစ်ခုစီအတွက် distinct models (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | အထူးပြုမှု & အမြန်နှုန်း | alias env vars ကို ရွေးချယ်ပြီး per-role alias ဖြင့် `chat_once` ကို ခေါ်ပါ |
| Structured Traces | act(tool,input,latency,tokens) တစ်ခုချင်းစီ၏ JSON trace | Debug & အကဲဖြတ်မှု | dict ကို list ထဲသို့ ထည့်ပြီး `.jsonl` ကို နောက်ဆုံးရေးပါ |
| Memory Persistence | ပြန်လည်ဖွင့်နိုင်သော စကားဝိုင်း context | အစည်းအဝေး ဆက်လက်မှု | `Agent.memory` ကို `sessions/<ts>.json` သို့ dump လုပ်ပါ |
| Tool Registry | ကိရိယာများကို dynamic ရှာဖွေမှု | Extensibility | `TOOLS` dict ကို ထိန်းသိမ်းပြီး name/desc ကို စစ်ဆေးပါ |
| Retry & Backoff | အကြာကြီး chains များကို ခိုင်မာမှုရှိစေရန် | အချိန်ပိုင်း ပြဿနာများ လျှော့ချရန် | `act` ကို try/except + exponential backoff ဖြင့် wrap လုပ်ပါ |
| Rubric Scoring | အရည်အသွေးကို အလိုအလျောက် အမှတ်ပေးခြင်း | တိုးတက်မှုများကို စောင့်ကြည့်ရန် | "Rate clarity 1-5" ဟု model ကို prompting လုပ်ပြီး secondary pass |
| Vector Memory | Semantic recall | ရေရှည် context အကြွယ်အို | အကျဉ်းချုပ်များကို embed လုပ်ပြီး top-k ကို system message ထဲသို့ retrieve လုပ်ပါ |
| Streaming Replies | အမြန်ဆုံးဖြေကြားမှု | UX တိုးတက်မှု | Streaming ကို အသုံးပြုပြီး partial tokens ကို flush လုပ်ပါ |
| Deterministic Tests | Regression control | Stable CI | `temperature=0`, fixed prompt seeds ဖြင့် run လုပ်ပါ |
| Parallel Branching | စူးစမ်းမှု အမြန်နှုန်း | Throughput | `concurrent.futures` ကို အသုံးပြု၍ အင်ဂျင်အဆင့်များကို လွတ်လပ်စွာ run လုပ်ပါ |

#### Trace Record နမူနာ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### ရိုးရှင်းသော အကဲဖြတ်မှု Prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) အတွဲများကို သိမ်းဆည်းပြီး အရည်အသွေးသမိုင်းကြောင်းကို တည်ဆောက်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။