<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:30:26+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "he"
}
-->
# דוגמאות לסדנה - סיכום עדכון Foundry Local SDK

## סקירה כללית

כל דוגמאות ה-Python בתיקיית `Workshop/samples` עודכנו בהתאם לשיטות העבודה המומלצות של Foundry Local SDK ולשמירה על עקביות בסדנה.

**תאריך**: 8 באוקטובר, 2025  
**היקף**: 9 קבצי Python ב-6 מפגשי סדנה  
**מיקוד עיקרי**: טיפול בשגיאות, תיעוד, תבניות SDK, חוויית משתמש

---

## קבצים מעודכנים

### מפגש 01: התחלה
- ✅ `chat_bootstrap.py` - דוגמאות בסיסיות לצ'אט וסטרימינג

### מפגש 02: פתרונות RAG
- ✅ `rag_pipeline.py` - יישום RAG עם embeddings
- ✅ `rag_eval_ragas.py` - הערכת RAG עם מדדי RAGAS

### מפגש 03: מודלים בקוד פתוח
- ✅ `benchmark_oss_models.py` - השוואת ביצועים בין מודלים שונים

### מפגש 04: מודלים מתקדמים
- ✅ `model_compare.py` - השוואה בין SLM ל-LLM

### מפגש 05: סוכנים מבוססי AI
- ✅ `agents_orchestrator.py` - תיאום בין סוכנים מרובים

### מפגש 06: מודלים ככלים
- ✅ `models_router.py` - ניתוב מודלים מבוסס כוונה
- ✅ `models_pipeline.py` - צינור ניתוב רב-שלבי

### תשתית תומכת
- ✅ `workshop_utils.py` - כבר עומד בשיטות העבודה המומלצות (לא נדרשו שינויים)

---

## שיפורים מרכזיים

### 1. שיפור טיפול בשגיאות

**לפני:**
```python
manager, client, model_id = get_client(alias)
```

**אחרי:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**יתרונות:**
- טיפול בשגיאות בצורה חלקה עם הודעות שגיאה ברורות
- רמזים לפתרון בעיות
- קודי יציאה מתאימים לסקריפטים

### 2. ניהול ייבוא משופר

**לפני:**
```python
from sentence_transformers import SentenceTransformer
```

**אחרי:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**יתרונות:**
- הנחיות ברורות כאשר חסרים תלות
- מניעת שגיאות ייבוא לא ברורות
- הוראות התקנה ידידותיות למשתמש

### 3. תיעוד מקיף

**נוסף לכל הדוגמאות:**
- תיעוד משתני סביבה ב-docstrings
- קישורים למקורות SDK
- דוגמאות שימוש
- תיעוד מפורט של פונקציות/פרמטרים
- רמזי סוגים לתמיכה טובה יותר ב-IDE

**דוגמה:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. משוב משתמש משופר

**נוסף לוגים אינפורמטיביים:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**אינדיקטורים להתקדמות:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**פלט מובנה:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. השוואת ביצועים חזקה

**שיפורים במפגש 03:**
- טיפול בשגיאות לכל מודל (ממשיך במקרה של כשל)
- דיווח מפורט על התקדמות
- ביצוע סבבי חימום כראוי
- תמיכה במדידת זמן תגובה של הטוקן הראשון
- הפרדה ברורה בין שלבים

### 6. רמזי סוגים עקביים

**נוסף בכל מקום:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**יתרונות:**
- השלמה אוטומטית טובה יותר ב-IDE
- זיהוי מוקדם של שגיאות
- קוד שמתעד את עצמו

### 7. ניתוב מודלים משופר

**שיפורים במפגש 06:**
- תיעוד מקיף של זיהוי כוונה
- הסבר על אלגוריתם בחירת מודלים
- לוגים מפורטים של ניתוב
- עיצוב פלט בדיקות
- התאוששות משגיאות בבדיקות קבוצתיות

### 8. תיאום סוכנים מרובים

**שיפורים במפגש 05:**
- דיווח על התקדמות שלב אחר שלב
- טיפול בשגיאות לכל סוכן
- מבנה צינור ברור
- תיעוד משופר לניהול זיכרון

---

## רשימת בדיקות

### דרישות מוקדמות
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### בדיקת כל דוגמה

#### מפגש 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### מפגש 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### מפגש 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### מפגש 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### מפגש 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### מפגש 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## התייחסות למשתני סביבה

### גלובלי (כל הדוגמאות)
| משתנה | תיאור | ברירת מחדל |
|-------|-------|------------|
| `FOUNDRY_LOCAL_ALIAS` | כינוי מודל לשימוש | משתנה לפי דוגמה |
| `FOUNDRY_LOCAL_ENDPOINT` | עקיפת נקודת שירות | מזוהה אוטומטית |
| `SHOW_USAGE` | הצגת שימוש בטוקנים | `0` |
| `RETRY_ON_FAIL` | הפעלת לוגיקת ניסיון חוזר | `1` |
| `RETRY_BACKOFF` | עיכוב ניסיון חוזר ראשוני | `1.0` |

