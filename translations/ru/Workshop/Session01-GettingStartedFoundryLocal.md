<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T20:14:14+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ru"
}
-->
# Сессия 1: Начало работы с Foundry Local

## Аннотация

Начните свое знакомство с Foundry Local, установив и настроив его на Windows 11. Узнайте, как настроить CLI, включить аппаратное ускорение и кэшировать модели для быстрого локального вывода. В этой практической сессии вы научитесь запускать модели, такие как Phi, Qwen, DeepSeek и GPT-OSS-20B, используя воспроизводимые команды CLI.

## Цели обучения

К концу этой сессии вы сможете:

- **Установить и настроить**: Установить Foundry Local на Windows 11 с оптимальными настройками производительности
- **Освоить работу с CLI**: Использовать Foundry Local CLI для управления и развертывания моделей
- **Включить аппаратное ускорение**: Настроить ускорение GPU с помощью ONNXRuntime или WebGPU
- **Развернуть несколько моделей**: Локально запустить модели phi-4, GPT-OSS-20B, Qwen и DeepSeek
- **Создать свое первое приложение**: Адаптировать существующие примеры для использования Foundry Local Python SDK

# Тестирование модели (неинтерактивный одиночный запрос)
foundry model run phi-4-mini --prompt "Привет, представься"

- Windows 11 (22H2 или новее)
# Список доступных моделей каталога (загруженные модели появляются после запуска)
foundry model list
## NOTE: В настоящее время нет специального флага `--running`; чтобы увидеть загруженные модели, начните чат или проверьте журналы службы.
- Установлен Python 3.10+
- Visual Studio Code с расширением Python
- Администраторские права для установки

### (Необязательно) Переменные окружения

Создайте `.env` (или задайте в оболочке), чтобы сделать скрипты переносимыми:
# Сравнение ответов (неинтерактивное)
foundry model run gpt-oss-20b --prompt "Объясните, что такое edge AI простыми словами"
| Переменная | Назначение | Пример |
|------------|------------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Предпочитаемый псевдоним модели (каталог автоматически выбирает лучший вариант) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Переопределение конечной точки (иначе автоматически из менеджера) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Включить демонстрацию потоковой передачи | `true` |

> Если `FOUNDRY_LOCAL_ENDPOINT=auto` (или не задан), мы определяем его из менеджера SDK.

## Демонстрационный процесс (30 минут)

### 1. Установка Foundry Local и проверка настройки CLI (10 минут)

# Список кэшированных моделей
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Предварительный просмотр / Если поддерживается)**

Если предоставлен родной пакет для macOS (проверьте официальную документацию для получения последней информации):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Если родные бинарные файлы для macOS пока недоступны, вы все равно можете: 
1. Использовать виртуальную машину Windows 11 ARM/Intel (Parallels / UTM) и следовать шагам для Windows. 
2. Запускать модели через контейнер (если опубликован образ контейнера) и установить `FOUNDRY_LOCAL_ENDPOINT` на открытый порт.

**Создание виртуального окружения Python (Кроссплатформенное)**

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

Обновите pip и установите основные зависимости:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Шаг 1.2: Проверка установки

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Шаг 1.3: Настройка окружения

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Инициализация SDK (Рекомендуется)

Вместо ручного запуска службы и моделей, **Foundry Local Python SDK** может автоматически настроить все:

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

Если вы предпочитаете явный контроль, вы все еще можете использовать CLI + клиент OpenAI, как показано далее.

### 2. Запуск моделей локально через CLI (10 минут)

#### Шаг 3.1: Развертывание модели Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Шаг 3.2: Развертывание GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Шаг 3.3: Загрузка дополнительных моделей

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Начальный проект: Адаптация 01-run-phi для Foundry Local (5 минут)

#### Шаг 4.1: Создание базового приложения для чата

Создайте `samples/01-foundry-quickstart/chat_quickstart.py` (обновлено для использования менеджера, если доступно):

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

#### Шаг 4.2: Тестирование приложения

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Основные концепции

### 1. Архитектура Foundry Local

- **Локальный движок вывода**: Запускает модели полностью на вашем устройстве
- **Совместимость с OpenAI SDK**: Бесшовная интеграция с существующим кодом OpenAI
- **Управление моделями**: Загрузка, кэширование и эффективный запуск нескольких моделей
- **Оптимизация оборудования**: Использование ускорения GPU, NPU и CPU

### 2. Справочник команд CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Интеграция Python SDK

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

## Устранение распространенных проблем

### Проблема 1: "Команда Foundry не найдена"

