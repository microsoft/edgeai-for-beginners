<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T23:20:09+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "sr"
}
-->
# Сесија 5: Брзо креирање агената са вештачком интелигенцијом уз Foundry Local

## Апстракт

Дизајнирајте и оркестрирајте мултиролне AI агенте користећи Foundry Local окружење са ниском латенцијом и заштитом приватности. Дефинисаћете улоге агената, стратегије меморије, обрасце позивања алата и графике извршења. Сесија представља шаблоне које можете проширити уз Chainlit или LangGraph. Почетни пројекат проширује постојећу архитектуру агента додавањем перзистенције меморије и кука за евалуацију.

## Циљеви учења

- **Дефинисање улога**: Системски упити и границе способности
- **Имплементација меморије**: Краткорочна (разговор), дугорочна (вектор / фајл), ефермерне белешке
- **Шаблонирање радних токова**: Секвенцијални, разгранати и паралелни кораци агента
- **Интеграција алата**: Лаган образац позивања функција алата
- **Евалуација**: Основно праћење + оцењивање исхода на основу рубрика

## Предуслови

- Завршене сесије 1–4
- Python са `foundry-local-sdk`, `openai`, опционо `chainlit`
- Локални модели активни (најмање `phi-4-mini`)

### Упутство за окружење на више платформи

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

Ако покрећете агенте са macOS-а на удаљеном Windows хост сервису:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрација (30 минута)

### 1. Дефинисање улога агента и меморије (7 минута)

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


### 2. CLI шаблон (3 минута)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Додавање позивања алата (7 минута)

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


Измените `agents_core.py` да омогућите једноставну синтаксу алата: корисник пише `#tool:get_time`, а агент проширује излаз алата у контекст пре генерисања.

### 4. Оркестрирани радни ток (6 минута)

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


### 5. Почетни пројекат: Проширите `05-agent-architecture` (7 минута)

Додајте:
1. Слој перзистентне меморије (нпр. додавање JSON линија разговора)
2. Једноставну рубрику за евалуацију: фактуалност / јасноћа / стил
3. Опциони Chainlit предњи крај (две картице: разговор и праћење)
4. Опциони LangGraph стил машине стања (ако додате зависност) за одлуке о разгранавању

## Контролна листа за валидацију

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


Очекујте структуриран излаз из цевовода са белешком о убризгавању алата.

## Преглед стратегија меморије

| Слој | Сврха | Пример |
|------|-------|--------|
| Краткорочна | Континуитет дијалога | Последњих N порука |
| Епизодна | Подсећање на сесију | JSON по сесији |
| Семантичка | Дугорочно преузимање | Векторска меморија сажетака |
| Белешке | Кораци размишљања | Унутрашњи ланац мисли (приватно) |

## Куке за евалуацију (концептуално)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Решавање проблема

| Проблем | Узрок | Решење |
|---------|-------|--------|
| Понављајући одговори | Превелики/премали контекстуални прозор | Подесите параметар прозора меморије |
| Алат није позван | Погрешна синтакса | Користите формат `#tool:tool_name` |
| Спора оркестрација | Више хладних модела | Покрените загревање упита унапред |

## Референце

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (опциони концепт): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Трајање сесије**: 30 минута  
**Тежина**: Напредно

## Пример сценарија и мапирање радионице

| Скрипта радионице | Сценарио | Циљ | Пример упита |
|-------------------|----------|-----|--------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Бот за истраживање знања који производи резиме за извршне директоре | Цевовод са два агента (истраживање → уређивање) са опционо различитим моделима | Објасните зашто је инференција на ивици важна за усклађеност. |
| (Проширени) концепт `tools.py` | Додајте алате за процену времена и токена | Демонстрирајте лаган образац позивања алата | #tool:get_time |

### Наратив сценарија

Тиму за документацију о усклађености потребни су брзи интерни извештаји засновани на локалном знању без слања нацрта у облачне сервисе. Агент истраживач прикупља концизне чињеничне белешке; агент уредник их прерађује за извршну јасноћу. Могу се доделити различити модели за оптимизацију латенције (брзи SLM) у односу на стилско уређивање (већи модел само када је потребно).

### Пример окружења са више модела

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Структура праћења (опционо)

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


Сачувајте сваки корак у JSONL фајл за касније оцењивање рубрике.

### Опциона побољшања

| Тема | Побољшање | Предност | Скица имплементације |
|------|-----------|----------|-----------------------|
| Улоге са више модела | Различити модели по агенту (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Специјализација и брзина | Изаберите алијасе из окружења, позовите `chat_once` са алијасом по улози |
| Структурирано праћење | JSON праћење сваког акта (алат, улаз, латенција, токени) | Дебаговање и евалуација | Додајте речник у листу; пишите `.jsonl` на крају |
| Перзистенција меморије | Контекст дијалога који се може поново учитати | Континуитет сесије | Сачувајте `Agent.memory` у `sessions/<ts>.json` |
| Регистар алата | Динамичко откривање алата | Проширивост | Одржавајте `TOOLS` речник и испитујте имена/описе |
| Поновно покретање и одлагање | Робусни дуги ланци | Смањење привремених грешака | Обмотајте `act` са try/except + експоненцијално одлагање |
| Оцењивање рубрике | Аутоматизоване квалитативне ознаке | Праћење побољшања | Секундарно покретање модела: "Оцени јасноћу 1-5" |
| Векторска меморија | Семантичко преузимање | Богат дугорочни контекст | Угради сажетке, преузми топ-k у системску поруку |
| Стриминг одговора | Бржи перципирани одговор | Побољшање UX-а | Користите стриминг када буде доступан и испуштајте делимичне токене |
| Детерминистички тестови | Контрола регресије | Стабилан CI | Покрените са `temperature=0`, фиксним семенима упита |
| Паралелно разгранавање | Бржа експлорација | Продуктивност | Користите `concurrent.futures` за независне кораке агента |

#### Пример записа праћења

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


Сачувајте парове (`answer`, `rating`) за изградњу историјског графа квалитета.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.