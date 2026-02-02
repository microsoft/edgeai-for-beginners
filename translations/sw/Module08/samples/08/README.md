# Mfano wa Mazungumzo ya Windows 11 - Foundry Local

Programu ya kisasa ya mazungumzo kwa Windows 11 inayojumuisha Microsoft Foundry Local na kiolesura cha asili chenye mvuto. Imejengwa kwa kutumia Electron na kufuata mifumo rasmi ya Microsoft Foundry Local.

## Muhtasari

Mfano huu unaonyesha jinsi ya kuunda programu ya mazungumzo inayofaa kwa uzalishaji ambayo inatumia mifano ya AI ya ndani kupitia Foundry Local, ikiwapa watumiaji mazungumzo ya AI yanayozingatia faragha bila utegemezi wa wingu.

## Vipengele

### 🎨 **Muundo Asilia wa Windows 11**
- Muunganisho wa Mfumo wa Fluent Design
- Athari za nyenzo za Mica na uwazi
- Msaada wa mandhari asilia ya Windows 11
- Mpangilio unaojibika kwa ukubwa wote wa skrini
- Kubadilisha kiotomatiki kati ya hali ya giza/nuru

### 🤖 **Ujumuishaji wa Mfano wa AI**
- Huduma ya Foundry Local imejumuishwa
- Msaada wa mifano mingi na kubadilisha papo hapo
- Majibu ya utiririshaji wa wakati halisi
- Kubadilisha kati ya mifano ya ndani na wingu
- Ufuatiliaji wa afya ya mifano na hali

### 💬 **Uzoefu wa Mazungumzo**
- Viashiria vya kuandika kwa wakati halisi
- Uhifadhi wa historia ya ujumbe
- Kusafirisha mazungumzo
- Maagizo maalum ya mfumo
- Usimamizi na matawi ya mazungumzo

### ⚡ **Vipengele vya Utendaji**
- Upakiaji wa polepole na uhalisia
- Utoaji ulioboreshwa kwa mazungumzo marefu
- Upakiaji wa mifano kwa nyuma
- Usimamizi mzuri wa kumbukumbu
- Uhuishaji laini na mabadiliko

## Muundo wa Kifaa

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

## Mahitaji ya Awali

### Mahitaji ya Mfumo
- **OS**: Windows 11 (22H2 au baadaye inapendekezwa)
- **RAM**: Angalau 8GB, 16GB+ inapendekezwa kwa mifano mikubwa
- **Hifadhi**: Angalau 10GB nafasi ya bure kwa mifano
- **GPU**: Hiari lakini inapendekezwa kwa utambuzi wa haraka

### Mahitaji ya Programu
- **Node.js**: v18.0.0 au baadaye
- **Foundry Local**: Toleo la hivi karibuni kutoka Microsoft
- **Git**: Kwa kunakili na maendeleo

## Usakinishaji

### 1. Sakinisha Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Nakili na Sanidi
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Sanidi Mazingira
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Endesha Programu
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Muundo wa Mradi

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

## Uchambuzi wa Vipengele Muhimu

### Ujumuishaji wa Windows 11

**Mfumo wa Fluent Design**
- Nyenzo za mandharinyuma za Mica
- Athari za uwazi wa Acrylic
- Pembe zilizozunguka na nafasi ya kisasa
- Paleti ya rangi asilia ya Windows 11
- Ishara za rangi za semantic kwa upatikanaji

**Vipengele Asilia vya Windows**
- Muunganisho wa orodha ya kuruka kwa mazungumzo ya hivi karibuni
- Arifa za Windows kwa ujumbe mpya
- Maendeleo ya upau wa kazi kwa operesheni za mifano
- Muunganisho wa tray ya mfumo na vitendo vya haraka
- Msaada wa uthibitishaji wa Windows Hello

### Usimamizi wa Mfano wa AI

**Mifano ya Ndani**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Msaada wa Mseto wa Wingu/Ndani**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Vipengele vya Kiolesura cha Mazungumzo

**Utiririshaji wa Wakati Halisi**
- Onyesho la majibu tokeni kwa tokeni
- Uhuishaji laini wa kuandika
- Maombi yanayoweza kufutwa
- Viashiria vya kuandika na hali

**Usimamizi wa Mazungumzo**
- Historia ya mazungumzo inayodumu
- Usafirishaji/uingizaji wa mazungumzo
- Utafutaji na uchujaji wa ujumbe
- Matawi ya mazungumzo
- Maagizo maalum ya mfumo kwa kila mazungumzo

**Upatikanaji**
- Uabiri kamili wa kibodi
- Utangamano wa wasomaji wa skrini
- Msaada wa hali ya utofauti wa juu
- Ukubwa wa fonti unaoweza kubadilishwa
- Muunganisho wa sauti kwa pembejeo

## Mifano ya Matumizi

### Ujumuishaji wa Mazungumzo ya Msingi
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

### Usimamizi wa Mfano
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

### Mipangilio na Ubinafsishaji
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

## Chaguo za Usanidi

