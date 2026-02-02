# Module 08: Hands on With Microsoft Foundry Local - Kumpletong Toolkit para sa Developer

## Pangkalahatang-ideya

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) ay kumakatawan sa susunod na henerasyon ng edge AI development, na nagbibigay sa mga developer ng makapangyarihang mga tool upang bumuo, mag-deploy, at mag-scale ng mga AI application nang lokal habang nananatiling seamless ang integrasyon sa Azure AI Foundry. Ang module na ito ay nagbibigay ng komprehensibong saklaw ng Foundry Local mula sa pag-install hanggang sa advanced na pag-develop ng mga agent.

**Pangunahing Teknolohiya:**
- Microsoft Foundry Local CLI at SDK
- Azure AI Foundry integration
- On-device model inference
- Lokal na pag-cache at pag-optimize ng modelo
- Arkitektura na nakabatay sa agent

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng module na ito, ikaw ay:

- **Magiging bihasa sa Foundry Local**: I-install, i-configure, at i-optimize para sa Windows 11 development
- **Mag-deploy ng Iba't Ibang Modelo**: Patakbuhin ang phi, qwen, deepseek, at GPT models nang lokal gamit ang mga CLI command
- **Lumikha ng Production Solutions**: Gumawa ng mga AI application gamit ang advanced prompt engineering at data integration
- **Samantalahin ang Open-Source Ecosystem**: I-integrate ang Hugging Face models at mga kontribusyon ng komunidad
- **Mag-develop ng AI Agents**: Bumuo ng mga intelligent agent na may grounding at orchestration capabilities
- **Magpatupad ng Enterprise Patterns**: Gumawa ng modular, scalable AI solutions para sa production deployment

## Estruktura ng Session

### [1: Pagsisimula sa Foundry Local](./01.FoundryLocalSetup.md)
**Pokús**: Pag-install, CLI setup, pag-deploy ng modelo, at hardware optimization

**Pangunahing Paksa**: Kumpletong pag-install • Mga CLI command • Pag-cache ng modelo • Hardware acceleration • Multi-model deployment

**Halimbawa**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**Tagal**: 2-3 oras | **Antas**: Baguhan

---

### [2: Gumawa ng AI Solutions gamit ang Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Pokús**: Advanced prompt engineering, data integration, at cloud connectivity

**Pangunahing Paksa**: Prompt engineering • Data integration • Azure workflows • Performance optimization • Monitoring

**Halimbawa**: [Chainlit RAG Application](./samples/04/README.md)

**Tagal**: 2-3 oras | **Antas**: Intermediate

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**Pokús**: Hugging Face integration, BYOM strategies, at community models

**Pangunahing Paksa**: HuggingFace integration • Bring-your-own-model • Model Mondays insights • Mga kontribusyon ng komunidad • Pagpili ng modelo

**Halimbawa**: [Multi-Agent Orchestration](./samples/05/README.md)

**Tagal**: 2-3 oras | **Antas**: Intermediate

---

### [4: Tuklasin ang Cutting-Edge Models](./04.CuttingEdgeModels.md)
**Pokús**: LLMs vs SLMs, EdgeAI implementation, at advanced demos

**Pangunahing Paksa**: Paghahambing ng modelo • Edge vs cloud inference • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimization

**Halimbawa**: [Models-as-Tools Router](./samples/06/README.md)

**Tagal**: 3-4 oras | **Antas**: Advanced

---

### [5: Mabilis na Bumuo ng AI-Powered Agents](./05.AIPoweredAgents.md)
**Pokús**: Agent architectures, system prompts, grounding, at orchestration

**Pangunahing Paksa**: Mga disenyo ng agent • System prompt engineering • Grounding techniques • Multi-agent systems • Production deployment

**Halimbawa**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**Tagal**: 3-4 oras | **Antas**: Advanced

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**Pokús**: Modular AI solutions, enterprise scaling, at production patterns

**Pangunahing Paksa**: Models as tools • On-device deployment • SDK/API integration • Enterprise architectures • Scaling strategies

**Halimbawa**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Tagal**: 3-4 oras | **Antas**: Expert

---

### [7: Mga Pattern ng Direktang API Integration](./samples/07/README.md)
**Pokús**: Pure REST API integration nang walang SDK dependencies para sa maximum na kontrol

**Pangunahing Paksa**: HTTP client implementation • Custom authentication • Model health monitoring • Streaming responses • Production error handling

**Halimbawa**: [Direct API Client](./samples/07/README.md)

**Tagal**: 2-3 oras | **Antas**: Intermediate

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**Pokús**: Pagbuo ng modernong native chat applications gamit ang Foundry Local integration

**Pangunahing Paksa**: Electron development • Fluent Design System • Native Windows integration • Real-time streaming • Chat interface design

**Halimbawa**: [Windows 11 Chat Application](./samples/08/README.md)

