<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T22:26:07+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "he"
}
-->
# מדריך התחלה מהירה לסדנה

## דרישות מקדימות

### 1. התקנת Foundry Local

עקוב אחר מדריך ההתקנה הרשמי:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. התקנת תלותים ב-Python

מתוך ספריית הסדנה:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## הפעלת דוגמאות מהסדנה

### מפגש 01: צ'אט בסיסי

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**משתני סביבה:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### מפגש 02: צינור RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**משתני סביבה:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### מפגש 02: הערכת RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**הערה**: דורש התקנת תלותים נוספים דרך `requirements.txt`

### מפגש 03: ביצועי מערכת

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**משתני סביבה:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**פלט**: JSON עם נתוני זמן תגובה, תפוקה ומדדי טוקן ראשון

### מפגש 04: השוואת מודלים

```bash
cd Workshop/samples
python -m session04.model_compare
```

**משתני סביבה:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### מפגש 05: תזמור רב-סוכנים

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**משתני סביבה:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### מפגש 06: ניתוב מודלים

```bash
cd Workshop/samples
python -m session06.models_router
```

**בודק לוגיקת ניתוב** עם מספר כוונות (קוד, סיכום, סיווג)

### מפגש 06: צינור עבודה

```bash
python -m session06.models_pipeline
```

**צינור עבודה מורכב רב-שלבי** עם תכנון, ביצוע ושיפור

## סקריפטים

### ייצוא דוח ביצועים

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**פלט**: טבלת Markdown + מדדי JSON

### בדיקת CLI ב-Markdown

```bash
python lint_markdown_cli.py --verbose
```

**מטרה**: זיהוי תבניות CLI מיושנות בתיעוד

## בדיקות

### בדיקות בסיסיות

```bash
cd Workshop
python -m tests.smoke
```

**בדיקות**: בדיקת פונקציונליות בסיסית של דוגמאות עיקריות

## פתרון בעיות

### השירות לא פועל

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### שגיאות ייבוא מודולים

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### שגיאות חיבור

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### מודל לא נמצא

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## הפניה למשתני סביבה

### הגדרות ליבה
| משתנה | ברירת מחדל | תיאור |
|-------|------------|--------|
| `FOUNDRY_LOCAL_ALIAS` | משתנה | כינוי מודל לשימוש |
| `FOUNDRY_LOCAL_ENDPOINT` | אוטומטי | עקיפת נקודת שירות |
| `SHOW_USAGE` | `0` | הצגת סטטיסטיקות שימוש בטוקנים |
| `RETRY_ON_FAIL` | `1` | הפעלת לוגיקת ניסיון חוזר |
| `RETRY_BACKOFF` | `1.0` | עיכוב ראשוני לניסיון חוזר (שניות) |

### ספציפי למפגש
| משתנה | ברירת מחדל | תיאור |
|-------|------------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | מודל הטמעה |
| `RAG_QUESTION` | ראה דוגמה | שאלה לבדיקה ב-RAG |
| `BENCH_MODELS` | משתנה | מודלים מופרדים בפסיקים |
| `BENCH_ROUNDS` | `3` | איטרציות ביצועים |
| `BENCH_PROMPT` | ראה דוגמה | הנחיה לביצועים |
| `BENCH_STREAM` | `0` | מדידת זמן תגובה לטוקן ראשון |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | מודל סוכן ראשי |
| `AGENT_MODEL_EDITOR` | ראשי | מודל סוכן עורך |
| `SLM_ALIAS` | `phi-4-mini` | מודל שפה קטן |
| `LLM_ALIAS` | `qwen2.5-7b` | מודל שפה גדול |
| `COMPARE_PROMPT` | ראה דוגמה | הנחיה להשוואה |

## מודלים מומלצים

### פיתוח ובדיקות
- **phi-4-mini** - איזון בין איכות למהירות
- **qwen2.5-0.5b** - מהיר מאוד לסיווג
- **gemma-2-2b** - איכות טובה, מהירות בינונית

### תרחישי ייצור
- **phi-4-mini** - שימוש כללי
- **deepseek-coder-1.3b** - יצירת קוד
- **qwen2.5-7b** - תגובות באיכות גבוהה

## תיעוד SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## קבלת עזרה

1. בדוק סטטוס שירות: `foundry service status`  
2. צפה ביומנים: בדוק יומני שירות Foundry Local  
3. עיין בתיעוד SDK: https://github.com/microsoft/Foundry-Local  
4. סקור קוד דוגמאות: כל הדוגמאות כוללות תיעוד מפורט  

## צעדים הבאים

1. השלם את כל מפגשי הסדנה לפי הסדר  
2. נסה מודלים שונים  
3. שנה דוגמאות לצרכים שלך  
4. עיין ב-`SDK_MIGRATION_NOTES.md` לדפוסים מתקדמים  

---

**עודכן לאחרונה**: 2025-01-08  
**גרסת סדנה**: אחרונה  
**SDK**: Foundry Local Python SDK  

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.