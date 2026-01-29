# Пример 02: Интеграција са OpenAI SDK-ом

Демонстрира напредну интеграцију са OpenAI Python SDK-ом, уз подршку за Microsoft Foundry Local и Azure OpenAI, са стриминг одговорима и правилним руковањем грешкама.

## Преглед

Овај пример приказује:
- Лако пребацивање између Foundry Local и Azure OpenAI
- Стриминг завршетка разговора за боље корисничко искуство
- Правилну употребу FoundryLocalManager SDK-а
- Робусне механизме за руковање грешкама и резервне опције
- Код спреман за продукцију

## Предуслови

- **Foundry Local**: Инсталиран и покренут (за локалну инференцију)
- **Python**: Верзија 3.8 или новија са OpenAI SDK-ом
- **Azure OpenAI**: Валидан крајњи тачка и API кључ (за инференцију у облаку)

## Инсталација

1. **Подесите Python окружење:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Инсталирајте зависности:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Покрените Foundry Local (за локални режим):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Сценарији употребе

### Foundry Local (Подразумевано)

**Опција 1: Коришћење FoundryLocalManager (Препоручено)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Опција 2: Ручна конфигурација**
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

### Патерн фабрике клијената

Пример користи патерн фабрике за креирање одговарајућих клијената:

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


### Стриминг одговора

Пример демонстрира стриминг за генерисање одговора у реалном времену:

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


## Променљиве окружења

### Конфигурација Foundry Local

| Променљива | Опис | Подразумевано | Обавезно |
|------------|-------|---------------|----------|
| `MODEL` | Алијас модела који се користи | `phi-4-mini` | Не |
| `BASE_URL` | Крајњи тачка Foundry Local-а | `http://localhost:8000` | Не |
| `API_KEY` | API кључ (опционо за локално) | `""` | Не |

### Конфигурација Azure OpenAI

| Променљива | Опис | Подразумевано | Обавезно |
|------------|-------|---------------|----------|
| `AZURE_OPENAI_ENDPOINT` | Крајњи тачка Azure OpenAI ресурса | - | Да |
| `AZURE_OPENAI_API_KEY` | API кључ Azure OpenAI-а | - | Да |
| `AZURE_OPENAI_API_VERSION` | Верзија API-а | `2024-08-01-preview` | Не |
| `MODEL` | Назив Azure деплоја | `your-deployment-name` | Да |

## Напредне функције

### Аутоматско откривање сервиса

Пример аутоматски детектује одговарајући сервис на основу променљивих окружења:

1. **Azure режим**: Ако су `AZURE_OPENAI_ENDPOINT` и `AZURE_OPENAI_API_KEY` подешени
2. **Foundry SDK режим**: Ако је Foundry Local SDK доступан
3. **Ручни режим**: Резервна опција за ручну конфигурацију

### Руковање грешкама

- Грациозно пребацивање са SDK-а на ручну конфигурацију
- Јасне поруке о грешкама за решавање проблема
- Правилно руковање изузецима за проблеме са мрежом
- Валидација обавезних променљивих окружења

## Перформансе

### Локално vs Облак

**Предности Foundry Local-а:**
- ✅ Нема трошкова API-а
- ✅ Приватност података (подаци не напуштају уређај)
- ✅ Ниска латенција за подржане моделе
- ✅ Ради офлајн

**Предности Azure OpenAI-а:**
- ✅ Приступ најновијим великим моделима
- ✅ Већи пропусни опсег
- ✅ Нема захтева за локалним рачунарским ресурсима
- ✅ SLA на нивоу предузећа

## Решавање проблема

### Уобичајени проблеми

1. **Упозорење "Није могуће користити Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Грешке у аутентификацији Azure-а:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Модел није доступан:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Провере здравља

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Следећи кораци

- **Пример 03**: Откривање модела и бенчмаркинг
- **Пример 04**: Изградња Chainlit RAG апликације
- **Пример 05**: Оркестрација више агената
- **Пример 06**: Рутање модела као алата

## Референце

- [Azure OpenAI документација](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK референца](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK документација](https://github.com/openai/openai-python)
- [Водич за стриминг завршетка](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

