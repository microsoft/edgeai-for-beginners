# Εγχειρίδιο Γρήγορης Εκκίνησης - Workshop Notebooks

## Πίνακας Περιεχομένων

- [Προαπαιτούμενα](../../../../Workshop/notebooks)
- [Αρχική Ρύθμιση](../../../../Workshop/notebooks)
- [Συνεδρία 04: Σύγκριση Μοντέλων](../../../../Workshop/notebooks)
- [Συνεδρία 05: Ορχηστρωτής Πολλαπλών Πρακτόρων](../../../../Workshop/notebooks)
- [Συνεδρία 06: Δρομολόγηση Μοντέλων με Βάση την Πρόθεση](../../../../Workshop/notebooks)
- [Μεταβλητές Περιβάλλοντος](../../../../Workshop/notebooks)
- [Συχνές Εντολές](../../../../Workshop/notebooks)

---

## Προαπαιτούμενα

### 1. Εγκατάσταση Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Επαλήθευση Εγκατάστασης:**
```bash
foundry --version
```

### 2. Εγκατάσταση Εξαρτήσεων Python

```bash
cd Workshop
pip install -r requirements.txt
```

Ή εγκατάσταση ξεχωριστά:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Αρχική Ρύθμιση

### Εκκίνηση Υπηρεσίας Foundry Local

**Απαραίτητο πριν την εκτέλεση οποιουδήποτε notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Αναμενόμενο αποτέλεσμα:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Λήψη και Φόρτωση Μοντέλων

Τα notebooks χρησιμοποιούν αυτά τα μοντέλα από προεπιλογή:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Επαλήθευση Ρύθμισης

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Συνεδρία 04: Σύγκριση Μοντέλων

### Σκοπός
Σύγκριση απόδοσης μεταξύ Μικρών Γλωσσικών Μοντέλων (SLM) και Μεγάλων Γλωσσικών Μοντέλων (LLM).

### Γρήγορη Ρύθμιση

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Εκτέλεση του Notebook

1. **Άνοιγμα** του `session04_model_compare.ipynb` στο VS Code ή Jupyter
2. **Επανεκκίνηση πυρήνα** (Kernel → Restart Kernel)
3. **Εκτέλεση όλων των κελιών** με τη σειρά

### Βασική Ρύθμιση

**Προεπιλεγμένα Μοντέλα:**
- **SLM:** `phi-4-mini` (~4GB RAM, γρηγορότερο)
- **LLM:** `qwen2.5-3b` (~3GB RAM, βελτιστοποιημένο για μνήμη)

**Μεταβλητές Περιβάλλοντος (προαιρετικά):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Αναμενόμενο Αποτέλεσμα

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Προσαρμογή

**Χρήση διαφορετικών μοντέλων:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Προσαρμοσμένο prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Λίστα Ελέγχου Επικύρωσης

- [ ] Το Κελί 12 εμφανίζει σωστά μοντέλα (phi-4-mini, qwen2.5-3b)
- [ ] Το Κελί 12 εμφανίζει σωστό endpoint (port 59959)
- [ ] Το Κελί 16 διαγνωστικό περνάει (✅ Η υπηρεσία λειτουργεί)
- [ ] Το Κελί 20 προ-έλεγχος περνάει (και τα δύο μοντέλα εντάξει)
- [ ] Το Κελί 22 σύγκριση ολοκληρώνεται με τιμές καθυστέρησης
- [ ] Το Κελί 24 επικύρωση δείχνει 🎉 ΟΛΟΙ ΟΙ ΕΛΕΓΧΟΙ ΠΕΡΑΣΑΝ!

### Εκτίμηση Χρόνου
- **Πρώτη εκτέλεση:** 5-10 λεπτά (συμπεριλαμβανομένων των λήψεων μοντέλων)
- **Επόμενες εκτελέσεις:** 1-2 λεπτά

---

## Συνεδρία 05: Ορχηστρωτής Πολλαπλών Πρακτόρων

