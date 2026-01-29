# Windows 11 Chat Eksempel - Foundry Local

En moderne chatapplikation til Windows 11, der integrerer Microsoft Foundry Local med en smuk, indbygget grænseflade. Bygget med Electron og følger Microsofts officielle Foundry Local-mønstre.

## Oversigt

Dette eksempel viser, hvordan man opretter en produktionsklar chatapplikation, der udnytter lokale AI-modeller via Foundry Local, og giver brugerne privatlivsfokuserede AI-samtaler uden afhængighed af skyen.

## Funktioner

### 🎨 **Windows 11 Indbygget Design**
- Integration med Fluent Design System
- Mica-materialeeffekter og gennemsigtighed
- Understøttelse af indbygget Windows 11-tema
- Responsivt layout til alle skærmstørrelser
- Automatisk skift mellem mørk/lys tilstand

### 🤖 **AI Model Integration**
- Integration med Foundry Local-tjenesten
- Understøttelse af flere modeller med hot-swapping
- Streaming-svar i realtid
- Skift mellem lokale og cloud-modeller
- Overvågning af modelstatus og sundhed

### 💬 **Chatoplevelse**
- Skriveindikatorer i realtid
- Vedvarende beskedhistorik
- Eksport af chat-samtaler
- Tilpassede systemprompter
- Forgrening og styring af samtaler

### ⚡ **Ydelsesfunktioner**
- Lazy loading og virtualisering
- Optimeret rendering til lange samtaler
- Forudindlæsning af modeller i baggrunden
- Effektiv hukommelseshåndtering
- Glatte animationer og overgange

## Arkitektur

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

## Forudsætninger

### Systemkrav
- **OS**: Windows 11 (22H2 eller nyere anbefales)
- **RAM**: Minimum 8GB, 16GB+ anbefales til større modeller
- **Lagring**: 10GB+ ledig plads til modeller
- **GPU**: Valgfrit, men anbefales til hurtigere inferens

### Softwareafhængigheder
- **Node.js**: v18.0.0 eller nyere
- **Foundry Local**: Seneste version fra Microsoft
- **Git**: Til kloning og udvikling

## Installation

### 1. Installer Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klon og opsæt
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurer miljø
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Kør applikationen
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projektstruktur

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

## Dybdegående funktioner

### Windows 11 Integration

**Fluent Design System**
- Mica baggrundsmaterialer
- Akryl gennemsigtighedseffekter
- Afrundede hjørner og moderne afstand
- Indbygget Windows 11 farvepalet
- Semantiske farvetokens for tilgængelighed

**Indbyggede Windows-funktioner**
- Jump list-integration til nylige chats
- Windows-notifikationer for nye beskeder
- Processtatus på proceslinjen for modeloperationer
- Systembakkeintegration med hurtige handlinger
- Understøttelse af Windows Hello-godkendelse

### AI Modelhåndtering

**Lokale modeller**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybrid Cloud/Lokal Support**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chatgrænsefladefunktioner

**Streaming i realtid**
- Token-for-token svarvisning
- Glatte skriveanimationer
- Annullerbare forespørgsler
- Skriveindikatorer og status

**Samtalestyring**
- Vedvarende chat-historik
- Eksport/import af samtaler
- Beskedsøgning og filtrering
- Forgrening af samtaler
- Tilpassede systemprompter pr. samtale

**Tilgængelighed**
- Fuld tastaturnavigation
- Kompatibilitet med skærmlæsere
- Understøttelse af høj kontrast-tilstand
- Tilpasning af skrifttypestørrelser
- Integration af stemmeinput

## Brugs Eksempler

### Grundlæggende Chat Integration
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

### Modelhåndtering
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

### Indstillinger og Tilpasning
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

## Konfigurationsmuligheder

### Applikationsindstillinger
- **Tema**: Auto, lys, mørk tilstand
- **Model**: Standard modelvalg
- **Ydelse**: Indstillinger for inferens
- **Privatliv**: Politik for dataopbevaring
- **Notifikationer**: Beskedalarmer
- **Genveje**: Tastaturgenveje

