# Пример 02: Интеграция с OpenAI SDK

Демонстрирует продвинутую интеграцию с OpenAI Python SDK, поддерживающую как Microsoft Foundry Local, так и Azure OpenAI с потоковыми ответами и корректной обработкой ошибок.

## Обзор

Этот пример демонстрирует:
- Легкое переключение между Foundry Local и Azure OpenAI
- Потоковые завершения чатов для улучшения пользовательского опыта
- Правильное использование FoundryLocalManager SDK
- Надежные механизмы обработки ошибок и резервирования
- Шаблоны кода, готовые к использованию в продакшене

## Предварительные требования

- **Foundry Local**: Установлен и запущен (для локального инференса)
- **Python**: Версия 3.8 или выше с OpenAI SDK
- **Azure OpenAI**: Действительный endpoint и API-ключ (для облачного инференса)

## Установка

1. **Настройте окружение Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Установите зависимости:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Запустите Foundry Local (для локального режима):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Сценарии использования

### Foundry Local (по умолчанию)

**Вариант 1: Использование FoundryLocalManager (рекомендуется)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Вариант 2: Ручная настройка**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```

## Архитектура кода

### Паттерн фабрики клиента

Пример использует паттерн фабрики для создания подходящих клиентов:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```

### Потоковые ответы

Пример демонстрирует потоковую генерацию ответов в реальном времени:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Переменные окружения

### Конфигурация Foundry Local

| Переменная | Описание | По умолчанию | Обязательно |
|------------|----------|--------------|-------------|
| `MODEL` | Псевдоним модели для использования | `phi-4-mini` | Нет |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Нет |
| `API_KEY` | API-ключ (опционально для локального режима) | `""` | Нет |

### Конфигурация Azure OpenAI

| Переменная | Описание | По умолчанию | Обязательно |
|------------|----------|--------------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint ресурса Azure OpenAI | - | Да |
| `AZURE_OPENAI_API_KEY` | API-ключ Azure OpenAI | - | Да |
| `AZURE_OPENAI_API_VERSION` | Версия API | `2024-08-01-preview` | Нет |
| `MODEL` | Имя развертывания Azure | `your-deployment-name` | Да |

## Расширенные возможности

### Автоматическое обнаружение сервиса

Пример автоматически определяет подходящий сервис на основе переменных окружения:

1. **Режим Azure**: Если заданы `AZURE_OPENAI_ENDPOINT` и `AZURE_OPENAI_API_KEY`
2. **Режим Foundry SDK**: Если доступен SDK Foundry Local
3. **Ручной режим**: Резервный вариант с ручной настройкой

### Обработка ошибок

- Плавное переключение с SDK на ручную настройку
- Понятные сообщения об ошибках для устранения неполадок
- Корректная обработка исключений для сетевых проблем
- Проверка обязательных переменных окружения

## Производительность

### Сравнение локального и облачного режимов

**Преимущества Foundry Local:**
- ✅ Отсутствие затрат на API
- ✅ Конфиденциальность данных (данные не покидают устройство)
- ✅ Низкая задержка для поддерживаемых моделей
- ✅ Работает в оффлайн-режиме

**Преимущества Azure OpenAI:**
- ✅ Доступ к последним крупным моделям
- ✅ Высокая пропускная способность
- ✅ Отсутствие требований к локальным вычислительным ресурсам
- ✅ SLA корпоративного уровня

## Устранение неполадок

### Частые проблемы

1. **Предупреждение "Не удалось использовать Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Ошибки аутентификации Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Модель недоступна:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Проверка работоспособности

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Следующие шаги

- **Пример 03**: Обнаружение моделей и тестирование производительности
- **Пример 04**: Создание Chainlit RAG-приложения
- **Пример 05**: Оркестрация нескольких агентов
- **Пример 06**: Маршрутизация моделей как инструментов

## Ссылки

- [Документация Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Справочник Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Документация OpenAI Python SDK](https://github.com/openai/openai-python)
- [Руководство по потоковым завершениям](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

