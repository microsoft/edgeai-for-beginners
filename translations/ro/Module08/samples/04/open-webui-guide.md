# Ghid de Integrare Open WebUI + Foundry Local

Acest ghid explică cum să conectezi Open WebUI la Microsoft Foundry Local pentru o interfață profesională asemănătoare ChatGPT, alimentată de modelele tale AI locale.

## Prezentare Generală

Open WebUI oferă o interfață modernă și prietenoasă pentru chat, care se poate conecta la orice API compatibil cu OpenAI. Prin conectarea la Foundry Local, obții:

- **Interfață Profesională**: O interfață asemănătoare ChatGPT, cu un design modern
- **Confidențialitate Locală**: Toate procesările au loc pe dispozitivul tău
- **Schimbare de Model**: Comutare ușoară între diferite modele locale
- **Istoric Conversații**: Istoric de chat persistent și context
- **Încărcare Fișiere**: Capacități de analiză a documentelor și procesare fișiere
- **Personaje Personalizate**: Promptere de sistem și personalizare de rol

## Cerințe Prealabile

### Software Necesar

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Încărcarea unui Model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Configurare Rapidă (Recomandată)

### Pasul 1: Rulează Open WebUI cu Docker

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

### Pasul 2: Configurare Inițială

1. **Deschide Browserul**: Accesează `http://localhost:3000`
2. **Creează Cont**: Configurează utilizatorul admin (primul utilizator devine admin)
3. **Verifică Conexiunea**: Modelele ar trebui să apară automat în meniul dropdown

### Pasul 3: Testează Conexiunea

1. Selectează modelul din meniul dropdown (ex.: "phi-4-mini")
2. Scrie un mesaj de test: "Salut! Poți să te prezinți?"
3. Ar trebui să vezi un răspuns transmis în timp real de modelul local

## Configurare Avansată

### Variabile de Mediu

| Variabilă | Scop | Implicit | Exemplu |
|-----------|------|----------|---------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Cheie API (necesară, dar neutilizată local) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Cheie de criptare sesiune | generată automat | `your-secret-key` |
| `ENABLE_SIGNUP` | Permite înregistrarea de utilizatori noi | `True` | `False` |

### Configurare Manuală (Alternativă)

Dacă variabilele de mediu nu funcționează, configurează manual:

1. **Deschide Setări**: Click pe Setări (iconița roată)
2. **Navighează la Conexiuni**: Setări → Conexiuni → OpenAI
3. **Setează Detaliile API**:
   - URL Bază API: `http://host.docker.internal:51211/v1`
   - Cheie API: `foundry-local-key` (orice valoare funcționează)
4. **Salvează și Testează**: Click pe "Salvează", apoi testează cu un model

### Stocare Persistentă a Datelor

Pentru a păstra conversațiile și setările:

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

## Depanare

### Probleme de Conexiune

**Problemă**: "Conexiune refuzată" sau modelele nu se încarcă

**Soluții**:
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

### Modelul Nu Apare

**Problemă**: Open WebUI nu afișează modele în meniul dropdown

**Pași de Depanare**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Rezolvare**: Asigură-te că modelul este încărcat corect:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Probleme de Rețea Docker

**Problemă**: `host.docker.internal` nu se rezolvă

**Soluție Windows**:
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

**Alternativă**: Găsește IP-ul mașinii tale:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Probleme de Performanță

**Răspunsuri Lente**:
1. Verifică dacă modelul folosește accelerare GPU: `foundry service ps`
2. Asigură-te că ai suficiente resurse de sistem (RAM/memorie GPU)
3. Ia în considerare utilizarea unui model mai mic pentru testare

**Probleme de Memorie**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Ghid de Utilizare

### Chat de Bază

1. **Selectează Modelul**: Alege din meniul dropdown (afișează modelele Foundry Local)
2. **Scrie Mesajul**: Folosește câmpul de text din partea de jos
3. **Trimite**: Apasă Enter sau click pe butonul de trimitere
4. **Vizualizează Răspunsul**: Vezi răspunsul transmis în timp real

### Funcționalități Avansate

**Încărcare Fișiere**:
1. Click pe iconița agrafă
2. Încarcă documentul (PDF, TXT, etc.)
3. Pune întrebări despre conținut
4. Modelul va analiza și răspunde pe baza documentului

**Promptere Personalizate**:
1. Setări → Personalizare
2. Configurează un prompt de sistem personalizat
3. Creează o personalitate/comportament AI consistent

**Gestionarea Conversațiilor**:
- **Chat Nou**: Click pe "+" pentru a începe o conversație nouă
- **Istoric Chat**: Accesează conversațiile anterioare din bara laterală
- **Export**: Descarcă istoricul conversațiilor ca text/JSON

**Comparare Modele**:
1. Deschide mai multe tab-uri de browser cu același Open WebUI
2. Selectează modele diferite în fiecare tab
3. Compară răspunsurile la aceleași promptere

### Modele de Integrare

**Flux de Lucru pentru Dezvoltare**:
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

## Implementare în Producție

### Configurare Securizată

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

### Configurare Multi-Utilizator

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

### Monitorizare și Logare

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Curățare

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

## Pași Următori

### Idei de Îmbunătățire

1. **Modele Personalizate**: Adaugă modele proprii fine-tunate în Foundry Local
2. **Integrare API**: Conectează-te la API-uri externe prin funcțiile Open WebUI
3. **Procesare Documente**: Configurează pipeline-uri avansate RAG
4. **Multi-Modal**: Configurează modele de viziune pentru analiza imaginilor

### Considerații de Scalare

- **Balansare Sarcini**: Instanțe multiple Foundry Local în spatele unui proxy invers
- **Rutare Modele**: Modele diferite pentru cazuri de utilizare diferite
- **Gestionare Resurse**: Optimizare memorie GPU pentru utilizatori simultani
- **Strategie de Backup**: Backup regulat al datelor conversațiilor și configurațiilor

## Referințe

- [Documentație Open WebUI](https://docs.openwebui.com/)
- [Repository GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Documentație Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Ghid Instalare Docker](https://docs.docker.com/get-docker/)

---

