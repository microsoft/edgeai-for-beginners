<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:17:04+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ru"
}
-->
# Примеры для мастер-класса - Обновление Foundry Local SDK

## Обзор

Все примеры на Python в каталоге `Workshop/samples` были обновлены в соответствии с лучшими практиками Foundry Local SDK, чтобы обеспечить единообразие в рамках мастер-класса.

**Дата**: 8 октября 2025  
**Объем**: 9 файлов на Python в рамках 6 сессий мастер-класса  
**Основной акцент**: Обработка ошибок, документация, шаблоны SDK, удобство для пользователя

---

## Обновленные файлы

### Сессия 01: Начало работы
- ✅ `chat_bootstrap.py` - Основные примеры чата и потоковой передачи

### Сессия 02: Решения RAG
- ✅ `rag_pipeline.py` - Реализация RAG с использованием эмбеддингов
- ✅ `rag_eval_ragas.py` - Оценка RAG с метриками RAGAS

### Сессия 03: Модели с открытым исходным кодом
- ✅ `benchmark_oss_models.py` - Бенчмаркинг нескольких моделей

### Сессия 04: Передовые модели
- ✅ `model_compare.py` - Сравнение SLM и LLM

### Сессия 05: Агенты на основе ИИ
- ✅ `agents_orchestrator.py` - Координация нескольких агентов

### Сессия 06: Модели как инструменты
- ✅ `models_router.py` - Маршрутизация моделей на основе намерений
- ✅ `models_pipeline.py` - Многошаговый маршрутизированный конвейер

### Вспомогательная инфраструктура
- ✅ `workshop_utils.py` - Уже соответствует лучшим практикам (изменения не требуются)

---

## Основные улучшения

### 1. Улучшенная обработка ошибок

**До:**
```python
manager, client, model_id = get_client(alias)
```

**После:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Преимущества:**
- Элегантная обработка ошибок с понятными сообщениями
- Подсказки для устранения неполадок
- Корректные коды выхода для скриптов

### 2. Улучшенное управление импортами

**До:**
```python
from sentence_transformers import SentenceTransformer
```

**После:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Преимущества:**
- Четкие инструкции при отсутствии зависимостей
- Предотвращение непонятных ошибок импорта
- Удобные инструкции по установке

### 3. Полная документация

**Добавлено ко всем примерам:**
- Документация переменных окружения в docstrings
- Ссылки на SDK
- Примеры использования
- Подробная документация функций/параметров
- Подсказки типов для улучшенной поддержки IDE

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

### 4. Улучшенная обратная связь с пользователем

**Добавлено информативное логирование:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Индикаторы прогресса:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Структурированный вывод:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Надежный бенчмаркинг

**Улучшения в сессии 03:**
- Обработка ошибок для каждой модели (продолжение работы при сбое)
- Детальная отчетность о прогрессе
- Корректное выполнение прогревочных раундов
- Поддержка измерения задержки первого токена
- Четкое разделение этапов

### 6. Единообразные подсказки типов

**Добавлено повсеместно:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Преимущества:**
- Улучшенная автозаполняемость в IDE
- Раннее обнаружение ошибок
- Самодокументируемый код

### 7. Улучшенный маршрутизатор моделей

**Улучшения в сессии 06:**
- Полная документация по обнаружению намерений
- Объяснение алгоритма выбора модели
- Детализированные журналы маршрутизации
- Форматирование тестового вывода
- Восстановление после ошибок при пакетном тестировании

### 8. Оркестрация нескольких агентов

**Улучшения в сессии 05:**
- Отчетность о прогрессе на каждом этапе
- Обработка ошибок для каждого агента
- Четкая структура конвейера
- Улучшенная документация по управлению памятью

---

## Контрольный список тестирования

### Предварительные условия
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Тестирование каждого примера

#### Сессия 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Сессия 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Сессия 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Сессия 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Сессия 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Сессия 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Справочник по переменным окружения

### Глобальные (для всех примеров)
| Переменная | Описание | Значение по умолчанию |
|------------|----------|-----------------------|
| `FOUNDRY_LOCAL_ALIAS` | Псевдоним модели для использования | Зависит от примера |
| `FOUNDRY_LOCAL_ENDPOINT` | Переопределение конечной точки сервиса | Определяется автоматически |
| `SHOW_USAGE` | Показать использование токенов | `0` |
| `RETRY_ON_FAIL` | Включить логику повторных попыток | `1` |
| `RETRY_BACKOFF` | Начальная задержка повторной попытки | `1.0` |

