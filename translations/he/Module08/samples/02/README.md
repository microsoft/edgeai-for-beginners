# דוגמה 02: אינטגרציה עם OpenAI SDK

מדגים אינטגרציה מתקדמת עם OpenAI Python SDK, תומך גם ב-Microsoft Foundry Local וגם ב-Azure OpenAI עם תגובות סטרימינג וטיפול נכון בשגיאות.

## סקירה כללית

הדוגמה מציגה:
- מעבר חלק בין Foundry Local ל-Azure OpenAI
- תגובות סטרימינג לשיפור חוויית המשתמש
- שימוש נכון ב-SDK של FoundryLocalManager
- טיפול בשגיאות ומנגנוני גיבוי חזקים
- תבניות קוד מוכנות לייצור

## דרישות מקדימות

- **Foundry Local**: מותקן ופועל (לצורך חישוב מקומי)
- **Python**: גרסה 3.8 או מאוחרת יותר עם OpenAI SDK
- **Azure OpenAI**: נקודת קצה ומפתח API תקפים (לצורך חישוב בענן)

## התקנה

1. **הגדרת סביבת Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **התקנת תלות:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **הפעלת Foundry Local (למצב מקומי):**
   ```cmd
   foundry model run phi-4-mini
   ```


## תרחישי שימוש

### Foundry Local (ברירת מחדל)

**אפשרות 1: שימוש ב-FoundryLocalManager (מומלץ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**אפשרות 2: הגדרה ידנית**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## ארכיטקטורת קוד

### תבנית Factory ללקוח

הדוגמה משתמשת בתבנית Factory ליצירת לקוחות מתאימים:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### תגובות סטרימינג

הדוגמה מדגימה סטרימינג ליצירת תגובות בזמן אמת:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## משתני סביבה

### הגדרת Foundry Local

| משתנה | תיאור | ברירת מחדל | חובה |
|-------|-------|------------|------|
| `MODEL` | כינוי המודל לשימוש | `phi-4-mini` | לא |
| `BASE_URL` | נקודת קצה של Foundry Local | `http://localhost:8000` | לא |
| `API_KEY` | מפתח API (אופציונלי למצב מקומי) | `""` | לא |

### הגדרת Azure OpenAI

| משתנה | תיאור | ברירת מחדל | חובה |
|-------|-------|------------|------|
| `AZURE_OPENAI_ENDPOINT` | נקודת קצה של משאב Azure OpenAI | - | כן |
| `AZURE_OPENAI_API_KEY` | מפתח API של Azure OpenAI | - | כן |
| `AZURE_OPENAI_API_VERSION` | גרסת API | `2024-08-01-preview` | לא |
| `MODEL` | שם הפריסה של Azure | `your-deployment-name` | כן |

## תכונות מתקדמות

### גילוי שירות אוטומטי

הדוגמה מזהה אוטומטית את השירות המתאים בהתבסס על משתני סביבה:

1. **מצב Azure**: אם `AZURE_OPENAI_ENDPOINT` ו-`AZURE_OPENAI_API_KEY` מוגדרים
2. **מצב SDK של Foundry**: אם Foundry Local SDK זמין
3. **מצב ידני**: גיבוי להגדרה ידנית

### טיפול בשגיאות

- מעבר חלק מ-SDK להגדרה ידנית
- הודעות שגיאה ברורות לצורך פתרון בעיות
- טיפול נכון בחריגות עבור בעיות רשת
- אימות משתני סביבה נדרשים

## שיקולי ביצועים

### יתרונות מקומי מול ענן

**יתרונות Foundry Local:**
- ✅ ללא עלויות API
- ✅ פרטיות נתונים (הנתונים לא יוצאים מהמכשיר)
- ✅ זמן תגובה נמוך עבור מודלים נתמכים
- ✅ עובד במצב לא מקוון

**יתרונות Azure OpenAI:**
- ✅ גישה למודלים גדולים ומתקדמים
- ✅ תפוקה גבוהה יותר
- ✅ ללא דרישות חישוב מקומי
- ✅ SLA ברמה ארגונית

## פתרון בעיות

### בעיות נפוצות

1. **אזהרה: "לא ניתן להשתמש ב-SDK של Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **שגיאות אימות של Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **המודל אינו זמין:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### בדיקות בריאות

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## צעדים הבאים

- **דוגמה 03**: גילוי מודלים וביצועי השוואה
- **דוגמה 04**: בניית אפליקציית Chainlit RAG
- **דוגמה 05**: תזמור רב-סוכנים
- **דוגמה 06**: ניתוב מודלים ככלים

## מקורות

- [תיעוד Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [תיעוד SDK של Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [תיעוד OpenAI Python SDK](https://github.com/openai/openai-python)
- [מדריך תגובות סטרימינג](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

