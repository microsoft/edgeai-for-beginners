# Open WebUI + Foundry Local Integratiegids

Deze gids laat zien hoe je Open WebUI kunt verbinden met Microsoft Foundry Local voor een professionele ChatGPT-achtige interface aangedreven door je lokale AI-modellen.

## Overzicht

Open WebUI biedt een moderne, gebruiksvriendelijke chatinterface die kan verbinden met elke OpenAI-compatibele API. Door het te koppelen aan Foundry Local krijg je:

- **Professionele UI**: ChatGPT-achtige interface met modern ontwerp
- **Lokale Privacy**: Alle verwerking gebeurt op je eigen apparaat
- **Modelwissel**: Eenvoudig schakelen tussen verschillende lokale modellen
- **Gesprekshistorie**: Blijvende chatgeschiedenis en context
- **Bestandsuploads**: Documentanalyse en bestandsverwerkingsmogelijkheden
- **Aangepaste Persona's**: Systeemprompts en rolpersonalisatie

## Vereisten

### Benodigde Software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Een Model Laden

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Snelle Setup (Aanbevolen)

### Stap 1: Open WebUI draaien met Docker

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

### Stap 2: Initiële Setup

1. **Open Browser**: Navigeer naar `http://localhost:3000`
2. **Account Aanmaken**: Stel een admin-gebruiker in (de eerste gebruiker wordt admin)
3. **Verbinding Verifiëren**: Modellen zouden automatisch in de dropdown moeten verschijnen

### Stap 3: Test de Verbinding

1. Selecteer je model uit de dropdown (bijv. "phi-4-mini")
2. Typ een testbericht: "Hallo! Kun je jezelf voorstellen?"
3. Je zou een streamingantwoord van je lokale model moeten zien

## Geavanceerde Configuratie

### Omgevingsvariabelen

| Variabele | Doel | Standaard | Voorbeeld |
|-----------|------|-----------|-----------|
| `OPENAI_API_BASE_URL` | Foundry Local endpoint | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-sleutel (vereist maar lokaal niet gebruikt) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Sleutel voor sessie-encryptie | automatisch gegenereerd | `your-secret-key` |
| `ENABLE_SIGNUP` | Nieuwe gebruikersregistratie toestaan | `True` | `False` |

### Handmatige Configuratie (Alternatief)

Als omgevingsvariabelen niet werken, configureer handmatig:

1. **Open Instellingen**: Klik op Instellingen (tandwielicoon)
2. **Ga naar Verbindingen**: Instellingen → Verbindingen → OpenAI
3. **Stel API-gegevens in**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API-sleutel: `foundry-local-key` (elke waarde werkt)
4. **Opslaan en Testen**: Klik op "Opslaan" en test met een model

### Persistente Gegevensopslag

Om gesprekken en instellingen te bewaren:

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

## Probleemoplossing

### Verbindingsproblemen

**Probleem**: "Verbinding geweigerd" of modellen laden niet

**Oplossingen**:
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

### Model Verschijnt Niet

**Probleem**: Open WebUI toont geen modellen in de dropdown

**Debugging Stappen**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Oplossing**: Zorg ervoor dat het model correct is geladen:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker Netwerkproblemen

**Probleem**: `host.docker.internal` lost niet op

**Windows Oplossing**:
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

**Alternatief**: Zoek het IP-adres van je machine:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Prestatieproblemen

**Trage Reacties**:
1. Controleer of het model GPU-versnelling gebruikt: `foundry service ps`
2. Verifieer voldoende systeembronnen (RAM/GPU-geheugen)
3. Overweeg een kleiner model te gebruiken voor testen

**Geheugenproblemen**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Gebruikershandleiding

### Basis Chat

1. **Selecteer Model**: Kies uit de dropdown (toont Foundry Local modellen)
2. **Typ Bericht**: Gebruik het tekstveld onderaan
3. **Verstuur**: Druk op Enter of klik op de Verstuur-knop
4. **Bekijk Antwoord**: Zie streamingantwoord in real-time

### Geavanceerde Functies

**Bestandsupload**:
1. Klik op het paperclip-icoon
2. Upload een document (PDF, TXT, etc.)
3. Stel vragen over de inhoud
4. Het model analyseert en reageert op basis van het document

**Aangepaste Systeemprompts**:
1. Instellingen → Personalisatie
2. Stel een aangepaste systeemprompt in
3. Creëert een consistente AI-persoonlijkheid/gedrag

**Gespreksbeheer**:
- **Nieuw Gesprek**: Klik op "+" om een nieuw gesprek te starten
- **Gesprekshistorie**: Toegang tot eerdere gesprekken via de zijbalk
- **Exporteren**: Download gespreksgeschiedenis als tekst/JSON

**Modelvergelijking**:
1. Open meerdere browsertabs naar dezelfde Open WebUI
2. Selecteer verschillende modellen in elke tab
3. Vergelijk antwoorden op dezelfde prompts

### Integratiepatronen

**Ontwikkelworkflow**:
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

## Productie-implementatie

### Veilige Setup

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

### Multi-gebruiker Setup

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

### Monitoring en Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Opruimen

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

## Volgende Stappen

### Verbeteringsideeën

1. **Aangepaste Modellen**: Voeg je eigen fijn-afgestelde modellen toe aan Foundry Local
2. **API-integratie**: Verbind met externe API's via Open WebUI-functies
3. **Documentverwerking**: Stel geavanceerde RAG-pijplijnen in
4. **Multi-Modal**: Configureer vision-modellen voor beeldanalyse

### Schaaloverwegingen

- **Load Balancing**: Meerdere Foundry Local-instanties achter een reverse proxy
- **Modelroutering**: Verschillende modellen voor verschillende toepassingen
- **Resourcebeheer**: GPU-geheugenoptimalisatie voor gelijktijdige gebruikers
- **Back-upstrategie**: Regelmatige back-up van gespreksgegevens en configuraties

## Referenties

- [Open WebUI Documentatie](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installatiegids](https://docs.docker.com/get-docker/)

---

