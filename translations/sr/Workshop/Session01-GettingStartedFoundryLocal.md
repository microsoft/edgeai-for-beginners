# Сесија 1: Почетак рада са Foundry Local

## Апстракт

Научите како да инсталирате, конфигуришете и покренете своје прве AI моделе користећи Microsoft Foundry Local. Ова практична сесија пружа корак-по-корак увод у локалну инференцију, од инсталације до креирања ваше прве апликације за ћаскање користећи моделе као што су Phi-4, Qwen и DeepSeek.

## Циљеви учења

На крају ове сесије, моћи ћете:

- **Инсталирати и конфигурисати**: Поставити Foundry Local уз правилну проверу инсталације
- **Овладати CLI операцијама**: Користити Foundry Local CLI за управљање моделима и њихово покретање
- **Покренути свој први модел**: Успешно покренути и интерактивно радити са локалним AI моделом
- **Направити апликацију за ћаскање**: Креирати основну апликацију за ћаскање користећи Foundry Local Python SDK
- **Разумети локални AI**: Схватити основе локалне инференције и управљања моделима

## Предуслови

### Захтеви система

- **Windows**: Windows 11 (22H2 или новији) ИЛИ **macOS**: macOS 11+ (ограничена подршка)
- **RAM**: Минимум 8GB, препоручено 16GB+
- **Складиште**: 10GB+ слободног простора за моделе
- **Python**: Инсталиран 3.10 или новији
- **Администраторски приступ**: Привилегије администратора за инсталацију

### Развојно окружење

- Visual Studio Code са Python екстензијом (препоручено)
- Приступ командној линији (PowerShell на Windows-у, Terminal на macOS-у)
- Git за клонирање репозиторијума (опционо)

## Ток радионице (30 минута)

### Корак 1: Инсталирање Foundry Local (5 минута)

#### Инсталација на Windows-у

