# Open WebUI + Foundry Local ഇന്റഗ്രേഷൻ ഗൈഡ്

ഈ ഗൈഡ് Open WebUI-യെ Microsoft Foundry Local-ലുമായി ബന്ധിപ്പിച്ച് നിങ്ങളുടെ ലോക്കൽ AI മോഡലുകൾ ഉപയോഗിച്ച് പ്രൊഫഷണൽ ChatGPT പോലുള്ള ഇന്റർഫേസ് എങ്ങനെ സജ്ജമാക്കാമെന്ന് കാണിക്കുന്നു.

## അവലോകനം

Open WebUI ഒരു ആധുനികവും ഉപയോക്തൃ സൗഹൃദവുമായ ചാറ്റ് ഇന്റർഫേസ് നൽകുന്നു, ഇത് ഏതെങ്കിലും OpenAI-സമർത്ഥമായ API-യുമായി ബന്ധിപ്പിക്കാം. Foundry Local-ലുമായി ബന്ധിപ്പിച്ചാൽ നിങ്ങൾക്ക് ലഭിക്കുന്നത്:

- **പ്രൊഫഷണൽ UI**: ആധുനിക ഡിസൈനുള്ള ChatGPT പോലുള്ള ഇന്റർഫേസ്
- **ലോക്കൽ പ്രൈവസി**: എല്ലാ പ്രോസസ്സിംഗും നിങ്ങളുടെ ഉപകരണത്തിൽ നടക്കുന്നു
- **മോഡൽ സ്വിച്ച് ചെയ്യൽ**: വ്യത്യസ്ത ലോക്കൽ മോഡലുകൾ എളുപ്പത്തിൽ മാറാം
- **സംഭാഷണ ചരിത്രം**: സ്ഥിരമായ ചാറ്റ് ചരിത്രവും കോൺടെക്സ്റ്റും
- **ഫയൽ അപ്‌ലോഡുകൾ**: ഡോക്യുമെന്റ് വിശകലനവും ഫയൽ പ്രോസസ്സിംഗും
- **കസ്റ്റം പെർസോണാസ്**: സിസ്റ്റം പ്രോംപ്റ്റുകളും റോളുകൾ കസ്റ്റമൈസ് ചെയ്യൽ

## മുൻകൂട്ടി ആവശ്യമായവ

### ആവശ്യമായ സോഫ്റ്റ്വെയർ

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ഒരു മോഡൽ ലോഡ് ചെയ്യുക

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## വേഗത്തിലുള്ള സജ്ജീകരണം (ശുപാർശ ചെയ്യുന്നു)

### ഘട്ടം 1: Docker ഉപയോഗിച്ച് Open WebUI ഓടിക്കുക

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

### ഘട്ടം 2: പ്രാഥമിക സജ്ജീകരണം

1. **ബ്രൗസർ തുറക്കുക**: `http://localhost:3000` എന്ന വിലാസത്തിലേക്ക് പോവുക
2. **അക്കൗണ്ട് സൃഷ്ടിക്കുക**: അഡ്മിൻ ഉപയോക്താവ് സജ്ജമാക്കുക (ആദ്യ ഉപയോക്താവ് അഡ്മിൻ ആകും)
3. **ബന്ധം സ്ഥിരീകരിക്കുക**: മോഡലുകൾ ഡ്രോപ്പ്ഡൗണിൽ സ്വയം കാണിക്കണം

### ഘട്ടം 3: ബന്ധം പരീക്ഷിക്കുക

1. ഡ്രോപ്പ്ഡൗണിൽ നിന്നു നിങ്ങളുടെ മോഡൽ തിരഞ്ഞെടുക്കുക (ഉദാ: "phi-4-mini")
2. ഒരു ടെസ്റ്റ് സന്ദേശം ടൈപ്പ് ചെയ്യുക: "Hello! Can you introduce yourself?"
3. നിങ്ങളുടെ ലോക്കൽ മോഡലിൽ നിന്നുള്ള സ്ട്രീമിംഗ് പ്രതികരണം കാണണം

## ആധുനിക കോൺഫിഗറേഷൻ

### പരിസ്ഥിതി വേരിയബിളുകൾ

| വേരിയബിള്‍ | ഉദ്ദേശ്യം | ഡിഫോൾട്ട് | ഉദാഹരണം |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local എന്റ്പോയിന്റ് | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API കീ (ലോക്കലിൽ ഉപയോഗിക്കാറില്ല) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | സെഷൻ എൻക്രിപ്ഷൻ കീ | സ്വയം സൃഷ്ടിക്കപ്പെട്ടത് | `your-secret-key` |
| `ENABLE_SIGNUP` | പുതിയ ഉപയോക്തൃ രജിസ്ട്രേഷൻ അനുവദിക്കുക | `True` | `False` |

