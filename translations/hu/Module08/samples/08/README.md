# Windows 11 Chat Minta - Foundry Local

Egy modern chatalkalmazás Windows 11-hez, amely integrálja a Microsoft Foundry Local szolgáltatást egy gyönyörű, natív felülettel. Electronnal készült, és követi a Microsoft hivatalos Foundry Local mintáit.

## Áttekintés

Ez a minta bemutatja, hogyan lehet egy gyártásra kész chatalkalmazást létrehozni, amely helyi AI modelleket használ a Foundry Local segítségével, lehetővé téve a felhasználók számára a felhőfüggetlen, adatvédelmet előtérbe helyező AI beszélgetéseket.

## Funkciók

### 🎨 **Windows 11 Natív Dizájn**
- Fluent Design System integráció
- Mica anyaghatások és átlátszóság
- Natív Windows 11 tématámogatás
- Reszponzív elrendezés minden képernyőmérethez
- Automatikus váltás sötét/világos mód között

### 🤖 **AI Modell Integráció**
- Foundry Local szolgáltatás integráció
- Több modell támogatása, gyors váltással
- Valós idejű válaszok streamelése
- Helyi és felhőmodell váltás
- Modell állapotfigyelés és monitorozás

### 💬 **Chat Élmény**
- Valós idejű gépelési jelzések
- Üzenetelőzmények megőrzése
- Chatbeszélgetések exportálása
- Egyedi rendszerüzenetek
- Beszélgetés ágaztatás és kezelés

### ⚡ **Teljesítményfunkciók**
- Lusta betöltés és virtualizáció
- Optimalizált megjelenítés hosszú beszélgetésekhez
- Háttérmodell előtöltés
- Hatékony memóriahasználat
- Zökkenőmentes animációk és átmenetek

## Architektúra

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

## Előfeltételek

### Rendszerkövetelmények
- **Operációs rendszer**: Windows 11 (22H2 vagy újabb ajánlott)
- **RAM**: Minimum 8GB, 16GB+ ajánlott nagyobb modellekhez
- **Tárhely**: Legalább 10GB szabad hely a modellekhez
- **GPU**: Opcionális, de ajánlott a gyorsabb következtetéshez

### Szoftverfüggőségek
- **Node.js**: v18.0.0 vagy újabb
- **Foundry Local**: Microsoft legfrissebb verziója
- **Git**: Klónozáshoz és fejlesztéshez

## Telepítés

### 1. Foundry Local telepítése
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klónozás és beállítás
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Környezet konfigurálása
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Alkalmazás futtatása
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projektstruktúra

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

## Kulcsfontosságú Funkciók Részletesen

### Windows 11 Integráció

**Fluent Design System**
- Mica háttéranyagok
- Akril átlátszósági hatások
- Lekerekített sarkok és modern térközök
- Natív Windows 11 színpaletta
- Szemantikus színtokenek az akadálymentesség érdekében

**Natív Windows Funkciók**
- Gyorslisták integrációja a legutóbbi beszélgetésekhez
- Windows értesítések új üzenetekről
- Feladatlistás előrehaladás modellműveletekhez
- Rendszertálca integráció gyors műveletekkel
- Windows Hello hitelesítési támogatás

### AI Modellkezelés

**Helyi Modellek**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hibrid Felhő/Helyi Támogatás**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chat Felület Funkciók

**Valós idejű Streamelés**
- Tokenenkénti válaszmegjelenítés
- Zökkenőmentes gépelési animációk
- Megszakítható kérések
- Gépelési jelzések és állapot

**Beszélgetéskezelés**
- Tartós chatelőzmények
- Beszélgetések exportálása/importálása
- Üzenetkeresés és szűrés
- Beszélgetés ágaztatás
- Egyedi rendszerüzenetek beszélgetésenként

**Akadálymentesség**
- Teljes billentyűzet-navigáció
- Képernyőolvasó kompatibilitás
- Magas kontraszt mód támogatása
- Testreszabható betűméretek
- Hangbevitel integráció

## Használati Példák

### Alapvető Chat Integráció
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

### Modellkezelés
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

### Beállítások és Testreszabás
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

## Konfigurációs Opciók

### Alkalmazás Beállítások
- **Téma**: Automatikus, Világos, Sötét mód
- **Modell**: Alapértelmezett modell kiválasztása
- **Teljesítmény**: Következtetési beállítások
- **Adatvédelem**: Adatmegőrzési irányelvek
- **Értesítések**: Üzenetértesítések
- **Gyorsbillentyűk**: Billentyűparancsok

