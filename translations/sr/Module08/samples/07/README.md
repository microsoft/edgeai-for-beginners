# Foundry Local као пример API

Овај пример показује како да користите Microsoft Foundry Local као REST API услугу без ослањања на OpenAI SDK. Приказује директне HTTP интеграционе шаблоне за максималну контролу и прилагођавање.

## Преглед

На основу званичних шаблона Microsoft Foundry Local, овај пример пружа:
- Директну REST API интеграцију са FoundryLocalManager
- Прилагођену имплементацију HTTP клијента
- Управљање моделима и праћење здравственог стања
- Обраду одговора са стримингом и без стриминга
- Логика за руковање грешкама и поновним покушајима спремна за производњу

## Предуслови

1. **Инсталација Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python зависности**
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

## Кључне карактеристике

### 1. **Директна HTTP интеграција**
- Чисти REST API позиви без зависности од SDK-а
- Прилагођена аутентификација и заглавља
- Потпуна контрола над обрадом захтева и одговора

### 2. **Управљање моделима**
- Динамичко учитавање и уклањање модела
- Праћење здравственог стања и провере статуса
- Прикупљање метрика перформанси

### 3. **Шаблони за производњу**
- Механизми за поновне покушаје са експоненцијалним одлагањем
- Circuit breaker за толеранцију на грешке
- Свеобухватно логовање и праћење

### 4. **Флексибилна обрада одговора**
- Одговори са стримингом за апликације у реалном времену
- Обрада у серијама за сценарије са великим протоком
- Прилагођено парсирање и валидација одговора

## Примери употребе

### Основна API интеграција
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

### Интеграција са стримингом
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Праћење здравственог стања
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Структура фајлова

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

## Интеграција Microsoft Foundry Local

Овај пример прати званичне шаблоне Microsoft-а:

1. **SDK интеграција**: Користи `FoundryLocalManager` за управљање услугама
2. **REST крајње тачке**: Директни позиви на `/v1/chat/completions` и друге крајње тачке
3. **Аутентификација**: Правилно руковање API кључем за локалне услуге
4. **Управљање моделима**: Листање каталога, преузимање и шаблони за учитавање
5. **Руковање грешкама**: Препоручени кодови грешака и одговори од Microsoft-а

## Почетак

1. **Инсталирајте зависности**
   ```bash
   pip install -r requirements.txt
   ```

2. **Покрените основни пример**
   ```bash
   python examples/basic_usage.py
   ```

3. **Испробајте стриминг**
   ```bash
   python examples/streaming.py
   ```

4. **Подешавање за производњу**
   ```bash
   python examples/production.py
   ```

## Конфигурација

Променљиве окружења за прилагођавање:
- `FOUNDRY_MODEL`: Подразумевани модел за употребу (подразумевано: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Време истека захтева у секундама (подразумевано: 30)
- `FOUNDRY_RETRIES`: Број покушаја поновног покушаја (подразумевано: 3)
- `FOUNDRY_LOG_LEVEL`: Ниво логовања (подразумевано: "INFO")

## Најбоље праксе

1. **Управљање конекцијама**: Поновно коришћење HTTP конекција за боље перформансе
2. **Руковање грешкама**: Имплементирајте правилну логику поновних покушаја са експоненцијалним одлагањем
3. **Праћење ресурса**: Пратите употребу меморије модела и перформансе
4. **Безбедност**: Користите правилну аутентификацију чак и за локалне услуге
5. **Тестирање**: Укључите и јединичне и интеграционе тестове

## Решавање проблема

### Уобичајени проблеми

**Услуга не ради**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Проблеми са учитавањем модела**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Грешке у конекцији**
- Проверите да ли Foundry Local ради на исправном порту
- Проверите подешавања заштитног зида
- Уверите се да су заглавља за аутентификацију исправна

## Оптимизација перформанси

1. **Пул конекција**: Користите session објекте за више захтева
2. **Асинхроне операције**: Искористите asyncio за истовремене захтеве
3. **Кеширање**: Кеширајте одговоре модела где је то прикладно
4. **Праћење**: Пратите време одговора и прилагодите временска ограничења

## Резултати учења

Након завршетка овог примера, разумећете:
- Директну REST API интеграцију са Foundry Local
- Шаблоне имплементације прилагођеног HTTP клијента
- Руковање грешкама и праћење спремно за производњу
- Архитектуру услуге Microsoft Foundry Local
- Технике оптимизације перформанси за локалне AI услуге

## Следећи кораци

- Истражите Пример 08: Windows 11 Chat апликација
- Испробајте Пример 09: Оркестрација више агената
- Научите Пример 10: Foundry Local као интеграција алата

---

