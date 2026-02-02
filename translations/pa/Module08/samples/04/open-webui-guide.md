# Open WebUI + Foundry Local ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ Open WebUI ਨੂੰ Microsoft Foundry Local ਨਾਲ ਕਿਵੇਂ ਜੋੜਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਸਥਾਨਕ AI ਮਾਡਲਾਂ ਦੁਆਰਾ ਸੰਚਾਲਿਤ ਇੱਕ ਪੇਸ਼ੇਵਰ ChatGPT-ਜੈਸਾ ਇੰਟਰਫੇਸ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ।

## ਝਲਕ

Open WebUI ਇੱਕ ਆਧੁਨਿਕ, ਵਰਤੋਂਕਾਰ-ਅਨੁਕੂਲ ਚੈਟ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਕਿਸੇ ਵੀ OpenAI-ਅਨੁਕੂਲ API ਨਾਲ ਜੁੜ ਸਕਦਾ ਹੈ। ਇਸਨੂੰ Foundry Local ਨਾਲ ਜੋੜ ਕੇ, ਤੁਹਾਨੂੰ ਮਿਲਦਾ ਹੈ:

- **ਪੇਸ਼ੇਵਰ UI**: ChatGPT-ਜੈਸਾ ਇੰਟਰਫੇਸ ਆਧੁਨਿਕ ਡਿਜ਼ਾਇਨ ਨਾਲ
- **ਸਥਾਨਕ ਗੋਪਨੀਯਤਾ**: ਸਾਰਾ ਪ੍ਰੋਸੈਸਿੰਗ ਤੁਹਾਡੇ ਡਿਵਾਈਸ 'ਤੇ ਹੁੰਦੀ ਹੈ
- **ਮਾਡਲ ਸਵਿੱਚਿੰਗ**: ਵੱਖ-ਵੱਖ ਸਥਾਨਕ ਮਾਡਲਾਂ ਵਿੱਚ ਆਸਾਨ ਸਵਿੱਚਿੰਗ
- **ਗੱਲਬਾਤ ਦਾ ਇਤਿਹਾਸ**: ਸਥਾਈ ਚੈਟ ਇਤਿਹਾਸ ਅਤੇ ਸੰਦਰਭ
- **ਫਾਈਲ ਅੱਪਲੋਡ**: ਦਸਤਾਵੇਜ਼ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਫਾਈਲ ਪ੍ਰੋਸੈਸਿੰਗ ਸਮਰੱਥਾ
- **ਕਸਟਮ ਪੁਰਸਨਾਸ**: ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਅਤੇ ਭੂਮਿਕਾ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

### ਲੋੜੀਂਦਾ ਸੌਫਟਵੇਅਰ

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ਮਾਡਲ ਲੋਡ ਕਰੋ

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## ਤੁਰੰਤ ਸੈਟਅਪ (ਸਿਫਾਰਸ਼ੀ)

### ਪਦਅੰਤਰ 1: Docker ਨਾਲ Open WebUI ਚਲਾਓ

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

### ਪਦਅੰਤਰ 2: ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ

1. **ਬ੍ਰਾਊਜ਼ਰ ਖੋਲ੍ਹੋ**: `http://localhost:3000` 'ਤੇ ਜਾਓ
2. **ਖਾਤਾ ਬਣਾਓ**: ਐਡਮਿਨ ਯੂਜ਼ਰ ਸੈਟਅਪ ਕਰੋ (ਪਹਿਲਾ ਯੂਜ਼ਰ ਐਡਮਿਨ ਬਣਦਾ ਹੈ)
3. **ਕਨੈਕਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ**: ਮਾਡਲ ਆਪਣੇ ਆਪ ਡ੍ਰਾਪਡਾਊਨ ਵਿੱਚ ਦਿਖਾਈ ਦੇਣੇ ਚਾਹੀਦੇ ਹਨ

### ਪਦਅੰਤਰ 3: ਕਨੈਕਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ

1. ਡ੍ਰਾਪਡਾਊਨ ਵਿੱਚੋਂ ਆਪਣਾ ਮਾਡਲ ਚੁਣੋ (ਜਿਵੇਂ "phi-4-mini")
2. ਇੱਕ ਟੈਸਟ ਸੁਨੇਹਾ ਲਿਖੋ: "ਹੈਲੋ! ਕੀ ਤੁਸੀਂ ਆਪਣਾ ਪਰੀਚੇ ਦੇ ਸਕਦੇ ਹੋ?"
3. ਤੁਹਾਨੂੰ ਆਪਣੇ ਸਥਾਨਕ ਮਾਡਲ ਤੋਂ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ ਮਿਲਣਾ ਚਾਹੀਦਾ ਹੈ

## ਉੱਚ-ਸਤਹੀ ਸੰਰਚਨਾ

### ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

