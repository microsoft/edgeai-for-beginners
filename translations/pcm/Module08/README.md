# Module 08: Hands on With Microsoft Foundry Local - Complete Developer Toolkit

## Overview

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) na di next level for edge AI development, e dey give developers strong tools to build, deploy, and scale AI apps for dia local area, and e still dey connect well with Azure AI Foundry. Dis module go show you everything about Foundry Local, from how to install am to how to develop advanced agents.

**Key Technologies:**
- Microsoft Foundry Local CLI and SDK
- Azure AI Foundry integration
- On-device model inference
- Local model caching and optimization
- Agent-based architectures

## Learning Objectives

If you complete dis module, you go fit:

- **Sabi Foundry Local well well**: Install, configure, and optimize am for Windows 11 development
- **Deploy different models**: Run phi, qwen, deepseek, and GPT models for your local area with CLI commands
- **Build production solutions**: Create AI apps with advanced prompt engineering and data integration
- **Use open-source ecosystem**: Add Hugging Face models and community contributions
- **Develop AI agents**: Build smart agents wey sabi grounding and orchestration
- **Use enterprise patterns**: Create modular, scalable AI solutions for production deployment

## Session Structure

### [1: Getting Started with Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: How to install, set up CLI, deploy model, and optimize hardware

**Key Topics**: Complete installation • CLI commands • Model caching • Hardware acceleration • Multi-model deployment

**Sample**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**Duration**: 2-3 hours | **Level**: Beginner

---

### [2: Build AI Solutions with Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Advanced prompt engineering, data integration, and cloud connectivity

**Key Topics**: Prompt engineering • Data integration • Azure workflows • Performance optimization • Monitoring

**Sample**: [Chainlit RAG Application](./samples/04/README.md)

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**Focus**: Hugging Face integration, BYOM strategies, and community models

**Key Topics**: HuggingFace integration • Bring-your-own-model • Model Mondays insights • Community contributions • Model selection

**Sample**: [Multi-Agent Orchestration](./samples/05/README.md)

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [4: Explore Cutting-Edge Models](./04.CuttingEdgeModels.md)
**Focus**: LLMs vs SLMs, EdgeAI implementation, and advanced demos

**Key Topics**: Model comparison • Edge vs cloud inference • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimization

**Sample**: [Models-as-Tools Router](./samples/06/README.md)

**Duration**: 3-4 hours | **Level**: Advanced

---

### [5: Build AI-Powered Agents Fast](./05.AIPoweredAgents.md)
**Focus**: Agent architectures, system prompts, grounding, and orchestration

**Key Topics**: Agent design patterns • System prompt engineering • Grounding techniques • Multi-agent systems • Production deployment

**Sample**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**Duration**: 3-4 hours | **Level**: Advanced

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**Focus**: Modular AI solutions, enterprise scaling, and production patterns

**Key Topics**: Models as tools • On-device deployment • SDK/API integration • Enterprise architectures • Scaling strategies

**Sample**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Duration**: 3-4 hours | **Level**: Expert

---

### [7: Direct API Integration Patterns](./samples/07/README.md)
**Focus**: Pure REST API integration without SDK dependencies for maximum control

**Key Topics**: HTTP client implementation • Custom authentication • Model health monitoring • Streaming responses • Production error handling

**Sample**: [Direct API Client](./samples/07/README.md)

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**Focus**: Building modern native chat applications with Foundry Local integration

**Key Topics**: Electron development • Fluent Design System • Native Windows integration • Real-time streaming • Chat interface design

**Sample**: [Windows 11 Chat Application](./samples/08/README.md)

**Duration**: 3-4 hours | **Level**: Advanced

---

### [9: Advanced Multi-Agent Orchestration](./samples/09/README.md)
**Focus**: Sophisticated agent coordination, specialized task delegation, and collaborative AI workflows

**Key Topics**: Intelligent agent coordination • Function calling patterns • Cross-agent communication • Workflow orchestration • Quality assurance mechanisms

**Sample**: [Advanced Multi-Agent System](./samples/09/README.md)

**Duration**: 4-5 hours | **Level**: Expert

---

### [10: Foundry Local as Tools Framework](./samples/10/README.md)
**Focus**: Tool-first architecture for integrating Foundry Local into existing applications and frameworks

**Key Topics**: LangChain integration • Semantic Kernel functions • REST API frameworks • CLI tools • Jupyter integration • Production deployment patterns

**Sample**: [Foundry Tools Framework](./samples/10/README.md)

**Duration**: 4-5 hours | **Level**: Expert

## Prerequisites

### System Requirements
- **Operating System**: Windows 11 (22H2 or later)
- **Memory**: 16GB RAM (32GB recommended for larger models)
- **Storage**: 50GB free space for model caching
- **Hardware**: NPU-enabled device recommended (Copilot+ PC), GPU optional
- **Network**: High-speed internet for initial model downloads

### Development Environment
- Visual Studio Code with AI Toolkit extension
- Python 3.10+ and pip
- Git for version control
- PowerShell or Command Prompt
- Azure CLI (optional for cloud integration)

### Knowledge Prerequisites
- Basic understanding of AI/ML concepts
- Command line familiarity
- Python programming basics
- REST API concepts
- Basic knowledge of prompting and model inference

