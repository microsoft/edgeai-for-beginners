# Windows 11 Chat Sample - Foundry Local

Moderni chat-sovellus Windows 11:lle, joka yhdistää Microsoft Foundry Localin kauniiseen natiivikäyttöliittymään. Rakennettu Electronilla ja noudattaen Microsoftin virallisia Foundry Local -malleja.

## Yleiskatsaus

Tämä esimerkki näyttää, kuinka luoda tuotantovalmiin chat-sovelluksen, joka hyödyntää paikallisia AI-malleja Foundry Localin kautta. Sovellus tarjoaa käyttäjille yksityisyyttä korostavia AI-keskusteluja ilman pilvipalveluriippuvuuksia.

## Ominaisuudet

### 🎨 **Windows 11 Natiivimuotoilu**
- Fluent Design System -integraatio
- Mica-materiaaliefektit ja läpinäkyvyys
- Windows 11:n natiiviteemojen tuki
- Responsiivinen asettelu kaikille näytön kokoille
- Automaattinen tumma/vaalea tila

### 🤖 **AI-mallien integrointi**
- Foundry Local -palvelun integrointi
- Useiden mallien tuki ja niiden vaihtaminen lennossa
- Reaaliaikaiset suoratoistovastaukset
- Paikallisten ja pilvimallien vaihtaminen
- Mallien terveyden seuranta ja tilan tarkistus

### 💬 **Chat-kokemus**
- Reaaliaikaiset kirjoitusilmaisimet
- Viestihistorian säilytys
- Chat-keskustelujen vienti
- Mukautetut järjestelmäkehotteet
- Keskustelujen haarautuminen ja hallinta

### ⚡ **Suorituskykyominaisuudet**
- Viivästetty lataus ja virtualisointi
- Optimoitu renderöinti pitkiä keskusteluja varten
- Mallien esilataus taustalla
- Tehokas muistinhallinta
- Sulavat animaatiot ja siirtymät

## Arkkitehtuuri

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

## Esivaatimukset

### Järjestelmävaatimukset
- **OS**: Windows 11 (suositeltu versio 22H2 tai uudempi)
- **RAM**: Vähintään 8GB, suositus 16GB+ suuremmille malleille
- **Tallennustila**: Vähintään 10GB vapaata tilaa malleille
- **GPU**: Valinnainen, mutta suositeltu nopeampaan mallin käsittelyyn

### Ohjelmistovaatimukset
- **Node.js**: v18.0.0 tai uudempi
- **Foundry Local**: Microsoftin uusin versio
- **Git**: Kloonausta ja kehitystä varten

## Asennus

### 1. Asenna Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Kloonaa ja asenna
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Määritä ympäristö
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Käynnistä sovellus
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Projektin rakenne

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

## Keskeisten ominaisuuksien tarkastelu

### Windows 11 -integraatio

**Fluent Design System**
- Mica-taustamateriaalit
- Akryyliläpinäkyvyys
- Pyöristetyt kulmat ja moderni tilankäyttö
- Windows 11:n natiiviväripaletti
- Semanttiset värikoodit saavutettavuuden parantamiseksi

**Windowsin natiivitoiminnot**
- Jump list -integraatio viimeisille keskusteluille
- Windows-ilmoitukset uusista viesteistä
- Tehtäväpalkin eteneminen mallitoiminnoille
- Järjestelmäpalkin integraatio pikatoiminnoilla
- Windows Hello -tunnistautumisen tuki

### AI-mallien hallinta

**Paikalliset mallit**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybridipilvi/paikallinen tuki**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chat-käyttöliittymän ominaisuudet

**Reaaliaikainen suoratoisto**
- Token-tokenilta vastausten näyttö
- Sulavat kirjoitusanimaatiot
- Peruutettavat pyynnöt
- Kirjoitusilmaisimet ja tilatiedot

**Keskustelujen hallinta**
- Keskusteluhistorian säilytys
- Keskustelujen vienti/tuonti
- Viestien haku ja suodatus
- Keskustelujen haarautuminen
- Mukautetut järjestelmäkehotteet keskustelukohtaisesti

**Saavutettavuus**
- Täysi näppäimistönavigointi
- Näytönlukijan yhteensopivuus
- Korkean kontrastin tilan tuki
- Mukautettavat fonttikoot
- Puheentunnistuksen integrointi

## Käyttöesimerkit

### Peruschat-integraatio
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

### Mallien hallinta
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

### Asetukset ja mukauttaminen
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

## Konfigurointivaihtoehdot

