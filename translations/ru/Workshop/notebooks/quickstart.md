# Рабочие тетради - Краткое руководство

## Содержание

- [Предварительные требования](../../../../Workshop/notebooks)
- [Первоначальная настройка](../../../../Workshop/notebooks)
- [Сессия 04: Сравнение моделей](../../../../Workshop/notebooks)
- [Сессия 05: Оркестратор многоагентных систем](../../../../Workshop/notebooks)
- [Сессия 06: Маршрутизация моделей на основе намерений](../../../../Workshop/notebooks)
- [Переменные окружения](../../../../Workshop/notebooks)
- [Общие команды](../../../../Workshop/notebooks)

---

## Предварительные требования

### 1. Установите Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Проверка установки:**
```bash
foundry --version
```

### 2. Установите зависимости Python

```bash
cd Workshop
pip install -r requirements.txt
```

Или установите по отдельности:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Первоначальная настройка

### Запуск локального сервиса Foundry

**Необходимо перед запуском любой тетради:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Ожидаемый результат:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Загрузка и подключение моделей

Тетради используют следующие модели по умолчанию:

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

### Проверка настройки

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Сессия 04: Сравнение моделей

### Цель
Сравнение производительности между малыми языковыми моделями (SLM) и большими языковыми моделями (LLM).

### Быстрая настройка

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Запуск тетради

1. **Откройте** `session04_model_compare.ipynb` в VS Code или Jupyter
2. **Перезапустите ядро** (Kernel → Restart Kernel)
3. **Запустите все ячейки** по порядку

### Основная конфигурация

**Модели по умолчанию:**
- **SLM:** `phi-4-mini` (~4 ГБ ОЗУ, быстрее)
- **LLM:** `qwen2.5-3b` (~3 ГБ ОЗУ, оптимизировано по памяти)

**Переменные окружения (опционально):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Ожидаемый результат

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

### Настройка

**Использование других моделей:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Пользовательский запрос:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Контрольный список проверки

- [ ] В ячейке 12 отображаются правильные модели (phi-4-mini, qwen2.5-3b)
- [ ] В ячейке 12 указан правильный конечный пункт (порт 59959)
- [ ] Диагностика в ячейке 16 проходит успешно (✅ Сервис работает)
- [ ] Предварительная проверка в ячейке 20 проходит успешно (обе модели в порядке)
- [ ] Сравнение в ячейке 22 завершается с показателями задержки
- [ ] Проверка в ячейке 24 показывает 🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!

### Оценка времени
- **Первый запуск:** 5-10 минут (включая загрузку моделей)
- **Последующие запуски:** 1-2 минуты

---

## Сессия 05: Оркестратор многоагентных систем

### Цель
Демонстрация совместной работы нескольких агентов с использованием Foundry Local SDK - агенты работают вместе для получения улучшенных результатов.

### Быстрая настройка

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Запуск тетради

1. **Откройте** `session05_agents_orchestrator.ipynb`
2. **Перезапустите ядро**
3. **Запустите все ячейки** по порядку

### Основная конфигурация

**Настройка по умолчанию (одна модель для обоих агентов):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Расширенная настройка (разные модели):**
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

### Ожидаемый результат

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

### Расширения

**Добавление дополнительных агентов:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Тестирование пакетами:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Оценка времени
- **Первый запуск:** 3-5 минут
- **Последующие запуски:** 1-2 минуты на вопрос

---

## Сессия 06: Маршрутизация моделей на основе намерений

### Цель
Интеллектуальная маршрутизация запросов к специализированным моделям на основе обнаруженных намерений.

### Быстрая настройка

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Примечание:** Сессия 06 использует модели на CPU для максимальной совместимости.

### Запуск тетради

1. **Откройте** `session06_models_router.ipynb`
2. **Перезапустите ядро**
3. **Запустите все ячейки** по порядку

### Основная конфигурация

