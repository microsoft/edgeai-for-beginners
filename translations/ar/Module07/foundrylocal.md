# Foundry Local على ويندوز وماك

هذا الدليل يساعدك على تثبيت وتشغيل ودمج Microsoft Foundry Local على ويندوز وماك. جميع الخطوات والأوامر تم التحقق منها وفقًا لوثائق Microsoft Learn.

- البدء: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- الهندسة المعمارية: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- مرجع CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- دمج SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- تجميع نماذج HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: محلي مقابل السحابة: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) التثبيت / الترقية على ويندوز

- التثبيت:
```cmd
winget install Microsoft.FoundryLocal
```
- الترقية:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- التحقق من الإصدار:
```cmd
foundry --version
```
     
**التثبيت / ماك**

**MacOS**: 
افتح نافذة الطرفية وقم بتشغيل الأمر التالي:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) أساسيات CLI (ثلاث فئات)

- النموذج:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- الخدمة:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- التخزين المؤقت:
```cmd
foundry cache --help
foundry cache list
```

ملاحظات:
- الخدمة توفر واجهة REST API متوافقة مع OpenAI. يتم تخصيص منفذ نقطة النهاية ديناميكيًا؛ استخدم `foundry service status` لاكتشافه.
- استخدم SDKs للراحة؛ فهي تتعامل مع اكتشاف نقطة النهاية تلقائيًا حيثما كان ذلك مدعومًا.

## 3) اكتشاف نقطة النهاية المحلية (منفذ ديناميكي)

يقوم Foundry Local بتخصيص منفذ ديناميكي في كل مرة يتم فيها بدء الخدمة:
```cmd
foundry service status
```
استخدم `http://localhost:<PORT>` المبلغ عنه كـ `base_url` مع المسارات المتوافقة مع OpenAI (على سبيل المثال، `/v1/chat/completions`).

## 4) اختبار سريع عبر OpenAI Python SDK

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
المراجع:
- دمج SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) استخدم النموذج الخاص بك (تجميع باستخدام Olive)

إذا كنت بحاجة إلى نموذج غير موجود في الكتالوج، قم بتجميعه إلى ONNX لـ Foundry Local باستخدام Olive.

التدفق العام (راجع الوثائق للخطوات):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
الوثائق:
- تجميع BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) استكشاف الأخطاء وإصلاحها

- تحقق من حالة الخدمة والسجلات:
```cmd
foundry service status
foundry service diag
```
- مسح أو نقل التخزين المؤقت:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- التحديث إلى أحدث معاينة:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) تجربة المطورين على ويندوز

- خيارات الذكاء الاصطناعي المحلي مقابل السحابة على ويندوز، بما في ذلك Foundry Local وWindows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- أدوات الذكاء الاصطناعي في VS Code مع Foundry Local (استخدم `foundry service status` للحصول على عنوان URL لنقطة نهاية الدردشة):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[المطور التالي على ويندوز](./windowdeveloper.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.