| ਵੈਰੀਏਬਲ | ਉਦੇਸ਼ | ਡਿਫਾਲਟ | ਉਦਾਹਰਨ |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local ਐਂਡਪੌਇੰਟ | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API ਕੁੰਜੀ (ਲੋੜੀਂਦੀ ਪਰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਵਰਤੋਂ ਨਹੀਂ ਹੁੰਦੀ) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | ਸੈਸ਼ਨ ਇਨਕ੍ਰਿਪਸ਼ਨ ਕੁੰਜੀ | ਆਟੋ-ਜਨਰੇਟ ਕੀਤੀ | `your-secret-key` |
| `ENABLE_SIGNUP` | ਨਵੇਂ ਯੂਜ਼ਰ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ | `True` | `False` |

### ਮੈਨੁਅਲ ਸੰਰਚਨਾ (ਵਿਕਲਪ)

ਜੇਕਰ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਕੰਮ ਨਹੀਂ ਕਰਦੇ, ਤਾਂ ਮੈਨੁਅਲ ਤੌਰ 'ਤੇ ਸੰਰਚਨਾ ਕਰੋ:

1. **ਸੈਟਿੰਗ ਖੋਲ੍ਹੋ**: ਸੈਟਿੰਗ (ਗਿਅਰ ਆਈਕਨ) 'ਤੇ ਕਲਿਕ ਕਰੋ
2. **ਕਨੈਕਸ਼ਨ 'ਤੇ ਜਾਓ**: ਸੈਟਿੰਗ → ਕਨੈਕਸ਼ਨ → OpenAI
3. **API ਵੇਰਵੇ ਸੈਟ ਕਰੋ**:
   - API ਬੇਸ URL: `http://host.docker.internal:51211/v1`
   - API ਕੁੰਜੀ: `foundry-local-key` (ਕੋਈ ਵੀ ਮੁੱਲ ਕੰਮ ਕਰਦਾ ਹੈ)
4. **ਸੇਵ ਅਤੇ ਟੈਸਟ ਕਰੋ**: "ਸੇਵ" 'ਤੇ ਕਲਿਕ ਕਰੋ ਅਤੇ ਮਾਡਲ ਨਾਲ ਟੈਸਟ ਕਰੋ

### ਸਥਾਈ ਡਾਟਾ ਸਟੋਰੇਜ

ਗੱਲਬਾਤਾਂ ਅਤੇ ਸੈਟਿੰਗਾਂ ਨੂੰ ਸਥਾਈ ਬਣਾਉਣ ਲਈ:

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

## ਸਮੱਸਿਆ ਹੱਲ

### ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ**: "ਕਨੈਕਸ਼ਨ ਰਿਫਿਊਜ਼ਡ" ਜਾਂ ਮਾਡਲ ਲੋਡ ਨਹੀਂ ਹੋ ਰਹੇ

**ਹੱਲ**:
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

### ਮਾਡਲ ਦਿਖਾਈ ਨਹੀਂ ਦੇ ਰਿਹਾ

**ਸਮੱਸਿਆ**: Open WebUI ਡ੍ਰਾਪਡਾਊਨ ਵਿੱਚ ਕੋਈ ਮਾਡਲ ਨਹੀਂ ਦਿਖਾਉਂਦਾ

**ਡਿਬੱਗਿੰਗ ਕਦਮ**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**ਸੁਧਾਰ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਮਾਡਲ ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਲੋਡ ਕੀਤਾ ਗਿਆ ਹੈ:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker ਨੈਟਵਰਕ ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ**: `host.docker.internal` ਹੱਲ ਨਹੀਂ ਹੋ ਰਿਹਾ

**Windows ਹੱਲ**:
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

**ਵਿਕਲਪ**: ਆਪਣੀ ਮਸ਼ੀਨ ਦਾ IP ਲੱਭੋ:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### ਪ੍ਰਦਰਸ਼ਨ ਸਮੱਸਿਆਵਾਂ

**ਧੀਮੇ ਜਵਾਬ**:
1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਮਾਡਲ GPU ਐਕਸਲੇਰੇਸ਼ਨ ਵਰਤ ਰਿਹਾ ਹੈ: `foundry service ps`
2. ਪ੍ਰਯਾਪਤ ਸਿਸਟਮ ਸਰੋਤਾਂ (RAM/GPU ਮੈਮੋਰੀ) ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
3. ਟੈਸਟਿੰਗ ਲਈ ਛੋਟਾ ਮਾਡਲ ਵਰਤਣ 'ਤੇ ਵਿਚਾਰ ਕਰੋ

**ਮੈਮੋਰੀ ਸਮੱਸਿਆਵਾਂ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## ਵਰਤੋਂ ਗਾਈਡ

### ਬੁਨਿਆਦੀ ਚੈਟ

1. **ਮਾਡਲ ਚੁਣੋ**: ਡ੍ਰਾਪਡਾਊਨ ਵਿੱਚੋਂ ਚੁਣੋ (Foundry Local ਮਾਡਲ ਦਿਖਾਉਂਦਾ ਹੈ)
2. **ਸੁਨੇਹਾ ਲਿਖੋ**: ਹੇਠਾਂ ਟੈਕਸਟ ਇਨਪੁਟ ਵਰਤੋ
3. **ਭੇਜੋ**: Enter ਦਬਾਓ ਜਾਂ ਭੇਜਣ ਵਾਲੇ ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ
4. **ਜਵਾਬ ਵੇਖੋ**: ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ ਵੇਖੋ

