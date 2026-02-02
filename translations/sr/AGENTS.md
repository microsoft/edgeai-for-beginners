# AGENTS.md

> **Водич за програмере: допринос EdgeAI за почетнике**
> 
> Овај документ пружа свеобухватне информације за програмере, AI агенте и сараднике који раде са овим репозиторијумом. Обухвата подешавање, радне токове развоја, тестирање и најбоље праксе.
> 
> **Последње ажурирање**: 30. октобар 2025 | **Верзија документа**: 3.0

## Садржај

- [Преглед пројекта](../..)
- [Структура репозиторијума](../..)
- [Предуслови](../..)
- [Команде за подешавање](../..)
- [Радни ток развоја](../..)
- [Упутства за тестирање](../..)
- [Смернице за стил кода](../..)
- [Смернице за Pull Request](../..)
- [Систем за превођење](../..)
- [Интеграција Foundry Local](../..)
- [Изградња и распоређивање](../..)
- [Уобичајени проблеми и решавање](../..)
- [Додатни ресурси](../..)
- [Белешке специфичне за пројекат](../..)
- [Добијање помоћи](../..)

## Преглед пројекта

EdgeAI за почетнике је свеобухватан образовни репозиторијум који подучава развој Edge AI-а са малим језичким моделима (SLM). Курс обухвата основе EdgeAI-а, распоређивање модела, технике оптимизације и имплементације спремне за производњу користећи Microsoft Foundry Local и различите AI оквире.

**Кључне технологије:**
- Python 3.8+ (примарни језик за AI/ML примере)
- .NET C# (AI/ML примери)
- JavaScript/Node.js са Electron-ом (за десктоп апликације)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI оквири: LangChain, Semantic Kernel, Chainlit
- Оптимизација модела: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозиторијума:** Репозиторијум образовног садржаја са 8 модула и 10 свеобухватних примера апликација

**Архитектура:** Вишемодулни пут учења са практичним примерима који демонстрирају обрасце распоређивања Edge AI-а

## Структура репозиторијума

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

## Предуслови

### Потребни алати

- **Python 3.8+** - За AI/ML примере и бележнице
- **Node.js 16+** - За Electron пример апликације
- **Git** - За контролу верзија
- **Microsoft Foundry Local** - За локално покретање AI модела

### Препоручени алати

- **Visual Studio Code** - Са Python, Jupyter и Pylance екстензијама
- **Windows Terminal** - За боље искуство командне линије (корисници Windows-а)
- **Docker** - За развој у контејнерима (опционо)

### Системски захтеви

- **RAM**: Минимум 8GB, препоручено 16GB+ за сценарије са више модела
- **Складиште**: 10GB+ слободног простора за моделе и зависности
- **ОС**: Windows 10/11, macOS 11+, или Linux (Ubuntu 20.04+)
- **Хардвер**: CPU са подршком за AVX2; GPU (CUDA, Qualcomm NPU) опционално, али препоручено

### Предзнање

- Основно разумевање Python програмирања
- Познавање интерфејса командне линије
- Разумевање AI/ML концепата (за развој примера)
- Git радни токови и процеси Pull Request-а

## Команде за подешавање

### Подешавање репозиторијума

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Подешавање Python примера (Модул08 и радионички примери)

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

### Подешавање Node.js примера (Пример 08 - Windows Chat App)

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

### Подешавање Foundry Local-а

Foundry Local је потребан за покретање примера. Преузмите и инсталирајте са званичног репозиторијума:

