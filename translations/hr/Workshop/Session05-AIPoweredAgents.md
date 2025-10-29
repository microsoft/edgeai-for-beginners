<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T23:25:39+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "hr"
}
-->
# Sesija 5: Brzo izgradite AI-agente uz Foundry Local

## Sažetak

Dizajnirajte i koordinirajte AI agente s više uloga koristeći Foundry Local za rad u okruženju s niskom latencijom i očuvanjem privatnosti. Definirat ćete uloge agenata, strategije memorije, obrasce pozivanja alata i grafove izvršenja. Sesija uvodi obrasce za izgradnju koje možete proširiti pomoću Chainlit ili LangGraph. Početni projekt proširuje postojeći uzorak arhitekture agenata dodavanjem trajne memorije i evaluacijskih kuka.

## Ciljevi učenja

- **Definiranje uloga**: Sistemski upiti i granice sposobnosti
- **Implementacija memorije**: Kratkoročna (razgovor), dugoročna (vektor / datoteka), privremene bilješke
- **Izgradnja tijeka rada**: Sekvencijalni, razgranati i paralelni koraci agenata
- **Integracija alata**: Lagani obrazac pozivanja funkcijskih alata
- **Evaluacija**: Osnovno praćenje + ocjenjivanje rezultata prema kriterijima

## Preduvjeti

- Završene sesije 1–4
- Python s `foundry-local-sdk`, `openai`, opcionalno `chainlit`
- Lokalni modeli pokrenuti (barem `phi-4-mini`)

### Snippet za više platformi

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

Ako pokrećete agente s macOS-a na udaljenom Windows host servisu:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo tijek (30 min)

### 1. Definiranje uloga agenata i memorije (7 min)

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


### 2. CLI obrazac za izgradnju (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Dodavanje pozivanja alata (7 min)

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


Izmijenite `agents_core.py` kako biste omogućili jednostavnu sintaksu alata: korisnik piše `#tool:get_time`, a agent proširuje izlaz alata u kontekst prije generiranja.

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


### 5. Početni projekt: Proširenje `05-agent-architecture` (7 min)

Dodajte:
1. Sloj trajne memorije (npr. dodavanje JSON linija razgovora)
2. Jednostavni evaluacijski kriterij: točnost / jasnoća / stil
3. Opcionalni Chainlit front-end (dva taba: razgovor i praćenje)
4. Opcionalni LangGraph stil stroja stanja (ako dodajete ovisnost) za odluke o grananju

## Provjera valjanosti

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


Očekujte strukturirani izlaz cjevovoda s bilješkom o ubrizgavanju alata.

## Pregled strategija memorije

| Sloj | Svrha | Primjer |
|------|-------|---------|
| Kratkoročna | Kontinuitet dijaloga | Posljednjih N poruka |
| Epizodna | Podsjećanje na sesiju | JSON po sesiji |
| Semantička | Dugoročno dohvaćanje | Vektorska pohrana sažetaka |
| Privremena bilješka | Koraci razmišljanja | Privatan lanac misli |

## Evaluacijski kukovi (konceptualno)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Rješavanje problema

| Problem | Uzrok | Rješenje |
|---------|-------|---------|
| Ponavljajući odgovori | Prozor konteksta prevelik/premalen | Prilagodite parametar prozora memorije |
| Alat nije pozvan | Pogrešna sintaksa | Koristite format `#tool:tool_name` |
| Spora orkestracija | Više hladnih modela | Pokrenite zagrijavanje upita unaprijed |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (opcionalni koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Trajanje sesije**: 30 min  
**Težina**: Napredno

## Primjer scenarija i mapiranje radionice

| Skripta radionice | Scenarij | Cilj | Primjer upita |
|-------------------|----------|------|---------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot za istraživanje znanja koji proizvodi sažetke prilagođene izvršnim osobama | Cjevovod s dva agenta (istraživanje → uređivačko poliranje) s opcionalnim različitim modelima | Objasnite zašto je inferencija na rubu važna za usklađenost. |
| (Prošireni) koncept `tools.py` | Dodavanje alata za procjenu vremena i tokena | Demonstracija laganog obrasca pozivanja alata | #tool:get_time |

### Narativ scenarija

Tim za dokumentaciju usklađenosti treba brze interne sažetke iz lokalnog znanja bez slanja nacrta u cloud servise. Agent istraživač prikuplja sažete činjenične točke; agent urednik prepisuje za jasnoću prilagođenu izvršnim osobama. Različiti aliasi modela mogu se dodijeliti za optimizaciju latencije (brzi SLM) naspram stilskog poliranja (veći model samo kad je potrebno).

### Primjer okruženja s više modela

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktura praćenja (opcionalno)

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


Svaki korak spremite u JSONL datoteku za kasnije ocjenjivanje prema kriterijima.

### Opcionalna poboljšanja

| Tema | Poboljšanje | Prednost | Skica implementacije |
|------|-------------|----------|-----------------------|
| Uloge s više modela | Različiti modeli po agentu (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specijalizacija i brzina | Odaberite alias varijable okruženja, pozovite `chat_once` s aliasom po ulozi |
| Strukturirano praćenje | JSON praćenje svakog koraka (alat, unos, latencija, tokeni) | Debug i evaluacija | Dodajte dict u listu; napišite `.jsonl` na kraju |
| Trajna memorija | Ponovno učitavanje konteksta dijaloga | Kontinuitet sesije | Spremite `Agent.memory` u `sessions/<ts>.json` |
| Registar alata | Dinamičko otkrivanje alata | Proširivost | Održavajte `TOOLS` dict i introspektirajte imena/opise |
| Ponovno pokušavanje i odgoda | Robusni dugi lanci | Smanjenje privremenih grešaka | Omotajte `act` s try/except + eksponencijalnom odgodom |
| Ocjenjivanje prema kriterijima | Automatske kvalitativne oznake | Praćenje poboljšanja | Sekundarni prolaz modela: "Ocijeni jasnoću 1-5" |
| Vektorska memorija | Semantičko dohvaćanje | Bogat dugoročni kontekst | Ugradite sažetke, dohvatite top-k u sistemsku poruku |
| Streaming odgovori | Brži percipirani odgovor | Poboljšanje korisničkog iskustva | Koristite streaming kad bude dostupno i ispisujte djelomične tokene |
| Deterministički testovi | Kontrola regresije | Stabilan CI | Pokrenite s `temperature=0`, fiksnim sjemenkama upita |
| Paralelno grananje | Brže istraživanje | Propusnost | Koristite `concurrent.futures` za neovisne korake agenata |

#### Primjer zapisa praćenja

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Jednostavni evaluacijski upit

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```


Spremite parove (`answer`, `rating`) za izgradnju povijesnog grafikona kvalitete.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.