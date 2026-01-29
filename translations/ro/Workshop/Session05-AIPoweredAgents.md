# Sesiunea 5: Construiește rapid agenți AI cu Foundry Local

## Rezumat

Proiectează și orchestrează agenți AI cu mai multe roluri, utilizând runtime-ul Foundry Local, care oferă latență redusă și protecția confidențialității. Vei defini rolurile agenților, strategiile de memorie, modelele de invocare a instrumentelor și graficele de execuție. Sesiunea introduce modele de structurare pe care le poți extinde cu Chainlit sau LangGraph. Proiectul de început extinde arhitectura existentă a agenților pentru a adăuga persistența memoriei și cârlige de evaluare.

## Obiective de învățare

- **Definirea rolurilor**: Prompteri de sistem și limitele capacităților
- **Implementarea memoriei**: Pe termen scurt (conversație), pe termen lung (vector / fișier), scratchpad-uri efemere
- **Structurarea fluxurilor de lucru**: Pași secvențiali, ramificați și paraleli ai agenților
- **Integrarea instrumentelor**: Model de invocare a funcțiilor ușoare
- **Evaluare**: Urmărire de bază + scorarea rezultatelor bazată pe rubrici

## Cerințe preliminare

- Finalizarea sesiunilor 1–4
- Python cu `foundry-local-sdk`, `openai`, opțional `chainlit`
- Modele locale funcționale (cel puțin `phi-4-mini`)

### Fragment de mediu cross-platform

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

Dacă rulezi agenți de pe macOS împotriva unui serviciu gazdă Windows la distanță:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Fluxul demonstrației (30 min)

### 1. Definirea rolurilor agenților și memoriei (7 min)

Creează `samples/05-agents/agents_core.py`:

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


### 2. Model de structurare CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Adăugarea invocării instrumentelor (7 min)

Extinde cu `samples/05-agents/tools.py`:

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

Modifică `agents_core.py` pentru a permite sintaxa simplă a instrumentelor: utilizatorul scrie `#tool:get_time`, iar agentul extinde ieșirea instrumentului în context înainte de generare.

### 4. Flux de lucru orchestrat (6 min)

Creează `samples/05-agents/orchestrator.py`:

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


### 5. Proiect de început: Extinde `05-agent-architecture` (7 min)

Adaugă:
1. Strat de memorie persistentă (de exemplu, adăugarea liniilor JSON ale conversațiilor)
2. Rubrică simplă de evaluare: factualitate / claritate / stil
3. Interfață frontală opțională Chainlit (două file: conversație și urme)
4. Mașină de stare în stil LangGraph opțională (dacă se adaugă dependența) pentru decizii ramificate

## Lista de verificare pentru validare

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Așteaptă ieșirea structurată a conductei cu nota de injecție a instrumentului.

## Prezentare generală a strategiilor de memorie

| Strat       | Scop                | Exemplu               |
|-------------|---------------------|-----------------------|
| Pe termen scurt | Continuitatea dialogului | Ultimele N mesaje     |
| Episodic    | Amintirea sesiunii  | JSON per sesiune      |
| Semantic    | Recuperare pe termen lung | Stoc de vectori cu rezumate |
| Scratchpad  | Pași de raționament | Lanț de gânduri inline (privat) |

## Cârlige de evaluare (conceptual)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Depanare

| Problemă             | Cauză                     | Rezolvare                     |
|----------------------|---------------------------|--------------------------------|
| Răspunsuri repetitive | Fereastra de context prea mare/mică | Ajustează parametrul ferestrei de memorie |
| Instrumentul nu este invocat | Sintaxă greșită            | Folosește formatul `#tool:tool_name` |
| Orchestrare lentă    | Mai multe modele reci     | Rulează prompturi de încălzire înainte |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (concept opțional): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Durata sesiunii**: 30 min  
**Dificultate**: Avansat

## Scenariu exemplu și mapare workshop

| Script workshop | Scenariu | Obiectiv | Exemplu de prompt |
|-----------------|----------|----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot de cercetare a cunoștințelor care produce rezumate prietenoase pentru executivi | Conductă cu doi agenți (cercetare → rafinare editorială) cu modele distincte opționale | Explică de ce inferența locală este importantă pentru conformitate. |
| (Extins) conceptul `tools.py` | Adaugă instrumente de estimare a timpului și token-urilor | Demonstrează modelul de invocare ușoară a instrumentelor | #tool:get_time |

### Narațiunea scenariului

Echipa de documentare pentru conformitate are nevoie de rezumate interne rapide, obținute din cunoștințe locale, fără a trimite schițele către servicii cloud. Un agent cercetător adună puncte factuale concise; un agent editor rescrie pentru claritate executivă. Aliasuri de modele distincte pot fi atribuite pentru a optimiza latența (SLM rapid) vs rafinarea stilistică (model mai mare doar când este necesar).

### Exemplu de mediu multi-model

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Structura urmelor (opțional)

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

Persistă fiecare pas într-un fișier JSONL pentru scorarea ulterioară bazată pe rubrici.

### Îmbunătățiri opționale

| Temă              | Îmbunătățire            | Beneficiu              | Schiță de implementare       |
|-------------------|-------------------------|------------------------|------------------------------|
| Roluri multi-model | Modele distincte per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializare și viteză | Selectează variabile de mediu alias, apelează `chat_once` cu alias per rol |
| Urme structurate  | Urmă JSON a fiecărui act(tool,input,latency,tokens) | Debugging și evaluare | Adaugă dict la o listă; scrie `.jsonl` la final |
| Persistența memoriei | Context de dialog reîncărcabil | Continuitatea sesiunii | Salvează `Agent.memory` în `sessions/<ts>.json` |
| Registru de instrumente | Descoperire dinamică a instrumentelor | Extensibilitate | Menține dict-ul `TOOLS` și introspectează numele/descrierea |
| Retry și Backoff | Lanțuri lungi robuste | Reducerea eșecurilor tranzitorii | Învelește `act` cu try/except + backoff exponențial |
| Scorarea rubricii | Etichete calitative automate | Urmărirea îmbunătățirilor | Trecere secundară promptând modelul: "Evaluează claritatea 1-5" |
| Memorie vectorială | Recuperare semantică | Context bogat pe termen lung | Încorporează rezumate, recuperează top-k în mesajul sistemului |
| Răspunsuri în flux | Răspuns perceput mai rapid | Îmbunătățirea UX | Folosește streaming odată disponibil și elimină tokenii parțiali |
| Teste deterministe | Control regresiv | CI stabil | Rulează cu `temperature=0`, semințe de prompt fixe |
| Ramificare paralelă | Explorare mai rapidă | Debit | Folosește `concurrent.futures` pentru pași independenți ai agenților |

#### Exemplu de înregistrare a urmelor

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Prompt simplu de evaluare

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persistă perechile (`answer`, `rating`) pentru a construi un grafic istoric al calității.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.