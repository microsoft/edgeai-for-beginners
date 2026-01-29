# מדריך מהיר למחברות סדנה

## תוכן עניינים

- [דרישות מקדימות](../../../../Workshop/notebooks)
- [הגדרה ראשונית](../../../../Workshop/notebooks)
- [מפגש 04: השוואת מודלים](../../../../Workshop/notebooks)
- [מפגש 05: מתזמר רב-סוכנים](../../../../Workshop/notebooks)
- [מפגש 06: ניתוב מודלים מבוסס כוונה](../../../../Workshop/notebooks)
- [משתני סביבה](../../../../Workshop/notebooks)
- [פקודות נפוצות](../../../../Workshop/notebooks)

---

## דרישות מקדימות

### 1. התקנת Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**אימות התקנה:**
```bash
foundry --version
```

### 2. התקנת תלותים ב-Python

```bash
cd Workshop
pip install -r requirements.txt
```

או התקנה פרטנית:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## הגדרה ראשונית

### הפעלת שירות Foundry Local

**נדרש לפני הפעלת כל מחברת:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

פלט צפוי:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### הורדה וטעינת מודלים

המחברות משתמשות במודלים הבאים כברירת מחדל:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### אימות הגדרה

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## מפגש 04: השוואת מודלים

### מטרה
השוואת ביצועים בין מודלים קטנים (SLM) למודלים גדולים (LLM).

### הגדרה מהירה

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### הפעלת המחברת

1. **פתחו** `session04_model_compare.ipynb` ב-VS Code או Jupyter
2. **אתחלו את הליבה** (Kernel → Restart Kernel)
3. **הריצו את כל התאים** לפי הסדר

### הגדרות עיקריות

**מודלים ברירת מחדל:**
- **SLM:** `phi-4-mini` (~4GB RAM, מהיר יותר)
- **LLM:** `qwen2.5-3b` (~3GB RAM, מותאם לזיכרון)

**משתני סביבה (אופציונלי):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### פלט צפוי

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### התאמה אישית

**שימוש במודלים שונים:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**הנחיה מותאמת אישית:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### רשימת בדיקות אימות

- [ ] תא 12 מציג מודלים נכונים (phi-4-mini, qwen2.5-3b)
- [ ] תא 12 מציג נקודת קצה נכונה (פורט 59959)
- [ ] תא 16 בדיקת אבחון עברה (✅ השירות פועל)
- [ ] תא 20 בדיקת טרום טיסה עברה (שני המודלים תקינים)
- [ ] תא 22 השוואה הושלמה עם ערכי זמן תגובה
- [ ] תא 24 אימות מציג 🎉 כל הבדיקות עברו!

### הערכת זמן
- **הרצה ראשונה:** 5-10 דקות (כולל הורדת מודלים)
- **הרצות נוספות:** 1-2 דקות

---

## מפגש 05: מתזמר רב-סוכנים

### מטרה
הדגמת שיתוף פעולה בין סוכנים באמצעות Foundry Local SDK - הסוכנים עובדים יחד ליצירת תוצרים משופרים.

### הגדרה מהירה

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### הפעלת המחברת

1. **פתחו** `session05_agents_orchestrator.ipynb`
2. **אתחלו את הליבה**
3. **הריצו את כל התאים** לפי הסדר

### הגדרות עיקריות

**הגדרה ברירת מחדל (אותו מודל לשני הסוכנים):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**הגדרה מתקדמת (מודלים שונים):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### ארכיטקטורה

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### פלט צפוי

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### הרחבות

**הוספת סוכנים נוספים:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**בדיקות בקבוצות:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### הערכת זמן
- **הרצה ראשונה:** 3-5 דקות
- **הרצות נוספות:** 1-2 דקות לשאלה

---

## מפגש 06: ניתוב מודלים מבוסס כוונה

### מטרה
ניתוב חכם של הנחיות למודלים מתמחים בהתאם לכוונה שזוהתה.

### הגדרה מהירה

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**הערה:** מפגש 06 משתמש במודלים מבוססי CPU כברירת מחדל לצורך תאימות מרבית.

### הפעלת המחברת

1. **פתחו** `session06_models_router.ipynb`
2. **אתחלו את הליבה**
3. **הריצו את כל התאים** לפי הסדר

### הגדרות עיקריות

