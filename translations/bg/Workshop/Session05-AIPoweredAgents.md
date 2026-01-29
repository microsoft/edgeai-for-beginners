# Сесия 5: Бързо изграждане на AI агенти с Foundry Local

## Резюме

Проектирайте и организирайте AI агенти с множество роли, използвайки средата на Foundry Local с ниска латентност и защита на личните данни. Ще дефинирате роли на агенти, стратегии за памет, модели за извикване на инструменти и графики за изпълнение. Сесията представя шаблони за структуриране, които можете да разширите с Chainlit или LangGraph. Началният проект разширява съществуващата архитектура на агенти, като добавя постоянство на паметта и куки за оценка.

## Цели на обучението

- **Дефиниране на роли**: Системни подсказки и граници на възможностите
- **Реализиране на памет**: Краткосрочна (разговор), дългосрочна (вектор / файл), временни бележници
- **Структуриране на работни потоци**: Последователни, разклонени и паралелни стъпки на агенти
- **Интегриране на инструменти**: Лек модел за извикване на функции
- **Оценка**: Основно проследяване + оценка на резултатите по критерии

## Предварителни изисквания

- Завършени сесии 1–4
- Python с `foundry-local-sdk`, `openai`, опционално `chainlit`
- Локално работещи модели (поне `phi-4-mini`)

### Код за многоплатформена среда

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

Ако стартирате агенти от macOS към отдалечена Windows услуга:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Демонстрационен процес (30 минути)

### 1. Дефиниране на роли и памет на агенти (7 минути)

Създайте `samples/05-agents/agents_core.py`:

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

### 2. Шаблон за CLI структуриране (3 минути)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Добавяне на извикване на инструменти (7 минути)

Разширете с `samples/05-agents/tools.py`:

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

Модифицирайте `agents_core.py`, за да позволите прост синтаксис за инструменти: потребителят пише `#tool:get_time`, а агентът разширява изхода на инструмента в контекста преди генериране.

### 4. Организиран работен поток (6 минути)

Създайте `samples/05-agents/orchestrator.py`:

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

### 5. Начален проект: Разширяване на `05-agent-architecture` (7 минути)

Добавете:
1. Слой за постоянна памет (например, добавяне на JSON линии за разговори)
2. Прост критерий за оценка: placeholders за фактичност / яснота / стил
3. Опционален Chainlit интерфейс (два таба: разговор и проследяване)
4. Опционална LangGraph стилова машина за състояния (ако добавите зависимост) за решения с разклонения

## Контролен списък за валидиране

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Очаквайте структурирани изходни данни от тръбопровода с бележка за инжектиране на инструменти.

## Преглед на стратегии за памет

| Слой | Цел | Пример |
|------|-----|--------|
| Краткосрочна | Непрекъснатост на диалога | Последните N съобщения |
| Епизодична | Спомняне на сесията | JSON за всяка сесия |
| Семантична | Дългосрочно извличане | Векторно хранилище на резюмета |
| Бележник | Стъпки на разсъждение | Вградена верига на мисли (лична) |

## Куки за оценка (Концептуално)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Отстраняване на проблеми

| Проблем | Причина | Решение |
|---------|---------|---------|
| Повтарящи се отговори | Прозорецът на контекста е твърде голям/малък | Настройте параметъра за прозорец на паметта |
| Инструментът не е извикан | Неправилен синтаксис | Използвайте формат `#tool:tool_name` |
| Бавна организация | Множество студени модели | Предварително стартирайте подготвителни подсказки |

## Референции

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (опционална концепция): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Продължителност на сесията**: 30 минути  
**Трудност**: Напреднала

## Примерен сценарий и картографиране на работилница

| Скрипт на работилницата | Сценарий | Цел | Примерна подсказка |
|-------------------------|----------|-----|--------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Бот за изследване на знания, който създава резюмета за ръководители | Тръбопровод с два агента (изследване → редакторска обработка) с опционални различни модели | Обяснете защо локалното извеждане е важно за съответствието. |
| (Разширена) концепция `tools.py` | Добавяне на инструменти за време и оценка на токени | Демонстрация на лек модел за извикване на инструменти | #tool:get_time |

### Разказ за сценария
Екипът за документация за съответствие се нуждае от бързи вътрешни резюмета, извлечени от локални знания, без да изпраща чернови към облачни услуги. Агенти за изследване събират кратки фактически точки; редакторски агент пренаписва за яснота, подходяща за ръководители. Могат да се зададат различни псевдоними на модели за оптимизиране на латентността (бърз SLM) срещу стилистично усъвършенстване (по-голям модел само когато е необходимо).

### Примерна многомоделна среда
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### Структура на проследяване (опционално)
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

Запазете всяка стъпка в JSONL файл за по-късно оценяване по критерии.

### Опционални подобрения

| Тема | Подобрение | Полза | Скица за реализация |
|------|-----------|-------|---------------------|
| Роли с многомоделност | Различни модели за всеки агент (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Специализация и скорост | Изберете псевдоними за среда, извикайте `chat_once` с псевдоним за всяка роля |
| Структурирани проследявания | JSON проследяване на всяко действие (инструмент, вход, латентност, токени) | Дебъг и оценка | Добавете речник към списък; запишете `.jsonl` в края |
| Постоянство на паметта | Възможност за презареждане на контекста на диалога | Непрекъснатост на сесията | Запишете `Agent.memory` в `sessions/<ts>.json` |
| Регистър на инструменти | Динамично откриване на инструменти | Разширяемост | Поддържайте речник `TOOLS` и инспектирайте имена/описания |
| Повторение и изчакване | Устойчиви дълги вериги | Намаляване на временни грешки | Обвийте `act` с try/except + експоненциално изчакване |
| Оценка по критерии | Автоматизирани качествени етикети | Проследяване на подобрения | Вторично преминаване с модел: "Оцени яснота 1-5" |
| Векторна памет | Семантично извличане | Богат дългосрочен контекст | Вградете резюмета, извлечете топ-k в системното съобщение |
| Потокови отговори | По-бързо възприемане на отговорите | Подобрение на UX | Използвайте поточно предаване, когато е налично, и изчистете частични токени |
| Детерминистични тестове | Контрол на регресията | Стабилно CI | Стартирайте с `temperature=0`, фиксирани семена за подсказки |
| Паралелно разклоняване | По-бързо изследване | Пропускателна способност | Използвайте `concurrent.futures` за независими стъпки на агенти |

#### Пример за запис на проследяване

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Проста подсказка за оценка

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Запазете двойки (`answer`, `rating`), за да изградите исторически график за качество.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.