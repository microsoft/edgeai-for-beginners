<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T10:45:26+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ru"
}
-->
# AGENTS.md

> **Руководство разработчика по работе с EdgeAI для начинающих**
> 
> Этот документ предоставляет исчерпывающую информацию для разработчиков, AI-агентов и участников, работающих с этим репозиторием. Он охватывает настройку, рабочие процессы разработки, тестирование и лучшие практики.
> 
> **Последнее обновление**: 30 октября 2025 | **Версия документа**: 3.0

## Содержание

- [Обзор проекта](../..)
- [Структура репозитория](../..)
- [Предварительные требования](../..)
- [Команды для настройки](../..)
- [Рабочий процесс разработки](../..)
- [Инструкции по тестированию](../..)
- [Руководство по стилю кода](../..)
- [Руководство по Pull Request](../..)
- [Система перевода](../..)
- [Интеграция Foundry Local](../..)
- [Сборка и развертывание](../..)
- [Распространенные проблемы и их устранение](../..)
- [Дополнительные ресурсы](../..)
- [Примечания, специфичные для проекта](../..)
- [Получение помощи](../..)

## Обзор проекта

EdgeAI для начинающих — это образовательный репозиторий, обучающий разработке Edge AI с использованием малых языковых моделей (SLM). Курс охватывает основы EdgeAI, развертывание моделей, методы оптимизации и готовые к производству реализации с использованием Microsoft Foundry Local и различных AI-фреймворков.

**Основные технологии:**
- Python 3.8+ (основной язык для примеров AI/ML)
- .NET C# (примеры AI/ML)
- JavaScript/Node.js с Electron (для настольных приложений)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-фреймворки: LangChain, Semantic Kernel, Chainlit
- Оптимизация моделей: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозитория:** Образовательный контент с 8 модулями и 10 комплексными примерами приложений

**Архитектура:** Многомодульный учебный путь с практическими примерами, демонстрирующими шаблоны развертывания Edge AI

## Структура репозитория

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

## Предварительные требования

### Необходимые инструменты

- **Python 3.8+** - Для примеров AI/ML и ноутбуков
- **Node.js 16+** - Для примера приложения на Electron
- **Git** - Для контроля версий
- **Microsoft Foundry Local** - Для локального запуска AI-моделей

### Рекомендуемые инструменты

- **Visual Studio Code** - С расширениями Python, Jupyter и Pylance
- **Windows Terminal** - Для улучшенного опыта работы с командной строкой (пользователи Windows)
- **Docker** - Для контейнеризированной разработки (опционально)

### Системные требования

- **ОЗУ**: минимум 8 ГБ, рекомендуется 16 ГБ+ для многомодельных сценариев
- **Хранилище**: 10 ГБ+ свободного места для моделей и зависимостей
- **ОС**: Windows 10/11, macOS 11+ или Linux (Ubuntu 20.04+)
- **Оборудование**: процессор с поддержкой AVX2; GPU (CUDA, Qualcomm NPU) опционально, но рекомендуется

### Требования к знаниям

- Базовые знания программирования на Python
- Знакомство с интерфейсами командной строки
- Понимание концепций AI/ML (для разработки примеров)
- Рабочие процессы Git и процессы Pull Request

## Команды для настройки

### Настройка репозитория

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Настройка примеров на Python (модуль 08 и примеры Workshop)

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

### Настройка примеров на Node.js (пример 08 - Windows Chat App)

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

### Настройка Foundry Local

Foundry Local необходим для запуска примеров. Скачайте и установите из официального репозитория:

