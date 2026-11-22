# ਸੈਸ਼ਨ 5: ਫਾਉਂਡਰੀ ਲੋਕਲ ਨਾਲ ਤੇਜ਼ੀ ਨਾਲ AI-ਚਲਿਤ ਏਜੰਟ ਬਣਾਓ

## ਸਾਰ

ਫਾਉਂਡਰੀ ਲੋਕਲ ਦੇ ਥੋੜ੍ਹੇ-ਸਮੇਂ ਵਾਲੇ, ਗੋਪਨੀਯਤਾ ਸੰਭਾਲਣ ਵਾਲੇ ਰਨਟਾਈਮ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਮਲਟੀ-ਰੋਲ AI ਏਜੰਟ ਡਿਜ਼ਾਈਨ ਤੇ ਸੰਗਠਿਤ ਕਰੋ। ਤੁਸੀਂ ਏਜੰਟ ਦੇ ਕਿਰਦਾਰ, ਮੈਮੋਰੀ ਰਣਨੀਤੀਆਂ, ਸੰਦ ਬੁਲਾਣ ਦੇ ਰੂਪ, ਅਤੇ ਕਾਰਜ ਗ੍ਰਾਫ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋਗੇ। ਸੈਸ਼ਨ ਚੇਨਲਿਟ ਜਾਂ ਲੈਂਗਗ੍ਰਾਫ ਨਾਲ ਵਧਾਉਣ ਯੋਗ ਸਕਾਫੋਲਡਿੰਗ ਪੈਟਰਨ ਲੈ ਕੇ ਆਉਂਦਾ ਹੈ। ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ ਮੌਜੂਦਾ ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ ਨਮੂਨੇ ਨੂੰ ਮੈਮੋਰੀ ਪੜ੍ਹਾਈ + ਮੁਲਾਂਕਣ ਹੁਕਮ ਜੋੜਨ ਲਈ ਵਧਾਉਂਦਾ ਹੈ।

## ਸਿਖਣ ਦੇ ਲਕੜੇ

- **ਕਿਰਦਾਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ**: ਸਿਸਟਮ ਪ੍ਰੌਮਪਟ ਅਤੇ ਸਮਰੱਥਾ ਸੀਮਾਵਾਂ
- **ਮੈਮੋਰੀ ਲਾਗੂ ਕਰੋ**: ਛੋਟੀ ਮਿਆਦ (ਗੱਲਬਾਤ), ਲੰਮੀ ਮਿਆਦ (ਵੇਕਟਰ / ਫਾਈਲ), ਅਸਥਾਈ ਸਕ੍ਰੈਚਪੈਡ
- **ਵਰਕਫਲੋ ਸਕਾਫੋਲਡ ਕਰੋ**: ਲੜੀਵਾਰ, ਸ਼ਾਖਾਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਏਜੰਟ ਕਦਮ
- **ਸੰਦ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ**: ਲਘੁ ਭਾਰ ਫੰਕਸ਼ਨ ਸੰਦ ਬੁਲਾਣ ਦਾ ਪੈਟਰਨ
- **ਮੁਲਾਂਕਣ ਕਰੋ**: ਬੁਨਿਆਦੀ ਟਰੇਸ + ਰੁਬ੍ਰਿਕ-ਆਧਾਰਤ ਨਤੀਜਾ ਸਕੋਰਿੰਗ

## ਪ੍ਰੀ-ਰਿਕੁਆਜ਼ਿਟਸ

- ਸੈਸ਼ਨਾਂ 1-4 ਸਮਾਪਤ
- ਪਾਈਥਨ ਨਾਲ `foundry-local-sdk`, `openai`, ਵਿਕਲਪਿਕ `chainlit`
- ਲੋਕਲ ਮਾਡਲ ਚੱਲ ਰਹੇ (ਘੱਟੋ-ਘੱਟ `phi-4-mini`)

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਕਲਾਦੀ ਕੋਡ

ਵਿੰਡੋਜ਼:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

ਮੈਕਓਐਸ:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

