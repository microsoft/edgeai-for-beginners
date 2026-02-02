# Windows 11 Chat Sample - Foundry Local

Μια σύγχρονη εφαρμογή συνομιλίας για Windows 11 που ενσωματώνει το Microsoft Foundry Local με μια όμορφη, εγγενή διεπαφή. Χτισμένη με Electron και ακολουθώντας τα επίσημα πρότυπα του Foundry Local της Microsoft.

## Επισκόπηση

Αυτό το δείγμα δείχνει πώς να δημιουργήσετε μια εφαρμογή συνομιλίας έτοιμη για παραγωγή, που αξιοποιεί τοπικά μοντέλα AI μέσω του Foundry Local, προσφέροντας στους χρήστες συνομιλίες AI με έμφαση στην ιδιωτικότητα, χωρίς εξάρτηση από το cloud.

## Χαρακτηριστικά

### 🎨 **Εγγενής Σχεδίαση Windows 11**
- Ενσωμάτωση του Fluent Design System
- Εφέ υλικού Mica και διαφάνειας
- Υποστήριξη θεμάτων Windows 11
- Ανταποκρινόμενη διάταξη για όλες τις οθόνες
- Αυτόματη εναλλαγή σκοτεινής/φωτεινής λειτουργίας

### 🤖 **Ενσωμάτωση Μοντέλων AI**
- Ενσωμάτωση υπηρεσίας Foundry Local
- Υποστήριξη πολλαπλών μοντέλων με δυνατότητα εναλλαγής
- Ροές απαντήσεων σε πραγματικό χρόνο
- Εναλλαγή μεταξύ τοπικών και cloud μοντέλων
- Παρακολούθηση υγείας και κατάστασης μοντέλων

### 💬 **Εμπειρία Συνομιλίας**
- Ενδείξεις πληκτρολόγησης σε πραγματικό χρόνο
- Διατήρηση ιστορικού μηνυμάτων
- Εξαγωγή συνομιλιών
- Προσαρμοσμένες προτροπές συστήματος
- Διαχείριση και διακλάδωση συνομιλιών

### ⚡ **Χαρακτηριστικά Απόδοσης**
- Φόρτωση κατά ζήτηση και εικονικοποίηση
- Βελτιστοποιημένη απόδοση για μεγάλες συνομιλίες
- Προφόρτωση μοντέλων στο παρασκήνιο
- Αποτελεσματική διαχείριση μνήμης
- Ομαλές κινήσεις και μεταβάσεις

## Αρχιτεκτονική

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

## Προαπαιτούμενα

### Απαιτήσεις Συστήματος
- **Λειτουργικό Σύστημα**: Windows 11 (συνιστάται η έκδοση 22H2 ή νεότερη)
- **RAM**: Ελάχιστο 8GB, συνιστάται 16GB+ για μεγαλύτερα μοντέλα
- **Αποθηκευτικός Χώρος**: 10GB+ ελεύθερος χώρος για μοντέλα
- **GPU**: Προαιρετική αλλά συνιστάται για ταχύτερη επεξεργασία

### Εξαρτήσεις Λογισμικού
- **Node.js**: v18.0.0 ή νεότερη
- **Foundry Local**: Τελευταία έκδοση από τη Microsoft
- **Git**: Για κλωνοποίηση και ανάπτυξη

## Εγκατάσταση

### 1. Εγκατάσταση του Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Κλωνοποίηση και Ρύθμιση
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Ρύθμιση Περιβάλλοντος
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Εκτέλεση της Εφαρμογής
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Δομή Έργου

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

## Ανάλυση Βασικών Χαρακτηριστικών

### Ενσωμάτωση Windows 11

**Fluent Design System**
- Υλικά φόντου Mica
- Εφέ διαφάνειας Acrylic
- Στρογγυλεμένες γωνίες και σύγχρονη διάταξη
- Εγγενής παλέτα χρωμάτων Windows 11
- Χρωματικά σύμβολα για προσβασιμότητα

**Εγγενή Χαρακτηριστικά Windows**
- Ενσωμάτωση λίστας άλματος για πρόσφατες συνομιλίες
- Ειδοποιήσεις Windows για νέα μηνύματα
- Πρόοδος στη γραμμή εργασιών για λειτουργίες μοντέλων
- Ενσωμάτωση στο σύστημα ειδοποιήσεων με γρήγορες ενέργειες
- Υποστήριξη πιστοποίησης Windows Hello

