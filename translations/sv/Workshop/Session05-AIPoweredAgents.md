# Session 5: Skapa AI-drivna agenter snabbt med Foundry Local

## Sammanfattning

Designa och orkestrera AI-agenter med flera roller med Foundry Locals låglatens, integritetsbevarande runtime. Du kommer att definiera agentroller, minnesstrategier, verktygsanropsmönster och exekveringsgrafer. Sessionen introducerar ramverksmönster som du kan utöka med Chainlit eller LangGraph. Startprojektet utökar det befintliga agentsarkitektur-exemplet för att lägga till minnespersistens + utvärderingskrokar.

## Lärandemål

- **Definiera roller**: Systempromptar & kapacitetsgränser
- **Implementera minne**: Korttids(minne för konversation), långtids (vektor / fil), flyktiga scratchpads
- **Bygg upp arbetsflöden**: Sekventiella, förgrenande och parallella agentsteg
- **Integrera verktyg**: Lättviktsmönster för funktionsanrop av verktyg
- **Utvärdera**: Grundläggande spårning + resultatbedömning via kriterier

## Förkunskaper

- Sessioner 1–4 slutförda
- Python med `foundry-local-sdk`, `openai`, valfritt `chainlit`
- Lokala modeller igång (minst `phi-4-mini`)

### Plattformoberoende miljösnutt

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

Vid körning av agenter från macOS mot en fjärrtjänst på Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo-flöde (30 min)

### 1. Definiera agentroller & minne (7 min)

Skapa `samples/05-agents/agents_core.py`:

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

### 2. CLI-ramverk (3 min)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Lägg till verktygsanrop (7 min)

Utöka med `samples/05-agents/tools.py`:

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

Modifiera `agents_core.py` för att tillåta enkel verktygssyntax: användaren skriver `#tool:get_time` och agenten expanderar verktygets utdata i kontexten innan generering.

### 4. Orkestrerat arbetsflöde (6 min)

Skapa `samples/05-agents/orchestrator.py`:

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

### 5. Startprojekt: Utöka `05-agent-architecture` (7 min)

Lägg till:
1. Beständig minneslager (t.ex. JSON-linjetillägg av konversationer)
2. Enkel utvärderingsmall: faktualitet / tydlighet / stilplatshållare
3. Valfri Chainlit front-end (två flikar: konversation & spår)
4. Valfri LangGraph-stil tillståndsmaskin (om beroende läggs till) för förgreningsbeslut

## Valideringschecklista

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Förvänta strukturerad pipelinematning med notering om verktygsinjektion.

## Översikt över minnesstrategier

| Lager | Syfte | Exempel |
|-------|---------|---------|
| Korttids | Dialogkontinuitet | Senaste N meddelandena |
| Episodiskt | Sessionsåterkallning | JSON per session |
| Semantiskt | Långtidsåtervinning | Vektorlagring av sammanfattningar |
| Scratchpad | Resonemangssteg | Inline chain-of-thought (privat) |

## Utvärderingskrokar (Konceptuellt)

```python
evaluation = {
  "factuality": None,  # manuell eller heuristisk
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Felsökning

| Problem | Orsak | Lösning |
|-------|------|------------|
| Upprepande svar | Kontextfönstret för stort/litet | Justera parameter för minnesfönster |
| Verktyg anropas inte | Fel syntax | Använd formatet `#tool:tool_name` |
| Långsam orkestrering | Flera kalla modeller | Förvärm med förkörnings-promptar |

## Referenser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valfritt koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sessionslängd**: 30 min  
**Svårighetsgrad**: Avancerad

## Exempelscenario & Workshopkoppling

| Workshopskript | Scenario | Mål | Exempelfråga |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Kunskapsforskningsbot som producerar chefsvänliga sammanfattningar | Två-agentpipelines (forskning → redaktionell polering) med valfria olika modeller | Förklara varför edge-inferens är viktigt för efterlevnad. |
| (Utökad) `tools.py`-koncept | Lägg till tid- & tokenuppskattningsverktyg | Demonstrera lättviktsmönster för verktygsanrop | #tool:get_time |

### Scenario-narrativ
Efterlevnadsdokumentationsteamet behöver snabba interna sammanfattningar baserade på lokal kunskap utan att skicka utkast till molntjänster. En forskningsagent samlar kortfattade faktabaserade punkter; en redigeringsagent skriver om för chefens tydlighet. Olika modelalias kan tilldelas för att optimera latens (snabb SLM) kontra stilistisk förbättring (större modell endast vid behov).

### Exempel på multimodellmiljö
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### Spårningsstruktur (valfritt)
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

Spara varje steg till en JSONL-fil för senare bedömning med mall.

### Valfria förbättringar

| Tema | Förbättring | Nytta | Implementationsskiss |
|-------|------------|---------|-----------------------|
| Multimodellroller | Olika modeller per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialisering & snabbhet | Välj alias-miljövariabler, anropa `chat_once` med per-rolle alias |
| Strukturerade spår | JSON-spår av varje akt(verktyg,indata,latens,tokens) | Felsökning & utvärdering | Lägg till dikt i lista; skriv `.jsonl` vid slut |
| Minnespersistens | Laddningsbart dialogkontext | Sessionskontinuitet | Dumpa `Agent.memory` till `sessions/<ts>.json` |
| Verktygsregister | Dynamisk verktygsupptäckt | Utbyggbarhet | Underhåll `TOOLS` dikt & introspektera namn/beskrivning |
| Försök & backoff | Robust långa kedjor | Minska övergående fel | Wrappa `act` med try/except + exponentiell backoff |
| Mallbedömning | Automatiserade kvalitativa etiketter | Följ förbättringar | Sekundär promptning av modell: "Betygsätt tydlighet 1-5" |
| Vektorminne | Semantisk återkallning | Rikt långtidskontext | Bädda in sammanfattningar, hämta top-k till systemmeddelande |
| Strömmade svar | Snabbare upplevd respons | UX-förbättring | Använd strömning när tillgängligt och skriv ut partiella tokens |
| Deterministiska tester | Regressionskontroll | Stabil CI | Kör med `temperature=0`, fasta promptfrön |
| Parallell förgrening | Snabbare utforskning | Genomströmning | Använd `concurrent.futures` för oberoende agentsteg |

#### Exempel på spårningsinskrivning

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Enkel utvärderingsprompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Spara (`answer`, `rating`) par för att bygga en historisk kvalitetsgraf.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->