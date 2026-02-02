# Windows 11 Chat Voorbeeld - Foundry Local

Een moderne chatapplicatie voor Windows 11 die Microsoft Foundry Local integreert met een prachtige native interface. Gebouwd met Electron en volgens de officiële Foundry Local richtlijnen van Microsoft.

## Overzicht

Dit voorbeeld laat zien hoe je een productieklare chatapplicatie kunt maken die gebruikmaakt van lokale AI-modellen via Foundry Local, waardoor gebruikers privacygerichte AI-gesprekken kunnen voeren zonder afhankelijkheid van de cloud.

## Functies

### 🎨 **Windows 11 Native Ontwerp**
- Integratie met het Fluent Design System
- Mica-materiaal effecten en transparantie
- Ondersteuning voor native Windows 11 thema's
- Responsieve lay-out voor alle schermformaten
- Automatische schakeling tussen donker/licht modus

### 🤖 **AI Model Integratie**
- Integratie met Foundry Local service
- Ondersteuning voor meerdere modellen met directe wisseling
- Real-time streaming reacties
- Schakeling tussen lokale en cloudmodellen
- Monitoring en status van modelgezondheid

### 💬 **Chatervaring**
- Real-time typindicatoren
- Persistente berichtgeschiedenis
- Exporteren van chatgesprekken
- Aangepaste systeem prompts
- Beheer en vertakking van gesprekken

### ⚡ **Prestatiekenmerken**
- Lazy loading en virtualisatie
- Geoptimaliseerde rendering voor lange gesprekken
- Voorladen van modellen op de achtergrond
- Efficiënt geheugenbeheer
- Soepele animaties en overgangen

## Architectuur

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

## Vereisten

### Systeemvereisten
- **OS**: Windows 11 (22H2 of later aanbevolen)
- **RAM**: Minimaal 8GB, 16GB+ aanbevolen voor grotere modellen
- **Opslag**: Minimaal 10GB vrije ruimte voor modellen
- **GPU**: Optioneel maar aanbevolen voor snellere inferentie

### Softwarevereisten
- **Node.js**: v18.0.0 of later
- **Foundry Local**: Laatste versie van Microsoft
- **Git**: Voor klonen en ontwikkeling

## Installatie

### 1. Installeer Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clone en Setup
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configureer Omgeving
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Start de Applicatie
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projectstructuur

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

## Diepgaande Uitleg van Belangrijke Functies

### Windows 11 Integratie

**Fluent Design System**
- Mica achtergrondmaterialen
- Acrylic transparantie-effecten
- Afgeronde hoeken en moderne spacing
- Native Windows 11 kleurenpalet
- Semantische kleur tokens voor toegankelijkheid

**Native Windows Functies**
- Jump list integratie voor recente chats
- Windows notificaties voor nieuwe berichten
- Taakbalkvoortgang voor modeloperaties
- Systeemvak integratie met snelle acties
- Ondersteuning voor Windows Hello authenticatie

### AI Modelbeheer

**Lokale Modellen**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybride Cloud/Lokale Ondersteuning**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chatinterface Functies

**Real-time Streaming**
- Token-voor-token weergave van reacties
- Soepele typanimaties
- Annuleerbare verzoeken
- Typindicatoren en status

**Gespreksbeheer**
- Persistente chatgeschiedenis
- Exporteren/importeren van gesprekken
- Bericht zoeken en filteren
- Vertakking van gesprekken
- Aangepaste systeem prompts per gesprek

**Toegankelijkheid**
- Volledige toetsenbordnavigatie
- Compatibiliteit met schermlezers
- Ondersteuning voor hoog contrast modus
- Aanpasbare lettergroottes
- Integratie van spraakinvoer

## Gebruik Voorbeelden

### Basis Chat Integratie
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

### Modelbeheer
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

### Instellingen en Aanpassingen
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

## Configuratieopties

### Applicatie-instellingen
- **Thema**: Automatisch, licht, donker modus
- **Model**: Standaard modelselectie
- **Prestaties**: Inferentie-instellingen
- **Privacy**: Beleid voor gegevensbewaring
- **Notificaties**: Berichtmeldingen
- **Sneltoetsen**: Toetsenbord sneltoetsen

