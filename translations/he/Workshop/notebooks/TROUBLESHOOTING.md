# מחברות סדנה - מדריך לפתרון בעיות

## תוכן עניינים

- [בעיות נפוצות ופתרונות](../../../../Workshop/notebooks)
- [בעיות ספציפיות למפגש 04](../../../../Workshop/notebooks)
- [בעיות ספציפיות למפגש 05](../../../../Workshop/notebooks)
- [בעיות ספציפיות למפגש 06](../../../../Workshop/notebooks)
- [בעיות ספציפיות לחומרה](../../../../Workshop/notebooks)
- [פקודות אבחון](../../../../Workshop/notebooks)
- [קבלת עזרה](../../../../Workshop/notebooks)

---

## בעיות נפוצות ופתרונות

### 🔴 CUDA Out of Memory

**הודעת שגיאה:**
```
CUDA failure 2: out of memory
```

**סיבה עיקרית:** ל-GPU אין מספיק זיכרון VRAM לטעינת המודל.

**פתרונות:**

#### אפשרות 1: שימוש בגרסאות CPU (מומלץ)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### אפשרות 2: שימוש במודלים קטנים יותר על GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### אפשרות 3: ניקוי זיכרון GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### אפשרות 4: הגדלת זיכרון GPU (אם אפשרי)
- סגור לשוניות בדפדפן, עורכי וידאו או אפליקציות אחרות המשתמשות ב-GPU
- הפחת אפקטים חזותיים ב-Windows
- השתמש ב-GPU ייעודי אם יש לך גם GPU משולב וגם ייעודי

---

### 🔴 APIConnectionError: Connection Error

**הודעת שגיאה:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**סיבה עיקרית:** שירות Foundry Local אינו פועל או אינו נגיש.

**פתרונות:**

#### שלב 1: בדוק את מצב השירות
```bash
foundry service status
```

#### שלב 2: הפעל את השירות אם הוא נעצר
```bash
foundry service start
```

#### שלב 3: אמת את נקודת הקצה
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### שלב 4: טען מודלים נדרשים
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### שלב 5: הפעל מחדש את Kernel של המחברת
לאחר הפעלת השירות וטעינת המודלים, הפעל מחדש את Kernel של המחברת והרץ מחדש את כל התאים.

---

### 🔴 Model Not Found in Catalog

**הודעת שגיאה:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**סיבה עיקרית:** המודל לא הורד או נטען ב-Foundry Local.

**פתרונות:**

