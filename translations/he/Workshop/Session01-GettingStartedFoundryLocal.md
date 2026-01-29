# מפגש 1: התחלת עבודה עם Foundry Local

## תקציר

למדו כיצד להתקין, להגדיר ולהפעיל את מודלי הבינה המלאכותית הראשונים שלכם באמצעות Microsoft Foundry Local. מפגש מעשי זה מספק הדרכה שלב אחר שלב על הסקת מסקנות מקומית, החל מהתקנה ועד לבניית אפליקציית צ'אט ראשונה באמצעות מודלים כמו Phi-4, Qwen ו-DeepSeek.

## מטרות למידה

בסיום המפגש, תוכלו:

- **להתקין ולהגדיר**: להגדיר את Foundry Local עם אימות התקנה נכון
- **לשלוט בפעולות CLI**: להשתמש ב-CLI של Foundry Local לניהול והפעלת מודלים
- **להפעיל מודל ראשון**: לפרוס ולהפעיל מודל AI מקומי בהצלחה
- **לבנות אפליקציית צ'אט**: ליצור אפליקציית צ'אט בסיסית באמצעות Foundry Local Python SDK
- **להבין AI מקומי**: להבין את יסודות ההסקה המקומית וניהול המודלים

## דרישות מקדימות

### דרישות מערכת

- **Windows**: Windows 11 (22H2 או גרסה מאוחרת יותר) או **macOS**: macOS 11+ (תמיכה מוגבלת)
- **RAM**: מינימום 8GB, מומלץ 16GB+
- **אחסון**: לפחות 10GB פנויים עבור מודלים
- **Python**: גרסה 3.10 או מאוחרת יותר מותקנת
- **גישה מנהלית**: הרשאות מנהל להתקנה

### סביבת פיתוח

- Visual Studio Code עם הרחבת Python (מומלץ)
- גישה לשורת הפקודה (PowerShell ב-Windows, Terminal ב-macOS)
- Git לשכפול מאגרים (אופציונלי)

## מהלך הסדנה (30 דקות)

### שלב 1: התקנת Foundry Local (5 דקות)

#### התקנה ב-Windows

התקינו את Foundry Local באמצעות מנהל החבילות של Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

