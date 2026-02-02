# Зразок 02: Інтеграція OpenAI SDK

Демонструє розширену інтеграцію з OpenAI Python SDK, підтримуючи як Microsoft Foundry Local, так і Azure OpenAI зі стрімінговими відповідями та належною обробкою помилок.

## Огляд

Цей зразок демонструє:
- Легке перемикання між Foundry Local та Azure OpenAI
- Стрімінгові завершення чату для покращення користувацького досвіду
- Правильне використання SDK FoundryLocalManager
- Надійні механізми обробки помилок та резервування
- Кодові шаблони, готові до використання у виробництві

## Попередні вимоги

- **Foundry Local**: Встановлений і запущений (для локального інференсу)
- **Python**: Версія 3.8 або новіша з OpenAI SDK
- **Azure OpenAI**: Дійсний кінцевий пункт і ключ API (для хмарного інференсу)

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

3. **Запустіть Foundry Local (для локального режиму):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Сценарії використання

### Foundry Local (за замовчуванням)

**Варіант 1: Використання FoundryLocalManager (рекомендовано)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Варіант 2: Ручна конфігурація**
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


## Архітектура коду

### Шаблон фабрики клієнтів

Зразок використовує шаблон фабрики для створення відповідних клієнтів:

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


### Стрімінгові відповіді

Зразок демонструє стрімінг для генерації відповідей у реальному часі:

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


## Змінні середовища

### Конфігурація Foundry Local

| Змінна | Опис | За замовчуванням | Обов'язково |
|--------|------|------------------|-------------|
| `MODEL` | Псевдонім моделі для використання | `phi-4-mini` | Ні |
| `BASE_URL` | Кінцевий пункт Foundry Local | `http://localhost:8000` | Ні |
| `API_KEY` | Ключ API (необов'язковий для локального режиму) | `""` | Ні |

### Конфігурація Azure OpenAI

| Змінна | Опис | За замовчуванням | Обов'язково |
|--------|------|------------------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Кінцевий пункт ресурсу Azure OpenAI | - | Так |
| `AZURE_OPENAI_API_KEY` | Ключ API Azure OpenAI | - | Так |
| `AZURE_OPENAI_API_VERSION` | Версія API | `2024-08-01-preview` | Ні |
| `MODEL` | Назва розгортання Azure | `your-deployment-name` | Так |

## Розширені функції

### Автоматичне виявлення сервісу

Зразок автоматично визначає відповідний сервіс на основі змінних середовища:

1. **Режим Azure**: Якщо встановлені `AZURE_OPENAI_ENDPOINT` та `AZURE_OPENAI_API_KEY`
2. **Режим SDK Foundry**: Якщо доступний SDK Foundry Local
3. **Ручний режим**: Резервування до ручної конфігурації

### Обробка помилок

- Плавне резервування від SDK до ручної конфігурації
- Чіткі повідомлення про помилки для усунення несправностей
- Належна обробка виключень для мережевих проблем
- Перевірка необхідних змінних середовища

## Міркування щодо продуктивності

### Порівняння локального та хмарного режимів

**Переваги Foundry Local:**
- ✅ Відсутність витрат на API
- ✅ Конфіденційність даних (дані не залишають пристрій)
- ✅ Низька затримка для підтримуваних моделей
- ✅ Працює офлайн

**Переваги Azure OpenAI:**
- ✅ Доступ до найновіших великих моделей
- ✅ Вища пропускна здатність
- ✅ Відсутність вимог до локальних обчислень
- ✅ SLA корпоративного рівня

## Усунення несправностей

### Поширені проблеми

1. **Попередження "Не вдалося використати SDK Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Помилки автентифікації Azure:**
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


### Перевірка стану

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Наступні кроки

- **Зразок 03**: Виявлення моделей та тестування продуктивності
- **Зразок 04**: Створення Chainlit RAG додатку
- **Зразок 05**: Оркестрація мультиагентів
- **Зразок 06**: Маршрутизація моделей як інструментів

## Посилання

- [Документація Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Довідник SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Документація OpenAI Python SDK](https://github.com/openai/openai-python)
- [Посібник зі стрімінгових завершень](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

