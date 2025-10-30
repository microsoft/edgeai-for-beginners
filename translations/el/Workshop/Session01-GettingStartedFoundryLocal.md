<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:52:59+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "el"
}
-->
# Συνεδρία 1: Ξεκινώντας με το Foundry Local

## Περίληψη

Ξεκινήστε το ταξίδι σας με το Foundry Local εγκαθιστώντας και ρυθμίζοντάς το στα Windows 11. Μάθετε πώς να ρυθμίζετε το CLI, να ενεργοποιείτε την επιτάχυνση υλικού και να αποθηκεύετε μοντέλα για γρήγορη τοπική επεξεργασία. Αυτή η πρακτική συνεδρία σας καθοδηγεί στη λειτουργία μοντέλων όπως τα Phi, Qwen, DeepSeek και GPT-OSS-20B χρησιμοποιώντας αναπαραγώγιμες εντολές CLI.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτής της συνεδρίας, θα μπορείτε:

- **Εγκατάσταση και Ρύθμιση**: Να εγκαταστήσετε το Foundry Local στα Windows 11 με βέλτιστες ρυθμίσεις απόδοσης
- **Κατανόηση Λειτουργιών CLI**: Να χρησιμοποιείτε το Foundry Local CLI για διαχείριση και ανάπτυξη μοντέλων
- **Ενεργοποίηση Επιτάχυνσης Υλικού**: Να ρυθμίζετε την επιτάχυνση GPU με ONNXRuntime ή WebGPU
- **Ανάπτυξη Πολλαπλών Μοντέλων**: Να εκτελείτε τα μοντέλα phi-4, GPT-OSS-20B, Qwen και DeepSeek τοπικά
- **Δημιουργία της Πρώτης σας Εφαρμογής**: Να προσαρμόζετε υπάρχοντα δείγματα για χρήση του Foundry Local Python SDK

# Δοκιμή του μοντέλου (μη διαδραστική μονή προτροπή)
foundry model run phi-4-mini --prompt "Γεια, συστήσου"

- Windows 11 (22H2 ή νεότερη έκδοση)
# Λίστα διαθέσιμων μοντέλων καταλόγου (τα φορτωμένα μοντέλα εμφανίζονται μετά την εκτέλεση)
foundry model list
## ΣΗΜΕΙΩΣΗ: Προς το παρόν δεν υπάρχει ειδική σημαία `--running`. Για να δείτε ποια είναι φορτωμένα, ξεκινήστε μια συνομιλία ή ελέγξτε τα αρχεία καταγραφής υπηρεσίας.
- Εγκατεστημένο Python 3.10+
- Visual Studio Code με επέκταση Python
- Δικαιώματα διαχειριστή για εγκατάσταση

### (Προαιρετικά) Μεταβλητές Περιβάλλοντος

Δημιουργήστε ένα αρχείο `.env` (ή ορίστε το στο shell) για να κάνετε τα σενάρια φορητά:
# Σύγκριση απαντήσεων (μη διαδραστική)
foundry model run gpt-oss-20b --prompt "Εξήγησε την τεχνητή νοημοσύνη αιχμής με απλούς όρους"
| Μεταβλητή | Σκοπός | Παράδειγμα |
|-----------|--------|------------|
| `FOUNDRY_LOCAL_ALIAS` | Προτιμώμενο ψευδώνυμο μοντέλου (ο κατάλογος επιλέγει αυτόματα την καλύτερη παραλλαγή) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Υπέρβαση του τελικού σημείου (διαφορετικά αυτόματα από τον διαχειριστή) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Ενεργοποίηση επίδειξης ροής | `true` |

> Αν `FOUNDRY_LOCAL_ENDPOINT=auto` (ή δεν έχει οριστεί), το παράγουμε από τον διαχειριστή SDK.

## Ροή Επίδειξης (30 λεπτά)

### 1. Εγκατάσταση του Foundry Local και Επαλήθευση Ρύθμισης CLI (10 λεπτά)

# Λίστα αποθηκευμένων μοντέλων
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Προεπισκόπηση / Αν Υποστηρίζεται)**

Αν παρέχεται ένα εγγενές πακέτο macOS (ελέγξτε την επίσημη τεκμηρίωση για τις τελευταίες ενημερώσεις):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Αν δεν είναι ακόμη διαθέσιμα εγγενή δυαδικά αρχεία macOS, μπορείτε να:
1. Χρησιμοποιήσετε ένα VM Windows 11 ARM/Intel (Parallels / UTM) και να ακολουθήσετε τα βήματα για Windows.
2. Εκτελέσετε μοντέλα μέσω container (αν έχει δημοσιευθεί εικόνα container) και να ορίσετε το `FOUNDRY_LOCAL_ENDPOINT` στη διαθέσιμη θύρα.

