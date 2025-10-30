<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T14:33:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bg"
}
-->
# AGENTS.md

> **Ръководство за разработчици за допринасяне към EdgeAI за начинаещи**
> 
> Този документ предоставя изчерпателна информация за разработчици, AI агенти и сътрудници, работещи с това хранилище. Той обхваща настройка, работни процеси за разработка, тестване и добри практики.
> 
> **Последна актуализация**: 30 октомври 2025 | **Версия на документа**: 3.0

## Съдържание

- [Преглед на проекта](../..)
- [Структура на хранилището](../..)
- [Предварителни изисквания](../..)
- [Команди за настройка](../..)
- [Работен процес за разработка](../..)
- [Инструкции за тестване](../..)
- [Насоки за стил на код](../..)
- [Насоки за Pull Request](../..)
- [Система за превод](../..)
- [Интеграция с Foundry Local](../..)
- [Създаване и разгръщане](../..)
- [Често срещани проблеми и отстраняване на неизправности](../..)
- [Допълнителни ресурси](../..)
- [Бележки, специфични за проекта](../..)
- [Получаване на помощ](../..)

## Преглед на проекта

EdgeAI за начинаещи е изчерпателно образователно хранилище, което обучава разработка на Edge AI с Малки езикови модели (SLMs). Курсът обхваща основи на EdgeAI, разгръщане на модели, техники за оптимизация и готови за производство реализации с Microsoft Foundry Local и различни AI рамки.

**Основни технологии:**
- Python 3.8+ (основен език за AI/ML примери)
- .NET C# (AI/ML примери)
- JavaScript/Node.js с Electron (за десктоп приложения)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI рамки: LangChain, Semantic Kernel, Chainlit
- Оптимизация на модели: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип хранилище:** Образователно съдържание с 8 модула и 10 изчерпателни примерни приложения

**Архитектура:** Многомодулен учебен път с практически примери, демонстриращи модели за разгръщане на Edge AI

## Структура на хранилището

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Предварителни изисквания

### Необходими инструменти

- **Python 3.8+** - За AI/ML примери и тетрадки
- **Node.js 16+** - За Electron примерното приложение
- **Git** - За контрол на версиите
- **Microsoft Foundry Local** - За локално изпълнение на AI модели

### Препоръчителни инструменти

- **Visual Studio Code** - С разширения за Python, Jupyter и Pylance
- **Windows Terminal** - За по-добро командно изживяване (потребители на Windows)
- **Docker** - За контейнеризирана разработка (по избор)

### Системни изисквания

- **RAM**: Минимум 8GB, препоръчително 16GB+ за многомоделни сценарии
- **Съхранение**: 10GB+ свободно пространство за модели и зависимости
- **OS**: Windows 10/11, macOS 11+ или Linux (Ubuntu 20.04+)
- **Хардуер**: CPU с поддръжка на AVX2; GPU (CUDA, Qualcomm NPU) по избор, но препоръчително

### Предварителни знания

- Основно разбиране на програмиране с Python
- Запознатост с командни интерфейси
- Разбиране на AI/ML концепции (за разработка на примери)
- Git работни процеси и процеси за Pull Request

## Команди за настройка