### ਉੱਚ-ਸਤਹੀ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

**ਫਾਈਲ ਅੱਪਲੋਡ**:
1. ਪੇਪਰਕਲਿਪ ਆਈਕਨ 'ਤੇ ਕਲਿਕ ਕਰੋ
2. ਦਸਤਾਵੇਜ਼ ਅੱਪਲੋਡ ਕਰੋ (PDF, TXT, ਆਦਿ)
3. ਸਮੱਗਰੀ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ
4. ਮਾਡਲ ਦਸਤਾਵੇਜ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇਗਾ ਅਤੇ ਜਵਾਬ ਦੇਵੇਗਾ

**ਕਸਟਮ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ**:
1. ਸੈਟਿੰਗ → ਪੈਰਸਨਲਾਈਜ਼ੇਸ਼ਨ
2. ਕਸਟਮ ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਸੈਟ ਕਰੋ
3. ਸਥਿਰ AI ਪੁਰਸਨਾਲਿਟੀ/ਵਿਹਾਰ ਬਣਾਉਂਦਾ ਹੈ

**ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ**:
- **ਨਵੀਂ ਚੈਟ**: ਤਾਜ਼ਾ ਗੱਲਬਾਤ ਸ਼ੁਰੂ ਕਰਨ ਲਈ "+" 'ਤੇ ਕਲਿਕ ਕਰੋ
- **ਚੈਟ ਇਤਿਹਾਸ**: ਸਾਈਡਬਾਰ ਤੋਂ ਪਿਛਲੀ ਗੱਲਬਾਤਾਂ 'ਤੇ ਪਹੁੰਚ ਕਰੋ
- **ਨਿਰਯਾਤ**: ਚੈਟ ਇਤਿਹਾਸ ਨੂੰ ਟੈਕਸਟ/JSON ਵਜੋਂ ਡਾਊਨਲੋਡ ਕਰੋ

**ਮਾਡਲ ਤੁਲਨਾ**:
1. ਇੱਕੋ Open WebUI ਨੂੰ ਕਈ ਬ੍ਰਾਊਜ਼ਰ ਟੈਬ ਵਿੱਚ ਖੋਲ੍ਹੋ
2. ਹਰ ਟੈਬ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਮਾਡਲ ਚੁਣੋ
3. ਇੱਕੋ ਪ੍ਰੋੰਪਟ ਲਈ ਜਵਾਬਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ

### ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਪੈਟਰਨ

**ਡਿਵੈਲਪਮੈਂਟ ਵਰਕਫਲੋ**:
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

## ਪ੍ਰੋਡਕਸ਼ਨ ਡਿਪਲੌਇਮੈਂਟ

### ਸੁਰੱਖਿਅਤ ਸੈਟਅਪ

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

### ਮਲਟੀ-ਯੂਜ਼ਰ ਸੈਟਅਪ

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

### ਮਾਨੀਟਰਿੰਗ ਅਤੇ ਲੌਗਿੰਗ

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ਸਫਾਈ

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

## ਅਗਲੇ ਕਦਮ

### ਸੁਧਾਰ ਦੇ ਵਿਚਾਰ

1. **ਕਸਟਮ ਮਾਡਲ**: Foundry Local ਵਿੱਚ ਆਪਣੇ ਫਾਈਨ-ਟਿਊਨ ਮਾਡਲ ਸ਼ਾਮਲ ਕਰੋ
2. **API ਇੰਟਿਗ੍ਰੇਸ਼ਨ**: Open WebUI ਫੰਕਸ਼ਨ ਦੁਆਰਾ ਬਾਹਰੀ APIs ਨਾਲ ਜੁੜੋ
3. **ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸਿੰਗ**: ਉੱਚ-ਸਤਹੀ RAG ਪਾਈਪਲਾਈਨ ਸੈਟਅਪ ਕਰੋ
4. **ਮਲਟੀ-ਮੋਡਲ**: ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਵਿਜ਼ਨ ਮਾਡਲ ਸੰਰਚਿਤ ਕਰੋ

### ਸਕੇਲਿੰਗ ਵਿਚਾਰ

- **ਲੋਡ ਬੈਲੈਂਸਿੰਗ**: ਰਿਵਰਸ ਪ੍ਰੌਕਸੀ ਦੇ ਪਿੱਛੇ ਕਈ Foundry Local ਇੰਸਟੈਂਸ
- **ਮਾਡਲ ਰੂਟਿੰਗ**: ਵੱਖ-ਵੱਖ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ
- **ਸਰੋਤ ਪ੍ਰਬੰਧਨ**: ਸਮਕਾਲੀ ਯੂਜ਼ਰਾਂ ਲਈ GPU ਮੈਮੋਰੀ ਅਨੁਕੂਲਤਾ
- **ਬੈਕਅੱਪ ਰਣਨੀਤੀ**: ਗੱਲਬਾਤ ਡਾਟਾ ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਦੀ ਨਿਯਮਤ ਬੈਕਅੱਪ

## ਸੰਦਰਭ

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

