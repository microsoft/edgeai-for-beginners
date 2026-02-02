# Сесия 6: Foundry Local – Модели като инструменти

## Резюме

Отнасяйте се към моделите като към съставни инструменти в локален AI операционен слой. Тази сесия показва как да свържете множество специализирани SLM/LLM повиквания, да маршрутизирате задачи селективно и да предоставите унифицирана SDK повърхност за приложения. Ще изградите лек модел за маршрутизация + планировчик на задачи, ще го интегрирате в скрипт за приложение и ще очертаете пътя за мащабиране към Azure AI Foundry за производствени натоварвания.

## Цели на обучението

- **Концептуализирайте** моделите като атомни инструменти с декларирани възможности
- **Маршрутизирайте** заявки въз основа на намерение / евристично оценяване
- **Свържете** изходите през многоетапни задачи (разграждане → решаване → усъвършенстване)
- **Интегрирайте** унифициран клиентски API за приложения надолу по веригата
- **Мащабирайте** дизайна към облака (същия OpenAI-съвместим договор)

## Предварителни условия

- Завършени сесии 1–5
- Кеширани множество локални модели (например, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Фрагмент за кръстосана платформа

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

Достъп до отдалечена/виртуална машина от macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрационен поток (30 мин)

### 1. Декларация за възможности на инструмента (5 мин)

Създайте `samples/06-tools/models_catalog.py`:

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


### 2. Откриване на намерение и маршрутизация (8 мин)

Създайте `samples/06-tools/router.py`:

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


### 3. Свързване на многоетапни задачи (7 мин)

Създайте `samples/06-tools/pipeline.py`:

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


### 4. Начален проект: Адаптирайте `06-models-as-tools` (5 мин)

Подобрения:
- Добавете поддръжка за стрийминг на токени (прогресивно обновяване на UI)
- Добавете оценка на увереност: лексикално припокриване или рубрика за подканване
- Експортирайте JSON за проследяване (намерение → модел → латентност → използване на токени)
- Реализирайте повторно използване на кеша за повтарящи се подетапи

### 5. Път за мащабиране към Azure (5 мин)

| Слой | Локално (Foundry) | Облак (Azure AI Foundry) | Стратегия за преход |
|------|-------------------|--------------------------|---------------------|
| Маршрутизация | Евристичен Python | Устойчив микросървис | Контейнеризирайте и внедрете API |
| Модели | Кеширани SLMs | Управляеми внедрения | Картирайте локални имена към идентификатори на внедрения |
| Наблюдаемост | CLI статистики/ръчно | Централизирано логване и метрики | Добавете структурирани събития за проследяване |
| Сигурност | Само локален хост | Azure удостоверяване / мрежа | Въведете ключов трезор за тайни |
| Разходи | Ресурс на устройството | Таксуване за потребление | Добавете предпазни мерки за бюджет |

## Контролен списък за валидиране

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Очаквайте избор на модел въз основа на намерение и окончателен усъвършенстван изход.

## Отстраняване на проблеми

| Проблем | Причина | Решение |
|---------|---------|---------|
| Всички задачи се маршрутизират към един и същ модел | Слаби правила | Обогатете набора от regex INTENT_RULES |
| Пайплайнът се проваля в средата на етап | Липсва зареден модел | Изпълнете `foundry model run <model>` |
| Ниска съгласуваност на изхода | Няма фаза на усъвършенстване | Добавете обобщение/валидиране |

## Референции

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Документация: https://learn.microsoft.com/azure/ai-foundry
- Модели за качество на подканвания: Вижте Сесия 2

---

**Продължителност на сесията**: 30 мин  
**Трудност**: Експерт

## Примерен сценарий и картографиране на работилница

| Скриптове / Тетрадки за работилница | Сценарий | Цел | Източник на набор от данни / каталог |
|-------------------------------------|----------|-----|--------------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Асистент за разработчици, обработващ смесени подканвания за намерение (рефакториране, обобщение, класификация) | Евристично намерение → маршрутизация на псевдоним на модел с използване на токени | Вграден `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Многоетапно планиране и усъвършенстване за сложна задача за помощ при кодиране | Разграждане → специализирано изпълнение → обобщение и усъвършенстване | Същият `CATALOG`; етапи, извлечени от изхода на плана |

### Разказ за сценария
Инструмент за инженерна продуктивност получава хетерогенни задачи: рефакториране на код, обобщение на архитектурни бележки, класификация на обратна връзка. За да се минимизират латентността и използването на ресурси, малък общ модел планира и обобщава, специализиран модел за код обработва рефакториране, а лек модел за класификация етикетира обратната връзка. Скриптът за пайплайн демонстрира свързване + усъвършенстване; скриптът за маршрутизация изолира адаптивна маршрутизация с единична подканва.

### Снимка на каталога
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Примерни тестови подканвания
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Разширение за проследяване (по избор)
Добавете JSON линии за проследяване на етапи за `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Евристика за ескалация (Идея)
Ако планът съдържа ключови думи като "оптимизиране", "сигурност" или дължина на етапа > 280 символа → ескалирайте към по-голям модел (например, `gpt-oss-20b`) само за този етап.

### Подобрения по избор

| Област | Подобрение | Стойност | Подсказка |
|--------|------------|----------|-----------|
| Кеширане | Повторно използване на мениджър + клиентски обекти | По-ниска латентност, по-малко натоварване | Използвайте `workshop_utils.get_client` |
| Метрики за използване | Заснемане на токени и латентност на етап | Профилиране и оптимизация | Измерете всяко маршрутизирано повикване; съхранявайте в списък за проследяване |
| Адаптивна маршрутизация | Увереност / осведоменост за разходите | По-добър баланс качество-разходи | Добавете оценяване: ако подканването > N символа или regex съвпада с домейн → ескалирайте към по-голям модел |
| Динамичен регистър на възможности | Горещо презареждане на каталог | Без рестартиране на внедряване | Заредете `catalog.json` по време на изпълнение; наблюдавайте времевия печат на файла |
| Стратегия за резерв | Робустност при откази | По-висока наличност | Опитайте основен → при изключение резервен псевдоним |
| Стрийминг пайплайн | Ранна обратна връзка | Подобрение на UX | Стриймвайте всеки етап и буферирайте входа за окончателно усъвършенстване |
| Векторни вграждания за намерение | По-нюансирана маршрутизация | По-висока точност на намерението | Вградете подканването, клъстеризирайте и картографирайте центроид → възможност |
| Експорт на проследяване | Одитируемо свързване | Съответствие/отчитане | Излъчвайте JSON линии: етап, намерение, модел, латентност_ms, токени |
| Симулация на разходи | Предварителна оценка за облака | Планиране на бюджет | Присвойте условна стойност/токен на модел и обобщете на задача |
| Детерминистичен режим | Възпроизводимост | Стабилно бенчмаркиране | Env: `temperature=0`, фиксиран брой етапи |

#### Примерна структура за проследяване

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Скица за адаптивна ескалация

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Горещо презареждане на каталог на модели

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

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.