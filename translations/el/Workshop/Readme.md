<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b994c57f1207012e4d7f58b7c0d1ae7",
  "translation_date": "2025-10-17T09:40:09+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "el"
}
-->
# EdgeAI για Αρχάριους - Εργαστήριο

> **Πρακτική Διαδρομή Μάθησης για Δημιουργία Εφαρμογών Edge AI Έτοιμων για Παραγωγή**
>
> Μάθετε την τοπική ανάπτυξη AI με το Microsoft Foundry Local, από την πρώτη ολοκλήρωση συνομιλίας έως τον συντονισμό πολλαπλών πρακτόρων σε 6 προοδευτικές συνεδρίες.

---

## 🎯 Εισαγωγή

Καλώς ήρθατε στο **Εργαστήριο EdgeAI για Αρχάριους** - ο πρακτικός σας οδηγός για τη δημιουργία έξυπνων εφαρμογών που λειτουργούν αποκλειστικά σε τοπικό υλικό. Αυτό το εργαστήριο μετατρέπει τις θεωρητικές έννοιες του Edge AI σε πραγματικές δεξιότητες μέσω προοδευτικά απαιτητικών ασκήσεων χρησιμοποιώντας το Microsoft Foundry Local και Μικρά Μοντέλα Γλώσσας (SLMs).

### Γιατί Αυτό το Εργαστήριο;

**Η Επανάσταση του Edge AI Είναι Εδώ**

Οργανισμοί παγκοσμίως μεταβαίνουν από την εξαρτώμενη από το cloud AI στην υπολογιστική στο edge για τρεις κρίσιμους λόγους:

1. **Ιδιωτικότητα & Συμμόρφωση** - Επεξεργασία ευαίσθητων δεδομένων τοπικά χωρίς μετάδοση στο cloud (HIPAA, GDPR, χρηματοοικονομικοί κανονισμοί)
2. **Απόδοση** - Εξάλειψη της καθυστέρησης δικτύου (50-500ms τοπικά έναντι 500-2000ms στο cloud)
3. **Έλεγχος Κόστους** - Αφαίρεση κόστους ανά token API και κλιμάκωση χωρίς έξοδα cloud

**Αλλά το Edge AI Είναι Διαφορετικό**

Η λειτουργία AI στις εγκαταστάσεις απαιτεί νέες δεξιότητες:
- Επιλογή και βελτιστοποίηση μοντέλων για περιορισμούς πόρων
- Διαχείριση τοπικών υπηρεσιών και επιτάχυνση υλικού
- Σχεδιασμός προτροπών για μικρότερα μοντέλα
- Πρότυπα ανάπτυξης παραγωγής για συσκευές edge

**Αυτό το Εργαστήριο Παρέχει Αυτές τις Δεξιότητες**

Σε 6 εστιασμένες συνεδρίες (~3 ώρες συνολικά), θα προχωρήσετε από το "Hello World" στην ανάπτυξη συστημάτων πολλαπλών πρακτόρων έτοιμων για παραγωγή - όλα λειτουργούν τοπικά στον υπολογιστή σας.

---

## 📚 Στόχοι Μάθησης

Με την ολοκλήρωση αυτού του εργαστηρίου, θα μπορείτε να:

### Βασικές Δεξιότητες
1. **Ανάπτυξη και Διαχείριση Τοπικών Υπηρεσιών AI**
   - Εγκατάσταση και διαμόρφωση του Microsoft Foundry Local
   - Επιλογή κατάλληλων μοντέλων για ανάπτυξη στο edge
   - Διαχείριση κύκλου ζωής μοντέλων (λήψη, φόρτωση, προσωρινή αποθήκευση)
   - Παρακολούθηση χρήσης πόρων και βελτιστοποίηση απόδοσης

2. **Δημιουργία Εφαρμογών Με Τεχνητή Νοημοσύνη**
   - Υλοποίηση τοπικών ολοκληρώσεων συνομιλίας συμβατών με OpenAI
   - Σχεδιασμός αποτελεσματικών προτροπών για Μικρά Μοντέλα Γλώσσας
   - Διαχείριση ροών απαντήσεων για καλύτερη εμπειρία χρήστη
   - Ενσωμάτωση τοπικών μοντέλων σε υπάρχουσες εφαρμογές

