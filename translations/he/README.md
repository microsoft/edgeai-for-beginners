# EdgeAI למתחילים


![תמונת עטיפת הקורס](../../translated_images/he/cover.eb18d1b9605d754b.webp)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![נושאים ב-GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![בקשות משיכה מתקבלות בברכה](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![צופים ב-GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![פורקים ב-GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

עקבו אחר הצעדים הללו כדי להתחיל להשתמש במשאבים אלה:

1. **צור fork של המאגר**: לחץ על [![פורקים ב-GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **שכפל את המאגר**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**הצטרף ל-Azure AI Foundry Discord ופגוש מומחים ומפתחי חברים**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 תמיכה בריבוי שפות

#### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מקאו)](../zh-MO/README.md) | [סינית (מסורתית, טייוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ׳כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדי](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנדה](../kn/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מאלית](../ms/README.md) | [מאלייאלאם](../ml/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פידג׳ין ניגרי](../pcm/README.md) | [נורווגית](../no/README.md) | [פרסית (פרסי)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פונג׳בי (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סוואהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טגלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

> **מעדיפים לשכפל מקומית?**

> מאגר זה כולל יותר מ-50 תרגומים בשפות שונות שמגדילים משמעותית את גודל ההורדה. כדי לשכפל ללא תרגומים, השתמשו ב-sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> זה נותן לך את כל מה שצריך כדי להשלים את הקורס עם הורדה הרבה יותר מהירה.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**אם תרצו לתמוך בשפות תרגום נוספות הן רשומות [כאן](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## مقدمة

ברוכים הבאים ל-**EdgeAI למתחילים** – המסע המקיף שלכם לעולם המהפכני של בינה מלאכותית בקצה. הקורס הזה מגשר על הפער בין יכולות AI עוצמתיות לפריסה מעשית בעולם האמיתי על התקני קצה, ומאפשר לכם לנצל את הפוטנציאל של AI ישירות במקום בו הנתונים נוצרים וההחלטות חייבות להתבצע.

### מה תלמדו לשלוט בו

הקורס יקח אתכם מהמושגים הבסיסיים ועד יישומים מוכנים לייצור, כולל:
- **מודלים שפתיים קטנים (SLMs)** מותאמים לפריסה בקצה
- **אופטימיזציה מודעת חומרה** על פני פלטפורמות מגוונות
- **חיזוי בזמן אמת** עם יכולות שמירה על פרטיות
- **אסטרטגיות פריסה ליישומים ארגוניים**

### למה EdgeAI חשוב

Edge AI מייצג שינוי פרדיגמה שמטפל באתגרים קריטיים מודרניים:
- **פרטיות ואבטחה**: עיבוד נתונים רגישים במכשיר ללא חשיפה לענן
- **ביצועים בזמן אמת**: הסרת עיכובי רשת ליישומים קריטיים לזמן
- **יעילות כלכלית**: הורדת עלויות רוחב פס ומחשוב ענן
- **עמידות תפעולית**: שמירה על פונקציונליות בזמן הפסקות רשת
- **ציות לרגולציה**: עמידה בדרישות ריבונות נתונים

### Edge AI

Edge AI מתייחס להרצת אלגוריתמים ומודלים שפתיים של AI באופן מקומי על חומרה, קרוב למקום בו הנתונים נוצרים, ללא תלות במשאבי ענן לצורך חיזוי. זה מקטין את העיכוב, משפר פרטיות ומאפשר קבלת החלטות בזמן אמת.

### עקרונות יסוד:
- **חיזוי במכשיר**: מודלי AI רצים על התקני קצה (טלפונים, נתבים, מיקרו-בקרים, מחשבים תעשייתיים)
- **יכולת לא מקוונת**: פועל ללא חיבור אינטרנט מתמיד
- **עיכוב נמוך**: תגובות מידיות מתאימות למערכות בזמן אמת
- **ריבונות נתונים**: שומר נתונים רגישים במכשיר, משפר אבטחה ועמידה ברגולציה

### מודלים שפתיים קטנים (SLMs)

SLMs כמו Phi-4, Mistral-7B ו-Gemma הם גרסאות מותאמות של LLM גדולים יותר — מאומנים או מזוקקים עבור:
- **רוחב זיכרון קטן**: שימוש יעיל בזיכרון המוגבל של התקני קצה
- **דרישת מחשוב נמוכה**: מותאם לביצועי CPU ו-GPU קטנים
- **זמני התחלה מהירים**: אתחול מהיר ליישומים תגובתיים

הם משחררים יכולות NLP עוצמתיות תוך עמידה במגבלות של:
- **מערכות משובצות**: התקני IoT ובקרים תעשייתיים
- **התקנים ניידים**: סמארטפונים וטאבלטים עם יכולות לא מקוונות
- **התקני IoT**: חיישנים והתקנים חכמים עם משאבים מוגבלים
- **שרתים בקצה**: יחידות עיבוד מקומיות עם משאבי GPU מוגבלים
- **מחשבים אישיים**: תרחישי פריסה במחשבים נייחים וניידים

## מודולי הקורס וניווט

| מודול | נושא | אזור מיקוד | תוכן מרכזי | רמה | משך זמן |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [הקדמה ל-EdgeAI](./introduction.md) | יסודות והקשר | סקירת EdgeAI • יישומי תעשייה • מבוא ל-SLM • מטרות הלמידה | מתחילים | 1-2 שעות |
| [📚 01](../../Module01) | [יסודות EdgeAI](./Module01/README.md) | השוואת ענן מול Edge AI | יסודות EdgeAI • מחקרי מקרה מהעולם האמיתי • מדריך ליישום • פריסת קצה | מתחילים | 3-4 שעות |
| [🧠 02](../../Module02) | [יסודות מודל SLM](./Module02/README.md) | משפחות מודלים ואדריכלות | משפחת Phi • משפחת Qwen • משפחת Gemma • BitNET • μModel • Phi-Silica | מתחילים | 4-5 שעות |
| [🚀 03](../../Module03) | [פרקטיקה בפריסת SLM](./Module03/README.md) | פריסה מקומית ועננית | למידה מתקדמת • סביבה מקומית • פריסת ענן | בינוני | 4-5 שעות |
| [⚙️ 04](../../Module04) | [כלי אופטימיזציה למודל](./Module04/README.md) | אופטימיזציה חוצה פלטפורמות | מבוא • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • סינתזת זרימת עבודה | בינוני | 5-6 שעות |
| [🔧 05](../../Module05) | [SLMOps בפרודקשן](./Module05/README.md) | פעולות פרודקשן | מבוא ל-SLMOps • זיקוק מודל • כוונון • פריסת פרודקשן | מתקדם | 5-6 שעות |
| [🤖 06](../../Module06) | [סוכנים בינה מלאכותית וקריאת פונקציות](./Module06/README.md) | מסגרות סוכנים ו-MCP | מבוא לסוכן • קריאת פונקציות • פרוטוקול הקשר מודלים | מתקדם | 4-5 שעות |
| [💻 07](../../Module07) | [יישום פלטפורמה](./Module07/README.md) | דוגמאות חוצה פלטפורמה | כלי AI • Foundry מקומי • פיתוח ב-Windows | מתקדם | 3-4 שעות |
| [🏭 08](../../Module08) | [כלי Foundry מקומיים](./Module08/README.md) | דוגמאות מוכנות לפרודקשן | יישומי דוגמה (ראו פרטים למטה) | מומחה | 8-10 שעות |

### 🏭 **מודול 08: יישומי דוגמה**

- [01: התחלת שיחה מהירה ב-REST](./Module08/samples/01/README.md)
- [02: אינטגרציית SDK של OpenAI](./Module08/samples/02/README.md)
- [03: גילוי מודלים וביצועי השוואה](./Module08/samples/03/README.md)
- [04: יישום Chainlit RAG](./Module08/samples/04/README.md)
- [05: תזמור רב-סוכנים](./Module08/samples/05/README.md)
- [06: נתב מודלים ככלים](./Module08/samples/06/README.md)
- [07: לקוח API ישיר](./Module08/samples/07/README.md)
- [08: אפליקציית שיחה ב-Windows 11](./Module08/samples/08/README.md)
- [09: מערכת רב-סוכנים מתקדמת](./Module08/samples/09/README.md)
- [10: מסגרת כלי Foundry](./Module08/samples/10/README.md)

### 🎓 **סדנה: מסלול למידה מעשי**

חומרים מקיפים לסדנה עם יישומים מוכנים לפרודקשן:

- **[מדריך לסדנה](./Workshop/Readme.md)** - מטרות למידה מלאות, תוצאות וניווט במשאבים
- **דוגמאות פייתון** (6 מפגשים) - מעודכנות עם שיטות עבודה מומלצות, טיפול בשגיאות ותיעוד מלא
- **מחברות Jupyter** (8 אינטראקטיביות) - מדריכים שלב אחר שלב עם מדדי ביצועים ומעקב
- **מדריכים למפגשים** - מדריכים מפורטים במארקדאון לכל מפגש בסדנה
- **כלי אימות** - סקריפטים לאימות איכות הקוד והרצת בדיקות בסיס

**מה תבנו:**
- אפליקציות שיחה מבוססות AI מקומיות עם תמיכה בזרימה
- צינורות RAG עם הערכת איכות (RAGAS)
- כלי השוואה וביצועים למודלים מרובים
- מערכות תזמור רב-סוכנים
- ניתוב מודלים חכם עם בחירה מבוססת משימות

### 🎙️ **סדנת Agentic: Hands-On - הסטודיו לפודקאסט AI**

בנו צינור הפקה לפודקאסט מונע בינה מלאכותית מאפס! הסדנה המעמיקה הזו מלמדת כיצד ליצור מערכת רב-סוכנים שלמה שהופכת רעיונות לפרקי פודקאסט מקצועיים.
**[🎬 התחילו את סדנת אולפן הפודקאסטים מבוססי ה-AI](./WorkshopForAgentic/README.md)**

**המשימה שלך**: השיקו את "Future Bytes" — פודקאסט טכנולוגי מופעל כולו על ידי סוכני AI שתבנו בעצמכם. ללא תלות בענן, ללא עלויות API — הכל רץ מקומית במחשב שלכם.

**מה עושה את זה ייחודי:**
- **🤖 אורקסטרציה אמיתית של סוכני AI מרובים** - בנו סוכני AI מתמחים שמחקרים, כותבים ומפיקים אודיו
- **🎯 צינור הפקה מלא** - מבחירת נושא ועד פלט סופי של אודיו לפודקאסט
- **💻 פריסה מקומית 100%** - משתמש באולמה ודגמים מקומיים (Qwen-3-8B) לפרטיות ושליטה מלאה
- **🎤 אינטגרציית טקסט לדיבור** - הפכו סקריפטים לשיחות טבעיות עם דוברים מרובים
- **✋ תהליכים עם מעורבות אנושית** - שערי אישור שמבטיחים איכות תוך שמירה על אוטומציה

**מסע למידה בשלושה שלבים:**

| שלב | מוקד | מיומנויות עיקריות | משך זמן |
|-----|-------|------------|----------|
| **[שלב 1: הכירו את סוכני ה-AI שלכם](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | בנו את סוכן ה-AI הראשון שלכם | אינטגרציית כלים • חיפוש ברשת • פתרון בעיות • ניתוח סוכני | 2-3 שעות |
| **[שלב 2: הרכיבו את צוות ההפקה שלכם](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | אורקסטרציה של סוכנים מרובים | תיאום צוות • תהליכי אישור • ממשק DevUI • פיקוח אנושי | 3-4 שעות |
| **[שלב 3: הביאו את הפודקאסט שלכם לחיים](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | יצירת אודיו לפודקאסט | טקסט לדיבור • סינתזה עם דוברים מרובים • אודיו ארוך • אוטומציה מלאה | 2-3 שעות |

**טכנולוגיות בשימוש:**
- **מסגרת סוכני מיקרוסופט** - אורקסטרציה ותיאום סוכנים מרובים
- **אולמה** - סביבה להפעלת דגמי AI מקומיים (ללא צורך בענן)
- **Qwen-3-8B** - דגם שפה קוד פתוח מותאם למשימות סוכנויות
- **ממשקי API לטקסט לדיבור** - סינתוז קול טבעי ליצירת פודקאסטים

**תמיכת חומרה:**
- ✅ **מצב CPU** - עובד על כל מחשב מודרני (מומלץ 8GB+ RAM)
- 🚀 **האצת GPU** - אינפרנס מהיר באופן משמעותי עם GPUs של NVIDIA/AMD
- ⚡ **תמיכת NPU** - האצת יחידת עיבוד עצבי דור הבא

**מתאים במיוחד ל:**
- מפתחים הלומדים מערכות AI מרובות סוכנים
- כל המעוניין באוטומציה ומערכות עבודה מבוססות AI
- יוצרים החוקרים הפקה בסיוע AI
- סטודנטים הלומדים תבניות מעשיות של אורקסטרציה ב-AI

**התחילו לבנות**: [🎙️ סדנת אולפן הפודקאסטים ב-AI →](./WorkshopForAgentic/README.md)

### 📊 **סיכום מסלול הלמידה**
- **משך כולל**: 36-45 שעות
- **מסלול המתאים למתחילים**: מודולים 01-02 (7-9 שעות)  
- **מסלול ביניים**: מודולים 03-04 (9-11 שעות)
- **מסלול מתקדם**: מודולים 05-07 (12-15 שעות)
- **מסלול מומחים**: מודול 08 (8-10 שעות)

## מה תבנו

### 🎯 מיומנויות מרכזיות
- **ארכיטקטורת Edge AI**: עיצוב מערכות AI שמתחילות במכשיר המקומי עם אינטגרציה לענן
- **אופטימיזציה של מודלים**: כימות ודחיסת מודלים לפריסה על ה-edge (שיפור מהירות של 85%, הקטנת גודל ב-75%)
- **פריסה רב-פלטפורמית**: Windows, מובייל, מוטמע ומערכות היברידיות ענן-Edge
- **תפעול הפקה**: ניטור, קנה מידה ותחזוקה של Edge AI בפרודקשן

### 🏗️ פרויקטים מעשיים
- **אפליקציות צ'אט מקומיות Foundry**: אפליקציית Windows 11 עם החלפת דגמים
- **מערכות מרובות סוכנים**: מתאם עם סוכנים מומחים לתהליכים מורכבים  
- **אפליקציות RAG**: עיבוד מסמכים מקומי עם חיפוש וקטורי
- **מנתבים למודלים**: בחירה חכמה בין מודלים בהתבסס על ניתוח משימות
- **מסגרות API**: לקוחות מוכנים לפרודקשן עם סטרימינג וניטור בריאות
- **כלים רב-פלטפורמיים**: דפוסי אינטגרציה עם LangChain/Semantic Kernel

### 🏢 תחומי תעשייה
**ייצור** • **בריאות** • **רכבים אוטונומיים** • **ערים חכמות** • **אפליקציות מובייל**

## התחלה מהירה

**מסלול לימוד מומלץ** (20-30 שעות בסך הכל):

0. **📖 מבוא** ([Introduction.md](./introduction.md)): יסודות EdgeAI + הקשר תעשייתי + מסגרת למידה
1. **📚 יסודות** (מודולים 01-02): מושגים ב-EdgeAI + משפחות דגמי SLM
2. **⚙️ אופטימיזציה** (מודולים 03-04): פריסה + מסגרות כימות  
3. **🚀 פרודקשן** (מודולים 05-06): SLMOps + סוכני AI + קריאות לפונקציות
4. **💻 יישום** (מודולים 07-08): דגימות פלטפורמה + ערכת Foundry Local

כל מודול כולל תאוריה, תרגילים מעשיים ודוגמאות קוד מוכנות לפרודקשן.

## השפעה מקצועית

**תפקידים טכניים**: אדריכל פתרונות EdgeAI • מהנדס ML (Edge) • מפתח AI לאינטרנט של הדברים • מפתח AI מובייל

**ענפי תעשייה**: ייצור 4.0 • טכנולוגיות בריאות • מערכות אוטונומיות • FinTech • אלקטרוניקה לצרכן

**פרויקטים בפורטפוליו**: מערכות מרובות סוכנים • אפליקציות RAG לפרודקשן • פריסה רוחבית • אופטימיזציית ביצועים

## מבנה מאגר

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## נקודות מרכזיות בקורס

✅ **למידה הדרגתית**: תאוריה → פרקטיקה → פריסה בפרודקשן  
✅ **מקרי מבחן אמיתיים**: מיקרוסופט, Japan Airlines, יישומי ארגונים  
✅ **דוגמאות מעשיות**: 50+ דוגמאות, 10 הדגמות Foundry Local מקיפות  
✅ **מיקוד בביצועים**: שיפורי מהירות של 85%, הקטנת גודל ב-75%  
✅ **רב-פלטפורמי**: Windows, מובייל, מוטמע, היברידי ענן-Edge  
✅ **מוכן לפרודקשן**: ניטור, קנה מידה, אבטחה ומסגרות עמידה ברגולציה

📖 **[מדריך לימוד זמין](STUDY_GUIDE.md)**: מסלול לימוד מובנה של 20 שעות עם הנחיות לחלוקת זמן וכלי הערכה עצמית.

---

**EdgeAI מייצג את עתיד פריסת ה-AI**: תחילה מקומית, שומר על פרטיות ויעיל. שלט במיומנויות אלו כדי לבנות את הדור הבא של יישומים אינטיליגנטיים.

## קורסים נוספים

הצוות שלנו מייצר קורסים נוספים! בדקו:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j למתחילים](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js למתחילים](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain למתחילים](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / סוכנים
[![AZD למתחילים](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI למתחילים](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP למתחילים](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![סוכני AI למתחילים](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת AI מחולל
[![AI מחולל למתחילים](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI מחולל (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![AI מחולל (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![AI מחולל (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### למידה בסיסית
[![ML למתחילים](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science למתחילים](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI למתחילים](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity למתחילים](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev למתחילים](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT למתחילים](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development למתחילים](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## לקבלת עזרה

אם נתקעת או יש לך שאלות לגבי בניית אפליקציות AI, הצטרף ל:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

אם יש לך משוב על המוצר או שגיאות במהלך הבנייה, בקר ב:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש להביא בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור נחשב למקור הרשמי והמהימן. למידע קריטי מומלץ להיעזר בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל טעות או אי-הבנה שנובעים מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->