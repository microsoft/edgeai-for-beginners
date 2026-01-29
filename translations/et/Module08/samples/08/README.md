# Windows 11 Vestlusrakenduse Näidis - Foundry Local

Kaasaegne vestlusrakendus Windows 11 jaoks, mis integreerib Microsoft Foundry Locali kauni ja loomuliku kasutajaliidesega. Ehitatud Electroni abil ja järgides Microsofti ametlikke Foundry Locali mustreid.

## Ülevaade

See näidis näitab, kuidas luua tootmisvalmis vestlusrakendus, mis kasutab kohalikke AI-mudeleid Foundry Locali kaudu, pakkudes kasutajatele privaatsusele keskendunud AI-vestlusi ilma pilve sõltuvuseta.

## Funktsioonid

### 🎨 **Windows 11 loomulik disain**
- Fluent Design Systemi integreerimine
- Mica materjaliefektid ja läbipaistvus
- Windows 11 loomuliku teemakujunduse tugi
- Kohanduv paigutus kõikidele ekraanisuurustele
- Automaatne tumeda/hele režiimi vahetus

### 🤖 **AI-mudelite integreerimine**
- Foundry Locali teenuse integreerimine
- Mitme mudeli tugi koos kiire vahetamisega
- Reaalajas voogesituse vastused
- Kohalike ja pilvemudelite vahetamine
- Mudeli tervise jälgimine ja olek

### 💬 **Vestluskogemus**
- Reaalajas tippimise indikaatorid
- Sõnumiajaloo säilitamine
- Vestluste eksportimine
- Kohandatud süsteemiküsimused
- Vestluste harutamine ja haldamine

### ⚡ **Jõudlusfunktsioonid**
- Laadimise edasilükkamine ja virtualiseerimine
- Optimeeritud renderdamine pikkade vestluste jaoks
- Mudelite eelkoormamine taustal
- Tõhus mäluhaldus
- Sujuvad animatsioonid ja üleminekud

## Arhitektuur

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

## Eeltingimused

### Süsteeminõuded
- **OS**: Windows 11 (soovitatavalt 22H2 või uuem)
- **RAM**: Minimaalselt 8GB, soovitatavalt 16GB+ suuremate mudelite jaoks
- **Salvestusruum**: 10GB+ vaba ruumi mudelite jaoks
- **GPU**: Valikuline, kuid soovitatav kiiremaks järeldamiseks

### Tarkvaranõuded
- **Node.js**: v18.0.0 või uuem
- **Foundry Local**: Microsofti uusim versioon
- **Git**: Kloonimiseks ja arendamiseks

## Paigaldamine

### 1. Paigalda Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klooni ja seadista
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigureeri keskkond
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Käivita rakendus
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projekti struktuur

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

## Põhifunktsioonide süvaanalüüs

### Windows 11 integreerimine

**Fluent Design System**
- Mica taustamaterjalid
- Akrüül-läbipaistvuse efektid
- Ümarad nurgad ja kaasaegne paigutus
- Windows 11 loomulik värvipalett
- Semantilised värvitokendid ligipääsetavuse jaoks

**Windowsi loomulikud funktsioonid**
- Hüppeloendi integreerimine hiljutiste vestluste jaoks
- Windowsi teavitused uute sõnumite kohta
- Tööriistariba edenemine mudeli toimingute jaoks
- Süsteemisalve integreerimine kiirtoimingutega
- Windows Hello autentimise tugi

### AI-mudelite haldamine

**Kohalikud mudelid**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hübriidne pilv/kohalik tugi**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Vestlusliidese funktsioonid

**Reaalajas voogesitus**
- Vastuste kuvamine token-tokeni kaupa
- Sujuvad tippimisanimatsioonid
- Tühistatavad päringud
- Tippimise indikaatorid ja olek

**Vestluste haldamine**
- Püsiv vestluste ajalugu
- Vestluste eksportimine/importimine
- Sõnumite otsing ja filtreerimine
- Vestluste harutamine
- Kohandatud süsteemiküsimused vestluse kaupa

**Ligipääsetavus**
- Täielik klaviatuuri navigeerimine
- Ekraanilugeja ühilduvus
- Kõrge kontrastsuse režiimi tugi
- Kohandatavad fondi suurused
- Häälkäskluste integreerimine

## Kasutusnäited

### Põhiline vestluse integreerimine
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

### Mudelite haldamine
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

### Seaded ja kohandamine
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

## Konfiguratsioonivalikud

