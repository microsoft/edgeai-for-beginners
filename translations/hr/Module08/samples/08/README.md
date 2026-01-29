# Windows 11 Chat Sample - Foundry Local

Moderna aplikacija za chat na Windows 11 koja integrira Microsoft Foundry Local s prekrasnim izvornim sučeljem. Izrađena pomoću Electron-a i slijedeći službene obrasce Microsoft Foundry Local.

## Pregled

Ovaj primjer pokazuje kako stvoriti aplikaciju za chat spremnu za produkciju koja koristi lokalne AI modele putem Foundry Local, omogućujući korisnicima privatne AI razgovore bez ovisnosti o oblaku.

## Značajke

### 🎨 **Izvorni dizajn za Windows 11**
- Integracija Fluent Design System-a
- Efekti Mica materijala i transparentnosti
- Podrška za izvorne teme Windows 11
- Responzivni izgled za sve veličine ekrana
- Automatsko prebacivanje između tamnog i svijetlog načina rada

### 🤖 **Integracija AI modela**
- Integracija usluge Foundry Local
- Podrška za više modela s mogućnošću brzog prebacivanja
- Odgovori u stvarnom vremenu
- Prebacivanje između lokalnih i oblačnih modela
- Praćenje zdravlja modela i statusa

### 💬 **Iskustvo chata**
- Indikatori tipkanja u stvarnom vremenu
- Pohrana povijesti poruka
- Izvoz razgovora
- Prilagođeni sistemski upiti
- Razgranavanje i upravljanje razgovorima

### ⚡ **Značajke performansi**
- Lijeno učitavanje i virtualizacija
- Optimizirano renderiranje za duge razgovore
- Predučitavanje modela u pozadini
- Učinkovito upravljanje memorijom
- Glatke animacije i prijelazi

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

## Preduvjeti

### Sistemski zahtjevi
- **OS**: Windows 11 (preporučeno 22H2 ili novije)
- **RAM**: Minimalno 8GB, preporučeno 16GB+ za veće modele
- **Pohrana**: 10GB+ slobodnog prostora za modele
- **GPU**: Opcionalno, ali preporučeno za bržu inferenciju

### Softverske ovisnosti
- **Node.js**: v18.0.0 ili novije
- **Foundry Local**: Najnovija verzija od Microsofta
- **Git**: Za kloniranje i razvoj

## Instalacija

### 1. Instalirajte Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonirajte i postavite
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurirajte okruženje
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Pokrenite aplikaciju
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

## Detaljan pregled ključnih značajki

### Integracija s Windows 11

**Fluent Design System**
- Materijali pozadine Mica
- Efekti akrilne transparentnosti
- Zaobljeni kutovi i moderan razmak
- Izvorna paleta boja Windows 11
- Semantički kolor tokeni za pristupačnost

**Izvorne značajke Windows-a**
- Integracija Jump lista za nedavne razgovore
- Obavijesti Windows-a za nove poruke
- Napredak na traci zadataka za operacije modela
- Integracija sistemske trake s brzim akcijama
- Podrška za autentifikaciju Windows Hello

### Upravljanje AI modelima

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

**Hibridna podrška za oblak/lokalno**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Značajke sučelja za chat

**Streaming u stvarnom vremenu**
- Prikaz odgovora token po token
- Glatke animacije tipkanja
- Mogućnost otkazivanja zahtjeva
- Indikatori tipkanja i status

**Upravljanje razgovorima**
- Trajna povijest chata
- Izvoz/uvoz razgovora
- Pretraživanje i filtriranje poruka
- Razgranavanje razgovora
- Prilagođeni sistemski upiti za svaki razgovor

**Pristupačnost**
- Potpuna navigacija putem tipkovnice
- Kompatibilnost sa čitačima ekrana
- Podrška za način rada visokog kontrasta
- Prilagodljive veličine fonta
- Integracija glasovnog unosa

## Primjeri korištenja

### Osnovna integracija chata
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

### Upravljanje modelima
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

### Postavke i prilagodba
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

## Opcije konfiguracije

### Postavke aplikacije
- **Tema**: Automatski, svijetli, tamni način rada
- **Model**: Zadani odabir modela
- **Performanse**: Postavke inferencije
- **Privatnost**: Politike zadržavanja podataka
- **Obavijesti**: Upozorenja o porukama
- **Prečaci**: Prečaci na tipkovnici