### Специфичные для примеров
| Переменная | Используется в | Описание |
|------------|---------------|----------|
| `EMBED_MODEL` | Сессия 02 | Название модели эмбеддинга |
| `RAG_QUESTION` | Сессия 02 | Тестовый вопрос для RAG |
| `BENCH_MODELS` | Сессия 03 | Модели для бенчмаркинга (через запятую) |
| `BENCH_ROUNDS` | Сессия 03 | Количество раундов бенчмаркинга |
| `BENCH_PROMPT` | Сессия 03 | Тестовый запрос для бенчмаркинга |
| `BENCH_STREAM` | Сессия 03 | Измерение задержки первого токена |
| `SLM_ALIAS` | Сессия 04 | Маленькая языковая модель |
| `LLM_ALIAS` | Сессия 04 | Большая языковая модель |
| `COMPARE_PROMPT` | Сессия 04 | Тестовый запрос для сравнения |
| `AGENT_MODEL_PRIMARY` | Сессия 05 | Основная модель агента |
| `AGENT_MODEL_EDITOR` | Сессия 05 | Модель агента-редактора |
| `AGENT_QUESTION` | Сессия 05 | Тестовый вопрос для агентов |
| `PIPELINE_TASK` | Сессия 06 | Задача для конвейера |

---

## Изменения, нарушающие совместимость

**Отсутствуют** - Все изменения совместимы с предыдущими версиями.

Существующие скрипты продолжат работать. Новые функции включают:
- Дополнительные переменные окружения
- Улучшенные сообщения об ошибках (не нарушают функциональность)
- Дополнительное логирование (можно отключить)
- Улучшенные подсказки типов (не влияют на выполнение)

---

## Реализованные лучшие практики

### 1. Всегда используйте Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Шаблон корректной обработки ошибок
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Информативное логирование
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Подсказки типов
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Полные docstrings
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

### 6. Поддержка переменных окружения
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Плавная деградация
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

## Распространенные проблемы и их решения

### Проблема: Ошибки импорта
**Решение:** Установите отсутствующие зависимости
```bash
pip install sentence-transformers ragas datasets numpy
```

### Проблема: Ошибки подключения
**Решение:** Убедитесь, что Foundry Local запущен
```bash
foundry service status
foundry model run phi-4-mini
```

### Проблема: Модель не найдена
**Решение:** Проверьте доступные модели
```bash
foundry model ls
foundry model download <alias>
```

### Проблема: Низкая производительность
**Решение:** Используйте меньшие модели или настройте параметры
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Следующие шаги

### 1. Тестирование всех примеров
Пройдите контрольный список тестирования выше, чтобы убедиться, что все примеры работают корректно.

### 2. Обновление документации
- Обновите файлы сессий с новыми примерами
- Добавьте раздел устранения неполадок в основной README
- Создайте краткий справочник

### 3. Создание интеграционных тестов
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Добавление бенчмарков производительности
Отслеживайте улучшения производительности благодаря улучшенной обработке ошибок.

### 5. Обратная связь от пользователей
Соберите отзывы участников мастер-класса о:
- Понятности сообщений об ошибках
- Полноте документации
- Удобстве использования

---

## Ресурсы

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Краткий справочник**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Заметки по миграции**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Основной репозиторий**: https://github.com/microsoft/Foundry-Local

---

## Обслуживание

### Добавление новых примеров
Следуйте этим шаблонам при создании новых примеров:

1. Используйте `workshop_utils` для управления клиентом
2. Добавьте полную обработку ошибок
3. Включите поддержку переменных окружения
4. Добавьте подсказки типов и docstrings
5. Обеспечьте информативное логирование
6. Включите примеры использования в docstrings
7. Ссылки на документацию SDK

### Проверка обновлений
При проверке обновлений примеров убедитесь, что:
- [ ] Обработка ошибок для всех операций ввода/вывода
- [ ] Подсказки типов для публичных функций
- [ ] Полные docstrings
- [ ] Документация переменных окружения
- [ ] Информативная обратная связь с пользователем
- [ ] Ссылки на документацию SDK
- [ ] Единообразный стиль кода

---

**Итог**: Все примеры на Python для мастер-класса теперь соответствуют лучшим практикам Foundry Local SDK с улучшенной обработкой ошибок, полной документацией и улучшенным пользовательским интерфейсом. Изменения не нарушают совместимость - вся существующая функциональность сохранена и улучшена.

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.