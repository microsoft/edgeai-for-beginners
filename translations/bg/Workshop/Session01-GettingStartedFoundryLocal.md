<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-12T00:23:19+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "bg"
}
-->
# Сесия 1: Започване с Foundry Local

## Резюме

Научете как да инсталирате, конфигурирате и стартирате първите си AI модели с Microsoft Foundry Local. Тази практическа сесия предоставя стъпка по стъпка въведение в локалното предсказване, от инсталацията до създаването на първото ви чат приложение с модели като Phi-4, Qwen и DeepSeek.

## Цели на обучението

До края на тази сесия ще можете:

- **Инсталиране и конфигуриране**: Настройте Foundry Local с правилна проверка на инсталацията
- **Овладяване на CLI операции**: Използвайте Foundry Local CLI за управление и разгръщане на модели
- **Стартиране на първия модел**: Успешно разгръщане и взаимодействие с локален AI модел
- **Създаване на чат приложение**: Създайте основно чат приложение с Foundry Local Python SDK
- **Разбиране на локалния AI**: Усвоете основите на локалното предсказване и управление на модели

## Предварителни изисквания

### Системни изисквания

- **Windows**: Windows 11 (22H2 или по-нова) ИЛИ **macOS**: macOS 11+ (ограничена поддръжка)
- **RAM**: Минимум 8GB, препоръчително 16GB+
- **Съхранение**: 10GB+ свободно пространство за модели
- **Python**: Инсталиран 3.10 или по-нова версия
- **Административен достъп**: Привилегии на администратор за инсталация

### Среда за разработка

- Visual Studio Code с Python разширение (препоръчително)
- Достъп до команден ред (PowerShell за Windows, Terminal за macOS)
- Git за клониране на хранилища (по избор)

## Програма на работилницата (30 минути)

### Стъпка 1: Инсталиране на Foundry Local (5 минути)

#### Инсталация за Windows

