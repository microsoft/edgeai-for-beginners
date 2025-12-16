<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-12-15T21:04:30+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "te"
}
-->
# సెషన్ 5: Foundry Local తో AI-పవర్డ్ ఏజెంట్లను వేగంగా నిర్మించండి

## సారాంశం

Foundry Local యొక్క తక్కువ-విలంబన, గోప్యతా పరిరక్షణ రన్‌టైమ్‌ను ఉపయోగించి బహుళ పాత్ర AI ఏజెంట్లను డిజైన్ చేసి సమన్వయ పరచండి. మీరు ఏజెంట్ పాత్రలు, మెమరీ వ్యూహాలు, టూల్ పిలుపు నమూనాలు, మరియు అమలు గ్రాఫ్‌లను నిర్వచిస్తారు. ఈ సెషన్ Chainlit లేదా LangGraph తో విస్తరించగల స్కాఫోల్డింగ్ నమూనాలను పరిచయం చేస్తుంది. స్టార్టర్ ప్రాజెక్ట్ ఇప్పటికే ఉన్న ఏజెంట్ ఆర్కిటెక్చర్ నమూనాను మెమరీ నిల్వ + మూల్యాంకన హుక్స్ తో విస్తరించుతుంది.

## నేర్చుకునే లక్ష్యాలు

- **పాత్రలను నిర్వచించండి**: సిస్టమ్ ప్రాంప్ట్‌లు & సామర్థ్య పరిమితులు  
- **మెమరీ అమలు చేయండి**: తాత్కాలిక (సంభాషణ), దీర్ఘకాలిక (వెక్టర్ / ఫైల్), తాత్కాలిక స్క్రాచ్‌ప్యాడ్లు  
- **వర్క్‌ఫ్లోలను స్కాఫోల్డ్ చేయండి**: వరుస, శాఖల, మరియు సమాంతర ఏజెంట్ దశలు  
- **టూల్స్‌ను సమగ్రపరచండి**: తేలికపాటి ఫంక్షన్ టూల్ పిలుపు నమూనా  
- **మూల్యాంకనం చేయండి**: ప్రాథమిక ట్రేస్ + రూబ్రిక్ ఆధారిత ఫలిత స్కోరింగ్  

## ముందస్తు అవసరాలు

- సెషన్లు 1–4 పూర్తి చేయాలి  
- Python తో `foundry-local-sdk`, `openai`, ఐచ్ఛికంగా `chainlit`  
- స్థానిక మోడల్స్ నడుస్తున్నవి (కనీసం `phi-4-mini`)  

### క్రాస్-ప్లాట్‌ఫారమ్ వాతావరణ స్నిపెట్

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
  
macOS నుండి రిమోట్ Windows హోస్ట్ సర్వీస్ పై ఏజెంట్లను నడిపితే:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## డెమో ఫ్లో (30 నిమిషాలు)

### 1. ఏజెంట్ పాత్రలు & మెమరీ నిర్వచించండి (7 నిమిషాలు)

`samples/05-agents/agents_core.py` సృష్టించండి:  

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
  
### 2. CLI స్కాఫోల్డింగ్ నమూనా (3 నిమిషాలు)

```powershell
python samples/05-agents/agents_core.py
```
  
### 3. టూల్ పిలుపు జోడించండి (7 నిమిషాలు)

`samples/05-agents/tools.py` తో విస్తరించండి:  

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
  
సాధారణ టూల్ సింటాక్స్ అనుమతించడానికి `agents_core.py` మార్చండి: యూజర్ `#tool:get_time` వ్రాస్తాడు, ఏజెంట్ టూల్ అవుట్‌పుట్‌ను జనరేషన్ ముందు కాంటెక్స్ట్‌లో విస్తరించును.

### 4. సమన్వయ వర్క్‌ఫ్లో (6 నిమిషాలు)

`samples/05-agents/orchestrator.py` సృష్టించండి:  

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
  
### 5. స్టార్టర్ ప్రాజెక్ట్: `05-agent-architecture` విస్తరించండి (7 నిమిషాలు)