ਜੇ ਮੈਕਓਐਸ ਤੋਂ ਏਜੰਟ ਵਿੰਡੋਜ਼ ਰਿਮੋਟ ਹੋਸਟ ਸਰਵਿਸ ਵਿਰੁੱਧ ਚੱਲ ਰਹੇ ਹਨ:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## ਡੈਮੋ ਤਰਤੀਬ (30 ਮਿੰਟ)

### 1. ਏਜੰਟ ਰੋਲ ਅਤੇ ਮੈਮੋਰੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ (7 ਮਿੰਟ)

`samples/05-agents/agents_core.py` ਬਣਾਓ:

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

### 2. CLI ਸਕਾਫੋਲਡਿੰਗ ਪੈਟਰਨ (3 ਮਿੰਟ)

```powershell
python samples/05-agents/agents_core.py
```

### 3. ਸੰਦ ਬੁਲਾਣ ਜੋੜੋ (7 ਮਿੰਟ)

`samples/05-agents/tools.py` ਨਾਲ ਵਧਾਓ:

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

`agents_core.py` ਨੂੰ ਸਧਾਰਨ ਸੰਦ ਸਿੰਟੈਕਸ ਦੀ ਆਗਿਆ ਦਿਓ: ਉਪਭੋਗੀ `#tool:get_time` ਲਿਖਦਾ ਹੈ ਅਤੇ ਏਜੰਟ ਪੈਦਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸੰਦ ਦੇ ਨਤੀਜੇ ਨੂੰ ਸੰਦਰਭ ਵਿੱਚ ਵਧਾਉਂਦਾ ਹੈ।

### 4. ਸੰਗਠਿਤ ਵਰਕਫਲੋ (6 ਮਿੰਟ)

`samples/05-agents/orchestrator.py` ਬਣਾਓ:

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

### 5. ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ: `05-agent-architecture` ਵਧਾਓ (7 ਮਿੰਟ)

ਜੋੜੋ:
1. ਸਥਾਈ ਮੈਮੋਰੀ ਪਰਤ (ਜਿਵੇਂ, ਗੱਲਬਾਤਾਂ ਦੇ JSON ਲਾਈਨਾਂ ਐਪੈਂਡ)
2. ਸਧਾਰਨ ਮੁਲਾਂਕਣ ਰੁਬ੍ਰਿਕ: ਤੱਥਤਾ / ਸਪਸ਼ਟੀਕਰਨ / ਸਟਾਈਲ ਪਲੇਸਹੋਲਡਰ
3. ਵਿਕਲਪਿਕ ਚੇਨਲਿਟ ਫਰੰਟ-ਐਂਡ (ਦੋ ਟੈਬਜ਼: ਗੱਲਬਾਤ ਅਤੇ ਟਰੇਸ)
4. ਵਿਕਲਪਿਕ ਲੈਂਗਗ੍ਰਾਫ ਸਟਾਈਲ ਸਟੇਟ ਮਸ਼ੀਨ (ਜੇ ਨਿਰਭਰਤਾ ਜੋੜਨੀ ਹੋਵੇ) ਸ਼ਾਖਾਵਾਰ ਫੈਸਲੇ ਲਈ

## ਜਾਂਚ ਚੈੱਕਲਿਸਟ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

ਉਮੀਦ ਕਰੋ ਕਿ ਸਾਂਚਿਤ ਪਾਈਪਲਾਈਨ ਨਤੀਜਾ ਸੰਦ ਇੰਜੈਕਸ਼ਨ ਨੋਟ ਦੇ ਨਾਲ ਹੋਵੇਗਾ।

## ਮੈਮੋਰੀ ਰਣਨੀਤੀਆਂ ਦਾ ਸਾਰ