### ספציפי לדוגמה
| משתנה | בשימוש על ידי | תיאור |
|-------|---------------|-------|
| `EMBED_MODEL` | מפגש 02 | שם מודל embedding |
| `RAG_QUESTION` | מפגש 02 | שאלה לבדיקה ב-RAG |
| `BENCH_MODELS` | מפגש 03 | מודלים להשוואת ביצועים, מופרדים בפסיקים |
| `BENCH_ROUNDS` | מפגש 03 | מספר סבבי השוואת ביצועים |
| `BENCH_PROMPT` | מפגש 03 | הנחיה לבדיקה בהשוואת ביצועים |
| `BENCH_STREAM` | מפגש 03 | מדידת זמן תגובה של הטוקן הראשון |
| `SLM_ALIAS` | מפגש 04 | מודל שפה קטן |
| `LLM_ALIAS` | מפגש 04 | מודל שפה גדול |
| `COMPARE_PROMPT` | מפגש 04 | הנחיה לבדיקה בהשוואה |
| `AGENT_MODEL_PRIMARY` | מפגש 05 | מודל סוכן ראשי |
| `AGENT_MODEL_EDITOR` | מפגש 05 | מודל סוכן עורך |
| `AGENT_QUESTION` | מפגש 05 | שאלה לבדיקה עם סוכנים |
| `PIPELINE_TASK` | מפגש 06 | משימה לצינור |

---

## שינויים משמעותיים

**אין** - כל השינויים תואמים לאחור.

סקריפטים קיימים ימשיכו לעבוד. תכונות חדשות הן:
- משתני סביבה אופציונליים
- הודעות שגיאה משופרות (לא פוגעות בפונקציונליות)
- לוגים נוספים (ניתן לדכא אותם)
- רמזי סוגים משופרים (ללא השפעה בזמן ריצה)

---

## שיטות עבודה מומלצות שיושמו

### 1. שימוש תמידי ב-workshop_utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. תבנית טיפול בשגיאות נכונה
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. לוגים אינפורמטיביים
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. רמזי סוגים
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. docstrings מקיפים
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. תמיכה במשתני סביבה
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. התמודדות עם תקלות בצורה חלקה
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## בעיות נפוצות ופתרונות

### בעיה: שגיאות ייבוא
**פתרון:** התקנת תלות חסרות
```bash
pip install sentence-transformers ragas datasets numpy
```

### בעיה: שגיאות חיבור
**פתרון:** לוודא ש-Foundry Local פועל
```bash
foundry service status
foundry model run phi-4-mini
```

### בעיה: מודל לא נמצא
**פתרון:** לבדוק אילו מודלים זמינים
```bash
foundry model ls
foundry model download <alias>
```

### בעיה: ביצועים איטיים
**פתרון:** להשתמש במודלים קטנים יותר או להתאים פרמטרים
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## צעדים הבאים

### 1. בדיקת כל הדוגמאות
לעבור על רשימת הבדיקות לעיל כדי לוודא שכל הדוגמאות פועלות כראוי.

### 2. עדכון תיעוד
- לעדכן קבצי Markdown של המפגשים עם דוגמאות חדשות
- להוסיף סעיף פתרון בעיות ל-README הראשי
- ליצור מדריך עזר מהיר

### 3. יצירת בדיקות אינטגרציה
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. הוספת השוואות ביצועים
מעקב אחר שיפורי ביצועים בעקבות שיפורי טיפול בשגיאות.

### 5. משוב משתמשים
איסוף משוב ממשתתפי הסדנה על:
- בהירות הודעות השגיאה
- שלמות התיעוד
- קלות השימוש

---

## משאבים

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **מדריך עזר מהיר**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **הערות מעבר**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **מאגר ראשי**: https://github.com/microsoft/Foundry-Local  

---

## תחזוקה

### הוספת דוגמאות חדשות
יש לעקוב אחר התבניות הבאות בעת יצירת דוגמאות חדשות:

1. להשתמש ב-`workshop_utils` לניהול לקוחות
2. להוסיף טיפול שגיאות מקיף
3. לכלול תמיכה במשתני סביבה
4. להוסיף רמזי סוגים ו-docstrings
5. לספק לוגים אינפורמטיביים
6. לכלול דוגמאות שימוש ב-docstring
7. לקשר לתיעוד SDK

### סקירת עדכונים
בעת סקירת עדכוני דוגמאות, יש לבדוק:
- [ ] טיפול בשגיאות בכל פעולות I/O
- [ ] רמזי סוגים בפונקציות ציבוריות
- [ ] docstrings מקיפים
- [ ] תיעוד משתני סביבה
- [ ] משוב אינפורמטיבי למשתמש
- [ ] קישורים לתיעוד SDK
- [ ] סגנון קוד עקבי

---

**סיכום**: כל דוגמאות ה-Python בסדנה כעת עומדות בשיטות העבודה המומלצות של Foundry Local SDK עם טיפול שגיאות משופר, תיעוד מקיף וחוויית משתמש משופרת. אין שינויים משמעותיים - כל הפונקציונליות הקיימת נשמרה ושופרה.

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.