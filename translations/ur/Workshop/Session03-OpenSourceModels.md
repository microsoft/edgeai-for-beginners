<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T21:47:36+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ur"
}
-->
# سیشن 3: فاؤنڈری لوکل میں اوپن سورس ماڈلز

## خلاصہ

جانیں کہ Hugging Face اور دیگر اوپن سورس ماڈلز کو فاؤنڈری لوکل میں کیسے لایا جا سکتا ہے۔ انتخاب کی حکمت عملی، کمیونٹی تعاون کے ورک فلو، کارکردگی کے موازنہ کے طریقے، اور فاؤنڈری کو کسٹم ماڈل رجسٹریشن کے ساتھ کیسے بڑھایا جا سکتا ہے، کے بارے میں سیکھیں۔ یہ سیشن ہفتہ وار "ماڈل منڈے" کے موضوعات سے مطابقت رکھتا ہے اور آپ کو اوپن سورس ماڈلز کو مقامی طور پر جانچنے اور عملی بنانے کے قابل بناتا ہے، اس سے پہلے کہ Azure پر اس کا دائرہ وسیع کیا جائے۔

## سیکھنے کے مقاصد

آخر تک آپ یہ کر سکیں گے:

- **دریافت اور جانچ**: معیار بمقابلہ وسائل کے توازن کا استعمال کرتے ہوئے امیدوار ماڈلز (mistral، gemma، qwen، deepseek) کی شناخت کریں۔
- **لوڈ اور چلائیں**: فاؤنڈری لوکل CLI کا استعمال کرتے ہوئے کمیونٹی ماڈلز کو ڈاؤن لوڈ، کیش، اور لانچ کریں۔
- **بینچ مارک**: مستقل لیٹنسی + ٹوکن تھروپٹ + معیار کے اصولوں کا اطلاق کریں۔
- **توسیع کریں**: SDK-مطابقت پذیر پیٹرنز کی پیروی کرتے ہوئے کسٹم ماڈل ریپر رجسٹر یا اپنائیں۔
- **موازنہ کریں**: SLM بمقابلہ درمیانے سائز کے LLM انتخاب کے فیصلوں کے لیے منظم موازنہ تیار کریں۔

## ضروریات

- سیشن 1 اور 2 مکمل کیے گئے ہوں
- Python ماحول جس میں `foundry-local-sdk` انسٹال ہو
- متعدد ماڈل کیشز کے لیے کم از کم 15GB خالی ڈسک

### کراس پلیٹ فارم ماحول فوری آغاز

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

جب macOS سے Windows میزبان سروس کے خلاف بینچ مارکنگ کریں، تو سیٹ کریں:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ڈیمو فلو (30 منٹ)

### 1. CLI کے ذریعے Hugging Face ماڈلز لوڈ کریں (8 منٹ)

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


### 2. چلائیں اور فوری جانچ کریں (5 منٹ)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. بینچ مارک اسکرپٹ (8 منٹ)

`samples/03-oss-models/benchmark_models.py` بنائیں:

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

چلائیں:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. کارکردگی کا موازنہ کریں (5 منٹ)

تجارت کے پہلوؤں پر بات کریں: لوڈ کا وقت، میموری کا استعمال (Task Manager / `nvidia-smi` / OS resource monitor کا مشاہدہ کریں)، آؤٹ پٹ کا معیار بمقابلہ رفتار۔ لیٹنسی اور تھروپٹ کے لیے Python بینچ مارک اسکرپٹ (سیشن 3) استعمال کریں؛ GPU ایکسیلیریشن فعال کرنے کے بعد دوبارہ آزمائیں۔

### 5. اسٹارٹر پروجیکٹ (4 منٹ)

ماڈل موازنہ رپورٹ جنریٹر بنائیں (بینچ مارکنگ اسکرپٹ کو مارک ڈاؤن ایکسپورٹ کے ساتھ بڑھائیں)۔

## اسٹارٹر پروجیکٹ: `03-huggingface-models` کو بڑھائیں

موجودہ نمونے کو بہتر بنائیں:

1. بینچ مارک ایگریگیشن + CSV/Markdown آؤٹ پٹ شامل کریں۔
2. سادہ معیاری اسکورنگ نافذ کریں (پرامپٹ جوڑی سیٹ + دستی تشریح اسٹب فائل)۔
3. JSON کنفیگریشن (`models.json`) متعارف کروائیں تاکہ ماڈل کی فہرست اور پرامپٹ سیٹ کو پلگ ان کیا جا سکے۔

## توثیق چیک لسٹ

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

تمام ہدف ماڈلز کو ظاہر ہونا چاہیے اور پروب چیٹ درخواست کا جواب دینا چاہیے۔

## نمونہ منظر نامہ اور ورکشاپ میپنگ

| ورکشاپ اسکرپٹ | منظر نامہ | مقصد | پرامپٹ / ڈیٹاسیٹ ماخذ |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ایج پلیٹ فارم ٹیم جو ایمبیڈڈ سمریزر کے لیے ڈیفالٹ SLM کا انتخاب کر رہی ہے | امیدوار ماڈلز کے درمیان لیٹنسی + p95 + ٹوکنز/سیکنڈ کا موازنہ تیار کریں | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### منظر نامہ بیانیہ