### Chatinstellingen
- **Streaming**: Inschakelen/uitschakelen van real-time reacties
- **Contextlengte**: Gespreksgeheugen
- **Temperatuur**: Creativiteit van reacties
- **Max Tokens**: Limieten voor lengte van reacties
- **Systeem Prompts**: Standaard gedrag van assistent

### Modelinstellingen
- **Automatisch downloaden**: Automatische modelupdates
- **Cachegrootte**: Limieten voor lokale modelopslag
- **Prestatiemodus**: Voorkeuren voor CPU vs GPU
- **Gezondheidscontroles**: Monitoringintervallen

## Ontwikkeling

### Bouwen vanuit Bron
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

### Debuggen
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testen
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Prestatieoptimalisatie

### Geheugenbeheer
- Efficiënte berichtvirtualisatie
- Automatische garbage collection
- Monitoring van modelgeheugen
- Opruimen van bronnen bij afsluiten

### Renderingoptimalisatie
- Virtueel scrollen voor lange gesprekken
- Lazy loading van berichtgeschiedenis
- Geoptimaliseerde React/DOM updates
- GPU-versnelde animaties

### Netwerkoptimalisatie
- Verbinding pooling
- Batchen van verzoeken
- Automatische retry-logica
- Ondersteuning voor offline modus

## Veiligheidsoverwegingen

### Gegevensprivacy
- Lokale-first architectuur
- Geen cloudgegevensoverdracht (lokale modus)
- Versleutelde opslag van gesprekken
- Beveiligd beheer van inloggegevens

### Applicatiebeveiliging
- Gesandboxte rendererprocessen
- Content Security Policy (CSP)
- Geen uitvoering van externe code
- Beveiligde IPC-communicatie

## Probleemoplossing

### Veelvoorkomende Problemen

**Foundry Local Start Niet**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Model Laadfouten**
- Controleer voldoende schijfruimte
- Controleer internetverbinding voor downloads
- Zorg dat GPU-drivers up-to-date zijn
- Probeer verschillende modelvarianten

**Prestatieproblemen**
- Monitor systeembronnen
- Pas modelinstellingen aan
- Schakel hardwareversnelling in
- Sluit andere resource-intensieve applicaties

### Debugmodus
Schakel debug logging in door omgevingsvariabelen in te stellen:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Bijdragen

### Ontwikkelomgeving Instellen
1. Fork de repository
2. Maak een feature branch
3. Installeer afhankelijkheden: `npm install`
4. Maak wijzigingen en test
5. Dien een pull request in

### Code Stijl
- ESLint configuratie beschikbaar
- Prettier voor code formatting
- TypeScript voor typeveiligheid
- JSDoc commentaar voor documentatie

## Leerresultaten

Na het voltooien van dit voorbeeld begrijp je:

1. **Windows 11 Native Ontwikkeling**
   - Implementatie van Fluent Design System
   - Integratie met Windows native functies
   - Beste praktijken voor Electron beveiliging

2. **AI Model Integratie**
   - Architectuur van Foundry Local service
   - Beheer van modellevenscyclus
   - Monitoring en optimalisatie van prestaties

3. **Real-time Chat Systemen**
   - Afhandeling van streaming reacties
   - Beheer van gespreksstatus
   - Gebruikerservaring patronen

4. **Productie Applicatie Ontwikkeling**
   - Foutafhandeling en herstel
   - Prestatieoptimalisatie
   - Veiligheidsoverwegingen
   - Teststrategieën

## Volgende Stappen

- **Voorbeeld 09**: Multi-Agent Orchestration System
- **Voorbeeld 10**: Foundry Local als Tools Integratie
- **Geavanceerde Onderwerpen**: Aangepaste model fine-tuning
- **Implementatie**: Patronen voor bedrijfsimplementatie

## Licentie

Dit voorbeeld volgt dezelfde licentie als het Microsoft Foundry Local project.

---

