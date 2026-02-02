# AGENTS.md

> **Οδηγός Ανάπτυξης για Συμβολή στο EdgeAI για Αρχάριους**
> 
> Το παρόν έγγραφο παρέχει ολοκληρωμένες πληροφορίες για προγραμματιστές, πράκτορες AI και συνεισφέροντες που εργάζονται με αυτό το αποθετήριο. Καλύπτει τη ρύθμιση, τις ροές εργασίας ανάπτυξης, τη δοκιμή και τις βέλτιστες πρακτικές.
> 
> **Τελευταία Ενημέρωση**: 30 Οκτωβρίου 2025 | **Έκδοση Εγγράφου**: 3.0

## Πίνακας Περιεχομένων

- [Επισκόπηση Έργου](../..)
- [Δομή Αποθετηρίου](../..)
- [Προαπαιτούμενα](../..)
- [Εντολές Ρύθμισης](../..)
- [Ροή Εργασίας Ανάπτυξης](../..)
- [Οδηγίες Δοκιμής](../..)
- [Κατευθυντήριες Γραμμές Στυλ Κώδικα](../..)
- [Κατευθυντήριες Γραμμές Αιτήσεων Ενσωμάτωσης](../..)
- [Σύστημα Μετάφρασης](../..)
- [Τοπική Ενσωμάτωση Foundry](../..)
- [Δημιουργία και Ανάπτυξη](../..)
- [Συνηθισμένα Προβλήματα και Αντιμετώπιση](../..)
- [Πρόσθετοι Πόροι](../..)
- [Σημειώσεις Ειδικές για το Έργο](../..)
- [Λήψη Βοήθειας](../..)

## Επισκόπηση Έργου

Το EdgeAI για Αρχάριους είναι ένα ολοκληρωμένο εκπαιδευτικό αποθετήριο που διδάσκει την ανάπτυξη Edge AI με Μικρά Μοντέλα Γλώσσας (SLMs). Το μάθημα καλύπτει τις βασικές αρχές του EdgeAI, την ανάπτυξη μοντέλων, τις τεχνικές βελτιστοποίησης και τις υλοποιήσεις έτοιμες για παραγωγή χρησιμοποιώντας το Microsoft Foundry Local και διάφορα πλαίσια AI.

**Κύριες Τεχνολογίες:**
- Python 3.8+ (κύρια γλώσσα για δείγματα AI/ML)
- .NET C# (δείγματα AI/ML)
- JavaScript/Node.js με Electron (για εφαρμογές επιτραπέζιων υπολογιστών)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Πλαίσια AI: LangChain, Semantic Kernel, Chainlit
- Βελτιστοποίηση Μοντέλων: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Τύπος Αποθετηρίου:** Εκπαιδευτικό περιεχόμενο με 8 ενότητες και 10 ολοκληρωμένες δείγματα εφαρμογών

**Αρχιτεκτονική:** Πολυεπίπεδο μονοπάτι μάθησης με πρακτικά δείγματα που δείχνουν μοτίβα ανάπτυξης Edge AI

## Δομή Αποθετηρίου

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Προαπαιτούμενα

### Απαιτούμενα Εργαλεία

- **Python 3.8+** - Για δείγματα AI/ML και σημειωματάρια
- **Node.js 16+** - Για την εφαρμογή δείγματος Electron
- **Git** - Για έλεγχο εκδόσεων
- **Microsoft Foundry Local** - Για την εκτέλεση μοντέλων AI τοπικά

### Συνιστώμενα Εργαλεία

- **Visual Studio Code** - Με επεκτάσεις Python, Jupyter και Pylance
- **Windows Terminal** - Για καλύτερη εμπειρία γραμμής εντολών (χρήστες Windows)
- **Docker** - Για ανάπτυξη σε κοντέινερ (προαιρετικό)

### Απαιτήσεις Συστήματος

