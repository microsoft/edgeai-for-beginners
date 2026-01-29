# Сесія 6: Foundry Local – Моделі як інструменти

## Анотація

Розглядайте моделі як складові інструменти всередині локального AI операційного шару. У цій сесії показано, як об'єднувати кілька спеціалізованих викликів SLM/LLM, вибірково маршрутизувати завдання та надавати єдиний SDK для додатків. Ви створите легкий маршрутизатор моделей + планувальник завдань, інтегруєте його в скрипт додатка та окреслите шлях масштабування до Azure AI Foundry для робочих навантажень у виробництві.

## Цілі навчання

- **Уявляти** моделі як атомарні інструменти з задекларованими можливостями
- **Маршрутизувати** запити на основі намірів / евристичного оцінювання
- **Об'єднувати** результати через багатокрокові завдання (розкласти → вирішити → уточнити)
- **Інтегрувати** єдиний клієнтський API для додатків
- **Масштабувати** дизайн до хмари (той самий контракт, сумісний з OpenAI)

## Попередні вимоги

- Завершені сесії 1–5
- Кешовані кілька локальних моделей (наприклад, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Фрагмент для кросплатформного середовища

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Доступ до віддаленого/віртуального сервісу з macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстраційний процес (30 хв)

### 1. Декларація можливостей інструментів (5 хв)

Створіть `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Визначення намірів та маршрутизація (8 хв)

Створіть `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Об'єднання багатокрокових завдань (7 хв)

Створіть `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Стартовий проєкт: адаптація `06-models-as-tools` (5 хв)

Покращення:
- Додати підтримку потокової передачі токенів (поступове оновлення інтерфейсу)
- Додати оцінювання впевненості: лексичне співпадіння або рубрика запиту
- Експорт JSON трасування (намір → модель → затримка → використання токенів)
- Реалізувати повторне використання кешу для повторюваних підзадач

### 5. Шлях масштабування до Azure (5 хв)

| Шар | Локальний (Foundry) | Хмара (Azure AI Foundry) | Стратегія переходу |
|-----|----------------------|--------------------------|--------------------|
| Маршрутизація | Евристичний Python | Довговічний мікросервіс | Контейнеризація та розгортання API |
| Моделі | Кешовані SLM | Керовані розгортання | Відображення локальних назв на ID розгортання |
| Спостережуваність | Статистика CLI/ручна | Центральний журнал та метрики | Додати структуровані події трасування |
| Безпека | Лише локальний хост | Azure аутентифікація / мережа | Впровадження сховища ключів для секретів |
| Вартість | Ресурси пристрою | Оплата за споживання | Додати обмеження бюджету |

## Контрольний список перевірки

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Очікуйте вибір моделі на основі намірів та остаточного уточненого результату.

## Вирішення проблем

| Проблема | Причина | Рішення |
|----------|---------|---------|
| Усі завдання маршрутизуються до однієї моделі | Слабкі правила | Розширте набір regex INTENT_RULES |
| Помилка в середині виконання конвеєра | Модель не завантажена | Запустіть `foundry model run <model>` |
| Низька узгодженість результатів | Відсутня фаза уточнення | Додайте етап узагальнення/перевірки |

## Посилання

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Документація Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Шаблони якості запитів: див. Сесію 2

---

**Тривалість сесії**: 30 хв  
**Складність**: Експерт

## Приклад сценарію та відповідність воркшопу

| Скрипти воркшопу / Ноутбуки | Сценарій | Мета | Джерело даних / каталог |
|-----------------------------|----------|------|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Асистент розробника, який обробляє змішані запити (рефакторинг, узагальнення, класифікація) | Евристична маршрутизація намірів → псевдоніми моделей з використанням токенів | Вбудований `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Планування та уточнення багатокрокових завдань для складних завдань з програмування | Розкласти → спеціалізоване виконання → етап уточнення узагальнення | Той самий `CATALOG`; кроки отримані з результату плану |

### Опис сценарію
Інструмент для підвищення продуктивності інженерів отримує різнорідні завдання: рефакторинг коду, узагальнення архітектурних нотаток, класифікація відгуків. Щоб мінімізувати затримку та використання ресурсів, невелика загальна модель планує та узагальнює, спеціалізована модель для коду займається рефакторингом, а легка модель для класифікації маркує відгуки. Скрипт конвеєра демонструє об'єднання + уточнення; скрипт маршрутизатора ізолює адаптивну маршрутизацію одного запиту.

### Знімок каталогу
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Приклади тестових запитів
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Розширення трасування (опціонально)
Додайте лінії JSON трасування для кожного кроку у `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Евристика ескалації (ідея)
Якщо план містить ключові слова, такі як "оптимізувати", "безпека", або довжина кроку > 280 символів → ескалація до більшої моделі (наприклад, `gpt-oss-20b`) лише для цього кроку.

### Опціональні покращення

| Область | Покращення | Цінність | Підказка |
|---------|------------|----------|----------|
| Кешування | Повторне використання об'єктів менеджера + клієнта | Зниження затримки, менше навантаження | Використовуйте `workshop_utils.get_client` |
| Метрики використання | Захоплення токенів та затримки на кожному кроці | Профілювання та оптимізація | Виміряйте час кожного виклику маршрутизації; зберігайте у списку трасування |
| Адаптивна маршрутизація | Впевненість / обізнаність про витрати | Кращий баланс якості та витрат | Додайте оцінювання: якщо запит > N символів або regex відповідає домену → ескалація до більшої моделі |
| Динамічний реєстр можливостей | Гаряче перезавантаження каталогу | Без перезапуску розгортання | Завантажуйте `catalog.json` під час виконання; слідкуйте за часовою міткою файлу |
| Стратегія резервування | Надійність у разі збоїв | Вища доступність | Спробуйте основну → у разі виключення резервний псевдонім |
| Потоковий конвеєр | Ранній зворотний зв'язок | Покращення UX | Потоково передавайте кожен крок і буферизуйте остаточний ввід для уточнення |
| Векторні вбудовування намірів | Більш точна маршрутизація | Вища точність намірів | Вбудуйте запит, кластеризуйте та зіставте центроїд → можливість |
| Експорт трасування | Аудитний ланцюг | Відповідність/звітність | Виводьте JSON лінії: крок, намір, модель, затримка_ms, токени |
| Симуляція витрат | Оцінка перед хмарою | Планування бюджету | Призначте умовну вартість/токен для кожної моделі та агрегуйте за завданням |
| Детермінований режим | Відтворюваність тестів | Стабільне тестування | Env: `temperature=0`, фіксована кількість кроків |

#### Приклад структури трасування

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Ескіз адаптивної ескалації

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Гаряче перезавантаження каталогу моделей

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.