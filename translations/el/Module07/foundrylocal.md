# Foundry Local σε Windows & Mac

Αυτός ο οδηγός σας βοηθά να εγκαταστήσετε, να εκτελέσετε και να ενσωματώσετε το Microsoft Foundry Local σε Windows και Mac. Όλα τα βήματα και οι εντολές έχουν επικυρωθεί σύμφωνα με τα έγγραφα του Microsoft Learn.

- Ξεκινήστε: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Αρχιτεκτονική: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Αναφορά CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Ενσωμάτωση SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Συμπίεση μοντέλων HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Τοπικό vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Εγκατάσταση / Αναβάθμιση σε Windows

- Εγκατάσταση:
```cmd
winget install Microsoft.FoundryLocal
```
- Αναβάθμιση:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Έλεγχος έκδοσης:
```cmd
foundry --version
```
     
**Εγκατάσταση / Mac**

**MacOS**: 
Ανοίξτε ένα τερματικό και εκτελέστε την παρακάτω εντολή:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Βασικά CLI (Τρεις Κατηγορίες)

- Μοντέλο:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Υπηρεσία:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Σημειώσεις:
- Η υπηρεσία εκθέτει ένα REST API συμβατό με OpenAI. Η θύρα του endpoint εκχωρείται δυναμικά· χρησιμοποιήστε `foundry service status` για να την ανακαλύψετε.
- Χρησιμοποιήστε τα SDKs για ευκολία· αυτά χειρίζονται την ανακάλυψη του endpoint αυτόματα όπου υποστηρίζεται.

## 3) Ανακάλυψη Τοπικού Endpoint (Δυναμική Θύρα)

Το Foundry Local εκχωρεί μια δυναμική θύρα κάθε φορά που ξεκινά η υπηρεσία:
```cmd
foundry service status
```
Χρησιμοποιήστε το αναφερόμενο `http://localhost:<PORT>` ως `base_url` με συμβατά μονοπάτια OpenAI (για παράδειγμα, `/v1/chat/completions`).

## 4) Γρήγορη Δοκιμή μέσω OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Αναφορές:
- Ενσωμάτωση SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Φέρτε το Δικό σας Μοντέλο (Συμπίεση με Olive)

Αν χρειάζεστε ένα μοντέλο που δεν υπάρχει στον κατάλογο, συμπιέστε το σε ONNX για το Foundry Local χρησιμοποιώντας το Olive.

Γενική ροή (δείτε τα έγγραφα για βήματα):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Έγγραφα:
- Συμπίεση BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Αντιμετώπιση Προβλημάτων

- Έλεγχος κατάστασης υπηρεσίας και αρχείων καταγραφής:
```cmd
foundry service status
foundry service diag
```
- Εκκαθάριση ή μετακίνηση cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Ενημέρωση στην τελευταία προεπισκόπηση:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Σχετική Εμπειρία Ανάπτυξης σε Windows

- Επιλογές τοπικής vs cloud AI σε Windows, συμπεριλαμβανομένων των Foundry Local και Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit με Foundry Local (χρησιμοποιήστε `foundry service status` για να λάβετε το URL του chat endpoint):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Επόμενος Windows Developer](./windowdeveloper.md)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.