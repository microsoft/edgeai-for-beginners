# Open WebUI + Foundry Local Integrasjonsguide

Denne guiden viser hvordan du kobler Open WebUI til Microsoft Foundry Local for et profesjonelt ChatGPT-lignende grensesnitt drevet av dine lokale AI-modeller.

## Oversikt

Open WebUI gir et moderne, brukervennlig chat-grensesnitt som kan kobles til enhver OpenAI-kompatibel API. Ved å koble det til Foundry Local får du:

- **Profesjonelt grensesnitt**: ChatGPT-lignende design med moderne utseende
- **Lokal personvern**: All behandling skjer på din egen enhet
- **Modellbytte**: Enkel bytting mellom ulike lokale modeller
- **Samtalehistorikk**: Vedvarende chat-historikk og kontekst
- **Filopplastinger**: Dokumentanalyse og filbehandlingsfunksjoner
- **Egendefinerte personas**: Systemprompter og rolletilpasning

## Forutsetninger

### Nødvendig programvare

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Last inn en modell

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Rask oppsett (anbefalt)

### Steg 1: Kjør Open WebUI med Docker

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

### Steg 2: Første oppsett

1. **Åpne nettleser**: Gå til `http://localhost:3000`
2. **Opprett konto**: Sett opp admin-bruker (første bruker blir admin)
3. **Bekreft tilkobling**: Modeller skal vises automatisk i nedtrekksmenyen

### Steg 3: Test tilkoblingen

1. Velg modellen din fra nedtrekksmenyen (f.eks. "phi-4-mini")
2. Skriv en testmelding: "Hei! Kan du introdusere deg selv?"
3. Du bør se en strømmet respons fra din lokale modell

## Avansert konfigurasjon

### Miljøvariabler

| Variabel | Formål | Standard | Eksempel |
|----------|--------|----------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local-endepunkt | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-nøkkel (påkrevd, men ikke brukt lokalt) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Krypteringsnøkkel for sesjon | auto-generert | `your-secret-key` |
| `ENABLE_SIGNUP` | Tillat registrering av nye brukere | `True` | `False` |

### Manuell konfigurasjon (alternativ)

Hvis miljøvariabler ikke fungerer, konfigurer manuelt:

1. **Åpne innstillinger**: Klikk på innstillinger (tannhjul-ikon)
2. **Naviger til tilkoblinger**: Innstillinger → Tilkoblinger → OpenAI
3. **Sett API-detaljer**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API-nøkkel: `foundry-local-key` (hvilken som helst verdi fungerer)
4. **Lagre og test**: Klikk "Lagre" og test med en modell

### Vedvarende datalagring

For å lagre samtaler og innstillinger:

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

## Feilsøking

### Tilkoblingsproblemer

**Problem**: "Connection refused" eller modeller lastes ikke inn

**Løsninger**:
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

### Modell vises ikke

**Problem**: Open WebUI viser ingen modeller i nedtrekksmenyen

**Feilsøking**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Løsning**: Sørg for at modellen er riktig lastet:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker-nettverksproblemer

**Problem**: `host.docker.internal` løses ikke

**Windows-løsning**:
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

**Alternativ**: Finn IP-adressen til maskinen din:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Ytelsesproblemer

**Sakte responser**:
1. Sjekk at modellen bruker GPU-akselerasjon: `foundry service ps`
2. Bekreft tilstrekkelige systemressurser (RAM/GPU-minne)
3. Vurder å bruke en mindre modell for testing

**Minneproblemer**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Brukerveiledning

### Grunnleggende chat

1. **Velg modell**: Velg fra nedtrekksmenyen (viser Foundry Local-modeller)
2. **Skriv melding**: Bruk tekstfeltet nederst
3. **Send**: Trykk Enter eller klikk på Send-knappen
4. **Se respons**: Se strømmet respons i sanntid

### Avanserte funksjoner

**Filopplasting**:
1. Klikk på binders-ikonet
2. Last opp dokument (PDF, TXT, osv.)
3. Still spørsmål om innholdet
4. Modellen analyserer og svarer basert på dokumentet

**Egendefinerte systemprompter**:
1. Innstillinger → Personalisering
2. Sett egendefinert systemprompt
3. Skaper en konsistent AI-personlighet/oppførsel

**Samtalehåndtering**:
- **Ny chat**: Klikk "+" for å starte en ny samtale
- **Chat-historikk**: Få tilgang til tidligere samtaler fra sidepanelet
- **Eksport**: Last ned samtalehistorikk som tekst/JSON

**Modellsammenligning**:
1. Åpne flere nettleserfaner til samme Open WebUI
2. Velg ulike modeller i hver fane
3. Sammenlign svar på samme spørsmål

### Integrasjonsmønstre

**Utviklingsarbeidsflyt**:
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

## Produksjonsutplassering

### Sikker oppsett

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

### Multi-bruker oppsett

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

### Overvåking og logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Opprydding

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

## Neste steg

### Forbedringsideer

1. **Egendefinerte modeller**: Legg til dine egne finjusterte modeller i Foundry Local
2. **API-integrasjon**: Koble til eksterne API-er via Open WebUI-funksjoner
3. **Dokumentbehandling**: Sett opp avanserte RAG-pipelines
4. **Multi-modal**: Konfigurer visjonsmodeller for bildeanalyse

### Skaleringsoverveielser

- **Lastbalansering**: Flere Foundry Local-installasjoner bak en reverse proxy
- **Modellruting**: Ulike modeller for ulike bruksområder
- **Ressursstyring**: Optimalisering av GPU-minne for samtidige brukere
- **Backup-strategi**: Regelmessig sikkerhetskopiering av samtaledata og konfigurasjoner

## Referanser

- [Open WebUI Dokumentasjon](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentasjon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installasjonsguide](https://docs.docker.com/get-docker/)

---