### Σκοπός
Επίδειξη συνεργασίας πολλαπλών πρακτόρων χρησιμοποιώντας το Foundry Local SDK - οι πράκτορες συνεργάζονται για να παράγουν βελτιωμένα αποτελέσματα.

### Γρήγορη Ρύθμιση

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Εκτέλεση του Notebook

1. **Άνοιγμα** του `session05_agents_orchestrator.ipynb`
2. **Επανεκκίνηση πυρήνα**
3. **Εκτέλεση όλων των κελιών** με τη σειρά

### Βασική Ρύθμιση

**Προεπιλεγμένη Ρύθμιση (Ίδιο Μοντέλο για Όλους τους Πράκτορες):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Προχωρημένη Ρύθμιση (Διαφορετικά Μοντέλα):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Αρχιτεκτονική

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Αναμενόμενο Αποτέλεσμα

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Επεκτάσεις

**Προσθήκη περισσότερων πρακτόρων:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Δοκιμή σε παρτίδες:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Εκτίμηση Χρόνου
- **Πρώτη εκτέλεση:** 3-5 λεπτά
- **Επόμενες εκτελέσεις:** 1-2 λεπτά ανά ερώτηση

---

## Συνεδρία 06: Δρομολόγηση Μοντέλων με Βάση την Πρόθεση

### Σκοπός
Έξυπνη δρομολόγηση prompts σε εξειδικευμένα μοντέλα με βάση την ανιχνευθείσα πρόθεση.

### Γρήγορη Ρύθμιση

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Σημείωση:** Η Συνεδρία 06 χρησιμοποιεί προεπιλεγμένα μοντέλα CPU για μέγιστη συμβατότητα.

### Εκτέλεση του Notebook

1. **Άνοιγμα** του `session06_models_router.ipynb`
2. **Επανεκκίνηση πυρήνα**
3. **Εκτέλεση όλων των κελιών** με τη σειρά

### Βασική Ρύθμιση