**Инсталација:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ручно**: Преузмите са [странице са издањима](https://github.com/microsoft/Foundry-Local/releases)

**Брзи почетак:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Напомена**: Foundry Local аутоматски бира најбољу варијанту модела за ваш хардвер (CUDA GPU, Qualcomm NPU, или CPU).

## Радни ток развоја

### Развој садржаја

Овај репозиторијум садржи првенствено **Markdown образовни садржај**. Приликом измена:

1. Уредите `.md` датотеке у одговарајућим директоријумима модула
2. Пратите постојеће обрасце форматирања
3. Осигурајте да су примери кода тачни и тестирани
4. Ажурирајте одговарајући преведени садржај ако је потребно (или дозволите аутоматизацији да то уради)

### Развој пример апликација

За Python примере из Модула08 (примери 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

За радионичке Python примере:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

За Electron пример (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестирање пример апликација

Python примери немају аутоматизоване тестове, али се могу проверити покретањем:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron пример има инфраструктуру за тестирање:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Упутства за тестирање

### Валидација садржаја

Репозиторијум користи аутоматизоване радне токове за превођење. Није потребно ручно тестирање превода.

**Ручна валидација за измене садржаја:**
1. Прегледајте рендеровање Markdown-а прегледом `.md` датотека
2. Проверите да ли све везе воде ка важећим циљевима
3. Тестирајте све делове кода укључене у документацију
4. Проверите да ли се слике правилно учитавају

### Тестирање пример апликација

**Модул08/примери/08 (Electron апликација) има свеобухватно тестирање:**
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

**Python примери треба ручно тестирати:**
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

## Смернице за стил кода

### Markdown садржај

- Користите доследну хијерархију наслова (# за наслов, ## за главне секције, ### за подсекције)
- Укључите блокове кода са спецификацијом језика: ```python, ```bash, ```javascript
- Пратите постојеће форматирање за табеле, листе и наглашавање
- Држите линије читљивим (циљајте ~80-100 карактера, али није строго)
- Користите релативне везе за унутрашње референце

### Python стил кода

- Пратите PEP 8 конвенције
- Користите типске назнаке где је прикладно
- Укључите docstring-ове за функције и класе
- Користите смислена имена променљивих
- Држите функције фокусираним и концизним

### JavaScript/Node.js стил кода

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Кључне конвенције:**
- ESLint конфигурација обезбеђена у примеру 08
- Prettier за форматирање кода
- Користите модеран ES6+ синтакс
- Пратите постојеће обрасце у бази кода

## Смернице за Pull Request

### Радни ток доприноса

1. **Fork-ујте репозиторијум** и креирајте нову грану из `main`
2. **Направите измене** пратећи смернице за стил кода
3. **Тестирајте темељно** користећи упутства за тестирање изнад
4. **Комитујте са јасним порукама** пратећи формат конвенционалних комита
5. **Пошаљите на ваш fork** и креирајте Pull Request
6. **Одговорите на повратне информације** од одржавалаца током прегледа

### Конвенција именовања грана

- `feature/<module>-<description>` - За нове функције или садржај
- `fix/<module>-<description>` - За исправке грешака
- `docs/<description>` - За побољшања документације
- `refactor/<description>` - За рефакторисање кода

### Формат поруке комита

Пратите [Conventional Commits](https://www.conventionalcommits.org/):

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

### Формат наслова
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Кодекс понашања

Сви сарадници морају пратити [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Молимо вас да прегледате [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) пре доприноса.

### Пре слања

**За измене садржаја:**
- Прегледајте све модификоване Markdown датотеке
- Проверите да ли везе и слике раде
- Проверите правописне и граматичке грешке

**За измене пример кода (Модул08/примери/08):**
```bash
npm run lint
npm test
```

**За измене Python примера:**
- Тестирајте да пример успешно ради
- Проверите да ли обрада грешака функционише
- Проверите компатибилност са Foundry Local-ом

### Процес прегледа

- Измене образовног садржаја се прегледају ради тачности и јасноће
- Примери кода се тестирају ради функционалности
- Ажурирања превода се аутоматски обрађују преко GitHub Actions-а

## Систем за превођење

**ВАЖНО:** Овај репозиторијум користи аутоматизовано превођење преко GitHub Actions-а.

- Преводи се налазе у директоријуму `/translations/` (50+ језика)
- Аутоматизовано преко `co-op-translator.yml` радног тока
- **НЕ МОЈТЕ ручно уређивати датотеке превода** - биће преписане
- Уређујте само изворне датотеке на енглеском у корену и директоријумима модула
- Преводи се аутоматски генеришу при пушу на `main` грану

## Интеграција Foundry Local-а

Већина примера из Модула08 захтева да Microsoft Foundry Local буде покренут.

### Инсталација и подешавање

**Инсталирајте Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Инсталирајте Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Покретање Foundry Local-а
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

### Коришћење SDK-а (Python)
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

### Верификација Foundry Local-а
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Енвиронмент променљиве за примере

Већина примера користи ове енвиронмент променљиве:
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

**Напомена**: При коришћењу `FoundryLocalManager`, SDK аутоматски обрађује откривање сервиса и учитавање модела. Алијаси модела (као `phi-3.5-mini`) осигуравају да се најбоља варијанта изабере за ваш хардвер.

## Изградња и распоређивање

### Распоређивање садржаја

Овај репозиторијум је првенствено документација - није потребан процес изградње за садржај.

### Изградња пример апликација

**Electron апликација (Модул08/примери/08):**
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
Нема процеса изградње - примери се директно покрећу са Python интерпретатором.

## Уобичајени проблеми и решавање

> **Савет**: Проверите [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) за познате проблеме и решења.

### Критични проблеми (блокирајући)

#### Foundry Local није покренут
**Проблем:** Примери не успевају са грешкама у вези

**Решење:**
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

### Уобичајени проблеми (умерени)

#### Проблеми са Python виртуелним окружењем
**Проблем:** Грешке при увозу модула

**Решење:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Проблеми са изградњом Electron-а
**Проблем:** npm install или грешке при изградњи

**Решење:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Проблеми са радним током (мањи)

#### Конфликти у радном току превођења
**Проблем:** Преводни PR у конфликту са вашим изменама

**Решење:**
- Уређујте само изворне датотеке на енглеском
- Дозволите аутоматизованом радном току превођења да обради преводе
- Ако дође до конфликта, спојите `main` у вашу грану након што се преводи споје

#### Неуспеси при преузимању модела
**Проблем:** Foundry Local не успева да преузме моделе

**Решење:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Додатни ресурси

### Путеви учења
- **Почетнички пут:** Модули 01-02 (7-9 сати)
- **Средњи пут:** Модули 03-04 (9-11 сати)
- **Напредни пут:** Модули 05-07 (12-15 сати)
- **Експертски пут:** Модул 08 (8-10 сати)
- **Практична радионица:** Материјали радионице (6-8 сати)

### Кључни садржај модула
- **Модул01:** Основе EdgeAI-а и студије случаја из стварног света
- **Модул02:** Породице и архитектуре малих језичких модела (SLM)
- **Модул03:** Стратегије локалног и облачног распоређивања
- **Модул04:** Оптимизација модела са више оквира (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Модул05:** SLMOps - операције у производњи
- **Модул06:** AI агенти и позивање функција
- **Модул07:** Имплементације специфичне за платформу
- **Модул08:** Foundry Local алат са 10 свеобухватних примера

### Спољне зависности
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Локално окружење за AI моделе са OpenAI-компатибилним API-јем
  - [Документација](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Оквир за оптимизацију
- [Microsoft Olive](https://microsoft.github.io/Olive/)
10. **10-Алатке за Foundry Framework** - Интеграција LangChain/Semantic Kernel

### Пример апликације за радионицу

Радионица укључује 6 прогресивних сесија са практичним имплементацијама:

1. **Сесија 01** - Покретање чета са интеграцијом Foundry Local
2. **Сесија 02** - RAG процес и евалуација са RAGAS
3. **Сесија 03** - Бенчмаркинг модела отвореног кода
4. **Сесија 04** - Поређење и избор модела
5. **Сесија 05** - Системи за оркестрацију више агената
6. **Сесија 06** - Рутање модела и управљање процесима

Сваки пример демонстрира различите аспекте развоја Edge AI-а са Foundry Local.

### Перформансе

- SLM-ови су оптимизовани за edge примену (2-16GB RAM-а)
- Локално закључивање пружа време одговора од 50-500ms
- Технике квантовања постижу смањење величине од 75% уз задржавање 85% перформанси
- Могућности за разговор у реалном времену са локалним моделима

### Безбедност и приватност

- Сва обрада се дешава локално - нема слања података у облак
- Погодно за апликације осетљиве на приватност (здравство, финансије)
- Испуњава захтеве за суверенитет података
- Foundry Local ради искључиво на локалном хардверу

## Помоћ

### Документација

- **Главни README**: [README.md](README.md) - Преглед репозиторијума и путеви учења
- **Водич за учење**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Ресурси за учење и временски оквир
- **Подршка**: [SUPPORT.md](SUPPORT.md) - Како добити помоћ
- **Безбедност**: [SECURITY.md](SECURITY.md) - Пријављивање безбедносних проблема

### Подршка заједнице

- **GitHub Issues**: [Пријавите грешке или затражите функције](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Поставите питања и поделите идеје](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Технички проблеми са Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Контакт

- **Одржаваоци**: Погледајте [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Безбедносни проблеми**: Пратите одговорно пријављивање у [SECURITY.md](SECURITY.md)
- **Microsoft подршка**: За подршку предузећима, контактирајте корисничку службу Microsoft-а

### Додатни ресурси

- **Microsoft Learn**: [Путеви учења за AI и машинско учење](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Документација Foundry Local**: [Званична документација](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Примери заједнице**: Погледајте [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) за доприносе заједнице

---

**Ово је едукативни репозиторијум фокусиран на подучавање развоја Edge AI-а. Примарни образац доприноса је побољшање едукативног садржаја и додавање/унапређење пример апликација које демонстрирају концепте Edge AI-а.**

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.