### Postavke chata
- **Streaming**: Omogući/onemogući odgovore u stvarnom vremenu
- **Duljina konteksta**: Memorija razgovora
- **Temperatura**: Kreativnost odgovora
- **Maksimalni tokeni**: Ograničenja duljine odgovora
- **Sistemski upiti**: Zadano ponašanje asistenta

### Postavke modela
- **Automatsko preuzimanje**: Automatska ažuriranja modela
- **Veličina predmemorije**: Ograničenja lokalne pohrane modela
- **Način rada performansi**: Preferencije CPU-a ili GPU-a
- **Provjere zdravlja**: Intervali praćenja

## Razvoj

### Izgradnja iz izvornog koda
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

### Otklanjanje pogrešaka
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

## Optimizacija performansi

### Upravljanje memorijom
- Učinkovita virtualizacija poruka
- Automatsko prikupljanje smeća
- Praćenje memorije modela
- Čišćenje resursa pri izlasku

### Optimizacija renderiranja
- Virtualno pomicanje za duge razgovore
- Lijeno učitavanje povijesti poruka
- Optimizirana ažuriranja React/DOM-a
- Animacije ubrzane GPU-om

### Optimizacija mreže
- Grupiranje veza
- Grupiranje zahtjeva
- Automatska logika ponovnog pokušaja
- Podrška za offline način rada

## Sigurnosni aspekti

### Privatnost podataka
- Arhitektura usmjerena na lokalno
- Bez prijenosa podataka u oblak (lokalni način rada)
- Šifrirana pohrana razgovora
- Sigurno upravljanje vjerodajnicama

### Sigurnost aplikacije
- Procesi renderiranja u sandboxu
- Politika sigurnosti sadržaja (CSP)
- Bez daljinskog izvršavanja koda
- Sigurna komunikacija putem IPC-a

## Rješavanje problema

### Uobičajeni problemi

**Foundry Local se ne pokreće**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Neuspjesi pri učitavanju modela**
- Provjerite ima li dovoljno prostora na disku
- Provjerite internetsku vezu za preuzimanja
- Ažurirajte GPU upravljačke programe
- Isprobajte različite varijante modela

**Problemi s performansama**
- Pratite resurse sustava
- Prilagodite postavke modela
- Omogućite hardversko ubrzanje
- Zatvorite druge aplikacije koje troše resurse

### Način rada za otklanjanje pogrešaka
Omogućite zapisivanje pogrešaka postavljanjem varijabli okruženja:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Doprinos

### Postavljanje za razvoj
1. Forkajte repozitorij
2. Kreirajte granu za značajke
3. Instalirajte ovisnosti: `npm install`
4. Napravite promjene i testirajte
5. Pošaljite pull request

### Stil koda
- Pruža se konfiguracija za ESLint
- Prettier za formatiranje koda
- TypeScript za sigurnost tipova
- JSDoc komentari za dokumentaciju

## Ishodi učenja

Nakon dovršetka ovog primjera, razumjet ćete:

1. **Izvorni razvoj za Windows 11**
   - Implementacija Fluent Design System-a
   - Integracija s Windows-om
   - Najbolje prakse sigurnosti za Electron

2. **Integracija AI modela**
   - Arhitektura usluge Foundry Local
   - Upravljanje životnim ciklusom modela
   - Praćenje performansi i optimizacija

3. **Sustavi za chat u stvarnom vremenu**
   - Upravljanje odgovorima u stvarnom vremenu
   - Upravljanje stanjem razgovora
   - Obrasci korisničkog iskustva

4. **Razvoj aplikacija za produkciju**
   - Upravljanje pogreškama i oporavak
   - Optimizacija performansi
   - Sigurnosni aspekti
   - Strategije testiranja

## Sljedeći koraci

- **Primjer 09**: Sustav za orkestraciju više agenata
- **Primjer 10**: Foundry Local kao integracija alata
- **Napredne teme**: Fino podešavanje prilagođenih modela
- **Implementacija**: Obrasci za implementaciju u poduzeću

## Licenca

Ovaj primjer slijedi istu licencu kao i projekt Microsoft Foundry Local.

---

