# דוגמת צ'אט ל-Windows 11 - Foundry Local

אפליקציית צ'אט מודרנית ל-Windows 11 שמשלבת את Microsoft Foundry Local עם ממשק מקומי יפהפה. נבנתה באמצעות Electron ועוקבת אחר דפוסי Foundry Local הרשמיים של מיקרוסופט.

## סקירה כללית

דוגמה זו מדגימה כיצד ליצור אפליקציית צ'אט מוכנה לייצור שמנצלת מודלים של AI מקומיים דרך Foundry Local, ומספקת למשתמשים שיחות AI ממוקדות פרטיות ללא תלות בענן.

## תכונות

### 🎨 **עיצוב מקומי ל-Windows 11**
- שילוב עם Fluent Design System  
- אפקטים של חומר Mica ושקיפות  
- תמיכה בעיצוב מקומי של Windows 11  
- פריסה רספונסיבית לכל גדלי המסכים  
- מעבר אוטומטי בין מצב כהה/בהיר  

### 🤖 **שילוב מודלי AI**
- שילוב שירות Foundry Local  
- תמיכה במודלים מרובים עם החלפה מהירה  
- תגובות בזמן אמת בסטרימינג  
- מעבר בין מודלים מקומיים ומודלי ענן  
- ניטור מצב המודלים ובריאותם  

### 💬 **חוויית צ'אט**
- אינדיקטורים להקלדה בזמן אמת  
- שמירת היסטוריית הודעות  
- ייצוא שיחות צ'אט  
- הנחיות מערכת מותאמות אישית  
- ניהול ופיצול שיחות  

### ⚡ **תכונות ביצועים**
- טעינה עצלה ווירטואליזציה  
- רינדור אופטימלי לשיחות ארוכות  
- טעינה מוקדמת של מודלים ברקע  
- ניהול זיכרון יעיל  
- אנימציות ומעברים חלקים  

## ארכיטקטורה

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```
  
## דרישות מוקדמות

### דרישות מערכת
- **מערכת הפעלה**: Windows 11 (מומלץ 22H2 או גרסה מאוחרת יותר)  
- **RAM**: מינימום 8GB, מומלץ 16GB+ למודלים גדולים יותר  
- **אחסון**: 10GB+ שטח פנוי למודלים  
- **GPU**: אופציונלי אך מומלץ להאצת ביצועים  

### תלות בתוכנה
- **Node.js**: גרסה v18.0.0 או מאוחרת יותר  
- **Foundry Local**: הגרסה האחרונה ממיקרוסופט  
- **Git**: לשכפול ופיתוח  

## התקנה

### 1. התקנת Foundry Local  
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```
  
### 2. שכפול והגדרה  
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```
  
### 3. הגדרת סביבה  
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```
  
### 4. הפעלת האפליקציה  
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```
  
## מבנה הפרויקט

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```
  
## תכונות מרכזיות - פירוט

### שילוב עם Windows 11

**Fluent Design System**  
- חומרים עם רקע Mica  
- אפקטי שקיפות אקריליים  
- פינות מעוגלות וריווח מודרני  
- פלטת צבעים מקומית של Windows 11  
- סמנטיקה צבעונית לנגישות  

**תכונות מקומיות של Windows**  
- שילוב רשימת קפיצה לשיחות אחרונות  
- התראות Windows להודעות חדשות  
- התקדמות בשורת המשימות לפעולות מודל  
- שילוב במגש המערכת עם פעולות מהירות  
- תמיכה באימות Windows Hello  

### ניהול מודלי AI

**מודלים מקומיים**  
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```
  
**תמיכה היברידית בענן/מקומי**  
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```
  
### תכונות ממשק הצ'אט

**סטרימינג בזמן אמת**  
- תצוגת תגובות לפי טוקן  
- אנימציות הקלדה חלקות  
- בקשות ניתנות לביטול  
- אינדיקטורים להקלדה ומצב  

**ניהול שיחות**  
- שמירת היסטוריית צ'אט  
- ייצוא/ייבוא שיחות  
- חיפוש וסינון הודעות  
- פיצול שיחות  
- הנחיות מערכת מותאמות אישית לכל שיחה  

**נגישות**  
- ניווט מלא באמצעות מקלדת  
- תאימות לקוראי מסך  
- תמיכה במצב ניגודיות גבוהה  
- התאמת גדלי גופן  
- שילוב קלט קולי  

## דוגמאות שימוש

### שילוב צ'אט בסיסי  
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```
  
### ניהול מודלים  
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```
  
