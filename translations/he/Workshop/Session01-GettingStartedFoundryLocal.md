<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:23:22+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "he"
}
-->
# מפגש 1: התחלת עבודה עם Foundry Local

## תקציר

התחילו את המסע שלכם עם Foundry Local על ידי התקנה והגדרה שלו ב-Windows 11. למדו כיצד להגדיר את CLI, להפעיל האצת חומרה ולשמור מודלים במטמון לצורך הסקת מסקנות מהירה מקומית. מפגש מעשי זה כולל הפעלה של מודלים כמו Phi, Qwen, DeepSeek ו-GPT-OSS-20B באמצעות פקודות CLI שחוזרות על עצמן.

## מטרות למידה

בסיום המפגש הזה, תוכלו:

- **להתקין ולהגדיר**: להגדיר את Foundry Local ב-Windows 11 עם הגדרות ביצועים מיטביות
- **לשלוט בפעולות CLI**: להשתמש ב-CLI של Foundry Local לניהול והפעלת מודלים
- **להפעיל האצת חומרה**: להגדיר האצת GPU עם ONNXRuntime או WebGPU
- **להפעיל מספר מודלים**: להפעיל מודלים כמו phi-4, GPT-OSS-20B, Qwen ו-DeepSeek באופן מקומי
- **לבנות את האפליקציה הראשונה שלכם**: להתאים דוגמאות קיימות לשימוש ב-SDK של Foundry Local ב-Python

# בדיקת המודל (הנחיה יחידה לא אינטראקטיבית)
foundry model run phi-4-mini --prompt "שלום, הצג את עצמך"

- Windows 11 (22H2 או גרסה מאוחרת יותר)
# רשימת מודלים זמינים בקטלוג (מודלים טעונים מופיעים לאחר הפעלה)
foundry model list  
## NOTE: כרגע אין דגל ייעודי `--running`; כדי לראות אילו מודלים טעונים, התחילו שיחה או בדקו את לוגי השירות.
- Python 3.10+ מותקן
- Visual Studio Code עם הרחבת Python
- הרשאות מנהל להתקנה

### (אופציונלי) משתני סביבה

צרו `.env` (או הגדירו ב-shell) כדי להפוך סקריפטים לניידים:
# השוואת תגובות (לא אינטראקטיבי)
foundry model run gpt-oss-20b --prompt "הסבר על Edge AI במונחים פשוטים"
| משתנה | מטרה | דוגמה |
|-------|-------|-------|
| `FOUNDRY_LOCAL_ALIAS` | כינוי מועדף למודל (הקטלוג בוחר אוטומטית את הגרסה הטובה ביותר) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | עקיפת נקודת קצה (אחרת אוטומטית מהמנהלת) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | הפעלת הדגמת סטרימינג | `true` |

> אם `FOUNDRY_LOCAL_ENDPOINT=auto` (או לא מוגדר) אנו נגזור אותו ממנהלת ה-SDK.

## זרימת הדגמה (30 דקות)

### 1. התקנת Foundry Local ואימות הגדרת CLI (10 דקות)

# רשימת מודלים במטמון
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```
  
**macOS (תצוגה מקדימה / אם נתמך)**

אם חבילת macOS מקורית זמינה (בדקו את התיעוד הרשמי לעדכונים האחרונים):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```
  
אם בינאריים מקוריים ל-macOS עדיין לא זמינים, ניתן עדיין:  
1. להשתמש ב-VM של Windows 11 ARM/Intel (Parallels / UTM) ולעקוב אחר שלבי Windows.  
2. להפעיל מודלים דרך קונטיינר (אם תמונת קונטיינר פורסמה) ולהגדיר `FOUNDRY_LOCAL_ENDPOINT` ליציאת החשיפה.  

**יצירת סביבה וירטואלית ב-Python (חוצה פלטפורמות)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```
  
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
  
שדרגו pip והתקינו תלות ליבה:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
#### שלב 1.2: אימות התקנה

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```
  
#### שלב 1.3: הגדרת סביבה

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```
  
### אתחול SDK (מומלץ)

במקום להפעיל ידנית את השירות ולהפעיל מודלים, **Foundry Local Python SDK** יכול לאתחל הכל:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```
  
אם אתם מעדיפים שליטה מפורשת, עדיין ניתן להשתמש ב-CLI + לקוח OpenAI כפי שמוצג בהמשך.

### 2. הפעלת מודלים באופן מקומי דרך CLI (10 דקות)

#### שלב 3.1: הפעלת מודל Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```
  
#### שלב 3.2: הפעלת GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```
  
#### שלב 3.3: טעינת מודלים נוספים

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```
  
### 4. פרויקט התחלתי: התאמת 01-run-phi ל-Foundry Local (5 דקות)

#### שלב 4.1: יצירת אפליקציית צ'אט בסיסית

צרו `samples/01-foundry-quickstart/chat_quickstart.py` (מעודכן לשימוש במנהלת אם זמינה):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```
  
#### שלב 4.2: בדיקת האפליקציה

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```
  
## מושגים מרכזיים שנלמדו

### 1. ארכיטקטורת Foundry Local

- **מנוע הסקת מסקנות מקומי**: מפעיל מודלים לחלוטין על המכשיר שלכם  
- **תאימות ל-SDK של OpenAI**: אינטגרציה חלקה עם קוד OpenAI קיים  
- **ניהול מודלים**: הורדה, שמירה במטמון והפעלה של מספר מודלים ביעילות  
- **אופטימיזציית חומרה**: ניצול האצת GPU, NPU ו-CPU  

### 2. הפניות לפקודות CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```
  
### 3. אינטגרציה עם Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```
  