**Προεπιλεγμένος Κατάλογος (Μοντέλα CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Εναλλακτική (Μοντέλα GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Ανίχνευση Πρόθεσης

Ο δρομολογητής χρησιμοποιεί μοτίβα regex για την ανίχνευση πρόθεσης:

| Πρόθεση | Παραδείγματα Μοτίβων | Δρομολογείται Σε |
|--------|---------------------|------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Οτιδήποτε άλλο | phi-4-mini-cpu |

### Αναμενόμενο Αποτέλεσμα

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Προσαρμογή

**Προσθήκη προσαρμοσμένης πρόθεσης:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Ενεργοποίηση παρακολούθησης tokens:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Εναλλαγή σε Μοντέλα GPU

Εάν έχετε 8GB+ VRAM:

1. Στο **Κελί #6**, σχολιάστε τον κατάλογο CPU
2. Ξεσχολιάστε τον κατάλογο GPU
3. Φορτώστε μοντέλα GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Επανεκκινήστε τον πυρήνα και επανεκτελέστε το notebook

### Εκτίμηση Χρόνου
- **Πρώτη εκτέλεση:** 5-10 λεπτά (φόρτωση μοντέλων)
- **Επόμενες εκτελέσεις:** 30-60 δευτερόλεπτα ανά δοκιμή

---

## Μεταβλητές Περιβάλλοντος

### Γενική Ρύθμιση

Ορίστε πριν την εκκίνηση του Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Ρύθμιση Μέσα στο Notebook

Ορίστε στην αρχή οποιουδήποτε notebook:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Συχνές Εντολές

### Διαχείριση Υπηρεσίας

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Διαχείριση Μοντέλων

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Δοκιμή Endpoints

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Διαγνωστικές Εντολές

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Καλές Πρακτικές

### Πριν την Εκκίνηση Οποιουδήποτε Notebook

1. **Ελέγξτε ότι η υπηρεσία λειτουργεί:**
   ```bash
   foundry service status
   ```

2. **Επαληθεύστε ότι τα μοντέλα έχουν φορτωθεί:**
   ```bash
   foundry model ls
   ```

3. **Επανεκκινήστε τον πυρήνα του notebook** αν το εκτελείτε ξανά

4. **Καθαρίστε όλα τα αποτελέσματα** για καθαρή εκτέλεση

### Διαχείριση Πόρων

1. **Χρησιμοποιήστε μοντέλα CPU από προεπιλογή** για συμβατότητα
2. **Μεταβείτε σε μοντέλα GPU** μόνο αν έχετε 8GB+ VRAM
3. **Κλείστε άλλες εφαρμογές GPU** πριν την εκτέλεση
4. **Διατηρήστε την υπηρεσία ενεργή** μεταξύ των συνεδριών notebook
5. **Παρακολουθήστε τη χρήση πόρων** με Task Manager / nvidia-smi

### Αντιμετώπιση Προβλημάτων

1. **Πάντα ελέγξτε την υπηρεσία πρώτα** πριν κάνετε debugging στον κώδικα
2. **Επανεκκινήστε τον πυρήνα** αν δείτε παλιές ρυθμίσεις
3. **Επανεκτελέστε τα διαγνωστικά κελιά** μετά από οποιαδήποτε αλλαγή
4. **Ελέγξτε τα ονόματα μοντέλων** να ταιριάζουν με αυτά που έχουν φορτωθεί
5. **Επαληθεύστε ότι η θύρα endpoint** ταιριάζει με την κατάσταση της υπηρεσίας

---

## Γρήγορη Αναφορά: Ψευδώνυμα Μοντέλων

### Συχνά Μοντέλα

| Ψευδώνυμο | Μέγεθος | Καλύτερο Για | RAM/VRAM | Παραλλαγές |
|-----------|---------|--------------|----------|------------|
| `phi-4-mini` | ~4B | Γενική συνομιλία, περίληψη | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Δημιουργία κώδικα, αναδιάρθρωση | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Γενικές εργασίες, αποδοτικό | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Γρήγορο, χαμηλοί πόροι | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Κατηγοριοποίηση, ελάχιστοι πόροι | 1-2GB | `-cpu`, `-cuda-gpu` |

### Ονοματολογία Παραλλαγών

- **Βασικό όνομα** (π.χ., `phi-4-mini`): Επιλέγει αυτόματα την καλύτερη παραλλαγή για το υλικό σας
- **`-cpu`**: Βελτιστοποιημένο για CPU, λειτουργεί παντού
- **`-cuda-gpu`**: Βελτιστοποιημένο για NVIDIA GPU, απαιτεί 8GB+ VRAM
- **`-npu`**: Βελτιστοποιημένο για Qualcomm NPU, απαιτεί drivers NPU

**Σύσταση:** Χρησιμοποιήστε βασικά ονόματα (χωρίς κατάληξη) και αφήστε το Foundry Local να επιλέξει αυτόματα την καλύτερη παραλλαγή.

---

## Δείκτες Επιτυχίας

Είστε έτοιμοι όταν βλέπετε:

✅ Το `foundry service status` δείχνει "running"
✅ Το `foundry model ls` δείχνει τα απαιτούμενα μοντέλα
✅ Η υπηρεσία είναι προσβάσιμη στο σωστό endpoint
✅ Ο έλεγχος υγείας επιστρέφει 200 OK
✅ Τα διαγνωστικά κελιά του notebook περνούν
✅ Δεν υπάρχουν σφάλματα σύνδεσης στα αποτελέσματα

---

## Λήψη Βοήθειας

### Τεκμηρίωση
- **Κύριο Αποθετήριο**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Αναφορά CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Αντιμετώπιση Προβλημάτων**: Δείτε το `troubleshooting.md` σε αυτόν τον φάκελο

### Ζητήματα GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Τελευταία Ενημέρωση:** 8 Οκτωβρίου 2025
**Έκδοση:** Workshop Notebooks 2.0

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.