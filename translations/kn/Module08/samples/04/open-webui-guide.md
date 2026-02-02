# Open WebUI + Foundry Local ಸಂಯೋಜನೆ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ Open WebUI ಅನ್ನು Microsoft Foundry Local ಗೆ ಸಂಪರ್ಕಿಸುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ, ಇದು ನಿಮ್ಮ ಸ್ಥಳೀಯ AI ಮಾದರಿಗಳಿಂದ ಚಾಲಿತ ವೃತ್ತಿಪರ ChatGPT-ಹಾಗಿನ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

Open WebUI ಯಾವುದೇ OpenAI-ಸಮ್ಮತ API ಗೆ ಸಂಪರ್ಕಿಸಬಹುದಾದ ಆಧುನಿಕ, ಬಳಕೆದಾರ ಸ್ನೇಹಿ ಚಾಟ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ. Foundry Local ಗೆ ಸಂಪರ್ಕಿಸುವ ಮೂಲಕ, ನೀವು ಪಡೆಯುತ್ತೀರಿ:

- **ವೃತ್ತಿಪರ UI**: ಆಧುನಿಕ ವಿನ್ಯಾಸದ ChatGPT-ಹಾಗಿನ ಇಂಟರ್ಫೇಸ್
- **ಸ್ಥಳೀಯ ಗೌಪ್ಯತೆ**: ಎಲ್ಲಾ ಪ್ರಕ್ರಿಯೆ ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ನಡೆಯುತ್ತದೆ
- **ಮಾದರಿ ಬದಲಾವಣೆ**: ವಿಭಿನ್ನ ಸ್ಥಳೀಯ ಮಾದರಿಗಳ ನಡುವೆ ಸುಲಭ ಬದಲಾವಣೆ
- **ಸಂವಾದ ಇತಿಹಾಸ**: ಸ್ಥಿರ ಚಾಟ್ ಇತಿಹಾಸ ಮತ್ತು ಸಂದರ್ಭ
- **ಫೈಲ್ ಅಪ್ಲೋಡ್‌ಗಳು**: ಡಾಕ್ಯುಮೆಂಟ್ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಫೈಲ್ ಪ್ರಕ್ರಿಯೆ ಸಾಮರ್ಥ್ಯಗಳು
- **ಕಸ್ಟಮ್ ವ್ಯಕ್ತಿತ್ವಗಳು**: ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಪಾತ್ರ ಕಸ್ಟಮೈಜೆಷನ್

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

### ಅಗತ್ಯ ಸಾಫ್ಟ್‌ವೇರ್

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ಮಾದರಿ ಲೋಡ್ ಮಾಡುವುದು

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## ತ್ವರಿತ ಸೆಟ್‌ಅಪ್ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)

### ಹಂತ 1: ಡೋಕರ್‌ನೊಂದಿಗೆ Open WebUI ಅನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

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

### ಹಂತ 2: ಪ್ರಾಥಮಿಕ ಸೆಟ್‌ಅಪ್

1. **ಬ್ರೌಸರ್ ತೆರೆಯಿರಿ**: `http://localhost:3000` ಗೆ ಹೋಗಿ
2. **ಖಾತೆ ರಚಿಸಿ**: ಆಡಳಿತ ಬಳಕೆದಾರರನ್ನು ಸೆಟ್ ಮಾಡಿ (ಮೊದಲ ಬಳಕೆದಾರರು ಆಡಳಿತಗಾರರಾಗುತ್ತಾರೆ)
3. **ಸಂಪರ್ಕ ಪರಿಶೀಲನೆ**: ಮಾದರಿಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಡ್ರಾಪ್‌ಡೌನ್‌ನಲ್ಲಿ ಕಾಣಿಸಬೇಕು

### ಹಂತ 3: ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ

