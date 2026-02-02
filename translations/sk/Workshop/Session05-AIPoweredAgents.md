# Session 5: Rýchle vytváranie AI agentov s Foundry Local

## Abstrakt

Navrhnite a koordinujte AI agentov s viacerými rolami pomocou nízkolatenčného a súkromie zachovávajúceho runtime Foundry Local. Definujete role agentov, stratégie pamäte, vzory vyvolania nástrojov a grafy vykonávania. Táto relácia predstavuje vzory štruktúry, ktoré môžete rozšíriť pomocou Chainlit alebo LangGraph. Štartovací projekt rozširuje existujúcu architektúru agentov o perzistenciu pamäte + hodnotiace háčiky.

## Ciele učenia

- **Definovať role**: Systémové výzvy & hranice schopností
- **Implementovať pamäť**: Krátkodobá (konverzácia), dlhodobá (vektor / súbor), dočasné poznámkové bloky
- **Štruktúrovať pracovné postupy**: Sekvenčné, vetvené a paralelné kroky agentov
- **Integrovať nástroje**: Jednoduchý vzor volania funkčných nástrojov
- **Hodnotiť**: Základné sledovanie + hodnotenie výsledkov na základe kritérií

## Predpoklady

- Dokončené relácie 1–4
- Python s `foundry-local-sdk`, `openai`, voliteľne `chainlit`
- Lokálne modely spustené (minimálne `phi-4-mini`)

### Úryvok pre prostredie na viacerých platformách

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

Ak spúšťate agentov z macOS proti vzdialenej službe hostovanej na Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Ukážkový priebeh (30 min)

### 1. Definovanie rolí agentov a pamäte (7 min)

Vytvorte `samples/05-agents/agents_core.py`:

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


### 2. Vzor štruktúry CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Pridanie vyvolania nástrojov (7 min)

Rozšírte pomocou `samples/05-agents/tools.py`:

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

Upravte `agents_core.py`, aby umožňoval jednoduchú syntax nástrojov: používateľ napíše `#tool:get_time` a agent rozšíri výstup nástroja do kontextu pred generovaním.

### 4. Koordinovaný pracovný postup (6 min)

Vytvorte `samples/05-agents/orchestrator.py`:

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


### 5. Štartovací projekt: Rozšírenie `05-agent-architecture` (7 min)

Pridajte:
1. Vrstvu perzistentnej pamäte (napr. pridávanie konverzácií do JSON riadkov)
2. Jednoduché hodnotiace kritériá: faktickosť / jasnosť / štýlové zástupné symboly
3. Voliteľné front-end Chainlit (dve záložky: konverzácia & sledovanie)
4. Voliteľný štýl LangGraph stavového stroja (ak pridávate závislosť) pre rozhodovanie vo vetvení

## Kontrolný zoznam validácie

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Očakávajte štruktúrovaný výstup pipeline s poznámkou o injekcii nástroja.

## Prehľad stratégií pamäte

| Vrstva | Účel | Príklad |
|-------|---------|---------|
| Krátkodobá | Kontinuita dialógu | Posledných N správ |
| Epizodická | Spomienka na reláciu | JSON pre reláciu |
| Semantická | Dlhodobé vyhľadávanie | Vektorový úložisko súhrnov |
| Poznámkový blok | Kroky uvažovania | Inline reťazec myšlienok (súkromné) |

## Hodnotiace háčiky (Konceptuálne)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Riešenie problémov

| Problém | Príčina | Riešenie |
|-------|------|------------|
| Opakujúce sa odpovede | Príliš veľké/malé okno kontextu | Nastavte parameter okna pamäte |
| Nástroj nebol vyvolaný | Nesprávna syntax | Použite formát `#tool:tool_name` |
| Pomalá koordinácia | Viacero studených modelov | Predbežné spustenie výzvových promptov |

## Referencie

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (voliteľný koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Trvanie relácie**: 30 min  
**Obtiažnosť**: Pokročilá

## Ukážkový scenár & mapovanie workshopu

| Skript workshopu | Scenár | Cieľ | Príklad výzvy |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot na výskum znalostí produkujúci zhrnutia vhodné pre vedenie | Pipeline s dvoma agentmi (výskum → redakčné úpravy) s voliteľnými odlišnými modelmi | Vysvetlite, prečo je dôležitý edge inference pre súlad. |
| (Rozšírený) koncept `tools.py` | Pridanie nástrojov na odhad času & tokenov | Demonštrácia jednoduchého vzoru vyvolania nástrojov | #tool:get_time |

### Naratív scenára
Tím pre dokumentáciu súladu potrebuje rýchle interné zhrnutia získané z lokálnych znalostí bez odosielania návrhov do cloudových služieb. Agent výskumník zhromažďuje stručné faktické body; agent editor prepisuje pre jasnosť vedenia. Môžu byť priradené odlišné aliasy modelov na optimalizáciu latencie (rýchly SLM) vs štýlové úpravy (väčší model len keď je potrebné).

### Príklad prostredia s viacerými modelmi
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Štruktúra sledovania (voliteľné)
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

Uložte každý krok do súboru JSONL pre neskoršie hodnotenie na základe kritérií.

### Voliteľné vylepšenia

| Téma | Vylepšenie | Výhoda | Náčrt implementácie |
|-------|------------|---------|-----------------------|
| Role s viacerými modelmi | Odlišné modely pre agenta (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Špecializácia & rýchlosť | Vyberte aliasy env vars, volajte `chat_once` s aliasom pre každú rolu |
| Štruktúrované sledovanie | JSON sledovanie každého aktu (nástroj, vstup, latencia, tokeny) | Debug & hodnotenie | Pridajte dict do zoznamu; zapíšte `.jsonl` na konci |
| Perzistencia pamäte | Znovu načítateľný kontext dialógu | Kontinuita relácie | Uložte `Agent.memory` do `sessions/<ts>.json` |
| Registrácia nástrojov | Dynamické objavovanie nástrojov | Rozšíriteľnosť | Udržujte dict `TOOLS` & preskúmajte názvy/popisy |
| Opakovanie & zálohovanie | Robustné dlhé reťazce | Zníženie prechodných zlyhaní | Obalte `act` s try/except + exponenciálne zálohovanie |
| Hodnotenie na základe kritérií | Automatizované kvalitatívne označenia | Sledovanie zlepšení | Sekundárne prechádzanie modelom: "Ohodnoťte jasnosť 1-5" |
| Vektorová pamäť | Semantické vyhľadávanie | Bohatý dlhodobý kontext | Vložte súhrny, vyhľadajte top-k do systémovej správy |
| Streamované odpovede | Rýchlejšie vnímanie odpovede | Zlepšenie UX | Použite streamovanie, keď je dostupné, a flushujte čiastočné tokeny |
| Deterministické testy | Kontrola regresie | Stabilné CI | Spustite s `temperature=0`, pevnými semienkami promptov |
| Paralelné vetvenie | Rýchlejšie skúmanie | Priepustnosť | Použite `concurrent.futures` pre nezávislé kroky agentov |

#### Príklad záznamu sledovania

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Jednoduchý hodnotiaci prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Uložte páry (`answer`, `rating`) na vytvorenie historického grafu kvality.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.