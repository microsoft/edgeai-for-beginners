# פרק 07: דוגמאות ל-EdgeAI

Edge AI מייצג את המפגש בין בינה מלאכותית למחשוב בקצה, ומאפשר עיבוד חכם ישירות על גבי מכשירים ללא תלות בחיבור לענן. פרק זה מציג חמישה יישומים שונים של EdgeAI בפלטפורמות ובמסגרות שונות, המדגימים את הגמישות והעוצמה של הרצת מודלים של AI בקצה.

## 1. EdgeAI ב-NVIDIA Jetson Orin Nano

ה-NVIDIA Jetson Orin Nano מייצג פריצת דרך במחשוב Edge AI נגיש, ומספק עד 67 TOPS של ביצועי AI בגודל קומפקטי, בגודל של כרטיס אשראי. פלטפורמת Edge AI עוצמתית זו מנגישה את פיתוח ה-AI הגנרטיבי לחובבים, סטודנטים ומפתחים מקצועיים כאחד.

### תכונות עיקריות
- מספק עד 67 TOPS של ביצועי AI—שיפור של פי 1.7 לעומת הדור הקודם
- 1024 ליבות CUDA ועד 32 ליבות Tensor לעיבוד AI
- מעבד 6 ליבות Arm Cortex-A78AE v8.2 64-bit עם תדר מקסימלי של 1.5 GHz
- מחיר של $249 בלבד, מה שהופך אותו לפלטפורמה נגישה ומשתלמת למפתחים, סטודנטים ויוצרים

### יישומים
ה-Jetson Orin Nano מצטיין בהרצת מודלים גנרטיביים מודרניים, כולל Vision Transformers, מודלים של שפה גדולה (LLMs) ומודלים של Vision-Language. הוא תוכנן במיוחד עבור מקרי שימוש של GenAI, וכעת ניתן להריץ מספר LLMs על מכשיר בגודל כף יד. מקרי שימוש פופולריים כוללים רובוטיקה מבוססת AI, רחפנים חכמים, מצלמות אינטליגנטיות ומכשירים אוטונומיים בקצה.

**למידע נוסף**: [Jetson Orin Nano SuperComputer של NVIDIA: הדבר הגדול הבא ב-EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI באפליקציות מובייל עם .NET MAUI ו-ONNX Runtime GenAI

פתרון זה מדגים כיצד לשלב AI גנרטיבי ומודלים של שפה גדולה (LLMs) באפליקציות מובייל חוצות פלטפורמות באמצעות .NET MAUI (Multi-platform App UI) ו-ONNX Runtime GenAI. גישה זו מאפשרת למפתחי .NET לבנות אפליקציות מובייל מתקדמות מבוססות AI שרצות באופן טבעי על מכשירי Android ו-iOS.

### תכונות עיקריות
- מבוסס על מסגרת .NET MAUI, המספקת בסיס קוד יחיד לאפליקציות Android ו-iOS
- אינטגרציה של ONNX Runtime GenAI מאפשרת הרצת מודלים גנרטיביים ישירות על מכשירי מובייל
- תומך במאיצי חומרה שונים המותאמים למכשירי מובייל, כולל CPU, GPU ומעבדי AI ייעודיים
- אופטימיזציות ייחודיות לפלטפורמות כמו CoreML ל-iOS ו-NNAPI ל-Android באמצעות ONNX Runtime
- מיישם את כל הלולאה של AI גנרטיבי, כולל עיבוד מקדים ואחר, הסקה, עיבוד לוגיטים, חיפוש ודגימה, וניהול KV Cache

### יתרונות הפיתוח
שיטת .NET MAUI מאפשרת למפתחים לנצל את כישורי ה-C# וה-.NET הקיימים שלהם תוך בניית אפליקציות AI חוצות פלטפורמות. מסגרת ONNX Runtime GenAI תומכת בארכיטקטורות מודלים רבות, כולל Llama, Mistral, Phi, Gemma ועוד. ליבות ARM64 מותאמות מאיצות כפל מטריצות INT4, ומבטיחות ביצועים יעילים על חומרת מובייל תוך שמירה על חוויית פיתוח מוכרת ב-.NET.

### מקרי שימוש
פתרון זה אידיאלי למפתחים המעוניינים לבנות אפליקציות מובייל מבוססות AI באמצעות טכנולוגיות .NET, כולל צ'אטבוטים חכמים, אפליקציות לזיהוי תמונות, כלים לתרגום שפות ומערכות המלצה מותאמות אישית שפועלות לחלוטין על המכשיר לשיפור הפרטיות ויכולת עבודה במצב לא מקוון.

**למידע נוסף**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI ב-Azure עם מנוע Small Language Models

פתרון EdgeAI מבוסס Azure של מיקרוסופט מתמקד בפריסה יעילה של Small Language Models (SLMs) בסביבות היברידיות של ענן-קצה. גישה זו מגשרת על הפער בין שירותי AI בקנה מידה ענני לדרישות פריסה בקצה.

### יתרונות הארכיטקטורה
- אינטגרציה חלקה עם שירותי Azure AI
- הרצת SLMs/LLMs ומודלים מולטי-מודליים על המכשיר ובענן באמצעות ONNX Runtime
- מותאם לפריסה בקנה מידה ארגוני
- תמיכה בעדכונים וניהול מתמשכים של מודלים

### מקרי שימוש
היישום של Azure EdgeAI מצטיין בתרחישים הדורשים פריסת AI ברמה ארגונית עם יכולות ניהול ענן. זה כולל עיבוד מסמכים חכם, ניתוח בזמן אמת וזרימות עבודה היברידיות של AI המנצלות משאבי מחשוב בענן ובקצה.

**למידע נוסף**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI עם Windows ML](./windowdeveloper.md)

