<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:44:41+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "uk"
}
-->
# Зразки для воркшопу - Оновлення Foundry Local SDK

## Огляд

Усі зразки на Python у каталозі `Workshop/samples` були оновлені відповідно до найкращих практик Foundry Local SDK, щоб забезпечити узгодженість у рамках воркшопу.

**Дата**: 8 жовтня 2025  
**Обсяг**: 9 файлів на Python у 6 сесіях воркшопу  
**Основний акцент**: Обробка помилок, документація, шаблони SDK, зручність для користувача

---

## Оновлені файли

### Сесія 01: Початок роботи
- ✅ `chat_bootstrap.py` - Основні приклади чату та потокової передачі

### Сесія 02: Рішення RAG
- ✅ `rag_pipeline.py` - Реалізація RAG з використанням ембедингів
- ✅ `rag_eval_ragas.py` - Оцінка RAG за допомогою метрик RAGAS

### Сесія 03: Моделі з відкритим кодом
- ✅ `benchmark_oss_models.py` - Бенчмаркінг багатьох моделей

### Сесія 04: Передові моделі
- ✅ `model_compare.py` - Порівняння SLM та LLM

### Сесія 05: Агенти на основі AI
- ✅ `agents_orchestrator.py` - Координація багатьох агентів

### Сесія 06: Моделі як інструменти
- ✅ `models_router.py` - Маршрутизація моделей на основі намірів
- ✅ `models_pipeline.py` - Багатокроковий маршрутизований конвеєр

### Підтримуюча інфраструктура
- ✅ `workshop_utils.py` - Вже відповідає найкращим практикам (змін не потрібно)

---

## Основні покращення

### 1. Покращена обробка помилок

**До:**
```python
manager, client, model_id = get_client(alias)
```

**Після:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Переваги:**
- Акуратна обробка помилок із чіткими повідомленнями
- Практичні підказки для усунення несправностей
- Коректні коди виходу для скриптів

### 2. Кращий менеджмент імпорту

**До:**
```python
from sentence_transformers import SentenceTransformer
```

**Після:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Переваги:**
- Чіткі інструкції при відсутності залежностей
- Запобігання неясним помилкам імпорту
- Зручні інструкції з встановлення

### 3. Комплексна документація

**Додано до всіх зразків:**
- Документація змінних середовища у docstrings
- Посилання на SDK
- Приклади використання
- Детальна документація функцій/параметрів
- Підказки типів для кращої підтримки IDE

**Приклад:**
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

### 4. Покращений зворотний зв'язок для користувача

**Додано інформативне логування:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Індикатори прогресу:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Структурований вивід:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Надійний бенчмаркінг

**Покращення для сесії 03:**
- Обробка помилок для кожної моделі (продовження у разі збою)
- Детальна звітність про прогрес
- Коректне виконання розігріву
- Підтримка вимірювання затримки першого токена
- Чітке розділення етапів

### 6. Узгоджені підказки типів

**Додано всюди:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Переваги:**
- Краща автозаповнення в IDE
- Раннє виявлення помилок
- Самодокументуючий код

### 7. Покращена маршрутизація моделей

**Покращення для сесії 06:**
- Комплексна документація виявлення намірів
- Пояснення алгоритму вибору моделі
- Детальні журнали маршрутизації
- Форматування тестового виводу
- Відновлення помилок у пакетному тестуванні

### 8. Оркестрація багатьох агентів

**Покращення для сесії 05:**
- Звітність про прогрес на кожному етапі
- Обробка помилок для кожного агента
- Чітка структура конвеєра
- Краща документація управління пам'яттю

---

## Контрольний список тестування

### Попередні умови
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Тестування кожного зразка

#### Сесія 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Сесія 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Сесія 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Сесія 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Сесія 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Сесія 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Довідник змінних середовища

### Глобальні (усі зразки)
| Змінна | Опис | За замовчуванням |
|--------|------|------------------|
| `FOUNDRY_LOCAL_ALIAS` | Псевдонім моделі для використання | Залежить від зразка |
| `FOUNDRY_LOCAL_ENDPOINT` | Перевизначення кінцевої точки сервісу | Визначається автоматично |
| `SHOW_USAGE` | Показати використання токенів | `0` |
| `RETRY_ON_FAIL` | Увімкнути логіку повтору | `1` |
| `RETRY_BACKOFF` | Початкова затримка повтору | `1.0` |

