# Παράδειγμα 01: Γρήγορη Συνομιλία μέσω OpenAI SDK

Ένα απλό παράδειγμα συνομιλίας που δείχνει πώς να χρησιμοποιήσετε το OpenAI SDK με το Microsoft Foundry Local για τοπική επεξεργασία AI.

## Επισκόπηση

Αυτό το παράδειγμα δείχνει πώς να:
- Χρησιμοποιήσετε το OpenAI Python SDK με το Foundry Local
- Διαχειριστείτε τόσο τις ρυθμίσεις του Azure OpenAI όσο και του τοπικού Foundry
- Εφαρμόσετε σωστό χειρισμό σφαλμάτων και στρατηγικές εφεδρείας
- Χρησιμοποιήσετε το FoundryLocalManager για τη διαχείριση υπηρεσιών

## Προαπαιτούμενα

- **Foundry Local**: Εγκατεστημένο και διαθέσιμο στο PATH
- **Python**: Έκδοση 3.8 ή νεότερη
- **Μοντέλο**: Ένα μοντέλο φορτωμένο στο Foundry Local (π.χ., `phi-4-mini`)

## Εγκατάσταση

1. **Ρύθμιση περιβάλλοντος Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Εγκατάσταση εξαρτήσεων:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Εκκίνηση της υπηρεσίας Foundry Local και φόρτωση μοντέλου:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Χρήση

### Foundry Local (Προεπιλογή)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## Χαρακτηριστικά Κώδικα

### Ενσωμάτωση FoundryLocalManager

Το παράδειγμα χρησιμοποιεί το επίσημο Foundry Local SDK για σωστή διαχείριση υπηρεσιών:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### Χειρισμός Σφαλμάτων

Ανθεκτικός χειρισμός σφαλμάτων με εφεδρεία σε χειροκίνητη ρύθμιση:
- Αυτόματη ανακάλυψη υπηρεσιών
- Ομαλή υποβάθμιση αν το SDK δεν είναι διαθέσιμο
- Σαφή μηνύματα σφαλμάτων για αντιμετώπιση προβλημάτων

## Μεταβλητές Περιβάλλοντος

| Μεταβλητή | Περιγραφή | Προεπιλογή | Απαιτείται |
|----------|-------------|---------|----------|
| `MODEL` | Ψευδώνυμο ή όνομα μοντέλου | `phi-4-mini` | Όχι |
| `BASE_URL` | Βασικό URL του Foundry Local | `http://localhost:8000` | Όχι |
| `API_KEY` | Κλειδί API (συνήθως δεν χρειάζεται για τοπικό) | `""` | Όχι |
| `AZURE_OPENAI_ENDPOINT` | Endpoint του Azure OpenAI | - | Για Azure |
| `AZURE_OPENAI_API_KEY` | Κλειδί API του Azure OpenAI | - | Για Azure |
| `AZURE_OPENAI_API_VERSION` | Έκδοση API του Azure | `2024-08-01-preview` | Όχι |

## Αντιμετώπιση Προβλημάτων

### Συνηθισμένα Προβλήματα

1. **Προειδοποίηση "Δεν ήταν δυνατή η χρήση του Foundry SDK":**
   - Εγκαταστήστε το foundry-local-sdk: `pip install foundry-local-sdk`
   - Ή ορίστε μεταβλητές περιβάλλοντος για χειροκίνητη ρύθμιση

2. **Αρνήθηκε η σύνδεση:**
   - Βεβαιωθείτε ότι το Foundry Local εκτελείται: `foundry service status`
   - Ελέγξτε αν έχει φορτωθεί ένα μοντέλο: `foundry service ps`

3. **Το μοντέλο δεν βρέθηκε:**
   - Λίστα διαθέσιμων μοντέλων: `foundry model list`
   - Φόρτωση μοντέλου: `foundry model run phi-4-mini`

### Επαλήθευση

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Αναφορές

- [Τεκμηρίωση Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Αναφορά API συμβατή με OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

