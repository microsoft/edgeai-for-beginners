<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T23:46:48+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "lt"
}
-->
# Sesija 5: Greitai kurkite AI valdomus agentus su Foundry Local

## Santrauka

Sukurkite ir koordinuokite daugelio vaidmenų AI agentus, naudodami Foundry Local mažo delsos ir privatumo išsaugojimo vykdymo aplinką. Apibrėžkite agentų vaidmenis, atminties strategijas, įrankių naudojimo modelius ir vykdymo grafikus. Sesijoje pristatomi karkaso modeliai, kuriuos galima plėsti naudojant Chainlit arba LangGraph. Pradinis projektas praplečia esamą agentų architektūros pavyzdį, pridedant atminties išsaugojimą ir vertinimo kabliukus.

## Mokymosi tikslai

- **Apibrėžti vaidmenis**: Sistemos raginimai ir galimybių ribos
- **Įgyvendinti atmintį**: Trumpalaikė (pokalbis), ilgalaikė (vektoriai / failai), laikina užrašų knygelė
- **Karkaso kūrimas**: Nuoseklūs, šakoti ir lygiagretūs agentų žingsniai
- **Integruoti įrankius**: Lengvas funkcijų įrankių kvietimo modelis
- **Vertinti**: Pagrindinis sekimas + vertinimas pagal rubriką

## Būtinos sąlygos

- Užbaigtos 1–4 sesijos
- Python su `foundry-local-sdk`, `openai`, neprivaloma `chainlit`
- Vietiniai modeliai veikia (bent jau `phi-4-mini`)

### Kryžminės platformos aplinkos fragmentas

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

Jei agentai vykdomi iš macOS prieš nuotolinę Windows paslaugą:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demonstracijos eiga (30 min)

### 1. Apibrėžti agentų vaidmenis ir atmintį (7 min)

Sukurkite `samples/05-agents/agents_core.py`:

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


### 2. CLI karkaso modelis (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Pridėti įrankių naudojimą (7 min)

Pridėkite `samples/05-agents/tools.py`:

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

Pakeiskite `agents_core.py`, kad būtų galima naudoti paprastą įrankių sintaksę: vartotojas rašo `#tool:get_time`, o agentas įtraukia įrankio rezultatą į kontekstą prieš generavimą.

### 4. Koordinuotas darbo procesas (6 min)

Sukurkite `samples/05-agents/orchestrator.py`:

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


### 5. Pradinis projektas: Praplėsti `05-agent-architecture` (7 min)

Pridėti:
1. Nuolatinės atminties sluoksnį (pvz., JSON linijų pokalbių papildymą)
2. Paprastą vertinimo rubriką: faktualumo / aiškumo / stiliaus vietos rezervavimo ženklus
3. Neprivalomą Chainlit sąsają (du skirtukai: pokalbis ir sekimas)
4. Neprivalomą LangGraph stiliaus būsenos mašiną (jei pridedama priklausomybė) šakotų sprendimų priėmimui

## Patikros sąrašas

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Tikėtis struktūrizuoto proceso išvesties su įrankių įtraukimo pastaba.

## Atminties strategijų apžvalga

| Sluoksnis | Paskirtis | Pavyzdys |
|-----------|-----------|----------|
| Trumpalaikė | Pokalbio tęstinumas | Paskutinės N žinutės |
| Epizodinė | Sesijos prisiminimas | JSON kiekvienai sesijai |
| Semantinė | Ilgalaikis atminties išsaugojimas | Santraukų vektorinė saugykla |
| Užrašų knygelė | Mąstymo žingsniai | Vidinė mąstymo grandinė (privati) |

## Vertinimo kabliukai (konceptualūs)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Trikčių šalinimas

| Problema | Priežastis | Sprendimas |
|----------|-----------|-----------|
| Pasikartojantys atsakymai | Konteksto langas per didelis / mažas | Koreguokite atminties lango parametrą |
| Įrankis neįvykdytas | Neteisinga sintaksė | Naudokite `#tool:tool_name` formatą |
| Lėta koordinacija | Daug šaltų modelių | Iš anksto paleiskite šildymo raginimus |

