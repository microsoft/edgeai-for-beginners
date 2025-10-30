<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:26:59+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
# AGENTS.md

> **מדריך למפתחים לתרומה ל-EdgeAI למתחילים**
> 
> מסמך זה מספק מידע מקיף למפתחים, סוכני AI ותורמים העובדים עם מאגר זה. הוא כולל הגדרות, תהליכי פיתוח, בדיקות והנחיות לשיטות עבודה מומלצות.
> 
> **עודכן לאחרונה**: 30 באוקטובר 2025 | **גרסת מסמך**: 3.0

## תוכן עניינים

- [סקירת הפרויקט](../..)
- [מבנה המאגר](../..)
- [דרישות מוקדמות](../..)
- [פקודות הגדרה](../..)
- [תהליך פיתוח](../..)
- [הנחיות בדיקה](../..)
- [הנחיות לסגנון קוד](../..)
- [הנחיות לבקשות משיכה](../..)
- [מערכת תרגום](../..)
- [אינטגרציה מקומית של Foundry](../..)
- [בנייה ופריסה](../..)
- [בעיות נפוצות ופתרון תקלות](../..)
- [משאבים נוספים](../..)
- [הערות ספציפיות לפרויקט](../..)
- [קבלת עזרה](../..)

## סקירת הפרויקט

EdgeAI למתחילים הוא מאגר חינוכי מקיף המלמד פיתוח Edge AI עם מודלים לשוניים קטנים (SLMs). הקורס מכסה יסודות EdgeAI, פריסת מודלים, טכניקות אופטימיזציה ויישומים מוכנים לייצור באמצעות Microsoft Foundry Local ומסגרות AI שונות.

**טכנולוגיות מרכזיות:**
- Python 3.8+ (שפה ראשית לדוגמאות AI/ML)
- .NET C# (דוגמאות AI/ML)
- JavaScript/Node.js עם Electron (לאפליקציות שולחניות)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- מסגרות AI: LangChain, Semantic Kernel, Chainlit
- אופטימיזציית מודלים: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**סוג מאגר:** מאגר תוכן חינוכי עם 8 מודולים ו-10 אפליקציות דוגמה מקיפות

**ארכיטקטורה:** מסלול למידה רב-מודולי עם דוגמאות מעשיות המדגימות דפוסי פריסת Edge AI

## מבנה המאגר

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## דרישות מוקדמות

### כלים נדרשים

- **Python 3.8+** - לדוגמאות AI/ML ומחברות
- **Node.js 16+** - לאפליקציית דוגמה של Electron
- **Git** - לשליטה בגרסאות
- **Microsoft Foundry Local** - להפעלת מודלים AI באופן מקומי

### כלים מומלצים

- **Visual Studio Code** - עם הרחבות Python, Jupyter ו-Pylance
- **Windows Terminal** - לחוויית שורת פקודה טובה יותר (משתמשי Windows)
- **Docker** - לפיתוח במיכלים (אופציונלי)

### דרישות מערכת

- **RAM**: מינימום 8GB, מומלץ 16GB+ לתרחישים רב-מודליים
- **אחסון**: 10GB+ שטח פנוי למודלים ותלויות
- **OS**: Windows 10/11, macOS 11+, או Linux (Ubuntu 20.04+)
- **חומרה**: מעבד עם תמיכה ב-AVX2; GPU (CUDA, Qualcomm NPU) אופציונלי אך מומלץ

### דרישות ידע

- הבנה בסיסית של תכנות ב-Python
- היכרות עם ממשקי שורת פקודה
- הבנה של מושגי AI/ML (לפיתוח דוגמאות)
- תהליכי עבודה עם Git ובקשות משיכה

## פקודות הגדרה

### הגדרת מאגר

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### הגדרת דוגמאות Python (מודול08 ודוגמאות סדנה)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### הגדרת דוגמאות Node.js (דוגמה 08 - אפליקציית צ'אט ל-Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### הגדרת Foundry Local

Foundry Local נדרש להפעלת הדוגמאות. הורד והתקן מהמאגר הרשמי:

