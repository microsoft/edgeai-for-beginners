# Водич за брзи почетак - Радне свеске

## Садржај

- [Предуслови](../../../../Workshop/notebooks)
- [Почетно подешавање](../../../../Workshop/notebooks)
- [Сесија 04: Поређење модела](../../../../Workshop/notebooks)
- [Сесија 05: Оркестратор са више агената](../../../../Workshop/notebooks)
- [Сесија 06: Рутање модела на основу намере](../../../../Workshop/notebooks)
- [Променљиве окружења](../../../../Workshop/notebooks)
- [Заједничке команде](../../../../Workshop/notebooks)

---

## Предуслови

### 1. Инсталирајте Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Проверите инсталацију:**
```bash
foundry --version
```

### 2. Инсталирајте Python зависности

```bash
cd Workshop
pip install -r requirements.txt
```

Или инсталирајте појединачно:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Почетно подешавање

### Покрените Foundry Local сервис

**Потребно пре покретања било које радне свеске:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Очекивани излаз:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Преузмите и учитајте моделе

Радне свеске подразумевано користе следеће моделе:

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

### Проверите подешавање

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Сесија 04: Поређење модела

### Сврха
Упоредите перформансе између малих језичких модела (SLM) и великих језичких модела (LLM).

### Брзо подешавање

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Покретање радне свеске

1. **Отворите** `session04_model_compare.ipynb` у VS Code или Jupyter
2. **Рестартујте језгро** (Kernel → Restart Kernel)
3. **Покрените све ћелије** редом

### Кључна конфигурација

**Подразумевани модели:**
- **SLM:** `phi-4-mini` (~4GB RAM, бржи)
- **LLM:** `qwen2.5-3b` (~3GB RAM, оптимизован за меморију)

**Променљиве окружења (опционо):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Очекивани излаз

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

### Прилагођавање

**Користите различите моделе:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Прилагођени упит:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Контролна листа за валидацију

- [ ] Ћелија 12 приказује исправне моделе (phi-4-mini, qwen2.5-3b)
- [ ] Ћелија 12 приказује исправан крајњи чвор (порт 59959)
- [ ] Ћелија 16 дијагностика пролази (✅ Сервис ради)
- [ ] Ћелија 20 провера пре покретања пролази (оба модела су у реду)
- [ ] Ћелија 22 поређење завршено са вредностима кашњења
- [ ] Ћелија 24 валидација показује 🎉 СВЕ ПРОВЕРЕ ПРОШЛЕ!

### Процена времена
- **Прво покретање:** 5-10 минута (укључујући преузимање модела)
- **Накнадна покретања:** 1-2 минута

---

## Сесија 05: Оркестратор са више агената

### Сврха
Демонстрирајте сарадњу више агената користећи Foundry Local SDK - агенти раде заједно на производњи унапређених резултата.

### Брзо подешавање

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Покретање радне свеске

1. **Отворите** `session05_agents_orchestrator.ipynb`
2. **Рестартујте језгро**
3. **Покрените све ћелије** редом

### Кључна конфигурација

**Подразумевано подешавање (исти модел за оба агента):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Напредно подешавање (различити модели):**
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

### Очекивани излаз

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

### Проширења

**Додајте више агената:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Тестирање у серијама:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Процена времена
- **Прво покретање:** 3-5 минута
- **Накнадна покретања:** 1-2 минута по питању

---

## Сесија 06: Рутање модела на основу намере

### Сврха
Паметно усмеравање упита ка специјализованим моделима на основу детектоване намере.

### Брзо подешавање

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Напомена:** Сесија 06 подразумевано користи CPU моделе ради максималне компатибилности.

### Покретање радне свеске

1. **Отворите** `session06_models_router.ipynb`
2. **Рестартујте језгро**
3. **Покрените све ћелије** редом

### Кључна конфигурација

**Подразумевани каталог (CPU модели):**
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

