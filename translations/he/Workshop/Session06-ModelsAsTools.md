# מפגש 6: Foundry Local – מודלים ככלים

## תקציר

התייחסו למודלים ככלים שניתן להרכיב בתוך שכבת הפעלה מקומית של AI. במפגש זה תלמדו כיצד לשרשר קריאות למספר מודלים מתמחים (SLM/LLM), לנתב משימות באופן סלקטיבי, ולחשוף ממשק SDK אחיד ליישומים. תבנו נתב מודלים קל משקל + מתכנן משימות, תשלבו אותו בסקריפט אפליקציה, ותתוו את מסלול ההרחבה ל-Azure AI Foundry עבור עומסי עבודה בייצור.

## מטרות למידה

- **להמשיג** מודלים ככלים אטומיים עם יכולות מוגדרות
- **לנתב** בקשות על בסיס כוונה / ניקוד היוריסטי
- **לשרשר** פלטים במשימות מרובות שלבים (פירוק → פתרון → שיפור)
- **לשלב** ממשק API אחיד ליישומים במורד הזרם
- **להרחיב** את העיצוב לענן (אותו חוזה תואם OpenAI)

## דרישות מוקדמות

- השלמת מפגשים 1–5
- מספר מודלים מקומיים במטמון (לדוגמה, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### קטע קוד לסביבה חוצת פלטפורמות

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
גישה לשירות מרוחק/VM מ-macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## זרימת הדגמה (30 דקות)

### 1. הצהרת יכולות כלי (5 דקות)

צרו `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```
  

### 2. זיהוי כוונה וניתוב (8 דקות)

צרו `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```
  

### 3. שרשור משימות מרובות שלבים (7 דקות)

צרו `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```
  

### 4. פרויקט התחלתי: התאמת `06-models-as-tools` (5 דקות)

שיפורים:
- הוספת תמיכה בזרימת טוקנים (עדכון UI מתקדם)
- הוספת ניקוד ביטחון: חפיפה לקסיקלית או קריטריונים של הנחיה
- ייצוא JSON של מעקב (כוונה → מודל → זמן תגובה → שימוש בטוקנים)
- יישום שימוש חוזר במטמון עבור שלבים חוזרים

### 5. מסלול הרחבה ל-Azure (5 דקות)

| שכבה | מקומי (Foundry) | ענן (Azure AI Foundry) | אסטרטגיית מעבר |
|------|------------------|------------------------|-----------------|
| ניתוב | Python היוריסטי | מיקרו-שירות עמיד | קונטיינריזציה ופריסת API |
| מודלים | SLMs במטמון | פריסות מנוהלות | מיפוי שמות מקומיים ל-IDs של פריסות |
| תצפיות | סטטיסטיקות CLI/ידני | לוגים מרכזיים ומדדים | הוספת אירועי מעקב מובנים |
| אבטחה | מארח מקומי בלבד | אימות Azure / רשת | הוספת כספת מפתחות לסודות |
| עלות | משאבי מכשיר | חיוב צריכה | הוספת מגבלות תקציב |

## רשימת בדיקות לאימות

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
צפו בבחירת מודל מבוססת כוונה ובפלט סופי משופר.

## פתרון בעיות

| בעיה | סיבה | פתרון |
|------|------|-------|
| כל המשימות מנותבות לאותו מודל | כללים חלשים | העשרת סט regex של INTENT_RULES |
| הצינור נכשל באמצע שלב | מודל חסר טעון | הריצו `foundry model run <model>` |
| לכידות פלט נמוכה | אין שלב שיפור | הוספת מעבר סיכום/אימות |

## מקורות

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry  
- דפוסי איכות הנחיה: ראו מפגש 2  

---

**משך המפגש**: 30 דקות  
**רמת קושי**: מומחה  

## תרחיש לדוגמה ומיפוי סדנה

| סקריפטים / מחברות סדנה | תרחיש | מטרה | מקור נתונים / קטלוג |
|-------------------------|--------|-------|---------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | עוזר למפתחים המטפל בהנחיות כוונה מעורבות (שכתוב, סיכום, סיווג) | כוונה היוריסטית → ניתוב כינוי מודל עם שימוש בטוקנים | `CATALOG` מוטמע + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | תכנון ושיפור מרובי שלבים למשימת עזרה בקידוד מורכבת | פירוק → ביצוע מתמחה → שלב שיפור סיכום | אותו `CATALOG`; שלבים נגזרים מפלט תכנון |

### נרטיב תרחיש
כלי לשיפור פרודוקטיביות הנדסית מקבל משימות הטרוגניות: שכתוב קוד, סיכום הערות ארכיטקטורה, סיווג משוב. כדי למזער זמן תגובה ושימוש במשאבים, מודל כללי קטן מתכנן ומסכם, מודל מתמחה בקוד מטפל בשכתוב, ומודל קל משקל המסוגל לסיווג מתייג משוב. סקריפט הצינור מדגים שרשור + שיפור; סקריפט הנתב מבודד ניתוב הנחיה אדפטיבי.

### צילום קטלוג
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  

### הנחיות בדיקה לדוגמה
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  

### הרחבת מעקב (אופציונלי)
הוספת שורות JSON מעקב לכל שלב עבור `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  

### היוריסטיקת הסלמה (רעיון)
אם התכנון מכיל מילות מפתח כמו "אופטימיזציה", "אבטחה", או אורך שלב > 280 תווים → הסלמה למודל גדול יותר (לדוגמה, `gpt-oss-20b`) עבור אותו שלב בלבד.

### שיפורים אופציונליים

| תחום | שיפור | ערך | רמז |
|------|-------|-----|-----|
| מטמון | שימוש חוזר באובייקטי מנהל + לקוח | זמן תגובה נמוך יותר, פחות עומס | השתמשו ב-`workshop_utils.get_client` |
| מדדי שימוש | לכידת טוקנים וזמן תגובה לכל שלב | פרופיל ואופטימיזציה | מדדו כל קריאה מנותבת; שמרו ברשימת מעקב |
| ניתוב אדפטיבי | מודעות לביטחון / עלות | איזון איכות-עלות טוב יותר | הוספת ניקוד: אם הנחיה > N תווים או regex תואם תחום → הסלמה למודל גדול יותר |
| רישום יכולות דינמי | טעינת קטלוג חמה | אין צורך בהפעלה מחדש | טעינת `catalog.json` בזמן ריצה; מעקב אחר חותמת זמן קובץ |
| אסטרטגיית גיבוי | עמידות תחת כשלונות | זמינות גבוהה יותר | נסו ראשוני → במקרה של חריגה גיבוי כינוי |
| צינור זרימה | משוב מוקדם | שיפור חוויית משתמש | זרמו כל שלב ואגרו קלט שיפור סופי |
| הטמעות כוונה וקטוריות | ניתוב מעודן יותר | דיוק כוונה גבוה יותר | הטמעת הנחיה, אשכול ומיפוי מרכז → יכולת |
| ייצוא מעקב | שרשרת ניתנת לביקורת | תאימות/דיווח | פליטת שורות JSON: שלב, כוונה, מודל, זמן תגובה_ms, טוקנים |
| סימולציית עלות | הערכה לפני ענן | תכנון תקציב | הקצאת עלות נומינלית/טוקן לכל מודל וסיכום לכל משימה |
| מצב דטרמיניסטי | שחזור רפרודוקציה | מדדי ביצועים יציבים | סביבה: `temperature=0`, מספר שלבים קבוע |

#### דוגמת מבנה מעקב

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  

#### סקיצה להסלמה אדפטיבית

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```
  

#### טעינת קטלוג חמה

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```  

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.