### Rakenduse seaded
- **Teema**: Automaatne, hele, tume režiim
- **Mudel**: Vaikimisi mudeli valik
- **Jõudlus**: Järeldamise seaded
- **Privaatsus**: Andmete säilitamise poliitikad
- **Teavitused**: Sõnumi märguanded
- **Kiirklahvid**: Klaviatuuri otseteed

### Vestluse seaded
- **Voogesitus**: Reaalajas vastuste lubamine/keelamine
- **Konteksti pikkus**: Vestluse mälu
- **Temperatuur**: Vastuste loovus
- **Maksimaalne tokenite arv**: Vastuse pikkuse piirangud
- **Süsteemiküsimused**: Vaikimisi assistendi käitumine

### Mudeli seaded
- **Automaatne allalaadimine**: Mudelite automaatsed uuendused
- **Vahemälu suurus**: Kohalike mudelite salvestuspiirangud
- **Jõudlusrežiim**: CPU vs GPU eelistused
- **Tervisekontrollid**: Jälgimisintervallid

## Arendus

### Allikast ehitamine
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

### Silumine
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testimine
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Jõudluse optimeerimine

### Mäluhaldus
- Tõhus sõnumite virtualiseerimine
- Automaatne prügikoristus
- Mudeli mälu jälgimine
- Ressursside puhastamine väljumisel

### Renderdamise optimeerimine
- Virtuaalne kerimine pikkade vestluste jaoks
- Sõnumiajaloo laadimise edasilükkamine
- Optimeeritud React/DOM värskendused
- GPU-kiirendusega animatsioonid

### Võrgu optimeerimine
- Ühenduste koondamine
- Päringute rühmitamine
- Automaatne uuesti proovimine
- Võrguühenduseta režiimi tugi

## Turvalisuse kaalutlused

### Andmete privaatsus
- Kohalikule arhitektuurile keskendunud
- Pilveandmete edastamine puudub (kohalik režiim)
- Krüpteeritud vestluste salvestamine
- Turvaline mandaadihaldus

### Rakenduse turvalisus
- Liivakasti renderdamisprotsessid
- Sisu turvapoliitika (CSP)
- Kaugkoodi täitmine puudub
- Turvaline IPC suhtlus

## Tõrkeotsing

### Levinud probleemid

**Foundry Local ei käivitu**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Mudelite laadimise tõrked**
- Kontrolli piisavat kettaruumi
- Kontrolli internetiühendust allalaadimiste jaoks
- Veendu, et GPU draiverid on ajakohased
- Proovi erinevaid mudelivariante

**Jõudlusprobleemid**
- Jälgi süsteemi ressursse
- Kohanda mudeli seadeid
- Luba riistvarakiirendus
- Sulge teised ressursimahukad rakendused

### Silumisrežiim
Luba silumispäevikute logimine, määrates keskkonnamuutujad:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Kaasamine

### Arenduskeskkonna seadistamine
1. Forki repositoorium
2. Loo funktsiooni haru
3. Paigalda sõltuvused: `npm install`
4. Tee muudatused ja testi
5. Esita pull request

### Koodistiil
- ESLinti konfiguratsioon on kaasas
- Prettier koodi vormindamiseks
- TypeScript tüübi turvalisuse jaoks
- JSDoc kommentaarid dokumenteerimiseks

## Õpitulemused

Pärast selle näidise läbimist mõistad:

1. **Windows 11 loomulik arendus**
   - Fluent Design Systemi rakendamine
   - Windowsi loomulik integreerimine
   - Electroni turvalisuse parimad tavad

2. **AI-mudelite integreerimine**
   - Foundry Locali teenuse arhitektuur
   - Mudeli elutsükli haldamine
   - Jõudluse jälgimine ja optimeerimine

3. **Reaalajas vestlussüsteemid**
   - Voogesituse vastuste käsitlemine
   - Vestluse oleku haldamine
   - Kasutajakogemuse mustrid

4. **Tootmisrakenduse arendus**
   - Vigade käsitlemine ja taastamine
   - Jõudluse optimeerimine
   - Turvalisuse kaalutlused
   - Testimisstrateegiad

## Järgmised sammud

- **Näidis 09**: Mitme agendi orkestreerimissüsteem
- **Näidis 10**: Foundry Locali tööriistade integreerimine
- **Edasijõudnud teemad**: Kohandatud mudelite peenhäälestamine
- **Paigaldamine**: Ettevõtte paigaldamise mustrid

## Litsents

See näidis järgib sama litsentsi nagu Microsoft Foundry Local projekt.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.