Windows ML מייצג את סביבת הריצה המתקדמת של מיקרוסופט, המותאמת להסקת מודלים על המכשיר ולפריסה פשוטה, ומהווה את הבסיס ל-Windows AI Foundry. פלטפורמה זו מאפשרת למפתחים ליצור אפליקציות Windows מבוססות AI המנצלות את מלוא הפוטנציאל של חומרת המחשב האישי.

### יכולות הפלטפורמה
- פועל על כל מחשבי Windows 11 עם גרסה 24H2 (build 26100) או יותר
- תומך בכל חומרת PC x64 ו-ARM64, כולל מחשבים ללא NPUs או GPUs
- מאפשר למפתחים להביא מודלים משלהם ולפרוס אותם ביעילות על פני אקוסיסטם השותפים של הסיליקון, כולל AMD, Intel, NVIDIA ו-Qualcomm
- באמצעות APIs של תשתית, מפתחים אינם צריכים ליצור גרסאות מרובות של האפליקציה שלהם כדי להתאים לחומרות שונות

### יתרונות למפתחים
Windows ML מפשט את העבודה עם חומרה וספקי ביצוע, כך שתוכלו להתמקד בכתיבת הקוד שלכם. בנוסף, Windows ML מתעדכן אוטומטית לתמוך ב-NPUs, GPUs ו-CPUs החדשים ביותר עם שחרורם. הפלטפורמה מספקת מסגרת אחידה לפיתוח AI על פני האקוסיסטם המגוון של חומרת Windows.