### മാനുവൽ കോൺഫിഗറേഷൻ (മാറ്റുവഴി)

പരിസ്ഥിതി വേരിയബിളുകൾ പ്രവർത്തിക്കാത്ത പക്ഷം, മാനുവലായി കോൺഫിഗർ ചെയ്യുക:

1. **സജ്ജീകരണങ്ങൾ തുറക്കുക**: സജ്ജീകരണങ്ങൾ (ഗിയർ ഐക്കൺ) ക്ലിക്ക് ചെയ്യുക
2. **ബന്ധങ്ങൾ തുറക്കുക**: സജ്ജീകരണങ്ങൾ → ബന്ധങ്ങൾ → OpenAI
3. **API വിശദാംശങ്ങൾ നൽകുക**:
   - API ബേസ് URL: `http://host.docker.internal:51211/v1`
   - API കീ: `foundry-local-key` (ഏതെങ്കിലും മൂല്യം പ്രവർത്തിക്കും)
4. **സേവ് ചെയ്ത് പരീക്ഷിക്കുക**: "Save" ക്ലിക്ക് ചെയ്ത് മോഡലിൽ പരീക്ഷിക്കുക

### സ്ഥിരമായ ഡാറ്റ സംഭരണം

സംഭാഷണങ്ങളും സജ്ജീകരണങ്ങളും സ്ഥിരമായി സൂക്ഷിക്കാൻ:

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

## പ്രശ്നപരിഹാരം

### ബന്ധം പ്രശ്നങ്ങൾ

**പ്രശ്നം**: "Connection refused" അല്ലെങ്കിൽ മോഡലുകൾ ലോഡ് ചെയ്യാത്തത്

**പരിഹാരങ്ങൾ**:
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

### മോഡൽ കാണാനില്ല

**പ്രശ്നം**: Open WebUI ഡ്രോപ്പ്ഡൗണിൽ മോഡലുകൾ കാണിക്കുന്നില്ല

**ഡീബഗിംഗ് ഘട്ടങ്ങൾ**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**പരിഹാരം**: മോഡൽ ശരിയായി ലോഡ് ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker നെറ്റ്‌വർക്ക് പ്രശ്നങ്ങൾ

**പ്രശ്നം**: `host.docker.internal` പരിഹരിക്കാനാകാത്തത്

**Windows പരിഹാരം**:
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

**മാറ്റുവഴി**: നിങ്ങളുടെ മെഷീന്റെ IP കണ്ടെത്തുക:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### പ്രകടന പ്രശ്നങ്ങൾ

**മന്ദഗതിയുള്ള പ്രതികരണങ്ങൾ**:
1. മോഡൽ GPU ആക്സിലറേഷൻ ഉപയോഗിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക: `foundry service ps`
2. മതിയായ സിസ്റ്റം വിഭവങ്ങൾ (RAM/GPU മെമ്മറി) ഉറപ്പാക്കുക
3. പരീക്ഷണത്തിനായി ചെറിയ മോഡൽ ഉപയോഗിക്കാൻ പരിഗണിക്കുക

**മെമ്മറി പ്രശ്നങ്ങൾ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## ഉപയോഗ മാർഗ്ഗനിർദ്ദേശം

### അടിസ്ഥാന ചാറ്റ്

1. **മോഡൽ തിരഞ്ഞെടുക്കുക**: ഡ്രോപ്പ്ഡൗണിൽ നിന്ന് തിരഞ്ഞെടുക്കുക (Foundry Local മോഡലുകൾ കാണിക്കും)
2. **സന്ദേശം ടൈപ്പ് ചെയ്യുക**: താഴെ ടെക്സ്റ്റ് ഇൻപുട്ട് ഉപയോഗിക്കുക
3. **അയയ്ക്കുക**: Enter അമർത്തുക അല്ലെങ്കിൽ Send ബട്ടൺ ക്ലിക്ക് ചെയ്യുക
4. **പ്രതികരണം കാണുക**: സ്ട്രീമിംഗ് പ്രതികരണം യഥാർത്ഥ സമയത്ത് കാണുക

### ആധുനിക ഫീച്ചറുകൾ

**ഫയൽ അപ്‌ലോഡ്**:
1. പേപ്പർക്ലിപ്പ് ഐക്കൺ ക്ലിക്ക് ചെയ്യുക
2. ഡോക്യുമെന്റ് അപ്‌ലോഡ് ചെയ്യുക (PDF, TXT, മുതലായവ)
3. ഉള്ളടക്കത്തെക്കുറിച്ച് ചോദ്യങ്ങൾ ചോദിക്കുക
4. മോഡൽ ഡോക്യുമെന്റ് അനാലൈസ് ചെയ്ത് പ്രതികരിക്കും

