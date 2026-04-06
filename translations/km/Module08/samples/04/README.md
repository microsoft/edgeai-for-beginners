# Sample 04: កម្មវិធី Chat សម្រាប់ផលិតកម្មជាមួយ Chainlit

ឧទាហរណ៍ទំហំពិពេញដែលបង្ហាញពីវិធីផ្សេងៗក្នុងការកសាងកម្មវិធីជជែកដែលត្រៀមសម្រាប់ផលិតកម្មដោយប្រើ Microsoft Foundry Local, មានផ្ទាំងបណ្តាញទំនើប, ចម្លើយបន្ត (streaming), និងបច្ចេកវិទ្យារុករកទំនärkពេលនេះ។

## What's Included

- **🚀 Chainlit Chat App** (`app.py`): កម្មវិធីជជែកសម្រាប់ផលិតកម្មដែលមានចលនា streaming
- **🌐 WebGPU Demo** (`webgpu-demo/`): ការបញ្ជាផ្ទាល់ AI ក្នុងកម្មវិធីរុករកជាមួយ присហារដ៏លឿន
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): ផ្ទាំងមុខងារដូច ChatGPT សម្រាប់ការប្រើប្រាស់វិជ្ជាជីវៈ
- **📚 Educational Notebook** (`chainlit_app.ipynb`): សម្ភារៈសិក្សាអន្តរកម្ម

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

បើកនៅ: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

បើកនៅ: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

បើកនៅ: `http://localhost:3000`

## Architecture Patterns

### Local vs Cloud Decision Matrix

| Scenario | Recommendation | Reason |
|----------|----------------|--------|
| **Privacy-Sensitive Data** | 🏠 Local (Foundry) | ទិន្នន័យមិនដែលចាកចេញពីឧបករណ៍ |
| **Complex Reasoning** | ☁️ Cloud (Azure OpenAI) | ចូលដំណើរការម៉ូឌែលទំហំធំជាង |
| **Real-time Chat** | 🏠 Local (Foundry) | ពេលយឺតទាប, ចម្លើយលឿនជាង |
| **Document Analysis** | 🔄 Hybrid | នៅលើកន្លែងសម្រាប់ការទាញទិន្នន័យ, cloud សម្រាប់វិភាគ |
| **Code Generation** | 🏠 Local (Foundry) | ភាពឯកជន + ម៉ូឌែលឯកជនជាពិសេស |
| **Research Tasks** | ☁️ Cloud (Azure OpenAI) | តម្រូវប្រភពចំណេះទូលំទូលាយ |

### Technology Comparison

| Technology | Use Case | Pros | Cons |
|------------|----------|------|------|
| **Chainlit** | Python developers, rapid prototyping | កំណត់បានងាយ, គាំទ្រការបន្ត (streaming) | គ្រាន់តែ Python |
| **WebGPU** | Maximum privacy, offline scenarios | ជាមូលដ្ឋានក្នុងរុករក, មិនចាំបាច់ម៉ាស៊ីនមេ | ទំហំម៉ូឌែលមានកំណូត |
| **Open WebUI** | Production deployment, teams | ផ្ទាំង UI វិជ្ជាជីវៈ, គ្រប់គ្រងអ្នកប្រើ | តម្រូវ Docker |

## Prerequisites

