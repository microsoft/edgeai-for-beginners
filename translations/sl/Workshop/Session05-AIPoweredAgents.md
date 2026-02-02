# Seja 5: Hitro ustvarjanje agentov, ki jih poganja AI, z Foundry Local

## Povzetek

Oblikujte in usklajujte večvlogovne AI agente z uporabo Foundry Local, ki omogoča nizko zakasnitev in ohranjanje zasebnosti. Določili boste vloge agentov, strategije pomnjenja, vzorce klicanja orodij in grafe izvajanja. Seja uvaja vzorce ogrodja, ki jih lahko razširite z Chainlit ali LangGraph. Začetni projekt razširi obstoječi vzorec arhitekture agenta z dodajanjem trajnega pomnjenja in kljukic za ocenjevanje.

## Cilji učenja

- **Določite vloge**: Sistemski pozivi in meje zmogljivosti
- **Implementirajte pomnjenje**: Kratkoročno (pogovor), dolgoročno (vektor / datoteka), začasne beležke
- **Zgradite delovne tokove**: Zaporedni, razvejani in vzporedni koraki agenta
- **Integrirajte orodja**: Vzorec lahkega klicanja funkcijskega orodja
- **Ocenite**: Osnovno sledenje + ocenjevanje rezultatov na podlagi rubrike

## Predpogoji

- Zaključene seje 1–4
- Python z `foundry-local-sdk`, `openai`, opcijsko `chainlit`
- Lokalni modeli v teku (vsaj `phi-4-mini`)

### Snippet za okolje na več platformah

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

Če izvajate agente iz macOS proti oddaljeni storitvi na Windows gostitelju:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Potek predstavitve (30 min)

### 1. Določite vloge agentov in pomnjenje (7 min)

Ustvarite `samples/05-agents/agents_core.py`:

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


### 2. Vzorec ogrodja CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Dodajte klicanje orodij (7 min)

Razširite z `samples/05-agents/tools.py`:

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

Spremenite `agents_core.py`, da omogočite preprosto sintakso orodja: uporabnik napiše `#tool:get_time`, agent pa razširi izhod orodja v kontekst pred generiranjem.

### 4. Usklajen delovni tok (6 min)

Ustvarite `samples/05-agents/orchestrator.py`:

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


### 5. Začetni projekt: Razširite `05-agent-architecture` (7 min)

Dodajte:
1. Plast trajnega pomnjenja (npr. dodajanje pogovorov v JSON linije)
2. Preprosto ocenjevalno rubriko: dejanskost / jasnost / slog
3. Opcijski Chainlit vmesnik (dva zavihka: pogovor in sledi)
4. Opcijski LangGraph slog strojnega stanja (če dodate odvisnost) za razvejene odločitve

## Kontrolni seznam za validacijo

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Pričakujte strukturiran izhod cevovoda z opombo o vbrizganju orodja.

## Pregled strategij pomnjenja

| Plast | Namen | Primer |
|-------|-------|--------|
| Kratkoročno | Kontinuiteta dialoga | Zadnjih N sporočil |
| Epizodično | Spomin na sejo | JSON na sejo |
| Semantično | Dolgoročni priklic | Vektorska shramba povzetkov |
| Beležka | Koraki razmišljanja | Vgrajena veriga misli (zasebno) |

## Kljukice za ocenjevanje (konceptualno)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Odpravljanje težav

| Težava | Vzrok | Rešitev |
|--------|-------|---------|
| Ponavljajoči se odgovori | Preveliko/premajhno okno konteksta | Prilagodite parameter okna pomnjenja |
| Orodje ni bilo uporabljeno | Napačna sintaksa | Uporabite format `#tool:tool_name` |
| Počasna usklajenost | Več hladnih modelov | Predhodno zaženite pozive za ogrevanje |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (opcijski koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Trajanje seje**: 30 min  
**Težavnost**: Napredno

## Vzorec scenarija in preslikava delavnice

| Skripta delavnice | Scenarij | Cilj | Primer poziva |
|-------------------|----------|------|---------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot za raziskovanje znanja, ki ustvarja povzetke za vodstvo | Cevovod z dvema agentoma (raziskovanje → uredniško poliranje) z opcijskimi ločenimi modeli | Pojasnite, zakaj je sklepanje na robu pomembno za skladnost. |
| (Razširjen) koncept `tools.py` | Dodajte orodja za čas in oceno žetonov | Prikaz vzorca lahkega klicanja orodij | #tool:get_time |

### Pripoved scenarija
Ekipa za dokumentacijo skladnosti potrebuje hitre interne povzetke, pridobljene iz lokalnega znanja, brez pošiljanja osnutkov v oblačne storitve. Raziskovalni agent zbere jedrnate dejanske točke; uredniški agent jih preoblikuje za jasnost, primerno za vodstvo. Ločeni vzdevki modelov se lahko dodelijo za optimizacijo zakasnitve (hiter SLM) proti stilističnemu poliranju (večji model le, kadar je potrebno).

### Primer okolja z več modeli
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktura sledi (opcijsko)
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

Vsak korak shranite v datoteko JSONL za kasnejše ocenjevanje z rubriko.

### Opcijske izboljšave

| Tema | Izboljšava | Prednost | Osnutek implementacije |
|------|------------|----------|-------------------------|
| Vloge z več modeli | Ločeni modeli za vsakega agenta (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializacija in hitrost | Izberite vzdevke okolja, pokličite `chat_once` z vzdevkom za vsako vlogo |
| Strukturirane sledi | JSON sled vsakega dejanja (orodje, vnos, zakasnitev, žetoni) | Odpravljanje napak in ocenjevanje | Dodajte slovar na seznam; na koncu zapišite `.jsonl` |
| Trajno pomnjenje | Ponovno naložljiv kontekst dialoga | Kontinuiteta seje | Shranite `Agent.memory` v `sessions/<ts>.json` |
| Register orodij | Dinamično odkrivanje orodij | Razširljivost | Vzdržujte slovar `TOOLS` in preverite imena/opise |
| Ponovni poskus in odložitev | Zanesljive dolge verige | Zmanjšanje začasnih napak | Ovijte `act` z try/except + eksponentno odložitev |
| Ocenjevanje z rubriko | Samodejne kvalitativne oznake | Sledenje izboljšavam | Sekundarni poziv modelu: "Oceni jasnost 1-5" |
| Vektorsko pomnjenje | Semantični priklic | Bogat dolgoročni kontekst | Vdelajte povzetke, prikličite top-k v sistemsko sporočilo |
| Pretakanje odgovorov | Hitrejši zaznani odziv | Izboljšanje uporabniške izkušnje | Uporabite pretakanje, ko je na voljo, in sproti posredujte delne žetone |
| Deterministični testi | Nadzor regresije | Stabilen CI | Zaženite z `temperature=0`, fiksnimi semeni pozivov |
| Vzporedno razvejanje | Hitrejše raziskovanje | Prepustnost | Uporabite `concurrent.futures` za neodvisne korake agenta |

#### Primer zapisa sledi

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Preprost ocenjevalni poziv

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Shranjujte pare (`answer`, `rating`) za izdelavo zgodovinskega grafa kakovosti.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.