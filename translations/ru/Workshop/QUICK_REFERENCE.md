<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:16:54+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ru"
}
-->
# Образцы для мастерской - Краткая справочная карта

**Последнее обновление**: 8 октября 2025 года

---

## 🚀 Быстрый старт

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Обзор образцов

| Сессия | Образец | Назначение | Время |
|--------|---------|------------|-------|
| 01 | `chat_bootstrap.py` | Базовый чат + потоковая передача | ~30с |
| 02 | `rag_pipeline.py` | RAG с эмбеддингами | ~45с |
| 02 | `rag_eval_ragas.py` | Оценка RAG | ~60с |
| 03 | `benchmark_oss_models.py` | Сравнение моделей | ~2м |
| 04 | `model_compare.py` | SLM vs LLM | ~45с |
| 05 | `agents_orchestrator.py` | Система с несколькими агентами | ~60с |
| 06 | `models_router.py` | Маршрутизация намерений | ~45с |
| 06 | `models_pipeline.py` | Многошаговый конвейер | ~60с |

---

## 🛠️ Переменные окружения

### Основные
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Специфичные для сессии
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Проверка и тестирование

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Устранение неполадок

### Ошибка подключения
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Ошибка импорта
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Модель не найдена
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Низкая производительность
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Общие шаблоны

### Базовый чат
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Получение клиента
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Обработка ошибок
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Потоковая передача
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Выбор модели

| Модель | Размер | Лучшее применение | Скорость |
|--------|--------|-------------------|----------|
| `qwen2.5-0.5b` | 0.5B | Быстрая классификация | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Быстрая генерация кода | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Креативное письмо | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Код, рефакторинг | ⚡⚡ |
| `phi-4-mini` | 4B | Общее, резюме | ⚡⚡ |
| `qwen2.5-7b` | 7B | Сложное рассуждение | ⚡ |

---

## 🔗 Ресурсы

- **Документация SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Краткая справка**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Сводка обновлений**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Примечания по миграции**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Советы

1. **Кэшируйте клиентов**: `workshop_utils` делает это за вас
2. **Используйте меньшие модели**: Начните с `qwen2.5-0.5b` для тестирования
3. **Включите статистику использования**: Установите `SHOW_USAGE=1` для отслеживания токенов
4. **Пакетная обработка**: Обрабатывайте несколько запросов последовательно
5. **Уменьшите max_tokens**: Снижает задержку для быстрых ответов

---

## 🎯 Рабочие процессы образцов

### Тестирование всего
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Сравнение моделей
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG-конвейер
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Система с несколькими агентами
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Быстрая помощь**: Запустите любой образец с `--help` из директории `samples` или ознакомьтесь с docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Все образцы обновлены в октябре 2025 года с учетом лучших практик Foundry Local SDK** ✨

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.