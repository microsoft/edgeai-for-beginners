<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:17:55+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "bg"
}
-->
# Примери за работилница - Обобщение на актуализацията на Foundry Local SDK

## Преглед

Всички Python примери в директорията `Workshop/samples` са актуализирани, за да следват най-добрите практики на Foundry Local SDK и да осигурят последователност в рамките на работилницата.

**Дата**: 8 октомври 2025  
**Обхват**: 9 Python файла в 6 сесии на работилницата  
**Основен фокус**: Обработка на грешки, документация, модели на SDK, потребителско изживяване

---

## Актуализирани файлове

### Сесия 01: Първи стъпки
- ✅ `chat_bootstrap.py` - Основни примери за чат и стрийминг

### Сесия 02: RAG решения
- ✅ `rag_pipeline.py` - RAG имплементация с вграждания
- ✅ `rag_eval_ragas.py` - Оценка на RAG с метрики на RAGAS

### Сесия 03: Модели с отворен код
- ✅ `benchmark_oss_models.py` - Бенчмаркинг на множество модели

### Сесия 04: Най-нови модели
- ✅ `model_compare.py` - Сравнение между SLM и LLM

### Сесия 05: Агенти, задвижвани от AI
- ✅ `agents_orchestrator.py` - Координация на множество агенти

### Сесия 06: Модели като инструменти
- ✅ `models_router.py` - Рутинг на модели, базиран на намерение
- ✅ `models_pipeline.py` - Многоетапен рутинг в pipeline

### Поддържаща инфраструктура
- ✅ `workshop_utils.py` - Вече следва най-добрите практики (няма нужда от промени)

---

## Основни подобрения

### 1. Подобрена обработка на грешки

**Преди:**
```python
manager, client, model_id = get_client(alias)
```

**След:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Ползи:**
- Елегантна обработка на грешки с ясни съобщения
- Полезни съвети за отстраняване на проблеми
- Коректни кодове за изход при скриптове

### 2. По-добро управление на импорти

**Преди:**
```python
from sentence_transformers import SentenceTransformer
```

**След:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Ползи:**
- Ясни указания при липса на зависимости
- Предотвратяване на неясни грешки при импортиране
- Удобни инструкции за инсталация

### 3. Изчерпателна документация

**Добавено към всички примери:**
- Документация за променливи на средата в docstrings
- Връзки към SDK референции
- Примери за употреба
- Подробна документация за функции/параметри
- Типови подсказки за по-добра поддръжка в IDE

**Пример:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Подобрена обратна връзка към потребителя

**Добавено информативно логване:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Индикатори за прогрес:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Структуриран изход:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Надежден бенчмаркинг

**Подобрения в Сесия 03:**
- Обработка на грешки за всеки модел (продължава при неуспех)
- Подробно докладване на прогреса
- Коректно изпълнение на загряващи рундове
- Поддръжка за измерване на латентност на първия токен
- Ясно разделение на етапите

### 6. Последователни типови подсказки

**Добавено навсякъде:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Ползи:**
- По-добра автоматична допълняемост в IDE
- Ранно откриване на грешки
- Самодокументиращ се код

### 7. Подобрен рутер за модели

**Подобрения в Сесия 06:**
- Изчерпателна документация за откриване на намерения
- Обяснение на алгоритъма за избор на модел
- Подробни логове за рутинг
- Форматиране на тестовия изход
- Възстановяване от грешки при групово тестване

### 8. Оркестрация на множество агенти

**Подобрения в Сесия 05:**
- Докладване на прогреса етап по етап
- Обработка на грешки за всеки агент
- Ясна структура на pipeline
- По-добра документация за управление на паметта

---

## Контролен списък за тестване

### Предпоставки
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Тествайте всеки пример

#### Сесия 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Сесия 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Сесия 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Сесия 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Сесия 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Сесия 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Референция за променливи на средата

### Глобални (за всички примери)
| Променлива | Описание | По подразбиране |
|------------|----------|-----------------|
| `FOUNDRY_LOCAL_ALIAS` | Псевдоним на модела за използване | Различен за всеки пример |
| `FOUNDRY_LOCAL_ENDPOINT` | Пренасочване на крайна точка на услугата | Автоматично откриване |
| `SHOW_USAGE` | Показване на използването на токени | `0` |
| `RETRY_ON_FAIL` | Активиране на логика за повторение | `1` |
| `RETRY_BACKOFF` | Начално забавяне при повторение | `1.0` |

