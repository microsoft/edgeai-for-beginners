<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T22:55:07+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "hu"
}
-->
# 5. szekció: AI-alapú ügynökök gyors létrehozása a Foundry Local segítségével

## Összefoglaló

Tervezzen és irányítson több szerepkörű AI ügynököket a Foundry Local alacsony késleltetésű, adatvédelmet biztosító futtatási környezetével. Meghatározza az ügynökök szerepköreit, memória-stratégiákat, eszközhasználati mintákat és végrehajtási grafikonokat. A szekció bemutatja azokat a keretrendszereket, amelyeket kiterjeszthet a Chainlit vagy LangGraph segítségével. A kezdő projekt kiegészíti a meglévő ügynök-architektúra mintát memória-tárolással és értékelési horgokkal.

## Tanulási célok

- **Szerepkörök meghatározása**: Rendszerüzenetek és képességek határainak kijelölése
- **Memória megvalósítása**: Rövid távú (beszélgetés), hosszú távú (vektor / fájl), átmeneti jegyzetek
- **Munkafolyamatok keretezése**: Szekvenciális, elágazó és párhuzamos ügynöklépések
- **Eszközök integrálása**: Könnyű funkcióhívási minta
- **Értékelés**: Alapvető nyomkövetés + rubrika-alapú eredményértékelés

## Előfeltételek

- Az 1–4. szekciók elvégzése
- Python a `foundry-local-sdk`, `openai`, opcionális `chainlit` csomagokkal
- Lokális modellek futtatása (legalább `phi-4-mini`)

### Keresztplatform környezet snippet

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

Ha macOS-ról futtat ügynököket távoli Windows host szolgáltatás ellen:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Bemutató menete (30 perc)

### 1. Ügynök szerepek és memória meghatározása (7 perc)

Hozzon létre egy `samples/05-agents/agents_core.py` fájlt:

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


### 2. CLI keretrendszer minta (3 perc)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Eszközhasználat hozzáadása (7 perc)

Egészítse ki a `samples/05-agents/tools.py` fájllal:

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

Módosítsa az `agents_core.py` fájlt, hogy egyszerű eszközszintaxist engedélyezzen: a felhasználó beírja `#tool:get_time`, és az ügynök az eszköz kimenetét a generálás előtt a kontextusba helyezi.

### 4. Orkesztrált munkafolyamat (6 perc)

Hozzon létre egy `samples/05-agents/orchestrator.py` fájlt:

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


### 5. Kezdő projekt: A `05-agent-architecture` kiterjesztése (7 perc)

Adja hozzá:
1. Tartós memória réteget (pl. JSON sorok hozzáfűzése a beszélgetésekhez)
2. Egyszerű értékelési rubrikát: tényszerűség / érthetőség / stílus helyőrzők
3. Opcionális Chainlit front-end (két fül: beszélgetés és nyomkövetés)
4. Opcionális LangGraph stílusú állapotgép (ha függőséget ad hozzá) az elágazási döntésekhez

## Érvényesítési ellenőrzőlista

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Várhatóan strukturált csővezeték kimenet eszközbeillesztési megjegyzéssel.

## Memória-stratégiák áttekintése

| Réteg       | Cél                 | Példa              |
|-------------|---------------------|--------------------|
| Rövid távú  | Párbeszéd folytonossága | Utolsó N üzenet    |
| Epizodikus  | Munkamenet visszaidézése | JSON munkamenetenként |
| Szemantikus | Hosszú távú visszakeresés | Összefoglalók vektortára |
| Jegyzetfüzet| Gondolkodási lépések | Inline gondolatlánc (privát) |

## Értékelési horgok (Koncepcionális)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Hibaelhárítás

