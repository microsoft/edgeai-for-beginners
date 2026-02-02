# سیشن 6: فاؤنڈری لوکل – ماڈلز بطور ٹولز

## خلاصہ

ماڈلز کو مقامی AI آپریٹنگ لیئر کے اندر کمپوزیبل ٹولز کے طور پر سمجھیں۔ اس سیشن میں دکھایا جائے گا کہ کس طرح متعدد خاص SLM/LLM کالز کو جوڑنا، کاموں کو منتخب طور پر روٹ کرنا، اور ایپلیکیشنز کے لیے ایک متحد SDK سطح کو ظاہر کرنا ہے۔ آپ ایک ہلکا پھلکا ماڈل روٹر + ٹاسک پلانر بنائیں گے، اسے ایک ایپ اسکرپٹ میں ضم کریں گے، اور پروڈکشن ورک لوڈز کے لیے Azure AI Foundry تک اسکیلنگ کا راستہ بیان کریں گے۔

## سیکھنے کے مقاصد

- **تصور کریں** ماڈلز کو ایٹمی ٹولز کے طور پر جن کی صلاحیتیں واضح ہوں
- **روٹ کریں** درخواستیں ارادے / ہیورسٹک اسکورنگ کی بنیاد پر
- **چین کریں** آؤٹ پٹس کو کثیر مرحلہ کاموں میں (تقسیم کریں → حل کریں → بہتر کریں)
- **ضم کریں** ایک متحد کلائنٹ API کو نیچے کی ایپلیکیشنز کے لیے
- **اسکیل کریں** ڈیزائن کو کلاؤڈ پر (ایک ہی OpenAI-مطابق معاہدہ)

## ضروریات

