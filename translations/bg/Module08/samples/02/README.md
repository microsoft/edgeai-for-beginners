# Пример 02: Интеграция с OpenAI SDK

Демонстрира напреднала интеграция с OpenAI Python SDK, поддържаща както Microsoft Foundry Local, така и Azure OpenAI, със стрийминг отговори и правилно управление на грешки.

## Общ преглед

Този пример показва:
- Лесно превключване между Foundry Local и Azure OpenAI
- Стрийминг на чат отговори за по-добро потребителско изживяване
- Правилно използване на FoundryLocalManager SDK
- Надеждно управление на грешки и механизми за резервиране
- Кодови шаблони, готови за производство

## Предпоставки

- **Foundry Local**: Инсталиран и работещ (за локално прогнозиране)
- **Python**: Версия 3.8 или по-нова с OpenAI SDK
- **Azure OpenAI**: Валиден крайна точка и API ключ (за облачно прогнозиране)

## Инсталация

1. **Настройка на Python среда:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Инсталиране на зависимости:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Стартиране на Foundry Local (за локален режим):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Сценарии за използване

### Foundry Local (по подразбиране)

**Опция 1: Използване на FoundryLocalManager (Препоръчително)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Опция 2: Ръчна конфигурация**
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


## Архитектура на кода

### Шаблон за фабрика на клиенти

Примерът използва фабричен шаблон за създаване на подходящи клиенти:

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


### Стрийминг отговори

Примерът демонстрира стрийминг за генериране на отговори в реално време:

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


## Променливи на средата

### Конфигурация на Foundry Local

| Променлива | Описание | По подразбиране | Задължително |
|------------|-----------|-----------------|--------------|
| `MODEL` | Псевдоним на модела за използване | `phi-4-mini` | Не |
| `BASE_URL` | Крайна точка на Foundry Local | `http://localhost:8000` | Не |
| `API_KEY` | API ключ (опционален за локално) | `""` | Не |

### Конфигурация на Azure OpenAI

| Променлива | Описание | По подразбиране | Задължително |
|------------|-----------|-----------------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Крайна точка на ресурса Azure OpenAI | - | Да |
| `AZURE_OPENAI_API_KEY` | API ключ за Azure OpenAI | - | Да |
| `AZURE_OPENAI_API_VERSION` | Версия на API | `2024-08-01-preview` | Не |
| `MODEL` | Име на разгръщане в Azure | `your-deployment-name` | Да |

## Напреднали функции

### Автоматично откриване на услуги

Примерът автоматично открива подходящата услуга въз основа на променливите на средата:

1. **Режим Azure**: Ако са зададени `AZURE_OPENAI_ENDPOINT` и `AZURE_OPENAI_API_KEY`
2. **Режим Foundry SDK**: Ако Foundry Local SDK е наличен
3. **Ръчен режим**: Резервиране към ръчна конфигурация

### Управление на грешки

- Грациозно резервиране от SDK към ръчна конфигурация
- Ясни съобщения за грешки за отстраняване на проблеми
- Правилно управление на изключения за мрежови проблеми
- Валидация на задължителните променливи на средата

## Съображения за производителност

### Локални срещу облачни компромиси

**Предимства на Foundry Local:**
- ✅ Няма разходи за API
- ✅ Поверителност на данните (данните не напускат устройството)
- ✅ Ниска латентност за поддържаните модели
- ✅ Работи офлайн

**Предимства на Azure OpenAI:**
- ✅ Достъп до най-новите големи модели
- ✅ По-висока пропускателна способност
- ✅ Няма изисквания за локални изчисления
- ✅ SLA от корпоративен клас

## Отстраняване на проблеми

### Чести проблеми

1. **Предупреждение "Не може да се използва Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Грешки при удостоверяване в Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Моделът не е наличен:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Проверки на състоянието

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Следващи стъпки

- **Пример 03**: Откриване и оценка на модели
- **Пример 04**: Създаване на Chainlit RAG приложение
- **Пример 05**: Оркестрация на множество агенти
- **Пример 06**: Маршрутизиране на модели като инструменти

## Референции

- [Документация за Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Референция за Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Документация за OpenAI Python SDK](https://github.com/openai/openai-python)
- [Ръководство за стрийминг отговори](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

