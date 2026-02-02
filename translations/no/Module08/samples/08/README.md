# Windows 11 Chat Eksempel - Foundry Local

En moderne chatapplikasjon for Windows 11 som integrerer Microsoft Foundry Local med et vakkert, naturlig grensesnitt. Bygget med Electron og følger Microsofts offisielle Foundry Local-mønstre.

## Oversikt

Dette eksemplet viser hvordan man lager en produksjonsklar chatapplikasjon som bruker lokale AI-modeller via Foundry Local, og gir brukerne personvernfokuserte AI-samtaler uten avhengighet av skyen.

## Funksjoner

### 🎨 **Windows 11 Naturlig Design**
- Integrasjon med Fluent Design System
- Mica-materialeffekter og gjennomsiktighet
- Støtte for naturlig Windows 11-tema
- Responsivt oppsett for alle skjermstørrelser
- Automatisk bytte mellom mørk/lys modus

### 🤖 **AI-modellintegrasjon**
- Integrasjon med Foundry Local-tjenesten
- Støtte for flere modeller med mulighet for bytte
- Sanntidsstrømming av svar
- Bytte mellom lokale og skybaserte modeller
- Overvåking av modellens helse og status

### 💬 **Chatopplevelse**
- Sanntids skriveindikatorer
- Vedvarende meldingshistorikk
- Eksport av chat-samtaler
- Tilpassede systemprompter
- Forgrening og administrasjon av samtaler

### ⚡ **Ytelsesfunksjoner**
- Lazy loading og virtualisering
- Optimalisert rendering for lange samtaler
- Forhåndslasting av modeller i bakgrunnen
- Effektiv minnehåndtering
- Glatte animasjoner og overganger

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

## Forutsetninger

### Systemkrav
- **OS**: Windows 11 (22H2 eller nyere anbefalt)
- **RAM**: Minimum 8GB, 16GB+ anbefalt for større modeller
- **Lagring**: 10GB+ ledig plass for modeller
- **GPU**: Valgfritt, men anbefalt for raskere inferens

### Programvareavhengigheter
- **Node.js**: v18.0.0 eller nyere
- **Foundry Local**: Nyeste versjon fra Microsoft
- **Git**: For kloning og utvikling

## Installasjon

### 1. Installer Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klon og sett opp
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurer miljøet
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Kjør applikasjonen
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Prosjektstruktur

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

## Dypdykk i nøkkelfunksjoner

### Windows 11-integrasjon

**Fluent Design System**
- Mica bakgrunnsmaterialer
- Akryl-gjennomsiktighetseffekter
- Runde hjørner og moderne avstand
- Naturlig Windows 11 fargepalett
- Semantiske fargetokens for tilgjengelighet

**Naturlige Windows-funksjoner**
- Jump list-integrasjon for nylige samtaler
- Windows-varsler for nye meldinger
- Oppgavelinjeprogresjon for modelloperasjoner
- Systemtray-integrasjon med hurtigtilgang
- Støtte for Windows Hello-autentisering

### AI-modelladministrasjon

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

**Hybrid sky/lokal støtte**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chatgrensesnittfunksjoner

**Sanntidsstrømming**
- Token-for-token visning av svar
- Glatte skriveanimasjoner
- Avbrytbare forespørsler
- Skriveindikatorer og status

**Samtaleadministrasjon**
- Vedvarende chat-historikk
- Eksport/import av samtaler
- Søking og filtrering av meldinger
- Forgrening av samtaler
- Tilpassede systemprompter per samtale

**Tilgjengelighet**
- Full tastaturnavigasjon
- Kompatibilitet med skjermlesere
- Støtte for høy kontrastmodus
- Tilpassbare skrifttyper
- Integrasjon av stemmeinput

## Brukseksempler

### Grunnleggende chatintegrasjon
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

### Modelladministrasjon
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

### Innstillinger og tilpasning
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

## Konfigurasjonsalternativer

