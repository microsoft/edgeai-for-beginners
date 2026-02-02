# דוגמה למפגש 6: מודלים ככלים

הדוגמה הזו מיישמת רישום כלים מינימלי + נתב שמבחר מודל על בסיס בקשת המשתמש ומבצע קריאה לנקודת הקצה של Foundry Local התואמת ל-OpenAI.

## קבצים
- `router.py`: רישום פשוט וניתוב לפי היגיון; גילוי נקודת קצה + בדיקת בריאות.

## הפעלה (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## הערות
- הנתב משתמש בהיגיון פשוט המבוסס על מילות מפתח כדי לבחור בין כלים `general`, `reasoning`, ו-`code`, ומדפיס `/v1/models` בעת ההפעלה.
- ניתן להגדיר באמצעות משתני סביבה:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## מקורות
- Foundry Local (לימוד): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- אינטגרציה עם SDKs להסקה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או פירושים שגויים הנובעים משימוש בתרגום זה.