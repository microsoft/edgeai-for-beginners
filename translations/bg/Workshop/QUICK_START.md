# Бързо ръководство за работилницата

## Предварителни изисквания

### 1. Инсталирайте Foundry Local

Следвайте официалното ръководство за инсталация:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Инсталирайте Python зависимости

От директорията на работилницата:

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

## Стартиране на примери от работилницата

### Сесия 01: Основен чат

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Променливи на средата:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Сесия 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Променливи на средата:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Сесия 02: Оценка на RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Забележка**: Изисква допълнителни зависимости, инсталирани чрез `requirements.txt`

### Сесия 03: Бенчмаркинг

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Променливи на средата:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Резултат**: JSON с метрики за латентност, пропускателна способност и първи токен

### Сесия 04: Сравнение на модели

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Променливи на средата:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Сесия 05: Оркестрация на много агенти

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Променливи на средата:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Сесия 06: Маршрутизатор на модели

```bash
cd Workshop/samples
python -m session06.models_router
```

**Тества логиката на маршрутизация** с множество намерения (код, обобщение, класификация)

### Сесия 06: Пайплайн

```bash
python -m session06.models_pipeline
```

**Комплексен многоетапен пайплайн** с планиране, изпълнение и усъвършенстване

## Скриптове

### Експорт на бенчмарк отчет

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Резултат**: Таблица в Markdown + JSON метрики

### Линт CLI шаблони в Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Цел**: Откриване на остарели CLI шаблони в документацията

## Тестване

### Smoke тестове

```bash
cd Workshop
python -m tests.smoke
```

**Тестове**: Основна функционалност на ключови примери

## Отстраняване на проблеми

### Услугата не работи

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Грешки при импортиране на модули

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Грешки при свързване

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Моделът не е намерен

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Референция за променливи на средата

### Основна конфигурация
| Променлива | По подразбиране | Описание |
|------------|----------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Различно | Алиас на модела за използване |
| `FOUNDRY_LOCAL_ENDPOINT` | Автоматично | Замяна на крайна точка на услугата |
| `SHOW_USAGE` | `0` | Показване на статистика за използване на токени |
| `RETRY_ON_FAIL` | `1` | Активиране на логика за повторение |
| `RETRY_BACKOFF` | `1.0` | Начално забавяне при повторение (секунди) |

### Специфични за сесията
| Променлива | По подразбиране | Описание |
|------------|----------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модел за вграждане |
| `RAG_QUESTION` | Вижте примера | Тестов въпрос за RAG |
| `BENCH_MODELS` | Различно | Модели, разделени със запетая |
| `BENCH_ROUNDS` | `3` | Итерации за бенчмарк |
| `BENCH_PROMPT` | Вижте примера | Подканващ текст за бенчмарк |
| `BENCH_STREAM` | `0` | Измерване на латентност на първия токен |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Основен модел на агент |
| `AGENT_MODEL_EDITOR` | Основен | Модел на агент редактор |
| `SLM_ALIAS` | `phi-4-mini` | Малък езиков модел |
| `LLM_ALIAS` | `qwen2.5-7b` | Голям езиков модел |
| `COMPARE_PROMPT` | Вижте примера | Подканващ текст за сравнение |

## Препоръчани модели

### Разработка и тестване
- **phi-4-mini** - Балансирано качество и скорост
- **qwen2.5-0.5b** - Много бърз за класификация
- **gemma-2-2b** - Добро качество, умерена скорост

### Производствени сценарии
- **phi-4-mini** - Общи цели
- **deepseek-coder-1.3b** - Генериране на код
- **qwen2.5-7b** - Висококачествени отговори

## SDK документация

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Получаване на помощ

1. Проверете статуса на услугата: `foundry service status`
2. Прегледайте логовете: Проверете логовете на услугата Foundry Local
3. Проверете SDK документацията: https://github.com/microsoft/Foundry-Local
4. Прегледайте примерния код: Всички примери имат подробни коментари

## Следващи стъпки

1. Завършете всички сесии от работилницата по ред
2. Експериментирайте с различни модели
3. Модифицирайте примерите за вашите нужди

---

**Последно обновено**: 2025-01-08  
**Версия на работилницата**: Най-нова  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->