# מדריך אינטגרציה בין Open WebUI ל-Foundry Local

מדריך זה מסביר כיצד לחבר את Open WebUI ל-Microsoft Foundry Local כדי ליצור ממשק מקצועי בסגנון ChatGPT המבוסס על מודלים AI מקומיים.

## סקירה כללית

Open WebUI מספק ממשק צ'אט מודרני וידידותי למשתמש שיכול להתחבר לכל API תואם OpenAI. על ידי חיבורו ל-Foundry Local, תוכלו ליהנות מ:

- **ממשק מקצועי**: ממשק בסגנון ChatGPT עם עיצוב מודרני
- **פרטיות מקומית**: כל העיבוד מתבצע במכשיר שלכם
- **מעבר בין מודלים**: מעבר קל בין מודלים מקומיים שונים
- **היסטוריית שיחות**: שמירת היסטוריית שיחות והקשר
- **העלאת קבצים**: ניתוח מסמכים ועיבוד קבצים
- **פרסונות מותאמות אישית**: התאמת הנחיות מערכת ותפקידים

## דרישות מקדימות

### תוכנה נדרשת

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### טעינת מודל

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## התקנה מהירה (מומלץ)

### שלב 1: הפעלת Open WebUI עם Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### שלב 2: הגדרה ראשונית

1. **פתחו את הדפדפן**: נווטו ל-`http://localhost:3000`
2. **צרו חשבון**: הגדירו משתמש מנהל (המשתמש הראשון הופך למנהל)
3. **אמתו את החיבור**: המודלים אמורים להופיע בתפריט הנפתח באופן אוטומטי

### שלב 3: בדיקת החיבור

1. בחרו את המודל שלכם מהתפריט הנפתח (לדוגמה, "phi-4-mini")
2. הקלידו הודעת בדיקה: "שלום! תוכל להציג את עצמך?"
3. אתם אמורים לראות תגובה זורמת מהמודל המקומי שלכם

## הגדרות מתקדמות

### משתני סביבה

| משתנה | מטרה | ברירת מחדל | דוגמה |
|-------|------|------------|-------|
| `OPENAI_API_BASE_URL` | נקודת הקצה של Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | מפתח API (נדרש אך לא בשימוש מקומי) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | מפתח הצפנת סשן | נוצר אוטומטית | `your-secret-key` |
| `ENABLE_SIGNUP` | אפשרות הרשמה למשתמשים חדשים | `True` | `False` |

### הגדרה ידנית (חלופה)

אם משתני הסביבה לא עובדים, ניתן להגדיר ידנית:

1. **פתחו את ההגדרות**: לחצו על סמל ההגדרות (גלגל שיניים)
2. **נווטו לחיבורים**: הגדרות → חיבורים → OpenAI
3. **הגדירו פרטי API**:
   - כתובת בסיס API: `http://host.docker.internal:51211/v1`
   - מפתח API: `foundry-local-key` (כל ערך יעבוד)
4. **שמרו ובדקו**: לחצו על "שמור" ואז בדקו עם מודל

### אחסון נתונים מתמשך

כדי לשמור שיחות והגדרות:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## פתרון בעיות

### בעיות חיבור

**בעיה**: "Connection refused" או שהמודלים לא נטענים

**פתרונות**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### מודל לא מופיע

**בעיה**: Open WebUI לא מציג מודלים בתפריט הנפתח

**שלבי דיבוג**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**תיקון**: ודאו שהמודל נטען כראוי:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### בעיות רשת עם Docker

**בעיה**: `host.docker.internal` לא נפתר

**פתרון ל-Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**חלופה**: מצאו את כתובת ה-IP של המחשב שלכם:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### בעיות ביצועים

**תגובות איטיות**:
1. בדקו שהמודל משתמש בהאצת GPU: `foundry service ps`
2. ודאו שיש מספיק משאבי מערכת (RAM/זיכרון GPU)
3. שקלו להשתמש במודל קטן יותר לבדיקה

**בעיות זיכרון**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## מדריך שימוש

### צ'אט בסיסי

1. **בחרו מודל**: בחרו מהתפריט הנפתח (מציג מודלים של Foundry Local)
2. **הקלידו הודעה**: השתמשו בשדה הטקסט בתחתית
3. **שלחו**: לחצו Enter או על כפתור השליחה
4. **צפו בתגובה**: ראו תגובה זורמת בזמן אמת

### תכונות מתקדמות

**העלאת קבצים**:
1. לחצו על סמל אטב הנייר
2. העלו מסמך (PDF, TXT וכו')
3. שאלו שאלות על התוכן
4. המודל ינתח ויגיב בהתאם למסמך

**הנחיות מערכת מותאמות אישית**:
1. הגדרות → התאמה אישית
2. הגדירו הנחיית מערכת מותאמת אישית
3. יוצרת אישיות/התנהגות עקבית ל-AI

**ניהול שיחות**:
- **שיחה חדשה**: לחצו על "+" כדי להתחיל שיחה חדשה
- **היסטוריית שיחות**: גשו לשיחות קודמות מהסרגל הצדדי
- **ייצוא**: הורידו את היסטוריית השיחות כטקסט/JSON

**השוואת מודלים**:
1. פתחו מספר טאבים בדפדפן ל-Open WebUI
2. בחרו מודלים שונים בכל טאב
3. השוו תגובות לאותן הנחיות

### דפוסי אינטגרציה

**תהליך פיתוח**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## פריסה בסביבת ייצור

### הגדרה מאובטחת

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### הגדרה מרובת משתמשים

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### ניטור ורישום

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ניקוי

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## צעדים הבאים

### רעיונות לשיפור

1. **מודלים מותאמים אישית**: הוסיפו מודלים מותאמים אישית ל-Foundry Local
2. **אינטגרציית API**: התחברו ל-APIs חיצוניים באמצעות פונקציות Open WebUI
3. **עיבוד מסמכים**: הגדירו צינורות RAG מתקדמים
4. **רב-מודאלי**: הגדירו מודלים חזותיים לניתוח תמונות

### שיקולי סקיילינג

- **איזון עומסים**: מספר מופעים של Foundry Local מאחורי פרוקסי הפוך
- **ניתוב מודלים**: מודלים שונים לשימושים שונים
- **ניהול משאבים**: אופטימיזציית זיכרון GPU למשתמשים מקבילים
- **אסטרטגיית גיבוי**: גיבוי קבוע של נתוני שיחות והגדרות

## מקורות

- [תיעוד Open WebUI](https://docs.openwebui.com/)
- [מאגר GitHub של Open WebUI](https://github.com/open-webui/open-webui)
- [תיעוד Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [מדריך התקנת Docker](https://docs.docker.com/get-docker/)

---

