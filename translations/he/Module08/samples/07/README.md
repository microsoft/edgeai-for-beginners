# דוגמת Foundry Local כ-API

דוגמה זו מדגימה כיצד להשתמש ב-Microsoft Foundry Local כשירות REST API ללא תלות ב-SDK של OpenAI. היא מציגה דפוסי אינטגרציה ישירה באמצעות HTTP לצורך שליטה והתאמה מרבית.

## סקירה כללית

בהתבסס על דפוסי Foundry Local הרשמיים של Microsoft, דוגמה זו מספקת:
- אינטגרציה ישירה עם FoundryLocalManager באמצעות REST API
- יישום מותאם אישית של לקוח HTTP
- ניהול מודלים ומעקב בריאות
- טיפול בתגובות סטרימינג ולא סטרימינג
- טיפול בטעויות והגיון ניסיונות חוזרים ברמה מוכנה לייצור

## דרישות מקדימות

1. **התקנת Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **תלויות Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## ארכיטקטורה

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## תכונות עיקריות

### 1. **אינטגרציה ישירה באמצעות HTTP**
- קריאות REST API טהורות ללא תלות ב-SDK
- אימות מותאם אישית וכותרות
- שליטה מלאה על טיפול בבקשות/תגובות

### 2. **ניהול מודלים**
- טעינה ופריקה דינמית של מודלים
- מעקב בריאות ובדיקות סטטוס
- איסוף מדדי ביצועים

### 3. **דפוסים מוכנים לייצור**
- מנגנוני ניסיונות חוזרים עם backoff אקספוננציאלי
- Circuit breaker לסבילות לתקלות
- לוגים ומעקב מקיפים

### 4. **טיפול גמיש בתגובות**
- תגובות סטרימינג ליישומים בזמן אמת
- עיבוד בקבוצות לתרחישים בעלי תפוקה גבוהה
- ניתוח ואימות תגובות מותאמות אישית

## דוגמאות שימוש

### אינטגרציה בסיסית עם API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### אינטגרציה סטרימינג
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### מעקב בריאות
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## מבנה קבצים

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## אינטגרציה עם Microsoft Foundry Local

דוגמה זו עוקבת אחר דפוסים רשמיים של Microsoft:

1. **אינטגרציה עם SDK**: שימוש ב-`FoundryLocalManager` לניהול שירותים
2. **נקודות קצה REST**: קריאות ישירות ל-`/v1/chat/completions` ונקודות קצה אחרות
3. **אימות**: טיפול נכון במפתחות API לשירותים מקומיים
4. **ניהול מודלים**: רישום קטלוג, הורדה ודפוסי טעינה
5. **טיפול בטעויות**: קודי שגיאה ותגובות מומלצים על ידי Microsoft

## התחלת עבודה

1. **התקנת תלויות**
   ```bash
   pip install -r requirements.txt
   ```

2. **הרצת דוגמה בסיסית**
   ```bash
   python examples/basic_usage.py
   ```

3. **ניסיון עם סטרימינג**
   ```bash
   python examples/streaming.py
   ```

4. **הגדרת ייצור**
   ```bash
   python examples/production.py
   ```

## תצורה

משתני סביבה להתאמה אישית:
- `FOUNDRY_MODEL`: מודל ברירת מחדל לשימוש (ברירת מחדל: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: זמן קצוב לבקשה בשניות (ברירת מחדל: 30)
- `FOUNDRY_RETRIES`: מספר ניסיונות חוזרים (ברירת מחדל: 3)
- `FOUNDRY_LOG_LEVEL`: רמת לוגים (ברירת מחדל: "INFO")

## שיטות עבודה מומלצות

1. **ניהול חיבורים**: שימוש חוזר בחיבורי HTTP לשיפור ביצועים
2. **טיפול בטעויות**: יישום הגיון ניסיונות חוזרים עם backoff אקספוננציאלי
3. **מעקב משאבים**: מעקב אחר שימוש בזיכרון וביצועי מודלים
4. **אבטחה**: שימוש באימות נכון גם לשירותים מקומיים
5. **בדיקות**: הכללת בדיקות יחידה ובדיקות אינטגרציה

## פתרון בעיות

### בעיות נפוצות

**השירות לא פועל**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**בעיות טעינת מודלים**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**שגיאות חיבור**
- ודא ש-Foundry Local פועל על הפורט הנכון
- בדוק הגדרות חומת אש
- ודא כותרות אימות נכונות

## אופטימיזציית ביצועים

1. **Pooling חיבורים**: שימוש באובייקטי session לבקשות מרובות
2. **פעולות אסינכרוניות**: ניצול asyncio לבקשות מקבילות
3. **Caching**: שמירת תגובות מודלים במידת הצורך
4. **מעקב**: מעקב אחר זמני תגובה והתאמת זמן קצוב

## תוצאות למידה

לאחר השלמת דוגמה זו, תבינו:
- אינטגרציה ישירה עם Foundry Local באמצעות REST API
- דפוסי יישום מותאמים אישית של לקוח HTTP
- טיפול בטעויות ומעקב ברמה מוכנה לייצור
- ארכיטקטורת שירות Microsoft Foundry Local
- טכניקות אופטימיזציית ביצועים לשירותי AI מקומיים

## צעדים הבאים

- חקור דוגמה 08: אפליקציית צ'אט ל-Windows 11
- נסה דוגמה 09: תזמור רב-סוכנים
- למד דוגמה 10: Foundry Local כאינטגרציה עם כלים

---

