<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-12-15T21:05:45+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ml"
}
-->
# സെഷൻ 5: Foundry Local ഉപയോഗിച്ച് എഐ-പവർഡ് ഏജന്റുകൾ വേഗത്തിൽ നിർമ്മിക്കുക

## സംക്ഷേപം

Foundry Local ന്റെ കുറഞ്ഞ വൈകിയുള്ളതും സ്വകാര്യത സംരക്ഷിക്കുന്ന റൺടൈം ഉപയോഗിച്ച് മൾട്ടി-റോൾ എഐ ഏജന്റുകൾ രൂപകൽപ്പന ചെയ്ത് ഓർക്കസ്ട്രേറ്റ് ചെയ്യുക. നിങ്ങൾ ഏജന്റ് റോളുകൾ, മെമ്മറി തന്ത്രങ്ങൾ, ടൂൾ വിളിക്കൽ മാതൃകകൾ, എക്സിക്യൂഷൻ ഗ്രാഫുകൾ നിർവചിക്കും. സെഷൻ Chainlit അല്ലെങ്കിൽ LangGraph ഉപയോഗിച്ച് നീട്ടാവുന്ന സ്കാഫോൾഡിംഗ് മാതൃകകൾ പരിചയപ്പെടുത്തുന്നു. സ്റ്റാർട്ടർ പ്രോജക്ട് നിലവിലുള്ള ഏജന്റ് ആർക്കിടെക്ചർ സാമ്പിൾ മെമ്മറി സ്ഥിരതയും മൂല്യനിർണയ ഹുക്കുകളും ചേർക്കാൻ വിപുലീകരിക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

- **റോളുകൾ നിർവചിക്കുക**: സിസ്റ്റം പ്രോംപ്റ്റുകളും കഴിവ് പരിധികളും  
- **മെമ്മറി നടപ്പിലാക്കുക**: ചെറുകാല (സംഭാഷണം), ദീർഘകാല (വെക്ടർ / ഫയൽ), താൽക്കാലിക സ്ക്രാച്ച്പാഡുകൾ  
- **വർക്ക്ഫ്ലോകൾ സ്കാഫോൾഡ് ചെയ്യുക**: അനുക്രമ, ശാഖാഗത, സമാന്തര ഏജന്റ് ഘട്ടങ്ങൾ  
- **ടൂളുകൾ സംയോജിപ്പിക്കുക**: ലഘു ഫംഗ്ഷൻ ടൂൾ വിളിക്കൽ മാതൃക  
- **മൂല്യനിർണയം നടത്തുക**: അടിസ്ഥാന ട്രേസ് + റൂബ്രിക്-നിർദ്ദേശിത ഫലം സ്കോറിംഗ്  

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- സെഷനുകൾ 1–4 പൂർത്തിയായി  
- Python `foundry-local-sdk`, `openai`, ഐച്ഛികം `chainlit`  
- ലോക്കൽ മോഡലുകൾ പ്രവർത്തനക്ഷമം (കുറഞ്ഞത് `phi-4-mini`)  

### ക്രോസ്-പ്ലാറ്റ്ഫോം പരിസ്ഥിതി സ്നിപ്പറ്റ്

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
  
macOS-ൽ നിന്ന് റിമോട്ട് Windows ഹോസ്റ്റ് സർവീസിനെതിരെ ഏജന്റുകൾ ഓടിക്കുന്നുവെങ്കിൽ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ഡെമോ ഫ്ലോ (30 മിനിറ്റ്)

### 1. ഏജന്റ് റോളുകളും മെമ്മറിയും നിർവചിക്കുക (7 മിനിറ്റ്)

`samples/05-agents/agents_core.py` സൃഷ്ടിക്കുക:  

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
  
### 2. CLI സ്കാഫോൾഡിംഗ് മാതൃക (3 മിനിറ്റ്)

```powershell
python samples/05-agents/agents_core.py
```
  
### 3. ടൂൾ വിളിക്കൽ ചേർക്കുക (7 മിനിറ്റ്)

`samples/05-agents/tools.py` ഉപയോഗിച്ച് വിപുലീകരിക്കുക:  

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
  