Инсталирайте Foundry Local чрез пакетния мениджър за Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Алтернатива: Изтеглете директно от [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Инсталация за macOS (ограничена поддръжка)

> [!NOTE] 
> Поддръжката за macOS е в предварителен преглед. Проверете официалната документация за най-новата наличност.

Ако е налично, инсталирайте чрез Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Алтернатива за потребители на macOS:**
- Използвайте Windows 11 VM (Parallels/UTM) и следвайте стъпките за Windows
- Стартирайте чрез контейнер, ако е наличен, и конфигурирайте `FOUNDRY_LOCAL_ENDPOINT`

### Стъпка 2: Проверка на инсталацията (3 минути)

След инсталацията, рестартирайте терминала си и проверете дали Foundry Local работи:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Очакваният изход трябва да показва информация за версията и наличните команди.

### Стъпка 3: Настройка на Python среда (5 минути)

Създайте специална Python среда за тази работилница:

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

### Стъпка 4: Стартиране на първия модел (7 минути)

Сега да стартираме първия AI модел локално!

#### Започнете с Phi-4 Mini (Препоръчителен първи модел)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Тази команда изтегля модела (за първи път) и автоматично стартира услугата Foundry Local.

#### Проверка на активните модели

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Опитайте различни модели

След като phi-4-mini работи, експериментирайте с други модели:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Стъпка 5: Създаване на първото чат приложение (10 минути)

Сега да създадем Python приложение, което използва моделите, които току-що стартирахме.

#### Създаване на скрипт за чат

Създайте нов файл, наречен `my_first_chat.py` (или използвайте предоставения пример):

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
> **Свързани примери**: За по-напреднала употреба, вижте:
>
> - **Python пример**: `Workshop/samples/session01/chat_bootstrap.py` - Включва стрийминг отговори и обработка на грешки
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Интерактивна версия с подробни обяснения

#### Тестване на чат приложението

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Алтернатива: Използвайте предоставените примери директно

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Или разгледайте интерактивния notebook
Отворете Workshop/notebooks/session01_chat_bootstrap.ipynb в VS Code

Опитайте тези примерни разговори:

- "Какво е Microsoft Foundry Local?"
- "Избройте 3 предимства на локалното изпълнение на AI модели"
- "Помогнете ми да разбера edge AI"

## Какво постигнахте

Поздравления! Успешно:

1. ✅ **Инсталирахте Foundry Local** и проверихте, че работи
2. ✅ **Стартирахте първия си AI модел** (phi-4-mini) локално
3. ✅ **Тествахте различни модели** чрез командния ред
4. ✅ **Създадохте чат приложение**, което се свързва с вашия локален AI
5. ✅ **Изпитахте локално предсказване** без зависимости от облака

## Разбиране на процеса

### Локално предсказване

- Вашите AI модели работят изцяло на вашия компютър
- Никакви данни не се изпращат към облака
- Отговорите се генерират локално чрез вашия CPU/GPU
- Поверителността и сигурността са запазени

### Управление на модели

- `foundry model run` изтегля и стартира модели
- **FoundryLocalManager SDK** автоматично управлява стартирането на услугата и зареждането на модели
- Моделите се кешират локално за бъдеща употреба
- Могат да се изтеглят множество модели, но обикновено се стартира само един
- Услугата автоматично управлява жизнения цикъл на модела

### SDK срещу CLI подходи

- **CLI подход**: Ръчно управление на модели с `foundry model run <model>`
- **SDK подход**: Автоматично управление на услуги и модели с `FoundryLocalManager(alias)`
- **Препоръка**: Използвайте SDK за приложения, CLI за тестване и изследване

## Референция за основни команди

### Основни CLI команди

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

### Препоръки за модели

- **phi-4-mini**: Най-добър начален модел - бърз, лек, добро качество
- **qwen2.5-0.5b**: Най-бързо предсказване, минимална употреба на памет
- **gpt-oss-20b**: По-високо качество на отговорите, изисква повече ресурси
- **deepseek-coder-1.3b**: Оптимизиран за програмиране и задачи с код

## Отстраняване на проблеми

### "Foundry команда не е намерена"

**Решение:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Моделът не успя да се зареди"

**Решение:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Връзката отказана на localhost"

**Решение:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Следващи стъпки

### Незабавни действия

1. **Експериментирайте** с различни модели и въпроси
2. **Модифицирайте** вашето чат приложение, за да опитате различни модели
3. **Създайте** свои собствени въпроси и тествайте отговорите
4. **Разгледайте** Сесия 2: Създаване на RAG приложения

### Път за напреднало обучение

1. **Сесия 2**: Създаване на AI решения с RAG (Retrieval-Augmented Generation)
2. **Сесия 3**: Сравнение на различни модели с отворен код
3. **Сесия 4**: Работа с най-новите модели
4. **Сесия 5**: Създаване на AI системи с множество агенти

## Променливи на средата (по избор)

За по-напреднала употреба можете да зададете тези променливи на средата:

| Променлива | Цел | Пример |
|------------|-----|--------|
| `FOUNDRY_LOCAL_ALIAS` | Модел по подразбиране | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Пренасочване на URL адреса на крайна точка | `http://localhost:5273/v1` |

Създайте `.env` файл в директорията на вашия проект:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Допълнителни ресурси

### Документация

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Примерен код

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Пълно чат приложение със стрийминг
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Интерактивен урок  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Общност

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Продължителност на сесията**: 30 минути практическа работа + 15 минути въпроси и отговори  
**Ниво на трудност**: Начинаещ  
**Предварителни изисквания**: Windows 11/macOS 11+, Python 3.10+, Административен достъп

## Примерен сценарий на работилницата

### Контекст от реалния свят

**Сценарий**: Екипът за IT в предприятие трябва да оцени локалното предсказване на AI за обработка на чувствителна обратна връзка от служители, без да изпраща данни към външни услуги.

**Вашата цел**: Демонстрирайте, че локалните AI модели могат да предоставят качествени отговори с латентност под секунда, като същевременно запазват пълна поверителност на данните.

### Тестови въпроси

Използвайте тези въпроси, за да валидирате настройката си:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Критерии за успех

- ✅ Всички въпроси получават отговори за по-малко от 2 секунди
- ✅ Никакви данни не напускат вашия локален компютър
- ✅ Отговорите са релевантни и полезни
- ✅ Вашето чат приложение работи гладко

Тази валидация гарантира, че вашата настройка на Foundry Local е готова за напредналите работилници в Сесии 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->