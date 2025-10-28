<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:29:10+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "uk"
}
-->
# Сесія 1: Початок роботи з Foundry Local

## Анотація

Розпочніть свою подорож з Foundry Local, встановивши та налаштувавши його на Windows 11. Дізнайтеся, як налаштувати CLI, увімкнути апаратне прискорення та кешувати моделі для швидкого локального виконання. Ця практична сесія демонструє запуск моделей, таких як Phi, Qwen, DeepSeek і GPT-OSS-20B, за допомогою відтворюваних команд CLI.

## Навчальні цілі

До кінця цієї сесії ви зможете:

- **Встановити та налаштувати**: Налаштувати Foundry Local на Windows 11 з оптимальними параметрами продуктивності
- **Опанувати операції CLI**: Використовувати Foundry Local CLI для управління моделями та їх розгортання
- **Увімкнути апаратне прискорення**: Налаштувати прискорення GPU за допомогою ONNXRuntime або WebGPU
- **Розгорнути кілька моделей**: Запустити моделі phi-4, GPT-OSS-20B, Qwen і DeepSeek локально
- **Створити свій перший додаток**: Адаптувати існуючі приклади для використання Foundry Local Python SDK

# Тестування моделі (неінтерактивний одиночний запит)
foundry model run phi-4-mini --prompt "Привіт, представ себе"

- Windows 11 (22H2 або новіше)
# Список доступних моделей каталогу (завантажені моделі з'являються після запуску)
foundry model list
## NOTE: Наразі немає спеціального прапорця `--running`; щоб побачити, які моделі завантажені, почніть чат або перевірте журнали сервісу.
- Встановлений Python 3.10+
- Visual Studio Code з розширенням Python
- Адміністраторські права для встановлення

### (Необов'язково) Змінні середовища

Створіть `.env` (або налаштуйте в оболонці), щоб зробити скрипти портативними:
# Порівняння відповідей (неінтерактивне)
foundry model run gpt-oss-20b --prompt "Поясни edge AI простими словами"
| Змінна | Призначення | Приклад |
|--------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Бажаний псевдонім моделі (каталог автоматично вибирає найкращий варіант) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Перевизначення кінцевої точки (інакше автоматично з менеджера) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Увімкнення демонстрації потокової передачі | `true` |

> Якщо `FOUNDRY_LOCAL_ENDPOINT=auto` (або не встановлено), ми отримуємо його з менеджера SDK.

## Демонстраційний процес (30 хвилин)

### 1. Встановлення Foundry Local та перевірка налаштування CLI (10 хвилин)

# Список кешованих моделей
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Попередній перегляд / Якщо підтримується)**

Якщо надано рідний пакет для macOS (перевірте офіційну документацію для останніх версій):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Якщо рідні двійкові файли для macOS ще недоступні, ви все одно можете: 
1. Використовувати Windows 11 ARM/Intel VM (Parallels / UTM) і виконувати кроки для Windows. 
2. Запускати моделі через контейнер (якщо опубліковано образ контейнера) і встановити `FOUNDRY_LOCAL_ENDPOINT` на відкритий порт. 

**Створення віртуального середовища Python (Кросплатформне)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Оновіть pip і встановіть основні залежності:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Крок 1.2: Перевірка встановлення

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Крок 1.3: Налаштування середовища

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Рекомендовано)

Замість ручного запуску сервісу та моделей, **Foundry Local Python SDK** може автоматично налаштувати все:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Якщо ви віддаєте перевагу явному контролю, ви все ще можете використовувати CLI + OpenAI клієнт, як показано далі.

### 2. Запуск моделей локально через CLI (10 хвилин)

#### Крок 3.1: Розгортання моделі Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Крок 3.2: Розгортання GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Крок 3.3: Завантаження додаткових моделей

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Стартовий проект: Адаптація 01-run-phi для Foundry Local (5 хвилин)

#### Крок 4.1: Створення базового чат-додатку

Створіть `samples/01-foundry-quickstart/chat_quickstart.py` (оновлено для використання менеджера, якщо доступно):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Крок 4.2: Тестування додатку

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Основні концепції, які розглядаються

### 1. Архітектура Foundry Local

- **Локальний двигун інференції**: Запускає моделі повністю на вашому пристрої
- **Сумісність з OpenAI SDK**: Безшовна інтеграція з існуючим кодом OpenAI
- **Управління моделями**: Завантаження, кешування та ефективний запуск кількох моделей
- **Оптимізація апаратного забезпечення**: Використання прискорення GPU, NPU та CPU

### 2. Довідник команд CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Інтеграція Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Вирішення поширених проблем

### Проблема 1: "Команда Foundry не знайдена"

**Рішення:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Проблема 2: "Модель не вдалося завантажити"