### Детекција намере

Рутер користи regex шаблоне за детекцију намере:

| Намера | Примери шаблона | Усмерено ка |
|--------|-----------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Све остало | phi-4-mini-cpu |

### Очекивани излаз

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

### Прилагођавање

**Додајте прилагођену намеру:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Омогућите праћење токена:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Прелазак на GPU моделе

Ако имате 8GB+ VRAM:

1. У **Ћелији #6**, коментаришите CPU каталог
2. Откоментирајте GPU каталог
3. Учитајте GPU моделе:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Рестартујте језгро и поново покрените радну свеску

### Процена времена
- **Прво покретање:** 5-10 минута (учитавање модела)
- **Накнадна покретања:** 30-60 секунди по тесту

---

## Променљиве окружења

### Глобална конфигурација

Поставите пре покретања Jupyter/VS Code:

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

### Конфигурација у радној свесци

Поставите на почетку било које радне свеске:

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

## Заједничке команде

### Управљање сервисом

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

### Управљање моделима

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

### Тестирање крајњих чворова

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

### Дијагностичке команде

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

## Најбоље праксе

### Пре покретања било које радне свеске

1. **Проверите да ли сервис ради:**
   ```bash
   foundry service status
   ```

2. **Проверите да ли су модели учитани:**
   ```bash
   foundry model ls
   ```

3. **Рестартујте језгро радне свеске** ако поново покрећете

4. **Очистите све излазе** за чисто покретање

### Управљање ресурсима

1. **Користите CPU моделе подразумевано** ради компатибилности
2. **Прелазите на GPU моделе** само ако имате 8GB+ VRAM
3. **Затворите друге GPU апликације** пре покретања
4. **Држите сервис активним** између сесија радних свески
5. **Пратите употребу ресурса** помоћу Task Manager / nvidia-smi

### Решавање проблема

1. **Увек прво проверите сервис** пре отклањања грешака у коду
2. **Рестартујте језгро** ако видите застарелу конфигурацију
3. **Поново покрените дијагностичке ћелије** након било каквих промена
4. **Проверите имена модела** да се поклапају са учитаним
5. **Проверите порт крајњег чвора** да се поклапа са статусом сервиса

---

## Брза референца: Алијаси модела

### Уобичајени модели

| Алијас | Величина | Најбоље за | RAM/VRAM | Варијанте |
|--------|----------|------------|----------|-----------|
| `phi-4-mini` | ~4B | Општи разговор, сумирање | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Генерисање кода, рефакторинг | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Општи задаци, ефикасност | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Брзина, ниски ресурси | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Класификација, минимални ресурси | 1-2GB | `-cpu`, `-cuda-gpu` |

### Именовање варијанти

- **Основно име** (нпр. `phi-4-mini`): Аутоматски бира најбољу варијанту за ваш хардвер
- **`-cpu`**: Оптимизовано за CPU, ради свуда
- **`-cuda-gpu`**: Оптимизовано за NVIDIA GPU, захтева 8GB+ VRAM
- **`-npu`**: Оптимизовано за Qualcomm NPU, захтева NPU драјвере

**Препорука:** Користите основна имена (без суфикса) и дозволите Foundry Local-у да аутоматски изабере најбољу варијанту.

---

## Индикатори успеха

Спремни сте када видите:

✅ `foundry service status` показује "running"
✅ `foundry model ls` приказује потребне моделе
✅ Сервис доступан на исправном крајњем чвору
✅ Провера здравља враћа 200 OK
✅ Дијагностичке ћелије у радној свесци пролазе
✅ Нема грешака у повезивању у излазу

---

## Добијање помоћи

### Документација
- **Главни репозиторијум**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI референца**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Решавање проблема**: Погледајте `troubleshooting.md` у овом директоријуму

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Последње ажурирање:** 8. октобар 2025.
**Верзија:** Workshop Notebooks 2.0

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.