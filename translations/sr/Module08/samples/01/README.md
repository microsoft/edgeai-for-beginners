# Пример 01: Брзи разговор преко OpenAI SDK-а

Једноставан пример разговора који показује како користити OpenAI SDK са Microsoft Foundry Local за локалну AI обраду.

## Преглед

Овај пример показује како:
- Користити OpenAI Python SDK са Foundry Local
- Руковати конфигурацијама за Azure OpenAI и локални Foundry
- Применити правилно руковање грешкама и стратегије резервног плана
- Користити FoundryLocalManager за управљање сервисима

## Предуслови

- **Foundry Local**: Инсталиран и доступан на PATH
- **Python**: Верзија 3.8 или новија
- **Модел**: Модел учитан у Foundry Local (нпр. `phi-4-mini`)

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

3. **Покрените Foundry Local сервис и учитајте модел:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Коришћење

### Foundry Local (Подразумевано)

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


## Карактеристике кода

### Интеграција FoundryLocalManager-а

Пример користи званични Foundry Local SDK за правилно управљање сервисима:

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


### Руковање грешкама

Робусно руковање грешкама са резервним планом за ручну конфигурацију:
- Аутоматско откривање сервиса
- Грациозно смањење функционалности ако SDK није доступан
- Јасне поруке о грешкама за решавање проблема

## Променљиве окружења

| Променљива | Опис | Подразумевано | Обавезно |
|------------|-------|---------------|----------|
| `MODEL` | Алијас или назив модела | `phi-4-mini` | Не |
| `BASE_URL` | Основни URL за Foundry Local | `http://localhost:8000` | Не |
| `API_KEY` | API кључ (обично није потребан за локално) | `""` | Не |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI крајња тачка | - | За Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API кључ | - | За Azure |
| `AZURE_OPENAI_API_VERSION` | Верзија Azure API-а | `2024-08-01-preview` | Не |

## Решавање проблема

### Уобичајени проблеми

1. **Упозорење "Није могуће користити Foundry SDK":**
   - Инсталирајте foundry-local-sdk: `pip install foundry-local-sdk`
   - Или подесите променљиве окружења за ручну конфигурацију

2. **Одбијена веза:**
   - Уверите се да Foundry Local ради: `foundry service status`
   - Проверите да ли је модел учитан: `foundry service ps`

3. **Модел није пронађен:**
   - Листајте доступне моделе: `foundry model list`
   - Учитајте модел: `foundry model run phi-4-mini`

### Верификација

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Референце

- [Foundry Local документација](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-компатибилна API референца](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