జోడించండి:  
1. స్థిరమైన మెమరీ లేయర్ (ఉదా: సంభాషణల JSON లైన్స్ జోడింపు)  
2. సులభ మూల్యాంకన రూబ్రిక్: వాస్తవికత / స్పష్టత / శైలి ప్లేస్‌హోల్డర్లు  
3. ఐచ్ఛిక Chainlit ఫ్రంట్-ఎండ్ (రెండు టాబ్స్: సంభాషణ & ట్రేస్‌లు)  
4. ఐచ్ఛిక LangGraph శైలి స్టేట్ మెషీన్ (డిపెండెన్సీ జోడిస్తే) శాఖల నిర్ణయాల కోసం  

## ధృవీకరణ చెక్లిస్ట్

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
టూల్ ఇంజెక్షన్ నోటుతో నిర్మిత పైప్‌లైన్ అవుట్‌పుట్ ఆశించండి.

## మెమరీ వ్యూహాల అవలోకనం

| లేయర్ | ఉద్దేశ్యం | ఉదాహరణ |  
|-------|---------|---------|  
| తాత్కాలిక | సంభాషణ నిరంతరత్వం | చివరి N సందేశాలు |  
| ఎపిసోడిక్ | సెషన్ రీకాల్ | ప్రతి సెషన్‌కు JSON |  
| సేమాంటిక్ | దీర్ఘకాలిక రిట్రీవల్ | సారాంశాల వెక్టర్ స్టోర్ |  
| స్క్రాచ్‌ప్యాడ్ | తర్క దశలు | ఇన్‌లైన్ చైన్-ఆఫ్-థాట్ (ప్రైవేట్) |  

## మూల్యాంకన హుక్స్ (సంకల్పనాత్మక)

```python
evaluation = {
  "factuality": None,  # మాన్యువల్ లేదా హ్యూరిస్టిక్
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  
## సమస్య పరిష్కారం

| సమస్య | కారణం | పరిష్కారం |  
|-------|---------|------------|  
| పునరావృత సమాధానాలు | కాంటెక్స్ట్ విండో చాలా పెద్ద/చిన్నది | మెమరీ విండో పరామితిని సర్దుబాటు చేయండి |  
| టూల్ పిలవబడలేదు | తప్పు సింటాక్స్ | `#tool:tool_name` ఫార్మాట్ ఉపయోగించండి |  
| నెమ్మదిగా సమన్వయం | బహుళ కోల్డ్ మోడల్స్ | ముందుగా వార్మప్ ప్రాంప్ట్‌లు నడపండి |  

## సూచనలు

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (ఐచ్ఛిక కాన్సెప్ట్): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**సెషన్ వ్యవధి**: 30 నిమిషాలు  
**కష్టత**: అధునాతన  

## నమూనా సన్నివేశం & వర్క్‌షాప్ మ్యాపింగ్

| వర్క్‌షాప్ స్క్రిప్ట్ | సన్నివేశం | లక్ష్యం | ఉదాహరణ ప్రాంప్ట్ |  
|-----------------|----------|-----------|----------------|  
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ఎగ్జిక్యూటివ్-ఫ్రెండ్లీ సారాంశాలు ఉత్పత్తి చేసే జ్ఞాన పరిశోధన బాట్ | రెండు ఏజెంట్ పైప్‌లైన్ (పరిశోధన → ఎడిటోరియల్ పాలిష్) ఐచ్ఛిక వేర్వేరు మోడల్స్ తో | కంప్లయెన్స్ కోసం ఎడ్జ్ ఇన్ఫరెన్స్ ఎందుకు ముఖ్యం అనేది వివరించండి. |  
| (విస్తరించబడిన) `tools.py` కాన్సెప్ట్ | సమయం & టోకెన్ అంచనా టూల్స్ జోడించండి | తేలికపాటి టూల్ పిలుపు నమూనా ప్రదర్శన | #tool:get_time |  

