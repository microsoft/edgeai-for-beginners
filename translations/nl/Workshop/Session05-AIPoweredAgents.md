# Sessie 5: Bouw snel AI-aangedreven agenten met Foundry Local

## Samenvatting

Ontwerp en orkestreer multi-role AI-agenten met behulp van Foundry Local’s low-latency, privacy-preserving runtime. Je definieert agentrollen, geheugenstrategieën, tool-aanroeppatronen en uitvoeringsgrafieken. De sessie introduceert scaffolding-patronen die je kunt uitbreiden met Chainlit of LangGraph. Het starterproject breidt de bestaande agentarchitectuur uit met geheugenpersistentie en evaluatiehooks.

## Leerdoelen

- **Definieer Rollen**: Systeemprompts & capaciteitsgrenzen
- **Implementeer Geheugen**: Kortetermijn (gesprek), langetermijn (vector / bestand), tijdelijke notitieblokken
- **Scaffold Workflows**: Sequentiële, vertakkende en parallelle agentstappen
- **Integreer Tools**: Lichtgewicht functie-aanroep patroon
- **Evalueer**: Basis trace + rubric-driven uitkomstbeoordeling

## Vereisten

- Sessies 1–4 voltooid
- Python met `foundry-local-sdk`, `openai`, optioneel `chainlit`
- Lokale modellen actief (minimaal `phi-4-mini`)

### Cross-platform omgeving snippet

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

Als je agenten uitvoert vanaf macOS tegen een externe Windows-hostservice:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Definieer Agentrollen & Geheugen (7 min)

Maak `samples/05-agents/agents_core.py`:

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


### 2. CLI Scaffolding Patroon (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Voeg Tool-aanroep toe (7 min)

Breid uit met `samples/05-agents/tools.py`:

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


Pas `agents_core.py` aan om eenvoudige toolsyntax mogelijk te maken: gebruiker schrijft `#tool:get_time` en agent voegt tooloutput toe aan de context vóór generatie.

### 4. Georkestreerde Workflow (6 min)

Maak `samples/05-agents/orchestrator.py`:

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


### 5. Starterproject: Breid `05-agent-architecture` uit (7 min)

Voeg toe:
1. Persistent geheugenlaag (bijv. JSON-lijnen toevoegen van gesprekken)
2. Eenvoudige evaluatierubric: placeholders voor feitelijkheid / duidelijkheid / stijl
3. Optionele Chainlit front-end (twee tabbladen: gesprek & traces)
4. Optionele LangGraph-stijl toestandsmachine (indien afhankelijkheid toegevoegd) voor vertakkingsbeslissingen

## Validatie Checklist

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Verwacht gestructureerde pijplijnoutput met toolinjectienotitie.

## Overzicht Geheugenstrategieën

| Laag       | Doel               | Voorbeeld            |
|------------|--------------------|----------------------|
| Kortetermijn | Gesprekscontinuïteit | Laatste N berichten  |
| Episodisch  | Sessieherinnering  | JSON per sessie      |
| Semantisch  | Langetermijnopslag | Vectoropslag van samenvattingen |
| Scratchpad  | Redeneerstappen    | Inline chain-of-thought (privé) |

## Evaluatiehooks (Conceptueel)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Probleemoplossing

| Probleem            | Oorzaak                  | Oplossing                     |
|---------------------|--------------------------|--------------------------------|
| Herhalende antwoorden | Contextvenster te groot/klein | Pas geheugenvensterparameter aan |
| Tool niet aangeroepen | Verkeerde syntax         | Gebruik `#tool:tool_name` formaat |
| Trage orkestratie    | Meerdere koude modellen  | Voer warmup prompts vooraf uit |

## Referenties

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optioneel concept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sessieduur**: 30 min  
**Moeilijkheidsgraad**: Geavanceerd

## Voorbeeldscenario & Workshop Mapping

| Workshop Script | Scenario | Doelstelling | Voorbeeldprompt |
|-----------------|----------|--------------|-----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Kennisonderzoeksbot die executive-vriendelijke samenvattingen produceert | Twee-agentenpijplijn (onderzoek → redactionele verfijning) met optioneel verschillende modellen | Leg uit waarom edge inference belangrijk is voor compliance. |
| (Uitgebreid) `tools.py` concept | Voeg tijd- & tokenramingtools toe | Demonstreer lichtgewicht tool-aanroep patroon | #tool:get_time |

### Scenario Narratief
Het compliance documentatieteam heeft snelle interne samenvattingen nodig, afkomstig van lokale kennis, zonder concepten naar cloudservices te sturen. Een onderzoeker-agent verzamelt beknopte feitelijke punten; een redacteur-agent herschrijft voor executive duidelijkheid. Verschillende modelaliassen kunnen worden toegewezen om latentie te optimaliseren (snelle SLM) versus stilistische verfijning (groter model alleen indien nodig).

### Voorbeeld Multi-Model Omgeving
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Trace Structuur (Optioneel)
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

Bewaar elke stap in een JSONL-bestand voor latere rubric scoring.

### Optionele Verbeteringen

| Thema              | Verbetering              | Voordeel               | Implementatieschets         |
|--------------------|--------------------------|------------------------|-----------------------------|
| Multi-Model Rollen | Verschillende modellen per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialisatie & snelheid | Selecteer alias omgevingsvariabelen, roep `chat_once` aan met per-rol alias |
| Gestructureerde Traces | JSON trace van elke act(tool,input,latency,tokens) | Debug & evaluatie        | Voeg dict toe aan een lijst; schrijf `.jsonl` aan het einde |
| Geheugenpersistentie | Herlaadbare dialoogcontext | Sessiecontinuïteit     | Dump `Agent.memory` naar `sessions/<ts>.json` |
| Toolregister        | Dynamische toolontdekking | Uitbreidbaarheid       | Beheer `TOOLS` dict & inspecteer namen/beschrijvingen |
| Retry & Backoff     | Robuuste lange ketens    | Verminder tijdelijke fouten | Omhul `act` met try/except + exponentiële backoff |
| Rubric Scoring      | Geautomatiseerde kwalitatieve labels | Volg verbeteringen       | Secundaire pass prompting model: "Beoordeel duidelijkheid 1-5" |
| Vectorgeheugen      | Semantische herinnering  | Rijke langetermijncontext | Embed samenvattingen, haal top-k op in systeembericht |
| Streaming Antwoorden | Snellere waargenomen respons | UX-verbetering          | Gebruik streaming zodra beschikbaar en flush gedeeltelijke tokens |
| Deterministische Tests | Regressiecontrole      | Stabiele CI            | Voer uit met `temperature=0`, vaste prompt seeds |
| Parallel Vertakken  | Snellere verkenning     | Doorvoer               | Gebruik `concurrent.futures` voor onafhankelijke agentstappen |

#### Trace Record Voorbeeld

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Eenvoudige Evaluatieprompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Bewaar (`answer`, `rating`) paren om een historische kwaliteitsgrafiek op te bouwen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.