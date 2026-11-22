# Sesija 5: Brzo izgradite AI-agentove pomoću Foundry Local

## Sažetak

Dizajnirajte i orkestrirajte AI-agentove s višestrukim ulogama koristeći Foundry Local runtime s niskom latencijom i zaštitom privatnosti. Definirat ćete uloge agenata, strategije memorije, obrasce pozivanja alata i izvršne grafove. Sesija uvodi obrasce za strukturu koje možete proširiti pomoću Chainlit ili LangGraph. Početni projekt proširuje postojeći primjer arhitekture agenta kako bi dodao trajnu memoriju i kukice za evaluaciju.

## Ciljevi učenja

- **Definirajte uloge**: Sistemske upute i granice mogućnosti
- **Implementirajte memoriju**: Kratkoročna (razgovor), dugoročna (vektorska / datotečna), efemerne radne ploče
- **Strukturirajte tijek rada**: Sekvencijalni, razgranati i paralelni koraci agenta
- **Integrirajte alate**: Lagani obrazac poziva funkcijskih alata
- **Evaluirajte**: Osnovno praćenje + ocjenjivanje prema rubrici

## Preduvjeti

- Završene sesije 1–4
- Python s `foundry-local-sdk`, `openai`, opcionalno `chainlit`
- Lokalni modeli pokrenuti (barem `phi-4-mini`)

### Okruženje za više platformi – isječak

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

Ako pokrećete agente s macOS na udaljenom Windows host servisu:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Tijek demonstracije (30 min)

### 1. Definirajte uloge agenata i memoriju (7 min)

Kreirajte `samples/05-agents/agents_core.py`:

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

### 2. Struktura CLI-a (3 min)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Dodajte pozivanje alata (7 min)

Proširite s `samples/05-agents/tools.py`:

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

Izmijenite `agents_core.py` da dopustite jednostavnu sintaksu alata: korisnik piše `#tool:get_time` i agent proširuje izlaz alata u kontekst prije generiranja.

### 4. Orkestrirani tijek rada (6 min)

Kreirajte `samples/05-agents/orchestrator.py`:

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

### 5. Početni projekt: Proširite `05-agent-architecture` (7 min)

Dodajte:
1. Trajni sloj memorije (npr. dodavanje razgovora u JSON linijama)
2. Jednostavnomérica evaluacije: mjesta za faktografiju / jasnoću / stil
3. Opcionalno Chainlit sučelje (dvije kartice: razgovor i tragovi)
4. Opcionalna LangGraph stil stanja stroja (ako se dodaje ovisnost) za razgranate odluke

## Popis za provjeru validacije

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Očekujte strukturiran izlaz pipelinea s napomenom o umetnutom alatu.

## Pregled strategija memorije

| Sloj | Svrha | Primjer |
|-------|---------|---------|
| Kratkoročna | Kontinuitet dijaloga | Zadnjih N poruka |
| Epizodna | Sjećanje na sesiju | JSON po sesiji |
| Semantička | Dugoročno dohvaćanje | Vektorska baza sažetaka |
| Radna ploča | Koraci rezoniranja | Ugrađeni lanac misli (privatno) |

## Kukice za evaluaciju (Konceptualno)

```python
evaluation = {
  "factuality": None,  # ručno ili heuristički
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Rješavanje problema

| Problem | Uzrok | Rješenje |
|-------|------|------------|
| Ponavljajući odgovori | Prozor konteksta prevelik/previše mali | Podešavanje parametra memorijskog prozora |
| Alat nije pozvan | Pogrešna sintaksa | Koristite format `#tool:naziv_alata` |
| Spora orkestracija | Više hladnih modela | Pokrenuti zagrijavajuće upute unaprijed |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (opcionalni koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Trajanje sesije**: 30 min  
**Težina**: Napredno

## Primjer scenarija i mapiranje radionice

| Scenarij radionice | Scenarij | Cilj | Primjer upute |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot za istraživanje znanja koji proizvodi sažetke prilagođene rukovodstvu | Dvostruki agent pipeline (istraživanje → urednička dorada) s opcionalnim posebnim modelima | Objasnite zašto edge inferencija ima važnost za usklađenost. |
| (Prošireni) koncept `tools.py` | Dodajte alate za procjenu vremena i tokena | Prikaz laganog poziva alata | #tool:get_time |

### Narativ scenarija
Tim za usklađenost dokumentacije treba brze interne sažetke temeljene na lokalnom znanju bez slanja nacrta u cloud servise. Istraživački agent prikuplja sažete činjenice; urednički agent prepisuje radi jasnoće za rukovodstvo. Mogu se dodijeliti različiti modeli za optimizaciju latencije (brzi SLM) vs stilsku doradu (veći model samo po potrebi).

### Primjer višemodelnog okruženja
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### Struktura traga (opcionalno)
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

Sačuvajte svaki korak u JSONL datoteku za kasnije ocjenjivanje prema rubrici.

### Opcionalna poboljšanja

| Tema | Poboljšanje | Korist | Skica implementacije |
|-------|------------|---------|-----------------------|
| Višemodelne uloge | Različiti modeli po agentu (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specijalizacija i brzina | Odaberite alias varijable okruženja, pozovite `chat_once` s aliasom po ulozi |
| Strukturirani tragovi | JSON trag svakog čina (alat, unos, latencija, tokeni) | Debug i evaluacija | Dodajte dict na listu; na kraju zapišite `.jsonl` |
| Trajnost memorije | Ponavljajoći kontekst razgovora | Kontinuitet sesije | Izvezite `Agent.memory` u `sessions/<ts>.json` |
| Registar alata | Dinamičko otkrivanje alata | Proširivost | Održavajte riječnik `TOOLS` i introspektirajte imena/opise |
| Ponavljanje i povlačenje | Robusne duge lančane operacije | Smanjenje privremenih pogrešaka | Zamotajte `act` s try/except + eksponencijalnim povlačenjem |
| Ocjenjivanje prema rubrici | Automatske kvalitativne oznake | Praćenje poboljšanja | Sekundarni prolaz potiče model: "Ocijenite jasnoću 1-5" |
| Vektorska memorija | Semantičko sjećanje | Bogat dugoročni kontekst | Ugradite sažetke, dohvatite top-k u sistemsku poruku |
| Streaming odgovori | Brže percipirani odgovor | Poboljšanje korisničkog iskustva | Koristite streaming kad je dostupan i isperite djelomične tokene |
| Deterministički testovi | Kontrola regresije | Stabilan CI | Pokrenite s `temperature=0`, fiksnim sjemenkama upita |
| Paralelno razgrananje | Brže ispitivanje | Protok | Koristite `concurrent.futures` za neovisne korake agenata |

#### Primjer zapisa traga

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Jednostavna evaluacija upita

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Snimite parove (`answer`, `rating`) da biste izgradili povijesni graf kvalitete.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->