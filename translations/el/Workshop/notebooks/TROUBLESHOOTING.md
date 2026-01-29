# Σημειωματάρια Εργαστηρίου - Οδηγός Αντιμετώπισης Προβλημάτων

## Πίνακας Περιεχομένων

- [Συνηθισμένα Προβλήματα και Λύσεις](../../../../Workshop/notebooks)
- [Προβλήματα Ειδικά για τη Συνεδρία 04](../../../../Workshop/notebooks)
- [Προβλήματα Ειδικά για τη Συνεδρία 05](../../../../Workshop/notebooks)
- [Προβλήματα Ειδικά για τη Συνεδρία 06](../../../../Workshop/notebooks)
- [Προβλήματα Σχετικά με το Υλικό](../../../../Workshop/notebooks)
- [Διαγνωστικές Εντολές](../../../../Workshop/notebooks)
- [Λήψη Βοήθειας](../../../../Workshop/notebooks)

---

## Συνηθισμένα Προβλήματα και Λύσεις

### 🔴 CUDA Out of Memory

**Μήνυμα Σφάλματος:**
```
CUDA failure 2: out of memory
```

**Αιτία:** Η GPU δεν έχει αρκετή VRAM για να φορτώσει το μοντέλο.

**Λύσεις:**

#### Επιλογή 1: Χρήση Παραλλαγών CPU (Συνιστάται)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Επιλογή 2: Χρήση Μικρότερων Μοντέλων στη GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Επιλογή 3: Εκκαθάριση Μνήμης GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Επιλογή 4: Αύξηση Μνήμης GPU (αν είναι δυνατόν)
- Κλείστε καρτέλες του προγράμματος περιήγησης, προγράμματα επεξεργασίας βίντεο ή άλλες εφαρμογές GPU
- Μειώστε τα οπτικά εφέ των Windows
- Χρησιμοποιήστε αποκλειστική GPU αν έχετε ενσωματωμένη + αποκλειστική

---

### 🔴 APIConnectionError: Σφάλμα Σύνδεσης

**Μήνυμα Σφάλματος:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Αιτία:** Η υπηρεσία Foundry Local δεν εκτελείται ή δεν είναι προσβάσιμη.

**Λύσεις:**

#### Βήμα 1: Έλεγχος Κατάστασης Υπηρεσίας
```bash
foundry service status
```

#### Βήμα 2: Εκκίνηση Υπηρεσίας αν είναι Σταματημένη
```bash
foundry service start
```

#### Βήμα 3: Επαλήθευση Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Βήμα 4: Φόρτωση Απαιτούμενων Μοντέλων
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Βήμα 5: Επανεκκίνηση Πυρήνα Σημειωματάριου
Μετά την εκκίνηση της υπηρεσίας και τη φόρτωση των μοντέλων, επανεκκινήστε τον πυρήνα του σημειωματάριου και εκτελέστε ξανά όλα τα κελιά.

---

### 🔴 Model Not Found in Catalog

**Μήνυμα Σφάλματος:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Αιτία:** Το μοντέλο δεν έχει ληφθεί ή φορτωθεί στο Foundry Local.

**Λύσεις:**

