<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:13:45+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "bg"
}
-->
# Сесия 4: Изследване на най-новите модели – LLMs, SLMs и локално извеждане

## Резюме

Сравнете големи езикови модели (LLMs) и малки езикови модели (SLMs) за сценарии на локално и облачно извеждане. Научете модели за внедряване, използващи ускорение на ONNX Runtime, изпълнение с WebGPU и хибридни RAG преживявания. Включва демонстрация на Chainlit RAG с локален модел плюс опционално изследване на OpenWebUI. Ще адаптирате стартер за WebGPU извеждане и ще оцените възможностите и компромисите между Phi и GPT-OSS-20B по отношение на цена и производителност.

## Цели на обучението

- **Сравнете** SLM и LLM по осите на латентност, памет и качество
- **Внедрете** модели с ONNXRuntime и (където е възможно) WebGPU
- **Изпълнете** извеждане в браузър (интерактивна демонстрация, запазваща поверителността)
- **Интегрирайте** Chainlit RAG тръбопровод с локален SLM бекенд
- **Оценете** с помощта на леки качествени + ценови евристики

## Предварителни условия

- Завършени сесии 1–3
- Инсталиран `chainlit` (вече включен в `requirements.txt` за Module08)
- Браузър, поддържащ WebGPU (Edge / Chrome последна версия на Windows 11)
- Работещ Foundry Local (`foundry status`)

### Бележки за различни платформи

Windows остава основната целева среда. За разработчици на macOS, които чакат родни бинарни файлове:
1. Стартирайте Foundry Local в Windows 11 VM (Parallels / UTM) ИЛИ на отдалечена Windows работна станция.
2. Експонирайте услугата (по подразбиране порт 5273) и настройте на macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Използвайте същите стъпки за Python виртуална среда като в предишните сесии.

Инсталиране на Chainlit (и за двете платформи):
```bash
pip install chainlit
```

## Демонстрационен поток (30 мин)

### 1. Сравнение на Phi (SLM) и GPT-OSS-20B (LLM) (6 мин)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Проследете: дълбочина на отговорите, фактическа точност, стилово богатство, латентност.

### 2. Ускорение с ONNX Runtime (5 мин)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Наблюдавайте промени в пропускателната способност след активиране на GPU спрямо само CPU.

### 3. Извеждане с WebGPU в браузър (6 мин)

