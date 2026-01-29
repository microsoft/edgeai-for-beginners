# ونڈوز اور میک پر Foundry Local

یہ گائیڈ آپ کو ونڈوز اور میک پر Microsoft Foundry Local انسٹال، چلانے اور انٹیگریٹ کرنے میں مدد دیتی ہے۔ تمام مراحل اور کمانڈز Microsoft Learn ڈاکیومنٹس کے مطابق تصدیق شدہ ہیں۔

- شروع کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- آرکیٹیکچر: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI حوالہ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs انٹیگریٹ کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF ماڈلز کمپائل کریں (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- ونڈوز AI: لوکل بمقابلہ کلاؤڈ: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) ونڈوز پر انسٹال / اپگریڈ کریں

- انسٹال:
```cmd
winget install Microsoft.FoundryLocal
```
- اپگریڈ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ورژن چیک کریں:
```cmd
foundry --version
```
     
**انسٹال / میک**

**MacOS**: 
ٹرمینل کھولیں اور درج ذیل کمانڈ چلائیں:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI بنیادی باتیں (تین کیٹیگریز)

- ماڈل:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- سروس:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- کیش:
```cmd
foundry cache --help
foundry cache list
```

نوٹس:
- سروس OpenAI-compatible REST API کو ظاہر کرتی ہے۔ اینڈ پوائنٹ پورٹ ڈائنامک طور پر الاٹ کیا جاتا ہے؛ اسے دریافت کرنے کے لیے `foundry service status` استعمال کریں۔
- سہولت کے لیے SDKs استعمال کریں؛ یہ اینڈ پوائنٹ دریافت کو خودکار طور پر ہینڈل کرتے ہیں جہاں سپورٹ ہو۔

## 3) لوکل اینڈ پوائنٹ دریافت کریں (ڈائنامک پورٹ)

Foundry Local ہر بار سروس شروع ہونے پر ایک ڈائنامک پورٹ الاٹ کرتا ہے:
```cmd
foundry service status
```
رپورٹ شدہ `http://localhost:<PORT>` کو OpenAI-compatible راستوں کے ساتھ اپنے `base_url` کے طور پر استعمال کریں (مثال کے طور پر، `/v1/chat/completions`)۔

## 4) OpenAI Python SDK کے ذریعے فوری ٹیسٹ

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
حوالہ جات:
- SDK انٹیگریشن: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) اپنا ماڈل لائیں (Olive کے ساتھ کمپائل کریں)

اگر آپ کو کیٹلاگ میں موجود ماڈل کی ضرورت نہیں ہے، تو اسے Olive کے ذریعے Foundry Local کے لیے ONNX میں کمپائل کریں۔

اعلی سطحی فلو (مراحل کے لیے ڈاکیومنٹس دیکھیں):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ڈاکیومنٹس:
- BYOM کمپائل: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) خرابیوں کا پتہ لگانا

- سروس اسٹیٹس اور لاگز چیک کریں:
```cmd
foundry service status
foundry service diag
```
- کیش صاف کریں یا منتقل کریں:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- تازہ ترین پریویو پر اپڈیٹ کریں:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) متعلقہ ونڈوز ڈویلپر تجربہ

- ونڈوز لوکل بمقابلہ کلاؤڈ AI کے انتخاب، بشمول Foundry Local اور Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit کے ساتھ Foundry Local (چیٹ اینڈ پوائنٹ URL حاصل کرنے کے لیے `foundry service status` استعمال کریں):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[اگلا ونڈوز ڈویلپر](./windowdeveloper.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