**למידע נוסף**: 
- [סקירה כללית של Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [מדריך פיתוח Windows EdgeAI](./windowdeveloper.md) - מדריך מקיף לפיתוח Edge AI ב-Windows

## [5. EdgeAI עם Foundry Local Applications](./foundrylocal.md)

Foundry Local מאפשר למפתחים ב-Windows וב-Mac לבנות אפליקציות RAG (Retrieval Augmented Generation) באמצעות משאבים מקומיים ב-.NET, ומשלב מודלים של שפה מקומית עם יכולות חיפוש סמנטי. גישה זו מספקת פתרונות AI ממוקדי פרטיות שפועלים לחלוטין על תשתית מקומית.

### ארכיטקטורה טכנית
- משלב את מודל השפה Phi, Local Embeddings ו-Semantic Kernel ליצירת תרחיש RAG
- משתמש ב-embeddings כווקטורים (מערכים) של ערכים עשרוניים המייצגים תוכן ומשמעות סמנטית
- ה-Semantic Kernel משמש כאורקסטרטור הראשי, ומשלב את Phi ורכיבים חכמים ליצירת צינור RAG חלק
- תמיכה במסדי נתונים ווקטוריים מקומיים, כולל SQLite ו-Qdrant

### יתרונות היישום
RAG, או Retrieval Augmented Generation, הוא פשוט דרך מתוחכמת לומר "חפש מידע והכנס אותו להנחיה". יישום מקומי זה מבטיח פרטיות נתונים תוך מתן תגובות חכמות המבוססות על מאגרי ידע מותאמים אישית. הגישה חשובה במיוחד לתרחישים ארגוניים הדורשים ריבונות נתונים ויכולת פעולה במצב לא מקוון.

**למידע נוסף**: 
- [Foundry Local](./foundrylocal.md)
- [דוגמאות RAG של Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Foundry Local ב-Windows

Microsoft Foundry Local מספק שרת REST תואם OpenAI המופעל על ידי ONNX Runtime להרצת מודלים באופן מקומי על Windows. להלן סיכום מהיר ומאומת; עיינו בתיעוד הרשמי לפרטים מלאים.

- התחלה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ארכיטקטורה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- עיון ב-CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- מדריך Windows מלא במאגר זה: [foundrylocal.md](./foundrylocal.md)

התקנה או שדרוג ב-Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

חקירת קטגוריות CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

הרצת מודל וגילוי נקודת קצה דינמית:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

בדיקת REST מהירה לרשימת מודלים (החלף PORT מסטטוס):
```cmd
curl -s http://localhost:PORT/v1/models
```

טיפים:
- אינטגרציה עם SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- הבאת מודל משלך (קומפילציה): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## משאבי פיתוח EdgeAI ב-Windows

עבור מפתחים הממוקדים בפלטפורמת Windows, יצרנו מדריך מקיף המכסה את כל אקוסיסטם ה-EdgeAI של Windows. משאב זה מספק מידע מפורט על Windows AI Foundry, כולל APIs, כלים ושיטות עבודה מומלצות לפיתוח EdgeAI ב-Windows.

### פלטפורמת Windows AI Foundry
פלטפורמת Windows AI Foundry מספקת מערך כלים ו-APIs מקיף המיועד במיוחד לפיתוח Edge AI על מכשירי Windows. זה כולל תמיכה מיוחדת בחומרה מואצת NPU, אינטגרציה של Windows ML וטכניקות אופטימיזציה ייחודיות לפלטפורמה.

**מדריך מקיף**: [מדריך פיתוח Windows EdgeAI](../windowdeveloper.md)

מדריך זה מכסה:
- סקירה כללית של פלטפורמת Windows AI Foundry ורכיביה
- Phi Silica API להסקה יעילה על חומרת NPU
- APIs לעיבוד תמונה ו-OCR
- אינטגרציה ואופטימיזציה של Windows ML runtime
- CLI של Foundry Local לפיתוח ובדיקה מקומיים
- אסטרטגיות אופטימיזציה לחומרת Windows
- דוגמאות יישום מעשיות ושיטות עבודה מומלצות

### [ערכת כלים ל-AI לפיתוח Edge AI](./aitoolkit.md)
עבור מפתחים המשתמשים ב-Visual Studio Code, תוסף AI Toolkit מספק סביבת פיתוח מקיפה המיועדת במיוחד לבנייה, בדיקה ופריסה של אפליקציות Edge AI. ערכת כלים זו מפשטת את כל זרימת העבודה של פיתוח Edge AI בתוך VS Code.

**מדריך פיתוח**: [ערכת כלים ל-AI לפיתוח Edge AI](./aitoolkit.md)

מדריך ערכת הכלים מכסה:
- גילוי ובחירת מודלים לפריסה בקצה
- בדיקות ואופטימיזציות מקומיות
- אינטגרציה של ONNX ו-Ollama למודלים בקצה
- טכניקות המרה וכימות מודלים
- פיתוח סוכנים לתרחישי קצה
- הערכת ביצועים וניטור
- הכנה לפריסה ושיטות עבודה מומלצות

## סיכום

חמשת היישומים של EdgeAI הללו מדגימים את הבשלות והמגוון של פתרונות Edge AI הזמינים כיום. ממכשירי קצה מואצים בחומרה כמו Jetson Orin Nano ועד מסגרות תוכנה כמו ONNX Runtime GenAI ו-Windows ML, למפתחים יש אפשרויות חסרות תקדים לפריסת אפליקציות חכמות בקצה.

החוט המקשר בין כל הפלטפורמות הללו הוא הנגשת יכולות AI, מה שהופך למידת מכונה מתקדמת לנגישה למפתחים ברמות מיומנות ושימושים שונים. בין אם מדובר בבניית אפליקציות מובייל, תוכנות שולחן עבודה או מערכות משובצות, פתרונות EdgeAI הללו מספקים את הבסיס לדור הבא של אפליקציות חכמות שפועלות ביעילות ובפרטיות בקצה.

כל פלטפורמה מציעה יתרונות ייחודיים: Jetson Orin Nano למחשוב קצה מואץ בחומרה, ONNX Runtime GenAI לפיתוח מובייל חוצה פלטפורמות, Azure EdgeAI לאינטגרציה ארגונית של ענן-קצה, Windows ML לאפליקציות מקוריות ב-Windows, ו-Foundry Local ליישומי RAG ממוקדי פרטיות. יחד, הן מייצגות אקוסיסטם מקיף לפיתוח EdgeAI.

[ערכת הכלים הבאה ל-AI](aitoolkit.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.