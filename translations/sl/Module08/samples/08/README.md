# Windows 11 Chat Sample - Foundry Local

Sodobna aplikacija za klepet za Windows 11, ki združuje Microsoft Foundry Local z čudovitim domačim vmesnikom. Zgrajena z Electronom in v skladu z uradnimi vzorci Microsoft Foundry Local.

## Pregled

Ta primer prikazuje, kako ustvariti aplikacijo za klepet, pripravljeno za produkcijo, ki uporablja lokalne modele AI prek Foundry Local, kar uporabnikom omogoča pogovore z AI, osredotočene na zasebnost, brez odvisnosti od oblaka.

## Funkcije

### 🎨 **Domači dizajn za Windows 11**
- Integracija Fluent Design System
- Učinki materiala Mica in prosojnost
- Podpora za tematsko oblikovanje Windows 11
- Prilagodljiva postavitev za vse velikosti zaslonov
- Samodejno preklapljanje med temnim/svetlim načinom

### 🤖 **Integracija AI modelov**
- Integracija storitve Foundry Local
- Podpora za več modelov z možnostjo hitrega preklapljanja
- Odzivi v realnem času
- Preklapljanje med lokalnimi in oblačnimi modeli
- Spremljanje zdravja modelov in statusa

### 💬 **Izkušnja klepeta**
- Kazalniki tipkanja v realnem času
- Ohranjanje zgodovine sporočil
- Izvoz pogovorov
- Prilagojeni sistemski pozivi
- Razvejanje in upravljanje pogovorov

### ⚡ **Funkcije zmogljivosti**
- Lenobno nalaganje in virtualizacija
- Optimizirano upodabljanje za dolge pogovore
- Predhodno nalaganje modelov v ozadju
- Učinkovito upravljanje pomnilnika
- Gladke animacije in prehodi

## Arhitektura

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

## Predpogoji

### Zahteve sistema
- **OS**: Windows 11 (priporočena različica 22H2 ali novejša)
- **RAM**: najmanj 8 GB, priporočeno 16 GB+ za večje modele
- **Shramba**: najmanj 10 GB prostega prostora za modele
- **GPU**: ni obvezen, vendar priporočljiv za hitrejše sklepanje

### Programske zahteve
- **Node.js**: v18.0.0 ali novejša
- **Foundry Local**: najnovejša različica od Microsofta
- **Git**: za kloniranje in razvoj

## Namestitev

### 1. Namestite Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonirajte in nastavite
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurirajte okolje
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Zaženite aplikacijo
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Struktura projekta

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

## Podroben pregled ključnih funkcij

### Integracija z Windows 11

**Fluent Design System**
- Materiali ozadja Mica
- Učinki prosojnosti Acrylic
- Zaobljeni vogali in sodobni razmiki
- Domača barvna paleta Windows 11
- Semantični barvni tokeni za dostopnost

**Domače funkcije Windows**
- Integracija seznama skokov za nedavne klepete
- Obvestila Windows za nova sporočila
- Napredek v opravilni vrstici za operacije modelov
- Integracija sistemske vrstice s hitrimi akcijami
- Podpora za avtentikacijo Windows Hello

### Upravljanje AI modelov

**Lokalni modeli**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hibridna podpora oblak/lokalno**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funkcije vmesnika za klepet

**Pretakanje v realnem času**
- Prikaz odzivov po tokenih
- Gladke animacije tipkanja
- Preklicljive zahteve
- Kazalniki tipkanja in status

**Upravljanje pogovorov**
- Ohranjanje zgodovine klepeta
- Izvoz/uvoz pogovorov
- Iskanje in filtriranje sporočil
- Razvejanje pogovorov
- Prilagojeni sistemski pozivi za vsak pogovor

**Dostopnost**
- Popolna navigacija s tipkovnico
- Združljivost z bralniki zaslona
- Podpora za način visokega kontrasta
- Prilagodljive velikosti pisave
- Integracija glasovnega vnosa

## Primeri uporabe

### Osnovna integracija klepeta
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

### Upravljanje modelov
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

### Nastavitve in prilagoditve
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

## Možnosti konfiguracije

