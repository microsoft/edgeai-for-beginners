<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:45:01+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "uk"
}
-->
# Примітки щодо міграції локального SDK Foundry

## Огляд

Усі файли Python у папці Workshop були оновлені відповідно до останніх шаблонів офіційного [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Резюме змін

### Основна інфраструктура (`workshop_utils.py`)

#### Покращені функції:
- **Підтримка перевизначення кінцевої точки**: Додано підтримку змінної середовища `FOUNDRY_LOCAL_ENDPOINT`
- **Покращене оброблення помилок**: Покращене оброблення виключень із детальними повідомленнями про помилки
- **Покращене кешування**: Ключі кешу тепер включають кінцеву точку для сценаріїв з кількома кінцевими точками
- **Експоненціальне збільшення часу очікування**: Логіка повторних спроб тепер використовує експоненціальне збільшення часу очікування для підвищення надійності
- **Анотації типів**: Додано детальні підказки типів для кращої підтримки IDE

#### Нові можливості:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Зразки застосунків

#### Сесія 01: Ініціалізація чату (`chat_bootstrap.py`)
- Оновлено модель за замовчуванням з `phi-3.5-mini` на `phi-4-mini`
- Додано підтримку перевизначення кінцевої точки
- Покращено документацію з посиланнями на SDK

#### Сесія 02: Конвеєр RAG (`rag_pipeline.py`)
- Оновлено для використання `phi-4-mini` за замовчуванням
- Додано підтримку перевизначення кінцевої точки
- Покращено документацію з деталями змінних середовища

#### Сесія 02: Оцінка RAG (`rag_eval_ragas.py`)
- Оновлено моделі за замовчуванням
- Додано конфігурацію кінцевої точки
- Покращене оброблення помилок

#### Сесія 03: Бенчмаркінг (`benchmark_oss_models.py`)
- Оновлено список моделей за замовчуванням, включаючи `phi-4-mini`
- Додано детальну документацію змінних середовища
- Покращено документацію функцій
- Додано підтримку перевизначення кінцевої точки

#### Сесія 04: Порівняння моделей (`model_compare.py`)
- Оновлено модель LLM за замовчуванням з `gpt-oss-20b` на `qwen2.5-7b`
- Додано конфігурацію кінцевої точки
- Покращено документацію

#### Сесія 05: Оркестрація мультиагентів (`agents_orchestrator.py`)
- Додано підказки типів (змінено `str | None` на `Optional[str]`)
- Покращено документацію класу Agent
- Додано підтримку перевизначення кінцевої точки
- Покращено шаблон ініціалізації

#### Сесія 06: Маршрутизатор моделей (`models_router.py`)
- Додано конфігурацію кінцевої точки
- Покращено документацію виявлення намірів
- Покращено документацію логіки маршрутизації

#### Сесія 06: Конвеєр (`models_pipeline.py`)
- Додано детальну документацію функцій
- Покращено покрокову документацію
- Покращене оброблення помилок

### Скрипти

#### Експорт бенчмарків (`export_benchmark_markdown.py`)
- Додано підтримку перевизначення кінцевої точки
- Оновлено моделі за замовчуванням
- Покращено документацію функцій
- Покращене оброблення помилок

#### CLI Linter (`lint_markdown_cli.py`)
- Додано посилання на SDK
- Покращено документацію використання

### Тести

#### Тести на працездатність (`smoke.py`)
- Додано підтримку перевизначення кінцевої точки
- Покращено документацію
- Покращено документацію тестових випадків
- Покращене звітування про помилки

## Змінні середовища

Усі зразки тепер підтримують ці змінні середовища:

### Основна конфігурація
- `FOUNDRY_LOCAL_ALIAS` - Псевдонім моделі для використання (за замовчуванням залежить від зразка)
- `FOUNDRY_LOCAL_ENDPOINT` - Перевизначення кінцевої точки сервісу (опціонально)
- `SHOW_USAGE` - Показати статистику використання токенів (за замовчуванням: "0")
- `RETRY_ON_FAIL` - Увімкнути логіку повторних спроб (за замовчуванням: "1")
- `RETRY_BACKOFF` - Початкова затримка повторної спроби в секундах (за замовчуванням: "1.0")

### Специфічні для зразків
- `EMBED_MODEL` - Модель для вбудовування для зразків RAG
- `BENCH_MODELS` - Моделі для бенчмаркінгу, розділені комами
- `BENCH_ROUNDS` - Кількість раундів бенчмаркінгу
- `BENCH_PROMPT` - Тестовий запит для бенчмарків
- `BENCH_STREAM` - Вимірювання затримки першого токена
- `RAG_QUESTION` - Тестове питання для зразків RAG
- `AGENT_MODEL_PRIMARY` - Основна модель агента
- `AGENT_MODEL_EDITOR` - Модель агента-редактора
- `SLM_ALIAS` - Псевдонім малої мовної моделі
- `LLM_ALIAS` - Псевдонім великої мовної моделі

## Найкращі практики використання SDK

### 1. Правильна ініціалізація клієнта
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

### 2. Отримання інформації про модель
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Оброблення помилок
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Логіка повторних спроб з експоненціальним збільшенням часу очікування
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

### 5. Підтримка потокової передачі
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

## Посібник з міграції для користувацьких зразків

Якщо ви створюєте нові зразки або оновлюєте існуючі:

1. **Використовуйте допоміжні функції з `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Підтримуйте перевизначення кінцевої точки**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Додайте детальну документацію**:
   - Змінні середовища в docstring
   - Посилання на SDK
   - Приклади використання

4. **Використовуйте підказки типів**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Реалізуйте правильне оброблення помилок**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Тестування

Усі зразки можна протестувати за допомогою:

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

## Посилання на документацію SDK

- **Основний репозиторій**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Документація API**: Перевірте репозиторій SDK для останньої документації API

## Зміни, що порушують сумісність

### Не очікується
Усі зміни є зворотно сумісними. Оновлення переважно:
- Додають нові опціональні функції (перевизначення кінцевої точки)
- Покращують оброблення помилок
- Покращують документацію
- Оновлюють назви моделей за замовчуванням до актуальних рекомендацій

### Опціональні покращення
Ви можете оновити свій код для використання:
- `FOUNDRY_LOCAL_ENDPOINT` для явного контролю кінцевої точки
- `SHOW_USAGE=1` для видимості використання токенів
- Оновлені моделі за замовчуванням (`phi-4-mini` замість `phi-3.5-mini`)

## Поширені проблеми та рішення

### Проблема: "Ініціалізація клієнта не вдалася"
**Рішення**: Переконайтеся, що сервіс Foundry Local запущений:
```bash
foundry service start
foundry model run phi-4-mini
```

### Проблема: "Модель не знайдена"
**Рішення**: Перевірте доступні моделі:
```bash
foundry model list
```

### Проблема: Помилки підключення до кінцевої точки
**Рішення**: Перевірте кінцеву точку:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Наступні кроки

1. **Оновіть зразки Module08**: Застосуйте подібні шаблони до Module08/samples
2. **Додайте інтеграційні тести**: Створіть комплексний набір тестів
3. **Бенчмаркінг продуктивності**: Порівняйте продуктивність до/після оновлення
4. **Оновлення документації**: Оновіть основний README з новими шаблонами

## Керівництво для внесення змін

При додаванні нових зразків:
1. Використовуйте `workshop_utils.py` для узгодженості
2. Дотримуйтесь шаблону існуючих зразків
3. Додайте детальні docstring
4. Включіть посилання на SDK
5. Підтримуйте перевизначення кінцевої точки
6. Додайте правильні підказки типів
7. Включіть приклади використання в docstring

## Сумісність версій

Ці оновлення сумісні з:
- `foundry-local-sdk` (остання версія)
- `openai>=1.30.0`
- Python 3.8+

---

**Останнє оновлення**: 2025-01-08  
**Відповідальний**: Команда EdgeAI Workshop  
**Версія SDK**: Foundry Local SDK (остання 0.7.117+67073234e7)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.