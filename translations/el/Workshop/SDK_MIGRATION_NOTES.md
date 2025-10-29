<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:57:19+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "el"
}
-->
# Σημειώσεις Μετάβασης για το Foundry Local SDK

## Επισκόπηση

Όλα τα αρχεία Python στον φάκελο Workshop έχουν ενημερωθεί ώστε να ακολουθούν τα πιο πρόσφατα πρότυπα από το επίσημο [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Περίληψη Αλλαγών

### Βασική Υποδομή (`workshop_utils.py`)

#### Βελτιωμένες Λειτουργίες:
- **Υποστήριξη Εναλλακτικού Endpoint**: Προστέθηκε υποστήριξη για τη μεταβλητή περιβάλλοντος `FOUNDRY_LOCAL_ENDPOINT`
- **Βελτιωμένος Χειρισμός Σφαλμάτων**: Καλύτερος χειρισμός εξαιρέσεων με λεπτομερή μηνύματα σφάλματος
- **Ενισχυμένη Προσωρινή Αποθήκευση**: Τα κλειδιά προσωρινής αποθήκευσης περιλαμβάνουν πλέον το endpoint για σενάρια πολλαπλών endpoints
- **Εκθετική Επαναπροσπάθεια**: Η λογική επαναπροσπάθειας χρησιμοποιεί πλέον εκθετική καθυστέρηση για καλύτερη αξιοπιστία
- **Σχολιασμοί Τύπων**: Προστέθηκαν εκτενείς υποδείξεις τύπων για καλύτερη υποστήριξη από IDE

#### Νέες Δυνατότητες:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Δείγματα Εφαρμογών

#### Συνεδρία 01: Εκκίνηση Συνομιλίας (`chat_bootstrap.py`)
- Ενημερώθηκε το προεπιλεγμένο μοντέλο από `phi-3.5-mini` σε `phi-4-mini`
- Προστέθηκε υποστήριξη εναλλακτικού endpoint
- Ενισχύθηκε η τεκμηρίωση με αναφορές στο SDK

#### Συνεδρία 02: RAG Pipeline (`rag_pipeline.py`)
- Ενημερώθηκε για χρήση του `phi-4-mini` ως προεπιλογή
- Προστέθηκε υποστήριξη εναλλακτικού endpoint
- Βελτιώθηκε η τεκμηρίωση με λεπτομέρειες για τις μεταβλητές περιβάλλοντος

#### Συνεδρία 02: Αξιολόγηση RAG (`rag_eval_ragas.py`)
- Ενημερώθηκαν οι προεπιλογές μοντέλων
- Προστέθηκε διαμόρφωση endpoint
- Ενισχύθηκε ο χειρισμός σφαλμάτων

#### Συνεδρία 03: Αξιολόγηση Απόδοσης (`benchmark_oss_models.py`)
- Ενημερώθηκε η προεπιλεγμένη λίστα μοντέλων για να περιλαμβάνει το `phi-4-mini`
- Προστέθηκε εκτενής τεκμηρίωση για τις μεταβλητές περιβάλλοντος
- Βελτιώθηκε η τεκμηρίωση των συναρτήσεων
- Προστέθηκε υποστήριξη εναλλακτικού endpoint σε όλη την εφαρμογή

#### Συνεδρία 04: Σύγκριση Μοντέλων (`model_compare.py`)
- Ενημερώθηκε το προεπιλεγμένο LLM από `gpt-oss-20b` σε `qwen2.5-7b`
- Προστέθηκε διαμόρφωση endpoint
- Ενισχύθηκε η τεκμηρίωση

#### Συνεδρία 05: Ορχήστρα Πολλαπλών Πρακτόρων (`agents_orchestrator.py`)
- Προστέθηκαν υποδείξεις τύπων (αλλαγή από `str | None` σε `Optional[str]`)
- Ενισχύθηκε η τεκμηρίωση της κλάσης Agent
- Προστέθηκε υποστήριξη εναλλακτικού endpoint
- Βελτιώθηκε το μοτίβο αρχικοποίησης

#### Συνεδρία 06: Δρομολογητής Μοντέλων (`models_router.py`)
- Προστέθηκε διαμόρφωση endpoint
- Ενισχύθηκε η τεκμηρίωση ανίχνευσης προθέσεων
- Βελτιώθηκε η τεκμηρίωση της λογικής δρομολόγησης

#### Συνεδρία 06: Pipeline (`models_pipeline.py`)
- Προστέθηκε εκτενής τεκμηρίωση συναρτήσεων
- Βελτιώθηκε η τεκμηρίωση βήμα προς βήμα
- Ενισχύθηκε ο χειρισμός σφαλμάτων

### Scripts

#### Εξαγωγή Αξιολόγησης Απόδοσης (`export_benchmark_markdown.py`)
- Προστέθηκε υποστήριξη εναλλακτικού endpoint
- Ενημερώθηκαν τα προεπιλεγμένα μοντέλα
- Ενισχύθηκε η τεκμηρίωση συναρτήσεων
- Βελτιώθηκε ο χειρισμός σφαλμάτων

#### CLI Linter (`lint_markdown_cli.py`)
- Προστέθηκαν σύνδεσμοι αναφοράς στο SDK
- Βελτιώθηκε η τεκμηρίωση χρήσης

### Δοκιμές

#### Δοκιμές Λειτουργίας (`smoke.py`)
- Προστέθηκε υποστήριξη εναλλακτικού endpoint
- Ενισχύθηκε η τεκμηρίωση
- Βελτιώθηκε η τεκμηρίωση των περιπτώσεων δοκιμής
- Καλύτερη αναφορά σφαλμάτων

## Μεταβλητές Περιβάλλοντος

Όλα τα δείγματα υποστηρίζουν πλέον αυτές τις μεταβλητές περιβάλλοντος:

### Βασική Διαμόρφωση
- `FOUNDRY_LOCAL_ALIAS` - Ψευδώνυμο μοντέλου προς χρήση (η προεπιλογή διαφέρει ανά δείγμα)
- `FOUNDRY_LOCAL_ENDPOINT` - Εναλλακτικό endpoint υπηρεσίας (προαιρετικό)
- `SHOW_USAGE` - Εμφάνιση στατιστικών χρήσης token (προεπιλογή: "0")
- `RETRY_ON_FAIL` - Ενεργοποίηση λογικής επαναπροσπάθειας (προεπιλογή: "1")
- `RETRY_BACKOFF` - Αρχική καθυστέρηση επαναπροσπάθειας σε δευτερόλεπτα (προεπιλογή: "1.0")

### Ειδικές για Δείγματα
- `EMBED_MODEL` - Μοντέλο ενσωμάτωσης για δείγματα RAG
- `BENCH_MODELS` - Μοντέλα διαχωρισμένα με κόμμα για αξιολόγηση απόδοσης
- `BENCH_ROUNDS` - Αριθμός γύρων αξιολόγησης
- `BENCH_PROMPT` - Δοκιμαστική προτροπή για αξιολογήσεις
- `BENCH_STREAM` - Μέτρηση καθυστέρησης πρώτου token
- `RAG_QUESTION` - Δοκιμαστική ερώτηση για δείγματα RAG
- `AGENT_MODEL_PRIMARY` - Κύριο μοντέλο πράκτορα
- `AGENT_MODEL_EDITOR` - Μοντέλο πράκτορα επεξεργασίας
- `SLM_ALIAS` - Ψευδώνυμο μικρού γλωσσικού μοντέλου
- `LLM_ALIAS` - Ψευδώνυμο μεγάλου γλωσσικού μοντέλου

## Βέλτιστες Πρακτικές SDK που Εφαρμόστηκαν

### 1. Σωστή Αρχικοποίηση Πελάτη
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Ανάκτηση Πληροφοριών Μοντέλου
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Χειρισμός Σφαλμάτων
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Λογική Επαναπροσπάθειας με Εκθετική Καθυστέρηση
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Υποστήριξη Ροής
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Οδηγός Μετάβασης για Προσαρμοσμένα Δείγματα

Αν δημιουργείτε νέα δείγματα ή ενημερώνετε υπάρχοντα:

1. **Χρησιμοποιήστε τους βοηθούς του `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Υποστηρίξτε εναλλακτικό endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Προσθέστε εκτενή τεκμηρίωση**:
   - Μεταβλητές περιβάλλοντος στο docstring
   - Σύνδεσμοι αναφοράς SDK
   - Παραδείγματα χρήσης

4. **Χρησιμοποιήστε υποδείξεις τύπων**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Εφαρμόστε σωστό χειρισμό σφαλμάτων**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Δοκιμές

Όλα τα δείγματα μπορούν να δοκιμαστούν με:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Αναφορές Τεκμηρίωσης SDK

- **Κύριο Αποθετήριο**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Τεκμηρίωση API**: Ελέγξτε το αποθετήριο SDK για την πιο πρόσφατη τεκμηρίωση API

## Σημαντικές Αλλαγές

### Δεν Αναμένονται
Όλες οι αλλαγές είναι συμβατές με προηγούμενες εκδόσεις. Οι ενημερώσεις κυρίως:
- Προσθέτουν νέες προαιρετικές λειτουργίες (εναλλακτικό endpoint)
- Βελτιώνουν τον χειρισμό σφαλμάτων
- Ενισχύουν την τεκμηρίωση
- Ενημερώνουν τα προεπιλεγμένα ονόματα μοντέλων σύμφωνα με τις τρέχουσες συστάσεις

### Προαιρετικές Βελτιώσεις
Ίσως θελήσετε να ενημερώσετε τον κώδικά σας για να χρησιμοποιήσετε:
- `FOUNDRY_LOCAL_ENDPOINT` για ρητό έλεγχο του endpoint
- `SHOW_USAGE=1` για ορατότητα χρήσης token
- Ενημερωμένες προεπιλογές μοντέλων (`phi-4-mini` αντί για `phi-3.5-mini`)

## Συνηθισμένα Προβλήματα & Λύσεις

### Πρόβλημα: "Αποτυχία αρχικοποίησης πελάτη"
**Λύση**: Βεβαιωθείτε ότι η υπηρεσία Foundry Local λειτουργεί:
```bash
foundry service start
foundry model run phi-4-mini
```

### Πρόβλημα: "Το μοντέλο δεν βρέθηκε"
**Λύση**: Ελέγξτε τα διαθέσιμα μοντέλα:
```bash
foundry model list
```

### Πρόβλημα: Σφάλματα σύνδεσης με το endpoint
**Λύση**: Επαληθεύστε το endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Επόμενα Βήματα

1. **Ενημέρωση δειγμάτων Module08**: Εφαρμόστε παρόμοια πρότυπα στα δείγματα του Module08
2. **Προσθήκη δοκιμών ενσωμάτωσης**: Δημιουργήστε εκτενή σουίτα δοκιμών
3. **Αξιολόγηση απόδοσης**: Συγκρίνετε την απόδοση πριν/μετά
4. **Ενημερώσεις τεκμηρίωσης**: Ενημερώστε το κύριο README με νέα πρότυπα

## Οδηγίες Συνεισφοράς

Κατά την προσθήκη νέων δειγμάτων:
1. Χρησιμοποιήστε το `workshop_utils.py` για συνέπεια
2. Ακολουθήστε το πρότυπο των υπαρχόντων δειγμάτων
3. Προσθέστε εκτενή docstrings
4. Συμπεριλάβετε συνδέσμους αναφοράς SDK
5. Υποστηρίξτε εναλλακτικό endpoint
6. Προσθέστε σωστές υποδείξεις τύπων
7. Συμπεριλάβετε παραδείγματα χρήσης στο docstring

## Συμβατότητα Έκδοσης

Αυτές οι ενημερώσεις είναι συμβατές με:
- `foundry-local-sdk` (τελευταία έκδοση)
- `openai>=1.30.0`
- Python 3.8+

---

**Τελευταία Ενημέρωση**: 2025-01-08  
**Υπεύθυνος Συντήρησης**: EdgeAI Workshop Team  
**Έκδοση SDK**: Foundry Local SDK (τελευταία 0.7.117+67073234e7)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.