**Рішення:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Проблема 3: "Відмова у з'єднанні на localhost:5273"

**Рішення:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Поради щодо оптимізації продуктивності

### 1. Стратегія вибору моделі

- **Phi-4-mini**: Найкраще для загальних завдань, менше використання пам'яті
- **Qwen2.5-0.5b**: Найшвидша інференція, мінімальні ресурси
- **GPT-OSS-20B**: Найвища якість, потребує більше ресурсів
- **DeepSeek-Coder**: Оптимізовано для програмування

### 2. Оптимізація апаратного забезпечення

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Моніторинг продуктивності

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Додаткові покращення

| Покращення | Що | Як |
|------------|-----|----|
| Спільні утиліти | Видалення дублюючої логіки клієнта/завантаження | Використовуйте `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Видимість використання токенів | Навчання мисленню про витрати/ефективність | Встановіть `SHOW_USAGE=1`, щоб друкувати токени запиту/відповіді/загальні |
| Детерміністичні порівняння | Стабільне тестування продуктивності та перевірка регресії | Використовуйте `temperature=0`, `top_p=1`, стабільний текст запиту |
| Затримка першого токена | Метрика сприйнятої швидкодії | Адаптуйте скрипт тестування з потоковою передачею (`BENCH_STREAM=1`) |
| Повтор при тимчасових помилках | Стійкі демонстрації при холодному старті | `RETRY_ON_FAIL=1` (за замовчуванням) та налаштуйте `RETRY_BACKOFF` |
| Тестування працездатності | Швидка перевірка основних функцій | Запустіть `python Workshop/tests/smoke.py` перед воркшопом |
| Профілі псевдонімів моделей | Швидке переключення набору моделей між машинами | Підтримуйте `.env` з `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Ефективність кешування | Уникайте повторних розігрівів у багатозразковому запуску | Утиліти кешування менеджерів; повторне використання між скриптами/ноутбуками |
| Розігрів першого запуску | Зменшення пікових затримок p95 | Виконайте невеликий запит після створення `FoundryLocalManager`

Приклад детерміністичного теплого запуску (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Ви повинні побачити схожий результат і однакову кількість токенів при другому запуску, що підтверджує детермінізм.

## Наступні кроки

Після завершення цієї сесії:

1. **Досліджуйте Сесію 2**: Створення AI-рішень з Azure AI Foundry RAG
2. **Спробуйте різні моделі**: Експериментуйте з Qwen, DeepSeek та іншими сімействами моделей
3. **Оптимізуйте продуктивність**: Тонке налаштування параметрів для вашого конкретного апаратного забезпечення
4. **Створюйте власні додатки**: Використовуйте Foundry Local SDK у своїх проектах

## Додаткові ресурси

### Документація
- [Довідник Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Посібник з встановлення Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Каталог моделей](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Зразки коду
- [Модуль08 Зразок 01](./samples/01/README.md) - Швидкий старт REST Chat
- [Модуль08 Зразок 02](./samples/02/README.md) - Інтеграція OpenAI SDK
- [Модуль08 Зразок 03](./samples/03/README.md) - Відкриття моделей та тестування продуктивності

### Спільнота
- [Обговорення Foundry Local на GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Спільнота Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Тривалість сесії**: 30 хвилин практики + 15 хвилин запитань та відповідей  
**Рівень складності**: Початковий  
**Попередні вимоги**: Windows 11, Python 3.10+, доступ адміністратора  

## Зразковий сценарій та відповідність воркшопу

| Скрипт / Ноутбук воркшопу | Сценарій | Мета | Приклад введення | Потрібний набір даних |
|---------------------------|----------|------|------------------|-----------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Внутрішня IT-команда оцінює інференцію на пристрої для порталу оцінки конфіденційності | Довести, що локальний SLM відповідає з затримкою менше секунди на стандартні запити | "Назвіть дві переваги локальної інференції." | Немає (одиночний запит) |
| Код адаптації швидкого старту | Розробник переносить існуючий скрипт OpenAI до Foundry Local | Показати сумісність "з коробки" | "Назвіть дві переваги локальної інференції." | Лише вбудований запит |

### Опис сценарію
Група з безпеки та відповідності повинна перевірити, чи можна обробляти конфіденційні дані прототипу локально. Вони запускають скрипт завантаження з кількома запитами (конфіденційність, затримка, вартість) у детерміністичному режимі temperature=0, щоб зафіксувати базові результати для подальшого порівняння (тестування продуктивності в Сесії 3 та контраст SLM vs LLM у Сесії 4).

### Мінімальний набір запитів JSON (необов'язково)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Використовуйте цей список для створення відтворюваного циклу оцінки або для підготовки майбутнього тестового набору регресії.

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.