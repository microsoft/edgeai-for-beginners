<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-12T00:25:25+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "bg"
}
-->
# Примерни материали за работилница - Бърза справка

**Последна актуализация**: 8 октомври 2025 г.

---

## 🚀 Бърз старт

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

## 📂 Преглед на примерите

| Сесия | Пример | Цел | Време |
|-------|--------|-----|-------|
| 01 | `chat_bootstrap.py` | Основен чат + стрийминг | ~30 сек |
| 02 | `rag_pipeline.py` | RAG с вградени елементи | ~45 сек |
| 02 | `rag_eval_ragas.py` | Оценка на RAG | ~60 сек |
| 03 | `benchmark_oss_models.py` | Бенчмарк на модели | ~2 мин |
| 04 | `model_compare.py` | SLM срещу LLM | ~45 сек |
| 05 | `agents_orchestrator.py` | Система с множество агенти | ~60 сек |
| 06 | `models_router.py` | Насочване според намерение | ~45 сек |
| 06 | `models_pipeline.py` | Многоетапен процес | ~60 сек |

---

## 🛠️ Променливи на средата

### Основни
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Специфични за сесията
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

## ✅ Валидация и тестване

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

## 🐛 Отстраняване на проблеми

### Грешка при свързване
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Грешка при импортиране
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Моделът не е намерен
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Бавна производителност
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Често срещани шаблони

### Основен чат
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Получаване на клиент
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Обработка на грешки
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Стрийминг
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

## 📊 Избор на модел

| Модел | Размер | Най-добър за | Скорост |
|-------|--------|-------------|---------|
| `qwen2.5-0.5b` | 0.5B | Бърза класификация | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Бързо генериране на код | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Креативно писане | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Код, рефакторинг | ⚡⚡ |
| `phi-4-mini` | 4B | Общи задачи, обобщение | ⚡⚡ |
| `qwen2.5-7b` | 7B | Сложно разсъждение | ⚡ |

---

## 🔗 Ресурси

- **Документация за SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Бърза справка**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Съвети

1. **Кеширайте клиентите**: `workshop_utils` го прави вместо вас
2. **Използвайте по-малки модели**: Започнете с `qwen2.5-0.5b` за тестване
3. **Активирайте статистика за използване**: Задайте `SHOW_USAGE=1`, за да следите токените
4. **Партидна обработка**: Обработвайте множество заявки последователно
5. **Намалете max_tokens**: Намалява латентността за бързи отговори

---

## 🎯 Примерни работни процеси

### Тествайте всичко
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Бенчмарк на модели
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG процес
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Система с множество агенти
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Бърза помощ**: Стартирайте всеки пример с `--help` от директорията `samples` или проверете docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Всички примери са актуализирани през октомври 2025 г. с най-добрите практики на Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->