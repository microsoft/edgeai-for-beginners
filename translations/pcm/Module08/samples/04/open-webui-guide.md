# Open WebUI + Foundry Local Integration Guide

Dis guide go show you how you fit connect Open WebUI to Microsoft Foundry Local for beta ChatGPT-like interface wey dey powered by your local AI models.

## Overview

Open WebUI dey provide modern, easy-to-use chat interface wey fit connect to any OpenAI-compatible API. If you connect am to Foundry Local, you go get:

- **Beta UI**: ChatGPT-like interface wey get modern design
- **Local Privacy**: All processing dey happen for your device
- **Model Switching**: Easy way to change between different local models
- **Conversation History**: Persistent chat history and context
- **File Uploads**: Document analysis and file processing features
- **Custom Personas**: System prompts and role customization

## Prerequisites

### Software wey you go need

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Load Model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Quick Setup (Recommended)

### Step 1: Run Open WebUI with Docker

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

### Step 2: Initial Setup

1. **Open Browser**: Go to `http://localhost:3000`
2. **Create Account**: Set up admin user (first user go be admin)
3. **Verify Connection**: Models go show for dropdown automatically

### Step 3: Test Connection

1. Choose your model from the dropdown (e.g., "phi-4-mini")
2. Type test message: "Hello! Can you introduce yourself?"
3. You go see streaming response from your local model

## Advanced Configuration

### Environment Variables

| Variable | Purpose | Default | Example |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local endpoint | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (required but not used locally) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Session encryption key | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | Allow new user registration | `True` | `False` |

### Manual Configuration (Alternative)

If environment variables no work, configure am manually:

1. **Open Settings**: Click Settings (gear icon)
2. **Go Connections**: Settings → Connections → OpenAI
3. **Set API Details**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (any value dey work)
4. **Save and Test**: Click "Save" then test am with model

### Persistent Data Storage

To keep conversations and settings:

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

## Troubleshooting

### Connection Wahala

**Problem**: "Connection refused" or models no dey load

**Solutions**:
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

### Model No Show

**Problem**: Open WebUI no show models for dropdown

**Debugging Steps**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Fix**: Make sure say model dey properly loaded:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker Network Wahala

**Problem**: `host.docker.internal` no dey resolve

**Windows Solution**:
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

**Alternative**: Find your machine IP:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Performance Wahala

**Slow Responses**:
1. Check say model dey use GPU acceleration: `foundry service ps`
2. Confirm say system resources dey enough (RAM/GPU memory)
3. Try use smaller model for testing

**Memory Wahala**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Usage Guide

### Basic Chat

1. **Select Model**: Choose from dropdown (Foundry Local models go show)
2. **Type Message**: Use text input for bottom
3. **Send**: Press Enter or click Send button
4. **View Response**: See streaming response as e dey happen

### Advanced Features

**File Upload**:
1. Click paperclip icon
2. Upload document (PDF, TXT, etc.)
3. Ask questions about wetin dey inside
4. Model go analyze and respond based on document

**Custom System Prompts**:
1. Settings → Personalization
2. Set custom system prompt
3. E go create consistent AI personality/behavior

**Conversation Management**:
- **New Chat**: Click "+" to start new conversation
- **Chat History**: Check old conversations for sidebar
- **Export**: Download chat history as text/JSON

**Model Comparison**:
1. Open multiple browser tabs to same Open WebUI
2. Choose different models for each tab
3. Compare responses to same prompts

### Integration Patterns

**Development Workflow**:
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

## Production Deployment

### Secure Setup

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

### Monitoring and Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Cleanup

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

## Next Steps

### Enhancement Ideas

1. **Custom Models**: Add your own fine-tuned models to Foundry Local
2. **API Integration**: Connect to external APIs via Open WebUI functions
3. **Document Processing**: Set up advanced RAG pipelines
4. **Multi-Modal**: Configure vision models for image analysis

### Scaling Considerations

- **Load Balancing**: Multiple Foundry Local instances behind reverse proxy
- **Model Routing**: Different models for different use cases
- **Resource Management**: GPU memory optimization for concurrent users
- **Backup Strategy**: Regular backup of conversation data and configurations

## References

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->