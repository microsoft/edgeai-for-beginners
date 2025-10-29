<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T20:21:15+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ar"
}
-->
# الجلسة 6: Foundry Local – النماذج كأدوات

## الملخص

تعامل مع النماذج كأدوات قابلة للتكوين داخل طبقة تشغيل الذكاء الاصطناعي المحلية. تعرض هذه الجلسة كيفية ربط استدعاءات متعددة لنماذج SLM/LLM المتخصصة، توجيه المهام بشكل انتقائي، وتوفير واجهة SDK موحدة للتطبيقات. ستقوم ببناء موجه نماذج خفيف الوزن + مخطط مهام، دمجه في نص تطبيق، وتوضيح مسار التوسع إلى Azure AI Foundry للمهام الإنتاجية.

## أهداف التعلم

- **تصور** النماذج كأدوات ذرية ذات قدرات معلنة
- **توجيه** الطلبات بناءً على النية / تسجيل الاستدلال
- **ربط** المخرجات عبر مهام متعددة الخطوات (تفكيك → حل → تحسين)
- **دمج** واجهة API موحدة للتطبيقات النهائية
- **توسيع** التصميم إلى السحابة (نفس العقد المتوافقة مع OpenAI)

## المتطلبات الأساسية

- إكمال الجلسات 1–5
- تخزين نماذج محلية متعددة (مثل `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### مقتطف بيئة متعددة المنصات

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

الوصول إلى الخدمة عن بُعد/VM من macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## تدفق العرض التوضيحي (30 دقيقة)

### 1. إعلان قدرات الأدوات (5 دقائق)

إنشاء `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. اكتشاف النية والتوجيه (8 دقائق)

إنشاء `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. ربط المهام متعددة الخطوات (7 دقائق)

إنشاء `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. مشروع البداية: تعديل `06-models-as-tools` (5 دقائق)

التحسينات:
- إضافة دعم تدفق الرموز (تحديث واجهة المستخدم التدريجي)
- إضافة تسجيل الثقة: تداخل لغوي أو معيار التوجيه
- تصدير تتبع JSON (النية → النموذج → التأخير → استخدام الرموز)
- تنفيذ إعادة استخدام التخزين المؤقت للخطوات المتكررة

### 5. مسار التوسع إلى Azure (5 دقائق)

| الطبقة | محلي (Foundry) | السحابة (Azure AI Foundry) | استراتيجية الانتقال |
|-------|-----------------|--------------------------|---------------------|
| التوجيه | Python استدلالي | خدمة صغيرة دائمة | حاوية ونشر API |
| النماذج | نماذج مخزنة | عمليات نشر مُدارة | ربط الأسماء المحلية بمعرفات النشر |
| المراقبة | إحصائيات CLI/يدوي | تسجيل مركزي ومقاييس | إضافة أحداث تتبع منظمة |
| الأمان | المضيف المحلي فقط | مصادقة Azure / الشبكات | إدخال خزنة المفاتيح للأسرار |
| التكلفة | موارد الجهاز | فواتير الاستهلاك | إضافة حدود الميزانية |

## قائمة التحقق من التحقق

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

توقع اختيار النموذج بناءً على النية والمخرجات النهائية المحسنة.

## استكشاف الأخطاء وإصلاحها

| المشكلة | السبب | الحل |
|---------|-------|-----|
| جميع المهام موجهة إلى نفس النموذج | قواعد ضعيفة | تحسين مجموعة INTENT_RULES regex |
| فشل خط الأنابيب في منتصف الخطوة | النموذج غير محمل | تشغيل `foundry model run <model>` |
| انخفاض تماسك المخرجات | لا توجد مرحلة تحسين | إضافة تمرير التلخيص/التحقق |

## المراجع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- وثائق Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- أنماط جودة التوجيه: انظر الجلسة 2

---

**مدة الجلسة**: 30 دقيقة  
**الصعوبة**: خبير

## سيناريو العينة وتخطيط الورشة

| نصوص الورشة / دفاتر الملاحظات | السيناريو | الهدف | مصدر البيانات / الكتالوج |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | مساعد المطور يتعامل مع مطالب مختلطة النية (إعادة صياغة، تلخيص، تصنيف) | استدلال النية → توجيه اسم النموذج مع استخدام الرموز | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | تخطيط متعدد الخطوات وتحسين لمهمة مساعدة البرمجة المعقدة | تفكيك → تنفيذ متخصص → خطوة تحسين التلخيص | نفس `CATALOG`; الخطوات مشتقة من مخرجات الخطة |

### سرد السيناريو
أداة إنتاجية هندسية تتلقى مهام متنوعة: إعادة صياغة الكود، تلخيص الملاحظات المعمارية، تصنيف الملاحظات. لتقليل التأخير واستخدام الموارد، يقوم نموذج عام صغير بالتخطيط والتلخيص، بينما يتعامل نموذج متخصص بالكود مع إعادة الصياغة، ونموذج خفيف الوزن قادر على التصنيف يقوم بتسمية الملاحظات. يوضح نص خط الأنابيب الربط + التحسين؛ بينما يعزل نص الموجه التوجيه التكيفي لمطالب فردية.

### لقطة الكتالوج
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### أمثلة مطالب الاختبار
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### تمديد التتبع (اختياري)
إضافة خطوط تتبع JSON لكل خطوة لـ `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### استدلال التصعيد (فكرة)
إذا احتوت الخطة على كلمات مثل "تحسين"، "الأمان"، أو طول الخطوة > 280 حرفًا → التصعيد إلى نموذج أكبر (مثل `gpt-oss-20b`) لتلك الخطوة فقط.

### تحسينات اختيارية

| المجال | التحسين | القيمة | التلميح |
|------|-------------|-------|------|
| التخزين المؤقت | إعادة استخدام مدير + كائنات العميل | تقليل التأخير، تقليل الحمل | استخدم `workshop_utils.get_client` |
| مقاييس الاستخدام | التقاط الرموز وتأخير كل خطوة | التوصيف والتحسين | قياس كل استدعاء موجه؛ تخزين في قائمة التتبع |
| التوجيه التكيفي | واعي بالثقة / التكلفة | تحسين جودة التكلفة | إضافة تسجيل: إذا كان الطلب > N حرفًا أو تطابق regex المجال → التصعيد إلى نموذج أكبر |
| سجل القدرات الديناميكي | إعادة تحميل الكتالوج الساخن | لا إعادة تشغيل أو إعادة نشر | تحميل `catalog.json` أثناء التشغيل؛ مراقبة طابع الوقت للملف |
| استراتيجية التراجع | القوة تحت الفشل | توفر أعلى | تجربة الأساسي → عند استثناء التراجع إلى الاسم المستعار |
| خط أنابيب التدفق | ردود فعل مبكرة | تحسين تجربة المستخدم | تدفق كل خطوة وتخزين مدخلات التحسين النهائية |
| تضمينات نية المتجه | توجيه أكثر دقة | دقة نية أعلى | تضمين الطلب، تجميع وتعيين المركز → القدرة |
| تصدير التتبع | سلسلة قابلة للتدقيق | الامتثال/التقارير | إصدار خطوط JSON: الخطوة، النية، النموذج، التأخير_ms، الرموز |
| محاكاة التكلفة | تقدير ما قبل السحابة | تخطيط الميزانية | تعيين تكلفة رمزية/النموذج وتجمع لكل مهمة |
| الوضع الحتمي | إعادة إنتاج قابلة للتكرار | معيار مستقر | البيئة: `temperature=0`, عدد خطوات ثابت |

#### مثال هيكل التتبع

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### رسم تخطيطي للتصعيد التكيفي

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### إعادة تحميل كتالوج النماذج الساخن

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.