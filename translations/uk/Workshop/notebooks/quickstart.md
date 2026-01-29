# Зошити для воркшопу - Короткий посібник

## Зміст

- [Попередні вимоги](../../../../Workshop/notebooks)
- [Початкова настройка](../../../../Workshop/notebooks)
- [Сесія 04: Порівняння моделей](../../../../Workshop/notebooks)
- [Сесія 05: Оркестратор багатозадачних агентів](../../../../Workshop/notebooks)
- [Сесія 06: Маршрутизація моделей на основі намірів](../../../../Workshop/notebooks)
- [Змінні середовища](../../../../Workshop/notebooks)
- [Загальні команди](../../../../Workshop/notebooks)

---

## Попередні вимоги

### 1. Встановіть Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Перевірка встановлення:**
```bash
foundry --version
```

### 2. Встановіть залежності Python

```bash
cd Workshop
pip install -r requirements.txt
```

Або встановіть окремо:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Початкова настройка

### Запуск локального сервісу Foundry

**Необхідно перед запуском будь-якого зошита:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Очікуваний результат:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Завантаження та завантаження моделей

Зошити за замовчуванням використовують ці моделі:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Перевірка налаштувань

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Сесія 04: Порівняння моделей

### Мета
Порівняти продуктивність між малими мовними моделями (SLM) та великими мовними моделями (LLM).

### Швидка настройка

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Запуск зошита

1. **Відкрийте** `session04_model_compare.ipynb` у VS Code або Jupyter
2. **Перезапустіть ядро** (Kernel → Restart Kernel)
3. **Запустіть усі комірки** по порядку

### Основна конфігурація

