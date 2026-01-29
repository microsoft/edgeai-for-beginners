# Windows 11 Chat-Beispiel - Foundry Local

Eine moderne Chat-Anwendung für Windows 11, die Microsoft Foundry Local mit einer ansprechenden nativen Benutzeroberfläche integriert. Entwickelt mit Electron und basierend auf den offiziellen Foundry Local-Mustern von Microsoft.

## Überblick

Dieses Beispiel zeigt, wie man eine produktionsreife Chat-Anwendung erstellt, die lokale KI-Modelle über Foundry Local nutzt. Es ermöglicht datenschutzorientierte KI-Gespräche ohne Cloud-Abhängigkeiten.

## Funktionen

### 🎨 **Windows 11 Native Design**
- Integration des Fluent Design Systems
- Mica-Materialeffekte und Transparenz
- Unterstützung für native Windows 11-Themen
- Responsives Layout für alle Bildschirmgrößen
- Automatischer Wechsel zwischen Dunkel-/Hellmodus

### 🤖 **KI-Modellintegration**
- Integration des Foundry Local-Dienstes
- Unterstützung mehrerer Modelle mit Hot-Swapping
- Echtzeit-Streaming-Antworten
- Wechsel zwischen lokalen und Cloud-Modellen
- Überwachung und Status der Modellgesundheit

### 💬 **Chat-Erlebnis**
- Echtzeit-Tippindikatoren
- Persistenz der Nachrichtenhistorie
- Export von Chat-Gesprächen
- Anpassbare System-Prompts
- Verzweigung und Verwaltung von Gesprächen

### ⚡ **Leistungsmerkmale**
- Lazy Loading und Virtualisierung
- Optimiertes Rendering für lange Gespräche
- Hintergrundvorladen von Modellen
- Effizientes Speichermanagement
- Sanfte Animationen und Übergänge

## Architektur

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

## Voraussetzungen

### Systemanforderungen
- **Betriebssystem**: Windows 11 (22H2 oder später empfohlen)
- **RAM**: Mindestens 8 GB, 16 GB+ empfohlen für größere Modelle
- **Speicherplatz**: Mindestens 10 GB freier Speicherplatz für Modelle
- **GPU**: Optional, aber empfohlen für schnellere Inferenz

### Software-Abhängigkeiten
- **Node.js**: v18.0.0 oder später
- **Foundry Local**: Neueste Version von Microsoft
- **Git**: Zum Klonen und Entwickeln

## Installation

### 1. Foundry Local installieren
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Repository klonen und einrichten
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Umgebung konfigurieren
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Anwendung starten
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

## Detaillierte Funktionen

### Windows 11-Integration

**Fluent Design System**
- Mica-Hintergrundmaterialien
- Acryl-Transparenzeffekte
- Abgerundete Ecken und modernes Layout
- Native Windows 11-Farbpalette
- Semantische Farbtokens für Barrierefreiheit

**Native Windows-Funktionen**
- Integration der Sprungliste für zuletzt verwendete Chats
- Windows-Benachrichtigungen für neue Nachrichten
- Fortschrittsanzeige in der Taskleiste für Modelloperationen
- Integration in das System-Tray mit Schnellaktionen
- Unterstützung für Windows Hello-Authentifizierung

### KI-Modellverwaltung

**Lokale Modelle**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybrid Cloud/Lokale Unterstützung**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chat-Oberflächenfunktionen

**Echtzeit-Streaming**
- Anzeige von Antworten Token für Token
- Sanfte Tippanimationen
- Abbrechbare Anfragen
- Tippindikatoren und Statusanzeige

**Gesprächsverwaltung**
- Persistente Chat-Historie
- Export/Import von Gesprächen
- Nachrichten-Suche und Filterung
- Verzweigung von Gesprächen
- Anpassbare System-Prompts pro Gespräch

**Barrierefreiheit**
- Vollständige Tastaturnavigation
- Kompatibilität mit Bildschirmlesegeräten
- Unterstützung für den Hochkontrastmodus
- Anpassbare Schriftgrößen
- Integration von Spracheingabe

## Anwendungsbeispiele

### Grundlegende Chat-Integration
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

### Modellverwaltung
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

### Einstellungen und Anpassung
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

## Konfigurationsoptionen

### Anwendungseinstellungen
- **Thema**: Automatisch, Hell-, Dunkelmodus
- **Modell**: Standardmodell-Auswahl
- **Leistung**: Inferenz-Einstellungen
- **Datenschutz**: Richtlinien zur Datenaufbewahrung
- **Benachrichtigungen**: Nachrichtenwarnungen
- **Shortcuts**: Tastenkombinationen