### Διαχείριση Μοντέλων AI

**Τοπικά Μοντέλα**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Υβριδική Υποστήριξη Cloud/Τοπικού**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Χαρακτηριστικά Διεπαφής Συνομιλίας

**Ροές σε Πραγματικό Χρόνο**
- Εμφάνιση απαντήσεων ανά token
- Ομαλές κινήσεις πληκτρολόγησης
- Ακύρωση αιτημάτων
- Ενδείξεις πληκτρολόγησης και κατάστασης

**Διαχείριση Συνομιλιών**
- Διατήρηση ιστορικού συνομιλιών
- Εξαγωγή/Εισαγωγή συνομιλιών
- Αναζήτηση και φιλτράρισμα μηνυμάτων
- Διακλάδωση συνομιλιών
- Προσαρμοσμένες προτροπές συστήματος ανά συνομιλία

**Προσβασιμότητα**
- Πλήρης πλοήγηση με πληκτρολόγιο
- Συμβατότητα με αναγνώστες οθόνης
- Υποστήριξη λειτουργίας υψηλής αντίθεσης
- Προσαρμόσιμα μεγέθη γραμματοσειράς
- Ενσωμάτωση φωνητικής εισόδου

## Παραδείγματα Χρήσης

### Βασική Ενσωμάτωση Συνομιλίας
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

### Διαχείριση Μοντέλων
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

### Ρυθμίσεις και Εξατομίκευση
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

## Επιλογές Ρύθμισης

### Ρυθμίσεις Εφαρμογής
- **Θέμα**: Αυτόματο, Φωτεινό, Σκοτεινό
- **Μοντέλο**: Επιλογή προεπιλεγμένου μοντέλου
- **Απόδοση**: Ρυθμίσεις επεξεργασίας
- **Ιδιωτικότητα**: Πολιτικές διατήρησης δεδομένων
- **Ειδοποιήσεις**: Ειδοποιήσεις μηνυμάτων
- **Συντομεύσεις**: Συντομεύσεις πληκτρολογίου

### Ρυθμίσεις Συνομιλίας
- **Ροές**: Ενεργοποίηση/Απενεργοποίηση απαντήσεων σε πραγματικό χρόνο
- **Μήκος Συμφραζομένων**: Μνήμη συνομιλίας
- **Θερμοκρασία**: Δημιουργικότητα απαντήσεων
- **Μέγιστοι Tokens**: Όρια μήκους απαντήσεων
- **Προτροπές Συστήματος**: Προεπιλεγμένη συμπεριφορά βοηθού

### Ρυθμίσεις Μοντέλων
- **Αυτόματη Λήψη**: Αυτόματες ενημερώσεις μοντέλων
- **Μέγεθος Cache**: Όρια αποθήκευσης τοπικών μοντέλων
- **Λειτουργία Απόδοσης**: Προτιμήσεις CPU vs GPU
- **Έλεγχοι Υγείας**: Διαστήματα παρακολούθησης

## Ανάπτυξη

### Δημιουργία από Πηγαίο Κώδικα
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

### Εντοπισμός Σφαλμάτων
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Δοκιμές
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Βελτιστοποίηση Απόδοσης

### Διαχείριση Μνήμης
- Αποτελεσματική εικονικοποίηση μηνυμάτων
- Αυτόματη συλλογή απορριμμάτων
- Παρακολούθηση μνήμης μοντέλων
- Καθαρισμός πόρων κατά την έξοδο

### Βελτιστοποίηση Απόδοσης Απόδοσης
- Εικονική κύλιση για μεγάλες συνομιλίες
- Φόρτωση ιστορικού μηνυμάτων κατά ζήτηση
- Βελτιστοποιημένες ενημερώσεις React/DOM
- Κινήσεις με επιτάχυνση GPU

### Βελτιστοποίηση Δικτύου
- Συγκέντρωση συνδέσεων
- Ομαδοποίηση αιτημάτων
- Αυτόματη λογική επαναπροσπάθειας
- Υποστήριξη λειτουργίας εκτός σύνδεσης

