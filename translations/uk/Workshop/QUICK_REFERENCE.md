<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T23:44:31+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "uk"
}
-->
# Зразки для воркшопу - Швидка довідкова картка

**Останнє оновлення**: 8 жовтня 2025 року

---

## 🚀 Швидкий старт

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

## 📂 Огляд зразків

| Сесія | Зразок | Призначення | Час |
|-------|--------|-------------|------|
| 01 | `chat_bootstrap.py` | Базовий чат + стрімінг | ~30с |
| 02 | `rag_pipeline.py` | RAG з ембедингами | ~45с |
| 02 | `rag_eval_ragas.py` | Оцінка RAG | ~60с |
| 03 | `benchmark_oss_models.py` | Бенчмаркінг моделей | ~2хв |
| 04 | `model_compare.py` | SLM vs LLM | ~45с |
| 05 | `agents_orchestrator.py` | Система з багатьма агентами | ~60с |
| 06 | `models_router.py` | Роутинг намірів | ~45с |
| 06 | `models_pipeline.py` | Багатокроковий конвеєр | ~60с |

---

## 🛠️ Змінні середовища

### Основні
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Специфічні для сесії
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

## ✅ Валідація та тестування

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

## 🐛 Виправлення помилок

### Помилка з'єднання
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Помилка імпорту
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Модель не знайдена
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Повільна продуктивність
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Загальні шаблони

### Базовий чат
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Отримання клієнта
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Обробка помилок
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Стрімінг
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

## 📊 Вибір моделі

| Модель | Розмір | Найкраще для | Швидкість |
|--------|--------|--------------|-----------|
| `qwen2.5-0.5b` | 0.5B | Швидка класифікація | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Швидке генерування коду | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Креативне письмо | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Код, рефакторинг | ⚡⚡ |
| `phi-4-mini` | 4B | Загальне, резюме | ⚡⚡ |
| `qwen2.5-7b` | 7B | Складне мислення | ⚡ |

---

## 🔗 Ресурси

- **Документація SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Швидка довідка**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Оновлення**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Примітки щодо міграції**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Поради

1. **Кешуйте клієнтів**: `workshop_utils` робить це за вас
2. **Використовуйте менші моделі**: Починайте з `qwen2.5-0.5b` для тестування
3. **Увімкніть статистику використання**: Встановіть `SHOW_USAGE=1`, щоб відстежувати токени
4. **Пакетна обробка**: Обробляйте кілька запитів послідовно
5. **Зменшіть max_tokens**: Знижує затримку для швидких відповідей

---

## 🎯 Робочі процеси зразків

### Тестування всього
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Бенчмаркінг моделей
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG-конвеєр
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Система з багатьма агентами
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Швидка допомога**: Запустіть будь-який зразок з `--help` з каталогу `samples` або перегляньте docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Усі зразки оновлені у жовтні 2025 року відповідно до найкращих практик Foundry Local SDK** ✨

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.