3. **Δημιουργία Συστημάτων RAG (Ανάκτηση Ενισχυμένης Γενιάς)**
   - Δημιουργία σημασιολογικής αναζήτησης με ενσωματώσεις
   - Ενίσχυση απαντήσεων LLM με γνώση συγκεκριμένου τομέα
   - Αξιολόγηση ποιότητας RAG με βιομηχανικά πρότυπα
   - Κλιμάκωση από πρωτότυπο σε παραγωγή

4. **Βελτιστοποίηση Απόδοσης Μοντέλων**
   - Δοκιμή πολλαπλών μοντέλων για την περίπτωσή σας
   - Μέτρηση καθυστέρησης, ρυθμού και χρόνου πρώτου token
   - Επιλογή βέλτιστων μοντέλων βάσει συμβιβασμών ταχύτητας/ποιότητας
   - Σύγκριση SLM έναντι LLM σε πραγματικά σενάρια

5. **Συντονισμός Συστημάτων Πολλαπλών Πρακτόρων**
   - Σχεδιασμός εξειδικευμένων πρακτόρων για διαφορετικές εργασίες
   - Υλοποίηση μνήμης πρακτόρων και διαχείριση πλαισίου
   - Συντονισμός πρακτόρων σε σύνθετες ροές εργασίας
   - Δρομολόγηση αιτημάτων έξυπνα σε πολλαπλά μοντέλα

6. **Ανάπτυξη Λύσεων Έτοιμων για Παραγωγή**
   - Υλοποίηση λογικής χειρισμού σφαλμάτων και επαναπροσπάθειας
   - Παρακολούθηση χρήσης token και πόρων συστήματος
   - Δημιουργία κλιμακούμενων αρχιτεκτονικών με πρότυπα μοντέλων ως εργαλεία
   - Σχεδιασμός μονοπατιών μετανάστευσης από edge σε υβριδικό (edge + cloud)

---

## 🎓 Αποτελέσματα Μάθησης

### Τι Θα Δημιουργήσετε

Μέχρι το τέλος αυτού του εργαστηρίου, θα έχετε δημιουργήσει:

| Συνεδρία | Παραδοτέο | Δεξιότητες που Επιδεικνύονται |
|----------|-----------|-----------------------------|
| **1** | Εφαρμογή συνομιλίας με ροή | Ρύθμιση υπηρεσίας, βασικές ολοκληρώσεις, UX ροής |
| **2** | Σύστημα RAG με αξιολόγηση | Ενσωματώσεις, σημασιολογική αναζήτηση, μετρικές ποιότητας |
| **3** | Σουίτα δοκιμών πολλαπλών μοντέλων | Μέτρηση απόδοσης, σύγκριση μοντέλων |
| **4** | Σύγκριση SLM έναντι LLM | Ανάλυση συμβιβασμών, στρατηγικές βελτιστοποίησης |
| **5** | Συντονιστής πολλαπλών πρακτόρων | Σχεδιασμός πρακτόρων, διαχείριση μνήμης, συντονισμός |
| **6** | Σύστημα έξυπνης δρομολόγησης | Ανίχνευση προθέσεων, επιλογή μοντέλων, κλιμακούμενη αρχιτεκτονική |

### Πίνακας Δεξιοτήτων

| Επίπεδο Δεξιοτήτων | Συνεδρίες 1-2 | Συνεδρίες 3-4 | Συνεδρίες 5-6 |
|--------------------|---------------|---------------|---------------|
| **Αρχάριος** | ✅ Ρύθμιση & βασικά | ⚠️ Απαιτητικό | ❌ Πολύ προχωρημένο |
| **Μεσαίος** | ✅ Γρήγορη ανασκόπηση | ✅ Βασική μάθηση | ⚠️ Στόχοι επέκτασης |
| **Προχωρημένος** | ✅ Εύκολη ολοκλήρωση | ✅ Βελτίωση | ✅ Πρότυπα παραγωγής |

### Δεξιότητες Έτοιμες για Καριέρα

**Μετά από αυτό το εργαστήριο, θα είστε έτοιμοι να:**

