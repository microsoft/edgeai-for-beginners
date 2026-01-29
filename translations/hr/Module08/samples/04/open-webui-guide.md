# Vodič za integraciju Open WebUI + Foundry Local

Ovaj vodič pokazuje kako povezati Open WebUI s Microsoft Foundry Local za profesionalno sučelje nalik ChatGPT-u koje koristi vaše lokalne AI modele.

## Pregled

Open WebUI pruža moderno, korisnički prilagođeno sučelje za chat koje se može povezati s bilo kojim API-jem kompatibilnim s OpenAI-jem. Povezivanjem s Foundry Local dobivate:

- **Profesionalno sučelje**: Sučelje nalik ChatGPT-u s modernim dizajnom
- **Lokalna privatnost**: Sva obrada odvija se na vašem uređaju
- **Prebacivanje modela**: Jednostavno prebacivanje između različitih lokalnih modela
- **Povijest razgovora**: Trajna povijest chata i konteksta
- **Učitavanje datoteka**: Analiza dokumenata i obrada datoteka
- **Prilagođene osobnosti**: Sustavni upiti i prilagodba uloga

## Preduvjeti

### Potreban softver

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Učitavanje modela

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Brza postavka (preporučeno)

### Korak 1: Pokrenite Open WebUI s Dockerom

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

### Korak 2: Početna postavka

1. **Otvorite preglednik**: Idite na `http://localhost:3000`
2. **Kreirajte račun**: Postavite admin korisnika (prvi korisnik postaje admin)
3. **Provjerite vezu**: Modeli bi se trebali automatski pojaviti u padajućem izborniku

### Korak 3: Testirajte vezu

1. Odaberite svoj model iz padajućeg izbornika (npr. "phi-4-mini")
2. Unesite testnu poruku: "Pozdrav! Možete li se predstaviti?"
3. Trebali biste vidjeti odgovor u stvarnom vremenu od vašeg lokalnog modela

## Napredna konfiguracija

### Varijable okruženja

| Varijabla | Svrha | Zadano | Primjer |
|-----------|-------|--------|---------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API ključ (potreban, ali se lokalno ne koristi) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Ključ za enkripciju sesije | automatski generiran | `your-secret-key` |
| `ENABLE_SIGNUP` | Omogućuje registraciju novih korisnika | `True` | `False` |

### Ručna konfiguracija (alternativa)

Ako varijable okruženja ne rade, konfigurirajte ručno:

1. **Otvorite postavke**: Kliknite na Postavke (ikona zupčanika)
2. **Idite na Povezivanja**: Postavke → Povezivanja → OpenAI
3. **Postavite API detalje**:
   - API osnovni URL: `http://host.docker.internal:51211/v1`
   - API ključ: `foundry-local-key` (bilo koja vrijednost radi)
4. **Spremite i testirajte**: Kliknite "Spremi" i testirajte s modelom

### Trajna pohrana podataka

Za trajnu pohranu razgovora i postavki:

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

## Rješavanje problema

### Problemi s vezom

**Problem**: "Veza odbijena" ili modeli se ne učitavaju

**Rješenja**:
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

### Model se ne pojavljuje

**Problem**: Open WebUI ne prikazuje modele u padajućem izborniku

**Koraci za otklanjanje problema**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Rješenje**: Provjerite je li model pravilno učitan:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problemi s Docker mrežom

**Problem**: `host.docker.internal` se ne može riješiti

**Rješenje za Windows**:
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

**Alternativa**: Pronađite IP adresu svog računala:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problemi s performansama

**Spori odgovori**:
1. Provjerite koristi li model GPU akceleraciju: `foundry service ps`
2. Provjerite imate li dovoljno sistemskih resursa (RAM/GPU memorija)
3. Razmislite o korištenju manjeg modela za testiranje

**Problemi s memorijom**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Upute za korištenje

### Osnovni chat

1. **Odaberite model**: Izaberite iz padajućeg izbornika (prikazuje modele Foundry Local)
2. **Unesite poruku**: Koristite tekstualni unos na dnu
3. **Pošaljite**: Pritisnite Enter ili kliknite gumb za slanje
4. **Pogledajte odgovor**: Vidite odgovor u stvarnom vremenu

### Napredne značajke

**Učitavanje datoteka**:
1. Kliknite ikonu spajalice
2. Učitajte dokument (PDF, TXT itd.)
3. Postavite pitanja o sadržaju
4. Model će analizirati i odgovoriti na temelju dokumenta

**Prilagođeni sustavni upiti**:
1. Postavke → Personalizacija
2. Postavite prilagođeni sustavni upit
3. Stvara dosljednu osobnost/ponašanje AI-a

**Upravljanje razgovorima**:
- **Novi chat**: Kliknite "+" za započinjanje novog razgovora
- **Povijest chata**: Pristupite prethodnim razgovorima iz bočne trake
- **Izvoz**: Preuzmite povijest chata kao tekst/JSON

**Usporedba modela**:
1. Otvorite više kartica preglednika na istom Open WebUI
2. Odaberite različite modele u svakoj kartici
3. Usporedite odgovore na iste upite

### Obrasci integracije

**Razvojni tijek rada**:
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

## Postavljanje u produkciji

### Sigurna postavka

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

### Postavka za više korisnika

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

### Praćenje i zapisivanje

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Čišćenje

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

## Sljedeći koraci

### Ideje za poboljšanje

1. **Prilagođeni modeli**: Dodajte vlastite fine-tuned modele u Foundry Local
2. **API integracija**: Povežite se s vanjskim API-jevima putem funkcija Open WebUI
3. **Obrada dokumenata**: Postavite napredne RAG pipeline
4. **Multi-modalnost**: Konfigurirajte modele za analizu slika

### Razmatranja skaliranja

- **Balansiranje opterećenja**: Više instanci Foundry Local iza reverse proxyja
- **Usmjeravanje modela**: Različiti modeli za različite slučajeve korištenja
- **Upravljanje resursima**: Optimizacija GPU memorije za istovremene korisnike
- **Strategija sigurnosne kopije**: Redovita sigurnosna kopija podataka o razgovorima i konfiguracijama

## Reference

- [Open WebUI Dokumentacija](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Vodič za instalaciju Dockera](https://docs.docker.com/get-docker/)

---