پروڈکٹ انجینئرنگ کو آف لائن میٹنگ نوٹس فیچر کے لیے ڈیفالٹ ہلکے وزن کا سمری ماڈل منتخب کرنا ہوگا۔ وہ ایک مقررہ پرامپٹ سیٹ (نیچے دیے گئے مثال دیکھیں) کے ساتھ کنٹرولڈ ڈیٹرمینسٹک بینچ مارکس (temperature=0) چلاتے ہیں اور GPU ایکسیلیریشن کے ساتھ اور بغیر لیٹنسی + تھروپٹ میٹرکس جمع کرتے ہیں۔

### مثال پرامپٹ سیٹ JSON (قابل توسیع)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

ہر ماڈل کے لیے ہر پرامپٹ کو لوپ کریں، پرامپٹ لیٹنسی کو کیپچر کریں تاکہ تقسیم میٹرکس حاصل کریں اور آؤٹ لیئرز کا پتہ لگائیں۔

## ماڈل انتخاب کا فریم ورک

| جہت | میٹرک | کیوں اہم ہے |
|----------|--------|----------------|
| لیٹنسی | avg / p95 | صارف کے تجربے کی مستقل مزاجی |
| تھروپٹ | ٹوکنز/سیکنڈ | بیچ اور اسٹریمنگ کی توسیع پذیری |
| میموری | رہائشی سائز | ڈیوائس فٹ اور ہم وقتی |
| معیار | روبریک پرامپٹس | کام کی موزونیت |
| فٹ پرنٹ | ڈسک کیش | تقسیم اور اپڈیٹس |
| لائسنس | استعمال کی اجازت | تجارتی تعمیل |

## کسٹم ماڈل کے ساتھ توسیع

اعلی سطحی پیٹرن (پسیوڈو):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

ایڈاپٹر انٹرفیس کے ارتقاء کے لیے آفیشل ریپو سے مشورہ کریں:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## خرابیوں کا ازالہ

| مسئلہ | وجہ | حل |
|-------|-------|-----|
| mistral-7b پر OOM | ناکافی RAM/GPU | دیگر ماڈلز کو بند کریں؛ چھوٹے ورژن کو آزمائیں |
| پہلا جواب سست | کولڈ لوڈ | ہلکے وزن کے پرامپٹ کے ساتھ وقتاً فوقتاً گرم رکھیں |
| ڈاؤن لوڈ رک گیا | نیٹ ورک کی غیر استحکام | دوبارہ کوشش کریں؛ آف پیک کے دوران پیشگی ڈاؤن لوڈ کریں |

## حوالہ جات

- فاؤنڈری لوکل SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- ماڈل منڈے: https://aka.ms/model-mondays
- Hugging Face ماڈل دریافت: https://huggingface.co/models

---

**سیشن کا دورانیہ**: 30 منٹ (+ اختیاری گہرائی میں جانا)  
**مشکل کی سطح**: درمیانی

### اختیاری بہتریاں

| بہتری | فائدہ | کیسے |
|-------------|---------|-----|
| اسٹریمنگ فرسٹ-ٹوکن لیٹنسی | محسوس شدہ ردعمل کی پیمائش کرتا ہے | `BENCH_STREAM=1` کے ساتھ بینچ مارک چلائیں (ورکشاپ/samples/session03 میں بہتر اسکرپٹ) |
| ڈیٹرمینسٹک موڈ | مستحکم ریگریشن موازنہ | `temperature=0`, مقررہ پرامپٹ سیٹ، JSON آؤٹ پٹس کو ورژن کنٹرول کے تحت کیپچر کریں |
| معیار روبریک اسکورنگ | معیاری جہت شامل کرتا ہے | `prompts.json` کو متوقع پہلوؤں کے ساتھ برقرار رکھیں؛ اسکورز (1–5) کو دستی طور پر یا ثانوی ماڈل کے ذریعے تشریح کریں |
| CSV / Markdown ایکسپورٹ | شیئر ایبل رپورٹ | اسکرپٹ کو `benchmark_report.md` لکھنے کے لیے بڑھائیں جس میں ٹیبل اور جھلکیاں ہوں |
| ماڈل قابلیت ٹیگز | بعد میں خودکار روٹنگ میں مدد کرتا ہے | `models.json` کو برقرار رکھیں جس میں `{alias: {capabilities:[], size_mb:..}}` ہو |
| کیش وارم اپ فیز | کولڈ اسٹارٹ تعصب کو کم کریں | وقت کے لوپ سے پہلے ایک گرم راؤنڈ انجام دیں (پہلے ہی نافذ کیا گیا ہے) |
| پرسنٹائل درستگی | مضبوط ٹیل لیٹنسی | numpy پرسنٹائل استعمال کریں (پہلے سے ہی ریفیکٹڈ اسکرپٹ میں) |
| ٹوکن لاگت کا تخمینہ | اقتصادی موازنہ | تخمینہ لاگت = (tokens/sec * avg tokens per request) * energy heuristic |
| ناکام ماڈلز کو خودکار طور پر چھوڑنا | بیچ رنز میں لچک | ہر بینچ مارک کو try/except میں لپیٹیں اور اسٹیٹس فیلڈ کو نشان زد کریں |

#### کم سے کم مارک ڈاؤن ایکسپورٹ اسنیپ شاٹ

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### ڈیٹرمینسٹک پرامپٹ سیٹ مثال

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

جامد فہرست کو لوپ کریں بجائے کہ بے ترتیب پرامپٹس کے، تاکہ کمیٹس کے درمیان قابل موازنہ میٹرکس حاصل ہو سکیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->