**Tagal**: 3-4 oras | **Antas**: Advanced

---

### [9: Advanced Multi-Agent Orchestration](./samples/09/README.md)
**Pokús**: Mas sopistikadong koordinasyon ng agent, espesyal na task delegation, at collaborative AI workflows

**Pangunahing Paksa**: Intelligent agent coordination • Function calling patterns • Cross-agent communication • Workflow orchestration • Quality assurance mechanisms

**Halimbawa**: [Advanced Multi-Agent System](./samples/09/README.md)

**Tagal**: 4-5 oras | **Antas**: Expert

---

### [10: Foundry Local bilang Tools Framework](./samples/10/README.md)
**Pokús**: Tool-first architecture para sa integrasyon ng Foundry Local sa mga umiiral na application at framework

**Pangunahing Paksa**: LangChain integration • Semantic Kernel functions • REST API frameworks • CLI tools • Jupyter integration • Production deployment patterns

**Halimbawa**: [Foundry Tools Framework](./samples/10/README.md)

**Tagal**: 4-5 oras | **Antas**: Expert

## Mga Kinakailangan

### Mga Kinakailangan sa Sistema
- **Operating System**: Windows 11 (22H2 o mas bago)
- **Memorya**: 16GB RAM (32GB inirerekomenda para sa mas malalaking modelo)
- **Storage**: 50GB libreng espasyo para sa model caching
- **Hardware**: NPU-enabled device inirerekomenda (Copilot+ PC), GPU opsyonal
- **Network**: High-speed internet para sa unang pag-download ng modelo

### Kapaligiran sa Pag-develop
- Visual Studio Code na may AI Toolkit extension
- Python 3.10+ at pip
- Git para sa version control
- PowerShell o Command Prompt
- Azure CLI (opsyonal para sa cloud integration)

### Mga Kinakailangang Kaalaman
- Pangunahing kaalaman sa AI/ML concepts
- Kakayahan sa paggamit ng command line
- Mga batayan sa Python programming
- Mga konsepto ng REST API
- Pangunahing kaalaman sa prompting at model inference

## Timeline ng Module

**Kabuuang Tinatayang Oras**: 30-38 oras

| Session | Pokús | Mga Halimbawa | Oras | Antas |
|---------|------------|---------|------|------------|
|  1 | Setup & Basics | 01, 02, 03 | 2-3 oras | Baguhan |
|  2 | AI Solutions | 04 | 2-3 oras | Intermediate |
|  3 | Open Source | 05 | 2-3 oras | Intermediate |
|  4 | Advanced Models | 06 | 3-4 oras | Advanced |
|  5 | AI Agents | 05, 09 | 3-4 oras | Advanced |
|  6 | Enterprise Tools | 06, 10 | 3-4 oras | Expert |
|  7 | Direktang API Integration | 07 | 2-3 oras | Intermediate |
|  8 | Windows 11 Chat App | 08 | 3-4 oras | Advanced |
|  9 | Advanced Multi-Agent | 09 | 4-5 oras | Expert |
| 10 | Tools Framework | 10 | 4-5 oras | Expert |

## Pangunahing Resources

