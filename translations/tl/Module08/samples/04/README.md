# Sample 04: Mga Production Chat Application gamit ang Chainlit

Isang komprehensibong halimbawa na nagpapakita ng iba't ibang paraan sa paggawa ng mga production-ready chat application gamit ang Microsoft Foundry Local, na may modernong web interface, streaming responses, at mga makabagong teknolohiya sa browser.

## Kasama sa Package

- **🚀 Chainlit Chat App** (`app.py`): Production-ready chat application na may streaming
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inference sa browser na may hardware acceleration
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): Propesyonal na interface na parang ChatGPT
- **📚 Educational Notebook** (`chainlit_app.ipynb`): Mga interactive na materyales para sa pag-aaral

## Mabilisang Simula

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Bubuksan sa: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Bubuksan sa: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Bubuksan sa: `http://localhost:3000`

## Mga Pattern ng Arkitektura

### Local vs Cloud Decision Matrix

| Scenario | Rekomendasyon | Dahilan |
|----------|---------------|---------|
| **Privacy-Sensitive Data** | 🏠 Local (Foundry) | Hindi lumalabas ang data sa device |
| **Complex Reasoning** | ☁️ Cloud (Azure OpenAI) | Access sa mas malalaking modelo |
| **Real-time Chat** | 🏠 Local (Foundry) | Mas mababang latency, mas mabilis na tugon |
| **Document Analysis** | 🔄 Hybrid | Local para sa extraction, cloud para sa analysis |
| **Code Generation** | 🏠 Local (Foundry) | Privacy + mga specialized na modelo |
| **Research Tasks** | ☁️ Cloud (Azure OpenAI) | Kailangan ng malawak na knowledge base |

### Paghahambing ng Teknolohiya

| Teknolohiya | Gamit | Pros | Cons |
|-------------|-------|------|------|
| **Chainlit** | Python developers, mabilisang prototyping | Madaling setup, suporta sa streaming | Python-only |
| **WebGPU** | Maximum privacy, offline scenarios | Browser-native, walang server na kailangan | Limitado ang laki ng modelo |
| **Open WebUI** | Production deployment, teams | Propesyonal na UI, user management | Kailangan ng Docker |

## Mga Kinakailangan

- **Foundry Local**: Naka-install at tumatakbo ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ na may virtual environment
- **Model**: Hindi bababa sa isang naka-load (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge na may suporta sa WebGPU para sa mga demo
- **Docker**: Para sa Open WebUI (opsyonal)

## Pag-install at Setup

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

## Mga Halimbawang Aplikasyon

### Chainlit Chat Application

**Mga Tampok:**
- 🚀 **Real-time Streaming**: Lumalabas ang mga token habang sila ay nabubuo
- 🛡️ **Robust Error Handling**: Maayos na pag-aayos at pagbawi
- 🎨 **Modern UI**: Propesyonal na chat interface na handa na
- 🔧 **Flexible Configuration**: Mga environment variable at auto-detection
- 📱 **Responsive Design**: Gumagana sa desktop at mobile devices

**Mabilisang Simula:**
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

**Mga Tampok:**
- 🌐 **Browser-native AI**: Walang server na kailangan, tumatakbo nang buo sa browser
- ⚡ **WebGPU Acceleration**: Hardware acceleration kung available
- 🔒 **Maximum Privacy**: Walang data na lumalabas sa iyong device
- 🎯 **Zero Install**: Gumagana sa anumang compatible na browser
- 🔄 **Graceful Fallback**: Lumilipat sa CPU kung hindi available ang WebGPU

**Pagpapatakbo:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**Mga Tampok:**
- 🎨 **ChatGPT-like Interface**: Propesyonal, pamilyar na UI
- 👥 **Multi-user Support**: Mga user account at kasaysayan ng pag-uusap
- 📁 **File Processing**: Pag-upload at pagsusuri ng mga dokumento
- 🔄 **Model Switching**: Madaling pagpapalit ng iba't ibang modelo
- 🐳 **Docker Deployment**: Production-ready na containerized setup

**Mabilisang Setup:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Sanggunian sa Konfigurasyon

### Mga Environment Variable

| Variable | Deskripsyon | Default | Halimbawa |
|----------|-------------|---------|-----------|
| `MODEL` | Model alias na gagamitin | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local endpoint | Auto-detected | `http://localhost:51211` |
| `API_KEY` | API key (opsyonal para sa local) | `""` | `your-api-key` |

## Pag-aayos ng Problema

### Mga Karaniwang Isyu

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
   - Mag-update sa Chrome/Edge 113+
   - I-enable ang WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Suriin ang GPU status: `chrome://gpu`
   - Ang demo ay awtomatikong lilipat sa CPU

2. **Model loading errors:**
   - Siguraduhing may internet connection para sa pag-download ng modelo
   - Suriin ang browser console para sa CORS errors
   - Siguraduhing nagsisilbi ka sa HTTP (hindi file://)

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

### Pag-optimize ng Performance

**Chainlit:**
- Gumamit ng streaming para sa mas magandang perceived performance
- Mag-implement ng connection pooling para sa mataas na concurrency
- I-cache ang mga tugon ng modelo para sa mga paulit-ulit na query
- Subaybayan ang memory usage sa malalaking kasaysayan ng pag-uusap

**WebGPU:**
- Gumamit ng WebGPU para sa maximum privacy at bilis
- Mag-implement ng model quantization para sa mas maliliit na modelo
- Gumamit ng Web Workers para sa background processing
- I-cache ang mga compiled na modelo sa browser storage

**Open WebUI:**
- Gumamit ng persistent volumes para sa kasaysayan ng pag-uusap
- I-configure ang resource limits para sa Docker container
- Mag-implement ng backup strategies para sa user data
- Mag-set up ng reverse proxy para sa SSL termination

### Mga Pattern ng Integrasyon

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

### Mga Pagsasaalang-alang sa Seguridad

- **API Keys**: Gumamit ng environment variables, huwag mag-hardcode
- **Network**: Gumamit ng HTTPS sa production, isaalang-alang ang VPN para sa team access
- **Access Control**: Mag-implement ng authentication para sa Open WebUI
- **Data Privacy**: Suriin kung anong data ang nananatili sa local vs. napupunta sa cloud
- **Updates**: Panatilihing updated ang Foundry Local at mga container

### Monitoring at Maintenance

- **Health Checks**: Mag-implement ng endpoint monitoring
- **Logging**: I-centralize ang logs mula sa lahat ng components
- **Metrics**: Subaybayan ang response times, error rates, resource usage
- **Backup**: Regular na backup ng conversation data at configurations

## Mga Sanggunian at Resources

### Dokumentasyon
- [Chainlit Documentation](https://docs.chainlit.io/) - Kumpletong gabay sa framework
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Opisyal na Microsoft docs
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integration
- [Open WebUI Documentation](https://docs.openwebui.com/) - Advanced na konfigurasyon

### Mga Sample na File
- [`app.py`](../../../../../Module08/samples/04/app.py) - Production Chainlit application
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Educational notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI inference sa browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Kumpletong Open WebUI setup

### Mga Kaugnay na Halimbawa
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Kumpletong gabay sa session
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Opisyal na mga halimbawa

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.