`agents_core.py` ലളിതമായ ടൂൾ സിന്റാക്സ് അനുവദിക്കാൻ മാറ്റം വരുത്തുക: ഉപയോക്താവ് `#tool:get_time` എഴുതുമ്പോൾ ഏജന്റ് ടൂൾ ഔട്ട്പുട്ട് സൃഷ്ടിക്കുമ്ബോൾ കോൺടെക്സ്റ്റിലേക്ക് വിപുലീകരിക്കും.

### 4. ഓർക്കസ്ട്രേറ്റഡ് വർക്ക്ഫ്ലോ (6 മിനിറ്റ്)

`samples/05-agents/orchestrator.py` സൃഷ്ടിക്കുക:  

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
  
### 5. സ്റ്റാർട്ടർ പ്രോജക്ട്: `05-agent-architecture` വിപുലീകരിക്കുക (7 മിനിറ്റ്)

ചേർക്കുക:  
1. സ്ഥിരതയുള്ള മെമ്മറി ലെയർ (ഉദാ: സംഭാഷണങ്ങളുടെ JSON ലൈൻസ് അപ്‌എൻഡ്)  
2. ലളിതമായ മൂല്യനിർണയ റൂബ്രിക്: വാസ്തവസത്യവും വ്യക്തതയും ശൈലിയും പ്ലേസ്ഹോൾഡറുകൾ  
3. ഐച്ഛിക Chainlit ഫ്രണ്ട്-എൻഡ് (രണ്ട് ടാബുകൾ: സംഭാഷണം & ട്രേസുകൾ)  
4. ഐച്ഛിക LangGraph ശൈലി സ്റ്റേറ്റ് മെഷീൻ (ഡിപ്പെൻഡൻസി ചേർക്കുമ്പോൾ) ശാഖാഗത തീരുമാനങ്ങൾക്ക്  

## സാധുത പരിശോധന പട്ടിക

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
ടൂൾ ഇൻജക്ഷൻ കുറിപ്പോടെ ഘടനാപരമായ പൈപ്പ്‌ലൈൻ ഔട്ട്പുട്ട് പ്രതീക്ഷിക്കുക.

## മെമ്മറി തന്ത്രങ്ങൾ അവലോകനം

| ലെയർ | ഉദ്ദേശ്യം | ഉദാഹരണം |
|-------|---------|---------|
| ചെറുകാല | സംഭാഷണ തുടർച്ച | അവസാന N സന്ദേശങ്ങൾ |
| എപ്പിസോഡിക് | സെഷൻ ഓർമ്മ | സെഷൻപ്രതി JSON |
| സെമാന്റിക് | ദീർഘകാല വീണ്ടെടുക്കൽ | സംഗ്രഹങ്ങളുടെ വെക്ടർ സ്റ്റോർ |
| സ്ക്രാച്ച്പാഡ് | ചിന്തന ഘട്ടങ്ങൾ | ഇൻലൈൻ ചൈൻ-ഓഫ്-തോട്ട് (സ്വകാര്യ) |

## മൂല്യനിർണയ ഹുക്കുകൾ (സങ്കൽപാത്മകമായി)

```python
evaluation = {
  "factuality": None,  # മാനുവൽ അല്ലെങ്കിൽ ഹ്യൂറിസ്റ്റിക്
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  
## പ്രശ്നപരിഹാരം

| പ്രശ്നം | കാരണം | പരിഹാരം |
|-------|--------|----------|
| ആവർത്തിക്കുന്ന ഉത്തരങ്ങൾ | കോൺടെക്സ്റ്റ് വിൻഡോ വളരെ വലിയതോ ചെറുതോ | മെമ്മറി വിൻഡോ പാരാമീറ്റർ ട്യൂൺ ചെയ്യുക |
| ടൂൾ വിളിക്കപ്പെടുന്നില്ല | തെറ്റായ സിന്റാക്സ് | `#tool:tool_name` ഫോർമാറ്റ് ഉപയോഗിക്കുക |
| ഓർക്കസ്ട്രേഷൻ മന്ദഗതിയിലുള്ളത് | പല തണുത്ത മോഡലുകളും | പ്രീ-റൺ വാർംഅപ്പ് പ്രോംപ്റ്റുകൾ ഉപയോഗിക്കുക |

