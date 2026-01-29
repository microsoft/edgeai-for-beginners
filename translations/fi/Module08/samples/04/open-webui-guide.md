# Open WebUI + Foundry Local - Integraatio-opas

Tämä opas näyttää, kuinka yhdistää Open WebUI Microsoft Foundry Localiin, jotta saat ammattimaisen ChatGPT-tyylisen käyttöliittymän, joka hyödyntää paikallisia AI-mallejasi.

## Yleiskatsaus

Open WebUI tarjoaa modernin ja käyttäjäystävällisen chat-käyttöliittymän, joka voi yhdistyä mihin tahansa OpenAI-yhteensopivaan API:iin. Yhdistämällä sen Foundry Localiin saat:

- **Ammattimainen käyttöliittymä**: ChatGPT-tyylinen käyttöliittymä modernilla suunnittelulla
- **Paikallinen yksityisyys**: Kaikki käsittely tapahtuu omalla laitteellasi
- **Mallien vaihto**: Helppo vaihtaa eri paikallisten mallien välillä
- **Keskusteluhistoria**: Pysyvä chat-historia ja konteksti
- **Tiedostojen lataus**: Dokumenttianalyysi ja tiedostojen käsittelyominaisuudet
- **Mukautetut roolit**: Järjestelmäkehotteiden ja roolien räätälöinti

## Esivaatimukset

### Tarvittava ohjelmisto

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Mallin lataaminen

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Pikakäyttöönotto (suositeltu)

### Vaihe 1: Käynnistä Open WebUI Dockerilla

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

### Vaihe 2: Alkuasetukset

1. **Avaa selain**: Siirry osoitteeseen `http://localhost:3000`
2. **Luo käyttäjätili**: Määritä admin-käyttäjä (ensimmäinen käyttäjästä tulee admin)
3. **Vahvista yhteys**: Mallien pitäisi näkyä automaattisesti pudotusvalikossa

### Vaihe 3: Testaa yhteys

1. Valitse mallisi pudotusvalikosta (esim. "phi-4-mini")
2. Kirjoita testiviesti: "Hei! Voitko esitellä itsesi?"
3. Näet mallin suorittaman vastausvirran reaaliajassa

## Edistynyt konfigurointi

### Ympäristömuuttujat

| Muuttuja | Tarkoitus | Oletus | Esimerkki |
|----------|-----------|--------|-----------|
| `OPENAI_API_BASE_URL` | Foundry Local -päätepiste | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-avain (vaaditaan, mutta ei käytetä paikallisesti) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Istunnon salausavain | automaattisesti luotu | `your-secret-key` |
| `ENABLE_SIGNUP` | Uusien käyttäjien rekisteröinti | `True` | `False` |

### Manuaalinen konfigurointi (vaihtoehto)

Jos ympäristömuuttujat eivät toimi, konfiguroi manuaalisesti:

1. **Avaa asetukset**: Klikkaa asetukset (rataskuvake)
2. **Siirry yhteyksiin**: Asetukset → Yhteydet → OpenAI
3. **Määritä API-tiedot**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (mikä tahansa arvo toimii)
4. **Tallenna ja testaa**: Klikkaa "Tallenna" ja testaa mallilla

### Pysyvä tietojen tallennus

Keskustelujen ja asetusten tallentamiseksi:

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

## Vianmääritys

### Yhteysongelmat

**Ongelma**: "Yhteys kielletty" tai mallit eivät lataudu

**Ratkaisut**:
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

### Malli ei näy

**Ongelma**: Open WebUI ei näytä malleja pudotusvalikossa

**Vianmääritysvaiheet**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Korjaus**: Varmista, että malli on ladattu oikein:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker-verkko-ongelmat

**Ongelma**: `host.docker.internal` ei ratkea

**Windows-ratkaisu**:
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

**Vaihtoehto**: Etsi koneesi IP-osoite:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Suorituskykyongelmat

**Hitaat vastaukset**:
1. Varmista, että malli käyttää GPU-kiihdytystä: `foundry service ps`
2. Tarkista järjestelmän resurssit (RAM/GPU-muisti)
3. Kokeile pienempää mallia testaukseen

**Muistiongelmat**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Käyttöopas

### Peruskeskustelu

1. **Valitse malli**: Valitse pudotusvalikosta (näyttää Foundry Local -mallit)
2. **Kirjoita viesti**: Käytä tekstikenttää alareunassa
3. **Lähetä**: Paina Enter tai klikkaa Lähetä-painiketta
4. **Näe vastaus**: Katso reaaliaikainen vastausvirta

### Edistyneet ominaisuudet

**Tiedoston lataus**:
1. Klikkaa paperiliitinkuvaketta
2. Lataa dokumentti (PDF, TXT jne.)
3. Kysy kysymyksiä sisällöstä
4. Malli analysoi ja vastaa dokumentin perusteella

**Mukautetut järjestelmäkehotteet**:
1. Asetukset → Personointi
2. Määritä mukautettu järjestelmäkehotus
3. Luo johdonmukainen AI-persoonallisuus/käyttäytyminen

**Keskustelun hallinta**:
- **Uusi keskustelu**: Klikkaa "+" aloittaaksesi uuden keskustelun
- **Keskusteluhistoria**: Pääsy aiempiin keskusteluihin sivupalkista
- **Vie**: Lataa keskusteluhistoria tekstinä/JSON-muodossa

**Mallien vertailu**:
1. Avaa useita selaimen välilehtiä samaan Open WebUI:hin
2. Valitse eri mallit jokaisessa välilehdessä
3. Vertaa vastauksia samoihin kehotteisiin

### Integraatiomallit

**Kehitystyön kulku**:
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

## Tuotantokäyttöönotto

### Turvallinen asennus

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

### Monen käyttäjän asennus

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

### Seuranta ja lokitus

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Siivous

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

## Seuraavat askeleet

### Parannusideat

1. **Mukautetut mallit**: Lisää omia hienosäädettyjä malleja Foundry Localiin
2. **API-integraatio**: Yhdistä ulkoisiin API:ihin Open WebUI:n kautta
3. **Dokumenttien käsittely**: Määritä edistyneet RAG-putket
4. **Monimodaalisuus**: Konfiguroi visiomallit kuvien analysointiin

### Skaalausnäkökohdat

- **Kuormantasoitus**: Useita Foundry Local -instansseja käänteisen välityspalvelimen takana
- **Mallien reititys**: Eri mallit eri käyttötarkoituksiin
- **Resurssien hallinta**: GPU-muistin optimointi samanaikaisille käyttäjille
- **Varmuuskopiointistrategia**: Keskustelutietojen ja konfiguraatioiden säännöllinen varmuuskopiointi

## Viitteet

- [Open WebUI Dokumentaatio](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Asennusopas](https://docs.docker.com/get-docker/)

---

