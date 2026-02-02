# Οδηγός Ενσωμάτωσης Open WebUI + Foundry Local

Αυτός ο οδηγός δείχνει πώς να συνδέσετε το Open WebUI με το Microsoft Foundry Local για μια επαγγελματική διεπαφή τύπου ChatGPT, που τροφοδοτείται από τα τοπικά μοντέλα AI σας.

## Επισκόπηση

Το Open WebUI προσφέρει μια σύγχρονη, φιλική προς τον χρήστη διεπαφή συνομιλίας που μπορεί να συνδεθεί με οποιοδήποτε API συμβατό με OpenAI. Με τη σύνδεσή του στο Foundry Local, αποκτάτε:

- **Επαγγελματική Διεπαφή**: Διεπαφή τύπου ChatGPT με μοντέρνο σχεδιασμό
- **Τοπική Ιδιωτικότητα**: Όλη η επεξεργασία γίνεται στη συσκευή σας
- **Εναλλαγή Μοντέλων**: Εύκολη εναλλαγή μεταξύ διαφορετικών τοπικών μοντέλων
- **Ιστορικό Συνομιλιών**: Επίμονη αποθήκευση ιστορικού και πλαισίου συνομιλιών
- **Ανάλυση Αρχείων**: Δυνατότητες επεξεργασίας εγγράφων και αρχείων
- **Προσαρμοσμένες Προσωπικότητες**: Προσαρμογή συστημικών προτροπών και ρόλων

## Προαπαιτούμενα

### Απαιτούμενο Λογισμικό

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Φόρτωση Μοντέλου

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Γρήγορη Ρύθμιση (Συνιστάται)

### Βήμα 1: Εκτέλεση Open WebUI με Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Βήμα 2: Αρχική Ρύθμιση

1. **Άνοιγμα Περιηγητή**: Μεταβείτε στη διεύθυνση `http://localhost:3000`
2. **Δημιουργία Λογαριασμού**: Ρυθμίστε τον διαχειριστή χρήστη (ο πρώτος χρήστης γίνεται διαχειριστής)
3. **Επαλήθευση Σύνδεσης**: Τα μοντέλα θα εμφανιστούν αυτόματα στο αναπτυσσόμενο μενού

### Βήμα 3: Δοκιμή Σύνδεσης

1. Επιλέξτε το μοντέλο σας από το αναπτυσσόμενο μενού (π.χ., "phi-4-mini")
2. Πληκτρολογήστε ένα δοκιμαστικό μήνυμα: "Γεια! Μπορείς να συστηθείς;"
3. Θα δείτε μια ροή απάντησης από το τοπικό σας μοντέλο

## Προχωρημένη Ρύθμιση

### Μεταβλητές Περιβάλλοντος

| Μεταβλητή | Σκοπός | Προεπιλογή | Παράδειγμα |
|-----------|--------|------------|------------|
| `OPENAI_API_BASE_URL` | Σημείο πρόσβασης Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Κλειδί API (απαιτείται αλλά δεν χρησιμοποιείται τοπικά) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Κλειδί κρυπτογράφησης συνεδρίας | αυτόματα παραγόμενο | `your-secret-key` |
| `ENABLE_SIGNUP` | Επιτρέπει την εγγραφή νέων χρηστών | `True` | `False` |

### Χειροκίνητη Ρύθμιση (Εναλλακτική)

Αν οι μεταβλητές περιβάλλοντος δεν λειτουργούν, ρυθμίστε χειροκίνητα:

1. **Άνοιγμα Ρυθμίσεων**: Κάντε κλικ στο εικονίδιο ρυθμίσεων (γρανάζι)
2. **Μετάβαση στις Συνδέσεις**: Ρυθμίσεις → Συνδέσεις → OpenAI
3. **Ρύθμιση Λεπτομερειών API**:
   - Βασική Διεύθυνση API: `http://host.docker.internal:51211/v1`
   - Κλειδί API: `foundry-local-key` (οποιαδήποτε τιμή λειτουργεί)
4. **Αποθήκευση και Δοκιμή**: Κάντε κλικ στο "Αποθήκευση" και δοκιμάστε με ένα μοντέλο

### Επίμονη Αποθήκευση Δεδομένων

Για να αποθηκεύσετε συνομιλίες και ρυθμίσεις:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Επίλυση Προβλημάτων

### Προβλήματα Σύνδεσης

**Πρόβλημα**: "Η σύνδεση απορρίφθηκε" ή τα μοντέλα δεν φορτώνονται

**Λύσεις**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Το Μοντέλο Δεν Εμφανίζεται

