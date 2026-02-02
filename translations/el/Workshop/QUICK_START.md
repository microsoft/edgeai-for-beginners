# Οδηγός Γρήγορης Εκκίνησης Εργαστηρίου

## Προαπαιτούμενα

### 1. Εγκατάσταση του Foundry Local

Ακολουθήστε τον επίσημο οδηγό εγκατάστασης:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Εγκατάσταση Εξαρτήσεων Python

Από τον φάκελο του Εργαστηρίου:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Εκτέλεση Δειγμάτων Εργαστηρίου

### Συνεδρία 01: Βασική Συνομιλία

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Μεταβλητές Περιβάλλοντος:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Συνεδρία 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Μεταβλητές Περιβάλλοντος:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Συνεδρία 02: Αξιολόγηση RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Σημείωση**: Απαιτούνται επιπλέον εξαρτήσεις που εγκαθίστανται μέσω του `requirements.txt`

### Συνεδρία 03: Αξιολόγηση Απόδοσης

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Μεταβλητές Περιβάλλοντος:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Έξοδος**: JSON με μετρήσεις καθυστέρησης, απόδοσης και πρώτου token

### Συνεδρία 04: Σύγκριση Μοντέλων

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Μεταβλητές Περιβάλλοντος:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Συνεδρία 05: Ορχήστρα Πολλαπλών Πρακτόρων

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Μεταβλητές Περιβάλλοντος:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Συνεδρία 06: Δρομολογητής Μοντέλων

```bash
cd Workshop/samples
python -m session06.models_router
```

**Δοκιμές λογικής δρομολόγησης** με πολλαπλές προθέσεις (κώδικας, περίληψη, ταξινόμηση)

### Συνεδρία 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Σύνθετο pipeline πολλών βημάτων** με σχεδιασμό, εκτέλεση και βελτίωση

## Σενάρια

### Εξαγωγή Αναφοράς Αξιολόγησης

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Έξοδος**: Πίνακας Markdown + μετρήσεις JSON

### Έλεγχος CLI Patterns Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Σκοπός**: Εντοπισμός παρωχημένων CLI patterns στην τεκμηρίωση

## Δοκιμές

### Δοκιμές Λειτουργικότητας

```bash
cd Workshop
python -m tests.smoke
```

**Δοκιμές**: Βασική λειτουργικότητα βασικών δειγμάτων

## Επίλυση Προβλημάτων

### Υπηρεσία Δεν Λειτουργεί

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Σφάλματα Εισαγωγής Μονάδων

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Σφάλματα Σύνδεσης

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Μοντέλο Δεν Βρέθηκε

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Αναφορά Μεταβλητών Περιβάλλοντος

### Βασική Διαμόρφωση
| Μεταβλητή | Προεπιλογή | Περιγραφή |
|-----------|------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Διαφέρει | Ψευδώνυμο μοντέλου προς χρήση |
| `FOUNDRY_LOCAL_ENDPOINT` | Αυτόματο | Υπέρβαση του endpoint της υπηρεσίας |
| `SHOW_USAGE` | `0` | Εμφάνιση στατιστικών χρήσης token |
| `RETRY_ON_FAIL` | `1` | Ενεργοποίηση λογικής επαναπροσπάθειας |
| `RETRY_BACKOFF` | `1.0` | Αρχική καθυστέρηση επαναπροσπάθειας (δευτερόλεπτα) |

### Ειδικά για Συνεδρίες
| Μεταβλητή | Προεπιλογή | Περιγραφή |
|-----------|------------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Μοντέλο ενσωμάτωσης |
| `RAG_QUESTION` | Βλέπε δείγμα | Ερώτηση δοκιμής RAG |
| `BENCH_MODELS` | Διαφέρει | Μοντέλα χωρισμένα με κόμμα |
| `BENCH_ROUNDS` | `3` | Επαναλήψεις αξιολόγησης |
| `BENCH_PROMPT` | Βλέπε δείγμα | Ερώτημα αξιολόγησης |
| `BENCH_STREAM` | `0` | Μέτρηση καθυστέρησης πρώτου token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Κύριο μοντέλο πράκτορα |
| `AGENT_MODEL_EDITOR` | Κύριο | Μοντέλο πράκτορα επεξεργασίας |
| `SLM_ALIAS` | `phi-4-mini` | Μικρό μοντέλο γλώσσας |
| `LLM_ALIAS` | `qwen2.5-7b` | Μεγάλο μοντέλο γλώσσας |
| `COMPARE_PROMPT` | Βλέπε δείγμα | Ερώτημα σύγκρισης |

## Προτεινόμενα Μοντέλα

### Ανάπτυξη & Δοκιμές
- **phi-4-mini** - Ισορροπία ποιότητας και ταχύτητας
- **qwen2.5-0.5b** - Πολύ γρήγορο για ταξινόμηση
- **gemma-2-2b** - Καλή ποιότητα, μέτρια ταχύτητα

### Σενάρια Παραγωγής
- **phi-4-mini** - Γενικής χρήσης
- **deepseek-coder-1.3b** - Δημιουργία κώδικα
- **qwen2.5-7b** - Υψηλής ποιότητας απαντήσεις

## Τεκμηρίωση SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Λήψη Βοήθειας

1. Ελέγξτε την κατάσταση της υπηρεσίας: `foundry service status`
2. Δείτε τα αρχεία καταγραφής: Ελέγξτε τα αρχεία καταγραφής της υπηρεσίας Foundry Local
3. Ελέγξτε την τεκμηρίωση SDK: https://github.com/microsoft/Foundry-Local
4. Ανασκόπηση δείγματος κώδικα: Όλα τα δείγματα έχουν λεπτομερή docstrings

## Επόμενα Βήματα

1. Ολοκληρώστε όλες τις συνεδρίες του εργαστηρίου με τη σειρά
2. Πειραματιστείτε με διαφορετικά μοντέλα
3. Τροποποιήστε τα δείγματα για τις δικές σας περιπτώσεις χρήσης

---

**Τελευταία Ενημέρωση**: 2025-01-08  
**Έκδοση Εργαστηρίου**: Τελευταία  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->