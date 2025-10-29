<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T21:52:00+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "el"
}
-->
# Οδηγός Ρύθμισης Περιβάλλοντος

## Επισκόπηση

Τα δείγματα του Workshop χρησιμοποιούν μεταβλητές περιβάλλοντος για τη ρύθμιση, συγκεντρωμένες στο αρχείο `.env` στη ρίζα του αποθετηρίου. Αυτό επιτρέπει εύκολη προσαρμογή χωρίς τροποποίηση του κώδικα.

## Γρήγορη Εκκίνηση

### 1. Επαλήθευση Προαπαιτούμενων

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Ρύθμιση Περιβάλλοντος

Το αρχείο `.env` είναι ήδη ρυθμισμένο με λογικές προεπιλογές. Οι περισσότεροι χρήστες δεν χρειάζεται να αλλάξουν τίποτα.

**Προαιρετικό**: Ελέγξτε και προσαρμόστε τις ρυθμίσεις:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Εφαρμογή Ρύθμισης

**Για Python Scripts:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Για Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Αναφορά Μεταβλητών Περιβάλλοντος

### Βασική Ρύθμιση

| Μεταβλητή | Προεπιλογή | Περιγραφή |
|-----------|------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Προεπιλεγμένο μοντέλο για δείγματα |
| `FOUNDRY_LOCAL_ENDPOINT` | (κενό) | Υπέρβαση του endpoint της υπηρεσίας |
| `PYTHONPATH` | Διαδρομές Workshop | Διαδρομή αναζήτησης Python modules |

**Πότε να ορίσετε το FOUNDRY_LOCAL_ENDPOINT:**
- Απομακρυσμένη περίπτωση Foundry Local
- Προσαρμοσμένη ρύθμιση θύρας
- Διαχωρισμός ανάπτυξης/παραγωγής

**Παράδειγμα:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Μεταβλητές Ειδικές για Συνεδρίες

#### Συνεδρία 02: RAG Pipeline
| Μεταβλητή | Προεπιλογή | Σκοπός |
|-----------|------------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Μοντέλο ενσωμάτωσης |
| `RAG_QUESTION` | Προρυθμισμένο | Ερώτηση δοκιμής |

#### Συνεδρία 03: Benchmarking
| Μεταβλητή | Προεπιλογή | Σκοπός |
|-----------|------------|--------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Μοντέλα για benchmarking |
| `BENCH_ROUNDS` | `3` | Επαναλήψεις ανά μοντέλο |
| `BENCH_PROMPT` | Προρυθμισμένο | Ερώτημα δοκιμής |
| `BENCH_STREAM` | `0` | Μέτρηση καθυστέρησης πρώτου token |

#### Συνεδρία 04: Σύγκριση Μοντέλων
| Μεταβλητή | Προεπιλογή | Σκοπός |
|-----------|------------|--------|
| `SLM_ALIAS` | `phi-4-mini` | Μικρό γλωσσικό μοντέλο |
| `LLM_ALIAS` | `qwen2.5-7b` | Μεγάλο γλωσσικό μοντέλο |
| `COMPARE_PROMPT` | Προρυθμισμένο | Ερώτημα σύγκρισης |
| `COMPARE_RETRIES` | `2` | Προσπάθειες επανάληψης |

#### Συνεδρία 05: Ορχήστρα Πολλαπλών Πρακτόρων
| Μεταβλητή | Προεπιλογή | Σκοπός |
|-----------|------------|--------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Μοντέλο ερευνητή πράκτορα |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Μοντέλο πράκτορα επεξεργαστή |
| `AGENT_QUESTION` | Προρυθμισμένο | Ερώτηση δοκιμής |

### Ρύθμιση Αξιοπιστίας

| Μεταβλητή | Προεπιλογή | Σκοπός |
|-----------|------------|--------|
| `SHOW_USAGE` | `1` | Εκτύπωση χρήσης token |
| `RETRY_ON_FAIL` | `1` | Ενεργοποίηση λογικής επανάληψης |
| `RETRY_BACKOFF` | `1.0` | Καθυστέρηση επανάληψης (δευτερόλεπτα) |

