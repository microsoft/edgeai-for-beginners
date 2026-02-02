# Windows 11 Chat Sample - Foundry Local

Isang modernong chat application para sa Windows 11 na nag-iintegrate ng Microsoft Foundry Local gamit ang maganda at native na interface. Ginawa gamit ang Electron at sumusunod sa opisyal na mga pattern ng Microsoft Foundry Local.

## Pangkalahatang-ideya

Ipinapakita ng sample na ito kung paano gumawa ng isang production-ready na chat application na gumagamit ng lokal na AI models sa pamamagitan ng Foundry Local, na nagbibigay sa mga user ng privacy-focused na AI conversations nang walang cloud dependencies.

## Mga Tampok

### 🎨 **Windows 11 Native Design**
- Integrasyon ng Fluent Design System
- Mga epekto ng Mica material at transparency
- Suporta sa native na tema ng Windows 11
- Responsive na layout para sa lahat ng laki ng screen
- Awtomatikong paglipat sa Dark/Light mode

### 🤖 **Integrasyon ng AI Model**
- Integrasyon ng Foundry Local service
- Suporta sa maraming modelo na may hot-swapping
- Real-time na streaming na mga tugon
- Paglipat sa lokal at cloud na modelo
- Pagsubaybay sa kalusugan ng modelo at status

### 💬 **Karanasan sa Chat**
- Real-time na mga indicator ng pagta-type
- Pagpapanatili ng kasaysayan ng mensahe
- Pag-export ng mga chat conversation
- Custom na mga system prompt
- Pamamahala at pag-branch ng mga pag-uusap

### ⚡ **Mga Tampok sa Performance**
- Lazy loading at virtualization
- Optimized na rendering para sa mahahabang pag-uusap
- Background na preloading ng modelo
- Mahusay na pamamahala ng memorya
- Smooth na mga animation at transition

## Arkitektura

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

## Mga Kinakailangan

### Mga Kinakailangan sa Sistema
- **OS**: Windows 11 (22H2 o mas bago ay inirerekomenda)
- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+ para sa mas malalaking modelo
- **Storage**: 10GB+ na libreng espasyo para sa mga modelo
- **GPU**: Opsyonal ngunit inirerekomenda para sa mas mabilis na inference

### Mga Software na Kinakailangan
- **Node.js**: v18.0.0 o mas bago
- **Foundry Local**: Pinakabagong bersyon mula sa Microsoft
- **Git**: Para sa cloning at development

## Pag-install

### 1. I-install ang Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. I-clone at I-setup
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. I-configure ang Environment
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Patakbuhin ang Application
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Estruktura ng Proyekto

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

## Malalim na Pagsusuri ng Mga Pangunahing Tampok

### Integrasyon ng Windows 11

**Fluent Design System**
- Mga materyal na background ng Mica
- Mga epekto ng acrylic transparency
- Mga bilog na sulok at modernong spacing
- Native na color palette ng Windows 11
- Semantic na mga color token para sa accessibility

**Mga Native na Tampok ng Windows**
- Jump list integration para sa mga kamakailang chat
- Mga notification ng Windows para sa mga bagong mensahe
- Taskbar progress para sa mga operasyon ng modelo
- Integrasyon ng system tray na may quick actions
- Suporta sa Windows Hello authentication

### Pamamahala ng AI Model

**Lokal na Mga Modelo**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybrid Cloud/Lokal na Suporta**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Mga Tampok ng Chat Interface

**Real-time na Streaming**
- Token-by-token na pagpapakita ng tugon
- Smooth na mga animation ng pagta-type
- Mga kanselableng request
- Mga indicator ng pagta-type at status

**Pamamahala ng Pag-uusap**
- Persistent na kasaysayan ng chat
- Pag-export/import ng pag-uusap
- Paghahanap at pag-filter ng mensahe
- Pag-branch ng pag-uusap
- Custom na mga system prompt bawat pag-uusap

**Accessibility**
- Buong keyboard navigation
- Compatibility sa screen reader
- Suporta sa high contrast mode
- Customizable na laki ng font
- Integrasyon ng voice input

## Mga Halimbawa ng Paggamit

### Basic na Integrasyon ng Chat
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

### Pamamahala ng Modelo
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

### Mga Setting at Customization
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

## Mga Opsyon sa Configuration

