# Sesjon 5: Bygg AI-drevne agenter raskt med Foundry Local

## Sammendrag

Design og orkestrer AI-agenter med flere roller ved hjelp av Foundry Locals lav-latens og personvernvennlige runtime. Du vil definere agentroller, minnestrategier, verktøyinnkallingsmønstre og utførelsesgrafer. Sesjonen introduserer rammeverksmønstre som kan utvides med Chainlit eller LangGraph. Startprosjektet utvider den eksisterende agentarkitekturen for å legge til minnepersistens og evalueringskroker.

## Læringsmål

- **Definer roller**: Systemprompter og kapasitetsgrenser
- **Implementer minne**: Korttidsminne (samtale), langtidsminne (vektor / fil), midlertidige notatblokker
- **Bygg arbeidsflyter**: Sekvensielle, forgrenede og parallelle agentsteg
- **Integrer verktøy**: Lettvektig funksjonsinnkallingsmønster for verktøy
- **Evaluer**: Grunnleggende spor + vurdering basert på rubrikkskåring

## Forutsetninger

- Sesjoner 1–4 fullført
- Python med `foundry-local-sdk`, `openai`, valgfritt `chainlit`
- Lokale modeller i drift (minst `phi-4-mini`)

### Snutt for tverrplattformmiljø

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

Hvis agenter kjøres fra macOS mot en ekstern Windows-vertsserver:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-flyt (30 min)

### 1. Definer agentroller og minne (7 min)

Opprett `samples/05-agents/agents_core.py`:

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


### 2. CLI-rammeverksmønster (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Legg til verktøyinnkalling (7 min)

Utvid med `samples/05-agents/tools.py`:

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


Endre `agents_core.py` for å tillate enkel verktøysyntaks: brukeren skriver `#tool:get_time`, og agenten utvider verktøyutdata til konteksten før generering.

### 4. Orkestrert arbeidsflyt (6 min)

Opprett `samples/05-agents/orchestrator.py`:

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


### 5. Startprosjekt: Utvid `05-agent-architecture` (7 min)

Legg til:
1. Lag for vedvarende minne (f.eks. JSON-linjer som legger til samtaler)
2. Enkel evalueringsrubrikk: faktualitet / klarhet / stilplassholdere
3. Valgfri Chainlit front-end (to faner: samtale og spor)
4. Valgfri LangGraph-stil tilstandsmaskin (hvis avhengighet legges til) for forgreningsbeslutninger

## Valideringssjekkliste

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Forvent strukturert pipeline-utdata med notat om verktøyinnsprøyting.

## Oversikt over minnestrategier

| Lag | Formål | Eksempel |
|-----|--------|----------|
| Korttidsminne | Samtalekontinuitet | Siste N meldinger |
| Episodisk | Sesjonsminne | JSON per sesjon |
| Semantisk | Langtidsminne | Vektorlager med sammendrag |
| Notatblokk | Resonneringssteg | Inline tankerekke (privat) |

## Evalueringskroker (Konseptuelt)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Feilsøking

| Problem | Årsak | Løsning |
|---------|-------|--------|
| Gjentakende svar | Kontekstvinduet er for stort/lite | Juster parameter for minnevindu |
| Verktøy ikke innkalt | Feil syntaks | Bruk formatet `#tool:tool_name` |
| Langsom orkestrering | Flere kalde modeller | Forhåndskjør oppvarmingsprompter |

## Referanser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valgfritt konsept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Varighet på sesjon**: 30 min  
**Vanskelighetsgrad**: Avansert

## Eksempelscenario og workshopkartlegging

| Workshop-skript | Scenario | Mål | Eksempelprompt |
|-----------------|----------|-----|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Kunnskapsforskningsbot som lager ledelsesvennlige sammendrag | To-agent pipeline (forskning → redaksjonell polering) med valgfritt distinkte modeller | Forklar hvorfor edge-inferens er viktig for samsvar. |
| (Utvidet) `tools.py`-konsept | Legg til verktøy for tid- og tokenestimering | Demonstrer lettvektig verktøyinnkallingsmønster | #tool:get_time |

### Scenariofortelling
Teamet for samsvarsdokumentasjon trenger raske interne oppsummeringer hentet fra lokal kunnskap uten å sende utkast til skytjenester. En forskeragent samler konsise faktuelle punkter; en redaktøragent omskriver for ledelsesmessig klarhet. Distinkte modellaliaser kan tildeles for å optimalisere latens (rask SLM) vs stilistisk raffinering (større modell kun når nødvendig).

### Eksempel på miljø med flere modeller
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktur for spor (valgfritt)
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

Lagres hvert steg til en JSONL-fil for senere rubrikkskåring.

### Valgfrie forbedringer

| Tema | Forbedring | Fordel | Implementeringsskisse |
|------|------------|--------|-----------------------|
| Roller med flere modeller | Distinkte modeller per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Spesialisering og hastighet | Velg alias miljøvariabler, kall `chat_once` med alias per rolle |
| Strukturerte spor | JSON-spor for hver handling (verktøy, input, latens, tokens) | Feilsøking og evaluering | Legg til dict i en liste; skriv `.jsonl` til slutt |
| Minnepersistens | Gjenlastbar dialogkontekst | Sesjonskontinuitet | Dump `Agent.memory` til `sessions/<ts>.json` |
| Verktøyregister | Dynamisk oppdagelse av verktøy | Utvidbarhet | Vedlikehold `TOOLS`-dict og inspiser navn/beskrivelse |
| Gjentakelse og tilbakefall | Robust lange kjeder | Reduser midlertidige feil | Pakk `act` med try/except + eksponentiell tilbakefall |
| Rubrikkskåring | Automatiserte kvalitative etiketter | Spor forbedringer | Sekundær passering som ber modellen: "Vurder klarhet 1-5" |
| Vektorminne | Semantisk gjenkalling | Rik langtidskontekst | Legg inn sammendrag, hent topp-k inn i systemmelding |
| Strømmende svar | Raskere oppfattet respons | Forbedret brukeropplevelse | Bruk strømming når tilgjengelig og flush delvise tokens |
| Deterministiske tester | Kontroll av regresjon | Stabil CI | Kjør med `temperature=0`, faste promptfrø |
| Parallelle forgreninger | Raskere utforskning | Gjennomstrømning | Bruk `concurrent.futures` for uavhengige agentsteg |

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

Lagres (`answer`, `rating`) par for å bygge en historisk kvalitetsgraf.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.