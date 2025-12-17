<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-12-15T21:06:56+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "kn"
}
-->
# ಸೆಷನ್ 5: Foundry Local ಬಳಸಿ AI-ಚಾಲಿತ ಏಜೆಂಟ್ಗಳನ್ನು ವೇಗವಾಗಿ ನಿರ್ಮಿಸಿ

## ಸಾರಾಂಶ

Foundry Local ನ ಕಡಿಮೆ ವಿಳಂಬ, ಗೌಪ್ಯತೆ-ರಕ್ಷಿಸುವ ರನ್‌ಟೈಮ್ ಅನ್ನು ಉಪಯೋಗಿಸಿ ಬಹು-ಪಾತ್ರೆಯ AI ಏಜೆಂಟ್ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ ಮತ್ತು ಸಂಯೋಜಿಸಿ. ನೀವು ಏಜೆಂಟ್ ಪಾತ್ರಗಳು, ಮೆಮೊರಿ ತಂತ್ರಗಳು, ಉಪಕರಣ ಕರೆ ಮಾದರಿಗಳು ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣಾ ಗ್ರಾಫ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವಿರಿ. ಸೆಷನ್‌ನಲ್ಲಿ ನೀವು Chainlit ಅಥವಾ LangGraph ಬಳಸಿ ವಿಸ್ತರಿಸಬಹುದಾದ ಸ್ಕಾಫೋಲ್ಡಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಪರಿಚಯಿಸಲಾಗುತ್ತದೆ. ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್ ಈಗಿನ ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ ಮಾದರಿಯನ್ನು ವಿಸ್ತರಿಸಿ ಮೆಮೊರಿ ಸ್ಥಿರತೆ + ಮೌಲ್ಯಮಾಪನ ಹೂಕ್‌ಗಳನ್ನು ಸೇರಿಸುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

- **ಪಾತ್ರಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ**: ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಾಮರ್ಥ್ಯ ಗಡಿಗಳು
- **ಮೆಮೊರಿ ಅನುಷ್ಠಾನಗೊಳಿಸಿ**: ಚಿಕ್ಕ ಅವಧಿ (ಸಂವಾದ), ದೀರ್ಘ ಅವಧಿ (ವೆಕ್ಟರ್ / ಫೈಲ್), ತಾತ್ಕಾಲಿಕ ಸ್ಕ್ರಾಚ್‌ಪ್ಯಾಡ್‌ಗಳು
- **ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ಕಾಫೋಲ್ಡ್ ಮಾಡಿ**: ಕ್ರಮಬದ್ಧ, ಶಾಖಿತ ಮತ್ತು ಸಮಾಂತರ ಏಜೆಂಟ್ ಹಂತಗಳು
- **ಉಪಕರಣಗಳನ್ನು ಸಂಯೋಜಿಸಿ**: ಲಘು-ತೂಕದ ಫಂಕ್ಷನ್ ಉಪಕರಣ ಕರೆ ಮಾದರಿ
- **ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ**: ಮೂಲಭೂತ ಟ್ರೇಸ್ + ರೂಬ್ರಿಕ್ ಚಾಲಿತ ಫಲಿತಾಂಶ ಅಂಕನ

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- ಸೆಷನ್‌ಗಳು 1–4 ಪೂರ್ಣಗೊಂಡಿವೆ
- Python ನಲ್ಲಿ `foundry-local-sdk`, `openai`, ಐಚ್ಛಿಕವಾಗಿ `chainlit`
- ಸ್ಥಳೀಯ ಮಾದರಿಗಳು ಚಾಲನೆಯಲ್ಲಿವೆ (ಕನಿಷ್ಠ `phi-4-mini`)

### ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ಸ্নಿಪೆಟ್

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
  
macOS ನಿಂದ ದೂರದ Windows ಹೋಸ್ಟ್ ಸೇವೆಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡುತ್ತಿದ್ದರೆ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ಡೆಮೊ ಫ್ಲೋ (30 ನಿಮಿಷ)