### Mipangilio ya Programu
- **Mandhari**: Hali ya kiotomatiki, nuru, giza
- **Mfano**: Uchaguzi wa mfano wa msingi
- **Utendaji**: Mipangilio ya utambuzi
- **Faragha**: Sera za uhifadhi wa data
- **Arifa**: Tahadhari za ujumbe
- **Njia za mkato**: Njia za mkato za kibodi

### Mipangilio ya Mazungumzo
- **Utiririshaji**: Washa/zima majibu ya wakati halisi
- **Urefu wa Muktadha**: Kumbukumbu ya mazungumzo
- **Joto**: Ubunifu wa majibu
- **Tokeni za Juu**: Vikomo vya urefu wa majibu
- **Maagizo ya Mfumo**: Tabia ya msaidizi ya msingi

### Mipangilio ya Mfano
- **Upakuaji wa kiotomatiki**: Sasisho za mifano kiotomatiki
- **Ukubwa wa Akiba**: Vikomo vya hifadhi ya mifano ya ndani
- **Hali ya Utendaji**: Mapendeleo ya CPU dhidi ya GPU
- **Ukaguzi wa Afya**: Vipindi vya ufuatiliaji

## Maendeleo

### Kujenga kutoka Chanzo
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

### Ufuatiliaji wa Hitilafu
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Upimaji
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Uboreshaji wa Utendaji

### Usimamizi wa Kumbukumbu
- Uhalisia wa ujumbe mzuri
- Ukusanyaji wa takataka kiotomatiki
- Ufuatiliaji wa kumbukumbu ya mifano
- Usafishaji wa rasilimali wakati wa kutoka

### Uboreshaji wa Utoaji
- Utembezi wa kawaida kwa mazungumzo marefu
- Upakiaji wa polepole wa historia ya ujumbe
- Sasisho za React/DOM zilizoboreshwa
- Uhuishaji unaotumia GPU

### Uboreshaji wa Mtandao
- Ujumuishaji wa muunganisho
- Kundi la maombi
- Mantiki ya kurudia kiotomatiki
- Msaada wa hali ya nje ya mtandao

## Masuala ya Usalama

### Faragha ya Data
- Muundo wa ndani kwanza
- Hakuna usambazaji wa data ya wingu (hali ya ndani)
- Uhifadhi wa mazungumzo uliofichwa
- Usimamizi salama wa hati

### Usalama wa Programu
- Michakato ya renderer iliyotengwa
- Sera ya Usalama wa Maudhui (CSP)
- Hakuna utekelezaji wa msimbo wa mbali
- Mawasiliano salama ya IPC

## Utatuzi wa Hitilafu

### Masuala ya Kawaida

**Foundry Local Haianzi**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Hitilafu za Kupakia Mfano**
- Hakikisha nafasi ya diski ya kutosha
- Angalia muunganisho wa mtandao kwa upakuaji
- Hakikisha madereva ya GPU yamesasishwa
- Jaribu aina tofauti za mifano

**Masuala ya Utendaji**
- Fuatilia rasilimali za mfumo
- Rekebisha mipangilio ya mifano
- Washa kasi ya vifaa
- Funga programu nyingine zinazotumia rasilimali nyingi

### Hali ya Ufuatiliaji
Washa ufuatiliaji wa hitilafu kwa kuweka vigezo vya mazingira:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Kuchangia

### Usanidi wa Maendeleo
1. Nakili hifadhi
2. Unda tawi la kipengele
3. Sakinisha mahitaji: `npm install`
4. Fanya mabadiliko na ujaribu
5. Tuma ombi la kuvuta

### Mtindo wa Msimbo
- Usanidi wa ESLint umetolewa
- Prettier kwa muundo wa msimbo
- TypeScript kwa usalama wa aina
- Maoni ya JSDoc kwa nyaraka

## Matokeo ya Kujifunza

Baada ya kukamilisha mfano huu, utaelewa:

1. **Maendeleo Asilia ya Windows 11**
   - Utekelezaji wa Mfumo wa Fluent Design
   - Ujumuishaji wa asili wa Windows
   - Mazoea bora ya usalama wa Electron

2. **Ujumuishaji wa Mfano wa AI**
   - Muundo wa huduma ya Foundry Local
   - Usimamizi wa mzunguko wa maisha wa mifano
   - Ufuatiliaji wa utendaji na uboreshaji

3. **Mifumo ya Mazungumzo ya Wakati Halisi**
   - Ushughulikiaji wa majibu ya utiririshaji
   - Usimamizi wa hali ya mazungumzo
   - Mifumo ya uzoefu wa mtumiaji

4. **Maendeleo ya Programu ya Uzalishaji**
   - Ushughulikiaji wa hitilafu na urejeshaji
   - Uboreshaji wa utendaji
   - Masuala ya usalama
   - Mikakati ya upimaji

## Hatua Zifuatazo

- **Mfano 09**: Mfumo wa Uratibu wa Wakala Wengi
- **Mfano 10**: Foundry Local kama Ujumuishaji wa Zana
- **Mada za Juu**: Kuboresha mifano maalum
- **Upelekaji**: Mifumo ya upelekaji wa biashara

## Leseni

Mfano huu unafuata leseni sawa na mradi wa Microsoft Foundry Local.

---

