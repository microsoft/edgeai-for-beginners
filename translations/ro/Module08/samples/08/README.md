# Windows 11 Chat Sample - Foundry Local

O aplicație modernă de chat pentru Windows 11 care integrează Microsoft Foundry Local cu o interfață nativă elegantă. Construită cu Electron și urmând modelele oficiale Foundry Local de la Microsoft.

## Prezentare Generală

Acest exemplu demonstrează cum să creezi o aplicație de chat pregătită pentru producție, care utilizează modele AI locale prin Foundry Local, oferind utilizatorilor conversații AI axate pe confidențialitate, fără dependențe de cloud.

## Funcționalități

### 🎨 **Design Nativ Windows 11**
- Integrare cu Fluent Design System
- Efecte de material Mica și transparență
- Suport pentru tematică nativă Windows 11
- Layout responsiv pentru toate dimensiunile ecranului
- Comutare automată între modurile întunecat/luminos

### 🤖 **Integrare Model AI**
- Integrare cu serviciul Foundry Local
- Suport pentru modele multiple cu schimbare rapidă
- Răspunsuri în timp real prin streaming
- Comutare între modele locale și cloud
- Monitorizarea sănătății și stării modelelor

### 💬 **Experiență de Chat**
- Indicatori de tastare în timp real
- Persistența istoricului mesajelor
- Exportul conversațiilor de chat
- Prompteri de sistem personalizate
- Ramificarea și gestionarea conversațiilor

### ⚡ **Funcționalități de Performanță**
- Încărcare întârziată și virtualizare
- Redare optimizată pentru conversații lungi
- Preîncărcarea modelelor în fundal
- Gestionarea eficientă a memoriei
- Animații și tranziții fluide

## Arhitectură

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

## Cerințe Prealabile

### Cerințe de Sistem
- **OS**: Windows 11 (22H2 sau mai recent recomandat)
- **RAM**: Minimum 8GB, 16GB+ recomandat pentru modele mai mari
- **Spațiu de stocare**: Minimum 10GB liber pentru modele
- **GPU**: Opțional, dar recomandat pentru inferență mai rapidă

### Dependențe Software
- **Node.js**: v18.0.0 sau mai recent
- **Foundry Local**: Ultima versiune de la Microsoft
- **Git**: Pentru clonare și dezvoltare

## Instalare

### 1. Instalează Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clonează și Configurează
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configurează Mediul
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Rulează Aplicația
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Structura Proiectului

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

## Detalii Funcționalități Cheie

### Integrare Windows 11

**Fluent Design System**
- Materiale de fundal Mica
- Efecte de transparență Acrylic
- Colțuri rotunjite și spațiere modernă
- Paletă de culori nativă Windows 11
- Tokenuri de culoare semantice pentru accesibilitate

**Funcționalități Native Windows**
- Integrare cu lista de salturi pentru chat-uri recente
- Notificări Windows pentru mesaje noi
- Progres în bara de activități pentru operațiuni ale modelului
- Integrare în tava de sistem cu acțiuni rapide
- Suport pentru autentificare Windows Hello

### Gestionarea Modelelor AI

**Modele Locale**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Suport Hibrid Cloud/Local**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funcționalități Interfață Chat

**Streaming în Timp Real**
- Afișarea răspunsurilor token cu token
- Animații fluide de tastare
- Cereri anulabile
- Indicatori de tastare și stare

**Gestionarea Conversațiilor**
- Istoric de chat persistent
- Export/import conversații
- Căutare și filtrare mesaje
- Ramificarea conversațiilor
- Prompteri de sistem personalizate pentru fiecare conversație

**Accesibilitate**
- Navigare completă cu tastatura
- Compatibilitate cu cititoare de ecran
- Suport pentru mod de contrast ridicat
- Dimensiuni personalizabile ale fontului
- Integrare input vocal

## Exemple de Utilizare

### Integrare de Bază Chat
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

### Gestionarea Modelelor
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

### Setări și Personalizare
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

## Opțiuni de Configurare