## Module Timeline

**Total Estimated Time**: 30-38 hours

| Session | Focus Area | Samples | Time | Complexity |
|---------|------------|---------|------|------------|
|  1 | Setup & Basics | 01, 02, 03 | 2-3 hours | Beginner |
|  2 | AI Solutions | 04 | 2-3 hours | Intermediate |
|  3 | Open Source | 05 | 2-3 hours | Intermediate |
|  4 | Advanced Models | 06 | 3-4 hours | Advanced |
|  5 | AI Agents | 05, 09 | 3-4 hours | Advanced |
|  6 | Enterprise Tools | 06, 10 | 3-4 hours | Expert |
|  7 | Direct API Integration | 07 | 2-3 hours | Intermediate |
|  8 | Windows 11 Chat App | 08 | 3-4 hours | Advanced |
|  9 | Advanced Multi-Agent | 09 | 4-5 hours | Expert |
| 10 | Tools Framework | 10 | 4-5 hours | Expert |

## Key Resources

**Official Documentation:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Source code and official samples
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Complete setup and usage guide
- [Model Mondays Series](https://aka.ms/model-mondays) - Weekly model highlights and tutorials

**Community & Support:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A and feature requests
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Latest news and best practices

## Learning Outcomes

If you finish dis module, you go sabi:

### Technical Mastery
- **Deploy and Manage**: Foundry Local installations for development and production environments
- **Integrate Models**: Work well with different model families from Microsoft, Hugging Face, and community sources
- **Build Applications**: Create production-ready AI apps with advanced features and optimizations
- **Develop Agents**: Implement smart AI agents with grounding, reasoning, and tool integration

### Strategic Understanding
- **Architecture Decisions**: Know di difference between local vs cloud deployment
- **Performance Optimization**: Make inference performance better for different hardware configurations
- **Enterprise Scaling**: Design apps wey fit scale from local prototypes to enterprise deployments
- **Privacy and Security**: Create AI solutions wey dey protect privacy with local inference

### Innovation Capabilities
- **Rapid Prototyping**: Quickly build and test AI app ideas across all 10 sample patterns
- **Community Integration**: Use open-source models and contribute to di ecosystem
- **Advanced Patterns**: Implement di latest AI patterns like RAG, agents, and tool integration
- **Framework Mastery**: Expert-level integration with LangChain, Semantic Kernel, Chainlit, and Electron
- **Production Deployment**: Deploy scalable AI solutions from local prototypes to enterprise systems
- **Future-Ready Development**: Build apps wey ready for new AI technologies and patterns

## Getting Started

1. **Environment Setup**: Make sure say you dey use Windows 11 with di recommended hardware (check Prerequisites)
2. **Install Foundry Local**: Follow Session 1 for complete installation and configuration
3. **Run Sample 01**: Start with basic REST API integration to confirm say setup dey okay
4. **Progress Through Samples**: Finish samples 01-10 to sabi everything well

## Success Metrics

Track your progress through all 10 samples:

### Foundation Level (Samples 01-03)
- [ ] Install and configure Foundry Local well
- [ ] Finish REST API integration (Sample 01)
- [ ] Add OpenAI SDK compatibility (Sample 02)
- [ ] Do model discovery and benchmarking (Sample 03)

### Application Level (Samples 04-06)
- [ ] Deploy and run at least 4 different model families
- [ ] Build one RAG chat app wey dey work (Sample 04)
- [ ] Create multi-agent orchestration system (Sample 05)
- [ ] Implement smart model routing (Sample 06)

### Advanced Integration Level (Samples 07-10)
- [ ] Build production-ready API client (Sample 07)
- [ ] Develop Windows 11 native chat app (Sample 08)
- [ ] Implement advanced multi-agent system (Sample 09)
- [ ] Create complete tools framework (Sample 10)

### Mastery Indicators
- [ ] Run all 10 samples without errors
- [ ] Customize at least 3 samples for your own use cases
- [ ] Deploy 2+ samples for production-like environments
- [ ] Add improvements or extensions to sample code
- [ ] Use Foundry Local patterns for your personal or work projects

## Quick Start Guide - All 10 Samples

### Environment Setup (Required for All Samples)

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

**Sample 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Sample 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Sample 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Sample 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Sample 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Sample 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Advanced Integration Samples (07-10)

**Sample 07: Direct API Client**
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

**Sample 08: Windows 11 Chat Application**
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

**Sample 09: Advanced Multi-Agent System**
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

**Sample 10: Foundry Tools Framework**
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

### Troubleshooting Common Issues

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

## Summary
Dis module na di latest level for edge AI development, e dey join Microsoft enterprise-level tools wit di flexibility and innovation wey dey for open-source ecosystem. If you sabi Foundry Local well well through di 10 full samples, you go dey for di front line of AI application development.

**Full Learning Path:**
- **Foundation** (Samples 01-03): API integration and model management
- **Applications** (Samples 04-06): RAG, agents, and intelligent routing 
- **Advanced** (Samples 07-10): Production frameworks and enterprise integration

For Azure OpenAI integration (Session 2), check di README files for di individual sample to see di environment variables wey you need and di API version settings.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for di native language na di main correct source. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->