### Chat-Einstellungen
- **Streaming**: Echtzeit-Antworten aktivieren/deaktivieren
- **Kontextlänge**: Gesprächsspeicher
- **Temperatur**: Kreativität der Antworten
- **Max Tokens**: Begrenzung der Antwortlänge
- **System-Prompts**: Standardverhalten des Assistenten

### Modelleinstellungen
- **Auto-Download**: Automatische Modellaktualisierungen
- **Cache-Größe**: Begrenzung des lokalen Modell-Speichers
- **Leistungsmodus**: CPU- vs GPU-Präferenzen
- **Gesundheitschecks**: Überwachungsintervalle

## Entwicklung

### Aus dem Quellcode erstellen
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

### Debugging
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Tests
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Leistungsoptimierung

### Speichermanagement
- Effiziente Nachrichtenvirtualisierung
- Automatische Speicherbereinigung
- Überwachung des Modell-Speichers
- Ressourcenbereinigung beim Beenden

### Rendering-Optimierung
- Virtuelles Scrollen für lange Gespräche
- Lazy Loading der Nachrichtenhistorie
- Optimierte React/DOM-Updates
- GPU-beschleunigte Animationen

### Netzwerkoptimierung
- Verbindungspooling
- Batch-Verarbeitung von Anfragen
- Automatische Wiederholungslogik
- Unterstützung für Offline-Modus

## Sicherheitsüberlegungen

### Datenschutz
- Architektur mit lokalem Fokus
- Keine Cloud-Datenübertragung (lokaler Modus)
- Verschlüsselte Speicherung von Gesprächen
- Sichere Verwaltung von Anmeldedaten

### Anwendungssicherheit
- Sandboxed Renderer-Prozesse
- Content Security Policy (CSP)
- Keine Remote-Code-Ausführung
- Sichere IPC-Kommunikation

## Fehlerbehebung

### Häufige Probleme

**Foundry Local startet nicht**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Fehler beim Laden von Modellen**
- Überprüfen Sie den verfügbaren Speicherplatz
- Stellen Sie sicher, dass die Internetverbindung für Downloads funktioniert
- Aktualisieren Sie die GPU-Treiber
- Probieren Sie verschiedene Modellvarianten aus

**Leistungsprobleme**
- Überwachen Sie die Systemressourcen
- Passen Sie die Modelleinstellungen an
- Aktivieren Sie die Hardwarebeschleunigung
- Schließen Sie andere ressourcenintensive Anwendungen

### Debug-Modus
Aktivieren Sie das Debug-Logging, indem Sie Umgebungsvariablen setzen:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Beitrag leisten

### Entwicklungssetup
1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch
3. Installieren Sie Abhängigkeiten: `npm install`
4. Nehmen Sie Änderungen vor und testen Sie diese
5. Reichen Sie einen Pull-Request ein

### Code-Stil
- ESLint-Konfiguration bereitgestellt
- Prettier für Code-Formatierung
- TypeScript für Typensicherheit
- JSDoc-Kommentare für Dokumentation

## Lernziele

Nach Abschluss dieses Beispiels verstehen Sie:

1. **Native Entwicklung für Windows 11**
   - Implementierung des Fluent Design Systems
   - Integration in Windows
   - Sicherheitsbest-Practices für Electron

2. **KI-Modellintegration**
   - Architektur des Foundry Local-Dienstes
   - Lebenszyklusverwaltung von Modellen
   - Leistungsüberwachung und Optimierung

3. **Echtzeit-Chat-Systeme**
   - Umgang mit Streaming-Antworten
   - Verwaltung des Gesprächszustands
   - Benutzererfahrungsmuster

4. **Entwicklung von Produktionsanwendungen**
   - Fehlerbehandlung und Wiederherstellung
   - Leistungsoptimierung
   - Sicherheitsüberlegungen
   - Teststrategien

## Nächste Schritte

- **Beispiel 09**: Multi-Agent-Orchestrierungssystem
- **Beispiel 10**: Foundry Local als Tool-Integration
- **Fortgeschrittene Themen**: Feinabstimmung von benutzerdefinierten Modellen
- **Bereitstellung**: Muster für Unternehmensbereitstellungen

## Lizenz

Dieses Beispiel folgt der gleichen Lizenz wie das Microsoft Foundry Local-Projekt.

---

