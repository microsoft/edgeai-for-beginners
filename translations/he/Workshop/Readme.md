<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:28:36+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "he"
}
-->
# EdgeAI למתחילים - סדנה

> **מסלול למידה מעשי לבניית יישומי Edge AI מוכנים לייצור**
>
> שלוט בפריסת AI מקומית עם Microsoft Foundry Local, החל מהשלמת שיחה ראשונה ועד לתזמור רב-סוכנים ב-6 מפגשים מתקדמים.

---

## 🎯 מבוא

ברוכים הבאים ל**סדנת EdgeAI למתחילים** - המדריך המעשי שלך לבניית יישומים חכמים שפועלים לחלוטין על חומרה מקומית. הסדנה הזו הופכת את מושגי ה-Edge AI התיאורטיים לכישורים מעשיים בעולם האמיתי באמצעות תרגילים מאתגרים בהדרגה עם Microsoft Foundry Local ודגמי שפה קטנים (SLMs).

### למה הסדנה הזו?

**מהפכת ה-Edge AI כבר כאן**

ארגונים ברחבי העולם עוברים מ-AI תלוי ענן למחשוב קצה בשלושה סיבות קריטיות:

1. **פרטיות וציות** - עיבוד נתונים רגישים באופן מקומי ללא העברה לענן (HIPAA, GDPR, תקנות פיננסיות)
2. **ביצועים** - ביטול השהיית רשת (50-500ms מקומי לעומת 500-2000ms סבב ענן)
3. **שליטה בעלויות** - ביטול עלויות API לפי טוקן והרחבה ללא הוצאות ענן

**אבל Edge AI שונה**

הרצת AI מקומי דורשת כישורים חדשים:
- בחירה ואופטימיזציה של דגמים בהתחשב במגבלות משאבים
- ניהול שירותים מקומיים והאצת חומרה
- הנדסת הנחיות לדגמים קטנים
- תבניות פריסה לייצור עבור מכשירי קצה

**הסדנה הזו מספקת את הכישורים האלה**

ב-6 מפגשים ממוקדים (~3 שעות בסך הכל), תתקדם מ-"Hello World" לפריסת מערכות רב-סוכנים מוכנות לייצור - הכל פועל באופן מקומי על המחשב שלך.

---

## 📚 מטרות למידה

על ידי השלמת הסדנה, תוכל:

### מיומנויות ליבה
1. **לפרוס ולנהל שירותי AI מקומיים**
   - התקנה והגדרת Microsoft Foundry Local
   - בחירת דגמים מתאימים לפריסת קצה
   - ניהול מחזור חיים של דגמים (הורדה, טעינה, מטמון)
   - ניטור שימוש במשאבים ואופטימיזציה של ביצועים

2. **לבנות יישומים מבוססי AI**
   - יישום השלמות שיחה תואמות OpenAI באופן מקומי
   - עיצוב הנחיות אפקטיביות לדגמי שפה קטנים
   - טיפול בתגובות סטרימינג לשיפור חוויית המשתמש
   - שילוב דגמים מקומיים ביישומים קיימים

3. **ליצור מערכות RAG (הפקת מידע מוגברת)**
   - בניית חיפוש סמנטי עם הטבעות
   - ביסוס תגובות LLM בידע ספציפי לתחום
   - הערכת איכות RAG עם מדדים סטנדרטיים בתעשייה
   - הרחבה מפרוטוטיפ לייצור

4. **אופטימיזציה של ביצועי דגמים**
   - ביצוע בדיקות ביצועים לדגמים שונים עבור המקרה שלך
   - מדידת השהייה, תפוקה וזמן טוקן ראשון
   - בחירת דגמים אופטימליים בהתבסס על איזון בין מהירות ואיכות
   - השוואת יתרונות וחסרונות בין SLM ל-LLM בתרחישים אמיתיים

5. **תזמור מערכות רב-סוכנים**
   - עיצוב סוכנים מיוחדים למשימות שונות
   - יישום זיכרון סוכנים וניהול הקשר
   - תיאום סוכנים בתהליכי עבודה מורכבים
   - ניתוב בקשות בצורה חכמה בין דגמים שונים

