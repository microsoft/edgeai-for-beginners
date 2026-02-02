# Παράδειγμα 02: Ενσωμάτωση OpenAI SDK

Παρουσιάζει προηγμένη ενσωμάτωση με το OpenAI Python SDK, υποστηρίζοντας τόσο το Microsoft Foundry Local όσο και το Azure OpenAI με ροές απαντήσεων και σωστή διαχείριση σφαλμάτων.

## Επισκόπηση

Αυτό το παράδειγμα περιλαμβάνει:
- Ομαλή εναλλαγή μεταξύ Foundry Local και Azure OpenAI
- Ροές συνομιλιών για καλύτερη εμπειρία χρήστη
- Σωστή χρήση του FoundryLocalManager SDK
- Ισχυρούς μηχανισμούς διαχείρισης σφαλμάτων και εναλλακτικών λύσεων
- Κώδικα έτοιμο για παραγωγή

## Προαπαιτούμενα

- **Foundry Local**: Εγκατεστημένο και σε λειτουργία (για τοπική πρόβλεψη)
- **Python**: Έκδοση 3.8 ή νεότερη με OpenAI SDK
- **Azure OpenAI**: Έγκυρο endpoint και API key (για πρόβλεψη στο cloud)

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

3. **Εκκίνηση Foundry Local (για τοπική λειτουργία):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Σενάρια Χρήσης

### Foundry Local (Προεπιλογή)

**Επιλογή 1: Χρήση του FoundryLocalManager (Συνιστάται)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Επιλογή 2: Χειροκίνητη Ρύθμιση**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Αρχιτεκτονική Κώδικα

### Σχέδιο Εργοστασίου Πελάτη

Το παράδειγμα χρησιμοποιεί ένα σχέδιο εργοστασίου για τη δημιουργία κατάλληλων πελατών:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Ροές Απαντήσεων

Το παράδειγμα παρουσιάζει ροές για τη δημιουργία απαντήσεων σε πραγματικό χρόνο:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Μεταβλητές Περιβάλλοντος

### Ρύθμιση Foundry Local

| Μεταβλητή | Περιγραφή | Προεπιλογή | Απαιτείται |
|-----------|-----------|------------|------------|
| `MODEL` | Ψευδώνυμο μοντέλου προς χρήση | `phi-4-mini` | Όχι |
| `BASE_URL` | Endpoint του Foundry Local | `http://localhost:8000` | Όχι |
| `API_KEY` | API key (προαιρετικό για τοπική χρήση) | `""` | Όχι |

### Ρύθμιση Azure OpenAI

| Μεταβλητή | Περιγραφή | Προεπιλογή | Απαιτείται |
|-----------|-----------|------------|------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint του Azure OpenAI | - | Ναι |
| `AZURE_OPENAI_API_KEY` | API key του Azure OpenAI | - | Ναι |
| `AZURE_OPENAI_API_VERSION` | Έκδοση API | `2024-08-01-preview` | Όχι |
| `MODEL` | Όνομα ανάπτυξης Azure | `your-deployment-name` | Ναι |

## Προηγμένα Χαρακτηριστικά

### Αυτόματη Ανακάλυψη Υπηρεσιών

Το παράδειγμα ανιχνεύει αυτόματα την κατάλληλη υπηρεσία βάσει των μεταβλητών περιβάλλοντος:

1. **Λειτουργία Azure**: Εάν έχουν οριστεί οι `AZURE_OPENAI_ENDPOINT` και `AZURE_OPENAI_API_KEY`
2. **Λειτουργία Foundry SDK**: Εάν είναι διαθέσιμο το Foundry Local SDK
3. **Χειροκίνητη Λειτουργία**: Εναλλακτική λύση με χειροκίνητη ρύθμιση

### Διαχείριση Σφαλμάτων

- Ομαλή εναλλακτική λύση από SDK σε χειροκίνητη ρύθμιση
- Σαφή μηνύματα σφαλμάτων για αντιμετώπιση προβλημάτων
- Σωστή διαχείριση εξαιρέσεων για προβλήματα δικτύου
- Επικύρωση των απαιτούμενων μεταβλητών περιβάλλοντος

## Σκέψεις Απόδοσης

### Τοπική vs Cloud Ανταλλαγές

**Πλεονεκτήματα Foundry Local:**
- ✅ Χωρίς κόστος API
- ✅ Ιδιωτικότητα δεδομένων (τα δεδομένα δεν φεύγουν από τη συσκευή)
- ✅ Χαμηλή καθυστέρηση για υποστηριζόμενα μοντέλα
- ✅ Λειτουργεί εκτός σύνδεσης

**Πλεονεκτήματα Azure OpenAI:**
- ✅ Πρόσβαση στα τελευταία μεγάλα μοντέλα
- ✅ Υψηλότερη απόδοση
- ✅ Χωρίς απαιτήσεις τοπικής υπολογιστικής ισχύος
- ✅ SLA επιπέδου επιχείρησης

## Αντιμετώπιση Προβλημάτων

### Συνηθισμένα Προβλήματα

1. **Προειδοποίηση "Δεν ήταν δυνατή η χρήση του Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Σφάλματα αυθεντικοποίησης Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Μοντέλο μη διαθέσιμο:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Έλεγχοι Υγείας

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Επόμενα Βήματα

- **Παράδειγμα 03**: Ανακάλυψη και αξιολόγηση μοντέλων
- **Παράδειγμα 04**: Δημιουργία εφαρμογής Chainlit RAG
- **Παράδειγμα 05**: Ορχήστρα πολλαπλών πρακτόρων
- **Παράδειγμα 06**: Δρομολόγηση μοντέλων ως εργαλεία

## Αναφορές

- [Τεκμηρίωση Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Αναφορά SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Τεκμηρίωση OpenAI Python SDK](https://github.com/openai/openai-python)
- [Οδηγός Ροών Απαντήσεων](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