## פתרון בעיות נפוצות

### בעיה 1: "פקודת Foundry לא נמצאה"

**פתרון:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```
  
### בעיה 2: "המודל נכשל בטעינה"

**פתרון:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```
  
### בעיה 3: "חיבור נדחה ב-localhost:5273"

**פתרון:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```
  
## טיפים לאופטימיזציית ביצועים

### 1. אסטרטגיית בחירת מודלים

- **Phi-4-mini**: הטוב ביותר למשימות כלליות, שימוש נמוך בזיכרון  
- **Qwen2.5-0.5b**: הסקת מסקנות מהירה ביותר, משאבים מינימליים  
- **GPT-OSS-20B**: איכות גבוהה ביותר, דורש יותר משאבים  
- **DeepSeek-Coder**: מותאם למשימות תכנות  

### 2. אופטימיזציית חומרה

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```
  
### 3. ניטור ביצועים

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```
  
### שיפורים אופציונליים

| שיפור | מה | איך |
|-------|----|-----|
| כלי עזר משותפים | הסרת לוגיקת לקוח/אתחול כפולה | השתמשו ב-`Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| נראות שימוש בטוקנים | לימוד חשיבה על עלות/יעילות מוקדם | הגדירו `SHOW_USAGE=1` להדפסת טוקנים של הנחיה/תגובה/סה"כ |
| השוואות דטרמיניסטיות | בדיקות יציבות ובקרת רגרסיה | השתמשו ב-`temperature=0`, `top_p=1`, טקסט הנחיה עקבי |
| זמן תגובה לטוקן ראשון | מדד לתחושת תגובתיות | התאימו סקריפט בדיקה עם סטרימינג (`BENCH_STREAM=1`) |
| ניסיון חוזר על שגיאות חולפות | הדגמות עמידות בהפעלה קרה | `RETRY_ON_FAIL=1` (ברירת מחדל) והתאימו `RETRY_BACKOFF` |
| בדיקות עישון | בדיקות מהירות על זרימות מפתח | הריצו `python Workshop/tests/smoke.py` לפני סדנה |
| פרופילי כינוי מודלים | מעבר מהיר בין סט מודלים במכונות שונות | תחזקו `.env` עם `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| יעילות מטמון | הימנעות מחימום חוזר בהרצה מרובת דוגמאות | מנהלי מטמון כלי עזר; שימוש חוזר בין סקריפטים/מחברות |
| חימום בהרצה ראשונה | הפחתת קפיצות זמן תגובה p95 | הריצו הנחיה קטנה לאחר יצירת `FoundryLocalManager` |

דוגמה לחימום בסיסי דטרמיניסטי (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```
  
אתם אמורים לראות פלט דומה וספירת טוקנים זהה בהרצה השנייה, המאשרת דטרמיניזם.

## צעדים הבאים

לאחר סיום המפגש:

1. **חקירת מפגש 2**: בניית פתרונות AI עם Azure AI Foundry RAG  
2. **ניסוי עם מודלים שונים**: נסו את Qwen, DeepSeek ומשפחות מודלים אחרות  
3. **אופטימיזציית ביצועים**: כווננו הגדרות בהתאם לחומרה שלכם  
4. **בניית אפליקציות מותאמות אישית**: השתמשו ב-SDK של Foundry Local בפרויקטים שלכם  

## משאבים נוספים

### תיעוד
- [מדריך Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [מדריך התקנה של Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)  
- [קטלוג מודלים](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)  

### קוד לדוגמה
- [דוגמה מודול08 01](./samples/01/README.md) - התחלה מהירה עם REST Chat  
- [דוגמה מודול08 02](./samples/02/README.md) - אינטגרציה עם OpenAI SDK  
- [דוגמה מודול08 03](./samples/03/README.md) - גילוי מודלים ובדיקת ביצועים  

### קהילה
- [דיונים ב-GitHub של Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)  
- [קהילת Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)  

---

**משך המפגש**: 30 דקות מעשי + 15 דקות שאלות ותשובות  
**רמת קושי**: מתחילים  
**דרישות מוקדמות**: Windows 11, Python 3.10+, גישת מנהל  

## תרחיש לדוגמה ומיפוי סדנה

| סקריפט סדנה / מחברת | תרחיש | מטרה | קלט לדוגמה | נתונים נדרשים |
|----------------------|--------|------|------------|---------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | צוות IT פנימי שמעריך הסקת מסקנות על המכשיר עבור פורטל הערכת פרטיות | הוכחת תגובת SLM מקומי תוך פחות משנייה על הנחיות סטנדרטיות | "ציינו שני יתרונות של הסקת מסקנות מקומית." | אין (הנחיה יחידה) |
| קוד התאמה להתחלה מהירה | מפתח שמעתיק סקריפט OpenAI קיים ל-Foundry Local | הצגת תאימות ישירה | "ציינו שני יתרונות של הסקת מסקנות מקומית." | הנחיה בלבד |

### נרטיב תרחיש
צוות אבטחה וציות חייב לאמת האם ניתן לעבד נתוני אבטיפוס רגישים באופן מקומי. הם מריצים את סקריפט האתחול עם מספר הנחיות (פרטיות, זמן תגובה, עלות) תוך שימוש במצב דטרמיניסטי temperature=0 כדי ללכוד פלטים בסיסיים להשוואה עתידית (בדיקות ביצועים במפגש 3 והשוואת SLM מול LLM במפגש 4).

### סט הנחיות מינימלי JSON (אופציונלי)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```
  
השתמשו ברשימה זו ליצירת לולאת הערכה שחוזרת על עצמה או לזריעת מסגרת בדיקות רגרסיה עתידית.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.