# Сесія 4: Дослідження передових моделей – LLM, SLM та локальне виконання

## Анотація

Порівняйте великі мовні моделі (LLM) та малі мовні моделі (SLM) для локальних і хмарних сценаріїв виконання. Дізнайтеся про шаблони розгортання, які використовують прискорення ONNX Runtime, виконання WebGPU та гібридний досвід RAG. Включає демонстрацію Chainlit RAG із локальною моделлю та необов’язкове дослідження OpenWebUI. Ви адаптуєте стартовий проект для виконання WebGPU та оціните можливості Phi порівняно з GPT-OSS-20B, а також компроміси між продуктивністю та витратами.

## Цілі навчання

- **Порівняти** SLM і LLM за показниками затримки, пам’яті та якості
- **Розгорнути** моделі за допомогою ONNXRuntime і (де підтримується) WebGPU
- **Запустити** виконання в браузері (інтерактивна демонстрація з захистом конфіденційності)
- **Інтегрувати** конвеєр Chainlit RAG із локальним бекендом SLM
- **Оцінити** за допомогою легких евристик якості та витрат

## Попередні вимоги

- Завершені сесії 1–3
- Встановлений `chainlit` (вже в `requirements.txt` для Module08)
- Браузер із підтримкою WebGPU (Edge / Chrome останньої версії на Windows 11)
- Запущений Foundry Local (`foundry service status`)

### Примітки щодо кросплатформенності

Windows залишається основним цільовим середовищем. Для розробників macOS, які очікують на рідні бінарні файли:
1. Запустіть Foundry Local у Windows 11 VM (Parallels / UTM) АБО на віддаленій робочій станції Windows.
2. Відкрийте сервіс (порт за замовчуванням 5273) і налаштуйте на macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Використовуйте ті ж кроки для створення віртуального середовища Python, що й у попередніх сесіях.

Встановлення Chainlit (обидві платформи):
```bash
pip install chainlit
```

## Потік демонстрації (30 хв)

### 1. Порівняння Phi (SLM) і GPT-OSS-20B (LLM) (6 хв)

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

Відстежуйте: глибину відповіді, фактичну точність, стилістичне багатство, затримку.

Спостерігайте за змінами пропускної здатності після увімкнення GPU порівняно з лише CPU.

### 3. Виконання WebGPU у браузері (6 хв)

Адаптуйте стартовий проект `04-webgpu-inference` (створіть `samples/04-cutting-edge/webgpu_demo.html`):

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

Відкрийте файл у браузері; спостерігайте за низькою затримкою локального обміну даними.

### 4. Chainlit RAG Chat App (7 хв)

Мінімальний `samples/04-cutting-edge/chainlit_app.py`:

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

Запустіть:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Стартовий проект: адаптація `04-webgpu-inference` (6 хв)

Результати:
- Замініть логіку отримання даних-заповнювачів на потокові токени (використовуйте варіант кінцевої точки `stream=True`, коли він буде доступний)
- Додайте графік затримки (на стороні клієнта) для перемикання phi і gpt-oss-20b
- Вбудуйте контекст RAG (текстове поле для довідкових документів)

## Евристики оцінки

| Категорія | Phi-4-mini | GPT-OSS-20B | Спостереження |
|----------|------------|-------------|-------------|
| Затримка (холодний старт) | Швидка | Повільніша | SLM швидко прогрівається |
| Пам’ять | Низька | Висока | Можливість використання на пристрої |
| Дотримання контексту | Добре | Сильне | Більша модель може бути більш багатослівною |
| Витрати (локально) | Мінімальні | Вищі (ресурси) | Компроміс між енергією та часом |
| Найкращий випадок використання | Додатки на пристрої | Глибокі міркування | Можливий гібридний конвеєр |

## Перевірка середовища

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Вирішення проблем

| Симптом | Причина | Дія |
|---------|-------|--------|
| Не вдається отримати веб-сторінку | CORS або сервіс недоступний | Використовуйте `curl`, щоб перевірити кінцеву точку; увімкніть проксі CORS, якщо потрібно |
| Chainlit порожній | Середовище не активне | Активуйте venv і перевстановіть залежності |
| Висока затримка | Модель щойно завантажена | Прогрійте за допомогою невеликої послідовності підказок |