| ਪਰਤ | ਉਦੇਸ਼ | ਉਦਾਹਰਨ |
|-------|---------|---------|
| ਛੋਟੀ ਮਿਆਦ | ਸੰਵਾਦ ਦੀ ਲਗਾਤਾਰਤਾ | ਆਖਰੀ N ਸੁਨੇਹੇ |
| ਐਪੀਸੋਡਿਕ | ਸੈਸ਼ਨ ਯਾਦ ਦਿਲਾਉਣਾ | ਪ੍ਰਤੀ ਸੈਸ਼ਨ JSON |
| ਸੈਮੈਂਟਿਕ | ਲੰਮੀ ਮਿਆਦ ਰੀਟਰਿਵਲ | ਸਾਰਾਂ ਦੇ ਵੇਕਟਰ ਸਟੋਰ |
| ਸਕ੍ਰੈਚਪੈਡ | ਤਰਕਸ਼ੀਲ ਕਦਮ | ਇਨਲਾਈਨ ਲੜੀ-ਵਿਚਾਰ (ਨਾਂ-ਝਾੜੂ) |

## ਮੁਲਾਂਕਣ ਹੁਕਮ (ਧਾਰਣਾਤਮਕ)

```python
evaluation = {
  "factuality": None,  # ਮੈਨੂਅਲ ਜਾਂ ਅਨੁਮਾਨਤੱਮਕ
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## ਸਮੱਸਿਆ-ਸੁਧਾਰ

| ਸਮੱਸਿਆ | ਕਾਰਨ | ਮੁਰੰਮਤ |
|-------|------|------------|
| ਮੁੜ ਮੁੜ ਕੇ ਜਵਾਬ | ਸੰਦਰਭ ਵਿੰਡੋ ਬਹੁਤ ਵੱਡਾ / ਛੋਟਾ | ਮੈਮੋਰੀ ਵਿੰਡੋ ਪੈਰਾਮੀਟਰ ਨੂੰ ਠੀਕ ਕਰੋ |
| ਸੰਦ ਬੁਲਾਇਆ ਨਹੀਂ ਗਿਆ | ਗਲਤ ਸਿੰਟੈਕਸ | `#tool:tool_name` ਫਾਰਮੈਟ ਵਰਤੋਂ |
| ਢਿੱਲਾ ਔਰਕੀਸਟ੍ਰੇਸ਼ਨ | ਕਈ ਕੋਲਡ ਮਾਡਲ | ਪਹਿਲਾਂ ਤੋਂ ਵਾਰਮਅੱਪ ਪ੍ਰੌਮਪਟ ਚਲਾਓ |

## ਹਵਾਲੇ

- ਫਾਉਂਡਰੀ ਲੋਕਲ SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- ਲੈਂਗਗ੍ਰਾਫ (ਵਿਕਲਪਿਕ ਧਾਰਣਾ): https://github.com/langchain-ai/langgraph
- ਚੇਨਲਿਟ: https://docs.chainlit.io

---

**ਸੈਸ਼ਨ ਅਵਧੀ**: 30 ਮਿੰਟ  
**ਕਠਿਨਾਈ**: ਉੱਨਤ

## ਨਮੂਨਾ ਸਥਿਤੀ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੇਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ | ਸਥਿਤੀ | ਲਕੜਾ | ਉਦਾਹਰਨ ਪ੍ਰੌਮਪਟ |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ਗਿਆਨ ਖੋਜ ਬੋਟ ਜੋ ਕਾਰੋਬਾਰੀ-ਮੁਤਾਬਕ ਖੁਲਾਸੇ ਪੈਦਾ ਕਰਦਾ ਹੈ | ਦੋ-ਏਜੰਟ ਪਾਈਪਲਾਈਨ (ਖੋਜ → ਸੰਪਾਦਕੀ ਨਿਪੁੰਨਤਾ) ਨਾਲ ਵਿਕਲਪਿਕ ਵਿਲੱਖਣ ਮਾਡਲ | ਸਮਝਾਓ ਕਿ ਕਾਇਦਾ-ਕਨੂੰਨ ਲਈ ਐਜ ਇਨਫਰੰਸ ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹੈ। |
| (ਵਧਾਇਆ) `tools.py` ਧਾਰਣਾ | ਸਮਾਂ ਅਤੇ ਟੋਕਨ ਅੰਦਾਜ਼ਾ ਸੰਦ ਜੋੜੋ | ਹਲਕੇ ਭਾਰ ਸੰਦ ਬੁਲਾਣ ਦਾ ਪੈਟਰਨ ਦਰਸਾਓ | #tool:get_time |