1. ಡ್ರಾಪ್‌ಡೌನ್‌ನಿಂದ ನಿಮ್ಮ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ (ಉದಾ: "phi-4-mini")
2. ಪರೀಕ್ಷಾ ಸಂದೇಶವನ್ನು ಟೈಪ್ ಮಾಡಿ: "ನಮಸ್ಕಾರ! ನೀವು ನಿಮ್ಮ ಪರಿಚಯ ನೀಡಬಹುದುವೇ?"
3. ನಿಮ್ಮ ಸ್ಥಳೀಯ ಮಾದರಿಯಿಂದ ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೀವು ನೋಡಬಹುದು

## ಉನ್ನತ ಸಂರಚನೆ

### ಪರಿಸರ ಚರಗಳು

| ಚರ | ಉದ್ದೇಶ | ಡೀಫಾಲ್ಟ್ | ಉದಾಹರಣೆ |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local ಎಂಡ್‌ಪಾಯಿಂಟ್ | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API ಕೀ (ಸ್ಥಳೀಯವಾಗಿ ಬಳಸಲಾಗುವುದಿಲ್ಲ) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | ಸೆಷನ್ ಎನ್‌ಕ್ರಿಪ್ಷನ್ ಕೀ | ಸ್ವಯಂ-ಉತ್ಪಾದಿತ | `your-secret-key` |
| `ENABLE_SIGNUP` | ಹೊಸ ಬಳಕೆದಾರ ನೋಂದಣಿಗೆ ಅನುಮತಿ | `True` | `False` |

### ಕೈಯಿಂದ ಸಂರಚನೆ (ವೈಕಲ್ಪಿಕ)

ಪರಿಸರ ಚರಗಳು ಕೆಲಸ ಮಾಡದಿದ್ದರೆ, ಕೈಯಿಂದ ಸಂರಚಿಸಿ:

1. **ಸೆಟ್ಟಿಂಗ್ಸ್ ತೆರೆಯಿರಿ**: ಸೆಟ್ಟಿಂಗ್ಸ್ (ಗಿಯರ್ ಐಕಾನ್) ಕ್ಲಿಕ್ ಮಾಡಿ
2. **ಸಂಪರ್ಕಗಳಿಗೆ ಹೋಗಿ**: ಸೆಟ್ಟಿಂಗ್ಸ್ → ಸಂಪರ್ಕಗಳು → OpenAI
3. **API ವಿವರಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ**:
   - API ಬೇಸ್ URL: `http://host.docker.internal:51211/v1`
   - API ಕೀ: `foundry-local-key` (ಯಾವುದೇ ಮೌಲ್ಯ ಕೆಲಸ ಮಾಡುತ್ತದೆ)
4. **ಉಳಿಸಿ ಮತ್ತು ಪರೀಕ್ಷಿಸಿ**: "ಉಳಿಸಿ" ಕ್ಲಿಕ್ ಮಾಡಿ ನಂತರ ಮಾದರಿಯೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ

### ಸ್ಥಿರ ಡೇಟಾ ಸಂಗ್ರಹಣೆ

ಸಂವಾದಗಳು ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಸ್ ಅನ್ನು ಸ್ಥಿರಗೊಳಿಸಲು:

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

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳು

**ಸಮಸ್ಯೆ**: "ಸಂಪರ್ಕ ನಿರಾಕರಿಸಲಾಗಿದೆ" ಅಥವಾ ಮಾದರಿಗಳು ಲೋಡ್ ಆಗುತ್ತಿಲ್ಲ

**ಪರಿಹಾರಗಳು**:
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

### ಮಾದರಿ ಕಾಣಿಸದಿರುವುದು

**ಸಮಸ್ಯೆ**: Open WebUI ಡ್ರಾಪ್‌ಡೌನ್‌ನಲ್ಲಿ ಯಾವುದೇ ಮಾದರಿಗಳನ್ನು ತೋರಿಸುವುದಿಲ್ಲ

**ಡಿಬಗ್ ಹಂತಗಳು**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**ಪರಿಹಾರ**: ಮಾದರಿ ಸರಿಯಾಗಿ ಲೋಡ್ ಆಗಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### ಡೋಕರ್ ನೆಟ್‌ವರ್ಕ್ ಸಮಸ್ಯೆಗಳು