✅ **Δημιουργήσετε Εφαρμογές με Προτεραιότητα στην Ιδιωτικότητα**
- Εφαρμογές υγειονομικής περίθαλψης που χειρίζονται PHI/PII τοπικά
- Υπηρεσίες χρηματοοικονομικών με απαιτήσεις συμμόρφωσης
- Κυβερνητικά συστήματα με ανάγκες κυριαρχίας δεδομένων

✅ **Βελτιστοποιήσετε για Περιβάλλοντα Edge**
- Συσκευές IoT με περιορισμένους πόρους
- Εφαρμογές κινητών με προτεραιότητα την εκτός σύνδεσης λειτουργία
- Συστήματα πραγματικού χρόνου χαμηλής καθυστέρησης

✅ **Σχεδιάσετε Έξυπνες Αρχιτεκτονικές**
- Συστήματα πολλαπλών πρακτόρων για σύνθετες ροές εργασίας
- Υβριδικές αναπτύξεις edge-cloud
- Υποδομή AI με βελτιστοποιημένο κόστος

✅ **Ηγηθείτε Πρωτοβουλιών Edge AI**
- Αξιολόγηση εφικτότητας Edge AI για έργα
- Επιλογή κατάλληλων μοντέλων και πλαισίων
- Σχεδιασμός κλιμακούμενων τοπικών λύσεων AI

---

## 🗺️ Δομή Εργαστηρίου

### Επισκόπηση Συνεδριών (6 Συνεδρίες × 30 Λεπτά = 3 Ώρες)

| Συνεδρία | Θέμα | Εστίαση | Διάρκεια |
|----------|-------|--------|----------|
| **1** | Ξεκινώντας με το Foundry Local | Εγκατάσταση, επικύρωση, πρώτες ολοκληρώσεις | 30 λεπτά |
| **2** | Δημιουργία Λύσεων AI με RAG | Σχεδιασμός προτροπών, ενσωματώσεις, αξιολόγηση | 30 λεπτά |
| **3** | Ανοιχτά Μοντέλα | Ανακάλυψη μοντέλων, δοκιμές, επιλογή | 30 λεπτά |
| **4** | Μοντέλα Αιχμής | SLM έναντι LLM, βελτιστοποίηση, πλαίσια | 30 λεπτά |
| **5** | Πράκτορες με Τεχνητή Νοημοσύνη | Σχεδιασμός πρακτόρων, συντονισμός, μνήμη | 30 λεπτά |
| **6** | Μοντέλα ως Εργαλεία | Δρομολόγηση, αλυσίδες, στρατηγικές κλιμάκωσης | 30 λεπτά |

---

## 🚀 Γρήγορη Εκκίνηση

### Προαπαιτούμενα

**Απαιτήσεις Συστήματος:**
- **Λειτουργικό Σύστημα**: Windows 10/11, macOS 11+, ή Linux (Ubuntu 20.04+)
- **RAM**: Ελάχιστο 8GB, συνιστάται 16GB+
- **Αποθηκευτικός Χώρος**: 10GB+ ελεύθερος χώρος για μοντέλα
- **CPU**: Σύγχρονος επεξεργαστής με υποστήριξη AVX2
- **GPU** (προαιρετικό): Συμβατό με CUDA ή Qualcomm NPU για επιτάχυνση