- **RAM**: Ελάχιστο 8GB, συνιστάται 16GB+ για σενάρια πολλαπλών μοντέλων
- **Αποθηκευτικός Χώρος**: Ελεύθερος χώρος 10GB+ για μοντέλα και εξαρτήσεις
- **Λειτουργικό Σύστημα**: Windows 10/11, macOS 11+, ή Linux (Ubuntu 20.04+)
- **Υλικό**: CPU με υποστήριξη AVX2; GPU (CUDA, Qualcomm NPU) προαιρετική αλλά συνιστάται

### Γνώσεις Προαπαιτούμενες

- Βασική κατανόηση προγραμματισμού Python
- Εξοικείωση με γραμμές εντολών
- Κατανόηση εννοιών AI/ML (για ανάπτυξη δειγμάτων)
- Ροές εργασίας Git και διαδικασίες αιτήσεων ενσωμάτωσης

## Εντολές Ρύθμισης

### Ρύθμιση Αποθετηρίου

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Ρύθμιση Δείγματος Python (Ενότητα08 και δείγματα Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Ρύθμιση Δείγματος Node.js (Δείγμα 08 - Εφαρμογή Συνομιλίας Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Ρύθμιση Foundry Local

Το Foundry Local απαιτείται για την εκτέλεση των δειγμάτων. Κατεβάστε και εγκαταστήστε από το επίσημο αποθετήριο:

**Εγκατάσταση:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Χειροκίνητα**: Κατεβάστε από τη [σελίδα εκδόσεων](https://github.com/microsoft/Foundry-Local/releases)

**Γρήγορη Εκκίνηση:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Σημείωση**: Το Foundry Local επιλέγει αυτόματα την καλύτερη παραλλαγή μοντέλου για το υλικό σας (CUDA GPU, Qualcomm NPU, ή CPU).

## Ροή Εργασίας Ανάπτυξης

### Ανάπτυξη Περιεχομένου

Αυτό το αποθετήριο περιέχει κυρίως **εκπαιδευτικό περιεχόμενο Markdown**. Κατά την πραγματοποίηση αλλαγών:

1. Επεξεργαστείτε αρχεία `.md` στους κατάλληλους φακέλους ενοτήτων
2. Ακολουθήστε τα υπάρχοντα πρότυπα μορφοποίησης
3. Βεβαιωθείτε ότι τα παραδείγματα κώδικα είναι ακριβή και δοκιμασμένα
4. Ενημερώστε το αντίστοιχο μεταφρασμένο περιεχόμενο εάν είναι απαραίτητο (ή αφήστε την αυτοματοποίηση να το χειριστεί)

### Ανάπτυξη Δειγμάτων Εφαρμογών

Για δείγματα Python της Ενότητας08 (δείγματα 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Για δείγματα Python του Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Για δείγμα Electron (δείγμα 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Δοκιμή Δειγμάτων Εφαρμογών

Τα δείγματα Python δεν έχουν αυτοματοποιημένες δοκιμές αλλά μπορούν να επικυρωθούν με την εκτέλεσή τους:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Το δείγμα Electron διαθέτει υποδομή δοκιμών:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Οδηγίες Δοκιμής

### Επικύρωση Περιεχομένου

Το αποθετήριο χρησιμοποιεί αυτοματοποιημένες ροές εργασίας μετάφρασης. Δεν απαιτείται χειροκίνητη δοκιμή για μεταφράσεις.

**Χειροκίνητη επικύρωση για αλλαγές περιεχομένου:**
1. Προεπισκόπηση απόδοσης Markdown μέσω προβολής αρχείων `.md`
2. Επαλήθευση ότι όλοι οι σύνδεσμοι οδηγούν σε έγκυρους στόχους
3. Δοκιμή οποιωνδήποτε αποσπασμάτων κώδικα που περιλαμβάνονται στην τεκμηρίωση
4. Έλεγχος ότι οι εικόνες φορτώνονται σωστά

### Δοκιμή Δειγμάτων Εφαρμογών

**Module08/samples/08 (εφαρμογή Electron) διαθέτει ολοκληρωμένες δοκιμές:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Τα δείγματα Python πρέπει να δοκιμάζονται χειροκίνητα:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Κατευθυντήριες Γραμμές Στυλ Κώδικα

### Περιεχόμενο Markdown

- Χρησιμοποιήστε συνεπή ιεραρχία επικεφαλίδων (# για τίτλο, ## για κύριες ενότητες, ### για υποενότητες)
- Συμπεριλάβετε μπλοκ κώδικα με καθορισμό γλώσσας: ```python, ```bash, ```javascript
- Ακολουθήστε την υπάρχουσα μορφοποίηση για πίνακες, λίστες και έμφαση
- Κρατήστε τις γραμμές ευανάγνωστες (περίπου ~80-100 χαρακτήρες, αλλά όχι αυστηρά)
- Χρησιμοποιήστε σχετικούς συνδέσμους για εσωτερικές αναφορές

### Στυλ Κώδικα Python

- Ακολουθήστε τις συμβάσεις PEP 8
- Χρησιμοποιήστε υποδείξεις τύπων όπου είναι κατάλληλο
- Συμπεριλάβετε docstrings για συναρτήσεις και κλάσεις
- Χρησιμοποιήστε ουσιαστικά ονόματα μεταβλητών
- Κρατήστε τις συναρτήσεις εστιασμένες και συνοπτικές

### Στυλ Κώδικα JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Βασικές συμβάσεις:**
- Παρέχεται διαμόρφωση ESLint στο δείγμα 08
- Prettier για μορφοποίηση κώδικα
- Χρησιμοποιήστε σύγχρονη σύνταξη ES6+
- Ακολουθήστε τα υπάρχοντα μοτίβα στον κώδικα

## Κατευθυντήριες Γραμμές Αιτήσεων Ενσωμάτωσης

### Ροή Εργασίας Συμβολής

1. **Κλωνοποιήστε το αποθετήριο** και δημιουργήστε ένα νέο branch από το `main`
2. **Κάντε τις αλλαγές σας** ακολουθώντας τις κατευθυντήριες γραμμές στυλ κώδικα
3. **Δοκιμάστε διεξοδικά** χρησιμοποιώντας τις οδηγίες δοκιμής παραπάνω
4. **Κάντε commit με σαφή μηνύματα** ακολουθώντας τη μορφή συμβατικών commits
5. **Προωθήστε στο fork σας** και δημιουργήστε αίτηση ενσωμάτωσης
6. **Απαντήστε στα σχόλια** από τους συντηρητές κατά την αναθεώρηση

### Συμβάσεις Ονοματοδοσίας Branch

- `feature/<module>-<description>` - Για νέα χαρακτηριστικά ή περιεχόμενο
- `fix/<module>-<description>` - Για διορθώσεις σφαλμάτων
- `docs/<description>` - Για βελτιώσεις τεκμηρίωσης
- `refactor/<description>` - Για αναδιάρθρωση κώδικα

### Μορφή Μηνύματος Commit

Ακολουθήστε [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Παραδείγματα:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Μορφή Τίτλου
```
[ModuleXX] Brief description of change
```
ή
```
[Module08/samples/XX] Description for sample changes
```

### Κώδικας Συμπεριφοράς

Όλοι οι συνεισφέροντες πρέπει να ακολουθούν τον [Κώδικα Συμπεριφοράς Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/). Παρακαλούμε ανατρέξτε στο [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) πριν συνεισφέρετε.

### Πριν την Υποβολή

**Για αλλαγές περιεχομένου:**
- Προεπισκόπηση όλων των τροποποιημένων αρχείων Markdown
- Επαλήθευση συνδέσμων και εικόνων
- Έλεγχος για τυπογραφικά και γραμματικά λάθη

**Για αλλαγές δείγματος κώδικα (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Για αλλαγές δειγμάτων Python:**
- Δοκιμή ότι το δείγμα εκτελείται επιτυχώς
- Επαλήθευση ότι η διαχείριση σφαλμάτων λειτουργεί
- Έλεγχος συμβατότητας με το Foundry Local

### Διαδικασία Αναθεώρησης

- Οι αλλαγές εκπαιδευτικού περιεχομένου αναθεωρούνται για ακρίβεια και σαφήνεια
- Τα δείγματα κώδικα δοκιμάζονται για λειτουργικότητα
- Οι ενημερώσεις μετάφρασης χειρίζονται αυτόματα από το GitHub Actions

## Σύστημα Μετάφρασης

**ΣΗΜΑΝΤΙΚΟ:** Αυτό το αποθετήριο χρησιμοποιεί αυτοματοποιημένη μετάφραση μέσω GitHub Actions.

- Οι μεταφράσεις βρίσκονται στον φάκελο `/translations/` (50+ γλώσσες)
- Αυτοματοποιημένες μέσω της ροής εργασίας `co-op-translator.yml`
- **ΜΗΝ επεξεργάζεστε χειροκίνητα αρχεία μετάφρασης** - θα αντικατασταθούν
- Επεξεργαστείτε μόνο τα αρχεία πηγής στα Αγγλικά στον ριζικό φάκελο και στους φακέλους ενοτήτων
- Οι μεταφράσεις δημιουργούνται αυτόματα με την προώθηση στο branch `main`

## Τοπική Ενσωμάτωση Foundry

Τα περισσότερα δείγματα της Ενότητας08 απαιτούν την εκτέλεση του Microsoft Foundry Local.

### Εγκατάσταση & Ρύθμιση

**Εγκατάσταση Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Εγκατάσταση Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Εκκίνηση Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Χρήση SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Επαλήθευση Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Μεταβλητές Περιβάλλοντος για Δείγματα

Τα περισσότερα δείγματα χρησιμοποιούν αυτές τις μεταβλητές περιβάλλοντος:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Σημείωση**: Όταν χρησιμοποιείτε το `FoundryLocalManager`, το SDK χειρίζεται αυτόματα την ανακάλυψη υπηρεσιών και τη φόρτωση μοντέλων. Τα ψευδώνυμα μοντέλων (όπως `phi-3.5-mini`) εξασφαλίζουν ότι επιλέγεται η καλύτερη παραλλαγή για το υλικό σας.

## Δημιουργία και Ανάπτυξη

### Ανάπτυξη Περιεχομένου

Αυτό το αποθετήριο είναι κυρίως τεκμηρίωση - δεν απαιτείται διαδικασία δημιουργίας για το περιεχόμενο.

### Δημιουργία Εφαρμογών Δείγματος

**Εφαρμογή Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Δείγματα Python:**
Δεν υπάρχει διαδικασία δημιουργίας - τα δείγματα εκτελούνται απευθείας με τον διερμηνέα Python.

## Συνηθισμένα Προβλήματα και Αντιμετώπιση

> **Συμβουλή**: Ελέγξτε τα [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) για γνωστά προβλήματα και λύσεις.

### Κρίσιμα Προβλήματα (Αποκλειστικά)

#### Το Foundry Local δεν λειτουργεί
**Πρόβλημα:** Τα δείγματα αποτυγχάνουν με σφάλματα σύνδεσης

**Λύση:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Συνηθισμένα Προβλήματα (Μέτρια)

#### Προβλήματα Εικονικού Περιβάλλοντος Python
**Πρόβλημα:** Σφάλματα εισαγωγής μονάδων

**Λύση:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Προβλήματα Δημιουργίας Electron
**Πρόβλημα:** Αποτυχίες εγκατάστασης npm ή δημιουργίας

**Λύση:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Προβλήματα Ροής Εργασίας (Μικρά)

#### Συγκρούσεις Ροής Εργασίας Μετάφρασης
**Πρόβλημα:** Η αίτηση ενσωμάτωσης μετάφρασης συγκρούεται με τις αλλαγές σας

**Λύση:**
- Επεξεργαστείτε μόνο αρχεία πηγής στα Αγγλικά
- Αφήστε την αυτοματοποιημένη ροή εργασίας μετάφρασης να χειριστεί τις μεταφράσεις
- Εάν προκύψουν συγκρούσεις, συγχωνεύστε το `main` στο branch σας μετά τη συγχώνευση των μεταφράσεων

#### Αποτυχίες Λήψης Μοντέλων
**Πρόβλημα:** Το Foundry Local αποτυγχάνει να κατεβάσει μοντέλα

**Λύση:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Πρόσθετοι Πόροι

### Μ
10. **10-Πλαίσιο Εργαλείων Foundry** - Ενσωμάτωση LangChain/Semantic Kernel

### Εφαρμογές Δείγματος Εργαστηρίου

Το Εργαστήριο περιλαμβάνει 6 προοδευτικές συνεδρίες με πρακτικές εφαρμογές:

1. **Συνεδρία 01** - Εκκίνηση συνομιλίας με ενσωμάτωση Foundry Local
2. **Συνεδρία 02** - Αξιολόγηση και αγωγός RAG με RAGAS
3. **Συνεδρία 03** - Αξιολόγηση μοντέλων ανοιχτού κώδικα
4. **Συνεδρία 04** - Σύγκριση και επιλογή μοντέλων
5. **Συνεδρία 05** - Συστήματα ορχήστρας πολλαπλών πρακτόρων
6. **Συνεδρία 06** - Δρομολόγηση μοντέλων και διαχείριση αγωγών

Κάθε δείγμα παρουσιάζει διαφορετικές πτυχές ανάπτυξης edge AI με το Foundry Local.

### Σκέψεις για την Απόδοση

- Τα SLMs είναι βελτιστοποιημένα για ανάπτυξη σε edge (2-16GB RAM)
- Η τοπική πρόβλεψη παρέχει χρόνους απόκρισης 50-500ms
- Οι τεχνικές ποσοτικοποίησης επιτυγχάνουν μείωση μεγέθους κατά 75% με διατήρηση απόδοσης 85%
- Δυνατότητες συνομιλίας σε πραγματικό χρόνο με τοπικά μοντέλα

### Ασφάλεια και Ιδιωτικότητα

- Όλη η επεξεργασία γίνεται τοπικά - δεν αποστέλλονται δεδομένα στο cloud
- Κατάλληλο για εφαρμογές ευαίσθητες στην ιδιωτικότητα (υγειονομική περίθαλψη, χρηματοοικονομικά)
- Πληροί τις απαιτήσεις κυριαρχίας δεδομένων
- Το Foundry Local λειτουργεί εξ ολοκλήρου σε τοπικό υλικό

## Λήψη Βοήθειας

### Τεκμηρίωση

- **Κύριο README**: [README.md](README.md) - Επισκόπηση αποθετηρίου και μονοπάτια μάθησης
- **Οδηγός Μελέτης**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Πόροι μάθησης και χρονοδιάγραμμα
- **Υποστήριξη**: [SUPPORT.md](SUPPORT.md) - Πώς να λάβετε βοήθεια
- **Ασφάλεια**: [SECURITY.md](SECURITY.md) - Αναφορά ζητημάτων ασφαλείας

### Υποστήριξη Κοινότητας

- **GitHub Issues**: [Αναφορά σφαλμάτων ή αίτηση λειτουργιών](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Κάντε ερωτήσεις και μοιραστείτε ιδέες](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Τεχνικά ζητήματα με το Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Επικοινωνία

- **Συντηρητές**: Δείτε [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Ζητήματα Ασφαλείας**: Ακολουθήστε την υπεύθυνη αποκάλυψη στο [SECURITY.md](SECURITY.md)
- **Υποστήριξη Microsoft**: Για υποστήριξη επιχειρήσεων, επικοινωνήστε με την εξυπηρέτηση πελατών της Microsoft

### Πρόσθετοι Πόροι

- **Microsoft Learn**: [Μονοπάτια Μάθησης AI και Μηχανικής Μάθησης](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Τεκμηρίωση Foundry Local**: [Επίσημα Έγγραφα](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Δείγματα Κοινότητας**: Ελέγξτε [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) για συνεισφορές της κοινότητας

---

**Αυτό είναι ένα εκπαιδευτικό αποθετήριο που επικεντρώνεται στη διδασκαλία της ανάπτυξης Edge AI. Το κύριο μοτίβο συνεισφοράς είναι η βελτίωση του εκπαιδευτικού περιεχομένου και η προσθήκη/ενίσχυση δειγμάτων εφαρμογών που παρουσιάζουν έννοιες του Edge AI.**

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.