### Nastavitve aplikacije
- **Tema**: Samodejni, svetli, temni način
- **Model**: Privzeta izbira modela
- **Zmogljivost**: Nastavitve sklepanja
- **Zasebnost**: Politike zadrževanja podatkov
- **Obvestila**: Opozorila o sporočilih
- **Bližnjice**: Bližnjice na tipkovnici

### Nastavitve klepeta
- **Pretakanje**: Omogoči/onemogoči odzive v realnem času
- **Dolžina konteksta**: Spomin pogovora
- **Temperatura**: Ustvarjalnost odzivov
- **Največ tokenov**: Omejitve dolžine odzivov
- **Sistemski pozivi**: Privzeto vedenje asistenta

### Nastavitve modela
- **Samodejni prenos**: Samodejne posodobitve modelov
- **Velikost predpomnilnika**: Omejitve lokalnega shranjevanja modelov
- **Način zmogljivosti**: Nastavitve CPU proti GPU
- **Preverjanje zdravja**: Intervali spremljanja

## Razvoj

### Gradnja iz izvorne kode
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

### Odpravljanje napak
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testiranje
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimizacija zmogljivosti

### Upravljanje pomnilnika
- Učinkovita virtualizacija sporočil
- Samodejno zbiranje smeti
- Spremljanje pomnilnika modelov
- Čiščenje virov ob izhodu

### Optimizacija upodabljanja
- Virtualno pomikanje za dolge pogovore
- Lenobno nalaganje zgodovine sporočil
- Optimizirane posodobitve React/DOM
- Animacije pospešene z GPU

### Optimizacija omrežja
- Združevanje povezav
- Združevanje zahtev
- Samodejna logika ponovnega poskusa
- Podpora za način brez povezave

## Varnostni vidiki

### Zasebnost podatkov
- Arhitektura, osredotočena na lokalno
- Brez prenosa podatkov v oblak (lokalni način)
- Šifrirano shranjevanje pogovorov
- Varno upravljanje poverilnic

### Varnost aplikacije
- Procesi upodabljanja v peskovniku
- Politika varnosti vsebine (CSP)
- Brez oddaljenega izvajanja kode
- Varna komunikacija IPC

## Odpravljanje težav

### Pogoste težave

**Foundry Local se ne zažene**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Napake pri nalaganju modelov**
- Preverite zadostno diskovno prostor
- Preverite internetno povezavo za prenose
- Poskrbite za posodobljene gonilnike GPU
- Poskusite različne različice modelov

**Težave z zmogljivostjo**
- Spremljajte sistemske vire
- Prilagodite nastavitve modela
- Omogočite strojno pospeševanje
- Zaprite druge aplikacije, ki porabijo veliko virov

### Način odpravljanja napak
Omogočite beleženje napak z nastavitvijo okoljskih spremenljivk:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Prispevanje

### Nastavitev za razvoj
1. Forkajte repozitorij
2. Ustvarite vejo za funkcijo
3. Namestite odvisnosti: `npm install`
4. Naredite spremembe in testirajte
5. Pošljite pull request

### Slog kode
- Zagotovljena konfiguracija ESLint
- Prettier za oblikovanje kode
- TypeScript za varnost tipov
- JSDoc komentarji za dokumentacijo

## Cilji učenja

Po zaključku tega primera boste razumeli:

1. **Domači razvoj za Windows 11**
   - Implementacija Fluent Design System
   - Integracija z Windows
   - Najboljše prakse varnosti za Electron

2. **Integracija AI modelov**
   - Arhitektura storitve Foundry Local
   - Upravljanje življenjskega cikla modelov
   - Spremljanje zmogljivosti in optimizacija

3. **Sistemi za klepet v realnem času**
   - Upravljanje odzivov med pretakanjem
   - Upravljanje stanja pogovora
   - Vzorci uporabniške izkušnje

4. **Razvoj produkcijskih aplikacij**
   - Upravljanje napak in okrevanje
   - Optimizacija zmogljivosti
   - Varnostni vidiki
   - Strategije testiranja

## Naslednji koraki

- **Primer 09**: Sistem za orkestracijo več agentov
- **Primer 10**: Foundry Local kot integracija orodij
- **Napredne teme**: Prilagajanje modelov
- **Namestitev**: Vzorci za namestitev v podjetjih

## Licenca

Ta primer sledi isti licenci kot projekt Microsoft Foundry Local.

---

