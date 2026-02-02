# Foundry Local как пример использования API

Этот пример демонстрирует, как использовать Microsoft Foundry Local в качестве REST API сервиса без зависимости от OpenAI SDK. Он показывает шаблоны прямой HTTP-интеграции для максимального контроля и настройки.

## Обзор

На основе официальных шаблонов Microsoft Foundry Local этот пример предоставляет:
- Прямую интеграцию REST API с FoundryLocalManager
- Пользовательскую реализацию HTTP-клиента
- Управление моделями и мониторинг их состояния
- Обработку потоковых и непотоковых ответов
- Готовую к производству обработку ошибок и логику повторных попыток

## Предварительные требования

1. **Установка Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Зависимости Python**
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

## Основные возможности

### 1. **Прямая HTTP-интеграция**
- Чистые REST API вызовы без зависимости от SDK
- Пользовательская аутентификация и заголовки
- Полный контроль над обработкой запросов и ответов

### 2. **Управление моделями**
- Динамическая загрузка и выгрузка моделей
- Мониторинг состояния и проверка статуса
- Сбор метрик производительности

### 3. **Шаблоны для производства**
- Механизмы повторных попыток с экспоненциальной задержкой
- Circuit breaker для устойчивости к сбоям
- Полное логирование и мониторинг

### 4. **Гибкая обработка ответов**
- Потоковые ответы для приложений в реальном времени
- Пакетная обработка для сценариев с высокой пропускной способностью
- Пользовательский парсинг и проверка ответов

## Примеры использования

### Базовая интеграция API
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

### Потоковая интеграция
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Мониторинг состояния
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Структура файлов

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

## Интеграция Microsoft Foundry Local

Этот пример следует официальным шаблонам Microsoft:

1. **Интеграция SDK**: Использует `FoundryLocalManager` для управления сервисом
2. **REST Endpoints**: Прямые вызовы `/v1/chat/completions` и других конечных точек
3. **Аутентификация**: Корректная обработка API-ключей для локальных сервисов
4. **Управление моделями**: Список каталогов, загрузка и шаблоны загрузки
5. **Обработка ошибок**: Рекомендованные Microsoft коды ошибок и ответы

## Начало работы

1. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

2. **Запустите базовый пример**
   ```bash
   python examples/basic_usage.py
   ```

3. **Попробуйте потоковую обработку**
   ```bash
   python examples/streaming.py
   ```

4. **Настройка для производства**
   ```bash
   python examples/production.py
   ```

## Конфигурация

Переменные окружения для настройки:
- `FOUNDRY_MODEL`: Модель по умолчанию (по умолчанию: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Тайм-аут запроса в секундах (по умолчанию: 30)
- `FOUNDRY_RETRIES`: Количество попыток повторного запроса (по умолчанию: 3)
- `FOUNDRY_LOG_LEVEL`: Уровень логирования (по умолчанию: "INFO")

## Лучшие практики

1. **Управление соединениями**: Повторное использование HTTP-соединений для повышения производительности
2. **Обработка ошибок**: Реализуйте корректную логику повторных попыток с экспоненциальной задержкой
3. **Мониторинг ресурсов**: Отслеживайте использование памяти модели и производительность
4. **Безопасность**: Используйте корректную аутентификацию даже для локальных сервисов
5. **Тестирование**: Включите как модульные, так и интеграционные тесты

## Устранение неполадок

### Распространенные проблемы

**Сервис не запущен**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Проблемы с загрузкой модели**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Ошибки соединения**
- Убедитесь, что Foundry Local запущен на правильном порту
- Проверьте настройки брандмауэра
- Убедитесь в корректности заголовков аутентификации

## Оптимизация производительности

1. **Пул соединений**: Используйте объекты сессии для множества запросов
2. **Асинхронные операции**: Используйте asyncio для конкурентных запросов
3. **Кэширование**: Кэшируйте ответы моделей, где это уместно
4. **Мониторинг**: Отслеживайте время ответа и корректируйте тайм-ауты

## Результаты обучения

После завершения этого примера вы поймете:
- Прямую интеграцию REST API с Foundry Local
- Шаблоны реализации пользовательского HTTP-клиента
- Готовую к производству обработку ошибок и мониторинг
- Архитектуру сервиса Microsoft Foundry Local
- Техники оптимизации производительности для локальных AI-сервисов

## Следующие шаги

- Изучите пример 08: Приложение для чата в Windows 11
- Попробуйте пример 09: Оркестрация нескольких агентов
- Узнайте о примере 10: Интеграция Foundry Local как инструментов

---