### Настройка на хранилището

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Настройка на Python примери (Module08 и Workshop примери)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Настройка на Node.js примери (Пример 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Настройка на Foundry Local

Foundry Local е необходим за изпълнение на примерите. Изтеглете и инсталирайте от официалното хранилище:

**Инсталация:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ръчно**: Изтеглете от [страницата с издания](https://github.com/microsoft/Foundry-Local/releases)

**Бърз старт:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Забележка**: Foundry Local автоматично избира най-добрия вариант на модела за вашия хардуер (CUDA GPU, Qualcomm NPU или CPU).

## Работен процес за разработка

### Разработка на съдържание

Това хранилище съдържа предимно **Markdown образователно съдържание**. При извършване на промени:

1. Редактирайте `.md` файлове в съответните директории на модули
2. Следвайте съществуващите модели на форматиране
3. Уверете се, че примерите с код са точни и тествани
4. Актуализирайте съответното преведено съдържание, ако е необходимо (или оставете автоматизацията да го обработи)

### Разработка на примерни приложения

За Python примери от Module08 (примери 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

За Python примери от Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

За Electron пример (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестване на примерни приложения

Python примерите нямат автоматизирани тестове, но могат да бъдат валидирани чрез изпълнение:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron примерът има инфраструктура за тестове:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Инструкции за тестване

### Валидиране на съдържание

Хранилището използва автоматизирани работни процеси за превод. Не се изисква ръчно тестване за преводи.

**Ръчно валидиране за промени в съдържанието:**
1. Прегледайте рендирането на Markdown чрез предварителен преглед на `.md` файлове
2. Уверете се, че всички връзки сочат към валидни цели
3. Тествайте всички включени примери с код
4. Проверете дали изображенията се зареждат правилно

### Тестване на примерни приложения

**Module08/samples/08 (Electron приложение) има изчерпателно тестване:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python примерите трябва да бъдат тествани ръчно:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Насоки за стил на код

### Markdown съдържание

- Използвайте последователна йерархия на заглавията (# за заглавие, ## за основни секции, ### за подсекции)
- Включвайте блокове с код със спецификатори за език: ```python, ```bash, ```javascript
- Следвайте съществуващото форматиране за таблици, списъци и акценти
- Поддържайте редовете четими (целете ~80-100 символа, но не строго)
- Използвайте относителни връзки за вътрешни препратки

### Python стил на код

- Следвайте конвенциите на PEP 8
- Използвайте типови подсказки, където е подходящо
- Включвайте docstrings за функции и класове
- Използвайте значими имена на променливи
- Поддържайте функциите фокусирани и кратки

### JavaScript/Node.js стил на код

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основни конвенции:**
- Конфигурация на ESLint, предоставена в пример 08
- Prettier за форматиране на код
- Използвайте модерен ES6+ синтаксис
- Следвайте съществуващите модели в кодовата база

## Насоки за Pull Request

### Работен процес за допринасяне

1. **Fork хранилището** и създайте нов клон от `main`
2. **Направете вашите промени**, следвайки насоките за стил на код
3. **Тествайте обстойно**, използвайки инструкциите за тестване по-горе
4. **Комитнете с ясни съобщения**, следвайки формата за конвенционални комити
5. **Публикувайте във вашия fork** и създайте Pull Request
6. **Отговаряйте на обратна връзка** от поддържащите по време на прегледа

### Конвенция за именуване на клонове

- `feature/<module>-<description>` - За нови функции или съдържание
- `fix/<module>-<description>` - За поправки на грешки
- `docs/<description>` - За подобрения в документацията
- `refactor/<description>` - За рефакториране на код

### Формат на съобщенията за комит

Следвайте [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Примери:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Формат на заглавията
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Кодекс на поведение

Всички сътрудници трябва да следват [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Моля, прегледайте [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) преди да допринасяте.

### Преди подаване

**За промени в съдържанието:**
- Прегледайте всички модифицирани Markdown файлове
- Уверете се, че връзките и изображенията работят
- Проверете за правописни и граматически грешки

**За промени в примерния код (Module08/samples/08):**
```bash
npm run lint
npm test
```

**За промени в Python примерите:**
- Тествайте дали примерът се изпълнява успешно
- Уверете се, че обработката на грешки работи
- Проверете съвместимостта с Foundry Local

### Процес на преглед

- Промените в образователното съдържание се преглеждат за точност и яснота
- Примерите с код се тестват за функционалност
- Актуализациите на преводите се обработват автоматично от GitHub Actions

## Система за превод

**ВАЖНО:** Това хранилище използва автоматизиран превод чрез GitHub Actions.

- Преводите са в директорията `/translations/` (50+ езика)
- Автоматизирано чрез работния процес `co-op-translator.yml`
- **НЕ редактирайте ръчно файловете с преводи** - те ще бъдат презаписани
- Редактирайте само английските изходни файлове в основната и модулните директории
- Преводите се генерират автоматично при push към клона `main`

## Интеграция с Foundry Local

Повечето примери от Module08 изискват Microsoft Foundry Local да бъде стартиран.

### Инсталация и настройка

**Инсталирайте Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Инсталирайте Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Стартиране на Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Използване на SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Проверка на Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Променливи на средата за примери

Повечето примери използват тези променливи на средата:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Забележка**: При използване на `FoundryLocalManager`, SDK автоматично обработва откриването на услуги и зареждането на модели. Алиасите на модели (като `phi-3.5-mini`) гарантират, че най-добрият вариант е избран за вашия хардуер.

## Създаване и разгръщане

### Разгръщане на съдържание

Това хранилище е предимно документация - не се изисква процес на създаване за съдържание.

### Създаване на примерни приложения

**Electron приложение (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python примери:**
Няма процес на създаване - примерите се изпълняват директно с Python интерпретатор.

## Често срещани проблеми и отстраняване на неизправности

> **Съвет**: Проверете [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) за известни проблеми и решения.

### Критични проблеми (блокиращи)

#### Foundry Local не работи
**Проблем:** Примерите се провалят с грешки при свързване

**Решение:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Често срещани проблеми (умерени)

#### Проблеми с Python виртуална среда
**Проблем:** Грешки при импортиране на модули

**Решение:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Проблеми с изграждането на Electron
**Проблем:** npm install или грешки при изграждане

**Решение:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Проблеми с работния процес (незначителни)

#### Конфликти в работния процес за превод
**Проблем:** Преводният PR влиза в конфликт с вашите промени

**Решение:**
- Редактирайте само английските изходни файлове
- Оставете автоматизирания работен процес за превод да обработи преводите
- Ако възникнат конфликти, обединете `main` във вашия клон след като преводите бъдат обединени

#### Неуспехи при изтегляне на модели
**Проблем:** Foundry Local не успява да изтегли модели

**Решение:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Допълнителни ресурси

### Учебни пътеки
- **Път за начинаещи:** Модули 01-02 (7-9 часа)
- **Път за средно напреднали:** Модули 03-04 (9-11 часа)
- **Път за напреднали:** Модули 05-07 (12-15 часа)
- **Път за експерти:** Модул 08 (8-10 часа)
- **Практически семинар:** Материали за семинар (6-8 часа)

### Основно съдържание на модули
- **Module01:** Основи на EdgeAI и реални казуси
- **Module02:** Семейства и архитектури на Малки езикови модели (SLM)
- **Module03:** Стратегии за локално и облачно разгръщане
- **Module04:** Оптимизация на модели с множество рамки (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - операции в производството
- **Module06:** AI агенти и извикване на функции
- **Module07:** Имплементации, специфични за платформата
- **Module08:** Инструментариум Foundry Local с 10 изчерпателни примера

### Външни зависимости
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Локално изпълнение на AI модели с OpenAI-съвместим API
  - [Документация](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Рамка за оптимизация
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Инструмент за оптимизация на модели
- [OpenVINO](https://docs.openvino.ai/) - Инструмент за оптимизация на Intel

## Бележки, специфични за проекта

### Примерни приложения от Module08

Хранилището включва 10 изчерпателни примерни приложения:

1. **01-REST Chat Quickstart** - Основна интеграция с OpenAI SDK
2. **02-OpenAI SDK Integration** - Разширени функции на SDK
3. **03-Model Discovery & Benchmarking** - Инструменти за сравнение на модели
4. **04-Chainlit RAG Application** - Генерация с извличане на информация
5. **05-Multi-Agent Orchestration** - Основна
10. **10-Foundry Tools Framework** - Интеграция на LangChain/Semantic Kernel

### Примерни приложения от работилницата

Работилницата включва 6 прогресивни сесии с практически реализации:

1. **Сесия 01** - Стартиране на чат с интеграция на Foundry Local
2. **Сесия 02** - RAG pipeline и оценка с RAGAS
3. **Сесия 03** - Бенчмаркинг на модели с отворен код
4. **Сесия 04** - Сравнение и избор на модели
5. **Сесия 05** - Системи за оркестрация на множество агенти
6. **Сесия 06** - Управление на маршрутизация на модели и pipeline

Всеки пример демонстрира различни аспекти на разработката на Edge AI с Foundry Local.

### Съображения за производителност

- SLMs са оптимизирани за внедряване на edge устройства (2-16GB RAM)
- Локалното извеждане осигурява времена за отговор от 50-500ms
- Техники за квантизация постигат 75% намаление на размера със запазване на 85% от производителността
- Възможности за реалновремеви разговори с локални модели

### Сигурност и поверителност

- Цялата обработка се извършва локално - няма изпращане на данни към облака
- Подходящо за приложения, чувствителни към поверителност (здравеопазване, финанси)
- Отговаря на изискванията за суверенитет на данните
- Foundry Local работи изцяло на локален хардуер

## Получаване на помощ

### Документация

- **Основен README**: [README.md](README.md) - Преглед на хранилището и учебни пътеки
- **Учебен наръчник**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Учебни ресурси и график
- **Поддръжка**: [SUPPORT.md](SUPPORT.md) - Как да получите помощ
- **Сигурност**: [SECURITY.md](SECURITY.md) - Докладване на проблеми със сигурността

### Поддръжка от общността

- **GitHub Issues**: [Докладване на грешки или заявка за функции](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Задаване на въпроси и споделяне на идеи](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Технически проблеми с Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Контакт

- **Поддържащи лица**: Вижте [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Проблеми със сигурността**: Следвайте отговорното докладване в [SECURITY.md](SECURITY.md)
- **Поддръжка от Microsoft**: За корпоративна поддръжка, свържете се с клиентската служба на Microsoft

### Допълнителни ресурси

- **Microsoft Learn**: [Учебни пътеки за AI и машинно обучение](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Документация на Foundry Local**: [Официална документация](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Примерни приложения от общността**: Вижте [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) за приноси от общността

---

**Това е образователно хранилище, фокусирано върху обучението за разработка на Edge AI. Основният модел на принос е подобряване на образователното съдържание и добавяне/усъвършенстване на примерни приложения, които демонстрират концепции за Edge AI.**

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.