### הגדרות והתאמה אישית  
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```
  
## אפשרויות תצורה

### הגדרות אפליקציה  
- **עיצוב**: מצב אוטומטי, בהיר, כהה  
- **מודל**: בחירת מודל ברירת מחדל  
- **ביצועים**: הגדרות הסקה  
- **פרטיות**: מדיניות שמירת נתונים  
- **התראות**: התראות הודעות  
- **קיצורי דרך**: קיצורי מקלדת  

### הגדרות צ'אט  
- **סטרימינג**: הפעלה/השבתה של תגובות בזמן אמת  
- **אורך הקשר**: זיכרון שיחה  
- **טמפרטורה**: יצירתיות תגובות  
- **מקסימום טוקנים**: מגבלות אורך תגובות  
- **הנחיות מערכת**: התנהגות עוזר ברירת מחדל  

### הגדרות מודל  
- **הורדה אוטומטית**: עדכוני מודל אוטומטיים  
- **גודל מטמון**: מגבלות אחסון מודלים מקומיים  
- **מצב ביצועים**: העדפות CPU מול GPU  
- **בדיקות בריאות**: מרווחי ניטור  

## פיתוח

### בנייה מהמקור  
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```
  
### ניפוי שגיאות  
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```
  
### בדיקות  
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```
  
## אופטימיזציית ביצועים

### ניהול זיכרון  
- וירטואליזציה יעילה של הודעות  
- איסוף זבל אוטומטי  
- ניטור זיכרון מודלים  
- ניקוי משאבים ביציאה  

### אופטימיזציית רינדור  
- גלילה וירטואלית לשיחות ארוכות  
- טעינה עצלה של היסטוריית הודעות  
- עדכוני React/DOM אופטימליים  
- אנימציות מואצות GPU  

### אופטימיזציית רשת  
- איגום חיבורים  
- אצירת בקשות  
- לוגיקת ניסיון חוזר אוטומטית  
- תמיכה במצב לא מקוון  

## שיקולי אבטחה

### פרטיות נתונים  
- ארכיטקטורה מקומית תחילה  
- ללא העברת נתונים לענן (מצב מקומי)  
- אחסון שיחות מוצפן  
- ניהול אישורים מאובטח  

### אבטחת אפליקציה  
- תהליכי רינדור מבודדים  
- מדיניות אבטחת תוכן (CSP)  
- ללא ביצוע קוד מרחוק  
- תקשורת IPC מאובטחת  

## פתרון בעיות

### בעיות נפוצות

**Foundry Local לא מתחיל**  
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```
  
**כשלי טעינת מודלים**  
- ודא שיש מספיק שטח דיסק  
- בדוק חיבור אינטרנט להורדות  
- ודא שדרייברים של GPU מעודכנים  
- נסה גרסאות מודל שונות  

**בעיות ביצועים**  
- עקוב אחר משאבי מערכת  
- התאם הגדרות מודל  
- הפעל האצת חומרה  
- סגור אפליקציות אחרות שצורכות משאבים  

### מצב ניפוי שגיאות  
הפעלת לוגים לניפוי שגיאות על ידי הגדרת משתני סביבה:  
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```
  
## תרומה

### הגדרת פיתוח  
1. בצע Fork למאגר  
2. צור ענף פיצ'ר  
3. התקן תלות: `npm install`  
4. בצע שינויים ובדוק  
5. שלח Pull Request  

### סגנון קוד  
- תצורת ESLint מסופקת  
- Prettier לעיצוב קוד  
- TypeScript לבטיחות טיפוסים  
- הערות JSDoc לתיעוד  

## תוצאות למידה

לאחר השלמת דוגמה זו, תבין:

1. **פיתוח מקומי ל-Windows 11**  
   - יישום Fluent Design System  
   - שילוב מקומי של Windows  
   - שיטות אבטחה ב-Electron  

2. **שילוב מודלי AI**  
   - ארכיטקטורת שירות Foundry Local  
   - ניהול מחזור חיים של מודלים  
   - ניטור ביצועים ואופטימיזציה  

3. **מערכות צ'אט בזמן אמת**  
   - טיפול בתגובות סטרימינג  
   - ניהול מצב שיחה  
   - דפוסי חוויית משתמש  

4. **פיתוח אפליקציות לייצור**  
   - טיפול בשגיאות והתאוששות  
   - אופטימיזציית ביצועים  
   - שיקולי אבטחה  
   - אסטרטגיות בדיקה  

## צעדים הבאים

- **דוגמה 09**: מערכת תזמור מרובת סוכנים  
- **דוגמה 10**: Foundry Local כשילוב כלים  
- **נושאים מתקדמים**: התאמה אישית של מודלים  
- **פריסה**: דפוסי פריסה ארגוניים  

## רישיון

דוגמה זו עוקבת אחר אותו רישיון כמו פרויקט Microsoft Foundry Local.  

---

