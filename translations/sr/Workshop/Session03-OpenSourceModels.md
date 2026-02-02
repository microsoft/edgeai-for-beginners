# Сесија 3: Модели отвореног кода у Foundry Local

## Апстракт

Сазнајте како да интегришете Hugging Face и друге моделе отвореног кода у Foundry Local. Упознајте стратегије избора, радне токове за допринос заједници, методологију за поређење перформанси и како да проширите Foundry са прилагођеним регистрацијама модела. Ова сесија се повезује са недељним темама истраживања "Model Mondays" и омогућава вам да локално процените и оперативно примените моделе отвореног кода пре него што их скалирате на Azure.

## Циљеви учења

На крају ћете бити у могућности да:

- **Откријете и процените**: Идентификујете моделе кандидате (mistral, gemma, qwen, deepseek) користећи компромисе између квалитета и ресурса.
- **Учитате и покренете**: Користите Foundry Local CLI за преузимање, кеширање и покретање модела заједнице.
- **Бенчмаркирање**: Примените конзистентне хеуристике за кашњење + пропусност токена + квалитет.
- **Проширите**: Региструјете или прилагодите прилагођени омот модела пратећи SDK-компатибилне шаблоне.
- **Упоредите**: Направите структурна поређења за одлуке о избору SLM у односу на средње LLM моделе.

## Предуслови

- Завршене сесије 1 и 2
- Python окружење са инсталираним `foundry-local-sdk`
- Најмање 15GB слободног простора на диску за кеширање више модела

### Брзи почетак за окружење на више платформи

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Када вршите бенчмаркирање са macOS-а на Windows хост сервис, подесите:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрациони ток (30 мин)

### 1. Учитавање Hugging Face модела преко CLI (8 мин)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Покретање и брза провера (5 мин)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Скрипта за бенчмаркирање (8 мин)

Креирајте `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Покрените:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Упоређивање перформанси (5 мин)

Разговарајте о компромисима: време учитавања, меморијски отисак (посматрајте Task Manager / `nvidia-smi` / монитор ресурса ОС-а), квалитет излазног резултата у односу на брзину. Користите Python скрипту за бенчмаркирање (Сесија 3) за кашњење и пропусност; поновите након омогућавања GPU убрзања.

### 5. Почетни пројекат (4 мин)

Направите генератор извештаја за поређење модела (проширите скрипту за бенчмаркирање са извозом у markdown).

## Почетни пројекат: Проширите `03-huggingface-models`

Унапредите постојећи пример додавањем:

1. Агрегације бенчмаркирања + излаз у CSV/Markdown.
2. Имплементације једноставног квалитативног оцењивања (сет парова упита + датотека за ручну анотацију).
3. Увођења JSON конфигурације (`models.json`) за листу модела који се могу додати и сет упита.

## Контролна листа за валидацију

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Сви циљни модели треба да се појаве и одговоре на захтев за ћаскање.

## Пример сценарија и мапирање радионице

| Скрипта радионице | Сценарио | Циљ | Извор упита / скупа података |
|-------------------|----------|-----|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Тим за платформу на ивици бира подразумевани SLM за уграђени сажимач | Направите поређење кашњења + p95 + токена/секунди међу моделима кандидатима | Уграђена `PROMPT` променљива + листа окружења `BENCH_MODELS` |

### Наратив сценарија

Инжењеринг производа мора да изабере подразумевани лагани модел за сажимање за функцију офлајн белешки са састанка. Они спроводе контролисана детерминистичка бенчмаркирања (temperature=0) на фиксном сету упита (погледајте пример испод) и прикупљају метрике кашњења + пропусности са и без GPU убрзања.

### Пример JSON сета упита (проширив)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Поновите сваки упит за сваки модел, забележите кашњење по упиту како бисте израчунали метрике дистрибуције и открили одступања.

## Оквир за избор модела

| Димензија | Метрика | Зашто је важна |
|-----------|---------|----------------|
| Кашњење | просек / p95 | Конзистентност корисничког искуства |
| Пропусност | токени/сек | Скалабилност за серије и стриминг |
| Меморија | резидентна величина | Прилагођеност уређају и конкурентност |
| Квалитет | рубрика упита | Погодност за задатак |
| Отисак | кеш диска | Дистрибуција и ажурирања |
| Лиценца | дозвола за коришћење | Комерцијална усклађеност |

## Проширење са прилагођеним моделом

Шаблон високог нивоа (псеудо):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Консултујте званични репозиторијум за развој интерфејса адаптера:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Решавање проблема

| Проблем | Узрок | Решење |
|---------|-------|--------|
| Недостатак меморије на mistral-7b | Недовољно RAM/GPU ресурса | Зауставите друге моделе; пробајте мању варијанту |
| Спор први одговор | Хладно учитавање | Одржавајте топло са периодичним лаганим упитом |
| Застој у преузимању | Нестабилност мреже | Поновите; преузмите у периоду мањег оптерећења |

## Референце

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Трајање сесије**: 30 мин (+ опционално дубинско истраживање)  
**Тежина**: Средњи ниво

### Опционална унапређења

| Унапређење | Предност | Како |
|------------|----------|------|
| Кашњење првог токена у стримингу | Мери перципирану одзивност | Покрените бенчмаркирање са `BENCH_STREAM=1` (унапређена скрипта у `Workshop/samples/session03`) |
| Детерминистички режим | Стабилна поређења регресије | `temperature=0`, фиксни сет упита, забележите JSON излазе под контролом верзије |
| Оцењивање рубрике квалитета | Додаје квалитативну димензију | Одржавајте `prompts.json` са очекиваним аспектима; ручно или помоћу секундарног модела анотирајте оцене (1–5) |
| Извоз у CSV / Markdown | Извештај који се може делити | Проширите скрипту да пише `benchmark_report.md` са табелом и истакнутим деловима |
| Ознаке способности модела | Помаже каснијем аутоматском рутирању | Одржавајте `models.json` са `{alias: {capabilities:[], size_mb:..}}` |
| Фаза загревања кеша | Смањује пристрасност хладног старта | Извршите један круг загревања пре временске петље (већ имплементирано) |
| Тачност перцентила | Робусно кашњење у репу | Користите numpy перцентил (већ у рефакторисаној скрипти) |
| Приближна цена токена | Економско поређење | Приближна цена = (токени/сек * просечан број токена по захтеву) * енергетска хеуристика |
| Аутоматско прескакање неуспелих модела | Отпорност у серијским покретањима | Умотајте свако бенчмаркирање у try/except и означите статусно поље |

#### Минимални Markdown извозни исечак

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Пример детерминистичког сета упита

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Поновите статичну листу уместо случајних упита за упоредиве метрике кроз комитове.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->