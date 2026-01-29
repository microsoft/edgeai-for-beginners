# Foundry Local як приклад API

Цей приклад демонструє, як використовувати Microsoft Foundry Local як REST API сервіс без залежності від OpenAI SDK. Він показує прямі шаблони інтеграції HTTP для максимального контролю та налаштування.

## Огляд

На основі офіційних шаблонів Microsoft Foundry Local цей приклад надає:
- Пряму інтеграцію REST API з FoundryLocalManager
- Власну реалізацію HTTP клієнта
- Управління моделями та моніторинг стану
- Обробку потокових і непотокових відповідей
- Готову до використання в продакшені логіку обробки помилок і повторних спроб

## Попередні вимоги

1. **Встановлення Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-залежності**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Архітектура

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Основні функції

### 1. **Пряма інтеграція HTTP**
- Чисті виклики REST API без залежності від SDK
- Власна аутентифікація та заголовки
- Повний контроль над обробкою запитів/відповідей

### 2. **Управління моделями**
- Динамічне завантаження та розвантаження моделей
- Моніторинг стану та перевірка статусу
- Збір метрик продуктивності

### 3. **Шаблони для продакшену**
- Механізми повторних спроб із експоненціальним збільшенням інтервалу
- "Циркулярний вимикач" для стійкості до помилок
- Комплексне логування та моніторинг

### 4. **Гнучка обробка відповідей**
- Потокові відповіді для додатків у реальному часі
- Пакетна обробка для сценаріїв з високою пропускною здатністю
- Власний парсинг і перевірка відповідей

## Приклади використання

### Базова інтеграція API
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

### Потокова інтеграція
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Моніторинг стану
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Структура файлів

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

## Інтеграція Microsoft Foundry Local

Цей приклад слідує офіційним шаблонам Microsoft:

1. **Інтеграція SDK**: Використовує `FoundryLocalManager` для управління сервісом
2. **REST Endpoint-и**: Прямі виклики до `/v1/chat/completions` та інших endpoint-ів
3. **Аутентифікація**: Правильна обробка API ключів для локальних сервісів
4. **Управління моделями**: Списки каталогів, завантаження та шаблони завантаження
5. **Обробка помилок**: Рекомендовані Microsoft коди помилок і відповіді

## Початок роботи

1. **Встановіть залежності**
   ```bash
   pip install -r requirements.txt
   ```

2. **Запустіть базовий приклад**
   ```bash
   python examples/basic_usage.py
   ```

3. **Спробуйте потокову інтеграцію**
   ```bash
   python examples/streaming.py
   ```

4. **Налаштування для продакшену**
   ```bash
   python examples/production.py
   ```

## Конфігурація

Змінні середовища для налаштування:
- `FOUNDRY_MODEL`: Модель за замовчуванням (за замовчуванням: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Тайм-аут запиту в секундах (за замовчуванням: 30)
- `FOUNDRY_RETRIES`: Кількість спроб повтору (за замовчуванням: 3)
- `FOUNDRY_LOG_LEVEL`: Рівень логування (за замовчуванням: "INFO")

## Найкращі практики

1. **Управління з'єднаннями**: Повторне використання HTTP-з'єднань для кращої продуктивності
2. **Обробка помилок**: Реалізуйте правильну логіку повторних спроб із експоненціальним збільшенням інтервалу
3. **Моніторинг ресурсів**: Відстежуйте використання пам'яті моделі та продуктивність
4. **Безпека**: Використовуйте правильну аутентифікацію навіть для локальних сервісів
5. **Тестування**: Включіть як модульні, так і інтеграційні тести

## Вирішення проблем

### Поширені проблеми

**Сервіс не запущений**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Проблеми із завантаженням моделі**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Помилки з'єднання**
- Перевірте, чи Foundry Local запущений на правильному порту
- Перевірте налаштування брандмауера
- Переконайтеся, що заголовки аутентифікації правильні

## Оптимізація продуктивності

1. **Пулінг з'єднань**: Використовуйте об'єкти сесій для багаторазових запитів
2. **Асинхронні операції**: Використовуйте asyncio для одночасних запитів
3. **Кешування**: Кешуйте відповіді моделі там, де це доречно
4. **Моніторинг**: Відстежуйте час відповіді та налаштовуйте тайм-аути

## Результати навчання

Після завершення цього прикладу ви зрозумієте:
- Пряму інтеграцію REST API з Foundry Local
- Шаблони реалізації власного HTTP клієнта
- Логіку обробки помилок і моніторингу, готову до продакшену
- Архітектуру сервісу Microsoft Foundry Local
- Техніки оптимізації продуктивності для локальних AI сервісів

## Наступні кроки

- Досліджуйте приклад 08: Додаток для чату Windows 11
- Спробуйте приклад 09: Оркестрація мультиагентів
- Вивчіть приклад 10: Інтеграція Foundry Local як інструментів

---