**Δημιουργία Εικονικού Περιβάλλοντος Python (Δια-Πλατφόρμα)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Αναβάθμιση pip και εγκατάσταση βασικών εξαρτήσεων:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Βήμα 1.2: Επαλήθευση Εγκατάστασης

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Βήμα 1.3: Ρύθμιση Περιβάλλοντος

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Εκκίνηση SDK (Συνιστάται)

Αντί να ξεκινήσετε χειροκίνητα την υπηρεσία και να εκτελέσετε μοντέλα, το **Foundry Local Python SDK** μπορεί να εκκινήσει τα πάντα:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Αν προτιμάτε την άμεση διαχείριση, μπορείτε να χρησιμοποιήσετε το CLI + OpenAI client όπως φαίνεται αργότερα.

### 2. Εκτέλεση Μοντέλων Τοπικά μέσω CLI (10 λεπτά)

#### Βήμα 3.1: Ανάπτυξη Μοντέλου Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Βήμα 3.2: Ανάπτυξη GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Βήμα 3.3: Φόρτωση Επιπλέον Μοντέλων

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Έργο Εκκίνησης: Προσαρμογή του 01-run-phi για το Foundry Local (5 λεπτά)

#### Βήμα 4.1: Δημιουργία Βασικής Εφαρμογής Συνομιλίας

Δημιουργήστε το `samples/01-foundry-quickstart/chat_quickstart.py` (ενημερωμένο για χρήση του διαχειριστή αν είναι διαθέσιμο):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Βήμα 4.2: Δοκιμή της Εφαρμογής

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Βασικές Έννοιες που Καλύπτονται

### 1. Αρχιτεκτονική του Foundry Local

- **Μηχανή Τοπικής Επεξεργασίας**: Εκτελεί μοντέλα εξ ολοκλήρου στη συσκευή σας
- **Συμβατότητα με το OpenAI SDK**: Ομαλή ενσωμάτωση με υπάρχοντα κώδικα OpenAI
- **Διαχείριση Μοντέλων**: Λήψη, αποθήκευση και εκτέλεση πολλαπλών μοντέλων αποτελεσματικά
- **Βελτιστοποίηση Υλικού**: Χρήση επιτάχυνσης GPU, NPU και CPU

### 2. Αναφορά Εντολών CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Ενσωμάτωση Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Επίλυση Συνηθισμένων Προβλημάτων

### Πρόβλημα 1: "Η εντολή Foundry δεν βρέθηκε"

**Λύση:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Πρόβλημα 2: "Αποτυχία φόρτωσης μοντέλου"

**Λύση:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Πρόβλημα 3: "Η σύνδεση απορρίφθηκε στο localhost:5273"

**Λύση:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Συμβουλές Βελτιστοποίησης Απόδοσης

### 1. Στρατηγική Επιλογής Μοντέλου

- **Phi-4-mini**: Καλύτερο για γενικές εργασίες, χαμηλή χρήση μνήμης
- **Qwen2.5-0.5b**: Ταχύτερη επεξεργασία, ελάχιστοι πόροι
- **GPT-OSS-20B**: Υψηλότερη ποιότητα, απαιτεί περισσότερους πόρους
- **DeepSeek-Coder**: Βελτιστοποιημένο για εργασίες προγραμματισμού

### 2. Βελτιστοποίηση Υλικού

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Παρακολούθηση Απόδοσης

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Προαιρετικές Βελτιώσεις

| Βελτίωση | Τι | Πώς |
|----------|----|-----|
| Κοινές Βοηθητικές Λειτουργίες | Αφαίρεση διπλότυπου κώδικα client/bootstrap | Χρήση `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Ορατότητα Χρήσης Token | Εισαγωγή σκέψης για κόστος/αποδοτικότητα νωρίς | Ορισμός `SHOW_USAGE=1` για εκτύπωση προτροπής/ολοκλήρωσης/συνολικών tokens |
| Σταθερές Συγκρίσεις | Σταθερή αξιολόγηση και έλεγχοι παλινδρόμησης | Χρήση `temperature=0`, `top_p=1`, σταθερό κείμενο προτροπής |
| Καθυστέρηση Πρώτου Token | Μετρική αντιληπτής απόκρισης | Προσαρμογή σεναρίου αξιολόγησης με ροή (`BENCH_STREAM=1`) |
| Επανάληψη σε Παροδικά Σφάλματα | Ανθεκτικές επιδείξεις σε κρύα εκκίνηση | `RETRY_ON_FAIL=1` (προεπιλογή) & προσαρμογή `RETRY_BACKOFF` |
| Δοκιμή Λειτουργίας | Γρήγορος έλεγχος βασικών λειτουργιών | Εκτέλεση `python Workshop/tests/smoke.py` πριν από ένα εργαστήριο |
| Προφίλ Ψευδώνυμων Μοντέλων | Γρήγορη αλλαγή συνόλου μοντέλων μεταξύ μηχανών | Διατήρηση `.env` με `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Αποδοτικότητα Αποθήκευσης | Αποφυγή επαναλαμβανόμενων προθερμάνσεων σε πολλαπλές εκτελέσεις δειγμάτων | Βοηθητικά εργαλεία διαχείρισης αποθήκευσης; επαναχρησιμοποίηση σε σενάρια/σημειωματάρια |
| Προθέρμανση Πρώτης Εκτέλεσης | Μείωση αιχμών καθυστέρησης p95 | Εκτέλεση μικρής προτροπής μετά τη δημιουργία του `FoundryLocalManager` |