**Απαιτήσεις Λογισμικού:**
- **Python 3.8+** ([Λήψη](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Οδηγός Εγκατάστασης](../../../Workshop))
- **Git** ([Λήψη](https://git-scm.com/downloads))
- **Visual Studio Code** (συνιστάται) ([Λήψη](https://code.visualstudio.com/))

### Ρύθμιση σε 3 Βήματα

#### 1. Εγκατάσταση Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Επικύρωση Εγκατάστασης:**
```bash
foundry --version
foundry service status
```

**Βεβαιωθείτε ότι το Azure AI Foundry Local λειτουργεί με σταθερή θύρα**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Επικύρωση λειτουργίας:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Εύρεση Διαθέσιμων Μοντέλων**
Για να δείτε ποια μοντέλα είναι διαθέσιμα στην τοπική σας εγκατάσταση Foundry, μπορείτε να κάνετε ερώτηση στο endpoint μοντέλων:

```bash
# cmd/bash/powershell
foundry model list
```

Χρησιμοποιώντας Web Endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Κλωνοποίηση Αποθετηρίου & Εγκατάσταση Εξαρτήσεων

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Εκτέλεση Πρώτου Δείγματος

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Επιτυχία!** Θα πρέπει να δείτε μια ροή απάντησης σχετικά με το edge AI.

---

## 📦 Πόροι Εργαστηρίου

### Δείγματα Python

Προοδευτικά παραδείγματα που δείχνουν κάθε έννοια:

| Συνεδρία | Δείγμα | Περιγραφή | Χρόνος Εκτέλεσης |
|----------|--------|-----------|------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Βασική & ροή συνομιλίας | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG με ενσωματώσεις | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Αξιολόγηση ποιότητας RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Δοκιμή πολλαπλών μοντέλων | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Σύγκριση SLM έναντι LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Σύστημα πολλαπλών πρακτόρων | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Δρομολόγηση βάσει προθέσεων | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Πολυβηματική αλυσίδα | ~60s |

### Σημειωματάρια Jupyter

Διαδραστική εξερεύνηση με εξηγήσεις και οπτικοποιήσεις:

| Συνεδρία | Σημειωματάριο | Περιγραφή | Δυσκολία |
|----------|--------------|-----------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Βασικά συνομιλίας & ροή | ⭐ Αρχάριος |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Δημιουργία συστήματος RAG | ⭐⭐ Μεσαίος |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Αξιολόγηση ποιότητας RAG | ⭐⭐ Μεσαίος |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Δοκιμή μοντέλων | ⭐⭐ Μεσαίος |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Σύγκριση μοντέλων | ⭐⭐ Μεσαίος |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Συντονισμός πρακτόρων | ⭐⭐⭐ Προχωρημένος |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Δρομολόγηση προθέσεων | ⭐⭐⭐ Προχωρημένος |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Συντονισμός αλυσίδας | ⭐⭐⭐ Προχωρημένος |

### Τεκμηρίωση

Ολοκληρωμένοι οδηγοί και αναφορές:

| Έγγραφο | Περιγραφή | Χρήση Όταν |
|---------|-----------|------------|
| [QUICK_START.md](./QUICK_START.md) | Οδηγός γρήγορης ρύθμισης | Ξεκινώντας από την αρχή |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Φύλλο αναφοράς εντολών & API | Χρειάζεστε γρήγορες απαντήσεις |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Πρότυπα SDK & παραδείγματα | Γράφοντας κώδικα |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Οδηγός μεταβλητών περιβάλλοντος | Ρύθμιση δειγμάτων |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Βελτιώσεις δειγμάτων | Κατανόηση αλλαγών |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Οδηγός μετανάστευσης | Αναβάθμιση κώδικα |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Συνηθισμένα προβλήματα & λύσεις | Εντοπισμός σφαλμάτων |

---

## 🎓 Συστάσεις Διαδρομής Μάθησης

###
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Ρόλοι πρακτόρων, μνήμη, εργαλεία, ορχήστρα |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Δρομολόγηση, αλυσίδωση, κλιμάκωση προς Azure |

Κάθε αρχείο συνεδρίας περιλαμβάνει: περίληψη, μαθησιακούς στόχους, ροή επίδειξης 30 λεπτών, αρχικό έργο, λίστα ελέγχου επικύρωσης, αντιμετώπιση προβλημάτων και αναφορές στο επίσημο Foundry Local Python SDK.

### Δείγματα Scripts

Εγκατάσταση εξαρτήσεων εργαστηρίου (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Αν εκτελείτε την υπηρεσία Foundry Local σε διαφορετικό μηχάνημα (Windows) ή VM από macOS, εξαγάγετε το endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Συνεδρία | Script(s) | Περιγραφή |
|----------|-----------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Εκκίνηση υπηρεσίας & συνομιλία με ροή |
| 2 | `samples/session02/rag_pipeline.py` | Ελάχιστο RAG (ενσωματώσεις στη μνήμη) |
|   | `samples/session02/rag_eval_ragas.py` | Αξιολόγηση RAG με μετρικές ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Αξιολόγηση καθυστέρησης & απόδοσης πολλαπλών μοντέλων |
| 4 | `samples/session04/model_compare.py` | Σύγκριση SLM vs LLM (καθυστέρηση & δείγματα εξόδου) |
| 5 | `samples/session05/agents_orchestrator.py` | Δύο πράκτορες: έρευνα → συντακτική διαδικασία |
| 6 | `samples/session06/models_router.py` | Επίδειξη δρομολόγησης βάσει πρόθεσης |
|   | `samples/session06/models_pipeline.py` | Αλυσίδα σχεδίου/εκτέλεσης/βελτίωσης πολλαπλών βημάτων |

### Μεταβλητές Περιβάλλοντος (Κοινές για Δείγματα)

| Μεταβλητή | Σκοπός | Παράδειγμα |
|-----------|--------|------------|
| `FOUNDRY_LOCAL_ALIAS` | Προεπιλεγμένο ψευδώνυμο μοντέλου για βασικά δείγματα | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Ρητό SLM vs μεγαλύτερο μοντέλο για σύγκριση | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Λίστα ψευδωνύμων για αξιολόγηση | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Επαναλήψεις αξιολόγησης ανά μοντέλο | `3` |
| `BENCH_PROMPT` | Ερώτημα που χρησιμοποιείται στην αξιολόγηση | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Μοντέλο ενσωμάτωσης sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Υπέρβαση ερωτήματος δοκιμής για τον αγωγό RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Υπέρβαση ερωτήματος για τον αγωγό πρακτόρων | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Ψευδώνυμο μοντέλου για τον πράκτορα έρευνας | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Ψευδώνυμο μοντέλου για τον πράκτορα συντάκτη (μπορεί να διαφέρει) | `gpt-oss-20b` |
| `SHOW_USAGE` | Όταν είναι `1`, εκτυπώνει τη χρήση token ανά ολοκλήρωση | `1` |
| `RETRY_ON_FAIL` | Όταν είναι `1`, επαναλαμβάνει μία φορά σε προσωρινά σφάλματα συνομιλίας | `1` |
| `RETRY_BACKOFF` | Δευτερόλεπτα αναμονής πριν την επανάληψη | `1.0` |

Αν μια μεταβλητή δεν έχει οριστεί, τα scripts επιστρέφουν σε λογικές προεπιλογές. Για δείγματα με ένα μοντέλο, συνήθως χρειάζεστε μόνο το `FOUNDRY_LOCAL_ALIAS`.

### Βοηθητική Μονάδα

Όλα τα δείγματα μοιράζονται τώρα ένα βοηθητικό `samples/workshop_utils.py` που παρέχει:

* Δημιουργία cache `FoundryLocalManager` + OpenAI client
* Βοηθητικό `chat_once()` με προαιρετική επανάληψη + εκτύπωση χρήσης
* Απλή αναφορά χρήσης token (ενεργοποίηση μέσω `SHOW_USAGE=1`)

Αυτό μειώνει την επανάληψη και αναδεικνύει τις βέλτιστες πρακτικές για αποδοτική τοπική ορχήστρα μοντέλων.

## Προαιρετικές Βελτιώσεις (Διασυνεδριακές)

| Θέμα | Βελτίωση | Συνεδρίες | Env / Toggle |
|------|----------|-----------|--------------|
| Ντετερμινισμός | Σταθερή θερμοκρασία + σταθερά σύνολα ερωτημάτων | 1–6 | Ορίστε `temperature=0`, `top_p=1` |
| Ορατότητα Χρήσης Token | Συνεπής διδασκαλία κόστους/αποδοτικότητας | 1–6 | `SHOW_USAGE=1` |
| Ροή Πρώτου Token | Μετρική αντιληπτής καθυστέρησης | 1,3,4,6 | `BENCH_STREAM=1` (αξιολόγηση) |
| Ανθεκτικότητα Επανάληψης | Αντιμετωπίζει προσωρινή καθυστέρηση εκκίνησης | Όλες | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Πράκτορες Πολλαπλών Μοντέλων | Εξειδίκευση ρόλων | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Προσαρμοστική Δρομολόγηση | Πρόθεση + ευρετική κόστους | 6 | Επέκταση δρομολογητή με λογική κλιμάκωσης |
| Μνήμη Vector | Μακροχρόνια σημασιολογική ανάκληση | 2,5,6 | Ενσωμάτωση FAISS/Chroma embedding index |
| Εξαγωγή Ιχνών | Έλεγχος & αξιολόγηση | 2,5,6 | Προσθήκη JSON γραμμών ανά βήμα |
| Ποιοτικά Κριτήρια | Ποιοτική παρακολούθηση | 3–6 | Δευτερεύοντα ερωτήματα βαθμολόγησης |
| Δοκιμές Καπνού | Γρήγορη επικύρωση πριν το εργαστήριο | Όλες | `python Workshop/tests/smoke.py` |

### Ντετερμινιστική Γρήγορη Εκκίνηση

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Αναμένετε σταθερό αριθμό token σε επαναλαμβανόμενες πανομοιότυπες εισόδους.

### Αξιολόγηση RAG (Συνεδρία 2)

Χρησιμοποιήστε το `rag_eval_ragas.py` για να υπολογίσετε τη συνάφεια απαντήσεων, την αξιοπιστία και την ακρίβεια περιεχομένου σε ένα μικρό συνθετικό σύνολο δεδομένων:

```powershell
python samples/session02/rag_eval_ragas.py
```

Επεκτείνετε παρέχοντας ένα μεγαλύτερο JSONL με ερωτήσεις, περιεχόμενα και αλήθειες βάσης και στη συνέχεια μετατρέψτε το σε ένα `Dataset` του Hugging Face.

## Παράρτημα Ακρίβειας Εντολών CLI

Το εργαστήριο χρησιμοποιεί μόνο τεκμηριωμένες / σταθερές εντολές CLI του Foundry Local.

### Αναφερόμενες Σταθερές Εντολές

| Κατηγορία | Εντολή | Σκοπός |
|-----------|--------|--------|
| Βασικές | `foundry --version` | Εμφάνιση εγκατεστημένης έκδοσης |
| Βασικές | `foundry init` | Αρχικοποίηση ρυθμίσεων |
| Υπηρεσία | `foundry service start` | Εκκίνηση τοπικής υπηρεσίας (αν δεν είναι αυτόματη) |
| Υπηρεσία | `foundry status` | Εμφάνιση κατάστασης υπηρεσίας |
| Μοντέλα | `foundry model list` | Λίστα καταλόγου / διαθέσιμων μοντέλων |
| Μοντέλα | `foundry model download <alias>` | Λήψη βαρών μοντέλου στην cache |
| Μοντέλα | `foundry model run <alias>` | Εκκίνηση (φόρτωση) μοντέλου τοπικά; συνδυασμός με `--prompt` για μία φορά |
| Μοντέλα | `foundry model unload <alias>` / `foundry model stop <alias>` | Αποφόρτωση μοντέλου από τη μνήμη (αν υποστηρίζεται) |
| Cache | `foundry cache list` | Λίστα μοντέλων στην cache |
| Σύστημα | `foundry system info` | Στιγμιότυπο δυνατοτήτων υλικού & επιτάχυνσης |
| Σύστημα | `foundry system gpu-info` | Διαγνωστικές πληροφορίες GPU |
| Ρυθμίσεις | `foundry config list` | Εμφάνιση τρεχουσών τιμών ρυθμίσεων |
| Ρυθμίσεις | `foundry config set <key> <value>` | Ενημέρωση ρυθμίσεων |

### Μοτίβο Εντολής Μίας Φοράς

Αντί για την παρωχημένη υποεντολή `model chat`, χρησιμοποιήστε:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Αυτό εκτελεί έναν κύκλο ερωτήματος/απάντησης και στη συνέχεια τερματίζει.

### Αφαιρεθέντα / Αποφευγμένα Μοτίβα

| Παρωχημένα / Μη τεκμηριωμένα | Αντικατάσταση / Οδηγίες |
|-----------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Χρησιμοποιήστε απλό `foundry model list` + πρόσφατη δραστηριότητα / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Χρησιμοποιήστε το script αξιολόγησης Python + εργαλεία OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Αξιολόγηση & Τηλεμετρία

- Καθυστέρηση, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- Καθυστέρηση πρώτου token (ροή): ορίστε `BENCH_STREAM=1`
- Χρήση πόρων: Εργαλεία OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Καθώς σταθεροποιούνται νέες εντολές τηλεμετρίας CLI, μπορούν να ενσωματωθούν με ελάχιστες αλλαγές στα markdowns συνεδριών.

### Αυτόματη Φρουρά Lint

Ένας αυτόματος linter αποτρέπει την επανεισαγωγή παρωχημένων μοτίβων CLI μέσα σε μπλοκ κώδικα markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Παρωχημένα μοτίβα μπλοκάρονται μέσα σε περιφραγμένα μπλοκ κώδικα.

Συνιστώμενες αντικαταστάσεις:
| Παρωχημένα | Αντικατάσταση |
|------------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script αξιολόγησης + εργαλεία συστήματος |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Εκτέλεση τοπικά:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` εκτελείται σε κάθε push & PR.

Προαιρετικό hook πριν την commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Γρήγορος Πίνακας Μετάβασης CLI → SDK

| Εργασία | Εντολή CLI | Ισοδύναμο SDK (Python) | Σημειώσεις |
|---------|------------|------------------------|------------|
| Εκτέλεση μοντέλου μία φορά (ερώτημα) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Το SDK εκκινεί την υπηρεσία & την cache αυτόματα |
| Λήψη (cache) μοντέλου | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Ο διαχειριστής επιλέγει την καλύτερη παραλλαγή αν το ψευδώνυμο αντιστοιχεί σε πολλαπλές εκδόσεις |
| Λίστα καταλόγου | `foundry model list` | `# use manager for each alias or maintain known list` | Το CLI συγκεντρώνει; το SDK προς το παρόν ανά ψευδώνυμο |
| Λίστα μοντέλων στην cache | `foundry cache list` | `manager.list_cached_models()` | Μετά την αρχικοποίηση του διαχειριστή (οποιοδήποτε ψευδώνυμο) |
| Ενεργοποίηση επιτάχυνσης GPU | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Η ρύθμιση είναι εξωτερική παρενέργεια |
| Λήψη URL endpoint | (έμμεσα) | `manager.endpoint` | Χρησιμοποιείται για τη δημιουργία OpenAI-compatible client |
| Θέρμανση μοντέλου | `foundry model run <alias>` και πρώτο ερώτημα | `chat_once(alias, messages=[...])` (utility) | Τα βοηθητικά προγράμματα χειρίζονται την αρχική καθυστέρηση |
| Μέτρηση καθυστέρησης | `python benchmark_oss_models.py` | `import benchmark_oss_models` (ή νέο script εξαγωγής) | Προτιμήστε το script για συνεπείς μετρήσεις |
| Διακοπή / αποφόρτωση μοντέλου | `foundry model unload <alias>` | (Δεν εκτίθεται – επανεκκίνηση υπηρεσίας / διαδικασίας) | Συνήθως δεν απαιτείται για τη ροή του εργαστηρίου |
| Ανάκτηση χρήσης token | (προβολή εξόδου) | `resp.usage.total_tokens` | Παρέχεται αν το backend επιστρέφει αντικείμενο χρήσης |

## Εξαγωγή Markdown Αξιολόγησης

Χρησιμοποιήστε το script `Workshop/scripts/export_benchmark_markdown.py` για να εκτελέσετε μια νέα αξιολόγηση (ίδια λογική με το `samples/session03/benchmark_oss_models.py`) και να δημιουργήσετε έναν πίνακα Markdown φιλικό προς το GitHub και ακατέργαστο JSON.

### Παράδειγμα

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Δημιουργημένα αρχεία:
| Αρχείο | Περιεχόμενο |
|--------|-------------|
| `benchmark_report.md` | Πίνακας Markdown + υποδείξεις ερμηνείας |
| `benchmark_report.json` | Ακατέργαστος πίνακας μετρικών (για παρακολούθηση τάσεων) |

Ορίστε `BENCH_STREAM=1` στο περιβάλλον για να συμπεριλάβετε καθυστέρηση πρώτου token αν υποστηρίζεται.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.