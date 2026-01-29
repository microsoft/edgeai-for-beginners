# Συνεδρία 1: Ξεκινώντας με το Foundry Local

## Περίληψη

Μάθετε πώς να εγκαταστήσετε, να ρυθμίσετε και να εκτελέσετε τα πρώτα σας μοντέλα AI χρησιμοποιώντας το Microsoft Foundry Local. Αυτή η πρακτική συνεδρία παρέχει μια βήμα προς βήμα εισαγωγή στην τοπική επεξεργασία, από την εγκατάσταση μέχρι τη δημιουργία της πρώτης σας εφαρμογής συνομιλίας χρησιμοποιώντας μοντέλα όπως τα Phi-4, Qwen και DeepSeek.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτής της συνεδρίας, θα μπορείτε:

- **Εγκατάσταση και Ρύθμιση**: Να ρυθμίσετε το Foundry Local με σωστή επαλήθευση εγκατάστασης
- **Κατανόηση των Εντολών CLI**: Να χρησιμοποιείτε το Foundry Local CLI για διαχείριση και ανάπτυξη μοντέλων
- **Εκτέλεση του Πρώτου Μοντέλου**: Να αναπτύξετε και να αλληλεπιδράσετε επιτυχώς με ένα τοπικό μοντέλο AI
- **Δημιουργία Εφαρμογής Συνομιλίας**: Να δημιουργήσετε μια βασική εφαρμογή συνομιλίας χρησιμοποιώντας το Foundry Local Python SDK
- **Κατανόηση Τοπικού AI**: Να κατανοήσετε τα βασικά της τοπικής επεξεργασίας και διαχείρισης μοντέλων

## Προαπαιτούμενα

### Απαιτήσεις Συστήματος

- **Windows**: Windows 11 (22H2 ή νεότερο) Ή **macOS**: macOS 11+ (περιορισμένη υποστήριξη)
- **RAM**: Ελάχιστο 8GB, συνιστάται 16GB+
- **Αποθηκευτικός Χώρος**: Τουλάχιστον 10GB ελεύθερος χώρος για τα μοντέλα
- **Python**: Εγκατεστημένη έκδοση 3.10 ή νεότερη
- **Δικαιώματα Διαχειριστή**: Δικαιώματα διαχειριστή για την εγκατάσταση

### Περιβάλλον Ανάπτυξης

- Visual Studio Code με επέκταση Python (συνιστάται)
- Πρόσβαση στη γραμμή εντολών (PowerShell στα Windows, Terminal στο macOS)
- Git για κλωνοποίηση αποθετηρίων (προαιρετικό)

## Ροή Εργαστηρίου (30 λεπτά)

### Βήμα 1: Εγκατάσταση του Foundry Local (5 λεπτά)

#### Εγκατάσταση στα Windows