### Mga Setting ng Application
- **Tema**: Auto, Light, Dark mode
- **Modelo**: Default na pagpili ng modelo
- **Performance**: Mga setting ng inference
- **Privacy**: Mga patakaran sa pag-retain ng data
- **Mga Notification**: Mga alerto sa mensahe
- **Mga Shortcut**: Mga shortcut sa keyboard

### Mga Setting ng Chat
- **Streaming**: Paganahin/huwag paganahin ang real-time na mga tugon
- **Context Length**: Memorya ng pag-uusap
- **Temperature**: Pagkamalikhain ng tugon
- **Max Tokens**: Mga limitasyon sa haba ng tugon
- **System Prompts**: Default na pag-uugali ng assistant

### Mga Setting ng Modelo
- **Auto-download**: Awtomatikong pag-update ng modelo
- **Cache Size**: Mga limitasyon sa lokal na storage ng modelo
- **Performance Mode**: Mga kagustuhan sa CPU vs GPU
- **Health Checks**: Mga interval ng pagsubaybay

## Pag-develop

### Pagbuo mula sa Source
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

### Pagsusuri
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Pag-optimize ng Performance

### Pamamahala ng Memorya
- Mahusay na virtualization ng mensahe
- Awtomatikong garbage collection
- Pagsubaybay sa memorya ng modelo
- Paglilinis ng resources sa pag-exit

### Pag-optimize ng Rendering
- Virtual scrolling para sa mahahabang pag-uusap
- Lazy loading ng kasaysayan ng mensahe
- Optimized na React/DOM updates
- GPU-accelerated na mga animation

### Pag-optimize ng Network
- Connection pooling
- Request batching
- Awtomatikong retry logic
- Suporta sa offline mode

## Mga Pagsasaalang-alang sa Seguridad

### Privacy ng Data
- Lokal-first na arkitektura
- Walang cloud data transmission (lokal na mode)
- Encrypted na storage ng pag-uusap
- Secure na pamamahala ng kredensyal

### Seguridad ng Application
- Sandboxed na mga renderer process
- Content Security Policy (CSP)
- Walang remote code execution
- Secure na komunikasyon ng IPC

## Pag-troubleshoot

### Mga Karaniwang Isyu

**Foundry Local Hindi Nag-iistart**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Mga Pagkabigo sa Pag-load ng Modelo**
- Siguraduhing may sapat na espasyo sa disk
- Suriin ang koneksyon sa internet para sa mga download
- Siguraduhing updated ang mga driver ng GPU
- Subukan ang iba't ibang variant ng modelo

**Mga Isyu sa Performance**
- Subaybayan ang mga resource ng sistema
- Ayusin ang mga setting ng modelo
- Paganahin ang hardware acceleration
- Isara ang iba pang resource-intensive na application

### Debug Mode
Paganahin ang debug logging sa pamamagitan ng pag-set ng environment variables:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Pag-contribute

### Setup ng Development
1. I-fork ang repository
2. Gumawa ng feature branch
3. I-install ang mga dependency: `npm install`
4. Gumawa ng mga pagbabago at subukan
5. Mag-submit ng pull request

### Code Style
- May kasamang ESLint configuration
- Prettier para sa pag-format ng code
- TypeScript para sa type safety
- JSDoc comments para sa dokumentasyon

## Mga Matutunan

Pagkatapos makumpleto ang sample na ito, mauunawaan mo:

1. **Windows 11 Native Development**
   - Implementasyon ng Fluent Design System
   - Integrasyon ng native na Windows
   - Mga best practice sa seguridad ng Electron

2. **Integrasyon ng AI Model**
   - Arkitektura ng Foundry Local service
   - Pamamahala ng lifecycle ng modelo
   - Pagsubaybay at pag-optimize ng performance

3. **Real-time na Chat Systems**
   - Paghawak ng streaming na tugon
   - Pamamahala ng estado ng pag-uusap
   - Mga pattern sa karanasan ng user

4. **Pag-develop ng Production Application**
   - Paghawak ng error at recovery
   - Pag-optimize ng performance
   - Mga pagsasaalang-alang sa seguridad
   - Mga estratehiya sa pagsusuri

## Mga Susunod na Hakbang

- **Sample 09**: Multi-Agent Orchestration System
- **Sample 10**: Foundry Local bilang Tools Integration
- **Mga Advanced na Paksa**: Custom na fine-tuning ng modelo
- **Deployment**: Mga pattern sa enterprise deployment

## Lisensya

Ang sample na ito ay sumusunod sa parehong lisensya ng Microsoft Foundry Local project.

---