### ਸਥਿਤੀ ਕਥਾ
ਕਾਇਦਾ ਦਸਤਾਵੇਜ਼ੀ ਟੀਮ ਨੂੰ ਤੇਜ਼ ਘਰੇਲੂ ਜਾਣਕਾਰੀ ਤੋਂ ਅੰਦਰੂਨੀ ਰਿਪੋਰਟਾਂ ਦੀ ਲੋੜ ਹੈ ਬਿਨਾਂ ਮਸੋਂਦੇ ਕਲਾਊਡ ਸਰਵਿਸਣ ਨੂੰ ਭੇਜੇ। ਇੱਕ ਖੋਜਕਾਰ ਏਜੰਟ ਸੰਖੇਪ ਤੱਥ ਬੱਲੀਟਾਂ ਇਕੱਠਾ ਕਰਦਾ ਹੈ; ਇੱਕ ਸੰਪਾਦਕ ਏਜੰਟ ਕਾਰੋਬਾਰੀ ਸਪਸ਼ਟੀਕਰਨ ਲਈ ਮੁੜਲਿਖਦਾ ਹੈ। ਵੱਖ-ਵੱਖ ਮਾਡਲ ਉਪਨਾਮਾਂ ਨੂੰ ਵਢੀ ਸਲਹੀ ਹਵਾਈ ਰਫਤਾਰ (ਫਾਸਟ SLM) ਅਤੇ ਸ਼ੈਲੀਸ਼ ਢੰਗ ਨਾਲ ਵਧਾਉਣ ਲਈ ਸੌਂਪਿਆ ਜਾ ਸਕਦਾ ਹੈ (ਵੱਡਾ ਮਾਡਲ ਸਿਰਫ਼ ਜਦ ਲੋੜ ਹੋਵੇ)।

### ਉਦਾਹਰਨ ਬਹੁ-ਮਾਡਲ ਵਾਤਾਵਰਨ
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### ਟਰੇਸ ਸਾਂਚਾ (ਵਿਕਲਪਿਕ)
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