Εγκαταστήστε το Foundry Local χρησιμοποιώντας τον διαχειριστή πακέτων των Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Εναλλακτικά: Κατεβάστε απευθείας από το [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Εγκατάσταση στο macOS (Περιορισμένη Υποστήριξη)

> [!NOTE] 
> Η υποστήριξη για macOS είναι προς το παρόν σε προεπισκόπηση. Ελέγξτε την επίσημη τεκμηρίωση για την πιο πρόσφατη διαθεσιμότητα.

Αν είναι διαθέσιμο, εγκαταστήστε μέσω Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Εναλλακτική για χρήστες macOS:**
- Χρησιμοποιήστε ένα VM Windows 11 (Parallels/UTM) και ακολουθήστε τα βήματα για Windows
- Εκτελέστε μέσω container αν είναι διαθέσιμο και ρυθμίστε το `FOUNDRY_LOCAL_ENDPOINT`

### Βήμα 2: Επαλήθευση Εγκατάστασης (3 λεπτά)

Μετά την εγκατάσταση, επανεκκινήστε το τερματικό σας και επαληθεύστε ότι το Foundry Local λειτουργεί:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Η αναμενόμενη έξοδος πρέπει να δείχνει πληροφορίες έκδοσης και διαθέσιμες εντολές.

### Βήμα 3: Ρύθμιση Περιβάλλοντος Python (5 λεπτά)

Δημιουργήστε ένα ειδικό περιβάλλον Python για αυτό το εργαστήριο:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Βήμα 4: Εκτέλεση του Πρώτου Μοντέλου (7 λεπτά)

Ας εκτελέσουμε το πρώτο μας μοντέλο AI τοπικά!

#### Ξεκινήστε με το Phi-4 Mini (Συνιστώμενο Πρώτο Μοντέλο)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Αυτή η εντολή κατεβάζει το μοντέλο (για πρώτη φορά) και ξεκινά αυτόματα την υπηρεσία Foundry Local.

#### Ελέγξτε Τι Τρέχει

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Δοκιμάστε Διαφορετικά Μοντέλα

Μόλις το phi-4-mini λειτουργήσει, πειραματιστείτε με άλλα μοντέλα:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Βήμα 5: Δημιουργία της Πρώτης Εφαρμογής Συνομιλίας (10 λεπτά)

Ας δημιουργήσουμε τώρα μια εφαρμογή Python που χρησιμοποιεί τα μοντέλα που μόλις ξεκινήσαμε.

#### Δημιουργία του Script Συνομιλίας

Δημιουργήστε ένα νέο αρχείο με όνομα `my_first_chat.py` (ή χρησιμοποιήστε το παρεχόμενο δείγμα):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Σχετικά Παραδείγματα**: Για πιο προχωρημένη χρήση, δείτε:
>
> - **Δείγμα Python**: `Workshop/samples/session01/chat_bootstrap.py` - Περιλαμβάνει ροές απαντήσεων και διαχείριση σφαλμάτων
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Διαδραστική έκδοση με λεπτομερείς εξηγήσεις

#### Δοκιμή της Εφαρμογής Συνομιλίας

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Εναλλακτικά: Χρησιμοποιήστε απευθείας τα παρεχόμενα δείγματα

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Ή εξερευνήστε το διαδραστικό notebook
Ανοίξτε το Workshop/notebooks/session01_chat_bootstrap.ipynb στο VS Code

Δοκιμάστε αυτές τις παραδειγματικές συνομιλίες:

- "Τι είναι το Microsoft Foundry Local;"
- "Αναφέρετε 3 πλεονεκτήματα της εκτέλεσης μοντέλων AI τοπικά"
- "Βοηθήστε με να κατανοήσω το edge AI"

## Τι Έχετε Επιτύχει

Συγχαρητήρια! Έχετε επιτυχώς:

1. ✅ **Εγκαταστήσει το Foundry Local** και επαληθεύσει ότι λειτουργεί
2. ✅ **Ξεκινήσει το πρώτο σας μοντέλο AI** (phi-4-mini) τοπικά
3. ✅ **Δοκιμάσει διαφορετικά μοντέλα** μέσω της γραμμής εντολών
4. ✅ **Δημιουργήσει μια εφαρμογή συνομιλίας** που συνδέεται με το τοπικό AI σας
5. ✅ **Ζήσει την τοπική επεξεργασία AI** χωρίς εξαρτήσεις από το cloud

## Κατανόηση Τι Συνέβη

### Τοπική Επεξεργασία AI

- Τα μοντέλα AI σας εκτελούνται εξ ολοκλήρου στον υπολογιστή σας
- Δεν αποστέλλονται δεδομένα στο cloud
- Οι απαντήσεις δημιουργούνται τοπικά χρησιμοποιώντας τη CPU/GPU σας
- Η ιδιωτικότητα και η ασφάλεια διατηρούνται

### Διαχείριση Μοντέλων

- Το `foundry model run` κατεβάζει και ξεκινά τα μοντέλα
- Το **FoundryLocalManager SDK** χειρίζεται αυτόματα την εκκίνηση της υπηρεσίας και τη φόρτωση των μοντέλων
- Τα μοντέλα αποθηκεύονται τοπικά για μελλοντική χρήση
- Πολλαπλά μοντέλα μπορούν να κατέβουν, αλλά συνήθως εκτελείται ένα κάθε φορά
- Η υπηρεσία διαχειρίζεται αυτόματα τον κύκλο ζωής των μοντέλων

### Προσεγγίσεις SDK vs CLI

- **Προσέγγιση CLI**: Χειροκίνητη διαχείριση μοντέλων με `foundry model run <model>`
- **Προσέγγιση SDK**: Αυτόματη διαχείριση υπηρεσίας + μοντέλων με `FoundryLocalManager(alias)`
- **Σύσταση**: Χρησιμοποιήστε το SDK για εφαρμογές, το CLI για δοκιμές και εξερεύνηση

## Αναφορά Κοινών Εντολών

### Βασικές Εντολές CLI

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Συστάσεις Μοντέλων

- **phi-4-mini**: Καλύτερο μοντέλο για αρχάριους - γρήγορο, ελαφρύ, καλή ποιότητα
- **qwen2.5-0.5b**: Ταχύτερη επεξεργασία, ελάχιστη χρήση μνήμης
- **gpt-oss-20b**: Υψηλότερη ποιότητα απαντήσεων, απαιτεί περισσότερους πόρους
- **deepseek-coder-1.3b**: Βελτιστοποιημένο για προγραμματισμό και εργασίες κώδικα

## Επίλυση Προβλημάτων

### "Η εντολή Foundry δεν βρέθηκε"

**Λύση:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Το μοντέλο απέτυχε να φορτωθεί"

**Λύση:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Η σύνδεση απορρίφθηκε στο localhost"

**Λύση:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Επόμενα Βήματα

### Άμεσες Ενέργειες

1. **Πειραματιστείτε** με διαφορετικά μοντέλα και ερωτήματα
2. **Τροποποιήστε** την εφαρμογή συνομιλίας σας για να δοκιμάσετε διαφορετικά μοντέλα
3. **Δημιουργήστε** τα δικά σας ερωτήματα και δοκιμάστε απαντήσεις
4. **Εξερευνήστε** τη Συνεδρία 2: Δημιουργία εφαρμογών RAG

### Προχωρημένο Μονοπάτι Μάθησης

1. **Συνεδρία 2**: Δημιουργία λύσεων AI με RAG (Retrieval-Augmented Generation)
2. **Συνεδρία 3**: Σύγκριση διαφορετικών μοντέλων ανοιχτού κώδικα
3. **Συνεδρία 4**: Εργασία με μοντέλα αιχμής
4. **Συνεδρία 5**: Δημιουργία συστημάτων AI πολλαπλών πρακτόρων

## Μεταβλητές Περιβάλλοντος (Προαιρετικό)

Για πιο προχωρημένη χρήση, μπορείτε να ορίσετε αυτές τις μεταβλητές περιβάλλοντος:

| Μεταβλητή | Σκοπός | Παράδειγμα |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Προεπιλεγμένο μοντέλο προς χρήση | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Υπέρβαση URL endpoint | `http://localhost:5273/v1` |

Δημιουργήστε ένα αρχείο `.env` στον κατάλογο του έργου σας:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Πρόσθετοι Πόροι

### Τεκμηρίωση

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Δείγματα Κώδικα

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Πλήρης εφαρμογή συνομιλίας με streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Διαδραστικό σεμινάριο  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Κοινότητα

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Διάρκεια Συνεδρίας**: 30 λεπτά πρακτική + 15 λεπτά Q&A  
**Επίπεδο Δυσκολίας**: Αρχάριος  
**Προαπαιτούμενα**: Windows 11/macOS 11+, Python 3.10+, Δικαιώματα διαχειριστή

## Παράδειγμα Σεναρίου Εργαστηρίου

### Πραγματικό Πλαίσιο

**Σενάριο**: Μια ομάδα IT μιας επιχείρησης πρέπει να αξιολογήσει την επεξεργασία AI στη συσκευή για την επεξεργασία ευαίσθητων σχολίων εργαζομένων χωρίς να στέλνει δεδομένα σε εξωτερικές υπηρεσίες.

**Ο Στόχος Σας**: Να δείξετε ότι τα τοπικά μοντέλα AI μπορούν να παρέχουν ποιοτικές απαντήσεις με καθυστέρηση κάτω του δευτερολέπτου, διατηρώντας πλήρη ιδιωτικότητα δεδομένων.

### Ερωτήματα Δοκιμής

Χρησιμοποιήστε αυτά τα ερωτήματα για να επικυρώσετε τη ρύθμιση σας:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Κριτήρια Επιτυχίας

- ✅ Όλα τα ερωτήματα λαμβάνουν απαντήσεις σε λιγότερο από 2 δευτερόλεπτα
- ✅ Δεν φεύγουν δεδομένα από τον τοπικό υπολογιστή σας
- ✅ Οι απαντήσεις είναι σχετικές και χρήσιμες
- ✅ Η εφαρμογή συνομιλίας σας λειτουργεί ομαλά

Αυτή η επικύρωση διασφαλίζει ότι η ρύθμιση του Foundry Local είναι έτοιμη για τα προχωρημένα εργαστήρια στις Συνεδρίες 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->