**התקנה:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ידני**: הורד מ-[דף ההפצות](https://github.com/microsoft/Foundry-Local/releases)

**התחלה מהירה:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**הערה**: Foundry Local בוחר אוטומטית את גרסת המודל הטובה ביותר עבור החומרה שלך (CUDA GPU, Qualcomm NPU, או CPU).

## תהליך פיתוח

### פיתוח תוכן

מאגר זה מכיל בעיקר **תוכן חינוכי ב-Markdown**. בעת ביצוע שינויים:

1. ערוך קבצי `.md` בתיקיות המודולים המתאימות
2. עקוב אחר דפוסי העיצוב הקיימים
3. ודא שדוגמאות הקוד מדויקות ונבדקו
4. עדכן את התוכן המתורגם המתאים אם יש צורך (או תן לאוטומציה לטפל בכך)

### פיתוח אפליקציות דוגמה

לדוגמאות Python במודול08 (דוגמאות 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

לדוגמאות Python בסדנה:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

לדוגמת Electron (דוגמה 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### בדיקת אפליקציות דוגמה

לדוגמאות Python אין בדיקות אוטומטיות אך ניתן לאמת אותן על ידי הפעלתן:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

לדוגמת Electron יש תשתית בדיקות:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## הנחיות בדיקה

### אימות תוכן

המאגר משתמש בתהליכי תרגום אוטומטיים. אין צורך בבדיקות ידניות לתרגומים.

**אימות ידני לשינויים בתוכן:**
1. סקור את תצוגת Markdown על ידי תצוגה מקדימה של קבצי `.md`
2. ודא שכל הקישורים מצביעים על יעדים תקפים
3. בדוק כל קטעי קוד הכלולים בתיעוד
4. בדוק שהתמונות נטענות כראוי

### בדיקת אפליקציות דוגמה

**מודול08/דוגמאות/08 (אפליקציית Electron) כוללת בדיקות מקיפות:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**דוגמאות Python צריכות להיבדק ידנית:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## הנחיות לסגנון קוד

### תוכן Markdown

- השתמש בהיררכיית כותרות עקבית (# לכותרת, ## לסעיפים ראשיים, ### לסעיפים משנה)
- כלול קטעי קוד עם מפרטי שפה: ```python, ```bash, ```javascript
- עקוב אחר העיצוב הקיים לטבלאות, רשימות והדגשות
- שמור על שורות קריאות (שאף ל-~80-100 תווים, אך לא חובה)
- השתמש בקישורים יחסיים להפניות פנימיות

### סגנון קוד Python

- עקוב אחר מוסכמות PEP 8
- השתמש ברמזי סוגים במידת הצורך
- כלול docstrings לפונקציות ומחלקות
- השתמש בשמות משתנים משמעותיים
- שמור על פונקציות ממוקדות ותמציתיות

### סגנון קוד JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**מוסכמות מרכזיות:**
- תצורת ESLint מסופקת בדוגמה 08
- Prettier לעיצוב קוד
- השתמש בתחביר מודרני ES6+
- עקוב אחר דפוסים קיימים בקוד

## הנחיות לבקשות משיכה

### תהליך תרומה

1. **פצל את המאגר** ויצור ענף חדש מ-`main`
2. **בצע את השינויים שלך** בהתאם להנחיות סגנון הקוד
3. **בדוק היטב** באמצעות הנחיות הבדיקה לעיל
4. **בצע התחייבות עם הודעות ברורות** בהתאם לפורמט התחייבויות קונבנציונלי
5. **דחף למאגר שלך** ויצור בקשת משיכה
6. **הגב למשוב** מהמתחזקים במהלך הסקירה

### מוסכמות שמות ענפים

- `feature/<module>-<description>` - לתכונות או תוכן חדשים
- `fix/<module>-<description>` - לתיקוני באגים
- `docs/<description>` - לשיפורי תיעוד
- `refactor/<description>` - לשינוי מבנה קוד

### פורמט הודעת התחייבות

עקוב אחר [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**דוגמאות:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### פורמט כותרת
```
[ModuleXX] Brief description of change
```
או
```
[Module08/samples/XX] Description for sample changes
```

### קוד התנהגות

כל התורמים חייבים לעקוב אחר [קוד ההתנהגות של Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). אנא עיין ב-[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) לפני התרומה.

### לפני הגשה

**לשינויים בתוכן:**
- תצוגה מקדימה של כל קבצי Markdown ששונו
- ודא שהקישורים והתמונות עובדים
- בדוק שגיאות כתיב ודקדוק

**לשינויים בקוד דוגמה (מודול08/דוגמאות/08):**
```bash
npm run lint
npm test
```

**לשינויים בדוגמאות Python:**
- בדוק שהדוגמה פועלת בהצלחה
- ודא שטיפול בשגיאות עובד
- בדוק תאימות עם Foundry Local

### תהליך סקירה

- שינויים בתוכן חינוכי נבדקים לדיוק ובהירות
- דוגמאות קוד נבדקות לפונקציונליות
- עדכוני תרגום מטופלים אוטומטית על ידי GitHub Actions

## מערכת תרגום

**חשוב:** מאגר זה משתמש בתרגום אוטומטי באמצעות GitHub Actions.

- תרגומים נמצאים בתיקיית `/translations/` (50+ שפות)
- אוטומטי באמצעות `co-op-translator.yml` workflow
- **אל תערוך ידנית קבצי תרגום** - הם יוחלפו
- ערוך רק קבצי מקור באנגלית בתיקיות השורש והמודולים
- תרגומים נוצרים אוטומטית בעת דחיפה לענף `main`

## אינטגרציה מקומית של Foundry

רוב דוגמאות מודול08 דורשות הפעלת Microsoft Foundry Local.

### התקנה והגדרה

**התקן Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**התקן Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### הפעלת Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### שימוש ב-SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### אימות Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### משתני סביבה לדוגמאות

רוב הדוגמאות משתמשות במשתני סביבה אלו:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**הערה**: בעת שימוש ב-`FoundryLocalManager`, ה-SDK מטפל אוטומטית בגילוי שירות וטעינת מודלים. כינויים למודלים (כמו `phi-3.5-mini`) מבטיחים שהגרסה הטובה ביותר נבחרת עבור החומרה שלך.

## בנייה ופריסה

### פריסת תוכן

מאגר זה הוא בעיקר תיעוד - אין צורך בתהליך בנייה לתוכן.

### בניית אפליקציות דוגמה

**אפליקציית Electron (מודול08/דוגמאות/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**דוגמאות Python:**
אין תהליך בנייה - הדוגמאות מופעלות ישירות עם מפרש Python.

## בעיות נפוצות ופתרון תקלות

> **טיפ**: בדוק [בעיות GitHub](https://github.com/microsoft/edgeai-for-beginners/issues) לבעיות ופתרונות ידועים.

### בעיות קריטיות (חוסמות)

#### Foundry Local לא פועל
**בעיה:** דוגמאות נכשלות עם שגיאות חיבור

**פתרון:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### בעיות נפוצות (מתונות)

#### בעיות בסביבת Python Virtual
**בעיה:** שגיאות ייבוא מודולים

**פתרון:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### בעיות בניית Electron
**בעיה:** npm install או כשלי בנייה

**פתרון:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### בעיות תהליך עבודה (קלות)

#### קונפליקטים בתהליך תרגום
**בעיה:** קונפליקטים בבקשת תרגום עם השינויים שלך

**פתרון:**
- ערוך רק קבצי מקור באנגלית
- תן לתהליך התרגום האוטומטי לטפל בתרגומים
- אם מתרחשים קונפליקטים, מיזג `main` לענף שלך לאחר שהתמזגו תרגומים

#### כשלי הורדת מודלים
**בעיה:** Foundry Local נכשל בהורדת מודלים

**פתרון:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## משאבים נוספים

### מסלולי למידה
- **מסלול מתחילים:** מודולים 01-02 (7-9 שעות)
- **מסלול ביניים:** מודולים 03-04 (9-11 שעות)
- **מסלול מתקדם:** מודולים 05-07 (12-15 שעות)
- **מסלול מומחים:** מודול 08 (8-10 שעות)
- **סדנה מעשית:** חומרי סדנה (6-8 שעות)

### תוכן מודול מרכזי
- **מודול01:** יסודות EdgeAI ומקרי מבחן בעולם האמיתי
- **מודול02:** משפחות מודלים לשוניים קטנים (SLM) וארכיטקטורות
- **מודול03:** אסטרטגיות פריסה מקומיות ובענן
- **מודול04:** אופטימיזציית מודלים עם מסגרות שונות (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **מודול05:** SLMOps - תפעול בייצור
- **מודול06:** סוכני AI וקריאת פונקציות
- **מודול07:** יישומים ספציפיים לפלטפורמה
- **מודול08:** ערכת כלים Foundry Local עם 10 דוגמאות מקיפות

### תלות חיצוניות
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - זמן ריצה למודלים AI מקומיים עם API תואם OpenAI
  - [תיעוד](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - מסגרת אופטימיזציה
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ערכת כלים לאופטימיזציית מודלים
- [OpenVINO](https://docs.openvino.ai/) - ערכת אופטימיזציה של אינטל

## הערות ספציפיות לפרויקט

### אפליקציות דוגמה מודול08

המאגר כולל 10 אפליקציות דוגמה מקיפות:

1. **01-REST Chat Quickstart** - אינטגרציה בסיסית של OpenAI SDK
2. **02-OpenAI SDK Integration** - תכונות מתקדמות של SDK
3. **03-Model Discovery & Benchmarking** - כלי השוואת מודלים
4. **04-Chainlit RAG Application** - יצירה מוגברת על ידי אחזור מידע
5. **05-Multi-Agent Orchestration** - תיאום סוכנים בסיסי
6. **06-Models-as-Tools Router** - ניתוב מודלים חכם
7. **07-Direct API Client** - אינטגרציה API ברמה נמוכה
8. **08-Windows 11 Chat App** - אפליקציית שולחן עבודה Electron מקורית
9. **09-Advanced Multi-Agent System** - תיאום סוכנים מורכב
10. **10-כלי מסגרת Foundry** - אינטגרציה של LangChain/Semantic Kernel

### דוגמאות יישומים בסדנה

הסדנה כוללת 6 מפגשים מתקדמים עם יישומים מעשיים:

1. **מפגש 01** - אתחול צ'אט עם אינטגרציה של Foundry Local
2. **מפגש 02** - צנרת RAG והערכה עם RAGAS
3. **מפגש 03** - ביצוע השוואות למודלים בקוד פתוח
4. **מפגש 04** - השוואה ובחירה של מודלים
5. **מפגש 05** - מערכות תזמור רב-סוכנים
6. **מפגש 06** - ניתוב מודלים וניהול צנרת

כל דוגמה מציגה היבטים שונים של פיתוח AI בקצה עם Foundry Local.

### שיקולי ביצועים

- SLMs מותאמים לפריסה בקצה (2-16GB RAM)
- הסקת מסקנות מקומית מספקת זמני תגובה של 50-500ms
- טכניקות כימות משיגות הפחתת גודל של 75% עם שמירה על 85% ביצועים
- יכולות שיחה בזמן אמת עם מודלים מקומיים

### אבטחה ופרטיות

- כל העיבוד מתבצע באופן מקומי - אין שליחת נתונים לענן
- מתאים ליישומים רגישים לפרטיות (בריאות, פיננסים)
- עומד בדרישות ריבונות נתונים
- Foundry Local פועל כולו על חומרה מקומית

## קבלת עזרה

### תיעוד

- **README ראשי**: [README.md](README.md) - סקירת מאגר ונתיבי למידה
- **מדריך לימוד**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - משאבי למידה ולוח זמנים
- **תמיכה**: [SUPPORT.md](SUPPORT.md) - כיצד לקבל עזרה
- **אבטחה**: [SECURITY.md](SECURITY.md) - דיווח על בעיות אבטחה

### תמיכה קהילתית

- **בעיות GitHub**: [דיווח על באגים או בקשת תכונות](https://github.com/microsoft/edgeai-for-beginners/issues)
- **דיונים ב-GitHub**: [שאל שאלות ושתף רעיונות](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **בעיות Foundry Local**: [בעיות טכניות עם Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### יצירת קשר

- **מתחזקים**: ראו [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **בעיות אבטחה**: עקוב אחר גילוי אחראי ב-[SECURITY.md](SECURITY.md)
- **תמיכת Microsoft**: לתמיכה ארגונית, צור קשר עם שירות הלקוחות של Microsoft

### משאבים נוספים

- **Microsoft Learn**: [נתיבי למידה של AI ולמידת מכונה](https://learn.microsoft.com/training/browse/?products=ai-services)
- **תיעוד Foundry Local**: [תיעוד רשמי](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **דוגמאות קהילתיות**: בדוק [דיונים ב-GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) עבור תרומות קהילתיות

---

**זהו מאגר חינוכי המתמקד בהוראת פיתוח AI בקצה. דפוס התרומה העיקרי הוא שיפור תוכן חינוכי והוספה/שיפור של יישומים לדוגמה שמדגימים מושגים של AI בקצה.**

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.