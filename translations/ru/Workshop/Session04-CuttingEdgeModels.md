<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:30:47+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ru"
}
-->
# Сессия 4: Исследование передовых моделей – LLM, SLM и локальное выполнение

## Аннотация

Сравните большие языковые модели (LLM) и малые языковые модели (SLM) для сценариев локального и облачного выполнения. Узнайте о шаблонах развертывания с использованием ускорения ONNX Runtime, выполнения WebGPU и гибридных RAG-решений. Включает демонстрацию Chainlit RAG с локальной моделью и дополнительное исследование OpenWebUI. Вы адаптируете начальный проект для выполнения WebGPU и оцените возможности Phi и GPT-OSS-20B, а также компромиссы между производительностью и стоимостью.

## Цели обучения

- **Сравнить** SLM и LLM по параметрам задержки, памяти и качества
- **Развернуть** модели с помощью ONNXRuntime и (где поддерживается) WebGPU
- **Запустить** выполнение в браузере (интерактивная демонстрация с сохранением конфиденциальности)
- **Интегрировать** конвейер Chainlit RAG с локальной SLM-базой
- **Оценить** с использованием легких эвристик качества и стоимости

## Предварительные требования

- Завершены сессии 1–3
- Установлен `chainlit` (уже включен в `requirements.txt` для Module08)
- Браузер с поддержкой WebGPU (последние версии Edge / Chrome на Windows 11)
- Запущен Foundry Local (`foundry service status`)

### Заметки о кроссплатформенности

Windows остается основной целевой средой. Для разработчиков на macOS, ожидающих появления нативных бинарных файлов:
1. Запустите Foundry Local в виртуальной машине Windows 11 (Parallels / UTM) ИЛИ на удаленной рабочей станции Windows.
2. Откройте доступ к сервису (порт по умолчанию 5273) и настройте на macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Используйте те же шаги для виртуальной среды Python, что и в предыдущих сессиях.

Установка Chainlit (для обеих платформ):
```bash
pip install chainlit
```

## Ход демонстрации (30 мин)

### 1. Сравнение Phi (SLM) и GPT-OSS-20B (LLM) (6 мин)

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

Отслеживайте: глубину ответа, точность фактов, богатство стиля, задержку.

Наблюдайте изменения пропускной способности после включения GPU по сравнению с только CPU.

### 3. Выполнение WebGPU в браузере (6 мин)

Адаптируйте начальный проект `04-webgpu-inference` (создайте `samples/04-cutting-edge/webgpu_demo.html`):

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

Откройте файл в браузере; наблюдайте за локальным обменом данными с низкой задержкой.

### 4. Приложение Chainlit RAG Chat (7 мин)

Минимальный пример `samples/04-cutting-edge/chainlit_app.py`:

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

Запустите:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Начальный проект: адаптация `04-webgpu-inference` (6 мин)

Результаты:
- Замените логику получения данных-заглушек на потоковые токены (используйте вариант конечной точки `stream=True`, как только он будет доступен)
- Добавьте график задержки (на стороне клиента) для переключения между phi и gpt-oss-20b
- Вставьте контекст RAG в текстовое поле для справочных документов

## Эвристики оценки

| Категория | Phi-4-mini | GPT-OSS-20B | Наблюдение |
|-----------|------------|-------------|------------|
| Задержка (холодный старт) | Быстрая | Медленнее | SLM быстро прогревается |
| Память | Низкая | Высокая | Возможность использования на устройстве |
| Соответствие контексту | Хорошее | Сильное | Большая модель может быть более многословной |
| Стоимость (локально) | Минимальная | Выше (ресурсы) | Компромисс между энергией и временем |
| Лучший случай использования | Приложения на устройстве | Глубокое рассуждение | Возможен гибридный конвейер |

## Проверка среды

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Устранение неполадок