## റഫറൻസുകൾ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (ഐച്ഛിക സങ്കൽപം): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**സെഷൻ ദൈർഘ്യം**: 30 മിനിറ്റ്  
**പ്രയാസം**: ഉയർന്നതരം  

## സാമ്പിൾ സീനാരിയോ & വർക്ക്‌ഷോപ്പ് മാപ്പിംഗ്

| വർക്ക്‌ഷോപ്പ് സ്ക്രിപ്റ്റ് | സീനാരിയോ | ലക്ഷ്യം | ഉദാഹരണ പ്രോംപ്റ്റ് |
|-------------------------|----------|---------|---------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | എക്സിക്യൂട്ടീവ്-സൗഹൃദ സംഗ്രഹങ്ങൾ സൃഷ്ടിക്കുന്ന നോളജ് റിസർച്ച് ബോട്ട് | രണ്ട് ഏജന്റ് പൈപ്പ്‌ലൈൻ (റിസർച്ച് → എഡിറ്റോറിയൽ പോളിഷ്) ഐച്ഛിക വ്യത്യസ്ത മോഡലുകളോടെ | എഡ്ജ് ഇൻഫറൻസ് പാലനത്തിന് എന്തുകൊണ്ട് പ്രധാനമാണെന്ന് വിശദീകരിക്കുക. |
| (വിപുലീകരിച്ച) `tools.py` സങ്കൽപം | സമയം & ടോക്കൺ അളവുകൾ ചേർക്കുക | ലഘു ടൂൾ വിളിക്കൽ മാതൃക പ്രദർശിപ്പിക്കുക | #tool:get_time |

### സീനാരിയോ വിവരണം  
കമ്പ്ലയൻസ് ഡോക്യുമെന്റേഷൻ ടീം ക്ലൗഡ് സർവീസുകളിലേക്ക് ഡ്രാഫ്റ്റുകൾ അയക്കാതെ ലോക്കൽ നോളജ് ഉപയോഗിച്ച് വേഗത്തിലുള്ള ആഭ്യന്തര ബ്രീഫുകൾ ആവശ്യപ്പെടുന്നു. ഒരു റിസർചർ ഏജന്റ് സംക്ഷിപ്ത വാസ്തവ ബുള്ളറ്റുകൾ ശേഖരിക്കുന്നു; ഒരു എഡിറ്റർ ഏജന്റ് എക്സിക്യൂട്ടീവ് വ്യക്തതയ്ക്കായി പുനഃരചിക്കുന്നു. വ്യത്യസ്ത മോഡൽ അലിയാസുകൾ വൈകിയുള്ളതും ശൈലിപരമായ മെച്ചപ്പെടുത്തലും (വേഗത്തിലുള്ള SLM vs വലിയ മോഡൽ ആവശ്യമായപ്പോൾ മാത്രം) മെച്ചപ്പെടുത്താൻ അനുവദിക്കുന്നു.

