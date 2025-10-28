<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:27:35+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sr"
}
-->
# Сесија 1: Почетак рада са Foundry Local

## Апстракт

Започните своје путовање са Foundry Local инсталирањем и конфигурисањем на Windows 11. Научите како да подесите CLI, омогућите хардверско убрзање и кеширате моделе за брзу локалну инференцију. Ова практична сесија објашњава како да покренете моделе као што су Phi, Qwen, DeepSeek и GPT-OSS-20B користећи репродуктивне CLI команде.

## Циљеви учења

До краја ове сесије, моћи ћете:

- **Инсталирати и конфигурисати**: Подесите Foundry Local на Windows 11 са оптималним подешавањима перформанси
- **Овладати CLI операцијама**: Користите Foundry Local CLI за управљање моделима и њихово покретање
- **Омогућити хардверско убрзање**: Конфигуришите GPU убрзање са ONNXRuntime или WebGPU
- **Покренути више модела**: Локално покрените моделе phi-4, GPT-OSS-20B, Qwen и DeepSeek
- **Направити своју прву апликацију**: Прилагодите постојеће примере користећи Foundry Local Python SDK

# Тестирање модела (неинтерактивни једноструки упит)
foundry model run phi-4-mini --prompt "Здраво, представи се"

- Windows 11 (22H2 или новији)
# Листа доступних модела из каталога (учитани модели се појављују након покретања)
foundry model list
## NOTE: Тренутно не постоји посебна `--running` ознака; да бисте видели који су учитани, започните разговор или прегледајте логове сервиса.
- Python 3.10+ инсталиран
- Visual Studio Code са Python екстензијом
- Администраторске привилегије за инсталацију

### (Опционо) Променљиве окружења

Направите `.env` (или подесите у shell-у) да бисте скрипте учинили преносивим:
# Поређење одговора (неинтерактивно)
foundry model run gpt-oss-20b --prompt "Објасни edge AI једноставним речима"
| Променљива | Сврха | Пример |
|------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Преферирани алијас модела (каталог аутоматски бира најбољу варијанту) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Замена за подразумевани endpoint (иначе аутоматски из менаџера) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Омогућава демо стриминг | `true` |

> Ако је `FOUNDRY_LOCAL_ENDPOINT=auto` (или није постављен), изводимо га из SDK менаџера.

## Демонстрација (30 минута)

### 1. Инсталирање Foundry Local и провера CLI подешавања (10 минута)

# Листа кешираних модела
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Преглед / Ако је подржано)**

Ако је доступан native macOS пакет (проверите званичну документацију за најновије):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ако native macOS бинарни фајлови још нису доступни, можете:
1. Користити Windows 11 ARM/Intel VM (Parallels / UTM) и следити кораке за Windows. 
2. Покренути моделе преко контејнера (ако је објављена слика контејнера) и поставити `FOUNDRY_LOCAL_ENDPOINT` на отворени порт.

**Креирање Python виртуелног окружења (Cross‑Platform)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Ажурирајте pip и инсталирајте основне зависности:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Корак 1.2: Провера инсталације

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Корак 1.3: Конфигурисање окружења

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Препоручено)

Уместо ручног покретања сервиса и модела, **Foundry Local Python SDK** може аутоматски покренути све:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Ако више волите експлицитну контролу, можете и даље користити CLI + OpenAI клијент као што је приказано касније.

### 2. Локално покретање модела преко CLI (10 минута)

#### Корак 3.1: Покретање Phi-4 модела

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Корак 3.2: Покретање GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Корак 3.3: Учитавање додатних модела

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Почетни пројекат: Прилагођавање 01-run-phi за Foundry Local (5 минута)

#### Корак 4.1: Креирање основне апликације за разговор

Направите `samples/01-foundry-quickstart/chat_quickstart.py` (ажурирано за коришћење менаџера ако је доступан):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Корак 4.2: Тестирање апликације

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Кључни концепти

### 1. Архитектура Foundry Local

- **Локални инференцијски мотор**: Покреће моделе у потпуности на вашем уређају
- **Компатибилност са OpenAI SDK**: Лака интеграција са постојећим OpenAI кодом
- **Управљање моделима**: Преузимање, кеширање и ефикасно покретање више модела
- **Оптимизација хардвера**: Искористите GPU, NPU и CPU убрзање