**Установка:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ручная установка**: Скачайте с [страницы релизов](https://github.com/microsoft/Foundry-Local/releases)

**Быстрый старт:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Примечание**: Foundry Local автоматически выбирает лучший вариант модели для вашего оборудования (CUDA GPU, Qualcomm NPU или CPU).

## Рабочий процесс разработки

### Разработка контента

Этот репозиторий содержит преимущественно **образовательный контент в формате Markdown**. При внесении изменений:

1. Редактируйте `.md` файлы в соответствующих директориях модулей
2. Следуйте существующим шаблонам форматирования
3. Убедитесь, что примеры кода точны и протестированы
4. Обновите соответствующий переведенный контент, если необходимо (или доверьте это автоматизации)

### Разработка примеров приложений

Для примеров на Python из модуля 08 (примеры 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Для примеров Workshop на Python:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Для примера на Electron (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестирование примеров приложений

Примеры на Python не имеют автоматических тестов, но могут быть проверены запуском:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Пример на Electron имеет инфраструктуру тестирования:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Инструкции по тестированию

### Проверка контента

Репозиторий использует автоматизированные рабочие процессы перевода. Ручное тестирование переводов не требуется.

**Ручная проверка изменений контента:**
1. Просмотрите рендеринг Markdown, предварительно просмотрев `.md` файлы
2. Убедитесь, что все ссылки ведут на действительные цели
3. Протестируйте любые примеры кода, включенные в документацию
4. Проверьте, что изображения загружаются корректно

### Тестирование примеров приложений

**Модуль 08/примеры/08 (приложение Electron) имеет комплексное тестирование:**
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

**Примеры на Python должны быть протестированы вручную:**
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

## Руководство по стилю кода

### Контент в Markdown

- Используйте последовательную иерархию заголовков (# для заголовка, ## для основных разделов, ### для подразделов)
- Включайте блоки кода с указанием языка: ```python, ```bash, ```javascript
- Следуйте существующему форматированию для таблиц, списков и выделений
- Делайте строки читаемыми (стремитесь к ~80-100 символам, но не строго)
- Используйте относительные ссылки для внутренних ссылок

### Стиль кода на Python

- Следуйте соглашениям PEP 8
- Используйте подсказки типов, где это уместно
- Включайте docstrings для функций и классов
- Используйте осмысленные имена переменных
- Держите функции сфокусированными и лаконичными

### Стиль кода на JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основные соглашения:**
- Конфигурация ESLint предоставлена в примере 08
- Prettier для форматирования кода
- Используйте современный синтаксис ES6+
- Следуйте существующим шаблонам в кодовой базе

## Руководство по Pull Request

### Рабочий процесс внесения изменений

1. **Сделайте форк репозитория** и создайте новую ветку от `main`
2. **Внесите изменения**, следуя руководству по стилю кода
3. **Тщательно протестируйте** с использованием инструкций по тестированию выше
4. **Коммит с понятными сообщениями**, следуя формату conventional commits
5. **Запушьте изменения в свой форк** и создайте Pull Request
6. **Ответьте на обратную связь** от мейнтейнеров во время ревью

### Конвенция именования веток

- `feature/<module>-<description>` - Для новых функций или контента
- `fix/<module>-<description>` - Для исправления ошибок
- `docs/<description>` - Для улучшения документации
- `refactor/<description>` - Для рефакторинга кода

### Формат сообщений коммитов

Следуйте [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Примеры:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Формат заголовков
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Кодекс поведения

Все участники должны соблюдать [Кодекс поведения Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Пожалуйста, ознакомьтесь с [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) перед внесением изменений.

### Перед отправкой

**Для изменений контента:**
- Предварительно просмотрите все измененные файлы Markdown
- Убедитесь, что ссылки и изображения работают
- Проверьте наличие опечаток и грамматических ошибок

**Для изменений примеров кода (модуль 08/примеры/08):**
```bash
npm run lint
npm test
```

**Для изменений примеров на Python:**
- Убедитесь, что пример успешно запускается
- Проверьте обработку ошибок
- Убедитесь в совместимости с Foundry Local

### Процесс ревью

- Изменения образовательного контента проверяются на точность и ясность
- Примеры кода тестируются на функциональность
- Обновления переводов обрабатываются автоматически через GitHub Actions

## Система перевода

**ВАЖНО:** Этот репозиторий использует автоматизированный перевод через GitHub Actions.

- Переводы находятся в директории `/translations/` (50+ языков)
- Автоматизация через рабочий процесс `co-op-translator.yml`
- **НЕ редактируйте файлы перевода вручную** - они будут перезаписаны
- Редактируйте только исходные файлы на английском языке в корневой директории и директориях модулей
- Переводы автоматически генерируются при пуше в ветку `main`

## Интеграция Foundry Local

Большинство примеров модуля 08 требуют запущенного Microsoft Foundry Local.

### Установка и настройка

**Установите Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Установите Python SDK:**
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

### Использование SDK (Python)
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

### Проверка Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Переменные окружения для примеров

Большинство примеров используют следующие переменные окружения:
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

**Примечание**: При использовании `FoundryLocalManager` SDK автоматически обрабатывает обнаружение сервисов и загрузку моделей. Псевдонимы моделей (например, `phi-3.5-mini`) обеспечивают выбор лучшего варианта для вашего оборудования.

## Сборка и развертывание

### Развертывание контента

Этот репозиторий в основном содержит документацию - процесс сборки для контента не требуется.

### Сборка примеров приложений

**Приложение Electron (модуль 08/примеры/08):**
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

**Примеры на Python:**
Процесс сборки отсутствует - примеры запускаются напрямую через интерпретатор Python.

## Распространенные проблемы и их устранение

> **Совет**: Проверьте [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) для известных проблем и решений.

### Критические проблемы (блокирующие)

#### Foundry Local не запущен
**Проблема:** Примеры завершаются ошибками подключения

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

### Распространенные проблемы (умеренные)

#### Проблемы с виртуальной средой Python
**Проблема:** Ошибки импорта модулей

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

#### Проблемы сборки Electron
**Проблема:** npm install или ошибки сборки

**Решение:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Проблемы рабочего процесса (незначительные)

#### Конфликты рабочего процесса перевода
**Проблема:** PR перевода конфликтует с вашими изменениями

**Решение:**
- Редактируйте только исходные файлы на английском языке
- Доверьте автоматизированному рабочему процессу перевода обработку переводов
- Если возникают конфликты, объедините `main` в вашу ветку после слияния переводов

#### Ошибки загрузки моделей
**Проблема:** Foundry Local не может загрузить модели

**Решение:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Дополнительные ресурсы

### Учебные пути
- **Путь для начинающих:** Модули 01-02 (7-9 часов)
- **Путь для среднего уровня:** Модули 03-04 (9-11 часов)
- **Путь для продвинутого уровня:** Модули 05-07 (12-15 часов)
- **Путь для экспертов:** Модуль 08 (8-10 часов)
- **Практический семинар:** Материалы семинара (6-8 часов)

### Основной контент модулей
- **Модуль 01:** Основы EdgeAI и примеры из реальной жизни
- **Модуль 02:** Семейства и архитектуры малых языковых моделей (SLM)
- **Модуль 03:** Стратегии локального и облачного развертывания
- **Модуль 04:** Оптимизация моделей с использованием различных фреймворков (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Модуль 05:** SLMOps - эксплуатация в производстве
- **Модуль 06:** AI-агенты и вызов функций
- **Модуль 07:** Реализации, специфичные для платформ
- **Модуль 08:** Инструментарий Foundry Local с 10 комплексными примерами

### Внешние зависимости
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Локальное выполнение AI-моделей с API, совместимым с OpenAI
  - [Документация](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Фреймворк оптимизации
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Инструментарий оптимизации моделей
- [OpenVINO](https://docs.openvino.ai/) - Инструментарий оптимизации от Intel

## Примечания, специфичные для проекта

### Примеры приложений модуля 08

Репозиторий включает 10 комплексных примеров приложений:

1. **01-REST Chat Quickstart** - Базовая интеграция OpenAI SDK
2. **02-OpenAI SDK Integration** - Расширенные функции SDK
3. **03-Model Discovery & Benchmarking** - Инструменты сравнения моделей
4. **04-Chainlit RAG Application** - Генерация с использованием поиска
5. **05-Multi-Agent Orchestration** - Базовая координация агентов
6. **06-Models-as-Tools Router** - Интеллектуальная маршрутизация моделей
7. **07-Direct API Client** - Низкоуровневая интеграция API
8. **08-Windows 11 Chat App** - Нативное настольное приложение на Electron
9. **09-Advanced Multi-Agent System** - Сложная координация агентов
10. **10-Foundry Tools Framework** - Интеграция LangChain/Semantic Kernel

### Примерные приложения для мастер-класса

Мастер-класс включает 6 последовательных сессий с практическими реализациями:

1. **Сессия 01** - Начальная настройка чата с интеграцией Foundry Local
2. **Сессия 02** - Конвейер RAG и оценка с использованием RAGAS
3. **Сессия 03** - Бенчмаркинг моделей с открытым исходным кодом
4. **Сессия 04** - Сравнение и выбор моделей
5. **Сессия 05** - Системы оркестрации мульти-агентов
6. **Сессия 06** - Маршрутизация моделей и управление конвейером

Каждый пример демонстрирует различные аспекты разработки Edge AI с использованием Foundry Local.

### Производительность

- SLMs оптимизированы для развертывания на периферийных устройствах (2-16 ГБ ОЗУ)
- Локальный вывод обеспечивает время отклика 50-500 мс
- Техники квантования позволяют сократить размер на 75% при сохранении 85% производительности
- Возможности ведения реального времени разговоров с локальными моделями

### Безопасность и конфиденциальность

- Вся обработка данных происходит локально - данные не отправляются в облако
- Подходит для приложений, требующих конфиденциальности (здравоохранение, финансы)
- Соответствует требованиям суверенитета данных
- Foundry Local полностью работает на локальном оборудовании

## Получение помощи

### Документация

- **Основной README**: [README.md](README.md) - Обзор репозитория и пути обучения
- **Руководство по обучению**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Ресурсы для обучения и временные рамки
- **Поддержка**: [SUPPORT.md](SUPPORT.md) - Как получить помощь
- **Безопасность**: [SECURITY.md](SECURITY.md) - Сообщение о проблемах безопасности

### Поддержка сообщества

- **GitHub Issues**: [Сообщить об ошибках или запросить функции](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Задавайте вопросы и делитесь идеями](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Технические проблемы с Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Контакты

- **Сопровождающие**: См. [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Проблемы безопасности**: Следуйте ответственному раскрытию информации в [SECURITY.md](SECURITY.md)
- **Поддержка Microsoft**: Для корпоративной поддержки свяжитесь с клиентской службой Microsoft

### Дополнительные ресурсы

- **Microsoft Learn**: [Пути обучения AI и машинному обучению](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Документация Foundry Local**: [Официальная документация](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Примеры сообщества**: Ознакомьтесь с [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) для вкладов сообщества

---

**Это образовательный репозиторий, ориентированный на обучение разработке Edge AI. Основной вклад заключается в улучшении образовательного контента и добавлении/улучшении примерных приложений, демонстрирующих концепции Edge AI.**

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.