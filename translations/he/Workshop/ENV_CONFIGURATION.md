<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:26:38+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "he"
}
-->
# מדריך הגדרת סביבה

## סקירה כללית

דוגמאות הסדנה משתמשות במשתני סביבה לצורך הגדרה, אשר מרוכזים בקובץ `.env` שנמצא בשורש המאגר. זה מאפשר התאמה אישית קלה ללא צורך בשינוי קוד.

## התחלה מהירה

### 1. בדיקת דרישות מקדימות

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. הגדרת סביבה

קובץ `.env` כבר מוגדר עם ערכים ברירת מחדל הגיוניים. רוב המשתמשים לא יצטרכו לשנות דבר.

**אופציונלי**: סקירה והתאמה של ההגדרות:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. יישום ההגדרות

**עבור סקריפטים ב-Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**עבור מחברות:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## הפניה למשתני סביבה

### הגדרות ליבה

| משתנה | ברירת מחדל | תיאור |
|-------|------------|--------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | מודל ברירת מחדל לדוגמאות |
| `FOUNDRY_LOCAL_ENDPOINT` | (ריק) | נקודת שירות חלופית |
| `PYTHONPATH` | נתיבי סדנה | נתיב חיפוש למודולים ב-Python |

**מתי להגדיר את FOUNDRY_LOCAL_ENDPOINT:**
- מופע מרוחק של Foundry Local
- הגדרת פורט מותאמת אישית
- הפרדה בין פיתוח לייצור

**דוגמה:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### משתנים ספציפיים למפגשים

#### מפגש 02: צינור RAG
| משתנה | ברירת מחדל | מטרה |
|-------|------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | מודל הטמעה |
| `RAG_QUESTION` | מוגדר מראש | שאלה לבדיקה |

#### מפגש 03: ביצועי מודלים
| משתנה | ברירת מחדל | מטרה |
|-------|------------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | מודלים לביצועי השוואה |
| `BENCH_ROUNDS` | `3` | מספר סבבים לכל מודל |
| `BENCH_PROMPT` | מוגדר מראש | הנחיה לבדיקה |
| `BENCH_STREAM` | `0` | מדידת זמן תגובה לטוקן הראשון |

#### מפגש 04: השוואת מודלים
| משתנה | ברירת מחדל | מטרה |
|-------|------------|-------|
| `SLM_ALIAS` | `phi-4-mini` | מודל שפה קטן |
| `LLM_ALIAS` | `qwen2.5-7b` | מודל שפה גדול |
| `COMPARE_PROMPT` | מוגדר מראש | הנחיה להשוואה |
| `COMPARE_RETRIES` | `2` | ניסיונות חוזרים |

#### מפגש 05: תזמור רב-סוכנים
| משתנה | ברירת מחדל | מטרה |
|-------|------------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | מודל סוכן מחקר |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | מודל סוכן עורך |
| `AGENT_QUESTION` | מוגדר מראש | שאלה לבדיקה |

### הגדרות אמינות

| משתנה | ברירת מחדל | מטרה |
|-------|------------|-------|
| `SHOW_USAGE` | `1` | הדפסת שימוש בטוקנים |
| `RETRY_ON_FAIL` | `1` | הפעלת לוגיקת ניסיון חוזר |
| `RETRY_BACKOFF` | `1.0` | עיכוב ניסיון חוזר (שניות) |

## הגדרות נפוצות

### הגדרת פיתוח (חזרות מהירות)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### הגדרת ייצור (מיקוד באיכות)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### הגדרת ביצועי מודלים
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### התמחות רב-סוכנים
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### פיתוח מרחוק
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## מודלים מומלצים

### לפי שימוש

**שימוש כללי:**
- `phi-4-mini` - איזון בין איכות למהירות

**תגובות מהירות:**
- `qwen2.5-0.5b` - מהיר מאוד, טוב לסיווג
- `phi-4-mini` - מהיר עם איכות טובה

**איכות גבוהה:**
- `qwen2.5-7b` - איכות הטובה ביותר, שימוש גבוה במשאבים
- `phi-4-mini` - איכות טובה, משאבים נמוכים יותר

**יצירת קוד:**
- `deepseek-coder-1.3b` - מותאם במיוחד לקוד
- `phi-4-mini` - מתאים לשימוש כללי בקוד

### לפי זמינות משאבים

**משאבים נמוכים (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**משאבים בינוניים (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**משאבים גבוהים (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## הגדרות מתקדמות

### נקודות שירות מותאמות אישית

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### טמפרטורה ודגימה (הגדרה בקוד)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### הגדרת Azure OpenAI היברידית

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## פתרון בעיות

### משתני סביבה לא נטענים

**תסמינים:**
- סקריפטים משתמשים במודלים שגויים
- שגיאות חיבור
- משתנים לא מזוהים

**פתרונות:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### בעיות חיבור לשירות

**תסמינים:**
- שגיאות "Connection refused"
- "שירות לא זמין"
- שגיאות זמן קצוב

**פתרונות:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### מודל לא נמצא

**תסמינים:**
- שגיאות "מודל לא נמצא"
- "Alias לא מזוהה"

**פתרונות:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### שגיאות ייבוא

**תסמינים:**
- שגיאות "מודול לא נמצא"

**פתרונות:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## בדיקת הגדרות

### אימות טעינת סביבה

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### בדיקת חיבור Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## שיטות עבודה מומלצות לאבטחה

### 1. לעולם לא לשמור סודות

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. שימוש בקבצי .env נפרדים

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. סיבוב מפתחות API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. שימוש בהגדרות ייחודיות לסביבה

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## תיעוד SDK

- **מאגר ראשי**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **תיעוד API**: בדוק את מאגר ה-SDK לעדכונים האחרונים

## משאבים נוספים

- `QUICK_START.md` - מדריך התחלה מהירה
- `SDK_MIGRATION_NOTES.md` - פרטי עדכון SDK
- `Workshop/samples/*/README.md` - מדריכים לדוגמאות ספציפיות

---

**עודכן לאחרונה**: 2025-01-08  
**גרסה**: 2.0  
**SDK**: Foundry Local Python SDK (עדכני)

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.