### Chat Beállítások
- **Streamelés**: Valós idejű válaszok engedélyezése/letiltása
- **Kontextus Hossza**: Beszélgetési memória
- **Hőmérséklet**: Válasz kreativitása
- **Maximális Tokenek**: Válasz hosszkorlátok
- **Rendszerüzenetek**: Alapértelmezett asszisztens viselkedés

### Modell Beállítások
- **Automatikus Letöltés**: Modellfrissítések automatikus letöltése
- **Gyorsítótár Méret**: Helyi modell tárolási korlátok
- **Teljesítmény Mód**: CPU vs GPU preferenciák
- **Egészségügyi Ellenőrzések**: Monitorozási intervallumok

## Fejlesztés

### Forrásból Építés
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

### Hibakeresés
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Tesztelés
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Teljesítményoptimalizálás

### Memóriakezelés
- Hatékony üzenetvirtualizáció
- Automatikus szemétgyűjtés
- Modell memória monitorozása
- Erőforrások tisztítása kilépéskor

### Renderelési Optimalizálás
- Virtuális görgetés hosszú beszélgetésekhez
- Üzenetelőzmények lusta betöltése
- Optimalizált React/DOM frissítések
- GPU-gyorsított animációk

### Hálózati Optimalizálás
- Kapcsolat pooling
- Kéréscsomagolás
- Automatikus újrapróbálkozási logika
- Offline mód támogatás

## Biztonsági Szempontok

### Adatvédelem
- Helyi-első architektúra
- Nincs felhő adatátvitel (helyi mód)
- Titkosított beszélgetéstárolás
- Biztonságos hitelesítő adatkezelés

### Alkalmazásbiztonság
- Homokozott renderelő folyamatok
- Tartalom Biztonsági Politika (CSP)
- Nincs távoli kódvégrehajtás
- Biztonságos IPC kommunikáció

## Hibakeresés

### Gyakori Problémák

**Foundry Local Nem Indul**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Modell Betöltési Hibák**
- Ellenőrizze a megfelelő lemezterületet
- Ellenőrizze az internetkapcsolatot a letöltésekhez
- Győződjön meg róla, hogy a GPU illesztőprogramok frissítve vannak
- Próbáljon ki különböző modellváltozatokat

**Teljesítményproblémák**
- Monitorozza a rendszer erőforrásait
- Állítsa be a modell beállításait
- Engedélyezze a hardvergyorsítást
- Zárja be más erőforrás-igényes alkalmazásokat

### Hibakeresési Mód
Engedélyezze a hibakeresési naplózást környezeti változók beállításával:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Hozzájárulás

### Fejlesztési Beállítás
1. Forkolja a repót
2. Hozzon létre egy funkcióágat
3. Telepítse a függőségeket: `npm install`
4. Végezze el a módosításokat és teszteljen
5. Küldjön be egy pull requestet

### Kódstílus
- ESLint konfiguráció biztosított
- Prettier a kódformázáshoz
- TypeScript a típusbiztonság érdekében
- JSDoc megjegyzések a dokumentációhoz

## Tanulási Eredmények

A minta befejezése után megérti:

1. **Windows 11 Natív Fejlesztés**
   - Fluent Design System implementáció
   - Natív Windows integráció
   - Electron biztonsági legjobb gyakorlatok

2. **AI Modell Integráció**
   - Foundry Local szolgáltatás architektúra
   - Modell életciklus kezelése
   - Teljesítmény monitorozás és optimalizálás

3. **Valós idejű Chat Rendszerek**
   - Streamelési válaszkezelés
   - Beszélgetési állapotkezelés
   - Felhasználói élmény minták

4. **Gyártási Alkalmazás Fejlesztés**
   - Hibakezelés és helyreállítás
   - Teljesítményoptimalizálás
   - Biztonsági szempontok
   - Tesztelési stratégiák

## Következő Lépések

- **Minta 09**: Többügynökös Orkesztrációs Rendszer
- **Minta 10**: Foundry Local mint Eszközök Integráció
- **Haladó Témák**: Egyedi modell finomhangolás
- **Telepítés**: Vállalati telepítési minták

## Licenc

Ez a minta ugyanazt a licencet követi, mint a Microsoft Foundry Local projekt.

---

