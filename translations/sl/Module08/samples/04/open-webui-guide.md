# Vodnik za integracijo Open WebUI + Foundry Local

Ta vodnik prikazuje, kako povezati Open WebUI z Microsoft Foundry Local za profesionalni vmesnik, podoben ChatGPT, ki ga poganjajo vaši lokalni AI modeli.

## Pregled

Open WebUI ponuja sodoben, uporabniku prijazen klepetalni vmesnik, ki se lahko poveže s katerim koli API-jem, združljivim z OpenAI. S povezavo na Foundry Local pridobite:

- **Profesionalni vmesnik**: Vmesnik, podoben ChatGPT, z modernim dizajnom
- **Lokalna zasebnost**: Vsa obdelava poteka na vaši napravi
- **Preklapljanje modelov**: Enostavno preklapljanje med različnimi lokalnimi modeli
- **Zgodovina pogovorov**: Trajna zgodovina klepeta in kontekst
- **Nalaganje datotek**: Analiza dokumentov in obdelava datotek
- **Prilagojene osebnosti**: Sistemski pozivi in prilagoditev vlog

## Predpogoji

### Zahtevana programska oprema

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Nalaganje modela

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Hitra nastavitev (priporočeno)

### Korak 1: Zaženite Open WebUI z Dockerjem

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

### Korak 2: Začetna nastavitev

1. **Odprite brskalnik**: Pojdite na `http://localhost:3000`
2. **Ustvarite račun**: Nastavite skrbniškega uporabnika (prvi uporabnik postane skrbnik)
3. **Preverite povezavo**: Modeli se morajo samodejno prikazati v spustnem meniju

### Korak 3: Preizkusite povezavo

1. Izberite svoj model iz spustnega menija (npr. "phi-4-mini")
2. Vnesite testno sporočilo: "Pozdravljeni! Se lahko predstavite?"
3. Videti bi morali pretočni odgovor vašega lokalnega modela

## Napredna konfiguracija

### Okoljske spremenljivke

| Spremenljivka | Namen | Privzeto | Primer |
|---------------|-------|----------|--------|
| `OPENAI_API_BASE_URL` | Končna točka Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API ključ (zahtevan, vendar lokalno ni uporabljen) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Ključ za šifriranje sej | samodejno generiran | `your-secret-key` |
| `ENABLE_SIGNUP` | Omogoči registracijo novih uporabnikov | `True` | `False` |

### Ročna konfiguracija (alternativa)

Če okoljske spremenljivke ne delujejo, konfigurirajte ročno:

1. **Odprite nastavitve**: Kliknite Nastavitve (ikona zobnika)
2. **Pojdite na Povezave**: Nastavitve → Povezave → OpenAI
3. **Nastavite podrobnosti API-ja**:
   - Osnovni URL API-ja: `http://host.docker.internal:51211/v1`
   - API ključ: `foundry-local-key` (katerakoli vrednost deluje)
4. **Shrani in preizkusi**: Kliknite "Shrani" in nato preizkusite z modelom

### Trajna shranjevanje podatkov

Za trajno shranjevanje pogovorov in nastavitev:

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

## Odpravljanje težav

### Težave s povezavo

**Težava**: "Povezava zavrnjena" ali modeli se ne nalagajo

**Rešitve**:
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

### Model se ne prikaže

**Težava**: Open WebUI ne prikazuje modelov v spustnem meniju

**Koraki za odpravljanje težav**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Popravek**: Prepričajte se, da je model pravilno naložen:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Težave z Docker omrežjem

**Težava**: `host.docker.internal` se ne razreši

**Rešitev za Windows**:
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

**Alternativa**: Poiščite IP vašega računalnika:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Težave z zmogljivostjo

**Počasni odzivi**:
1. Preverite, ali model uporablja GPU pospeševanje: `foundry service ps`
2. Preverite zadostne sistemske vire (RAM/GPU pomnilnik)
3. Razmislite o uporabi manjšega modela za testiranje

**Težave s pomnilnikom**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Navodila za uporabo

### Osnovni klepet

1. **Izberite model**: Izberite iz spustnega menija (prikazuje modele Foundry Local)
2. **Vnesite sporočilo**: Uporabite besedilni vnos na dnu
3. **Pošljite**: Pritisnite Enter ali kliknite gumb Pošlji
4. **Oglejte si odgovor**: Oglejte si pretočni odgovor v realnem času

### Napredne funkcije

**Nalaganje datotek**:
1. Kliknite ikono s sponko za papir
2. Naložite dokument (PDF, TXT itd.)
3. Postavite vprašanja o vsebini
4. Model bo analiziral in odgovoril na podlagi dokumenta

**Prilagojeni sistemski pozivi**:
1. Nastavitve → Personalizacija
2. Nastavite prilagojen sistemski poziv
3. Ustvari dosledno osebnost/vedenje AI

**Upravljanje pogovorov**:
- **Nov klepet**: Kliknite "+" za začetek novega pogovora
- **Zgodovina klepeta**: Dostopajte do prejšnjih pogovorov iz stranske vrstice
- **Izvoz**: Prenesite zgodovino klepeta kot besedilo/JSON

**Primerjava modelov**:
1. Odprite več zavihkov brskalnika na istem Open WebUI
2. Izberite različne modele v vsakem zavihku
3. Primerjajte odgovore na iste pozive

### Vzorci integracije

**Razvojni potek dela**:
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

## Namestitev v produkcijo

### Varna nastavitev

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

### Nastavitev za več uporabnikov

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

### Spremljanje in beleženje

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Čiščenje

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

## Naslednji koraki

### Ideje za izboljšave

1. **Prilagojeni modeli**: Dodajte svoje lastne fino uglašene modele v Foundry Local
2. **API integracija**: Povežite se z zunanjimi API-ji prek funkcij Open WebUI
3. **Obdelava dokumentov**: Nastavite napredne RAG pipeline
4. **Multi-modalnost**: Konfigurirajte modele za analizo slik

### Premisleki o skaliranju

- **Uravnavanje obremenitve**: Več primerkov Foundry Local za reverse proxy
- **Usmerjanje modelov**: Različni modeli za različne primere uporabe
- **Upravljanje virov**: Optimizacija GPU pomnilnika za sočasne uporabnike
- **Strategija varnostnega kopiranja**: Redno varnostno kopiranje podatkov o pogovorih in konfiguracij

## Reference

- [Open WebUI Dokumentacija](https://docs.openwebui.com/)
- [Open WebUI GitHub Repozitorij](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Vodnik za namestitev Dockerja](https://docs.docker.com/get-docker/)

---

