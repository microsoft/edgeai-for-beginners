<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:39:59+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "fa"
}
-->
# جلسه ۴: بررسی مدل‌های پیشرفته – LLMها، SLMها و استنتاج روی دستگاه

## خلاصه

مدل‌های زبان بزرگ (LLMها) و مدل‌های زبان کوچک (SLMها) را برای سناریوهای استنتاج محلی و ابری مقایسه کنید. الگوهای استقرار را با استفاده از شتاب‌دهنده ONNX Runtime، اجرای WebGPU و تجربیات ترکیبی RAG بیاموزید. شامل یک دمو Chainlit RAG با یک مدل محلی به همراه یک بررسی اختیاری OpenWebUI است. شما یک شروع‌کننده استنتاج WebGPU را تطبیق داده و قابلیت‌ها و توازن هزینه/عملکرد Phi در مقابل GPT-OSS-20B را ارزیابی خواهید کرد.

## اهداف یادگیری

- **مقایسه** SLM و LLM از نظر تأخیر، حافظه و کیفیت
- **استقرار** مدل‌ها با ONNXRuntime و (در صورت پشتیبانی) WebGPU
- **اجرای** استنتاج مبتنی بر مرورگر (دموی تعاملی حفظ حریم خصوصی)
- **ادغام** یک خط لوله Chainlit RAG با یک بک‌اند SLM محلی
- **ارزیابی** با استفاده از معیارهای سبک کیفیت و هزینه

## پیش‌نیازها

- جلسات ۱ تا ۳ تکمیل شده باشد
- `chainlit` نصب شده باشد (در حال حاضر در `requirements.txt` برای Module08 موجود است)
- مرورگر سازگار با WebGPU (Edge / Chrome آخرین نسخه در ویندوز ۱۱)
- Foundry Local در حال اجرا (`foundry service status`)

### نکات بین‌پلتفرمی

ویندوز همچنان محیط هدف اصلی است. برای توسعه‌دهندگان macOS که منتظر باینری‌های بومی هستند:
1. Foundry Local را در یک ماشین مجازی ویندوز ۱۱ (Parallels / UTM) یا یک ایستگاه کاری ویندوز راه دور اجرا کنید.
2. سرویس را (پورت پیش‌فرض 5273) در macOS تنظیم کنید:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. از همان مراحل محیط مجازی پایتون که در جلسات قبلی استفاده شده است، بهره ببرید.

نصب Chainlit (هر دو پلتفرم):
```bash
pip install chainlit
```

## جریان دمو (۳۰ دقیقه)

### ۱. مقایسه Phi (SLM) و GPT-OSS-20B (LLM) (۶ دقیقه)

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

پیگیری کنید: عمق پاسخ، دقت واقعی، غنای سبک، تأخیر.

تغییرات در توان عملیاتی را پس از فعال کردن GPU در مقابل فقط CPU مشاهده کنید.

### ۳. استنتاج WebGPU در مرورگر (۶ دقیقه)

شروع‌کننده `04-webgpu-inference` را تطبیق دهید (ایجاد `samples/04-cutting-edge/webgpu_demo.html`):

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

فایل را در مرورگر باز کنید؛ مشاهده کنید که چگونه دوربرگردان محلی با تأخیر کم انجام می‌شود.

### ۴. اپلیکیشن چت Chainlit RAG (۷ دقیقه)

`samples/04-cutting-edge/chainlit_app.py` حداقلی:

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

اجرا کنید:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### ۵. پروژه شروع‌کننده: تطبیق `04-webgpu-inference` (۶ دقیقه)

تحویل‌ها:
- منطق دریافت جایگزین را با توکن‌های استریمینگ جایگزین کنید (از نوع endpoint `stream=True` استفاده کنید وقتی فعال شد)
- نمودار تأخیر (سمت کلاینت) برای تغییرات phi و gpt-oss-20b اضافه کنید
- زمینه RAG را به صورت داخلی جاسازی کنید (textarea برای اسناد مرجع)

## معیارهای ارزیابی

| دسته‌بندی | Phi-4-mini | GPT-OSS-20B | مشاهده |
|-----------|------------|-------------|--------|
| تأخیر (سرد) | سریع | کندتر | SLM سریع گرم می‌شود |
| حافظه | کم | زیاد | امکان‌پذیری دستگاه |
| پایبندی به زمینه | خوب | قوی | مدل بزرگ‌تر ممکن است پرحرف‌تر باشد |
| هزینه (محلی) | حداقل | بالاتر (منابع) | توازن انرژی/زمان |
| بهترین مورد استفاده | اپلیکیشن‌های لبه | استدلال عمیق | خط لوله ترکیبی ممکن است |

## اعتبارسنجی محیط

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## رفع اشکال

| علامت | علت | اقدام |
|-------|-----|-------|
| دریافت صفحه وب شکست می‌خورد | CORS یا سرویس غیرفعال | از `curl` برای تأیید endpoint استفاده کنید؛ در صورت نیاز پروکسی CORS را فعال کنید |
| Chainlit خالی | محیط فعال نیست | venv را فعال کنید و وابستگی‌ها را دوباره نصب کنید |
| تأخیر بالا | مدل تازه بارگذاری شده | با یک دنباله کوچک درخواست گرم کنید |

