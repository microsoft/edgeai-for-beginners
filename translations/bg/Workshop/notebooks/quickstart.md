# Ръководство за бърз старт - Работни тетрадки

## Съдържание

- [Предварителни условия](../../../../Workshop/notebooks)
- [Първоначална настройка](../../../../Workshop/notebooks)
- [Сесия 04: Сравнение на модели](../../../../Workshop/notebooks)
- [Сесия 05: Оркестратор с множество агенти](../../../../Workshop/notebooks)
- [Сесия 06: Маршрутизиране на модели на база намерение](../../../../Workshop/notebooks)
- [Променливи на средата](../../../../Workshop/notebooks)
- [Често използвани команди](../../../../Workshop/notebooks)

---

## Предварителни условия

### 1. Инсталирайте Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Проверка на инсталацията:**
```bash
foundry --version
```

### 2. Инсталирайте Python зависимости

```bash
cd Workshop
pip install -r requirements.txt
```

Или инсталирайте поотделно:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Първоначална настройка

### Стартиране на Foundry Local Service

**Необходимо преди изпълнение на която и да е тетрадка:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Очакван изход:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Изтегляне и зареждане на модели

Тетрадките използват тези модели по подразбиране:

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

### Проверка на настройката

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Сесия 04: Сравнение на модели

### Цел
Сравнение на производителността между малки езикови модели (SLM) и големи езикови модели (LLM).

### Бърза настройка

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Изпълнение на тетрадката

1. **Отворете** `session04_model_compare.ipynb` във VS Code или Jupyter
2. **Рестартирайте ядрото** (Kernel → Restart Kernel)
3. **Изпълнете всички клетки** по ред

### Основна конфигурация

**Модели по подразбиране:**
- **SLM:** `phi-4-mini` (~4GB RAM, по-бърз)
- **LLM:** `qwen2.5-3b` (~3GB RAM, оптимизиран за памет)

**Променливи на средата (по избор):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Очакван изход

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

### Персонализация

**Използване на различни модели:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Персонализиран prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Контролен списък за валидиране

- [ ] Клетка 12 показва правилните модели (phi-4-mini, qwen2.5-3b)
- [ ] Клетка 12 показва правилния endpoint (порт 59959)
- [ ] Диагностиката в клетка 16 преминава (✅ Услугата работи)
- [ ] Предварителната проверка в клетка 20 преминава (и двата модела са наред)
- [ ] Сравнението в клетка 22 завършва с латентност стойности
- [ ] Валидирането в клетка 24 показва 🎉 ВСИЧКИ ПРОВЕРКИ ПРЕМИНАХА!

### Оценка на времето
- **Първо изпълнение:** 5-10 минути (включително изтегляне на модели)
- **Следващи изпълнения:** 1-2 минути

---

## Сесия 05: Оркестратор с множество агенти

### Цел
Демонстрация на сътрудничество между множество агенти с Foundry Local SDK - агентите работят заедно за създаване на усъвършенствани резултати.

### Бърза настройка

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Изпълнение на тетрадката

1. **Отворете** `session05_agents_orchestrator.ipynb`
2. **Рестартирайте ядрото**
3. **Изпълнете всички клетки** по ред

### Основна конфигурация

**Настройка по подразбиране (един и същ модел за двата агента):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Разширена настройка (различни модели):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Архитектура

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

### Очакван изход

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

### Разширения

**Добавяне на повече агенти:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Тестване на партиди:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Оценка на времето
- **Първо изпълнение:** 3-5 минути
- **Следващи изпълнения:** 1-2 минути на въпрос

---

## Сесия 06: Маршрутизиране на модели на база намерение

### Цел
Интелигентно маршрутизиране на prompt-ове към специализирани модели въз основа на откритото намерение.

### Бърза настройка

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Забележка:** Сесия 06 използва CPU модели по подразбиране за максимална съвместимост.

### Изпълнение на тетрадката

1. **Отворете** `session06_models_router.ipynb`
2. **Рестартирайте ядрото**
3. **Изпълнете всички клетки** по ред