## Посилання

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Документація Chainlit: https://docs.chainlit.io
- Оцінка RAG (Ragas): https://docs.ragas.io

---

**Тривалість сесії**: 30 хв  
**Складність**: Висока

## Приклад сценарію та відповідність воркшопу

| Артефакти воркшопу | Сценарій | Ціль | Джерело даних / підказок |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Команда архітекторів оцінює SLM і LLM для генератора виконавчих резюме | Кількісна оцінка затримки + використання токенів | Єдина змінна середовища `COMPARE_PROMPT` |
| `chainlit_app.py` (демо RAG) | Прототип внутрішнього помічника знань | Обґрунтування коротких відповідей із мінімальним лексичним пошуком | Вбудований список `DOCS` у файлі |
| `webgpu_demo.html` | Перспективне виконання в браузері на пристрої | Демонстрація низької затримки локального обміну даними + UX-наратив | Лише живий запит користувача |

### Наратив сценарію
Продуктова організація хоче генератор виконавчих резюме. Легка SLM (phi‑4‑mini) створює чернетки резюме; більша LLM (gpt‑oss‑20b) може вдосконалювати лише звіти високого пріоритету. Скрипти сесії фіксують емпіричні показники затримки та токенів, щоб обґрунтувати гібридний дизайн, тоді як демонстрація Chainlit ілюструє, як обґрунтоване отримання даних забезпечує фактичність відповідей малої моделі. Концептуальна сторінка WebGPU надає шлях бачення для повністю клієнтського оброблення, коли прискорення браузера дозріє.

### Мінімальний контекст RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Гібридний потік Чернетка→Вдосконалення (Псевдо)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Відстежуйте обидва компоненти затримки, щоб повідомити середню змішану вартість.

### Необов’язкові покращення

| Фокус | Покращення | Чому | Підказка щодо реалізації |
|-------|------------|-----|---------------------|
| Порівняльні метрики | Відстежуйте використання токенів + затримку першого токена | Комплексний огляд продуктивності | Використовуйте вдосконалений скрипт тестування (Сесія 3) із `BENCH_STREAM=1` |
| Гібридний конвеєр | Чернетка SLM → Вдосконалення LLM | Зменшення затримки та витрат | Генеруйте за допомогою phi-4-mini, вдосконалюйте резюме за допомогою gpt-oss-20b |
| Потоковий інтерфейс користувача | Кращий UX у Chainlit | Інкрементальний зворотний зв’язок | Використовуйте `stream=True`, коли локальне потокове передавання буде доступне; накопичуйте фрагменти |
| Кешування WebGPU | Швидша ініціалізація JS | Зменшення накладних витрат на перекомпіляцію | Кешуйте скомпільовані артефакти шейдерів (майбутня можливість виконання) |
| Детермінований набір QA | Справедливе порівняння моделей | Усунення варіацій | Фіксований список підказок + `temperature=0` для тестових запусків |
| Оцінка результатів | Структурований об’єктив якості | Вийти за межі анекдотів | Проста рубрика: узгодженість / фактичність / стислість (1–5) |
| Примітки щодо енергії / ресурсів | Обговорення в класі | Показати компроміси | Використовуйте монітори ОС (Диспетчер завдань, `nvidia-smi`) + вихідні дані скриптів тестування |
| Емуляція витрат | Обґрунтування перед хмарою | Планування масштабування | Відображення токенів на гіпотетичне хмарне ціноутворення для наративу TCO |
| Розкладання затримки | Виявлення вузьких місць | Цільові оптимізації | Виміряйте підготовку підказок, надсилання запиту, перший токен, повне завершення |
| RAG + резерв LLM | Страхувальна сітка якості | Покращення складних запитів | Якщо довжина відповіді SLM < порогового значення або низька впевненість → ескалація |

#### Приклад гібридного шаблону Чернетка/Вдосконалення

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Ескіз розкладання затримки

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Використовуйте узгоджені вимірювальні рамки для моделей, щоб забезпечити справедливі порівняння.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->