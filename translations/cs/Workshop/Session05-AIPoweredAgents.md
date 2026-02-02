# Sezení 5: Rychlá tvorba agentů s umělou inteligencí pomocí Foundry Local

## Abstrakt

Navrhněte a koordinujte AI agenty s více rolemi pomocí runtime prostředí Foundry Local, které zajišťuje nízkou latenci a ochranu soukromí. Definujete role agentů, strategie paměti, vzory volání nástrojů a grafy provádění. Sezení představí vzory pro strukturování, které můžete rozšířit pomocí Chainlit nebo LangGraph. Startovací projekt rozšiřuje existující vzor architektury agentů o perzistenci paměti a hodnotící háčky.

## Cíle učení

- **Definovat role**: Systémové výzvy a hranice schopností
- **Implementovat paměť**: Krátkodobou (konverzace), dlouhodobou (vektor / soubor), dočasné poznámkové bloky
- **Strukturovat pracovní postupy**: Sekvenční, větvené a paralelní kroky agentů
- **Integrovat nástroje**: Lehký vzor volání funkcí nástrojů
- **Hodnotit**: Základní sledování + hodnocení výsledků podle kritérií

## Předpoklady

- Dokončené sezení 1–4
- Python s `foundry-local-sdk`, `openai`, volitelně `chainlit`
- Lokální modely spuštěné (alespoň `phi-4-mini`)

### Ukázka prostředí pro různé platformy

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

Pokud spouštíte agenty z macOS na vzdálené hostitelské službě Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Průběh ukázky (30 minut)

### 1. Definování rolí agentů a paměti (7 minut)

Vytvořte `samples/05-agents/agents_core.py`:

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


### 2. Vzor strukturování CLI (3 minuty)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Přidání volání nástrojů (7 minut)

Rozšiřte pomocí `samples/05-agents/tools.py`:

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

Upravte `agents_core.py`, aby umožňoval jednoduchou syntaxi nástrojů: uživatel napíše `#tool:get_time` a agent rozšíří výstup nástroje do kontextu před generováním.

### 4. Koordinovaný pracovní postup (6 minut)

Vytvořte `samples/05-agents/orchestrator.py`:

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


### 5. Startovací projekt: Rozšíření `05-agent-architecture` (7 minut)

Přidejte:
1. Vrstvu perzistentní paměti (např. přidávání konverzací do JSON řádků)
2. Jednoduché hodnotící kritérium: faktualita / jasnost / styl
3. Volitelný front-end Chainlit (dvě záložky: konverzace a sledování)
4. Volitelný stavový automat ve stylu LangGraph (pokud přidáte závislost) pro rozhodování o větvení

## Kontrolní seznam validace

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Očekávejte strukturovaný výstup pipeline s poznámkou o injekci nástroje.

## Přehled strategií paměti

| Vrstva | Účel | Příklad |
|--------|------|---------|
| Krátkodobá | Kontinuita dialogu | Posledních N zpráv |
| Epizodická | Připomenutí sezení | JSON pro každé sezení |
| Sémantická | Dlouhodobé vyhledávání | Vektorový úložiště souhrnů |
| Poznámkový blok | Kroky uvažování | Inline řetězec myšlenek (soukromý) |

## Hodnotící háčky (konceptuální)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Řešení problémů

| Problém | Příčina | Řešení |
|---------|---------|--------|
| Opakující se odpovědi | Příliš velké/malé okno kontextu | Upravte parametr okna paměti |
| Nástroj nebyl spuštěn | Nesprávná syntaxe | Použijte formát `#tool:tool_name` |
| Pomalá koordinace | Více studených modelů | Předehřejte modely pomocí úvodních výzev |

## Odkazy

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (volitelný koncept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Délka sezení**: 30 minut  
**Obtížnost**: Pokročilá

## Ukázkový scénář a mapování workshopu

| Skript workshopu | Scénář | Cíl | Ukázkový výzva |
|------------------|--------|-----|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot pro výzkum znalostí vytvářející přehledy vhodné pro vedení | Pipeline dvou agentů (výzkum → redakční úprava) s volitelnými odlišnými modely | Vysvětlete, proč je důležité okrajové inferenční zpracování pro dodržování předpisů. |
| (Rozšířený) koncept `tools.py` | Přidání nástrojů pro odhad času a tokenů | Ukázka lehkého vzoru volání nástrojů | #tool:get_time |

### Narativ scénáře
Tým pro dokumentaci dodržování předpisů potřebuje rychlé interní přehledy získané z lokálních znalostí bez odesílání návrhů na cloudové služby. Agent výzkumník shromažďuje stručné faktické body; editor agent upravuje text pro jasnost a srozumitelnost pro vedení. Lze přiřadit odlišné aliasy modelů pro optimalizaci latence (rychlý SLM) vs stylistické úpravy (větší model pouze v případě potřeby).

### Ukázkové prostředí s více modely
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktura sledování (volitelné)
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

Uložte každý krok do souboru JSONL pro pozdější hodnocení podle kritérií.

### Volitelná vylepšení

| Téma | Vylepšení | Přínos | Náčrt implementace |
|------|-----------|--------|--------------------|
| Role s více modely | Odlišné modely pro agenty (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializace a rychlost | Vyberte aliasy prostředí, volejte `chat_once` s aliasem pro každou roli |
| Strukturované sledování | JSON sledování každého aktu (nástroj, vstup, latence, tokeny) | Ladění a hodnocení | Přidejte slovník do seznamu; na konci zapište `.jsonl` |
| Perzistence paměti | Znovunačitatelný kontext dialogu | Kontinuita sezení | Uložte `Agent.memory` do `sessions/<ts>.json` |
| Registr nástrojů | Dynamické objevování nástrojů | Rozšiřitelnost | Udržujte slovník `TOOLS` a prozkoumávejte názvy/popisy |
| Opakování a zpětné odložení | Robustní dlouhé řetězce | Snížení přechodných chyb | Obalte `act` try/except + exponenciální zpětné odložení |
| Hodnocení podle kritérií | Automatické kvalitativní štítky | Sledování zlepšení | Sekundární průchod modelu: "Ohodnoťte jasnost 1-5" |
| Vektorová paměť | Sémantické vyhledávání | Bohatý dlouhodobý kontext | Vložte souhrny, vyhledejte top-k do systémové zprávy |
| Streamované odpovědi | Rychlejší vnímaná odezva | Zlepšení UX | Použijte streamování, jakmile bude dostupné, a průběžně odesílejte částečné tokeny |
| Deterministické testy | Kontrola regresí | Stabilní CI | Spusťte s `temperature=0`, pevnými semeny výzev |
| Paralelní větvení | Rychlejší průzkum | Průchodnost | Použijte `concurrent.futures` pro nezávislé kroky agentů |

#### Příklad záznamu sledování

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Jednoduchá hodnotící výzva

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Uložte páry (`odpověď`, `hodnocení`) pro vytvoření historického grafu kvality.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.