### Специфічні для зразків
| Змінна | Використовується у | Опис |
|--------|--------------------|------|
| `EMBED_MODEL` | Сесія 02 | Назва моделі ембедингів |
| `RAG_QUESTION` | Сесія 02 | Тестове питання для RAG |
| `BENCH_MODELS` | Сесія 03 | Моделі для бенчмаркінгу (через кому) |
| `BENCH_ROUNDS` | Сесія 03 | Кількість раундів бенчмаркінгу |
| `BENCH_PROMPT` | Сесія 03 | Тестовий запит для бенчмаркінгу |
| `BENCH_STREAM` | Сесія 03 | Вимірювання затримки першого токена |
| `SLM_ALIAS` | Сесія 04 | Мала мовна модель |
| `LLM_ALIAS` | Сесія 04 | Велика мовна модель |
| `COMPARE_PROMPT` | Сесія 04 | Тестовий запит для порівняння |
| `AGENT_MODEL_PRIMARY` | Сесія 05 | Основна модель агента |
| `AGENT_MODEL_EDITOR` | Сесія 05 | Модель агента-редактора |
| `AGENT_QUESTION` | Сесія 05 | Тестове питання для агентів |
| `PIPELINE_TASK` | Сесія 06 | Завдання для конвеєра |

---

## Зміни, що порушують сумісність

**Відсутні** - Усі зміни є зворотно сумісними.

Існуючі скрипти продовжать працювати. Нові функції включають:
- Додаткові змінні середовища
- Покращені повідомлення про помилки (не порушують функціональність)
- Додаткове логування (можна вимкнути)
- Кращі підказки типів (без впливу на виконання)

---

## Реалізовані найкращі практики

### 1. Завжди використовуйте Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Коректний шаблон обробки помилок
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Інформативне логування
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Підказки типів
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Комплексні docstrings
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

### 6. Підтримка змінних середовища
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Акуратна деградація
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

## Поширені проблеми та рішення

### Проблема: Помилки імпорту
**Рішення:** Встановіть відсутні залежності
```bash
pip install sentence-transformers ragas datasets numpy
```

### Проблема: Помилки з'єднання
**Рішення:** Переконайтеся, що Foundry Local запущений
```bash
foundry service status
foundry model run phi-4-mini
```

### Проблема: Модель не знайдена
**Рішення:** Перевірте доступні моделі
```bash
foundry model ls
foundry model download <alias>
```

### Проблема: Повільна продуктивність
**Рішення:** Використовуйте менші моделі або налаштуйте параметри
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Наступні кроки

### 1. Тестуйте всі зразки
Пройдіть контрольний список тестування, щоб переконатися, що всі зразки працюють коректно.

### 2. Оновіть документацію
- Оновіть файли markdown для сесій новими прикладами
- Додайте розділ усунення несправностей до основного README
- Створіть короткий довідник

### 3. Створіть інтеграційні тести
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Додайте бенчмарки продуктивності
Відстежуйте покращення продуктивності завдяки вдосконаленій обробці помилок.

### 5. Зворотний зв'язок від користувачів
Збирайте відгуки учасників воркшопу щодо:
- Чіткості повідомлень про помилки
- Повноти документації
- Зручності використання

---

## Ресурси

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Короткий довідник**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Примітки щодо міграції**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Основний репозиторій**: https://github.com/microsoft/Foundry-Local

---

## Обслуговування

### Додавання нових зразків
Дотримуйтесь цих шаблонів при створенні нових зразків:

1. Використовуйте `workshop_utils` для управління клієнтами
2. Додайте комплексну обробку помилок
3. Включіть підтримку змінних середовища
4. Додайте підказки типів та docstrings
5. Забезпечте інформативне логування
6. Включіть приклади використання у docstrings
7. Додайте посилання на документацію SDK

### Перевірка оновлень
При перевірці оновлень зразків перевірте:
- [ ] Обробку помилок для всіх операцій вводу/виводу
- [ ] Підказки типів для публічних функцій
- [ ] Комплексні docstrings
- [ ] Документацію змінних середовища
- [ ] Інформативний зворотний зв'язок для користувача
- [ ] Посилання на SDK
- [ ] Узгоджений стиль коду

---

**Резюме**: Усі зразки Python для воркшопу тепер відповідають найкращим практикам Foundry Local SDK з покращеною обробкою помилок, комплексною документацією та вдосконаленим досвідом користувача. Змін, що порушують сумісність, немає - вся існуюча функціональність збережена та покращена.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.