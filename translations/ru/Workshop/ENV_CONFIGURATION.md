<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T21:31:19+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "ru"
}
-->
# Руководство по настройке окружения

## Обзор

Примеры из Workshop используют переменные окружения для настройки, которые централизованно хранятся в файле `.env` в корневой директории репозитория. Это позволяет легко настраивать параметры без изменения кода.

## Быстрый старт

### 1. Проверьте требования

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Настройте окружение

Файл `.env` уже настроен с разумными значениями по умолчанию. Большинству пользователей не потребуется ничего менять.

**Опционально**: Ознакомьтесь с настройками и при необходимости измените их:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Примените настройки

**Для Python-скриптов:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Для ноутбуков:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Справочник переменных окружения

### Основные настройки

| Переменная | Значение по умолчанию | Описание |
|------------|------------------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Модель по умолчанию для примеров |
| `FOUNDRY_LOCAL_ENDPOINT` | (пусто) | Переопределение конечной точки сервиса |
| `PYTHONPATH` | Пути Workshop | Путь поиска модулей Python |

**Когда нужно установить FOUNDRY_LOCAL_ENDPOINT:**
- Удалённый экземпляр Foundry Local
- Настройка пользовательского порта
- Разделение разработки и производства

**Пример:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Переменные для конкретных сессий

#### Сессия 02: RAG Pipeline
| Переменная | Значение по умолчанию | Назначение |
|------------|------------------------|------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модель для создания эмбеддингов |
| `RAG_QUESTION` | Преднастроено | Тестовый вопрос |

#### Сессия 03: Бенчмаркинг
| Переменная | Значение по умолчанию | Назначение |
|------------|------------------------|------------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Модели для бенчмаркинга |
| `BENCH_ROUNDS` | `3` | Количество итераций на модель |
| `BENCH_PROMPT` | Преднастроено | Тестовый запрос |
| `BENCH_STREAM` | `0` | Измерение задержки первого токена |

#### Сессия 04: Сравнение моделей
| Переменная | Значение по умолчанию | Назначение |
|------------|------------------------|------------|
| `SLM_ALIAS` | `phi-4-mini` | Малая языковая модель |
| `LLM_ALIAS` | `qwen2.5-7b` | Большая языковая модель |
| `COMPARE_PROMPT` | Преднастроено | Запрос для сравнения |
| `COMPARE_RETRIES` | `2` | Количество попыток повторного выполнения |

#### Сессия 05: Оркестрация мультиагентов
| Переменная | Значение по умолчанию | Назначение |
|------------|------------------------|------------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Модель агента-исследователя |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Модель агента-редактора |
| `AGENT_QUESTION` | Преднастроено | Тестовый вопрос |

### Настройки надёжности

| Переменная | Значение по умолчанию | Назначение |
|------------|------------------------|------------|
| `SHOW_USAGE` | `1` | Печать использования токенов |
| `RETRY_ON_FAIL` | `1` | Включить логику повторных попыток |
| `RETRY_BACKOFF` | `1.0` | Задержка перед повторной попыткой (в секундах) |

## Общие настройки

### Настройка для разработки (быстрая итерация)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Настройка для производства (ориентация на качество)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Настройка для бенчмаркинга
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Специализация мультиагентов
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Удалённая разработка
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Рекомендуемые модели

### По назначению

**Общее назначение:**
- `phi-4-mini` - Сбалансированное качество и скорость

**Быстрые ответы:**
- `qwen2.5-0.5b` - Очень быстро, подходит для классификации
- `phi-4-mini` - Быстрое выполнение с хорошим качеством

**Высокое качество:**
- `qwen2.5-7b` - Лучшее качество, больше ресурсов
- `phi-4-mini` - Хорошее качество, меньше ресурсов

**Генерация кода:**
- `deepseek-coder-1.3b` - Специализированная для кода
- `phi-4-mini` - Универсальная для кодирования

### По доступным ресурсам

**Малые ресурсы (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Средние ресурсы (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Большие ресурсы (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Расширенные настройки

### Пользовательские конечные точки

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Температура и выборка (переопределение в коде)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Гибридная настройка Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Устранение неполадок

### Переменные окружения не загружаются

**Симптомы:**
- Скрипты используют неправильные модели
- Ошибки подключения
- Переменные не распознаются

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

### Проблемы с подключением к сервису

**Симптомы:**
- Ошибки "Connection refused"
- "Сервис недоступен"
- Ошибки тайм-аута

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

### Модель не найдена

**Симптомы:**
- Ошибки "Model not found"
- "Alias не распознан"

**Решения:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Ошибки импорта

**Симптомы:**
- Ошибки "Module not found"

**Решения:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Тестирование конфигурации

### Проверка загрузки окружения

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

### Тестирование подключения к Foundry Local

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

## Рекомендации по безопасности

### 1. Никогда не коммитите секреты

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Используйте отдельные файлы .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Регулярно меняйте API-ключи

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Используйте конфигурацию для конкретного окружения

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Документация SDK

- **Основной репозиторий**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Документация API**: Проверьте репозиторий SDK для актуальной информации

## Дополнительные ресурсы

- `QUICK_START.md` - Руководство по началу работы
- `Workshop/samples/*/README.md` - Руководства для конкретных примеров

---

**Последнее обновление**: 2025-01-08  
**Версия**: 2.0  
**SDK**: Foundry Local Python SDK (последняя версия)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->