**ಸಮಸ್ಯೆ**: `host.docker.internal` ಪರಿಹರಿಸಲಾಗುತ್ತಿಲ್ಲ

**Windows ಪರಿಹಾರ**:
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

**ವೈಕಲ್ಪಿಕ**: ನಿಮ್ಮ ಯಂತ್ರದ IP ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳು

**ಮಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳು**:
1. ಮಾದರಿ GPU ವೇಗವರ್ಧನೆ ಬಳಸುತ್ತಿರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ: `foundry service ps`
2. ಸಾಕಷ್ಟು ಸಿಸ್ಟಮ್ ಸಂಪನ್ಮೂಲಗಳು (RAM/GPU ಮೆಮೊರಿ) ಇದ್ದಾರೆ ಎಂದು ಖಚಿತಪಡಿಸಿ
3. ಪರೀಕ್ಷೆಗೆ ಸಣ್ಣ ಮಾದರಿಯನ್ನು ಬಳಸುವುದನ್ನು ಪರಿಗಣಿಸಿ

**ಮೆಮೊರಿ ಸಮಸ್ಯೆಗಳು**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## ಬಳಕೆ ಮಾರ್ಗದರ್ಶಿ

### ಮೂಲ ಚಾಟ್

1. **ಮಾದರಿ ಆಯ್ಕೆಮಾಡಿ**: ಡ್ರಾಪ್‌ಡೌನ್‌ನಿಂದ ಆಯ್ಕೆಮಾಡಿ (Foundry Local ಮಾದರಿಗಳನ್ನು ತೋರಿಸುತ್ತದೆ)
2. **ಸಂದೇಶ ಟೈಪ್ ಮಾಡಿ**: ಕೆಳಗಿನ ಪಠ್ಯ ಇನ್‌ಪುಟ್ ಬಳಸಿ
3. **ಕಳುಹಿಸಿ**: ಎಂಟರ್ ಒತ್ತಿ ಅಥವಾ ಕಳುಹಿಸಿ ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ
4. **ಪ್ರತಿಕ್ರಿಯೆ ನೋಡಿ**: ನೈಜ ಸಮಯದಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಿ

### ಉನ್ನತ ವೈಶಿಷ್ಟ್ಯಗಳು

**ಫೈಲ್ ಅಪ್ಲೋಡ್**:
1. ಪೇಪರ್‌ಕ್ಲಿಪ್ ಐಕಾನ್ ಕ್ಲಿಕ್ ಮಾಡಿ
2. ಡಾಕ್ಯುಮೆಂಟ್ ಅಪ್ಲೋಡ್ ಮಾಡಿ (PDF, TXT, ಇತ್ಯಾದಿ)
3. ವಿಷಯದ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಿ
4. ಮಾದರಿ ಡಾಕ್ಯುಮೆಂಟ್ ಆಧಾರಿತವಾಗಿ ವಿಶ್ಲೇಷಿಸಿ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ

**ಕಸ್ಟಮ್ ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು**:
1. ಸೆಟ್ಟಿಂಗ್ಸ್ → ವೈಯಕ್ತೀಕರಣ
2. ಕಸ್ಟಮ್ ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್ ಮಾಡಿ
3. ಸತತ AI ವ್ಯಕ್ತಿತ್ವ/ನಡವಳಿಕೆ ರಚಿಸುತ್ತದೆ

**ಸಂವಾದ ನಿರ್ವಹಣೆ**:
- **ಹೊಸ ಚಾಟ್**: ಹೊಸ ಸಂವಾದ ಆರಂಭಿಸಲು "+" ಕ್ಲಿಕ್ ಮಾಡಿ
- **ಚಾಟ್ ಇತಿಹಾಸ**: ಸೈಡ್‌ಬಾರ್‌ನಿಂದ ಹಿಂದಿನ ಸಂವಾದಗಳನ್ನು ಪ್ರವೇಶಿಸಿ
- **ರಫ್ತು**: ಚಾಟ್ ಇತಿಹಾಸವನ್ನು ಪಠ್ಯ/JSON ಆಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ

**ಮಾದರಿ ಹೋಲಿಕೆ**:
1. ಒಂದೇ Open WebUI ಗೆ ಹಲವಾರು ಬ್ರೌಸರ್ ಟ್ಯಾಬ್‌ಗಳನ್ನು ತೆರೆಯಿರಿ
2. ಪ್ರತಿ ಟ್ಯಾಬ್‌ನಲ್ಲಿ ವಿಭಿನ್ನ ಮಾದರಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ
3. ಒಂದೇ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಹೋಲಿಸಿ

### ಸಂಯೋಜನೆ ಮಾದರಿಗಳು

**ವಿಕಸನ ಕಾರ್ಯಪ್ರವಾಹ**:
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

## ಉತ್ಪಾದನಾ ನಿಯೋಜನೆ

### ಸುರಕ್ಷಿತ ಸೆಟ್‌ಅಪ್

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

### ಬಹು-ಬಳಕೆದಾರ ಸೆಟ್‌ಅಪ್

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

### ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಲಾಗಿಂಗ್

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ಶುದ್ಧೀಕರಣ

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

## ಮುಂದಿನ ಹಂತಗಳು

### ಸುಧಾರಣೆ ಆಲೋಚನೆಗಳು

1. **ಕಸ್ಟಮ್ ಮಾದರಿಗಳು**: ನಿಮ್ಮ ಸ್ವಂತ ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜಿತ ಮಾದರಿಗಳನ್ನು Foundry Local ಗೆ ಸೇರಿಸಿ
2. **API ಸಂಯೋಜನೆ**: Open WebUI ಕಾರ್ಯಗಳ ಮೂಲಕ ಬಾಹ್ಯ API ಗಳಿಗೆ ಸಂಪರ್ಕಿಸಿ
3. **ಡಾಕ್ಯುಮೆಂಟ್ ಪ್ರಕ್ರಿಯೆ**: ಉನ್ನತ RAG ಪೈಪ್ಲೈನ್ಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ
4. **ಬಹು-ಮೋಡಲ್**: ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಗೆ ದೃಷ್ಟಿ ಮಾದರಿಗಳನ್ನು ಸಂರಚಿಸಿ

### ವಿಸ್ತರಣೆ ಪರಿಗಣನೆಗಳು

- **ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್**: ರಿವರ್ಸ್ ಪ್ರಾಕ್ಸಿ ಹಿಂದೆ ಹಲವಾರು Foundry Local ಉದಾಹರಣೆಗಳು
- **ಮಾದರಿ ಮಾರ್ಗದರ್ಶನ**: ವಿಭಿನ್ನ ಬಳಕೆಗಳಿಗೆ ವಿಭಿನ್ನ ಮಾದರಿಗಳು
- **ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆ**: ಸಮಕಾಲೀನ ಬಳಕೆದಾರರಿಗಾಗಿ GPU ಮೆಮೊರಿ ಆಪ್ಟಿಮೈಜೆಷನ್
- **ಬ್ಯಾಕಪ್ ತಂತ್ರಜ್ಞಾನ**: ಸಂವಾದ ಡೇಟಾ ಮತ್ತು ಸಂರಚನೆಗಳ ನಿಯಮಿತ ಬ್ಯಾಕಪ್

## ಉಲ್ಲೇಖಗಳು

- [Open WebUI ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://docs.openwebui.com/)
- [Open WebUI GitHub ರೆಪೊ](https://github.com/open-webui/open-webui)
- [Foundry Local ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [ಡೋಕರ್ ಸ್ಥಾಪನೆ ಮಾರ್ಗದರ್ಶಿ](https://docs.docker.com/get-docker/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->