### 1. ಏಜೆಂಟ್ ಪಾತ್ರಗಳು ಮತ್ತು ಮೆಮೊರಿ ವ್ಯಾಖ್ಯಾನಿಸಿ (7 ನಿಮಿಷ)

`samples/05-agents/agents_core.py` ರಚಿಸಿ:

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
  
### 2. CLI ಸ್ಕಾಫೋಲ್ಡಿಂಗ್ ಮಾದರಿ (3 ನಿಮಿಷ)

```powershell
python samples/05-agents/agents_core.py
```
  
### 3. ಉಪಕರಣ ಕರೆ ಸೇರಿಸಿ (7 ನಿಮಿಷ)

`samples/05-agents/tools.py` ನೊಂದಿಗೆ ವಿಸ್ತರಿಸಿ:

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
  
ಸರಳ ಉಪಕರಣ ಸಿಂಟ್ಯಾಕ್ಸ್ ಅನುಮತಿಸಲು `agents_core.py` ಅನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಿ: ಬಳಕೆದಾರರು `#tool:get_time` ಅನ್ನು ಬರೆಯುತ್ತಾರೆ ಮತ್ತು ಏಜೆಂಟ್ ಉತ್ಪಾದನೆಯ ಮೊದಲು ಉಪಕರಣದ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಸಂದರ್ಭದಲ್ಲಿ ವಿಸ್ತರಿಸುತ್ತದೆ.

### 4. ಸಂಯೋಜಿತ ಕಾರ್ಯಪ್ರವಾಹ (6 ನಿಮಿಷ)

`samples/05-agents/orchestrator.py` ರಚಿಸಿ:

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
  
### 5. ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್: `05-agent-architecture` ವಿಸ್ತರಿಸಿ (7 ನಿಮಿಷ)

ಸೇರಿಸಿ:  
1. ಸ್ಥಿರ ಮೆಮೊರಿ ಪದರ (ಉದಾ: ಸಂವಾದಗಳ JSON ಸಾಲುಗಳ ಸೇರಿಸುವಿಕೆ)  
2. ಸರಳ ಮೌಲ್ಯಮಾಪನ ರೂಬ್ರಿಕ್: ವಾಸ್ತವಿಕತೆ / ಸ್ಪಷ್ಟತೆ / ಶೈಲಿ ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್‌ಗಳು  
3. ಐಚ್ಛಿಕ Chainlit ಮುಂಭಾಗ (ಎರಡು ಟ್ಯಾಬ್‌ಗಳು: ಸಂವಾದ ಮತ್ತು ಟ್ರೇಸ್‌ಗಳು)  
4. ಐಚ್ಛಿಕ LangGraph ಶೈಲಿ ಸ್ಥಿತಿ ಯಂತ್ರ (ಆಧಾರ ಸೇರಿಸಿದರೆ) ಶಾಖಿತ ನಿರ್ಣಯಗಳಿಗೆ  

## ಮಾನ್ಯತೆ ಪರಿಶೀಲನಾ ಪಟ್ಟಿಕೆ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
ಉಪಕರಣ ಇಂಜೆಕ್ಷನ್ ಟಿಪ್ಪಣಿಯೊಂದಿಗೆ ರಚನಾತ್ಮಕ ಪೈಪ್‌ಲೈನ್ ಔಟ್‌ಪುಟ್ ನಿರೀಕ್ಷಿಸಿ.

## ಮೆಮೊರಿ ತಂತ್ರಗಳ ಅವಲೋಕನ

| ಪದರ | ಉದ್ದೇಶ | ಉದಾಹರಣೆ |
|-------|---------|---------|
| ಚಿಕ್ಕ ಅವಧಿ | ಸಂವಾದ ನಿರಂತರತೆ | ಕೊನೆಯ N ಸಂದೇಶಗಳು |
| ಘಟನಾತ್ಮಕ | ಸೆಷನ್ ಸ್ಮರಣೆ | ಪ್ರತಿ ಸೆಷನ್‌ಗೆ JSON |
| ಅರ್ಥಾತ್ಮಕ | ದೀರ್ಘಾವಧಿ ಹಿಂತೆಗೆದುಕೊಳ್ಳುವಿಕೆ | ಸಾರಾಂಶಗಳ ವೆಕ್ಟರ್ ಸ್ಟೋರ್ |
| ಸ್ಕ್ರಾಚ್‌ಪ್ಯಾಡ್ | ತರ್ಕ ಹಂತಗಳು | ಇನ್‌ಲೈನ್ ಚೈನ್-ಆಫ್-ಥಾಟ್ (ಖಾಸಗಿ) |