#### Επιλογή 1: Λήψη και Φόρτωση Μοντέλων
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Επιλογή 2: Χρήση Λειτουργίας Αυτόματης Επιλογής
Ενημερώστε τον CATALOG ώστε να χρησιμοποιεί βασικά ονόματα μοντέλων (χωρίς το επίθεμα `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Το Foundry Local SDK θα επιλέξει αυτόματα την καλύτερη παραλλαγή (CPU, GPU ή NPU) για το υλικό σας.

---

### 🔴 HttpResponseError: 500 - Αποτυχία Φόρτωσης Μοντέλου

**Μήνυμα Σφάλματος:**
```
HttpResponseError: 500 - Failed loading model
```

**Αιτία:** Το αρχείο του μοντέλου είναι κατεστραμμένο ή ασύμβατο με το υλικό.

**Λύσεις:**

#### Επαναλήψη Λήψης Μοντέλου
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Χρήση Διαφορετικής Παραλλαγής
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Μήνυμα Σφάλματος:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Αιτία:** Το πακέτο foundry-local-sdk δεν είναι εγκατεστημένο.

**Λύσεις:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Αργή Πρώτη Αίτηση

**Σύμπτωμα:** Η πρώτη ολοκλήρωση διαρκεί πάνω από 30 δευτερόλεπτα, ενώ οι επόμενες αιτήσεις είναι γρήγορες.

**Αιτία:** Αυτό είναι φυσιολογικό - η υπηρεσία φορτώνει το μοντέλο στη μνήμη κατά την πρώτη αίτηση.

**Λύσεις:**

#### Προ-φόρτωση Μοντέλων
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Διατήρηση Υπηρεσίας Ενεργής
```bash
# Start service manually and leave it running
foundry service start
```

---

## Προβλήματα Ειδικά για τη Συνεδρία 04

### Λανθασμένη Διαμόρφωση Θύρας

**Πρόβλημα:** Το σημειωματάριο συνδέεται σε λάθος θύρα (55769 αντί για 59959 ή 57127)

**Λύση:**

1. Ελέγξτε ποια θύρα χρησιμοποιεί το Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Ενημερώστε το Κελί 10 στο σημειωματάριο:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Επανεκκινήστε τον πυρήνα και εκτελέστε ξανά τα κελιά 6, 8, 10, 12, 16, 20, 22

---

### Λανθασμένη Επιλογή Μοντέλου

**Πρόβλημα:** Το σημειωματάριο εμφανίζει gpt-oss-20b ή qwen2.5-7b αντί για qwen2.5-3b

**Λύση:**

1. Επανεκκινήστε τον πυρήνα του σημειωματάριου (καθαρίζει την παλιά κατάσταση μεταβλητών)
2. Εκτελέστε ξανά το Κελί 10 (Ορισμός Ψευδώνυμων Μοντέλων)
3. Εκτελέστε ξανά το Κελί 12 (Εμφάνιση Διαμόρφωσης)
4. **Επαλήθευση:** Το Κελί 12 πρέπει να δείχνει `LLM Model: qwen2.5-3b`

---

### Αποτυχία Διαγνωστικού Κελιού

**Πρόβλημα:** Το Κελί 16 δείχνει "❌ Foundry Local service not found!"

**Λύση:**

1. Επαληθεύστε ότι η υπηρεσία εκτελείται:
```bash
foundry service status
```

2. Δοκιμάστε το endpoint χειροκίνητα:
```bash
curl http://localhost:59959/v1/models
```

3. Αν το curl λειτουργεί αλλά το σημειωματάριο όχι:
   - Επανεκκινήστε τον πυρήνα του σημειωματάριου
   - Εκτελέστε ξανά τα κελιά με τη σειρά: 6, 8, 10, 12, 14, 16

4. Αν το curl αποτύχει:
   - Εκκινήστε την υπηρεσία: `foundry service start`
   - Φορτώστε μοντέλα: `foundry model run phi-4-mini` και `foundry model run qwen2.5-3b`

---

### Αποτυχία Προ-ελέγχου

**Πρόβλημα:** Το Κελί 20 δείχνει σφάλματα σύνδεσης παρόλο που το διαγνωστικό πέρασε

**Λύση:**

1. Ελέγξτε ότι τα μοντέλα είναι φορτωμένα:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Αν λείπουν μοντέλα:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Εκτελέστε ξανά το Κελί 20 αφού φορτωθούν τα μοντέλα

---

### Αποτυχία Σύγκρισης με Τιμές None

**Πρόβλημα:** Το Κελί 22 ολοκληρώνεται αλλά δείχνει καθυστέρηση ως None

**Λύση:**

1. Ελέγξτε ότι ο προ-έλεγχος πέρασε πρώτα (Κελί 20)
2. Εκτελέστε ξανά το Κελί 22 - τα μοντέλα μπορεί να χρειάζονται προθέρμανση στην πρώτη αίτηση
3. Επαληθεύστε ότι και τα δύο μοντέλα είναι φορτωμένα: `foundry model ls`

---

## Προβλήματα Ειδικά για τη Συνεδρία 05

### Ο Agent Χρησιμοποιεί Λάθος Μοντέλο

**Πρόβλημα:** Ο Agent δεν χρησιμοποιεί το αναμενόμενο μοντέλο

**Λύση:**

Επαληθεύστε τη διαμόρφωση:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Επανεκκινήστε τον πυρήνα αν τα μοντέλα είναι λανθασμένα.

---

### Υπερχείλιση Μνήμης Πλαισίου Συμφραζομένων

**Πρόβλημα:** Οι απαντήσεις του Agent υποβαθμίζονται με την πάροδο του χρόνου

**Λύση:** Έχει ήδη αντιμετωπιστεί αυτόματα - οι agents διατηρούν μόνο τα τελευταία 6 μηνύματα στη μνήμη.

---

## Προβλήματα Ειδικά για τη Συνεδρία 06

### Σύγχυση Μοντέλων CPU vs GPU

**Πρόβλημα:** Εμφανίζονται σφάλματα CUDA κατά τη χρήση της προεπιλεγμένης διαμόρφωσης

**Λύση:** Η προεπιλεγμένη διαμόρφωση χρησιμοποιεί πλέον μοντέλα CPU. Αν δείτε σφάλματα CUDA:

1. Επαληθεύστε ότι χρησιμοποιείτε τον προεπιλεγμένο κατάλογο CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Επανεκκινήστε τον πυρήνα και εκτελέστε ξανά όλα τα κελιά

---

### Η Ανίχνευση Πρόθεσης Δεν Λειτουργεί

**Πρόβλημα:** Οι προτροπές δρομολογούνται σε λάθος μοντέλα

**Λύση:**

Δοκιμάστε την ανίχνευση πρόθεσης:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Ενημερώστε τους ΚΑΝΟΝΕΣ αν χρειάζονται προσαρμογή.

---

## Προβλήματα Σχετικά με το Υλικό

### NVIDIA GPU

**Έλεγχος Κατάστασης GPU:**
```bash
nvidia-smi
```

**Συνηθισμένα Προβλήματα:**
- **Παλαιός οδηγός:** Ενημερώστε τους οδηγούς NVIDIA
- **Ασυμβατότητα έκδοσης CUDA:** Εγκαταστήστε ξανά το Foundry Local
- **Κατακερματισμένη μνήμη GPU:** Επανεκκινήστε το σύστημα

### Qualcomm NPU

**Έλεγχος Κατάστασης NPU:**
```bash
foundry device info
```

**Συνηθισμένα Προβλήματα:**
- **Οι οδηγοί NPU δεν είναι εγκατεστημένοι:** Εγκαταστήστε τους οδηγούς Qualcomm NPU
- **Η παραλλαγή NPU δεν είναι διαθέσιμη:** Χρησιμοποιήστε την παραλλαγή CPU
- **Πολύ παλιά έκδοση Windows:** Ενημερώστε στην τελευταία έκδοση των Windows 11

### Συστήματα Μόνο με CPU

**Συνιστώμενα Μοντέλα:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Συμβουλές Απόδοσης:**
- Χρησιμοποιήστε τα μικρότερα μοντέλα
- Μειώστε το max_tokens
- Δείξτε υπομονή για την πρώτη αίτηση

---

## Διαγνωστικές Εντολές

### Έλεγχος Όλων
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Σε Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Λήψη Βοήθειας

### 1. Έλεγχος Αρχείων Καταγραφής
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Θέματα στο GitHub
- Αναζήτηση υπαρχόντων θεμάτων: https://github.com/microsoft/Foundry-Local/issues
- Δημιουργία νέου θέματος με:
  - Μήνυμα σφάλματος (πλήρες κείμενο)
  - Έξοδο του `foundry service status`
  - Έξοδο του `foundry --version`
  - Πληροφορίες GPU/NPU (nvidia-smi, κ.λπ.)
  - Βήματα αναπαραγωγής

### 3. Τεκμηρίωση
- **Κύριο Αποθετήριο:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Αναφορά CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Αντιμετώπιση Προβλημάτων:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Λίστα Ελέγχου Γρήγορων Επιδιορθώσεων

Όταν κάτι πάει στραβά, δοκιμάστε τα εξής με τη σειρά:

- [ ] Ελέγξτε ότι η υπηρεσία εκτελείται: `foundry service status`
- [ ] Επανεκκινήστε την υπηρεσία: `foundry service stop && foundry service start`
- [ ] Επαληθεύστε ότι το μοντέλο υπάρχει: `foundry model ls | grep phi-4-mini`
- [ ] Φορτώστε τα απαιτούμενα μοντέλα: `foundry model run phi-4-mini`
- [ ] Ελέγξτε τη μνήμη GPU: `nvidia-smi` (αν χρησιμοποιείτε NVIDIA)
- [ ] Δοκιμάστε την παραλλαγή CPU: Χρησιμοποιήστε `phi-4-mini-cpu` αντί για `phi-4-mini`
- [ ] Επανεκκινήστε τον πυρήνα του σημειωματάριου
- [ ] Καθαρίστε τις εξόδους του σημειωματάριου και εκτελέστε ξανά όλα τα κελιά
- [ ] Επανεγκαταστήστε το SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Επανεκκινήστε το σύστημα (τελευταία λύση)

---

## Συμβουλές Πρόληψης

### Καλές Πρακτικές

1. **Πάντα ελέγξτε πρώτα την υπηρεσία:**
   ```bash
   foundry service status
   ```

2. **Χρησιμοποιήστε παραλλαγές CPU από προεπιλογή:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Προ-φορτώστε μοντέλα πριν εκτελέσετε σημειωματάρια:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Διατηρήστε την υπηρεσία ενεργή:**
   - Μην σταματάτε/ξεκινάτε την υπηρεσία χωρίς λόγο
   - Αφήστε την να εκτελείται στο παρασκήνιο μεταξύ των συνεδριών

5. **Παρακολουθήστε τους πόρους:**
   - Ελέγξτε τη μνήμη GPU πριν την εκτέλεση
   - Κλείστε περιττές εφαρμογές GPU
   - Χρησιμοποιήστε Task Manager / nvidia-smi

6. **Ενημερώστε τακτικά:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Τελευταία Ενημέρωση:** 8 Οκτωβρίου 2025

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.