**Каталог по умолчанию (модели на CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Альтернатива (модели на GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Обнаружение намерений

Маршрутизатор использует шаблоны регулярных выражений для определения намерений:

| Намерение | Примеры шаблонов | Маршрутизируется к |
|-----------|------------------|--------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Все остальное | phi-4-mini-cpu |

### Ожидаемый результат

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

### Настройка

**Добавление пользовательских намерений:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Включение отслеживания токенов:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Переключение на модели GPU

Если у вас есть 8 ГБ+ видеопамяти:

1. В **ячейке #6** закомментируйте каталог CPU
2. Раскомментируйте каталог GPU
3. Загрузите модели GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Перезапустите ядро и повторно запустите тетрадь

### Оценка времени
- **Первый запуск:** 5-10 минут (загрузка моделей)
- **Последующие запуски:** 30-60 секунд на тест

---

## Переменные окружения

### Глобальная конфигурация

Установите перед запуском Jupyter/VS Code:

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

### Конфигурация в тетради

Установите в начале любой тетради:

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

## Общие команды

### Управление сервисом

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

### Управление моделями

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

### Тестирование конечных точек

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

### Диагностические команды

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

## Лучшие практики

### Перед запуском любой тетради

1. **Проверьте, что сервис работает:**
   ```bash
   foundry service status
   ```

2. **Убедитесь, что модели загружены:**
   ```bash
   foundry model ls
   ```

3. **Перезапустите ядро тетради**, если запускаете повторно

4. **Очистите все выводы** для чистого запуска

### Управление ресурсами

1. **Используйте модели на CPU по умолчанию** для совместимости
2. **Переключайтесь на модели GPU** только если у вас есть 8 ГБ+ видеопамяти
3. **Закройте другие приложения, использующие GPU**, перед запуском
4. **Держите сервис запущенным** между сессиями тетрадей
5. **Следите за использованием ресурсов** через Диспетчер задач / nvidia-smi

### Устранение неполадок

1. **Всегда сначала проверяйте сервис**, прежде чем отлаживать код
2. **Перезапустите ядро**, если видите устаревшую конфигурацию
3. **Повторно запустите диагностические ячейки** после любых изменений
4. **Убедитесь, что имена моделей** совпадают с загруженными
5. **Проверьте порт конечной точки**, чтобы он совпадал с состоянием сервиса

---

## Быстрая справка: псевдонимы моделей

### Популярные модели

| Псевдоним | Размер | Лучшее применение | ОЗУ/видеопамять | Варианты |
|-----------|--------|-------------------|-----------------|----------|
| `phi-4-mini` | ~4B | Общение, суммирование | 4-6 ГБ | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Генерация кода, рефакторинг | 3-5 ГБ | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Общие задачи, эффективность | 3-4 ГБ | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Быстро, мало ресурсов | 2-3 ГБ | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Классификация, минимальные ресурсы | 1-2 ГБ | `-cpu`, `-cuda-gpu` |

### Названия вариантов

- **Базовое название** (например, `phi-4-mini`): Автоматически выбирает лучший вариант для вашего оборудования
- **`-cpu`**: Оптимизировано для CPU, работает везде
- **`-cuda-gpu`**: Оптимизировано для NVIDIA GPU, требуется 8 ГБ+ видеопамяти
- **`-npu`**: Оптимизировано для Qualcomm NPU, требуется драйвер NPU

**Рекомендация:** Используйте базовые названия (без суффиксов), чтобы Foundry Local автоматически выбирал лучший вариант.

---

## Индикаторы успеха

Вы готовы, если:

✅ `foundry service status` показывает "running"  
✅ `foundry model ls` показывает необходимые модели  
✅ Сервис доступен по правильной конечной точке  
✅ Проверка состояния возвращает 200 OK  
✅ Диагностические ячейки тетради проходят  
✅ Нет ошибок подключения в выводе  

---

## Получение помощи

### Документация
- **Основной репозиторий**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Справочник CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Устранение неполадок**: См. `troubleshooting.md` в этом каталоге

### Проблемы на GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Последнее обновление:** 8 октября 2025 г.  
**Версия:** Workshop Notebooks 2.0

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.