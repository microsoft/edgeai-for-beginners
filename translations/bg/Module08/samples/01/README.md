# Пример 01: Бърз чат чрез OpenAI SDK

Прост пример за чат, демонстриращ как да използвате OpenAI SDK с Microsoft Foundry Local за локално AI заключение.

## Общ преглед

Този пример показва как да:
- Използвате OpenAI Python SDK с Foundry Local
- Работите с конфигурации както за Azure OpenAI, така и за локален Foundry
- Реализирате правилно обработване на грешки и стратегии за резервиране
- Използвате FoundryLocalManager за управление на услугите

## Предпоставки

- **Foundry Local**: Инсталиран и наличен в PATH
- **Python**: Версия 3.8 или по-нова
- **Модел**: Зареден модел в Foundry Local (например, `phi-4-mini`)

## Инсталация

1. **Настройте Python среда:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Инсталирайте зависимости:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Стартирайте Foundry Local услуга и заредете модел:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Употреба

### Foundry Local (по подразбиране)

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


## Характеристики на кода

### Интеграция с FoundryLocalManager

Примерът използва официалния Foundry Local SDK за правилно управление на услугите:

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


### Обработване на грешки

Надеждно обработване на грешки с резервиране към ръчна конфигурация:
- Автоматично откриване на услуги
- Грациозно намаляване на функционалността, ако SDK не е наличен
- Ясни съобщения за грешки за улесняване на диагностицирането

## Променливи на средата

| Променлива | Описание | По подразбиране | Задължителна |
|------------|-----------|-----------------|--------------|
| `MODEL` | Псевдоним или име на модела | `phi-4-mini` | Не |
| `BASE_URL` | Основен URL за Foundry Local | `http://localhost:8000` | Не |
| `API_KEY` | API ключ (обикновено не е нужен за локално) | `""` | Не |
| `AZURE_OPENAI_ENDPOINT` | Endpoint за Azure OpenAI | - | За Azure |
| `AZURE_OPENAI_API_KEY` | API ключ за Azure OpenAI | - | За Azure |
| `AZURE_OPENAI_API_VERSION` | Версия на Azure API | `2024-08-01-preview` | Не |

## Отстраняване на проблеми

### Чести проблеми

1. **Предупреждение "Не може да се използва Foundry SDK":**
   - Инсталирайте foundry-local-sdk: `pip install foundry-local-sdk`
   - Или задайте променливи на средата за ръчна конфигурация

2. **Отказ на връзката:**
   - Уверете се, че Foundry Local работи: `foundry service status`
   - Проверете дали моделът е зареден: `foundry service ps`

3. **Моделът не е намерен:**
   - Списък с налични модели: `foundry model list`
   - Заредете модел: `foundry model run phi-4-mini`

### Проверка

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Референции

- [Документация за Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Референция за OpenAI-съвместим API](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