**Πρόβλημα**: Το Open WebUI δεν εμφανίζει μοντέλα στο αναπτυσσόμενο μενού

**Βήματα Εντοπισμού Σφαλμάτων**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Διόρθωση**: Βεβαιωθείτε ότι το μοντέλο έχει φορτωθεί σωστά:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Προβλήματα Δικτύου Docker

**Πρόβλημα**: Το `host.docker.internal` δεν επιλύεται

**Λύση για Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Εναλλακτική**: Βρείτε τη διεύθυνση IP του μηχανήματός σας:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Προβλήματα Απόδοσης

**Αργές Απαντήσεις**:
1. Ελέγξτε αν το μοντέλο χρησιμοποιεί επιτάχυνση GPU: `foundry service ps`
2. Βεβαιωθείτε ότι υπάρχουν επαρκείς πόροι συστήματος (RAM/μνήμη GPU)
3. Σκεφτείτε να χρησιμοποιήσετε ένα μικρότερο μοντέλο για δοκιμές

**Προβλήματα Μνήμης**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Οδηγός Χρήσης

### Βασική Συνομιλία

1. **Επιλογή Μοντέλου**: Επιλέξτε από το αναπτυσσόμενο μενού (εμφανίζει μοντέλα Foundry Local)
2. **Πληκτρολόγηση Μηνύματος**: Χρησιμοποιήστε το πεδίο κειμένου στο κάτω μέρος
3. **Αποστολή**: Πατήστε Enter ή κάντε κλικ στο κουμπί Αποστολή
4. **Προβολή Απάντησης**: Δείτε την απάντηση σε πραγματικό χρόνο

### Προχωρημένες Δυνατότητες

**Ανέβασμα Αρχείων**:
1. Κάντε κλικ στο εικονίδιο συνδετήρα
2. Ανεβάστε έγγραφο (PDF, TXT, κ.λπ.)
3. Κάντε ερωτήσεις σχετικά με το περιεχόμενο
4. Το μοντέλο θα αναλύσει και θα απαντήσει βάσει του εγγράφου

**Προσαρμοσμένες Συστημικές Προτροπές**:
1. Ρυθμίσεις → Εξατομίκευση
2. Ορίστε προσαρμοσμένη συστημική προτροπή
3. Δημιουργεί συνεπή προσωπικότητα/συμπεριφορά AI

**Διαχείριση Συνομιλιών**:
- **Νέα Συνομιλία**: Κάντε κλικ στο "+" για να ξεκινήσετε νέα συνομιλία
- **Ιστορικό Συνομιλιών**: Πρόσβαση σε προηγούμενες συνομιλίες από την πλαϊνή μπάρα
- **Εξαγωγή**: Κατεβάστε το ιστορικό συνομιλιών ως κείμενο/JSON

**Σύγκριση Μοντέλων**:
1. Ανοίξτε πολλαπλές καρτέλες περιηγητή στο ίδιο Open WebUI
2. Επιλέξτε διαφορετικά μοντέλα σε κάθε καρτέλα
3. Συγκρίνετε απαντήσεις στις ίδιες προτροπές

### Μοτίβα Ενσωμάτωσης

**Ροή Εργασίας Ανάπτυξης**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Ανάπτυξη σε Παραγωγή

### Ασφαλής Ρύθμιση

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Ρύθμιση Πολλαπλών Χρηστών

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Παρακολούθηση και Καταγραφή

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Καθαρισμός

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Επόμενα Βήματα

### Ιδέες Βελτίωσης

1. **Προσαρμοσμένα Μοντέλα**: Προσθέστε τα δικά σας μοντέλα που έχουν προσαρμοστεί στο Foundry Local
2. **Ενσωμάτωση API**: Συνδέστε εξωτερικά APIs μέσω λειτουργιών του Open WebUI
3. **Επεξεργασία Εγγράφων**: Ρυθμίστε προηγμένες ροές RAG
4. **Πολυτροπικότητα**: Ρυθμίστε μοντέλα όρασης για ανάλυση εικόνων

### Σκέψεις Κλιμάκωσης

- **Εξισορρόπηση Φορτίου**: Πολλαπλές παρουσίες Foundry Local πίσω από αντίστροφο proxy
- **Δρομολόγηση Μοντέλων**: Διαφορετικά μοντέλα για διαφορετικές περιπτώσεις χρήσης
- **Διαχείριση Πόρων**: Βελτιστοποίηση μνήμης GPU για ταυτόχρονους χρήστες
- **Στρατηγική Αντιγράφων Ασφαλείας**: Τακτική δημιουργία αντιγράφων ασφαλείας δεδομένων συνομιλιών και ρυθμίσεων

## Αναφορές

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