### Специфични за примери
| Променлива | Използва се от | Описание |
|------------|---------------|----------|
| `EMBED_MODEL` | Сесия 02 | Име на модела за вграждане |
| `RAG_QUESTION` | Сесия 02 | Тестов въпрос за RAG |
| `BENCH_MODELS` | Сесия 03 | Модели за бенчмаркинг, разделени със запетая |
| `BENCH_ROUNDS` | Сесия 03 | Брой рундове за бенчмаркинг |
| `BENCH_PROMPT` | Сесия 03 | Тестов prompt за бенчмаркинг |
| `BENCH_STREAM` | Сесия 03 | Измерване на латентност на първия токен |
| `SLM_ALIAS` | Сесия 04 | Псевдоним на малък езиков модел |
| `LLM_ALIAS` | Сесия 04 | Псевдоним на голям езиков модел |
| `COMPARE_PROMPT` | Сесия 04 | Тестов prompt за сравнение |
| `AGENT_MODEL_PRIMARY` | Сесия 05 | Основен модел за агент |
| `AGENT_MODEL_EDITOR` | Сесия 05 | Модел за редактор агент |
| `AGENT_QUESTION` | Сесия 05 | Тестов въпрос за агенти |
| `PIPELINE_TASK` | Сесия 06 | Задача за pipeline |

---

## Промени, нарушаващи съвместимостта

**Няма** - Всички промени са съвместими с предишните версии.

Съществуващите скриптове ще продължат да работят. Новите функции са:
- Опционални променливи на средата
- Подобрени съобщения за грешки (не нарушават функционалността)
- Допълнително логване (може да бъде изключено)
- По-добри типови подсказки (без влияние върху изпълнението)

---

## Внедрени най-добри практики

### 1. Винаги използвайте Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Коректен модел за обработка на грешки
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Информативно логване
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Типови подсказки
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Изчерпателни docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Поддръжка на променливи на средата
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Елегантна деградация
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Чести проблеми и решения

### Проблем: Грешки при импортиране
**Решение:** Инсталирайте липсващите зависимости
```bash
pip install sentence-transformers ragas datasets numpy
```

### Проблем: Грешки при свързване
**Решение:** Уверете се, че Foundry Local работи
```bash
foundry service status
foundry model run phi-4-mini
```

### Проблем: Моделът не е намерен
**Решение:** Проверете наличните модели
```bash
foundry model ls
foundry model download <alias>
```

### Проблем: Бавна производителност
**Решение:** Използвайте по-малки модели или коригирайте параметрите
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Следващи стъпки

### 1. Тествайте всички примери
Изпълнете контролния списък за тестване по-горе, за да се уверите, че всички примери работят правилно.

### 2. Актуализирайте документацията
- Актуализирайте markdown файловете на сесиите с нови примери
- Добавете секция за отстраняване на проблеми към основния README
- Създайте кратък справочник

### 3. Създайте интеграционни тестове
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Добавете бенчмаркинг на производителността
Проследете подобренията в производителността от подобренията в обработката на грешки.

### 5. Обратна връзка от потребителите
Съберете обратна връзка от участниците в работилницата относно:
- Яснотата на съобщенията за грешки
- Пълнотата на документацията
- Леснотата на използване

---

## Ресурси

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Кратък справочник**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Бележки за миграция**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Основно хранилище**: https://github.com/microsoft/Foundry-Local

---

## Поддръжка

### Добавяне на нови примери
Следвайте тези модели при създаване на нови примери:

1. Използвайте `workshop_utils` за управление на клиента
2. Добавете изчерпателна обработка на грешки
3. Включете поддръжка на променливи на средата
4. Добавете типови подсказки и docstrings
5. Осигурете информативно логване
6. Включете примери за употреба в docstring
7. Връзка към документацията на SDK

### Преглед на актуализации
При преглед на актуализации на примери, проверете:
- [ ] Обработка на грешки при всички I/O операции
- [ ] Типови подсказки за публични функции
- [ ] Изчерпателни docstrings
- [ ] Документация за променливи на средата
- [ ] Информативна обратна връзка към потребителя
- [ ] Връзки към SDK референции
- [ ] Последователен стил на код

---

**Обобщение**: Всички Python примери за работилницата вече следват най-добрите практики на Foundry Local SDK с подобрена обработка на грешки, изчерпателна документация и подобрено потребителско изживяване. Няма промени, нарушаващи съвместимостта - цялата съществуваща функционалност е запазена и подобрена.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.