**Моделі за замовчуванням:**
- **SLM:** `phi-4-mini` (~4GB RAM, швидше)
- **LLM:** `qwen2.5-3b` (~3GB RAM, оптимізовано для пам'яті)

**Змінні середовища (опціонально):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Очікуваний результат

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Налаштування

**Використання інших моделей:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Користувацький запит:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Контрольний список перевірки

- [ ] У комірці 12 відображаються правильні моделі (phi-4-mini, qwen2.5-3b)
- [ ] У комірці 12 відображається правильний кінцевий пункт (порт 59959)
- [ ] Діагностика в комірці 16 проходить (✅ Сервіс працює)
- [ ] Перевірка перед запуском у комірці 20 проходить (обидві моделі ок)
- [ ] Порівняння в комірці 22 завершується з показниками затримки
- [ ] Перевірка в комірці 24 показує 🎉 УСІ ПЕРЕВІРКИ ПРОЙДЕНО!

### Оцінка часу
- **Перший запуск:** 5-10 хвилин (включаючи завантаження моделей)
- **Наступні запуски:** 1-2 хвилини

---

## Сесія 05: Оркестратор багатозадачних агентів

### Мета
Демонстрація співпраці багатозадачних агентів за допомогою Foundry Local SDK - агенти працюють разом для створення вдосконалених результатів.

### Швидка настройка

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Запуск зошита

1. **Відкрийте** `session05_agents_orchestrator.ipynb`
2. **Перезапустіть ядро**
3. **Запустіть усі комірки** по порядку

### Основна конфігурація

**Налаштування за замовчуванням (однакова модель для обох агентів):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Розширене налаштування (різні моделі):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Архітектура

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Очікуваний результат

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Розширення

**Додати більше агентів:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Тестування пакетів:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Оцінка часу
- **Перший запуск:** 3-5 хвилин
- **Наступні запуски:** 1-2 хвилини на запитання

---

## Сесія 06: Маршрутизація моделей на основі намірів

### Мета
Інтелектуально направляти запити до спеціалізованих моделей на основі виявлених намірів.

### Швидка настройка

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Примітка:** Сесія 06 за замовчуванням використовує моделі для CPU для максимальної сумісності.

### Запуск зошита

1. **Відкрийте** `session06_models_router.ipynb`
2. **Перезапустіть ядро**
3. **Запустіть усі комірки** по порядку

### Основна конфігурація

**Каталог за замовчуванням (моделі для CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Альтернатива (моделі для GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Виявлення намірів

Маршрутизатор використовує шаблони regex для виявлення намірів:

| Намір | Приклади шаблонів | Направлено до |
|-------|-------------------|---------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Все інше | phi-4-mini-cpu |

### Очікуваний результат

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Налаштування

**Додати користувацький намір:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Увімкнути відстеження токенів:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Перехід на моделі для GPU

Якщо у вас є 8GB+ VRAM:

1. У **комірці #6** закоментуйте каталог для CPU
2. Розкоментуйте каталог для GPU
3. Завантажте моделі для GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Перезапустіть ядро та повторно запустіть зошит

### Оцінка часу
- **Перший запуск:** 5-10 хвилин (завантаження моделей)
- **Наступні запуски:** 30-60 секунд на тест

---

## Змінні середовища

### Глобальна конфігурація

Встановіть перед запуском Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Конфігурація в зошиті

Встановіть на початку будь-якого зошита:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Загальні команди

### Управління сервісом

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Управління моделями

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Тестування кінцевих точок

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Діагностичні команди

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Найкращі практики

### Перед запуском будь-якого зошита

1. **Перевірте, чи сервіс працює:**
   ```bash
   foundry service status
   ```

2. **Переконайтеся, що моделі завантажені:**
   ```bash
   foundry model ls
   ```

3. **Перезапустіть ядро зошита**, якщо повторно запускаєте

4. **Очистіть усі результати** для чистого запуску

### Управління ресурсами

1. **Використовуйте моделі для CPU за замовчуванням** для сумісності
2. **Переключіться на моделі для GPU**, якщо у вас є 8GB+ VRAM
3. **Закрийте інші програми для GPU** перед запуском
4. **Тримайте сервіс запущеним** між сесіями зошитів
5. **Моніторьте використання ресурсів** за допомогою Task Manager / nvidia-smi

### Вирішення проблем

1. **Завжди перевіряйте сервіс спочатку**, перед налагодженням коду
2. **Перезапустіть ядро**, якщо бачите застарілу конфігурацію
3. **Повторно запустіть діагностичні комірки** після будь-яких змін
4. **Перевірте назви моделей**, щоб вони відповідали завантаженим
5. **Переконайтеся, що порт кінцевої точки** відповідає статусу сервісу

---

## Швидка довідка: Аліаси моделей

### Загальні моделі

| Аліас | Розмір | Найкраще для | RAM/VRAM | Варіанти |
|-------|--------|--------------|----------|----------|
| `phi-4-mini` | ~4B | Загальний чат, підсумовування | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Генерація коду, рефакторинг | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Загальні завдання, ефективність | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Швидкість, низькі ресурси | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Класифікація, мінімальні ресурси | 1-2GB | `-cpu`, `-cuda-gpu` |

### Назви варіантів

- **Базова назва** (наприклад, `phi-4-mini`): Автоматично вибирає найкращий варіант для вашого обладнання
- **`-cpu`**: Оптимізовано для CPU, працює скрізь
- **`-cuda-gpu`**: Оптимізовано для NVIDIA GPU, потребує 8GB+ VRAM
- **`-npu`**: Оптимізовано для Qualcomm NPU, потребує драйверів NPU

**Рекомендація:** Використовуйте базові назви (без суфіксів) і дозвольте Foundry Local автоматично вибирати найкращий варіант.

---

## Індикатори успіху

Ви готові, якщо бачите:

✅ `foundry service status` показує "running"  
✅ `foundry model ls` показує необхідні моделі  
✅ Сервіс доступний за правильною кінцевою точкою  
✅ Перевірка стану повертає 200 OK  
✅ Діагностичні комірки зошита проходять  
✅ Немає помилок з'єднання у результатах  

---

## Отримання допомоги

### Документація
- **Основний репозиторій**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Вирішення проблем**: Див. `troubleshooting.md` у цьому каталозі

### Проблеми на GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Останнє оновлення:** 8 жовтня 2025  
**Версія:** Workshop Notebooks 2.0

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.