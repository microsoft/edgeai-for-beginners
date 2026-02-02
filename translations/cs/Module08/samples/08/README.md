# Windows 11 Chat Ukázka - Foundry Local

Moderní chatovací aplikace pro Windows 11, která integruje Microsoft Foundry Local s krásným nativním rozhraním. Postaveno pomocí Electronu a podle oficiálních vzorů Foundry Local od Microsoftu.

## Přehled

Tato ukázka demonstruje, jak vytvořit produkčně připravenou chatovací aplikaci, která využívá lokální AI modely prostřednictvím Foundry Local, což uživatelům poskytuje soukromé AI konverzace bez závislosti na cloudu.

## Funkce

### 🎨 **Nativní design Windows 11**
- Integrace Fluent Design System
- Efekty materiálu Mica a průhlednost
- Podpora nativního tématu Windows 11
- Responzivní rozvržení pro všechny velikosti obrazovek
- Automatické přepínání mezi tmavým a světlým režimem

### 🤖 **Integrace AI modelů**
- Integrace služby Foundry Local
- Podpora více modelů s možností rychlé výměny
- Odpovědi v reálném čase
- Přepínání mezi lokálními a cloudovými modely
- Monitorování stavu modelů

### 💬 **Chatovací zážitek**
- Indikátory psaní v reálném čase
- Ukládání historie zpráv
- Export chatových konverzací
- Vlastní systémové výzvy
- Rozvětvování a správa konverzací

### ⚡ **Výkonnostní funkce**
- Lazy loading a virtualizace
- Optimalizované vykreslování pro dlouhé konverzace
- Předběžné načítání modelů na pozadí
- Efektivní správa paměti
- Plynulé animace a přechody

## Architektura

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

## Požadavky

### Systémové požadavky
- **OS**: Windows 11 (doporučeno 22H2 nebo novější)
- **RAM**: Minimálně 8 GB, doporučeno 16 GB+ pro větší modely
- **Úložiště**: Minimálně 10 GB volného místa pro modely
- **GPU**: Volitelné, ale doporučeno pro rychlejší inferenci

### Softwarové závislosti
- **Node.js**: v18.0.0 nebo novější
- **Foundry Local**: Nejnovější verze od Microsoftu
- **Git**: Pro klonování a vývoj

## Instalace

### 1. Instalace Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonování a nastavení
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurace prostředí
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Spuštění aplikace
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Struktura projektu

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

## Podrobný přehled klíčových funkcí

### Integrace Windows 11

**Fluent Design System**
- Materiály pozadí Mica
- Efekty průhlednosti Acrylic
- Zaoblené rohy a moderní rozestupy
- Nativní barevná paleta Windows 11
- Semantické barevné tokeny pro přístupnost

**Nativní funkce Windows**
- Integrace seznamu skoků pro nedávné chaty
- Windows notifikace pro nové zprávy
- Pokrok na hlavním panelu pro operace modelu
- Integrace systémové lišty s rychlými akcemi
- Podpora autentizace Windows Hello

### Správa AI modelů

**Lokální modely**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybridní podpora cloud/lokál**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funkce chatovacího rozhraní

**Streamování v reálném čase**
- Zobrazení odpovědí token po tokenu
- Plynulé animace psaní
- Možnost zrušení požadavků
- Indikátory psaní a stav

**Správa konverzací**
- Ukládání historie chatu
- Export/import konverzací
- Vyhledávání a filtrování zpráv
- Rozvětvování konverzací
- Vlastní systémové výzvy pro každou konverzaci

**Přístupnost**
- Plná navigace pomocí klávesnice
- Kompatibilita se čtečkami obrazovky
- Podpora režimu vysokého kontrastu
- Přizpůsobitelné velikosti písma
- Integrace hlasového vstupu

## Příklady použití

### Základní integrace chatu
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

### Správa modelů
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

### Nastavení a přizpůsobení
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

## Možnosti konfigurace