Инсталирајте Foundry Local користећи Windows пакет менаџер:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Алтернатива: Преузмите директно са [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Инсталација на macOS-у (ограничена подршка)

> [!NOTE] 
> Подршка за macOS је тренутно у прегледу. Проверите званичну документацију за најновије информације.

Ако је доступно, инсталирајте користећи Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Алтернатива за кориснике macOS-а:**
- Користите Windows 11 VM (Parallels/UTM) и следите кораке за Windows
- Покрените преко контејнера ако је доступно и конфигуришите `FOUNDRY_LOCAL_ENDPOINT`

### Корак 2: Провера инсталације (3 минута)

Након инсталације, поново покрените терминал и проверите да ли Foundry Local ради:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Очекујани излаз треба да приказује информације о верзији и доступне команде.

### Корак 3: Постављање Python окружења (5 минута)

Креирајте посебно Python окружење за ову радионицу:

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

### Корак 4: Покрените свој први модел (7 минута)

Сада покренимо наш први AI модел локално!

#### Почетак са Phi-4 Mini (препоручени први модел)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ова команда преузима модел (први пут) и аутоматски покреће Foundry Local сервис.

#### Провера шта је покренуто

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Испробајте различите моделе

Када phi-4-mini ради, експериментишите са другим моделима:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Корак 5: Направите своју прву апликацију за ћаскање (10 минута)

Сада ћемо креирати Python апликацију која користи моделе које смо управо покренули.

#### Креирање скрипте за ћаскање

Креирајте нову датотеку под називом `my_first_chat.py` (или користите обезбеђени пример):

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
> **Повезани примери**: За напредније коришћење, погледајте:
>
> - **Python пример**: `Workshop/samples/session01/chat_bootstrap.py` - Укључује стриминг одговора и руковање грешкама
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Интерактивна верзија са детаљним објашњењима

#### Тестирање ваше апликације за ћаскање

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Алтернатива: Користите директно обезбеђене примере

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Или истражите интерактивни нотебук  
Отворите Workshop/notebooks/session01_chat_bootstrap.ipynb у VS Code-у

Испробајте ове пример разговоре:

- "Шта је Microsoft Foundry Local?"
- "Наведи 3 предности покретања AI модела локално"
- "Помози ми да разумем edge AI"

## Шта сте постигли

Честитамо! Успешно сте:

1. ✅ **Инсталирали Foundry Local** и проверили његово функционисање
2. ✅ **Покренули свој први AI модел** (phi-4-mini) локално
3. ✅ **Тестирали различите моделе** преко командне линије
4. ✅ **Направили апликацију за ћаскање** која се повезује са вашим локалним AI
5. ✅ **Искусили локалну AI инференцију** без зависности од облака

## Разумевање шта се догодило

### Локална AI инференција

- Ваши AI модели раде у потпуности на вашем рачунару
- Нема слања података у облак
- Одговори се генеришу локално користећи ваш CPU/GPU
- Приватност и безбедност су очувани

### Управљање моделима

- `foundry model run` преузима и покреће моделе
- **FoundryLocalManager SDK** аутоматски управља покретањем сервиса и учитавањем модела
- Модели се кеширају локално за будућу употребу
- Више модела може бити преузето, али обично се један покреће у исто време
- Сервис аутоматски управља животним циклусом модела

### SDK vs CLI приступи

- **CLI приступ**: Ручно управљање моделима са `foundry model run <model>`
- **SDK приступ**: Аутоматско управљање сервисом и моделима са `FoundryLocalManager(alias)`
- **Препорука**: Користите SDK за апликације, CLI за тестирање и истраживање

## Референца за основне команде

### Основне CLI команде

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

### Препоруке за моделе

- **phi-4-mini**: Најбољи почетни модел - брз, лаган, добар квалитет
- **qwen2.5-0.5b**: Најбржа инференција, минимална употреба меморије
- **gpt-oss-20b**: Виши квалитет одговора, захтева више ресурса
- **deepseek-coder-1.3b**: Оптимизован за програмирање и задатке кодирања

## Решавање проблема

### "Foundry команда није пронађена"

**Решење:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Модел није успео да се учита"

**Решење:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Веза одбијена на localhost-у"

**Решење:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Следећи кораци

### Непосредне акције

1. **Експериментишите** са различитим моделима и упитима
2. **Модификујте** своју апликацију за ћаскање да испробате различите моделе
3. **Креирајте** своје упите и тестирајте одговоре
4. **Истражите** Сесију 2: Креирање RAG апликација

### Напредни пут учења

1. **Сесија 2**: Креирање AI решења са RAG (Retrieval-Augmented Generation)
2. **Сесија 3**: Поређење различитих open-source модела
3. **Сесија 4**: Рад са најсавременијим моделима
4. **Сесија 5**: Креирање мулти-агентских AI система

## Енвиронмент променљиве (опционо)

За напредније коришћење, можете поставити ове енвиронмент променљиве:

| Променљива | Сврха | Пример |
|------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Подразумевани модел за коришћење | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Замена URL-а за крајњу тачку | `http://localhost:5273/v1` |

Креирајте `.env` датотеку у вашем директоријуму пројекта:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Додатни ресурси

### Документација

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Пример кода

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Комплетна апликација за ћаскање са стримингом
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Интерактивни туторијал  
- [Module08 Sample 01](../Module08/samples/01/README.md) - Брзи почетак са REST Chat
- [Module08 Sample 02](../Module08/samples/02/README.md) - Интеграција са OpenAI SDK
- [Module08 Sample 03](../Module08/samples/03/README.md) - Откривање модела и бенчмаркинг

### Заједница

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Трајање сесије**: 30 минута практично + 15 минута питања и одговори  
**Ниво тежине**: Почетни  
**Предуслови**: Windows 11/macOS 11+, Python 3.10+, Администраторски приступ

## Пример сценарија радионице

### Контекст из стварног живота

**Сценарио**: IT тим у компанији треба да процени AI инференцију на уређају за обраду осетљивих повратних информација запослених без слања података на екстерне сервисе.

**Ваш циљ**: Демонстрирати да локални AI модели могу пружити квалитетне одговоре са латенцијом мањом од једне секунде уз потпуно очување приватности података.

### Тест упити

Користите ове упите за валидацију вашег подешавања:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Критеријуми успеха

- ✅ Сви упити добијају одговоре за мање од 2 секунде
- ✅ Нема слања података са вашег локалног рачунара
- ✅ Одговори су релевантни и корисни
- ✅ Ваша апликација за ћаскање ради без проблема

Ова валидација осигурава да је ваше Foundry Local подешавање спремно за напредне радионице у Сесијама 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->