- سیشنز 1–5 مکمل کیے گئے ہوں
- متعدد مقامی ماڈلز کیش کیے گئے ہوں (جیسے، `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### کراس-پلیٹ فارم ماحول کا ٹکڑا

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

Remote/VM سروس تک رسائی macOS سے:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ڈیمو فلو (30 منٹ)

### 1. ٹول کی صلاحیت کا اعلان (5 منٹ)

`samples/06-tools/models_catalog.py` بنائیں:

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


### 2. ارادے کی شناخت اور روٹنگ (8 منٹ)

`samples/06-tools/router.py` بنائیں:

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


### 3. کثیر مرحلہ ٹاسک چیننگ (7 منٹ)

`samples/06-tools/pipeline.py` بنائیں:

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


### 4. اسٹارٹر پروجیکٹ: `06-models-as-tools` کو اپنانا (5 منٹ)

بہتریاں:
- اسٹریمنگ ٹوکن سپورٹ شامل کریں (پروگریسو UI اپ ڈیٹ)
- اعتماد اسکورنگ شامل کریں: لغوی اوورلیپ یا پرامپٹ روبریک
- ٹریس JSON برآمد کریں (ارادہ → ماڈل → لیٹنسی → ٹوکن استعمال)
- بار بار سب اسٹیپس کے لیے کیش کا دوبارہ استعمال نافذ کریں

### 5. Azure تک اسکیلنگ کا راستہ (5 منٹ)

| لیئر | لوکل (فاؤنڈری) | کلاؤڈ (Azure AI Foundry) | منتقلی کی حکمت عملی |
|------|----------------|--------------------------|---------------------|
| روٹنگ | ہیورسٹک Python | پائیدار مائیکرو سروس | API کو کنٹینرائز کریں اور تعینات کریں |
| ماڈلز | SLMs کیش کیے گئے | منظم تعیناتیاں | مقامی ناموں کو تعیناتی IDs سے میپ کریں |
| مشاہدہ | CLI اعدادوشمار/دستی | مرکزی لاگنگ اور میٹرکس | ساختی ٹریس ایونٹس شامل کریں |
| سیکیورٹی | صرف لوکل ہوسٹ | Azure تصدیق / نیٹ ورکنگ | رازوں کے لیے کلیدی والٹ متعارف کروائیں |
| لاگت | ڈیوائس وسائل | کھپت بلنگ | بجٹ گارڈریلز شامل کریں |

## توثیق کی چیک لسٹ

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

ارادے پر مبنی ماڈل کا انتخاب اور حتمی بہتر آؤٹ پٹ کی توقع کریں۔

## خرابیوں کا پتہ لگانا

| مسئلہ | وجہ | حل |
|-------|-----|-----|
| تمام کام ایک ہی ماڈل پر روٹ ہو رہے ہیں | کمزور قواعد | INTENT_RULES regex سیٹ کو بہتر کریں |
| پائپ لائن درمیان میں ناکام ہو رہی ہے | لوڈ کیا گیا ماڈل غائب ہے | `foundry model run <model>` چلائیں |
| آؤٹ پٹ کا ہم آہنگی کم ہے | کوئی بہتر مرحلہ نہیں | خلاصہ/توثیق پاس شامل کریں |

## حوالہ جات

- فاؤنڈری لوکل SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- پرامپٹ کوالٹی پیٹرنز: سیشن 2 دیکھیں

---

**سیشن کا دورانیہ**: 30 منٹ  
**مشکل**: ماہر

## نمونہ منظر نامہ اور ورکشاپ میپنگ

| ورکشاپ اسکرپٹس / نوٹ بکس | منظر نامہ | مقصد | ڈیٹاسیٹ / کیٹلاگ سورس |
|--------------------------|-----------|-------|-----------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ڈویلپر اسسٹنٹ جو مخلوط ارادے کے پرامپٹس کو ہینڈل کرتا ہے (ریفیکٹر، خلاصہ، درجہ بندی) | ہیورسٹک ارادہ → ماڈل عرف روٹنگ کے ساتھ ٹوکن استعمال | ان لائن `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | پیچیدہ کوڈنگ اسسٹنس ٹاسک کے لیے کثیر مرحلہ منصوبہ بندی اور بہتری | تقسیم کریں → خاص عملدرآمد → خلاصہ بہتر مرحلہ | وہی `CATALOG`; منصوبہ آؤٹ پٹ سے اخذ کردہ مراحل |

### منظر نامے کی کہانی
ایک انجینئرنگ پروڈکٹیویٹی ٹول مختلف کام وصول کرتا ہے: کوڈ کو ریفیکٹر کریں، آرکیٹیکچرل نوٹس کا خلاصہ کریں، فیڈبیک کو درجہ بند کریں۔ لیٹنسی اور وسائل کے استعمال کو کم کرنے کے لیے، ایک چھوٹا عمومی ماڈل منصوبہ بندی اور خلاصہ کرتا ہے، ایک کوڈ-خاص ماڈل ریفیکٹرنگ کو ہینڈل کرتا ہے، اور ایک ہلکا پھلکا درجہ بندی کرنے والا ماڈل فیڈبیک کو لیبل کرتا ہے۔ پائپ لائن اسکرپٹ چیننگ + بہتری کو ظاہر کرتا ہے؛ روٹر اسکرپٹ موافق سنگل-پرامپٹ روٹنگ کو الگ کرتا ہے۔

### کیٹلاگ اسنیپ شاٹ
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### مثال ٹیسٹ پرامپٹس
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### ٹریس ایکسٹینشن (اختیاری)
`models_pipeline.py` کے لیے ہر مرحلے کے ٹریس JSON لائنز شامل کریں:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### اسکیلیشن ہیورسٹک (خیال)
اگر منصوبے میں "optimize"، "security" جیسے کلیدی الفاظ شامل ہوں یا مرحلے کی لمبائی > 280 حروف ہو → اس مرحلے کے لیے بڑے ماڈل (جیسے، `gpt-oss-20b`) پر اسکیلیٹ کریں۔

### اختیاری بہتریاں

| علاقہ | بہتری | قدر | اشارہ |
|------|-------|-----|------|
| کیشنگ | مینیجر + کلائنٹ آبجیکٹس کا دوبارہ استعمال | کم لیٹنسی، کم اوور ہیڈ | `workshop_utils.get_client` استعمال کریں |
| استعمال میٹرکس | ٹوکنز اور ہر مرحلے کی لیٹنسی کو کیپچر کریں | پروفائلنگ اور آپٹیمائزیشن | ہر روٹڈ کال کا وقت لیں؛ ٹریس لسٹ میں اسٹور کریں |
| موافق روٹنگ | اعتماد / لاگت کے بارے میں آگاہ | بہتر معیار-لاگت کا توازن | اسکورنگ شامل کریں: اگر پرامپٹ > N حروف یا regex ڈومین سے میل کھاتا ہے → بڑے ماڈل پر اسکیلیٹ کریں |
| ڈائنامک صلاحیت رجسٹری | کیٹلاگ کو ہاٹ ری لوڈ کریں | دوبارہ شروع کرنے کی ضرورت نہیں | `catalog.json` کو رن ٹائم پر لوڈ کریں؛ فائل ٹائم اسٹیمپ دیکھیں |
| فال بیک حکمت عملی | ناکامیوں کے تحت مضبوطی | زیادہ دستیابی | پرائمری آزمائیں → استثنا پر فال بیک عرف |
| اسٹریمنگ پائپ لائن | ابتدائی فیڈبیک | UX میں بہتری | ہر مرحلے کو اسٹریم کریں اور حتمی بہتر ان پٹ کو بفر کریں |
| ویکٹر ارادہ ایمبیڈنگز | زیادہ باریک بینی سے روٹنگ | زیادہ ارادے کی درستگی | پرامپٹ کو ایمبیڈ کریں، کلسٹر کریں اور سینٹروئڈ کو میپ کریں → صلاحیت |
| ٹریس ایکسپورٹ | آڈٹ ایبل چین | تعمیل/رپورٹنگ | JSON لائنز جاری کریں: مرحلہ، ارادہ، ماڈل، لیٹنسی_ms، ٹوکنز |
| لاگت کی تخمینہ | پری-کلاؤڈ تخمینہ | بجٹ کی منصوبہ بندی | ہر ماڈل کے لیے ٹوکن پر خیالی لاگت تفویض کریں اور ہر کام کے لیے مجموعی کریں |
| ڈیٹرمینسٹک موڈ | دوبارہ پیدا کرنے کی قابلیت | مستحکم بینچ مارکنگ | Env: `temperature=0`, مقررہ مراحل کی تعداد |

#### ٹریس اسٹرکچر کی مثال

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### موافق اسکیلیشن خاکہ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### ماڈل کیٹلاگ ہاٹ ری لوڈ

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

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