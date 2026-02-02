# Windows 11 Chat Sample - Foundry Local

Moderná chatovacia aplikácia pre Windows 11, ktorá integruje Microsoft Foundry Local s krásnym natívnym rozhraním. Vytvorená pomocou Electronu a podľa oficiálnych vzorov Microsoft Foundry Local.

## Prehľad

Tento príklad ukazuje, ako vytvoriť produkčne pripravenú chatovaciu aplikáciu, ktorá využíva lokálne AI modely prostredníctvom Foundry Local, poskytujúc používateľom súkromné AI konverzácie bez závislosti na cloude.

## Funkcie

### 🎨 **Natívny dizajn Windows 11**
- Integrácia Fluent Design System
- Efekty materiálu Mica a transparentnosť
- Podpora natívneho tematického vzhľadu Windows 11
- Responzívne rozloženie pre všetky veľkosti obrazovky
- Automatické prepínanie medzi tmavým a svetlým režimom

### 🤖 **Integrácia AI modelov**
- Integrácia služby Foundry Local
- Podpora viacerých modelov s možnosťou ich výmeny
- Odpovede v reálnom čase
- Prepínanie medzi lokálnymi a cloudovými modelmi
- Monitorovanie stavu modelov

### 💬 **Chatovacia skúsenosť**
- Indikátory písania v reálnom čase
- Ukladanie histórie správ
- Export chatových konverzácií
- Vlastné systémové výzvy
- Vetvenie a správa konverzácií

### ⚡ **Výkonnostné funkcie**
- Lazy loading a virtualizácia
- Optimalizované vykresľovanie pre dlhé konverzácie
- Predbežné načítanie modelov na pozadí
- Efektívne spravovanie pamäte
- Plynulé animácie a prechody

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

## Predpoklady

### Systémové požiadavky
- **OS**: Windows 11 (odporúčaný 22H2 alebo novší)
- **RAM**: Minimálne 8GB, odporúčaných 16GB+ pre väčšie modely
- **Úložisko**: 10GB+ voľného miesta pre modely
- **GPU**: Voliteľné, ale odporúčané pre rýchlejšie spracovanie

### Softvérové závislosti
- **Node.js**: v18.0.0 alebo novší
- **Foundry Local**: Najnovšia verzia od Microsoftu
- **Git**: Na klonovanie a vývoj

## Inštalácia

### 1. Inštalácia Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonovanie a nastavenie
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurácia prostredia
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Spustenie aplikácie
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Štruktúra projektu

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

## Podrobný pohľad na kľúčové funkcie

### Integrácia Windows 11

**Fluent Design System**
- Materiály pozadia Mica
- Efekty transparentnosti Acrylic
- Zaoblené rohy a moderné rozostupy
- Natívna farebná paleta Windows 11
- Semantické farebné tokeny pre prístupnosť

**Natívne funkcie Windows**
- Integrácia zoznamu skokov pre nedávne chaty
- Notifikácie Windows pre nové správy
- Pokrok na paneli úloh pre operácie modelov
- Integrácia systémovej lišty s rýchlymi akciami
- Podpora autentifikácie Windows Hello

### Správa AI modelov

**Lokálne modely**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybridná podpora cloudu/lokálneho režimu**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funkcie chatovacieho rozhrania

**Streamovanie v reálnom čase**
- Zobrazenie odpovedí po tokenoch
- Plynulé animácie písania
- Možnosť zrušenia požiadaviek
- Indikátory písania a stavu

**Správa konverzácií**
- Ukladanie histórie chatu
- Export/import konverzácií
- Vyhľadávanie a filtrovanie správ
- Vetvenie konverzácií
- Vlastné systémové výzvy pre každú konverzáciu

**Prístupnosť**
- Plná navigácia pomocou klávesnice
- Kompatibilita so čítačkami obrazovky
- Podpora režimu vysokého kontrastu
- Prispôsobiteľné veľkosti písma
- Integrácia hlasového vstupu

## Príklady použitia

### Základná integrácia chatu
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

### Správa modelov
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

### Nastavenia a prispôsobenie
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

## Možnosti konfigurácie

### Nastavenia aplikácie
- **Téma**: Automatický, svetlý, tmavý režim
- **Model**: Predvolený výber modelu
- **Výkon**: Nastavenia spracovania
- **Súkromie**: Politiky uchovávania údajov
- **Notifikácie**: Upozornenia na správy
- **Skratky**: Klávesové skratky

