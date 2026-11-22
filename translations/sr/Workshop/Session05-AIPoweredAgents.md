# Сесија 5: Брза изградња АИ-агената помоћу Foundry Local

## Резиме

Дизајнирајте и оркестрирајте вишеролнe АИ агентe користећи извршни систем с малом латенцијом и заштитом приватности Foundry Local. Дефинишете улоге агената, стратегије меморије, обрасце позивања алата и графиконе извршавања. Сесија представља образце који се могу проширити са Chainlit или LangGraph. Почетни пројекат проширује постојећи пример архитектуре агената додавајући перзистенцију меморије и окидаче за евалуацију.

## Циљеви учења

- **Дефинисање улога**: системске поруке и границе могућности
- **Имплементација меморије**: краткорочна (конверзација), дугорочна (вектор / фајл), ефермерни белешки
- **Оформљење радних токова**: секвенцијални, гранајући и паралелни кораци агената
- **Интеграција алата**: лагани образац позива функција алата
- **Евалуација**: основни траг + бодовање резултата по рубрици

## Предуслови

- Комплетиране сесије 1–4
- Python са `foundry-local-sdk`, `openai`, опционо `chainlit`
- Локални модели у покретању (барем `phi-4-mini`)

### Пример за више платформи

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

Ако покрећете агенте са macOS-а према удаљеном Windows хост сервису:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Ток демонстрације (30 мин)

### 1. Дефинисација улога агената и меморије (7 мин)

Креирајте `samples/05-agents/agents_core.py`:

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

### 2. CLI образац (3 мин)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Додавање позива алата (7 мин)

Проширите са `samples/05-agents/tools.py`:

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

Измените `agents_core.py` да бисте омогућили једноставну синтаксу алата: корисник пише `#tool:get_time`, а агент проширује излаз алата у контекст пре генерисања.

### 4. Оркестрирани радни ток (6 мин)

Креирајте `samples/05-agents/orchestrator.py`:

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

### 5. Почетни пројекат: проширите `05-agent-architecture` (7 мин)

Додајте:
1. Перзистентни слој меморије (нпр. додавање JSON линија конверзацијама)
2. Једноставна евалуациона рубрика: чињеничност / јасноћа / стил као маркери
3. Опционални Chainlit front-end (два таба: конверзација и трагови)
4. Опционална LangGraph стилска стања машина (ако додајете зависност) за одлуке о гранању

## Контрола валидности

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Очекујте структурисани излаз са напоменом о уметању алата.

## Преглед стратегија меморије

| Слой | Сврха | Пример |
|-------|---------|---------|
| Краткорочна | Континуитет дијалога | Последњих N порука |
| Епизодична | Подсећање на сесију | JSON по сесији |
| Семантичка | Дугорочно пребацивање | Векторска база резимеа |
| Белешка | Кораци резоновања | inline ланац размишљања (приватно) |

## Окидачи евалуације (концепт)

```python
evaluation = {
  "factuality": None,  # ручни или хеуристички
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Решавање проблема

| Проблем | Узрок | Решавање |
|-------|------|------------|
| Понављајући одговори | Прекомерно велики/мали контекстни прозор | Подесите параметар величине прозора меморије |
| Алат није позван | Погрешна синтакса | Користите формат `#tool:име_алата` |
| Споро оркестрирање | Више хладних модела | Покрените унапред иницијализационе поруке |

## Референце

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (опционални концепт): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Трајање сесије**: 30 мин  
**Тежина**: Напредна

## Пример сценарија и мапирање радионице

| Скрипта радионице | Сценарио | Циљ | Пример упита |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Бот за истраживање знања који прави резимее прилагођене руководству | Пипелине са два агента (истраживач → уредничка обрада) са опционалним дистинктним моделима | Објасните зашто је инференца на рубу важна за усаглашеност. |
| (Проширен) концепт `tools.py` | Додавање алата за процену времена и броја токена | Демонстрирајте лагани образац позива алата | #tool:get_time |

### Приповедање сценарија
Тим за документацију о усаглашености треба брзе интерне сажетке узете из локалног знања без слања на облачне сервисе. Истраживачки агент прикупља концизне чињеничне тачке; уреднички агент преписује за јасноћу руководству. Могу се доделити различити алијаси модела за оптимизацију латенције (брз SLM) у односу на стилску прецизност (већи модел само кад је потребно).

### Пример окружења са више модела
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### Структура трага (опционо)
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

Сваки корак се чува у JSONL датотеку ради каснијег бодовања по рубрици.

### Опционална побољшања

| Тема | Побољшање | Корист | Пример имплементације |
|-------|------------|---------|-----------------------|
| Улоге више модела | Различити модели по агенту (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Специјализација и брзина | Изаберите алијасе из env променљивих, позовите `chat_once` са алијасом по улози |
| Структурисани трагови | JSON траг сваког акта (алат, улаз, латенција, токени) | Дебаг и евалуација | Додајте речник у листу; напишите `.jsonl` на крају |
| Перзистенција меморије | Преузимање дијалог контекста | Континуитет сесије | Сачувајте `Agent.memory` у `sessions/<ts>.json` |
| Регистар алата | Динамичко откривање алата | Проширивост | Одржавајте `TOOLS` речник и истражујте имена/описе |
| Понављање & отказивање | Робусни дуги ланци | Смањите транзиентне грешке | Обавијте `act` са try/except + експоненцијално одлагање |
| Бодовање рубрике | Аутоматизоване квалитативне ознаке | Праћење напретка | Други корак: упит моделу "Оцени јасноћу од 1 до 5" |
| Векторска меморија | Семантичко подсећање | Богат дугорочни контекст | Ембедујте резимеа, преузмите top-k у системску поруку |
| Стриминг одговора | Бржи перципирани одговор | Побољшање корисничког искуства | Користите стриминг кад је доступан и испразните делимичне токене |
| Детерминистичка тестирања | Контрола регресије | Стабилно CI | Пустите са `temperature=0`, фиксним насумце извором упита |
| Паралелно гранање | Бржа експлорација | Пропусни опсег | Користите `concurrent.futures` за независне кораке агената |

#### Пример записа трага

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Једноставан упит за евалуацију

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Сачувајте парове (`answer`, `rating`) за креирање историјског графикона квалитета.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->