| Probléma            | Ok                     | Megoldás                     |
|---------------------|------------------------|------------------------------|
| Ismétlődő válaszok  | Túl nagy/kicsi kontextusablak | Memóriaablak paraméterének hangolása |
| Eszköz nem hívható  | Hibás szintaxis        | Használja a `#tool:tool_name` formátumot |
| Lassú orkesztráció  | Több hideg modell      | Előzetes bemelegítő üzenetek futtatása |

## Hivatkozások

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (opcionális koncepció): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Szekció időtartama**: 30 perc  
**Nehézségi szint**: Haladó

## Példa forgatókönyv és workshop térkép

| Workshop szkript | Forgatókönyv | Célkitűzés | Példa prompt |
|------------------|--------------|------------|--------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Tudáskutató bot, amely vezetői összefoglalókat készít | Két ügynökből álló csővezeték (kutatás → szerkesztői finomítás) opcionális külön modellekkel | Magyarázza el, miért fontos az edge inference a megfelelőség szempontjából. |
| (Kiterjesztett) `tools.py` koncepció | Idő- és tokenbecslő eszközök hozzáadása | Könnyű eszközhasználati minta bemutatása | #tool:get_time |

### Forgatókönyv narratíva

A megfelelőségi dokumentációs csapatnak gyors belső összefoglalókra van szüksége, amelyeket helyi tudásból szereznek, anélkül, hogy a tervezeteket felhőszolgáltatásokba küldenék. Egy kutató ügynök tömör tényeket gyűjt össze; egy szerkesztő ügynök átfogalmazza azokat vezetői érthetőség érdekében. Különböző modell aliasok rendelhetők hozzá a késleltetés optimalizálásához (gyors SLM) vs stilisztikai finomítás (csak nagyobb modell szükség esetén).

### Példa többmodellű környezet

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Nyomkövetési struktúra (Opcionális)

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

Minden lépést JSONL fájlba menthet későbbi rubrika-alapú értékeléshez.

### Opcionális fejlesztések

| Téma              | Fejlesztés              | Előny                  | Megvalósítási vázlat         |
|-------------------|-------------------------|------------------------|------------------------------|
| Többmodellű szerepek | Különböző modellek ügynökönként (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializáció és sebesség | Alias környezeti változók kiválasztása, `chat_once` hívása szerepkör-alias szerint |
| Strukturált nyomkövetés | Minden művelet (eszköz, bemenet, késleltetés, tokenek) JSON nyomkövetése | Hibakeresés és értékelés | Szótár hozzáfűzése listához; `.jsonl` fájlba írás a végén |
| Memória tárolása | Újratölthető párbeszéd kontextus | Munkamenet folytonossága | `Agent.memory` mentése `sessions/<ts>.json` fájlba |
| Eszközregiszter | Dinamikus eszközfelfedezés | Bővíthetőség | `TOOLS` szótár karbantartása és nevek/leírások introspektálása |
| Újrapróbálkozás és visszalépés | Robusztus hosszú láncok | Átmeneti hibák csökkentése | `act` becsomagolása try/except + exponenciális visszalépéssel |
| Rubrika-alapú értékelés | Automatikus minőségi címkék | Fejlődés nyomon követése | Másodlagos passz modellel: "Értékeld az érthetőséget 1-5" |
| Vektor memória | Szemantikus visszaidézés | Gazdag hosszú távú kontextus | Összefoglalók beágyazása, top-k visszakeresése a rendszerüzenetbe |
| Folyamatos válaszok | Gyorsabb érzékelt válaszidő | Felhasználói élmény javítása | Folyamatos válaszok használata, amint elérhető, részleges tokenek kiírása |
| Determinisztikus tesztek | Regresszió kontroll | Stabil CI | Futtatás `temperature=0`, fix prompt magokkal |
| Párhuzamos elágazás | Gyorsabb feltárás | Átbocsátóképesség | `concurrent.futures` használata független ügynöklépésekhez |

#### Nyomkövetési rekord példa

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Egyszerű értékelési prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Mentse el az (`answer`, `rating`) párokat, hogy történeti minőségi grafikont készítsen.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.