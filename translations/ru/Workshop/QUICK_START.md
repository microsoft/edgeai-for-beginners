<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T21:30:15+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ru"
}
-->
# Краткое руководство по началу работы с мастерской

## Предварительные требования

### 1. Установите Foundry Local

Следуйте официальному руководству по установке:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Установите зависимости Python

Из директории мастерской:

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

## Запуск примеров мастерской

### Сессия 01: Основной чат

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Переменные окружения:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Сессия 02: Конвейер RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Переменные окружения:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Сессия 02: Оценка RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Примечание**: Требуются дополнительные зависимости, установленные через `requirements.txt`

### Сессия 03: Бенчмаркинг

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Переменные окружения:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Вывод**: JSON с метриками задержки, пропускной способности и времени первого токена

### Сессия 04: Сравнение моделей

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Переменные окружения:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Сессия 05: Оркестрация нескольких агентов

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Переменные окружения:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Сессия 06: Маршрутизатор моделей

```bash
cd Workshop/samples
python -m session06.models_router
```

**Тестирует логику маршрутизации** для нескольких намерений (код, резюмирование, классификация)

### Сессия 06: Конвейер

```bash
python -m session06.models_pipeline
```

**Сложный многоэтапный конвейер** с планированием, выполнением и уточнением

## Скрипты

### Экспорт отчета о бенчмаркинге

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Вывод**: Таблица в формате Markdown + метрики JSON

### Проверка CLI шаблонов в Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Цель**: Обнаружение устаревших CLI шаблонов в документации

## Тестирование

### Тесты на дым

```bash
cd Workshop
python -m tests.smoke
```

**Тесты**: Основная функциональность ключевых примеров

## Устранение неполадок

### Сервис не запущен

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Ошибки импорта модулей

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ошибки подключения

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Модель не найдена

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Справочник по переменным окружения

### Основная конфигурация
| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Различается | Используемый псевдоним модели |
| `FOUNDRY_LOCAL_ENDPOINT` | Авто | Переопределение конечной точки сервиса |
| `SHOW_USAGE` | `0` | Показать статистику использования токенов |
| `RETRY_ON_FAIL` | `1` | Включить логику повторных попыток |
| `RETRY_BACKOFF` | `1.0` | Начальная задержка повторной попытки (в секундах) |

### Специфичные для сессии
| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модель для создания эмбеддингов |
| `RAG_QUESTION` | См. пример | Тестовый вопрос для RAG |
| `BENCH_MODELS` | Различается | Модели через запятую |
| `BENCH_ROUNDS` | `3` | Итерации бенчмаркинга |
| `BENCH_PROMPT` | См. пример | Запрос для бенчмаркинга |
| `BENCH_STREAM` | `0` | Измерение задержки первого токена |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Основная модель агента |
| `AGENT_MODEL_EDITOR` | Основная | Модель редактора агента |
| `SLM_ALIAS` | `phi-4-mini` | Малая языковая модель |
| `LLM_ALIAS` | `qwen2.5-7b` | Большая языковая модель |
| `COMPARE_PROMPT` | См. пример | Запрос для сравнения |

## Рекомендуемые модели

### Разработка и тестирование
- **phi-4-mini** - Сбалансированное качество и скорость
- **qwen2.5-0.5b** - Очень быстро для классификации
- **gemma-2-2b** - Хорошее качество, умеренная скорость

### Производственные сценарии
- **phi-4-mini** - Универсальное назначение
- **deepseek-coder-1.3b** - Генерация кода
- **qwen2.5-7b** - Высокое качество ответов

## Документация SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Получение помощи

1. Проверьте статус сервиса: `foundry service status`
2. Просмотрите логи: Проверьте логи сервиса Foundry Local
3. Ознакомьтесь с документацией SDK: https://github.com/microsoft/Foundry-Local
4. Изучите примеры кода: Все примеры содержат подробные комментарии

## Следующие шаги

1. Пройдите все сессии мастерской по порядку
2. Экспериментируйте с различными моделями
3. Модифицируйте примеры под свои задачи

---

**Последнее обновление**: 2025-01-08  
**Версия мастерской**: Последняя  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->