# Windows 11 Pokalbio Pavyzdys - Foundry Local

Moderni pokalbių programa, skirta Windows 11, integruojanti Microsoft Foundry Local su gražia natūralia sąsaja. Sukurta naudojant Electron ir laikantis oficialių Microsoft Foundry Local šablonų.

## Apžvalga

Šis pavyzdys parodo, kaip sukurti gamybai paruoštą pokalbių programą, kuri naudoja vietinius AI modelius per Foundry Local, suteikiant vartotojams privatumo orientuotus AI pokalbius be debesų priklausomybės.

## Funkcijos

### 🎨 **Windows 11 Natūralus Dizainas**
- Integracija su Fluent Design System
- Mica medžiagos efektai ir skaidrumas
- Natūralus Windows 11 temų palaikymas
- Prisitaikantis dizainas visiems ekrano dydžiams
- Automatinis tamsaus/šviesaus režimo perjungimas

### 🤖 **AI Modelių Integracija**
- Foundry Local paslaugos integracija
- Kelių modelių palaikymas su greitu perjungimu
- Atsakymų transliacija realiu laiku
- Vietinių ir debesų modelių perjungimas
- Modelių būklės stebėjimas ir statusas

### 💬 **Pokalbių Patirtis**
- Rašymo indikatoriai realiu laiku
- Žinučių istorijos išsaugojimas
- Pokalbių eksportavimas
- Individualūs sistemos raginimai
- Pokalbių šakų valdymas

### ⚡ **Našumo Funkcijos**
- Lėtas įkrovimas ir virtualizacija
- Optimizuotas ilgesnių pokalbių atvaizdavimas
- Modelių išankstinis įkrovimas fone
- Efektyvus atminties valdymas
- Sklandžios animacijos ir perėjimai

## Architektūra

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

## Reikalavimai

### Sistemos Reikalavimai
- **OS**: Windows 11 (rekomenduojama 22H2 ar naujesnė versija)
- **RAM**: Mažiausiai 8GB, rekomenduojama 16GB+ didesniems modeliams
- **Saugykla**: 10GB+ laisvos vietos modeliams
- **GPU**: Neprivaloma, bet rekomenduojama greitesniam apdorojimui

### Programinės Įrangos Priklausomybės
- **Node.js**: v18.0.0 ar naujesnė versija
- **Foundry Local**: Naujausia Microsoft versija
- **Git**: Klonavimui ir kūrimui

## Įdiegimas

### 1. Įdiekite Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonuokite ir Nustatykite
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigūruokite Aplinką
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Paleiskite Programą
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projekto Struktūra

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

## Pagrindinių Funkcijų Išsamus Aprašymas

### Windows 11 Integracija

**Fluent Design System**
- Mica foninės medžiagos
- Akrilo skaidrumo efektai
- Užapvalinti kampai ir modernus tarpai
- Natūralus Windows 11 spalvų paletės palaikymas
- Semantiniai spalvų žymekliai prieinamumui

**Natūralios Windows Funkcijos**
- Greito sąrašo integracija naujausiems pokalbiams
- Windows pranešimai apie naujas žinutes
- Užduočių juostos progresas modelių operacijoms
- Sistemos dėklo integracija su greitais veiksmais
- Windows Hello autentifikacijos palaikymas

### AI Modelių Valdymas

**Vietiniai Modeliai**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hibridinis Debesų/Vietinis Palaikymas**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Pokalbių Sąsajos Funkcijos

**Transliacija Realiu Laiku**
- Atsakymų rodymas po vieną simbolį
- Sklandžios rašymo animacijos
- Užklausų atšaukimas
- Rašymo indikatoriai ir statusas

**Pokalbių Valdymas**
- Nuolatinė pokalbių istorija
- Pokalbių eksportavimas/importavimas
- Žinučių paieška ir filtravimas
- Pokalbių šakų kūrimas
- Individualūs sistemos raginimai kiekvienam pokalbiui

**Prieinamumas**
- Pilnas klaviatūros navigavimas
- Suderinamumas su ekrano skaitytuvais
- Aukšto kontrasto režimo palaikymas
- Pritaikomi šriftų dydžiai
- Balso įvesties integracija

## Naudojimo Pavyzdžiai

### Pagrindinė Pokalbių Integracija
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

### Modelių Valdymas
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

### Nustatymai ir Pritaikymas
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

## Konfigūracijos Parinktys

### Programos Nustatymai
- **Tema**: Automatinis, šviesus, tamsus režimas
- **Modelis**: Numatytojo modelio pasirinkimas
- **Našumas**: Apdorojimo nustatymai
- **Privatumas**: Duomenų saugojimo politika
- **Pranešimai**: Žinučių įspėjimai
- **Spartieji Klavišai**: Klaviatūros kombinacijos

