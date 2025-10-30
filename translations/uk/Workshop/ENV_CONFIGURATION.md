<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T23:41:11+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "uk"
}
-->
# Посібник з налаштування середовища

## Огляд

Зразки для майстер-класу використовують змінні середовища для налаштування, які централізовано зберігаються у файлі `.env` в кореневій папці репозиторію. Це дозволяє легко налаштовувати параметри без внесення змін у код.

## Швидкий старт

### 1. Перевірте передумови

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Налаштуйте середовище

Файл `.env` вже налаштований з розумними значеннями за замовчуванням. Більшість користувачів не потребуватимуть змін.

**Опціонально**: Перегляньте та налаштуйте параметри:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Застосуйте налаштування

**Для скриптів Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Для ноутбуків:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Довідник змінних середовища

### Основна конфігурація

| Змінна | За замовчуванням | Опис |
|--------|------------------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Модель за замовчуванням для зразків |
| `FOUNDRY_LOCAL_ENDPOINT` | (порожньо) | Перевизначення кінцевої точки сервісу |
| `PYTHONPATH` | Шляхи майстер-класу | Шлях пошуку модулів Python |

**Коли встановлювати FOUNDRY_LOCAL_ENDPOINT:**
- Віддалений екземпляр Foundry Local
- Налаштування користувацького порту
- Розділення середовищ розробки/продукції

**Приклад:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Змінні для конкретних сесій

#### Сесія 02: RAG Pipeline
| Змінна | За замовчуванням | Призначення |
|--------|------------------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модель для вбудовування |
| `RAG_QUESTION` | Попередньо налаштовано | Тестове питання |

#### Сесія 03: Бенчмаркінг
| Змінна | За замовчуванням | Призначення |
|--------|------------------|-------------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Моделі для бенчмаркінгу |
| `BENCH_ROUNDS` | `3` | Кількість ітерацій на модель |
| `BENCH_PROMPT` | Попередньо налаштовано | Тестовий запит |
| `BENCH_STREAM` | `0` | Вимірювання затримки першого токена |

#### Сесія 04: Порівняння моделей
| Змінна | За замовчуванням | Призначення |
|--------|------------------|-------------|
| `SLM_ALIAS` | `phi-4-mini` | Мала мовна модель |
| `LLM_ALIAS` | `qwen2.5-7b` | Велика мовна модель |
| `COMPARE_PROMPT` | Попередньо налаштовано | Запит для порівняння |
| `COMPARE_RETRIES` | `2` | Кількість спроб повтору |

#### Сесія 05: Оркестрація багатьох агентів
| Змінна | За замовчуванням | Призначення |
|--------|------------------|-------------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Модель агента-дослідника |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Модель агента-редактора |
| `AGENT_QUESTION` | Попередньо налаштовано | Тестове питання |

### Конфігурація надійності

| Змінна | За замовчуванням | Призначення |
|--------|------------------|-------------|
| `SHOW_USAGE` | `1` | Виведення використання токенів |
| `RETRY_ON_FAIL` | `1` | Увімкнення логіки повтору |
| `RETRY_BACKOFF` | `1.0` | Затримка перед повтором (секунди) |

## Загальні налаштування

### Налаштування для розробки (швидка ітерація)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Налаштування для продукції (фокус на якості)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Налаштування для бенчмаркінгу
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Спеціалізація багатьох агентів
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Віддалена розробка
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Рекомендовані моделі

### За призначенням

**Загального призначення:**
- `phi-4-mini` - Збалансована якість і швидкість

**Швидкі відповіді:**
- `qwen2.5-0.5b` - Дуже швидка, підходить для класифікації
- `phi-4-mini` - Швидка з гарною якістю

**Висока якість:**
- `qwen2.5-7b` - Найкраща якість, більше ресурсів
- `phi-4-mini` - Гарна якість, менше ресурсів

**Генерація коду:**
- `deepseek-coder-1.3b` - Спеціалізована для коду
- `phi-4-mini` - Загального призначення для кодування

### За доступністю ресурсів

**Малі ресурси (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Середні ресурси (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Великі ресурси (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Розширене налаштування

### Користувацькі кінцеві точки

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Температура та семплінг (перевизначення в коді)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Гібридне налаштування Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Вирішення проблем

### Змінні середовища не завантажуються

**Симптоми:**
- Скрипти використовують неправильні моделі
- Помилки з'єднання
- Змінні не розпізнаються

**Рішення:**
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

### Проблеми з підключенням до сервісу

**Симптоми:**
- Помилки "З'єднання відхилено"
- "Сервіс недоступний"
- Помилки тайм-ауту

**Рішення:**
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

### Модель не знайдена

**Симптоми:**
- Помилки "Модель не знайдена"
- "Псевдонім не розпізнано"

**Рішення:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Помилки імпорту

**Симптоми:**
- Помилки "Модуль не знайдено"

**Рішення:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Тестування конфігурації

### Перевірка завантаження середовища

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

### Тестування підключення до Foundry Local

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

## Найкращі практики безпеки

### 1. Ніколи не комітуйте секрети

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Використовуйте окремі файли .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Ротуйте API ключі

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Використовуйте конфігурацію для конкретного середовища

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Документація SDK

- **Основний репозиторій**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Документація API**: Перевірте репозиторій SDK для останніх оновлень

## Додаткові ресурси

- `QUICK_START.md` - Посібник для початку роботи
- `SDK_MIGRATION_NOTES.md` - Деталі оновлення SDK
- `Workshop/samples/*/README.md` - Посібники для конкретних зразків

---

**Останнє оновлення**: 2025-01-08  
**Версія**: 2.0  
**SDK**: Foundry Local Python SDK (остання версія)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.