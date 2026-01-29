# Gabay sa Pagsasama ng Open WebUI + Foundry Local

Ang gabay na ito ay nagpapakita kung paano ikonekta ang Open WebUI sa Microsoft Foundry Local para sa isang propesyonal na interface na parang ChatGPT na pinapagana ng iyong mga lokal na AI model.

## Pangkalahatang-ideya

Ang Open WebUI ay nagbibigay ng modernong, madaling gamitin na chat interface na maaaring ikonekta sa anumang OpenAI-compatible na API. Sa pamamagitan ng pagkonekta nito sa Foundry Local, makakakuha ka ng:

- **Propesyonal na UI**: Interface na parang ChatGPT na may modernong disenyo  
- **Lokal na Privacy**: Lahat ng pagproseso ay nangyayari sa iyong device  
- **Pagpapalit ng Modelo**: Madaling pagpapalit sa pagitan ng iba't ibang lokal na modelo  
- **Kasaysayan ng Usapan**: Permanenteng kasaysayan ng chat at konteksto  
- **Pag-upload ng File**: Kakayahang mag-analisa ng dokumento at magproseso ng file  
- **Custom na Persona**: Mga system prompt at pag-customize ng role  

## Mga Kinakailangan

### Kinakailangang Software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Mag-load ng Modelo

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Mabilisang Setup (Inirerekomenda)

### Hakbang 1: Patakbuhin ang Open WebUI gamit ang Docker

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

### Hakbang 2: Paunang Setup

1. **Buksan ang Browser**: Pumunta sa `http://localhost:3000`  
2. **Gumawa ng Account**: Mag-set up ng admin user (ang unang user ay magiging admin)  
3. **I-verify ang Koneksyon**: Ang mga modelo ay dapat awtomatikong lumitaw sa dropdown  

### Hakbang 3: Subukan ang Koneksyon

1. Piliin ang iyong modelo mula sa dropdown (hal., "phi-4-mini")  
2. Mag-type ng test message: "Hello! Can you introduce yourself?"  
3. Dapat kang makakita ng streaming na tugon mula sa iyong lokal na modelo  

## Advanced na Konpigurasyon

### Mga Environment Variable

| Variable | Layunin | Default | Halimbawa |
|----------|---------|---------|-----------|
| `OPENAI_API_BASE_URL` | Endpoint ng Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (kailangan ngunit hindi ginagamit nang lokal) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Session encryption key | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | Payagan ang bagong user registration | `True` | `False` |

### Manual na Konpigurasyon (Alternatibo)

Kung hindi gumagana ang mga environment variable, mag-configure nang manu-mano:

1. **Buksan ang Settings**: I-click ang Settings (gear icon)  
2. **Pumunta sa Connections**: Settings → Connections → OpenAI  
3. **I-set ang API Details**:  
   - API Base URL: `http://host.docker.internal:51211/v1`  
   - API Key: `foundry-local-key` (anumang halaga ay gagana)  
4. **I-save at Subukan**: I-click ang "Save" pagkatapos ay subukan gamit ang isang modelo  

### Permanenteng Imbakan ng Data

Upang mapanatili ang mga usapan at settings:

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

## Pag-aayos ng Problema

### Mga Isyu sa Koneksyon

**Problema**: "Connection refused" o hindi naglo-load ang mga modelo  

**Mga Solusyon**:  
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

### Hindi Lumilitaw ang Modelo

**Problema**: Walang modelo sa dropdown ng Open WebUI  

**Mga Hakbang sa Pag-debug**:  
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Ayos**: Siguraduhing maayos na na-load ang modelo:  
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Mga Isyu sa Docker Network

**Problema**: Hindi nareresolba ang `host.docker.internal`  

**Solusyon sa Windows**:  
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

**Alternatibo**: Hanapin ang IP ng iyong makina:  
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Mga Isyu sa Performance

**Mabagal na Tugon**:  
1. Siguraduhing gumagamit ng GPU acceleration ang modelo: `foundry service ps`  
2. Tiyaking sapat ang system resources (RAM/GPU memory)  
3. Isaalang-alang ang paggamit ng mas maliit na modelo para sa pagsubok  

**Mga Isyu sa Memorya**:  
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Gabay sa Paggamit

### Pangunahing Chat

1. **Piliin ang Modelo**: Pumili mula sa dropdown (ipinapakita ang mga modelo ng Foundry Local)  
2. **Mag-type ng Mensahe**: Gamitin ang text input sa ibaba  
3. **Ipadala**: Pindutin ang Enter o i-click ang Send button  
4. **Tingnan ang Tugon**: Makikita ang streaming na tugon sa real-time  

### Mga Advanced na Tampok

**Pag-upload ng File**:  
1. I-click ang paperclip icon  
2. Mag-upload ng dokumento (PDF, TXT, atbp.)  
3. Magtanong tungkol sa nilalaman  
4. I-aanalisa ng modelo at tutugon batay sa dokumento  

**Custom na System Prompts**:  
1. Settings → Personalization  
2. Mag-set ng custom na system prompt  
3. Lumilikha ng pare-parehong personalidad/ugali ng AI  

**Pamamahala ng Usapan**:  
- **Bagong Chat**: I-click ang "+" para magsimula ng bagong usapan  
- **Kasaysayan ng Chat**: I-access ang mga nakaraang usapan mula sa sidebar  
- **I-export**: I-download ang kasaysayan ng chat bilang text/JSON  

**Paghahambing ng Modelo**:  
1. Buksan ang maraming browser tab sa parehong Open WebUI  
2. Pumili ng iba't ibang modelo sa bawat tab  
3. Ihambing ang mga tugon sa parehong prompt  

### Mga Pattern ng Integrasyon

**Workflow ng Pag-develop**:  
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

## Deployment sa Produksyon

### Secure na Setup

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

### Multi-User Setup

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

### Monitoring at Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Paglilinis

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

## Mga Susunod na Hakbang

### Mga Ideya para sa Pagpapahusay

1. **Custom na Modelo**: Magdagdag ng sarili mong fine-tuned na mga modelo sa Foundry Local  
2. **API Integration**: Ikonekta sa mga external na API gamit ang mga function ng Open WebUI  
3. **Pagproseso ng Dokumento**: Mag-set up ng advanced na RAG pipelines  
4. **Multi-Modal**: I-configure ang mga vision model para sa pagsusuri ng imahe  

### Mga Pagsasaalang-alang sa Scaling

- **Load Balancing**: Maramihang Foundry Local instances sa likod ng reverse proxy  
- **Model Routing**: Iba't ibang modelo para sa iba't ibang use case  
- **Resource Management**: Pag-optimize ng GPU memory para sa sabay-sabay na mga user  
- **Backup Strategy**: Regular na pag-backup ng data ng usapan at mga configuration  

## Mga Sanggunian

- [Open WebUI Documentation](https://docs.openwebui.com/)  
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)  
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)  
- [Docker Installation Guide](https://docs.docker.com/get-docker/)  

---