Адаптирайте стартер `04-webgpu-inference` (създайте `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Отворете файла в браузър; наблюдавайте локалния кръговрат с ниска латентност.

### 4. Chainlit RAG чат приложение (7 мин)

Минимален `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Стартирайте:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Стартер проект: Адаптиране на `04-webgpu-inference` (6 мин)

Резултати:
- Заменете логиката за извличане на заместители с поточни токени (използвайте варианта `stream=True` на крайна точка, когато е активиран)
- Добавете диаграма за латентност (клиентска страна) за превключване между phi и gpt-oss-20b
- Вградете контекст на RAG (текстово поле за референтни документи)

## Евристики за оценка

| Категория | Phi-4-mini | GPT-OSS-20B | Наблюдение |
|-----------|------------|-------------|------------|
| Латентност (студено) | Бързо | По-бавно | SLM се загрява бързо |
| Памет | Ниска | Висока | Възможност за устройство |
| Придържане към контекста | Добро | Силно | По-големият модел може да бъде по-обстоятелен |
| Цена (локално) | Минимална | По-висока (ресурси) | Компромис между енергия/време |
| Най-добър случай на употреба | Приложения на ръба | Дълбоко разсъждение | Възможен хибриден тръбопровод |

## Валидиране на средата

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Отстраняване на проблеми

| Симптом | Причина | Действие |
|---------|---------|----------|
| Уеб страницата не се зарежда | CORS или услугата е спряна | Използвайте `curl`, за да проверите крайна точка; активирайте CORS прокси, ако е необходимо |
| Chainlit празен | Средата не е активна | Активирайте venv и преинсталирайте зависимости |
| Висока латентност | Моделът току-що е зареден | Загрейте с малка последователност от подканващи |

## Референции

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Документация: https://docs.chainlit.io
- Оценка на RAG (Ragas): https://docs.ragas.io

---

**Продължителност на сесията**: 30 мин  
**Трудност**: Напреднала

## Примерен сценарий и картографиране на работилница

| Артефакти от работилницата | Сценарий | Цел | Източник на данни/подканващи |
|----------------------------|----------|-----|-----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Екип по архитектура, оценяващ SLM спрямо LLM за генератор на изпълнителни резюмета | Количествено определяне на латентност + разлика в използването на токени | Единична променлива на средата `COMPARE_PROMPT` |
| `chainlit_app.py` (демо на RAG) | Прототип на вътрешен помощник за знания | Основа за кратки отговори с минимално лексикално извличане | Вградени `DOCS` списък във файла |
| `webgpu_demo.html` | Преглед на бъдещо извеждане в браузър на устройството | Показване на локален кръговрат с ниска латентност + разказ за UX | Само потребителски подканващи на живо |

### Разказ за сценария
Продуктовата организация иска генератор за изпълнителни резюмета. Лек SLM (phi‑4‑mini) създава чернови на резюмета; по-голям LLM (gpt‑oss‑20b) може да ги усъвършенства само за доклади с висок приоритет. Скриптовете от сесията улавят емпирични латентност и метрики за токени, за да оправдаят хибридния дизайн, докато демонстрацията на Chainlit илюстрира как основаното на извличане поддържа фактологичността на отговорите от малкия модел. Концептуалната страница за WebGPU предоставя визия за напълно клиентска обработка, когато ускорението в браузъра узрее.

### Минимален контекст на RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Хибриден поток Чернова→Усъвършенстване (Псевдо)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Проследете и двата компонента на латентността, за да отчетете средната смесена цена.

### Опционални подобрения

| Фокус | Подобрение | Защо | Подсказка за имплементация |
|-------|------------|------|---------------------------|
| Сравнителни метрики | Проследяване на използването на токени + латентност на първия токен | Холистичен поглед върху производителността | Използвайте подобрен скрипт за бенчмарк (Сесия 3) с `BENCH_STREAM=1` |
| Хибриден тръбопровод | Чернова с SLM → Усъвършенстване с LLM | Намаляване на латентността и разходите | Генерирайте с phi-4-mini, усъвършенствайте резюмето с gpt-oss-20b |
| Поточно UI | По-добър UX в Chainlit | Инкрементална обратна връзка | Използвайте `stream=True`, когато локалното поточно предаване е активирано; натрупвайте части |
| Кеширане на WebGPU | По-бързо инициализиране на JS | Намаляване на режийните разходи за компилация | Кеширайте компилирани артефакти на шейдъри (бъдеща възможност за изпълнение) |
| Детерминиран QA набор | Справедливо сравнение на модели | Премахване на вариациите | Фиксиран списък с подканващи + `temperature=0` за оценъчни изпълнения |
| Оценка на резултатите | Структуриран качествен поглед | Надхвърляне на анекдотите | Прост рубрикатор: съгласуваност / фактологичност / краткост (1–5) |
| Бележки за енергия/ресурси | Дискусия в клас | Показване на компромиси | Използвайте OS монитори (`foundry system info`, Task Manager, `nvidia-smi`) + изходи от скрипт за бенчмарк |
| Емулация на разходи | Предварителна обосновка за облака | Планиране на мащабиране | Картирайте токени към хипотетични облачни цени за разказ за TCO |
| Разграждане на латентността | Идентифициране на тесни места | Целеви оптимизации | Измерете подготовка на подканващи, изпращане на заявка, първи токен, пълно завършване |
| RAG + LLM резерв | Мрежа за безопасност на качеството | Подобряване на трудни запитвания | Ако дължината на отговора на SLM < праг или ниска увереност → ескалация |

#### Примерен хибриден модел Чернова/Усъвършенстване

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Скица за разграждане на латентността

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Използвайте последователна рамка за измерване между моделите за справедливи сравнения.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.