**Решение:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Проблема 2: "Модель не удалось загрузить"

**Решение:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Проблема 3: "Отказ в подключении к localhost:5273"

**Решение:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Советы по оптимизации производительности

### 1. Стратегия выбора модели

- **Phi-4-mini**: Лучший выбор для общих задач, низкое потребление памяти
- **Qwen2.5-0.5b**: Самый быстрый вывод, минимальные ресурсы
- **GPT-OSS-20B**: Высокое качество, требует больше ресурсов
- **DeepSeek-Coder**: Оптимизирован для задач программирования

### 2. Оптимизация оборудования

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Мониторинг производительности

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

### Дополнительные улучшения

| Улучшение | Что | Как |
|-----------|-----|-----|
| Общие утилиты | Удаление дублирующей логики клиента/инициализации | Используйте `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Видимость использования токенов | Обучение мышлению о стоимости/эффективности | Установите `SHOW_USAGE=1`, чтобы выводить токены запроса/ответа/общие |
| Детерминированные сравнения | Стабильное тестирование производительности и проверки регрессии | Используйте `temperature=0`, `top_p=1`, одинаковый текст запроса |
| Задержка первого токена | Метрика воспринимаемой отзывчивости | Адаптируйте скрипт тестирования с потоковой передачей (`BENCH_STREAM=1`) |
| Повтор при временных ошибках | Устойчивые демонстрации при холодном старте | `RETRY_ON_FAIL=1` (по умолчанию) и настройте `RETRY_BACKOFF` |
| Тестирование на дым | Быстрая проверка ключевых потоков | Запустите `python Workshop/tests/smoke.py` перед воркшопом |
| Профили псевдонимов моделей | Быстрое переключение набора моделей между машинами | Поддерживайте `.env` с `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Эффективность кэширования | Избегайте повторных прогревов при многократном запуске | Утилиты менеджеров кэша; повторное использование между скриптами/ноутбуками |
| Прогрев при первом запуске | Снижение пиковых задержек p95 | Запустите небольшой запрос после создания `FoundryLocalManager`

Пример детерминированного прогрева (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Вы должны увидеть похожий вывод и идентичное количество токенов при втором запуске, подтверждающее детерминированность.

## Следующие шаги

После завершения этой сессии:

1. **Изучите Сессию 2**: Создание AI-решений с Azure AI Foundry RAG
2. **Попробуйте разные модели**: Экспериментируйте с Qwen, DeepSeek и другими семействами моделей
3. **Оптимизируйте производительность**: Настройте параметры для вашего оборудования
4. **Создавайте собственные приложения**: Используйте Foundry Local SDK в своих проектах

## Дополнительные ресурсы

### Документация
- [Справочник Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Руководство по установке Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Каталог моделей](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Примеры кода
- [Пример модуля 08, 01](./samples/01/README.md) - Быстрый старт REST Chat
- [Пример модуля 08, 02](./samples/02/README.md) - Интеграция OpenAI SDK
- [Пример модуля 08, 03](./samples/03/README.md) - Обнаружение моделей и тестирование производительности

### Сообщество
- [Обсуждения Foundry Local на GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Сообщество Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Продолжительность сессии**: 30 минут практики + 15 минут вопросов и ответов  
**Уровень сложности**: Начальный  
**Предварительные требования**: Windows 11, Python 3.10+, доступ администратора

## Пример сценария и сопоставление с воркшопом

| Скрипт / Ноутбук воркшопа | Сценарий | Цель | Пример ввода | Необходимый набор данных |
|----------------------------|----------|------|--------------|--------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Внутренняя IT-команда оценивает локальный вывод для портала оценки конфиденциальности | Доказать, что локальный SLM отвечает с задержкой менее секунды на стандартные запросы | "Назовите два преимущества локального вывода." | Нет (одиночный запрос) |
| Код адаптации быстрого старта | Разработчик переносит существующий скрипт OpenAI в Foundry Local | Показать совместимость "из коробки" | "Назовите два преимущества локального вывода." | Только встроенный запрос |

### Сценарий

Группа безопасности и соответствия должна проверить, можно ли обрабатывать конфиденциальные данные прототипа локально. Они запускают скрипт и тестируют несколько запросов (конфиденциальность, задержка, стоимость) в детерминированном режиме temperature=0, чтобы зафиксировать базовые результаты для последующего сравнения (тестирование производительности в Сессии 3 и сравнение SLM vs LLM в Сессии 4).

### Минимальный набор запросов в формате JSON (опционально)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Используйте этот список для создания воспроизводимого цикла оценки или для подготовки будущего тестового набора регрессии.

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.