## ಮೌಲ್ಯಮಾಪನ ಹೂಕ್‌ಗಳು (ಸಿದ್ಧಾಂತಾತ್ಮಕ)

```python
evaluation = {
  "factuality": None,  # ಕೈಯಿಂದ ಅಥವಾ ಅನುಮಾನಾತ್ಮಕ
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  
## ಸಮಸ್ಯೆ ಪರಿಹಾರ

| ಸಮಸ್ಯೆ | ಕಾರಣ | ಪರಿಹಾರ |
|-------|------|------------|
| ಪುನರಾವರ್ತಿತ ಉತ್ತರಗಳು | ಸಂದರ್ಭ ವಿಂಡೋ ತುಂಬಾ ದೊಡ್ಡ/ಸಣ್ಣ | ಮೆಮೊರಿ ವಿಂಡೋ ಪರಿಮಾಣವನ್ನು ಹೊಂದಿಸಿ |
| ಉಪಕರಣ ಕರೆ ಆಗುತ್ತಿಲ್ಲ | ತಪ್ಪು ಸಿಂಟ್ಯಾಕ್ಸ್ | `#tool:tool_name` ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸಿ |
| ನಿಧಾನ ಸಂಯೋಜನೆ | ಅನೇಕ ಶೀತಲ ಮಾದರಿಗಳು | ಪೂರ್ವ ಚಾಲನೆ ವಾರ್ಮಪ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು |

## ಉಲ್ಲೇಖಗಳು

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (ಐಚ್ಛಿಕ ಕಲ್ಪನೆ): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**ಸೆಷನ್ ಅವಧಿ**: 30 ನಿಮಿಷ  
**ಕಷ್ಟದ ಮಟ್ಟ**: ಉನ್ನತ

## ಮಾದರಿ ದೃಶ್ಯ ಮತ್ತು ಕಾರ್ಯಾಗಾರ ನಕ್ಷೆ

| ಕಾರ್ಯಾಗಾರ ಸ್ಕ್ರಿಪ್ಟ್ | ದೃಶ್ಯ | ಉದ್ದೇಶ | ಉದಾಹರಣಾ ಪ್ರಾಂಪ್ಟ್ |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ಜ್ಞಾನ ಸಂಶೋಧನಾ ಬಾಟ್ ಕಾರ್ಯನಿರ್ವಹಣಾ ಸ್ನೇಹಿ ಸಾರಾಂಶಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ | ಎರಡು ಏಜೆಂಟ್ ಪೈಪ್‌ಲೈನ್ (ಸಂಶೋಧನೆ → ಸಂಪಾದಕೀಯ ಶೈಲಿ) ಐಚ್ಛಿಕ ವಿಭಿನ್ನ ಮಾದರಿಗಳೊಂದಿಗೆ | ಅನುಪಾಲನೆಗಾಗಿ ಎಡ್ಜ್ ಇನ್ಫರೆನ್ಸ್ ಮಹತ್ವವನ್ನು ವಿವರಿಸಿ. |
| (ವಿಸ್ತರಿಸಿದ) `tools.py` ಕಲ್ಪನೆ | ಸಮಯ ಮತ್ತು ಟೋಕನ್ ಅಂದಾಜು ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸಿ | ಲಘು-ತೂಕದ ಉಪಕರಣ ಕರೆ ಮಾದರಿಯನ್ನು ಪ್ರದರ್ಶಿಸಿ | #tool:get_time |

