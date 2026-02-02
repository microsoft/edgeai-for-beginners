# Open WebUI + Foundry Local integracijos vadovas

Šiame vadove paaiškinama, kaip sujungti Open WebUI su Microsoft Foundry Local, kad gautumėte profesionalią ChatGPT tipo sąsają, veikiančią su vietiniais AI modeliais.

## Apžvalga

Open WebUI siūlo modernią, patogią pokalbių sąsają, kuri gali prisijungti prie bet kurio OpenAI suderinamo API. Sujungus ją su Foundry Local, gausite:

- **Profesionali sąsaja**: ChatGPT tipo sąsaja su šiuolaikiniu dizainu
- **Vietinis privatumas**: Visa apdorojimo veikla vyksta jūsų įrenginyje
- **Modelių keitimas**: Lengvas perjungimas tarp skirtingų vietinių modelių
- **Pokalbių istorija**: Nuolatinė pokalbių istorija ir kontekstas
- **Failų įkėlimas**: Dokumentų analizės ir failų apdorojimo galimybės
- **Individualūs personažai**: Sistemos raginimai ir vaidmenų pritaikymas

## Reikalavimai

### Reikalinga programinė įranga

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Įkelkite modelį

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Greitas nustatymas (rekomenduojama)

### 1 žingsnis: Paleiskite Open WebUI su Docker

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

### 2 žingsnis: Pradinis nustatymas

1. **Atidarykite naršyklę**: Eikite į `http://localhost:3000`
2. **Sukurkite paskyrą**: Sukurkite administratoriaus vartotoją (pirmasis vartotojas tampa administratoriumi)
3. **Patikrinkite ryšį**: Modeliai turėtų automatiškai pasirodyti išskleidžiamajame meniu

### 3 žingsnis: Patikrinkite ryšį

1. Pasirinkite savo modelį iš išskleidžiamojo meniu (pvz., "phi-4-mini")
2. Įveskite testinę žinutę: "Sveiki! Ar galite prisistatyti?"
3. Turėtumėte matyti srautinį atsakymą iš vietinio modelio

## Išplėstinis konfigūravimas

### Aplinkos kintamieji

| Kintamasis | Paskirtis | Numatytasis | Pavyzdys |
|------------|-----------|-------------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local galinis taškas | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API raktas (reikalingas, bet vietoje nenaudojamas) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Sesijos šifravimo raktas | automatiškai sugeneruotas | `your-secret-key` |
| `ENABLE_SIGNUP` | Leidžia naujų vartotojų registraciją | `True` | `False` |

### Rankinis konfigūravimas (alternatyva)

Jei aplinkos kintamieji neveikia, konfigūruokite rankiniu būdu:

1. **Atidarykite nustatymus**: Spustelėkite nustatymų (krumpliaračio) piktogramą
2. **Eikite į ryšius**: Nustatymai → Ryšiai → OpenAI
3. **Nustatykite API duomenis**:
   - API bazinis URL: `http://host.docker.internal:51211/v1`
   - API raktas: `foundry-local-key` (bet kokia reikšmė tinka)
4. **Išsaugokite ir patikrinkite**: Spustelėkite "Išsaugoti", tada patikrinkite su modeliu

### Nuolatinis duomenų saugojimas

Norėdami išsaugoti pokalbius ir nustatymus:

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

## Trikčių šalinimas

### Ryšio problemos

**Problema**: "Ryšys atmestas" arba modeliai neįkeliami

**Sprendimai**:
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

### Modelis nepasirodo

**Problema**: Open WebUI nerodo modelių išskleidžiamajame meniu

**Diagnostikos veiksmai**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Sprendimas**: Įsitikinkite, kad modelis tinkamai įkeltas:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker tinklo problemos

**Problema**: `host.docker.internal` neatsako

**Windows sprendimas**:
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

**Alternatyva**: Suraskite savo kompiuterio IP adresą:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Našumo problemos

**Lėti atsakymai**:
1. Patikrinkite, ar modelis naudoja GPU pagreitį: `foundry service ps`
2. Įsitikinkite, kad yra pakankamai sistemos resursų (RAM/GPU atmintis)
3. Bandymams naudokite mažesnį modelį

**Atminties problemos**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Naudojimo vadovas

### Pagrindinis pokalbis

1. **Pasirinkite modelį**: Pasirinkite iš išskleidžiamojo meniu (rodomi Foundry Local modeliai)
2. **Įveskite žinutę**: Naudokite teksto įvestį apačioje
3. **Siųsti**: Paspauskite Enter arba spustelėkite Siųsti mygtuką
4. **Peržiūrėkite atsakymą**: Matykite srautinį atsakymą realiu laiku

### Išplėstinės funkcijos

**Failų įkėlimas**:
1. Spustelėkite sąvaržėlės piktogramą
2. Įkelkite dokumentą (PDF, TXT ir kt.)
3. Užduokite klausimus apie turinį
4. Modelis analizuos ir atsakys remdamasis dokumentu

**Individualūs sistemos raginimai**:
1. Nustatymai → Personalizavimas
2. Nustatykite individualų sistemos raginimą
3. Sukuriamas nuoseklus AI asmenybė/elgesys

**Pokalbių valdymas**:
- **Naujas pokalbis**: Spustelėkite "+" pradėti naują pokalbį
- **Pokalbių istorija**: Pasiekite ankstesnius pokalbius iš šoninės juostos
- **Eksportas**: Atsisiųskite pokalbių istoriją kaip tekstą/JSON

**Modelių palyginimas**:
1. Atidarykite kelis naršyklės skirtukus su tuo pačiu Open WebUI
2. Pasirinkite skirtingus modelius kiekviename skirtuke
3. Palyginkite atsakymus į tuos pačius raginimus

### Integracijos modeliai

**Kūrimo darbo eiga**:
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

## Produkcijos diegimas

### Saugus nustatymas

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

### Daugelio vartotojų nustatymas

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

### Stebėjimas ir registravimas

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Valymas

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

## Tolimesni žingsniai

### Tobulinimo idėjos

1. **Individualūs modeliai**: Pridėkite savo patobulintus modelius į Foundry Local
2. **API integracija**: Prisijunkite prie išorinių API per Open WebUI funkcijas
3. **Dokumentų apdorojimas**: Nustatykite pažangias RAG sistemas
4. **Daugiarūšis**: Konfigūruokite vaizdo modelius vaizdų analizei

### Skalavimo aspektai

- **Krovos balansavimas**: Keli Foundry Local egzemplioriai už atvirkštinio tarpinio serverio
- **Modelių maršrutizavimas**: Skirtingi modeliai skirtingiems naudojimo atvejams
- **Resursų valdymas**: GPU atminties optimizavimas keliems vartotojams
- **Atsarginės kopijos strategija**: Reguliarus pokalbių duomenų ir konfigūracijų atsarginis kopijavimas

## Nuorodos

- [Open WebUI dokumentacija](https://docs.openwebui.com/)
- [Open WebUI GitHub saugykla](https://github.com/open-webui/open-webui)
- [Foundry Local dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker diegimo vadovas](https://docs.docker.com/get-docker/)

---