6. **פריסת פתרונות מוכנים לייצור**
   - יישום טיפול בשגיאות ולוגיקת ניסיון חוזר
   - ניטור שימוש בטוקנים ומשאבי מערכת
   - בניית ארכיטקטורות ניתנות להרחבה עם תבניות דגם-ככלי
   - תכנון מסלולי מעבר מקצה להיברידי (קצה + ענן)

---

## 🎓 תוצאות למידה

### מה תבנה

בסיום הסדנה, תיצור:

| מפגש | תוצר | מיומנויות שהודגמו |
|------|-------|--------------------|
| **1** | יישום צ'אט עם סטרימינג | הגדרת שירות, השלמות בסיסיות, חוויית משתמש בסטרימינג |
| **2** | מערכת RAG עם הערכה | הטבעות, חיפוש סמנטי, מדדי איכות |
| **3** | חבילת בדיקות לדגמים מרובים | מדידת ביצועים, השוואת דגמים |
| **4** | משווה SLM מול LLM | ניתוח יתרונות וחסרונות, אסטרטגיות אופטימיזציה |
| **5** | מתזמר רב-סוכנים | עיצוב סוכנים, ניהול זיכרון, תיאום |
| **6** | מערכת ניתוב חכמה | זיהוי כוונה, בחירת דגמים, יכולת הרחבה |

### מטריצת מיומנויות

| רמת מיומנות | מפגש 1-2 | מפגש 3-4 | מפגש 5-6 |
|-------------|----------|----------|----------|
| **מתחילים** | ✅ הגדרה ובסיסים | ⚠️ מאתגר | ❌ מתקדם מדי |
| **בינוני** | ✅ סקירה מהירה | ✅ למידה עיקרית | ⚠️ מטרות מתקדמות |
| **מתקדמים** | ✅ קל ומהיר | ✅ שיפור | ✅ תבניות לייצור |

### מיומנויות מוכנות לקריירה

**לאחר הסדנה, תהיה מוכן ל:**

✅ **לבנות יישומים עם פרטיות בראש**
- אפליקציות בריאות המטפלות ב-PHI/PII באופן מקומי
- שירותים פיננסיים עם דרישות ציות
- מערכות ממשלתיות עם צורך בריבונות נתונים

✅ **אופטימיזציה לסביבות קצה**
- מכשירי IoT עם משאבים מוגבלים
- אפליקציות מובייל עם גישה ראשונית לא מקוונת
- מערכות בזמן אמת עם השהייה נמוכה

✅ **עיצוב ארכיטקטורות חכמות**
- מערכות רב-סוכנים לתהליכי עבודה מורכבים
- פריסות היברידיות קצה-ענן
- תשתית AI אופטימלית מבחינת עלויות

✅ **הובלת יוזמות Edge AI**
- הערכת היתכנות Edge AI לפרויקטים
- בחירת דגמים ומסגרות מתאימות
- עיצוב פתרונות AI מקומיים ניתנים להרחבה

---

## 🗺️ מבנה הסדנה

### סקירת מפגשים (6 מפגשים × 30 דקות = 3 שעות)

| מפגש | נושא | מיקוד | משך |
|------|------|-------|------|
| **1** | התחלה עם Foundry Local | התקנה, אימות, השלמות ראשונות | 30 דקות |
| **2** | בניית פתרונות AI עם RAG | הנדסת הנחיות, הטבעות, הערכה | 30 דקות |
| **3** | דגמים בקוד פתוח | גילוי דגמים, בדיקות ביצועים, בחירה | 30 דקות |
| **4** | דגמים מתקדמים | SLM מול LLM, אופטימיזציה, מסגרות | 30 דקות |
| **5** | סוכנים מבוססי AI | עיצוב סוכנים, תזמור, זיכרון | 30 דקות |
| **6** | דגמים ככלים | ניתוב, שרשור, אסטרטגיות הרחבה | 30 דקות |

---

## 🚀 התחלה מהירה

### דרישות מקדימות