## منابع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- مستندات Chainlit: https://docs.chainlit.io
- ارزیابی RAG (Ragas): https://docs.ragas.io

---

**مدت جلسه**: ۳۰ دقیقه  
**سطح دشواری**: پیشرفته

## سناریوی نمونه و نگاشت کارگاه

| مصنوعات کارگاه | سناریو | هدف | منبع داده/درخواست |
|----------------|--------|------|-------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | تیم معماری که SLM و LLM را برای تولید خلاصه اجرایی ارزیابی می‌کند | کمیت‌گذاری تأخیر + تفاوت استفاده از توکن | متغیر محیطی `COMPARE_PROMPT` واحد |
| `chainlit_app.py` (دموی RAG) | نمونه اولیه دستیار دانش داخلی | پاسخ‌های کوتاه را با حداقل بازیابی لغوی پایه‌گذاری کنید | لیست `DOCS` داخلی در فایل |
| `webgpu_demo.html` | پیش‌نمایش استنتاج مرورگر روی دستگاه آینده‌نگر | نمایش دوربرگردان محلی با تأخیر کم + روایت UX | فقط درخواست زنده کاربر |

### روایت سناریو
سازمان محصول به دنبال یک تولیدکننده خلاصه اجرایی است. یک SLM سبک (phi-4-mini) پیش‌نویس‌ها را تهیه می‌کند؛ یک LLM بزرگ‌تر (gpt-oss-20b) ممکن است فقط گزارش‌های با اولویت بالا را اصلاح کند. اسکریپت‌های جلسه معیارهای تأخیر تجربی و توکن را برای توجیه طراحی ترکیبی ثبت می‌کنند، در حالی که دموی Chainlit نشان می‌دهد که چگونه بازیابی پایه‌گذاری شده پاسخ‌های مدل کوچک را واقعی نگه می‌دارد. صفحه مفهوم WebGPU مسیر چشم‌انداز پردازش کاملاً سمت کلاینت را زمانی که شتاب‌دهی مرورگر بالغ شود، ارائه می‌دهد.

### زمینه حداقلی RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### جریان ترکیبی پیش‌نویس→اصلاح (شبه‌کد)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

هر دو مؤلفه تأخیر را پیگیری کنید تا میانگین هزینه ترکیبی گزارش شود.

### بهبودهای اختیاری

| تمرکز | بهبود | دلیل | نکته پیاده‌سازی |
|-------|-------|------|----------------|
| معیارهای مقایسه‌ای | پیگیری استفاده از توکن + تأخیر اولین توکن | نمای کلی عملکرد | از اسکریپت معیار پیشرفته (جلسه ۳) با `BENCH_STREAM=1` استفاده کنید |
| خط لوله ترکیبی | پیش‌نویس SLM → اصلاح LLM | کاهش تأخیر و هزینه | با phi-4-mini تولید کنید، خلاصه را با gpt-oss-20b اصلاح کنید |
| رابط کاربری استریمینگ | UX بهتر در Chainlit | بازخورد تدریجی | از `stream=True` استفاده کنید وقتی استریم محلی فعال شد؛ قطعات را جمع‌آوری کنید |
| کش WebGPU | شروع سریع‌تر JS | کاهش سربار کامپایل مجدد | کش مصنوعات شیدر کامپایل شده (قابلیت آینده در زمان اجرا) |
| مجموعه QA قطعی | مقایسه منصفانه مدل | حذف تغییرات | لیست درخواست ثابت + `temperature=0` برای اجرای ارزیابی |
| امتیازدهی خروجی | لنز کیفیت ساختاری | فراتر از حکایات بروید | معیار ساده: انسجام / واقعی بودن / اختصار (۱–۵) |
| یادداشت‌های انرژی/منابع | بحث کلاسی | نمایش توازن‌ها | از مانیتورهای سیستم‌عامل (Task Manager، `nvidia-smi`) + خروجی‌های اسکریپت معیار استفاده کنید |
| شبیه‌سازی هزینه | توجیه پیش‌ابری | برنامه‌ریزی مقیاس‌گذاری | توکن‌ها را به قیمت‌گذاری ابری فرضی برای روایت TCO نگاشت کنید |
| تجزیه تأخیر | شناسایی گلوگاه‌ها | هدف‌گذاری بهینه‌سازی‌ها | آماده‌سازی درخواست، ارسال درخواست، اولین توکن، تکمیل کامل را اندازه‌گیری کنید |
| RAG + بازگشت به LLM | شبکه ایمنی کیفیت | بهبود درخواست‌های دشوار | اگر طول پاسخ SLM < آستانه یا اعتماد پایین → ارتقا دهید |

#### الگوی ترکیبی پیش‌نویس/اصلاح نمونه

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### طرح تجزیه تأخیر

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

از چارچوب اندازه‌گیری سازگار در مدل‌ها برای مقایسه‌های منصفانه استفاده کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->