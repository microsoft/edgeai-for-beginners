# Windows 11 Chat Sample - Foundry Local

Un'applicazione chat moderna per Windows 11 che integra Microsoft Foundry Local con un'interfaccia nativa elegante. Costruita con Electron e seguendo i modelli ufficiali di Microsoft Foundry Local.

## Panoramica

Questo esempio dimostra come creare un'applicazione chat pronta per la produzione che utilizza modelli di intelligenza artificiale locali tramite Foundry Local, offrendo agli utenti conversazioni AI focalizzate sulla privacy senza dipendenze dal cloud.

## Funzionalità

### 🎨 **Design Nativo di Windows 11**
- Integrazione con il Fluent Design System
- Effetti materiali Mica e trasparenza
- Supporto per il tema nativo di Windows 11
- Layout reattivo per tutte le dimensioni dello schermo
- Passaggio automatico tra modalità chiara/scura

### 🤖 **Integrazione Modelli AI**
- Integrazione con il servizio Foundry Local
- Supporto per modelli multipli con cambio rapido
- Risposte in streaming in tempo reale
- Passaggio tra modelli locali e cloud
- Monitoraggio dello stato e della salute dei modelli

### 💬 **Esperienza Chat**
- Indicatori di digitazione in tempo reale
- Persistenza della cronologia dei messaggi
- Esportazione delle conversazioni
- Prompt di sistema personalizzati
- Gestione e ramificazione delle conversazioni

### ⚡ **Funzionalità di Prestazioni**
- Caricamento ritardato e virtualizzazione
- Rendering ottimizzato per conversazioni lunghe
- Precaricamento dei modelli in background
- Gestione efficiente della memoria
- Animazioni e transizioni fluide

## Architettura

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

## Prerequisiti

### Requisiti di Sistema
- **OS**: Windows 11 (22H2 o successivo consigliato)
- **RAM**: Minimo 8GB, 16GB+ consigliati per modelli più grandi
- **Storage**: Spazio libero di almeno 10GB per i modelli
- **GPU**: Facoltativa ma consigliata per inferenze più rapide

### Dipendenze Software
- **Node.js**: v18.0.0 o successivo
- **Foundry Local**: Ultima versione da Microsoft
- **Git**: Per clonazione e sviluppo

## Installazione

### 1. Installa Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clona e Configura
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configura l'Ambiente
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Avvia l'Applicazione
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Struttura del Progetto

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

## Approfondimento delle Funzionalità Chiave

### Integrazione con Windows 11

**Fluent Design System**
- Materiali di sfondo Mica
- Effetti di trasparenza Acrylic
- Angoli arrotondati e spaziatura moderna
- Palette di colori nativa di Windows 11
- Token di colore semantico per l'accessibilità

**Funzionalità Nativa di Windows**
- Integrazione con la Jump List per le chat recenti
- Notifiche di Windows per nuovi messaggi
- Barra delle attività con progressi per operazioni sui modelli
- Integrazione con il vassoio di sistema con azioni rapide
- Supporto per l'autenticazione Windows Hello

### Gestione dei Modelli AI

**Modelli Locali**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Supporto Ibrido Cloud/Locale**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funzionalità dell'Interfaccia Chat

**Streaming in Tempo Reale**
- Visualizzazione delle risposte token per token
- Animazioni di digitazione fluide
- Richieste annullabili
- Indicatori di digitazione e stato

**Gestione delle Conversazioni**
- Cronologia chat persistente
- Esportazione/importazione delle conversazioni
- Ricerca e filtraggio dei messaggi
- Ramificazione delle conversazioni
- Prompt di sistema personalizzati per conversazione

**Accessibilità**
- Navigazione completa tramite tastiera
- Compatibilità con lettori di schermo
- Supporto per modalità ad alto contrasto
- Dimensioni dei caratteri personalizzabili
- Integrazione input vocale

## Esempi di Utilizzo

### Integrazione Chat di Base
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

### Gestione dei Modelli
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

### Impostazioni e Personalizzazione
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

## Opzioni di Configurazione

### Impostazioni dell'Applicazione
- **Tema**: Modalità automatica, chiara, scura
- **Modello**: Selezione del modello predefinito
- **Prestazioni**: Impostazioni di inferenza
- **Privacy**: Politiche di conservazione dei dati
- **Notifiche**: Avvisi sui messaggi
- **Scorciatoie**: Scorciatoie da tastiera

