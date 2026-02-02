# דוגמה 01: צ'אט מהיר באמצעות OpenAI SDK

דוגמה פשוטה לצ'אט המדגימה כיצד להשתמש ב-SDK של OpenAI עם Microsoft Foundry Local לצורך הסקת AI מקומית.

## סקירה כללית

דוגמה זו מראה כיצד:
- להשתמש ב-SDK של OpenAI Python עם Foundry Local
- לטפל הן בקונפיגורציות של Azure OpenAI והן בקונפיגורציות מקומיות של Foundry
- ליישם טיפול נכון בשגיאות ואסטרטגיות גיבוי
- להשתמש ב-FoundryLocalManager לניהול שירותים

## דרישות מקדימות

- **Foundry Local**: מותקן וזמין ב-PATH
- **Python**: גרסה 3.8 או מאוחרת יותר
- **מודל**: מודל טעון ב-Foundry Local (לדוגמה, `phi-4-mini`)

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

3. **הפעלת שירות Foundry Local וטעינת מודל:**
   ```cmd
   foundry model run phi-4-mini
   ```


## שימוש

### Foundry Local (ברירת מחדל)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## תכונות קוד

### אינטגרציה עם FoundryLocalManager

הדוגמה משתמשת ב-SDK הרשמי של Foundry Local לניהול נכון של שירותים:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### טיפול בשגיאות

טיפול בשגיאות בצורה חזקה עם גיבוי לקונפיגורציה ידנית:
- גילוי שירות אוטומטי
- התמודדות הדרגתית במקרה שה-SDK אינו זמין
- הודעות שגיאה ברורות לצורך פתרון בעיות

## משתני סביבה

| משתנה | תיאור | ברירת מחדל | נדרש |
|-------|--------|------------|-------|
| `MODEL` | שם או כינוי של מודל | `phi-4-mini` | לא |
| `BASE_URL` | כתובת בסיס של Foundry Local | `http://localhost:8000` | לא |
| `API_KEY` | מפתח API (בדרך כלל לא נדרש למקומי) | `""` | לא |
| `AZURE_OPENAI_ENDPOINT` | נקודת קצה של Azure OpenAI | - | עבור Azure |
| `AZURE_OPENAI_API_KEY` | מפתח API של Azure OpenAI | - | עבור Azure |
| `AZURE_OPENAI_API_VERSION` | גרסת API של Azure | `2024-08-01-preview` | לא |

## פתרון בעיות

### בעיות נפוצות

1. **אזהרה: "לא ניתן להשתמש ב-SDK של Foundry":**
   - התקן את foundry-local-sdk: `pip install foundry-local-sdk`
   - או הגדר משתני סביבה לקונפיגורציה ידנית

2. **חיבור נדחה:**
   - ודא ש-Foundry Local פועל: `foundry service status`
   - בדוק אם מודל טעון: `foundry service ps`

3. **מודל לא נמצא:**
   - רשום את המודלים הזמינים: `foundry model list`
   - טען מודל: `foundry model run phi-4-mini`

### אימות

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## מקורות

- [תיעוד Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [תיעוד API תואם OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

