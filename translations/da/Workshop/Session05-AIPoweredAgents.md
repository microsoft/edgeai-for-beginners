# Session 5: Byg AI-drevne agenter hurtigt med Foundry Local

## Resumé

Design og orkestrer multi-rolle AI-agenter ved hjælp af Foundry Locals lav-latens, privatlivsbevarende runtime. Du vil definere agentroller, hukommelsesstrategier, værktøjsanvendelsesmønstre og eksekveringsgrafer. Sessionen introducerer skabelonmønstre, som du kan udvide med Chainlit eller LangGraph. Startprojektet udvider den eksisterende agentarkitektursample til at inkludere hukommelsespersistens + evalueringshooks.

## Læringsmål

- **Definer roller**: Systemprompter & kapacitetsgrænser
- **Implementer hukommelse**: Kortvarig (samtale), langvarig (vektor / fil), midlertidige notater
- **Skabelonarbejdsgange**: Sekventielle, forgrenede og parallelle agenttrin
- **Integrer værktøjer**: Letvægtsmønster for værktøjskald
- **Evaluer**: Grundlæggende spor + rubric-drevet resultatvurdering

## Forudsætninger

- Sessioner 1–4 gennemført
- Python med `foundry-local-sdk`, `openai`, valgfri `chainlit`
- Lokale modeller kørende (mindst `phi-4-mini`)

### Snippet til tværplatformsmiljø

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

Hvis agenter køres fra macOS mod en fjern Windows-værtstjeneste:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Definer agentroller & hukommelse (7 min)

Opret `samples/05-agents/agents_core.py`:

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


### 2. CLI-skabelonmønster (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Tilføj værktøjsanvendelse (7 min)

Udvid med `samples/05-agents/tools.py`:

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


Rediger `agents_core.py` for at tillade enkel værktøjssyntaks: brugeren skriver `#tool:get_time`, og agenten udvider værktøjets output til konteksten før generering.

### 4. Orkestreret arbejdsgang (6 min)

Opret `samples/05-agents/orchestrator.py`:

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


### 5. Startprojekt: Udvid `05-agent-architecture` (7 min)

Tilføj:
1. Lag til vedvarende hukommelse (f.eks. JSON-linjer med samtaler)
2. Enkel evalueringsrubric: placeholders for faktualitet / klarhed / stil
3. Valgfri Chainlit front-end (to faner: samtale & spor)
4. Valgfri LangGraph-stil tilstandsmaskine (hvis afhængighed tilføjes) til forgreningsbeslutninger

## Valideringscheckliste

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Forvent struktureret pipeline-output med notat om værktøjsindsprøjtning.

## Oversigt over hukommelsesstrategier

| Lag         | Formål               | Eksempel               |
|-------------|----------------------|------------------------|
| Kortvarig   | Samtale kontinuitet  | Sidste N beskeder      |
| Episodisk   | Session genkaldelse  | JSON pr. session       |
| Semantisk   | Langvarig genkaldelse| Vektorlager af resuméer|
| Scratchpad  | Ræsonneringstrin     | Inline tankekæde (privat)|

## Evalueringshooks (Konceptuelt)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Fejlfinding

| Problem            | Årsag                     | Løsning                     |
|--------------------|---------------------------|-----------------------------|
| Gentagne svar      | Kontekstvindue for stort/småt | Juster parameter for hukommelsesvindue |
| Værktøj ikke anvendt | Forkert syntaks          | Brug formatet `#tool:tool_name` |
| Langsom orkestrering| Flere kolde modeller      | Forvarm prompts før kørsel |

## Referencer

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valgfrit koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sessionens varighed**: 30 min  
**Sværhedsgrad**: Avanceret

## Eksempelscenarie & workshopkortlægning

| Workshop Script | Scenarie | Mål | Eksempelprompt |
|-----------------|----------|-----|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Vidensforskningsbot, der producerer ledelsesvenlige resuméer | To-agent pipeline (forskning → redaktionel polering) med valgfri separate modeller | Forklar hvorfor edge inference er vigtigt for compliance. |
| (Udvidet) `tools.py` koncept | Tilføj værktøjer til tids- & tokenestimering | Demonstrer letvægtsmønster for værktøjsanvendelse | #tool:get_time |

### Scenariefortælling
Compliance-dokumentationsteamet har brug for hurtige interne briefinger baseret på lokal viden uden at sende udkast til cloud-tjenester. En forskningsagent samler præcise faktuelle punkter; en redaktøragent omskriver for ledelsesmæssig klarhed. Separate modelaliaser kan tildeles for at optimere latens (hurtig SLM) vs stilistisk forfining (større model kun når nødvendigt).

### Eksempel på multi-model miljø
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Sporstruktur (valgfrit)
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

Gem hvert trin i en JSONL-fil til senere rubric-vurdering.

### Valgfrie forbedringer

| Tema              | Forbedring               | Fordel                  | Implementeringsskitse       |
|-------------------|--------------------------|-------------------------|-----------------------------|
| Multi-model roller| Separate modeller pr. agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialisering & hastighed | Vælg alias miljøvariabler, kald `chat_once` med alias pr. rolle |
| Strukturerede spor| JSON-spor af hver handling (værktøj, input, latens, tokens) | Fejlfinding & evaluering | Tilføj dict til en liste; skriv `.jsonl` ved afslutning |
| Hukommelsespersistens | Genindlæselig dialogkontekst | Session kontinuitet | Dump `Agent.memory` til `sessions/<ts>.json` |
| Værktøjsregister   | Dynamisk værktøjsopdagelse | Udvidelsesmuligheder    | Vedligehold `TOOLS` dict & inspicer navne/beskrivelser |
| Retry & Backoff    | Robust lange kæder       | Reducer midlertidige fejl | Wrap `act` med try/except + eksponentiel backoff |
| Rubric-vurdering   | Automatiske kvalitative labels | Spor forbedringer       | Sekundær prompt til model: "Vurder klarhed 1-5" |
| Vektormemory       | Semantisk genkaldelse    | Rig langvarig kontekst  | Embed resuméer, hent top-k ind i systemmeddelelse |
| Streaming svar     | Hurtigere opfattet respons | UX-forbedring           | Brug streaming når tilgængelig og flush delvise tokens |
| Deterministiske tests | Regression kontrol      | Stabil CI               | Kør med `temperature=0`, faste prompt seeds |
| Parallel forgrening | Hurtigere udforskning    | Gennemstrømning         | Brug `concurrent.futures` til uafhængige agenttrin |

#### Eksempel på sporregistrering

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Enkel evalueringsprompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Gem (`answer`, `rating`) par for at opbygge en historisk kvalitetsgraf.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.