# Session 5: How to Build AI-Powered Agents Quick with Foundry Local

## Abstract

Learn how to design and manage multi-role AI agents using Foundry Local wey dey run fast and dey protect privacy. You go fit define agent roles, memory strategies, tool invocation patterns, and execution graphs. This session go show you scaffolding patterns wey you fit use with Chainlit or LangGraph. Starter project go expand the agent architecture sample wey dey already to add memory persistence plus evaluation hooks.

## Learning Objectives

- **Define Roles**: System prompts & capability boundaries
- **Implement Memory**: Short-term (conversation), long-term (vector / file), ephemeral scratchpads
- **Scaffold Workflows**: Sequential, branching, and parallel agent steps
- **Integrate Tools**: Lightweight function tool calling pattern
- **Evaluate**: Basic trace + rubric-driven outcome scoring

## Prerequisites

- Sessions 1–4 don complete
- Python with `foundry-local-sdk`, `openai`, optional `chainlit`
- Local models dey run (at least `phi-4-mini`)

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

If you dey run agents from macOS against remote Windows host service:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo Flow (30 min)

### 1. Define Agent Roles & Memory (7 min)

Create `samples/05-agents/agents_core.py`:

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

### 2. CLI Scaffolding Pattern (3 min)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Add Tool Invocation (7 min)

Expand with `samples/05-agents/tools.py`:

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

Change `agents_core.py` so agent fit use simple tool syntax: user go write `#tool:get_time` and agent go add tool output into context before e generate response.

### 4. Orchestrated Workflow (6 min)

Create `samples/05-agents/orchestrator.py`:

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

### 5. Starter Project: Expand `05-agent-architecture` (7 min)

Add:
1. Persistent memory layer (e.g., JSON lines append of conversations)
2. Simple evaluation rubric: factuality / clarity / style placeholders
3. Optional Chainlit front-end (two tabs: conversation & traces)
4. Optional LangGraph style state machine (if you wan add dependency) for branching decisions

## Validation Checklist

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Expect structured pipeline output with tool injection note.

## Memory Strategies Overview

| Layer | Purpose | Example |
|-------|---------|---------|
| Short-term | Dialogue continuity | Last N messages |
| Episodic | Session recall | JSON per session |
| Semantic | Long-term retrieval | Vector store of summaries |
| Scratchpad | Reasoning steps | Inline chain-of-thought (private) |

## Evaluation Hooks (Conceptual)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Troubleshooting

| Issue | Cause | Resolution |
|-------|------|------------|
| Repetitive answers | Context window too large/small | Adjust memory window parameter |
| Tool no dey work | Wrong syntax | Use `#tool:tool_name` format |
| Slow orchestration | Multiple cold models | Pre-run warmup prompts |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optional concept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Session Duration**: 30 min  
**Difficulty**: Advanced

## Sample Scenario & Workshop Mapping

| Workshop Script | Scenario | Objective | Example Prompt |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Knowledge research bot wey dey produce executive-friendly summaries | Two-agent pipeline (research → editorial polish) with optional distinct models | Explain why edge inference dey important for compliance. |
| (Extended) `tools.py` concept | Add time & token estimation tools | Show lightweight tool invocation pattern | #tool:get_time |

### Scenario Narrative
The compliance documentation team need quick internal briefs wey dem go source from local knowledge without sending drafts to cloud services. Researcher agent go gather short factual points; editor agent go rewrite am for executive clarity. You fit assign different model aliases to improve speed (fast SLM) vs stylistic refinement (bigger model only when e dey necessary).

### Example Multi-Model Environment
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

Save each step to a JSONL file for later rubric scoring.

### Optional Enhancements

| Theme | Enhancement | Benefit | Implementation Sketch |
|-------|------------|---------|-----------------------|
| Multi-Model Roles | Different models for each agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialization & speed | Select alias env vars, call `chat_once` with per-role alias |
| Structured Traces | JSON trace of each act(tool,input,latency,tokens) | Debug & evaluation | Add dict to a list; save `.jsonl` at the end |
| Memory Persistence | Reloadable dialog context | Session continuity | Save `Agent.memory` to `sessions/<ts>.json` |
| Tool Registry | Dynamic tool discovery | Extensibility | Keep `TOOLS` dict & check names/desc |
| Retry & Backoff | Strong long chains | Reduce temporary failures | Use try/except + exponential backoff for `act` |
| Rubric Scoring | Automated qualitative labels | Track improvements | Secondary pass prompting model: "Rate clarity 1-5" |
| Vector Memory | Semantic recall | Rich long-term context | Embed summaries, retrieve top-k into system message |
| Streaming Replies | Faster perceived response | UX improvement | Use streaming when e dey available and flush partial tokens |
| Deterministic Tests | Regression control | Stable CI | Run with `temperature=0`, fixed prompt seeds |
| Parallel Branching | Faster exploration | Throughput | Use `concurrent.futures` for independent agent steps |

#### Trace Record Example

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Simple Evaluation Prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Save (`answer`, `rating`) pairs to build historical quality graph.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for di native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->