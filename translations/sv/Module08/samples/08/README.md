# Windows 11 Chat Sample - Foundry Local

En modern chattapplikation för Windows 11 som integrerar Microsoft Foundry Local med ett vackert, inbyggt gränssnitt. Byggd med Electron och följer Microsofts officiella Foundry Local-mönster.

## Översikt

Detta exempel visar hur man skapar en produktionsklar chattapplikation som utnyttjar lokala AI-modeller via Foundry Local, vilket ger användare integritetsfokuserade AI-konversationer utan molnberoenden.

## Funktioner

### 🎨 **Windows 11 Native Design**
- Integration med Fluent Design System
- Mica-materialeffekter och transparens
- Stöd för inbyggd Windows 11-tema
- Responsiv layout för alla skärmstorlekar
- Automatisk växling mellan mörkt/ljust läge

### 🤖 **AI-modellintegration**
- Integration med Foundry Local-tjänsten
- Stöd för flera modeller med snabb växling
- Realtidsströmmande svar
- Växling mellan lokala och molnbaserade modeller
- Övervakning av modellhälsa och status

### 💬 **Chattupplevelse**
- Realtidsindikatorer för skrivande
- Ihållande meddelandehistorik
- Exportera chattkonversationer
- Anpassade systemprompter
- Hantering och förgrening av konversationer

### ⚡ **Prestandafunktioner**
- Lazy loading och virtualisering
- Optimerad rendering för långa konversationer
- Förladdning av modeller i bakgrunden
- Effektiv minneshantering
- Smidiga animationer och övergångar

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

## Förutsättningar

### Systemkrav
- **OS**: Windows 11 (22H2 eller senare rekommenderas)
- **RAM**: Minst 8GB, 16GB+ rekommenderas för större modeller
- **Lagring**: 10GB+ ledigt utrymme för modeller
- **GPU**: Valfritt men rekommenderas för snabbare inferens

### Programvarukrav
- **Node.js**: v18.0.0 eller senare
- **Foundry Local**: Senaste versionen från Microsoft
- **Git**: För kloning och utveckling

## Installation

### 1. Installera Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klona och konfigurera
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurera miljön
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Kör applikationen
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

## Djupdykning i nyckelfunktioner

### Windows 11-integration

**Fluent Design System**
- Mica-bakgrundsmaterial
- Akryltransparenseffekter
- Rundade hörn och modern spacing
- Inbyggd Windows 11-färgpalett
- Semantiska färgtokens för tillgänglighet

**Inbyggda Windows-funktioner**
- Jump list-integration för senaste chattar
- Windows-notifikationer för nya meddelanden
- Aktivitetsfältets framsteg för modelloperationer
- Systemfackintegration med snabbåtgärder
- Stöd för Windows Hello-autentisering

### AI-modellhantering

**Lokala modeller**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybridstöd för moln/lokalt**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funktioner i chattgränssnittet

**Realtidsströmning**
- Token-för-token-svarvisning
- Smidiga skrivanimationer
- Avbrytbara förfrågningar
- Indikatorer för skrivande och status

**Hantering av konversationer**
- Ihållande chattlogg
- Export/import av konversationer
- Sök och filtrering av meddelanden
- Förgrening av konversationer
- Anpassade systemprompter per konversation

**Tillgänglighet**
- Fullständig tangentbordsnavigering
- Kompatibilitet med skärmläsare
- Stöd för högkontrastläge
- Anpassningsbara teckenstorlekar
- Röstinmatningsintegration

## Användningsexempel

### Grundläggande chattintegration
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

### Modellhantering
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

### Inställningar och anpassning
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

## Konfigurationsalternativ

### Applikationsinställningar
- **Tema**: Auto, ljust, mörkt läge
- **Modell**: Standardval av modell
- **Prestanda**: Inställningar för inferens
- **Integritet**: Policyer för datalagring
- **Notifikationer**: Meddelandevarningar
- **Snabbkommandon**: Tangentbordsgenvägar

### Chattinställningar
- **Strömning**: Aktivera/inaktivera realtidssvar
- **Kontextlängd**: Minneskapacitet för konversationer
- **Temperatur**: Kreativitet i svar
- **Max Tokens**: Begränsningar för svarslängd
- **Systemprompter**: Standardbeteende för assistenten

### Modellinställningar
- **Auto-nedladdning**: Automatiska modelluppdateringar
- **Cache-storlek**: Begränsningar för lokal modellagring
- **Prestandaläge**: CPU kontra GPU-preferenser
- **Hälsokontroller**: Övervakningsintervaller

## Utveckling

### Bygga från källkod
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

### Felsökning
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testning
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Prestandaoptimering

### Minneshantering
- Effektiv virtualisering av meddelanden
- Automatisk garbage collection
- Övervakning av modellminne
- Resursrensning vid avslut

### Renderingoptimering
- Virtuell scrollning för långa konversationer
- Lazy loading av meddelandehistorik
- Optimerade React/DOM-uppdateringar
- GPU-accelererade animationer

### Nätverksoptimering
- Poolning av anslutningar
- Batchning av förfrågningar
- Automatisk återförsökslogik
- Stöd för offline-läge

## Säkerhetsöverväganden

### Dataintegritet
- Lokal-först-arkitektur
- Ingen dataöverföring till molnet (lokalt läge)
- Krypterad lagring av konversationer
- Säker hantering av autentiseringsuppgifter

### Applikationssäkerhet
- Sandlåda för renderer-processer
- Content Security Policy (CSP)
- Ingen fjärrkodskörning
- Säker IPC-kommunikation

## Felsökning

### Vanliga problem

**Foundry Local startar inte**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Fel vid modellinladdning**
- Kontrollera tillräckligt med diskutrymme
- Kontrollera internetanslutning för nedladdningar
- Se till att GPU-drivrutiner är uppdaterade
- Testa olika modellvarianter

**Prestandaproblem**
- Övervaka systemresurser
- Justera modellinställningar
- Aktivera hårdvaruacceleration
- Stäng andra resurskrävande applikationer

### Debug-läge
Aktivera felsökningsloggning genom att ställa in miljövariabler:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Bidra

### Utvecklingsinställning
1. Forka repositoryn
2. Skapa en feature branch
3. Installera beroenden: `npm install`
4. Gör ändringar och testa
5. Skicka in en pull request

### Kodstil
- ESLint-konfiguration tillhandahålls
- Prettier för kodformatering
- TypeScript för typkontroll
- JSDoc-kommentarer för dokumentation

## Lärandemål

Efter att ha slutfört detta exempel kommer du att förstå:

1. **Windows 11-inbyggd utveckling**
   - Implementering av Fluent Design System
   - Integration med Windows-funktioner
   - Säkerhetsbästa praxis för Electron

2. **AI-modellintegration**
   - Arkitektur för Foundry Local-tjänsten
   - Hantering av modellens livscykel
   - Övervakning och optimering av prestanda

3. **Realtidssystem för chatt**
   - Hantering av strömmande svar
   - Hantering av konversationsstatus
   - Mönster för användarupplevelse

4. **Utveckling av produktionsapplikationer**
   - Felhantering och återhämtning
   - Prestandaoptimering
   - Säkerhetsöverväganden
   - Teststrategier

## Nästa steg

- **Exempel 09**: Multi-Agent Orchestration System
- **Exempel 10**: Foundry Local som verktygsintegration
- **Avancerade ämnen**: Anpassad modellfinjustering
- **Distribution**: Mönster för företagsdistribution

## Licens

Detta exempel följer samma licens som Microsoft Foundry Local-projektet.

---

