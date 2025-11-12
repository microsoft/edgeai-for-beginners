<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-12T00:47:47+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "uk"
}
-->
# Сесія 1: Початок роботи з Foundry Local

## Анотація

Дізнайтеся, як встановити, налаштувати та запустити ваші перші AI моделі за допомогою Microsoft Foundry Local. Ця практична сесія пропонує покрокове введення в локальне інференсування, від встановлення до створення вашого першого чат-додатку з використанням моделей, таких як Phi-4, Qwen і DeepSeek.

## Цілі навчання

До кінця цієї сесії ви зможете:

- **Встановити та налаштувати**: Налаштувати Foundry Local з перевіркою правильності встановлення
- **Опанувати CLI операції**: Використовувати Foundry Local CLI для управління моделями та їх розгортання
- **Запустити вашу першу модель**: Успішно розгорнути та взаємодіяти з локальною AI моделлю
- **Створити чат-додаток**: Розробити базовий чат-додаток за допомогою Foundry Local Python SDK
- **Зрозуміти локальний AI**: Оволодіти основами локального інференсування та управління моделями

## Попередні вимоги

### Системні вимоги

- **Windows**: Windows 11 (22H2 або новіше) АБО **macOS**: macOS 11+ (обмежена підтримка)
- **ОЗП**: мінімум 8 ГБ, рекомендовано 16 ГБ+
- **Пам'ять**: мінімум 10 ГБ вільного місця для моделей
- **Python**: встановлений Python 3.10 або новіший
- **Доступ адміністратора**: права адміністратора для встановлення

### Середовище розробки

- Visual Studio Code з розширенням Python (рекомендовано)
- Доступ до командного рядка (PowerShell на Windows, Terminal на macOS)
- Git для клонування репозиторіїв (опціонально)

## Хід воркшопу (30 хвилин)

### Крок 1: Встановлення Foundry Local (5 хвилин)

#### Встановлення на Windows