### Основна конфигурация

**Каталог по подразбиране (CPU модели):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Алтернатива (GPU модели):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Откриване на намерение

Маршрутизаторът използва regex шаблони за откриване на намерение:

| Намерение | Примери за шаблони | Маршрутизирано към |
|-----------|--------------------|--------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Всичко останало | phi-4-mini-cpu |

### Очакван изход

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

### Персонализация

**Добавяне на персонализирано намерение:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Активиране на проследяване на токени:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Превключване към GPU модели

Ако разполагате с 8GB+ VRAM:

1. В **Клетка #6**, коментирайте CPU каталога
2. Откоментирайте GPU каталога
3. Заредете GPU модели:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Рестартирайте ядрото и изпълнете тетрадката отново

### Оценка на времето
- **Първо изпълнение:** 5-10 минути (зареждане на модели)
- **Следващи изпълнения:** 30-60 секунди на тест

---

## Променливи на средата

### Глобална конфигурация

Настройте преди стартиране на Jupyter/VS Code:

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

### Конфигурация в тетрадка

Настройте в началото на всяка тетрадка:

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

## Често използвани команди

### Управление на услугата

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

### Управление на модели

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

### Тестване на endpoints

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

### Диагностични команди

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

## Най-добри практики

### Преди стартиране на която и да е тетрадка

1. **Проверете дали услугата работи:**
   ```bash
   foundry service status
   ```

2. **Уверете се, че моделите са заредени:**
   ```bash
   foundry model ls
   ```

3. **Рестартирайте ядрото на тетрадката**, ако я изпълнявате повторно

4. **Изчистете всички изходи** за чисто изпълнение

### Управление на ресурси

1. **Използвайте CPU модели по подразбиране** за съвместимост
2. **Превключете към GPU модели** само ако разполагате с 8GB+ VRAM
3. **Затворете други GPU приложения** преди изпълнение
4. **Поддържайте услугата активна** между сесиите на тетрадките
5. **Следете използването на ресурси** с Task Manager / nvidia-smi

### Отстраняване на проблеми

1. **Винаги проверявайте услугата първо**, преди да дебъгвате кода
2. **Рестартирайте ядрото**, ако видите остаряла конфигурация
3. **Изпълнете диагностичните клетки** след всяка промяна
4. **Уверете се, че имената на моделите** съвпадат с заредените
5. **Проверете порта на endpoint**, за да съответства на състоянието на услугата

---

## Бърза справка: Алиаси на модели

### Често използвани модели

| Алиас | Размер | Най-добро за | RAM/VRAM | Варианти |
|-------|--------|--------------|----------|----------|
| `phi-4-mini` | ~4B | Общ чат, обобщение | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Генериране на код, рефакторинг | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Общи задачи, ефективен | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Бърз, ниски ресурси | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Класификация, минимални ресурси | 1-2GB | `-cpu`, `-cuda-gpu` |

### Именуване на варианти

- **Основно име** (например, `phi-4-mini`): Автоматично избира най-добрия вариант за вашия хардуер
- **`-cpu`**: Оптимизиран за CPU, работи навсякъде
- **`-cuda-gpu`**: Оптимизиран за NVIDIA GPU, изисква 8GB+ VRAM
- **`-npu`**: Оптимизиран за Qualcomm NPU, изисква NPU драйвери

**Препоръка:** Използвайте основните имена (без суфикс) и оставете Foundry Local да избере най-добрия вариант.

---

## Индикатори за успех

Готови сте, когато видите:

✅ `foundry service status` показва "running"
✅ `foundry model ls` показва необходимите модели
✅ Услугата е достъпна на правилния endpoint
✅ Проверка на здравето връща 200 OK
✅ Диагностичните клетки в тетрадката преминават
✅ Няма грешки при свързване в изхода

---

## Получаване на помощ

### Документация
- **Основно хранилище**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI референция**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Отстраняване на проблеми**: Вижте `troubleshooting.md` в тази директория

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Последна актуализация:** 8 октомври 2025 г.
**Версия:** Работни тетрадки 2.0

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.