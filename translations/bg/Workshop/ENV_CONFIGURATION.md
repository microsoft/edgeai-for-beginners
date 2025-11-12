<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-12T00:22:42+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "bg"
}
-->
# Ръководство за конфигурация на средата

## Общ преглед

Примерите от Workshop използват променливи на средата за конфигурация, централизирани в `.env` файла в основната директория на хранилището. Това позволява лесна персонализация без промяна на кода.

## Бърз старт

### 1. Проверете предпоставките

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Конфигурирайте средата

Файлът `.env` вече е конфигуриран с разумни настройки по подразбиране. Повечето потребители няма да се нуждаят от промени.

**По избор**: Прегледайте и персонализирайте настройките:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Приложете конфигурацията

**За Python скриптове:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**За тетрадки:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Референция на променливите на средата

### Основна конфигурация

| Променлива | По подразбиране | Описание |
|------------|-----------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Модел по подразбиране за примерите |
| `FOUNDRY_LOCAL_ENDPOINT` | (празно) | Замяна на крайна точка на услугата |
| `PYTHONPATH` | Пътища на Workshop | Път за търсене на Python модули |

**Кога да зададете FOUNDRY_LOCAL_ENDPOINT:**
- Отдалечен Foundry Local инстанс
- Персонализирана конфигурация на порт
- Разделение между разработка и продукция

**Пример:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Променливи, специфични за сесията

#### Сесия 02: RAG Pipeline
| Променлива | По подразбиране | Цел |
|------------|-----------------|-----|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модел за вграждане |
| `RAG_QUESTION` | Предварително конфигурирано | Тестов въпрос |

#### Сесия 03: Бенчмаркинг
| Променлива | По подразбиране | Цел |
|------------|-----------------|-----|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Модели за бенчмаркинг |
| `BENCH_ROUNDS` | `3` | Итерации на модел |
| `BENCH_PROMPT` | Предварително конфигурирано | Тестов промпт |
| `BENCH_STREAM` | `0` | Измерване на латентност на първия токен |

#### Сесия 04: Сравнение на модели
| Променлива | По подразбиране | Цел |
|------------|-----------------|-----|
| `SLM_ALIAS` | `phi-4-mini` | Малък езиков модел |
| `LLM_ALIAS` | `qwen2.5-7b` | Голям езиков модел |
| `COMPARE_PROMPT` | Предварително конфигурирано | Промпт за сравнение |
| `COMPARE_RETRIES` | `2` | Опити за повторение |

#### Сесия 05: Оркестрация на много агенти
| Променлива | По подразбиране | Цел |
|------------|-----------------|-----|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Модел на изследователски агент |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Модел на редакторски агент |
| `AGENT_QUESTION` | Предварително конфигурирано | Тестов въпрос |

### Конфигурация за надеждност

| Променлива | По подразбиране | Цел |
|------------|-----------------|-----|
| `SHOW_USAGE` | `1` | Показване на използването на токени |
| `RETRY_ON_FAIL` | `1` | Активиране на логика за повторение |
| `RETRY_BACKOFF` | `1.0` | Забавяне при повторение (секунди) |

## Чести конфигурации

### Настройка за разработка (бърза итерация)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Настройка за продукция (фокус върху качеството)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Настройка за бенчмаркинг
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Специализация за много агенти
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Отдалечена разработка
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Препоръчителни модели

### Според предназначение

**Общо предназначение:**
- `phi-4-mini` - Балансирано качество и скорост

**Бързи отговори:**
- `qwen2.5-0.5b` - Много бърз, подходящ за класификация
- `phi-4-mini` - Бърз с добро качество

**Високо качество:**
- `qwen2.5-7b` - Най-добро качество, по-висока употреба на ресурси
- `phi-4-mini` - Добро качество, по-ниски ресурси

**Генериране на код:**
- `deepseek-coder-1.3b` - Специализиран за код
- `phi-4-mini` - Общопредназначен за кодиране

### Според налични ресурси

**Ниски ресурси (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Средни ресурси (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Високи ресурси (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Разширена конфигурация

### Персонализирани крайни точки

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Температура и семплиране (замяна в кода)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Хибридна настройка на Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Отстраняване на проблеми

### Променливите на средата не са заредени

**Симптоми:**
- Скриптовете използват грешни модели
- Грешки при свързване
- Променливите не са разпознати

**Решения:**
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

### Проблеми със свързването към услугата

**Симптоми:**
- Грешки "Connection refused"
- "Услугата не е налична"
- Грешки при изчакване

**Решения:**
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

### Моделът не е намерен

**Симптоми:**
- Грешки "Model not found"
- "Alias не е разпознат"

**Решения:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Грешки при импортиране

**Симптоми:**
- Грешки "Module not found"

**Решения:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Тестване на конфигурацията

### Проверка на зареждането на средата

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

### Тест за връзка с Foundry Local

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

## Най-добри практики за сигурност

### 1. Никога не качвайте тайни

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Използвайте отделни .env файлове

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Редовно сменяйте API ключовете

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Използвайте конфигурация, специфична за средата

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Документация за SDK

- **Основно хранилище**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API документация**: Проверете хранилището на SDK за най-новата версия

## Допълнителни ресурси

- `QUICK_START.md` - Ръководство за започване
- `Workshop/samples/*/README.md` - Ръководства, специфични за примерите

---

**Последно обновяване**: 2025-01-08  
**Версия**: 2.0  
**SDK**: Foundry Local Python SDK (най-новата)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->