**കസ്റ്റം സിസ്റ്റം പ്രോംപ്റ്റുകൾ**:
1. സജ്ജീകരണങ്ങൾ → വ്യക്തിഗതമാക്കൽ
2. കസ്റ്റം സിസ്റ്റം പ്രോംപ്റ്റ് സജ്ജമാക്കുക
3. സ്ഥിരമായ AI വ്യക്തിത്വം/പ്രവർത്തനം സൃഷ്ടിക്കും

**സംഭാഷണ മാനേജ്മെന്റ്**:
- **പുതിയ ചാറ്റ്**: "+" ക്ലിക്ക് ചെയ്ത് പുതിയ സംഭാഷണം ആരംഭിക്കുക
- **ചാറ്റ് ചരിത്രം**: സൈഡ്ബാറിൽ നിന്ന് മുൻ സംഭാഷണങ്ങൾ ആക്‌സസ് ചെയ്യുക
- **എക്സ്പോർട്ട്**: ചാറ്റ് ചരിത്രം ടെക്സ്റ്റ്/JSON ആയി ഡൗൺലോഡ് ചെയ്യുക

**മോഡൽ താരതമ്യം**:
1. ഒരേ Open WebUI-യുടെ പല ബ്രൗസർ ടാബുകൾ തുറക്കുക
2. ഓരോ ടാബിലും വ്യത്യസ്ത മോഡലുകൾ തിരഞ്ഞെടുക്കുക
3. ഒരേ പ്രോംപ്റ്റുകൾക്ക് ലഭിക്കുന്ന പ്രതികരണങ്ങൾ താരതമ്യം ചെയ്യുക

### ഇന്റഗ്രേഷൻ പാറ്റേണുകൾ

**ഡെവലപ്പ്മെന്റ് വർക്ക്‌ഫ്ലോ**:
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

## പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ്

### സുരക്ഷിത സജ്ജീകരണം

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

### മൾട്ടി-ഉപയോക്തൃ സജ്ജീകരണം

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

### നിരീക്ഷണവും ലോഗിംഗും

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ക്ലീനപ്പ്

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

## അടുത്ത ഘട്ടങ്ങൾ

### മെച്ചപ്പെടുത്തൽ ആശയങ്ങൾ

1. **കസ്റ്റം മോഡലുകൾ**: നിങ്ങളുടെ സ്വന്തം ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡലുകൾ Foundry Local-ലേക്ക് ചേർക്കുക
2. **API ഇന്റഗ്രേഷൻ**: Open WebUI ഫംഗ്ഷനുകൾ വഴി ബാഹ്യ API-കളുമായി ബന്ധിപ്പിക്കുക
3. **ഡോക്യുമെന്റ് പ്രോസസ്സിംഗ്**: ആധുനിക RAG പൈപ്പ്‌ലൈൻ സജ്ജമാക്കുക
4. **മൾട്ടി-മോഡൽ**: ദൃശ്യ മോഡലുകൾ ഇമേജ് വിശകലനത്തിനായി കോൺഫിഗർ ചെയ്യുക

### സ്കെയിലിംഗ് പരിഗണനകൾ

- **ലോഡ് ബാലൻസിംഗ്**: റിവേഴ്സ് പ്രോക്സി പിന്നിൽ പല Foundry Local ഇൻസ്റ്റൻസുകളും
- **മോഡൽ റൂട്ടിംഗ്**: വ്യത്യസ്ത ഉപയോഗങ്ങൾക്ക് വ്യത്യസ്ത മോഡലുകൾ
- **വിഭവ മാനേജ്മെന്റ്**: സമകാലിക ഉപയോക്താക്കൾക്കായി GPU മെമ്മറി ഓപ്റ്റിമൈസേഷൻ
- **ബാക്കപ്പ് തന്ത്രം**: സംഭാഷണ ഡാറ്റയും കോൺഫിഗറേഷനുകളും নিয়മിതമായി ബാക്കപ്പ് എടുക്കുക

## റഫറൻസുകൾ

- [Open WebUI ഡോക്യുമെന്റേഷൻ](https://docs.openwebui.com/)
- [Open WebUI GitHub റിപോസിറ്ററി](https://github.com/open-webui/open-webui)
- [Foundry Local ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker ഇൻസ്റ്റലേഷൻ ഗൈഡ്](https://docs.docker.com/get-docker/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->