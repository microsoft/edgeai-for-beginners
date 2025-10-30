<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T23:58:05+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "et"
}
-->
# Sessioon 5: Ehita kiiresti tehisintellektiga varustatud agente Foundry Localiga

## Kokkuvõte

Kujunda ja korralda mitme rolliga tehisintellekti agente, kasutades Foundry Locali madala latentsusega ja privaatsust säilitavat tööaega. Määratled agentide rollid, mälustrateegiad, tööriistade kasutamise mustrid ja täitmisgraafikud. Sessioon tutvustab raamistikumustreid, mida saab laiendada Chainlit või LangGraphiga. Algusprojekt laiendab olemasolevat agentide arhitektuuri näidist, lisades mälupüsivuse ja hindamiskonksud.

## Õpieesmärgid

- **Määratle rollid**: Süsteemi juhised ja võimekuse piirid
- **Rakenda mälu**: Lühiajaline (vestlus), pikaajaline (vektor / fail), ajutised märkmikud
- **Raamista töövood**: Järjestikused, hargnevad ja paralleelsed agentide sammud
- **Integreeri tööriistad**: Kergekaaluline funktsioonide tööriistade kutsumise muster
- **Hinda**: Põhiline jälgimine + rubriigipõhine tulemuste hindamine

## Eeltingimused

- Sessioonid 1–4 läbitud
- Python koos `foundry-local-sdk`, `openai`, valikuline `chainlit`
- Kohalikud mudelid töötavad (vähemalt `phi-4-mini`)

### Platvormidevaheline keskkonna näidis

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

Kui agente käitatakse macOS-is kaugjuhtimisega Windowsi hostiteenuse vastu:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo voog (30 min)

### 1. Määratle agentide rollid ja mälu (7 min)

Loo `samples/05-agents/agents_core.py`:

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


### 2. CLI raamistikumuster (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Lisa tööriistade kasutamine (7 min)

Laienda `samples/05-agents/tools.py` abil:

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

Muuda `agents_core.py`, et lubada lihtsat tööriista süntaksit: kasutaja kirjutab `#tool:get_time` ja agent laiendab tööriista väljundi konteksti enne genereerimist.

### 4. Orkestreeritud töövoog (6 min)

Loo `samples/05-agents/orchestrator.py`:

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


### 5. Algusprojekt: Laienda `05-agent-architecture` (7 min)

Lisa:
1. Püsiv mälukiht (nt vestluste JSON-ridade lisamine)
2. Lihtne hindamisrubriik: faktilisus / selgus / stiili kohad
3. Valikuline Chainlit kasutajaliides (kaks vahekaarti: vestlus ja jäljed)
4. Valikuline LangGraph stiilis olekumasin (kui lisatakse sõltuvus) hargnemisotsuste jaoks

## Valideerimise kontrollnimekiri

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Oota struktureeritud torujuhtme väljundit koos tööriista süstimise märkega.

## Mälustrateegiate ülevaade

| Kiht | Eesmärk | Näide |
|------|---------|-------|
| Lühiajaline | Vestluse järjepidevus | Viimased N sõnumid |
| Episoodiline | Sessiooni mälu | JSON iga sessiooni kohta |
| Semantiline | Pikaajaline otsing | Kokkuvõtete vektoripood |
| Märkmik | Mõttekäikude jälgimine | Sisemine mõttekäik (privaatne) |

## Hindamiskonksud (kontseptuaalne)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Tõrkeotsing

| Probleem | Põhjus | Lahendus |
|----------|--------|----------|
| Korduvad vastused | Kontekstiaken liiga suur/väike | Kohanda mäluakna parameetrit |
| Tööriista ei kutsuta | Vale süntaks | Kasuta `#tool:tool_name` formaati |
| Aeglane orkestreerimine | Mitu külma mudelit | Käivita eelsoojenduse juhised |

## Viited

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valikuline kontseptsioon): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sessiooni kestus**: 30 min  
**Raskusaste**: Edasijõudnud

## Näidistsenaarium ja töötoa kaardistamine

| Töötoa skript | Stsenaarium | Eesmärk | Näidisjuhis |
|---------------|------------|---------|-------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Teadmiste uurimise bot, mis koostab juhtkonnasõbralikke kokkuvõtteid | Kahe agendi torujuhe (uurimine → toimetamine) koos valikuliste eraldi mudelitega | Selgita, miks servapõhine järeldamine on vastavuse jaoks oluline. |
| (Laiendatud) `tools.py` kontseptsioon | Lisa aja- ja märgihinnangu tööriistad | Näita kergekaalulist tööriista kasutamise mustrit | #tool:get_time |

### Stsenaariumi narratiiv
Vastavusdokumentatsiooni meeskond vajab kiireid sisemisi kokkuvõtteid, mis pärinevad kohalikest teadmistest, ilma et mustandeid pilveteenustesse saadetaks. Uurimisagent kogub lühikesi faktilisi punkte; toimetaja agent kirjutab need ümber juhtkonna jaoks selgemaks. Erinevaid mudelialiaase saab määrata latentsuse optimeerimiseks (kiire SLM) vs stiililine viimistlus (suurem mudel ainult vajadusel).

### Näidis mitme mudeliga keskkond
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Jälje struktuur (valikuline)
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

Salvesta iga samm JSONL-faili hilisemaks rubriigipõhiseks hindamiseks.

### Valikulised täiustused

| Teema | Täiustus | Kasu | Rakenduse visand |
|-------|----------|------|------------------|
| Mitme mudeliga rollid | Erinevad mudelid iga agendi jaoks (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Spetsialiseerumine ja kiirus | Vali alias keskkonnamuutujad, kutsu `chat_once` iga rolli aliasiga |
| Struktureeritud jäljed | Iga tegevuse (tööriist, sisend, latentsus, märgid) JSON-jälg | Silumine ja hindamine | Lisa sõnastik loendisse; kirjuta `.jsonl` lõpus |
| Mälupüsivus | Laaditav vestluse kontekst | Sessiooni järjepidevus | Salvesta `Agent.memory` kausta `sessions/<ts>.json` |
| Tööriistade register | Dünaamiline tööriistade avastamine | Laiendatavus | Halda `TOOLS` sõnastikku ja kontrolli nimesid/kirjeldusi |
| Kordus ja tagasipõrge | Tugevad pikad ahelad | Vähenda ajutisi tõrkeid | Ümbritse `act` try/except + eksponentsiaalse tagasipõrkega |
| Rubriigi hindamine | Automaatne kvalitatiivne märgistamine | Jälgi parandusi | Teisene mudeli läbivaatamine: "Hinda selgust 1-5" |
| Vektormälu | Semantiline otsing | Rikkalik pikaajaline kontekst | Sisesta kokkuvõtted, otsi top-k süsteemisõnumisse |
| Voogesituse vastused | Kiirem tajutav vastus | Kasutajakogemuse parandus | Kasuta voogesitust, kui saadaval, ja tühjenda osalised märgid |
| Deterministlikud testid | Regresseerimise kontroll | Stabiilne CI | Käivita `temperature=0`, fikseeritud juhiste seemned |
| Paralleelne hargnemine | Kiirem uurimine | Läbilaskevõime | Kasuta `concurrent.futures` sõltumatute agentide sammude jaoks |

#### Jälje kirje näide

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Lihtne hindamisjuhis

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Salvesta (`answer`, `rating`) paarid, et luua ajalooline kvaliteedigraafik.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tuleneda selle tõlke kasutamisest.