## Συνήθεις Ρυθμίσεις

### Ρύθμιση Ανάπτυξης (Γρήγορη Επανάληψη)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Ρύθμιση Παραγωγής (Εστίαση στην Ποιότητα)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Ρύθμιση Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Εξειδίκευση Πολλαπλών Πρακτόρων
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Απομακρυσμένη Ανάπτυξη
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Συνιστώμενα Μοντέλα

### Ανά Περίπτωση Χρήσης

**Γενική Χρήση:**
- `phi-4-mini` - Ισορροπία ποιότητας και ταχύτητας

**Γρήγορες Απαντήσεις:**
- `qwen2.5-0.5b` - Πολύ γρήγορο, καλό για ταξινόμηση
- `phi-4-mini` - Γρήγορο με καλή ποιότητα

**Υψηλή Ποιότητα:**
- `qwen2.5-7b` - Καλύτερη ποιότητα, υψηλότερη χρήση πόρων
- `phi-4-mini` - Καλή ποιότητα, χαμηλότεροι πόροι

**Δημιουργία Κώδικα:**
- `deepseek-coder-1.3b` - Εξειδικευμένο για κώδικα
- `phi-4-mini` - Γενική χρήση για κώδικα

### Ανά Διαθεσιμότητα Πόρων

**Χαμηλοί Πόροι (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Μεσαίοι Πόροι (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Υψηλοί Πόροι (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Προχωρημένη Ρύθμιση

### Προσαρμοσμένα Endpoints

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Θερμοκρασία & Δειγματοληψία (Υπέρβαση στον Κώδικα)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Υβριδική Ρύθμιση Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Αντιμετώπιση Προβλημάτων

### Μεταβλητές Περιβάλλοντος Δεν Φορτώθηκαν

**Συμπτώματα:**
- Τα scripts χρησιμοποιούν λάθος μοντέλα
- Σφάλματα σύνδεσης
- Οι μεταβλητές δεν αναγνωρίζονται

**Λύσεις:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Προβλήματα Σύνδεσης Υπηρεσίας

**Συμπτώματα:**
- Σφάλματα "Connection refused"
- "Η υπηρεσία δεν είναι διαθέσιμη"
- Σφάλματα χρονικού ορίου

**Λύσεις:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Μοντέλο Δεν Βρέθηκε

**Συμπτώματα:**
- Σφάλματα "Model not found"
- "Alias δεν αναγνωρίζεται"

**Λύσεις:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Σφάλματα Εισαγωγής

**Συμπτώματα:**
- Σφάλματα "Module not found"

**Λύσεις:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Δοκιμή Ρύθμισης

### Επαλήθευση Φόρτωσης Περιβάλλοντος

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Δοκιμή Σύνδεσης Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Βέλτιστες Πρακτικές Ασφαλείας

### 1. Μην Κάνετε Commit Μυστικά

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Χρησιμοποιήστε Ξεχωριστά Αρχεία .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Περιστρέψτε Κλειδιά API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Χρησιμοποιήστε Ρύθμιση Ειδική για Περιβάλλον

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Τεκμηρίωση SDK

- **Κύριο Αποθετήριο**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Τεκμηρίωση API**: Ελέγξτε το αποθετήριο SDK για τις τελευταίες ενημερώσεις

## Πρόσθετοι Πόροι

- `QUICK_START.md` - Οδηγός γρήγορης εκκίνησης
- `SDK_MIGRATION_NOTES.md` - Λεπτομέρειες ενημέρωσης SDK
- `Workshop/samples/*/README.md` - Οδηγοί ειδικοί για δείγματα

---

**Τελευταία Ενημέρωση**: 2025-01-08  
**Έκδοση**: 2.0  
**SDK**: Foundry Local Python SDK (τελευταία έκδοση)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.