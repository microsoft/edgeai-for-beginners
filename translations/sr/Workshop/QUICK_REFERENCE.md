<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T23:23:26+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "sr"
}
-->
# Пример радионице - Брза референтна карта

**Последње ажурирање**: 8. октобар 2025.

---

## 🚀 Брзи почетак

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

## 📂 Преглед примера

| Сесија | Пример | Сврха | Време |
|--------|--------|-------|-------|
| 01 | `chat_bootstrap.py` | Основни чет + стриминг | ~30с |
| 02 | `rag_pipeline.py` | RAG са уграђивањем | ~45с |
| 02 | `rag_eval_ragas.py` | Евалуација RAG-а | ~60с |
| 03 | `benchmark_oss_models.py` | Бенчмаркинг модела | ~2м |
| 04 | `model_compare.py` | SLM vs LLM | ~45с |
| 05 | `agents_orchestrator.py` | Систем са више агената | ~60с |
| 06 | `models_router.py` | Рутање намере | ~45с |
| 06 | `models_pipeline.py` | Вишестепени процес | ~60с |

---

## 🛠️ Променљиве окружења

### Основне
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Специфичне за сесију
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

## ✅ Валидација и тестирање

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

## 🐛 Решавање проблема

### Грешка у конекцији
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Грешка при увозу
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Модел није пронађен
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Спор перформанс
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Уобичајени обрасци

### Основни чет
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Добијање клијента
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Руководење грешкама
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Стриминг
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

## 📊 Избор модела

| Модел | Величина | Најбоље за | Брзина |
|-------|----------|------------|--------|
| `qwen2.5-0.5b` | 0.5B | Брза класификација | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Брза генерација кода | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Креативно писање | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Код, рефакторинг | ⚡⚡ |
| `phi-4-mini` | 4B | Опште, резиме | ⚡⚡ |
| `qwen2.5-7b` | 7B | Комплексно резоновање | ⚡ |

---

## 🔗 Ресурси

- **SDK документација**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Брза референца**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Резиме ажурирања**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Белешке о миграцији**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Савети

1. **Кеширајте клијенте**: `workshop_utils` то ради за вас
2. **Користите мање моделе**: Почните са `qwen2.5-0.5b` за тестирање
3. **Омогућите статистику коришћења**: Поставите `SHOW_USAGE=1` за праћење токена
4. **Обрада у серијама**: Обрадите више упита узастопно
5. **Смањите max_tokens**: Смањује кашњење за брзе одговоре

---

## 🎯 Радни токови примера

### Тестирајте све
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Бенчмаркинг модела
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

### Систем са више агената
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Брза помоћ**: Покрените било који пример са `--help` из директоријума `samples` или погледајте docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Сви примери ажурирани октобра 2025. са најбољим праксама Foundry Local SDK-а** ✨

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.