### సన్నివేశ కథనం  
కంప్లయెన్స్ డాక్యుమెంటేషన్ టీమ్ స్థానిక జ్ఞానంతో వేగవంతమైన అంతర్గత బ్రీఫ్‌లు అవసరం, డ్రాఫ్ట్‌లను క్లౌడ్ సర్వీసులకు పంపకుండా. ఒక పరిశోధక ఏజెంట్ సంక్షిప్త వాస్తవ బుల్లెట్లు సేకరిస్తుంది; ఒక ఎడిటర్ ఏజెంట్ ఎగ్జిక్యూటివ్ స్పష్టత కోసం తిరిగి వ్రాస్తుంది. వేర్వేరు మోడల్ అలియాసులు లేటెన్సీ (వేగవంతమైన SLM) మరియు శైలీ పరిమార్జన (పెద్ద మోడల్ అవసరమైనప్పుడు మాత్రమే) కోసం కేటాయించవచ్చు.

### ఉదాహరణ బహుమోడల్ వాతావరణం  
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```
  
### ట్రేస్ నిర్మాణం (ఐచ్ఛికం)  
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
  
ప్రతి దశను JSONL ఫైల్‌గా నిల్వ చేసి తర్వాత రూబ్రిక్ స్కోరింగ్ కోసం ఉపయోగించండి.

### ఐచ్ఛిక అభివృద్ధులు

| థీమ్ | అభివృద్ధి | లాభం | అమలు స్కెచ్ |  
|-------|------------|---------|-----------------------|  
| బహుమోడల్ పాత్రలు | ప్రతి ఏజెంట్‌కు వేర్వేరు మోడల్స్ (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ప్రత్యేకత & వేగం | అలియాస్ env vars ఎంచుకుని, ప్రతి పాత్ర అలియాస్ తో `chat_once` పిలవండి |  
| నిర్మిత ట్రేస్‌లు | ప్రతి చర్య(tool,input,latency,tokens) JSON ట్రేస్ | డీబగ్ & మూల్యాంకనం | డిక్ట్‌ను జాబితాకు జోడించి చివరలో `.jsonl` రాయండి |  
| మెమరీ నిల్వ | రీలోడబుల్ డైలాగ్ కాంటెక్స్ట్ | సెషన్ నిరంతరత్వం | `Agent.memory` ను `sessions/<ts>.json` కు డంప్ చేయండి |  
| టూల్ రిజిస్ట్రీ | డైనమిక్ టూల్ కనుగొనడం | విస్తరణ సామర్థ్యం | `TOOLS` డిక్ట్ నిర్వహించి పేర్లు/వివరణలు పరిశీలించండి |  
| రీట్రై & బ్యాకాఫ్ | బలమైన దీర్ఘ చైన్లు | తాత్కాలిక వైఫల్యాలు తగ్గించండి | `act` ను try/except + exponential backoff తో ర్యాప్ చేయండి |  
| రూబ్రిక్ స్కోరింగ్ | ఆటోమేటెడ్ నాణ్యత లేబుల్స్ | మెరుగుదల ట్రాక్ చేయండి | రెండవ దశ prompting మోడల్: "స్పష్టత 1-5 రేట్ చేయండి" |  
| వెక్టర్ మెమరీ | సేమాంటిక్ రీకాల్ | సంపన్నమైన దీర్ఘకాలిక కాంటెక్స్ట్ | సారాంశాలను ఎంబెడ్ చేసి, టాప్-k ను సిస్టమ్ మెసేజ్‌లో రిట్రీవ్ చేయండి |  
| స్ట్రీమింగ్ ప్రతిస్పందనలు | వేగవంతమైన అనుభూతి | UX మెరుగుదల | స్ట్రీమింగ్ అందుబాటులో ఉన్నప్పుడు ఉపయోగించి భాగస్వామ్య టోకెన్లను ఫ్లష్ చేయండి |  
| నిర్ణీత పరీక్షలు | రిగ్రెషన్ నియంత్రణ | స్థిరమైన CI | `temperature=0`, స్థిరమైన ప్రాంప్ట్ సీడ్స్ తో నడపండి |  
| సమాంతర శాఖలు | వేగవంతమైన అన్వేషణ | థ్రూపుట్ | స్వతంత్ర ఏజెంట్ దశల కోసం `concurrent.futures` ఉపయోగించండి |  

#### ట్రేస్ రికార్డ్ ఉదాహరణ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  
#### సులభ మూల్యాంకన ప్రాంప్ట్

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
ఇతరించిన (`answer`, `rating`) జంటలను నిల్వ చేసి చారిత్రక నాణ్యత గ్రాఫ్ నిర్మించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->