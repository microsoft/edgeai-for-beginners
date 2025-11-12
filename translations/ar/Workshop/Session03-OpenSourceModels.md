<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T21:38:45+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ar"
}
-->
# الجلسة الثالثة: النماذج مفتوحة المصدر في Foundry Local

## الملخص

اكتشف كيفية دمج نماذج Hugging Face وغيرها من النماذج مفتوحة المصدر في Foundry Local. تعلم استراتيجيات الاختيار، عمليات المساهمة المجتمعية، منهجية مقارنة الأداء، وكيفية توسيع Foundry من خلال تسجيل نماذج مخصصة. هذه الجلسة تتماشى مع موضوعات استكشاف "Model Mondays" الأسبوعية وتجهزك لتقييم وتشغيل النماذج مفتوحة المصدر محليًا قبل التوسع إلى Azure.

## أهداف التعلم

بنهاية الجلسة ستكون قادرًا على:

- **الاكتشاف والتقييم**: تحديد النماذج المرشحة (mistral، gemma، qwen، deepseek) باستخدام موازنة الجودة مقابل الموارد.
- **التحميل والتشغيل**: استخدام Foundry Local CLI لتنزيل وتخزين وتشغيل نماذج المجتمع.
- **القياس**: تطبيق معايير ثابتة للكمون + معدل معالجة الرموز + جودة الأداء.
- **التوسيع**: تسجيل أو تعديل غلاف نموذج مخصص وفقًا لأنماط متوافقة مع SDK.
- **المقارنة**: إنتاج مقارنات منظمة لاتخاذ قرارات اختيار SLM مقابل LLM متوسطة الحجم.

## المتطلبات الأساسية

- إكمال الجلسات 1 و 2
- بيئة Python مثبت عليها `foundry-local-sdk`
- مساحة تخزين لا تقل عن 15 جيجابايت لتخزين نماذج متعددة

### بدء سريع للبيئة متعددة الأنظمة

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

عند القياس من macOS مقابل خدمة مضيفة على Windows، قم بتعيين:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## تدفق العرض التوضيحي (30 دقيقة)

### 1. تحميل نماذج Hugging Face عبر CLI (8 دقائق)

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


### 2. التشغيل والفحص السريع (5 دقائق)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. نص القياس (8 دقائق)

إنشاء `samples/03-oss-models/benchmark_models.py`:

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

تشغيل:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. مقارنة الأداء (5 دقائق)

ناقش الموازنة: وقت التحميل، استهلاك الذاكرة (راقب Task Manager / `nvidia-smi` / مراقب موارد النظام)، جودة المخرجات مقابل السرعة. استخدم نص القياس في Python (الجلسة 3) للكمون ومعدل المعالجة؛ كرر بعد تمكين تسريع GPU.

### 5. مشروع البداية (4 دقائق)

قم بإنشاء مولد تقرير مقارنة النماذج (قم بتوسيع نص القياس مع تصدير Markdown).

## مشروع البداية: توسيع `03-huggingface-models`

قم بتحسين العينة الحالية من خلال:

1. إضافة تجميع القياسات + إخراج CSV/Markdown.
2. تنفيذ تسجيل نوعي بسيط (مجموعة أزواج التعليمات + ملف تعليق يدوي).
3. تقديم تكوين JSON (`models.json`) لقائمة نماذج قابلة للتوصيل ومجموعة التعليمات.

## قائمة التحقق من التحقق

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

يجب أن تظهر جميع النماذج المستهدفة وتستجيب لطلب دردشة الفحص.

## سيناريو العينة وتخطيط ورشة العمل

| نص ورشة العمل | السيناريو | الهدف | مصدر التعليمات / مجموعة البيانات |
|---------------|----------|-------|-----------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | فريق منصة الحافة يختار SLM الافتراضي لميزة تلخيص مدمجة | إنتاج مقارنة الكمون + p95 + الرموز/الثانية عبر النماذج المرشحة | متغير `PROMPT` المدمج + قائمة `BENCH_MODELS` في البيئة |

