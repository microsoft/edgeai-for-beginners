# Module 08: Hands-on With Microsoft Foundry Local - Complete Developer Toolkit

## Overview

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) is the next generation of edge AI development, offering developers robust tools to create, deploy, and scale AI applications locally while maintaining seamless integration with Azure AI Foundry. This module provides a comprehensive guide to Foundry Local, from installation to advanced agent development.

**Key Technologies:**
- Microsoft Foundry Local CLI and SDK
- Azure AI Foundry integration
- On-device model inference
- Local model caching and optimization
- Agent-based architectures

## Learning Objectives

By completing this module, you will:

- **Master Foundry Local**: Install, configure, and optimize for Windows 11 development.
- **Deploy Diverse Models**: Run phi, qwen, deepseek, and GPT models locally using CLI commands.
- **Build Production Solutions**: Develop AI applications with advanced prompt engineering and data integration.
- **Leverage Open-Source Ecosystem**: Integrate Hugging Face models and community contributions.
- **Develop AI Agents**: Create intelligent agents with grounding and orchestration capabilities.
- **Implement Enterprise Patterns**: Design modular, scalable AI solutions for production deployment.

## Session Structure

### [1: Getting Started with Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Installation, CLI setup, model deployment, and hardware optimization.

**Key Topics**: Complete installation • CLI commands • Model caching • Hardware acceleration • Multi-model deployment.

**Sample**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md).

**Duration**: 2-3 hours | **Level**: Beginner

---

### [2: Build AI Solutions with Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Advanced prompt engineering, data integration, and cloud connectivity.

**Key Topics**: Prompt engineering • Data integration • Azure workflows • Performance optimization • Monitoring.

**Sample**: [Chainlit RAG Application](./samples/04/README.md).

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**Focus**: Hugging Face integration, BYOM strategies, and community models.

**Key Topics**: Hugging Face integration • Bring-your-own-model • Model Mondays insights • Community contributions • Model selection.

**Sample**: [Multi-Agent Orchestration](./samples/05/README.md).

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [4: Explore Cutting-Edge Models](./04.CuttingEdgeModels.md)
**Focus**: LLMs vs SLMs, EdgeAI implementation, and advanced demos.

**Key Topics**: Model comparison • Edge vs cloud inference • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimization.

**Sample**: [Models-as-Tools Router](./samples/06/README.md).

**Duration**: 3-4 hours | **Level**: Advanced

---

### [5: Build AI-Powered Agents Fast](./05.AIPoweredAgents.md)
**Focus**: Agent architectures, system prompts, grounding, and orchestration.

**Key Topics**: Agent design patterns • System prompt engineering • Grounding techniques • Multi-agent systems • Production deployment.

**Sample**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md).

**Duration**: 3-4 hours | **Level**: Advanced

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
**Focus**: Modular AI solutions, enterprise scaling, and production patterns.

**Key Topics**: Models as tools • On-device deployment • SDK/API integration • Enterprise architectures • Scaling strategies.

**Sample**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md).

**Duration**: 3-4 hours | **Level**: Expert

---

### [7: Direct API Integration Patterns](./samples/07/README.md)
**Focus**: Pure REST API integration without SDK dependencies for maximum control.

**Key Topics**: HTTP client implementation • Custom authentication • Model health monitoring • Streaming responses • Production error handling.

**Sample**: [Direct API Client](./samples/07/README.md).

**Duration**: 2-3 hours | **Level**: Intermediate

---

### [8: Windows 11 Native Chat Application](./samples/08/README.md)
**Focus**: Building modern native chat applications with Foundry Local integration.

**Key Topics**: Electron development • Fluent Design System • Native Windows integration • Real-time streaming • Chat interface design.

**Sample**: [Windows 11 Chat Application](./samples/08/README.md).

**Duration**: 3-4 hours | **Level**: Advanced

---

### [9: Advanced Multi-Agent Orchestration](./samples/09/README.md)
**Focus**: Sophisticated agent coordination, specialized task delegation, and collaborative AI workflows.

**Key Topics**: Intelligent agent coordination • Function calling patterns • Cross-agent communication • Workflow orchestration • Quality assurance mechanisms.

**Sample**: [Advanced Multi-Agent System](./samples/09/README.md).

**Duration**: 4-5 hours | **Level**: Expert

---

### [10: Foundry Local as Tools Framework](./samples/10/README.md)
**Focus**: Tool-first architecture for integrating Foundry Local into existing applications and frameworks.

**Key Topics**: LangChain integration • Semantic Kernel functions • REST API frameworks • CLI tools • Jupyter integration • Production deployment patterns.

**Sample**: [Foundry Tools Framework](./samples/10/README.md).

