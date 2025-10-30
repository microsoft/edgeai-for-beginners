<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:23:58+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sr"
}
-->
# Напомене о миграцији локалног SDK-а Foundry

## Преглед

Сви Python фајлови у фасцикли Workshop ажурирани су да прате најновије шаблоне из званичног [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Резиме промена

### Основна инфраструктура (`workshop_utils.py`)

#### Побољшане функције:
- **Подршка за замену крајњих тачака**: Додата подршка за променљиву окружења `FOUNDRY_LOCAL_ENDPOINT`
- **Побољшано руковање грешкама**: Боље руковање изузецима са детаљним порукама о грешкама
- **Побољшано кеширање**: Кључеви кеша сада укључују крајњу тачку за сценарије са више крајњих тачака
- **Експоненцијално одлагање**: Логика поновног покушаја сада користи експоненцијално одлагање за бољу поузданост
- **Анотације типова**: Додате свеобухватне анотације типова за бољу подршку у IDE-у

#### Нове могућности:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Пример апликација

#### Сесија 01: Покретање чета (`chat_bootstrap.py`)
- Ажуриран подразумевани модел са `phi-3.5-mini` на `phi-4-mini`
- Додата подршка за замену крајњих тачака
- Побољшана документација са референцама на SDK

#### Сесија 02: RAG Платформа (`rag_pipeline.py`)
- Ажурирано да користи `phi-4-mini` као подразумевани модел
- Додата подршка за замену крајњих тачака
- Побољшана документација са детаљима о променљивама окружења

#### Сесија 02: RAG Евалуација (`rag_eval_ragas.py`)
- Ажурирани подразумевани модели
- Додата конфигурација крајњих тачака
- Побољшано руковање грешкама

#### Сесија 03: Бенчмаркинг (`benchmark_oss_models.py`)
- Ажурирана листа подразумеваних модела да укључује `phi-4-mini`
- Додата свеобухватна документација о променљивама окружења
- Побољшана документација функција
- Додата подршка за замену крајњих тачака

#### Сесија 04: Поређење модела (`model_compare.py`)
- Ажуриран подразумевани LLM са `gpt-oss-20b` на `qwen2.5-7b`
- Додата конфигурација крајњих тачака
- Побољшана документација

#### Сесија 05: Оркестрација више агената (`agents_orchestrator.py`)
- Додате анотације типова (промењено `str | None` у `Optional[str]`)
- Побољшана документација класе Agent
- Додата подршка за замену крајњих тачака
- Побољшан образац иницијализације

#### Сесија 06: Рутер модела (`models_router.py`)
- Додата конфигурација крајњих тачака
- Побољшана документација детекције намере
- Побољшана документација логике рутирања

#### Сесија 06: Платформа (`models_pipeline.py`)
- Додата свеобухватна документација функција
- Побољшана документација корак по корак
- Побољшано руковање грешкама

### Скрипте

#### Извоз бенчмарка (`export_benchmark_markdown.py`)
- Додата подршка за замену крајњих тачака
- Ажурирани подразумевани модели
- Побољшана документација функција
- Побољшано руковање грешкама

#### CLI Линтер (`lint_markdown_cli.py`)
- Додате референце на SDK
- Побољшана документација употребе

### Тестови

#### Smoke тестови (`smoke.py`)
- Додата подршка за замену крајњих тачака
- Побољшана документација
- Побољшана документација тест случајева
- Боље извештавање о грешкама

## Променљиве окружења

Сви примери сада подржавају следеће променљиве окружења:

### Основна конфигурација
- `FOUNDRY_LOCAL_ALIAS` - Алијас модела који се користи (подразумевано варира по примеру)
- `FOUNDRY_LOCAL_ENDPOINT` - Замена крајње тачке сервиса (опционо)
- `SHOW_USAGE` - Приказ статистике употребе токена (подразумевано: "0")
- `RETRY_ON_FAIL` - Омогућава логику поновног покушаја (подразумевано: "1")
- `RETRY_BACKOFF` - Почетно одлагање поновног покушаја у секундама (подразумевано: "1.0")

### Специфично за пример
- `EMBED_MODEL` - Модел за уграђивање за RAG примере
- `BENCH_MODELS` - Модели одвојени зарезом за бенчмаркинг
- `BENCH_ROUNDS` - Број рунди бенчмарка
- `BENCH_PROMPT` - Тестни упит за бенчмарке
- `BENCH_STREAM` - Мерење кашњења првог токена
- `RAG_QUESTION` - Тестно питање за RAG примере
- `AGENT_MODEL_PRIMARY` - Примарни модел агента
- `AGENT_MODEL_EDITOR` - Модел агента уредника
- `SLM_ALIAS` - Алијас малог језичког модела
- `LLM_ALIAS` - Алијас великог језичког модела

## Најбоље праксе SDK-а које су имплементиране

### 1. Правилна иницијализација клијента
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Преузимање информација о моделу
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Руковање грешкама
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Логика поновног покушаја са експоненцијалним одлагањем
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Подршка за стриминг
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Водич за миграцију за прилагођене примере

Ако креирате нове примере или ажурирате постојеће:

1. **Користите помоћне функције из `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Подржите замену крајњих тачака**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Додајте свеобухватну документацију**:
   - Променљиве окружења у docstring-у
   - Референца на SDK
   - Примери употребе

4. **Користите анотације типова**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Имплементирајте правилно руковање грешкама**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Тестирање

Сви примери могу се тестирати са:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Референце документације SDK-а

- **Главни репозиторијум**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API документација**: Проверите SDK репозиторијум за најновију API документацију

## Промене које прекидају компатибилност

### Није очекивано
Све промене су уназад компатибилне. Ажурирања углавном:
- Додају нове опционалне функције (замена крајњих тачака)
- Побољшавају руковање грешкама
- Унапређују документацију
- Ажурирају подразумевана имена модела на тренутне препоруке

### Опционална побољшања
Можда ћете желети да ажурирате свој код да користи:
- `FOUNDRY_LOCAL_ENDPOINT` за експлицитну контролу крајњих тачака
- `SHOW_USAGE=1` за видљивост употребе токена
- Ажуриране подразумеване моделе (`phi-4-mini` уместо `phi-3.5-mini`)

## Уобичајени проблеми и решења

### Проблем: "Иницијализација клијента није успела"
**Решење**: Уверите се да је Foundry Local сервис покренут:
```bash
foundry service start
foundry model run phi-4-mini
```

### Проблем: "Модел није пронађен"
**Решење**: Проверите доступне моделе:
```bash
foundry model list
```

### Проблем: Грешке у повезивању са крајњом тачком
**Решење**: Проверите крајњу тачку:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Следећи кораци

1. **Ажурирајте Module08 примере**: Примените сличне шаблоне на Module08/samples
2. **Додајте интеграционе тестове**: Креирајте свеобухватан тестни пакет
3. **Бенчмаркинг перформанси**: Упоредите перформансе пре/после
4. **Ажурирање документације**: Ажурирајте главни README са новим шаблонима

## Упутства за допринос

Када додајете нове примере:
1. Користите `workshop_utils.py` ради конзистентности
2. Пратите шаблон у постојећим примерима
3. Додајте свеобухватне docstring-ове
4. Укључите референце на SDK
5. Подржите замену крајњих тачака
6. Додајте правилне анотације типова
7. Укључите примере употребе у docstring-у

## Компатибилност верзија

Ова ажурирања су компатибилна са:
- `foundry-local-sdk` (најновија)
- `openai>=1.30.0`
- Python 3.8+

---

**Последње ажурирање**: 2025-01-08  
**Одржавалац**: EdgeAI Workshop тим  
**Верзија SDK-а**: Foundry Local SDK (најновија 0.7.117+67073234e7)

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.