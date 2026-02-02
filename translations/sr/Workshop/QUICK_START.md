# Водич за брзи почетак радионице

## Предуслови

### 1. Инсталирајте Foundry Local

Пратите званични водич за инсталацију:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Инсталирајте Python зависности

Из директоријума радионице:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Покретање примера радионице

### Сесија 01: Основни разговор

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Променљиве окружења:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Сесија 02: RAG Платформа

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Променљиве окружења:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Сесија 02: RAG Евалуација (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Напомена**: Захтева додатне зависности инсталиране преко `requirements.txt`

### Сесија 03: Бенчмаркинг

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Променљиве окружења:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Излаз:** JSON са метрикама за кашњење, пропусност и време првог токена

### Сесија 04: Поређење модела

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Променљиве окружења:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Сесија 05: Оркестрација више агената

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Променљиве окружења:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Сесија 06: Рутер модела

```bash
cd Workshop/samples
python -m session06.models_router
```

**Тестира логичко рутирање** са више намера (код, сумирање, класификација)

### Сесија 06: Платформа

```bash
python -m session06.models_pipeline
```

**Комплексна платформа са више корака** укључујући планирање, извршење и усавршавање

## Скрипте

### Извоз извештаја бенчмарка

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Излаз:** Markdown табела + JSON метрике

### Линт CLI шаблона у Markdown-у

```bash
python lint_markdown_cli.py --verbose
```

**Сврха:** Откривање застарелих CLI шаблона у документацији

## Тестирање

### Основни тестови

```bash
cd Workshop
python -m tests.smoke
```

**Тестови:** Основна функционалност кључних примера

## Решавање проблема

### Услуга не ради

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Грешке при увозу модула

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Грешке у вези

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Модел није пронађен

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Референца променљивих окружења

### Основна конфигурација
| Променљива | Подразумевано | Опис |
|------------|---------------|------|
| `FOUNDRY_LOCAL_ALIAS` | Различито | Алијас модела који се користи |
| `FOUNDRY_LOCAL_ENDPOINT` | Аутоматски | Замена за крајњу тачку услуге |
| `SHOW_USAGE` | `0` | Приказ статистике коришћења токена |
| `RETRY_ON_FAIL` | `1` | Омогућава логику поновног покушаја |
| `RETRY_BACKOFF` | `1.0` | Почетно кашњење при поновном покушају (секунде) |

### Специфично за сесију
| Променљива | Подразумевано | Опис |
|------------|---------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модел за уграђивање |
| `RAG_QUESTION` | Погледајте пример | Питање за тестирање RAG-а |
| `BENCH_MODELS` | Различито | Модели одвојени зарезом |
| `BENCH_ROUNDS` | `3` | Итерације бенчмарка |
| `BENCH_PROMPT` | Погледајте пример | Подстицај за бенчмарк |
| `BENCH_STREAM` | `0` | Мерење кашњења првог токена |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Примарни модел агента |
| `AGENT_MODEL_EDITOR` | Примарни | Модел агента уредника |
| `SLM_ALIAS` | `phi-4-mini` | Мали језички модел |
| `LLM_ALIAS` | `qwen2.5-7b` | Велики језички модел |
| `COMPARE_PROMPT` | Погледајте пример | Подстицај за поређење |

## Препоручени модели

### Развој и тестирање
- **phi-4-mini** - Балансиран квалитет и брзина
- **qwen2.5-0.5b** - Веома брз за класификацију
- **gemma-2-2b** - Добар квалитет, умерена брзина

### Производни сценарији
- **phi-4-mini** - Општа намена
- **deepseek-coder-1.3b** - Генерисање кода
- **qwen2.5-7b** - Одговори високог квалитета

## SDK Документација

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## Добијање помоћи

1. Проверите статус услуге: `foundry service status`  
2. Прегледајте логове: Проверите логове услуге Foundry Local  
3. Проверите SDK документацију: https://github.com/microsoft/Foundry-Local  
4. Прегледајте пример кода: Сви примери имају детаљне коментаре  

## Следећи кораци

1. Завршите све сесије радионице редом  
2. Експериментишите са различитим моделима  
3. Прилагодите примере за своје случајеве  

---

**Последње ажурирање**: 2025-01-08  
**Верзија радионице**: Најновија  
**SDK**: Foundry Local Python SDK  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->