### ದೃಶ್ಯ ಕಥನ  
ಅನುಪಾಲನೆ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ತಂಡವು ಸ್ಥಳೀಯ ಜ್ಞಾನದಿಂದ ವೇಗದ ಆಂತರಿಕ ಸಾರಾಂಶಗಳನ್ನು ಬೇಕಾಗುತ್ತದೆ, ಕ್ಲೌಡ್ ಸೇವೆಗಳಿಗೆ ಡ್ರಾಫ್ಟ್‌ಗಳನ್ನು ಕಳುಹಿಸದೆ. ಸಂಶೋಧಕ ಏಜೆಂಟ್ ಸಂಕ್ಷಿಪ್ತ ವಾಸ್ತವಿಕ ಬಿಂದುಗಳನ್ನು ಸಂಗ್ರಹಿಸುತ್ತಾನೆ; ಸಂಪಾದಕ ಏಜೆಂಟ್ ಕಾರ್ಯನಿರ್ವಹಣಾ ಸ್ಪಷ್ಟತೆಯಿಗಾಗಿ ಮರುಬರೆಯುತ್ತಾನೆ. ವಿಭಿನ್ನ ಮಾದರಿ ಅಲಿಯಾಸ್‌ಗಳನ್ನು ವಿಳಂಬ (ವೇಗದ SLM) ಮತ್ತು ಶೈಲಿ ಸುಧಾರಣೆ (ಮಾತ್ರ ಅಗತ್ಯವಿರುವಾಗ ದೊಡ್ಡ ಮಾದರಿ) ಗಾಗಿ ನಿಯೋಜಿಸಬಹುದು.