ਬਾਅਦ ਵਿੱਚ ਰੁਬ੍ਰਿਕ ਸਕੋਰਿੰਗ ਲਈ ਹਰ ਕਦਮ ਨੂੰ JSONL ਫਾਈਲ ਵਿੱਚ ਸੰਭਾਲੋ।

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਥੀਮ | ਸੁਧਾਰ | ਲਾਭ | ਲਾਗੂ ਕਰਨ ਦਾ ਰੂਪਰੇਖਾ |
|-------|------------|---------|-----------------------|
| ਬਹੁ-ਮਾਡਲ ਰੋਲ | ਪ੍ਰਤੀ ਏਜੰਟ ਅਲੱਗ ਮਾਡਲ (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ਵਿਸ਼ੇਸ਼ਤਾ ਅਤੇ ਰਫ਼ਤਾਰ | ਉਪਨਾਮ env vars ਚੁਣੋ, ਪ੍ਰਤੀ-ਰੋਲ ਉਪਨਾਮ ਨਾਲ `chat_once` ਕਾਲ ਕਰੋ |
| ਸੰਰਚਿਤ ਟਰੇਸ | ਹਰ ਕ੍ਰਿਆ (ਸੰਦ, ਇਨਪੁੱਟ, ਲੈਟੈਂਸੀ, ਟੋਕਨ) ਦਾ JSON ਟਰੇਸ | ਡੀਬੱਗ ਅਤੇ ਮੁਲਾਂਕਣ | ਡਿਕਟ ਨੂੰ ਸੂਚੀ ਵਿੱਚ ਜੋੜੋ; ਅੰਤ ਵਿੱਚ `.jsonl` ਲਿਖੋ |
| ਮੈਮੋਰੀ ਲਾਗੂ ਕਰਨਯੋਗਤਾ | ਮੁੜਭਰਨਾ ਯੋਗ ਡਾਇਲਾਗ ਸੰਦਰਭ | ਸੈਸ਼ਨ ਦੀ ਲਗਾਤਾਰਤਾ | `Agent.memory` ਨੂੰ `sessions/<ts>.json` ਵਿੱਚ ਡੰਪ ਕਰੋ |
| ਸੰਦ ਰਜਿਸਟਰੀ | ਗਤੀਸ਼ੀਲ ਸੰਦ ਖੋਜ | ਵਧਾਈਯੋਗਤਾ | `TOOLS` ਡਿਕਟ ਨੂੰ ਰੱਖੋ ਅਤੇ ਨਾਮ/ਵੇਰਵਾ ਦੀ ਜਾਂਚ ਕਰੋ |
| ਮੁੜ ਕੋਸ਼ਿਸ਼ ਅਤੇ ਬੈਕਆਫ਼ | ਮਜ਼ਬੂਤ ਲੰਮੀ ਚੇਨ | ਅਸਥਾਈ ਅਸਫਲਤਾਵਾਂ ਘਟਾਓ | `act` ਨੂੰ ਟਰਾਈ/ਐਕਸਪਟ + ਘਣਤਾ ਵਧਾਉਣ ਨਾਲ ਢੱਕੋ |
| ਰੁਬ੍ਰਿਕ ਸਕੋਰਿੰਗ | ਸੁਚਾਲਿਤ ਗੁਣਵੱਤਾ ਲੇਬਲ | ਸੁਧਾਰ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ | ਮਾਡਲ ਨੂੰ ਦੂਜਾ ਪਾਸ ਪ੍ਰੌਮਪਟ: "ਸਪਸ਼ਟੀਕਰਨ ਨੂੰ 1-5 ਦਰਜਾ ਦਿਓ" |
| ਵੇਕਟਰ ਮੈਮੋਰੀ | ਸੈਮੈਂਟਿਕ ਯਾਦ | ਧਨੀ ਲੰਮੀ ਮਿਆਦ ਲਈ ਸੰਦਰਭ | ਸਾਰਾਂ ਨੂੰ ਐम्बੈਡ ਕਰੋ, ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਿੱਚ ਸਿਖਰ-k ਪ੍ਰਾਪਤ ਕਰੋ |
| ਸਟੀਮਿੰਗ ਜਵਾਬ | ਤੇਜ਼ ਮਹਿਸੂਸ ਹੋਣ ਵਾਲਾ ਜਵਾਬ | ਵਰਤੋਂ ਵਿਕਾਸ | ਉਪਲਬਧ ਹੋਂਦਿਆਂ ਸਟੀਮਿੰਗ ਵਰਤੋਂ ਅਤੇ ਅਰਧ ਟੋਕਨ ਸੁੱਟੋ |
| ਨਿਰਧਾਰੀਤ ਟੈਸਟ | ਰਿਗ੍ਰੈਸ਼ਨ ਕੰਟਰੋਲ | ਸਥਿਰ CI | `temperature=0`, ਨਿਰਧਾਰਿਤ ਪ੍ਰੌਮਪਟ ਸੀਡਜ਼ ਨਾਲ ਚਲਾਓ |
| ਸਮਾਂਤਰ ਸ਼ਾਖਾਵਾਰ | ਤੇਜ਼ ਖੋਜ | ਜਾਇਦਾਦ | ਸੁਤੰਤਰ ਏਜੰਟ ਕਦਮ ਲਈ `concurrent.futures` ਵਰਤੋਂ |

#### ਟਰੇਸ ਰਿਕਾਰਡ ਉਦਾਹਰਨ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### ਸਧਾਰਨ ਮੁਲਾਂਕਣ ਪ੍ਰੌਮਪਟ

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

ਲੰਬੇ ਸਮੇਂ ਲਈ ਗੁਣਵੱਤਾ ਚਾਰਟ ਬਣਾਉਣ ਲਈ (`answer`, `rating`) ਜੋੜਨ ਕਰੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->