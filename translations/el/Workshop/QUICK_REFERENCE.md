<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T23:06:48+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "el"
}
-->
# Δείγματα Εργαστηρίου - Γρήγορος Οδηγός Αναφοράς

**Τελευταία Ενημέρωση**: 8 Οκτωβρίου 2025

---

## 🚀 Γρήγορη Εκκίνηση

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Επισκόπηση Δειγμάτων

| Συνεδρία | Δείγμα | Σκοπός | Χρόνος |
|----------|--------|--------|--------|
| 01 | `chat_bootstrap.py` | Βασική συνομιλία + ροή | ~30s |
| 02 | `rag_pipeline.py` | RAG με ενσωματώσεις | ~45s |
| 02 | `rag_eval_ragas.py` | Αξιολόγηση RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Αξιολόγηση μοντέλων | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Σύστημα πολλαπλών πρακτόρων | ~60s |
| 06 | `models_router.py` | Δρομολόγηση προθέσεων | ~45s |
| 06 | `models_pipeline.py` | Πολυβηματική διαδικασία | ~60s |

---

## 🛠️ Μεταβλητές Περιβάλλοντος

### Απαραίτητες
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Ειδικές για Συνεδρία
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Επικύρωση & Δοκιμή

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Επίλυση Προβλημάτων

### Σφάλμα Σύνδεσης
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Σφάλμα Εισαγωγής
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Μοντέλο Δεν Βρέθηκε
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Αργή Απόδοση
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Κοινά Μοτίβα

### Βασική Συνομιλία
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Λήψη Πελάτη
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Διαχείριση Σφαλμάτων
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Ροή
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Επιλογή Μοντέλου

| Μοντέλο | Μέγεθος | Καλύτερο Για | Ταχύτητα |
|---------|---------|--------------|----------|
| `qwen2.5-0.5b` | 0.5B | Γρήγορη ταξινόμηση | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Γρήγορη δημιουργία κώδικα | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Δημιουργική γραφή | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Κώδικας, αναδιάρθρωση | ⚡⚡ |
| `phi-4-mini` | 4B | Γενικά, σύνοψη | ⚡⚡ |
| `qwen2.5-7b` | 7B | Σύνθετη λογική | ⚡ |

---

## 🔗 Πόροι

- **Έγγραφα SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Γρήγορη Αναφορά**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Συμβουλές

1. **Αποθήκευση πελατών**: Το `workshop_utils` αποθηκεύει για εσάς
2. **Χρησιμοποιήστε μικρότερα μοντέλα**: Ξεκινήστε με το `qwen2.5-0.5b` για δοκιμές
3. **Ενεργοποιήστε στατιστικά χρήσης**: Ορίστε `SHOW_USAGE=1` για παρακολούθηση tokens
4. **Επεξεργασία σε παρτίδες**: Επεξεργαστείτε πολλαπλά prompts διαδοχικά
5. **Μειώστε το max_tokens**: Μειώνει την καθυστέρηση για γρήγορες απαντήσεις

---

## 🎯 Δείγματα Ροών Εργασίας

### Δοκιμή Όλων
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Αξιολόγηση Μοντέλων
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG Pipeline
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Σύστημα Πολλαπλών Πρακτόρων
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Γρήγορη Βοήθεια**: Εκτελέστε οποιοδήποτε δείγμα με `--help` από τον φάκελο `samples` ή ελέγξτε το docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Όλα τα δείγματα ενημερώθηκαν τον Οκτώβριο 2025 με τις βέλτιστες πρακτικές του Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->