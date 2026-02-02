# Session 5: Bygg AI-drivna agenter snabbt med Foundry Local

## Sammanfattning

Designa och orkestrera AI-agenter med flera roller genom att använda Foundry Locals låg-latens och integritetsbevarande runtime. Du kommer att definiera agentroller, minnesstrategier, verktygsanropsmönster och exekveringsgrafer. Sessionen introducerar grundläggande mönster som du kan utöka med Chainlit eller LangGraph. Startprojektet bygger vidare på den befintliga agentarkitekturen för att lägga till minnespersistens och utvärderingsfunktioner.

## Lärandemål

- **Definiera roller**: Systemprompter och kapacitetsgränser
- **Implementera minne**: Kortvarigt (konversation), långvarigt (vektor / fil), tillfälliga anteckningar
- **Skapa arbetsflöden**: Sekventiella, förgrenade och parallella agentsteg
- **Integrera verktyg**: Lättviktigt funktionsanropsmönster
- **Utvärdera**: Grundläggande spårning + resultatbedömning baserad på kriterier

## Förkunskaper

- Sessioner 1–4 genomförda
- Python med `foundry-local-sdk`, `openai`, valfritt `chainlit`
- Lokala modeller igång (minst `phi-4-mini`)

### Miljöutdrag för flera plattformar

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

Om agenter körs från macOS mot en fjärrvärdtjänst på Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-flöde (30 min)

### 1. Definiera agentroller och minne (7 min)

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


### 2. CLI-strukturmönster (3 min)

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


Ändra `agents_core.py` för att tillåta enkel verktygssyntax: användaren skriver `#tool:get_time` och agenten expanderar verktygsutdata till kontexten innan generering.

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
1. Persistent minneslager (t.ex. JSON-linjer som lägger till konversationer)
2. Enkel utvärderingsmall: faktualitet / tydlighet / stilplatshållare
3. Valfri Chainlit-front-end (två flikar: konversation och spår)
4. Valfri LangGraph-stil statsmaskin (om beroende läggs till) för förgreningsbeslut

## Valideringschecklista

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


Förvänta dig strukturerad pipelineutdata med anteckning om verktygsinjektion.

## Översikt över minnesstrategier

| Lager | Syfte | Exempel |
|-------|-------|---------|
| Kortvarigt | Dialogkontinuitet | Senaste N meddelanden |
| Episodiskt | Sessionsminne | JSON per session |
| Semantiskt | Långtidsåterkallelse | Vektorlager av sammanfattningar |
| Anteckningar | Resonemangssteg | Inbyggd kedja av tankar (privat) |

## Utvärderingsfunktioner (Konceptuellt)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| Upprepande svar | Kontextfönstret är för stort/litet | Justera minnesfönsterparametern |
| Verktyg anropas inte | Fel syntax | Använd formatet `#tool:tool_name` |
| Långsam orkestrering | Flera kalla modeller | Förbered uppvärmningsprompter i förväg |

## Referenser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valfritt koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sessionens längd**: 30 min  
**Svårighetsgrad**: Avancerad

## Exempelscenario och workshopkartläggning

| Workshopskript | Scenario | Mål | Exempelprompt |
|----------------|----------|-----|---------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Kunskapsforskningsbot som producerar sammanfattningar för ledningsgrupper | Två-agentspipeline (forskning → redaktionell polering) med valfria separata modeller | Förklara varför edge-inferens är viktigt för efterlevnad. |
| (Utökat) `tools.py`-koncept | Lägg till tid- och tokenberäkningsverktyg | Demonstrera lättviktigt verktygsanropsmönster | #tool:get_time |

### Scenarionarrativ

Teamet för efterlevnadsdokumentation behöver snabba interna sammanfattningar baserade på lokal kunskap utan att skicka utkast till molntjänster. En forskaragent samlar kortfattade faktapunkter; en redaktörsagent omformulerar för ledningsmässig tydlighet. Separata modellalias kan tilldelas för att optimera latens (snabb SLM) kontra stilistisk förfining (större modell endast vid behov).

### Exempel på miljö med flera modeller

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Spårstruktur (Valfritt)

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


Spara varje steg till en JSONL-fil för senare bedömning med kriterier.

### Valfria förbättringar

| Tema | Förbättring | Fördel | Implementeringsskiss |
|------|-------------|--------|-----------------------|
| Roller med flera modeller | Separata modeller per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialisering och hastighet | Välj aliasmiljövariabler, anropa `chat_once` med alias per roll |
| Strukturerade spår | JSON-spår av varje akt (verktyg, input, latens, tokens) | Felsökning och utvärdering | Lägg till dict till en lista; skriv `.jsonl` vid slutet |
| Minnespersistens | Återladdningsbar dialogkontext | Sessionskontinuitet | Spara `Agent.memory` till `sessions/<ts>.json` |
| Verktygsregister | Dynamisk verktygsupptäckt | Utbyggbarhet | Underhåll `TOOLS`-dict och inspektera namn/beskrivningar |
| Återförsök och backoff | Robust långa kedjor | Minska tillfälliga fel | Omslut `act` med try/except + exponentiell backoff |
| Bedömningsmall | Automatiserade kvalitativa etiketter | Spåra förbättringar | Sekundär passering som ber modellen: "Betygsätt tydlighet 1-5" |
| Vektorminne | Semantisk återkallelse | Rik långsiktig kontext | Bädda in sammanfattningar, hämta topp-k till systemmeddelande |
| Strömmande svar | Snabbare upplevd respons | UX-förbättring | Använd strömning när tillgängligt och spola ut delvisa tokens |
| Deterministiska tester | Regressionskontroll | Stabil CI | Kör med `temperature=0`, fasta promptfrön |
| Parallell förgrening | Snabbare utforskning | Genomströmning | Använd `concurrent.futures` för oberoende agentsteg |

#### Exempel på spårpost

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


Spara (`answer`, `rating`)-par för att bygga en historisk kvalitetsgraf.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.