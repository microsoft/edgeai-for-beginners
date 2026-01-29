# דוגמה 04: אפליקציות צ'אט לייצור עם Chainlit

דוגמה מקיפה המציגה גישות שונות לבניית אפליקציות צ'אט מוכנות לייצור באמצעות Microsoft Foundry Local, עם ממשקי אינטרנט מודרניים, תגובות זורמות וטכנולוגיות דפדפן מתקדמות.

## מה כלול

- **🚀 אפליקציית צ'אט Chainlit** (`app.py`): אפליקציית צ'אט מוכנה לייצור עם תגובות זורמות
- **🌐 הדגמת WebGPU** (`webgpu-demo/`): הסקת AI מבוססת דפדפן עם האצת חומרה
- **🎨 אינטגרציה עם Open WebUI** (`open-webui-guide.md`): ממשק מקצועי בסגנון ChatGPT
- **📚 מחברת לימודית** (`chainlit_app.ipynb`): חומרי לימוד אינטראקטיביים

## התחלה מהירה

### 1. אפליקציית צ'אט Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

נפתח בכתובת: `http://localhost:8080`

### 2. הדגמת WebGPU בדפדפן

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

נפתח בכתובת: `http://localhost:5173`

### 3. הגדרת Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

נפתח בכתובת: `http://localhost:3000`

## דפוסי ארכיטקטורה

### מטריצת החלטות: מקומי מול ענן

| תרחיש | המלצה | סיבה |
|-------|--------|------|
| **נתונים רגישים לפרטיות** | 🏠 מקומי (Foundry) | הנתונים נשארים במכשיר |
| **הסקה מורכבת** | ☁️ ענן (Azure OpenAI) | גישה למודלים גדולים יותר |
| **צ'אט בזמן אמת** | 🏠 מקומי (Foundry) | זמן תגובה נמוך יותר, תגובות מהירות |
| **ניתוח מסמכים** | 🔄 היברידי | מקומי לחילוץ, ענן לניתוח |
| **יצירת קוד** | 🏠 מקומי (Foundry) | פרטיות + מודלים מותאמים |
| **משימות מחקר** | ☁️ ענן (Azure OpenAI) | נדרש בסיס ידע רחב |

### השוואת טכנולוגיות

| טכנולוגיה | שימוש | יתרונות | חסרונות |
|-----------|-------|---------|---------|
| **Chainlit** | מפתחים ב-Python, אב טיפוס מהיר | התקנה קלה, תמיכה בתגובות זורמות | מוגבל ל-Python |
| **WebGPU** | פרטיות מרבית, תרחישים לא מקוונים | מובנה בדפדפן, ללא צורך בשרת | גודל מודל מוגבל |
| **Open WebUI** | פריסה לייצור, צוותים | ממשק מקצועי, ניהול משתמשים | דורש Docker |

## דרישות מקדימות

