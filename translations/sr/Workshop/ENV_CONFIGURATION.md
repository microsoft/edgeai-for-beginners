<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:19:35+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "sr"
}
-->
# Водич за конфигурацију окружења

## Преглед

Примери из радионице користе променљиве окружења за конфигурацију, централизоване у `.env` датотеци на корену репозиторијума. Ово омогућава лако прилагођавање без измене кода.

## Брзи почетак

### 1. Проверите предуслове

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Конфигуришите окружење

`.env` датотека је већ конфигурисана са разумним подразумеваним вредностима. Већина корисника неће морати ништа да мења.

**Опционо**: Прегледајте и прилагодите подешавања:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Примените конфигурацију

**За Python скрипте:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**За бележнице:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Референца променљивих окружења

### Основна конфигурација

| Променљива | Подразумевано | Опис |
|------------|---------------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Подразумевани модел за примере |
| `FOUNDRY_LOCAL_ENDPOINT` | (празно) | Замена за сервисни крајњи тачку |
| `PYTHONPATH` | Путање радионице | Путања за претрагу Python модула |

**Када поставити FOUNDRY_LOCAL_ENDPOINT:**
- Далеко инстанцирање Foundry Local-а
- Прилагођена конфигурација порта
- Раздвајање развоја и продукције

**Пример:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Променљиве специфичне за сесију

#### Сесија 02: RAG Пипелине
| Променљива | Подразумевано | Сврха |
|------------|---------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модел за уграђивање |
| `RAG_QUESTION` | Предконфигурисано | Тест питање |

#### Сесија 03: Бенчмаркинг
| Променљива | Подразумевано | Сврха |
|------------|---------------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Модели за бенчмаркинг |
| `BENCH_ROUNDS` | `3` | Итерације по моделу |
| `BENCH_PROMPT` | Предконфигурисано | Тест упит |
| `BENCH_STREAM` | `0` | Мерење кашњења првог токена |

#### Сесија 04: Поређење модела
| Променљива | Подразумевано | Сврха |
|------------|---------------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Мали језички модел |
| `LLM_ALIAS` | `qwen2.5-7b` | Велики језички модел |
| `COMPARE_PROMPT` | Предконфигурисано | Упит за поређење |
| `COMPARE_RETRIES` | `2` | Покушаји поновног покушаја |

#### Сесија 05: Оркестрација више агената
| Променљива | Подразумевано | Сврха |
|------------|---------------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Модел истраживачког агента |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Модел уредничког агента |
| `AGENT_QUESTION` | Предконфигурисано | Тест питање |

### Конфигурација поузданости

| Променљива | Подразумевано | Сврха |
|------------|---------------|-------|
| `SHOW_USAGE` | `1` | Испис коришћења токена |
| `RETRY_ON_FAIL` | `1` | Омогућава логику поновног покушаја |
| `RETRY_BACKOFF` | `1.0` | Кашњење пре поновног покушаја (секунде) |

## Уобичајене конфигурације

### Развојно окружење (брза итерација)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Продукцијско окружење (фокус на квалитет)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Бенчмаркинг конфигурација
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Специјализација више агената
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Далеко развојно окружење
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Препоручени модели

### Према намени

**Општа намена:**
- `phi-4-mini` - Балансиран квалитет и брзина

**Брзи одговори:**
- `qwen2.5-0.5b` - Веома брз, добар за класификацију
- `phi-4-mini` - Брз са добрим квалитетом

**Висок квалитет:**
- `qwen2.5-7b` - Најбољи квалитет, већа потрошња ресурса
- `phi-4-mini` - Добар квалитет, мања потрошња ресурса

**Генерисање кода:**
- `deepseek-coder-1.3b` - Специјализован за код
- `phi-4-mini` - Општа намена за кодирање

### Према доступности ресурса

**Мали ресурси (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Средњи ресурси (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Велики ресурси (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Напредна конфигурација

### Прилагођени крајњи тачке

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Температура и узорковање (замена у коду)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI хибридна конфигурација

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Решавање проблема

### Променљиве окружења нису учитане

**Симптоми:**
- Скрипте користе погрешне моделе
- Грешке у повезивању
- Променљиве нису препознате

**Решења:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Проблеми са повезивањем сервиса

**Симптоми:**
- Грешке "Connection refused"
- "Service not available"
- Грешке временског истека

**Решења:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Модел није пронађен

**Симптоми:**
- Грешке "Model not found"
- "Alias not recognized"

**Решења:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Грешке у увозу

**Симптоми:**
- Грешке "Module not found"

**Решења:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Тестирање конфигурације

### Проверите учитавање окружења

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Тестирајте повезивање са Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Најбоље праксе за безбедност

### 1. Никада не објављујте тајне

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Користите одвојене .env датотеке

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Ротирајте API кључеве

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Користите конфигурацију специфичну за окружење

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK документација

- **Главни репозиторијум**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API документација**: Погледајте SDK репозиторијум за најновије информације

## Додатни ресурси

- `QUICK_START.md` - Водич за почетак
- `SDK_MIGRATION_NOTES.md` - Детаљи о ажурирању SDK-а
- `Workshop/samples/*/README.md` - Водичи специфични за примере

---

**Последње ажурирање**: 2025-01-08  
**Верзија**: 2.0  
**SDK**: Foundry Local Python SDK (најновији)

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.