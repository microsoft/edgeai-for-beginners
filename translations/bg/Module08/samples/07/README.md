# Пример за Foundry Local като API

Този пример демонстрира как да използвате Microsoft Foundry Local като REST API услуга, без да разчитате на OpenAI SDK. Показва директни HTTP интеграционни модели за максимален контрол и персонализация.

## Преглед

Въз основа на официалните модели на Microsoft Foundry Local, този пример предоставя:
- Директна REST API интеграция с FoundryLocalManager
- Персонализирана имплементация на HTTP клиент
- Управление на модели и мониторинг на състоянието
- Обработка на стрийминг и нестийминг отговори
- Готова за производство логика за обработка на грешки и повторения

## Предпоставки

1. **Инсталация на Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python зависимости**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Архитектура

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Основни функции

### 1. **Директна HTTP интеграция**
- Чисти REST API заявки без зависимости от SDK
- Персонализирана автентикация и заглавия
- Пълен контрол върху обработката на заявки/отговори

### 2. **Управление на модели**
- Динамично зареждане и разтоварване на модели
- Мониторинг на състоянието и проверки на статуса
- Събиране на метрики за производителност

### 3. **Производствени модели**
- Механизми за повторение с експоненциално забавяне
- Circuit breaker за устойчивост при грешки
- Изчерпателно логване и мониторинг

### 4. **Гъвкава обработка на отговори**
- Стрийминг отговори за приложения в реално време
- Партидна обработка за сценарии с висока пропускателност
- Персонализирано парсване и валидиране на отговори

## Примери за употреба

### Основна API интеграция
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Стрийминг интеграция
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Мониторинг на състоянието
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Структура на файловете

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Интеграция с Microsoft Foundry Local

Този пример следва официалните модели на Microsoft:

1. **SDK интеграция**: Използва `FoundryLocalManager` за управление на услугите
2. **REST крайни точки**: Директни заявки към `/v1/chat/completions` и други крайни точки
3. **Автентикация**: Правилно управление на API ключове за локални услуги
4. **Управление на модели**: Списък на каталога, изтегляне и зареждане на модели
5. **Обработка на грешки**: Препоръчани от Microsoft кодове за грешки и отговори

## Първи стъпки

1. **Инсталирайте зависимости**
   ```bash
   pip install -r requirements.txt
   ```

2. **Стартирайте основния пример**
   ```bash
   python examples/basic_usage.py
   ```

3. **Опитайте стрийминг**
   ```bash
   python examples/streaming.py
   ```

4. **Настройка за производство**
   ```bash
   python examples/production.py
   ```

## Конфигурация

Променливи на средата за персонализация:
- `FOUNDRY_MODEL`: Модел по подразбиране (по подразбиране: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Таймаут за заявки в секунди (по подразбиране: 30)
- `FOUNDRY_RETRIES`: Брой опити за повторение (по подразбиране: 3)
- `FOUNDRY_LOG_LEVEL`: Ниво на логване (по подразбиране: "INFO")

## Най-добри практики

1. **Управление на връзките**: Повторно използване на HTTP връзки за по-добра производителност
2. **Обработка на грешки**: Имплементирайте правилна логика за повторение с експоненциално забавяне
3. **Мониторинг на ресурсите**: Проследявайте използването на паметта и производителността на модела
4. **Сигурност**: Използвайте правилна автентикация, дори за локални услуги
5. **Тестване**: Включете както модулни, така и интеграционни тестове

## Отстраняване на проблеми

### Чести проблеми

**Услугата не работи**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Проблеми със зареждането на модела**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Грешки при връзката**
- Проверете дали Foundry Local работи на правилния порт
- Проверете настройките на защитната стена
- Уверете се, че заглавията за автентикация са правилни

## Оптимизация на производителността

1. **Пул на връзки**: Използвайте обекти на сесия за множество заявки
2. **Асинхронни операции**: Използвайте asyncio за конкурентни заявки
3. **Кеширане**: Кеширайте отговорите на модела, когато е подходящо
4. **Мониторинг**: Проследявайте времето за отговор и настройвайте таймаутите

## Резултати от обучението

След завършване на този пример ще разберете:
- Директна REST API интеграция с Foundry Local
- Модели за имплементация на персонализиран HTTP клиент
- Логика за обработка на грешки и мониторинг, готова за производство
- Архитектурата на услугите Microsoft Foundry Local
- Техники за оптимизация на производителността за локални AI услуги

## Следващи стъпки

- Разгледайте Пример 08: Приложение за чат в Windows 11
- Опитайте Пример 09: Оркестрация на много агенти
- Научете Пример 10: Foundry Local като интеграция на инструменти

---