### Sovelluksen asetukset
- **Teema**: Automaattinen, vaalea, tumma tila
- **Malli**: Oletusmallin valinta
- **Suorituskyky**: Mallin käsittelyasetukset
- **Yksityisyys**: Tietojen säilytyskäytännöt
- **Ilmoitukset**: Viesti-ilmoitukset
- **Pikanäppäimet**: Näppäimistön pikanäppäimet

### Chat-asetukset
- **Suoratoisto**: Reaaliaikaisten vastausten käyttö/pysäytys
- **Kontekstin pituus**: Keskustelumuisti
- **Lämpötila**: Vastausten luovuus
- **Maksimitokenit**: Vastausten pituusrajat
- **Järjestelmäkehotteet**: Oletusavustajan käyttäytyminen

### Malliasetukset
- **Automaattinen lataus**: Mallien automaattiset päivitykset
- **Välimuistin koko**: Paikallisten mallien tallennusrajat
- **Suorituskykytila**: CPU vs GPU -asetukset
- **Terveystarkistukset**: Seurantavälit

## Kehitys

### Lähdekoodista rakentaminen
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

### Vianetsintä
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testaus
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Suorituskyvyn optimointi

### Muistinhallinta
- Tehokas viestien virtualisointi
- Automaattinen roskien keräys
- Mallin muistin seuranta
- Resurssien siivous sovelluksen sulkemisen yhteydessä

### Renderöinnin optimointi
- Virtuaalinen vieritys pitkiä keskusteluja varten
- Viestihistorian viivästetty lataus
- Optimoidut React/DOM-päivitykset
- GPU-kiihdytetyt animaatiot

### Verkon optimointi
- Yhteyksien yhdistäminen
- Pyyntöjen eräajo
- Automaattinen uudelleenyritto
- Offline-tilan tuki

## Tietoturva

### Tietosuoja
- Paikallinen ensisijainen arkkitehtuuri
- Ei pilvitiedonsiirtoa (paikallinen tila)
- Keskustelujen salattu tallennus
- Turvallinen tunnistetietojen hallinta

### Sovelluksen tietoturva
- Hiekkalaatikkoon eristetyt renderöintiprosessit
- Sisällön suojauskäytäntö (CSP)
- Ei etäkoodin suorittamista
- Turvallinen IPC-viestintä

## Vianetsintä

### Yleiset ongelmat

**Foundry Local ei käynnisty**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Mallien latausvirheet**
- Varmista riittävä levytila
- Tarkista internetyhteys latauksia varten
- Päivitä GPU-ajurit
- Kokeile eri mallivaihtoehtoja

**Suorituskykyongelmat**
- Seuraa järjestelmän resursseja
- Säädä malliasetuksia
- Ota laitteistokiihdytys käyttöön
- Sulje muut resurssiintensiiviset sovellukset

### Vikasietotila
Ota vikasietoloki käyttöön asettamalla ympäristömuuttujat:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Osallistuminen

### Kehitysympäristön asennus
1. Haarauta arkisto
2. Luo ominaisuushaara
3. Asenna riippuvuudet: `npm install`
4. Tee muutokset ja testaa
5. Lähetä pull request

### Koodityyli
- ESLint-konfiguraatio mukana
- Prettier koodin muotoiluun
- TypeScript tyyppiturvallisuuteen
- JSDoc-kommentit dokumentointiin

## Oppimistavoitteet

Kun olet suorittanut tämän esimerkin, ymmärrät:

1. **Windows 11:n natiivikehitys**
   - Fluent Design System -toteutus
   - Windowsin natiivitoiminnot
   - Electronin tietoturvakäytännöt

2. **AI-mallien integrointi**
   - Foundry Local -palvelun arkkitehtuuri
   - Mallien elinkaaren hallinta
   - Suorituskyvyn seuranta ja optimointi

3. **Reaaliaikaiset chat-järjestelmät**
   - Suoratoistovastausten käsittely
   - Keskustelutilan hallinta
   - Käyttäjäkokemuksen mallit

4. **Tuotantosovelluksen kehitys**
   - Virheiden käsittely ja palautuminen
   - Suorituskyvyn optimointi
   - Tietoturvan huomioiminen
   - Testausstrategiat

## Seuraavat askeleet

- **Esimerkki 09**: Moniagenttinen orkestrointijärjestelmä
- **Esimerkki 10**: Foundry Local työkalujen integrointina
- **Edistyneet aiheet**: Mukautettujen mallien hienosäätö
- **Käyttöönotto**: Yrityskäyttöönoton mallit

## Lisenssi

Tämä esimerkki noudattaa samaa lisenssiä kuin Microsoft Foundry Local -projekti.

---