### 2. Референца за CLI команде

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Интеграција Python SDK-а

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Решавање уобичајених проблема

### Проблем 1: "Foundry команда није пронађена"

**Решење:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Проблем 2: "Модел није успео да се учита"

**Решење:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Проблем 3: "Веза одбијена на localhost:5273"

**Решење:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Савети за оптимизацију перформанси

### 1. Стратегија избора модела

- **Phi-4-mini**: Најбољи за опште задатке, мања потрошња меморије
- **Qwen2.5-0.5b**: Најбржа инференција, минимални ресурси
- **GPT-OSS-20B**: Највиши квалитет, захтева више ресурса
- **DeepSeek-Coder**: Оптимизован за програмске задатке

### 2. Оптимизација хардвера

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Праћење перформанси

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Опциона побољшања

| Побољшање | Шта | Како |
|-----------|-----|------|
| Заједничке алатке | Уклоните дуплирану логику клијента/покретања | Користите `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Видљивост коришћења токена | Рано учење о трошковима/ефикасности | Поставите `SHOW_USAGE=1` за приказ упита/завршетка/укупних токена |
| Детерминистичка поређења | Стабилно тестирање и проверa регресије | Користите `temperature=0`, `top_p=1`, конзистентан текст упита |
| Латенција првог токена | Метрика перцепције одзивности | Прилагодите скрипту за тестирање са стримингом (`BENCH_STREAM=1`) |
| Поновно покретање код привремених грешака | Отпорне демонстрације при хладном старту | `RETRY_ON_FAIL=1` (подразумевано) и прилагодите `RETRY_BACKOFF` |
| Брзо тестирање | Брза провера кључних токова | Покрените `python Workshop/tests/smoke.py` пре радионице |
| Профили алијаса модела | Брзо пребацивање између сетова модела на различитим машинама | Одржавајте `.env` са `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Ефикасност кеширања | Избегавајте поновљено загревање у више узорака | Алатке за кеширање менаџера; поновно коришћење у скриптама/бележницама |
| Загревање при првом покретању | Смањите латенцију p95 | Покрените мали упит након креирања `FoundryLocalManager`

Пример детерминистичког загревања (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Требало би да видите сличан излаз и идентичан број токена при другом покретању, што потврђује детерминизам.

## Следећи кораци

Након завршетка ове сесије:

1. **Истражите Сесију 2**: Изградите AI решења са Azure AI Foundry RAG
2. **Испробајте различите моделе**: Експериментишите са Qwen, DeepSeek и другим породицама модела
3. **Оптимизујте перформансе**: Фино подесите подешавања за ваш специфичан хардвер
4. **Направите прилагођене апликације**: Користите Foundry Local SDK у својим пројектима

## Додатни ресурси

### Документација
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Пример кода
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Заједница
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Трајање сесије**: 30 минута практично + 15 минута Q&A
**Ниво тежине**: Почетни
**Предуслови**: Windows 11, Python 3.10+, Администраторски приступ

## Пример сценарија и мапирање радионице

| Скрипта радионице / Бележница | Сценарио | Циљ | Пример уноса | Потребан сет података |
|-------------------------------|----------|------|--------------|-----------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Интерни IT тим процењује инференцију на уређају за портал процене приватности | Доказати да локални SLM одговара унутар латенције мање од секунде на стандардне упите | "Наведи две предности локалне инференције." | Ниједан (једноструки упит) |
| Код адаптације за брзи почетак | Програмер који мигрира постојећу OpenAI скрипту на Foundry Local | Прикажи компатибилност без измена | "Наведи две предности локалне инференције." | Само унутрашњи упит |

### Наратив сценарија
Тим за безбедност и усклађеност мора да потврди да ли се осетљиви прототипски подаци могу обрађивати локално. Они покрећу скрипту за покретање са неколико упита (приватност, латенција, трошкови) користећи детерминистички режим temperature=0 како би забележили основне излазе за касније поређење (Сесија 3 тестирање перформанси и Сесија 4 контраст SLM vs LLM).

### Минимални JSON сет упита (опционо)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Користите ову листу за креирање репродуктивног циклуса евалуације или за иницирање будућег теста регресије.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.