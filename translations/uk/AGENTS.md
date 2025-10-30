<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T15:12:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "uk"
}
-->
# AGENTS.md

> **Посібник для розробників щодо внесення змін до EdgeAI для початківців**
> 
> Цей документ містить детальну інформацію для розробників, AI агентів та учасників, які працюють із цим репозиторієм. Він охоплює налаштування, робочі процеси розробки, тестування та найкращі практики.
> 
> **Останнє оновлення**: 30 жовтня 2025 | **Версія документа**: 3.0

## Зміст

- [Огляд проєкту](../..)
- [Структура репозиторію](../..)
- [Попередні вимоги](../..)
- [Команди для налаштування](../..)
- [Робочий процес розробки](../..)
- [Інструкції з тестування](../..)
- [Рекомендації щодо стилю коду](../..)
- [Рекомендації щодо Pull Request](../..)
- [Система перекладу](../..)
- [Інтеграція Foundry Local](../..)
- [Збірка та розгортання](../..)
- [Поширені проблеми та усунення несправностей](../..)
- [Додаткові ресурси](../..)
- [Примітки щодо проєкту](../..)
- [Отримання допомоги](../..)

## Огляд проєкту

EdgeAI для початківців — це навчальний репозиторій, який навчає розробці Edge AI з використанням малих мовних моделей (SLM). Курс охоплює основи EdgeAI, розгортання моделей, техніки оптимізації та готові до виробництва реалізації з використанням Microsoft Foundry Local та різних AI фреймворків.

**Основні технології:**
- Python 3.8+ (основна мова для AI/ML прикладів)
- .NET C# (AI/ML приклади)
- JavaScript/Node.js з Electron (для настільних додатків)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI фреймворки: LangChain, Semantic Kernel, Chainlit
- Оптимізація моделей: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозиторію:** Репозиторій навчального контенту з 8 модулями та 10 комплексними прикладами додатків

**Архітектура:** Багатомодульний навчальний шлях із практичними прикладами, що демонструють шаблони розгортання Edge AI

## Структура репозиторію

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

## Попередні вимоги

### Необхідні інструменти

- **Python 3.8+** - Для AI/ML прикладів та ноутбуків
- **Node.js 16+** - Для прикладу додатку Electron
- **Git** - Для контролю версій
- **Microsoft Foundry Local** - Для локального запуску AI моделей

### Рекомендовані інструменти

- **Visual Studio Code** - З розширеннями Python, Jupyter та Pylance
- **Windows Terminal** - Для покращеного досвіду роботи з командним рядком (користувачам Windows)
- **Docker** - Для контейнеризованої розробки (опціонально)

### Системні вимоги

- **ОЗП**: мінімум 8 ГБ, рекомендовано 16 ГБ+ для сценаріїв з кількома моделями
- **Сховище**: 10 ГБ+ вільного місця для моделей та залежностей
- **ОС**: Windows 10/11, macOS 11+ або Linux (Ubuntu 20.04+)
- **Обладнання**: CPU з підтримкою AVX2; GPU (CUDA, Qualcomm NPU) опціонально, але рекомендовано

### Попередні знання

- Базове розуміння програмування на Python
- Знайомство з інтерфейсами командного рядка
- Розуміння концепцій AI/ML (для розробки прикладів)
- Робочі процеси Git та процеси Pull Request

## Команди для налаштування

### Налаштування репозиторію

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Налаштування Python прикладів (модуль 08 та приклади Workshop)

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

### Налаштування Node.js прикладу (Приклад 08 - Windows Chat App)

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

### Налаштування Foundry Local

Foundry Local необхідний для запуску прикладів. Завантажте та встановіть з офіційного репозиторію:

