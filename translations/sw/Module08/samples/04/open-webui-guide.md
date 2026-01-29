# Mwongozo wa Muunganisho wa Open WebUI + Foundry Local

Mwongozo huu unaonyesha jinsi ya kuunganisha Open WebUI na Microsoft Foundry Local ili kupata kiolesura cha kitaalamu cha ChatGPT kinachotumia mifano ya AI ya ndani.

## Muhtasari

Open WebUI hutoa kiolesura cha kisasa, rahisi kutumia cha mazungumzo ambacho kinaweza kuunganishwa na API yoyote inayolingana na OpenAI. Kwa kuunganisha na Foundry Local, unapata:

- **UI ya Kitaalamu**: Kiolesura cha ChatGPT chenye muundo wa kisasa
- **Faragha ya Ndani**: Usindikaji wote unafanyika kwenye kifaa chako
- **Kubadilisha Mifano**: Kubadilisha kwa urahisi kati ya mifano tofauti ya ndani
- **Historia ya Mazungumzo**: Historia ya mazungumzo na muktadha unaoendelea
- **Upakiaji wa Faili**: Uchanganuzi wa nyaraka na usindikaji wa faili
- **Personas Maalum**: Maagizo ya mfumo na ubinafsishaji wa majukumu

## Mahitaji

### Programu Zinazohitajika

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Kupakia Mfano

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Usanidi wa Haraka (Unapendekezwa)

### Hatua ya 1: Endesha Open WebUI kwa Docker

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

### Hatua ya 2: Usanidi wa Awali

1. **Fungua Kivinjari**: Tembelea `http://localhost:3000`
2. **Unda Akaunti**: Sanidi mtumiaji mkuu (mtumiaji wa kwanza anakuwa msimamizi)
3. **Thibitisha Muunganisho**: Mifano inapaswa kuonekana kiotomatiki kwenye menyu ya kushuka

### Hatua ya 3: Jaribu Muunganisho

1. Chagua mfano wako kutoka kwenye menyu ya kushuka (mfano, "phi-4-mini")
2. Andika ujumbe wa majaribio: "Habari! Unaweza kujitambulisha?"
3. Unapaswa kuona majibu yanayotiririka kutoka kwa mfano wako wa ndani

## Usanidi wa Juu

### Vigezo vya Mazingira

| Kigezo | Kusudi | Chaguo-msingi | Mfano |
|--------|--------|--------------|-------|
| `OPENAI_API_BASE_URL` | Endpoint ya Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (inayohitajika lakini haitumiki ndani) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Funguo ya usimbaji wa kikao | inazalishwa kiotomatiki | `your-secret-key` |
| `ENABLE_SIGNUP` | Ruhusu usajili wa watumiaji wapya | `True` | `False` |

### Usanidi wa Mwongozo (Njia Mbadala)

Ikiwa vigezo vya mazingira havifanyi kazi, sanidi kwa mkono:

1. **Fungua Mipangilio**: Bofya Mipangilio (ikoni ya gia)
2. **Nenda kwa Muunganisho**: Mipangilio → Muunganisho → OpenAI
3. **Sanidi Maelezo ya API**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (thamani yoyote inafanya kazi)
4. **Hifadhi na Jaribu**: Bofya "Hifadhi" kisha jaribu na mfano

### Hifadhi ya Data ya Kudumu

Ili kuhifadhi mazungumzo na mipangilio:

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

## Utatuzi wa Shida

### Masuala ya Muunganisho

**Tatizo**: "Connection refused" au mifano haipakii

**Suluhisho**:
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

### Mfano Hauonekani

**Tatizo**: Open WebUI haionyeshi mifano kwenye menyu ya kushuka

**Hatua za Urekebishaji**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Suluhisho**: Hakikisha mfano umepakiwa vizuri:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Masuala ya Mtandao wa Docker

**Tatizo**: `host.docker.internal` haifanyi kazi

**Suluhisho la Windows**:
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

**Njia Mbadala**: Tafuta IP ya mashine yako:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Masuala ya Utendaji

**Majibu Polepole**:
1. Hakikisha mfano unatumia kasi ya GPU: `foundry service ps`
2. Thibitisha rasilimali za mfumo zinatosha (RAM/kumbukumbu ya GPU)
3. Fikiria kutumia mfano mdogo kwa majaribio

**Masuala ya Kumbukumbu**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Mwongozo wa Matumizi

### Mazungumzo ya Msingi

1. **Chagua Mfano**: Chagua kutoka kwenye menyu ya kushuka (inaonyesha mifano ya Foundry Local)
2. **Andika Ujumbe**: Tumia sehemu ya maandishi chini
3. **Tuma**: Bonyeza Enter au bofya kitufe cha Tuma
4. **Tazama Majibu**: Tazama majibu yanayotiririka kwa wakati halisi

### Vipengele vya Juu

**Upakiaji wa Faili**:
1. Bofya ikoni ya kipande cha karatasi
2. Pakia nyaraka (PDF, TXT, nk.)
3. Uliza maswali kuhusu yaliyomo
4. Mfano utachanganua na kujibu kulingana na nyaraka

**Maagizo ya Mfumo Maalum**:
1. Mipangilio → Ubinafsishaji
2. Sanidi maagizo ya mfumo maalum
3. Hutoa tabia/mwenendo wa AI thabiti

**Usimamizi wa Mazungumzo**:
- **Mazungumzo Mapya**: Bofya "+" kuanza mazungumzo mapya
- **Historia ya Mazungumzo**: Fikia mazungumzo ya awali kutoka kwenye upau wa pembeni
- **Hamisha**: Pakua historia ya mazungumzo kama maandishi/JSON

**Ulinganisho wa Mifano**:
1. Fungua tabo nyingi za kivinjari kwa Open WebUI moja
2. Chagua mifano tofauti kwenye kila tabo
3. Linganisha majibu kwa maelekezo sawa

### Mifumo ya Muunganisho

**Mtiririko wa Kazi wa Maendeleo**:
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

## Utekelezaji wa Uzalishaji

### Usanidi Salama

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

### Usanidi wa Watumiaji Wengi

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

### Ufuatiliaji na Kumbukumbu

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Usafishaji

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

## Hatua Zifuatazo

### Mawazo ya Uboreshaji

1. **Mifano Maalum**: Ongeza mifano yako iliyoboreshwa kwa Foundry Local
2. **Muunganisho wa API**: Unganisha na API za nje kupitia Open WebUI
3. **Usindikaji wa Nyaraka**: Sanidi mifumo ya RAG ya hali ya juu
4. **Multi-Modal**: Sanidi mifano ya kuona kwa uchanganuzi wa picha

### Mazingatio ya Uwezo wa Kupanuka

- **Usawazishaji wa Mizigo**: Vifaa vingi vya Foundry Local nyuma ya proxy ya kurudi nyuma
- **Uelekezaji wa Mifano**: Mifano tofauti kwa matumizi tofauti
- **Usimamizi wa Rasilimali**: Uboreshaji wa kumbukumbu ya GPU kwa watumiaji wa wakati mmoja
- **Mkakati wa Hifadhi Nakala**: Hifadhi nakala ya mara kwa mara ya data ya mazungumzo na usanidi

## Marejeleo

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

