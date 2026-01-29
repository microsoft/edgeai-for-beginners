# الجلسة 6: النماذج كأدوات

يقدم هذا المثال مسجلًا بسيطًا + سجل أدوات يختار نموذجًا بناءً على طلب المستخدم ويستدعي نقطة النهاية المتوافقة مع OpenAI الخاصة بـ Foundry Local.

## الملفات
- `router.py`: سجل بسيط وتوجيه استدلالي؛ اكتشاف نقطة النهاية + فحص الصحة.

## التشغيل (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## ملاحظات
- يستخدم المسجل استدلالات بسيطة تعتمد على الكلمات المفتاحية للاختيار بين أدوات `general` و`reasoning` و`code` ويطبع `/v1/models` عند البدء.
- التكوين عبر متغيرات البيئة:
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

## المراجع
- Foundry Local (تعلم): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- التكامل مع SDKs الاستدلالية: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.