**דרישות מערכת:**
- **מערכת הפעלה**: Windows 10/11, macOS 11+, או Linux (Ubuntu 20.04+)
- **RAM**: מינימום 8GB, מומלץ 16GB+
- **אחסון**: לפחות 10GB פנוי לדגמים
- **מעבד**: מעבד מודרני עם תמיכה ב-AVX2
- **GPU** (אופציונלי): תואם CUDA או Qualcomm NPU להאצה

**דרישות תוכנה:**
- **Python 3.8+** ([הורדה](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([מדריך התקנה](../../../Workshop))
- **Git** ([הורדה](https://git-scm.com/downloads))
- **Visual Studio Code** (מומלץ) ([הורדה](https://code.visualstudio.com/))

### הגדרה ב-3 שלבים

#### 1. התקנת Foundry Local

**Windows:**
```powershell
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
foundry service status
```

**וודא ש-Azure AI Foundry Local פועל עם פורט קבוע**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**אימות פעולה:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**מציאת דגמים זמינים**
כדי לראות אילו דגמים זמינים ב-Foundry Local שלך, ניתן לשאול את נקודת הקצה של הדגמים:

```bash
# cmd/bash/powershell
foundry model list
```

באמצעות נקודת קצה אינטרנטית 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. שיבוט מאגר והתקנת תלות

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. הרצת דוגמה ראשונה

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ הצלחה!** אתה אמור לראות תגובת סטרימינג על Edge AI.

---

## 📦 משאבי הסדנה

### דוגמאות Python

דוגמאות מעשיות מדורגות המדגימות כל מושג:

| מפגש | דוגמה | תיאור | זמן ריצה |
|------|-------|-------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | צ'אט בסיסי וסטרימינג | ~30 שניות |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG עם הטבעות | ~45 שניות |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | הערכת איכות RAG | ~60 שניות |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | בדיקות ביצועים לדגמים מרובים | ~2-3 דקות |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | השוואת SLM מול LLM | ~45 שניות |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | מערכת רב-סוכנים | ~60 שניות |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | ניתוב מבוסס כוונה | ~45 שניות |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | צנרת רב-שלבית | ~60 שניות |

### מחברות Jupyter

חקירה אינטראקטיבית עם הסברים והדמיות:

| מפגש | מחברת | תיאור | רמת קושי |
|------|-------|-------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | יסודות צ'אט וסטרימינג | ⭐ מתחילים |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | בניית מערכת RAG | ⭐⭐ בינוני |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | הערכת איכות RAG | ⭐⭐ בינוני |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | בדיקות ביצועים לדגמים | ⭐⭐ בינוני |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | השוואת דגמים | ⭐⭐ בינוני |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | תזמור סוכנים | ⭐⭐⭐ מתקדם |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | ניתוב כוונות | ⭐⭐⭐ מתקדם |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | תזמור צנרת | ⭐⭐⭐ מתקדם |

### תיעוד

מדריכים ועמודי עזר מקיפים:

| מסמך | תיאור | מתי להשתמש |
|------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | מדריך הגדרה מהיר | התחלה מאפס |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | דף עזר לפקודות ו-API | צריך תשובות מהירות |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | תבניות ודוגמאות SDK | כתיבת קוד |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | מדריך משתני סביבה | הגדרת דוגמאות |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | שיפורים אחרונים בדוגמאות | הבנת שינויים |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | מדריך מעבר | שדרוג קוד |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | בעיות נפוצות ופתרונות | פתרון בעיות |

---

## 🎓 המלצות מסלול למידה

### למתחילים (3-4 שעות)
1. ✅ מפגש 1: התחלה (מיקוד בהגדרה וצ'אט בסיסי)
2. ✅ מפגש 2: יסודות RAG (דלג על הערכה בהתחלה)
3. ✅ מפגש 3: בדיקות פשוטות (רק 2 דגמים)
4. ⏭️ דלג על מפגשים 4-6 לעת עתה
5. 🔄 חזור למפגשים 4-6 לאחר בניית יישום ראשון

### למפתחים בינוניים (3 שעות)
1. ⚡ מפגש 1: אימות הגדרה מהיר
2. ✅ מפגש 2: השלמת צנרת RAG עם הערכה
3. ✅ מפגש 3: חבילת בדיקות מלאה
4. ✅ מפגש 4: אופטימיזציה של דגמים
5. ✅ מפגשים 5-6: מיקוד בתבניות ארכיטקטורה

### למשתמשים מתקדמים (2-3 שעות)
1. ⚡ מפגשים 1-3: סקירה ואימות מהירים
2. ✅ מפגש 4: העמקה באופטימיזציה
3. ✅ מפגש 5: ארכיטקטורת רב-סוכנים
4. ✅ מפגש 6: תבניות לייצור והרחבה
5. 🚀 הרחבה: בניית לוגיקת ניתוב מותאמת אישית ופריסות היברידיות

---

## חבילת מפגשי סדנה (מעבדות ממוקדות של 30 דקות)

אם אתה עוקב אחרי פורמט הסדנה המכווץ של 6 מפגשים, השתמש במדריכים הייעודיים האלה (כל אחד מתאים ומשלים את מסמכי המודול הרחבים לעיל):

| מפגש סדנה | מדריך | מיקוד עיקרי |
|-----------|-------|-------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | התקנה, אימות, הרצת phi & GPT-OSS-20B, האצה |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | הנדסת הנחיות, תבניות RAG, בסיסי CSV ומסמכים, מעבר |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | אינטגרציה עם Hugging Face, בדיקות ביצועים, בחירת דגמים |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM מול LLM, WebGPU, Chainlit RAG, האצת ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | תפקידי סוכנים, זיכרון, כלים, תזמור |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | ניתוב, שרשור, מסלול סקיילינג ל-Azure |

כל קובץ סשן כולל: תקציר, מטרות למידה, זרימת הדגמה של 30 דקות, פרויקט התחלתי, רשימת בדיקות אימות, פתרון בעיות, והפניות ל-SDK של Foundry Local Python הרשמי.

### סקריפטים לדוגמה

התקנת תלותים לסדנה (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

אם מפעילים את שירות Foundry Local במחשב או VM אחר (Windows) מ-macOS, יש לייצא את נקודת הקצה:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| סשן | סקריפט(ים) | תיאור |
|-----|------------|-------|
| 1 | `samples/session01/chat_bootstrap.py` | הפעלת שירות וצ'אט סטרימינג |
| 2 | `samples/session02/rag_pipeline.py` | RAG מינימלי (הטמעות בזיכרון) |
|   | `samples/session02/rag_eval_ragas.py` | הערכת RAG עם מדדי ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | מדידת זמן תגובה ותפוקה של מודלים מרובים |
| 4 | `samples/session04/model_compare.py` | השוואת SLM מול LLM (זמן תגובה ותוצאות דוגמה) |
| 5 | `samples/session05/agents_orchestrator.py` | צינור מחקר → עריכה עם שני סוכנים |
| 6 | `samples/session06/models_router.py` | הדגמת ניתוב מבוסס כוונה |
|   | `samples/session06/models_pipeline.py` | שרשרת תכנון/ביצוע/שיפור רב-שלבית |

### משתני סביבה (משותפים לכל הסקריפטים)

| משתנה | מטרה | דוגמה |
|-------|------|-------|
| `FOUNDRY_LOCAL_ALIAS` | כינוי מודל יחיד ברירת מחדל לדוגמאות בסיסיות | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM מפורש מול מודל גדול יותר להשוואה | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | רשימת כינויים למדידת ביצועים | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | חזרות למדידת ביצועים לכל מודל | `3` |
| `BENCH_PROMPT` | פקודה המשמשת במדידת ביצועים | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | מודל הטמעות של sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | שאילתה מותאמת אישית לצינור RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | שאילתה מותאמת אישית לצינור סוכנים | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | כינוי מודל לסוכן מחקר | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | כינוי מודל לסוכן עורך (יכול להיות שונה) | `gpt-oss-20b` |
| `SHOW_USAGE` | כאשר `1`, מדפיס שימוש בטוקנים לכל השלמה | `1` |
| `RETRY_ON_FAIL` | כאשר `1`, מנסה שוב במקרה של שגיאות צ'אט זמניות | `1` |
| `RETRY_BACKOFF` | שניות להמתנה לפני ניסיון חוזר | `1.0` |

אם משתנה לא מוגדר, הסקריפטים נופלים לברירות מחדל הגיוניות. לדוגמאות של מודל יחיד בדרך כלל צריך רק את `FOUNDRY_LOCAL_ALIAS`.

### מודול עזר

כל הדוגמאות חולקות כעת את `samples/workshop_utils.py`, המספק:

* יצירת `FoundryLocalManager` + לקוח OpenAI עם מטמון
* עזר `chat_once()` עם ניסיון חוזר אופציונלי + הדפסת שימוש
* דיווח פשוט על שימוש בטוקנים (ניתן להפעיל באמצעות `SHOW_USAGE=1`)

זה מפחית כפילויות ומדגיש שיטות עבודה מומלצות לתזמור יעיל של מודלים מקומיים.

## שיפורים אופציונליים (בין סשנים)

| נושא | שיפור | סשנים | סביבה / מתג |
|------|-------|-------|-------------|
| דטרמיניזם | טמפרטורה קבועה + סטים יציבים של פקודות | 1–6 | הגדר `temperature=0`, `top_p=1` |
| נראות שימוש בטוקנים | הוראה עקבית על עלות/יעילות | 1–6 | `SHOW_USAGE=1` |
| סטרימינג טוקן ראשון | מדד זמן תגובה נתפס | 1,3,4,6 | `BENCH_STREAM=1` (מדידת ביצועים) |
| עמידות לניסיון חוזר | טיפול בהתחלה קרה זמנית | הכל | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| סוכנים רב-מודליים | התמחות תפקידים הטרוגנית | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| ניתוב אדפטיבי | כוונה + היוריסטיקות עלות | 6 | הרחב את הניתוב עם לוגיקת הסלמה |
| זיכרון וקטורי | זיכרון סמנטי לטווח ארוך | 2,5,6 | שלב אינדקס הטמעות FAISS/Chroma |
| ייצוא מעקב | ביקורת והערכה | 2,5,6 | הוסף שורות JSON לכל שלב |
| מדדי איכות | מעקב איכותני | 3–6 | פקודות ניקוד משניות |
| בדיקות מהירות | אימות מהיר לפני הסדנה | הכל | `python Workshop/tests/smoke.py` |

### התחלה מהירה דטרמיניסטית

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

צפו בספירת טוקנים יציבה על פני קלטים זהים חוזרים.

### הערכת RAG (סשן 2)

השתמשו ב-`rag_eval_ragas.py` לחישוב רלוונטיות תשובה, נאמנות, ודיוק הקשר על מערך נתונים סינתטי קטן:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

הרחיבו על ידי אספקת JSONL גדול יותר של שאלות, הקשרים, ואמיתות קרקע, ואז המרה ל-Dataset של Hugging Face.

## נספח דיוק פקודות CLI

הסדנה משתמשת רק בפקודות CLI של Foundry Local מתועדות ויציבות.

### פקודות יציבות שהוזכרו

| קטגוריה | פקודה | מטרה |
|---------|-------|------|
| ליבה | `foundry --version` | הצגת גרסה מותקנת |
| ליבה | `foundry init` | אתחול תצורה |
| שירות | `foundry service start` | הפעלת שירות מקומי (אם לא אוטומטי) |
| שירות | `foundry status` | הצגת מצב שירות |
| מודלים | `foundry model list` | רשימת קטלוג / מודלים זמינים |
| מודלים | `foundry model download <alias>` | הורדת משקלי מודל למטמון |
| מודלים | `foundry model run <alias>` | הפעלת מודל מקומי; ניתן לשלב עם `--prompt` להפעלה חד-פעמית |
| מודלים | `foundry model unload <alias>` / `foundry model stop <alias>` | הסרת מודל מהזיכרון (אם נתמך) |
| מטמון | `foundry cache list` | רשימת מודלים במטמון (שהורדו) |
| מערכת | `foundry system info` | צילום יכולות חומרה והאצה |
| מערכת | `foundry system gpu-info` | מידע אבחון GPU |
| תצורה | `foundry config list` | הצגת ערכי תצורה נוכחיים |
| תצורה | `foundry config set <key> <value>` | עדכון תצורה |

### תבנית פקודת הפעלה חד-פעמית

במקום פקודת משנה `model chat` שהוצאה משימוש, השתמשו ב:

```powershell
foundry model run <alias> --prompt "Your question here"
```

זה מבצע מחזור פקודה/תגובה יחיד ואז יוצא.

### דפוסים שהוסרו / נמנעו

| הוצאה משימוש / לא מתועד | תחליף / הנחיות |
|--------------------------|----------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | השתמשו ב-`foundry model list` רגיל + פעילות אחרונה / לוגים |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | השתמשו בסקריפט מדידת ביצועים + כלי מערכת (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### מדידת ביצועים וטלמטריה

- זמן תגובה, p95, טוקנים לשנייה: `samples/session03/benchmark_oss_models.py`
- זמן תגובה טוקן ראשון (סטרימינג): הגדר `BENCH_STREAM=1`
- שימוש במשאבים: כלי מערכת (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

כאשר פקודות טלמטריה CLI חדשות יתייצבו, ניתן יהיה לשלב אותן עם עריכות מינימליות לקובצי Markdown של הסשנים.

### שומר לינט אוטומטי

לינטר אוטומטי מונע החזרת דפוסי CLI שהוצאו משימוש בתוך בלוקי קוד מסומנים בקובצי Markdown:

סקריפט: `Workshop/scripts/lint_markdown_cli.py`

דפוסים שהוצאו משימוש נחסמים בתוך בלוקי קוד.

תחליפים מומלצים:
| הוצאה משימוש | תחליף |
|--------------|-------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | סקריפט מדידת ביצועים + כלי מערכת |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

הרצה מקומית:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` רץ בכל push ו-PR.

וו pre-commit אופציונלי:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## טבלת מעבר מהירה CLI → SDK

| משימה | פקודת CLI | מקבילה ב-SDK (Python) | הערות |
|-------|-----------|-----------------------|-------|
| הפעלת מודל פעם אחת (פקודה) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | ה-SDK מפעיל שירות ומטמון באופן אוטומטי |
| הורדת מודל (מטמון) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | המנהל בוחר את הגרסה הטובה ביותר אם הכינוי ממפה למספר בניות |
| רשימת קטלוג | `foundry model list` | `# use manager for each alias or maintain known list` | CLI מאגד; SDK כרגע לפי אתחול כינוי |
| רשימת מודלים במטמון | `foundry cache list` | `manager.list_cached_models()` | לאחר אתחול המנהל (כל כינוי) |
| הפעלת האצת GPU | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | התצורה היא תוצאה חיצונית |
| קבלת כתובת נקודת קצה | (מרומז) | `manager.endpoint` | משמש ליצירת לקוח תואם OpenAI |
| חימום מודל | `foundry model run <alias>` ואז פקודה ראשונה | `chat_once(alias, messages=[...])` (עזר) | עזרים מטפלים בחימום ראשוני של זמן תגובה קר |
| מדידת זמן תגובה | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (או סקריפט ייצוא חדש) | העדיפו סקריפט למדדים עקביים |
| עצירת מודל / הסרה מהזיכרון | `foundry model unload <alias>` | (לא חשוף – הפעל מחדש שירות / תהליך) | בדרך כלל לא נדרש לזרימת הסדנה |
| קבלת שימוש בטוקנים | (צפו בפלט) | `resp.usage.total_tokens` | מסופק אם ה-backend מחזיר אובייקט שימוש |

## ייצוא Markdown למדידת ביצועים

השתמשו בסקריפט `Workshop/scripts/export_benchmark_markdown.py` להרצת מדידת ביצועים חדשה (אותו לוגיקה כמו `samples/session03/benchmark_oss_models.py`) והפקת טבלת Markdown ידידותית ל-GitHub יחד עם JSON גולמי.

### דוגמה

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

קבצים שנוצרו:
| קובץ | תוכן |
|------|------|
| `benchmark_report.md` | טבלת Markdown + רמזי פרשנות |
| `benchmark_report.json` | מערך מדדים גולמי (למעקב אחר מגמות) |

הגדר `BENCH_STREAM=1` בסביבה כדי לכלול זמן תגובה טוקן ראשון אם נתמך.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.