### Applikasjonsinnstillinger
- **Tema**: Auto, lys, mørk modus
- **Modell**: Standard modellvalg
- **Ytelse**: Innstillinger for inferens
- **Personvern**: Retningslinjer for datalagring
- **Varsler**: Meldingsvarsler
- **Snarveier**: Tastatursnarveier

### Chatinnstillinger
- **Strømming**: Aktiver/deaktiver sanntidssvar
- **Kontekstlengde**: Samtaleminne
- **Temperatur**: Kreativitet i svar
- **Maks tokens**: Begrensninger på svarlengde
- **Systemprompter**: Standard assistentoppførsel

### Modellinnstillinger
- **Automatisk nedlasting**: Automatiske modelloppdateringer
- **Cache-størrelse**: Begrensninger for lokal modellagring
- **Ytelsesmodus**: CPU vs GPU preferanser
- **Helsesjekker**: Overvåkingsintervaller

## Utvikling

### Bygge fra kilde
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

### Feilsøking
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testing
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Ytelsesoptimalisering

### Minnehåndtering
- Effektiv virtualisering av meldinger
- Automatisk søppelinnsamling
- Overvåking av modellminne
- Ressursopprydding ved avslutning

### Renderingoptimalisering
- Virtuell scrolling for lange samtaler
- Lazy loading av meldingshistorikk
- Optimaliserte React/DOM-oppdateringer
- GPU-akselererte animasjoner

### Nettverksoptimalisering
- Tilkoblingspooling
- Batch-behandling av forespørsler
- Automatisk gjenopprykkingslogikk
- Støtte for offline modus

## Sikkerhetsvurderinger

### Datapersonvern
- Lokal-først arkitektur
- Ingen skydataoverføring (lokal modus)
- Kryptert samtalelagring
- Sikker håndtering av legitimasjon

### Applikasjonssikkerhet
- Sandkasse for renderer-prosesser
- Content Security Policy (CSP)
- Ingen ekstern kodeutførelse
- Sikker IPC-kommunikasjon

## Feilsøking

### Vanlige problemer

**Foundry Local starter ikke**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Feil ved modelllasting**
- Kontroller tilstrekkelig diskplass
- Sjekk internettforbindelsen for nedlastinger
- Sørg for at GPU-drivere er oppdatert
- Prøv forskjellige modellvarianter

**Ytelsesproblemer**
- Overvåk systemressurser
- Juster modellinnstillinger
- Aktiver maskinvareakselerasjon
- Lukk andre ressurskrevende applikasjoner

### Feilmodus
Aktiver feillogging ved å sette miljøvariabler:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Bidra

### Utviklingsoppsett
1. Fork prosjektet
2. Opprett en funksjonsgren
3. Installer avhengigheter: `npm install`
4. Gjør endringer og test
5. Send inn en pull request

### Kodestil
- ESLint-konfigurasjon inkludert
- Prettier for kodeformatering
- TypeScript for typesikkerhet
- JSDoc-kommentarer for dokumentasjon

## Læringsutbytte

Etter å ha fullført dette eksemplet, vil du forstå:

1. **Windows 11 Naturlig Utvikling**
   - Implementering av Fluent Design System
   - Naturlig Windows-integrasjon
   - Beste praksis for Electron-sikkerhet

2. **AI-modellintegrasjon**
   - Foundry Local tjenestearkitektur
   - Livssyklusadministrasjon for modeller
   - Ytelsesovervåking og optimalisering

3. **Sanntidssystemsamtaler**
   - Håndtering av strømmingssvar
   - Administrasjon av samtaletilstand
   - Brukeropplevelsesmønstre

4. **Utvikling av produksjonsapplikasjoner**
   - Feilhåndtering og gjenoppretting
   - Ytelsesoptimalisering
   - Sikkerhetsvurderinger
   - Teststrategier

## Neste steg

- **Eksempel 09**: Multi-Agent Orchestration System
- **Eksempel 10**: Foundry Local som verktøyintegrasjon
- **Avanserte emner**: Tilpasning av modeller
- **Distribusjon**: Mønstre for bedriftsdistribusjon

## Lisens

Dette eksemplet følger samme lisens som Microsoft Foundry Local-prosjektet.

---

