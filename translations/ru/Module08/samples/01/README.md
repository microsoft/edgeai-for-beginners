# Пример 01: Быстрый чат через OpenAI SDK

Простой пример чата, демонстрирующий использование OpenAI SDK с Microsoft Foundry Local для локального AI-анализа.

## Обзор

Этот пример показывает, как:
- Использовать OpenAI Python SDK с Foundry Local
- Работать с конфигурациями Azure OpenAI и локального Foundry
- Реализовать корректную обработку ошибок и стратегии резервирования
- Использовать FoundryLocalManager для управления сервисами

## Предварительные требования

- **Foundry Local**: Установлен и доступен в PATH
- **Python**: версии 3.8 или выше
- **Модель**: Загруженная модель в Foundry Local (например, `phi-4-mini`)

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

3. **Запустите сервис Foundry Local и загрузите модель:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Использование

### Foundry Local (по умолчанию)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Особенности кода

### Интеграция FoundryLocalManager

Пример использует официальный SDK Foundry Local для корректного управления сервисами:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Обработка ошибок

Надежная обработка ошибок с резервированием на ручную конфигурацию:
- Автоматическое обнаружение сервисов
- Плавная деградация, если SDK недоступен
- Понятные сообщения об ошибках для устранения неполадок

## Переменные окружения

| Переменная | Описание | Значение по умолчанию | Обязательно |
|------------|----------|-----------------------|-------------|
| `MODEL` | Псевдоним или название модели | `phi-4-mini` | Нет |
| `BASE_URL` | Базовый URL Foundry Local | `http://localhost:8000` | Нет |
| `API_KEY` | API-ключ (обычно не требуется для локального использования) | `""` | Нет |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Для Azure |
| `AZURE_OPENAI_API_KEY` | API-ключ Azure OpenAI | - | Для Azure |
| `AZURE_OPENAI_API_VERSION` | Версия API Azure | `2024-08-01-preview` | Нет |

## Устранение неполадок

### Распространенные проблемы

1. **Предупреждение "Не удалось использовать Foundry SDK":**
   - Установите foundry-local-sdk: `pip install foundry-local-sdk`
   - Или задайте переменные окружения для ручной конфигурации

2. **Отказ в подключении:**
   - Убедитесь, что Foundry Local запущен: `foundry service status`
   - Проверьте, загружена ли модель: `foundry service ps`

3. **Модель не найдена:**
   - Список доступных моделей: `foundry model list`
   - Загрузите модель: `foundry model run phi-4-mini`

### Проверка

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Ссылки

- [Документация Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local на GitHub](https://github.com/microsoft/Foundry-Local)
- [Справочник по API, совместимому с OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

