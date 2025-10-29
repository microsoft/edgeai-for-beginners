<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:31:01+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "he"
}
-->
# סקריפטים לסדנה

תיקייה זו מכילה סקריפטים לאוטומציה ותמיכה המשמשים לשמירה על איכות ועקביות בחומרי הסדנה.

## תוכן

| קובץ | מטרה |
|------|---------|
| `lint_markdown_cli.py` | בודק גדרות קוד Markdown כדי לחסום דפוסי פקודות CLI מיושנות של Foundry Local. |
| `export_benchmark_markdown.py` | מבצע בדיקת ביצועים רב-מודלית ומפיק דוחות Markdown + JSON. |

## 1. בודק דפוסי CLI ב-Markdown

`lint_markdown_cli.py` סורק את כל קבצי `.md` שאינם תרגומים עבור דפוסי CLI של Foundry Local שאינם מותרים **בתוך גדרות קוד** (``` ... ```). ניתן עדיין להזכיר פקודות מיושנות בפרוזה אינפורמטיבית לצורך הקשר היסטורי.

### דפוסים מיושנים (חסומים בתוך גדרות קוד)

הבודק חוסם דפוסי CLI מיושנים. יש להשתמש באלטרנטיבות מודרניות במקום.

### החלפות נדרשות
| מיושן | השתמש במקום |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | סקריפט בדיקת ביצועים + כלי מערכת (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### קודי יציאה
| קוד | משמעות |
|------|---------|
| 0 | לא נמצאו הפרות |
| 1 | נמצאו דפוסים מיושנים אחד או יותר |

### הרצה מקומית
מתוך שורש המאגר (מומלץ):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### הוק לפני התחייבות (אופציונלי)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
זה חוסם התחייבויות שמכניסות דפוסים מיושנים.

### אינטגרציה ב-CI
תהליך עבודה של GitHub Action (`.github/workflows/markdown-cli-lint.yml`) מריץ את הבודק בכל דחיפה ובקשת משיכה לענפים `main` ו-`Reactor`. יש לתקן עבודות שנכשלו לפני מיזוג.

### הוספת דפוסים מיושנים חדשים
1. פתח את `lint_markdown_cli.py`.
2. הוסף זוג `(regex, suggestion)` לרשימת `DEPRECATED`. השתמש במחרוזת גולמית והכלל גבולות מילים `\b` במידת הצורך.
3. הרץ את הבודק מקומית כדי לוודא זיהוי.
4. התחייב ודחף; CI יאכוף את הכלל החדש.

דוגמה להוספה:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### התייחסות הסברית מותרת
מכיוון שרק גדרות קוד נאכפות, ניתן לתאר פקודות מיושנות בטקסט נרטיבי בבטחה. אם *חייבים* להציג אותן בתוך גדר לצורך השוואה, הוסף גדר **ללא** שלושה גרשיים (לדוגמה, הזחה או ציטוט) או כתוב בצורה פסאודו.

### דילוג על קבצים ספציפיים (מתקדם)
אם יש צורך, עטוף דוגמאות ישנות בקובץ נפרד מחוץ למאגר או שנה את הסיומת בזמן טיוטה. דילוגים מכוונים עבור עותקים מתורגמים הם אוטומטיים (נתיבים המכילים `translations`).

### פתרון בעיות
| בעיה | סיבה | פתרון |
|-------|-------|-----------|
| הבודק מסמן שורה שעדכנת | Regex רחב מדי | צמצם את הדפוס עם גבול מילים נוסף (`\b`) או עוגנים |
| CI נכשל אבל מקומי עובר | גרסת Python שונה או שינויים שלא התחייבו | הרץ מחדש מקומית, ודא עץ עבודה נקי, בדוק גרסת Python בתהליך העבודה (3.11) |
| צריך לעקוף זמנית | תיקון חירום | החל תיקון מיד לאחר מכן; שקול להשתמש בענף זמני ובקשת משיכה מעקבת (הימנע מהוספת מתגי עקיפה) |

### רציונל
שמירה על תיעוד מותאם לממשק CLI יציב *נוכחי* מונעת חיכוך בסדנה, נמנעת מבלבול למשתתפים, ומרכזת מדידת ביצועים דרך סקריפטים Python מתוחזקים במקום פקודות CLI משתנות.

---
מתוחזק כחלק משרשרת הכלים לאיכות הסדנה. לשיפורים (לדוגמה, תיקון אוטומטי של הצעות או יצירת דוחות HTML), פתח בעיה או הגש בקשת משיכה.

## 2. סקריפט אימות דוגמאות

`validate_samples.py` מאמת את כל קבצי הדוגמאות Python עבור תקינות תחביר, ייבוא, והתאמה לשיטות עבודה מומלצות.

### שימוש
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### מה הוא בודק
- ✅ תקינות תחביר Python
- ✅ ייבוא נדרש קיים
- ✅ יישום טיפול בשגיאות (מצב מפורט)
- ✅ שימוש ברמזי סוג (מצב מפורט)
- ✅ תיעוד פונקציות (מצב מפורט)
- ✅ קישורי הפניה ל-SDK (מצב מפורט)

### משתני סביבה
- `SKIP_IMPORT_CHECK=1` - דילוג על אימות ייבוא
- `SKIP_SYNTAX_CHECK=1` - דילוג על אימות תחביר

### קודי יציאה
- `0` - כל הדוגמאות עברו אימות
- `1` - אחת או יותר מהדוגמאות נכשלו

## 3. מריץ בדיקות לדוגמאות

`test_samples.py` מריץ בדיקות עישון על כל הדוגמאות כדי לוודא שהן מבוצעות ללא שגיאות.

### שימוש
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### דרישות מוקדמות
- שירות Foundry Local פועל: `foundry service start`
- מודלים נטענים: `foundry model run phi-4-mini`
- תלות מותקנות: `pip install -r requirements.txt`

### מה הוא בודק
- ✅ הדוגמה יכולה להתבצע ללא שגיאות בזמן ריצה
- ✅ הפלט הנדרש נוצר
- ✅ טיפול נכון בשגיאות במקרה של כשל
- ✅ ביצועים (זמן ביצוע)

### משתני סביבה
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - מודל לשימוש בבדיקה
- `TEST_TIMEOUT=30` - זמן קצוב לדוגמה בשניות

### כשלונות צפויים
חלק מהבדיקות עשויות להיכשל אם תלות אופציונליות לא מותקנות (לדוגמה, `ragas`, `sentence-transformers`). התקן עם:
```bash
pip install sentence-transformers ragas datasets
```

### קודי יציאה
- `0` - כל הבדיקות עברו
- `1` - אחת או יותר מהבדיקות נכשלו

## 4. ייצוא Markdown לבדיקת ביצועים

סקריפט: `export_benchmark_markdown.py`

יוצר טבלת ביצועים שחוזרת על עצמה עבור סט מודלים.

### שימוש
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### פלטים
| קובץ | תיאור |
|------|-------------|
| `benchmark_report.md` | טבלת Markdown (ממוצע, p95, טוקנים/שנייה, טוקן ראשון אופציונלי) |
| `benchmark_report.json` | מערך מדדים גולמי להשוואה והיסטוריה |

### אפשרויות
| דגל | תיאור | ברירת מחדל |
|------|-------------|---------|
| `--models` | שמות מודלים מופרדים בפסיקים | (נדרש) |
| `--prompt` | הנחיה בשימוש בכל סבב | (נדרש) |
| `--rounds` | סבבים לכל מודל | 3 |
| `--output` | קובץ פלט Markdown | `benchmark_report.md` |
| `--json` | קובץ פלט JSON | `benchmark_report.json` |
| `--fail-on-empty` | יציאה לא אפס אם כל הבדיקות נכשלות | כבוי |

משתנה סביבה `BENCH_STREAM=1` מוסיף מדידת זמן לטוקן הראשון.

### הערות
- משתמש מחדש ב-`workshop_utils` לצורך אתחול מודלים עקבי ואחסון במטמון.
- אם מורץ מתיקיית עבודה שונה, הסקריפט מנסה נתיבי גיבוי לאיתור `workshop_utils`.
- להשוואת GPU: הרץ פעם אחת, הפעל האצה דרך הגדרות CLI, הרץ מחדש והשווה את ה-JSON.

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.