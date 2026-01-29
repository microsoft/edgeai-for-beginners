# Open WebUI + Foundry Local Integration Guide

This guide explains how to connect Open WebUI to Microsoft Foundry Local, enabling a professional ChatGPT-like interface powered by your local AI models.

## Overview

Open WebUI offers a modern, user-friendly chat interface that integrates with any OpenAI-compatible API. By connecting it to Foundry Local, you gain:

- **Professional UI**: A ChatGPT-style interface with a sleek design
- **Local Privacy**: All processing happens on your device
- **Model Switching**: Easily switch between different local models
- **Conversation History**: Persistent chat history and context
- **File Uploads**: Analyze documents and process files
- **Custom Personas**: Customize system prompts and roles

## Prerequisites

### Required Software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Load a Model

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
2. **Create Account**: Set up an admin user (the first user becomes admin)
3. **Verify Connection**: Models should automatically appear in the dropdown menu

### Step 3: Test the Connection

1. Select your model from the dropdown (e.g., "phi-4-mini")
2. Type a test message: "Hello! Can you introduce yourself?"
3. You should see a streaming response from your local model

## Advanced Configuration

### Environment Variables

| Variable | Purpose | Default | Example |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local endpoint | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (required but not used locally) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Session encryption key | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | Allow new user registration | `True` | `False` |

### Manual Configuration (Alternative)

If environment variables don't work, configure manually:

1. **Open Settings**: Click the Settings (gear icon)
2. **Navigate to Connections**: Settings → Connections → OpenAI
3. **Set API Details**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (any value works)
4. **Save and Test**: Click "Save" and test with a model

### Persistent Data Storage

To save conversations and settings:

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

### Connection Issues

**Problem**: "Connection refused" or models not loading

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

### Model Not Appearing

**Problem**: Open WebUI does not show models in the dropdown

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

**Fix**: Ensure the model is properly loaded:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker Network Issues

**Problem**: `host.docker.internal` is not resolving

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

**Alternative**: Find your machine's IP:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Performance Issues

**Slow Responses**:
1. Check if the model is using GPU acceleration: `foundry service ps`
2. Verify that your system has sufficient resources (RAM/GPU memory)
3. Consider using a smaller model for testing

**Memory Issues**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Usage Guide

### Basic Chat

1. **Select Model**: Choose a model from the dropdown (shows Foundry Local models)
2. **Type Message**: Enter text in the input field at the bottom
3. **Send**: Press Enter or click the Send button
4. **View Response**: Watch the streaming response in real-time

### Advanced Features

**File Upload**:
1. Click the paperclip icon
2. Upload a document (PDF, TXT, etc.)
3. Ask questions about the content
4. The model will analyze and respond based on the document

**Custom System Prompts**:
1. Go to Settings → Personalization
2. Set a custom system prompt
3. This creates a consistent AI personality/behavior

**Conversation Management**:
- **New Chat**: Click "+" to start a new conversation
- **Chat History**: Access previous conversations from the sidebar
- **Export**: Download chat history as text/JSON

**Model Comparison**:
1. Open multiple browser tabs with the same Open WebUI
2. Select different models in each tab
3. Compare responses to the same prompts

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
2. **API Integration**: Connect to external APIs using Open WebUI functions
3. **Document Processing**: Set up advanced RAG pipelines
4. **Multi-Modal**: Configure vision models for image analysis

### Scaling Considerations

- **Load Balancing**: Use multiple Foundry Local instances behind a reverse proxy
- **Model Routing**: Assign different models for specific use cases
- **Resource Management**: Optimize GPU memory for concurrent users
- **Backup Strategy**: Regularly back up conversation data and configurations

## References

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

