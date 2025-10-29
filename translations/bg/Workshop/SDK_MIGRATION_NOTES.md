<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:18:16+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "bg"
}
-->
# Бележки за миграция на Foundry Local SDK

## Общ преглед

Всички Python файлове в папката Workshop са актуализирани, за да следват най-новите модели от официалния [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Обобщение на промените

### Основна инфраструктура (`workshop_utils.py`)

#### Подобрени функции:
- **Поддръжка за замяна на крайни точки**: Добавена е поддръжка за променливата на средата `FOUNDRY_LOCAL_ENDPOINT`
- **Подобрено управление на грешки**: По-добро обработване на изключения с подробни съобщения за грешки
- **Подобрено кеширане**: Ключовете за кеш вече включват крайна точка за сценарии с множество крайни точки
- **Експоненциално изчакване**: Логиката за повторение вече използва експоненциално изчакване за по-добра надеждност
- **Анотации на типове**: Добавени са подробни подсказки за типове за по-добра поддръжка в IDE

#### Нови възможности:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Примерни приложения

#### Сесия 01: Начално зареждане на чат (`chat_bootstrap.py`)
- Актуализиран е моделът по подразбиране от `phi-3.5-mini` на `phi-4-mini`
- Добавена е поддръжка за замяна на крайни точки
- Подобрена документация с препратки към SDK

#### Сесия 02: RAG Pipeline (`rag_pipeline.py`)
- Актуализиран за използване на `phi-4-mini` като модел по подразбиране
- Добавена е поддръжка за замяна на крайни точки
- Подобрена документация с подробности за променливите на средата

#### Сесия 02: Оценка на RAG (`rag_eval_ragas.py`)
- Актуализирани модели по подразбиране
- Добавена конфигурация на крайни точки
- Подобрено управление на грешки

#### Сесия 03: Бенчмаркинг (`benchmark_oss_models.py`)
- Актуализиран списък с модели по подразбиране, включващ `phi-4-mini`
- Добавена подробна документация за променливите на средата
- Подобрена документация за функциите
- Добавена поддръжка за замяна на крайни точки навсякъде

#### Сесия 04: Сравнение на модели (`model_compare.py`)
- Актуализиран модел по подразбиране от `gpt-oss-20b` на `qwen2.5-7b`
- Добавена конфигурация на крайни точки
- Подобрена документация

#### Сесия 05: Оркестрация на множество агенти (`agents_orchestrator.py`)
- Добавени подсказки за типове (променено `str | None` на `Optional[str]`)
- Подобрена документация за класа Agent
- Добавена поддръжка за замяна на крайни точки
- Подобрен модел за инициализация

#### Сесия 06: Рутер за модели (`models_router.py`)
- Добавена конфигурация на крайни точки
- Подобрена документация за откриване на намерения
- Подобрена документация за логиката на маршрутизация

#### Сесия 06: Pipeline (`models_pipeline.py`)
- Добавена подробна документация за функциите
- Подобрена документация стъпка по стъпка
- Подобрено управление на грешки

### Скриптове

#### Експорт на бенчмаркинг (`export_benchmark_markdown.py`)
- Добавена поддръжка за замяна на крайни точки
- Актуализирани модели по подразбиране
- Подобрена документация за функциите
- Подобрено управление на грешки

#### CLI Linter (`lint_markdown_cli.py`)
- Добавени препратки към SDK
- Подобрена документация за употреба

### Тестове

#### Smoke Tests (`smoke.py`)
- Добавена поддръжка за замяна на крайни точки
- Подобрена документация
- Подобрена документация за тестовите случаи
- По-добро докладване на грешки

## Променливи на средата

Всички примери вече поддържат следните променливи на средата:

### Основна конфигурация
- `FOUNDRY_LOCAL_ALIAS` - Алиас на модела за използване (по подразбиране варира според примера)
- `FOUNDRY_LOCAL_ENDPOINT` - Замяна на крайна точка на услугата (по избор)
- `SHOW_USAGE` - Показване на статистика за използване на токени (по подразбиране: "0")
- `RETRY_ON_FAIL` - Активиране на логика за повторение (по подразбиране: "1")
- `RETRY_BACKOFF` - Начално забавяне при повторение в секунди (по подразбиране: "1.0")

### Специфични за примери
- `EMBED_MODEL` - Модел за вграждане за примери с RAG
- `BENCH_MODELS` - Модели, разделени със запетаи, за бенчмаркинг
- `BENCH_ROUNDS` - Брой кръгове за бенчмаркинг
- `BENCH_PROMPT` - Тестов промпт за бенчмаркинг
- `BENCH_STREAM` - Измерване на латентността на първия токен
- `RAG_QUESTION` - Тестов въпрос за примери с RAG
- `AGENT_MODEL_PRIMARY` - Основен модел за агент
- `AGENT_MODEL_EDITOR` - Модел за редактор на агент
- `SLM_ALIAS` - Алиас за малък езиков модел
- `LLM_ALIAS` - Алиас за голям езиков модел

## Най-добри практики за SDK

### 1. Правилна инициализация на клиент
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

### 2. Извличане на информация за модела
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Управление на грешки
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Логика за повторение с експоненциално изчакване
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

### 5. Поддръжка за стрийминг
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

## Ръководство за миграция на персонализирани примери

Ако създавате нови примери или актуализирате съществуващи:

1. **Използвайте помощниците от `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Поддържайте замяна на крайни точки**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Добавете подробна документация**:
   - Променливи на средата в docstring
   - Препратка към SDK
   - Примери за употреба

4. **Използвайте подсказки за типове**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Реализирайте правилно управление на грешки**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Тестване

Всички примери могат да бъдат тествани с:

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

## Препратки към документацията на SDK

- **Основно хранилище**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Документация за API**: Проверете хранилището на SDK за най-новата документация за API

## Промени, които нарушават съвместимостта

### Не се очакват
Всички промени са съвместими с предишни версии. Актуализациите основно:
- Добавят нови опционални функции (замяна на крайни точки)
- Подобряват управлението на грешки
- Подобряват документацията
- Актуализират имената на моделите по подразбиране според текущите препоръки

### Опционални подобрения
Може да искате да актуализирате кода си, за да използвате:
- `FOUNDRY_LOCAL_ENDPOINT` за явен контрол на крайната точка
- `SHOW_USAGE=1` за видимост на използването на токени
- Актуализирани модели по подразбиране (`phi-4-mini` вместо `phi-3.5-mini`)

## Чести проблеми и решения

### Проблем: "Инициализацията на клиента не успя"
**Решение**: Уверете се, че услугата Foundry Local работи:
```bash
foundry service start
foundry model run phi-4-mini
```

### Проблем: "Моделът не е намерен"
**Решение**: Проверете наличните модели:
```bash
foundry model list
```

### Проблем: Грешки при свързване с крайна точка
**Решение**: Проверете крайната точка:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Следващи стъпки

1. **Актуализирайте примерите от Module08**: Приложете подобни модели към Module08/samples
2. **Добавете интеграционни тестове**: Създайте подробен тестов пакет
3. **Бенчмаркинг на производителността**: Сравнете производителността преди/след актуализацията
4. **Актуализации на документацията**: Актуализирайте основния README с новите модели

## Насоки за принос

При добавяне на нови примери:
1. Използвайте `workshop_utils.py` за последователност
2. Следвайте модела в съществуващите примери
3. Добавете подробни docstrings
4. Включете препратки към SDK
5. Поддържайте замяна на крайни точки
6. Добавете подходящи подсказки за типове
7. Включете примери за употреба в docstring

## Съвместимост на версиите

Тези актуализации са съвместими с:
- `foundry-local-sdk` (най-новата версия)
- `openai>=1.30.0`
- Python 3.8+

---

**Последна актуализация**: 2025-01-08  
**Поддръжка**: EdgeAI Workshop Team  
**Версия на SDK**: Foundry Local SDK (най-новата 0.7.117+67073234e7)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.