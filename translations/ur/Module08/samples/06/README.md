# سیشن 6 نمونہ: ماڈلز بطور اوزار

یہ نمونہ ایک سادہ روٹر + ٹول رجسٹری کو نافذ کرتا ہے جو صارف کے پرامپٹ کی بنیاد پر ماڈل منتخب کرتا ہے اور Foundry Local کے OpenAI-compatible endpoint کو کال کرتا ہے۔

## فائلیں
- `router.py`: سادہ رجسٹری اور ہیورسٹک روٹنگ؛ اینڈ پوائنٹ دریافت + صحت کی جانچ۔

## چلائیں (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## نوٹس
- روٹر سادہ کلیدی الفاظ کے ہیورسٹکس استعمال کرتا ہے تاکہ `general`، `reasoning`، اور `code` ٹولز کے درمیان انتخاب کرے اور شروع میں `/v1/models` پرنٹ کرے۔
- ماحول کے متغیرات کے ذریعے ترتیب دیں:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## حوالہ جات
- Foundry Local (سیکھیں): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- انفرنس SDKs کے ساتھ انضمام کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