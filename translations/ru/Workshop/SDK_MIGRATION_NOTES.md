<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:17:22+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ru"
}
-->
# Заметки о миграции локального SDK Foundry

## Обзор

Все файлы Python в папке Workshop были обновлены в соответствии с последними шаблонами официального [локального Python SDK Foundry](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Сводка изменений

### Основная инфраструктура (`workshop_utils.py`)

#### Улучшенные функции:
- **Поддержка переопределения конечной точки**: Добавлена поддержка переменной окружения `FOUNDRY_LOCAL_ENDPOINT`
- **Улучшенная обработка ошибок**: Более качественная обработка исключений с подробными сообщениями об ошибках
- **Улучшенное кэширование**: Ключи кэша теперь включают конечную точку для сценариев с несколькими конечными точками
- **Экспоненциальное увеличение интервала повторных попыток**: Логика повторных попыток теперь использует экспоненциальное увеличение интервала для повышения надежности
- **Аннотации типов**: Добавлены подробные подсказки типов для улучшенной поддержки IDE

#### Новые возможности:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Пример приложений

#### Сессия 01: Инициализация чата (`chat_bootstrap.py`)
- Обновлена модель по умолчанию с `phi-3.5-mini` на `phi-4-mini`
- Добавлена поддержка переопределения конечной точки
- Улучшена документация с ссылками на SDK

#### Сессия 02: Конвейер RAG (`rag_pipeline.py`)
- Обновлено использование модели по умолчанию на `phi-4-mini`
- Добавлена поддержка переопределения конечной точки
- Улучшена документация с деталями о переменных окружения

#### Сессия 02: Оценка RAG (`rag_eval_ragas.py`)
- Обновлены модели по умолчанию
- Добавлена конфигурация конечной точки
- Улучшена обработка ошибок

#### Сессия 03: Бенчмаркинг (`benchmark_oss_models.py`)
- Обновлен список моделей по умолчанию, включая `phi-4-mini`
- Добавлена подробная документация о переменных окружения
- Улучшена документация функций
- Добавлена поддержка переопределения конечной точки

#### Сессия 04: Сравнение моделей (`model_compare.py`)
- Обновлена модель LLM по умолчанию с `gpt-oss-20b` на `qwen2.5-7b`
- Добавлена конфигурация конечной точки
- Улучшена документация

#### Сессия 05: Оркестрация мульти-агентов (`agents_orchestrator.py`)
- Добавлены подсказки типов (изменено `str | None` на `Optional[str]`)
- Улучшена документация класса Agent
- Добавлена поддержка переопределения конечной точки
- Улучшен шаблон инициализации

#### Сессия 06: Маршрутизатор моделей (`models_router.py`)
- Добавлена конфигурация конечной точки
- Улучшена документация по обнаружению намерений
- Улучшена документация логики маршрутизации

#### Сессия 06: Конвейер (`models_pipeline.py`)
- Добавлена подробная документация функций
- Улучшена пошаговая документация
- Улучшена обработка ошибок

### Скрипты

#### Экспорт бенчмарка (`export_benchmark_markdown.py`)
- Добавлена поддержка переопределения конечной точки
- Обновлены модели по умолчанию
- Улучшена документация функций
- Улучшена обработка ошибок

#### CLI Linter (`lint_markdown_cli.py`)
- Добавлены ссылки на SDK
- Улучшена документация по использованию

### Тесты

#### Smoke Tests (`smoke.py`)
- Добавлена поддержка переопределения конечной точки
- Улучшена документация
- Улучшена документация тестовых случаев
- Улучшена отчетность об ошибках

## Переменные окружения

Все примеры теперь поддерживают следующие переменные окружения:

### Основная конфигурация
- `FOUNDRY_LOCAL_ALIAS` - Алиас модели для использования (значение по умолчанию зависит от примера)
- `FOUNDRY_LOCAL_ENDPOINT` - Переопределение конечной точки сервиса (опционально)
- `SHOW_USAGE` - Показать статистику использования токенов (значение по умолчанию: "0")
- `RETRY_ON_FAIL` - Включить логику повторных попыток (значение по умолчанию: "1")
- `RETRY_BACKOFF` - Начальная задержка повторной попытки в секундах (значение по умолчанию: "1.0")

### Специфичные для примеров
- `EMBED_MODEL` - Модель для встраивания в примерах RAG
- `BENCH_MODELS` - Модели для бенчмаркинга, разделенные запятыми
- `BENCH_ROUNDS` - Количество раундов бенчмаркинга
- `BENCH_PROMPT` - Тестовый запрос для бенчмарков
- `BENCH_STREAM` - Измерение задержки первого токена
- `RAG_QUESTION` - Тестовый вопрос для примеров RAG
- `AGENT_MODEL_PRIMARY` - Основная модель агента
- `AGENT_MODEL_EDITOR` - Модель редактора агента
- `SLM_ALIAS` - Алиас небольшой языковой модели
- `LLM_ALIAS` - Алиас большой языковой модели

## Реализованные лучшие практики SDK

### 1. Правильная инициализация клиента
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Получение информации о модели
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Обработка ошибок
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Логика повторных попыток с экспоненциальным увеличением интервала
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Поддержка потоковой передачи
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Руководство по миграции для пользовательских примеров

Если вы создаете новые примеры или обновляете существующие:

1. **Используйте помощники из `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Поддерживайте переопределение конечной точки**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Добавляйте подробную документацию**:
   - Переменные окружения в docstring
   - Ссылки на SDK
   - Примеры использования

4. **Используйте подсказки типов**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Реализуйте правильную обработку ошибок**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Тестирование

Все примеры можно протестировать с помощью:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Ссылки на документацию SDK

- **Основное репозиторий**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Документация API**: Проверьте репозиторий SDK для получения последней документации API

## Изменения, нарушающие совместимость

### Не ожидается
Все изменения обратно совместимы. Обновления в основном:
- Добавляют новые опциональные функции (переопределение конечной точки)
- Улучшают обработку ошибок
- Улучшают документацию
- Обновляют названия моделей по умолчанию в соответствии с текущими рекомендациями

### Опциональные улучшения
Вы можете обновить свой код для использования:
- `FOUNDRY_LOCAL_ENDPOINT` для явного управления конечной точкой
- `SHOW_USAGE=1` для отображения использования токенов
- Обновленных моделей по умолчанию (`phi-4-mini` вместо `phi-3.5-mini`)

## Распространенные проблемы и решения

### Проблема: "Не удалось инициализировать клиента"
**Решение**: Убедитесь, что локальный сервис Foundry запущен:
```bash
foundry service start
foundry model run phi-4-mini
```

### Проблема: "Модель не найдена"
**Решение**: Проверьте доступные модели:
```bash
foundry model list
```

### Проблема: Ошибки подключения к конечной точке
**Решение**: Проверьте конечную точку:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Следующие шаги

1. **Обновите примеры Module08**: Примените аналогичные шаблоны к Module08/samples
2. **Добавьте интеграционные тесты**: Создайте комплексный набор тестов
3. **Бенчмаркинг производительности**: Сравните производительность до и после
4. **Обновления документации**: Обновите основной README с новыми шаблонами

## Руководство по внесению изменений

При добавлении новых примеров:
1. Используйте `workshop_utils.py` для согласованности
2. Следуйте шаблону существующих примеров
3. Добавляйте подробные docstring
4. Включайте ссылки на SDK
5. Поддерживайте переопределение конечной точки
6. Добавляйте подсказки типов
7. Включайте примеры использования в docstring

## Совместимость версий

Эти обновления совместимы с:
- `foundry-local-sdk` (последняя версия)
- `openai>=1.30.0`
- Python 3.8+

---

**Последнее обновление**: 08.01.2025  
**Ответственный**: Команда EdgeAI Workshop  
**Версия SDK**: Foundry Local SDK (последняя 0.7.117+67073234e7)

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.