Παράδειγμα σταθερής αρχικής βάσης (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Θα πρέπει να δείτε παρόμοια αποτελέσματα και ταυτόσημο αριθμό tokens στη δεύτερη εκτέλεση, επιβεβαιώνοντας τη σταθερότητα.

## Επόμενα Βήματα

Μετά την ολοκλήρωση αυτής της συνεδρίας:

1. **Εξερευνήστε τη Συνεδρία 2**: Δημιουργήστε λύσεις AI με το Azure AI Foundry RAG
2. **Δοκιμάστε Διαφορετικά Μοντέλα**: Πειραματιστείτε με τα Qwen, DeepSeek και άλλες οικογένειες μοντέλων
3. **Βελτιστοποιήστε την Απόδοση**: Προσαρμόστε τις ρυθμίσεις για το συγκεκριμένο υλικό σας
4. **Δημιουργήστε Προσαρμοσμένες Εφαρμογές**: Χρησιμοποιήστε το Foundry Local SDK στα δικά σας έργα

## Πρόσθετοι Πόροι

### Τεκμηρίωση
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Δείγματα Κώδικα
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Κοινότητα
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Διάρκεια Συνεδρίας**: 30 λεπτά πρακτική + 15 λεπτά ερωτήσεις & απαντήσεις  
**Επίπεδο Δυσκολίας**: Αρχάριος  
**Προαπαιτούμενα**: Windows 11, Python 3.10+, πρόσβαση διαχειριστή  

## Δείγμα Σεναρίου & Χαρτογράφηση Εργαστηρίου

| Σενάριο Εργαστηρίου / Σημειωματάριο | Σενάριο | Στόχος | Παράδειγμα Εισόδου | Απαιτούμενο Σύνολο Δεδομένων |
|------------------------------------|---------|--------|--------------------|----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Εσωτερική ομάδα IT που αξιολογεί την επεξεργασία στη συσκευή για πύλη αξιολόγησης απορρήτου | Απόδειξη ότι το τοπικό SLM ανταποκρίνεται με καθυστέρηση κάτω του δευτερολέπτου σε τυπικές προτροπές | "Αναφέρετε δύο πλεονεκτήματα της τοπικής επεξεργασίας." | Καμία (μόνο μία προτροπή) |
| Κώδικας προσαρμογής γρήγορης εκκίνησης | Προγραμματιστής που μεταφέρει έναν υπάρχοντα κώδικα OpenAI στο Foundry Local | Επίδειξη συμβατότητας | "Αναφέρετε δύο πλεονεκτήματα της τοπικής επεξεργασίας." | Μόνο ενσωματωμένη προτροπή |

### Αφήγηση Σεναρίου
Η ομάδα ασφάλειας και συμμόρφωσης πρέπει να επαληθεύσει αν τα ευαίσθητα δεδομένα πρωτοτύπου μπορούν να επεξεργαστούν τοπικά. Εκτελούν το σενάριο εκκίνησης με διάφορες προτροπές (απόρρητο, καθυστέρηση, κόστος) χρησιμοποιώντας μια σταθερή λειτουργία temperature=0 για να καταγράψουν βασικά αποτελέσματα για μελλοντική σύγκριση (Συνεδρία 3 αξιολόγηση και Συνεδρία 4 σύγκριση SLM vs LLM).

### Ελάχιστο Σύνολο Προτροπών JSON (προαιρετικό)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Χρησιμοποιήστε αυτήν τη λίστα για να δημιουργήσετε έναν αναπαραγώγιμο βρόχο αξιολόγησης ή για να προετοιμάσετε ένα μελλοντικό εργαλείο ελέγχου παλινδρόμησης.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.