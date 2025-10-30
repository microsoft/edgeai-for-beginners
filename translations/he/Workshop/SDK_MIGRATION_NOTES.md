<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:30:44+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "he"
}
-->
# הערות מעבר ל-SDK המקומי של Foundry

## סקירה כללית

כל קבצי ה-Python בתיקיית Workshop עודכנו בהתאם לדפוסים העדכניים ביותר מ-[Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## סיכום שינויים

### תשתית ליבה (`workshop_utils.py`)

#### תכונות משופרות:
- **תמיכה בהחלפת נקודת קצה**: נוספה תמיכה במשתנה הסביבה `FOUNDRY_LOCAL_ENDPOINT`
- **שיפור טיפול בשגיאות**: טיפול טוב יותר בשגיאות עם הודעות שגיאה מפורטות
- **שיפור במטמון**: מפתחות המטמון כוללים כעת את נקודת הקצה עבור תרחישים מרובי נקודות קצה
- **Backoff אקספוננציאלי**: לוגיקת הניסיונות משתמשת כעת ב-backoff אקספוננציאלי לשיפור האמינות
- **הערות סוג**: נוספו רמזי סוג מקיפים לתמיכה טובה יותר ב-IDE

#### יכולות חדשות:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### יישומים לדוגמה

#### מפגש 01: Chat Bootstrap (`chat_bootstrap.py`)
- עודכן מודל ברירת המחדל מ-`phi-3.5-mini` ל-`phi-4-mini`
- נוספה תמיכה בהחלפת נקודת קצה
- שופרה התיעוד עם הפניות ל-SDK

#### מפגש 02: RAG Pipeline (`rag_pipeline.py`)
- עודכן לשימוש ב-`phi-4-mini` כברירת מחדל
- נוספה תמיכה בהחלפת נקודת קצה
- שופרה התיעוד עם פרטים על משתני סביבה

#### מפגש 02: RAG Evaluation (`rag_eval_ragas.py`)
- עודכנו ברירות מחדל של מודלים
- נוספה תצורת נקודת קצה
- שופרה טיפול בשגיאות

#### מפגש 03: Benchmarking (`benchmark_oss_models.py`)
- עודכן רשימת מודלים ברירת מחדל לכלול את `phi-4-mini`
- נוספה תיעוד מקיף על משתני סביבה
- שופרה תיעוד פונקציות
- נוספה תמיכה בהחלפת נקודת קצה לאורך כל הקובץ

#### מפגש 04: Model Comparison (`model_compare.py`)
- עודכן מודל LLM ברירת מחדל מ-`gpt-oss-20b` ל-`qwen2.5-7b`
- נוספה תצורת נקודת קצה
- שופרה תיעוד

#### מפגש 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- נוספו רמזי סוג (שינוי מ-`str | None` ל-`Optional[str]`)
- שופרה תיעוד מחלקת Agent
- נוספה תמיכה בהחלפת נקודת קצה
- שופרה תבנית האתחול

#### מפגש 06: Model Router (`models_router.py`)
- נוספה תצורת נקודת קצה
- שופרה תיעוד זיהוי כוונה
- שופרה תיעוד לוגיקת הניתוב

#### מפגש 06: Pipeline (`models_pipeline.py`)
- נוספה תיעוד פונקציות מקיף
- שופרה תיעוד שלב אחר שלב
- שופרה טיפול בשגיאות

### סקריפטים

#### Benchmark Export (`export_benchmark_markdown.py`)
- נוספה תמיכה בהחלפת נקודת קצה
- עודכנו מודלים ברירת מחדל
- שופרה תיעוד פונקציות
- שופרה טיפול בשגיאות

#### CLI Linter (`lint_markdown_cli.py`)
- נוספו קישורים להפניות ל-SDK
- שופרה תיעוד שימוש

### בדיקות

#### בדיקות Smoke (`smoke.py`)
- נוספה תמיכה בהחלפת נקודת קצה
- שופרה תיעוד
- שופרה תיעוד מקרי בדיקה
- שופרה דיווח שגיאות

## משתני סביבה

כל הדוגמאות תומכות כעת במשתני הסביבה הבאים:

### תצורת ליבה
- `FOUNDRY_LOCAL_ALIAS` - כינוי מודל לשימוש (ברירת מחדל משתנה לפי דוגמה)
- `FOUNDRY_LOCAL_ENDPOINT` - החלפת נקודת שירות (אופציונלי)
- `SHOW_USAGE` - הצגת סטטיסטיקות שימוש בטוקנים (ברירת מחדל: "0")
- `RETRY_ON_FAIL` - הפעלת לוגיקת ניסיונות (ברירת מחדל: "1")
- `RETRY_BACKOFF` - עיכוב ראשוני לניסיון מחדש בשניות (ברירת מחדל: "1.0")

### ספציפי לדוגמה
- `EMBED_MODEL` - מודל הטמעה לדוגמאות RAG
- `BENCH_MODELS` - מודלים מופרדים בפסיקים לבנצ'מרק
- `BENCH_ROUNDS` - מספר סבבי בנצ'מרק
- `BENCH_PROMPT` - פרומפט בדיקה לבנצ'מרק
- `BENCH_STREAM` - מדידת זמן תגובה לטוקן הראשון
- `RAG_QUESTION` - שאלת בדיקה לדוגמאות RAG
- `AGENT_MODEL_PRIMARY` - מודל סוכן ראשי
- `AGENT_MODEL_EDITOR` - מודל סוכן עורך
- `SLM_ALIAS` - כינוי מודל שפה קטן
- `LLM_ALIAS` - כינוי מודל שפה גדול

## שיטות עבודה מומלצות ל-SDK

### 1. אתחול נכון של לקוח
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. שליפת מידע על מודל
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. טיפול בשגיאות
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. לוגיקת ניסיונות עם Backoff אקספוננציאלי
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. תמיכה בזרימה
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## מדריך מעבר לדוגמאות מותאמות אישית

אם אתם יוצרים דוגמאות חדשות או מעדכנים קיימות:

1. **השתמשו בעזרי `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **תמכו בהחלפת נקודת קצה**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **הוסיפו תיעוד מקיף**:
   - משתני סביבה בתיעוד
   - קישור להפניות ל-SDK
   - דוגמאות שימוש

4. **השתמשו ברמזי סוג**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **יישמו טיפול נכון בשגיאות**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## בדיקות

ניתן לבדוק את כל הדוגמאות עם:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## הפניות לתיעוד SDK

- **מאגר ראשי**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **תיעוד API**: בדקו את מאגר ה-SDK לתיעוד API העדכני ביותר

## שינויים משמעותיים

### לא צפויים
כל השינויים תואמים לאחור. העדכונים בעיקר:
- מוסיפים תכונות אופציונליות חדשות (החלפת נקודת קצה)
- משפרים טיפול בשגיאות
- משפרים תיעוד
- מעדכנים שמות מודלים ברירת מחדל להמלצות הנוכחיות

### שיפורים אופציונליים
ייתכן שתרצו לעדכן את הקוד שלכם לשימוש ב:
- `FOUNDRY_LOCAL_ENDPOINT` לשליטה מפורשת בנקודת הקצה
- `SHOW_USAGE=1` לצפייה בשימוש בטוקנים
- שמות מודלים מעודכנים (`phi-4-mini` במקום `phi-3.5-mini`)

## בעיות נפוצות ופתרונות

### בעיה: "Client initialization failed"
**פתרון**: ודאו ששירות Foundry Local פועל:
```bash
foundry service start
foundry model run phi-4-mini
```

### בעיה: "Model not found"
**פתרון**: בדקו את המודלים הזמינים:
```bash
foundry model list
```

### בעיה: שגיאות חיבור לנקודת קצה
**פתרון**: בדקו את נקודת הקצה:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## צעדים הבאים

1. **עדכון דוגמאות Module08**: יישום דפוסים דומים ב-Module08/samples
2. **הוספת בדיקות אינטגרציה**: יצירת מערך בדיקות מקיף
3. **בנצ'מרק ביצועים**: השוואת ביצועים לפני/אחרי
4. **עדכוני תיעוד**: עדכון README הראשי עם דפוסים חדשים

## הנחיות לתרומה

בעת הוספת דוגמאות חדשות:
1. השתמשו ב-`workshop_utils.py` לצורך עקביות
2. עקבו אחר הדפוס בדוגמאות הקיימות
3. הוסיפו תיעוד מקיף
4. כללו קישורים להפניות ל-SDK
5. תמכו בהחלפת נקודת קצה
6. הוסיפו רמזי סוג מתאימים
7. כללו דוגמאות שימוש בתיעוד

## תאימות גרסאות

עדכונים אלו תואמים ל:
- `foundry-local-sdk` (הגרסה העדכנית ביותר)
- `openai>=1.30.0`
- Python 3.8+

---

**תאריך עדכון אחרון**: 2025-01-08  
**אחראי**: צוות EdgeAI Workshop  
**גרסת SDK**: Foundry Local SDK (גרסה עדכנית 0.7.117+67073234e7)

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.