- **Foundry Local**: ត្រូវបានដំឡើង និងកំពុងដំណើរការ ([ទាញយក](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ ជាមួយ virtual environment
- **Model**: តិចទៅតាមមួយបានផ្ទុក (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge ដែលគាំទ្រ WebGPU សម្រាប់ការបង្ហាញ
- **Docker**: សម្រាប់ Open WebUI (ជាជម្រើស)

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

**លក្ខណៈពិសេស:**
- 🚀 **ការបន្តពេលពិត**: តួអក្សរបង្ហាញជាពេលកើតមាន
- 🛡️ **ការគ្រប់គ្រងកំហុសរឹងមាំ**: ការធ្លាក់ចុះយ៉ាងរលូន និងការស្ដារឡើងវិញ
- 🎨 **UI ទំនើប**: ផ្ទាំងជជែកវិជ្ជាជីវៈដែលរួចរាល់
- 🔧 **ការកំណត់បត់បែន**: អថេរបរិយាកាស និងការរកឃើញដោយស្វ័យប្រវត្តិ
- 📱 **រចនាឆ្លើយតប**: ធ្វើការលើកុំព្យូទ័រ និងឧបករណ៍កាន់ដៃ

**ចាប់ផ្តើមរហ័ស:**
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

**លក្ខណៈពិសេស:**
- 🌐 **AI បន្ទាត់ក្នុងរុករក**: មិនចាំបាច់ម៉ាស៊ីនមេ, រត់ទាំងមូលក្នុងកម្មវិធីរុករក
- ⚡ **ជំរុញដោយ WebGPU**: ជំរុញដោយឧបករណ៍ពេលមាន
- 🔒 **ភាពឯកជនខ្ពស់បំផុត**: ទិន្នន័យមិនដែលចាកចេញពីឧបករណ៍របស់អ្នក
- 🎯 **មិនចាំបាច់ដំឡើង**: ធ្វើការនៅលើរុករកដែលស្គាល់
- 🔄 **វិលត្រឡប់យ៉ាងរលូន**: វិលទៅ CPU បើ WebGPU មិនមាន

**កំពុងរត់:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**លក្ខណៈពិសេស:**
- 🎨 **ផ្ទាំងដូច ChatGPT**: UI វិជ្ជាជីវៈ និងស្របចិត្ត
- 👥 **គាំទ្រប្រើប្រាស់ច្រើនជន**: គណនីអ្នកប្រើ និងប្រវត្តិការជជែក
- 📁 **ដំណោះស្រាយឯកសារ**: ផ្ទុកឡើង និងវិភាគឯកសារ
- 🔄 **ប្តូរម៉ូឌែលបានងាយ**: ប្តូរវាងម៉ូឌែលផ្សេងៗបានយ៉ាងងាយ
- 🐳 **ដាក់នៅលើ Docker**: កំណត់ container សម្រាប់ផលិតកម្ម

**ការកំណត់រហ័ស:**
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
| `MODEL` | ឈ្មោះម៉ូឌែលដែលប្រើ | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | ចំណុចចូល Foundry Local | Auto-detected | `http://localhost:51211` |
| `API_KEY` | កូនសោ API (ច្រើនជាឧបករណ៍សម្រាប់លើកន្លែង) | `""` | `your-api-key` |

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
   - អាប់ដេតទៅ Chrome/Edge 113+
   - បើក WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - ពិនិត្យស្ថានភាព GPU: `chrome://gpu`
   - ការបង្ហាញនឹងវិលទៅ CPU ដោយស្វ័យប្រវត្តិ

2. **Model loading errors:**
   - ប្រាកដថាមានការតភ្ជាប់អ៊ីនធឺណេតសម្រាប់ទាញម៉ូឌែល
   - ពិនិត្យ console រុករកសម្រាប់កំហុស CORS
   - ផ្ទៀងផ្ទាត់ថាអ្នកកំពុងបម្រើតាម HTTP (មិនមែន file://)

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
- ប្រើការបន្ត (streaming) សម្រាប់អានគិតថាដំណើរការលឿនឡើង
- អនុវត្ត connection pooling សម្រាប់ concurrency ខ្ពស់
- ស្កេរការ cache ចម្លើយម៉ូឌែលសម្រាប់សំណើដែលធម្មតា
- ត្រួតពិនិត្យការប្រើ memory ជាមួយប្រវត្តិជជែកធំៗ

**WebGPU:**
- ប្រើ WebGPU សម្រាប់ភាពឯកជន និងល្បឿនអតិបរមា
- អនុវត្ត quantization សម្រាប់ម៉ូឌែលតូច
- ប្រើ Web Workers សម្រាប់ដំណើរការផ្ទៃខាងក្រោយ
- Cache ម៉ូឌែលដែលបានសម្រួលក្នុង storage រុករក

**Open WebUI:**
- ប្រើ volume រឹងសម្រាប់ប្រវត្តិជជែក
- កំណត់កម្រិតធនធានសម្រាប់ container Docker
- អនុវត្តយុទ្ធសាស្ត្របម្រុងទុកសម្រាប់ទិន្នន័យអ្នកប្រើ
- ដំឡើង reverse proxy សម្រាប់ SSL termination

### Integration Patterns

**Hybrid Local/Cloud:**
```python
# ដឹកជញ្ជូនដោយផ្អែកលើភាពស្មុគស្មាញ និងតម្រូវការការពារភាពឯកជន
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # ពាក់ព័ន្ធនឹងភាពឯកជន
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # ការគិតវិនិច្ឆ័យស្មុគស្មាញ
    else:
        return await foundry_local_completion(prompt)  # លំនាំដើមក្នុងស្រុក
```

**Multi-Modal Pipeline:**
```python
# ផ្សំសមត្ថភាព AI ផ្សេងៗ
async def analyze_document(file_path: str):
    # 1. OCR ជាមួយ WebGPU (នៅលើកម្មវិធីរុករក)
    text = await webgpu_ocr(file_path)
    
    # 2. ការវិភាគជាមួយ Foundry Local (ឯកជន)
    summary = await foundry_local_analyze(text)
    
    # 3. ការកែលម្អជាមួយពពក (ប្រសិនបើចាំបាច់)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Production Deployment

### Security Considerations

- **API Keys**: ប្រើអថេរបរិយាកាស, កុំដាក់​ជា​កូដដាច់
- **Network**: ប្រើ HTTPS នៅក្នុង​ផលិតកម្ម, ពិចារណា VPN សម្រាប់ចូលពីក្រុម
- **Access Control**: អនុវត្ត authentication សម្រាប់ Open WebUI
- **Data Privacy**: វាយតម្លៃថាអ្វីនៅតែក្នុងកន្លែង ប្រឆាំងនឹងអ្វីទៅកាន់ cloud
- **Updates**: រក្សា Foundry Local និង containers ឱ្យទាន់សម័យ

### Monitoring and Maintenance

- **Health Checks**: អនុវត្តការត្រួតពិនិត្យ endpoint
- **Logging**: មណ្ឌលហៅ logs ពីគ្រប់ក	component
- **Metrics**: តាមដានពេលឆ្លើយតប, អត្រាកំហុស, និងការប្រើធនធាន
- **Backup**: បម្រុងទុកប្រវត្តិជជែក និងការកំណត់បញ្ជា​រៀងរាល់ពេល

## References and Resources

### Documentation
- [Chainlit Documentation](https://docs.chainlit.io/) - មគ្គុទេសក៏សម្រាប់ស៊ុមក្របខ័ណ្ឌពេញលេញ
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - ឯកសារ​ផ្លូវការ Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - การចូលដំណើរការ WebGPU
- [Open WebUI Documentation](https://docs.openwebui.com/) - ការកំណត់តំរូវជាន់ខ្ពស់

### Sample Files
- [`app.py`](../../../../../Module08/samples/04/app.py) - កម្មវិធី Chainlit សម្រាប់ផលិតកម្ម
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - សៀវភៅចំណាំសិក្សា
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - ការបញ្ជាផ្ទាល់ AI ក្នុងរុករក
- [`open-webui-guide.md`](./open-webui-guide.md) - ការកំណត់ Open WebUI ពេញលេញ

### Related Samples
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - មគ្គុទេសក៏សម្រាប់សម័យពេញលេញ
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - ឧទាហរណ៍ផ្លូវការ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ប្រកាសបដិសេធ**:
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះបីយើងខិតខំស្វែងរកភាពត្រឹមត្រូវក៏ដោយ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬ មិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើម គួរត្រូវបានចាត់ទុកថាជាប្រភពដែលអាចទុកចិត្តបាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមពិចារណាបកប្រែដោយអ្នកជំនាញមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬ ការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->