### Nastavení aplikace
- **Téma**: Automatický, světlý, tmavý režim
- **Model**: Výchozí výběr modelu
- **Výkon**: Nastavení inferencí
- **Soukromí**: Politiky uchovávání dat
- **Notifikace**: Upozornění na zprávy
- **Zkratky**: Klávesové zkratky

### Nastavení chatu
- **Streamování**: Povolit/zakázat odpovědi v reálném čase
- **Délka kontextu**: Paměť konverzace
- **Teplota**: Kreativita odpovědí
- **Maximální počet tokenů**: Limity délky odpovědí
- **Systémové výzvy**: Výchozí chování asistenta

### Nastavení modelu
- **Automatické stahování**: Automatické aktualizace modelů
- **Velikost cache**: Limity úložiště lokálních modelů
- **Režim výkonu**: Preference CPU vs GPU
- **Kontroly stavu**: Intervaly monitorování

## Vývoj

### Sestavení ze zdroje
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

### Ladění
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testování
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimalizace výkonu

### Správa paměti
- Efektivní virtualizace zpráv
- Automatické uvolňování paměti
- Monitorování paměti modelu
- Vyčištění zdrojů při ukončení

### Optimalizace vykreslování
- Virtuální posouvání pro dlouhé konverzace
- Lazy loading historie zpráv
- Optimalizované aktualizace React/DOM
- Animace akcelerované GPU

### Optimalizace sítě
- Pooling připojení
- Dávkování požadavků
- Automatická logika opakování
- Podpora offline režimu

## Bezpečnostní aspekty

### Ochrana dat
- Architektura zaměřená na lokální provoz
- Žádný přenos dat do cloudu (lokální režim)
- Šifrované ukládání konverzací
- Bezpečná správa přihlašovacích údajů

### Bezpečnost aplikace
- Procesy rendereru v sandboxu
- Content Security Policy (CSP)
- Žádné vzdálené spouštění kódu
- Bezpečná komunikace IPC

## Řešení problémů

### Běžné problémy

**Foundry Local se nespouští**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Chyby při načítání modelů**
- Ověřte dostatek volného místa na disku
- Zkontrolujte internetové připojení pro stahování
- Ujistěte se, že jsou aktualizovány ovladače GPU
- Vyzkoušejte různé varianty modelů

**Problémy s výkonem**
- Monitorujte systémové zdroje
- Upravte nastavení modelu
- Povolit hardwarovou akceleraci
- Zavřete jiné aplikace náročné na zdroje

### Režim ladění
Povolte ladicí logování nastavením proměnných prostředí:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Přispívání

### Nastavení vývoje
1. Forkněte repozitář
2. Vytvořte větev pro funkci
3. Nainstalujte závislosti: `npm install`
4. Proveďte změny a otestujte
5. Odešlete pull request

### Styl kódu
- Poskytnuta konfigurace ESLint
- Prettier pro formátování kódu
- TypeScript pro typovou bezpečnost
- JSDoc komentáře pro dokumentaci

## Výukové cíle

Po dokončení této ukázky budete rozumět:

1. **Nativnímu vývoji pro Windows 11**
   - Implementace Fluent Design System
   - Integrace nativních funkcí Windows
   - Nejlepší praktiky zabezpečení Electronu

2. **Integraci AI modelů**
   - Architektura služby Foundry Local
   - Správa životního cyklu modelů
   - Monitorování výkonu a optimalizace

3. **Systémům chatu v reálném čase**
   - Zpracování odpovědí při streamování
   - Správa stavu konverzace
   - Vzory uživatelského zážitku

4. **Vývoji produkčních aplikací**
   - Zpracování chyb a obnova
   - Optimalizace výkonu
   - Bezpečnostní aspekty
   - Strategie testování

## Další kroky

- **Ukázka 09**: Systém orchestrace více agentů
- **Ukázka 10**: Foundry Local jako integrace nástrojů
- **Pokročilá témata**: Vlastní doladění modelů
- **Nasazení**: Vzory nasazení pro podniky

## Licence

Tato ukázka se řídí stejnou licencí jako projekt Microsoft Foundry Local.

---