**קטלוג ברירת מחדל (מודלים CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**חלופה (מודלים GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### זיהוי כוונה

הנתב משתמש בתבניות regex לזיהוי כוונה:

| כוונה | דוגמאות לתבניות | מנותב ל- |
|-------|-----------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | כל השאר | phi-4-mini-cpu |

### פלט צפוי

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### התאמה אישית

**הוספת כוונה מותאמת אישית:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**הפעלת מעקב אחר טוקנים:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### מעבר למודלים GPU

אם יש לכם 8GB+ VRAM:

1. בתא **#6**, הגיבו את קטלוג ה-CPU
2. בטלו את ההערה מקטלוג ה-GPU
3. טענו מודלים GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. אתחלו את הליבה והריצו את המחברת מחדש

### הערכת זמן
- **הרצה ראשונה:** 5-10 דקות (טעינת מודלים)
- **הרצות נוספות:** 30-60 שניות לבדיקה

---

## משתני סביבה

### הגדרה גלובלית

יש להגדיר לפני הפעלת Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### הגדרה בתוך המחברת

יש להגדיר בתחילת כל מחברת:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## פקודות נפוצות

### ניהול שירות

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### ניהול מודלים

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### בדיקת נקודות קצה

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### פקודות אבחון

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## שיטות עבודה מומלצות

### לפני הפעלת כל מחברת

1. **בדקו שהשירות פועל:**
   ```bash
   foundry service status
   ```

2. **וודאו שהמודלים נטענו:**
   ```bash
   foundry model ls
   ```

3. **אתחלו את ליבת המחברת** אם מריצים מחדש

4. **נקו את כל הפלטים** להרצה נקייה

### ניהול משאבים

1. **השתמשו במודלים CPU כברירת מחדל** לצורך תאימות
2. **עברו למודלים GPU** רק אם יש לכם 8GB+ VRAM
3. **סגרו יישומי GPU אחרים** לפני ההרצה
4. **השאירו את השירות פועל** בין מפגשי מחברות
5. **עקבו אחר שימוש במשאבים** באמצעות Task Manager / nvidia-smi

### פתרון בעיות

1. **תמיד בדקו את השירות תחילה** לפני ניפוי שגיאות בקוד
2. **אתחלו את הליבה** אם אתם רואים הגדרות ישנות
3. **הריצו מחדש תאי אבחון** לאחר כל שינוי
4. **וודאו ששמות המודלים** תואמים למה שנטען
5. **אמתו את פורט נקודת הקצה** תואם למצב השירות

---

## הפניה מהירה: כינויים למודלים

### מודלים נפוצים

| כינוי | גודל | שימוש מיטבי | RAM/VRAM | וריאנטים |
|-------|------|-------------|----------|----------|
| `phi-4-mini` | ~4B | צ'אט כללי, סיכום | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | יצירת קוד, שכתוב | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | משימות כלליות, יעיל | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | מהיר, משאבים נמוכים | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | סיווג, משאבים מינימליים | 1-2GB | `-cpu`, `-cuda-gpu` |

### שמות וריאנטים

- **שם בסיס** (לדוגמה, `phi-4-mini`): בוחר אוטומטית את הווריאנט הטוב ביותר עבור החומרה שלכם
- **`-cpu`**: מותאם ל-CPU, עובד בכל מקום
- **`-cuda-gpu`**: מותאם ל-GPU של NVIDIA, דורש 8GB+ VRAM
- **`-npu`**: מותאם ל-NPU של Qualcomm, דורש דרייברים ל-NPU

**המלצה:** השתמשו בשמות בסיס (ללא סיומת) ותנו ל-Foundry Local לבחור אוטומטית את הווריאנט הטוב ביותר.

---

## מדדי הצלחה

אתם מוכנים כאשר:

✅ `foundry service status` מציג "פועל"
✅ `foundry model ls` מציג את המודלים הנדרשים
✅ השירות נגיש בנקודת הקצה הנכונה
✅ בדיקת בריאות מחזירה 200 OK
✅ תאי אבחון במחברת עוברים
✅ אין שגיאות חיבור בפלט

---

## קבלת עזרה

### תיעוד
- **מאגר ראשי**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **פתרון בעיות**: ראו `troubleshooting.md` בתיקייה זו

### בעיות ב-GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**עודכן לאחרונה:** 8 באוקטובר 2025  
**גרסה:** מחברות סדנה 2.0

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.