**Duration**: 4-5 hours | **Level**: Expert

## Prerequisites

### System Requirements
- **Operating System**: Windows 11 (22H2 or later).
- **Memory**: 16GB RAM (32GB recommended for larger models).
- **Storage**: 50GB free space for model caching.
- **Hardware**: NPU-enabled device recommended (Copilot+ PC), GPU optional.
- **Network**: High-speed internet for initial model downloads.

### Development Environment
- Visual Studio Code with AI Toolkit extension.
- Python 3.10+ and pip.
- Git for version control.
- PowerShell or Command Prompt.
- Azure CLI (optional for cloud integration).

### Knowledge Prerequisites
- Basic understanding of AI/ML concepts.
- Command line familiarity.
- Python programming basics.
- REST API concepts.
- Basic knowledge of prompting and model inference.

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
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Source code and official samples.
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Complete setup and usage guide.
- [Model Mondays Series](https://aka.ms/model-mondays) - Weekly model highlights and tutorials.

**Community & Support:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A and feature requests.
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Latest news and best practices.

## Learning Outcomes

Upon completing this module, you will be equipped to:

### Technical Mastery
- **Deploy and Manage**: Foundry Local installations across development and production environments.
- **Integrate Models**: Seamlessly work with diverse model families from Microsoft, Hugging Face, and community sources.
- **Build Applications**: Create production-ready AI applications with advanced features and optimizations.
- **Develop Agents**: Implement sophisticated AI agents with grounding, reasoning, and tool integration.

### Strategic Understanding
- **Architecture Decisions**: Make informed choices between local vs cloud deployment.
- **Performance Optimization**: Optimize inference performance across different hardware configurations.
- **Enterprise Scaling**: Design applications that scale from local prototypes to enterprise deployments.
- **Privacy and Security**: Implement privacy-preserving AI solutions with local inference.

### Innovation Capabilities
- **Rapid Prototyping**: Quickly build and test AI application concepts across all 10 sample patterns.
- **Community Integration**: Leverage open-source models and contribute to the ecosystem.
- **Advanced Patterns**: Implement cutting-edge AI patterns including RAG, agents, and tool integration.
- **Framework Mastery**: Expert-level integration with LangChain, Semantic Kernel, Chainlit, and Electron.
- **Production Deployment**: Deploy scalable AI solutions from local prototypes to enterprise systems.
- **Future-Ready Development**: Build applications ready for emerging AI technologies and patterns.

## Getting Started

1. **Environment Setup**: Ensure Windows 11 with recommended hardware (see Prerequisites).
2. **Install Foundry Local**: Follow Session 1 for complete installation and configuration.
3. **Run Sample 01**: Start with basic REST API integration to verify setup.
4. **Progress Through Samples**: Complete samples 01-10 for comprehensive mastery.

## Success Metrics

Track your progress through all 10 comprehensive samples:

### Foundation Level (Samples 01-03)
- [ ] Successfully install and configure Foundry Local.
- [ ] Complete REST API integration (Sample 01).
- [ ] Implement OpenAI SDK compatibility (Sample 02).
- [ ] Perform model discovery and benchmarking (Sample 03).

### Application Level (Samples 04-06)
- [ ] Deploy and run at least 4 different model families.
- [ ] Build a functional RAG chat application (Sample 04).
- [ ] Create multi-agent orchestration system (Sample 05).
- [ ] Implement intelligent model routing (Sample 06).

### Advanced Integration Level (Samples 07-10)
- [ ] Build production-ready API client (Sample 07).
- [ ] Develop Windows 11 native chat application (Sample 08).
- [ ] Implement advanced multi-agent system (Sample 09).
- [ ] Create comprehensive tools framework (Sample 10).

### Mastery Indicators
- [ ] Successfully run all 10 samples without errors.
- [ ] Customize at least 3 samples for specific use cases.
- [ ] Deploy 2+ samples in production-like environments.
- [ ] Contribute improvements or extensions to sample code.
- [ ] Integrate Foundry Local patterns into personal/professional projects.

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
This module represents the latest advancements in edge AI development, merging Microsoft's enterprise-grade tools with the adaptability and creativity of the open-source ecosystem. By mastering Foundry Local through all 10 detailed samples, you'll be at the forefront of AI application development.

**Complete Learning Path:**
- **Foundation** (Samples 01-03): API integration and model management
- **Applications** (Samples 04-06): RAG, agents, and intelligent routing
- **Advanced** (Samples 07-10): Production frameworks and enterprise integration

For Azure OpenAI integration (Session 2), refer to the README files of each sample for details on required environment variables and API version configurations.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.