### ಉದಾಹರಣಾ ಬಹು-ಮಾದರಿ ಪರಿಸರ  
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```
  
### ಟ್ರೇಸ್ ರಚನೆ (ಐಚ್ಛಿಕ)  
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
  
ಪ್ರತಿ ಹಂತವನ್ನು JSONL ಫೈಲ್‌ಗೆ ಉಳಿಸಿ ನಂತರ ರೂಬ್ರಿಕ್ ಅಂಕನಕ್ಕೆ.

### ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳು

| ಥೀಮ್ | ಸುಧಾರಣೆ | ಲಾಭ | ಅನುಷ್ಠಾನ ರೇಖಾಚಿತ್ರ |
|-------|------------|---------|-----------------------|
| ಬಹು-ಮಾದರಿ ಪಾತ್ರಗಳು | ಪ್ರತಿ ಏಜೆಂಟ್‌ಗೆ ವಿಭಿನ್ನ ಮಾದರಿಗಳು (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ವಿಶೇಷೀಕರಣ ಮತ್ತು ವೇಗ | ಅಲಿಯಾಸ್ ಪರಿಸರ ಚರಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ, ಪ್ರತಿ ಪಾತ್ರದ ಅಲಿಯಾಸ್‌ನೊಂದಿಗೆ `chat_once` ಕರೆ ಮಾಡಿ |
| ರಚನಾತ್ಮಕ ಟ್ರೇಸ್‌ಗಳು | ಪ್ರತಿ ಕ್ರಿಯೆಯ JSON ಟ್ರೇಸ್ (ಉಪಕರಣ, ಇನ್‌ಪುಟ್, ವಿಳಂಬ, ಟೋಕನ್‌ಗಳು) | ಡಿಬಗ್ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ | ಡಿಕ್ಷನರಿ ಪಟ್ಟಿಗೆ ಸೇರಿಸಿ; ಕೊನೆಯಲ್ಲಿ `.jsonl` ಬರೆಯಿರಿ |
| ಮೆಮೊರಿ ಸ್ಥಿರತೆ | ಮರುಲೋಡ್ ಮಾಡಬಹುದಾದ ಸಂವಾದ ಸಂದರ್ಭ | ಸೆಷನ್ ನಿರಂತರತೆ | `Agent.memory` ಅನ್ನು `sessions/<ts>.json` ಗೆ ಡಂಪ್ ಮಾಡಿ |
| ಉಪಕರಣ ರಿಜಿಸ್ಟ್ರಿ | ಡೈನಾಮಿಕ್ ಉಪಕರಣ ಪತ್ತೆ | ವಿಸ್ತರಣೀಯತೆ | `TOOLS` ಡಿಕ್ಷನರಿ ನಿರ್ವಹಿಸಿ ಮತ್ತು ಹೆಸರು/ವಿವರಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ |
| ಮರುಪ್ರಯತ್ನ ಮತ್ತು ಬ್ಯಾಕ್ಓಫ್ | ಬಲವಾದ ದೀರ್ಘ ಸರಪಳಿ | ತಾತ್ಕಾಲಿಕ ವೈಫಲ್ಯಗಳನ್ನು ಕಡಿಮೆ ಮಾಡಿ | `act` ಅನ್ನು try/except + ಘಾತಾಕಾರ ಬ್ಯಾಕ್ಓಫ್‌ನೊಂದಿಗೆ ಮುಚ್ಚಿ |
| ರೂಬ್ರಿಕ್ ಅಂಕನ | ಸ್ವಯಂಚಾಲಿತ ಗುಣಮಟ್ಟ ಲೇಬಲ್‌ಗಳು | ಸುಧಾರಣೆಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ | ಎರಡನೇ ಹಂತ ಪ್ರಾಂಪ್ಟ್: "ಸ್ಪಷ್ಟತೆ 1-5 ರೇಟ್ ಮಾಡಿ" |
| ವೆಕ್ಟರ್ ಮೆಮೊರಿ | ಅರ್ಥಾತ್ಮಕ ಹಿಂತೆಗೆದುಕೊಳ್ಳುವಿಕೆ | ಶ್ರೀಮಂತ ದೀರ್ಘಾವಧಿ ಸಂದರ್ಭ | ಸಾರಾಂಶಗಳನ್ನು ಎम्बೆಡ್ ಮಾಡಿ, ಟಾಪ್-k ಅನ್ನು ಸಿಸ್ಟಮ್ ಸಂದೇಶಕ್ಕೆ ಹಿಂತೆಗೆದುಕೊಳ್ಳಿ |
| ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳು | ವೇಗವಾದ ಪ್ರತಿಕ್ರಿಯೆ ಅನುಭವ | ಬಳಕೆದಾರ ಅನುಭವ ಸುಧಾರಣೆ | ಲಭ್ಯವಿದ್ದಾಗ ಸ್ಟ್ರೀಮಿಂಗ್ ಬಳಸಿ ಮತ್ತು ಭಾಗಶಃ ಟೋಕನ್‌ಗಳನ್ನು ಫ್ಲಷ್ ಮಾಡಿ |
| ನಿರ್ಧಾರಾತ್ಮಕ ಪರೀಕ್ಷೆಗಳು | ರಿಗ್ರೆಶನ್ ನಿಯಂತ್ರಣ | ಸ್ಥಿರ CI | `temperature=0`, ನಿಶ್ಚಿತ ಪ್ರಾಂಪ್ಟ್ ಬೀಜಗಳೊಂದಿಗೆ ಚಾಲನೆ ಮಾಡಿ |
| ಸಮಾಂತರ ಶಾಖಿತ | ವೇಗವಾದ ಅನ್ವೇಷಣೆ | ಥ್ರೂಪುಟ್ | ಸ್ವತಂತ್ರ ಏಜೆಂಟ್ ಹಂತಗಳಿಗೆ `concurrent.futures` ಬಳಸಿ |

#### ಟ್ರೇಸ್ ದಾಖಲೆ ಉದಾಹರಣೆ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  
#### ಸರಳ ಮೌಲ್ಯಮಾಪನ ಪ್ರಾಂಪ್ಟ್

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
ಇತಿಹಾಸಾತ್ಮಕ ಗುಣಮಟ್ಟ ಗ್ರಾಫ್ ನಿರ್ಮಿಸಲು (`answer`, `rating`) ಜೋಡಿಗಳನ್ನು ಉಳಿಸಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->