### ഉദാഹരണ മൾട്ടി-മോഡൽ പരിസ്ഥിതി  
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```
  
### ട്രേസ് ഘടന (ഐച്ഛികം)  
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
  
പ്രതിയ ഘട്ടവും JSONL ഫയലായി സ്ഥിരമാക്കുക പിന്നീട് റൂബ്രിക് സ്കോറിംഗിനായി.

### ഐച്ഛിക മെച്ചപ്പെടുത്തലുകൾ

| തീം | മെച്ചപ്പെടുത്തൽ | ഗുണം | നടപ്പാക്കൽ സ്കെച്ച് |
|-------|--------------|-------|---------------------|
| മൾട്ടി-മോഡൽ റോളുകൾ | ഏജന്റ് ഓരോരുത്തർക്കും വ്യത്യസ്ത മോഡലുകൾ (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | പ്രത്യേകതയും വേഗതയും | അലിയാസ് എൻവൈറൺമെന്റ് വേരിയബിളുകൾ തിരഞ്ഞെടുക്കുക, per-role അലിയാസോടെ `chat_once` വിളിക്കുക |
| ഘടനാപരമായ ട്രേസുകൾ | ഓരോ പ്രവർത്തനത്തിന്റെ JSON ട്രേസ് (ടൂൾ, ഇൻപുട്ട്, വൈകിയുള്ളത്, ടോക്കണുകൾ) | ഡീബഗ് & മൂല്യനിർണയം | ലിസ്റ്റിലേക്ക് ഡിക്ഷണറി ചേർക്കുക; അവസാനം `.jsonl` എഴുതുക |
| മെമ്മറി സ്ഥിരത | ഡയലോഗ് കോൺടെക്സ്റ്റ് പുനഃലോഡ് ചെയ്യാവുന്നതായി | സെഷൻ തുടർച്ച | `Agent.memory` `sessions/<ts>.json` ആയി ഡംപ് ചെയ്യുക |
| ടൂൾ രജിസ്ട്രി | ഡൈനാമിക് ടൂൾ കണ്ടെത്തൽ | വിപുലീകരണക്ഷമത | `TOOLS` ഡിക്ഷണറി പരിപാലിക്കുക & പേരുകൾ/വിവരണങ്ങൾ ഇൻട്രോസ്പെക്ട് ചെയ്യുക |
| റിട്രൈ & ബാക്ക്ഓഫ് | ദീർഘചെയിൻ തകരാറുകൾ കുറയ്ക്കുക | താൽക്കാലിക പരാജയങ്ങൾ കുറയ്ക്കുക | `act` try/except + exponential backoff ഉപയോഗിച്ച് റാപ്പ് ചെയ്യുക |
| റൂബ്രിക് സ്കോറിംഗ് | സ്വയം പ്രവർത്തിക്കുന്ന ഗുണനിലവാര ലേബലുകൾ | മെച്ചപ്പെടുത്തലുകൾ ട്രാക്ക് ചെയ്യുക | രണ്ടാം പാസ് പ്രോംപ്റ്റ്: "വ്യക്തത 1-5 റേറ്റ് ചെയ്യുക" |
| വെക്ടർ മെമ്മറി | സെമാന്റിക് ഓർമ്മ | സമൃദ്ധമായ ദീർഘകാല കോൺടെക്സ്റ്റ് | സംഗ്രഹങ്ങൾ എംബെഡ് ചെയ്ത് ടോപ്പ്-കെ തിരികെ സിസ്റ്റം സന്ദേശത്തിൽ ഉൾപ്പെടുത്തുക |
| സ്ട്രീമിംഗ് മറുപടികൾ | വേഗത്തിലുള്ള പ്രതികരണം | ഉപയോക്തൃ അനുഭവം മെച്ചപ്പെടുത്തുക | സ്ട്രീമിംഗ് ലഭ്യമായാൽ ഉപയോഗിച്ച് ഭാഗിക ടോക്കണുകൾ ഫ്ലഷ് ചെയ്യുക |
| നിർണ്ണായക പരീക്ഷണങ്ങൾ | റിഗ്രഷൻ നിയന്ത്രണം | സ്ഥിരതയുള്ള CI | `temperature=0`, സ്ഥിരമായ പ്രോംപ്റ്റ് സീഡുകൾ ഉപയോഗിച്ച് ഓടിക്കുക |
| സമാന്തര ശാഖാഗതം | വേഗത്തിലുള്ള പരീക്ഷണം | ത്രൂപുട്ട് | സ്വതന്ത്ര ഏജന്റ് ഘട്ടങ്ങൾക്ക് `concurrent.futures` ഉപയോഗിക്കുക |

#### ട്രേസ് റെക്കോർഡ് ഉദാഹരണം

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  
#### ലളിതമായ മൂല്യനിർണയ പ്രോംപ്റ്റ്

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
(`answer`, `rating`) ജോഡികൾ സ്ഥിരമാക്കി ചരിത്ര ഗുണനിലവാര ഗ്രാഫ് നിർമ്മിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ പ്രാമാണികമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->