### Impostazioni Chat
- **Streaming**: Abilita/disabilita risposte in tempo reale
- **Lunghezza del Contesto**: Memoria della conversazione
- **Temperatura**: Creatività delle risposte
- **Max Tokens**: Limiti di lunghezza delle risposte
- **Prompt di Sistema**: Comportamento predefinito dell'assistente

### Impostazioni Modello
- **Auto-download**: Aggiornamenti automatici dei modelli
- **Cache Size**: Limiti di archiviazione dei modelli locali
- **Performance Mode**: Preferenze CPU vs GPU
- **Health Checks**: Intervalli di monitoraggio

## Sviluppo

### Costruire dal Codice Sorgente
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

### Testing
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Ottimizzazione delle Prestazioni

### Gestione della Memoria
- Virtualizzazione efficiente dei messaggi
- Raccolta automatica dei rifiuti
- Monitoraggio della memoria dei modelli
- Pulizia delle risorse alla chiusura

### Ottimizzazione del Rendering
- Scorrimento virtuale per conversazioni lunghe
- Caricamento ritardato della cronologia dei messaggi
- Aggiornamenti React/DOM ottimizzati
- Animazioni accelerate dalla GPU

### Ottimizzazione della Rete
- Pooling delle connessioni
- Raggruppamento delle richieste
- Logica di retry automatico
- Supporto per modalità offline

## Considerazioni sulla Sicurezza

### Privacy dei Dati
- Architettura locale-first
- Nessuna trasmissione di dati al cloud (modalità locale)
- Archiviazione delle conversazioni crittografata
- Gestione sicura delle credenziali

### Sicurezza dell'Applicazione
- Processi di rendering isolati
- Content Security Policy (CSP)
- Nessuna esecuzione di codice remoto
- Comunicazione IPC sicura

## Risoluzione dei Problemi

### Problemi Comuni

**Foundry Local Non Si Avvia**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Errori di Caricamento dei Modelli**
- Verifica dello spazio su disco disponibile
- Controlla la connessione internet per i download
- Assicurati che i driver GPU siano aggiornati
- Prova varianti di modelli diversi

**Problemi di Prestazioni**
- Monitora le risorse di sistema
- Regola le impostazioni del modello
- Abilita l'accelerazione hardware
- Chiudi altre applicazioni che consumano molte risorse

### Modalità Debug
Abilita il logging di debug impostando variabili di ambiente:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contributi

### Configurazione per lo Sviluppo
1. Effettua un fork del repository
2. Crea un branch per la funzionalità
3. Installa le dipendenze: `npm install`
4. Apporta modifiche e testa
5. Invia una pull request

### Stile del Codice
- Configurazione ESLint fornita
- Prettier per la formattazione del codice
- TypeScript per la sicurezza dei tipi
- Commenti JSDoc per la documentazione

## Obiettivi di Apprendimento

Dopo aver completato questo esempio, comprenderai:

1. **Sviluppo Nativo per Windows 11**
   - Implementazione del Fluent Design System
   - Integrazione nativa con Windows
   - Best practices di sicurezza per Electron

2. **Integrazione Modelli AI**
   - Architettura del servizio Foundry Local
   - Gestione del ciclo di vita dei modelli
   - Monitoraggio e ottimizzazione delle prestazioni

3. **Sistemi Chat in Tempo Reale**
   - Gestione delle risposte in streaming
   - Gestione dello stato delle conversazioni
   - Modelli di esperienza utente

4. **Sviluppo di Applicazioni per la Produzione**
   - Gestione degli errori e recupero
   - Ottimizzazione delle prestazioni
   - Considerazioni sulla sicurezza
   - Strategie di testing

## Prossimi Passi

- **Esempio 09**: Sistema di Orchestrazione Multi-Agente
- **Esempio 10**: Foundry Local come Integrazione di Strumenti
- **Argomenti Avanzati**: Fine-tuning personalizzato dei modelli
- **Distribuzione**: Modelli di distribuzione aziendale

## Licenza

Questo esempio segue la stessa licenza del progetto Microsoft Foundry Local.

---