| Симптом | Причина | Действие |
|---------|---------|----------|
| Ошибка получения веб-страницы | CORS или сервис недоступен | Используйте `curl` для проверки конечной точки; включите прокси CORS, если необходимо |
| Chainlit пустой | Среда не активна | Активируйте виртуальную среду и переустановите зависимости |
| Высокая задержка | Модель только что загружена | Прогрейте с помощью небольшой последовательности подсказок |

## Ссылки

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Документация Chainlit: https://docs.chainlit.io
- Оценка RAG (Ragas): https://docs.ragas.io

---

**Длительность сессии**: 30 мин  
**Сложность**: Продвинутый уровень

## Пример сценария и карта мастер-класса

| Артефакты мастер-класса | Сценарий | Цель | Источник данных / подсказок |
|-------------------------|----------|------|-----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Команда архитекторов оценивает SLM и LLM для генератора кратких отчетов | Количественная оценка задержки и использования токенов | Единая переменная окружения `COMPARE_PROMPT` |
| `chainlit_app.py` (демо RAG) | Прототип внутреннего помощника по знаниям | Основание коротких ответов на минимальном лексическом поиске | Встроенный список `DOCS` в файле |
| `webgpu_demo.html` | Превью выполнения в браузере на устройстве | Демонстрация локального обмена данными с низкой задержкой + UX | Только живой пользовательский запрос |

### Сценарий

Продуктовая команда хочет создать генератор кратких отчетов для руководства. Легкая SLM (phi‑4‑mini) создает черновики, а большая LLM (gpt‑oss‑20b) может дорабатывать только отчеты высокой важности. Скрипты сессии фиксируют эмпирические метрики задержки и токенов для обоснования гибридного дизайна, а демонстрация Chainlit иллюстрирует, как основанный на поиске подход помогает малой модели давать точные ответы. Концептуальная страница WebGPU предоставляет путь к полностью клиентскому выполнению, когда ускорение браузера станет более зрелым.

### Минимальный контекст RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Гибридный поток Черновик→Доработка (Псевдокод)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Отслеживайте оба компонента задержки для расчета среднего совокупного времени.

### Дополнительные улучшения

| Фокус | Улучшение | Зачем | Подсказка по реализации |
|-------|-----------|-------|-------------------------|
| Сравнительные метрики | Отслеживание использования токенов + задержки первого токена | Комплексный обзор производительности | Используйте улучшенный скрипт тестирования (Сессия 3) с `BENCH_STREAM=1` |
| Гибридный конвейер | Черновик SLM → Доработка LLM | Снижение задержки и стоимости | Генерация с phi-4-mini, доработка с gpt-oss-20b |
| Потоковый интерфейс | Улучшение UX в Chainlit | Инкрементальная обратная связь | Используйте `stream=True`, как только локальная потоковая передача станет доступной; накапливайте фрагменты |
| Кэширование WebGPU | Быстрая инициализация JS | Снижение накладных расходов на перекомпиляцию | Кэшируйте скомпилированные артефакты шейдеров (возможность будущего выполнения) |
| Детерминированный набор QA | Справедливое сравнение моделей | Устранение вариативности | Фиксированный список подсказок + `temperature=0` для тестовых запусков |
| Оценка вывода | Структурированный взгляд на качество | Выход за рамки анекдотов | Простая рубрика: связность / фактичность / краткость (1–5) |
| Заметки о ресурсах / энергии | Обсуждение в классе | Демонстрация компромиссов | Используйте мониторы ОС (Диспетчер задач, `nvidia-smi`) + выводы скриптов тестирования |
| Эмуляция стоимости | Обоснование перед облаком | Планирование масштабирования | Сопоставьте токены с гипотетическими облачными ценами для нарратива TCO |
| Разложение задержки | Выявление узких мест | Целевые оптимизации | Измеряйте подготовку подсказок, отправку запроса, первый токен, полное завершение |
| RAG + резерв LLM | Страховка качества | Улучшение сложных запросов | Если длина ответа SLM < порога или низкая уверенность → эскалация |

#### Пример гибридного шаблона Черновик/Доработка

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Эскиз разложения задержки

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Используйте согласованную структуру измерений для справедливого сравнения моделей.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->