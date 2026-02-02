# Open WebUI + Foundry Local Integrationsguide

Den här guiden visar hur du ansluter Open WebUI till Microsoft Foundry Local för ett professionellt ChatGPT-liknande gränssnitt som drivs av dina lokala AI-modeller.

## Översikt

Open WebUI erbjuder ett modernt, användarvänligt chattgränssnitt som kan anslutas till vilken OpenAI-kompatibel API som helst. Genom att ansluta det till Foundry Local får du:

- **Professionellt gränssnitt**: ChatGPT-liknande design med modern layout
- **Lokal integritet**: All bearbetning sker på din enhet
- **Modellväxling**: Enkel växling mellan olika lokala modeller
- **Konversationshistorik**: Ihållande chattloggar och kontext
- **Filuppladdningar**: Dokumentanalys och filbearbetningsmöjligheter
- **Anpassade personas**: Systemprompter och rollanpassning

## Förutsättningar

### Nödvändig programvara

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Ladda en modell

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Snabbinstallation (Rekommenderas)

### Steg 1: Kör Open WebUI med Docker

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

### Steg 2: Grundläggande inställningar

1. **Öppna webbläsaren**: Navigera till `http://localhost:3000`
2. **Skapa konto**: Ställ in administratörsanvändare (första användaren blir administratör)
3. **Verifiera anslutning**: Modeller bör automatiskt visas i rullgardinsmenyn

### Steg 3: Testa anslutningen

1. Välj din modell från rullgardinsmenyn (t.ex. "phi-4-mini")
2. Skriv ett testmeddelande: "Hej! Kan du introducera dig själv?"
3. Du bör se ett strömmande svar från din lokala modell

## Avancerad konfiguration

### Miljövariabler

| Variabel | Syfte | Standard | Exempel |
|----------|-------|----------|---------|
| `OPENAI_API_BASE_URL` | Foundry Local-endpunkt | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-nyckel (krävs men används inte lokalt) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Sessionskrypteringsnyckel | auto-genererad | `your-secret-key` |
| `ENABLE_SIGNUP` | Tillåt registrering av nya användare | `True` | `False` |

### Manuell konfiguration (Alternativ)

Om miljövariabler inte fungerar, konfigurera manuellt:

1. **Öppna inställningar**: Klicka på inställningar (kugghjulsikon)
2. **Navigera till anslutningar**: Inställningar → Anslutningar → OpenAI
3. **Ställ in API-detaljer**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API-nyckel: `foundry-local-key` (vilket värde som helst fungerar)
4. **Spara och testa**: Klicka på "Spara" och testa med en modell

### Ihållande datalagring

För att spara konversationer och inställningar:

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

## Felsökning

### Anslutningsproblem

**Problem**: "Connection refused" eller modeller laddas inte

**Lösningar**:
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

### Modell visas inte

**Problem**: Open WebUI visar inga modeller i rullgardinsmenyn

**Felsökningssteg**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Lösning**: Kontrollera att modellen är korrekt laddad:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Nätverksproblem med Docker

**Problem**: `host.docker.internal` kan inte lösas

**Windows-lösning**:
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

**Alternativ**: Hitta din dators IP-adress:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Prestandaproblem

**Långsamma svar**:
1. Kontrollera att modellen använder GPU-acceleration: `foundry service ps`
2. Verifiera tillräckliga systemresurser (RAM/GPU-minne)
3. Överväg att använda en mindre modell för testning

**Minnesproblem**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Användningsguide

### Grundläggande chatt

1. **Välj modell**: Välj från rullgardinsmenyn (visar Foundry Local-modeller)
2. **Skriv meddelande**: Använd textfältet längst ner
3. **Skicka**: Tryck på Enter eller klicka på Skicka-knappen
4. **Visa svar**: Se strömmande svar i realtid

### Avancerade funktioner

**Filuppladdning**:
1. Klicka på gemikonen
2. Ladda upp dokument (PDF, TXT, etc.)
3. Ställ frågor om innehållet
4. Modellen analyserar och svarar baserat på dokumentet

**Anpassade systemprompter**:
1. Inställningar → Personalisering
2. Ställ in anpassad systemprompt
3. Skapar en konsekvent AI-personlighet/beteende

**Konversationshantering**:
- **Ny chatt**: Klicka på "+" för att starta en ny konversation
- **Chattloggar**: Åtkomst till tidigare konversationer från sidomenyn
- **Exportera**: Ladda ner chattloggar som text/JSON

**Modelljämförelse**:
1. Öppna flera webbläsarflikar till samma Open WebUI
2. Välj olika modeller i varje flik
3. Jämför svar på samma frågor

### Integrationsmönster

**Utvecklingsarbetsflöde**:
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

## Produktionsdistribution

### Säker installation

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

### Fleranvändarinställning

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

### Övervakning och loggning

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Rensning

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

## Nästa steg

### Förbättringsidéer

1. **Anpassade modeller**: Lägg till dina egna finjusterade modeller till Foundry Local
2. **API-integration**: Anslut till externa API:er via Open WebUI-funktioner
3. **Dokumentbearbetning**: Ställ in avancerade RAG-pipelines
4. **Multi-modal**: Konfigurera visionsmodeller för bildanalys

### Skalningsöverväganden

- **Lastbalansering**: Flera Foundry Local-instanser bakom en omvänd proxy
- **Modellroutning**: Olika modeller för olika användningsområden
- **Resurshantering**: Optimering av GPU-minne för samtidiga användare
- **Backupstrategi**: Regelbunden säkerhetskopiering av konversationsdata och konfigurationer

## Referenser

- [Open WebUI Dokumentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installationsguide](https://docs.docker.com/get-docker/)

---