### Pokalbių Nustatymai
- **Transliacija**: Įjungti/išjungti atsakymus realiu laiku
- **Konteksto Ilgis**: Pokalbio atmintis
- **Temperatūra**: Atsakymų kūrybiškumas
- **Maksimalūs Simboliai**: Atsakymų ilgio ribos
- **Sistemos Raginimai**: Numatytoji asistento elgsena

### Modelių Nustatymai
- **Automatinis Atsisiuntimas**: Automatiniai modelių atnaujinimai
- **Talpyklos Dydis**: Vietinių modelių saugojimo ribos
- **Našumo Režimas**: CPU vs GPU pasirinkimai
- **Sveikatos Patikrinimai**: Stebėjimo intervalai

## Kūrimas

### Kūrimas iš Šaltinio
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

### Derinimas
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testavimas
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Našumo Optimizavimas

### Atminties Valdymas
- Efektyvi žinučių virtualizacija
- Automatinis šiukšlių surinkimas
- Modelių atminties stebėjimas
- Išteklių valymas uždarant

### Atvaizdavimo Optimizavimas
- Virtualus slinkimas ilgiems pokalbiams
- Lėtas žinučių istorijos įkrovimas
- Optimizuoti React/DOM atnaujinimai
- GPU pagreitintos animacijos

### Tinklo Optimizavimas
- Jungčių telkimas
- Užklausų grupavimas
- Automatinė pakartotinio bandymo logika
- Neprisijungus režimo palaikymas

## Saugumo Apsvarstymai

### Duomenų Privatumas
- Vietinis pirmasis architektūros principas
- Nėra debesų duomenų perdavimo (vietiniu režimu)
- Užšifruotas pokalbių saugojimas
- Saugus kredencialų valdymas

### Programos Saugumas
- Sandarinti atvaizdavimo procesai
- Turinio Saugumo Politika (CSP)
- Nėra nuotolinio kodo vykdymo
- Saugus IPC ryšys

## Trikčių Šalinimas

### Dažnos Problemos

**Foundry Local Nepasileidžia**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Modelių Įkrovimo Klaidos**
- Patikrinkite, ar pakanka disko vietos
- Patikrinkite interneto ryšį atsisiuntimams
- Įsitikinkite, kad GPU tvarkyklės atnaujintos
- Išbandykite skirtingus modelių variantus

**Našumo Problemos**
- Stebėkite sistemos išteklius
- Koreguokite modelių nustatymus
- Įjunkite aparatūros pagreitį
- Uždarykite kitas daug išteklių reikalaujančias programas

### Derinimo Režimas
Įjunkite derinimo žurnalus nustatydami aplinkos kintamuosius:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Prisidėjimas

### Kūrimo Nustatymai
1. Fork'inkite saugyklą
2. Sukurkite funkcijų šaką
3. Įdiekite priklausomybes: `npm install`
4. Atlikite pakeitimus ir testuokite
5. Pateikite pull request

### Kodo Stilius
- Pateikta ESLint konfigūracija
- Prettier kodo formatavimui
- TypeScript tipų saugumui
- JSDoc komentarai dokumentacijai

## Mokymosi Rezultatai

Baigę šį pavyzdį, suprasite:

1. **Windows 11 Natūralų Kūrimą**
   - Fluent Design System įgyvendinimą
   - Natūralią Windows integraciją
   - Electron saugumo geriausią praktiką

2. **AI Modelių Integraciją**
   - Foundry Local paslaugos architektūrą
   - Modelių gyvavimo ciklo valdymą
   - Našumo stebėjimą ir optimizavimą

3. **Realaus Laiko Pokalbių Sistemos**
   - Atsakymų transliacijos valdymą
   - Pokalbių būsenos valdymą
   - Vartotojo patirties šablonus

4. **Gamybos Programų Kūrimą**
   - Klaidų tvarkymą ir atkūrimą
   - Našumo optimizavimą
   - Saugumo apsvarstymus
   - Testavimo strategijas

## Kiti Žingsniai

- **Pavyzdys 09**: Daugiaagentinė Orkestracijos Sistema
- **Pavyzdys 10**: Foundry Local kaip Įrankių Integracija
- **Pažangios Temos**: Individualus modelių tobulinimas
- **Diegimas**: Įmonės diegimo šablonai

## Licencija

Šis pavyzdys laikosi tos pačios licencijos kaip ir Microsoft Foundry Local projektas.

---