- **Foundry Local**: מותקן ופועל ([הורדה](https://aka.ms/foundry-local-installer))
- **Python**: גרסה 3.10+ עם סביבה וירטואלית
- **מודל**: לפחות אחד טעון (`foundry model run phi-4-mini`)
- **דפדפן**: Chrome/Edge עם תמיכה ב-WebGPU להדגמות
- **Docker**: עבור Open WebUI (אופציונלי)

## התקנה והגדרה

### 1. הגדרת סביבה ב-Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. הגדרת Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## אפליקציות לדוגמה

### אפליקציית צ'אט Chainlit

**תכונות:**
- 🚀 **תגובות בזמן אמת**: טוקנים מופיעים בזמן יצירתם
- 🛡️ **טיפול שגיאות חזק**: התמודדות והתאוששות בצורה חלקה
- 🎨 **ממשק מודרני**: ממשק צ'אט מקצועי מוכן לשימוש
- 🔧 **תצורה גמישה**: משתני סביבה וזיהוי אוטומטי
- 📱 **עיצוב רספונסיבי**: עובד על מחשבים שולחניים ומכשירים ניידים

**התחלה מהירה:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### הדגמת WebGPU בדפדפן

**תכונות:**
- 🌐 **AI מובנה בדפדפן**: ללא צורך בשרת, פועל כולו בדפדפן
- ⚡ **האצת WebGPU**: האצת חומרה כאשר זמינה
- 🔒 **פרטיות מרבית**: הנתונים לעולם לא עוזבים את המכשיר שלך
- 🎯 **ללא התקנה**: עובד בכל דפדפן תואם
- 🔄 **התמודדות חלקה**: נופל ל-CPU אם WebGPU אינו זמין

**הפעלה:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### אינטגרציה עם Open WebUI

**תכונות:**
- 🎨 **ממשק בסגנון ChatGPT**: ממשק מקצועי ומוכר
- 👥 **תמיכה בריבוי משתמשים**: חשבונות משתמשים והיסטוריית שיחות
- 📁 **עיבוד קבצים**: העלאה וניתוח מסמכים
- 🔄 **מעבר בין מודלים**: מעבר קל בין מודלים שונים
- 🐳 **פריסה עם Docker**: הגדרה מוכנה לייצור במיכלים

**הגדרה מהירה:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## הפניה להגדרות

### משתני סביבה

| משתנה | תיאור | ברירת מחדל | דוגמה |
|-------|-------|------------|-------|
| `MODEL` | כינוי המודל לשימוש | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | נקודת קצה של Foundry Local | זיהוי אוטומטי | `http://localhost:51211` |
| `API_KEY` | מפתח API (אופציונלי למקומי) | `""` | `your-api-key` |

## פתרון בעיות

### בעיות נפוצות

**אפליקציית Chainlit:**

1. **שירות לא זמין:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **התנגשויות פורטים:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **בעיות בסביבת Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**הדגמת WebGPU:**

1. **WebGPU לא נתמך:**
   - עדכון ל-Chrome/Edge גרסה 113+
   - הפעלת WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - בדיקת מצב GPU: `chrome://gpu`
   - ההדגמה תעבור אוטומטית ל-CPU

2. **שגיאות טעינת מודל:**
   - ודא חיבור לאינטרנט להורדת מודלים
   - בדוק את קונסולת הדפדפן לשגיאות CORS
   - ודא שאתה משרת דרך HTTP (לא file://)

**Open WebUI:**

1. **חיבור נדחה:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **מודלים לא מופיעים:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### רשימת בדיקות אימות

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## שימוש מתקדם

### אופטימיזציית ביצועים

**Chainlit:**
- השתמש בתגובות זורמות לשיפור תחושת הביצועים
- יישם pooling חיבורים לתמיכה בריבוי משתמשים
- אחסן תגובות מודל לשאילתות חוזרות
- עקוב אחר שימוש בזיכרון עם היסטוריות שיחה גדולות

**WebGPU:**
- השתמש ב-WebGPU לפרטיות ומהירות מרבית
- יישם כימות מודלים למודלים קטנים יותר
- השתמש ב-Web Workers לעיבוד ברקע
- אחסן מודלים מקומפלים באחסון הדפדפן

**Open WebUI:**
- השתמש בנפחים מתמשכים להיסטוריית שיחות
- הגדר מגבלות משאבים למיכל Docker
- יישם אסטרטגיות גיבוי לנתוני משתמשים
- הגדר פרוקסי הפוך לסיום SSL

### דפוסי אינטגרציה

**היברידי מקומי/ענן:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**צינור רב-מודלי:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## פריסה לייצור

### שיקולי אבטחה

- **מפתחות API**: השתמש במשתני סביבה, לעולם אל תכתוב בקוד
- **רשת**: השתמש ב-HTTPS בייצור, שקול VPN לגישה צוותית
- **בקרת גישה**: יישם אימות עבור Open WebUI
- **פרטיות נתונים**: בדוק אילו נתונים נשארים מקומיים ואילו עוברים לענן
- **עדכונים**: שמור את Foundry Local והמיכלים מעודכנים

### ניטור ותחזוקה

- **בדיקות בריאות**: יישם ניטור נקודות קצה
- **רישום**: רכז לוגים מכל הרכיבים
- **מדדים**: עקוב אחר זמני תגובה, שיעורי שגיאות ושימוש במשאבים
- **גיבוי**: גיבוי קבוע של נתוני שיחות והגדרות

## הפניות ומשאבים

### תיעוד
- [תיעוד Chainlit](https://docs.chainlit.io/) - מדריך מלא למסגרת
- [תיעוד Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - תיעוד רשמי של Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - אינטגרציית WebGPU
- [תיעוד Open WebUI](https://docs.openwebui.com/) - הגדרות מתקדמות

### קבצים לדוגמה
- [`app.py`](../../../../../Module08/samples/04/app.py) - אפליקציית Chainlit לייצור
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - מחברת לימודית
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - הסקת AI מבוססת דפדפן
- [`open-webui-guide.md`](./open-webui-guide.md) - הגדרת Open WebUI מלאה

### דוגמאות קשורות
- [תיעוד מושב 4](../../04.CuttingEdgeModels.md) - מדריך מושב מלא
- [דוגמאות Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - דוגמאות רשמיות

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.