### سرد السيناريو
يجب على فريق هندسة المنتج اختيار نموذج تلخيص خفيف الوزن افتراضي لميزة ملاحظات الاجتماعات غير المتصلة. يقومون بتشغيل قياسات محددة ومضبوطة (temperature=0) عبر مجموعة تعليمات ثابتة (انظر المثال أدناه) ويجمعون مقاييس الكمون ومعدل المعالجة مع وبدون تسريع GPU.

### مثال مجموعة التعليمات JSON (قابلة للتوسيع)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

قم بتكرار كل تعليمات لكل نموذج، وقم بالتقاط الكمون لكل تعليمات لاشتقاق مقاييس التوزيع واكتشاف القيم الشاذة.

## إطار عمل اختيار النموذج

| البعد | المقياس | الأهمية |
|-------|---------|---------|
| الكمون | متوسط / p95 | اتساق تجربة المستخدم |
| معدل المعالجة | الرموز/الثانية | قابلية التوسع في الدُفعات والبث |
| الذاكرة | الحجم المقيم | التوافق مع الجهاز والتزامن |
| الجودة | تعليمات التقييم | ملاءمة المهمة |
| البصمة | تخزين القرص | التوزيع والتحديثات |
| الترخيص | السماح بالاستخدام | الامتثال التجاري |

## التوسيع باستخدام نموذج مخصص

النمط عالي المستوى (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

راجع المستودع الرسمي للحصول على واجهات التكيف المتطورة:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## استكشاف الأخطاء وإصلاحها

| المشكلة | السبب | الحل |
|---------|-------|------|
| نفاد الذاكرة مع mistral-7b | ذاكرة RAM/GPU غير كافية | إيقاف النماذج الأخرى؛ جرب إصدار أصغر |
| استجابة أولى بطيئة | تحميل بارد | حافظ على النشاط باستخدام تعليمات خفيفة دورية |
| توقف التنزيل | عدم استقرار الشبكة | إعادة المحاولة؛ التحميل المسبق خلال أوقات الذروة المنخفضة |

## المراجع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- اكتشاف نماذج Hugging Face: https://huggingface.co/models

---

**مدة الجلسة**: 30 دقيقة (+ تعمق اختياري)  
**الصعوبة**: متوسط

### تحسينات اختيارية

| التحسين | الفائدة | الطريقة |
|---------|---------|---------|
| كمون أول رمز في البث | قياس استجابة المستخدم المدركة | تشغيل القياس باستخدام `BENCH_STREAM=1` (نص محسن في `Workshop/samples/session03`) |
| وضع الحتمية | مقارنات استقرار الانحدار | `temperature=0`، مجموعة تعليمات ثابتة، التقاط مخرجات JSON تحت التحكم في الإصدار |
| تسجيل نوعي | إضافة بُعد نوعي | الحفاظ على `prompts.json` مع الجوانب المتوقعة؛ تسجيل الدرجات (1–5) يدويًا أو عبر نموذج ثانوي |
| تصدير CSV / Markdown | تقرير قابل للمشاركة | توسيع النص لكتابة `benchmark_report.md` مع جدول وملخصات |
| علامات قدرات النموذج | تساعد في التوجيه الآلي لاحقًا | الحفاظ على `models.json` مع `{alias: {capabilities:[], size_mb:..}}` |
| مرحلة تسخين التخزين المؤقت | تقليل تحيز التحميل البارد | تنفيذ جولة تسخين واحدة قبل حلقة التوقيت (تم تنفيذها بالفعل) |
| دقة النسبة المئوية | كمون الذيل القوي | استخدام numpy percentile (موجود بالفعل في النص المعاد صياغته) |
| تقدير تكلفة الرموز | مقارنة اقتصادية | التكلفة التقريبية = (الرموز/الثانية * متوسط الرموز لكل طلب) * تقدير الطاقة |
| تخطي النماذج الفاشلة تلقائيًا | المرونة في تشغيل الدُفعات | تغليف كل قياس في try/except وتحديد حقل الحالة |

#### مقتطف تصدير Markdown بسيط

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### مثال مجموعة تعليمات حتمية

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

قم بتكرار القائمة الثابتة بدلاً من التعليمات العشوائية للحصول على مقاييس قابلة للمقارنة عبر الالتزامات.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->