### Chatindstillinger
- **Streaming**: Aktiver/deaktiver svar i realtid
- **Kontekstens længde**: Samtalens hukommelse
- **Temperatur**: Kreativitet i svar
- **Maksimale tokens**: Begrænsninger for svarlængde
- **Systemprompter**: Standardassistentens adfærd

### Modelindstillinger
- **Auto-download**: Automatiske modelopdateringer
- **Cache-størrelse**: Begrænsninger for lokal modelopbevaring
- **Ydelsestilstand**: CPU vs GPU præferencer
- **Sundhedstjek**: Overvågningsintervaller

## Udvikling

### Byg fra kilde
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

### Fejlfinding
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Test
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Ydelsesoptimering

### Hukommelseshåndtering
- Effektiv virtualisering af beskeder
- Automatisk affaldsindsamling
- Overvågning af modelhukommelse
- Ressourceoprydning ved afslutning

### Renderingoptimering
- Virtuel scrolling til lange samtaler
- Lazy loading af beskedhistorik
- Optimerede React/DOM-opdateringer
- GPU-accelererede animationer

### Netværksoptimering
- Forbindelsespooling
- Batchning af forespørgsler
- Automatisk genforsøg
- Understøttelse af offline-tilstand

## Sikkerhedsovervejelser

### Dataprivacy
- Lokal-først arkitektur
- Ingen dataoverførsel til skyen (lokal tilstand)
- Krypteret samtaleopbevaring
- Sikker håndtering af legitimationsoplysninger

### Applikationssikkerhed
- Sandkasse til renderer-processer
- Content Security Policy (CSP)
- Ingen fjernudførelse af kode
- Sikker IPC-kommunikation

## Fejlfinding

### Almindelige Problemer

**Foundry Local Starter Ikke**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Fejl ved Modelloading**
- Kontroller tilstrækkelig diskplads
- Tjek internetforbindelse til downloads
- Sørg for, at GPU-drivere er opdaterede
- Prøv forskellige modelvarianter

**Ydelsesproblemer**
- Overvåg systemressourcer
- Juster modelindstillinger
- Aktiver hardwareacceleration
- Luk andre ressourcekrævende applikationer

### Fejltilstand
Aktiver fejllogning ved at indstille miljøvariabler:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Bidrag

### Udviklingsopsætning
1. Fork repositoryet
2. Opret en feature branch
3. Installer afhængigheder: `npm install`
4. Foretag ændringer og test
5. Indsend en pull request

### Kodestil
- ESLint-konfiguration inkluderet
- Prettier til kodeformatering
- TypeScript for type-sikkerhed
- JSDoc-kommentarer til dokumentation

## Læringsresultater

Efter at have gennemført dette eksempel vil du forstå:

1. **Windows 11 Indbygget Udvikling**
   - Implementering af Fluent Design System
   - Integration med Windows-funktioner
   - Elektron-sikkerheds bedste praksis

2. **AI Model Integration**
   - Foundry Local servicearkitektur
   - Håndtering af modellivscyklus
   - Ydelsesovervågning og optimering

3. **Chat Systemer i Real-tid**
   - Håndtering af streaming-svar
   - Styring af samtaletilstand
   - Brugeroplevelsesmønstre

4. **Udvikling af Produktionsapplikationer**
   - Fejlhåndtering og genopretning
   - Ydelsesoptimering
   - Sikkerhedsovervejelser
   - Teststrategier

## Næste Skridt

- **Eksempel 09**: Multi-Agent Orchestration System
- **Eksempel 10**: Foundry Local som værktøjsintegration
- **Avancerede Emner**: Tilpasning af model finjustering
- **Udrulning**: Mønstre for virksomhedsudrulning

## Licens

Dette eksempel følger samme licens som Microsoft Foundry Local-projektet.

---

