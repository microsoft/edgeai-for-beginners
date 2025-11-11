<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f1754a482b6a84e07287a5b775e65b6",
  "translation_date": "2025-11-11T18:02:38+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "pcm"
}
-->
# Sample 04: Production Chat Applications wit Chainlit

Dis na beta sample wey show different ways to build chat apps wey fit work well for production, using Microsoft Foundry Local. E get modern web interface, streaming response, and latest browser technology.

## Wetin dey inside

- **🚀 Chainlit Chat App** (`app.py`): Chat app wey don ready for production wit streaming
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inference wey dey run for browser wit hardware acceleration
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): ChatGPT-style professional interface
- **📚 Educational Notebook** (`chainlit_app.ipynb`): Materials wey dey teach interactive learning

## How to start quick

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

E go open for: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

E go open for: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

E go open for: `http://localhost:3000`

## Architecture Patterns

### Local vs Cloud Decision Matrix

| Scenario | Recommendation | Reason |
|----------|----------------|--------|
| **Sensitive Data wey need privacy** | 🏠 Local (Foundry) | Data no go comot from device |
| **Complex Reasoning** | ☁️ Cloud (Azure OpenAI) | Big models dey available |
| **Real-time Chat** | 🏠 Local (Foundry) | E dey fast, response quick |
| **Document Analysis** | 🔄 Hybrid | Local for extraction, cloud for analysis |
| **Code Generation** | 🏠 Local (Foundry) | Privacy + models wey dey specialized |
| **Research Tasks** | ☁️ Cloud (Azure OpenAI) | E need wide knowledge base |

### Technology Comparison

| Technology | Use Case | Pros | Cons |
|------------|----------|------|------|
| **Chainlit** | Python developers, quick prototyping | Easy to setup, streaming dey | Na only Python |
| **WebGPU** | Maximum privacy, offline use | E dey native for browser, no need server | Model size dey limited |
| **Open WebUI** | Production deployment, teams | Professional UI, user management | E need Docker |

## Wetin you need

- **Foundry Local**: E don install and dey run ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ wit virtual environment
- **Model**: At least one wey don load (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge wey get WebGPU support for demo
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
- 🚀 **Real-time Streaming**: Tokens dey show as dem dey generate
- 🛡️ **Strong Error Handling**: E dey recover well if error happen
- 🎨 **Modern UI**: Professional chat interface wey don ready
- 🔧 **Flexible Configuration**: Environment variables and auto-detection
- 📱 **Responsive Design**: E dey work for desktop and mobile

**How to start quick:**
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
- 🌐 **Browser-native AI**: No need server, e dey run for browser
- ⚡ **WebGPU Acceleration**: Hardware acceleration if e dey available
- 🔒 **Maximum Privacy**: Data no go comot from your device
- 🎯 **Zero Install**: E dey work for any browser wey fit support am
- 🔄 **Graceful Fallback**: E go use CPU if WebGPU no dey

**How to run:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**Features:**
- 🎨 **ChatGPT-style Interface**: Professional and familiar UI
- 👥 **Multi-user Support**: User accounts and conversation history
- 📁 **File Processing**: Upload and analyze documents
- 🔄 **Model Switching**: Easy to switch between different models
- 🐳 **Docker Deployment**: Containerized setup wey don ready for production

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
| `MODEL` | Model alias wey you go use | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local endpoint | Auto-detected | `http://localhost:51211` |
| `API_KEY` | API key (optional for local) | `""` | `your-api-key` |

## Troubleshooting

### Common Issues

**Chainlit Application:**

1. **Service no dey available:**
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

3. **Python environment wahala:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU no dey supported:**
   - Update to Chrome/Edge 113+
   - Enable WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Check GPU status: `chrome://gpu`
   - Demo go fallback to CPU automatically

2. **Model loading errors:**
   - Make sure say internet dey for model download
   - Check browser console for CORS errors
   - Confirm say you dey serve via HTTP (no be file://)

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

2. **Models no dey show:**
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
- Use streaming to make performance look better
- Do connection pooling for high concurrency
- Cache model responses for repeated queries
- Monitor memory usage if conversation history dey long

**WebGPU:**
- Use WebGPU for maximum privacy and speed
- Do model quantization to make models smaller
- Use Web Workers for background processing
- Cache compiled models for browser storage

**Open WebUI:**
- Use persistent volumes for conversation history
- Set resource limits for Docker container
- Do backup plans for user data
- Setup reverse proxy for SSL termination

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

- **API Keys**: Use environment variables, no hardcode am
- **Network**: Use HTTPS for production, consider VPN for team access
- **Access Control**: Setup authentication for Open WebUI
- **Data Privacy**: Check wetin dey local and wetin dey go cloud
- **Updates**: Keep Foundry Local and containers updated

### Monitoring and Maintenance

- **Health Checks**: Setup endpoint monitoring
- **Logging**: Gather logs from all components
- **Metrics**: Track response times, error rates, resource usage
- **Backup**: Do regular backup for conversation data and configurations

## References and Resources

### Documentation
- [Chainlit Documentation](https://docs.chainlit.io/) - Complete framework guide
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Official Microsoft docs
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integration
- [Open WebUI Documentation](https://docs.openwebui.com/) - Advanced configuration

### Sample Files
- [`app.py`](../../../../../Module08/samples/04/app.py) - Production Chainlit application
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Educational notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Browser-based AI inference
- [`open-webui-guide.md`](./open-webui-guide.md) - Complete Open WebUI setup

### Related Samples
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Complete session guide
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Official samples

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->