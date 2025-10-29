<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T23:15:01+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "bg"
}
-->
# Сесия 1: Започване с Foundry Local

## Резюме

Започнете своето пътешествие с Foundry Local, като го инсталирате и конфигурирате на Windows 11. Научете как да настроите CLI, да активирате хардуерно ускорение и да кеширате модели за бързо локално изпълнение. Тази практическа сесия показва как да стартирате модели като Phi, Qwen, DeepSeek и GPT-OSS-20B, използвайки възпроизводими CLI команди.

## Цели на обучението

До края на тази сесия ще можете:

- **Инсталиране и конфигуриране**: Настройка на Foundry Local на Windows 11 с оптимални настройки за производителност
- **Овладяване на CLI операции**: Използване на Foundry Local CLI за управление и внедряване на модели
- **Активиране на хардуерно ускорение**: Конфигуриране на GPU ускорение с ONNXRuntime или WebGPU
- **Внедряване на множество модели**: Стартиране на phi-4, GPT-OSS-20B, Qwen и DeepSeek модели локално
- **Създаване на първо приложение**: Адаптиране на съществуващи примери за използване на Foundry Local Python SDK

# Тест на модела (неинтерактивен единичен въпрос)
foundry model run phi-4-mini --prompt "Здравей, представи се"

- Windows 11 (22H2 или по-нова версия)
# Списък на наличните модели в каталога (заредените модели се появяват след стартиране)
foundry model list
## NOTE: В момента няма специален флаг `--running`; за да видите кои са заредени, започнете чат или проверете логовете на услугата.
- Инсталиран Python 3.10+
- Visual Studio Code с разширение за Python
- Администраторски права за инсталация

### (По избор) Променливи на средата

Създайте `.env` (или задайте в shell), за да направите скриптовете преносими:
# Сравнение на отговори (неинтерактивно)
foundry model run gpt-oss-20b --prompt "Обясни edge AI с прости думи"
| Променлива | Цел | Пример |
|------------|-----|--------|
| `FOUNDRY_LOCAL_ALIAS` | Предпочитан псевдоним на модела (каталогът автоматично избира най-добрия вариант) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Замяна на endpoint (иначе автоматично от мениджъра) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Активиране на демонстрация със стрийминг | `true` |

> Ако `FOUNDRY_LOCAL_ENDPOINT=auto` (или не е зададен), го извеждаме от SDK мениджъра.

## Демонстрационен поток (30 минути)

### 1. Инсталиране на Foundry Local и проверка на CLI настройката (10 минути)

# Списък на кешираните модели
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Предварителен преглед / Ако е поддържан)**

Ако е предоставен роден пакет за macOS (проверете официалната документация за най-новото):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ако родните бинарни файлове за macOS все още не са налични, можете да:
1. Използвате Windows 11 ARM/Intel VM (Parallels / UTM) и да следвате стъпките за Windows.
2. Стартирате модели чрез контейнер (ако е публикуван образ на контейнер) и да зададете `FOUNDRY_LOCAL_ENDPOINT` към изложения порт.

**Създаване на Python виртуална среда (Мултиплатформено)**

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

Актуализирайте pip и инсталирайте основните зависимости:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Стъпка 1.2: Проверка на инсталацията

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Стъпка 1.3: Конфигуриране на средата

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Препоръчително)

Вместо ръчно стартиране на услугата и модели, **Foundry Local Python SDK** може да автоматизира всичко:

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

Ако предпочитате явен контрол, все още можете да използвате CLI + OpenAI клиент, както е показано по-късно.

### 2. Стартиране на модели локално чрез CLI (10 минути)

#### Стъпка 3.1: Внедряване на Phi-4 модел

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Стъпка 3.2: Внедряване на GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Стъпка 3.3: Зареждане на допълнителни модели

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Начален проект: Адаптиране на 01-run-phi за Foundry Local (5 минути)

#### Стъпка 4.1: Създаване на основно чат приложение

Създайте `samples/01-foundry-quickstart/chat_quickstart.py` (актуализирано за използване на мениджъра, ако е наличен):

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

#### Стъпка 4.2: Тест на приложението

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Основни концепции, които се разглеждат

### 1. Архитектура на Foundry Local

- **Локален двигател за изпълнение**: Стартира модели изцяло на вашето устройство
- **Съвместимост със OpenAI SDK**: Безпроблемна интеграция със съществуващ OpenAI код
- **Управление на модели**: Изтегляне, кеширане и ефективно стартиране на множество модели
- **Оптимизация на хардуера**: Използване на GPU, NPU и CPU ускорение

