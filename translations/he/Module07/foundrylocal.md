# Foundry Local ב-Windows וב-Mac

מדריך זה מסביר כיצד להתקין, להפעיל ולשלב את Microsoft Foundry Local ב-Windows וב-Mac. כל השלבים והפקודות נבדקו מול מסמכי Microsoft Learn.

- התחלה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started  
- ארכיטקטורה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture  
- עזרי CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli  
- שילוב SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks  
- קומפילציה של מודלים HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models  
- Windows AI: מקומי מול ענן: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers  

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
פתחו טרמינל והריצו את הפקודה הבאה:  
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```
  

## 2) יסודות CLI (שלוש קטגוריות)

- מודל:  
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
- השירות חושף API REST תואם OpenAI. הפורט של נקודת הקצה מוקצה באופן דינמי; השתמשו ב-`foundry service status` כדי לגלות אותו.  
- השתמשו ב-SDKs לנוחות; הם מטפלים בגילוי נקודת הקצה באופן אוטומטי כאשר נתמך.  

## 3) גילוי נקודת הקצה המקומית (פורט דינמי)

Foundry Local מקצה פורט דינמי בכל פעם שהשירות מתחיל:  
```cmd
foundry service status
```
  
השתמשו ב-`http://localhost:<PORT>` שדווח כ-`base_url` שלכם עם נתיבים תואמי OpenAI (לדוגמה, `/v1/chat/completions`).  

## 4) בדיקה מהירה באמצעות OpenAI Python SDK

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

## 5) הביאו מודל משלכם (קומפילציה עם Olive)

אם אתם זקוקים למודל שאינו נמצא בקטלוג, קומפלו אותו ל-ONNX עבור Foundry Local באמצעות Olive.

תהליך ברמה גבוהה (ראו מסמכים לשלבים):  
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
  
מסמכים:  
- קומפילציה BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models  

## 6) פתרון בעיות

- בדיקת סטטוס השירות ולוגים:  
```cmd
foundry service status
foundry service diag
```
  
- ניקוי או העברת מטמון:  
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
  
- עדכון לגרסת התצוגה המקדימה האחרונה:  
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
  

## 7) חוויית פיתוח קשורה ב-Windows

- בחירות AI מקומי מול ענן ב-Windows, כולל Foundry Local ו-Windows ML:  
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers  
- ערכת כלים AI של VS Code עם Foundry Local (השתמשו ב-`foundry service status` כדי לקבל את כתובת URL של נקודת הקצה לשיחה):  
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components  

[מפתח Windows הבא](./windowdeveloper.md)  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.