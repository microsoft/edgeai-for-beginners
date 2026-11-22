# Foundry Local ב-Windows ו-Mac

מדריך זה עוזר לך להתקין, להפעיל ולשלב את Microsoft Foundry Local ב-Windows ו-Mac. כל השלבים והפקודות מאומתים מול מסמכי Microsoft Learn.

- התחל: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ארכיטקטורה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- התייחסות ל-CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- שילוב SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- הידור דגמי HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- AI ב-Windows: מקומי מול ענן: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) התקנה / שדרוג ב-Windows

- התקנה:
```cmd
winget install Microsoft.FoundryLocal
```
- שדרוג:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- בדיקת גרסה:
```cmd
foundry --version
```
     
**התקנה / Mac**

**MacOS**: 
פתח מסוף והרץ את הפקודה הבאה:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) יסודות CLI (שלוש קטגוריות)

- דגם:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- שירות:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- מטמון:
```cmd
foundry cache --help
foundry cache list
```

הערות:
- השירות חושף API REST תואם OpenAI. פורט הקצה מוקצה דינמית; השתמש ב`foundry service status` כדי לגלות אותו.
- השתמש ב-SDK לנוחות; הם מטפלים באיתור נקודת הקצה באופן אוטומטי במערכות הנתמכות.

## 3) גלה את נקודת הקצה המקומית (פורט דינמי)

Foundry Local מקצה פורט דינמי בכל פעם שהשירות מתחיל:
```cmd
foundry service status
```
השתמש בכתובת המדווחת `http://localhost:<PORT>` כ-`base_url` עם נתיבי OpenAI תואמים (למשל, `/v1/chat/completions`).

## 4) בדיקה מהירה דרך OpenAI Python SDK

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
הפניות:
- שילוב SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) הבא את הדגם שלך (הידור עם Olive)

אם אתה צריך דגם שלא נמצא בקטלוג, המדר אותו ל-ONNX עבור Foundry Local באמצעות Olive.

תהליך כללי (ראה מסמכים לפרטים):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
מסמכים:
- הידור BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) פתרון תקלות

- בדוק את סטטוס השירות והלוגים:
```cmd
foundry service status
foundry service diag
```
- נקה או הזז את המטמון:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- עדכן לגרסת התצוגה המקדימה האחרונה:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) חוויית פיתוח קשורה ב-Windows

- אפשרויות AI מקומי מול ענן ב-Windows, כולל Foundry Local ו-Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- ערכת כלים VS Code AI עם Foundry Local (השתמש ב`foundry service status` לקבלת URL נקודת הצ'אט):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[מפתח Windows הבא](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->