### Nastavenia chatu
- **Streamovanie**: Povolenie/zakázanie odpovedí v reálnom čase
- **Dĺžka kontextu**: Pamäť konverzácie
- **Teplota**: Kreativita odpovedí
- **Maximálny počet tokenov**: Limity dĺžky odpovedí
- **Systémové výzvy**: Predvolené správanie asistenta

### Nastavenia modelov
- **Automatické sťahovanie**: Automatické aktualizácie modelov
- **Veľkosť cache**: Limity úložiska lokálnych modelov
- **Režim výkonu**: Preferencie CPU vs GPU
- **Kontroly stavu**: Intervaly monitorovania

## Vývoj

### Vytvorenie zo zdroja
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

### Ladenie
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testovanie
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimalizácia výkonu

### Správa pamäte
- Efektívna virtualizácia správ
- Automatické zberanie odpadu
- Monitorovanie pamäte modelov
- Vyčistenie zdrojov pri ukončení

### Optimalizácia vykresľovania
- Virtuálne rolovanie pre dlhé konverzácie
- Lazy loading histórie správ
- Optimalizované aktualizácie React/DOM
- Animácie akcelerované GPU

### Optimalizácia siete
- Pooling pripojení
- Dávkovanie požiadaviek
- Automatická logika opakovania
- Podpora offline režimu

## Bezpečnostné aspekty

### Ochrana údajov
- Architektúra orientovaná na lokálne spracovanie
- Žiadny prenos údajov do cloudu (lokálny režim)
- Šifrované ukladanie konverzácií
- Bezpečné spravovanie poverení

### Bezpečnosť aplikácie
- Procesy rendereru v sandboxe
- Politika bezpečnosti obsahu (CSP)
- Žiadne vzdialené vykonávanie kódu
- Bezpečná komunikácia IPC

## Riešenie problémov

### Bežné problémy

**Foundry Local sa nespúšťa**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Zlyhanie načítania modelov**
- Skontrolujte dostatok miesta na disku
- Overte internetové pripojenie pre sťahovanie
- Uistite sa, že ovládače GPU sú aktuálne
- Vyskúšajte rôzne varianty modelov

**Problémy s výkonom**
- Monitorujte systémové zdroje
- Upravte nastavenia modelov
- Povolenie hardvérovej akcelerácie
- Zatvorte iné aplikácie náročné na zdroje

### Režim ladenia
Povolenie logovania ladenia nastavením premenných prostredia:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Prispievanie

### Nastavenie vývoja
1. Forknite repozitár
2. Vytvorte vetvu pre funkciu
3. Nainštalujte závislosti: `npm install`
4. Urobte zmeny a otestujte
5. Podajte pull request

### Štýl kódu
- Poskytnutá konfigurácia ESLint
- Prettier na formátovanie kódu
- TypeScript pre typovú bezpečnosť
- JSDoc komentáre pre dokumentáciu

## Výsledky učenia

Po dokončení tohto príkladu budete rozumieť:

1. **Natívny vývoj pre Windows 11**
   - Implementácia Fluent Design System
   - Integrácia natívnych funkcií Windows
   - Najlepšie praktiky bezpečnosti Electronu

2. **Integrácia AI modelov**
   - Architektúra služby Foundry Local
   - Správa životného cyklu modelov
   - Monitorovanie výkonu a optimalizácia

3. **Systémy chatu v reálnom čase**
   - Spracovanie odpovedí v reálnom čase
   - Správa stavu konverzácie
   - Vzory používateľskej skúsenosti

4. **Vývoj produkčných aplikácií**
   - Riešenie chýb a obnova
   - Optimalizácia výkonu
   - Bezpečnostné aspekty
   - Testovacie stratégie

## Ďalšie kroky

- **Príklad 09**: Systém orchestrácie viacerých agentov
- **Príklad 10**: Integrácia Foundry Local ako nástroja
- **Pokročilé témy**: Jemné doladenie vlastných modelov
- **Nasadenie**: Vzory nasadenia pre podniky

## Licencia

Tento príklad nasleduje rovnakú licenciu ako projekt Microsoft Foundry Local.

---