#### אפשרות 1: הורד וטעון מודלים
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### אפשרות 2: השתמש במצב בחירה אוטומטי
עדכן את CATALOG לשימוש בשמות מודלים בסיסיים (ללא הסיומת `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

SDK של Foundry Local יבחר אוטומטית את הגרסה הטובה ביותר (CPU, GPU או NPU) עבור החומרה שלך.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**הודעת שגיאה:**
```
HttpResponseError: 500 - Failed loading model
```

**סיבה עיקרית:** קובץ המודל פגום או אינו תואם לחומרה.

**פתרונות:**

#### הורד מחדש את המודל
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### השתמש בגרסה אחרת
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**הודעת שגיאה:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**סיבה עיקרית:** חבילת foundry-local-sdk לא מותקנת.

**פתרונות:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � בקשה ראשונה איטית

**תסמין:** השלמה ראשונה לוקחת יותר מ-30 שניות, בקשות עוקבות מהירות.

**סיבה עיקרית:** זהו התנהגות נורמלית - השירות טוען את המודל לזיכרון בבקשה הראשונה.

**פתרונות:**

#### טעינת מודלים מראש
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### שמור על השירות פועל
```bash
# Start service manually and leave it running
foundry service start
```

---

## בעיות ספציפיות למפגש 04

### תצורת פורט שגויה

**בעיה:** המחברת מתחברת לפורט שגוי (55769 במקום 59959 או 57127)

**פתרון:**

1. בדוק באיזה פורט Foundry Local משתמש:
```bash
foundry service status
# Note the port number displayed
```

2. עדכן תא 10 במחברת:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. הפעל מחדש את Kernel והרץ מחדש את תאים 6, 8, 10, 12, 16, 20, 22

---

### בחירת מודל שגויה

**בעיה:** המחברת מציגה gpt-oss-20b או qwen2.5-7b במקום qwen2.5-3b

**פתרון:**

1. הפעל מחדש את Kernel של המחברת (מנקה מצב משתנים ישן)
2. הרץ מחדש תא 10 (הגדר שמות מודלים)
3. הרץ מחדש תא 12 (הצג תצורה)
4. **אמת:** תא 12 צריך להציג `LLM Model: qwen2.5-3b`

---

### תא אבחון נכשל

**בעיה:** תא 16 מציג "❌ Foundry Local service not found!"

**פתרון:**

1. אמת שהשירות פועל:
```bash
foundry service status
```

2. בדוק את נקודת הקצה ידנית:
```bash
curl http://localhost:59959/v1/models
```

3. אם curl עובד אבל המחברת לא:
   - הפעל מחדש את Kernel של המחברת
   - הרץ מחדש את התאים בסדר: 6, 8, 10, 12, 14, 16

4. אם curl נכשל:
   - הפעל את השירות: `foundry service start`
   - טען מודלים: `foundry model run phi-4-mini` ו-`foundry model run qwen2.5-3b`

---

### בדיקת Pre-flight נכשלת

**בעיה:** תא 20 מציג שגיאות חיבור למרות שהאבחון עבר

**פתרון:**

1. בדוק שהמודלים נטענו:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. אם מודלים חסרים:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. הרץ מחדש תא 20 לאחר טעינת המודלים

---

### השוואה נכשלת עם ערכי None

**בעיה:** תא 22 מסתיים אך מציג זמן תגובה כ-None

**פתרון:**

1. בדוק שהבדיקה המקדימה עברה קודם (תא 20)
2. הרץ מחדש תא 22 - ייתכן שהמודלים צריכים להתחמם בבקשה הראשונה
3. אמת ששני המודלים נטענו: `foundry model ls`

---

## בעיות ספציפיות למפגש 05

### הסוכן משתמש במודל שגוי

**בעיה:** הסוכן לא משתמש במודל הצפוי

**פתרון:**

אמת את התצורה:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

הפעל מחדש את Kernel אם המודלים שגויים.

---

### זיכרון הקשר מלא

**בעיה:** תגובות הסוכן מתדרדרות עם הזמן

**פתרון:** כבר מטופל אוטומטית - הסוכנים שומרים רק את 6 ההודעות האחרונות בזיכרון.

---

## בעיות ספציפיות למפגש 06

### בלבול בין מודלים של CPU ל-GPU

**בעיה:** שגיאות CUDA מופיעות בעת שימוש בתצורה ברירת מחדל

**פתרון:** תצורת ברירת המחדל כעת משתמשת במודלים של CPU. אם אתה רואה שגיאות CUDA:

1. אמת שאתה משתמש בקטלוג CPU ברירת מחדל:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. הפעל מחדש את Kernel והרץ מחדש את כל התאים

---

### זיהוי כוונה לא עובד

**בעיה:** הנחיות מנותבות למודלים שגויים

**פתרון:**

בדוק זיהוי כוונה:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

עדכן את RULES אם יש צורך בהתאמת תבניות.

---

## בעיות ספציפיות לחומרה

### NVIDIA GPU

**בדוק מצב GPU:**
```bash
nvidia-smi
```

**בעיות נפוצות:**
- **דרייבר מיושן**: עדכן את דרייברי NVIDIA
- **אי התאמה של גרסת CUDA**: התקן מחדש את Foundry Local
- **זיכרון GPU מקוטע**: הפעל מחדש את המערכת

### Qualcomm NPU

**בדוק מצב NPU:**
```bash
foundry device info
```

**בעיות נפוצות:**
- **דרייברי NPU לא מותקנים**: התקן דרייברי Qualcomm NPU
- **גרסת NPU לא זמינה**: השתמש בגרסת CPU
- **גרסת Windows ישנה מדי**: עדכן ל-Windows 11 העדכנית ביותר

### מערכות מבוססות CPU בלבד

**מודלים מומלצים:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**טיפים לשיפור ביצועים:**
- השתמש במודלים הקטנים ביותר
- הפחת max_tokens
- הגבר סבלנות לבקשה הראשונה

---

## פקודות אבחון

### בדוק הכל
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### ב-Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## קבלת עזרה

### 1. בדוק לוגים
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. בעיות ב-GitHub
- חפש בעיות קיימות: https://github.com/microsoft/Foundry-Local/issues
- צור בעיה חדשה עם:
  - הודעת שגיאה (טקסט מלא)
  - פלט של `foundry service status`
  - פלט של `foundry --version`
  - מידע על GPU/NPU (nvidia-smi וכו')
  - שלבים לשחזור

### 3. תיעוד
- **מאגר ראשי**: https://github.com/microsoft/Foundry-Local
- **SDK ב-Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **התייחסות CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **פתרון בעיות**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## רשימת תיקונים מהירים

כשמשהו משתבש, נסה את השלבים הבאים לפי הסדר:

- [ ] בדוק שהשירות פועל: `foundry service status`
- [ ] הפעל מחדש את השירות: `foundry service stop && foundry service start`
- [ ] אמת שהמודל קיים: `foundry model ls | grep phi-4-mini`
- [ ] טען מודלים נדרשים: `foundry model run phi-4-mini`
- [ ] בדוק זיכרון GPU: `nvidia-smi` (אם NVIDIA)
- [ ] נסה גרסת CPU: השתמש ב-`phi-4-mini-cpu` במקום `phi-4-mini`
- [ ] הפעל מחדש את Kernel של המחברת
- [ ] נקה פלטי מחברת והרץ מחדש את כל התאים
- [ ] התקן מחדש את SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] הפעל מחדש את המערכת (מוצא אחרון)

---

## טיפים למניעה

### שיטות עבודה מומלצות

1. **תמיד בדוק את השירות תחילה:**
   ```bash
   foundry service status
   ```

2. **השתמש בגרסאות CPU כברירת מחדל:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **טען מודלים מראש לפני הפעלת מחברות:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **שמור על השירות פועל:**
   - אל תעצור/תתחיל את השירות שלא לצורך
   - תן לו לפעול ברקע בין מפגשים

5. **עקוב אחר משאבים:**
   - בדוק זיכרון GPU לפני הפעלה
   - סגור אפליקציות GPU מיותרות
   - השתמש ב-Task Manager / nvidia-smi

6. **עדכן באופן קבוע:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**עודכן לאחרונה:** 8 באוקטובר 2025

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.