## Σκέψεις Ασφαλείας

### Ιδιωτικότητα Δεδομένων
- Αρχιτεκτονική με προτεραιότητα το τοπικό
- Χωρίς μετάδοση δεδομένων στο cloud (τοπική λειτουργία)
- Κρυπτογραφημένη αποθήκευση συνομιλιών
- Ασφαλής διαχείριση διαπιστευτηρίων

### Ασφάλεια Εφαρμογής
- Απομονωμένες διεργασίες renderer
- Πολιτική Ασφάλειας Περιεχομένου (CSP)
- Χωρίς απομακρυσμένη εκτέλεση κώδικα
- Ασφαλής επικοινωνία IPC

## Επίλυση Προβλημάτων

### Συνηθισμένα Θέματα

**Το Foundry Local Δεν Ξεκινά**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Αποτυχίες Φόρτωσης Μοντέλων**
- Επαληθεύστε επαρκή χώρο στο δίσκο
- Ελέγξτε τη σύνδεση στο διαδίκτυο για λήψεις
- Βεβαιωθείτε ότι οι οδηγοί GPU είναι ενημερωμένοι
- Δοκιμάστε διαφορετικές παραλλαγές μοντέλων

**Θέματα Απόδοσης**
- Παρακολουθήστε τους πόρους του συστήματος
- Ρυθμίστε τις ρυθμίσεις μοντέλων
- Ενεργοποιήστε την επιτάχυνση υλικού
- Κλείστε άλλες εφαρμογές που καταναλώνουν πόρους

### Λειτουργία Εντοπισμού Σφαλμάτων
Ενεργοποιήστε την καταγραφή εντοπισμού σφαλμάτων ορίζοντας μεταβλητές περιβάλλοντος:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Συνεισφορά

### Ρύθμιση Ανάπτυξης
1. Κλωνοποιήστε το αποθετήριο
2. Δημιουργήστε ένα κλάδο χαρακτηριστικών
3. Εγκαταστήστε εξαρτήσεις: `npm install`
4. Κάντε αλλαγές και δοκιμές
5. Υποβάλετε ένα αίτημα συγχώνευσης

### Στυλ Κώδικα
- Παρέχεται διαμόρφωση ESLint
- Prettier για μορφοποίηση κώδικα
- TypeScript για ασφάλεια τύπων
- Σχόλια JSDoc για τεκμηρίωση

## Μαθησιακά Αποτελέσματα

Μετά την ολοκλήρωση αυτού του δείγματος, θα κατανοήσετε:

1. **Εγγενής Ανάπτυξη Windows 11**
   - Εφαρμογή του Fluent Design System
   - Εγγενής ενσωμάτωση Windows
   - Βέλτιστες πρακτικές ασφάλειας Electron

2. **Ενσωμάτωση Μοντέλων AI**
   - Αρχιτεκτονική υπηρεσίας Foundry Local
   - Διαχείριση κύκλου ζωής μοντέλων
   - Παρακολούθηση και βελτιστοποίηση απόδοσης

3. **Συστήματα Συνομιλίας σε Πραγματικό Χρόνο**
   - Διαχείριση ροών απαντήσεων
   - Διαχείριση κατάστασης συνομιλιών
   - Πρότυπα εμπειρίας χρήστη

4. **Ανάπτυξη Εφαρμογών Παραγωγής**
   - Διαχείριση σφαλμάτων και ανάκαμψη
   - Βελτιστοποίηση απόδοσης
   - Σκέψεις ασφαλείας
   - Στρατηγικές δοκιμών

## Επόμενα Βήματα

- **Δείγμα 09**: Σύστημα Ορχήστρωσης Πολλαπλών Πρακτόρων
- **Δείγμα 10**: Το Foundry Local ως Ενσωμάτωση Εργαλείων
- **Προχωρημένα Θέματα**: Προσαρμοσμένη εκπαίδευση μοντέλων
- **Ανάπτυξη**: Πρότυπα ανάπτυξης για επιχειρήσεις

## Άδεια Χρήσης

Αυτό το δείγμα ακολουθεί την ίδια άδεια χρήσης με το έργο Microsoft Foundry Local.

---

