# Sample 04: Production Chat Applications with Chainlit

A detailed example showcasing various methods to create production-ready chat applications using Microsoft Foundry Local, featuring modern web interfaces, streaming responses, and advanced browser technologies.

## What's Included

- **🚀 Chainlit Chat App** (`app.py`): A production-ready chat application with streaming capabilities
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inference in the browser with hardware acceleration
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): A professional ChatGPT-style interface
- **📚 Educational Notebook** (`chainlit_app.ipynb`): Interactive learning resources

## Quick Start

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```
  
Accessible at: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```
  
Accessible at: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  
Accessible at: `http://localhost:3000`

## Architecture Patterns

### Local vs Cloud Decision Matrix

| Scenario | Recommendation | Reason |
|----------|----------------|--------|
| **Privacy-Sensitive Data** | 🏠 Local (Foundry) | Data remains on the device |
| **Complex Reasoning** | ☁️ Cloud (Azure OpenAI) | Access to larger models |
| **Real-time Chat** | 🏠 Local (Foundry) | Lower latency, faster responses |
| **Document Analysis** | 🔄 Hybrid | Local for extraction, cloud for analysis |
| **Code Generation** | 🏠 Local (Foundry) | Privacy + specialized models |
| **Research Tasks** | ☁️ Cloud (Azure OpenAI) | Requires a broad knowledge base |

### Technology Comparison

| Technology | Use Case | Pros | Cons |
|------------|----------|------|------|
| **Chainlit** | Python developers, rapid prototyping | Easy setup, streaming support | Python-only |
| **WebGPU** | Maximum privacy, offline scenarios | Browser-native, no server required | Limited model size |
| **Open WebUI** | Production deployment, teams | Professional UI, user management | Requires Docker |

## Prerequisites

- **Foundry Local**: Installed and running ([Download](https://aka.ms/foundry-local-installer))
- **Python**: Version 3.10+ with virtual environment
- **Model**: At least one loaded (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge with WebGPU support for demos
- **Docker**: For Open WebUI (optional)

## Installation & Setup

### 1. Python Environment Setup

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
  

### 2. Foundry Local Setup

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```
  

## Sample Applications

### Chainlit Chat Application

**Features:**
- 🚀 **Real-time Streaming**: Tokens appear as they are generated
- 🛡️ **Robust Error Handling**: Handles errors gracefully
- 🎨 **Modern UI**: Professional chat interface ready to use
- 🔧 **Flexible Configuration**: Supports environment variables and auto-detection
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices

**Quick Start:**  
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```
  

### WebGPU Browser Demo

**Features:**
- 🌐 **Browser-native AI**: Runs entirely in the browser, no server required
- ⚡ **WebGPU Acceleration**: Utilizes hardware acceleration when available
- 🔒 **Maximum Privacy**: Data never leaves your device
- 🎯 **Zero Install**: Works in any compatible browser
- 🔄 **Graceful Fallback**: Automatically switches to CPU if WebGPU is unavailable

**Running:**  
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```
  

### Open WebUI Integration

**Features:**
- 🎨 **ChatGPT-like Interface**: Professional and familiar user interface
- 👥 **Multi-user Support**: Includes user accounts and conversation history
- 📁 **File Processing**: Upload and analyze documents
- 🔄 **Model Switching**: Easily switch between different models
- 🐳 **Docker Deployment**: Production-ready containerized setup

**Quick Setup:**  
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  

## Configuration Reference

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|----------|
| `MODEL` | Model alias to use | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local endpoint | Auto-detected | `http://localhost:51211` |
| `API_KEY` | API key (optional for local) | `""` | `your-api-key` |

## Troubleshooting

### Common Issues

**Chainlit Application:**

1. **Service not available:**  
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```
  

2. **Port conflicts:**  
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```
  

3. **Python environment issues:**  
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```
  

**WebGPU Demo:**

1. **WebGPU not supported:**
   - Update to Chrome/Edge 113+
   - Enable WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Check GPU status: `chrome://gpu`
   - The demo will automatically fallback to CPU

2. **Model loading errors:**
   - Ensure an active internet connection for model download
   - Check the browser console for CORS errors
   - Verify that the demo is served via HTTP (not file://)

**Open WebUI:**

1. **Connection refused:**  
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```
  

2. **Models not appearing:**  
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```
  

### Validation Checklist

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```
  

## Advanced Usage

### Performance Optimization

**Chainlit:**
- Use streaming for better perceived performance
- Implement connection pooling for high concurrency
- Cache model responses for repeated queries
- Monitor memory usage with large conversation histories

**WebGPU:**
- Use WebGPU for maximum privacy and speed
- Implement model quantization for smaller models
- Use Web Workers for background processing
- Cache compiled models in browser storage

**Open WebUI:**
- Use persistent volumes for conversation history
- Configure resource limits for Docker containers
- Implement backup strategies for user data
- Set up a reverse proxy for SSL termination

### Integration Patterns

**Hybrid Local/Cloud:**  
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```
  

**Multi-Modal Pipeline:**  
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```
  

## Production Deployment

### Security Considerations

- **API Keys**: Use environment variables; never hardcode them
- **Network**: Use HTTPS in production; consider VPN for team access
- **Access Control**: Implement authentication for Open WebUI
- **Data Privacy**: Audit what data remains local versus what goes to the cloud
- **Updates**: Keep Foundry Local and containers up to date

### Monitoring and Maintenance

- **Health Checks**: Implement endpoint monitoring
- **Logging**: Centralize logs from all components
- **Metrics**: Track response times, error rates, and resource usage
- **Backup**: Regularly back up conversation data and configurations

## References and Resources

### Documentation
- [Chainlit Documentation](https://docs.chainlit.io/) - Comprehensive framework guide
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Official Microsoft documentation
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integration guide
- [Open WebUI Documentation](https://docs.openwebui.com/) - Advanced configuration details

### Sample Files
- [`app.py`](../../../../../Module08/samples/04/app.py) - Production Chainlit application
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Educational notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Browser-based AI inference
- [`open-webui-guide.md`](./open-webui-guide.md) - Complete Open WebUI setup guide

### Related Samples
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Complete session guide
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Official sample repository

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.