**Інсталяція:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ручна**: Завантажте з [сторінки релізів](https://github.com/microsoft/Foundry-Local/releases)

**Швидкий старт:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Примітка**: Foundry Local автоматично вибирає найкращий варіант моделі для вашого обладнання (CUDA GPU, Qualcomm NPU або CPU).

## Робочий процес розробки

### Розробка контенту

Цей репозиторій містить переважно **Markdown навчальний контент**. При внесенні змін:

1. Редагуйте `.md` файли у відповідних директоріях модулів
2. Дотримуйтесь існуючих шаблонів форматування
3. Переконайтеся, що приклади коду точні та протестовані
4. Оновіть відповідний перекладений контент, якщо необхідно (або дозвольте автоматизації зробити це)

### Розробка прикладів додатків

Для Python прикладів модуля 08 (приклади 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Для Python прикладів Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Для Electron прикладу (приклад 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестування прикладів додатків

Python приклади не мають автоматизованих тестів, але можуть бути перевірені шляхом їх запуску:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron приклад має тестову інфраструктуру:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Інструкції з тестування

### Перевірка контенту

Репозиторій використовує автоматизовані робочі процеси перекладу. Ручне тестування перекладів не потрібне.

**Ручна перевірка змін контенту:**
1. Перегляньте рендеринг Markdown, переглядаючи `.md` файли
2. Переконайтеся, що всі посилання ведуть до дійсних цілей
3. Протестуйте будь-які фрагменти коду, включені в документацію
4. Перевірте, чи зображення завантажуються правильно

### Тестування прикладів додатків

**Модуль08/приклади/08 (Electron додаток) має комплексне тестування:**
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

**Python приклади повинні бути протестовані вручну:**
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

## Рекомендації щодо стилю коду

### Markdown контент

- Використовуйте послідовну ієрархію заголовків (# для заголовка, ## для основних розділів, ### для підрозділів)
- Включайте блоки коду з вказівкою мови: ```python, ```bash, ```javascript
- Дотримуйтесь існуючого форматування для таблиць, списків та акцентів
- Зберігайте читабельність рядків (прагніть до ~80-100 символів, але не строго)
- Використовуйте відносні посилання для внутрішніх референцій

### Стиль коду Python

- Дотримуйтесь конвенцій PEP 8
- Використовуйте типові підказки, де це доречно
- Включайте docstrings для функцій та класів
- Використовуйте змістовні назви змінних
- Робіть функції сфокусованими та лаконічними

### Стиль коду JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основні конвенції:**
- Конфігурація ESLint надана у прикладі 08
- Prettier для форматування коду
- Використовуйте сучасний синтаксис ES6+
- Дотримуйтесь існуючих шаблонів у кодовій базі

## Рекомендації щодо Pull Request

### Робочий процес внесення змін

1. **Форкніть репозиторій** та створіть нову гілку від `main`
2. **Внесіть свої зміни**, дотримуючись рекомендацій щодо стилю коду
3. **Ретельно протестуйте** за допомогою наведених вище інструкцій з тестування
4. **Зробіть коміт із чіткими повідомленнями**, дотримуючись формату conventional commits
5. **Запуште у свій форк** та створіть Pull Request
6. **Відповідайте на відгуки** від мейнтейнерів під час перегляду

### Конвенція іменування гілок

- `feature/<module>-<description>` - Для нових функцій або контенту
- `fix/<module>-<description>` - Для виправлення помилок
- `docs/<description>` - Для покращення документації
- `refactor/<description>` - Для рефакторингу коду

### Формат повідомлень комітів

Дотримуйтесь [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Приклади:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Формат заголовка
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Кодекс поведінки

Усі учасники повинні дотримуватися [Кодексу поведінки Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Будь ласка, перегляньте [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) перед внесенням змін.

### Перед поданням

**Для змін контенту:**
- Перегляньте всі змінені файли Markdown
- Переконайтеся, що посилання та зображення працюють
- Перевірте на наявність орфографічних та граматичних помилок

**Для змін у прикладах коду (Модуль08/приклади/08):**
```bash
npm run lint
npm test
```

**Для змін у Python прикладах:**
- Перевірте, чи приклад успішно запускається
- Переконайтеся, що обробка помилок працює
- Перевірте сумісність із Foundry Local

### Процес перегляду

- Зміни навчального контенту перевіряються на точність та зрозумілість
- Приклади коду тестуються на функціональність
- Оновлення перекладів обробляються автоматично через GitHub Actions

## Система перекладу

**ВАЖЛИВО:** Цей репозиторій використовує автоматизований переклад через GitHub Actions.

- Переклади знаходяться в директорії `/translations/` (50+ мов)
- Автоматизовано через робочий процес `co-op-translator.yml`
- **НЕ редагуйте файли перекладу вручну** - вони будуть перезаписані
- Редагуйте лише англомовні вихідні файли в кореневій та модульних директоріях
- Переклади автоматично генеруються при пуші в гілку `main`

## Інтеграція Foundry Local

Більшість прикладів модуля 08 вимагають запуску Microsoft Foundry Local.

### Інсталяція та налаштування

**Інсталяція Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Інсталяція Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Запуск Foundry Local
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

### Використання SDK (Python)
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

### Перевірка Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Змінні середовища для прикладів

Більшість прикладів використовують ці змінні середовища:
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

**Примітка**: При використанні `FoundryLocalManager` SDK автоматично обробляє виявлення сервісів та завантаження моделей. Псевдоніми моделей (наприклад, `phi-3.5-mini`) забезпечують вибір найкращого варіанту для вашого обладнання.

## Збірка та розгортання

### Розгортання контенту

Цей репозиторій переважно містить документацію - процес збірки для контенту не потрібен.

### Збірка прикладів додатків

**Додаток Electron (Модуль08/приклади/08):**
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

**Python приклади:**
Процес збірки відсутній - приклади запускаються безпосередньо через інтерпретатор Python.

## Поширені проблеми та усунення несправностей

> **Порада**: Перевірте [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) для відомих проблем та рішень.

### Критичні проблеми (блокуючі)

#### Foundry Local не запущений
**Проблема:** Приклади не працюють через помилки з'єднання

**Рішення:**
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

### Поширені проблеми (помірні)

#### Проблеми з Python віртуальним середовищем
**Проблема:** Помилки імпорту модулів

**Рішення:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Проблеми зі збіркою Electron
**Проблема:** npm install або помилки збірки

**Рішення:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Проблеми з робочим процесом (незначні)

#### Конфлікти робочого процесу перекладу
**Проблема:** Конфлікт PR перекладу з вашими змінами

**Рішення:**
- Редагуйте лише англомовні вихідні файли
- Дозвольте автоматизованому робочому процесу перекладу обробляти переклади
- Якщо виникають конфлікти, об'єднайте `main` у вашу гілку після злиття перекладів

#### Помилки завантаження моделей
**Проблема:** Foundry Local не може завантажити моделі

**Рішення:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Додаткові ресурси

### Навчальні шляхи
- **Шлях для початківців:** Модулі 01-02 (7-9 годин)
- **Шлях для середнього рівня:** Модулі 03-04 (9-11 годин)
- **Шлях для просунутого рівня:** Модулі 05-07 (12-15 годин)
- **Шлях для експертів:** Модуль 08 (8-10 годин)
- **Практичний семінар:** Матеріали семінару (6-8 годин)

### Основний контент модулів
- **Модуль01:** Основи EdgeAI та реальні кейси
- **Модуль02:** Сімейства та архітектури малих мовних моделей (SLM)
- **Модуль03:** Стратегії локального та хмарного розгортання
- **Модуль04:** Оптимізація моделей з використанням різних фреймворків (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Модуль05:** SLMOps - операції у виробництві
- **Модуль06:** AI агенти та виклик функцій
- **Модуль07:** Реалізації для конкретних платформ
- **Модуль08:** Інструментарій Foundry Local з 10 комплексними прикладами

### Зовнішні залежності
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Локальний runtime AI моделей з OpenAI-сумісним API
  - [Документація](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Фреймворк оптимізації
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Інструментарій оптимізації моделей
10. **10-Foundry Tools Framework** - Інтеграція LangChain/Semantic Kernel

### Зразки додатків для воркшопу

Воркшоп включає 6 прогресивних сесій із практичними реалізаціями:

1. **Сесія 01** - Запуск чату з інтеграцією Foundry Local
2. **Сесія 02** - Конвеєр RAG та оцінка за допомогою RAGAS
3. **Сесія 03** - Бенчмаркінг моделей з відкритим кодом
4. **Сесія 04** - Порівняння та вибір моделей
5. **Сесія 05** - Системи оркестрації мультиагентів
6. **Сесія 06** - Маршрутизація моделей та управління конвеєрами

Кожен зразок демонструє різні аспекти розробки Edge AI з Foundry Local.

### Міркування щодо продуктивності

- SLM оптимізовані для розгортання на периферії (2-16 ГБ оперативної пам'яті)
- Локальне інференсування забезпечує час відповіді 50-500 мс
- Техніки квантування дозволяють зменшити розмір на 75% при збереженні 85% продуктивності
- Можливості реального часу для ведення розмов із локальними моделями

### Безпека та конфіденційність

- Усі обробки виконуються локально - дані не надсилаються в хмару
- Підходить для додатків, чутливих до конфіденційності (охорона здоров'я, фінанси)
- Відповідає вимогам суверенітету даних
- Foundry Local працює виключно на локальному обладнанні

## Отримання допомоги

### Документація

- **Основний README**: [README.md](README.md) - Огляд репозиторію та навчальні шляхи
- **Навчальний посібник**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Ресурси для навчання та графік
- **Підтримка**: [SUPPORT.md](SUPPORT.md) - Як отримати допомогу
- **Безпека**: [SECURITY.md](SECURITY.md) - Повідомлення про проблеми безпеки

### Підтримка спільноти

- **GitHub Issues**: [Повідомити про помилки або запропонувати функції](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Ставте запитання та діліться ідеями](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Технічні проблеми з Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Контакти

- **Мейнтейнери**: Див. [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Проблеми безпеки**: Дотримуйтесь відповідального розкриття у [SECURITY.md](SECURITY.md)
- **Підтримка Microsoft**: Для корпоративної підтримки звертайтеся до служби підтримки Microsoft

### Додаткові ресурси

- **Microsoft Learn**: [Навчальні шляхи з AI та машинного навчання](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Документація Foundry Local**: [Офіційна документація](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Зразки спільноти**: Перегляньте [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) для внесків спільноти

---

**Це освітній репозиторій, спрямований на навчання розробці Edge AI. Основний шаблон внесків полягає у вдосконаленні освітнього контенту та додаванні/покращенні зразків додатків, які демонструють концепції Edge AI.**

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.