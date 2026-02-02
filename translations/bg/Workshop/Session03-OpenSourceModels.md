# Сесия 3: Модели с отворен код във Foundry Local

## Резюме

Научете как да интегрирате модели от Hugging Face и други с отворен код във Foundry Local. Разберете стратегии за избор, работни процеси за принос към общността, методология за сравнение на производителността и как да разширите Foundry с персонализирани регистрации на модели. Тази сесия се свързва с седмичните теми на "Model Mondays" и ви подготвя да оценявате и използвате модели с отворен код локално, преди да ги мащабирате към Azure.

## Цели на обучението

До края ще можете:

- **Откриване и оценка**: Идентифициране на подходящи модели (mistral, gemma, qwen, deepseek) чрез баланс между качество и ресурси.
- **Зареждане и изпълнение**: Използване на Foundry Local CLI за изтегляне, кеширане и стартиране на модели от общността.
- **Бенчмарк**: Прилагане на последователни критерии за латентност, пропускателна способност на токени и качество.
- **Разширяване**: Регистриране или адаптиране на персонализиран модел, следвайки съвместими с SDK модели.
- **Сравнение**: Създаване на структурирани сравнения за избор между SLM и средни LLM модели.

## Предварителни изисквания

- Завършени сесии 1 и 2
- Python среда с инсталиран `foundry-local-sdk`
- Най-малко 15GB свободно дисково пространство за кеширане на множество модели

### Бърз старт за многоплатформена среда

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

При бенчмаркинг от macOS към Windows хост услуга, задайте:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрационен поток (30 минути)

### 1. Зареждане на модели от Hugging Face чрез CLI (8 минути)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Изпълнение и бърза проверка (5 минути)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Скрипт за бенчмарк (8 минути)

Създайте `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Изпълнете:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Сравнение на производителността (5 минути)

Обсъдете компромисите: време за зареждане, използване на памет (наблюдавайте Task Manager / `nvidia-smi` / монитор за ресурси на ОС), качество на изхода спрямо скорост. Използвайте Python скрипта за бенчмарк (Сесия 3) за латентност и пропускателна способност; повторете след активиране на GPU ускорение.

### 5. Начален проект (4 минути)

Създайте генератор за доклади за сравнение на модели (разширете скрипта за бенчмарк с експорт в markdown).

## Начален проект: Разширяване на `03-huggingface-models`

Подобрете съществуващия пример чрез:

1. Добавяне на агрегиране на бенчмарк + изход в CSV/Markdown.
2. Имплементиране на проста качествена оценка (набор от двойки подканващи + файл за ръчна анотация).
3. Въвеждане на JSON конфигурация (`models.json`) за списък с модели и набор от подканващи.

## Контролен списък за валидиране

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Всички целеви модели трябва да се появят и да отговорят на заявка за чат.

## Примерен сценарий и картографиране на работилницата

| Скрипт на работилницата | Сценарий | Цел | Източник на подканващи / набор от данни |
|-------------------------|----------|-----|-----------------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Екип за платформа на ръба, избиращ стандартен SLM за вграден обобщител | Създаване на сравнение на латентност + p95 + токени/секунда между кандидатите | Вградена променлива `PROMPT` + списък `BENCH_MODELS` в средата |

### Разказ за сценария

Екипът за продуктово инженерство трябва да избере стандартен лек модел за обобщение за функция за офлайн бележки от срещи. Те изпълняват контролирани детерминистични бенчмаркове (temperature=0) върху фиксиран набор от подканващи (вижте примера по-долу) и събират метрики за латентност и пропускателна способност с и без GPU ускорение.

### Примерен JSON за набор от подканващи (разширяем)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Циклирайте всяка подканваща за всеки модел, улавяйте латентността за всяка подканваща, за да извлечете метрики за разпределение и да откриете отклонения.

## Рамка за избор на модел

| Измерение | Метрика | Защо е важно |
|-----------|---------|--------------|
| Латентност | средно / p95 | Консистентност на потребителското изживяване |
| Пропускателна способност | токени/секунда | Скала за партиди и стрийминг |
| Памет | размер на резидентната памет | Съвместимост с устройството и едновременност |
| Качество | подканващи за оценка | Подходящост за задачата |
| Отпечатък | кеш на диска | Разпространение и актуализации |
| Лиценз | разрешение за използване | Съответствие с търговски изисквания |

## Разширяване с персонализиран модел

Високо ниво на шаблон (псевдо):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Консултирайте се с официалното хранилище за развиващи се интерфейси за адаптери:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Отстраняване на проблеми

| Проблем | Причина | Решение |
|---------|---------|---------|
| OOM на mistral-7b | Недостатъчна RAM/GPU | Спрете други модели; опитайте по-малък вариант |
| Бавен първи отговор | Студено зареждане | Поддържайте топло с периодична лека подканваща |
| Затруднения при изтегляне | Нестабилност на мрежата | Опитайте отново; предварително изтегляне извън пиковите часове |

## Референции

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Откриване на модели в Hugging Face: https://huggingface.co/models

---

**Продължителност на сесията**: 30 минути (+ опционално задълбочаване)  
**Трудност**: Средно напреднали

### Опционални подобрения

| Подобрение | Полза | Как |
|------------|-------|-----|
| Латентност на първия токен при стрийминг | Измерва възприеманата отзивчивост | Изпълнете бенчмарк с `BENCH_STREAM=1` (подобрен скрипт в `Workshop/samples/session03`) |
| Детерминистичен режим | Стабилни регресионни сравнения | `temperature=0`, фиксиран набор от подканващи, улавяне на JSON изходи под контрол на версиите |
| Оценка по качествена рубрика | Добавя качествено измерение | Поддържайте `prompts.json` с очаквани аспекти; анотирайте оценки (1–5) ръчно или чрез вторичен модел |
| Експорт в CSV / Markdown | Споделяем доклад | Разширете скрипта за запис на `benchmark_report.md` с таблица и акценти |
| Тагове за способности на модела | Помага за автоматизирано маршрутизиране по-късно | Поддържайте `models.json` с `{alias: {capabilities:[], size_mb:..}}` |
| Фаза на предварително загряване на кеша | Намалява пристрастията при студен старт | Изпълнете един топъл кръг преди времевия цикъл (вече имплементирано) |
| Точност на процентила | Робустна латентност на опашката | Използвайте numpy процентил (вече в рефакторирания скрипт) |
| Приблизителна цена на токен | Икономическо сравнение | Приблизителна цена = (токени/сек * средни токени на заявка) * енергийна евристика |
| Автоматично пропускане на неуспешни модели | Устойчивост при партидни изпълнения | Обгърнете всеки бенчмарк в try/except и маркирайте статус поле |

#### Минимален Markdown експортен фрагмент

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Пример за детерминистичен набор от подканващи

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Циклирайте статичния списък вместо случайни подканващи за сравними метрики между комитове.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->