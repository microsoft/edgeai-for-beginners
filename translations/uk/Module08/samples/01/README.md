# Приклад 01: Швидкий чат через OpenAI SDK

Простий приклад чату, який демонструє, як використовувати OpenAI SDK разом із Microsoft Foundry Local для локального AI-аналізу.

## Огляд

Цей приклад показує, як:
- Використовувати OpenAI Python SDK із Foundry Local
- Працювати як з конфігураціями Azure OpenAI, так і з локальними Foundry
- Реалізувати правильну обробку помилок і стратегії резервування
- Використовувати FoundryLocalManager для управління сервісами

## Попередні вимоги

- **Foundry Local**: Встановлений і доступний у PATH
- **Python**: Версія 3.8 або новіша
- **Модель**: Модель, завантажена у Foundry Local (наприклад, `phi-4-mini`)

## Встановлення

1. **Налаштуйте середовище Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Встановіть залежності:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Запустіть сервіс Foundry Local і завантажте модель:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Використання

### Foundry Local (за замовчуванням)

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

## Особливості коду

### Інтеграція FoundryLocalManager

У прикладі використовується офіційний SDK Foundry Local для правильного управління сервісами:

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

### Обробка помилок

Надійна обробка помилок із резервуванням для ручної конфігурації:
- Автоматичне виявлення сервісу
- Плавна деградація у разі недоступності SDK
- Чіткі повідомлення про помилки для усунення несправностей

## Змінні середовища

| Змінна | Опис | За замовчуванням | Обов'язково |
|--------|------|------------------|-------------|
| `MODEL` | Псевдонім або назва моделі | `phi-4-mini` | Ні |
| `BASE_URL` | Базовий URL Foundry Local | `http://localhost:8000` | Ні |
| `API_KEY` | API-ключ (зазвичай не потрібен для локального використання) | `""` | Ні |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Для Azure |
| `AZURE_OPENAI_API_KEY` | API-ключ Azure OpenAI | - | Для Azure |
| `AZURE_OPENAI_API_VERSION` | Версія API Azure | `2024-08-01-preview` | Ні |

## Усунення несправностей

### Поширені проблеми

1. **Попередження "Не вдалося використовувати Foundry SDK":**
   - Встановіть foundry-local-sdk: `pip install foundry-local-sdk`
   - Або налаштуйте змінні середовища для ручної конфігурації

2. **Відмова у з'єднанні:**
   - Переконайтеся, що Foundry Local запущений: `foundry service status`
   - Перевірте, чи завантажена модель: `foundry service ps`

3. **Модель не знайдена:**
   - Перегляньте доступні моделі: `foundry model list`
   - Завантажте модель: `foundry model run phi-4-mini`

### Перевірка

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Посилання

- [Документація Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local на GitHub](https://github.com/microsoft/Foundry-Local)
- [Довідник API, сумісного з OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