Встановіть Foundry Local за допомогою менеджера пакетів Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Альтернатива: Завантажте безпосередньо з [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Встановлення на macOS (обмежена підтримка)

> [!NOTE] 
> Підтримка macOS наразі в режимі попереднього перегляду. Перевірте офіційну документацію для отримання актуальної інформації.

Якщо доступно, встановіть за допомогою Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Альтернатива для користувачів macOS:**
- Використовуйте Windows 11 VM (Parallels/UTM) і дотримуйтесь інструкцій для Windows
- Запустіть через контейнер, якщо доступно, і налаштуйте `FOUNDRY_LOCAL_ENDPOINT`

### Крок 2: Перевірка встановлення (3 хвилини)

Після встановлення перезапустіть ваш термінал і перевірте, чи працює Foundry Local:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Очікуваний результат має показати інформацію про версію та доступні команди.

### Крок 3: Налаштування середовища Python (5 хвилин)

Створіть спеціальне середовище Python для цього воркшопу:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Крок 4: Запуск вашої першої моделі (7 хвилин)

Тепер запустимо нашу першу AI модель локально!

#### Початок з Phi-4 Mini (рекомендована перша модель)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ця команда завантажує модель (вперше) і автоматично запускає службу Foundry Local.

#### Перевірка запущених процесів

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Спробуйте інші моделі

Після запуску phi-4-mini спробуйте інші моделі:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Крок 5: Створення вашого першого чат-додатку (10 хвилин)

Тепер створимо Python-додаток, який використовує моделі, які ми щойно запустили.

#### Створення скрипта чату

Створіть новий файл під назвою `my_first_chat.py` (або використовуйте наданий зразок):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Пов’язані приклади**: Для більш просунутого використання дивіться:
>
> - **Python-зразок**: `Workshop/samples/session01/chat_bootstrap.py` - включає потокові відповіді та обробку помилок
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - інтерактивна версія з детальними поясненнями

#### Тестування вашого чат-додатку

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Альтернатива: Використовуйте надані зразки безпосередньо

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Або досліджуйте інтерактивний ноутбук
Відкрийте Workshop/notebooks/session01_chat_bootstrap.ipynb у VS Code

Спробуйте ці приклади розмов:

- "Що таке Microsoft Foundry Local?"
- "Перелічіть 3 переваги запуску AI моделей локально"
- "Допоможіть мені зрозуміти edge AI"

## Що ви досягли

Вітаємо! Ви успішно:

1. ✅ **Встановили Foundry Local** і перевірили його роботу
2. ✅ **Запустили вашу першу AI модель** (phi-4-mini) локально
3. ✅ **Протестували різні моделі** через командний рядок
4. ✅ **Створили чат-додаток**, який підключається до вашого локального AI
5. ✅ **Відчули локальне інференсування AI** без залежності від хмари

## Розуміння того, що сталося

### Локальне інференсування AI

- Ваші AI моделі працюють повністю на вашому комп'ютері
- Дані не передаються в хмару
- Відповіді генеруються локально за допомогою вашого CPU/GPU
- Конфіденційність і безпека зберігаються

### Управління моделями

- `foundry model run` завантажує та запускає моделі
- **FoundryLocalManager SDK** автоматично керує запуском служби та завантаженням моделей
- Моделі кешуються локально для майбутнього використання
- Можна завантажити кілька моделей, але зазвичай працює одна за раз
- Служба автоматично керує життєвим циклом моделі

### SDK проти CLI підходів

- **CLI підхід**: Ручне управління моделями за допомогою `foundry model run <model>`
- **SDK підхід**: Автоматичне управління службою + моделями за допомогою `FoundryLocalManager(alias)`
- **Рекомендація**: Використовуйте SDK для додатків, CLI для тестування та дослідження

## Довідник основних команд

### Основні CLI команди

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Рекомендації щодо моделей

- **phi-4-mini**: Найкраща стартова модель - швидка, легка, гарна якість
- **qwen2.5-0.5b**: Найшвидше інференсування, мінімальне використання пам'яті
- **gpt-oss-20b**: Вищої якості відповіді, потребує більше ресурсів
- **deepseek-coder-1.3b**: Оптимізована для програмування та завдань з кодом

## Вирішення проблем

### "Команда Foundry не знайдена"

**Рішення:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Модель не вдалося завантажити"

**Рішення:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "З'єднання відхилено на localhost"

**Рішення:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Наступні кроки

### Негайні дії

1. **Експериментуйте** з різними моделями та запитами
2. **Модифікуйте** ваш чат-додаток, щоб спробувати різні моделі
3. **Створіть** власні запити та протестуйте відповіді
4. **Досліджуйте** Сесію 2: Створення RAG-додатків

### Шлях до поглибленого навчання

1. **Сесія 2**: Створення AI рішень з RAG (генерація з розширеним пошуком)
2. **Сесія 3**: Порівняння різних моделей з відкритим кодом
3. **Сесія 4**: Робота з передовими моделями
4. **Сесія 5**: Створення багатокомпонентних AI систем

## Змінні середовища (опціонально)

Для більш просунутого використання ви можете встановити ці змінні середовища:

| Змінна | Призначення | Приклад |
|--------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Модель за замовчуванням | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Перевизначення URL кінцевої точки | `http://localhost:5273/v1` |

Створіть файл `.env` у вашій директорії проекту:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Додаткові ресурси

### Документація

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Зразки коду

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Повний чат-додаток з потоковими відповідями
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Інтерактивний підручник  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - Інтеграція OpenAI SDK
- [Module08 Sample 03](../Module08/samples/03/README.md) - Відкриття моделей та тестування продуктивності

### Спільнота

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Тривалість сесії**: 30 хвилин практики + 15 хвилин запитань та відповідей  
**Рівень складності**: Початковий  
**Попередні вимоги**: Windows 11/macOS 11+, Python 3.10+, доступ адміністратора

## Приклад сценарію воркшопу

### Контекст реального світу

**Сценарій**: Команда IT в підприємстві має оцінити інференсування AI на пристрої для обробки конфіденційних відгуків співробітників без передачі даних до зовнішніх сервісів.

**Ваша мета**: Продемонструвати, що локальні AI моделі можуть забезпечити якісні відповіді з затримкою менше секунди, зберігаючи повну конфіденційність даних.

### Тестові запити

Використовуйте ці запити для перевірки вашої конфігурації:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Критерії успіху

- ✅ Усі запити отримують відповіді менш ніж за 2 секунди
- ✅ Жодні дані не залишають ваш локальний комп'ютер
- ✅ Відповіді є релевантними та корисними
- ✅ Ваш чат-додаток працює безперебійно

Ця перевірка гарантує, що ваша конфігурація Foundry Local готова до просунутих воркшопів у Сесіях 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->