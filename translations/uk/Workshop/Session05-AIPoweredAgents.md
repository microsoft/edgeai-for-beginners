# Сесія 5: Швидке створення агентів на основі AI з Foundry Local

## Анотація

Розробляйте та оркеструйте багаторольові AI-агенти, використовуючи середовище виконання Foundry Local з низькою затримкою та збереженням конфіденційності. Ви визначите ролі агентів, стратегії пам’яті, шаблони виклику інструментів та графи виконання. У сесії представлені шаблони структурування, які можна розширити за допомогою Chainlit або LangGraph. Стартовий проєкт розширює існуючу архітектуру агентів, додаючи збереження пам’яті та гачки для оцінювання.

## Цілі навчання

- **Визначення ролей**: Системні підказки та межі можливостей
- **Реалізація пам’яті**: Короткострокова (розмова), довгострокова (вектор / файл), тимчасові блокноти
- **Структурування робочих процесів**: Послідовні, розгалужені та паралельні кроки агентів
- **Інтеграція інструментів**: Легкий шаблон виклику функціональних інструментів
- **Оцінювання**: Базове трасування + оцінювання результатів за рубрикою

## Попередні вимоги

- Завершені сесії 1–4
- Python з `foundry-local-sdk`, `openai`, опціонально `chainlit`
- Локальні моделі запущені (принаймні `phi-4-mini`)

### Фрагмент середовища для різних платформ

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

Якщо агенти запускаються з macOS на віддаленому хост-сервісі Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстраційний процес (30 хв)

### 1. Визначення ролей агентів та пам’яті (7 хв)

Створіть `samples/05-agents/agents_core.py`:

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


### 2. Шаблон структурування CLI (3 хв)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Додавання виклику інструментів (7 хв)

Розширте за допомогою `samples/05-agents/tools.py`:

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


Змініть `agents_core.py`, щоб дозволити простий синтаксис інструментів: користувач пише `#tool:get_time`, і агент розширює вихід інструменту в контекст перед генерацією.

### 4. Оркестрування робочого процесу (6 хв)

Створіть `samples/05-agents/orchestrator.py`:

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


### 5. Стартовий проєкт: Розширення `05-agent-architecture` (7 хв)

Додайте:
1. Шар постійної пам’яті (наприклад, додавання JSON-рядків розмов)
2. Просту рубрику оцінювання: фактичність / ясність / стиль
3. Опціональний фронтенд Chainlit (дві вкладки: розмова та трасування)
4. Опціональний стиль машини станів LangGraph (якщо додається залежність) для розгалужених рішень

## Контрольний список перевірки

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Очікуйте структурований вихід конвеєра з приміткою про ін’єкцію інструментів.

## Огляд стратегій пам’яті

| Шар | Призначення | Приклад |
|-----|-------------|---------|
| Короткострокова | Безперервність діалогу | Останні N повідомлень |
| Епізодична | Запам’ятовування сесії | JSON для кожної сесії |
| Семантична | Довгострокове отримання | Векторне сховище резюме |
| Блокнот | Кроки міркувань | Вбудований ланцюг думок (приватний) |

## Гачки оцінювання (концептуально)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Вирішення проблем

| Проблема | Причина | Рішення |
|----------|---------|---------|
| Повторювані відповіді | Занадто великий/малий контекстний вікно | Налаштуйте параметр вікна пам’яті |
| Інструмент не викликаний | Неправильний синтаксис | Використовуйте формат `#tool:tool_name` |
| Повільне оркестрування | Кілька холодних моделей | Попередньо запустіть підказки для розігріву |

## Посилання

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (опціональна концепція): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Тривалість сесії**: 30 хв  
**Складність**: Висока

## Приклад сценарію та відповідність воркшопу

| Сценарій воркшопу | Сценарій | Ціль | Приклад підказки |
|-------------------|----------|------|------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Бот для дослідження знань, який створює резюме для керівників | Конвеєр з двома агентами (дослідження → редакційна обробка) з опціонально різними моделями | Поясніть, чому інференція на краю важлива для відповідності. |
| (Розширений) концепт `tools.py` | Додайте інструменти оцінки часу та токенів | Демонстрація легкого шаблону виклику інструментів | #tool:get_time |

### Опис сценарію
Команда з документування відповідності потребує швидких внутрішніх звітів, отриманих з локальних знань, без надсилання чернеток у хмарні сервіси. Агент-дослідник збирає короткі фактичні тези; агент-редактор переписує їх для ясності та зручності керівників. Можна призначити різні моделі для оптимізації затримки (швидка SLM) проти стилістичного вдосконалення (більша модель лише за потреби).

### Приклад багатомодельного середовища
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Структура трасування (опціонально)
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

Збережіть кожен крок у файл JSONL для подальшого оцінювання за рубрикою.

### Опціональні покращення

| Тема | Покращення | Перевага | Ескіз реалізації |
|------|------------|----------|------------------|
| Ролі багатомоделей | Різні моделі для кожного агента (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Спеціалізація та швидкість | Виберіть псевдоніми змінних середовища, викликайте `chat_once` з псевдонімом для кожної ролі |
| Структуровані трасування | JSON-трасування кожної дії (інструмент, введення, затримка, токени) | Налагодження та оцінювання | Додайте словник до списку; запишіть `.jsonl` наприкінці |
| Збереження пам’яті | Контекст діалогу, що можна перезавантажити | Безперервність сесії | Збережіть `Agent.memory` у `sessions/<ts>.json` |
| Реєстр інструментів | Динамічне виявлення інструментів | Розширюваність | Підтримуйте словник `TOOLS` та досліджуйте назви/опис |
| Повторні спроби та відступи | Надійні довгі ланцюги | Зменшення тимчасових збоїв | Обгорніть `act` у try/except + експоненціальний відступ |
| Оцінювання за рубрикою | Автоматизовані якісні мітки | Відстеження покращень | Вторинний прохід моделі: "Оцініть ясність 1-5" |
| Векторна пам’ять | Семантичне запам’ятовування | Багатий довгостроковий контекст | Вбудуйте резюме, отримайте top-k у системне повідомлення |
| Потокові відповіді | Швидше сприйняття відповіді | Покращення UX | Використовуйте потокову передачу, коли вона доступна, і виводьте часткові токени |
| Детерміновані тести | Контроль регресії | Стабільний CI | Запускайте з `temperature=0`, фіксованими насіннями підказок |
| Паралельне розгалуження | Швидше дослідження | Пропускна здатність | Використовуйте `concurrent.futures` для незалежних кроків агентів |

#### Приклад запису трасування

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Проста підказка для оцінювання

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Збережіть пари (`answer`, `rating`) для створення історичного графіка якості.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для отримання критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.