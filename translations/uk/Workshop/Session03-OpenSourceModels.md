<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T00:49:21+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "uk"
}
-->
# Сесія 3: Моделі з відкритим кодом у Foundry Local

## Анотація

Дізнайтеся, як інтегрувати моделі Hugging Face та інші моделі з відкритим кодом у Foundry Local. Вивчіть стратегії вибору, робочі процеси внеску в спільноту, методологію порівняння продуктивності та способи розширення Foundry за допомогою реєстрації власних моделей. Ця сесія відповідає щотижневим темам дослідження "Model Mondays" і допоможе вам оцінити та впровадити моделі з відкритим кодом локально перед масштабуванням на Azure.

## Цілі навчання

До кінця ви зможете:

- **Відкривати та оцінювати**: Визначати кандидатів моделей (mistral, gemma, qwen, deepseek) з урахуванням компромісу між якістю та ресурсами.
- **Завантажувати та запускати**: Використовувати Foundry Local CLI для завантаження, кешування та запуску моделей спільноти.
- **Проводити бенчмаркінг**: Застосовувати узгоджені евристики затримки, пропускної здатності токенів та якості.
- **Розширювати**: Реєструвати або адаптувати власний обгортковий модуль моделі відповідно до сумісних з SDK шаблонів.
- **Порівнювати**: Створювати структуровані порівняння для вибору між SLM та середніми LLM.

## Попередні вимоги

- Завершені сесії 1 та 2
- Середовище Python з встановленим `foundry-local-sdk`
- Щонайменше 15 ГБ вільного диску для кешування кількох моделей

### Швидкий старт у кросплатформному середовищі

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

При проведенні бенчмаркінгу з macOS на хост-сервісі Windows встановіть:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстраційний процес (30 хв)

### 1. Завантаження моделей Hugging Face через CLI (8 хв)

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


### 2. Запуск та швидка перевірка (5 хв)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Скрипт бенчмаркінгу (8 хв)

Створіть `samples/03-oss-models/benchmark_models.py`:

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

Запустіть:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Порівняння продуктивності (5 хв)

Обговоріть компроміси: час завантаження, використання пам'яті (спостерігайте за Task Manager / `nvidia-smi` / монітором ресурсів ОС), якість вихідних даних у порівнянні зі швидкістю. Використовуйте Python-скрипт для бенчмаркінгу (Сесія 3) для затримки та пропускної здатності; повторіть після увімкнення прискорення GPU.

### 5. Стартовий проєкт (4 хв)

Створіть генератор звітів порівняння моделей (розширте скрипт бенчмаркінгу з експортом у формат markdown).

## Стартовий проєкт: Розширення `03-huggingface-models`

Покращіть існуючий зразок, додавши:

1. Агрегацію бенчмаркінгу + експорт у CSV/Markdown.
2. Просту якісну оцінку (набір пар запитів + файл ручної анотації).
3. JSON-конфігурацію (`models.json`) для списку моделей та набору запитів, що можна підключати.

## Контрольний список перевірки

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Усі цільові моделі повинні з'явитися та відповідати на запит чату.

## Приклад сценарію та відповідність воркшопу

| Скрипт воркшопу | Сценарій | Мета | Джерело запитів / набору даних |
|-----------------|----------|------|-------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Команда платформи Edge вибирає стандартний SLM для вбудованого підсумовувача | Створити порівняння затримки + p95 + токенів/сек серед кандидатів моделей | Вбудована змінна `PROMPT` + список середовища `BENCH_MODELS` |

### Опис сценарію
Інженери продукту повинні вибрати стандартну легку модель для підсумовування для функції офлайн-заміток зустрічей. Вони проводять контрольовані детерміновані бенчмарки (temperature=0) на фіксованому наборі запитів (див. приклад нижче) і збирають метрики затримки та пропускної здатності з GPU-акселерацією та без неї.

### Приклад JSON-набору запитів (розширюваний)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Циклічно обробляйте кожен запит для кожної моделі, фіксуйте затримку для кожного запиту, щоб отримати метрики розподілу та виявити аномалії.

## Рамка вибору моделі

| Вимір | Метрика | Чому це важливо |
|-------|--------|-----------------|
| Затримка | середнє / p95 | Консистенція користувацького досвіду |
| Пропускна здатність | токени/сек | Масштабованість пакетів та потоків |
| Пам'ять | розмір резидентної пам'яті | Відповідність пристрою та одночасність |
| Якість | рубрикові запити | Відповідність завданню |
| Розмір | кеш диску | Розповсюдження та оновлення |
| Ліцензія | дозвіл на використання | Відповідність комерційним вимогам |

## Розширення з власною моделлю

Загальний шаблон (псевдокод):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Зверніться до офіційного репозиторію для актуальних інтерфейсів адаптерів:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Вирішення проблем

| Проблема | Причина | Рішення |
|----------|---------|---------|
| OOM на mistral-7b | Недостатньо RAM/GPU | Зупиніть інші моделі; спробуйте менший варіант |
| Повільна перша відповідь | Холодне завантаження | Підтримуйте активність за допомогою періодичних легких запитів |
| Затримка завантаження | Нестабільність мережі | Повторіть спробу; попередньо завантажте в непіковий час |

## Ресурси

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Відкриття моделей Hugging Face: https://huggingface.co/models

---

**Тривалість сесії**: 30 хв (+ опціональне поглиблене вивчення)  
**Складність**: Середній рівень

### Опціональні покращення

| Покращення | Перевага | Як |
|------------|----------|----|
| Затримка першого токена в потоковому режимі | Вимірює сприйнятливу швидкість відповіді | Запустіть бенчмарк з `BENCH_STREAM=1` (покращений скрипт у `Workshop/samples/session03`) |
| Детермінований режим | Стабільні порівняння регресії | `temperature=0`, фіксований набір запитів, збереження JSON-виходів під контролем версій |
| Оцінка якості за рубрикою | Додає якісний вимір | Підтримуйте `prompts.json` з очікуваними аспектами; оцінюйте вручну або за допомогою додаткової моделі |
| Експорт у CSV / Markdown | Звіт для спільного використання | Розширте скрипт для запису `benchmark_report.md` з таблицею та основними моментами |
| Теги можливостей моделі | Допомагає автоматизованому маршрутизації | Підтримуйте `models.json` з `{alias: {capabilities:[], size_mb:..}}` |
| Фаза розігріву кешу | Зменшує упередженість холодного старту | Виконайте один розігрів перед циклом вимірювання часу (вже реалізовано) |
| Точність за процентилем | Надійна затримка хвоста | Використовуйте numpy percentile (вже у рефакторизованому скрипті) |
| Приблизна вартість токенів | Економічне порівняння | Приблизна вартість = (токени/сек * середня кількість токенів на запит) * енергетична евристика |
| Автоматичне пропускання невдалих моделей | Стійкість у пакетних запусках | Обгорніть кожен бенчмарк у try/except і позначте поле статусу |

#### Мінімальний фрагмент експорту Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Приклад детермінованого набору запитів

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Циклічно обробляйте статичний список замість випадкових запитів для порівнянних метрик між комітами.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->