### Setări Aplicație
- **Temă**: Mod automat, luminos, întunecat
- **Model**: Selectarea modelului implicit
- **Performanță**: Setări de inferență
- **Confidențialitate**: Politici de retenție a datelor
- **Notificări**: Alerte pentru mesaje
- **Scurtături**: Scurtături de tastatură

### Setări Chat
- **Streaming**: Activare/dezactivare răspunsuri în timp real
- **Lungime Context**: Memoria conversației
- **Temperatură**: Creativitatea răspunsurilor
- **Max Tokens**: Limite de lungime a răspunsurilor
- **Prompteri de Sistem**: Comportamentul implicit al asistentului

### Setări Model
- **Descărcare Automată**: Actualizări automate ale modelelor
- **Dimensiune Cache**: Limite de stocare pentru modele locale
- **Mod Performanță**: Preferințe CPU vs GPU
- **Verificări de Sănătate**: Intervale de monitorizare

## Dezvoltare

### Construirea din Sursă
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

### Depanare
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testare
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimizare Performanță

### Gestionarea Memoriei
- Virtualizare eficientă a mesajelor
- Colectare automată de gunoi
- Monitorizarea memoriei modelului
- Curățarea resurselor la ieșire

### Optimizare Redare
- Derulare virtuală pentru conversații lungi
- Încărcare întârziată a istoricului mesajelor
- Actualizări optimizate React/DOM
- Animații accelerate de GPU

### Optimizare Rețea
- Grupare conexiuni
- Grupare cereri
- Logică automată de retry
- Suport pentru modul offline

## Considerații de Securitate

### Confidențialitatea Datelor
- Arhitectură locală prioritară
- Fără transmisie de date în cloud (mod local)
- Stocare criptată a conversațiilor
- Gestionare sigură a acreditărilor

### Securitatea Aplicației
- Procese renderer sandboxate
- Politică de Securitate a Conținutului (CSP)
- Fără execuție de cod la distanță
- Comunicare IPC securizată

## Depanare

### Probleme Comune

**Foundry Local Nu Pornește**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Eșecuri la Încărcarea Modelului**
- Verifică spațiul liber pe disc
- Verifică conexiunea la internet pentru descărcări
- Asigură-te că driverele GPU sunt actualizate
- Încearcă variante diferite ale modelului

**Probleme de Performanță**
- Monitorizează resursele sistemului
- Ajustează setările modelului
- Activează accelerarea hardware
- Închide alte aplicații consumatoare de resurse

### Mod Depanare
Activează jurnalizarea de depanare prin setarea variabilelor de mediu:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contribuții

### Configurare Dezvoltare
1. Clonează repository-ul
2. Creează un branch pentru funcționalitate
3. Instalează dependențele: `npm install`
4. Fă modificări și testează
5. Trimite un pull request

### Stil Cod
- Configurație ESLint furnizată
- Prettier pentru formatarea codului
- TypeScript pentru siguranța tipurilor
- Comentarii JSDoc pentru documentare

## Rezultate Învățare

După finalizarea acestui exemplu, vei înțelege:

1. **Dezvoltare Nativă Windows 11**
   - Implementarea Fluent Design System
   - Integrarea nativă Windows
   - Cele mai bune practici de securitate Electron

2. **Integrare Model AI**
   - Arhitectura serviciului Foundry Local
   - Gestionarea ciclului de viață al modelului
   - Monitorizarea și optimizarea performanței

3. **Sisteme de Chat în Timp Real**
   - Gestionarea răspunsurilor prin streaming
   - Gestionarea stării conversației
   - Modele de experiență utilizator

4. **Dezvoltare Aplicație de Producție**
   - Gestionarea erorilor și recuperarea
   - Optimizarea performanței
   - Considerații de securitate
   - Strategii de testare

## Pași Următori

- **Exemplu 09**: Sistem de Orchestrare Multi-Agent
- **Exemplu 10**: Foundry Local ca Integrare de Instrumente
- **Subiecte Avansate**: Ajustarea personalizată a modelului
- **Implementare**: Modele de implementare în mediul enterprise

## Licență

Acest exemplu urmează aceeași licență ca proiectul Microsoft Foundry Local.

---