## Nuorodos

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (neprivalomas konceptas): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sesijos trukmė**: 30 min  
**Sudėtingumas**: Pažengęs

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių scenarijus | Situacija | Tikslas | Pavyzdinis raginimas |
|-----------------------|-----------|---------|----------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Žinių tyrimo robotas, kuriantis vadovams pritaikytas santraukas | Dviejų agentų procesas (tyrimas → redakcinis tobulinimas) su neprivalomais skirtingais modeliais | Paaiškinkite, kodėl kraštinis įžvalgos procesas yra svarbus atitikties užtikrinimui. |
| (Praplėstas) `tools.py` konceptas | Pridėti laiko ir žetonų skaičiavimo įrankius | Pademonstruoti lengvą įrankių naudojimo modelį | #tool:get_time |

### Situacijos pasakojimas
Atitikties dokumentacijos komanda reikalauja greitų vidinių santraukų, surinktų iš vietinių žinių, neskelbiant juodraščių į debesų paslaugas. Tyrimo agentas surenka glaustus faktinius punktus; redaktorius agentas perrašo juos, kad būtų aiškūs vadovams. Skirtingi modelių aliasai gali būti priskirti, siekiant optimizuoti delsą (greitas SLM) ir stilistinį tobulinimą (didesnis modelis tik tada, kai reikia).

### Pavyzdinė daugelio modelių aplinka
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Sekimo struktūra (neprivaloma)
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

Išsaugokite kiekvieną žingsnį JSONL faile vėlesniam vertinimui pagal rubriką.

### Neprivalomi patobulinimai

| Tema | Patobulinimas | Privalumas | Įgyvendinimo eskizas |
|------|--------------|------------|-----------------------|
| Daugelio modelių vaidmenys | Skirtingi modeliai kiekvienam agentui (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializacija ir greitis | Pasirinkite alias aplinkos kintamuosius, kvieskite `chat_once` su kiekvieno vaidmens alias |
| Struktūrizuotas sekimas | JSON sekimas kiekvienam veiksmui (įrankis, įvestis, delsos laikas, žetonai) | Derinimas ir vertinimas | Pridėkite žodyną į sąrašą; rašykite `.jsonl` pabaigoje |
| Atminties išsaugojimas | Pakartotinai įkeliama pokalbio aplinka | Sesijos tęstinumas | Išsaugokite `Agent.memory` į `sessions/<ts>.json` |
| Įrankių registras | Dinaminis įrankių aptikimas | Išplėstumas | Tvarkykite `TOOLS` žodyną ir tikrinkite pavadinimus/aprašymus |
| Pakartojimas ir atidėjimas | Patikimos ilgos grandinės | Sumažinti laikinas klaidas | Apgaubkite `act` su try/except + eksponentiniu atidėjimu |
| Vertinimo rubrika | Automatiniai kokybiniai žymėjimai | Stebėti patobulinimus | Antrinis modelio raginimas: "Įvertinkite aiškumą 1-5" |
| Vektorinė atmintis | Semantinis prisiminimas | Turtingas ilgalaikis kontekstas | Įterpkite santraukas, ištraukite top-k į sistemos pranešimą |
| Srautiniai atsakymai | Greitesnis suvokiamas atsakas | UX patobulinimas | Naudokite srautą, kai jis pasiekiamas, ir išvalykite dalinius žetonus |
| Deterministiniai testai | Regresijos kontrolė | Stabilus CI | Vykdykite su `temperature=0`, fiksuotais raginimo sėklomis |
| Lygiagretus šakojimas | Greitesnė analizė | Našumas | Naudokite `concurrent.futures` nepriklausomiems agentų žingsniams |

#### Sekimo įrašo pavyzdys

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Paprastas vertinimo raginimas

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Išsaugokite (`answer`, `rating`) poras, kad sukurtumėte istorinių kokybės grafiką.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.