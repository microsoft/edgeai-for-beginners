# Foundry Local ως Παράδειγμα API

Αυτό το παράδειγμα δείχνει πώς να χρησιμοποιήσετε το Microsoft Foundry Local ως υπηρεσία REST API χωρίς να βασίζεστε στο OpenAI SDK. Παρουσιάζει άμεσες μεθόδους ενσωμάτωσης HTTP για μέγιστο έλεγχο και προσαρμογή.

## Επισκόπηση

Βασισμένο στα επίσημα πρότυπα του Microsoft Foundry Local, αυτό το παράδειγμα παρέχει:
- Άμεση ενσωμάτωση REST API με το FoundryLocalManager
- Προσαρμοσμένη υλοποίηση HTTP client
- Διαχείριση μοντέλων και παρακολούθηση υγείας
- Χειρισμός αποκρίσεων με και χωρίς ροή
- Λογική χειρισμού σφαλμάτων και επαναπροσπαθειών έτοιμη για παραγωγή

## Προαπαιτούμενα

1. **Εγκατάσταση Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Εξαρτήσεις Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Αρχιτεκτονική

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Βασικά Χαρακτηριστικά

### 1. **Άμεση Ενσωμάτωση HTTP**
- Καθαρά REST API κλήσεις χωρίς εξαρτήσεις από SDK
- Προσαρμοσμένος έλεγχος ταυτότητας και επικεφαλίδες
- Πλήρης έλεγχος χειρισμού αιτημάτων/αποκρίσεων

### 2. **Διαχείριση Μοντέλων**
- Δυναμική φόρτωση και εκφόρτωση μοντέλων
- Παρακολούθηση υγείας και έλεγχοι κατάστασης
- Συλλογή μετρήσεων απόδοσης

### 3. **Παραγωγικά Πρότυπα**
- Μηχανισμοί επαναπροσπαθειών με εκθετική καθυστέρηση
- Circuit breaker για ανοχή σε σφάλματα
- Ολοκληρωμένη καταγραφή και παρακολούθηση

### 4. **Ευέλικτος Χειρισμός Αποκρίσεων**
- Αποκρίσεις με ροή για εφαρμογές σε πραγματικό χρόνο
- Επεξεργασία παρτίδων για σενάρια υψηλής απόδοσης
- Προσαρμοσμένη ανάλυση και επικύρωση αποκρίσεων

## Παραδείγματα Χρήσης

### Βασική Ενσωμάτωση API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Ενσωμάτωση με Ροή
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Παρακολούθηση Υγείας
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Δομή Αρχείων

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Ενσωμάτωση Microsoft Foundry Local

Αυτό το παράδειγμα ακολουθεί τα επίσημα πρότυπα της Microsoft:

1. **Ενσωμάτωση SDK**: Χρησιμοποιεί το `FoundryLocalManager` για διαχείριση υπηρεσιών
2. **REST Endpoints**: Άμεσες κλήσεις σε `/v1/chat/completions` και άλλα endpoints
3. **Έλεγχος Ταυτότητας**: Σωστή διαχείριση API key για τοπικές υπηρεσίες
4. **Διαχείριση Μοντέλων**: Λίστα καταλόγου, λήψη και φόρτωση μοντέλων
5. **Χειρισμός Σφαλμάτων**: Συνιστώμενοι κωδικοί σφαλμάτων και αποκρίσεις από τη Microsoft

## Ξεκινώντας

1. **Εγκατάσταση Εξαρτήσεων**
   ```bash
   pip install -r requirements.txt
   ```

2. **Εκτέλεση Βασικού Παραδείγματος**
   ```bash
   python examples/basic_usage.py
   ```

3. **Δοκιμή Ροής**
   ```bash
   python examples/streaming.py
   ```

4. **Ρύθμιση Παραγωγής**
   ```bash
   python examples/production.py
   ```

## Ρύθμιση

Μεταβλητές περιβάλλοντος για προσαρμογή:
- `FOUNDRY_MODEL`: Προεπιλεγμένο μοντέλο προς χρήση (προεπιλογή: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Χρονικό όριο αιτήματος σε δευτερόλεπτα (προεπιλογή: 30)
- `FOUNDRY_RETRIES`: Αριθμός προσπαθειών επαναπροσπάθειας (προεπιλογή: 3)
- `FOUNDRY_LOG_LEVEL`: Επίπεδο καταγραφής (προεπιλογή: "INFO")

## Βέλτιστες Πρακτικές

1. **Διαχείριση Συνδέσεων**: Επαναχρησιμοποίηση συνδέσεων HTTP για καλύτερη απόδοση
2. **Χειρισμός Σφαλμάτων**: Υλοποίηση σωστής λογικής επαναπροσπάθειας με εκθετική καθυστέρηση
3. **Παρακολούθηση Πόρων**: Παρακολούθηση χρήσης μνήμης και απόδοσης μοντέλων
4. **Ασφάλεια**: Χρήση σωστού ελέγχου ταυτότητας ακόμα και για τοπικές υπηρεσίες
5. **Δοκιμές**: Συμπερίληψη τόσο μονάδων όσο και δοκιμών ενσωμάτωσης

## Αντιμετώπιση Προβλημάτων

### Συνηθισμένα Προβλήματα

**Η Υπηρεσία Δεν Λειτουργεί**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Προβλήματα Φόρτωσης Μοντέλων**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Σφάλματα Σύνδεσης**
- Επαλήθευση ότι το Foundry Local λειτουργεί στη σωστή θύρα
- Έλεγχος ρυθμίσεων τείχους προστασίας
- Εξασφάλιση σωστών επικεφαλίδων ελέγχου ταυτότητας

## Βελτιστοποίηση Απόδοσης

1. **Pooling Συνδέσεων**: Χρήση αντικειμένων συνεδρίας για πολλαπλά αιτήματα
2. **Ασύγχρονες Λειτουργίες**: Αξιοποίηση του asyncio για ταυτόχρονα αιτήματα
3. **Caching**: Αποθήκευση αποκρίσεων μοντέλων όπου είναι κατάλληλο
4. **Παρακολούθηση**: Παρακολούθηση χρόνων αποκρίσεων και προσαρμογή χρονικών ορίων

## Μαθησιακά Αποτελέσματα

Μετά την ολοκλήρωση αυτού του παραδείγματος, θα κατανοήσετε:
- Άμεση ενσωμάτωση REST API με το Foundry Local
- Πρότυπα υλοποίησης προσαρμοσμένου HTTP client
- Χειρισμό σφαλμάτων και παρακολούθηση έτοιμα για παραγωγή
- Αρχιτεκτονική υπηρεσιών Microsoft Foundry Local
- Τεχνικές βελτιστοποίησης απόδοσης για τοπικές υπηρεσίες AI

## Επόμενα Βήματα

- Εξερευνήστε το Παράδειγμα 08: Εφαρμογή Συνομιλίας Windows 11
- Δοκιμάστε το Παράδειγμα 09: Ορχήστρωση Πολλαπλών Πρακτόρων
- Μάθετε το Παράδειγμα 10: Foundry Local ως Ενσωμάτωση Εργαλείων

---