חלופה: הורידו ישירות מ-[Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### התקנה ב-macOS (תמיכה מוגבלת)

> [!NOTE] 
> תמיכה ב-macOS נמצאת כרגע בתצוגה מקדימה. בדקו את התיעוד הרשמי למידע עדכני.

אם זמין, התקינו באמצעות Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**חלופה למשתמשי macOS:**
- השתמשו ב-VM של Windows 11 (Parallels/UTM) ועקבו אחר השלבים של Windows
- הפעלו דרך קונטיינר אם זמין והגדירו `FOUNDRY_LOCAL_ENDPOINT`

### שלב 2: אימות התקנה (3 דקות)

לאחר ההתקנה, הפעילו מחדש את שורת הפקודה ואמתו ש-Foundry Local פועל:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

התוצאה הצפויה צריכה להציג מידע על גרסה ופקודות זמינות.

### שלב 3: הגדרת סביבת Python (5 דקות)

צרו סביבת Python ייעודית לסדנה זו:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### שלב 4: הפעלת מודל ראשון (7 דקות)

כעת נפעיל את מודל הבינה המלאכותית הראשון שלנו באופן מקומי!

#### התחילו עם Phi-4 Mini (מודל מומלץ ראשון)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> פקודה זו מורידה את המודל (בפעם הראשונה) ומתחילה את שירות Foundry Local באופן אוטומטי.

#### בדקו מה פועל

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### נסו מודלים שונים

לאחר ש-phi-4-mini פועל, נסו מודלים אחרים:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### שלב 5: בניית אפליקציית צ'אט ראשונה (10 דקות)

כעת ניצור אפליקציית Python שמשתמשת במודלים שהפעלנו.

#### יצירת סקריפט הצ'אט

צרו קובץ חדש בשם `my_first_chat.py` (או השתמשו בדוגמה שסופקה):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **דוגמאות קשורות**: לשימוש מתקדם יותר, ראו:
>
> - **דוגמת Python**: `Workshop/samples/session01/chat_bootstrap.py` - כולל תגובות סטרימינג וטיפול בשגיאות
> - **מחברת Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - גרסה אינטראקטיבית עם הסברים מפורטים

#### בדיקת אפליקציית הצ'אט שלכם

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

חלופה: השתמשו בדוגמאות שסופקו ישירות

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

או חקרו את המחברת האינטראקטיבית
פתחו Workshop/notebooks/session01_chat_bootstrap.ipynb ב-VS Code

נסו את השיחות לדוגמה הבאות:

- "מה זה Microsoft Foundry Local?"
- "ציין 3 יתרונות של הפעלת מודלי AI באופן מקומי"
- "עזור לי להבין AI בקצה"

## מה השגתם

ברכות! הצלחתם:

1. ✅ **להתקין את Foundry Local** ולאמת שהוא פועל
2. ✅ **להפעיל מודל AI ראשון** (phi-4-mini) באופן מקומי
3. ✅ **לבדוק מודלים שונים** דרך שורת הפקודה
4. ✅ **לבנות אפליקציית צ'אט** שמתחברת ל-AI המקומי שלכם
5. ✅ **לחוות הסקת מסקנות AI מקומית** ללא תלות בענן

## הבנת מה שקרה

### הסקת מסקנות AI מקומית

- מודלי הבינה המלאכותית שלכם פועלים לחלוטין על המחשב שלכם
- אין נתונים שנשלחים לענן
- תגובות נוצרות באופן מקומי באמצעות CPU/GPU שלכם
- פרטיות ואבטחה נשמרות

### ניהול מודלים

- `foundry model run` מוריד ומפעיל מודלים
- **FoundryLocalManager SDK** מטפל אוטומטית בהפעלת השירות וטעינת המודלים
- מודלים נשמרים במטמון באופן מקומי לשימוש עתידי
- ניתן להוריד מספר מודלים אך בדרך כלל רק אחד פועל בכל פעם
- השירות מנהל אוטומטית את מחזור החיים של המודל

### גישות SDK לעומת CLI

- **גישה CLI**: ניהול מודלים ידני עם `foundry model run <model>`
- **גישה SDK**: שירות אוטומטי + ניהול מודלים עם `FoundryLocalManager(alias)`
- **המלצה**: השתמשו ב-SDK לאפליקציות, ב-CLI לבדיקות וחקר

## הפניות לפקודות נפוצות

### פקודות CLI חיוניות

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### המלצות מודלים

- **phi-4-mini**: מודל התחלה הטוב ביותר - מהיר, קל משקל, איכות טובה
- **qwen2.5-0.5b**: הסקה מהירה ביותר, שימוש מינימלי בזיכרון
- **gpt-oss-20b**: תגובות איכותיות יותר, דורש יותר משאבים
- **deepseek-coder-1.3b**: מותאם למשימות תכנות וקוד

## פתרון בעיות

### "פקודת Foundry לא נמצאה"

**פתרון:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "המודל נכשל בטעינה"

**פתרון:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "חיבור נדחה ב-localhost"

**פתרון:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## צעדים הבאים

### פעולות מיידיות

1. **נסו** מודלים והנחיות שונים
2. **שנו** את אפליקציית הצ'אט שלכם כדי לנסות מודלים שונים
3. **צרו** הנחיות משלכם ובדקו תגובות
4. **חקרו** את מפגש 2: בניית אפליקציות RAG

### מסלול למידה מתקדם

1. **מפגש 2**: בניית פתרונות AI עם RAG (הפקת מידע מוגברת)
2. **מפגש 3**: השוואת מודלים קוד פתוח שונים
3. **מפגש 4**: עבודה עם מודלים מתקדמים
4. **מפגש 5**: בניית מערכות AI מרובות סוכנים

## משתני סביבה (אופציונלי)

לשימוש מתקדם יותר, ניתן להגדיר את משתני הסביבה הבאים:

| משתנה | מטרה | דוגמה |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | מודל ברירת מחדל לשימוש | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | כתובת URL של נקודת קצה חלופית | `http://localhost:5273/v1` |

צרו קובץ `.env` בתיקיית הפרויקט שלכם:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## משאבים נוספים

### תיעוד

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### קוד לדוגמה

- **דוגמת Python למפגש 01**: `Workshop/samples/session01/chat_bootstrap.py` - אפליקציית צ'אט מלאה עם סטרימינג
- **מחברת למפגש 01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - הדרכה אינטראקטיבית  
- [דוגמת מודול 08 - 01](../Module08/samples/01/README.md) - התחלה מהירה עם REST Chat
- [דוגמת מודול 08 - 02](../Module08/samples/02/README.md) - אינטגרציה עם OpenAI SDK
- [דוגמת מודול 08 - 03](../Module08/samples/03/README.md) - גילוי מודלים וביצועי Benchmark

### קהילה

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**משך המפגש**: 30 דקות מעשי + 15 דקות שאלות ותשובות  
**רמת קושי**: מתחילים  
**דרישות מקדימות**: Windows 11/macOS 11+, Python 3.10+, גישה מנהלית

## תרחיש דוגמה לסדנה

### הקשר בעולם האמיתי

**תרחיש**: צוות IT ארגוני צריך להעריך הסקת מסקנות AI על המכשיר לצורך עיבוד משוב רגיש של עובדים מבלי לשלוח נתונים לשירותים חיצוניים.

**המטרה שלכם**: להדגים שמודלי AI מקומיים יכולים לספק תגובות איכותיות עם זמן תגובה של פחות משנייה תוך שמירה מלאה על פרטיות הנתונים.

### הנחיות בדיקה

השתמשו בהנחיות אלו כדי לאמת את ההגדרות שלכם:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### קריטריוני הצלחה

- ✅ כל ההנחיות מקבלות תגובות תוך פחות מ-2 שניות
- ✅ אין נתונים שעוזבים את המחשב המקומי שלכם
- ✅ התגובות רלוונטיות ומועילות
- ✅ אפליקציית הצ'אט שלכם פועלת בצורה חלקה

אימות זה מבטיח שההגדרות של Foundry Local שלכם מוכנות לסדנאות המתקדמות במפגשים 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או פירושים שגויים הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->