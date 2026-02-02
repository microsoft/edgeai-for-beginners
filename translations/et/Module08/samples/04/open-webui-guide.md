# Open WebUI + Foundry Locali integreerimise juhend

See juhend näitab, kuidas ühendada Open WebUI Microsoft Foundry Localiga, et luua professionaalne ChatGPT-laadne liides, mis kasutab teie kohalikke AI-mudeleid.

## Ülevaade

Open WebUI pakub kaasaegset ja kasutajasõbralikku vestlusliidest, mis saab ühenduda mis tahes OpenAI-ühilduva API-ga. Ühendades selle Foundry Localiga, saate:

- **Professionaalne liides**: ChatGPT-laadne liides kaasaegse disainiga
- **Kohalik privaatsus**: Kogu töötlemine toimub teie seadmes
- **Mudelite vahetamine**: Lihtne vahetada erinevate kohalike mudelite vahel
- **Vestluste ajalugu**: Püsiv vestluste ajalugu ja kontekst
- **Failide üleslaadimine**: Dokumentide analüüs ja failide töötlemise võimalused
- **Kohandatud rollid**: Süsteemi käskude ja rollide kohandamine

## Eeltingimused

### Vajalik tarkvara

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Mudeli laadimine

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Kiire seadistamine (soovitatav)

### Samm 1: Käivitage Open WebUI Dockeriga

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

### Samm 2: Esmane seadistamine

1. **Avage brauser**: Minge aadressile `http://localhost:3000`
2. **Looge konto**: Seadistage administraatori kasutaja (esimene kasutaja saab administraatoriks)
3. **Kontrollige ühendust**: Mudelid peaksid automaatselt rippmenüüs ilmuma

### Samm 3: Testige ühendust

1. Valige mudel rippmenüüst (nt "phi-4-mini")
2. Sisestage testisõnum: "Tere! Kas saaksite end tutvustada?"
3. Näete voogesituse vastust oma kohalikult mudelilt

## Täpsem seadistamine

### Keskkonnamuutujad

| Muutuja | Eesmärk | Vaikimisi | Näide |
|---------|---------|-----------|-------|
| `OPENAI_API_BASE_URL` | Foundry Locali lõpp-punkt | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API võti (vajalik, kuid kohalikult ei kasutata) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Sessiooni krüpteerimise võti | automaatselt genereeritud | `your-secret-key` |
| `ENABLE_SIGNUP` | Uute kasutajate registreerimise lubamine | `True` | `False` |

### Käsitsi seadistamine (alternatiiv)

Kui keskkonnamuutujad ei tööta, seadistage käsitsi:

1. **Avage seaded**: Klõpsake seadete (hammasratta) ikooni
2. **Minge ühenduste juurde**: Seaded → Ühendused → OpenAI
3. **Määrake API andmed**:
   - API põhiaadress: `http://host.docker.internal:51211/v1`
   - API võti: `foundry-local-key` (mis tahes väärtus sobib)
4. **Salvestage ja testige**: Klõpsake "Salvesta" ja testige mudeliga

### Püsiv andmesalvestus

Vestluste ja seadete säilitamiseks:

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

## Tõrkeotsing

### Ühenduse probleemid

**Probleem**: "Ühendus keelatud" või mudelid ei laadi

**Lahendused**:
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

### Mudel ei ilmu

**Probleem**: Open WebUI ei näita mudeleid rippmenüüs

**Tõrkeotsingu sammud**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Lahendus**: Veenduge, et mudel on korralikult laaditud:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker võrgu probleemid

**Probleem**: `host.docker.internal` ei lahene

**Windowsi lahendus**:
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

**Alternatiiv**: Leidke oma masina IP:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Jõudlusprobleemid

**Aeglased vastused**:
1. Kontrollige, kas mudel kasutab GPU kiirendust: `foundry service ps`
2. Veenduge, et süsteemi ressursid (RAM/GPU mälu) on piisavad
3. Katsetamiseks kasutage väiksemat mudelit

**Mäluprobleemid**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Kasutusjuhend

### Põhivestlus

1. **Valige mudel**: Valige rippmenüüst (kuvatakse Foundry Locali mudelid)
2. **Sisestage sõnum**: Kasutage allosas olevat tekstisisestust
3. **Saatke**: Vajutage Enter või klõpsake saatmisnuppu
4. **Vaadake vastust**: Näete voogesituse vastust reaalajas

### Täiustatud funktsioonid

**Failide üleslaadimine**:
1. Klõpsake kirjaklambri ikooni
2. Laadige üles dokument (PDF, TXT jne)
3. Esitage küsimusi dokumendi sisu kohta
4. Mudel analüüsib ja vastab dokumendi põhjal

**Kohandatud süsteemi käsklused**:
1. Seaded → Isikupärastamine
2. Määrake kohandatud süsteemi käsklus
3. Loob järjepideva AI isiksuse/käitumise

**Vestluste haldamine**:
- **Uus vestlus**: Klõpsake "+" uue vestluse alustamiseks
- **Vestluste ajalugu**: Juurdepääs varasematele vestlustele külgribalt
- **Eksport**: Laadige vestluste ajalugu alla tekstina/JSON-ina

**Mudelite võrdlus**:
1. Avage mitu brauseri vahekaarti samale Open WebUI-le
2. Valige igas vahekaardis erinevad mudelid
3. Võrrelge vastuseid samadele käsklustele

### Integreerimismustrid

**Arendustöövoog**:
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

## Tootmisseadistus

### Turvaline seadistus

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

### Mitme kasutaja seadistus

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

### Jälgimine ja logimine

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Puhastamine

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

## Järgmised sammud

### Parendusideed

1. **Kohandatud mudelid**: Lisage oma peenhäälestatud mudelid Foundry Locali
2. **API integreerimine**: Ühendage väliste API-dega Open WebUI funktsioonide kaudu
3. **Dokumentide töötlemine**: Seadistage täiustatud RAG torustikud
4. **Multimodaalsus**: Konfigureerige visioonimudelid pildianalüüsiks

### Skaalumise kaalutlused

- **Koormuse tasakaalustamine**: Mitme Foundry Locali eksemplari kasutamine pöördproksi taga
- **Mudelite suunamine**: Erinevad mudelid erinevateks kasutusjuhtudeks
- **Ressursside haldamine**: GPU mälu optimeerimine samaaegsete kasutajate jaoks
- **Varundusstrateegia**: Vestlusandmete ja konfiguratsioonide regulaarne varundamine

## Viited

- [Open WebUI dokumentatsioon](https://docs.openwebui.com/)
- [Open WebUI GitHubi repositoorium](https://github.com/open-webui/open-webui)
- [Foundry Local dokumentatsioon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dockeri paigaldusjuhend](https://docs.docker.com/get-docker/)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.