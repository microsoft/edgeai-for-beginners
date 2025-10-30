<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T19:57:32+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "en"
}
-->
# Session 5: Build AI-Powered Agents Fast with Foundry Local

## Abstract

Design and manage multi-role AI agents using Foundry Local’s low-latency, privacy-focused runtime. You’ll define agent roles, memory strategies, tool invocation patterns, and execution workflows. This session introduces scaffolding patterns that can be extended with Chainlit or LangGraph. The starter project builds on the existing agent architecture sample to include memory persistence and evaluation hooks.

## Learning Objectives

- **Define Roles**: System prompts and capability boundaries
- **Implement Memory**: Short-term (conversation), long-term (vector/file), ephemeral scratchpads
- **Scaffold Workflows**: Sequential, branching, and parallel agent steps
- **Integrate Tools**: Lightweight function tool invocation pattern
- **Evaluate**: Basic trace and rubric-driven outcome scoring

## Prerequisites

- Completion of Sessions 1–4
- Python with `foundry-local-sdk`, `openai`, optional `chainlit`
- Local models running (minimum `phi-4-mini`)

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

If running agents from macOS against a remote Windows host service:
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

Extend with `samples/05-agents/tools.py`:

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

Modify `agents_core.py` to enable simple tool syntax: users write `#tool:get_time`, and the agent incorporates tool output into the context before generating responses.

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


### 5. Starter Project: Extend `05-agent-architecture` (7 min)

Add:
1. Persistent memory layer (e.g., appending conversations to JSON lines)
2. Simple evaluation rubric: placeholders for factuality, clarity, and style
3. Optional Chainlit front-end (two tabs: conversation and traces)
4. Optional LangGraph-style state machine (if adding dependency) for branching decisions

## Validation Checklist

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Expect structured pipeline output with tool injection notes.

## Memory Strategies Overview

| Layer       | Purpose              | Example               |
|-------------|----------------------|-----------------------|
| Short-term  | Dialogue continuity  | Last N messages       |
| Episodic    | Session recall       | JSON per session      |
| Semantic    | Long-term retrieval  | Vector store of summaries |
| Scratchpad  | Reasoning steps      | Inline chain-of-thought (private) |

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

| Issue              | Cause                  | Resolution                     |
|--------------------|------------------------|---------------------------------|
| Repetitive answers | Context window too large/small | Adjust memory window parameter |
| Tool not invoked   | Incorrect syntax       | Use `#tool:tool_name` format   |
| Slow orchestration | Multiple cold models   | Pre-run warmup prompts         |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optional concept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Session Duration**: 30 min  
**Difficulty**: Advanced

## Sample Scenario & Workshop Mapping

| Workshop Script                                      | Scenario                                           | Objective                                      | Example Prompt                                |
|-----------------------------------------------------|---------------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Knowledge research bot producing executive-friendly summaries | Two-agent pipeline (research → editorial polish) with optional distinct models | Explain why edge inference matters for compliance. |
| (Extended) `tools.py` concept                       | Add time & token estimation tools                 | Demonstrate lightweight tool invocation pattern | #tool:get_time                                |

### Scenario Narrative

The compliance documentation team needs quick internal briefs sourced from local knowledge without sending drafts to cloud services. A researcher agent gathers concise factual points; an editor agent rewrites them for executive clarity. Distinct model aliases can be assigned to optimize latency (fast SLM) versus stylistic refinement (larger model only when necessary).

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

Persist each step to a JSONL file for later rubric scoring.

### Optional Enhancements

| Theme              | Enhancement                  | Benefit                     | Implementation Sketch       |
|--------------------|-----------------------------|----------------------------|-----------------------------|
| Multi-Model Roles  | Distinct models per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialization & speed      | Select alias env vars, call `chat_once` with per-role alias |
| Structured Traces  | JSON trace of each act(tool,input,latency,tokens) | Debug & evaluation          | Append dict to a list; write `.jsonl` at end |
| Memory Persistence | Reloadable dialog context   | Session continuity          | Dump `Agent.memory` to `sessions/<ts>.json` |
| Tool Registry      | Dynamic tool discovery      | Extensibility               | Maintain `TOOLS` dict & introspect names/descriptions |
| Retry & Backoff    | Robust long chains          | Reduce transient failures   | Wrap `act` with try/except + exponential backoff |
| Rubric Scoring     | Automated qualitative labels | Track improvements          | Secondary pass prompting model: "Rate clarity 1-5" |
| Vector Memory      | Semantic recall             | Rich long-term context      | Embed summaries, retrieve top-k into system message |
| Streaming Replies  | Faster perceived response   | UX improvement              | Use streaming once available and flush partial tokens |
| Deterministic Tests| Regression control          | Stable CI                   | Run with `temperature=0`, fixed prompt seeds |
| Parallel Branching | Faster exploration          | Throughput                  | Use `concurrent.futures` for independent agent steps |

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

Persist (`answer`, `rating`) pairs to build a historical quality graph.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.