### 2. Референция на CLI команди

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Интеграция на Python SDK

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

## Отстраняване на често срещани проблеми

### Проблем 1: "Foundry command not found"

**Решение:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Проблем 2: "Model failed to load"

**Решение:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Проблем 3: "Connection refused on localhost:5273"

**Решение:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Съвети за оптимизация на производителността

### 1. Стратегия за избор на модел

- **Phi-4-mini**: Най-добър за общи задачи, ниска употреба на памет
- **Qwen2.5-0.5b**: Най-бързо изпълнение, минимални ресурси
- **GPT-OSS-20B**: Най-високо качество, изисква повече ресурси
- **DeepSeek-Coder**: Оптимизиран за задачи, свързани с програмиране

### 2. Оптимизация на хардуера

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Мониторинг на производителността

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Допълнителни подобрения

| Подобрение | Какво | Как |
|------------|-------|-----|
| Споделени утилити | Премахване на дублираща логика за клиент/автоматизация | Използвайте `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Видимост на употребата на токени | Ранно обучение за разходи/ефективност | Задайте `SHOW_USAGE=1`, за да отпечатате токени за въпрос/отговор/общо |
| Детерминистични сравнения | Стабилно тестване и проверки за регресия | Използвайте `temperature=0`, `top_p=1`, последователен текст на въпроса |
| Латентност на първия токен | Метрика за възприемана отзивчивост | Адаптирайте скрипт за тестване със стрийминг (`BENCH_STREAM=1`) |
| Повторен опит при временни грешки | Устойчиви демонстрации при студен старт | `RETRY_ON_FAIL=1` (по подразбиране) и настройте `RETRY_BACKOFF` |
| Тестове за проверка | Бърза проверка на ключови потоци | Стартирайте `python Workshop/tests/smoke.py` преди работилница |
| Профили на псевдоними на модели | Бързо превключване на набор от модели между машини | Поддържайте `.env` с `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Ефективност на кеширане | Избягване на повторни загрявания при многократни стартирания | Утилити за кеширане на мениджъри; повторно използване в скриптове/тетрадки |
| Загряване при първо стартиране | Намаляване на латентността при първо стартиране | Стартирайте малък въпрос след създаване на `FoundryLocalManager`

Пример за детерминистична стабилна база (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Трябва да видите подобен изход и идентични броя на токените при второто стартиране, потвърждавайки детерминизма.

## Следващи стъпки

След завършване на тази сесия:

1. **Разгледайте Сесия 2**: Създаване на AI решения с Azure AI Foundry RAG
2. **Опитайте различни модели**: Експериментирайте с Qwen, DeepSeek и други семейства модели
3. **Оптимизирайте производителността**: Фина настройка на параметрите за вашия специфичен хардуер
4. **Създайте персонализирани приложения**: Използвайте Foundry Local SDK във вашите собствени проекти

## Допълнителни ресурси

### Документация
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Примерен код
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Общност
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Продължителност на сесията**: 30 минути практическа работа + 15 минути Q&A  
**Ниво на трудност**: Начинаещ  
**Предварителни изисквания**: Windows 11, Python 3.10+, Администраторски достъп

## Примерен сценарий и картографиране на работилницата

| Скрипт / Тетрадка на работилницата | Сценарий | Цел | Примерен вход | Необходим набор от данни |
|------------------------------------|----------|-----|---------------|--------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Вътрешен IT екип, оценяващ локално изпълнение за портал за оценка на поверителност | Доказване, че локалният SLM отговаря с подсекундна латентност на стандартни въпроси | "Избройте две предимства на локалното изпълнение." | Няма (единичен въпрос) |
| Кодов блок за адаптация на Quickstart | Разработчик, мигриращ съществуващ OpenAI скрипт към Foundry Local | Показване на съвместимост | "Дайте две предимства на локалното изпълнение." | Само вътрешен въпрос |

### Разказ за сценария
Екипът по сигурност и съответствие трябва да валидира дали чувствителни прототипни данни могат да бъдат обработени локално. Те стартират скрипта за автоматизация с няколко въпроса (поверителност, латентност, разходи), използвайки детерминистичен режим temperature=0, за да съберат базови изходи за по-късно сравнение (Сесия 3 тестване и Сесия 4 контраст между SLM и LLM).

### Минимален JSON набор от въпроси (по избор)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Използвайте този списък, за да създадете възпроизводим цикъл за оценка или за да подготвите бъдеща рамка за тестване на регресия.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.