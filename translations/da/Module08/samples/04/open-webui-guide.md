# Open WebUI + Foundry Local Integrationsguide

Denne guide viser, hvordan du forbinder Open WebUI med Microsoft Foundry Local for at få en professionel ChatGPT-lignende grænseflade drevet af dine lokale AI-modeller.

## Oversigt

Open WebUI tilbyder en moderne, brugervenlig chatgrænseflade, der kan forbindes til enhver OpenAI-kompatibel API. Ved at forbinde den til Foundry Local får du:

- **Professionel UI**: ChatGPT-lignende grænseflade med moderne design
- **Lokal Privatliv**: Al behandling sker på din enhed
- **Modelskift**: Nem skift mellem forskellige lokale modeller
- **Samtalehistorik**: Vedvarende chat-historik og kontekst
- **Filuploads**: Dokumentanalyse og filbehandlingsfunktioner
- **Tilpassede Personas**: Systemprompter og rolletilpasning

## Forudsætninger

### Påkrævet software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Indlæs en model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Hurtig opsætning (anbefalet)

### Trin 1: Kør Open WebUI med Docker

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

### Trin 2: Initial opsætning

1. **Åbn browser**: Naviger til `http://localhost:3000`
2. **Opret konto**: Opsæt admin-bruger (første bruger bliver admin)
3. **Bekræft forbindelse**: Modeller bør automatisk vises i dropdown-menuen

### Trin 3: Test forbindelsen

1. Vælg din model fra dropdown-menuen (f.eks. "phi-4-mini")
2. Skriv en testbesked: "Hej! Kan du introducere dig selv?"
3. Du bør se et streaming-svar fra din lokale model

## Avanceret konfiguration

### Miljøvariabler

| Variabel | Formål | Standard | Eksempel |
|----------|--------|----------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local endpoint | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-nøgle (påkrævet, men ikke brugt lokalt) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Sessionskrypteringsnøgle | auto-genereret | `your-secret-key` |
| `ENABLE_SIGNUP` | Tillad ny brugerregistrering | `True` | `False` |

### Manuel konfiguration (alternativ)

Hvis miljøvariabler ikke fungerer, konfigurer manuelt:

1. **Åbn indstillinger**: Klik på Indstillinger (tandhjulsikon)
2. **Naviger til forbindelser**: Indstillinger → Forbindelser → OpenAI
3. **Indstil API-detaljer**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API-nøgle: `foundry-local-key` (enhver værdi fungerer)
4. **Gem og test**: Klik "Gem" og test med en model

### Vedvarende datalagring

For at gemme samtaler og indstillinger:

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

## Fejlfinding

### Forbindelsesproblemer

**Problem**: "Forbindelse nægtet" eller modeller indlæses ikke

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

### Model vises ikke

**Problem**: Open WebUI viser ingen modeller i dropdown-menuen

**Fejlfindingstrin**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Løsning**: Sørg for, at modellen er korrekt indlæst:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker-netværksproblemer

**Problem**: `host.docker.internal` kan ikke løses

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

**Alternativ**: Find din maskines IP:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Ydelsesproblemer

**Langsomme svar**:
1. Tjek, om modellen bruger GPU-acceleration: `foundry service ps`
2. Bekræft tilstrækkelige systemressourcer (RAM/GPU-hukommelse)
3. Overvej at bruge en mindre model til test

**Hukommelsesproblemer**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Brugsvejledning

### Grundlæggende chat

1. **Vælg model**: Vælg fra dropdown-menuen (viser Foundry Local-modeller)
2. **Skriv besked**: Brug tekstfeltet nederst
3. **Send**: Tryk Enter eller klik på Send-knappen
4. **Se svar**: Se streaming-svar i realtid

### Avancerede funktioner

**Filupload**:
1. Klik på papirklipsikonet
2. Upload dokument (PDF, TXT osv.)
3. Stil spørgsmål om indholdet
4. Modellen analyserer og svarer baseret på dokumentet

**Tilpassede systemprompter**:
1. Indstillinger → Personalisering
2. Indstil tilpasset systemprompt
3. Skaber en konsistent AI-personlighed/adfærd

**Samtalestyring**:
- **Ny chat**: Klik på "+" for at starte en ny samtale
- **Chat-historik**: Få adgang til tidligere samtaler fra sidepanelet
- **Eksport**: Download chat-historik som tekst/JSON

**Model-sammenligning**:
1. Åbn flere browserfaner til samme Open WebUI
2. Vælg forskellige modeller i hver fane
3. Sammenlign svar på samme prompts

### Integrationsmønstre

**Udviklingsarbejdsgang**:
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

## Produktionsudrulning

### Sikker opsætning

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

### Opsætning for flere brugere

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

### Overvågning og logning

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Oprydning

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

## Næste trin

### Forbedringsidéer

1. **Tilpassede modeller**: Tilføj dine egne finjusterede modeller til Foundry Local
2. **API-integration**: Forbind til eksterne API'er via Open WebUI-funktioner
3. **Dokumentbehandling**: Opsæt avancerede RAG-pipelines
4. **Multi-modal**: Konfigurer visionsmodeller til billedanalyse

### Skaleringsovervejelser

- **Load Balancing**: Flere Foundry Local-instanser bag en reverse proxy
- **Model-routing**: Forskellige modeller til forskellige brugsscenarier
- **Ressourcehåndtering**: GPU-hukommelsesoptimering for samtidige brugere
- **Backup-strategi**: Regelmæssig backup af samtaledata og konfigurationer

## Referencer

- [Open WebUI Dokumentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installationsguide](https://docs.docker.com/get-docker/)

---