**Opisyal na Dokumentasyon:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Source code at opisyal na mga halimbawa
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kumpletong gabay sa setup at paggamit
- [Model Mondays Series](https://aka.ms/model-mondays) - Lingguhang mga highlight at tutorial ng modelo

**Komunidad at Suporta:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Komunidad na Q&A at mga kahilingan sa feature
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Pinakabagong balita at pinakamahusay na mga kasanayan

## Mga Resulta sa Pagkatuto

Sa pagtatapos ng module na ito, ikaw ay magiging handa upang:

### Teknikal na Kasanayan
- **Mag-deploy at Mag-manage**: Mga Foundry Local installation sa development at production environments
- **Mag-integrate ng Mga Modelo**: Gumamit ng iba't ibang pamilya ng modelo mula sa Microsoft, Hugging Face, at mga mapagkukunan ng komunidad
- **Gumawa ng Mga Application**: Lumikha ng production-ready AI applications na may advanced na mga tampok at optimizations
- **Mag-develop ng Mga Agent**: Magpatupad ng sopistikadong AI agents na may grounding, reasoning, at tool integration

### Estratehikong Pag-unawa
- **Mga Desisyon sa Arkitektura**: Gumawa ng mga tamang pagpili sa pagitan ng lokal at cloud deployment
- **Pag-optimize ng Performance**: I-optimize ang inference performance sa iba't ibang hardware configurations
- **Enterprise Scaling**: Magdisenyo ng mga application na maaaring mag-scale mula sa lokal na prototype hanggang sa enterprise deployments
- **Privacy at Seguridad**: Magpatupad ng privacy-preserving AI solutions gamit ang lokal na inference

### Kakayahan sa Inobasyon
- **Mabilis na Prototyping**: Mabilis na bumuo at sumubok ng mga konsepto ng AI application sa lahat ng 10 sample patterns
- **Integrasyon ng Komunidad**: Samantalahin ang open-source models at mag-ambag sa ecosystem
- **Advanced na Mga Pattern**: Magpatupad ng cutting-edge AI patterns kabilang ang RAG, agents, at tool integration
- **Framework Mastery**: Ekspertong integrasyon sa LangChain, Semantic Kernel, Chainlit, at Electron
- **Production Deployment**: Mag-deploy ng scalable AI solutions mula sa lokal na prototype hanggang sa enterprise systems
- **Handa sa Hinaharap na Pag-develop**: Gumawa ng mga application na handa para sa mga umuusbong na teknolohiya at pattern ng AI

## Pagsisimula

1. **Setup ng Kapaligiran**: Siguraduhing may Windows 11 na may inirerekomendang hardware (tingnan ang Mga Kinakailangan)
2. **I-install ang Foundry Local**: Sundin ang Session 1 para sa kumpletong pag-install at configuration
3. **Patakbuhin ang Sample 01**: Magsimula sa basic REST API integration upang i-verify ang setup
4. **Magpatuloy sa Mga Halimbawa**: Kumpletuhin ang mga halimbawa 01-10 para sa komprehensibong mastery

## Mga Sukatan ng Tagumpay

Subaybayan ang iyong progreso sa lahat ng 10 komprehensibong halimbawa:

### Foundation Level (Mga Halimbawa 01-03)
- [ ] Matagumpay na mai-install at ma-configure ang Foundry Local
- [ ] Kumpletuhin ang REST API integration (Halimbawa 01)
- [ ] Ipatupad ang OpenAI SDK compatibility (Halimbawa 02)
- [ ] Magsagawa ng model discovery at benchmarking (Halimbawa 03)

### Application Level (Mga Halimbawa 04-06)
- [ ] Mag-deploy at magpatakbo ng hindi bababa sa 4 na iba't ibang pamilya ng modelo
- [ ] Gumawa ng functional RAG chat application (Halimbawa 04)
- [ ] Lumikha ng multi-agent orchestration system (Halimbawa 05)
- [ ] Ipatupad ang intelligent model routing (Halimbawa 06)

### Advanced Integration Level (Mga Halimbawa 07-10)
- [ ] Gumawa ng production-ready API client (Halimbawa 07)
- [ ] Mag-develop ng Windows 11 native chat application (Halimbawa 08)
- [ ] Ipatupad ang advanced multi-agent system (Halimbawa 09)
- [ ] Lumikha ng komprehensibong tools framework (Halimbawa 10)

### Mga Palatandaan ng Mastery
- [ ] Matagumpay na mapatakbo ang lahat ng 10 halimbawa nang walang error
- [ ] I-customize ang hindi bababa sa 3 halimbawa para sa mga partikular na use case
- [ ] Mag-deploy ng 2+ halimbawa sa production-like environments
- [ ] Mag-ambag ng mga pagpapabuti o extension sa sample code
- [ ] I-integrate ang Foundry Local patterns sa personal/propesyonal na mga proyekto

## Quick Start Guide - Lahat ng 10 Halimbawa

### Setup ng Kapaligiran (Kinakailangan para sa Lahat ng Halimbawa)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Core Foundation Samples (01-06)

**Halimbawa 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Halimbawa 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Halimbawa 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Halimbawa 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Halimbawa 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Halimbawa 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Advanced Integration Samples (07-10)

**Halimbawa 07: Direct API Client**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Halimbawa 08: Windows 11 Chat Application**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Halimbawa 09: Advanced Multi-Agent System**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Halimbawa 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Pag-troubleshoot ng Karaniwang Isyu

**Foundry Local Connection Errors**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Model Loading Issues**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Dependency Issues**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Buod
Ang module na ito ay kumakatawan sa pinakabagong teknolohiya sa edge AI development, pinagsasama ang mga enterprise-grade tools ng Microsoft sa kakayahang umangkop at inobasyon ng open-source ecosystem. Sa pamamagitan ng pag-master ng Foundry Local gamit ang lahat ng 10 komprehensibong halimbawa, ikaw ay magiging nangunguna sa pag-develop ng AI applications.

**Kumpletong Landas ng Pag-aaral:**
- **Pundasyon** (Mga Halimbawa 01-03): API integration at pamamahala ng modelo
- **Aplikasyon** (Mga Halimbawa 04-06): RAG, mga ahente, at intelligent routing
- **Advanced** (Mga Halimbawa 07-10): Production frameworks at enterprise integration

Para sa Azure OpenAI integration (Session 2), tingnan ang mga indibidwal na README file ng mga halimbawa para sa kinakailangang environment variables at mga setting ng API version.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.